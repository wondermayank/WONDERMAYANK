"""Generates the static light/dark SVG assets (banner, headings, cards, divider). Run: python scripts/gen_assets.py"""
import os, base64
from theme import T, FONT, ICONS, esc, clay, shine_defs, shell, rise

for _m in T.values():
    for _i, _k in enumerate(("t1", "t2", "t3", "t4")):
        _m[_k] = _m["tint"][_i]

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
A = os.path.join(ROOT, "assets")
b64 = lambda p: base64.b64encode(open(os.path.join(A, p), "rb").read()).decode()
ICONS.update({
 "bolt": "M13 2L4 14h7l-1 8 9-12h-7z",
 "chat": "M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z",
 "book": "M2 4h7a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H2z M22 4h-7a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h8z",
 "test": "M9 4h6v3H9z M7 5H5a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V6a1 1 0 0 0-1-1h-2 M9 14l2 2 4-4",
 "spark": "M12 3l2.2 5.8L20 11l-5.8 2.2L12 19l-2.2-5.8L4 11l5.8-2.2z",
 "grid": "M4 4h7v7H4z M13 4h7v7h-7z M4 13h7v7H4z M13 13h7v7h-7z",
 "hex": "M12 3l8 4.5v9L12 21l-8-4.5v-9z M12 12l8-4.5 M12 12v9 M12 12L4 7.5",
 "key": "M3 6h18a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1z M6 10h.01 M10 10h.01 M14 10h.01 M18 10h.01 M7 14h10",
})
def w(name, s): open(os.path.join(A, name), "w").write(s)
def icon(c, name, cx, cy, r=26, tint=None, sc=1.0):
    s = r / 26 * 1.0 * sc
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{tint}"/>'
            f'<g transform="translate({cx-12*s} {cy-12*s}) scale({s})" fill="none" stroke="{c["active"]}" stroke-width="{2/s:.2f}" stroke-linecap="round" stroke-linejoin="round"><path d="{ICONS[name]}"/></g>')

def banner(mode):
    c = T[mode]; W, H = 1200, 380
    def orb(cx, cy, r, col, dx, dy, dur, op):
        return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" opacity="{op}" filter="url(#blur)"><animateTransform attributeName="transform" type="translate" values="0 0;{dx} {dy};0 0" dur="{dur}s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1;.45 0 .55 1" keyTimes="0;.5;1"/></circle>')
    def rs(x, y, size, weight, fill, text, delay):
        return rise(delay, f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}">{esc(text)}</text>', 26)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Mayank Shrivastava, Founder and Developer, Edtech and Web Applications">
<defs>{clay("clay", c)}<filter id="blur"><feGaussianBlur stdDeviation="38"/></filter>
<pattern id="dots" width="26" height="26" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.4" fill="{c["primary"]}" opacity=".35"/></pattern>
<linearGradient id="sheen" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{c["primary"]}"/><stop offset=".5" stop-color="{c["active"]}"/><stop offset="1" stop-color="{c["primary"]}"/>
<animate attributeName="x1" values="-0.5;0.5;-0.5" dur="5s" repeatCount="indefinite"/><animate attributeName="x2" values="0.5;1.5;0.5" dur="5s" repeatCount="indefinite"/></linearGradient>
<clipPath id="cp"><rect width="{W}" height="{H}" rx="32"/></clipPath></defs>
<g clip-path="url(#cp)">
<rect width="{W}" height="{H}" fill="{c["canvas"]}"/><rect width="{W}" height="{H}" fill="url(#dots)" opacity=".8"/>
{orb(180,320,150,c["t1"],60,-30,9,".85")}{orb(560,40,120,c["t2"],-50,40,11,".7")}{orb(1000,200,190,c["t3"],-40,-40,10,".9")}
<image x="64" y="30" width="54" height="54" href="data:image/svg+xml;base64,{b64("favicon.svg")}" xlink:href="data:image/svg+xml;base64,{b64("favicon.svg")}"/>
<text x="132" y="68" font-family="{FONT}" font-size="30" font-weight="700" fill="{c["ink"]}">Wonder<tspan fill="{c["primary"]}">mayank</tspan></text>
{rs(64,172,78,700,c["ink"],"Mayank",0.15)}{rs(64,254,78,700,"url(#sheen)","Shrivastava",0.35)}
{rs(64,306,27,600,c["body"],"Founder & Developer | Edtech & Web Applications",0.6)}
{rs(64,346,21,400,c["muted"],"Sironj, Madhya Pradesh, India",0.8)}
<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -7;0 0" dur="5s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1;.45 0 .55 1" keyTimes="0;.5;1"/>
<image x="760" y="22" width="400" height="356" preserveAspectRatio="xMidYMax meet" href="data:image/gif;base64,{b64("tiny.gif")}" xlink:href="data:image/gif;base64,{b64("tiny.gif")}"/></g>
</g></svg>'''

def heading(mode, plain, accent, name):
    c = T[mode]
    w(f"{name}-{mode}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 72" width="700" height="72" role="heading" aria-label="{esc(plain)} {esc(accent)}">
<text x="2" y="44" font-family="{FONT}" font-size="38" font-weight="700" fill="{c["ink"]}">{esc(plain)} <tspan fill="{c["primary"]}">{esc(accent)}</tspan></text>
<rect x="2" y="56" width="0" height="5" rx="2.5" fill="{c["primary"]}"><animate attributeName="width" from="0" to="64" dur=".9s" begin="0s" fill="freeze" calcMode="spline" keySplines=".2 .8 .2 1" keyTimes="0;1"/></rect></svg>''')

def card(mode, name, ic, title, lines, link, tk, delay=0):
    c = T[mode]; W, H = 420, 190
    defs, body = shell(c, 16, 12, 388, 166, "cc", 6 + delay)
    three = link and len(lines) == 3
    ys = [104, 122, 140] if three else [108, 129, 150]
    txt = "".join(f'<text x="40" y="{ys[i]}" font-family="{FONT}" font-size="15.5" fill="{c["body"]}">{esc(l)}</text>' for i, l in enumerate(lines))
    if link:
        txt += f'<text x="40" y="{164 if three else 160}" font-family="{FONT}" font-size="14" font-weight="600" fill="{c["active"]}">{esc(link)}  &#8594;</text>'
    w(f"{name}-{mode}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc(title)}">
<defs>{clay("clay", c, 7, 9)}{shine_defs(c)}{defs}</defs>{body}{icon(c, ic, 64, 62, 26, c[tk])}
<text x="104" y="70" font-family="{FONT}" font-size="23" font-weight="700" fill="{c["ink"]}">{esc(title)}</text>{txt}</svg>''')

def tile(mode, name, ic, big, label, tk, delay=0):
    c = T[mode]; W, H = 300, 116
    defs, body = shell(c, 12, 8, 276, 96, "ct", 7 + delay)
    w(f"{name}-{mode}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc(big)} {esc(label)}">
<defs>{clay("clay", c, 5, 7)}{shine_defs(c)}{defs}</defs>{body}{icon(c, ic, 62, 56, 26, c[tk])}
<text x="104" y="55" font-family="{FONT}" font-size="30" font-weight="700" fill="{c["ink"]}">{esc(big)}</text>
<text x="104" y="79" font-family="{FONT}" font-size="14.5" fill="{c["muted"]}">{esc(label)}</text></svg>''')

def divider(mode):
    a, b = ("#70A1FC", "#5D79B3") if mode == "light" else ("#5EEAD4", "#26427A")
    w(f"divider-{mode}.svg", ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 24" width="1200" height="24" role="presentation">'
      f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{a}" stop-opacity="0"/><stop offset=".3" stop-color="{a}"/><stop offset=".7" stop-color="{b}"/><stop offset="1" stop-color="{b}" stop-opacity="0"/></linearGradient></defs>'
      '<rect x="40" y="10" width="1120" height="4" rx="2" fill="url(#g)" opacity=".6"/>'
      f'<circle cy="12" r="7" fill="{a}"><animate attributeName="cx" values="60;1140;60" dur="9s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1;.45 0 .55 1" keyTimes="0;.5;1"/>'
      f'<animate attributeName="fill" values="{a};{b};{a}" dur="9s" repeatCount="indefinite"/></circle></svg>'))

for m in ("light", "dark"):
    w(f"banner-{m}.svg", banner(m)); divider(m)
    for p, a, n in [("About","Me","h-about"),("Featured","Projects","h-projects"),("Thunder","Ecosystem","h-thunder"),("Recent","Work","h-recent"),("Tech","Stack","h-stack"),
                    ("GitHub","Stats","h-stats"),("3D","Contributions","h-3d"),("Contribution","Snake","h-snake"),("Live","Status","h-status"),
                    ("Latest","Posts","h-posts"),("Let's","Connect","h-connect")]:
        heading(m, p, a, n)
    projs = [("c-hub","grid","Project Hub",["Free utility tools, vibecoding builds","and creative web experiments."],"project.wondermayank.in","t1"),
             ("c-logos","hex","Logos",["Free SVG logo explorer with a","viewer and an SVG maker."],"github.com/wondermayank/logos","t3"),
             ("c-typing","key","Hindi Typing",["Hindi typing practice with Inscript","and Remington layouts."],"project.wondermayank.in/typing","t2"),
             ("c-sign","spark","SignLearn",["Practise ASL and ISL sign language","with your webcam, right in the browser."],"project.wondermayank.in/fun/Sign_language","t1"),
             ("c-body","chat","Body School",["Bilingual body-awareness lessons,","activities and chat with Tiny and Byte."],"body.wondermayank.in","t2"),
             ("c-fest","star","Festivals by Tiny",["Tiny in festival dresses from Hindu,","Muslim, Sikh, Christian, Buddhist","and Jain traditions."],"festival.wondermayank.in","t3")]
    for i, (n, ic, t, l, lk, tk) in enumerate(projs): card(m, n, ic, t, l, lk, tk, i * 0.6)
    thunder = [("th-study","book","ThunderStudy",["Notes, PYQs, formulas and commerce","and CUET study pages, free for","every student."],"thunderstudy.indevs.in","t1"),
               ("th-test","test","ThunderTest",["CBT mock tests and PYQs for CUET, JEE,","NEET, SSC, Banking, CAT, CLAT","and NDA."],"thundertest.indevs.in","t2"),
               ("th-ai","spark","ThunderStudy AI",["AI chat, mind maps, formula stories","and AI-made mock tests for","faster exam prep."],"ai.thunderstudy.indevs.in","t3"),
               ("th-english","chat","Thunder English",["Fresh English MCQs and one-word","substitutions, plus CUET English","practice powered by Tiny."],"thunderenglish.indevs.in","t1"),
               ("th-bots","bolt","Thunder Bots",["22 Telegram bots for study chat,","notes, quizzes, PDFs, reminders","and more."],"wondermayank.in/bots","t2"),
               ("th-blog","book","ThunderStudy Blog",["Daily posts on CUET English, GK and","how to study smarter for","your exams."],"blog.thunderstudy.indevs.in","t3"),
               ("th-docs","grid","ThunderDocs",["AI document generator with Word, PDF,","PowerPoint, Excel and Markdown","output."],"aipdf.wondermayank.indevs.in","t1"),
               ("th-tg","chat","Telegram Community",["Updates, PYQs, CBT and English","practice channels for students","on Telegram."],"t.me/thunderstudy","t2")]
    for i, (n, ic, t, l, lk, tk) in enumerate(thunder): card(m, n, ic, t, l, lk, tk, i * 0.5)
    about = [("a-build","bolt","Building",["Educational platforms, CBT mock","tests, student tools and AI","study helpers."],"t1"),
             ("a-learn","book","Learning",["Advanced frontend, full-stack web,","AI tools, performance and","UI animation."],"t2"),
             ("a-open","spark","Open to",["Open-source education projects,","UI/UX design, SEO, and computer","teacher or operator roles."],"t3"),
             ("a-ask","chat","Ask me about",["Web development, GitHub Pages,","design systems, branding and","creative coding."],"t4" if False else "t1")]
    for i, (n, ic, t, l, tk) in enumerate(about): card(m, n, ic, t, l, None, tk, i * 0.7)
    for i, (n, ic, big, lab, tk) in enumerate([("t-tools","grid","800+","Free tools built","t1"),("t-stars","star","800+","GitHub stars earned","t2"),("t-hubs","test","7","Exam hubs live","t3")]):
        tile(m, n, ic, big, lab, tk, i * 0.8)
print("assets written")


# ---------- hand-drawn portrait (pencil sketch draws itself, then colour is painted in) ----------
def portrait():
    import io, numpy as np
    from PIL import Image, ImageOps, ImageFilter
    S = 460
    im = Image.open(os.path.join(A, "source", "mayank-photo.webp")).convert("RGB").resize((S, S), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=84, optimize=True); photo = base64.b64encode(buf.getvalue()).decode()
    a = np.asarray(ImageOps.grayscale(im).filter(ImageFilter.GaussianBlur(1.1))).astype(float)
    gx = np.zeros_like(a); gy = np.zeros_like(a)
    gx[:, 1:-1] = a[:, 2:] - a[:, :-2]; gy[1:-1, :] = a[2:, :] - a[:-2, :]
    alpha = (np.clip((np.hypot(gx, gy) - 10) / 60, 0, 1) * 255).astype(np.uint8)
    line = Image.new("RGBA", (S, S), (31, 42, 68, 0)); line.putalpha(Image.fromarray(alpha))
    buf = io.BytesIO(); line.save(buf, "PNG", optimize=True); sketch = base64.b64encode(buf.getvalue()).decode()
    # scribble path: back-and-forth hatching over the whole picture, 1000 units long after pathLength
    pts = []; x0, x1, step = -10, 470, 44
    for r, y in enumerate(range(20, 450, 38)):
        xs = list(range(x0, x1 + 1, step))
        if r % 2: xs.reverse()
        for k, x in enumerate(xs):
            pts.append((x, y + (-15 if k % 2 else 15)))
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    D = 18
    def dash(values, times):
        return (f'<animate attributeName="stroke-dashoffset" values="{values}" keyTimes="{times}" dur="{D}s" repeatCount="indefinite"/>')
    sk = f'<path d="{d}" pathLength="1000" fill="none" stroke="#fff" stroke-width="74" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1000" stroke-dashoffset="0">{dash("1000;0;0;0", "0;.28;.95;1")}</path>'
    co = f'<path d="{d}" pathLength="1000" fill="none" stroke="#fff" stroke-width="74" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1000" stroke-dashoffset="0">{dash("1000;1000;0;0", "0;.30;.62;1")}</path>'
    def tip(keys, times, opac_v, opac_t):
        return (f'<g opacity="0"><animateMotion dur="{D}s" repeatCount="indefinite" calcMode="linear" keyPoints="{keys}" keyTimes="{times}" path="{d}"/>'
                f'<animate attributeName="opacity" values="{opac_v}" keyTimes="{opac_t}" dur="{D}s" repeatCount="indefinite"/>'
                '<circle r="7" fill="#5D79B3"/><path d="M0 0 L26 -26" stroke="#26324A" stroke-width="5" stroke-linecap="round"/></g>')
    t1 = tip("0;1;1", "0;.28;1", "1;1;0;0", "0;.27;.29;1")
    t2 = tip("0;0;1;1", "0;.30;.62;1", "0;0;1;1;0;0", "0;.30;.31;.61;.63;1")
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 500 500" width="500" height="500" role="img" aria-label="Hand-drawn portrait of Mayank">
<defs><filter id="sh" x="-15%" y="-15%" width="130%" height="135%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000" flood-opacity=".28"/></filter>
<clipPath id="pc"><rect x="20" y="14" width="460" height="460" rx="44"/></clipPath>
<mask id="ms" maskUnits="userSpaceOnUse" x="0" y="0" width="500" height="500">{sk}</mask>
<mask id="mc" maskUnits="userSpaceOnUse" x="0" y="0" width="500" height="500">{co}</mask></defs>
<rect x="20" y="14" width="460" height="460" rx="44" fill="#FFFFFF" filter="url(#sh)"/>
<g clip-path="url(#pc)"><g transform="translate(20 14)">
<g><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.88;.95;1" dur="{D}s" repeatCount="indefinite"/>
<image width="{S}" height="{S}" mask="url(#mc)" href="data:image/jpeg;base64,{photo}" xlink:href="data:image/jpeg;base64,{photo}"/>
<image width="{S}" height="{S}" mask="url(#ms)" href="data:image/png;base64,{sketch}" xlink:href="data:image/png;base64,{sketch}"/>
<g transform="translate(0 0)">{t1}{t2}</g></g></g></g></svg>'''
    w("portrait.svg", svg)

# ---------- lightning bolt drawn by a snake ----------
def bolt(mode):
    c = T[mode]
    d = "M262 16 L124 170 L200 170 L162 304 L306 132 L230 132 L292 16 Z"
    D = 12
    trail = c["primary"] if mode == "light" else "#5EEAD4"
    track = c["soft"] if mode == "light" else "#1D5A56"
    body = c["primary"] if mode == "light" else "#99F6E4"
    def dashes(L, wdt, op):
        return (f'<path d="{d}" pathLength="1000" fill="none" stroke="{body}" stroke-width="{wdt}" stroke-linecap="round" stroke-linejoin="round" opacity="{op}" stroke-dasharray="{L} 2000">'
                f'<animate attributeName="stroke-dashoffset" values="{L};-1000;-1000" keyTimes="0;.5;1" dur="{D}s" repeatCount="indefinite"/></path>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 320" width="420" height="320" role="img" aria-label="Thunder bolt drawn by a snake">
<defs><linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFF5B8"/><stop offset=".55" stop-color="#FFD54A"/><stop offset="1" stop-color="#F59E0B"/></linearGradient>
<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="9"/></filter></defs>
<g><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.86;.95;1" dur="{D}s" repeatCount="indefinite"/>
<path d="{d}" fill="none" stroke="{track}" stroke-width="7" stroke-linejoin="round" opacity=".7"/>
<path d="{d}" fill="#FFD54A" opacity="0" filter="url(#glow)"><animate attributeName="opacity" values="0;0;.45;.45" keyTimes="0;.5;.62;1" dur="{D}s" repeatCount="indefinite"/></path>
<path d="{d}" fill="url(#gold)" opacity="0"><animate attributeName="opacity" values="0;0;1;1" keyTimes="0;.5;.62;1" dur="{D}s" repeatCount="indefinite"/></path>
<path d="{d}" pathLength="1000" fill="none" stroke="{trail}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="1000" stroke-dashoffset="1000">
<animate attributeName="stroke-dashoffset" values="1000;0;0" keyTimes="0;.5;1" dur="{D}s" repeatCount="indefinite"/></path>
{dashes(150, 7, ".45")}{dashes(95, 11, ".7")}{dashes(45, 16, "1")}
<g opacity="0"><animateMotion dur="{D}s" repeatCount="indefinite" calcMode="linear" keyPoints="0;1;1" keyTimes="0;.5;1" path="{d}"/>
<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.51;1" dur="{D}s" repeatCount="indefinite"/>
<circle r="11" fill="{body}"/><circle cx="3" cy="-3" r="3.4" fill="#fff"/><circle cx="4" cy="-3" r="1.6" fill="#26324A"/></g></g></svg>'''
    w(f"bolt-{mode}.svg", svg)

portrait(); bolt("light"); bolt("dark")
print("portrait + bolt written")
