import re,json,struct,sys,bisect,collections
from capstone import *
n=sys.argv[1]
d=open(f"{n}/ReedPlayer-Clover","rb").read()
phoff=struct.unpack_from("<I",d,28)[0]; phentsize,phnum=struct.unpack_from("<HH",d,42)
segs=[]
for i in range(phnum):
    t,off,va,pa,fs,ms,fl,al=struct.unpack_from("<8I",d,phoff+i*phentsize)
    if t==1: segs.append((va,off,fs,fl))
def rd(va,nb):
    for v,o,fs,fl in segs:
        if v<=va<v+fs: return d[o+va-v:o+va-v+nb]
reg=json.load(open(f"out/{n}-reg.json"))
idx=json.load(open(f"out/{n}/decompile-index.json"))["functions"]
starts=sorted({int(f["address"],16) for f in idx if f["address"].startswith("0x")}|{int(a,16) for _,_,a in reg})
md=Cs(CS_ARCH_ARM,CS_MODE_ARM); md.skipdata=True
def body(a):
    i=bisect.bisect_right(starts,a)
    end=starts[i] if i<len(starts) else a+0x400
    return list(md.disasm(rd(a,min(end-a,0x1200)),a))
num=lambda s:int(s.lstrip("#"),16) if s.lstrip("#").startswith("0x") else int(s.lstrip("#"))
out={}
for c,m,a in reg:
    ad=int(a,16); ins=body(ad)
    expected=None; calls=[]; r1=None; ret=None
    for k,i in enumerate(ins):
        if i.mnemonic=="asr" and i.op_str.endswith("#3"):
            for j in ins[k+1:k+3]:
                if j.mnemonic=="cmp" and "#" in j.op_str: expected=num(j.op_str.split("#")[1]); break
        if i.mnemonic=="mov" and i.op_str.startswith("r1, #"): r1=num(i.op_str.split("#")[1])
        if i.mnemonic in("bl","b") and i.op_str.startswith("#0x"):
            calls.append((int(i.op_str[1:],16),r1)); r1=None if i.mnemonic=="bl" else r1
        if i.mnemonic=="mov" and i.op_str.startswith("r0, #") and k+3<len(ins):
            nxt=[x.mnemonic for x in ins[k+1:k+4]]
            if "pop" in nxt or "bx" in nxt: ret=num(i.op_str.split("#")[1])
    out[f"{c}.{m}"]={"class":c,"method":m,"addr":a,"expected":expected,"calls":calls,"ret":ret}
json.dump(out,open(f"out/{n}-sig.json","w"))
print(n,len(out),"analysed; with expected:",sum(1 for v in out.values() if v["expected"] is not None))
