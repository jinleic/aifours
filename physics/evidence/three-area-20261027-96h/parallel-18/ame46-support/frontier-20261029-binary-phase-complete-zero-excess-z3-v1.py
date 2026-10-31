#!/usr/bin/env python3
"""Zero-excess E24 + simultaneous P24 + exact binary-root phases.

At --bits24 the phase group is complete for arbitrary complex phases on E24,
by the separately written Cramer/Hadamard/odd-multiplier theorem. A smaller
--bits is a restricted ansatz. All SAT models get sparse exact Gram checking.
UNSAT remains uncertified solver output, not a theorem. No-H1 is OPTIONAL and
its use is explicitly recorded. Output files are exclusive, never overwritten.
"""
import argparse
from collections import Counter,defaultdict
import itertools
import json
from pathlib import Path
import z3

PAIRS=list(itertools.combinations(range(4),2));CUTS=((0,1),(0,2),(0,3))


def qword(A,r,B,c):
    q=[0]*4
    for i,x in zip(A,r):q[i]=x
    for i,x in zip(B,c):q[i]=x
    return tuple(q)


def exact_grams(E,P,phase,bits,joint):
    L=1<<bits;half=L//2
    if len(E)!=24 or len(set(E))!=24:raise ValueError('E cardinality')
    if joint and (len(P)!=24 or len(set(P))!=24 or set(E)&set(P)):raise ValueError('P cardinality')
    for i,j in PAIRS:
        ec=Counter((q[i],q[j]) for q in E);pc=Counter((q[i],q[j]) for q in P)
        if len(ec)!=12 or set(ec.values())!={2}:raise ValueError('E pair counts')
        if joint and any(not ((ec[a,b]==2 and pc[a,b]==0) or (ec[a,b]==0 and pc[a,b]==1)) for a,b in itertools.product(range(6),repeat=2)):raise ValueError('pair partition')
    checked=[]
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);R=defaultdict(dict)
        for q in E:R[tuple(q[i] for i in A)][tuple(q[i] for i in B)]=('E',phase[q])
        for q in P:R[tuple(q[i] for i in A)][tuple(q[i] for i in B)]=('P',0)
        keys=list(itertools.product(range(6),repeat=2)) if joint else sorted(R);count=0
        for r in keys:
            for s in keys:
                poly=defaultdict(int)
                for c,(kind,a) in R[r].items():
                    if c not in R[s]:continue
                    k2,b=R[s][c]
                    if kind!=k2:raise ValueError('P/E mixed Gram term')
                    if kind=='P':poly[0]+=2
                    else:
                        d=(a-b)%L;poly[d%half]+=1 if d<half else -1
                if r==s:poly[0]-=2
                if any(poly.values()):raise ValueError('exact sparse cyclotomic Gram failure')
                count+=1
        checked.append(count)
    return checked


def build(deg,bits,joint,no_h1,fixed=None):
    sizes=tuple(map(len,deg));Q=list(itertools.product(*(range(r) for r in sizes)))
    E={q:z3.Bool('e'+''.join(map(str,q))) for q in Q};V={q:z3.BitVec('v'+''.join(map(str,q)),bits) for q in Q};S=z3.Solver()
    for q in Q:
        S.add(z3.Implies(z3.Not(E[q]),V[q]==0))
        if fixed is not None:S.add(E[q] if q in fixed else z3.Not(E[q]))
    for i,D in enumerate(deg):
        for a,d in enumerate(D):S.add(z3.PbEq([(E[q],1) for q in Q if q[i]==a],2*d))
    # A-party phase gauge: each A-fiber's first present entry can be made0 by
    # subtracting a phase depending only on that A value. Such phases cancel
    # from every block equation in all cuts, also within this finite root group.
    for a in range(sizes[0]):
        previous=z3.BoolVal(False)
        for q in (q for q in Q if q[0]==a):
            S.add(z3.Implies(z3.And(E[q],z3.Not(previous)),V[q]==0));previous=z3.Or(previous,E[q])
    P={q:z3.Bool('p'+''.join(map(str,q))) for q in itertools.product(range(6),repeat=4)} if joint else {}
    if joint:
        S.add(z3.PbEq([(v,1) for v in P.values()],24))
        for q in Q:S.add(z3.Or(z3.Not(E[q]),z3.Not(P[q])))
    for i,j in PAIRS:
        values=itertools.product(range(6),repeat=2) if joint else itertools.product(range(sizes[i]),range(sizes[j]))
        for a,b in values:
            es=[(E[q],1) for q in Q if (q[i],q[j])==(a,b)]
            if not joint:S.add(z3.Or(z3.PbEq(es,0),z3.PbEq(es,2)))
            else:
                ps=[(v,1) for q,v in P.items() if (q[i],q[j])==(a,b)]
                if not es:S.add(z3.PbEq(ps,1))
                else:S.add(z3.Or(z3.And(z3.PbEq(es,0),z3.PbEq(ps,1)),z3.And(z3.PbEq(es,2),z3.PbEq(ps,0))))
    # Sound label symmetry: if A,B each have an external E symbol, their first
    # external pair has exactly one P extension. Independently relabel C,D
    # within equal-degree classes (including degree0 outside E) so this unique
    # word uses the first value of its class. No type/category is forced.
    symmetry=False
    if joint and sizes[0]<6 and sizes[1]<6:
        reps=[]
        for i in (2,3):
            first={}
            for a,d in enumerate(tuple(deg[i])+(0,)*(6-sizes[i])):first.setdefault(d,a)
            reps.append(set(first.values()))
        for c,d in itertools.product(range(6),repeat=2):
            if c not in reps[0] or d not in reps[1]:S.add(z3.Not(P[sizes[0],sizes[1],c,d]))
        symmetry=True
    if no_h1:
        for free in range(4):
            C=tuple(i for i in range(4) if i!=free)
            for vals in itertools.product(*(range(sizes[i]) for i in C)):
                S.add(z3.PbLe([(E[q],1) for q in Q if tuple(q[i] for i in C)==vals],1))
    for A in CUTS:
        B=tuple(i for i in range(4) if i not in A);RR=list(itertools.product(*(range(sizes[i]) for i in A)));CC=list(itertools.product(*(range(sizes[i]) for i in B)))
        G={(r,c):qword(A,r,B,c) for r in RR for c in CC};SUM={r:sum((V[G[r,c]] for c in CC),z3.BitVecVal(0,bits)) for r in RR}
        for r in RR:
            for c,d in itertools.combinations(CC,2):S.add(z3.Implies(z3.And(E[G[r,c]],E[G[r,d]]),z3.Or(*[z3.And(E[G[t,c]],E[G[t,d]]) for t in RR if t!=r])))
        for r,s in itertools.combinations(RR,2):
            for c in CC:
                expr=SUM[r]-SUM[s]-2*V[G[r,c]]+2*V[G[s,c]]
                S.add(z3.Implies(z3.And(E[G[r,c]],E[G[s,c]]),expr==z3.BitVecVal(1<<(bits-1),bits)))
    return S,E,P,V,symmetry


def main():
    ap=argparse.ArgumentParser();ap.add_argument('degrees',help='four slash-separated comma lists, or control');ap.add_argument('out',type=Path)
    ap.add_argument('--bits',type=int,default=24);ap.add_argument('--joint-P',action='store_true');ap.add_argument('--no-H1',action='store_true');ap.add_argument('--timeout-ms',type=int,default=60000);a=ap.parse_args()
    if not 1<=a.bits<=48:raise ValueError('phase width1..48')
    fixed=None
    if a.degrees=='control':deg=[(3,3,3,3)]*4;fixed=set(itertools.permutations(range(4)))
    else:deg=[tuple(map(int,x.split(','))) for x in a.degrees.split('/')]
    if len(deg)!=4 or any(not D or sum(D)!=12 or min(D)<2 or max(D)>6 for D in deg):raise ValueError('invalid degree specification')
    S,E,P,V,sym=build(deg,a.bits,a.joint_P,a.no_H1,fixed);S.set(timeout=a.timeout_ms);ans=S.check()
    rec={'degrees':deg,'joint_P':a.joint_P,'no_H1_imposed':a.no_H1,'bits':a.bits,'phase_group_complete_for_E24':a.bits>=24,
      'A_fiber_first_phase_gauge':True,'external_pair_P_label_symmetry':sym,'status':str(ans),'timeout_ms':a.timeout_ms}
    if ans==z3.sat:
        M=S.model();points=sorted(q for q,v in E.items() if z3.is_true(M.eval(v,model_completion=True)));classical=sorted(q for q,v in P.items() if z3.is_true(M.eval(v,model_completion=True)))
        ph={q:M.eval(V[q],model_completion=True).as_long() for q in points}
        rec.update({'E_words_exponents':[[q,ph[q]] for q in points],'P_words':classical,
          'exact_Gram_entries_by_cut':exact_grams(points,classical,ph,a.bits,a.joint_P),
          'scope_of_SAT':'Literal48-term AME(4,6) candidate; independent full verification/review still required' if a.joint_P else 'Residual12x12 unitary only; not AME(4,6)'})
    elif ans==z3.unknown:rec['reason_unknown']=S.reason_unknown()
    rec['scope']='No accepted witness and no certified UNSAT theorem; phase completeness is conditional on the written determinant lemma.'
    with a.out.open('x',encoding='utf-8') as f:json.dump(rec,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in rec.items() if k not in ('E_words_exponents','P_words')},indent=2))


if __name__=='__main__':main()
