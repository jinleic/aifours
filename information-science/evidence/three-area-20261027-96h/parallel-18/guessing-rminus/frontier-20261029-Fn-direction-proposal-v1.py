#!/usr/bin/env python3
"""Search ONE floating original profile for classical F_n cuts, proposal only.
Usage: script.py OUT POINT POINT_SHA [N_CAP=1024] [SECONDS=120]
A found integer row is universally defined by the written F_n family; its
value at this unverified numerical direction is NOT a global bound or law.
No old archive/checker or original-source partial witness is replayed.
"""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json,math,os,resource,subprocess,sys,time
import numpy as np
ROOT=Path(__file__).resolve().parent

def exact_row(A,B,C,D,Z,n):
    out={}
    def I(a,b,z,w):
        for mask,c in ((a|z,1),(b|z,1),(a|b|z,-1),(z,-1)):
            if mask:out[mask]=out.get(mask,0)+w*c
    I(A,B,C|Z,n+1);I(A,B,Z,-n);I(A,B,D|Z,n);I(C,D,Z,n)
    w=n*(n+1)//2;I(A,C,B|Z,w);I(B,C,A|Z,w)
    return [[m,c] for m,c in sorted(out.items()) if c]

def main():
    start=time.monotonic();out=ROOT/sys.argv[1]
    if out.exists():raise FileExistsError('EXCLUSIVE_OUTPUT_ALREADY_EXISTS')
    raw=(ROOT/sys.argv[2]).read_bytes()
    if sha256(raw).hexdigest()!=sys.argv[3]:raise ValueError('POINT_SHA')
    cap=int(sys.argv[4]) if len(sys.argv)>4 else 1024;limit=float(sys.argv[5]) if len(sys.argv)>5 else 120
    if not 1<=cap<=4096 or not 0<limit<=120:raise ValueError('BOUNDED_ARGUMENTS')
    d=json.loads(raw);values=d['final_columns_float'];hf=[0.0]+[float(values[repr(('o',m))]) for m in range(1,1024)];h=np.asarray(hf);hq=[Fraction(v) for v in hf]
    rep={'kind':'NUMERICAL_Fn_SEPARATION_DIRECTION_PROPOSAL_ONLY','clock_start':subprocess.check_output(['/bin/date'],text=True).rstrip('\n'),'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'point_sha256':sys.argv[3],'pid':os.getpid(),'pgid':os.getpgrp(),'order_cap':cap,'wall_limit_s':limit,'universal_family':'F_n=(n+1)I(A;B|C,Z)-n*(I(A;B|Z)-I(A;B|D,Z)-I(C;D|Z))+n(n+1)/2*(I(A;C|B,Z)+I(B;C|A,Z)) >=0','source_family_written_proof':'frontier-20261028-all-order-copy-obstruction-v1.md section1; read its addenda2 and1 first. Only the universal proof, not any old partial-witness feasibility claim, is relevant.','not_established':['Exact current-point feasibility','All-positive-order satisfaction','Exhaustive overlapping-substitution result','Global entropy bound','Any old bulk-archive replay or scientific adoption']}
    def I(a,b,z):return h[a|z]+h[b|z]-h[a|b|z]-h[z]
    candidates=[];visited=0;minimum=0.0;completed=False
    def test(A,B,C,D,Z,mode):
        nonlocal visited,minimum
        a=I(A,B,C|Z);delta=I(A,B,Z)-I(A,B,D|Z)-I(C,D,Z);dd=I(A,C,B|Z)+I(B,C,A|Z)
        # Choosing n by clipped nonnegative components is only a search rule.
        # Scores use the ORIGINAL unmodified floating a,delta,d.
        root=np.sqrt(2*np.maximum(a,0)/np.maximum(dd,1e-20));n1=np.clip(np.floor(np.minimum(root,cap)),1,cap).astype(np.int64);n2=np.minimum(n1+1,cap)
        s1=a+a/n1+(n1+1)*dd/2-delta;s2=a+a/n2+(n2+1)*dd/2-delta
        take=s2<s1;score=np.minimum(s1,s2);nn=np.where(take,n2,n1);visited+=len(A)
        if len(score):minimum=min(minimum,float(np.min(score)))
        ids=np.flatnonzero(score < -1e-7)
        if len(ids)>16:ids=ids[np.argsort(score[ids])[:16]]
        for j in ids:
            vals=[int(x[j]) for x in (A,B,C,D,Z,nn)];terms=exact_row(*vals);exact=sum((c*hq[m] for m,c in terms),Fraction())
            if not terms or exact>=0:continue
            scale=max(abs(c) for m,c in terms);normalized=float(exact)/scale
            if normalized>=-1e-9:continue
            candidates.append({'A':vals[0],'B':vals[1],'C':vals[2],'D':vals[3],'Z':vals[4],'n':vals[5],'mode':mode,'Fn_over_n_float':float(score[j]),'exact_value_at_BINARY_FLOAT_DIRECTION':str(exact),'coefficient_max_norm':scale,'normalized_direction_value_float':normalized,'integer_row_terms':terms})
    # New direction, not the old exact partial point. All disjoint roles with
    # nonempty A-D are visited modulo A/B swap unless a lead/deadline stops it.
    nlow=6**6;codes=np.arange(nlow,dtype=np.int64);low=[np.zeros(nlow,dtype=np.int64) for _ in range(5)];temp=codes.copy()
    for i in range(6):
        digit=temp%6;temp//=6
        for j in range(5):low[j]|=np.where(digit==j+1,1<<i,0)
    for code in range(6**4):
        if time.monotonic()-start>limit:break
        t=code;high=[0]*5
        for i in range(6,10):
            digit=t%6;t//=6
            if digit:high[digit-1]|=1<<i
        masks=[low[j]|high[j] for j in range(5)];ok=(masks[0]>0)&(masks[1]>0)&(masks[2]>0)&(masks[3]>0)&(masks[0]<masks[1])
        args=[x[ok] for x in masks]
        if len(args[0]):test(*args,'disjoint')
        if candidates:break
    else:completed=True
    disjoint_count=visited;overlap_count=0
    # Only if no disjoint lead, change representation to overlapping tuples.
    if not candidates and time.monotonic()-start<limit:
        rng=np.random.default_rng(20261029)
        for k in range(16):
            if time.monotonic()-start>limit:break
            Z=rng.integers(0,1024,65536,dtype=np.int64);free=1023^Z;roles=[rng.integers(0,1024,65536,dtype=np.int64)&free for _ in range(4)]
            A,B,C,D=roles;overlap=(A&B)|(A&C)|(A&D)|(B&C)|(B&D)|(C&D)
            ok=(A>0)&(B>0)&(C>0)&(D>0)&(A<B)&(overlap>0)
            args=[x[ok] for x in (A,B,C,D,Z)];before=visited
            if len(args[0]):test(*args,'overlapping_tuples')
            overlap_count+=visited-before
            if candidates:break
    rep.update(disjoint_substitutions_visited=disjoint_count,disjoint_scan_completed=completed,expected_complete_disjoint_count=13729980,overlapping_proposals_visited=overlap_count,random_seed=20261029,min_Fn_div_n_float=minimum,candidates=candidates,state='INTEGER_ROW_PROPOSALS_NEED_GLOBAL_REOPTIMIZATION_AND_PROOF_BINDING' if candidates else 'NO_CUT_FOUND_IN_EXPLORED_REGION_NOT_AN_IMPOSSIBILITY_RESULT',clock_finish=subprocess.check_output(['/bin/date'],text=True).rstrip('\n'),elapsed_s=time.monotonic()-start,peak_RSS_bytes_if_darwin=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform=='darwin' else None)
    with out.open('x') as f:json.dump(rep,f,indent=1);f.write('\n')
    print(json.dumps({k:v for k,v in rep.items() if k!='candidates'},indent=1),flush=True)
    for c in candidates:print({k:v for k,v in c.items() if k!='integer_row_terms'},flush=True)
if __name__=='__main__':main()
