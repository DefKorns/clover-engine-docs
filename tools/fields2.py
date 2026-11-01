import re,json,glob,sys
base=sys.argv[1]
idx={f["address"]:f["name"] for f in json.load(open(f"{base}/decompile-index.json"))["functions"]}
pat=re.compile(r'FUN_([0-9a-f]+)\((\w+),(\w+),(".*?"|&DAT_[0-9a-f]+),([^;]*?)\)')
res={}
for p in glob.glob(f"{base}/functions/*.c"):
    s=open(p,encoding="utf-8",errors="ignore").read()
    m=[x for x in pat.findall(s) if x[1]=="param_2" and x[2]=="param_3"]
    if len(m)>=2:
        a=re.search(r"(0x[0-9a-f]+)\.c$",p.replace("\\","/")).group(1)
        res[a]=[(k.strip('"'),o) for h,_,_,k,o in m]
json.dump(res,open(sys.argv[2],"w"))
print(len(res))
for a,v in sorted(res.items(),key=lambda x:int(x[0],16)): print(a,[k for k,o in v])
