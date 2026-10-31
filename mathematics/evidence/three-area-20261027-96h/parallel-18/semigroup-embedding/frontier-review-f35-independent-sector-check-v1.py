#!/usr/bin/env python3
"""Independent exact sector-block and selected endpoint checks.

Own strict table parser; Z[sqrt(2),i] tuples, integer arithmetic throughout.
The checked finite endpoints do not replace the general unitary proof.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import sys


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def parse(path):
    raw=Path(path).read_bytes()
    T={}
    pairs=set()
    for line in raw.decode('utf-8').splitlines():
        line=line.strip()
        if not line or line.startswith('#'): continue
        fields=line.split()
        require(len(fields) in (3,4),'bad source row')
        a,b=map(int,fields[:2])
        require(0<=a<6 and 0<=b<6 and (a,b) not in pairs,'source pair')
        pairs.add((a,b))
        for token in fields[2:]:
            require(len(token)==3 and token[0] in '+-s' and token[1:].isdigit(),'bad ket')
            c,d=int(token[1]),int(token[2])
            require(0<=c<6 and 0<=d<6 and (a,b,c,d) not in T,'source coordinate')
            T[a,b,c,d]=(0,1,0,0) if token[0]=='s' else ((1 if token[0]=='+' else -1),0,0,0)
    require(pairs==set(product(range(6),repeat=2)) and len(T)==60,'source coverage')
    return raw,T


def classify(T):
    blocks={}
    outside=[]
    for coords,value in T.items():
        active=tuple(i for i,x in enumerate(coords) if x in (1,2))
        if len(active)==0:
            require(value==(0,1,0,0),'P coefficient')
            outside.append(coords)
        else:
            require(len(active)==2 and value in ((1,0,0,0),(-1,0,0,0)),'E coefficient/type')
            spectators=tuple(coords[i] for i in range(4) if i not in active)
            key=(active,spectators)
            mat=blocks.setdefault(key,[0,0,0,0])
            index=2*(coords[active[0]]-1)+(coords[active[1]]-1)
            require(mat[index]==0,'block duplicate')
            mat[index]=value[0]
    require(len(outside)==12 and len(blocks)==24,'block count')
    shapes={'I':(1,0,0,1),'J':(0,1,-1,0),'X':(0,1,1,0),'Z':(1,0,0,-1)}
    pairs={pair:Counter() for pair in combinations(range(4),2)}
    for (pair,_),values in blocks.items():
        v=tuple(values)
        matches=[name for name,shape in shapes.items() if v==shape or v==tuple(-x for x in shape)]
        require(len(matches)==1,'block shape')
        require(sum(x!=0 for x in v)==2 and v[0]*v[3]-v[1]*v[2] in (-1,1),'block rank')
        pairs[pair][matches[0]]+=1
    require(all(count==Counter({'I':1,'J':1,'X':1,'Z':1}) for count in pairs.values()),
            'per-pair type coverage')
    return len(outside),blocks,pairs


def gmul(x,y):
    return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])


def transform(T,mat,scale):
    out={}
    for coords,v in T.items():
        active=tuple(i for i,x in enumerate(coords) if x in (1,2))
        if not active:
            out[coords]=(0,scale*scale,0,0)
            continue
        i,j=active
        for p,q in product(range(2),repeat=2):
            phase=gmul(mat[p][coords[i]-1],mat[q][coords[j]-1])
            new=list(coords); new[i]=p+1;new[j]=q+1;new=tuple(new)
            prev=out.get(new,(0,0,0,0))
            out[new]=(prev[0]+v[0]*phase[0],prev[1],prev[2]+v[0]*phase[1],prev[3])
    return {k:v for k,v in out.items() if any(v)}


def gram_product(x,y):
    a,b,c,d=x; e,f,g,h=y
    return (a*e+2*b*f+c*g+2*d*h, a*f+b*e+c*h+d*g,
            c*e+2*d*f-a*g-2*b*h, c*f+d*e-a*h-b*g)




def main(path):
    raw,T=parse(path)
    p,blocks,pairs=classify(T)
    # Original coefficients represented with common scale factor two.
    original={k:tuple(2*z for z in v) for k,v in T.items()}
    R=(((1,0),(1,0)),((-1,0),(1,0)))
    Q=(((1,0),(0,1)),((0,1),(1,0)))
    Rrat=(((3,0),(4,0)),((-4,0),(3,0)))
    real=transform(T,R,1)  # scale^2=2 for these sqrt(2)-normalized gates below
    complex_=transform(T,Q,1)
    # transform multiplies P by scale^2; for 45 degrees use common denominator 2.
    for v in (real,complex_):
        for k in list(v):
            if not any(z in (1,2) for z in k): v[k]=(0,2,0,0)
    rat=transform(T,Rrat,5)
    require(len(real)==60 and len(complex_)==60 and len(rat)==84,'endpoint support')
    # Exact unnormalized denominator: 72*4 for 45-degree endpoints.
    for V,den in ((real,288),(complex_,288),(rat,45000)):
        # scale convention: vectors are multiplied by 2 or 25 respectively.
        for pair in combinations(range(4),2):
            other=tuple(i for i in range(4) if i not in pair)
            rows={}
            for coords,val in V.items():
                r=tuple(coords[i] for i in pair); c=tuple(coords[i] for i in other)
                rows.setdefault(r,{})[c]=val
            for x,y in product(product(range(6),repeat=2),repeat=2):
                aa,bb=rows.get(x,{}),rows.get(y,{})
                total=[0,0,0,0]
                for k in aa.keys()&bb.keys():
                    p0=gram_product(aa[k],bb[k]);total=[a+b for a,b in zip(total,p0)]
                require(tuple(total)==((den//36,0,0,0) if x==y else (0,0,0,0)),('endpoint marginal',pair,x,y))
    originalset=set(T); rset=set(real); qset=set(complex_)
    require(len(originalset&rset)==36 and len(originalset&qset)==36 and len(rset&qset)==36,'endpoint intersections')
    require(all(real[k]==original[k] for k in originalset&rset),'real common coefficients')
    altered=dict(T)
    key=next(k for k,v in T.items() if v==(1,0,0,0))
    altered[key]=(-1,0,0,0)
    try:
        classify(altered)
    except ValueError as error:
        require(str(error)=='per-pair type coverage','mutation wrong failure')
    else:
        raise ValueError('mutation accepted')
    print('table_sha256=',sha256(raw).hexdigest(),sep='')
    print('P_terms=',p,' active_blocks=',len(blocks),' pair_types=6x(I,J,X,Z)',sep='')
    print('PASS all blocks rank2, per-pair types, exact 60/60 endpoints and 84 rational-angle support')
    print('PASS all six exact marginals for real/complex endpoints and rational-angle state')
    print('support_intersections: original-real=36 original-complex=36 real-complex=36')
    print('PASS all36 original-real common coefficients unchanged')
    print('CONTROL one-coefficient sign flip rejected: per-pair type coverage')
    print('LIMIT: these finite examples do not prove the universal U(2)^4 equality criterion')


if __name__=='__main__':
    require(len(sys.argv)==2,'usage: checker TABLE')
    main(sys.argv[1])
