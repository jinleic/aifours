"""Backward dependency trimming of already RUP-checked textual LRAT.

Keeps all input clauses, marks ancestors of the checked empty clause,
retains only needed additions and drops all deletions. Output MUST be
checked by check_lrat.py before it is used as evidence. Peak extra disk
is the uncompressed proof; memory is a byte per clause ID plus mmap.
"""
import argparse
import gzip
import hashlib
import json
import mmap
from pathlib import Path
import shutil
import time


def main():
    p=argparse.ArgumentParser()
    p.add_argument('cnf')
    p.add_argument('proof')
    p.add_argument('output')
    args=p.parse_args()
    nc=None
    for line in Path(args.cnf).read_text().splitlines():
        if line.startswith('p '): nc=int(line.split()[3]); break
    assert nc
    temp=Path(args.output+'.uncompressed.tmp')
    start=time.monotonic()
    with gzip.open(args.proof,'rb') as src,open(temp,'wb') as dst:
        shutil.copyfileobj(src,dst,length=1024*1024)
    with open(temp,'rb') as fh:
        mm=mmap.mmap(fh.fileno(),0,access=mmap.ACCESS_READ)
        end=len(mm)
        final=None
        while end:
            if mm[end-1:end]==b'\n': end-=1
            begin=mm.rfind(b'\n',0,end)+1
            line=mm[begin:end]
            fields=line.split()
            if len(fields)>2 and fields[1]==b'0':
                final=int(fields[0])
                break
            end=max(0,begin-1)
        assert final is not None
        needed=bytearray(final+1)
        needed[final]=1
        end=len(mm)
        total=kept=0
        while end:
            if mm[end-1:end]==b'\n': end-=1
            begin=mm.rfind(b'\n',0,end)+1
            space=mm.find(b' ',begin,end)
            assert space>begin
            cid=int(mm[begin:space])
            deletion=mm[space+1:space+2]==b'd'
            if not deletion:
                total+=1
                if cid<=final and needed[cid]:
                    vals=list(map(int,mm[space+1:end].split()))
                    cut=vals.index(0)
                    hints=vals[cut+1:]
                    assert hints[-1]==0 and all(x>0 for x in hints[:-1])
                    for dep in hints[:-1]:
                        assert dep<cid
                        if dep>nc: needed[dep]=1
                    kept+=1
            end=max(0,begin-1)
        with open(args.output,'wb') as raw:
            with gzip.GzipFile(filename='',fileobj=raw,mode='wb',mtime=0,compresslevel=6) as out:
                begin=0
                while begin<len(mm):
                    end=mm.find(b'\n',begin)
                    if end<0: end=len(mm)
                    space=mm.find(b' ',begin,end)
                    cid=int(mm[begin:space])
                    if mm[space+1:space+2]!=b'd' and cid<=final and needed[cid]:
                        out.write(mm[begin:end]+b'\n')
                    begin=end+1
        mm.close()
    temp.unlink()
    result={'input_proof':args.proof,'output_proof':args.output,'input_sha256':hashlib.sha256(Path(args.proof).read_bytes()).hexdigest(),'output_sha256':hashlib.sha256(Path(args.output).read_bytes()).hexdigest(),'initial_clauses':nc,'input_additions':total,'retained_additions':kept,'seconds':time.monotonic()-start,'status':'requires independent proof check before use'}
    Path(args.output+'.trim.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)


if __name__=='__main__': main()
