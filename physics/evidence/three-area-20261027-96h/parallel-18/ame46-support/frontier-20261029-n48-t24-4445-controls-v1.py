#!/usr/bin/env python3
"""Tiny exact controls for the N48/t24 residual(5,4,4,4) written obstruction.

Normal form is proved in the paper: A degrees22233; B,C,D all3333;
missing BC and BD matchings identity, missing CD p double-transposition or4cycle;
three low A parity fibers U x complement(U) x complement(U). Two high A fibers
are six-triangle covers of the locally completed missing matchings.
No actual phase solver, SAT solver or prior research implementation is imported.
"""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path

I=(0,1,2,3);PAIRS=list(itertools.combinations(range(4),2))


def allowed(p,missL,missR):
    L=[x for x in range(4) if x!=missL];R=[x for x in range(4) if x!=missR]
    fixed={(x,p[x]) for x in L if p[x]!=missR};match=[]
    for q in itertools.permutations(R):
        M=set(zip(L,q))
        if fixed<=M:match.append(M)
    if len(match)!=1:raise ValueError('local matching completion not unique')
    return {(x,y) for x,y in itertools.product(L,R) if (x,y) not in match[0]}


def covers(BC,BD,CD):
    edges=sorted(BC);out=[]
    def visit(k,bd,cd,T):
        if k==len(edges):
            if bd==BD and cd==CD:out.append(T)
            return
        b,c=edges[k]
        for d in range(4):
            if (b,d) in BD and (c,d) in CD and (b,d) not in bd and (c,d) not in cd:visit(k+1,bd|{(b,d)},cd|{(c,d)},T+[(b,c,d)])
    visit(0,set(),set(),[]);return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);a=ap.parse_args();result={};totalpassBCBD=0;example=None
    for p in ((1,0,3,2),(1,2,3,0)):
        lows=[U for U in itertools.combinations(range(4),2) if {p[x] for x in U}==set(range(4))-set(U)];count=Counter();failure=Counter()
        for U in itertools.combinations_with_replacement(lows,3):
            freq=[sum(x in S for S in U) for x in range(4)]
            if sorted(freq)!=[1,1,2,2]:continue
            count['low_patterns']+=1;X=[x for x in range(4) if freq[x]==2];Y=[x for x in range(4) if freq[x]==1]
            for cm,dm in itertools.product(itertools.permutations(Y),repeat=2):
                count['high_exclusion_patterns']+=1;high=[]
                for b,c,d in zip(X,cm,dm):high.append(covers(allowed(I,b,c),allowed(I,b,d),allowed(p,c,d)))
                if any(not H for H in high):continue
                count['both_high_fibers_exist']+=1
                for H0,H1 in itertools.product(*high):
                  for signs in itertools.product((0,1),repeat=3):
                    fibers=[]
                    for S,bit in zip(U,signs):
                        V=tuple(sorted(set(range(4))-set(S)));alph=(S,V,V)
                        fibers.append([tuple(alph[i][q[i]] for i in range(3)) for q in itertools.product((0,1),repeat=3) if q[0]^q[1]^q[2]==bit])
                    E={(g,)+q for g,F in enumerate(fibers+[H0,H1]) for q in F};count['supports']+=1
                    flags=[]
                    for i,j in PAIRS:
                        C=Counter((q[i],q[j]) for q in E);flags.append(len(C)==12 and set(C.values())=={2})
                    if not all(flags[:3]):raise ValueError('A-partner pair conditions failed')
                    failure[str(tuple(flags[3:]))]+=1
                    if all(flags):raise ValueError('unexpected full six-pair support')
                    if flags[3] and flags[4]:
                        totalpassBCBD+=1
                        if example is None:example={'p':p,'low_sets':U,'C_missing':cm,'D_missing':dm,
                            'CD_count_histogram':dict(Counter(Counter((q[2],q[3]) for q in E).values()))}
        result[str(p)]={'counts':dict(count),'BC_BD_CD_condition_histogram':dict(failure)}
    if result[str((1,0,3,2))]['counts']!={'low_patterns':8,'high_exclusion_patterns':32,'both_high_fibers_exist':32,'supports':256}:raise ValueError('double-transposition counts')
    if result[str((1,2,3,0))]['counts']!={'low_patterns':2,'high_exclusion_patterns':8,'both_high_fibers_exist':2,'supports':16}:raise ValueError('4cycle counts')
    if totalpassBCBD==0:raise ValueError('no relaxed two-pair positive control')
    payload={'representatives':result,'supports_passing_BC_BD_but_failing_CD':totalpassBCBD,
      'relaxed_positive_example':example,'scope':'Tiny exact normal-form controls; complete written no-Hamming-one/profile derivation is separate.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(payload,f,indent=2);f.write('\n')
    print(json.dumps(payload,indent=2))


if __name__=='__main__':main()
