#!/usr/bin/env python3
"""Exact 2026 five-variable family search on known source-copy coordinates.

A,B,C,D are distinct singleton variables within one source branch; Z,W are
empty or distinct further singleton variables. Missing entropies are NEVER
filled in. All finite staircase parameters and positive k are assessed for
each fully evaluable tuple. A violation is a candidate source theorem cut.
"""
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
from math import comb,lcm
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
OUTPUT=ROOT/'frontier-20261028-five-variable-source-branch-scan-result.json'
BASE=tuple('abcdefghij')
SYMBOLS=BASE+("b'0","d'1","e'1","g'2","f'3","g'3","h'4")
BITS={v:1<<i for i,v in enumerate(SYMBOLS)}
BRANCHES=(BASE+("b'0",),BASE+("d'1","e'1","g'2"),BASE+("f'3","g'3","h'4"))


def main():
    started=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    items=json.loads(raw)['primal_values']
    vals={sum(BITS[v] for v in x['entropy_variables']):Fraction(x['value']) for x in items}
    if len(vals)!=len(items):raise ValueError('DUPLICATE')
    vals[0]=Fraction(0);scale=lcm(*(x.denominator for x in vals.values()))
    H={m:int(value*scale) for m,value in vals.items()}
    @lru_cache(maxsize=None)
    def I(a,b,z):
        if not a or not b:return 0
        if a>b:a,b=b,a
        masks=(a|z,b|z,a|b|z,z)
        if any(m not in H for m in masks):return None
        return H[masks[0]]+H[masks[1]]-H[masks[2]]-H[masks[3]]
    records=[];first=None;second=None
    for branch,variables in enumerate(BRANCHES,1):
        checked=evaluable=unknown=negative_first=0;profiles={};start=time.monotonic()
        bits=[BITS[v] for v in variables]
        for A,B in combinations(bits,2):
            others=[x for x in bits if x not in (A,B)]
            for C in others:
                for D in others:
                    if C==D:continue
                    rest=[x for x in others if x not in (C,D)]
                    for Z in (0,*rest):
                        for W in (0,*(x for x in rest if x!=Z)):
                            checked+=1
                            pieces=(I(A,B,Z|W),I(A,B,W),I(A,B,C|W),I(A,B,D|W),
                                    I(C,D,W),I(A,Z,B|W),I(B,Z,A|W),
                                    I(A,C,B|W),I(B,C,A|W),I(A,D,B|W),I(B,D,A|W),
                                    I(A,C,W),I(A,C,D|W),I(B,D,W),
                                    I(B,C,W),I(B,C,D|W),I(A,D,W))
                            if any(x is None for x in pieces):unknown+=1;continue
                            evaluable+=1
                            g,ab,abc,abd,cd,az,bz,acb,bca,adb,bda,ac,acd,bd,bc,bcd,ad=pieces
                            zterm=az+bz;v=-ab+abc+abd+cd+zterm;c=acb+bca;d=adb+bda
                            if min(g,c,d)<0:raise ValueError(('NEGATIVE_KNOWN_CMI',branch,A,B,C,D,Z,W,g,c,d))
                            if v<0:
                                negative_first+=1;profiles.setdefault((g,v,c,d),(A,B,C,D,Z,W))
                            # Theorem2 under both A/B orders.
                            for X,Y,slope,Cterm in ((A,B,-ac+acb+acd+bd+zterm,c),
                                                    (B,A,-bc+bca+bcd+ad+zterm,I(B,C,A|W)+I(A,C,B|W))):
                                if Cterm==0:
                                    if slope<0:
                                        k=g//(-slope)+1;second={'branch':branch,'masks':[X,Y,C,D,Z,W],
                                            'k':k,'exact_slack':str(Fraction(g+k*slope,scale))};break
                                    k=1
                                else:k=max(1,-(slope//Cterm))
                                slack=g+k*slope+k*(k-1)//2*Cterm
                                if slack<0:
                                    second={'branch':branch,'masks':[X,Y,C,D,Z,W],'k':k,
                                            'exact_slack':str(Fraction(slack,scale))};break
                            if second:break
                        if second:break
                    if second:break
                if second:break
            if second:break
        cases=[]
        for (g,v,c,d),masks in profiles.items():
            if c==0 or d==0:
                length=g//(-v)+1;cells=[(i,0) for i in range(length)] if c==0 else [(0,j) for j in range(length)]
                first={'branch':branch,'masks':masks,'cells':cells,'exact_slack':str(Fraction(g+length*v,scale))};break
            if max((-v-1)//c,(-v-1)//d)>1000:raise ValueError('STAIRCASE_RANGE')
            alpha=beta=gamma=0;cells=[]
            for i in range((-v-1)//c+1):
                for j in range((-v-1-i*c)//d+1):
                    w=comb(i+j,i);alpha+=w;beta+=i*w;gamma+=j*w;cells.append((i,j))
            slack=g+alpha*v+beta*c+gamma*d
            cases.append({'profile':[g,v,c,d],'minimum_scaled_slack':slack})
            if slack<0:
                first={'branch':branch,'masks':masks,'cells':cells,'triplet':[alpha,beta,gamma],
                       'exact_slack':str(Fraction(slack,scale))};break
        records.append({'branch':branch,'checked':checked,'fully_evaluable':evaluable,'unevaluable':unknown,
                        'negative_theorem1_inner':negative_first,'negative_profiles':len(profiles),
                        'minimization_cases':cases,'elapsed_s':time.monotonic()-start})
        if first or second:break
    out={'input_sha256':EXPECTED,'scale':scale,'symbols':SYMBOLS,'branches':records,
         'source_theorem1_violation':first,'source_theorem2_violation':second,
         'elapsed_s':time.monotonic()-started,
         'limits':'Only singleton blocks within individual source branches and the fully specified entropy coordinates. Missing coordinates, overlapping blocks and arbitrary larger groups are not tested. Source theorem remains an external import and no graph upper bound follows.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
