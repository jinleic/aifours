#!/usr/bin/env python3
"""Direct fourth-root-phase zero-excess witness search with exact validation.

E has24 positions (12 residual rows per cut), coefficients i^phase/sqrt72.
Optional joint P has24 classical positions, each coefficient1/6. Every full pair
value is E-carried twice or P-carried once. Primary phases are two bits per E
position, zero when absent. For each E row with two entries, S=sum(phases) mod4.
Two rows sharing a column c are orthogonal iff their S low bits agree and
high(Sr) xor high(Ss) xor low(phi_rc) xor low(phi_sc)=1. Cut closure is imposed,
so the rows share both nonzeros; this is the exact2x2 phase equation mod4.
All SAT models are directly checked in Gaussian-integer arithmetic; joint P
models additionally get all3888 full Gram entries checked in Z[i,sqrt2].
A solver UNSAT is only this fourth-root ansatz, not an arbitrary-complex theorem.
"""
import argparse
from collections import Counter,defaultdict
from functools import reduce
import itertools
import json
from pathlib import Path
import z3

PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3))


def xor(xs):return reduce(lambda a,b:z3.Xor(a,b),xs,z3.BoolVal(False))


def word(A,r,B,c):
    q=[0]*4
    for i,x in zip(A,r):q[i]=x
    for i,x in zip(B,c):q[i]=x
    return tuple(q)


def validate(E,P,phases,joint):
    if len(E)!=24 or len(set(E))!=24:raise ValueError('E cardinality')
    if joint and (len(P)!=24 or len(set(P))!=24 or set(E)&set(P)):raise ValueError('P cardinality/disjointness')
    for i,j in PAIRS:
        ec=Counter((q[i],q[j]) for q in E);pc=Counter((q[i],q[j]) for q in P)
        if len(ec)!=12 or set(ec.values())!={2}:raise ValueError('residual pair invariant')
        if joint and any(not ((ec[a,b]==2 and pc[a,b]==0) or (ec[a,b]==0 and pc[a,b]==1)) for a,b in itertools.product(range(6),repeat=2)):
            raise ValueError('full pair partition')
    counts=[]
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);R=defaultdict(dict)
        for q in E:R[tuple(q[i] for i in A)][tuple(q[i] for i in B)]=('E',phases[q])
        for q in P:R[tuple(q[i] for i in A)][tuple(q[i] for i in B)]=('P',0)
        keys=list(itertools.product(range(6),repeat=2)) if joint else sorted(R)
        checked=0
        for r in keys:
            for s in keys:
                real=imag=0
                for c,(kind,p) in R[r].items():
                    if c not in R[s]:continue
                    k2,q=R[s][c]
                    if kind!=k2:raise ValueError('P/E cross overlap')
                    if kind=='P':real+=2
                    else:
                        n=(p-q)%4;real+=(1,0,-1,0)[n];imag+=(0,1,0,-1)[n]
                if (real,imag)!=((2 if r==s else 0),0):raise ValueError('exact complex Gram failure')
                checked+=1
        counts.append(checked)
    return counts


def build(deg,joint=False,real_only=False,fixed=None):
    sizes=tuple(map(len,deg));Q=list(itertools.product(*(range(r) for r in sizes)))
    E={q:z3.Bool('e'+''.join(map(str,q))) for q in Q};L={q:z3.Bool('l'+''.join(map(str,q))) for q in Q};H={q:z3.Bool('h'+''.join(map(str,q))) for q in Q}
    S=z3.Solver()
    for q in Q:
        S.add(z3.Implies(L[q],E[q]),z3.Implies(H[q],E[q]))
        if real_only:S.add(z3.Not(L[q]))
        if fixed is not None:S.add(E[q] if q in fixed else z3.Not(E[q]))
    for i,D in enumerate(deg):
        for a,d in enumerate(D):S.add(z3.PbEq([(E[q],1) for q in Q if q[i]==a],2*d))
    P={q:z3.Bool('p'+''.join(map(str,q))) for q in itertools.product(range(6),repeat=4)} if joint else {}
    if joint:
        S.add(z3.PbEq([(v,1) for v in P.values()],24))
        for q in Q:S.add(z3.Or(z3.Not(E[q]),z3.Not(P[q])))
    for i,j in PAIRS:
        pairvalues=itertools.product(range(6),repeat=2) if joint else itertools.product(range(sizes[i]),range(sizes[j]))
        for a,b in pairvalues:
            es=[(E[q],1) for q in Q if (q[i],q[j])==(a,b)]
            if not joint:S.add(z3.Or(z3.PbEq(es,0),z3.PbEq(es,2)))
            else:
                ps=[(v,1) for q,v in P.items() if (q[i],q[j])==(a,b)]
                # Empty E lists occur outside the E alphabets and mean count0.
                if not es:S.add(z3.PbEq(ps,1))
                else:S.add(z3.Or(z3.And(z3.PbEq(es,0),z3.PbEq(ps,1)),z3.And(z3.PbEq(es,2),z3.PbEq(ps,0))))
    # Conditional no-distance-one, explicit search restriction outside fixed controls.
    if fixed is None:
        for free in range(4):
            coords=tuple(i for i in range(4) if i!=free)
            for vals in itertools.product(*(range(sizes[i]) for i in coords)):
                S.add(z3.PbLe([(E[q],1) for q in Q if tuple(q[i] for i in coords)==vals],1))
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);RR=list(itertools.product(*(range(sizes[i]) for i in A)));CC=list(itertools.product(*(range(sizes[i]) for i in B)))
        G={(r,c):word(A,r,B,c) for r in RR for c in CC};low={};high={}
        for r in RR:
            lows=[L[G[r,c]] for c in CC];highs=[H[G[r,c]] for c in CC]
            low[r]=xor(lows);carry=z3.PbEq([(b,1) for b in lows],2);high[r]=z3.Xor(xor(highs),carry)
            for c,d in itertools.combinations(CC,2):
                S.add(z3.Implies(z3.And(E[G[r,c]],E[G[r,d]]),z3.Or(*[z3.And(E[G[t,c]],E[G[t,d]]) for t in RR if t!=r])))
        for r,s in itertools.combinations(RR,2):
            for c in CC:
                S.add(z3.Implies(z3.And(E[G[r,c]],E[G[s,c]]),z3.And(low[r]==low[s],xor([high[r],high[s],L[G[r,c]],L[G[s,c]]]))))
    return S,E,P,L,H


def main():
    ap=argparse.ArgumentParser();ap.add_argument('degrees',help='four slash-separated comma lists, or control');ap.add_argument('out',type=Path)
    ap.add_argument('--joint-P',action='store_true');ap.add_argument('--real',action='store_true');ap.add_argument('--timeout-ms',type=int,default=60000);a=ap.parse_args()
    fixed=None
    if a.degrees=='control':deg=[(3,3,3,3)]*4;fixed=set(itertools.permutations(range(4)))
    else:deg=[tuple(map(int,x.split(','))) for x in a.degrees.split('/')]
    if len(deg)!=4 or any(sum(D)!=12 or min(D)<2 or max(D)>6 for D in deg):raise ValueError('invalid residual degree specification')
    S,E,P,L,H=build(deg,a.joint_P,a.real,fixed);S.set(timeout=a.timeout_ms);ans=S.check()
    rec={'degrees':deg,'joint_P':a.joint_P,'phase_group':'real signs' if a.real else 'fourth roots','status':str(ans),'timeout_ms':a.timeout_ms}
    if ans==z3.sat:
        M=S.model();points=sorted(q for q,v in E.items() if z3.is_true(M.eval(v,model_completion=True)));classical=sorted(q for q,v in P.items() if z3.is_true(M.eval(v,model_completion=True)))
        ph={q:int(z3.is_true(M.eval(L[q],model_completion=True)))+2*int(z3.is_true(M.eval(H[q],model_completion=True))) for q in points}
        rec.update({'E_words_exponents':[[q,ph[q]] for q in points],'P_words':classical,
          'exact_Gram_entries_by_cut':validate(points,classical,ph,a.joint_P),
          'scope_of_SAT':'Exact full AME(4,6) candidate' if a.joint_P else 'Exact residual12x12 unitary component only; not a full AME witness'})
    elif ans==z3.unknown:rec['reason_unknown']=S.reason_unknown()
    rec['scope']='Individual fourth-root ansatz only; no arbitrary-complex exclusion or accepted witness.'
    with a.out.open('x',encoding='utf-8') as f:json.dump(rec,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in rec.items() if k not in ('E_words_exponents','P_words')},indent=2))


if __name__=='__main__':main()
