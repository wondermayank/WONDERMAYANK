"""Auto-lists the most recently updated public repos as clay cards and rewrites the README block.
Each card links to the repo's website URL (the "Website" field in the repo About panel) or, if empty, to the repo itself."""
import os, re, sys, json, textwrap, urllib.request
from urllib.parse import urlparse
from theme import T, FONT, esc, clay, shine_defs, shell
from gen_assets_lib import icon

USER = os.environ.get("GH_USER", "wondermayank")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
DEMO = os.environ.get("DEMO") == "1"
COUNT = 4
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "assets", "auto")
README = os.path.join(ROOT, "README.md")
START, END = "<!-- LATEST-PROJECTS:START -->", "<!-- LATEST-PROJECTS:END -->"
LANG_TINT = {"HTML": 4, "CSS": 1, "JavaScript": 3, "TypeScript": 1, "Python": 2, "Shell": 3}

def api(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "profile-projects"})
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def pick():
    repos = api(f"https://api.github.com/users/{USER}/repos?per_page=100&sort=pushed&direction=desc&type=owner")
    ok = [r for r in repos if not r["fork"] and not r["archived"] and r["name"].lower() != USER.lower()]
    return ok[:COUNT]

def nice(name):
    return name.replace("-", " ").replace("_", " ").strip().title() if name == name.lower() else name

def short(txt, width=36, lines=2):
    out = textwrap.wrap(txt or "", width=width)
    if len(out) > lines:
        out = out[:lines]
        out[-1] = out[-1][:width - 1].rstrip(" .,;") + "..."
    return out or ["No description yet."]

def link_label(r):
    hp = (r.get("homepage") or "").strip()
    if hp:
        u = urlparse(hp if "//" in hp else "https://" + hp)
        return (u.netloc + u.path).rstrip("/")
    return f"github.com/{r['full_name']}"

def card_svg(mode, r, i):
    c = T[mode]; W, H = 420, 190
    defs, body = shell(c, 16, 12, 388, 166, "cc", 6 + i * .6)
    lang = r.get("language") or "Project"
    desc = "".join(f'<text x="40" y="{108 + k*21}" font-family="{FONT}" font-size="15.5" fill="{c["body"]}">{esc(l)}</text>' for k, l in enumerate(short(r.get("description"))))
    meta = f'{lang}  |  {r["stargazers_count"]} stars'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc(r["name"])}">'
            f'<defs>{clay("clay", c, 7, 9)}{shine_defs(c)}{defs}</defs>{body}{icon(c, "repo", 64, 62, 26, c["tint"][i % 4])}'
            f'<text x="104" y="62" font-family="{FONT}" font-size="22" font-weight="700" fill="{c["ink"]}">{esc(nice(r["name"])[:22])}</text>'
            f'<text x="104" y="82" font-family="{FONT}" font-size="13" fill="{c["muted"]}">{esc(meta)}</text>{desc}'
            f'<text x="40" y="160" font-family="{FONT}" font-size="13.5" font-weight="600" fill="{c["active"]}">{esc(link_label(r)[:40])}  &#8594;</text></svg>')

def block(repos):
    parts = []
    for i, r in enumerate(repos):
        href = (r.get("homepage") or "").strip() or r["html_url"]
        if "//" not in href:
            href = "https://" + href
        parts.append(f'<a href="{href}"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/auto/proj-{i+1}-dark.svg">'
                     f'<img src="assets/auto/proj-{i+1}-light.svg" alt="{esc(r["name"])}" width="398"></picture></a>')
    return START + '\n<p align="center">\n' + "\n".join(parts) + '\n</p>\n' + END

def main():
    if DEMO:
        repos = [dict(name=f"repo-{i+1}", full_name=f"{USER}/repo-{i+1}", html_url=f"https://github.com/{USER}?tab=repositories",
                      homepage="", description="Waiting for the first workflow run.", stargazers_count=0, language=None) for i in range(COUNT)]
    else:
        try:
            repos = pick()
        except Exception as e:
            print("GitHub API failed, keeping previous projects:", e)
            return 0
    os.makedirs(OUT, exist_ok=True)
    for i, r in enumerate(repos):
        for m in ("light", "dark"):
            open(os.path.join(OUT, f"proj-{i+1}-{m}.svg"), "w").write(card_svg(m, r, i))
    if os.path.exists(README):
        txt = open(README).read()
        new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: block(repos), txt, flags=re.S)
        open(README, "w").write(new)
    print("projects:", [r["name"] for r in repos])
    return 0

if __name__ == "__main__":
    sys.exit(main())
