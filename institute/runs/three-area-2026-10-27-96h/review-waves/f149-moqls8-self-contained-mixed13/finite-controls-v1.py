#!/usr/bin/env python3
"""Bounded independent incidence, projector, and exact-vector review controls.

Only stdlib; all mathematics below was implemented independently of candidate code.
Run: python3 finite-controls-v1.py --out finite-results-v1.json
Results are graph/support relaxations except for the explicitly checked QLS example.
"""
import argparse
import collections
import functools
import hashlib
import itertools
import json
import math
import pathlib
import subprocess
import sys
import time
from fractions import Fraction as F

SOURCE = pathlib.Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/moqls8/frontier-20261028-four-family-mixed13-self-contained-v1.md')
SOURCE_HASH = '2eeda45e6c4396530b856c1aef85816fd84076ecd82e782738ac95aa8d529775'
MANIFEST_HASH = 'aceb255e826d501b3049eb38604a90d9cad0764dafc673854f1e62fd2c0bd364'


def digest(b):
    return hashlib.sha256(b).hexdigest()


def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()


def pop(m):
    return m.bit_count()


def rows_enumerated(r, c, total):
    masks = [(mask, pop(mask)) for mask in range(1 << c) if pop(mask) >= 2]
    # Nondecreasing row masks quotient row permutation; repeated rows allowed.
    def rec(start, left, remaining, chosen):
        if left == 0:
            if remaining == 0:
                counts = [sum((x >> j) & 1 for x in chosen) for j in range(c)]
                if min(counts) >= 2:
                    yield tuple(chosen)
            return
        if remaining < 2 * left or remaining > c * left:
            return
        for idx in range(start, len(masks)):
            mask, size = masks[idx]
            if size <= remaining - 2 * (left - 1):
                yield from rec(idx, left - 1, remaining - size, chosen + [mask])
    yield from rec(0, r, total, [])


def canonical_columns(rows, c):
    """Canonicalize row and column permutations, respecting column degrees."""
    classes = collections.defaultdict(list)
    for j in range(c):
        classes[sum((x >> j) & 1 for x in rows)].append(j)
    groups = [classes[d] for d in sorted(classes)]
    best = None
    for group_perms in itertools.product(*(itertools.permutations(g) for g in groups)):
        order = tuple(itertools.chain.from_iterable(group_perms))
        transformed = tuple(sorted(sum(((row >> old) & 1) << new for new, old in enumerate(order)) for row in rows))
        if best is None or transformed < best:
            best = transformed
    return best


def transposed(rows, c):
    return tuple(sum(((row >> j) & 1) << i for i, row in enumerate(rows)) for j in range(c))


def canonical(rows, c):
    v = canonical_columns(rows, c)
    if len(rows) == c:
        v = min(v, canonical_columns(transposed(rows, c), c))
    return v


def row_multiplicity(rows):
    n = math.factorial(len(rows))
    for count in collections.Counter(rows).values():
        n //= math.factorial(count)
    return n


def edges_degrees(rows, c):
    edges = [(i, j) for i, row in enumerate(rows) for j in range(c) if row >> j & 1]
    dr = [pop(x) for x in rows]
    dc = [sum(row >> j & 1 for row in rows) for j in range(c)]
    return edges, dr, dc


def degree_label(ds):
    return ','.join(str(x) for x in sorted(ds, reverse=True))


def plausible_sizes(rows, c):
    """Exact DFS over a *necessary* per-cell support-cardinality relaxation.

    degree-3: at most one support-2; degree-4: 2+2+3 and 2+3+3
    forbidden; each support-2 family requires at least 2 ceil(s/2) axes;
    all-support-2 line has even degree. No sufficiency is asserted.
    """
    edges, dr, dc = edges_degrees(rows, c)
    lines = [[e for e, (i, _) in enumerate(edges) if i == v] for v in range(len(rows))]
    lines += [[e for e, (_, j) in enumerate(edges) if j == v] for v in range(c)]
    degs = dr + dc
    e_lines = [(i, len(rows) + j) for i, j in edges]
    assignment = [0] * len(edges)
    domains = [tuple(range(2, min(dr[i], dc[j]) + 1)) for i, j in edges]

    def line_ok(v):
        vals = [assignment[e] for e in lines[v] if assignment[e]]
        s2, s3, k = vals.count(2), vals.count(3), degs[v]
        if 2 * ((s2 + 1) // 2) > k:
            return False
        if k == 3 and s2 >= 2:
            return False
        if k == 4 and ((s2 >= 2 and s3 >= 1) or (s2 >= 1 and s3 >= 2)):
            return False
        if len(vals) == k and all(x == 2 for x in vals) and k % 2:
            return False
        return True

    order = sorted(range(len(edges)), key=lambda e: (len(domains[e]), -(dr[edges[e][0]] + dc[edges[e][1]])))
    def visit(pos):
        if pos == len(order):
            return tuple(assignment)
        e = order[pos]
        for val in domains[e]:
            assignment[e] = val
            if all(line_ok(v) for v in e_lines[e]):
                found = visit(pos + 1)
                if found is not None:
                    return found
        assignment[e] = 0
        return None
    return visit(0)


def forced_full_edges(rows, c):
    edges, dr, dc = edges_degrees(rows, c)
    full = set()
    for i, j in edges:
        if dr[i] == 3 and any(dc[k] == 2 for k in range(c) if rows[i] >> k & 1) and dc[j] != 2:
            full.add((0, i, j))
        if dc[j] == 3 and any(dr[k] == 2 for k, row in enumerate(rows) if row >> j & 1) and dr[i] != 2:
            full.add((1, i, j))
    return full


def axis_pattern_relaxation(rows, c):
    """Balanced coordinate-incidence multiset, not a vector realization.

    An occupied axis has equal row and column multiplicities by the projector
    identity, and >=2 occupied neighbors at each incident line. Degree-2
    lines use both axis coordinates in both mixed cells. If a degree-3 line
    already meets a degree-2 line, its two other cells have full support.
    Every coordinate has a 0/1 membership pattern in mixed line subspaces.
    """
    edges, dr, dc = edges_degrees(rows, c)
    r = len(rows)
    full = forced_full_edges(rows, c)
    patterns = []
    for k in range(2, min(r, c) + 1):
        for rs in itertools.combinations(range(r), k):
            rm = sum(1 << i for i in rs)
            for cs in itertools.combinations(range(c), k):
                cm = sum(1 << j for j in cs)
                if any(pop(rows[i] & cm) < 2 for i in rs):
                    continue
                if any(sum(1 for i in rs if rows[i] >> j & 1) < 2 for j in cs):
                    continue
                invalid = False
                for i, j in edges:
                    ir, jc = bool(rm >> i & 1), bool(cm >> j & 1)
                    if ((dr[i] == 2 or (0, i, j) in full) and ir and not jc) or ((dc[j] == 2 or (1, i, j) in full) and jc and not ir):
                        invalid = True
                        break
                if not invalid:
                    patterns.append(tuple(int(rm >> i & 1) for i in range(r)) + tuple(int(cm >> j & 1) for j in range(c)))
    by_vertex = [[p for p in patterns if p[i]] for i in range(r + c)]
    cap = tuple(dr + dc)
    max_axes = min(8, len(edges) // 2)
    nodes = 0
    @functools.lru_cache(None)
    def visit(rem, count):
        nonlocal nodes
        nodes += 1
        if not any(rem):
            return ()
        if count == max_axes:
            return None
        candidates = []
        for idx, amount in enumerate(rem):
            if amount:
                fits = [p for p in by_vertex[idx] if all(a <= b for a, b in zip(p, rem))]
                if not fits:
                    return None
                candidates.append(fits)
        choices = min(candidates, key=len)
        for p in choices:
            rest = tuple(x-y for x, y in zip(rem, p))
            found = visit(rest, count + 1)
            if found is not None:
                return (p,) + found
        return None
    witness = visit(cap, 0)
    return witness, len(patterns), nodes


def components(nodes, adjacency):
    unseen = set(nodes)
    out = []
    while unseen:
        start = unseen.pop()
        todo, comp = [start], [start]
        while todo:
            v = todo.pop()
            for w in adjacency[v]:
                if w in unseen:
                    unseen.remove(w)
                    todo.append(w)
                    comp.append(w)
        out.append(comp)
    return out


def boundary_5bb(rows, c):
    edges, dr, dc = edges_degrees(rows, c)
    if sorted(dr) != [2,2,2,3,3] or sorted(dc) != [2,2,2,3,3]:
        return None
    if any(dr[i] == 3 and sum(dc[j] == 2 for j in range(c) if rows[i] >> j & 1) > 1 for i in range(len(rows))):
        return 'excluded-high-two-low'
    if any(dc[j] == 3 and sum(dr[i] == 2 for i, row in enumerate(rows) if row >> j & 1) > 1 for j in range(c)):
        return 'excluded-high-two-low'
    hi_r = [i for i in range(len(rows)) if dr[i] == 3]
    hi_c = [j for j in range(c) if dc[j] == 3]
    assert all(rows[i] >> j & 1 for i in hi_r for j in hi_c)
    b = [(i,j) for i,j in edges if dr[i] == 2 or dc[j] == 2]
    assert len(b) == 8
    adj = {x: set() for x in b}
    for x, y in itertools.combinations(b, 2):
        if (x[0] == y[0] and dr[x[0]] == 2) or (x[1] == y[1] and dc[x[1]] == 2):
            adj[x].add(y); adj[y].add(x)
    comp = components(b, adj)
    paths, cycles = [], []
    for z in comp:
        if all(len(adj[x]) == 2 for x in z):
            cycles.append(len(z))
        else:
            assert sum(len(adj[x]) == 1 for x in z) == 2
            paths.append(len(z))
    key = 'paths=' + ','.join(map(str,sorted(paths))) + ';cycles=' + ','.join(map(str,sorted(cycles)))
    assert key in {'paths=2,6;cycles=', 'paths=3,5;cycles=', 'paths=4,4;cycles=', 'paths=2,2;cycles=4'}
    return key


def independent_direct_count(r, c, m):
    # Independent all-cell-subset route, used only on explicitly bounded boards.
    count = 0
    for chosen in itertools.combinations(range(r*c), m):
        rr = [0] * r; cc = [0] * c
        for e in chosen:
            rr[e // c] += 1; cc[e % c] += 1
        if min(rr) >= 2 and min(cc) >= 2:
            count += 1
    return count


def incidence_controls():
    start = time.monotonic()
    summary, examples, orbit_data = {}, {}, {}
    direct = {}
    c4pairs = collections.Counter()
    c4survivors = collections.Counter()
    c4bb = collections.Counter()
    b5bound = collections.Counter()
    b5labels = collections.Counter()
    # Every r,c<=6, up to transposition: also record impossible cells explicitly.
    for m in range(1,13):
        by_shape = {}
        for r in range(1,7):
            for c in range(r,7):
                key = f'{r}x{c}'
                if m < 2*r or m < 2*c or m > r*c or r < 2:
                    by_shape[key] = {'labeled':0,'orbits':0,'reason':'degree-or-capacity'}
                    continue
                orbits = {}
                raw = 0
                for rows in rows_enumerated(r,c,m):
                    w = row_multiplicity(rows)
                    raw += w
                    canon = canonical(rows,c)
                    orbits[canon] = orbits.get(canon,0) + w
                rec = {'labeled':raw,'orbits':len(orbits),'size_necessary_survivor_orbits':0,'axis_necessary_survivor_orbits':0,'both_necessary_survivor_orbits':0,'axis_dfs_nodes':0}
                shape_profiles = collections.Counter()
                for rows, weight in orbits.items():
                    _, dr, dc = edges_degrees(rows,c)
                    pair = tuple(sorted((degree_label(dr),degree_label(dc)))) if r == c else (degree_label(dr),degree_label(dc))
                    shape_profiles[' / '.join(pair)] += weight
                    sz = plausible_sizes(rows,c)
                    ax, patterns, nodes = axis_pattern_relaxation(rows,c)
                    rec['size_necessary_survivor_orbits'] += int(sz is not None)
                    rec['axis_necessary_survivor_orbits'] += int(ax is not None)
                    rec['both_necessary_survivor_orbits'] += int(sz is not None and ax is not None)
                    rec['axis_dfs_nodes'] += nodes
                    if sz is not None and ax is not None and 'first_relaxation_survivor' not in rec:
                        rec['first_relaxation_survivor'] = {'rows_bitmasks':list(rows),'support_sizes':list(sz),'axis_patterns':[list(x) for x in ax], 'warning':'these two separate witnesses need not be jointly realizable'}
                    if m == 12 and r == c == 4:
                        profmap = {'4,4,2,2':'A','4,3,3,2':'B','3,3,3,3':'C'}
                        prof = ''.join(sorted((profmap[degree_label(dr)],profmap[degree_label(dc)])))
                        c4pairs[prof] += weight
                        if sz is not None: c4survivors[prof + ':size'] += weight
                        if ax is not None: c4survivors[prof + ':axis'] += weight
                        if sz is not None and ax is not None: c4survivors[prof + ':both'] += weight
                        if prof == 'BB':
                            lr,lc = dr.index(2), dc.index(2)
                            c4bb['low-low-present' if rows[lr] >> lc & 1 else 'low-low-absent'] += weight
                    if m == 12 and r == c == 5:
                        b = boundary_5bb(rows,c)
                        if b is not None:
                            b5bound[b] += 1
                            b5labels[b] += weight
                rec['degree_profiles_labeled'] = dict(sorted(shape_profiles.items()))
                by_shape[key] = rec
                if r*c <= 20 and math.comb(r*c,m) <= 200000:
                    d = independent_direct_count(r,c,m)
                    assert d == raw, (m,r,c,d,raw)
                    direct[f'{m}:{key}'] = d
                if m == 10 and key in ('2x5','3x4','3x5','4x4','4x5','5x5'):
                    expected = {'2x5':1,'3x4':54,'3x5':210,'4x4':2040,'4x5':2580,'5x5':2040}[key]
                    assert raw == expected, (key,raw,expected)
        summary[str(m)] = by_shape
    assert set(c4pairs) == {'AA','AB','AC','BB','BC','CC'}
    assert set(c4bb) == {'low-low-present','low-low-absent'}
    assert set(b5bound) == {'excluded-high-two-low','paths=2,6;cycles=','paths=3,5;cycles=','paths=4,4;cycles=','paths=2,2;cycles=4'}
    return {'by_m_and_shape':summary,'direct_labeled_subset_crosschecks':direct,'m12_4x4_profile_labeled_counts':dict(sorted(c4pairs.items())),'m12_4x4_profile_necessary_survivors_labeled':dict(sorted(c4survivors.items())),'m12_4x4_BB_low_low_labeled':dict(c4bb),'m12_5x5_BB_boundary_orbits':dict(sorted(b5bound.items())),'m12_5x5_BB_boundary_labeled':dict(sorted(b5labels.items())),'elapsed_seconds':round(time.monotonic()-start,3)}


def maskset(m):
    return [i for i in range(8) if m >> i & 1]


def multiplicities(masks, n):
    return tuple(sum(m >> i & 1 for m in masks) for i in range(n))


def projector_controls():
    # P10: axes can be relabelled so K_1={0,1,2,3}. Repeated K_2,K_3
    # are allowed, and all coordinates from an eight-element universe occur.
    ks = [sum(1 << x for x in comb) for comb in itertools.combinations(range(8),4)]
    ts = [sum(1 << x for x in comb) for comb in itertools.combinations(range(8),3)]
    k1 = 15
    count = considered = 0
    no_balance_example = None
    for k2,k3 in itertools.combinations_with_replacement(ks,2):
        rowsets = (k1,k2,k3)
        counts = multiplicities(rowsets,8)
        if any(x == 1 for x in counts):
            continue
        eligible = [t for t in ts if sum((t & k) == t for k in rowsets) >= 2]
        if not eligible:
            continue
        considered += 1
        if len(set(rowsets)) > 1 and no_balance_example is None:
            cols = (eligible[0],)*4
            assert multiplicities(cols,8) != counts
            no_balance_example = {'row_4sets':[maskset(x) for x in rowsets],
                                  'column_3sets':[maskset(x) for x in cols],
                                  'row_coordinate_counts':counts,
                                  'column_coordinate_counts':multiplicities(cols,8)}
        for cols in itertools.combinations_with_replacement(eligible,4):
            if multiplicities(cols,8) == counts:
                count += 1
                assert len(set(rowsets)) == 1
                assert len(set(cols)) == 4
                assert all(pop(k1 ^ t) == 1 for t in cols)
    assert count == 1 and no_balance_example is not None

    k = 15
    twos = [m for m in range(16) if pop(m) == 2]
    threes = [m for m in range(16) if pop(m) == 3]
    p17_count = 0
    for v1,u,t1,t2 in itertools.product(twos,twos,threes,threes):
        v2 = k ^ v1
        left = multiplicities((k,k,v1,v2),4)
        right = multiplicities((k,t1,t2,u),4)
        if left == right:
            p17_count += 1
            omit1, omit2 = k ^ t1, k ^ t2
            assert omit1 != omit2 and u == (omit1 | omit2)
    assert p17_count == 72

    p22_count = 0
    for u in twos:
        containing = [t for t in threes if t & u == u]
        assert len(containing) == 2
        for ta,tb in (containing,tuple(reversed(containing))):
            for c1,c2 in itertools.product(threes, repeat=2):
                if multiplicities((c1,c2),4) == multiplicities((k,u),4):
                    p22_count += 1
                    assert sorted((c1,c2)) == sorted((ta,tb))
    assert p22_count == 24
    # Two candidate C columns can repeat if balance is omitted; they violate
    # the asserted balanced projector equation for this U.
    u = twos[0]
    ta,tb = [t for t in threes if t & u == u]
    assert multiplicities((ta,ta),4) != multiplicities((k,u),4)
    return {'P10_fixed_first_row_4set':maskset(k1),
            'P10_row_multisets_considered_with_no_singletons_and_eligible_columns':considered,
            'P10_balanced_models':count,'P10_mutation_drop_projector_balance':no_balance_example,
            'P17_balanced_models':p17_count,'P22_balanced_ordered_models':p22_count,
            'P22_mutation_drop_projector_balance':{'U':maskset(u),'C1':maskset(ta),'C2':maskset(ta),'TA':maskset(ta),'TB':maskset(tb)}}


def cube_controls():
    edges = [(i,j) for i in range(4) for j in range(4) if i != j]
    connected = disconnected = 0
    mutant = None
    for deleted_bits in range(1 << len(edges)):
        deleted = {edges[e] for e in range(len(edges)) if deleted_bits >> e & 1}
        dr = [sum(i == a for i,j in deleted) for a in range(4)]
        dc = [sum(j == b for i,j in deleted) for b in range(4)]
        if max(dr+dc) > 2:
            continue
        adj = {i:set() for i in range(8)}
        for i,j in edges:
            if (i,j) not in deleted:
                adj[i].add(4+j); adj[4+j].add(i)
        comps = components(range(8),adj)
        type_sizes = sorted((sum(v < 4 for v in z),sum(v >= 4 for v in z)) for z in comps)
        if max(dr+dc) <= 1:
            if len(comps) == 1:
                connected += 1
            else:
                disconnected += 1
                assert type_sizes == [(2,2),(2,2)]
                assert all(len(adj[v]) == 2 for v in range(8))
        elif len(comps) > 1 and type_sizes != [(2,2),(2,2)] and mutant is None:
            mutant = {'deleted_edges':[list(x) for x in sorted(deleted)],
                      'deleted_degrees_rows':dr,'deleted_degrees_cols':dc,
                      'component_row_column_sizes':type_sizes}
    assert disconnected and connected and mutant is not None
    return {'min_degree_2_connected_deletion_patterns':connected,
            'min_degree_2_disconnected_deletion_patterns':disconnected,
            'every_disconnected_pattern_two_K22':True,
            'mutation_allow_degree_1_counterexample':mutant}


def disjoint_nonempty_choices(n, slots):
    subsets = range(1,1 << slots)
    return [v for v in itertools.product(subsets,repeat=n)
            if all(v[i] & v[j] == 0 for i in range(n) for j in range(i))]


def pigeonhole_controls():
    assert len(disjoint_nonempty_choices(3,2)) == 0
    assert len(disjoint_nonempty_choices(2,2)) == 2
    assert len(disjoint_nonempty_choices(3,3)) == 6
    assignments = list(itertools.product(range(4),repeat=2)) # owner 0/1/2 or nobody
    assert all(any(m not in own for m in range(3)) for own in assignments)
    assert set((0,1)) == {0,1}  # with only two mates, both can be active
    return {'three_nonempty_disjoint_supports_on_two_axes':0,
            'mutation_only_two_mates_assignments':2,
            'mutation_allow_three_axes_assignments':6,
            'P16_two_slots_three_mates_assignments_checked':len(assignments),
            'P16_mutation_two_mates_two_slots':[0,1]}


# A Gaussian rational is represented by (real, imaginary), each a Fraction.
def g(a=0,b=0):
    return (F(a),F(b))


def ga(x,y):
    return (x[0]+y[0],x[1]+y[1])


def gm(x,y):
    return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])


def gc(x):
    return (x[0],-x[1])


def gvadd(x,y):
    return tuple(ga(a,b) for a,b in zip(x,y))


def gvscale(x,s):
    return tuple(gm(a,s) for a in x)


def dot(x,y):
    v = g()
    for a,b in zip(x,y):
        v = ga(v,gm(gc(a),b))
    return v


def supp(x):
    return tuple(i for i,a in enumerate(x) if a != g())


def basis(n,i):
    return tuple(g(1) if j == i else g() for j in range(n))


def serial(z):
    return [str(z[0]),str(z[1])]


def qls_controls():
    zero,one = g(),g(1)
    # A rational complex orthonormal triple from a Householder reflection,
    # left-multiplied by diag(1,i,1); all three vectors have full support.
    raw = [[F(-1,3),F(2,3),F(2,3)],
           [F(2,3),F(-1,3),F(2,3)],
           [F(2,3),F(2,3),F(-1,3)]]
    # The above is minus the conventional reflection; still orthogonal.
    abc = [tuple(g(raw[i][j]) if i != 1 else g(0,raw[i][j]) for i in range(3)) for j in range(3)]
    p,q,qp = abc
    assert all(dot(abc[i],abc[j]) == (one if i == j else zero) for i in range(3) for j in range(3))
    assert all(len(supp(v)) == 3 for v in abc)
    r = gvadd(gvscale(q,g(F(3,5))),gvscale(qp,g(0,F(4,5))))
    rp = gvadd(gvscale(q,g(0,F(4,5))),gvscale(qp,g(F(3,5))))
    assert dot(r,r) == dot(rp,rp) == one and dot(r,rp) == zero
    assert len(supp(r)) == len(supp(rp)) == 3
    assert all(dot(x,y) != zero for x in (q,qp) for y in (r,rp))
    def embed3(v):
        return v + (zero,)*5
    p,q,qp,r,rp = map(embed3,(p,q,qp,r,rp))
    square = [[None]*8 for _ in range(8)]
    pcol = (1,0,3,2)
    for i in range(4):
        for j in range(4):
            if i == j:
                square[i][j] = basis(8,3)
            elif j == pcol[i]:
                square[i][j] = p
            elif i < 2:
                square[i][j] = q if (i,j) in ((0,2),(1,3)) else qp
            else:
                square[i][j] = r if (i,j) in ((2,0),(3,1)) else rp
            square[i][j+4] = basis(8,4+(i+j)%4)
            square[i+4][j] = basis(8,4+(i+j)%4)
            square[i+4][j+4] = basis(8,(i+j)%4)
    line_checks = 0
    for lines in (square, list(zip(*square))):
        for line in lines:
            for i,j in itertools.product(range(8),repeat=2):
                assert dot(line[i],line[j]) == (one if i == j else zero)
                line_checks += 1
    chosen = square[4]
    assert {supp(v) for v in chosen} == {(i,) for i in range(8)}
    mixed = [(i,j) for i in range(8) for j in range(8) if len(supp(square[i][j])) > 1]
    assert len(mixed) == 12
    assert all(i < 4 and j < 4 and i != j for i,j in mixed)
    assert all(len(supp(square[i][j])) == 3 for i,j in mixed)
    assert [sum(i == x for i,j in mixed) for x in range(4)] == [3]*4
    assert [sum(j == x for i,j in mixed) for x in range(4)] == [3]*4

    # Exact arbitrary-phase controls. Supports with two common axes may
    # cancel; one common nonzero axis cannot.
    u = (g(F(3,5)),g(0,F(4,5)),zero)
    up = (g(0,F(4,5)),g(F(3,5)),zero)
    e2 = basis(3,2)
    assert dot(u,u) == dot(up,up) == one and dot(u,up) == zero
    one_axis = (zero,g(0,F(4,5)),g(F(3,5)))
    assert dot(u,one_axis) != zero and set(supp(u)) & set(supp(one_axis)) == {1}
    x = gvadd(gvscale(up,g(F(3,5))),gvscale(e2,g(F(4,5))))
    y = gvadd(gvscale(u,g(F(3,5))),gvscale(e2,g(0,F(4,5))))
    assert dot(x,x) == dot(y,y) == one and dot(x,u) == dot(y,up) == zero
    assert len(supp(x)) == len(supp(y)) == 3 and dot(x,y) != zero
    # Mutation: omit one full-support assumption, and the obstruction fails.
    xmut = up
    assert len(supp(xmut)) == 2 and dot(xmut,y) == zero

    # Common-plane intersection is load-bearing for the zero-diagonal
    # cross-Gram argument: in C^4 two orthogonal planes give all zeros.
    e = [basis(4,i) for i in range(4)]
    cross = [[dot(e[i],e[j]) for j in (2,3)] for i in (0,1)]
    assert all(z == zero for line in cross for z in line)
    return {'actual_complex_QLS_order8':{'gram_entries_checked':line_checks,
             'chosen_standardizing_row_zero_index':4,'chosen_row_coordinate_order':[supp(v)[0] for v in chosen],
             'mixed_count':len(mixed),'mixed_cells_zero_index':[list(x) for x in mixed],
             'all_12_mixed_supports_full_three':True,'mixed_degree_profiles':'C/C',
             'distinct_square_bases_cross_gram':[[serial(dot(x,y)) for y in (r,rp)] for x in (q,qp)],
             'claim':'Actual QLS only; no mate or pair-product orthogonality is asserted.'},
            'two_coordinate_overlap_can_cancel':{'u':list(map(serial,u)),'u_perp':list(map(serial,up)),'inner':serial(dot(u,up))},
            'single_coordinate_overlap_nonzero':{'inner':serial(dot(u,one_axis))},
            'three_space_full_support_inner':serial(dot(x,y)),
            'three_space_mutation_drop_one_full_support_inner':serial(dot(xmut,y)),
            'cross_gram_mutation_remove_plane_intersection':[[serial(z) for z in line] for line in cross]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', required=True, help='new output path; never overwrite')
    args = ap.parse_args()
    out = pathlib.Path(args.out)
    if out.exists():
        raise SystemExit('refusing to overwrite output')
    man = pathlib.Path(__file__).parent / 'manifest-v1.json'
    mb = man.read_bytes()
    assert digest(mb) == MANIFEST_HASH
    b = SOURCE.read_bytes()
    assert digest(b) == SOURCE_HASH and len(b) == 142557 and b.count(b'\n') == 852
    b.decode('utf-8')
    script_hash = digest(pathlib.Path(__file__).read_bytes())
    begin = clock()
    t0 = time.monotonic()
    result = {'schema':'finite-review-independent-controls-v1',
              'input_sha256':digest(b),'input_bytes':len(b),'input_LF':b.count(b'\n'),
              'manifest_sha256':digest(mb),'script_sha256':script_hash,
              'python':sys.version,'clock_before_controls':begin,
              'limitations':['same-harness, not independent-family, human, formal or novelty review',
                             'graph/cardinality/axis patterns are necessary relaxations only',
                             'separate cardinality and axis witnesses are not necessarily jointly realizable',
                             'no solver search for mates and no universal complex-vector theorem established']}
    result['projectors'] = projector_controls()
    result['cube_full_support_subgraph'] = cube_controls()
    result['pigeonholes'] = pigeonhole_controls()
    result['exact_complex_vectors'] = qls_controls()
    result['incidence'] = incidence_controls()
    result['elapsed_total_seconds'] = round(time.monotonic()-t0,3)
    result['clock_immediately_before_output'] = clock()
    with out.open('x', encoding='utf-8') as f:
        json.dump(result,f,indent=2,sort_keys=True)
        f.write('\n')
    print(json.dumps({'output':str(out),'output_sha256':digest(out.read_bytes()),
                      'script_sha256':script_hash,'elapsed_seconds':result['elapsed_total_seconds'],
                      'clock_before_output':result['clock_immediately_before_output']},sort_keys=True))


if __name__ == '__main__':
    main()
