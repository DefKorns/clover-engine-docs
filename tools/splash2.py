import struct,json,sys,bisect
from capstone import *
n,unk,sf=sys.argv[1],int(sys.argv[2],16),int(sys.argv[3],16)
d=open(f"{n}/clover-mcp","rb").read()
phoff=struct.unpack_from("<I",d,28)[0]; phentsize,phnum=struct.unpack_from("<HH",d,42)
segs=[]
for i in range(phnum):
    t,off,va,pa,fs,ms,fl,al=struct.unpack_from("<8I",d,phoff+i*phentsize)
    if t==1 and fl&1: segs.append((va,off,fs))
mcp=f"out/{n}-mcp"
import os
funcs=[]
if os.path.exists(mcp+"/decompile-index.json"):
    funcs=sorted((int(f["address"],16),f["name"]) for f in json.load(open(mcp+"/decompile-index.json"))["functions"] if f["address"].startswith("0x"))
elif os.path.exists(f"out/sneseur-2.0.14-mcp/decompile-index.json"): pass
addrs=[a for a,_ in funcs]
def fname(a):
    i=bisect.bisect_right(addrs,a)-1; return funcs[i] if i>=0 else None
md=Cs(CS_ARCH_ARM,CS_MODE_ARM); md.skipdata=True
for va,off,fs in segs:
    ins=list(md.disasm(d[off:off+fs],va))
    for k,i in enumerate(ins):
        if i.mnemonic in ("add","ldr") and (i.op_str.split(", ")[-1].rstrip("]") in (f"#{hex(unk)}",f"#{hex(sf)}")):
            f=fname(i.address)
            print(hex(i.address),f[1] if f else "?",hex(f[0]) if f else "",i.op_str)
