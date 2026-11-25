"""Build personal/cv.pdf (one page) from personal/profile.yaml.
Usage: python3 tools/make_cv.py   (needs pyyaml + playwright + Chrome)"""
import html, os, yaml
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = yaml.safe_load(open(os.path.join(ROOT, "personal", "profile.yaml"), encoding="utf-8"))
e = lambda s: html.escape(str(s or ""))

def when(i): return " – ".join(x for x in (i.get("start"), i.get("end")) if x)

edu = "".join(
    f'<div class="entry"><div class="row"><b>{e(i["degree"])}</b><span>{e(when(i))}</span></div>'
    f'<div class="org">{e(i["institution"])}</div><div class="d">{e(i.get("detail"))}</div></div>'
    for i in p["education"])
proj = "".join(
    f'<div class="entry"><b>{e(i["title"])}</b> <span class="t">({e(", ".join(i.get("tech", [])))})</span>'
    f'<div class="d">{e(i["summary"])}</div></div>' for i in p["projects"])
skills = "".join(f'<li><b>{e(g["group"])}:</b> {e(", ".join(g["items"]))}</li>' for g in p["skills"])
ach = "".join(f'<li>{e(a["title"])}{" – " + e(a["issuer"]) if a.get("issuer") else ""}</li>' for a in p["achievements"])
hob = "".join(f'<li><b>{e(h["title"])}:</b> {e(h["text"])}</li>' for h in p["hobbies"])
c = p["contact"]
links = [("Facebook", s["url"]) for s in p["socials"] if s.get("url") and s["name"] == "facebook"]
about = e(p["bio"].strip().split("\n\n")[0])
doc = f"""<!doctype html><html lang="en"><meta charset="utf-8"><title>{e(p['name'])} — CV</title>
<style>
@page {{ size: A4; margin: 0 }}
*{{box-sizing:border-box}} body{{margin:0;padding:15mm 16mm;color:#1F3A2E;background:#FBF7EF;font:9.6pt/1.42 "Liberation Sans",Helvetica,Arial,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact;height:297mm}}
h1{{margin:0;font:600 27pt/1 "DejaVu Serif",Georgia,serif;letter-spacing:-.5pt}}
.role{{margin-top:4pt;color:#A23E5A;font-weight:700;font-size:11pt}}
.contact{{margin-top:7pt;font-size:8.8pt;color:#526357;display:flex;flex-wrap:wrap;gap:2pt 14pt}}
header{{border-bottom:1.5pt solid #1F3A2E;padding-bottom:9pt;margin-bottom:10pt}}
h2{{font:700 8.8pt "Liberation Sans",sans-serif;letter-spacing:1.3pt;text-transform:uppercase;color:#1F3A2E;margin:12pt 0 5pt;padding-bottom:2pt;border-bottom:.6pt solid #E4DCCB}}
.entry{{margin-bottom:6pt;break-inside:avoid}} .row{{display:flex;justify-content:space-between;gap:10pt}} .row span{{color:#526357}}
.org{{color:#A23E5A;font-weight:600}} .d{{color:#3b4f43}} .t{{color:#526357}}
ul{{margin:0;padding:0;list-style:none}} li{{margin-bottom:2.5pt}}
</style>
<header><h1>{e(p['name'])}</h1><div class="role">{e(p['role'])}</div>
<div class="contact"><span>{e(c['email'])}</span><span>{e(c['phone'])}</span><span>{e(p['location'])}</span>{"".join(f"<span>{n}: {e(u)}</span>" for n,u in links)}</div></header>
<h2>About</h2><div>{about}</div>
<h2>Education</h2>{edu}
<h2>Skills</h2><ul>{skills}<li><b>Languages:</b> {e(", ".join(p['languages']))}</li></ul>
<h2>Projects</h2>{proj}
<h2>Achievements</h2><ul>{ach}</ul>
<h2>Interests</h2><ul>{hob}</ul>
</html>"""
open("/tmp/cv.html", "w", encoding="utf-8").write(doc)
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(); pg.goto("file:///tmp/cv.html")
    pg.pdf(path=os.path.join(ROOT, "personal", "cv.pdf"), format="A4", print_background=True, prefer_css_page_size=True)
    b.close()
