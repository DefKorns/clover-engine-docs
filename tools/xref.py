import struct,sys,re
from capstone import *
n,text=sys.argv[1],("\n  FATAL ERROR: "+sys.argv[2]).encode()
d=open(f"{n}/clover-mcp","rb").read()
phoff=struct.unpack_from("<I",d,28)[0]; phentsize,phnum=struct.unpack_from("<HH",d,42)
segs=[]
for i in range(phnum):
    t,off,va,pa,fs,ms,fl,al=struct.unpack_from("<8I",d,phoff+i*phentsize)
    if t==1: segs.append((va,off,fs,fl))
def f2v(o):
    for va,off,fs,fl in segs:
        if off<=o<off+fs: return va+o-off
target=f2v(d.find(text))
print("string at",hex(target))
md=Cs(CS_ARCH_ARM,CS_MODE_ARM); md.skipdata=True
num=lambda s:int(s,16) if s.startswith("0x") else int(s)
for va,off,fs,fl in segs:
    if not fl&1: continue
    ins=list(md.disasm(d[off:off+fs],va))
    for k,i in enumerate(ins):
        if i.mnemonic=="movw":
            r,imm=i.op_str.split(", #"); lo=num(imm)
            for j in ins[k+1:k+4]:
                if j.mnemonic=="movt" and j.op_str.startswith(r+","):
                    hi=num(j.op_str.split("#")[1])
                    if (hi<<16|lo)==target:
                        print("xref at",hex(i.address))
                        for q in ins[k:k+int(sys.argv[3])]: print("  ",hex(q.address),q.mnemonic,q.op_str)
