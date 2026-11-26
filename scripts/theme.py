"""ThunderStudy Clay UI (design_ai tokens): light = blue, dark = purple."""
from xml.sax.saxutils import escape as esc

FONT = "Inter, 'Segoe UI', Helvetica, Arial, sans-serif"

T = {
 "light": dict(canvas="#EEF3FF", deep="#E1EAFB", surface="#F8FAFF", ink="#26324A", body="#4F5D75", muted="#6B6485",
               primary="#70A1FC", active="#5D79B3", soft="#DCE8FF",
               sh_dark="#6E8CC8", sh_dark_o=".45", sh_light="#FFFFFF", sh_light_o=".9", shine=".55",
               tint=["#D9CCFF", "#C7DDFF", "#BDEBFF", "#C6F0D3", "#FFD9B8", "#FFCFE6"],
               bars=["#3E2A9E", "#1F4FA3", "#1B6B3A", "#A34A0B", "#9E2A68"],
               green=("#C6F0D3", "#1B6B3A"), red=("#FFCFCF", "#A12626"), yellow=("#FFF0A8", "#7A5C00")),
 "dark":  dict(canvas="#0F1F1E", deep="#0B1717", surface="#152827", ink="#E8FAF8", body="#B7D6D3", muted="#7FA3A0",
               primary="#5EEAD4", active="#99F6E4", soft="#1D5A56",
               sh_dark="#000000", sh_dark_o=".55", sh_light="#FFFFFF", sh_light_o=".05", shine=".10",
               tint=["#1D5A56", "#26427A", "#1C5670", "#1F5A36", "#7A4220", "#7A2F58"],
               bars=["#CCF6F1", "#D6E6FF", "#D3F6DF", "#FFE2CB", "#FFDAEE"],
               green=("#1F5A36", "#D3F6DF"), red=("#7A2A2A", "#FFDADA"), yellow=("#6B5A1A", "#FFF2B8")),
}

ICONS = {
 "star": "M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z",
 "commit": "M3 12h6 M15 12h6 M9 12a3 3 0 1 0 6 0a3 3 0 1 0-6 0",
 "repo": "M4 4h13a3 3 0 0 1 3 3v13H7a3 3 0 0 1-3-3z M4 17a3 3 0 0 1 3-3h13",
 "users": "M16 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6z M8 12a3 3 0 1 0 0-6 3 3 0 0 0 0 6z M2 20c0-3 3-5 6-5s6 2 6 5 M14 15c3 0 8 1 8 5",
 "pr": "M18 21a3 3 0 1 0 0-6 3 3 0 0 0 0 6z M6 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6z M13 6h3a2 2 0 0 1 2 2v7 M6 9v12",
 "fork": "M4 6a2 2 0 1 0 4 0a2 2 0 1 0-4 0 M16 6a2 2 0 1 0 4 0a2 2 0 1 0-4 0 M10 20a2 2 0 1 0 4 0a2 2 0 1 0-4 0 M6 8v1a3 3 0 0 0 3 3h6a3 3 0 0 0 3-3V8 M12 12v6",
}

def clay(id_, c, d=7, b=9):
    return (f'<filter id="{id_}" x="-20%" y="-20%" width="140%" height="150%">'
            f'<feDropShadow dx="{d}" dy="{d}" stdDeviation="{b/2}" flood-color="{c["sh_dark"]}" flood-opacity="{c["sh_dark_o"]}"/>'
            f'<feDropShadow dx="-{d}" dy="-{d}" stdDeviation="{b/2}" flood-color="{c["sh_light"]}" flood-opacity="{c["sh_light_o"]}"/></filter>')

def shine_defs(c):
    return (f'<linearGradient id="shine" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/>'
            f'<stop offset=".5" stop-color="#fff" stop-opacity="{c["shine"]}"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>')

def shell(c, x, y, w, h, clip_id="cc", dur=7):
    """Clay card with a shine sweep. Returns (defs, body)."""
    defs = f'<clipPath id="{clip_id}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="28"/></clipPath>'
    body = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="28" fill="{c["surface"]}" filter="url(#clay)"/>'
            f'<g clip-path="url(#{clip_id})"><rect x="-140" y="{y}" width="100" height="{h}" fill="url(#shine)" transform="skewX(-18)">'
            f'<animate attributeName="x" values="-140;{w+260};{w+260}" keyTimes="0;.35;1" dur="{dur}s" repeatCount="indefinite"/></rect></g>')
    return defs, body

def rise(delay, inner, dy=12):
    return (f'<g><animateTransform attributeName="transform" type="translate" from="0 {dy}" to="0 0" dur=".7s" begin="{delay}s" fill="freeze" '
            f'calcMode="spline" keySplines=".2 .8 .2 1" keyTimes="0;1"/><animate attributeName="opacity" from="0" to="1" dur=".7s" begin="{delay}s" fill="freeze"/>{inner}</g>')
