"""Checks the main sites and writes a live status board (light and dark SVG)."""
import os, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone
from theme import T, FONT, esc, clay, shine_defs, shell, rise

SITES = [
    ("ThunderStudy", "https://thunderstudy.indevs.in", "thunderstudy.indevs.in"),
    ("ThunderTest", "https://thundertest.indevs.in", "thundertest.indevs.in"),
    ("ThunderStudy AI", "https://ai.thunderstudy.indevs.in", "ai.thunderstudy.indevs.in"),
    ("Project Hub", "https://project.wondermayank.in", "project.wondermayank.in"),
    ("Wondermayank", "https://wondermayank.in", "wondermayank.in"),
    ("Study Blog", "https://blog.thunderstudy.indevs.in", "blog.thunderstudy.indevs.in"),
]
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "auto")
DEMO = os.environ.get("DEMO") == "1"

def check(url):
    if DEMO:
        return None, None
    t0 = time.time()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (profile-status-board)"})
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status < 400, int((time.time() - t0) * 1000)
    except urllib.error.HTTPError as e:
        return e.code < 400, int((time.time() - t0) * 1000)
    except Exception:
        return False, None

def svg(mode, results):
    c = T[mode]
    W, H = 860, 410
    defs, body = shell(c, 16, 12, 828, 378, "cst", 9)
    up = sum(1 for r in results if r[2] is True)
    known = any(r[2] is not None for r in results)
    sg, sink = (c["green"] if up == len(results) else c["red"]) if known else c["yellow"]
    summary = f"{up} of {len(results)} online" if known else "Waiting for first check"
    pw = 190
    out = (f'<text x="44" y="60" font-family="{FONT}" font-size="26" font-weight="700" fill="{c["ink"]}">Live <tspan fill="{c["primary"]}">Status</tspan></text>'
           f'<rect x="{816-pw}" y="36" width="{pw}" height="34" rx="17" fill="{sg}"/>'
           f'<text x="{816-pw/2}" y="58" text-anchor="middle" font-family="{FONT}" font-size="14" font-weight="600" fill="{sink}">{esc(summary)}</text>')
    for i, (name, url, state, ms, dom) in enumerate([(a, b, ok, m, d) for (a, b, ok, m, d) in results]):
        col, row = i % 2, i // 2
        x, y = 44 + col * 396, 94 + row * 90
        if state is True:
            fg, fi, label = c["green"][0], c["green"][1], "Online"
        elif state is False:
            fg, fi, label = c["red"][0], c["red"][1], "Down"
        else:
            fg, fi, label = c["yellow"][0], c["yellow"][1], "Pending"
        pulse = (f'<circle cx="{x+30}" cy="{y+39}" r="7" fill="{fi}"><animate attributeName="r" values="7;10;7" dur="2.4s" repeatCount="indefinite"/>'
                 f'<animate attributeName="opacity" values="1;.45;1" dur="2.4s" repeatCount="indefinite"/></circle>' if state is True else
                 f'<circle cx="{x+30}" cy="{y+39}" r="7" fill="{fi}"/>')
        ms_txt = f"{ms} ms" if ms is not None else "-"
        inner = (f'<rect x="{x}" y="{y}" width="380" height="78" rx="22" fill="{c["deep"]}"/>{pulse}'
                 f'<text x="{x+54}" y="{y+36}" font-family="{FONT}" font-size="18" font-weight="700" fill="{c["ink"]}">{esc(name)}</text>'
                 f'<text x="{x+54}" y="{y+57}" font-family="{FONT}" font-size="13" fill="{c["muted"]}">{esc(dom)}</text>'
                 f'<rect x="{x+282}" y="{y+14}" width="80" height="28" rx="14" fill="{fg}"/>'
                 f'<text x="{x+322}" y="{y+33}" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="600" fill="{fi}">{label}</text>'
                 f'<text x="{x+322}" y="{y+62}" text-anchor="middle" font-family="{FONT}" font-size="12.5" fill="{c["body"]}">{ms_txt}</text>')
        out += rise(0.15 + i * 0.1, inner)
    stamp = "Checked " + datetime.now(timezone.utc).strftime("%d %b %Y, %H:%M UTC") + "  |  refreshes every 3 hours" if known else "Runs automatically every 3 hours"
    out += f'<text x="44" y="374" font-family="{FONT}" font-size="12.5" fill="{c["muted"]}">{esc(stamp)}</text>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Live status of the main sites">'
            f'<defs>{clay("clay", c)}{shine_defs(c)}{defs}</defs>{body}{out}</svg>')

def main():
    results = []
    for name, url, dom in SITES:
        ok, ms = check(url)
        if ok is False:               # one retry before calling a site down
            time.sleep(3)
            ok, ms = check(url)
        results.append((name, url, ok, ms, dom))
        print(name, ok, ms)
    os.makedirs(OUT, exist_ok=True)
    for m in ("light", "dark"):
        open(os.path.join(OUT, f"status-{m}.svg"), "w").write(svg(m, results))
    return 0

if __name__ == "__main__":
    sys.exit(main())
