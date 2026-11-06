#!/usr/bin/env python3
"""Builds the Inter specimen page design/schriftmuster/index.html.

Shows every named variant (cv01 to cv16, ss01 to ss08) and a few useful
OpenType features, each with the affected characters side by side, and
every character of the font, marked by whether it is in the live font
subset and in the proposed English and German subset.

The page is standalone: the font is embedded as base64, so it opens by
double click in any browser. It is not part of the published site.

Usage: python3 design/schriftmuster/build.py  (needs fontTools)
"""
import base64
import tomllib
import html
import pathlib
import unicodedata

from fontTools.ttLib import TTFont

HERE = pathlib.Path(__file__).parent
FONT = HERE.parent.parent / "tools" / "fonts-src" / "InterVariable.woff2"  # full build from source, commit 353b61b

# Character sets, as unicode ranges (start, end inclusive).
CFG = tomllib.loads((HERE.parent.parent / "data" / "font.toml").read_text())
LIVE = []
for _e in CFG["unicodes"]:
    _a, _, _b = _e.partition("-")
    LIVE.append((int(_a, 16), int(_b or _a, 16)))
ENDE = LIVE  # the live set is the English and German set since 2026-11-06

BLOCKS = [
    (0x0000, 0x007F, "Grundlatein"), (0x0080, 0x00FF, "Latin-1 (Westeuropa)"),
    (0x0100, 0x017F, "Latein erweitert A (Mittel- und Osteuropa)"), (0x0180, 0x024F, "Latein erweitert B"),
    (0x0250, 0x02FF, "Lautschrift und Modifikatoren"), (0x0300, 0x036F, "Kombinierende Akzente"),
    (0x0370, 0x03FF, "Griechisch"), (0x0400, 0x052F, "Kyrillisch"), (0x1E00, 0x1EFF, "Latein erweitert (Vietnamesisch u. a.)"),
    (0x2000, 0x206F, "Satzzeichen"), (0x2070, 0x209F, "Hoch- und Tiefstellung"), (0x20A0, 0x20CF, "Währungen"),
    (0x2100, 0x214F, "Buchstabenähnliche Symbole"), (0x2150, 0x218F, "Zahlformen"), (0x2190, 0x21FF, "Pfeile"),
    (0x2200, 0x22FF, "Mathematik"), (0x2300, 0x23FF, "Technische Zeichen"), (0x2460, 0x24FF, "Umkreiste Zeichen"),
    (0x2500, 0x25FF, "Rahmen und Formen"), (0x2600, 0x27BF, "Symbole"), (0x0000, 0x10FFFF, "Sonstige"),
]

# Features worth showing besides the named variants, with a sample text.
EXTRA = {
    "tnum": ("Tabellenziffern (gleich breit)", "1111 0000 2026 47,11"),
    "zero": ("Null mit Strich", "0 10 100 2000"),
    "case": ("Großbuchstaben-Formen (Satzzeichen höher)", "(HALLO) [A-Z] {B} — ¿Q? «M» H-V H:V"),
    "frac": ("Brüche", "1/2 3/4 7/8 12/25"),
    "sups": ("Hochgestellt", "H2O m2 x10"),
    "ordn": ("Ordinalzahlen", "1a 2o No"),
    "dlig": ("Freie Ligaturen", "-> <- => != <= >= ->> www"),
    "calt": ("Kontextabhängige Formen (ist an)", "1x2 -> 3:30 10 × 20"),
}

FONT_INFO = TTFont(FONT)
CMAP = FONT_INFO.getBestCmap()
REV = {}
for cp, g in sorted(CMAP.items()):
    REV.setdefault(g, cp)


def in_set(cp, ranges):
    return any(a <= cp <= b for a, b in ranges)


def feature_inputs(tag):
    """Characters whose glyphs a feature substitutes (approximate, single level)."""
    gsub = FONT_INFO["GSUB"].table
    lookups = gsub.LookupList.Lookup
    idx = set()
    for fr in gsub.FeatureList.FeatureRecord:
        if fr.FeatureTag == tag:
            idx.update(fr.Feature.LookupListIndex)
    seen, todo, glyphs = set(), list(idx), set()
    while todo:
        i = todo.pop()
        if i in seen:
            continue
        seen.add(i)
        for st in lookups[i].SubTable:
            if lookups[i].LookupType == 7:
                st = st.ExtSubTable
            for attr in ("mapping", "alternates"):
                m = getattr(st, attr, None)
                if m:
                    glyphs.update(m.keys())
            if getattr(st, "ligatures", None):
                glyphs.update(st.ligatures.keys())
            for rec in getattr(st, "SubstLookupRecord", None) or []:
                todo.append(rec.LookupListIndex)
            for rs in (getattr(st, "ChainSubRuleSet", None) or []):
                for r in (rs.ChainSubRule if rs else []):
                    todo.extend(x.LookupListIndex for x in r.SubstLookupRecord)
    chars = sorted({REV[g] for g in glyphs if g in REV})
    return [c for c in chars if c >= 0x20]


def feature_names():
    names = {}
    name = FONT_INFO["name"]
    for fr in FONT_INFO["GSUB"].table.FeatureList.FeatureRecord:
        p = fr.Feature.FeatureParams
        nid = p and (getattr(p, "UINameID", None) or getattr(p, "FeatUILabelNameID", None))
        if nid:
            names[fr.FeatureTag] = name.getDebugName(nid)
    return names


def esc(cp):
    return html.escape(chr(cp))


def variant_section(tag, label, chars, sample=None, note=""):
    cells = "".join(f'<span title="U+{cp:04X}">{esc(cp)}</span>' for cp in chars[:120])
    more = f'<p class="more">und {len(chars) - 120} weitere Zeichen</p>' if len(chars) > 120 else ""
    body = cells if cells else html.escape(sample or "")
    sample_html = f'<p class="sample">{html.escape(sample)}</p>' if sample and cells else ""
    return f"""
<section class="feat{' wish' if note else ''}" id="{tag}">
  <h3><code>{tag}</code> {html.escape(label)}{f' <em>{note}</em>' if note else ''}</h3>
  <div class="pair">
    <div><p class="lbl">Standard</p><p class="glyphs" style="font-feature-settings:'{tag}' 0">{body}</p>{sample_html.replace('class="sample"', f'class="sample" style="font-feature-settings:&#39;{tag}&#39; 0"')}</div>
    <div><p class="lbl">Mit {tag}</p><p class="glyphs" style="font-feature-settings:'{tag}' 1">{body}</p>{sample_html.replace('class="sample"', f'class="sample" style="font-feature-settings:&#39;{tag}&#39; 1"')}</div>
  </div>{more}
</section>"""


def main():
    names = feature_names()
    named = sorted(t for t in names if t[:2] in ("cv", "ss"))
    notes = {t: "auf der Seite aktiv" for t in CFG["features"] if t[:2] in ("cv", "ss")}
    sample = "Product leader who builds things to understand them. Ill 1lI 0O 6 9 4 3 G ß ẞ ffi Rundfunk 2026"
    feats = "".join(variant_section(t, names[t], feature_inputs(t), sample, notes.get(t, "")) for t in named)
    extras = "".join(variant_section(t, label, [], s) for t, (label, s) in EXTRA.items())

    # Glyph grid by block.
    groups = {}
    for cp in sorted(CMAP):
        if cp < 0x20 or unicodedata.category(chr(cp)) in ("Cc", "Cf", "Zl", "Zp"):
            continue
        for a, b, label in BLOCKS:
            if a <= cp <= b:
                groups.setdefault(label, []).append(cp)
                break
    total = sum(len(v) for v in groups.values())
    grid = ""
    for _, _, label in BLOCKS:
        cps = groups.get(label)
        if not cps:
            continue
        cells = "".join(
            f'<span class="{"live " if in_set(cp, LIVE) else ""}{"ende" if in_set(cp, ENDE) else ""}" '
            f'title="U+{cp:04X} {html.escape(unicodedata.name(chr(cp), ""))}">{esc(cp)}</span>'
            for cp in cps)
        live = sum(in_set(cp, LIVE) for cp in cps)
        ende = sum(in_set(cp, ENDE) for cp in cps)
        grid += f'<h3>{label} <small>{len(cps)} Zeichen, davon {ende} auf der Seite</small></h3><div class="grid">{cells}</div>'

    b64 = base64.b64encode(FONT.read_bytes()).decode()
    page = f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Inter: Varianten und Zeichen</title>
<style>
@font-face{{font-family:"InterSpecimen";font-weight:100 900;src:url(data:font/woff2;base64,{b64}) format("woff2")}}
:root{{--w:400;--o:14}}
body:has(#w500:checked){{--w:500}} body:has(#o32:checked){{--o:32}}
html{{font-family:"InterSpecimen",system-ui,sans-serif;font-size:1.125rem;line-height:1.5;color:#000;background:#fff}}
body{{margin:0 auto;max-width:96rem;padding:2rem 5vw 4rem}}
*{{font-variation-settings:"wght" var(--w),"opsz" var(--o)}}
h1{{font-size:2.5rem;line-height:1.2;margin:0 0 .5rem}} h2{{margin:3rem 0 1rem;padding-top:.5rem;border-top:1px solid #000}}
h3{{font-size:1rem;margin:1.5rem 0 .5rem}} h3 small{{color:#6b6b6b;font-weight:400}} h3 em{{font-style:normal;background:#ffe500;padding:0 .3em}}
code{{font-family:ui-monospace,Menlo,monospace;font-size:.85em}}
.controls{{position:sticky;top:0;background:#fff;padding:.5rem 0;border-bottom:1px solid #c8c8c8;z-index:1}}
.controls label{{margin-right:1rem}}
.pair{{display:grid;grid-template-columns:1fr 1fr;gap:2rem}}
.lbl{{font-size:.8rem;color:#6b6b6b;margin:0}} .glyphs{{font-size:2.5rem;line-height:1.3;margin:0;word-break:break-all}}
.glyphs span{{display:inline-block;min-width:1.2em;text-align:center}}
.sample{{font-size:1.25rem;margin:.25rem 0 0}} .more{{color:#6b6b6b;font-size:.8rem}}
.feat{{padding-bottom:1rem;border-bottom:1px solid #eee}} .wish{{background:#fffbe0}}
.grid{{display:flex;flex-wrap:wrap;gap:2px;font-size:1.6rem}}
.grid span{{width:2.2em;height:2.2em;display:grid;place-items:center;outline:1px solid #eee;opacity:.35}}
.grid span.live{{opacity:1}} .grid span.ende{{background:#e6f2ff;opacity:1}}
.legend span{{display:inline-block;padding:0 .5em;margin-right:.5em;outline:1px solid #eee}}
</style></head>
<body>
<h1>Inter: Varianten und Zeichen</h1>
<p>Vollständige Schrift aus dem Quellcode (Commit 353b61b), {total} Zeichen. Gelb markiert: auf der Seite aktiv. Fahre mit der Maus über ein Zeichen für seinen Unicode-Namen.</p>
<div class="controls">
  <strong>Stärke</strong> <label><input type="radio" name="w" id="w400" checked> 400</label><label><input type="radio" name="w" id="w500"> 500</label>
  <strong>Optische Größe</strong> <label><input type="radio" name="o" id="o14" checked> 14 Text</label><label><input type="radio" name="o" id="o32"> 32 Display</label>
</div>
<h2>Benannte Varianten</h2>
{feats}
<h2>Weitere Funktionen</h2>
{extras}
<h2>Alle Zeichen</h2>
<p class="legend"><span style="opacity:.35">blass</span> nicht in der Schrift der Seite <span style="background:#e6f2ff">blau</span> in der Schrift der Seite (data/font.toml)</p>
{grid}
</body></html>"""
    out = HERE / "index.html"
    out.write_text(page)
    print(f"{out} geschrieben: {len(named)} Varianten, {total} Zeichen, {out.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
