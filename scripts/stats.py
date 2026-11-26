"""Builds self-hosted GitHub stats + top-languages cards (light and dark SVG, no external service)."""
import os, sys, json, urllib.request, urllib.parse
from theme import T, FONT, ICONS, esc, clay, shine_defs, shell, rise

USER = os.environ.get("GH_USER", "wondermayank")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
DEMO = os.environ.get("DEMO") == "1"
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "auto")

def api(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "profile-stats"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def fetch():
    user = api(f"https://api.github.com/users/{USER}")
    repos, page = [], 1
    while True:
        chunk = api(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner&page={page}")
        repos += chunk
        if len(chunk) < 100:
            break
        page += 1
    own = [r for r in repos if not r["fork"]]
    commits = api(f"https://api.github.com/search/commits?q=author:{USER}&per_page=1")["total_count"]
    prs = api(f"https://api.github.com/search/issues?q=author:{USER}+type:pr&per_page=1")["total_count"]
    langs = {}
    for r in own:
        try:
            for k, v in api(r["languages_url"]).items():
                langs[k] = langs.get(k, 0) + v
        except Exception:
            pass
    return dict(stars=sum(r["stargazers_count"] for r in own), forks=sum(r["forks_count"] for r in own),
                repos=len(own), followers=user["followers"], commits=commits, prs=prs, langs=langs)

def fmt(n):
    if isinstance(n, str):
        return n
    return f"{n/1000:.1f}k".replace(".0k", "k") if n >= 10000 else f"{n:,}"

def stats_svg(mode, d):
    c = T[mode]
    W, H = 420, 330
    defs, body = shell(c, 16, 12, 388, 300, "cs", 7)
    tiles = [("star", "Stars", d["stars"]), ("commit", "Commits", d["commits"]), ("repo", "Repositories", d["repos"]),
             ("users", "Followers", d["followers"]), ("pr", "Pull requests", d["prs"]), ("fork", "Forks", d["forks"])]
    out = f'<text x="40" y="56" font-family="{FONT}" font-size="24" font-weight="700" fill="{c["ink"]}">GitHub <tspan fill="{c["primary"]}">Stats</tspan></text>'
    for i, (ic, label, val) in enumerate(tiles):
        col, row = i % 2, i // 2
        x, y = 40 + col * 174, 78 + row * 74
        cx, cy = x + 32, y + 31
        inner = (f'<rect x="{x}" y="{y}" width="162" height="62" rx="20" fill="{c["deep"]}"/>'
                 f'<circle cx="{cx}" cy="{cy}" r="19" fill="{c["tint"][i % len(c["tint"])]}"/>'
                 f'<g transform="translate({cx-9.6} {cy-9.6}) scale(.8)" fill="none" stroke="{c["active"]}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="{ICONS[ic]}"/></g>'
                 f'<text x="{x+62}" y="{y+30}" font-family="{FONT}" font-size="21" font-weight="700" fill="{c["ink"]}">{esc(fmt(val))}</text>'
                 f'<text x="{x+62}" y="{y+49}" font-family="{FONT}" font-size="12.5" fill="{c["muted"]}">{esc(label)}</text>')
        out += rise(0.15 + i * 0.1, inner)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="GitHub stats for {USER}">'
            f'<defs>{clay("clay", c)}{shine_defs(c)}{defs}</defs>{body}{out}</svg>')

def langs_svg(mode, d):
    c = T[mode]
    W, H = 420, 330
    defs, body = shell(c, 16, 12, 388, 300, "cl", 8)
    out = f'<text x="40" y="56" font-family="{FONT}" font-size="24" font-weight="700" fill="{c["ink"]}">Top <tspan fill="{c["primary"]}">Languages</tspan></text>'
    langs = d["langs"]
    total = sum(langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: kv[1], reverse=True)[:5]
    if not top:
        top = [("Waiting for first run", 0)]
    bw = 340
    for i, (name, val) in enumerate(top):
        pct = 100 * val / total
        y = 92 + i * 41
        wbar = max(6, bw * pct / 100) if val else 0
        inner = (f'<text x="40" y="{y}" font-family="{FONT}" font-size="15" font-weight="600" fill="{c["ink"]}">{esc(name)}</text>'
                 f'<text x="380" y="{y}" text-anchor="end" font-family="{FONT}" font-size="14" fill="{c["body"]}">{pct:.1f}%</text>'
                 f'<rect x="40" y="{y+9}" width="{bw}" height="10" rx="5" fill="{c["deep"]}"/>'
                 f'<rect x="40" y="{y+9}" width="0" height="10" rx="5" fill="{c["bars"][i % 5]}">'
                 f'<animate attributeName="width" from="0" to="{wbar:.1f}" dur="1.1s" begin="{0.3+i*0.12:.2f}s" fill="freeze" calcMode="spline" keySplines=".2 .8 .2 1" keyTimes="0;1"/></rect>')
        out += rise(0.15 + i * 0.1, inner, 8)
    out += f'<text x="40" y="296" font-family="{FONT}" font-size="12" fill="{c["muted"]}">By bytes of code in public repositories</text>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Top languages for {USER}">'
            f'<defs>{clay("clay", c)}{shine_defs(c)}{defs}</defs>{body}{out}</svg>')

def main():
    if DEMO:
        d = dict(stars="-", forks="-", repos="-", followers="-", commits="-", prs="-", langs={})
    else:
        try:
            d = fetch()
        except Exception as e:
            print("GitHub API failed, keeping the previous cards:", e)
            return 0
    os.makedirs(OUT, exist_ok=True)
    for m in ("light", "dark"):
        open(os.path.join(OUT, f"stats-{m}.svg"), "w").write(stats_svg(m, d))
        open(os.path.join(OUT, f"langs-{m}.svg"), "w").write(langs_svg(m, d))
    print("stats cards written")
    return 0

if __name__ == "__main__":
    sys.exit(main())
