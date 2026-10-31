#!/usr/bin/env python3
"""Independent RREF/subspace-span replay of the 192-state character gate."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-coset192-character-enumeration-result.json','598e486ee42e05f99768e7bd4fa53278b12dffc7ba1577fe2eb7c02e59cff624')
OUT=ROOT/'frontier-20261028-coset192-character-independent-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
V=tuple(range(1,11));EDGES={tuple(sorted((u,v))) for u in V for v in N[u]}
GENS=((8,10,7,6,9,3,4,1,2,5),(1,5,6,7,2,3,4,8,9,10))
REPS=((1,2),(1,3),(2,3),(2,9),(3,4))


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError('HASH')
    return json.loads(raw)


def spaces_rref():
    out=[];all_count=0
    for p,q in combinations(range(8),2):
        a=[j for j in range(p+1,8) if j!=q];b=list(range(q+1,8))
        for av in range(1<<len(a)):
            x=(1<<p)|sum(1<<j for k,j in enumerate(a) if av>>k&1)
            for bv in range(1<<len(b)):
                y=(1<<q)|sum(1<<j for k,j in enumerate(b) if bv>>k&1)
                all_count+=1;R=frozenset((0,x,y,x^y))
                if all(not z or z.bit_count()>=3 for z in R):out.append(R)
    if all_count!=10795 or len(out)!=6769 or len(set(out))!=6769:raise ValueError(('RREF',all_count,len(out)))
    return out


def span(mask,R):
    vals=set(R)
    for i in range(8):
        if mask>>i&1:vals|={v^(1<<i) for v in tuple(vals)}
    return vals


def replay(edge,spaces):
    a,b=edge;others=[v for v in V if v not in edge];idx={v:i for i,v in enumerate(others)}
    ma=sum(1<<idx[v] for v in N[a] if v in idx);mb=sum(1<<idx[v] for v in N[b] if v in idx)
    neigh=[sum(1<<idx[w] for w in N[v] if w in idx) for v in others]
    both=[a in N[v] and b in N[v] for v in others]
    base=raw_signs=valid=0
    for R in spaces:
        spans=[span(m,R) for m in neigh]
        if any(not both[i] and (1<<i) not in spans[i] for i in range(8)):continue
        base+=1
        candidates=(span(ma,R)&span(mb,R))-set(R);raw_signs+=len(candidates)
        for t in candidates:
            if all(not both[i] or (1<<i) in spans[i] or ((1<<i)^t) in spans[i] for i in range(8)):valid+=1
    return {'edge':list(edge),'baseline_relation_survivors':base,'raw_nonzero_sign_vectors':raw_signs,'solutions':valid}


def edge_orbits():
    for p in GENS:
        if set(p)!=set(V) or {tuple(sorted((p[a-1],p[b-1]))) for a,b in EDGES}!=EDGES:raise ValueError('AUTOMORPHISM')
    unvisited=set(EDGES);out=[]
    while unvisited:
        e=min(unvisited);orb={e};queue=[e]
        while queue:
            a,b=queue.pop()
            for p in GENS:
                f=tuple(sorted((p[a-1],p[b-1])))
                if f not in orb:orb.add(f);queue.append(f)
        out.append(sorted(orb));unvisited-=orb
    if [x[0] for x in out]!=list(REPS) or [len(x) for x in out]!=[4,8,8,4,2]:raise ValueError('EDGE_ORBITS')
    return out


def main():
    src=pin(SOURCE)
    if src['graph_neighbors']!={str(v):list(N[v]) for v in V} or src['edges_checked']!=26 or src['total_solutions']!=0:raise ValueError('SOURCE')
    data={tuple(x['edge']):x for x in src['edge_results']}
    if set(data)!=EDGES:raise ValueError('EDGE_COVER')
    orbits=edge_orbits();spaces=spaces_rref();checks=[]
    for orbit in orbits:
        ref=data[orbit[0]]
        if any((data[e]['baseline_relation_survivors'],data[e]['exceptional_sign_cosets_tested'],len(data[e]['solutions'])) != (ref['baseline_relation_survivors'],ref['exceptional_sign_cosets_tested'],0) for e in orbit):raise ValueError('ORBIT_COUNTS')
        r=replay(orbit[0],spaces)
        if r['baseline_relation_survivors']!=ref['baseline_relation_survivors'] or r['raw_nonzero_sign_vectors']!=4*ref['exceptional_sign_cosets_tested'] or r['solutions']!=0:raise ValueError(('MISMATCH',r,ref))
        checks.append(r)
    # Basic span controls with two independent 3-bit relations.
    R=frozenset((0,7,56,63));controlspan=span(0,R)
    if 1 in controlspan or 1 not in span(1,R) or len(R)!=4:raise ValueError('SPAN_CONTROL')
    out={'source_receipt_sha256':SOURCE[1],'relation_space_count':len(spaces),'edge_orbit_sizes':[len(x) for x in orbits],
         'representatives_replayed':checks,'raw_sign_vectors_per_coset':4,'all_checked':True,
         'controls':{'nonmember_and_added_generator':'passed'},
         'limits':'Exact quotient-space span enumeration only; reduction from group cosets is a separate written argument.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
