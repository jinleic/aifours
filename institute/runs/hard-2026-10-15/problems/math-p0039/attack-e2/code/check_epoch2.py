#!/usr/bin/env python3
"""Python-only replay of the new evidence; no production code is imported.

Structural metadata and agreement of preserved hashes are distinguished from
reexecution. --blocks explicitly selects the only blocks reexecuted in full.
Full replay builds its own Eratosthenes sieve and uses Cipolla's algorithm to
derive root classes (neither scanner is imported). Ordinary modular powers use Python
integers, with built-in pow or a separate right-to-left loop. These two Python
control flows share CPython's underlying big-integer arithmetic.
"""
import argparse
import gzip
import hashlib
import json
from math import isqrt
from pathlib import Path
import struct
import sys
import time


def need(ok,message):
    if not ok:raise ValueError(message)


def load_run(prefix,allow_running=False):
    lines=Path(prefix+'.blocks.jsonl').read_text().splitlines(keepends=True)
    rows=[json.loads(x) for x in lines if x.endswith('\n')]
    need(rows and rows[0]['kind']=='header','missing header')
    h=rows[0];f=rows[-1] if rows[-1]['kind']=='footer' else None
    need(f is not None or allow_running,'missing completion footer')
    observed=rows[1:-1] if f is not None else rows[1:]
    need(all(b['kind']=='block' for b in observed),'unexpected live record')
    by_id={b['id']:b for b in observed};need(len(by_id)==len(observed),'duplicate block')
    if f is None:
        # Observe a real complete prefix only; no synthetic footer is created.
        blocks=[];i=0
        while i in by_id:blocks.append(by_id[i]);i+=1
    else:blocks=sorted(observed,key=lambda b:b['id'])
    a,z,step=h['start'],h['stop'],h['step'];size=h['block_size']
    need(2<=a<z and step>0 and 0<size<=67108864 and 0<=h['sieve_bound']<=1000000,'header bounds')
    count=len(range(a,z,step));planned=(count+size-1)//size
    need(h['total']==count and h['blocks']==planned,'header arithmetic')
    if f is not None:
        need(f['assigned_blocks']==len(blocks) and f['planned_blocks']==planned,'footer count')
        need(f['completed_plan']==(len(blocks)==planned),'footer completion')
    need(len(h['binary_sha256'])==64,'binary hash missing')
    cursor=a
    for i,b in enumerate(blocks):
        length=min(size,count-i*size)
        need(b['kind']=='block' and b['id']==i and b['index']==i*size,'block gap/id')
        need(b['start']==cursor==a+step*i*size,'block start')
        need(b['count']==length and b['end']==cursor+step*length,'block endpoint/count')
        need(b['sieved']+b['tested']==length and min(b['sieved'],b['tested'])>=0,'count bookkeeping')
        need(len(b['decision_sha256'])==64,'missing decision hash')
        need(b['survivors']==sorted(set(b['survivors'])) and b['hits']==len(b['survivors']),'hit count')
        need(0<=b['hits']<=b['tested'],'impossible hit count')
        if h['sieve_bound']==0:need(b['sieved']==0,'control must be unsieved')
        for n in b['survivors']:
            need(cursor<=n<b['end'] and (n-a)%step==0,'hit outside block')
            need(pow(2,n+1,n*n+n+1)==1,'false logged hit')
        cursor=b['end']
    return h,blocks,f


def expected_header(task,h):
    expected={
        'tiny':(2,20000,2,1000000,10000),
        'benchmark':(200000000000,201610612736,24,1000000,8388608),
        'controls':(2,5000000000,2,0,8388608),
        'main':(200000000000,2000000000000,24,1000000,8388608),
        'extension':(2000000000000,4000000000000,24,1000000,8388608)}
    need(tuple(h[k] for k in ('start','stop','step','sieve_bound','block_size'))==expected[task],
         'header differs from fixed task scope')


def compare(task,broken=False):
    prefixes=['logs/e2-'+task+'-'+s for s in ('scan128_digest','scan32')]
    a,b=[load_run(p) for p in prefixes]
    for h,_,f in (a,b):
        expected_header(task,h)
        if task!='extension':need(f['completed_plan'],'fixed planned interval incomplete')
    keys=('id','index','start','end','count','sieved','tested','hits','survivors','decision_sha256')
    common=min(len(a[1]),len(b[1]))
    need(common>0,'no common blocks')
    for i in range(common):
        one={k:a[1][i][k] for k in keys};two={k:b[1][i][k] for k in keys}
        if broken and i==0:two['decision_sha256']='0'*64
        need(one==two,'different full decision stream digest at block '+str(i))
    if task in ('benchmark','main','extension'):
        need(not [n for block in a[1][:common] for n in block['survivors']],
             'unresolved base-two survivor prevents interval exclusion')
    for prefix,(h,blocks,f) in zip(prefixes,(a,b)):
        exe=prefix.split('-')[-1]
        need(hashlib.sha256(Path('code/'+exe).read_bytes()).hexdigest()==h['binary_sha256'],'binary hash mismatch')
        record=json.loads(Path('evidence/epoch2/'+task+'-'+exe+'-run.json').read_text())
        need(record['returncode']==0 and record['binary_sha256']==h['binary_sha256'],'run provenance')
        need(record['source_sha256']==hashlib.sha256(Path('code/'+exe+'.c').read_bytes()).hexdigest(),'source hash mismatch')
    if task=='controls':
        expected=[2,8,24,90,512,134217728,297474474]
        for h,blocks,f in (a,b):
            need((h['start'],h['stop'],h['step'],h['sieve_bound'])==(2,5000000000,2,0),'control interval')
            need(f['completed_plan'],'full control interval incomplete')
            need([n for x in blocks for n in x['survivors']]==expected,'published control list')
    return dict(task=task,common_blocks=common,common_start=a[1][0]['start'],
                common_end=a[1][common-1]['end'],common_members=sum(x['count'] for x in a[1][:common]),
                common_sieved=sum(x['sieved'] for x in a[1][:common]),common_tested=sum(x['tested'] for x in a[1][:common]),
                logged_survivors=[n for x in a[1][:common] for n in x['survivors']],
                limitation='Preserved execution/hash agreement and bookkeeping only; no full arithmetic replay in this task. Factor records hash residue=0 (not computed); every unsieved full ordinary residue is hashed.')


def primes_to(bound):
    flags=bytearray(b'\1')*(bound+1)
    if bound>=1:flags[0]=flags[1]=0
    for q in range(2,isqrt(bound)+1):
        if flags[q]:flags[q*q::q]=b'\0'*((bound-q*q)//q+1)
    return [q for q in range(2,bound+1) if flags[q]]


def cipolla(value,q):
    value%=q
    if q%4==3:return pow(value,(q+1)//4,q)
    t=0
    while True:
        w=(t*t-value)%q
        if pow(w,(q-1)//2,q)==q-1:break
        t+=1
    # Exponentiation in F_q[u]/(u^2-w); this differs from both C root methods.
    re,im=1,0;base_re,base_im=t,1;e=(q+1)//2
    while e:
        if e&1:
            re,im=(re*base_re+im*base_im*w)%q,(re*base_im+im*base_re)%q
        base_re,base_im=(base_re*base_re+base_im*base_im*w)%q,2*base_re*base_im%q
        e>>=1
    need(im==0 and re*re%q==value,'Cipolla root failure')
    return re


def root_classes(h,primes):
    start,step=h['start'],h['step'];rows=[]
    for q in primes:
        if q!=3 and q%3!=1:continue
        if q==3:roots=[1]
        else:
            r=cipolla(q-3,q);half=(q+1)//2
            roots=[(-1+r)*half%q,(-1-r)*half%q]
        need(all((r*r+r+1)%q==0 for r in roots),'bad Python root')
        if step%q==0:
            if start%q in roots:rows.append((q,(0,),1))
        else:
            inv=pow(step,-1,q)
            rows.append((q,tuple(sorted({(r-start)*inv%q for r in roots})),q))
    return rows


def mark(h,b,classes):
    import numpy as np
    length=b['count'];a=np.zeros(length,dtype='<u4')
    for q,roots,jump in reversed(classes):
        for root in roots:
            first=(root-b['index'])%jump
            if h['start']*h['start']+h['start']+1>h['sieve_bound']:
                a[first::jump]=q
            else:
                for j in range(first,length,jump):
                    n=b['start']+j*h['step']
                    if 1<q<n*n+n+1:a[j]=q
    return a


def manual(e,p):
    r,a=1,2
    while e:
        if e&1:r=r*a%p
        e>>=1
        if e:a=a*a%p
    return r


def replay_blocks(task,ids,backend,broken=False):
    import numpy as np
    h,blocks,_=load_run('logs/e2-'+task+'-scan32',allow_running=True)
    h2,other,_=load_run('logs/e2-'+task+'-scan128_digest',allow_running=True)
    expected_header(task,h);expected_header(task,h2)
    need(ids and min(ids)>=0 and max(ids)<min(len(blocks),len(other)),'requested block is not completed')
    primes=primes_to(h['sieve_bound']);classes=root_classes(h,primes)
    total=0;out=[];all_hits=[]
    dtype=np.dtype([('n','<u8'),('q','<u4'),('tag','<u4'),('lo','<u8'),('hi','<u8')],align=False)
    need(dtype.itemsize==32,'record width')
    for block_id in ids:
        b=blocks[block_id];length=b['count'];q=mark(h,b,classes)
        record=np.zeros(length,dtype=dtype)
        record['n']=np.arange(length,dtype='<u8')*h['step']+b['start']
        record['q']=q;record['tag']=np.where(q!=0,1,2)
        zero=np.flatnonzero(q==0);hits=[]
        for j0 in zero:
            j=int(j0);n=b['start']+j*h['step'];p=n*n+n+1
            residue=pow(2,n+1,p) if backend=='pow' else manual(n+1,p)
            record['lo'][j]=residue&((1<<64)-1);record['hi'][j]=residue>>64
            if residue==1:record['tag'][j]=3;hits.append(n)
        expected=b['decision_sha256']
        if broken:expected='0'*64
        digest=hashlib.sha256(memoryview(record)).hexdigest()
        need(digest==expected==other[block_id]['decision_sha256'],'full block digest mismatch '+str(block_id))
        need(len(zero)==b['tested'] and length-len(zero)==b['sieved'],'full block decision counts')
        need(hits==b['survivors'],'full block hits')
        if task in ('benchmark','main','extension'):
            need(not hits,'unresolved base-two survivor prevents interval exclusion')
        all_hits.extend(hits)
        total+=length;out.append(dict(block=block_id,start=b['start'],end=b['end'],count=length,sha256=digest))
        del record,q,zero
    return dict(task=task,backend=backend,fully_recomputed_members=total,blocks=out,
                base_two_survivors=all_hits,
                method='Python arbitrary precision with independent root derivation. Complete residue for EVERY unsieved member, exact proper-factor classes for all other members. No producer imports or binary execution.')


def samples(task,broken=False):
    h,blocks,_=load_run('logs/e2-'+task+'-scan32')
    expected_header(task,h)
    h2,other,_=load_run('logs/e2-'+task+'-scan128_digest')
    expected_header(task,h2)
    common_blocks=min(len(blocks),len(other));need(common_blocks>0,'no common sample blocks')
    blocks=blocks[:common_blocks]
    common_count=blocks[-1]['index']+blocks[-1]['count']
    streams=[]
    for exe in ('scan32','scan128_digest'):
        path=Path('logs/e2-'+task+'-'+exe+'.records.jsonl')
        if Path(str(path)+'.gz').is_file():
            with gzip.open(str(path)+'.gz','rt') as source:rows=[json.loads(x) for x in source]
        else:
            rows=[json.loads(x) for x in path.read_text().splitlines()]
        selected=[r for r in rows if r['index']<common_count]
        streams.append({r['index']:r for r in selected})
        need(len(streams[-1])==len(selected),'duplicate sample')
    common=sorted(set(streams[0])&set(streams[1]));need(common,'no samples')
    primes=primes_to(h['sieve_bound']);digest=hashlib.sha256();counts=[0,0]
    window_hashes={};window_counts={}
    expected=set()
    for b in blocks:
        length=b['count'];base=b['index']
        expected.update(base+j for j in (0,1,length-2,length-1) if 0<=j<length)
        if h['window_every'] and (b['id']%h['window_every']==0 or b['id']+1==h['blocks']):
            expected.update(range(base,base+min(length,h['window_len'])))
        expected.update((n-h['start'])//h['step'] for n in b['survivors'])
    need(set(streams[0])==set(streams[1])==expected,'sample coverage differs')
    for index in common:
        a=streams[0][index];b=streams[1][index]
        need(a==b,'sample streams differ')
        n=h['start']+index*h['step'];p=n*n+n+1
        need(a['n']==n and int(a['p'])==p,'sample modulus/index')
        block=blocks[index//h['block_size']];local=index-block['index']
        window=bool(h['window_every'] and
                    (block['id']%h['window_every']==0 or block['id']+1==h['blocks'])
                    and local<h['window_len'])
        edge=local<2 or local+2>=block['count']
        need(a['block']==block['id'] and a['window']==window and a['edge']==edge,'sample selection flags')
        q=0
        for divisor in primes:
            if divisor*divisor>p:break
            if p%divisor==0:q=divisor;break
        need(a['factor']==q and (q==0 or 1<q<p),'sample actual smallest proper factor')
        residue=pow(2,n+1,p)
        if broken and index==common[0]:residue=0
        need(int(a['residue'])==residue,'sample full ordinary residue')
        need(a['decision']==('factor' if q else ('survivor' if residue==1 else 'base2-fail')),'sample decision')
        canonical=('%d\t%s\t%d\t%d\n'%(n,a['decision'],q,residue)).encode()
        digest.update(canonical)
        if window:
            number=block['id']
            if number not in window_hashes:window_hashes[number]=hashlib.sha256();window_counts[number]=0
            window_hashes[number].update(canonical);window_counts[number]+=1
        counts[q==0]+=1
    windows=[]
    for number in sorted(window_hashes):
        block=blocks[number];length=min(block['count'],h['window_len'])
        need(window_counts[number]==length,'incomplete arithmetic window')
        windows.append(dict(block=number,start=block['start'],end=block['start']+length*h['step'],count=length,
                            sha256_every_n_decision_factor_full_residue=window_hashes[number].hexdigest()))
    return dict(task=task,arithmetic_records=len(common),factor_records=counts[0],unsieved_records=counts[1],
                all_samples_sha256=digest.hexdigest(),contiguous_windows=windows,
                limitation='Only these samples received Python arithmetic checking; no full-range certification.')


def vectors(broken=False):
    data=json.loads(Path('evidence/epoch2/vectors.json').read_text());positive=0
    for i,row in enumerate(data['vectors']):
        e=row['exponent'];p=int(row['modulus']);r=manual(e,p)
        expected=int(row['residue'])
        if broken and i==0:expected+=1
        need(r==expected==int(row['radix32'])==int(row['radix64']),'vector full residue mismatch')
        if row['kind']=='large-positive':need(r==1 and p.bit_length()>=65,'large positive vector');positive+=1
    need(positive==data['positive_at_large_moduli']==90,'large positive count')
    return dict(vectors=len(data['vectors']),large_positives=positive,
                limitation='Finite arithmetic vectors only; synthetic positive moduli need not be n^2+n+1.')


def main():
    p=argparse.ArgumentParser();p.add_argument('action',choices=['compare','blocks','samples','vectors'])
    p.add_argument('--task',default='main',choices=['tiny','benchmark','controls','main','extension'])
    p.add_argument('--blocks',default='0');p.add_argument('--backend',choices=['pow','manual'],default='pow')
    p.add_argument('--broken',action='store_true');p.add_argument('--output')
    args=p.parse_args();begin=time.monotonic()
    if args.action=='compare':result=compare(args.task,args.broken)
    elif args.action=='samples':result=samples(args.task,args.broken)
    elif args.action=='vectors':result=vectors(args.broken)
    else:result=replay_blocks(args.task,list(map(int,args.blocks.split(','))),args.backend,args.broken)
    result['seconds']=time.monotonic()-begin
    text=json.dumps(result,indent=2)+'\n'
    if args.output:Path(args.output).write_text(text)
    print(text,end='')


if __name__=='__main__':
    try:main()
    except (ValueError,AssertionError,KeyError,IndexError) as e:
        print('CHECK FAILED: '+str(e),file=sys.stderr);sys.exit(1)
