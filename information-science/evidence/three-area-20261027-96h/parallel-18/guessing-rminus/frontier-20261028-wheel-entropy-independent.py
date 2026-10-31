#!/usr/bin/env python3
"""Check one integer Shannon/FD identity and its four R-minus wheel embeddings."""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=('frontier-20261028-wheel-entropy-certificate-v1.json','520fb9c6db778e795729d3671fa3a611b9f8e418da649d4fb31e2238944eff49')
CENSUS=('frontier-20261028-sparse-coloring-independent-result.json','5994e7fbec78f4fa864e713438e28d9676a107bf4a5e66df9044fe3103863eb4')
OUT=ROOT/'frontier-20261028-wheel-entropy-independent-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
E={tuple(sorted((v,w))) for v in N for w in N[v]}
MAPS=((3,1,2,9,8,4),(7,1,2,10,8,6),(4,1,3,8,10,5),(6,1,5,9,8,7))


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def verify(cert,maps=MAPS,target_joint=-3):
    if cert['variables']!=['H','R1','R2','R3','R4','R5']:raise ValueError('VARIABLES')
    expected=[62]+[1|(1<<(1+i%5))|(1<<(1+(i-2)%5)) for i in range(1,6)]
    masks=cert['neighbor_masks']
    if masks!=expected:raise ValueError(('NEIGHBORS',masks,expected))
    terms=cert['cmi_terms'];vec=[Fraction(0)]*64;seen=set();total=Fraction(0)
    if len(terms)!=22:raise ValueError('CMI_COUNT')
    def add(mask,c):
        if mask:vec[mask]+=c
    for t in terms:
        i,j,z=t['i'],t['j'],t['conditioning_mask'];w=Fraction(t['weight'])
        if not (0<=i<j<6 and 0<=z<64) or z&((1<<i)|(1<<j)) or w<=0 or w.denominator!=1 or (i,j,z) in seen:raise ValueError('BAD_CMI')
        seen.add((i,j,z));total+=w
        add(z|1<<i,w);add(z|1<<j,w);add(z|1<<i|1<<j,-w);add(z,-w)
    if total!=25:raise ValueError('WEIGHT_SUM')
    for i,ns in enumerate(masks):add(ns|1<<i,-1);add(ns,1)
    # Subtract the target 2 sum singleton entropies - 3 joint entropy.
    for i in range(6):add(1<<i,-2)
    add(63,-target_joint)
    if any(vec):raise ValueError(('NONZERO_RESIDUAL',[(i,str(v)) for i,v in enumerate(vec) if v]))
    wheel_edges={tuple(sorted((0,i))) for i in range(1,6)}|{tuple(sorted((i,1+i%5))) for i in range(1,6)}
    for mapping in maps:
        if len(set(mapping))!=6:raise ValueError('MAP')
        actual={e for e in E if set(e)<=set(mapping)}
        wanted={tuple(sorted((mapping[a],mapping[b]))) for a,b in wheel_edges}
        if actual!=wanted:raise ValueError(('GRAPH_WHEEL_MAP',mapping))
    return {'positive_cmi_rows':len(terms),'positive_integer_multiplier_sum':str(total),
            'graph_fd_equalities':6,'coefficient_coordinates_checked':63,'coefficient_residual_nonzero':0,
            'wheel_embeddings_checked':len(maps)}


def main():
    cert=pin(CERT);census=pin(CENSUS)
    if not census['all_checked'] or census['noncolorable_count']!=4 or {tuple(sorted(x)) for x in MAPS}!={tuple(x) for x in census['noncolorable_vertex_sets']}:raise ValueError('CENSUS_BINDING')
    checks=verify(cert);controls={}
    bad=json.loads(json.dumps(cert));bad['cmi_terms'][0]['weight']='2'
    try:verify(bad)
    except ValueError:controls['changed_cmi_weight']='rejected'
    else:raise ValueError('CONTROL')
    bad=json.loads(json.dumps(cert));bad['neighbor_masks'][1]^=1<<2
    try:verify(bad)
    except ValueError:controls['changed_fd_neighbors']='rejected'
    else:raise ValueError('CONTROL')
    try:verify(cert,target_joint=-4)
    except ValueError:controls['changed_target_joint']='rejected'
    else:raise ValueError('CONTROL')
    badmaps=list(MAPS);badmaps[0]=(3,1,2,9,4,8)
    try:verify(cert,maps=badmaps)
    except ValueError:controls['changed_wheel_embedding']='rejected'
    else:raise ValueError('CONTROL')
    out={'certificate_sha256':CERT[1],'graph_census_sha256':CENSUS[1],'exact_checks':checks,
         'wheel_vertex_maps':[list(x) for x in MAPS],'all_checked':True,'mutation_controls':controls,
         'limits':'Exact written Shannon/FD identity and four graph embeddings; not an unrestricted all-vertex R-minus inequality or a proof-assistant formalization.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
