import struct,json,bisect,hashlib,sys
from capstone import *
PRIM={"a12a0":"number","a1308":"number","a11a0":"integer","a1228":"integer","b9634":"boolean","a25dc":"string",
      "a09b8":"push:number","a0990":"push:integer","a056c":"push:boolean","a08a0":"push:string","a6294":"push:array"}
def load(n):
    d=open(f"{n}/ReedPlayer-Clover","rb").read()
    phoff=struct.unpack_from("<I",d,28)[0]; phentsize,phnum=struct.unpack_from("<HH",d,42)
    segs=[]
    for i in range(phnum):
        t,off,va,pa,fs,ms,fl,al=struct.unpack_from("<8I",d,phoff+i*phentsize)
        if t==1: segs.append((va,off,fs))
    idx=json.load(open(f"out/{n}/decompile-index.json"))["functions"]
    starts=sorted({int(f["address"],16) for f in idx if f["address"].startswith("0x")})
    return d,segs,starts
md=Cs(CS_ARCH_ARM,CS_MODE_ARM); md.skipdata=True
def fp(ctx,a):
    d,segs,starts=ctx
    i=bisect.bisect_right(starts,a); end=starts[i] if i<len(starts) else a+0x200
    code=None
    for v,o,fs in segs:
        if v<=a<v+fs: code=d[o+a-v:o+min(end-v,a-v+0x400)]; break
    if code is None: return None,0
    ms=[x.mnemonic for x in md.disasm(code,a)]
    return hashlib.sha1(" ".join(ms).encode()).hexdigest()[:12],len(ms)
if __name__=="__main__":
    ref=load("sneseur-2.0.14")
    fps={h:(k,fp(ref,int(h,16))) for h,k in PRIM.items()}
    for h,(k,(f,l)) in fps.items(): print(h,k,f,l)
    for n in ("nes-1.0.7","hvcj-shonen-3.0.1"):
        ctx=load(n); found={}
        for a in ctx[2]:
            f,l=fp(ctx,a)
            for h,(k,(rf,rl)) in fps.items():
                if f==rf and l==rl: found.setdefault(h,[]).append(hex(a))
        print(n,{k:v for k,v in found.items()}, "missing:",[h for h in fps if h not in found])
