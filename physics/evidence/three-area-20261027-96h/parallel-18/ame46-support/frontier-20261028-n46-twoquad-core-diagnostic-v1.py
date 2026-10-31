#!/usr/bin/env python3
"""Uncertified SMT assumption-core diagnostic for the two-quad subcase."""
import argparse
import itertools
import json
from pathlib import Path
import z3

Q=list(itertools.product(range(4),repeat=4));PAIRS=list(itertools.combinations(range(4),2))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);ap.add_argument('--timeout-ms',type=int,default=15000);a=ap.parse_args()
    E={q:z3.Bool('e'+''.join(map(str,q))) for q in Q};S=z3.Solver();S.set(timeout=a.timeout_ms)
    labels={}
    def impose(name,formula):
        tag=z3.Bool('assume_'+name);labels[name]=tag;S.add(z3.Implies(tag,formula))
    impose('total20',z3.PbEq([(v,1) for v in E.values()],20))
    for i in range(4):
      for x in range(4):
        impose(f'fiber{i}_{x}',z3.PbEq([(v,1) for q,v in E.items() if q[i]==x],4 if x<2 else 6))
    for i,j in PAIRS:
        group=[]
        for x,y in itertools.product(range(4),repeat=2):
            terms=[(v,1) for q,v in E.items() if q[i]==x and q[j]==y]
            group.append(z3.Or(z3.PbEq(terms,0),z3.PbEq(terms,2)))
        impose(f'pair{i}{j}',z3.And(*group))
        for x in (0,1):
            impose(f'forbid{i}{j}_{x}',z3.Not(z3.Or(*[v for q,v in E.items() if q[i]==x and q[j]==x])))
    alltags=list(labels.values());ans=S.check(*alltags);result={'status':str(ans),'timeout_ms':a.timeout_ms}
    if ans==z3.unsat:
        result['initial_assumption_core']=[str(x).removeprefix('assume_') for x in S.unsat_core()]
        trials=[]
        for i,j in PAIRS:
            name=f'pair{i}{j}';res=S.check(*[v for k,v in labels.items() if k!=name])
            trials.append({'omitted':name,'status':str(res),'reason_unknown':S.reason_unknown() if res==z3.unknown else None})
        result['individual_pair_group_omissions']=trials
    elif ans==z3.unknown:result['reason_unknown']=S.reason_unknown()
    result['scope']='Uncertified SMT core and relaxations; no proof-certificate claim.'
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
