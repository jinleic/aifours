#!/usr/bin/env python3
"""Exact normalized N46/(4,4,4,4) support enumeration with no Hamming-one.

The written packet supplies the complete normal form and group reductions.
This implementation generates six-point fibers as balanced cube subsets.
"""
import argparse
from collections import Counter,defaultdict
import itertools
import json
from pathlib import Path

CUTS=((0,1),(0,2),(0,3));PAIR3=((0,1),(0,2),(1,2))


def pair_graphs(rowsizes,coldegrees):
    choices=[list(itertools.combinations(range(4),r)) for r in rowsizes]
    return [tuple(tuple(x) for x in R) for R in itertools.product(*choices)
            if tuple(sum(x in row for row in R) for x in range(4))==coldegrees]


def canonical_yy(G):
    out=[]
    for a in range(4):
      rp=list(range(4))
      if a&1:rp[0],rp[1]=rp[1],rp[0]
      if a&2:rp[2],rp[3]=rp[3],rp[2]
      for b in range(4):
        cp=list(range(4))
        if b&1:cp[0],cp[1]=cp[1],cp[0]
        if b&2:cp[2],cp[3]=cp[3],cp[2]
        out.append(tuple(tuple(sorted(cp[x] for x in G[rp[i]])) for i in range(4)))
    return min(out)


def canonical_xy(G):
    out=[]
    for low in itertools.permutations(range(3)):
      for b in range(4):
        cp=list(range(4))
        if b&1:cp[0],cp[1]=cp[1],cp[0]
        if b&2:cp[2],cp[3]=cp[3],cp[2]
        out.append(tuple(tuple(sorted(cp[x] for x in G[i])) for i in (*low,3)))
    return min(out)


def rect(U,V):return sum(1<<(4*a+b) for a in U for b in V)

def sig(F):return tuple(sum(1<<(4*q[i]+q[j]) for q in F) for i,j in PAIR3)


def six_fibers():
    cube=list(itertools.product(range(3),repeat=3));out=[]
    for F in itertools.combinations(cube,6):
        if not all(sum(q[i]==v for q in F)==2 for i in range(3) for v in range(3)):continue
        if not all(len({(q[i],q[j]) for q in F})==6 for i,j in PAIR3):continue
        out.append(F)
    if len(out)!=144 or len({sig(F) for F in out})!=144:raise ValueError('six-fiber catalog mismatch')
    return out


def parity_fiber(alph,sign):
    return tuple(tuple(alph[j][q[j]] for j in range(3)) for q in itertools.product(range(2),repeat=3) if q[0]^q[1]^q[2]==sign)


def no_overlap_witness(S,A):
    B=tuple(i for i in range(4) if i not in A);rows=defaultdict(set);cols=defaultdict(set)
    for q in S:r=tuple(q[i] for i in A);c=tuple(q[i] for i in B);rows[r].add(c);cols[c].add(r)
    for side,M in (('rows',rows),('columns',cols)):
        for x,y in itertools.combinations(sorted(M),2):
            common=M[x]&M[y]
            if len(common)==1:return {'side':side,'lines':[x,y],'shared':next(iter(common))}
    return None


def check_support(S):
    if len(S)!=20:raise ValueError('wrong E size')
    for i,j in itertools.combinations(range(4),2):
        C=Counter((q[i],q[j]) for q in S)
        if len(C)!=10 or set(C.values())!={2}:raise ValueError('bad E pair projection')


def reg2(M):
    return M.bit_count()==8 and all(sum(bool(M>>(4*i+j)&1) for j in range(4))==2 for i in range(4)) and all(sum(bool(M>>(4*i+j)&1) for i in range(4))==2 for j in range(4))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    Gyy=pair_graphs((2,2,3,3),(2,2,3,3));Gyrep=sorted({canonical_yy(g) for g in Gyy})
    Gxy=pair_graphs((2,2,2,4),(2,2,3,3));Gxrep=sorted({canonical_xy(g) for g in Gxy})
    if (len(Gyy),len(Gyrep),len(Gxy),len(Gxrep))!=(34,5,15,2):raise ValueError('incidence graph normal forms')
    F6=six_fibers();mapped={}
    for alph in itertools.product(itertools.combinations(range(4),3),repeat=3):
        T=defaultdict(list)
        for F in F6:
            pts=tuple(tuple(alph[j][q[j]] for j in range(3)) for q in F);T[sig(pts)].append(pts)
        if len(T)!=144 or any(len(v)!=1 for v in T.values()):raise ValueError('mapped signature collision')
        mapped[alph]=T
    yy=Counter();yy_examples=[]
    for B in Gyrep:
      for ic,C in enumerate(Gyy):
       for D in Gyy[ic:]:
        yy['incidence_patterns']+=1
        L=[tuple(rect(*p) for p in ((B[g],C[g]),(B[g],D[g]),(C[g],D[g]))) for g in (0,1)]
        T2=mapped[(B[2],C[2],D[2])];T3=mapped[(B[3],C[3],D[3])]
        for H2,sets2 in T2.items():
            req=tuple(H2[z]^L[0][z]^L[1][z] for z in range(3))
            for F2,F3 in itertools.product(sets2,T3.get(req,())):
                if any(L[0][z]&L[1][z]&H2[z]&req[z] for z in range(3)):continue
                yy['high_fiber_signature_pairs']+=1
                for s0,s1 in itertools.product((0,1),repeat=2):
                    Fs=(parity_fiber((B[0],C[0],D[0]),s0),parity_fiber((B[1],C[1],D[1]),s1),F2,F3)
                    S={(g,)+q for g,F in enumerate(Fs) for q in F};check_support(S)
                    if any(sum(x!=y for x,y in zip(a,b))==1 for a,b in itertools.combinations(S,2)):
                        yy['cross_fiber_distance_one_superset']+=1
                    witnesses=[no_overlap_witness(S,c) for c in CUTS];yy['supports_checked']+=1
                    if any(x is None for x in witnesses):raise ValueError('YY support without all three overlap witnesses')
                    yy['all_three_cuts_unique_overlap']+=1
                    yy_examples.append({'B':B,'C':C,'D':D,'support':sorted(S),'overlaps':witnesses})
    xx=Counter();xx_examples=[]
    for B in Gxrep:
      for ic,C in enumerate(Gxy):
       for D in Gxy[ic:]:
        xx['incidence_patterns']+=1
        R=[tuple(rect(*p) for p in ((B[g],C[g]),(B[g],D[g]),(C[g],D[g]))) for g in range(3)]
        H=tuple(R[0][z]^R[1][z]^R[2][z] for z in range(3))
        if not all(reg2(m) for m in H):continue
        if any(R[0][z]&R[1][z]&R[2][z]&H[z] for z in range(3)):continue
        xx['admissible_high_pair_signatures']+=1
        T=[q for q in itertools.product(range(4),repeat=3) if all(H[z]>>(4*q[i]+q[j])&1 for z,(i,j) in enumerate(PAIR3))]
        sizes=tuple(len({(q[i],q[j]) for q in T}) for i,j in PAIR3)
        if len(T)!=8 or sizes!=(6,6,6):raise ValueError('unexpected X high-triangle profile')
        xx['high_triangle_projection_obstructions']+=1
        xx_examples.append({'B':B,'C':C,'D':D,'triangle_count':len(T),'triangle_pair_projection_sizes':sizes,'triangles':T})
    if (yy['incidence_patterns'],yy['high_fiber_signature_pairs'],yy['supports_checked'],yy['all_three_cuts_unique_overlap'])!=(2975,10,40,40):raise ValueError(f'YY counts {yy}')
    if (xx['incidence_patterns'],xx['admissible_high_pair_signatures'],xx['high_triangle_projection_obstructions'])!=(240,10,10):raise ValueError(f'XY counts {xx}')
    result={'allY':dict(yy),'oneX':dict(xx),'normalization':{'YY_pair_graphs':34,'YY_AB_orbits':5,'XY_pair_graphs':15,'XY_AB_orbits':2,'six_fiber_subsets':144},
      'allY_support_witnesses':yy_examples,'oneX_triangle_witnesses':xx_examples,
      'scope':'Exact finite normalized E-support enumeration conditional on the written no-Hamming-one lemma; no independent review.'}
    with a.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    print(json.dumps({k:v for k,v in result.items() if not k.endswith('_witnesses')},indent=2))


if __name__=='__main__':main()
