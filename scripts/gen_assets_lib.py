"""Small shared SVG helper."""
from theme import ICONS
ICONS.setdefault("repo", ICONS["repo"])

def icon(c, name, cx, cy, r=26, tint=None, sc=1.0):
    s = r / 26 * sc
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{tint}"/>'
            f'<g transform="translate({cx-12*s} {cy-12*s}) scale({s})" fill="none" stroke="{c["active"]}" stroke-width="{2/s:.2f}" stroke-linecap="round" stroke-linejoin="round"><path d="{ICONS[name]}"/></g>')
