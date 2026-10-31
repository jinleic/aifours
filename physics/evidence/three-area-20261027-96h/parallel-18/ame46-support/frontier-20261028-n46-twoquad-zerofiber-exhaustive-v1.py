#!/usr/bin/env python3
"""Independent exact zero-fiber search for the 4444 two-quad N=46 case.

No SMT or external mathematical package is used. The written proof establishes
that all solutions reduce to these zero-free configurations and fibers.
"""
import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path

PAIRS=list(itertools.combinations(range(4),2));PERMS=list(itertools.permutations(range(4)))
SYMBOLS=(1,2,3);TARGET={0:4,1:4,2:6,3:6}


def zero_free():
    universe=list(itertools.product(SYMBOLS,repeat=4));result=[]
    for W in itertools.combinations(universe,4):
        if any(any(v%2 for v in Counter(q[i] for q in W).values()) for i in range(4)):continue
        if any(max(Counter((q[i],q[j]) for q in W).values())>2 for i,j in PAIRS):continue
        result.append(W)
    return result


def canonical(W):
    best=None
    for perm in PERMS:
      for swap in range(16):
        transformed=tuple(sorted(tuple(5-q[perm[i]] if (swap>>i&1) and q[perm[i]] in (2,3)
                                       else q[perm[i]] for i in range(4)) for q in W))
        if best is None or transformed<best:best=transformed
    return best


def fiber_options():
    pairs=list(itertools.combinations(SYMBOLS,2));result=[]
    for alph in itertools.product(pairs,repeat=3):
        cube=list(itertools.product(*alph))
        for inds in itertools.combinations(range(8),4):
            F=tuple(cube[i] for i in inds)
            if all(sum(q[j]==x for q in F)==2 for j in range(3) for x in alph[j]):result.append(F)
    if len(result)!=216 or len(set(result))!=216:raise ValueError('wrong balanced fiber catalog')
    return result


def candidates(W,zero,options,targets):
    others=tuple(i for i in range(4) if i!=zero)
    prior={ij:Counter((q[ij[0]],q[ij[1]]) for q in W) for ij in itertools.combinations(others,2)}
    result=[]
    for F in options:
        if any(targets[j,x]==0 for z,j in enumerate(others) for x in {q[z] for q in F}):continue
        mapped=tuple(tuple(0 if j==zero else q[others.index(j)] for j in range(4)) for q in F)
        signatures={ij:Counter((q[ij[0]],q[ij[1]]) for q in mapped) for ij in itertools.combinations(others,2)}
        if any(any(v+prior[ij].get(key,0)>2 for key,v in sig.items()) for ij,sig in signatures.items()):continue
        values={j:{q[j] for q in mapped} for j in others}
        result.append((mapped,signatures,values))
    return result


def solve_rep(W,options):
    targets={}
    for j in range(4):
      for x in SYMBOLS:
        remaining=TARGET[x]-sum(q[j]==x for q in W)
        if remaining%2 or not 0<=remaining//2<=3:raise ValueError('zero-free target mismatch')
        targets[j,x]=remaining//2
    C=[candidates(W,i,options,targets) for i in range(4)];order=sorted(range(4),key=lambda i:len(C[i]))
    adj={}
    for i,j in itertools.combinations(range(4),2):
        pair=tuple(k for k in range(4) if k not in (i,j));prior=Counter((q[pair[0]],q[pair[1]]) for q in W)
        adj[i,j]=[]
        for ca in C[i]:
            A=ca[1][pair];ok=set()
            for idx,cb in enumerate(C[j]):
                B=cb[1][pair]
                if all(prior.get(x,0)+A.get(x,0)+B.get(x,0) in (0,2) for x in set(prior)|set(A)|set(B)):ok.add(idx)
            adj[i,j].append(ok)
    used=Counter();chosen={};nodes=Counter();solutions=[]
    def walk(depth):
        nodes[depth]+=1
        if depth==4:
            if all(used[j,x]==targets[j,x] for j in range(4) for x in SYMBOLS):
                solutions.append([list(C[i][chosen[i]][0]) for i in range(4)])
            return
        i=order[depth]
        for index,candidate in enumerate(C[i]):
            if any((index not in adj[j,i][old] if j<i else old not in adj[i,j][index]) for j,old in chosen.items()):continue
            values=candidate[2];ok=True
            for j,vals in values.items():
                for x in vals:
                    used[j,x]+=1
                    if used[j,x]>targets[j,x]:ok=False
            if ok:
                for j in range(4):
                    remaining=sum(k!=j and k not in chosen and k!=i for k in range(4))
                    if any(used[j,x]+remaining<targets[j,x] for x in SYMBOLS):ok=False;break
            if ok:chosen[i]=index;walk(depth+1);del chosen[i]
            for j,vals in values.items():
                for x in vals:used[j,x]-=1
    walk(0)
    return nodes,solutions,[len(x) for x in C]


def relaxed_positive(path):
    record=json.loads(path.read_text());case=next(c for c in record['cases'] if c['pair_multiplicity']=='even_unbounded' and c['forbidden_diagonal']=='both' and c['exact_fiber_sizes'] and c['status']=='sat')
    S=[tuple(x) for x in case['support']]
    if len(S)!=20 or len(set(S))!=20:raise ValueError('bad positive witness cardinality')
    if any(sum(q[i]==x for q in S)!=TARGET[x] for i in range(4) for x in range(4)):raise ValueError('bad positive fiber counts')
    if any(q.count(0)>1 for q in S):raise ValueError('bad positive forbidden 00')
    over=[]
    for i,j in PAIRS:
        c=Counter((q[i],q[j]) for q in S)
        if any(v%2 for v in c.values()):raise ValueError('bad positive parity')
        over.extend((i,j,pair,v) for pair,v in c.items() if v>2)
    if not over:raise ValueError('positive does not violate weakened pair cap')
    return {'status':'PASS for all constraints except pair cap 2','overfull_pairs':over}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('out',type=Path);ap.add_argument('relaxed_positive',type=Path);a=ap.parse_args()
    W=zero_free();orbits=Counter(canonical(x) for x in W)
    if len(W)!=6804 or len(orbits)!=62 or sum(orbits.values())!=len(W):raise ValueError('zero-free orbit coverage mismatch')
    options=fiber_options();nodes=Counter();solutions=0;records=[]
    for rep,orbit_size in sorted(orbits.items()):
        visit,found,sizes=solve_rep(rep,options);nodes.update(visit);solutions+=len(found)
        records.append({'zero_free':rep,'orbit_size':orbit_size,'fiber_candidate_counts':sizes,'depth_nodes':dict(visit),'solutions':len(found)})
    if solutions:raise ValueError('unexpected zero-fiber solution')
    positive=relaxed_positive(a.relaxed_positive)
    orbit_blob=json.dumps(records,sort_keys=True,separators=(',',':')).encode('ascii')
    result={'zero_free_labeled_candidates':len(W),'party_permutation_high_swap_orbits':len(orbits),
      'balanced_fibers_per_zero_position_before_pruning':len(options),'orbit_records':records,
      'total_depth_nodes':dict(sorted(nodes.items())),'solutions':solutions,
      'orbit_records_canonical_sha256':hashlib.sha256(orbit_blob).hexdigest(),
      'relaxed_pair_cap_positive_control':positive,
      'scope':'Exact exhaustive support enumeration; normal-form and symmetry completeness require the accompanying written proof.'}
    with a.out.open('x',encoding='utf-8') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='orbit_records'},indent=2))


if __name__=='__main__':main()
