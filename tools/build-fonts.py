#!/usr/bin/env python3
"""Builds the web fonts in static/fonts/inter/ from the full fonts in tools/fonts-src/.

Settings (characters, features, weight range) come from data/font.toml.
Steps per file: limit the weight axis, keep only the characters and features
from the settings, write WOFF2 with Brotli at its highest quality (the fontTools
default) and the optional hmtx transform.

The sources are the fonts built from the Inter source code, commit 353b61b
(see DECISIONS.md, "Schrift: Inter mit a mit Schweif").

Usage: python3 tools/build-fonts.py   (needs fontTools and brotli)
"""
import io
import pathlib
import tomllib

from fontTools import subset
from fontTools.ttLib import TTFont, woff2
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "tools" / "fonts-src"
OUT = ROOT / "static" / "fonts" / "inter"
FILES = ["InterVariable.woff2", "InterVariable-Italic.woff2"]


def unicodes(entries):
    result = []
    for e in entries:
        a, _, b = e.partition("-")
        result.extend(range(int(a, 16), int(b or a, 16) + 1))
    return result


def main():
    cfg = tomllib.loads((ROOT / "data" / "font.toml").read_text())
    for name in FILES:
        font = TTFont(SRC / name)
        font = instantiateVariableFont(font, {"wght": (cfg["weight_min"], cfg["weight_max"])})
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

        sfnt = io.BytesIO()
        font.flavor = None
        font.save(sfnt)
        sfnt.seek(0)
        out = OUT / name
        with open(out, "wb") as f:
            woff2.compress(sfnt, f, transform_tables=["glyf", "loca", "hmtx"])

        check = TTFont(out)
        tags = sorted({r.FeatureTag for r in check["GSUB"].table.FeatureList.FeatureRecord})
        axes = [(a.axisTag, a.minValue, a.maxValue) for a in check["fvar"].axes]
        print(f"{out.relative_to(ROOT)}: {out.stat().st_size} bytes, {len(check.getBestCmap())} characters, axes {axes}")
        print(f"  features: {' '.join(tags)}")


if __name__ == "__main__":
    main()
