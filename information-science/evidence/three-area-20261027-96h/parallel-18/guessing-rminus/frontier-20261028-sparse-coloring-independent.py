#!/usr/bin/env python3
"""Independent exhaustive color replay of a pinned sparse R-minus census."""
from hashlib import sha256
from itertools import combinations,product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-sparse-coloring-structure-result.json','75884fb96097853126b328c6308c822a8439bee05c0e94c083e91320e4c3062f')
OUT=ROOT/'frontier-20261028-sparse-coloring-independent-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
V=tuple(range(1,11));E={tuple(sorted((v,w))) for v in V for w in N[v]}


def proper(S,edges,c):
    if set(c)!=set(S) or any(c[v] not in (0,1,2) for v in S):return False
    return all(c[a]!=c[b] for a,b in edges)


def has_three_coloring(S,edges):
    for cs in product(range(3),repeat=len(S)):
        if proper(S,edges,dict(zip(S,cs))):return True
    return False


def main():
    raw=(ROOT/SOURCE[0]).read_bytes()
    if sha256(raw).hexdigest()!=SOURCE[1]:raise ValueError('HASH')
    src=json.loads(raw)
    if src['graph_neighbors']!={str(v):list(N[v]) for v in V} or src['edge_count']!=26 or len(E)!=26:raise ValueError('GRAPH')
    declared=src['exact_census'];wheels=declared['wheels'];by_set={tuple(w['vertices']):w for w in wheels}
    if len(by_set)!=4:raise ValueError('WHEELS')
    checked=0;noncolor=[]
    for n in range(7):
        for S in combinations(V,n):
            local={e for e in E if set(e)<=set(S)};checked+=1
            if not has_three_coloring(S,local):noncolor.append(S)
    if checked!=848 or set(noncolor)!=set(by_set):raise ValueError(('CENSUS',noncolor))
    wheel_edges=[];controls={};deletion_checks=0
    for S in noncolor:
        w=by_set[S];local={e for e in E if set(e)<=set(S)};wheel_edges.append(local)
        if len(S)!=6 or len(local)!=10 or {tuple(e) for e in w['edges']}!=local:raise ValueError('EDGES')
        deg={v:sum(v in e for e in local) for v in S};hub=w['hub']
        if deg[hub]!=5 or sorted(deg.values())!=[3,3,3,3,3,5]:raise ValueError('DEGREES')
        rim=set(S)-{hub};re={e for e in local if hub not in e}
        if len(re)!=5 or any(sum(v in e for e in re)!=2 for v in rim):raise ValueError('RIM')
        tri={T for T in combinations(S,3) if all(tuple(e) in local for e in combinations(T,2))}
        if len(tri)!=5 or tri!={tuple(T) for T in w['triangles']}:raise ValueError('TRIANGLES')
        seen=set()
        for record in w['edge_deletion_colorings']:
            e=tuple(record['edge']);seen.add(e);c={int(k):v for k,v in record['coloring'].items()}
            if e not in local or not proper(S,local-{e},c):raise ValueError('DELETION_COLOR')
            deletion_checks+=1
            u,v=next(iter(local-{e}));mut=dict(c);mut[u]=mut[v]
            if proper(S,local-{e},mut):raise ValueError('MUTATION_NOT_REJECTED')
        if seen!=local:raise ValueError('DELETION_COVERAGE')
    overlap=[[len(a&b) for b in wheel_edges] for a in wheel_edges]
    if any(overlap[i][j]>5 for i in range(4) for j in range(i)):raise ValueError('OVERLAPS')
    controls['same_color_edge_mutations']='rejected on all 40 witnesses'
    out={'source_receipt_sha256':SOURCE[1],'induced_subgraphs_checked':checked,
         'noncolorable_vertex_sets':[list(S) for S in noncolor],'noncolorable_count':4,
         'wheel_edge_deletion_witnesses_checked':deletion_checks,'wheel_triangles_each':5,
         'maximum_distinct_wheel_edge_overlap':max(overlap[i][j] for i in range(4) for j in range(i)),
         'all_checked':True,'mutation_controls':controls,
         'limits':'Exact graph census only; the general support-to-coloring argument is written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
