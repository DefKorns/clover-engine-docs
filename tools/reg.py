import re,glob,json,struct,sys
n=sys.argv[1]; base=f"out/{n}"
d=open(f"{n}/ReedPlayer-Clover","rb").read()
phoff=struct.unpack_from("<I",d,28)[0]; phentsize,phnum=struct.unpack_from("<HH",d,42)
segs=[]
for i in range(phnum):
    t,off,va,pa,fs,ms,fl,al=struct.unpack_from("<8I",d,phoff+i*phentsize)
    if t==1: segs.append((va,off,fs))
def rd(va):
    for v,o,fs in segs:
        if v<=va<v+fs: return d[o+va-v:o+va-v+80].split(b"\0")[0].decode(errors="replace")
opener=re.compile(r'FUN_[0-9a-f]+\((\w+),param_1,"([A-Za-z_]\w*)"\);')
lam=re.compile(r'FUN_[0-9a-f]+\((\w+),param_1,(?:&LAB_|&FUN_|FUN_|&DAT_)?([0-9a-f]{6,8})(?:,\w+)?\);')
meth=re.compile(r'FUN_[0-9a-f]+\((\w+),(".*?"|&DAT_[0-9a-f]+),(\w+)\);')
rows=[]
for p in glob.glob(base+"/functions/*.c"):
    s=open(p,encoding="utf-8",errors="ignore").read()
    cur=None; pend={}
    for line in s.splitlines():
        m=opener.search(line)
        if m: cur=(m.group(1),m.group(2)); continue
        if not cur: continue
        m=lam.search(line)
        if m and m.group(1)!=cur[0]: pend[m.group(1)]=m.group(2); continue
        m=meth.search(line)
        if m and m.group(1)==cur[0] and m.group(3) in pend:
            name=m.group(2)
            name=(rd(int(name[5:],16)) or name) if name.startswith("&DAT_") else name.strip('"')
            rows.append((cur[1],name,pend[m.group(3)]))
json.dump(rows,open(f"out/{n}-reg.json","w"))
print(n,len(rows),"bindings with lambda;",len({r[2] for r in rows}),"distinct lambdas")
