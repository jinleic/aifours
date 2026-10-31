#!/usr/bin/env python3
"""Finite, reviewer-owned sanity controls; not a proof for arbitrary groups."""
from itertools import combinations, permutations, product
from math import gcd


def comp(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    return tuple(p.index(i) for i in range(len(p)))


def subgroups(elements, multiply, identity):
    result = []
    for mask in range(1 << len(elements)):
        h = frozenset(elements[i] for i in range(len(elements)) if mask & (1 << i))
        if identity in h and all(multiply(x, y) in h for x in h for y in h):
            result.append(h)
    return result


def cosets(elements, multiply, groups):
    result = []
    for h in groups:
        seen = set()
        for x in elements:
            members = frozenset(multiply(x, y) for y in h)
            if members not in seen:
                seen.add(members)
                result.append((h, members, len(elements) // len(h)))
    return result


def bad_packing(coset_list, threshold):
    best = []

    def visit(start, chosen, occupied):
        nonlocal best
        if len(chosen) > len(best):
            best = chosen[:]
        for i in range(start, len(coset_list)):
            c = coset_list[i]
            if not (occupied & c[1]) and all(gcd(c[2], other[2]) <= threshold for other in chosen):
                visit(i + 1, chosen + [c], occupied | c[1])

    visit(0, [], frozenset())
    return best


def triple_gcds(indices):
    return sorted(gcd(x, y) for x, y in combinations(indices, 2))


# S3: exhaustive actual cosets, intersection orientations, index gcds,
# the d=s boundary, the failure when d<s, and pairwise-coprime Helly.
s3 = tuple(permutations(range(3)))
e3 = (0, 1, 2)
s3_groups = subgroups(s3, comp, e3)
s3_cosets = cosets(s3, comp, s3_groups)
packing = {t: len(bad_packing(s3_cosets, t)) for t in (2, 3, 7)}
assert len(s3_groups) == 6 and len(s3_cosets) == 18
assert packing == {2: 2, 3: 3, 7: 6}
slices = helly = nonhelly = 0
boundary = insufficient_d = one_nonunit = None
for a, b, c in product(s3_cosets, repeat=3):
    ah, aset, d = a
    bh, bset, bi = b
    ch, cset, ci = c
    if triple_gcds((d, bi, ci)) == [1, 1, 1]:
        helly += 1
        assert aset & bset & cset
    if aset & bset and aset & cset and bset & cset and not (aset & bset & cset):
        nonhelly += 1
        if triple_gcds((d, bi, ci)) == [1, 1, 3]:
            one_nonunit = (d, bi, ci)
    if not (aset & bset and aset & cset) or aset & bset & cset:
        continue
    slices += 1
    ds = []
    hs = []
    for other_h, other_set in ((bh, bset), (ch, cset)):
        section = aset & other_set
        w = next(x for x in s3 if x in section)
        common_h = ah & other_h
        assert section == frozenset(comp(w, h) for h in common_h)
        h = len(ah) // len(common_h)
        assert len(s3) // len(common_h) == d * h
        ds.append((common_h, section, d * h))
        hs.append(h)
    assert not (ds[0][1] & ds[1][1])
    complement = [item for item in s3_cosets if item[0] == ah and item[1] != aset]
    assert len(complement) == d - 1
    family = complement + ds
    assert len(family) == d + 1
    for i, j in combinations(range(len(family)), 2):
        assert not (family[i][1] & family[j][1])
        expected = d * gcd(*hs) if i >= len(complement) and j >= len(complement) else d
        assert gcd(family[i][2], family[j][2]) == expected
    slice_gcd = d * gcd(*hs)
    for t, s in packing.items():
        if d >= s:
            assert slice_gcd > t
            if t == 2 and d == s:
                boundary = (t, s, d, tuple(hs), slice_gcd)
        elif t == 7 and slice_gcd <= t:
            insufficient_d = (t, s, d, tuple(hs), slice_gcd)
assert slices and helly and nonhelly and boundary and insufficient_d and one_nonunit
normal_pairs = 0
nonnormal_counter = None
for h, k in product(s3_groups, repeat=2):
    normal = all(frozenset(comp(comp(g, x), inverse(g)) for x in h) == h for g in s3)
    hj = len(h) // len(h & k)
    aj = len(s3) // len(k)
    if normal:
        normal_pairs += 1
        assert aj % hj == 0
    elif hj == 2 and aj == 3 and aj % hj:
        nonnormal_counter = (hj, aj)
assert nonnormal_counter
print('S3 cosets=%d slices=%d coprime_helly_triples=%d nonhelly_triangles=%d packing=%s' % (len(s3_cosets), slices, helly, nonhelly, packing))
print('BOUNDARY d=s survives: T,s,d,h2h3,slice_gcd=%s' % (boundary,))
print('NEGATIVE drop d>=s: T,s,d,h2h3,slice_gcd=%s' % (insufficient_d,))
print('NORMALITY pairs=%d; NEGATIVE nonnormal h does not divide a: %s' % (normal_pairs, nonnormal_counter))
print('NEGATIVE non-Helly does not require every pair gcd>1: S3 indices=%s' % (one_nonunit,))

# Enumerate every subgroup/coset of S3 x C2 with normal N=S3 x 0.
# The representative t includes a noncentral kernel component, so the
# right-translation test genuinely exercises conjugation inside N.
def product_mul(x, y):
    return (comp(x[0], y[0]), x[1] ^ y[1])


def product_inv(x):
    return (inverse(x[0]), x[1])


g = tuple((p, bit) for p in s3 for bit in (0, 1))
ge = (e3, 0)
n = frozenset((p, 0) for p in s3)
g_groups = subgroups(g, product_mul, ge)
g_cosets = cosets(g, product_mul, g_groups)
tperm = (0, 2, 1)
translated_fibers = {}
fiber_count = 0
for i, (h, members, index) in enumerate(g_cosets):
    h_n = h & n
    b_index = len(n) // len(h_n)
    image = frozenset(x[1] for x in h)
    a_index = 2 // len(image)
    assert index == a_index * b_index
    for bit in (0, 1):
        t = (tperm, bit)
        t_inv = product_inv(t)
        fiber = frozenset(x for x in members if x[1] == bit)
        if not fiber:
            continue
        x = next(y for y in g if y in fiber)
        conjugate_h = frozenset(product_mul(product_mul(t, y), t_inv) for y in h_n)
        actual = frozenset(product_mul(y, t_inv) for y in fiber)
        base = product_mul(x, t_inv)
        expected = frozenset(product_mul(base, y) for y in conjugate_h)
        assert actual == expected and actual <= n and conjugate_h <= n
        assert len(n) // len(conjugate_h) == b_index
        translated_fibers[i, bit] = actual
        fiber_count += 1
fiber_pairs = low_gcd_pairs = 0
for i, j in combinations(range(len(g_cosets)), 2):
    hi, si, ni = g_cosets[i]
    hj, sj, nj = g_cosets[j]
    if si & sj:
        continue
    ai = 2 // len(frozenset(x[1] for x in hi))
    aj = 2 // len(frozenset(x[1] for x in hj))
    bi = len(n) // len(hi & n)
    bj = len(n) // len(hj & n)
    p = gcd(ai, aj) * gcd(bi, bj)
    assert ni % p == 0 and nj % p == 0
    for bit in (0, 1):
        if (i, bit) in translated_fibers and (j, bit) in translated_fibers:
            fiber_pairs += 1
            assert not (translated_fibers[i, bit] & translated_fibers[j, bit])
            assert gcd(bi, bj) >= 2
            if gcd(ni, nj) <= 7:
                low_gcd_pairs += 1
                assert gcd(ai, aj) <= 3
transposition = (1, 0, 2)
u = frozenset((p, 0) for p in (e3, transposition))
t = (tperm, 1)
t_inv = product_inv(t)
conj_u = frozenset(product_mul(product_mul(t, x), t_inv) for x in u)
assert conj_u != u
original = frozenset(product_mul(t, x) for x in u)
translated = frozenset(product_mul(x, t_inv) for x in original)
assert translated == conj_u and translated != u
assert fiber_count and fiber_pairs and low_gcd_pairs
print('FIBERS S3xC2 subgroups=%d cosets=%d fibers=%d disjoint_common_fiber_pairs=%d low_gcd_pairs=%d' % (len(g_groups), len(g_cosets), fiber_count, fiber_pairs, low_gcd_pairs))
print('NEGATIVE omitting conjugation changes actual translated fiber: |U|=%d index_original=6 index_fiber=3' % len(u))

# Elementary finite arithmetic, deliberately including shared primes in the
# quotient and kernel gcd factors. This is not a group-existence search.
arithmetic = 0
for a, aa, b, bb in product(range(1, 13), repeat=4):
    p = gcd(a, aa) * gcd(b, bb)
    assert (a * b) % p == 0 and (aa * bb) % p == 0
    if gcd(a * b, aa * bb) <= 7 and gcd(b, bb) >= 2:
        arithmetic += 1
        assert gcd(a, aa) <= 3
assert gcd(2, 2) * gcd(2, 2) == 4 and arithmetic
indices = (8, 10, 21)
assert min(indices) >= 8 and triple_gcds(indices) == [1, 1, 2]
print('ARITHMETIC product-divisibility and T=7 bound: %d qualifying quadruples' % arithmetic)
print('NUMERICAL ONLY no group witness: indices=%s gcds=%s' % (indices, triple_gcds(indices)))

# Independent V4 control: the Sun8 predicate does not imply B7<=2, and
# pairwise intersection alone does not force a common point.
v4 = (0, 1, 2, 3)
v4_groups = subgroups(v4, lambda x, y: x ^ y, 0)
v4_cosets = cosets(v4, lambda x, y: x ^ y, v4_groups)
v4_b7 = len(bad_packing(v4_cosets, 7))
v4_triangle = None
for a, b, c in combinations(v4_cosets, 3):
    if a[1] & b[1] and a[1] & c[1] and b[1] & c[1] and not (a[1] & b[1] & c[1]):
        v4_triangle = (a[2], b[2], c[2])
        break
assert v4_b7 == 4 and v4_triangle == (2, 2, 2)
print('NEGATIVE B7<=7 does not imply B7<=2: V4 exact B7=%d' % v4_b7)
print('NEGATIVE pairwise overlap does not imply common point: V4 indices=%s' % (v4_triangle,))

# Exhaust all labeled graphs; edge=overlap. Five vertices demonstrate that
# the Ramsey threshold cannot be lowered in the purely graph-theoretic step.
def graph_counts(n_vertices):
    edges = list(combinations(range(n_vertices), 2))
    triangles = [sum(1 << edges.index(e) for e in combinations(v, 2)) for v in combinations(range(n_vertices), 3)]
    neither = no_independent = 0
    for mask in range(1 << len(edges)):
        has_triangle = any(mask & t == t for t in triangles)
        has_independent = any(mask & t == 0 for t in triangles)
        no_independent += not has_independent
        neither += not has_triangle and not has_independent
    return (1 << len(edges), no_independent, neither)

five = graph_counts(5)
six = graph_counts(6)
assert five[2] == 12 and six[2] == 0
print('RAMSEY exact graph controls: n=5 %s; n=6 %s (total,no_independent,neither)' % (five, six))
print('CONTROLS_OK')
