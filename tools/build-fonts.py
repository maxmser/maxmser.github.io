#!/usr/bin/env python3
"""Builds the web fonts in static/fonts/ from the full fonts in tools/fonts-src/.

Settings (characters, features, weight range) come from data/font.toml:
the top level for Inter, the table [serif] for Crimson Pro.
Steps per file: limit the weight axis (and fix Inter's optical size), keep only the
characters and features from the settings, write WOFF2 with Brotli at its highest
quality (the fontTools default) and the optional hmtx transform.

Sources:
- Inter: built from the Inter source code, commit 353b61b
  (see DECISIONS.md, "Schrift: Inter mit a mit Schweif").
- Crimson Pro 1.003 from google/fonts, commit 5c70a79 (see DECISIONS.md, "Lauftext in Crimson Pro").

Usage: python3 tools/build-fonts.py   (needs fontTools and brotli)
"""
import io
import pathlib
import sys
import tomllib

from fontTools import subset
from fontTools.ttLib import TTFont, woff2
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "fonts-src"
OUT = ROOT / "static" / "fonts"


def unicodes(entries):
    result = []
    for e in entries:
        a, _, b = e.partition("-")
        result.extend(range(int(a, 16), int(b or a, 16) + 1))
    return result


def build(src, out, cfg):
    font = TTFont(src)
    modified = font["head"].modified  # every save stamps the current time; restore the source's date below
    missing = [f"U+{c:04X}" for c in unicodes(cfg["unicodes"]) if c not in font.getBestCmap()]
    if missing:
        sys.exit(f"{src.relative_to(ROOT)} lacks {' '.join(missing)}: remove them from data/font.toml")

    if "fvar" in font:  # variable fonts: limit the axes; static fonts stay as they are
        limits = {"wght": (cfg["weight_min"], cfg["weight_max"])}
        if "optical_size" in cfg:
            limits["opsz"] = cfg["optical_size"]
        font = instantiateVariableFont(font, limits)
    if "vertical_metrics" in cfg:
        # The same vertical metrics in every table and every style, no line gaps,
        # so all browsers place the baseline alike and no style makes a line taller.
        upm = font["head"].unitsPerEm
        asc, desc = (round(v * upm) for v in cfg["vertical_metrics"])
        hhea, os2 = font["hhea"], font["OS/2"]
        hhea.ascent, hhea.descent = os2.sTypoAscender, os2.sTypoDescender = asc, desc
        os2.sTypoLineGap = hhea.lineGap = 0
        os2.usWinAscent, os2.usWinDescent = asc, -desc
    # Save and reload once: the subsetter needs the fully compiled variation tables.
    buf = io.BytesIO()
    font.save(buf)
    buf.seek(0)
    font = TTFont(buf)

    opts = subset.Options()
    opts.layout_features = opts.layout_features + cfg["features"]  # default set plus ours
    opts.name_IDs = ["*"]
    opts.name_languages = ["*"]
    opts.notdef_outline = True
    sub = subset.Subsetter(opts)
    sub.populate(unicodes=unicodes(cfg["unicodes"]))
    sub.subset(font)

    if "rename" in cfg:
        # A new family name in every name record that names the font (OFL: a Modified
        # Version must not use the Reserved Font Names). Copyright and license stay.
        style = font["name"].getDebugName(2) or "Regular"
        new = {1: cfg["rename"], 3: f"{cfg['rename']} {style}; web subset", 4: f"{cfg['rename']} {style}",
               6: f"{cfg['rename']}-{style}".replace(" ", ""), 16: cfg["rename"], 17: style}
        for rec in list(font["name"].names):
            # 7 trademark and 8 manufacturer name the original too; copyright (0) and
            # license (13, 14) stay, as the OFL requires.
            if rec.nameID in (1, 3, 4, 6, 7, 8, 16, 17, 18, 21, 22, 25):
                font["name"].removeNames(nameID=rec.nameID)
        for nid, text in new.items():
            font["name"].setName(text, nid, 3, 1, 0x409)
        font["name"].setName(cfg["rename"], 1, 1, 0, 0)

    sfnt = io.BytesIO()
    font.flavor = None
    font["head"].modified = modified
    font.recalcTimestamp = False  # same input, same file
    font.save(sfnt)
    sfnt.seek(0)
    with open(out, "wb") as f:
        # The hmtx transform needs TrueType outlines (glyf); CFF fonts get the default.
        woff2.compress(sfnt, f, transform_tables=["glyf", "loca", "hmtx"] if "glyf" in font else None)

    check = TTFont(out)
    tags = sorted({r.FeatureTag for r in check["GSUB"].table.FeatureList.FeatureRecord})
    axes = [(a.axisTag, a.minValue, a.maxValue) for a in check["fvar"].axes] if "fvar" in check else "static"
    print(f"{out.relative_to(ROOT)}: {out.stat().st_size} bytes, {len(check.getBestCmap())} characters, axes {axes}")
    print(f"  features: {' '.join(tags)}")


def main():
    cfg = tomllib.loads((ROOT / "data" / "font.toml").read_text())
    serif = cfg.pop("serif")
    jobs = [
        (SRC / "InterVariable.woff2", OUT / "inter" / "InterVariable.woff2", cfg),
        (SRC / "InterVariable-Italic.woff2", OUT / "inter" / "InterVariable-Italic.woff2", cfg),
        (SRC / "crimson" / "CrimsonPro.woff2", OUT / "crimson" / "CrimsonPro.woff2", serif),
        (SRC / "crimson" / "CrimsonPro-Italic.woff2", OUT / "crimson" / "CrimsonPro-Italic.woff2", serif),
    ]
    for src, out, settings in jobs:
        build(src, out, settings)


if __name__ == "__main__":
    main()
