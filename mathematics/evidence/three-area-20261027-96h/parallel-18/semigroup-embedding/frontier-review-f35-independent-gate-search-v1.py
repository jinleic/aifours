#!/usr/bin/env python3
"""Independent exact replay of the 30^4 four-party two-level gate alphabet.

Uses a separately written gate action and fiber-count formula.  It imports only
our own pinned table parser; no author's search code or receipt is used.
Ring elements are integer tuples for a+b*sqrt(2)+i(c+d*sqrt(2)).
"""
import importlib.util
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
PARSER=HERE/'frontier-review-f35-independent-sector-check-v1.py'
PIN='aa7105b8e868ba9a53507ba77f4fa93853423f1454634960db9ce8061fda6066'
if sha256(PARSER.read_bytes()).hexdigest()!=PIN:
    raise ValueError('reviewer parser pin mismatch')
spec=importlib.util.spec_from_file_location('review_parser',PARSER)
parser=importlib.util.module_from_spec(spec)
spec.loader.exec_module(parser)
ZERO=(0,0,0,0)
PAIRS=tuple(combinations(range(6),2))
GATES=tuple((p,q,z) for p,q in PAIRS for z in (0,1))


def plus(a,b):
    return (a[0]+b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3])


def neg(a):
    return (-a[0],-a[1],-a[2],-a[3])


def times_i(a):
    return (-a[2],-a[3],a[0],a[1])


def times_sqrt2(a):
    return (2*a[1],a[0],2*a[3],a[2])


def push(out,key,value):
    value=plus(out.get(key,ZERO),value)
    if value==ZERO:
        out.pop(key,None)
    else:
        out[key]=value


def gate(tensor,axis,p,q,z):
    # Common denominator sqrt(2) per party; untouched coordinates acquire sqrt2.
    out={}
    for coords,value in tensor.items():
        loc=coords[axis]
        if loc!=p and loc!=q:
            push(out,coords,times_sqrt2(value))
            continue
        ep=coords[:axis]+(p,)+coords[axis+1:]
        eq=coords[:axis]+(q,)+coords[axis+1:]
        if loc==p:
            push(out,ep,value)
            push(out,eq,neg(value) if z==0 else times_i(value))
        else:
            push(out,ep,value if z==0 else times_i(value))
            push(out,eq,value)
    return out


def final_supports(tensor):
    # Each last-axis fiber is affected separately.  Untouched coordinates
    # cannot change zero; add exact support changes only for each selected pair.
    fibers={}
    for (a,b,c,d),value in tensor.items():
        fibers.setdefault((a,b,c),{})[d]=value
    result={(p,q,z):len(tensor) for p,q,z in GATES}
    for fiber in fibers.values():
        for p,q in PAIRS:
            x,y=fiber.get(p,ZERO),fiber.get(q,ZERO)
            before=int(x!=ZERO)+int(y!=ZERO)
            if before==0:
                continue
            one=int(plus(x,y)!=ZERO)+int(plus(neg(x),y)!=ZERO)
            ii=int(plus(x,times_i(y))!=ZERO)+int(plus(times_i(x),y)!=ZERO)
            result[(p,q,0)]+=one-before
            result[(p,q,1)]+=ii-before
    return result


def main(table):
    raw,source=parser.parse(table)
    if sha256(raw).hexdigest()!='cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38':
        raise ValueError('source pin')
    hist=Counter()
    phase_min={key:None for key in product((0,1),repeat=4)}
    best=[]
    total=0
    for g0 in GATES:
        s0=gate(source,0,*g0)
        for g1 in GATES:
            s1=gate(s0,1,*g1)
            for g2 in GATES:
                s2=gate(s1,2,*g2)
                for g3,count in final_supports(s2).items():
                    hist[count]+=1
                    pattern=(g0[2],g1[2],g2[2],g3[2])
                    current=phase_min[pattern]
                    phase_min[pattern]=count if current is None else min(current,count)
                    if count<=60:
                        best.append((g0,g1,g2,g3,count))
                    total+=1
    if total!=810000 or min(hist)!=60 or hist[60]!=2:
        raise ValueError(('search summary',total,min(hist),hist[60]))
    if any(k<60 for k in hist):
        raise ValueError('sub60 gate found')
    print('exact_gate_combinations=',total,' support_min=',min(hist),' minimizer_count=',hist[60],sep='')
    print('best_gates=',best,sep='')
    print('phase_pattern_minima=',sorted(phase_min.items()),sep='')
    print('PASS independently enumerated full stated 15^4*2^4 alphabet over Z[sqrt2,i]')
    print('LIMIT: finite gate alphabet only, not all U(6)^4 or all AME tensors')


if __name__=='__main__':
    if len(sys.argv)!=2:
        raise ValueError('usage: checker TABLE')
    main(sys.argv[1])
