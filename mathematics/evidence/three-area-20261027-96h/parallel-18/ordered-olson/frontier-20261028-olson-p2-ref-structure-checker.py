#!/usr/bin/env python3
"""Independent audit of the o_pi=p+2 REF-failure structure data.

Part 1: recompute, by a 4-step sequential DP (not 4-subset enumeration), the
set of normalised length-(p+2) cyclic sequences with no zero alternating
quadruple, for p=3,5, and compare it with the producer list and with the
directly generated class {rotations of c,c,c,c+d,...,c+(p-1)d}.
Part 2: re-decide REF failure of each sampled projection with a RUN-LEVEL
dynamic programme implementing the exact piece criterion
  exists T of runs, |T| even <= 2p, alternating sum 0, o_T-e_T >= o_pi-p+2,
and check the even-run labels between consecutive c-runs.
"""
import argparse
import hashlib
import itertools
import json


def has_zero_quadruple(seq,p):
    states={(0,0)}
    for y in seq:
        new=set(states)
        for k,x in states:
            if k<4:new.add((k+1,(x+(y if k%2==0 else -y))%p))
        states=new
    return (4,0) in states


def class_members(p):
    out=set()
    for c in range(p):
        for d in range(1,p):
            base=[c,c,c]+[(c+k*d)%p for k in range(1,p)]
            for s in range(p+2):
                lin=base[s:]+base[:s]
                if lin[0]==0:out.add(tuple(lin))
    return out


def ref_by_runs(runs,p):
    lab=[l for l,_ in runs];odd=[L%2 for _,L in runs];o_pi=sum(odd)
    need=o_pi-p+2
    states={(0,0,0)}  # (|T| capped at 2p+1, alternating sum, exact score o_T-e_T)
    for l,o in zip(lab,odd):
        new=set(states)
        for size,x,score in states:
            if size>=2*p+1:continue
            sign=1 if size%2==0 else -1
            new.add((size+1,(x+sign*l)%p,score+(1 if o else -1)))
        states=new
    return any(size%2==0 and size<=2*p and x==0 and score>=need for size,x,score in states)


def check_structure(runs,p):
    n=len(runs);odd_idx=[i for i in range(n) if runs[i][1]%2]
    if len(odd_idx)!=p+2:raise ValueError('ODD_COUNT')
    m=len(odd_idx);labels=[runs[i][0] for i in odd_idx]
    for t in range(m):
        seq=labels[t:]+labels[:t]
        c=seq[0];d=(seq[3]-c)%p
        if d and seq[:3]==[c,c,c] and all(seq[3+k]==(c+(k+1)*d)%p for k in range(p-1)):
            i1,i2,i3=odd_idx[t],odd_idx[(t+1)%m],odd_idx[(t+2)%m]
            b1=[runs[(i1+k)%n][0] for k in range(1,(i2-i1)%n)]
            b2=[runs[(i2+k)%n][0] for k in range(1,(i3-i2)%n)]
            if not b1 or not b2:raise ValueError('MISSING_SEPARATOR')
            if any(x not in (c,(c+d)%p) for x in b1) or any(x not in (c,(c-d)%p) for x in b2):
                raise ValueError('F2_VIOLATION')
            return len(b1),len(b2)
    raise ValueError('F1_VIOLATION')


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('input');parser.add_argument('--output',required=True);args=parser.parse_args()
    with open(args.input,'rb') as src:raw=src.read()
    data=json.loads(raw);part1={};part2={}
    for p in (3,5):
        mine={tuple([0]+list(r)) for r in itertools.product(range(p),repeat=p+1) if not has_zero_quadruple([0]+list(r),p)}
        theirs={tuple(s) for s in data['part1'][str(p)]['sequences']}
        cls=class_members(p)
        if not (mine==theirs==cls):raise ValueError('PART1_MISMATCH p=%d'%p)
        part1[str(p)]=len(mine)
    for p,entry in data['part2'].items():
        p=int(p);profiles={}
        for runs in entry['ref_failing']:
            runs=[tuple(r) for r in runs]
            if sum(L for _,L in runs)!=3*p-2 or any(runs[i][0]==runs[(i+1)%len(runs)][0] for i in range(len(runs))):
                raise ValueError('PROJECTION_FORMAT')
            if ref_by_runs(runs,p):raise ValueError('REF_ACTUALLY_HOLDS')
            key=str(check_structure(runs,p));profiles[key]=profiles.get(key,0)+1
        part2[str(p)]={'ref_failing_checked':len(entry['ref_failing']),'separator_counts':profiles}
    # controls: (a) p=5, o_pi=7, odd labels 0,1,0,2,3,4,1 contain the zero quadruple 0,1,0,4 -> REF must hold;
    # (b) the dominant REF-failing pattern 0,[1],0,[4],0,1,2,3,4 (F=13) -> REF must fail.
    ctrl_a=[(0,1),(1,1),(0,1),(2,1),(3,1),(4,1),(1,1),(2,2),(3,2),(4,2)]
    ctrl_b=[(0,1),(1,2),(0,1),(4,2),(0,1),(1,1),(2,1),(3,1),(4,3)]
    if sum(L for _,L in ctrl_a)!=13 or sum(L for _,L in ctrl_b)!=13:raise ValueError('CONTROL_FORMAT')
    controls=['REF_DETECTED' if ref_by_runs(ctrl_a,5) else 'REF_MISSED',
              'REF_FAIL_CONFIRMED' if not ref_by_runs(ctrl_b,5) else 'REF_FAIL_MISSED']
    if controls!=['REF_DETECTED','REF_FAIL_CONFIRMED']:raise ValueError('CONTROL_FAILED')
    result={'result':'PASS_INDEPENDENT_P2_REF_STRUCTURE','input_sha256':hashlib.sha256(raw).hexdigest(),
            'part1_no_zero_quadruple_equals_class':part1,'part2':part2,'controls':controls}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
