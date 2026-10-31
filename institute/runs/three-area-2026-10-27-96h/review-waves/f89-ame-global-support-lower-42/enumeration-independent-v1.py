#!/usr/bin/env python3
# Independent finite controls; no author checker is imported.
import cmath
import hashlib
import itertools
import json
import math
import random
from collections import Counter, deque
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

OUT = Path(__file__).with_name('enumeration-independent-v1.json')


def projected(points, a, b):
    return {(x[a], x[b]) for x in points}


def five_fibers():
    # Anchor, by local value permutations, two varying alphabets in fiber 0
    # and the remaining varying alphabet in fiber 1. Enumerate whole rectangles.
    alphabet = range(3)
    pairs = list(itertools.combinations(alphabet, 2))
    f0 = [{(a, b, c) for b in (0, 1) for c in (0, 1)} for a in alphabet]
    f1 = [{(a, b, c) for a in (0, 1) for c in C} for b in alphabet for C in pairs]
    f2 = [{(a, b, c) for a in A for b in B} for c in alphabet for A in pairs for B in pairs]
    hist = Counter()
    witness = None
    for x, y, z in itertools.product(f0, f1, f2):
        E = {(i,) + p for i, F in enumerate((x, y, z)) for p in F}
        if len(E) != 12:
            raise RuntimeError('incorrect rectangle size')
        if any(len(projected(E, 0, j)) != 5 for j in (1, 2, 3)):
            raise RuntimeError('incorrect fiber-pair projection')
        # Verify every pair with the fiber coordinate has two extensions.
        if any(min(Counter((p[0], p[j]) for p in E).values()) < 2 for j in (1, 2, 3)):
            raise RuntimeError('incorrect extension multiplicity')
        sz = tuple(len(projected(E, i, j)) for i, j in ((1, 2), (1, 3), (2, 3)))
        hist[sz] += 1
        if sz == (5, 5, 6) and witness is None:
            witness = sorted(E)
    return {'rectangle_choice_counts': [len(f0), len(f1), len(f2)],
            'gauged_fiber_supports': sum(hist.values()),
            'labelled_multiplier': 27,
            'labelled_total': 27 * sum(hist.values()),
            'gauged_5_5_5': hist[(5, 5, 5)],
            'gauged_5_5_6': hist[(5, 5, 6)],
            'labelled_5_5_6': 27 * hist[(5, 5, 6)],
            'labelled_projection_histogram': {','.join(map(str, k)): 27 * v for k, v in sorted(hist.items())},
            'gauged_5_5_6_witness': witness}


def vertex_class(fixed):
    # No direct coordinate-option parametrization: enumerate all 512 binary
    # incidence matrices of (fiber, value), retain row degrees 1/2/2.
    V = []
    for mask in range(1 << 9):
        rows = tuple((mask >> (3*f)) & 7 for f in range(3))
        if all(rows[f].bit_count() == (1 if f == fixed else 2) for f in range(3)):
            V.append(rows)
    others = [f for f in range(3) if f != fixed]
    return sorted(V, key=lambda r: (r[fixed], r[others[0]], r[others[1]]))


def pair_projection(A, B):
    return {(a, b) for f in range(3) for a in range(3) for b in range(3)
            if (A[f] >> a) & 1 and (B[f] >> b) & 1}


def five_graph():
    V = [vertex_class(j) for j in range(3)]
    matrices = {}
    n5 = failures = bad_or = 0
    for j, k, name in ((0, 1, 'AB'), (0, 2, 'AC'), (1, 2, 'BC')):
        l = 3 - j - k
        matrix = []
        for A in V[j]:
            mask = 0
            for t, B in enumerate(V[k]):
                size = len(pair_projection(A, B))
                in_base = (A[j] & A[l] == A[j]) and (B[k] & B[l] == B[k])
                eq_a, eq_b = A[k] == A[l], B[j] == B[l]
                pred = in_base and (eq_a != eq_b)
                n5 += size == 5
                failures += (size == 5) != pred
                bad_or += (size == 5) != (in_base and (not eq_a or not eq_b))
                if size == 5:
                    mask |= 1 << t
            matrix.append(mask)
        matrices[name] = matrix
    AB, AC, BC = (matrices[k] for k in ('AB', 'AC', 'BC'))
    wedges = triangles = 0
    for i, j in itertools.product(range(len(V[0])), range(len(V[1]))):
        if AB[i] >> j & 1:
            wedges += AC[i].bit_count()
            triangles += (AC[i] & BC[j]).bit_count()
    data = json.dumps(matrices, sort_keys=True, separators=(',', ':')).encode()
    return {'vertices_per_class': list(map(len, V)),
            'five_projection_pairs': n5, 'pair_cases': sum(len(V[j])*len(V[k]) for j,k in ((0,1),(0,2),(1,2))),
            'xor_disagreements': failures, 'weakened_or_disagreements': bad_or,
            'edge_counts': [sum(v.bit_count() for v in matrices[k]) for k in ('AB','AC','BC')],
            'wedges_at_class_A': wedges, 'triangles': triangles,
            'canonical_edge_masks_sha256': hashlib.sha256(data).hexdigest()}


def balanced_fibers(g, binary):
    two = tuple(v for v in range(3) if v != g)
    cube = list(itertools.product((0, 1) if binary else two, two, two))
    good = []
    for mask in range(1 << 8):
        if mask.bit_count() != 4:
            continue
        F = [cube[q] for q in range(8) if (mask >> q) & 1]
        if all(len({x[j] for x in F}) == 2 and all(sum(x[j] == value for x in F) == 2
               for value in {x[j] for x in F}) for j in range(3)):
            good.append(F)
    return good


def bipartite(vertices):
    graph = {v: set() for v in vertices}
    for a, b in itertools.combinations(vertices, 2):
        if any(a[j] == b[j] for j in range(3)):
            graph[a].add(b)
            graph[b].add(a)
    colors = {}
    for root in vertices:
        if root in colors:
            continue
        colors[root] = 0
        q = deque([root])
        while q:
            a = q.popleft()
            for b in graph[a]:
                if b in colors and colors[b] == colors[a]:
                    return False
                if b not in colors:
                    colors[b] = 1 - colors[a]
                    q.append(b)
    return True


def six_fibers(binary):
    options = [balanced_fibers(g, binary) for g in range(3)]
    count = Counter()
    examples = []
    for choice in itertools.product(*options):
        E = {(g,) + point for g, F in enumerate(choice) for point in F}
        count['forms'] += 1
        ps = [Counter((p[i], p[j]) for p in E) for i, j in itertools.combinations(range(4), 2)]
        if not all(len(x) == 6 for x in ps):
            continue
        count['all_six'] += 1
        if not all(set(x.values()) == {2} for x in ps):
            continue
        count['all_degrees_two'] += 1
        if binary:
            S = {(p[0], p[2], p[3]) for p in E}
            product_form = len(S) == 6 and all((a,b,c,d) in E for a,c,d in S for b in (0,1))
            count['binary_product'] += product_form
            is_bipartite = bipartite(S)
            count['bipartite' if is_bipartite else 'nonbipartite'] += 1
            examples.append({'S': sorted(S), 'bipartite': is_bipartite})
    return {'options_per_fiber': list(map(len, options)), 'counts': dict(count), 'examples': examples}


def row_weight(rows):
    q = math.factorial(len(rows))
    for c in Counter(rows).values():
        q //= math.factorial(c)
    return q


@lru_cache(None)
def degree_count(n, i, left, cols):
    # Column degrees clipped at two and sorted; row/column labels still count.
    if i == n:
        return int(left == 0 and min(cols) == 2)
    remain = n - i
    if left < 2 * remain or left > n * remain:
        return 0
    total = 0
    for mask in range(1 << n):
        degree = mask.bit_count()
        if 2 <= degree <= min(n, left):
            new = tuple(sorted(min(2, cols[j] + ((mask >> j) & 1)) for j in range(n)))
            total += degree_count(n, i + 1, left - degree, new)
    return total


def components(rows, n):
    # Bipartite support components, counted as (row vertices, column vertices, edges).
    unseen = set(range(2*n))
    result = []
    while unseen:
        todo = [min(unseen)]
        seen = set(todo)
        while todo:
            x = todo.pop()
            if x < n:
                adjacent = [n+j for j in range(n) if rows[x] >> j & 1]
            else:
                adjacent = [i for i in range(n) if rows[i] >> (x-n) & 1]
            for y in adjacent:
                if y not in seen:
                    seen.add(y)
                    todo.append(y)
        unseen -= seen
        rs = [i for i in seen if i < n]
        cs = [j-n for j in seen if j >= n]
        result.append((len(rs), len(cs), sum((rows[i] >> j) & 1 for i in rs for j in cs)))
    return tuple(sorted(result))


def support_patterns(n, k):
    # All multisets of rows of degree >=2 and <=4, with no unique row
    # intersection; k <= 2n+2 proves the degree cap. Restore labelled rows.
    masks = [x for x in range(1 << n) if 2 <= x.bit_count() <= min(4,n)]
    row_only = both = 0
    classes = Counter()
    representatives = {}
    multisets = 0
    def visit(rows, start, rem, cols):
        nonlocal row_only, both, multisets
        d = n-len(rows)
        if d == 0:
            if rem or min(cols) < 2:
                return
            w = row_weight(rows)
            row_only += w
            multisets += 1
            C = [sum(((r >> j) & 1) << i for i, r in enumerate(rows)) for j in range(n)]
            if any((a & b).bit_count() == 1 for a,b in itertools.combinations(C,2)):
                return
            both += w
            signature = components(rows, n)
            classes[signature] += w
            representatives.setdefault(signature, list(rows))
            return
        if rem < 2*d or rem > min(4,n)*d or any(c+d < 2 for c in cols):
            return
        for ix in range(start, len(masks)):
            x = masks[ix]
            size = x.bit_count()
            if not 2*(d-1) <= rem-size <= min(4,n)*(d-1):
                continue
            if any((x&r).bit_count() == 1 for r in rows):
                continue
            visit(rows+[x], ix, rem-size, [cols[j] + ((x>>j)&1) for j in range(n)])
    visit([], 0, k, [0]*n)
    return {'n': n, 'nonzeros': k, 'all_min_degree_labelled': degree_count(n, 0, k, (0,)*n),
            'no_unique_row_overlap_labelled': row_only, 'row_multisets_after_row_test': multisets,
            'no_unique_row_or_column_overlap_labelled': both,
            'component_classes': [{'components': [list(x) for x in key], 'labelled': value,
                                   'row_mask_representative': representatives[key]}
                                  for key, value in sorted(classes.items())]}


def author_small_histogram(n):
    hist = Counter()
    for rows in itertools.product(range(1 << n), repeat=n):
        if any(r.bit_count() < 2 for r in rows):
            continue
        if any(sum((r>>j)&1 for r in rows) < 2 for j in range(n)):
            continue
        if any((a&b).bit_count() == 1 for a,b in itertools.combinations(rows,2)):
            continue
        hist[sum(r.bit_count() for r in rows)] += 1
    return {'n': n, 'checked': 1 << (n*n), 'row_test_histogram': dict(sorted(hist.items()))}


def exact_gram(F):
    # Entries are (a,b), representing (a+b*sqrt(2))/2.
    out = []
    for x in F:
        line = []
        for y in F:
            a = b = 0
            for (u,v),(w,z) in zip(x,y):
                a += u*w + 2*v*z
                b += u*z + v*w
            line.append([a,b])
        out.append(line)
    return out


def exact_unitaries():
    s=(0,1); ns=(0,-1); one=(1,0); neg=(-1,0); zero=(0,0)
    H=[[s,s],[s,ns]]
    T=[[s,one,one],[ns,one,one],[zero,ns,s]]
    GH, GT = exact_gram(H), exact_gram(T)
    target_h = [[[4 if i == j else 0,0] for j in range(2)] for i in range(2)]
    target_t = [[[4 if i == j else 0,0] for j in range(3)] for i in range(3)]
    if GH != target_h or GT != target_t:
        raise RuntimeError('exact unitary construction failed')
    mutation = [list(row) for row in T]
    mutation[0][0] = zero
    return {'H_numerator': H, 'T_numerator': T, 'H_gram_times_four': GH,
            'T_gram_times_four': GT, 'deleted_entry_mutation_rejected': exact_gram(mutation) != target_t,
            'T_nonzeros': sum(v != zero for row in T for v in row)}


def pauli_tables():
    tables=[]
    for ops in itertools.product(range(4), repeat=4):
        weight=sum(p != 0 for p in ops)
        act=[]
        for x in range(16):
            y=x
            phase=1+0j
            for j,p in enumerate(ops):
                bit=(x>>j)&1
                if p == 1:
                    y ^= 1<<j
                elif p == 2:
                    y ^= 1<<j
                    phase *= 1j * (-1 if bit else 1)
                elif p == 3:
                    phase *= -1 if bit else 1
            act.append((y,phase))
        tables.append((ops,weight,act))
    return tables


def spin_stats(state, tables):
    sums=[0.0]*5
    values={}
    for ops,w,act in tables:
        r=sum(state[y].conjugate()*phase*state[x] for x,(y,phase) in enumerate(act))
        if abs(r.imag)>1e-11:
            raise RuntimeError('Pauli expectation must be real')
        sq=r.real*r.real
        sums[w]+=sq
        values[ops]=sq
    flip=abs(sum(((-1)**(x.bit_count()))*state[15-x]*state[x] for x in range(16)))**2
    parity=sum((-1)**w*sums[w] for w in range(5))/16
    purities=[]
    for a,b in itertools.combinations(range(4),2):
        purity=sum(v for ops,v in values.items() if all(ops[j]==0 for j in range(4) if j not in (a,b)))/4
        purities.append(purity)
    return {'weight_sums': sums, 'spin_flip': flip, 'parity': parity,
            'two_party_purities': purities,
            'weight3_identity_error': sums[3]-(12+sums[1]-2*sums[2]),
            'weight4_identity_error': sums[4]-(3-2*sums[1]+sums[2]),
            'inequality_margin': sums[2]-sums[1]-2}


def random_spin_controls():
    tables=pauli_tables()
    rng=random.Random(60281028)
    omega=cmath.exp(2j*math.pi/3)
    phases={3:1,12:1,5:omega,10:omega,6:omega**2,9:omega**2}
    HS=[phases.get(x,0)/math.sqrt(6) for x in range(16)]
    hs=spin_stats(HS,tables)
    groups={'near_HS_balanced_single_qubit': [], 'Haar_complex': []}
    for _ in range(256):
        v=[phases[x]*cmath.exp(1j*rng.uniform(-0.15,0.15))/math.sqrt(6) if x in phases else 0j for x in range(16)]
        groups['near_HS_balanced_single_qubit'].append(spin_stats(v,tables))
    for _ in range(128):
        v=[complex(rng.gauss(0,1),rng.gauss(0,1)) for _ in range(16)]
        norm=math.sqrt(sum(abs(x)**2 for x in v))
        groups['Haar_complex'].append(spin_stats([x/norm for x in v],tables))
    summary={}
    for name,stats in groups.items():
        summary[name]={'samples':len(stats),
          'min_spin_flip':min(s['spin_flip'] for s in stats),
          'max_spin_flip':max(s['spin_flip'] for s in stats),
          'max_abs_parity_identity_error':max(abs(s['spin_flip']-s['parity']) for s in stats),
          'max_abs_weight3_identity_error':max(abs(s['weight3_identity_error']) for s in stats),
          'max_abs_weight4_identity_error':max(abs(s['weight4_identity_error']) for s in stats),
          'min_inequality_margin':min(s['inequality_margin'] for s in stats),
          'min_pair_purity':min(min(s['two_party_purities']) for s in stats),
          'max_pair_purity':max(max(s['two_party_purities']) for s in stats),
          'min_mean_pair_purity':min(sum(s['two_party_purities'])/6 for s in stats),
          'max_single_weight_sum':max(s['weight_sums'][1] for s in stats)}
    weights=[Fraction(1),Fraction(0),Fraction(0),Fraction(12),Fraction(3)]
    impossible=sum((-1)**w*weights[w] for w in range(5))/16
    return {'seed':60281028,'hypothetical_weights':list(map(str,weights)),
            'hypothetical_spin_overlap_exact':str(impossible),
            'HS':hs, 'sample_summaries':summary}


def main():
    result={'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'five_fibers':five_fibers(), 'five_graph':five_graph(),
            'six_fibers_ternary':six_fibers(False), 'six_fibers_binary':six_fibers(True),
            'support_patterns':[support_patterns(n,2*n+delta) for n in (2,3,4,5,6) for delta in (0,1,2)],
            'small_full_row_histograms':[author_small_histogram(n) for n in (2,3,4)],
            'exact_unitaries':exact_unitaries(), 'spin_flip':random_spin_controls()}
    with OUT.open('x',encoding='utf-8') as f:
        json.dump(result,f,indent=2,sort_keys=True)
        f.write('\n')
    print(json.dumps({'receipt':str(OUT),'code_sha256':result['code_sha256'],
                      'five_normal_forms':result['five_fibers']['gauged_fiber_supports'],
                      'graph':result['five_graph'],
                      'six_ternary':result['six_fibers_ternary']['counts'],
                      'six_binary':result['six_fibers_binary']['counts'],
                      'support_patterns':result['support_patterns'],
                      'spin_flip':result['spin_flip']},indent=2))

if __name__ == '__main__':
    main()
