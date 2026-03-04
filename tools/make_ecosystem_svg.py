from pathlib import Path

def svg():
    w, h = 1100, 520

    # Style: minimal, architectural
    box_fill = "#0b1220"
    box_stroke = "#6b7280"
    text = "#e5e7eb"
    muted = "#94a3b8"
    arrow = "#9ca3af"

    def rect(x, y, rw, rh, label, sub=None):
        s = []
        s.append(f'<rect x="{x}" y="{y}" width="{rw}" height="{rh}" rx="16" ry="16" fill="{box_fill}" stroke="{box_stroke}" stroke-width="2"/>')
        s.append(f'<text x="{x+rw/2}" y="{y+34}" text-anchor="middle" font-family="ui-sans-serif,system-ui,Segoe UI,Arial" font-size="20" fill="{text}">{label}</text>')
        if sub:
            s.append(f'<text x="{x+rw/2}" y="{y+62}" text-anchor="middle" font-family="ui-sans-serif,system-ui,Segoe UI,Arial" font-size="14" fill="{muted}">{sub}</text>')
        return "\n".join(s)

    def line(x1, y1, x2, y2):
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{arrow}" stroke-width="2" marker-end="url(#arrow)"/>'

    # Layout
    core = dict(x=420, y=40,  w=260, h=92)
    kg   = dict(x=90,  y=210, w=260, h=92)
    tr   = dict(x=420, y=210, w=260, h=92)
    eb   = dict(x=750, y=210, w=260, h=92)
    civ  = dict(x=420, y=380, w=260, h=92)

    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">')
    parts.append('<defs>')
    parts.append('<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">')
    parts.append('<path d="M 0 0 L 10 5 L 0 10 z" fill="#9ca3af"/>')
    parts.append('</marker>')
    parts.append('</defs>')

    # Background
    parts.append(f'<rect x="0" y="0" width="{w}" height="{h}" fill="#0a0f1a"/>')

    # Boxes
    parts.append(rect(core["x"], core["y"], core["w"], core["h"], "MoCKA Core", "Research gate and execution core"))
    parts.append(rect(kg["x"],   kg["y"],   kg["w"],   kg["h"],   "Knowledge Gate", "Institutional memory layer"))
    parts.append(rect(tr["x"],   tr["y"],   tr["w"],   tr["h"],   "Transparency", "Audit and public proof"))
    parts.append(rect(eb["x"],   eb["y"],   eb["w"],   eb["h"],   "External Brain", "External knowledge layer"))
    parts.append(rect(civ["x"],  civ["y"],  civ["w"],  civ["h"],  "Civilization", "Governance philosophy layer"))

    # Lines (Core -> three)
    core_cx = core["x"] + core["w"]/2
    core_by = core["y"] + core["h"]
    parts.append(line(core_cx, core_by, kg["x"] + kg["w"]/2, kg["y"]))
    parts.append(line(core_cx, core_by, tr["x"] + tr["w"]/2, tr["y"]))
    parts.append(line(core_cx, core_by, eb["x"] + eb["w"]/2, eb["y"]))

    # Knowledge Gate -> Civilization
    parts.append(line(kg["x"] + kg["w"]/2, kg["y"] + kg["h"], civ["x"] + civ["w"]/2, civ["y"]))

    # Title
    parts.append(f'<text x="{w/2}" y="18" text-anchor="middle" font-family="ui-sans-serif,system-ui,Segoe UI,Arial" font-size="14" fill="#94a3b8">MoCKA Ecosystem Architecture</text>')

    parts.append('</svg>')
    return "\n".join(parts)

def main():
    out = Path(__file__).resolve().parent.parent / "docs" / "ecosystem.svg"
    out.write_text(svg(), encoding="utf-8")
    print(f"OK: wrote {out}")

if __name__ == "__main__":
    main()
