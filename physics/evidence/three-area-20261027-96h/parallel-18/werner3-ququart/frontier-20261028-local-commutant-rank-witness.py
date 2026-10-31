#!/usr/bin/env python3
"""Seek finite modular rank witnesses for four-replica local commutants.

No Schur-Weyl theorem is assumed by the calculation: derive a finite system
of diagonal-weight and E_ij commutator constraints, and compare its nullity
bound with the permutation span. One finite prime gives rigorous rank lower
bounds over Q/C. A partial/time-limited result is NOT a theorem or failure.
"""
import collections
import itertools
import json
import resource
import sys
import time
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-local-commutant-rank-witness-results.json'
WIT=ROOT/'frontier-20261028-local-commutant-pivot-rows.json'
P=65521
TIME_LIMIT=150.0
MEM_LIMIT=1_600_000_000


def memory_bytes():
    value=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform=='darwin' else value*1024)


def rank_insert(row,basis,pivots):
    row={k:v%P for k,v in row.items() if v%P}
    while row:
        k=min(row); v=row[k]
        if k not in basis:
            inv=pow(v,-1,P)
            row={j:(x*inv)%P for j,x in row.items() if (x*inv)%P}
            basis[k]=row;pivots.append(k);return True
        old=basis[k]
        row.pop(k,None)
        for j,x in old.items():
            if j==k:continue
            new=(row.get(j,0)-v*x)%P
            if new:row[j]=new
            else:row.pop(j,None)
    return False


def setup(n):
    words=list(itertools.product(range(n),repeat=4));blocks={}
    for x in words:
        w=tuple(x.count(i) for i in range(n));blocks.setdefault(w,[]).append(x)
    coords=[(x,y) for w in sorted(blocks) for x in blocks[w] for y in blocks[w]]
    lookup={key:i for i,key in enumerate(coords)}
    return words,blocks,coords,lookup


def permutation_rank(words,lookup):
    basis={};pivots=[]
    for perm in itertools.permutations(range(4)):
        col={}
        for y in words:
            x=[None]*4
            for i in range(4):x[perm[i]]=y[i]
            col[lookup[(tuple(x),y)]]=1
        rank_insert(col,basis,pivots)
    return len(basis),pivots


def equations(n,blocks,lookup):
    """Rows of [A,E_ij] over same-weight unknowns; retain explicit row labels."""
    for weight in sorted(blocks):
        inputs=blocks[weight]
        for i in range(n):
            for j in range(n):
                if i==j or weight[j]==0:continue
                target=list(weight);target[i]+=1;target[j]-=1
                for y in inputs:
                    rising=[]
                    for slot in range(4):
                        if y[slot]==j:
                            z=list(y);z[slot]=i;rising.append(tuple(z))
                    for x in blocks[tuple(target)]:
                        row={}
                        for z in rising:
                            col=lookup[(x,z)];row[col]=row.get(col,0)+1
                        for slot in range(4):
                            if x[slot]==i:
                                z=list(x);z[slot]=j
                                col=lookup[(tuple(z),y)];row[col]=row.get(col,0)-1
                        yield (i,j,x,y),row


def compute(n,start):
    words,blocks,coords,lookup=setup(n)
    prank,perm_piv=permutation_rank(words,lookup)
    target=len(coords)-prank
    basis={};pivots=[];witness=[];scanned=0;nonzero=0
    for label,row in equations(n,blocks,lookup):
        scanned+=1
        if any(row.values()):nonzero+=1
        if rank_insert(row,basis,pivots):witness.append(label)
        if len(basis)>=target:break
        if scanned%256==0 and (time.monotonic()-start>TIME_LIMIT or memory_bytes()>MEM_LIMIT):break
    reached=len(basis)==target
    return {'dimension':n,'replicas':4,'modulus':P,'full_replica_dimension':len(words),
            'weight_blocks':len(blocks),'commutant_unknowns':len(coords),
            'permutation_span_rank_mod_p':prank,'required_commutator_rank':target,
            'commutator_rank_lower_bound_mod_p':len(basis),'rows_scanned':scanned,
            'nonzero_rows_scanned':nonzero,'rank_target_reached':reached,
            'pivot_columns':pivots,'permutation_pivot_columns':perm_piv,
            'witness_rows':[[i,j,list(x),list(y)] for i,j,x,y in witness],
            'max_rss_bytes':memory_bytes()}


def main():
    start=time.monotonic()
    results=[]
    for n in (2,4):
        print('BEGIN local dimension',n,flush=True)
        result=compute(n,start);results.append(result)
        print('dimension',n,'rank',result['commutator_rank_lower_bound_mod_p'],
              '/',result['required_commutator_rank'],'rows',result['rows_scanned'],
              'memory',result['max_rss_bytes'],'elapsed',round(time.monotonic()-start,2),flush=True)
        if not result['rank_target_reached']:break
    witness={'kind':'selected_independent_commutator_equation_rows_for_exact_modular_rank',
             'prime':P,'cases':results,
             'meaning':'These are algebraic witness rows of the fully specified finite commutator system; not original physical inputs.'}
    WIT.write_text(json.dumps(witness,sort_keys=True,separators=(',',':'))+'\n')
    summary={'kind':'finite_local_four_replica_commutant_rank','prime':P,
             'cases':[{k:v for k,v in x.items() if k not in ('pivot_columns','permutation_pivot_columns','witness_rows')} for x in results],
             'all_requested_dimensions_reached':len(results)==2 and all(x['rank_target_reached'] for x in results),
             'elapsed_seconds':round(time.monotonic()-start,3),'witness_path':WIT.name,
             'max_rss_bytes':memory_bytes(),
             'scope':'A rank witness gives upper bounds for U(n) commutants only when combined with the explicit weight/infinitesimal argument and permutation-kernel inclusion. Separate independent witness replay and scientific review are required.',
             'verdict':'PASS' if len(results)==2 and all(x['rank_target_reached'] for x in results) else 'INCONCLUSIVE'}
    OUT.write_text(json.dumps(summary,sort_keys=True,indent=2)+'\n')
    print(json.dumps(summary,sort_keys=True,indent=2),flush=True)
    return 0 if summary['verdict']=='PASS' else 2


if __name__=='__main__':raise SystemExit(main())
