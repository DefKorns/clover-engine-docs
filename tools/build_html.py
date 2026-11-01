import re, html, pathlib, markdown

docs = pathlib.Path(__file__).resolve().parent.parent / "docs"
pages = [
    ("clover-engine-reference", "Reference"),
    ("supervisor", "Supervisor"),
    ("file-formats", "File formats"),
    ("scene-components", "Scene components"),
    ("lua-api", "Lua API (table)"),
    ("boot-music", "Boot music"),
    ("c8-error", "Error C8"),
    ("family-differences", "Family differences"),
    ("lua-toolchain", "Lua toolchain"),
    ("README", "About"),
]

def slug(text, sep="-"):
    s = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    return re.sub(r"[\s_-]+", sep, s)

sections, nav = [], []
for name, title in pages:
    src = (docs / f"{name}.md").read_text(encoding="utf-8")
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc"],
                           extension_configs={"toc": {"slugify": lambda v, s: f"{name}--" + slug(v), "permalink": False}})
    body = md.convert(src)
    # links between pages and to anchors
    for other, _ in pages:
        body = body.replace(f"<code>{other}.md</code>", f'<a href="#{other}" class="xref"><code>{other}.md</code></a>')
    page_ids = set(re.findall(r'id="([^"]+)"', body))
    body = re.sub(r'href="#([^"]+)"',
                  lambda m: f'href="#{name}--{m.group(1)}"' if f"{name}--{m.group(1)}" in page_ids else m.group(0), body)
    # the reference's contents list uses GitHub-style anchors: map them to the generated ids
    ids = {re.sub(r"<[^>]+>", "", h): i for i, h in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)}
    def fix(m):
        target = m.group(1)
        return m.group(0)
    sections.append(f'<section id="{name}" class="page">{body}</section>')
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    sub = "".join(f'<a class="sub" href="#{i}">{re.sub(r"<[^>]+>", "", t)}</a>' for i, t in heads) if name == "clover-engine-reference" else ""
    nav.append(f'<a class="top" href="#{name}" data-page="{name}">{html.escape(title)}</a>{sub}')

# GitHub-style anchors in the reference TOC: #1-architecture -> real id
import json as _json
api = _json.loads((docs / "lua-api.json").read_text(encoding="utf-8"))
explorer = (
    '<section id="api-explorer" class="page"><h1>API explorer</h1>'
    '<p class="lead">Every class and method the engine exposes to Lua. Click an operation to see its parameters, '
    'return values and the binding address in each build.</p>'
    '<div id="apibar"><input id="apiq" placeholder="Search a class or method" autocomplete="off">'
    '<label><input type="checkbox" class="fam" value="SNES" checked> SNES</label>'
    '<label><input type="checkbox" class="fam" value="NES" checked> NES</label>'
    '<label><input type="checkbox" class="fam" value="Shonen" checked> Shonen</label>'
    '<select id="apikind"><option value="">All kinds</option><option value="get">GET</option>'
    '<option value="set">SET</option><option value="do">CALL</option></select>'
    '<button id="apiexp">Expand all</button></div><div id="apiroot"></div></section>')
sections.insert(1, explorer)
nav.insert(1, '<a class="top" href="#api-explorer" data-page="api-explorer">API explorer</a>')
apijson = '<script type="application/json" id="apidata">' + _json.dumps(api).replace("</", "<\\/") + "</script>"
ajs = (pathlib.Path(__file__).parent / "explorer_js.txt").read_text(encoding="utf-8")
page_html = "\n".join(sections)
def anchor_fix(m):
    frag = m.group(1)
    mm = re.match(r"(\d+)-(.+)", frag)
    return m.group(0)
page_html = re.sub(r'href="#clover-engine-reference--(\d+)-([^"]*)"',
                   lambda m: f'href="#clover-engine-reference--{m.group(1)}-{m.group(2)}"', page_html)

css = (pathlib.Path(__file__).parent / "explorer.css").read_text(encoding="utf-8") + """
:root{--bg:#fff;--fg:#1d2330;--mut:#5b6478;--line:#dfe3ec;--side:#f5f7fb;--acc:#2c5fd6;--code:#eef1f7;--tbl:#f8f9fc}
@media(prefers-color-scheme:dark){:root{--bg:#14171f;--fg:#dde2ee;--mut:#98a2b8;--line:#2a3040;--side:#1a1e29;--acc:#7ea6ff;--code:#222838;--tbl:#191d27}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
nav{position:fixed;inset:0 auto 0 0;width:270px;background:var(--side);border-right:1px solid var(--line);overflow-y:auto;padding:18px 14px}
nav h1{font-size:15px;margin:0 0 12px;color:var(--mut);text-transform:uppercase;letter-spacing:.06em}
nav a{display:block;color:var(--fg);text-decoration:none;padding:4px 8px;border-radius:6px;font-size:14px}
nav a.top{font-weight:600;margin-top:8px}
nav a.sub{padding-left:20px;font-size:13px;color:var(--mut)}
nav a:hover{background:var(--line)}nav a.on{background:var(--acc);color:#fff}
nav input{width:100%;padding:7px 9px;margin-bottom:10px;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--fg)}
main{margin-left:270px;padding:36px 48px 120px;max-width:1040px}
section.page{display:none}section.page.on{display:block}
h1,h2,h3,h4{line-height:1.25;margin:1.8em 0 .5em}h1{font-size:2em;margin-top:0;border-bottom:1px solid var(--line);padding-bottom:.3em}
h2{font-size:1.45em;border-bottom:1px solid var(--line);padding-bottom:.2em}h3{font-size:1.15em}
a{color:var(--acc)}code{background:var(--code);padding:.1em .35em;border-radius:4px;font:13.5px/1.4 ui-monospace,Consolas,monospace}
pre{background:var(--code);padding:14px;border-radius:8px;overflow:auto}pre code{padding:0;background:none}
table{border-collapse:collapse;margin:1em 0;display:block;overflow-x:auto;width:max-content;max-width:100%}
th,td{border:1px solid var(--line);padding:6px 10px;vertical-align:top;text-align:left;font-size:14.5px}
th{background:var(--tbl);position:sticky;top:0}tr:nth-child(even) td{background:var(--tbl)}
hr{border:0;border-top:1px solid var(--line);margin:2em 0}
@media(max-width:860px){nav{position:static;width:auto;border:0}main{margin:0;padding:20px}}
@media print{nav{display:none}main{margin:0}section.page{display:block!important;page-break-after:always}}
"""

js = """
const pages=[...document.querySelectorAll('section.page')];
const links=[...document.querySelectorAll('nav a')];
function show(){
  let h=decodeURIComponent(location.hash.slice(1))||pages[0].id;
  let target=document.getElementById(h);
  let page=target?(target.closest('section.page')||pages[0]):pages[0];
  pages.forEach(p=>p.classList.toggle('on',p===page));
  links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+h||(a.dataset.page===page.id&&h===page.id)));
  if(target&&target!==page)target.scrollIntoView(); else window.scrollTo(0,0);
}
addEventListener('hashchange',show);show();
document.getElementById('q').addEventListener('input',e=>{
  const q=e.target.value.toLowerCase();
  links.forEach(a=>a.style.display=!q||a.textContent.toLowerCase().includes(q)?'':'none');
});
"""

out = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Clover engine reference</title><style>{css}</style></head>
<body><nav><h1>Clover engine</h1><input id="q" placeholder="Filter sections" autocomplete="off">
{''.join(nav)}</nav><main>{page_html}</main>{apijson}<script>{js}</script><script>{ajs}</script></body></html>
"""
(docs / "index.html").write_text(out, encoding="utf-8", newline="\n")
print("written", len(out), "bytes")
