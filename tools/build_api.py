import json,re,os,sys,collections
sys.path.insert(0,os.path.dirname(__file__))
import prim as P

STATIC={'Application','FileUtils','Input','Localization','CRC64'}
ERR={'SNES':0x9fd24,'Shonen':0x8937c,'NES':0xe78c0}
FAM={"SNES":"sneseur-2.0.14","NES":"nes-1.0.7","Shonen":"hvcj-shonen-3.0.1"}
PRIMS=P.PRIM
ref=P.load(FAM["SNES"]); REF_FP={h:P.fp(ref,int(h,16)) for h in PRIMS}

def helper_map(fam):
    n=FAM[fam]; ctx=P.load(n); m={}
    for a in ctx[2]:
        f=P.fp(ctx,a)
        for h,rf in REF_FP.items():
            if f==rf and f[0]: m[a]=PRIMS[h]
    return m

def literals(n,a):
    p=f"out/{n}/functions/0x{a:x}.c"
    if not os.path.exists(p): return []
    return re.findall(r'"([A-Za-z_][A-Za-z0-9_]*)"',open(p,encoding="utf-8",errors="ignore").read())

SKIP_TYPES={"Wrong","invalid"}
def typed_name(n,a):
    ls=[x for x in literals(n,a) if x[0].isupper() and not x.startswith("BASE_OBJECT") and " " not in x]
    return ls[-1] if ls else None

def snake_words(name):
    return re.sub(r"([a-z0-9])([A-Z])",r"\1 \2",name).lower()

def analyse(fam):
    n=FAM[fam]
    sig=json.load(open(f"out/{n}-sig.json"))
    hm=helper_map(fam) if fam!="NES" else {}
    # anchor fill for missing primitives
    if fam!="NES":
        s=sig["SoundComponent.setVolume"]
        base=set(a for a,_ in sig["SoundComponent.pause"]["calls"])|set(a for a,_ in sig["SoundComponent.play"]["calls"])
        cand=[a for a,_ in s["calls"] if a not in base and a not in hm]
        if cand: hm[cand[0]]="number"
    ctx=P.load(n)
    res={}
    for k,v in sig.items():
        cls=v["class"]; static=cls in STATIC
        args=None
        if v["expected"] is not None and v["expected"]<=10: args=v["expected"]-(0 if static else 1)
        params=[];rets=[]
        calls=[(a,r) for a,r in v["calls"]]
        # first non-error call of an instance method is the typed self getter
        errs=ERR.get(fam)
        seen_self=static
        for a,r1 in calls:
            if a==errs: continue
            kind=hm.get(a)
            if kind and kind.startswith("push:"): rets.append(kind[5:]); continue
            if kind: params.append(kind); continue
            if not seen_self: seen_self=True; continue
            if fam!="NES":
                t=typed_name(n,a)
                if t and t not in ("Wrong",) and not literals(n,a)==[]: params.append(t)
        if args is not None:
            params=params[:args]
            params+=["any"]*(args-len(params))
        if v["ret"] is not None and len(rets)>v["ret"]: rets=rets[:v["ret"]]
        res[k]={"args":args,"params":params,"returns":rets,"nret":v["ret"],"addr":"0x"+v["addr"].lstrip("0")}
    return res
data={f:analyse(f) for f in FAM}
json.dump(data,open("out/api-model.json","w"))
for f,d in data.items(): print(f,len(d),"methods;",sum(1 for v in d.values() if v["params"] or v["returns"]),"with types")
