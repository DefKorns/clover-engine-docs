import sys,struct
def block(d):
    o=bytearray();i=0
    while i<len(d):
        t=d[i];i+=1;l=t>>4
        if l==15:
            while True:
                b=d[i];i+=1;l+=b
                if b!=255:break
        o+=d[i:i+l];i+=l
        if i>=len(d):break
        off=d[i]|d[i+1]<<8;i+=2;m=t&15
        if m==15:
            while True:
                b=d[i];i+=1;m+=b
                if b!=255:break
        m+=4
        for _ in range(m):o.append(o[-off])
    return bytes(o)
d=open(sys.argv[1],"rb").read()
print(len(d),d[:8].hex())
# try chunked: u32 size + block
out=b"";i=0;chunks=0
try:
    while i<len(d):
        n=struct.unpack_from("<I",d,i)[0];i+=4
        out+=block(d[i:i+n]);i+=n;chunks+=1
except Exception as e: print("err",e,i)
print(chunks,len(out),1280*720*4,1280*720*2)
open(sys.argv[2],"wb").write(out)
