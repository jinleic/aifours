#!/usr/bin/env python3
"""Production orchestrator. Compiled programs here are NEVER replay commands.

At most four scanner threads. A separate invocation performs cheap arithmetic
vectors, tiny proper-factor controls, a benchmark, or the unsieved published
control interval. A main run is authorized only after the controls have passed.
"""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import random
import subprocess
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def vectors():
    rng = random.Random(390215)
    tests = []
    for n in [2,8,24,90,512,134217728,297474474,200000000000,200000000024,
              1999999999976,2000000000000,10341223092224]:
        tests.append((n+1,n*n+n+1,'plane-form'))
    for bits in range(65,95):
        m=(1<<bits)-1
        for k in (1,3,(1<<31)+1):
            tests.append((bits*k,m,'large-positive'))
            tests.append((bits*k+1,m,'large-nonunit'))
    for i in range(512):
        n=rng.randrange(200000000000,2000000000000)
        tests.append((n+1,n*n+n+1,'production-size'))
    for i in range(256):
        bits=rng.randrange(3,96)
        modulus=rng.randrange(1<<(bits-1),1<<bits)|1
        tests.append((rng.randrange(1,1<<64),modulus,'generic'))
    rows=[]
    for e,p,kind in tests:
        got=[]
        for exe in ('scan128_digest','scan32'):
            result=subprocess.run(['code/'+exe,'power',str(e),str(p),'vector'],
                                  capture_output=True,text=True,timeout=5,check=True)
            got.append(int(result.stdout))
        expected=pow(2,e,p)
        assert got==[expected,expected], (e,p,got,expected)
        if kind=='large-positive':assert expected==1
        rows.append(dict(exponent=e,modulus=str(p),kind=kind,residue=str(expected),
                         radix64=str(got[0]),radix32=str(got[1])))
    out=dict(vectors=rows,positive_at_large_moduli=sum(r['kind']=='large-positive' for r in rows),
             binary_sha256={exe:sha('code/'+exe) for exe in ('scan128_digest','scan32')},
             limitation='Explicit arithmetic vectors only; no general-range or natural-hit certification.')
    Path('evidence/epoch2/vectors.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS',len(rows),'full residues, including',out['positive_at_large_moduli'],'large positive vectors')


def scan(exe,name,start,stop,step,bound,block,threads,cap,window_every=256,window_len=64):
    prefix='logs/e2-'+name+'-'+exe
    command=['code/'+exe,*map(str,(start,stop,step,bound,block,threads,cap)),prefix,
             str(window_every),str(window_len),name,sha('code/'+exe)]
    begin=time.monotonic()
    Path('evidence/epoch2/'+name+'-'+exe+'-started.json').write_text(json.dumps(dict(
        command=command,started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_sha256=sha('code/'+exe+'.c'),binary_sha256=sha('code/'+exe)),indent=2)+'\n')
    result=subprocess.run(command,capture_output=True,text=True,timeout=cap+120)
    out=dict(command=command,seconds=time.monotonic()-begin,returncode=result.returncode,
             stdout=result.stdout,stderr=result.stderr,
             source_sha256=sha('code/'+exe+'.c'),binary_sha256=sha('code/'+exe))
    Path('evidence/epoch2/'+name+'-'+exe+'-run.json').write_text(json.dumps(out,indent=2)+'\n')
    assert result.returncode==0, out
    print(exe,name,result.stdout.strip(),flush=True)
    return prefix


def compare(prefixes,expected=None,allow_partial=False):
    data=[]
    for prefix in prefixes:
        rows=[json.loads(s) for s in Path(prefix+'.blocks.jsonl').read_text().splitlines()]
        assert rows[0]['kind']=='header' and rows[-1]['kind']=='footer'
        b=sorted(rows[1:-1],key=lambda x:x['id'])
        assert all(x['id']==i for i,x in enumerate(b))
        if not allow_partial:assert rows[-1]['completed_plan'], 'control/benchmark did not complete'
        data.append(b)
    keys=['id','index','start','end','count','sieved','tested','hits','survivors','decision_sha256']
    common=min(map(len,data));assert common>0
    assert [{k:b[k] for k in keys} for b in data[0][:common]]==[
        {k:b[k] for k in keys} for b in data[1][:common]], 'full decision/residue digests differ'
    hits=[n for b in data[0][:common] for n in b['survivors']]
    if expected is not None:assert hits==expected, hits
    return dict(blocks=common,count=sum(b['count'] for b in data[0][:common]),
                hits=hits,end=data[0][common-1]['end'],
                comparison='all 32-byte decision records via SHA-256; proper-factor records have an explicitly uncomputed residue')


def main():
    parser=argparse.ArgumentParser();parser.add_argument('task',choices=['vectors','tiny','benchmark','controls','main','extension'])
    parser.add_argument('--cap',type=int,default=7200)
    args=parser.parse_args()
    if args.task=='vectors':vectors();return
    if args.task=='tiny':spec=(2,20000,2,1000000,10000,2,60,1,10000);expected=[2,8,24,90,512,134217728,297474474][:5]
    elif args.task=='benchmark':spec=(200000000000,200000000000+24*8388608*8,24,1000000,8388608,2,120,1,64);expected=[]
    elif args.task=='controls':spec=(2,5000000000,2,0,8388608,2,3600,256,64);expected=[2,8,24,90,512,134217728,297474474]
    elif args.task=='main':
        prior=json.loads(Path('evidence/epoch2/controls-comparison.json').read_text())
        assert prior['hits']==[2,8,24,90,512,134217728,297474474]
        spec=(200000000000,2000000000000,24,1000000,8388608,2,args.cap,128,64);expected=[]
    else:
        prior=json.loads(Path('evidence/epoch2/main-comparison.json').read_text())
        assert prior['end']==2000000000000 and prior['hits']==[]
        spec=(2000000000000,4000000000000,24,1000000,8388608,1,args.cap,128,64);expected=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        futures=[pool.submit(scan,exe,args.task,*spec) for exe in ('scan128_digest','scan32')]
        prefixes=[f.result() for f in futures]
    result=compare(prefixes,expected,allow_partial=args.task=='extension')
    Path('evidence/epoch2/'+args.task+'-comparison.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
