#!/usr/bin/env python3
"""Uncertified maximal-code diagnostic for N47,t27,r4444.

P has27 words, pair-injective, local occurrences(4,4,4,3,6,6). A SAT P code
is checked directly, then its residual-allowed words are enumerated exactly;
no residual amplitudes or AME state is asserted. UNSAT is unverified solver output.
"""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path
import z3

Q=list(itertools.product(range(6),repeat=4));PAIRS=list(itertools.combinations(range(4),2));OCC=(4,4,4,3,6,6)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);ap.add_argument('--timeout-ms',type=int,default=20000);a=ap.parse_args()
    P={q:z3.Bool('p'+''.join(map(str,q))) for q in Q};S=z3.Solver();S.set(timeout=a.timeout_ms)
    S.add(z3.PbEq([(v,1) for v in P.values()],27))
    for i in range(4):
        for x in range(6):S.add(z3.PbEq([(v,1) for q,v in P.items() if q[i]==x],OCC[x]))
    for i,j in PAIRS:
        for x,y in itertools.product(range(6),repeat=2):S.add(z3.PbLe([(v,1) for q,v in P.items() if (q[i],q[j])==(x,y)],1))
    ans=S.check();result={'status':str(ans),'timeout_ms':a.timeout_ms}
    if ans==z3.sat:
        M=S.model();words=sorted(q for q,v in P.items() if z3.is_true(M.eval(v,model_completion=True)))
        if len(words)!=27:raise ValueError('bad P cardinality')
        if any([sum(q[i]==x for q in words) for x in range(6)]!=list(OCC) for i in range(4)):raise ValueError('P symbol multiplicity')
        pairs={ij:{(q[ij[0]],q[ij[1]]) for q in words} for ij in PAIRS}
        if any(len(x)!=27 for x in pairs.values()):raise ValueError('P pair collision')
        allowed=[q for q in itertools.product(range(4),repeat=4) if all((q[i],q[j]) not in pairs[i,j] for i,j in PAIRS)]
        result.update({'P_words':words,'residual_allowed_words':allowed,'residual_allowed_count':len(allowed),
          'P_active_count_histogram':dict(Counter(sum(x<4 for x in q) for q in words)),
          'residual_pair_cover_sizes':{str(ij):len({(q[ij[0]],q[ij[1]]) for q in allowed}) for ij in PAIRS},
          'direct_P_validation':'PASS; no E support, no amplitudes'})
    elif ans==z3.unknown:result['reason_unknown']=S.reason_unknown()
    result['scope']='P-code and residual capacity diagnostic only, not an AME witness or an UNSAT proof.'
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('P_words','residual_allowed_words')},indent=2))


if __name__=='__main__':main()
