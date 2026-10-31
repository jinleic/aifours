#!/usr/bin/env python3
"""Explore which support constraints cause the two-quad SMT contradiction.

Results are exact solver diagnostics, not independently checked UNSAT proofs.
"""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path
import z3

Q=list(itertools.product(range(4),repeat=4));PAIRS=list(itertools.combinations(range(4),2))


def solve(cap,lowmode,fibers,timeout):
    z=z3.Solver();z.set(timeout=timeout);v={q:z3.Bool('x'+''.join(map(str,q))) for q in Q}
    z.add(z3.PbEq([(x,1) for x in v.values()],20))
    if fibers:
      for i in range(4):
       for a in range(4):z.add(z3.PbEq([(v[q],1) for q in Q if q[i]==a],4 if a<2 else 6))
    for i,j in PAIRS:
      for a,b in itertools.product(range(4),repeat=2):
        cells=[v[q] for q in Q if (q[i],q[j])==(a,b)]
        if (a,b)==(0,0) and lowmode in ('zero','both') or (a,b)==(1,1) and lowmode=='both':z.add(z3.Not(z3.Or(*cells)));continue
        vals=(0,2) if cap else tuple(range(0,17,2))
        z.add(z3.Or(*[z3.PbEq([(x,1) for x in cells],k) for k in vals]))
    ans=z.check();r={'pair_multiplicity':'0_or_2' if cap else 'even_unbounded',
      'forbidden_diagonal':lowmode,'exact_fiber_sizes':fibers,'status':str(ans)}
    if ans==z3.sat:
        m=z.model();S=sorted(q for q in Q if z3.is_true(m.eval(v[q],model_completion=True)));r['support']=S
        if len(S)!=20:raise ValueError('bad SAT support')
        if fibers and any([sum(q[i]==a for q in S) for a in range(4)]!=[4,4,6,6] for i in range(4)):raise ValueError('bad SAT fiber')
        for i,j in PAIRS:
            c=Counter((q[i],q[j]) for q in S)
            if any(x%2 or cap and x>2 for x in c.values()):raise ValueError('bad SAT pair count')
            if lowmode in ('zero','both') and (0,0) in c or lowmode=='both' and (1,1) in c:raise ValueError('bad SAT forbidden pair')
    elif ans==z3.unknown:r['reason_unknown']=z.reason_unknown()
    return r


def main():
    p=argparse.ArgumentParser();p.add_argument('out',type=Path);p.add_argument('--timeout-ms',type=int,default=12000);a=p.parse_args()
    cases=[solve(cap,low,fibers,a.timeout_ms) for cap in (True,False) for low in ('both','zero','none') for fibers in (True,False)]
    result={'cases':cases,'timeout_ms_each':a.timeout_ms,'scope':'Support-only SMT relaxations; UNSAT is unverified solver output.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'cases':[{k:v for k,v in c.items() if k!='support'} for c in cases],'scope':result['scope']},indent=2))


if __name__=='__main__':main()
