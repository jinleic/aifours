#!/usr/bin/env python3
"""Independent ambient-GF(2) quotient enumeration for the f80 review.

The 30 columns are occurrence bits, not the author's 20 code parameters.
The quotient consists of ten triangle checks and seven independent local
checks.  Each bad class is the image of an explicitly nonzero vertex symbol
plus arbitrary non-neighbour bits.  All 2^17 quotient elements are inspected.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import subprocess

TRI = ((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),
       (3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
NEI = {1:{2,3,4,5,6,7}, 2:{1,3,7,9,10}, 3:{1,2,4,8,9},
       4:{1,3,5,8,10}, 5:{1,4,6,9,10}, 6:{1,5,7,8,9},
       7:{1,2,6,8,10}, 8:{3,4,6,7,9,10}, 9:{2,3,5,6,8},
       10:{2,4,5,7,8}}
V = tuple(range(1,11))
OCC = {v:tuple(j for j,t in enumerate(TRI) if v in t) for v in V}
COORD = [(v,j) for v in V for j in OCC[v]]
POS = {x:i for i,x in enumerate(COORD)}
TROWS = [sum(1 << POS[v,j] for v in TRI[j]) for j in range(10)]


def reduced_basis(rows, width=30):
    rows = list(rows)
    n = 0
    for bit in range(width-1, -1, -1):
        pivot = next((i for i in range(n,len(rows)) if rows[i] & (1<<bit)), None)
        if pivot is None:
            continue
        rows[n],rows[pivot] = rows[pivot],rows[n]
        for i in range(len(rows)):
            if i != n and rows[i] & (1<<bit):
                rows[i] ^= rows[n]
        n += 1
        if n == len(rows):
            break
    return tuple(rows[:n])


def rank(rows):
    return len(reduced_basis(rows))


def selected_components(indices):
    """Intersecting triangles belong to one full-triangle component."""
    pending = set(indices)
    pieces = []
    while pending:
        t = pending.pop()
        part = {t}
        vertices = set(TRI[t])
        while True:
            added = {j for j in pending if vertices.intersection(TRI[j])}
            if not added:
                break
            pending -= added
            part |= added
            for j in added:
                vertices.update(TRI[j])
        pieces.append((tuple(sorted(part)),tuple(sorted(vertices))))
    return sorted(pieces)


def classifications():
    result = []
    # With three free components on ten vertices, the 10-vertex case has
    # sizes 3,3,4; K4-freeness makes that exactly four full triangles.
    for ts in combinations(range(10),4):
        pieces = selected_components(ts)
        if sorted(len(vs) for _,vs in pieces) != [3,3,4]:
            continue
        choices = {v:tuple(j for j in OCC[v] if j in ts) for v in V}
        result.append(('cover',ts,None,None,choices))
    # The 9-vertex case has three disjoint triangles and a forced vertex.
    for ts in combinations(range(10),3):
        pieces = selected_components(ts)
        if sorted(len(vs) for _,vs in pieces) != [3,3,3]:
            continue
        covered = set().union(*(set(TRI[j]) for j in ts))
        missing = next(iter(set(V)-covered))
        for mask in range(1,8):
            choices = {v:tuple(j for k,j in enumerate(OCC[v])
                              if (mask>>k)&1) if v==missing
                       else tuple(j for j in OCC[v] if j in ts) for v in V}
            result.append(('packing',ts,missing,mask,choices))
    return result


def enumerate_case(case):
    kind,ts,missing,mask,choices = case
    local = [sum(1<<POS[v,j] for j in choices[v]) for v in V]
    assert all(local)
    checks = TROWS[:]
    for row in local:
        if rank(checks+[row]) > len(checks):
            checks.append(row)
    assert len(checks)==17 and rank(checks)==17
    images = [rank(checks+[1<<POS[v,j] for j in OCC[v]])-17 for v in V]
    assert images == [2]*10

    # q is the row-check vector of the ambient coordinate; p is its actual
    # ten-bit g pattern.  Build the induced linear map q -> p by spanning
    # independent columns.  This does not use the author's quotient code.
    qcol = [sum(((row>>k)&1)<<i for i,row in enumerate(checks)) for k in range(30)]
    pcol = [sum(((row>>k)&1)<<i for i,row in enumerate(local)) for k in range(30)]
    qpattern = [-1]*(1<<17)
    qpattern[0] = 0
    space = [0]
    for q,p in zip(qcol,pcol):
        if qpattern[q] >= 0:
            assert qpattern[q] == p
            continue
        new = [old^q for old in space]
        for old,fresh in zip(space,new):
            assert qpattern[fresh] < 0
            qpattern[fresh] = qpattern[old]^p
        space.extend(new)
    assert len(space)==(1<<17) and -1 not in qpattern
    fibers = Counter(qpattern)
    assert len(fibers)==1024 and set(fibers.values())=={128}

    forbidden = set()
    individual_sizes = []
    for v in V:
        outside = set(V)-NEI[v]-{v}
        others = {0}
        for u in sorted(outside):
            for j in OCC[u]:
                q = qcol[POS[u,j]]
                others |= {x^q for x in tuple(others)}
        own = [qcol[POS[v,j]] for j in OCC[v]]
        vertex_bad = set()
        for symbol in range(1,8):
            q = 0
            for i in range(3):
                if symbol & (1<<i):
                    q ^= own[i]
            vertex_bad.update(q^x for x in others)
        individual_sizes.append(len(vertex_bad))
        forbidden.update(vertex_bad)
    assert 0 not in forbidden
    zero = []
    single = {v:[] for v in V}
    for q,pat in enumerate(qpattern):
        if q in forbidden:
            continue
        if pat == 0:
            zero.append(q)
        elif pat.bit_count()==1:
            single[pat.bit_length()].append(q)
    single = {v:qs for v,qs in single.items() if qs}
    assert zero == [0] and len(single)<=2
    return {
        'kind':kind, 'selected_triangles':list(ts), 'remaining_vertex':missing,
        'remaining_vertex_local_mask':mask,
        'local_parity_masks_30bit':local,
        'kernel_dimension':30-len(checks), 'vertex_image_ranks':images,
        'distinct_g_patterns':len(fibers), 'classes_per_pattern':128,
        'all_quotient_classes':len(space),
        'isolated_image_sizes_by_vertex':individual_sizes,
        'forbidden_quotient_classes':len(forbidden),
        'zero_pattern_compatible_q':zero,
        'compatible_singleton_vertices':sorted(single),
        'compatible_singleton_counts':{str(v):len(qs) for v,qs in single.items()},
        'compatible_singleton_quotients':{str(v):qs for v,qs in single.items()},
        'annihilator_rref':list(reduced_basis(checks)),
    }


def main():
    assert len(COORD)==30 and all(len(OCC[v])==3 for v in V)
    assert all((u in NEI[v]) == (v in NEI[u]) for u in V for v in V)
    assert all(all(u in NEI[v] for v,u in combinations(t,2)) for t in TRI)
    cliques4 = [vs for vs in combinations(V,4)
                if all(u in NEI[v] for v,u in combinations(vs,2))]
    assert len(cliques4)==0 and rank(TROWS)==10
    triangles_in_graph = [vs for vs in combinations(V,3)
                          if all(u in NEI[v] for v,u in combinations(vs,2))]
    cases = classifications()
    assert sum(c[0]=='cover' for c in cases)==5
    assert sum(c[0]=='packing' for c in cases)==56
    records = [enumerate_case(case) for case in cases]
    unique_annihilators = len({tuple(r['annihilator_rref']) for r in records})
    # Compare invariant counts with the pinned author's receipt, rather than
    # importing or executing the author's code.  Coordinates need not agree.
    root = Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus')
    author = json.loads((root/'frontier-20261028-rank13-all-local-subcodes-result.json').read_text())
    assert len(author['case_records']) == len(records)
    for got,ref in zip(records,author['case_records']):
        assert (got['kind'],got['selected_triangles'],got['remaining_vertex'],got['remaining_vertex_local_mask']) == (ref['kind'],ref['selected_triangles'],ref['remaining_vertex'],ref['remaining_vertex_local_mask'])
        assert got['kernel_dimension']==ref['K_rank']
        assert got['vertex_image_ranks']==ref['vertex_image_ranks']
        assert got['forbidden_quotient_classes']==ref['forbidden_quotient_classes']
        assert ref['zero_pattern_allowed']==[[0,0]]
        assert got['compatible_singleton_vertices']==ref['allowed_singleton_vertices']
        assert got['compatible_singleton_counts']==ref['allowed_singleton_counts']
    fixed = records[0]
    assert fixed['selected_triangles']==[0,3,6,9]
    assert fixed['forbidden_quotient_classes']==20003
    assert fixed['compatible_singleton_vertices']==[1,9]
    assert fixed['compatible_singleton_counts']=={'1':8,'9':4}
    old = json.loads((root/'frontier-20261028-rank13-local-parity-obstruction-result.json').read_text())
    # First ten quotient bits are triangle syndromes in both encodings.
    got_s = sorted((int(v),q & 1023) for v,qs in fixed['compatible_singleton_quotients'].items() for q in qs)
    old_s = sorted((v,s) for v,s,r in old['g_singleton_compatible_cosets'])
    assert got_s==old_s
    assert 7**5>2**14
    assert sum(sorted(x.bit_count() for x in range(1<<10))[:16])==20
    result = {
        'clock_observed_before_receipt_write':subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip(),
        'method':'ambient 30-bit parity-check quotient; exhaustive non-neighbour images and all quotient patterns',
        'graph_triangle_count':len(triangles_in_graph), 'graph_K4_count':len(cliques4),
        'triangle_check_rank':rank(TROWS),
        'four_triangle_cover_representations':5,
        'three_triangle_packings':8, 'masks_per_packing':7,
        'equality_representations':len(records), 'distinct_K_annihilators':unique_annihilators,
        'author_receipt_invariants_match_in_all_cases':True,
        'fixed_singleton_vertex_and_syndrome_match':True,
        'forbidden_size_histogram':dict(sorted(Counter(r['forbidden_quotient_classes'] for r in records).items())),
        'compatible_singleton_vertex_count_histogram':dict(sorted(Counter(len(r['compatible_singleton_vertices']) for r in records).items())),
        'integer_comparison':{'7^5':7**5,'2^14':2**14},
        'minimum_weight_of_16_distinct_patterns':20,
        'cases':records,
    }
    dest=Path(__file__).with_name('independent-enumeration-result.json')
    with dest.open('x',encoding='utf-8') as f:
        json.dump(result,f,indent=2,sort_keys=True)
        f.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))


if __name__ == '__main__':
    main()
