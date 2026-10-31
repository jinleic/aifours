#!/usr/bin/env python3
"""Independent RREF-plane coverage bridge for the all-affine-plane entropy claim.
Usage: python3 script.py OUT.json
Pins prior exact identity receipts; does NOT claim to re-prove their written
mathematical callers. Enumerates every rank-two binary subspace by RREF bases,
replays the prior category predicates, and compares the unresolved SET (not
just its size) with the exact orbits of all 515 covered colorings. No producer
module is imported. No DFZ or two-syndrome entropy theorem is used.
"""
from collections import Counter
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parent
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
GEN=({6},{7},{2,5},{9,10},{1,2,10},{1,5,9},{5,8,9},{2,8,10})
CLASSES='frontier-20261029-residual-plane-colorings-v1.json';CLASS_SHA='103658a2febb098f0949c4fe010624ff7d20328d93f217352967e9eeb80ff956'
MIXED='frontier-20261028-mixed-visibility-certs-part3.json';MIXED_SHA='1b6194041f3a98b3b79313901cd2c2d3494790a8dc830fafda109a92970066fb'
MIXED_RECEIPT='frontier-20261028-mixed-visibility-check-part3-result.json';MIXED_RECEIPT_SHA='f01ca0c8a1c653998ca7552168e6b776c391e55da4da5c8776194d6aebf1e3b8'
BUNDLES=[{'certificates': 'frontier-20261029-plane-functional-certs-part2.json', 'certificates_sha256': '89132067417217f5ae4240f4fbce20da7d4befbdbf69ef25c03118e45e4dc0fb', 'receipt': 'frontier-20261029-plane-functional-check-part2-result.json', 'receipt_sha256': '8e3963fef841c8bac5cf2c68ff5c99f585f9c7bebf4fd01f2e239780c14678ee', 'count': 197}, {'certificates': 'frontier-20261029-plane-functional-certs-part3.json', 'certificates_sha256': '0f7cbace8039d12959791781acdede47ec4430c7eebacd927667d63ec295241d', 'receipt': 'frontier-20261029-plane-functional-check-part3-result.json', 'receipt_sha256': 'd6f11ce2463a952260b85d487e5785c32cf3a4464b41e4a2ecb47b4f6c45306f', 'count': 295}, {'certificates': 'frontier-20261029-plane-functional-direct-recovered-certs-v1.json', 'certificates_sha256': '65e6308cc3e32fa5e62fb022a3ff57796d9643c3b434db5e3a2b2e1c3cbb7378', 'receipt': 'frontier-20261029-plane-functional-direct-recovered-check-v1.json', 'receipt_sha256': '1f572c5c506418713f42a8132d2ee6a344e818107287fbb6c85f1e4c9fa6ddfb', 'count': 3}, {'certificates': 'frontier-20261029-single-functional-local-certs-all20-v1.json', 'certificates_sha256': 'c129b79abcf916afb8a91d4145e6bb9316d0a3968d919f92beb516bdadf5450d', 'receipt': 'frontier-20261029-single-functional-local-certs-all20-check-v1.json', 'receipt_sha256': '5dfeb0f85cb1c4fbc40d424e0e59b35f483baae24f29c990e53be981af6c7e60', 'count': 20}]

def pinned(path,expected):
    data=(ROOT/path).read_bytes()
    if sha256(data).hexdigest()!=expected:raise ValueError(('HASH',path))
    return json.loads(data)

def subsets(mask):
    u=mask;count=0
    while True:
        yield u;count+=1
        if not u:break
        u=(u-1)&mask
    if count!=(1<<mask.bit_count()):raise ValueError('SUBSET_COVERAGE')

def plane_from_coloring(text):
    if len(text)!=10 or any(c not in '-012' for c in text):raise ValueError('COLORING')
    a=sum(1<<i for i,c in enumerate(text) if c in '02');b=sum(1<<i for i,c in enumerate(text) if c in '12')
    if not a or not b or a==b:raise ValueError('RANK_TWO_COLORING')
    return tuple(sorted((a,b,a^b)))

def move_mask(mask,permutation):return sum(1<<permutation[i] for i in range(10) if mask>>i&1)
def plane_digest(planes):
    h=sha256()
    for plane in sorted(planes):
        for value in plane:h.update(value.to_bytes(2,'little'))
    return h.hexdigest()

def residual_match(actual,claimed):
    if actual!=claimed:raise ValueError('EXACT_RESIDUAL_SET_MISMATCH')

def proof_match(names,classes):
    if len(names)!=len(classes) or len(set(names))!=len(names) or set(names)!=set(classes):raise ValueError('EXACT_PROOF_CLASS_COVERAGE')

def rref_planes():
    for i in range(9):
        for j in range(i+1,10):
            free1=sum(1<<k for k in range(i+1,10) if k!=j);free2=sum(1<<k for k in range(j+1,10))
            for u in subsets(free1):
                a=(1<<i)|u
                for v in subsets(free2):
                    b=(1<<j)|v;yield tuple(sorted((a,b,a^b)))

def main():
    t=time.monotonic();classes_doc=pinned(CLASSES,CLASS_SHA);classes=classes_doc['colorings'];proof_names=[];proof_receipts=[]
    for spec in BUNDLES:
        doc=pinned(spec['certificates'],spec['certificates_sha256']);receipt=pinned(spec['receipt'],spec['receipt_sha256'])
        if not receipt['all_checked'] or receipt['count']!=spec['count'] or receipt['certificates_sha256']!=spec['certificates_sha256'] or len(doc['certificates'])!=spec['count']:raise ValueError('PROOF_RECEIPT_BINDING')
        for cert in doc['certificates']:proof_names.append(''.join('-' if c is None else str(c) for c in cert['colors']))
        proof_receipts.append(spec)
    proof_match(proof_names,classes)
    mixed=pinned(MIXED,MIXED_SHA);mr=pinned(MIXED_RECEIPT,MIXED_RECEIPT_SHA)
    if not mr['all_checked'] or mr['certificates_sha256']!=MIXED_SHA or mr['certificates_checked']!=len(mixed['certificates']):raise ValueError('MIXED_RECEIPT_BINDING')
    E={frozenset((v,u)) for v in N for u in N[v]};lookup={tuple(sorted(T)):i for i,T in enumerate(TRI)}
    if len(E)!=26 or any(any(u!=v and u not in N[v] for u in T) for T in TRI for v in T):raise ValueError('GRAPH_TRIANGLES')
    factor_actions=[];vertex_actions=[]
    for p in P:
        if sorted(p)!=list(range(1,11)) or {frozenset(p[v-1] for v in e) for e in E}!=E:raise ValueError('GRAPH_ACTION')
        moved=[tuple(sorted(p[v-1] for v in T)) for T in TRI]
        if set(moved)!=set(lookup):raise ValueError('FACTOR_ACTION')
        factor_actions.append(tuple(lookup[T] for T in moved));vertex_actions.append(tuple(v-1 for v in p))
    if any(tuple(p[q[i]-1] for i in range(10)) not in P for p in P for q in P):raise ValueError('FOUR_ACTION_CLOSURE')
    gen_images={frozenset(p[v-1] for v in g) for p in P for g in ({6},{2,5},{1,2,10})}
    if gen_images!={frozenset(g) for g in GEN}:raise ValueError('VISIBILITY_GENERATOR_TRANSPORT')
    claimed=set();orbit_sizes=Counter()
    for text in classes:
        base=plane_from_coloring(text);orbit={tuple(sorted(move_mask(x,f) for x in base)) for f in factor_actions}
        if claimed&orbit:raise ValueError('DUPLICATE_CLASS_PLANE_ORBIT')
        claimed.update(orbit);orbit_sizes[len(orbit)]+=1
        transformed=[]
        for f in factor_actions:
            for cp in permutations(range(3)):
                y=['-']*10
                for i,c in enumerate(text):y[f[i]]='-' if c=='-' else str(cp[int(c)])
                transformed.append(''.join(y))
        if text!=min(transformed):raise ValueError('NONCANONICAL_COLORING')
    if len(classes)!=515 or len(claimed)!=1905:raise ValueError('CLASS_CARDINALITY')
    table={}
    for cert in mixed['certificates']:
        J=cert['J']
        if cert['factors']!=[i+1 for i in range(10) if J>>i&1]:raise ValueError('MIXED_FACTOR_MASK')
        need=sum(1<<(v-1) for v in cert['visibility_required']);table.setdefault(J,[]).append(need)
    fmap=[[move_mask(mask,f) for mask in range(1024)] for f in factor_actions]
    vmap=[[move_mask(mask,p) for mask in range(1024)] for p in vertex_actions]
    vertex_factor_masks=[sum(1<<i for i,T in enumerate(TRI) if v in T) for v in range(1,11)]
    cover=[]
    for J in range(1024):
        used=set().union(*(set(TRI[i]) for i in range(10) if J>>i&1)) if J else set();cover.append(used==set(N))
    gen_masks=[sum(1<<(v-1) for v in g) for g in GEN];census=Counter();universe=set();unresolved=set()
    for plane in rref_planes():
        if plane in universe:raise ValueError('RREF_DUPLICATION')
        universe.add(plane);a,b,c=plane;J=a|b
        if not cover[J]:census['noncover']+=1;continue
        if J.bit_count()==4:census['four_factor_theorem']+=1;continue
        W=sum(1<<v for v,inc in enumerate(vertex_factor_masks) if a&inc and b&inc and c&inc)
        if any(W&g==g for g in gen_masks):census['full_model_lattice']+=1;continue
        hit=False
        for k in range(4):
            J2=fmap[k][J];W2=vmap[k][W]
            if any(W2&need==need for need in table.get(J2,())):hit=True;break
        if hit:census['mixed_certificate']+=1
        else:census['unresolved']+=1;unresolved.add(plane)
    if len(universe)!=174251 or sum(census.values())!=174251:raise ValueError('TOTAL_COUNT')
    if dict(census)!=mr['plane_census']:raise ValueError('PREDECESSOR_CATEGORY_COUNTS')
    residual_match(unresolved,claimed)
    controls={};bad=set(claimed);bad.remove(min(bad));bad.add(min(universe-unresolved))
    if len(bad)!=len(claimed):raise ValueError('CONTROL_SETUP')
    try:residual_match(unresolved,bad)
    except ValueError as e:controls['same_count_wrong_plane_set']=str(e)
    else:raise ValueError('CONTROL')
    try:proof_match(proof_names[:-1],classes)
    except ValueError as e:controls['dropped_proof_class']=str(e)
    else:raise ValueError('CONTROL')
    try:plane_from_coloring('0000000000')
    except ValueError as e:controls['rank_one_fake_plane']=str(e)
    else:raise ValueError('CONTROL')
    report={'checker_source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'class_file_sha256':CLASS_SHA,'mixed_certificate_sha256':MIXED_SHA,'mixed_receipt_sha256':MIXED_RECEIPT_SHA,'proof_receipts':proof_receipts,
       'RREF_planes_checked':len(universe),'predecessor_partition':dict(census),'residual_set_exactly_matched':True,'residual_colorings_with_exact_proofs':len(proof_names),'residual_planes_with_exact_proofs':len(claimed),
       'all_direction_planes_have_named_written_arguments':True,'uncovered_direction_planes':0,'class_orbit_size_counts':dict(orbit_sizes),
       'universe_digest_uint16LE_sorted_triples':plane_digest(universe),'residual_digest_uint16LE_sorted_triples':plane_digest(unresolved),'residual_direction_planes':sorted(unresolved),
       'negative_controls':controls,'elapsed_s':time.monotonic()-t,
       'limits':'This new check establishes exact set coverage and byte bindings to recorded coefficient-identity checks. It does not re-prove or independently review the written proper-subgraph, four-factor, visibility, component-decoder or fixed-factor lifting arguments. No global guessing-number, formal proof, novelty or scientific-adoption claim.'}
    with open(ROOT/sys.argv[1],'x') as f:json.dump(report,f,indent=1);f.write('\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('residual_direction_planes','proof_receipts')},indent=1))
if __name__=='__main__':main()
