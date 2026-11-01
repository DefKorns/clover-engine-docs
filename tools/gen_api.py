import json,re,collections,pathlib
M=json.load(open("out/api-model.json"))
FAMS=["SNES","NES","Shonen"]
STATIC={"Application","FileUtils","Input","Localization","CRC64"}
NOTES={
 "SoundComponent.isPlaying":"Returns false when the component has no native sound object (for example a disabled one); it does not raise an error.",
 "SoundComponent.getSamplePosition":"Returns 0.0 when the component has no native sound object; it does not raise an error.",
 "SoundComponent.setSoundResource":"The argument must be a loaded SoundResource; otherwise the engine raises 'resource (SoundResource) is not loaded'.",
 "Component.disable":"Disables the component. The boot music (Main.bootBGM) is disabled this way by main.lua and by the Shonen firmware.",
 "Component.enable":"Enables the component.",
}
def words(name): return re.sub(r"([a-z0-9])([A-Z])",r"\1 \2",name).lower()
def kind(m):
    if re.match(r"(get)",m): return "get"
    if re.match(r"(is|has)[A-Z]",m): return "get"
    if re.match(r"set",m): return "set"
    return "do"
def describe(c,m):
    k=kind(m)
    if k=="get":
        w=words(re.sub(r"^(get|is|has)","",m)) or "value"
        return (f"Returns whether {w}." if re.match(r"(is|has)[A-Z]",m) else f"Returns the {w}.")
    if k=="set": return f"Sets the {words(m[3:]) or 'value'}."
    return f"Calls {words(m)}."
def pname(m,i,n,t):
    if n==1 and m.startswith("set") and len(m)>3: return m[3].lower()+m[4:]
    return f"arg{i+1}"
classes=collections.OrderedDict()
allc=sorted({k.split(".")[0] for f in FAMS for k in M[f]})
for c in allc:
    ms=sorted({k.split(".",1)[1] for f in FAMS for k in M[f] if k.startswith(c+".")})
    ops=[]
    for m in ms:
        fam={f:M[f].get(f"{c}.{m}") for f in FAMS}
        src=next((fam[f] for f in ("SNES","Shonen","NES") if fam[f]),None)
        best=fam["SNES"] or fam["Shonen"] or fam["NES"]
        typed=bool(fam["SNES"] or fam["Shonen"])
        n=best["args"]
        params=[{"name":pname(m,i,n,t),"type":t} for i,t in enumerate(best["params"])] if n is not None else []
        ops.append({"method":m,"kind":kind(m),"static":c in STATIC,"args":n,"params":params,"returns":best["returns"],
            "typed":typed,"summary":describe(c,m),"note":NOTES.get(f"{c}.{m}",""),
            "families":{f:(fam[f]["addr"] if fam[f] else None) for f in FAMS},
            "arity":{f:(fam[f]["args"] if fam[f] else None) for f in FAMS}})
    classes[c]=ops
json.dump(classes,open("docs/lua-api.json","w",newline="\n"),indent=1)
# markdown
def sig(c,o):
    sep="." if o["static"] else ":"
    if o["args"] is None: ps="..."
    else: ps=", ".join(f'{p["name"]}: {p["type"]}' for p in o["params"])
    r=o["returns"]; rs=("" if not r else (": "+r[0] if len(r)==1 else ": ("+", ".join(r)+")"))
    return f"{c}{sep}{o['method']}({ps}){rs}"
out=["# Lua API reference","",
"Every class and method the engine exposes to Lua, with its signature, which engine families bind it, and the",
"address of its binding in each build. Interactive version: `index.html`, page *API explorer*.","",
"## How to read this","",
"- `Class:method(...)` is an instance method (called with a colon); `Class.method(...)` is a static function of a",
"  global table (`Application`, `FileUtils`, `Input`, `Localization`, `CRC64`).",
"- Parameter and return types come from the engine code: the helper each binding calls to read an argument or push a",
"  result (`number`, `integer`, `boolean`, `string`, or a resource class). `any` means the argument is read by a helper",
"  that was not classified. Parameter names are not in the binary: single-argument setters use the name after `set`,",
"  the rest are `argN`.",
"- Families: **S** = SNES (EUR, USA, SHVC; identical API), **N** = NES and HVC (identical API), **J** = Shonen. The NES",
"  signatures list only the number of arguments: its binding code was not classified.",
"- The summaries are derived from the method names. Lines under *Note* were verified in the code.","",
"## Contents",""]
for c in classes: out.append(f"- [{c}](#{c.lower()}) ({len(classes[c])} method{'' if len(classes[c])==1 else 's'})")
out.append("")
for c,ops in classes.items():
    out+= [f"## {c}","",f"{len(ops)} method{'' if len(ops)==1 else 's'}. "+("Static functions of a global table." if c in STATIC else "Instance methods."),"",
           "| Method | Signature | Families | Summary |","|---|---|---|---|"]
    for o in ops:
        fam="".join(x for x,f in (("S","SNES"),("N","NES"),("J","Shonen")) if o["families"][f])
        sg=sig(c,o) if o["typed"] else f'{c}{"." if o["static"] else ":"}{o["method"]}({o["args"] if o["args"] is not None else "?"} args)'
        out.append(f'| `{o["method"]}` | `{sg}` | {fam} | {o["summary"]}{(" **Note:** "+o["note"]) if o["note"] else ""} |')
    out.append("")
pathlib.Path("docs/lua-api.md").write_text("\n".join(out),encoding="utf-8",newline="\n")
tot=sum(len(v) for v in classes.values()); print(len(classes),"classes",tot,"methods")
