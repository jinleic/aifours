#!/usr/bin/env python3
"""Independent RREF coverage and direct clique-witness replay for syndrome 3-planes."""
from hashlib import sha256
from functools import reduce
from itertools import combinations,product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-syndrome-3plane-lifts-result.json','f31739ca90dde765c9d272567809fc5ec7c21803413db0248429e71e0e0a7562')
HYPER=('frontier-20261028-syndrome-hyperplane-check-result.json','ddc3c58d179f9602fa9284ca87efbf3bb14ce1a9193c47c4645638064b949a57')
OUT=ROOT/'frontier-20261028-syndrome-3plane-independent-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
INC={v:[t for t,T in enumerate(TRI) if v in T] for v in N}


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def syndrome(word):
    out=0
    for t,T in enumerate(TRI):
        parity=0
        for v in T:parity^=(word>>(3*(v-1)+INC[v].index(t)))&1
        out|=parity<<t
    return out


def conflict(word):
    if not 0<word<2**30:return False
    return any((word>>(3*(v-1)))&7 and all(not((word>>(3*(u-1)))&7) for u in N[v]) for v in N)


def check_witness(r):
    basis=tuple(r['rref_basis']);ordered=tuple(r['searched_basis']);words=tuple(r['word_representatives'])
    if len(basis)!=3 or len(words)!=3 or set(ordered)!=set(basis):raise ValueError('BASIS')
    if any(syndrome(w)!=s for s,w in zip(ordered,words)):raise ValueError('SYNDROME')
    if any(not conflict(reduce(int.__xor__,(words[j] for j in range(3) if subset>>j&1),0)) for subset in range(1,8)):raise ValueError('CLIQUE')
    return basis


def values(pivot,free):
    return [1<<pivot|sum(1<<j for i,j in enumerate(free) if k>>i&1) for k in range(1<<len(free))]


def require_count(records):
    if len(records)!=25086:raise ValueError('WITNESS_COUNT')


def coverage(records):
    require_count(records)
    table={}
    for r in records:
        b=check_witness(r)
        if b in table:raise ValueError('DUPLICATE')
        table[b]=True
    if len(table)!=25086:raise ValueError('WITNESS_COUNT')
    hypermask=sum(1<<(i-1) for i in (1,2,3,6,8,10));inc=[sum(1<<t for t in INC[v]) for v in N]
    counts=[0,0,0,0];seen=set()
    for p,q,r in combinations(range(10),3):
        one=values(p,[j for j in range(p+1,10) if j not in (q,r)])
        two=values(q,[j for j in range(q+1,10) if j!=r]);three=values(r,list(range(r+1,10)))
        for a,b,c in product(one,two,three):
            counts[0]+=1
            if (a|b|c)&hypermask!=hypermask:counts[1]+=1;continue
            local=False
            for mask in inc:
                x,y,z=a&mask,b&mask,c&mask
                if len({0,x,y,z,x^y,x^z,y^z,x^y^z})==8:local=True;break
            if local:counts[2]+=1;continue
            counts[3]+=1;key=(a,b,c)
            if key not in table:raise ValueError('MISSING_WITNESS')
            seen.add(key)
    if counts!=[6347715,3487095,2835534,25086] or seen!=set(table):raise ValueError(('COVERAGE',counts,len(seen)))
    return counts


def main():
    src=pin(SOURCE);hyper=pin(HYPER)
    if not hyper['all_checked'] or {x['missing_factor_one_based'] for x in hyper['independent_vertex_triples']}!={1,2,3,6,8,10}:raise ValueError('HYPERPLANE')
    if any(set(T)<=set(N[v]) for v in N for T in TRI):raise ValueError('LOCAL_COMPLETION')
    counts=coverage(src['exceptional_witnesses']);controls={};bad=json.loads(json.dumps(src['exceptional_witnesses'][0]));bad['word_representatives'][0]=0
    try:check_witness(bad)
    except ValueError as exc:
        if str(exc)!='SYNDROME':raise ValueError(('WRONG_REASON',str(exc)))
        controls['zeroed_representative']='SYNDROME'
    else:raise ValueError('MUTATION_ACCEPTED')
    try:require_count(src['exceptional_witnesses'][:-1])
    except ValueError as exc:
        if str(exc)!='WITNESS_COUNT':raise ValueError(('WRONG_REASON',str(exc)))
        controls['missing_witness_count']='WITNESS_COUNT'
    else:raise ValueError('MUTATION_ACCEPTED')
    out={'source_receipt_sha256':SOURCE[1],'hyperplane_receipt_sha256':HYPER[1],
         'planes_total':counts[0],'hyperplane_covered':counts[1],'local_rank_three_covered':counts[2],
         'direct_exceptional_3dim_clique_lifts_checked':counts[3],'nonzero_conflict_differences_checked':7*counts[3],
         'all_checked':True,'mutation_controls':controls,
         'limits':'Exact plane coverage and explicit clique lifts only; local section and coset-tiling implications are written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
