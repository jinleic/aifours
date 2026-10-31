#!/usr/bin/env python3
"""Independent partial-Latin/edge-set replay of the N46 4444 geometry."""
import argparse
from collections import Counter,defaultdict
import itertools
import json
from pathlib import Path

PAIR3=((0,1),(0,2),(1,2));CUTS=((0,1),(0,2),(0,3))


def rows(rowdegrees,coldegrees):
    alph=[list(itertools.combinations(range(4),d)) for d in rowdegrees]
    return [tuple(z) for z in itertools.product(*alph)
            if tuple(sum(x in r for r in z) for x in range(4))==coldegrees]


def relabel(G,row_perms):
    reps=[]
    for r in row_perms:
      for ls,hs in itertools.product((0,1),repeat=2):
        p=list(range(4))
        if ls:p[0],p[1]=p[1],p[0]
        if hs:p[2],p[3]=p[3],p[2]
        reps.append(tuple(tuple(sorted(p[v] for v in G[r[i]])) for i in range(4)))
    return min(reps)


def latin6():
    out=set()
    for missing in itertools.permutations(range(3)):
        cells=[(b,c) for b in range(3) for c in range(3) if c!=missing[b]]
        for ds in itertools.product(range(3),repeat=6):
            if any(ds.count(x)!=2 for x in range(3)):continue
            triples=tuple(sorted((b,c,d) for (b,c),d in zip(cells,ds)))
            if any(len({(q[i],q[j]) for q in triples})!=6 for i,j in PAIR3):continue
            out.add(triples)
    if len(out)!=144:raise ValueError('partial Latin fiber count')
    return sorted(out)


def edge_sets(F):return tuple(frozenset((q[i],q[j]) for q in F) for i,j in PAIR3)


def mapped_latin(alph,F):return tuple(tuple(alph[i][q[i]] for i in range(3)) for q in F)


def parity(alph,sign):
    return tuple(tuple(alph[i][q[i]] for i in range(3)) for q in itertools.product(range(2),repeat=3) if q[0]^q[1]^q[2]==sign)


def counterok(sets):
    M=Counter(x for S in sets for x in S)
    return len(M)==10 and all(v==2 for v in M.values())


def cut_witness(S,A):
    B=tuple(i for i in range(4) if i not in A);rows=defaultdict(set);cols=defaultdict(set)
    for q in S:r=tuple(q[i] for i in A);c=tuple(q[i] for i in B);rows[r].add(c);cols[c].add(r)
    for T in (rows,cols):
        for x,y in itertools.combinations(T.values(),2):
            if len(x&y)==1:return True
    return False


def triangle_covers(H):
    cells=sorted(H[0]);out=0
    def visit(k,used_bd,used_cd):
        nonlocal out
        if k==len(cells):out+=1;return
        b,c=cells[k]
        for d in range(4):
            if (b,d) not in H[1] or (c,d) not in H[2] or (b,d) in used_bd or (c,d) in used_cd:continue
            visit(k+1,used_bd|{(b,d)},used_cd|{(c,d)})
    visit(0,set(),set());return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args()
    Y=rows((2,2,3,3),(2,2,3,3));X=rows((2,2,2,4),(2,2,3,3));
    yr=[]
    for a0,a1 in itertools.product((False,True),repeat=2):
        z=list(range(4))
        if a0:z[0],z[1]=z[1],z[0]
        if a1:z[2],z[3]=z[3],z[2]
        yr.append(tuple(z))
    xr=[tuple(p)+(3,) for p in itertools.permutations(range(3))]
    Yrep=sorted({relabel(g,yr) for g in Y});Xrep=sorted({relabel(g,xr) for g in X});L=latin6()
    if (len(Y),len(Yrep),len(X),len(Xrep))!=(34,5,15,2):raise ValueError('graph-orbit count')
    maps={}
    for alph in itertools.product(itertools.combinations(range(4),3),repeat=3):
        D=defaultdict(list)
        for F in L:
            pts=mapped_latin(alph,F);D[edge_sets(pts)[0]].append((pts,edge_sets(pts)))
        maps[alph]=D
    cy=Counter();cx=Counter()
    for B in Yrep:
      for i,C in enumerate(Y):
       for D in Y[i:]:
        cy['incidence_patterns']+=1
        low=[tuple(frozenset(itertools.product(*x)) for x in ((B[g],C[g]),(B[g],D[g]),(C[g],D[g]))) for g in (0,1)]
        U=maps[(B[2],C[2],D[2])];V=maps[(B[3],C[3],D[3])]
        for vals in U.values():
         for F2,H2 in vals:
          target=H2[0]^low[0][0]^low[1][0]
          for F3,H3 in V.get(target,()):
           if not all(counterok((low[0][z],low[1][z],H2[z],H3[z])) for z in range(3)):continue
           cy['high_pairs']+=1
           for s0,s1 in itertools.product((0,1),repeat=2):
            Fs=(parity((B[0],C[0],D[0]),s0),parity((B[1],C[1],D[1]),s1),F2,F3)
            S={(g,)+q for g,F in enumerate(Fs) for q in F};cy['supports']+=1
            for i,j in itertools.combinations(range(4),2):
                Cnt=Counter((q[i],q[j]) for q in S)
                if len(Cnt)!=10 or set(Cnt.values())!={2}:raise ValueError('YY pair condition')
            if not all(cut_witness(S,cut) for cut in CUTS):raise ValueError('YY overlap gap')
            cy['all_three_unique_overlap']+=1
    for B in Xrep:
      for i,C in enumerate(X):
       for D in X[i:]:
        cx['incidence_patterns']+=1
        R=[tuple(frozenset(itertools.product(*x)) for x in ((B[g],C[g]),(B[g],D[g]),(C[g],D[g]))) for g in range(3)]
        H=tuple(R[0][z]^R[1][z]^R[2][z] for z in range(3))
        if any(len(h)!=8 or any(sum(x==v for x,y in h)!=2 or sum(y==v for x,y in h)!=2 for v in range(4)) for h in H):continue
        if any(R[0][z]&R[1][z]&R[2][z]&H[z] for z in range(3)):continue
        cx['admissible_high_graphs']+=1
        if triangle_covers(H):raise ValueError('X high fiber completion exists')
        cx['no_high_triangle_cover']+=1
    if tuple(cy[x] for x in ('incidence_patterns','high_pairs','supports','all_three_unique_overlap'))!=(2975,10,40,40):raise ValueError(f'YY counts {cy}')
    if tuple(cx[x] for x in ('incidence_patterns','admissible_high_graphs','no_high_triangle_cover'))!=(240,10,10):raise ValueError(f'X counts {cx}')
    result={'allY':dict(cy),'oneX':dict(cx),'independent_six_fiber_Latin_count':len(L),
      'scope':'Exact independent edge-set/partial-Latin replay; the normal-form and no-distance-one proofs are separate.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
