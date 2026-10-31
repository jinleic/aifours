#!/usr/bin/env python3
"""Exact finite incidence certificates for N48/t24 with a six-symbol E party.

Six labeled parity fibers; every partner incidence has row weight2, every used
column weight>=2 and total12. Columns may be independently relabeled, so each
matrix is a sorted multiset of nonempty6-bit columns (multiplicity retained).
All compatible triples have every integer column intersection in{0,2}. The
certificate is either a common pairing of identical rows in all3 matrices, or
one fiber pair with singleton rowset intersection at two partner coordinates.
Both imply quantum impossibility by the separate written argument, not here.
"""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path

FIBER_PAIRS=list(itertools.combinations(range(6),2))
MASKS={w:[x for x in range(1,64) if x.bit_count()==w] for w in range(2,7)}


def families(r):
    out=[]
    for weights in itertools.combinations_with_replacement(range(2,7),r):
        if sum(weights)!=12:continue
        counts=Counter(weights);groups=[list(itertools.combinations_with_replacement(MASKS[w],n)) for w,n in sorted(counts.items())]
        for parts in itertools.product(*groups):
            cols=tuple(sorted(x for p in parts for x in p))
            if all(sum(bool(x>>g&1) for x in cols)==2 for g in range(6)):out.append(cols)
    if len(out)!=len(set(out)):raise ValueError('duplicate incidence class')
    return sorted(out)


def data(cols):
    columnset=sum(1<<x for x in set(cols))
    compat=sum(1<<x for w in range(2,7) for x in MASKS[w] if all((x&y).bit_count() in (0,2) for y in cols))
    rows=tuple(sum(1<<j for j,c in enumerate(cols) if c>>g&1) for g in range(6))
    ones=sum(1<<k for k,(g,h) in enumerate(FIBER_PAIRS) if (rows[g]&rows[h]).bit_count()==1)
    return columnset,compat,rows,ones


def certificate(B,C,D):
    sets=(B,C,D);bad=(B[3]&C[3])|(B[3]&D[3])|(C[3]&D[3])
    if bad:
        index=(bad&-bad).bit_length()-1;g,h=FIBER_PAIRS[index]
        coords=[i for i,S in enumerate(sets) if (S[2][g]&S[2][h]).bit_count()==1]
        if len(coords)<2:raise ValueError('bad intersection classifier')
        return {'kind':'TWO_SINGLETON_INTERSECTIONS','fibers':[g,h],'partner_coordinates':coords[:2]}
    classes={}
    for g,key in enumerate(zip(B[2],C[2],D[2])):classes.setdefault(key,[]).append(g)
    if any(len(x)!=2 for x in classes.values()) or len(classes)!=3:raise ValueError('unclassified compatible incidence triple')
    return {'kind':'COMMON_ROW_PAIRING','pairs':sorted(classes.values())}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args();F={r:families(r) for r in range(2,7)}
    if [len(F[r]) for r in range(2,7)]!=[1,115,1150,1295,130]:raise ValueError('family counts')
    D={r:[data(c) for c in F[r]] for r in F};profiles=[p for p in itertools.combinations_with_replacement(range(2,7),3) if all(x*y>=12 for x,y in itertools.combinations(p,2))]
    records=[];summary={}
    for sizes in profiles:
        Bs,Cs,Ds=(D[r] for r in sizes);counts=Counter()
        for i,B in enumerate(Bs):
          for j,C in enumerate(Cs):
            if C[0]&~B[1]:continue
            allowed=B[1]&C[1]
            for k,E in enumerate(Ds):
                if E[0]&~allowed:continue
                c=certificate(B,C,E);counts[c['kind']]+=1
                records.append({'partner_sizes':sizes,'class_indices':[i,j,k],'certificate':c})
        summary[','.join(map(str,sizes))]={'compatible_triples':sum(counts.values()),'certificate_kinds':dict(counts)}
    if len(profiles)!=17:raise ValueError('partner profiles')
    result={'incidence_classes':{str(r):F[r] for r in F},'family_class_counts':{str(r):len(F[r]) for r in F},
      'profile_summary':summary,'records':records,
      'scope':'Exact finite matrix classification only. No-Hamming-one prerequisite, tensor reduction and unitary contradictions are separate written mathematics.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'family_class_counts':result['family_class_counts'],'profile_summary':summary,'total_records':len(records)},indent=2))


if __name__=='__main__':main()
