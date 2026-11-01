import re,glob,json
rx=re.compile(r'FUN_[0-9a-f]+\(\w+,(?:\w+,)?"([A-Za-z_]\w*)",')
def sets(base):
    out={}
    for p in glob.glob(base+"/functions/*.c"):
        s=open(p,encoding="utf-8",errors="ignore").read()
        ks=rx.findall(s)
        if len(ks)>=3: out[re.search(r"(0x[0-9a-f]+)\.c",p.replace("\\","/")).group(1)]=ks
    return out
S={n:sets(f"out/{n}") for n in ("sneseur-2.0.14","nes-1.0.7","hvcj-shonen-3.0.1")}
json.dump(S,open("out/keysets.json","w"))
sig=lambda ks:tuple(sorted(set(ks)))
base={sig(v):a for a,v in S["sneseur-2.0.14"].items()}
print("SNES keysets",len(base))
for n in ("nes-1.0.7","hvcj-shonen-3.0.1"):
    mine={sig(v):a for a,v in S[n].items()}
    print(n,len(mine),"keysets; same as SNES:",len(set(mine)&set(base)))
    for k in sorted(set(base)-set(mine)): print("  only SNES:",k)
    for k in sorted(set(mine)-set(base)): print("  only",n,":",k)
