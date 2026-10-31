#!/usr/bin/env python3
"""Exact check of two nine-variable Shannon/FD identities and graph orbits."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=('frontier-20261028-nine-active-shannon-certificates-v1.json','b4f8497f9c8400b360f004e9bb7b9f2e209e635e5a1af26dadd9c9e82173153d')
GRAPH=('frontier-20261028-sparse-coloring-structure-result.json','75884fb96097853126b328c6308c822a8439bee05c0e94c083e91320e4c3062f')
OUT=ROOT/'frontier-20261028-nine-active-shannon-independent-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
E={tuple(sorted((u,v))) for u in N for v in N[u]};V=tuple(range(1,11))
GENS=((8,10,7,6,9,3,4,1,2,5),(1,5,6,7,2,3,4,8,9,10))
COLOR={2:0,3:1,4:2,5:0,6:1,7:2,8:0,9:2,10:1}


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def check_cert(cert,missing,target_joint=-3):
    S=tuple(cert['active_vertices']);n=len(S);full=(1<<n)-1;scale=cert['scale']
    if n!=9 or S!=tuple(v for v in V if v!=missing) or cert['missing_vertex']!=missing or not isinstance(scale,int) or scale<=0:raise ValueError('SCOPE')
    vec=[0]*(full+1);seen=set();counts={'cmi':0,'conditional_entropy':0,'fd':0};fdseen=set()
    def add(m,c):
        if m:vec[m]+=c
    for t in cert['terms']:
        kind=t['kind'];i=t['i'];w=t['multiplier']
        if kind not in counts or not isinstance(i,int) or not 0<=i<n or not isinstance(w,int) or not w:raise ValueError('TERM')
        if kind=='cmi':
            j,z=t['j'],t['conditioning_mask'];key=(kind,i,j,z)
            if not isinstance(j,int) or not i<j<n or not isinstance(z,int) or not 0<=z<=full or z&((1<<i)|(1<<j)) or w<0:raise ValueError('CMI')
            add(z|1<<i,w);add(z|1<<j,w);add(z|1<<i|1<<j,-w);add(z,-w)
        elif kind=='conditional_entropy':
            key=(kind,i)
            if w<0:raise ValueError('MONOTONE')
            add(full,w);add(full^(1<<i),-w)
        else:
            key=(kind,i);fdseen.add(i);nb=sum(1<<j for j,v in enumerate(S) if v in N[S[i]])
            add(nb|1<<i,w);add(nb,-w)
        if key in seen:raise ValueError('DUPLICATE')
        seen.add(key);counts[kind]+=1
    if fdseen!=set(range(n)):raise ValueError('FD_COVER')
    for i in range(n):add(1<<i,-2*scale)
    add(full,-target_joint*scale)
    residual=[(i,x) for i,x in enumerate(vec) if x]
    if residual:raise ValueError(('COEFFICIENT_RESIDUAL',residual[:5]))
    return {'missing_vertex':missing,'scale':scale,'row_counts':counts,
            'all_shannon_coefficients_positive':True,'fd_equalities':len(fdseen),'coefficient_coordinates_checked':full,
            'coefficient_residual_nonzero':0}


def group(edges=E):
    for p in GENS:
        if set(p)!=set(V) or {tuple(sorted((p[a-1],p[b-1]))) for a,b in edges}!=edges:raise ValueError('NOT_AUTOMORPHISM')
    identity=tuple(V);seen={identity};queue=[identity]
    while queue:
        p=queue.pop()
        for g in GENS:
            q=tuple(g[p[i]-1] for i in range(10))
            if q not in seen:seen.add(q);queue.append(q)
    orbits=[];unseen=set(V)
    while unseen:
        v=min(unseen);o={p[v-1] for p in seen};orbits.append(sorted(o));unseen-=o
    if len(seen)!=8 or orbits!=[[1,8],[2,5,9,10],[3,4,6,7]]:raise ValueError(('ORBIT',orbits,len(seen)))
    return {'group_order':len(seen),'vertex_orbits':orbits}


def coloring():
    S=set(V)-{1}
    if set(COLOR)!=S or any(x not in (0,1,2) for x in COLOR.values()) or any(COLOR[a]==COLOR[b] for a,b in E if a in S and b in S):raise ValueError('COLOR')
    return {'missing_vertex':1,'proper_three_coloring':COLOR}


def main():
    certs=pin(CERT);graph=pin(GRAPH)
    if graph['graph_neighbors']!={str(v):list(N[v]) for v in V} or graph['edge_count']!=26:raise ValueError('GRAPH_BINDING')
    a=check_cert(certs['2'],2);b=check_cert(certs['3'],3);aut=group();col=coloring();controls={}
    bad=json.loads(json.dumps(certs['2']));bad['terms'][0]['multiplier']+=1
    try:check_cert(bad,2)
    except ValueError:controls['changed_shannon_multiplier']='rejected'
    else:raise ValueError('CONTROL')
    bad=json.loads(json.dumps(certs['3']));fd=next(t for t in bad['terms'] if t['kind']=='fd');fd['multiplier']+=1
    try:check_cert(bad,3)
    except ValueError:controls['changed_fd_multiplier']='rejected'
    else:raise ValueError('CONTROL')
    try:check_cert(certs['2'],2,target_joint=-4)
    except ValueError:controls['changed_target']='rejected'
    else:raise ValueError('CONTROL')
    try:group(E-{(1,2)})
    except ValueError:controls['deleted_graph_edge']='rejected'
    else:raise ValueError('CONTROL')
    out={'certificates_sha256':CERT[1],'graph_census_sha256':GRAPH[1],'exact_certificates':[a,b],
         'automorphisms':aut,'three_color_case':col,'all_checked':True,'mutation_controls':controls,
         'limits':'Exact Shannon/FD identities for G-2 and G-3 and graph orbit/color checks. Conditional lifting to ten variables is a separate written proof.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
