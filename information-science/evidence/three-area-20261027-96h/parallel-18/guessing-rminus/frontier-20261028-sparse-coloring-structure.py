#!/usr/bin/env python3
"""Exact small induced-subgraph and sparse 4-critical census for R-minus."""
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-sparse-coloring-structure-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
V=tuple(range(1,11));E={tuple(sorted((v,w))) for v in V for w in N[v]}


def coloring(vertices,edges):
    vertices=tuple(sorted(vertices));adj={v:set() for v in vertices}
    for u,v in edges:
        if u in adj and v in adj:adj[u].add(v);adj[v].add(u)
    colors={}
    def visit(i):
        if i==len(vertices):return {str(k):v for k,v in colors.items()}
        u=vertices[i]
        for c in range(3):
            if all(colors.get(v)!=c for v in adj[u]):
                colors[u]=c;result=visit(i+1)
                if result is not None:return result
        colors.pop(u,None);return None
    return visit(0)


def audit(edges):
    if any(tuple(sorted((u,v))) not in edges for u in V for v in N[u]):raise ValueError('MISSING_GRAPH_EDGE')
    wheels=[];counts={};tested=0
    for size in range(7):
        counts[str(size)]=0
        for S in combinations(V,size):
            tested+=1;local={e for e in edges if set(e)<=set(S)}
            if coloring(S,local) is None:
                counts[str(size)]+=1
                if size!=6 or len(local)!=10:raise ValueError(('UNEXPECTED_NON3COLOR',S,len(local)))
                deg={v:sum(v in e for e in local) for v in S}
                if sorted(deg.values())!=[3,3,3,3,3,5]:raise ValueError('WHEEL_DEGREES')
                hub=next(v for v in S if deg[v]==5)
                rim=[v for v in S if v!=hub];rim_edges={e for e in local if hub not in e}
                if len(rim_edges)!=5 or any(sum(v in e for e in rim_edges)!=2 for v in rim):raise ValueError('NOT_FIVE_CYCLE')
                triangles=[T for T in combinations(S,3) if all(tuple(sorted(e)) in local for e in combinations(T,2))]
                if len(triangles)!=5:raise ValueError('WHEEL_TRIANGLES')
                edge_deletions=[]
                for e in sorted(local):
                    witness=coloring(S,local-{e})
                    if witness is None:raise ValueError(('NONCRITICAL_EDGE',S,e))
                    edge_deletions.append({'edge':list(e),'coloring':witness})
                wheels.append({'vertices':list(S),'hub':hub,'edges':[list(e) for e in sorted(local)],
                               'triangles':[list(T) for T in triangles],'edge_deletion_colorings':edge_deletions})
    if tested!=848 or len(wheels)!=4 or len(edges)!=26:raise ValueError(('CENSUS',tested,len(wheels),len(edges)))
    sets=[set(map(tuple,w['edges'])) for w in wheels]
    overlaps=[[len(a&b) for b in sets] for a in sets]
    if any(overlaps[i][j]>5 for i in range(4) for j in range(i)):raise ValueError('WHEEL_OVERLAP')
    return {'induced_subgraphs_checked':tested,'non_3_colorable_counts_by_order':counts,
            'wheel_count':len(wheels),'wheel_edge_overlap_matrix':overlaps,'wheels':wheels,
            'critical_edge_deletion_colorings':40}


def main():
    if any(v not in N[w] for v in V for w in N[v]):raise ValueError('GRAPH_NOT_SYMMETRIC')
    exact=audit(E);controls={}
    for name,change in [('missing_original_edge',E-{(1,2)}),('added_K4_edge',E|{(2,4)})]:
        try:audit(change)
        except ValueError:controls[name]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',name))
    out={'graph_neighbors':{str(v):list(N[v]) for v in V},'edge_count':len(E),'exact_census':exact,
         'mutation_controls':controls,
         'limits':'Finite graph coloring census only; entropy proof and support-specific edge-selection argument are written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='exact_census'},indent=2))
    print(json.dumps({k:v for k,v in exact.items() if k!='wheels'},indent=2))


if __name__=='__main__':main()
