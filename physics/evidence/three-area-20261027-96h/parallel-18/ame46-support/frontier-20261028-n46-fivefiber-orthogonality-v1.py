#!/usr/bin/env python3
"""Exact F2 rank/orthogonality controls for N46 with a five-valued fiber party."""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path


def graph(m,degrees):
    p=list(itertools.combinations(range(m),2))
    return [tuple(sum(1<<x for x in row) for row in R) for R in itertools.product(p,repeat=5)
      if tuple(sum(x in row for row in R) for x in range(m))==degrees]


def rank(rows):
    basis={}
    for v in rows:
        while v:
            k=v.bit_length()-1
            if k not in basis:basis[k]=v;break
            v^=basis[k]
    return len(basis)


def product_zero(U,V,m,n):
    return all(sum(bool(U[g]>>i&1) and bool(V[g]>>j&1) for g in range(5))%2==0 for i in range(m) for j in range(n))


def columns(U,m):return [sum((bool(U[g]>>i&1)<<g) for g in range(5)) for i in range(m)]


def duplicate_group(U):
    found=[(i,j) for i,j in itertools.combinations(range(5),2) if U[i]==U[j]]
    if len(found)!=1:raise ValueError('not a unique duplicate pair')
    return sum(1<<i for i in found[0])


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    X=graph(4,(2,2,2,4));Y=graph(4,(2,2,3,3));Z=graph(5,(2,2,2,2,2))
    rx=Counter(rank(g) for g in X);ry=Counter(rank(g) for g in Y);rz=Counter(rank(g) for g in Z)
    if (len(X),len(Y),len(Z),dict(rx),dict(ry),dict(rz))!=(180,310,2040,{3:180},{2:10,3:300},{3:600,4:1440}):raise ValueError('rank distribution')
    xx=sum(product_zero(u,v,4,4) for u in X for v in X);yy=sum(product_zero(u,v,4,4) for u in Y for v in Y)
    xy=sum(product_zero(u,v,4,4) for u in X for v in Y)
    if (xx,yy,xy)!=(0,0,180):raise ValueError('4x4 parity products')
    # For all potential rank(3,2) zero products, the 4-symbol incidence
    # must be constant on the size-2 and size-3 kernel components.
    z3=[u for u in Z if rank(u)==3];y2=[v for v in Y if rank(v)==2];matched=0
    for u,v in itertools.product(z3,y2):
        if not product_zero(u,v,5,4):continue
        p=duplicate_group(u);q=31^p
        if any(col not in (p,q) for col in columns(v,4)):raise ValueError('unaligned kernel partition')
        matched+=1
    if matched!=600:raise ValueError('five/four kernel matches')
    # A three-symbol incidence, each column nonempty and of weight <=4,
    # cannot supply two symbols on both complementary 2/3 groups.
    P=0b00011;Q=0b11100;choices=[P,Q,31];poss=0
    for c in itertools.product(choices,repeat=3):
        if any(x.bit_count()>4 for x in c):continue
        if all(sum(bool(x>>g&1) for x in c)==2 for g in range(5)):poss+=1
    if poss:raise ValueError('three-symbol kernel allocation unexpectedly exists')
    result={'graphs_X':len(X),'graphs_Y':len(Y),'graphs_size5':len(Z),
      'rank_X':dict(rx),'rank_Y':dict(ry),'rank_size5':dict(rz),
      'zero_products_XX':xx,'zero_products_YY':yy,'zero_products_XY':xy,
      'five_four_rank3_rank2_zero_products':matched,'misaligned_kernel_partitions':0,
      'three_symbol_kernel_allocations_max_degree4':poss,
      'scope':'Exact finite F2 controls; no-Hamming-one and AME consequences are written separately.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
