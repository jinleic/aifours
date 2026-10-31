#!/usr/bin/env python3
"""Reviewer-authored exact bounded control for review wave
f182-ame46-t26-remaining-profiles-bridge (reviewer ReviewF182AME46T26, same harness).

Written from the candidate's written normal form (sections 2-7) only.  No author
program is imported, executed or copied; the two author receipts are parsed as
data, in full, and compared leaf by leaf.  Bounded exact control only: not a
proof certificate, not formal verification, not novelty clearance.

Usage:
  python3 -B reviewer-f182-independent-control-v1.py --out OUT.json [--mutation NAME]
  python3 -B reviewer-f182-independent-control-v1.py --no-write [--mutation NAME]
Exit: 0 all checks passed; 3 some check failed; 4 internal 120 s cap hit (UNKNOWN).
"""
import argparse
import hashlib
import itertools
import json
import platform
import random
import signal
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

CAP_SECONDS = 120
NF = 5            # a size-5 party A has five fibres, all of degree d = 2
RES = 10          # |pi_ij(E)| = 36 - 26 residual cells per pair of parties
MUTATIONS = ('none', 'rule-le2', 'drop-pair-23', 'wrong-expected-family', 'cylinder-fibre')

RUN = Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h')
WAVE = RUN / 'review-waves' / 'f182-ame46-t26-remaining-profiles-bridge'
EVD = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support')
PINS = [
    (WAVE / 'manifest-v1.json', 'c7168cafea342576daf582d48d907cdf127591e8f6ae24f4aef55758259bb0aa', 4817, None),
    (RUN / 'dispositions' / 'physics-6-n46-no-hamming-one-parent-v1.md',
     '262a5a09276a2d7ef3ce350425236b29af327c99f8ea3ba03cf50878978baac0', 5552, 25),
    (EVD / 'frontier-20261029-n46-t26-remaining-profiles-bridge-v1.md',
     'b5b592d17c21bd50801d23c0801a663194ac007584fae37cb1446bceb28913bb', 14477, 180),
    (EVD / 'frontier-20261029-n46-t26-remaining-profiles-check-v2.py',
     '83afb6b2f37e16e651d0999a7e7bd23904e8c1dc033d57a252001756e6a83911', 6755, 184),
    (EVD / 'frontier-20261029-n46-t26-remaining-profiles-check-v2.json',
     '856b1a876e04505575a8c87dffc799c8055655fa0258c9431c99a6fc2f093a23', 3207, 197),
    (EVD / 'frontier-20261029-n46-t26-remaining-profiles-check-v1.py',
     '69838b8d736b3e3739e3982e8ea9e586a328c52b2371741d53afd76bed736440', 11937, 284),
    (EVD / 'frontier-20261029-n46-t26-remaining-profiles-check-v1.json',
     '03604b9fe459ad717202b6d48725e0cdb6d90c72cf46ebe25cdce919922275db', 9559, 688),
]
AUTHOR_V1_JSON = PINS[6][0]
AUTHOR_V2_JSON = PINS[4][0]

EXPECTED_PROFILES = [(2, 5, 5, 5), (3, 4, 4, 4), (3, 4, 4, 5), (3, 4, 5, 5), (3, 5, 5, 5),
                     (4, 4, 4, 4), (4, 4, 4, 5), (4, 4, 5, 5), (4, 5, 5, 5), (5, 5, 5, 5)]
PROFILES5 = [p for p in EXPECTED_PROFILES if 5 in p]
FAMILY_PAIRS = [(2, 5), (3, 4), (3, 5), (4, 4), (4, 5), (5, 5)]
ALL_ONES = (1 << NF) - 1


class CapHit(Exception):
    pass


def on_alarm(signum, frame):
    raise CapHit('internal %d s cap reached' % CAP_SECONDS)


class Ledger:
    def __init__(self):
        self.items = []

    def check(self, cid, group, ok, detail=None):
        self.items.append({'id': cid, 'group': group, 'ok': bool(ok), 'detail': detail})
        return bool(ok)

    def failed(self):
        return [c['id'] for c in self.items if not c['ok']]


def pkey(p):
    return ','.join(str(x) for x in p)


def partners(p):
    q = list(p)
    q.remove(5)
    return tuple(sorted(q))


def hamming(x, y):
    return sum(1 for a, b in zip(x, y) if a != b)


# ---------------------------------------------------------------- pins
def sec_pins(L):
    out = []
    for path, sha, nbytes, lf in PINS:
        data = path.read_bytes()
        got = {'path': str(path), 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data),
               'LF': data.count(b'\n'), 'ends_with_LF': data.endswith(b'\n')}
        ok = got['sha256'] == sha and got['bytes'] == nbytes and (lf is None or got['LF'] == lf)
        L.check('pins.' + path.name, 'pins', ok, got)
        out.append(got)
    return out


# ---------------------------------------------------------------- profiles (D1-D4)
def degree_multisets(size, cap):
    """Nondecreasing tuples of `size` integers in [2, cap] with sum RES (D1, D2, D3)."""
    out = []

    def rec(prefix, lo, slots, remaining):
        if slots == 0:
            if remaining == 0:
                out.append(tuple(prefix))
            return
        for d in range(lo, cap + 1):
            if d * slots > remaining:
                break
            rec(prefix + [d], d, slots - 1, remaining - d)

    rec([], 2, size, RES)
    return out


def sec_profiles(L):
    pairs4 = list(itertools.combinations(range(4), 2))
    pp = [p for p in itertools.combinations_with_replacement(range(2, 6), 4)
          if all(p[a] * p[b] >= RES for a, b in pairs4)]
    full, allowed = [], {}
    for p in itertools.combinations_with_replacement(range(1, 7), 4):
        if any(p[a] * p[b] < RES for a, b in pairs4):
            continue
        per = [degree_multisets(p[i], min(p[j] for j in range(4) if j != i)) for i in range(4)]
        if all(per):
            full.append(p)
            allowed[p] = per
    L.check('profiles.pair_product_list_equals_candidate_ten', 'profiles', pp == EXPECTED_PROFILES,
            [list(p) for p in pp])
    L.check('profiles.alphabets_1_to_6_with_D1_D2_D3_feasibility_same_ten', 'profiles', full == pp,
            [list(p) for p in full])
    # degree multisets by size, without caps (D1, D2 only) and with the global cap r_j <= 5
    nocap = {r: degree_multisets(r, RES) for r in (2, 3, 4, 5)}
    cap5 = {r: degree_multisets(r, 5) for r in (2, 3, 4, 5)}
    L.check('profiles.size3_D1D2_only_includes_2_2_6', 'profiles', (2, 2, 6) in nocap[3],
            [list(d) for d in nocap[3]])
    L.check('profiles.size3_with_cap5_is_235_244_334', 'profiles',
            cap5[3] == [(2, 3, 5), (2, 4, 4), (3, 3, 4)], [list(d) for d in cap5[3]])
    L.check('profiles.size4_is_X_Y', 'profiles', cap5[4] == [(2, 2, 2, 4), (2, 2, 3, 3)], [list(d) for d in cap5[4]])
    L.check('profiles.size5_all_two', 'profiles', cap5[5] == [(2, 2, 2, 2, 2)], [list(d) for d in cap5[5]])
    L.check('profiles.size2_with_cap5_is_5_5', 'profiles', cap5[2] == [(5, 5)], [list(d) for d in cap5[2]])
    return pp, allowed, {'no_cap': {r: [list(d) for d in v] for r, v in nocap.items()},
                         'cap5': {r: [list(d) for d in v] for r, v in cap5.items()}}


# ---------------------------------------------------------------- binary cube (section 5)
def sec_cube(L):
    cube = list(itertools.product((0, 1), repeat=3))
    balanced = [S for S in itertools.combinations(cube, 4) if all(sum(x[c] for x in S) == 2 for c in range(3))]
    free = [S for S in balanced if all(hamming(x, y) != 1 for x, y in itertools.combinations(S, 2))]
    parity = [tuple(x for x in cube if sum(x) % 2 == b) for b in (0, 1)]
    cpairs = list(itertools.combinations(range(3), 2))
    L.check('cube.balanced_four_subsets_8', 'cube', len(balanced) == 8, len(balanced))
    L.check('cube.distance_one_free_2', 'cube', len(free) == 2, len(free))
    L.check('cube.distance_one_free_are_exactly_parity_classes', 'cube',
            sorted(free) == sorted(parity), [list(map(list, S)) for S in free])
    L.check('cube.parity_class_projection_bijective_on_every_pair', 'cube',
            all(len({(x[j], x[k]) for x in S}) == 4 for S in parity for j, k in cpairs))
    cyl = []
    for S in balanced:
        if S in parity:
            continue
        desc = [(j, k, eq) for j, k in cpairs for eq in (True, False) if all((x[j] == x[k]) == eq for x in S)]
        d1 = any(hamming(x, y) == 1 for x, y in itertools.combinations(S, 2))
        nonbij = [(j, k) for j, k in cpairs if len({(x[j], x[k]) for x in S}) != 4]
        cyl.append({'set': [list(x) for x in S], 'cylinder': desc, 'has_distance_one': d1, 'nonbijective_pairs': nonbij})
    ok = (len(cyl) == 6 and all(len(c['cylinder']) == 1 and c['has_distance_one'] for c in cyl)
          and sorted(c['cylinder'][0] for c in cyl) == sorted((j, k, eq) for j, k in cpairs for eq in (True, False))
          and all(c['nonbijective_pairs'] == [tuple(c['cylinder'][0][:2])] for c in cyl))
    L.check('cube.six_cylinders_each_has_distance_one_pair_and_nonbijective_own_pair', 'cube', ok, cyl)
    return {'balanced': len(balanced), 'free': len(free), 'cylinders': cyl}


# ---------------------------------------------------------------- incidence families (section 6)
def build_family(r):
    edges = list(itertools.combinations(range(r), 2))
    fam = []
    for rows in itertools.product(edges, repeat=NF):
        cols = [0] * r
        for g, (a, b) in enumerate(rows):
            cols[a] |= 1 << g
            cols[b] |= 1 << g
        if min(c.bit_count() for c in cols) >= 2:
            fam.append((rows, tuple(cols)))
    return fam


def f2_rank(vectors):
    basis = []  # kept fully reduced; pivot of a basis vector = its lowest set bit
    for v in vectors:
        x = v
        for b in basis:
            if x & (b & -b):
                x ^= b
        if x:
            low = x & -x
            basis = [b ^ x if b & low else b for b in basis]
            basis.append(x)
    return len(basis)


def n_components(r, rows):
    parent = list(range(r))

    def root(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for a, b in rows:
        ra, rb = root(a), root(b)
        if ra != rb:
            parent[ra] = rb
    return len({root(v) for v in range(r)})


def kernel_T(cols):
    """F2 vectors v in F2^5 orthogonal to every column: ker U^T (the cycle space)."""
    return [v for v in range(1 << NF) if all((v & c).bit_count() % 2 == 0 for c in cols)]


def col_span(cols):
    S = {0}
    for c in cols:
        S |= {s ^ c for s in S}
    return S


def deg_type(cols):
    return tuple(sorted(c.bit_count() for c in cols))


def sec_families(L, mutation):
    expected = {2: 1, 3: 210, 4: 2580, 5: 2040}
    if mutation == 'wrong-expected-family':
        expected[4] = 2581  # planted wrong expectation (intended-reason negative)
    F = {r: build_family(r) for r in (2, 3, 4, 5)}
    info = {}
    for r in (2, 3, 4, 5):
        L.check('families.size.r%d' % r, 'families', len(F[r]) == expected[r], {'got': len(F[r]), 'expected': expected[r]})
        rk, dg, bad = Counter(), Counter(), 0
        for rows, cols in F[r]:
            k = f2_rank(cols)
            if k != r - n_components(r, rows) or len(kernel_T(cols)) != 2 ** (NF - k) or f2_rank([
                    (1 << a) | (1 << b) for a, b in rows]) != k:
                bad += 1
            rk[k] += 1
            dg[deg_type(cols)] += 1
        L.check('families.rank_equals_r_minus_components_and_kernel_size.r%d' % r, 'families', bad == 0, bad)
        info[r] = {'size': len(F[r]), 'rank_hist': dict(sorted(rk.items())), 'degree_hist': dict(sorted(dg.items()))}
    return F, info


def two_cycle_triangle_pq(rows):
    cnt = Counter(rows)
    p = sum(1 << g for g, e in enumerate(rows) if cnt[e] == 2)
    return p, ALL_ONES ^ p


def sec_lemma_g(L, F):
    v = Counter()
    for rows, cols in F[5]:
        k, c, ker = f2_rank(cols), n_components(5, rows), sorted(kernel_T(cols))
        if k == 4:
            if not (c == 1 and len(set(rows)) == 5 and ker == [0, ALL_ONES]):
                v['G5_rank4_not_simple_5cycle'] += 1
        elif k == 3:
            p, q = two_cycle_triangle_pq(rows)
            if not (c == 2 and sorted(Counter(rows).values()) == [1, 1, 1, 2] and p.bit_count() == 2
                    and q.bit_count() == 3 and ker == sorted([0, p, q, ALL_ONES])):
                v['G5_rank3_not_2cycle_triangle_with_ker_0pq1'] += 1
        else:
            v['G5_other_rank'] += 1
    for rows, cols in F[4]:
        t, k, c = deg_type(cols), f2_rank(cols), n_components(4, rows)
        if t == (2, 2, 2, 4):
            if not (k == 3 and c == 1):
                v['G4_X_not_connected_rank3'] += 1
        elif t == (2, 2, 3, 3):
            if k == 2:
                w3 = {x for x in cols if x.bit_count() == 3}
                w2 = {x for x in cols if x.bit_count() == 2}
                if not (c == 2 and len(w3) == 1 and len(w2) == 1 and (min(w3) ^ min(w2)) == ALL_ONES
                        and ALL_ONES in col_span(cols)):
                    v['G4_Y_rank2_shape'] += 1
            elif k == 3:
                if c != 1:
                    v['G4_Y_rank3_disconnected'] += 1
            else:
                v['G4_Y_other_rank'] += 1
        else:
            v['G4_other_degrees'] += 1
    for rows, cols in F[3]:
        if f2_rank(cols) != 2 or n_components(3, rows) != 1:
            v['size3_not_connected_rank2'] += 1
    L.check('lemmaG.exhaustive_structure_facts', 'lemmaG', not v, dict(v))
    return dict(v)


# ---------------------------------------------------------------- pair compatibility (M), (O)
def rule_table(allowed):
    return [[(m & n).bit_count() in allowed for n in range(1 << NF)] for m in range(1 << NF)]


def groups_by_colset(fam):
    G = defaultdict(list)
    for idx, (_, cols) in enumerate(fam):
        G[frozenset(cols)].append(idx)
    return list(G.items())


def m1_adjacency(fa, fb, table):
    """Method 1 (pure Python, by distinct column sets): every column pair has allowed overlap."""
    A = np.zeros((len(fa), len(fb)), dtype=bool)
    for Sa, Ia in groups_by_colset(fa):
        for Sb, Ib in groups_by_colset(fb):
            if all(table[x][y] for x in Sa for y in Sb):
                A[np.ix_(Ia, Ib)] = True
    return A


def m2_adjacency(fa, ra, fb, rb, allowed):
    """Method 2 (numpy, labeled): accumulate, fibre by fibre, the four cells {b0,b1}x{c0,c1}
    contributed by a parity fibre (formula (M) applied literally), then test multiplicities."""
    Rb = np.array([rows for rows, _ in fb], dtype=np.int64)  # (nb, 5, 2)
    nb = len(fb)
    ar = np.arange(nb)
    ok_mult = np.zeros(4 * NF + 1, dtype=bool)
    for a in allowed:
        ok_mult[a] = True
    A = np.zeros((len(fa), nb), dtype=bool)
    for i, (rows, _) in enumerate(fa):
        cnt = np.zeros((nb, ra * rb), dtype=np.int64)
        for g, pair in enumerate(rows):
            for b in pair:
                for s in (0, 1):
                    cnt[ar, b * rb + Rb[:, g, s]] += 1
        A[i] = ok_mult[cnt].all(axis=1)
    return A


def m1_triples(F, s, table, drop=None):
    """Pure Python triple count over distinct column sets (group level)."""
    G = [groups_by_colset(F[x]) for x in s]

    def comp(Ga, Gb):
        return [[all(table[x][y] for x in Sa for y in Sb) for Sb, _ in Gb] for Sa, _ in Ga]

    c12, c13, c23 = comp(G[0], G[1]), comp(G[0], G[2]), comp(G[1], G[2])
    total = 0
    for i, (_, I1) in enumerate(G[0]):
        for j, (_, I2) in enumerate(G[1]):
            if drop != '12' and not c12[i][j]:
                continue
            for k, (_, I3) in enumerate(G[2]):
                if drop != '13' and not c13[i][k]:
                    continue
                if drop != '23' and not c23[j][k]:
                    continue
                total += len(I1) * len(I2) * len(I3)
    return total


def m2_triples(A12, A13, A23, drop=None):
    """BLAS count: sum_{b,c} A12[b,c] * #{d : A13[b,d] and A23[c,d]} (exact: integers < 2^53)."""
    B12 = np.ones(A12.shape) if drop == '12' else A12.astype(np.float64)
    B13 = np.ones(A13.shape) if drop == '13' else A13.astype(np.float64)
    B23 = np.ones(A23.shape) if drop == '23' else A23.astype(np.float64)
    return int(round(float((B12 * (B13 @ B23.T)).sum())))


def adjacency_set(F, table, allowed, L, tag):
    adj, sums = {}, {}
    for a, b in FAMILY_PAIRS:
        A1 = m1_adjacency(F[a], F[b], table)
        A2 = m2_adjacency(F[a], a, F[b], b, allowed)
        L.check('pairs.%s.methods_agree_pair_by_pair.%d_%d' % (tag, a, b), 'pairs', np.array_equal(A1, A2),
                {'m1': int(A1.sum()), 'm2': int(A2.sum())})
        adj[(a, b)] = A1
        sums[(a, b)] = int(A1.sum())
    return adj, sums


def sec_main_enumeration(L, F, mutation, adj02):
    allowed = (0, 1, 2) if mutation == 'rule-le2' else (0, 2)
    if allowed == (0, 2):
        adj, sums = adj02
    else:
        adj, sums = adjacency_set(F, rule_table(allowed), allowed, L, 'main_mutated')
    table = rule_table(allowed)
    drop = '23' if mutation == 'drop-pair-23' else None
    hand = {(2, 5): 2040, (3, 5): 600 * 6, (4, 5): 600 * 6, (5, 5): 0}
    for k, v in hand.items():
        L.check('pairs-hand.%d_%d' % k, 'pairs-hand', sums[k] == v, {'got': sums[k], 'hand_derived': v})
    out = {}
    for p in PROFILES5:
        s = partners(p)
        A12, A13, A23 = adj[(s[0], s[1])], adj[(s[0], s[2])], adj[(s[1], s[2])]
        t1 = m1_triples(F, s, table, drop)
        t2 = m2_triples(A12, A13, A23, drop)
        L.check('triples.methods_agree.' + pkey(p), 'triples', t1 == t2, {'m1': t1, 'm2': t2})
        L.check('triples.zero.' + pkey(p), 'triples', t1 == 0 and t2 == 0, {'m1': t1, 'm2': t2})
        out[pkey(p)] = {'partners_sorted': list(s), 'pairs_12': int(A12.sum()), 'pairs_13': int(A13.sum()),
                        'pairs_23': int(A23.sum()), 'triples_m1': t1, 'triples_m2': t2}
    return {'allowed_multiplicities': list(allowed), 'drop': drop, 'pair_counts': {'%d_%d' % k: v for k, v in sums.items()},
            'profiles': out}


# ---------------------------------------------------------------- F2 lemma S, cap, relaxations
def sec_lemma_s_f2(L, F):
    table = rule_table((0, 2, 4))  # even overlap: F2 orthogonality only
    fam_pairs = [(2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5), (5, 5)]
    counts, v, types = {}, Counter(), Counter()
    for a, b in fam_pairs:
        A = m1_adjacency(F[a], F[b], table)
        counts['%d_%d' % (a, b)] = int(A.sum())
        for i, k in zip(*np.nonzero(A)):
            ca, cb = F[a][i][1], F[b][k][1]
            ra, rb = f2_rank(ca), f2_rank(cb)
            if ra + rb > NF:
                v['S1_sylvester'] += 1
            ta = 'X' if (a == 4 and deg_type(ca) == (2, 2, 2, 4)) else ('Y' if a == 4 else str(a))
            tb = 'X' if (b == 4 and deg_type(cb) == (2, 2, 2, 4)) else ('Y' if b == 4 else str(b))
            types['%s%d|%s%d' % (ta, ra, tb, rb)] += 1
            if (a, b) == (4, 4) and ta == tb:
                v['S3_S4_same_type_size4_pair'] += 1
            if (a, b) == (4, 5):
                p, q = two_cycle_triangle_pq(F[b][k][0]) if rb == 3 else (None, None)
                if not (rb == 3 and ta == 'Y' and ra == 2 and sorted(ca) == sorted([q, q, p, p])):
                    v['S5_shape'] += 1
            if (a, b) == (3, 5):
                p, q = two_cycle_triangle_pq(F[b][k][0]) if rb == 3 else (None, None)
                if not (rb == 3 and sorted(ca) == sorted([p, q, ALL_ONES])):
                    v['S5_size3_columns_not_p_q_1'] += 1
    L.check('lemmaS.S2_no_F2_orthogonal_size5_pair', 'lemmaS', counts['5_5'] == 0, counts['5_5'])
    L.check('lemmaS.S1_S3_S4_S5_exhaustive_over_F2_orthogonal_pairs', 'lemmaS', not v, dict(v))
    f2_triples = {pkey(p): m1_triples(F, partners(p), table) for p in PROFILES5}
    L.check('lemmaS.F2_only_relaxation_still_zero_triples_all_eight', 'lemmaS',
            all(t == 0 for t in f2_triples.values()), f2_triples)
    return {'F2_orthogonal_pair_counts': counts, 'type_rank_pairs': dict(sorted(types.items())),
            'F2_only_triples': f2_triples}


def sec_cap_and_relaxations(L, F, adj02):
    adj, sums = adj02
    table02 = rule_table((0, 2))
    # (3,5) integer-compatible pairs: size-3 columns are exactly {p, q, 1}, degree type (2,3,5)
    A35 = adj[(3, 5)]
    bad, types = 0, Counter()
    for i, k in zip(*np.nonzero(A35)):
        c3 = F[3][i][1]
        types[deg_type(c3)] += 1
        rows5, c5 = F[5][k]
        if f2_rank(c5) != 3:
            bad += 1
            continue
        p, q = two_cycle_triangle_pq(rows5)
        if sorted(c3) != sorted([p, q, ALL_ONES]):
            bad += 1
    L.check('cap.all_3_5_pairs_have_size3_columns_p_q_1_type_235', 'cap',
            bad == 0 and dict(types) == {(2, 3, 5): sums[(3, 5)]}, {'bad': bad, 'types': {pkey(t): n for t, n in types.items()}})
    rel = {}
    for p in PROFILES5:
        s = partners(p)
        A12, A13, A23 = adj[(s[0], s[1])], adj[(s[0], s[2])], adj[(s[1], s[2])]
        d23_m1, d23_m2 = m1_triples(F, s, table02, '23'), m2_triples(A12, A13, A23, '23')
        rel[pkey(p)] = {'drop23_m1': d23_m1, 'drop23_m2': d23_m2,
                        'drop13_m1': m1_triples(F, s, table02, '13'), 'drop12_m1': m1_triples(F, s, table02, '12'),
                        'rule_le2_m1': m1_triples(F, s, rule_table((0, 1, 2)))}
        L.check('relax.drop23_methods_agree.' + pkey(p), 'relax', d23_m1 == d23_m2, [d23_m1, d23_m2])
    positive = [k for k in rel if k not in ('3,4,5,5', '5,5,5,5')]
    L.check('relax.positive_control_drop23_finds_triples', 'relax',
            all(rel[k]['drop23_m1'] > 0 for k in positive) and rel['3,4,5,5']['drop23_m1'] == 0
            and rel['5,5,5,5']['drop23_m1'] == 0, {k: rel[k]['drop23_m1'] for k in rel})
    L.check('relax.intended_negative_le2_rule_admits_triples_all_eight', 'relax',
            all(rel[k]['rule_le2_m1'] > 0 for k in rel), {k: rel[k]['rule_le2_m1'] for k in rel})
    return rel


def sec_integer_pair_types(F, adj02):
    """Informational: type/rank breakdown of the {0,2}-compatible labeled pairs."""
    adj, _ = adj02

    def tag(r, cols):
        t = ('X' if deg_type(cols) == (2, 2, 2, 4) else 'Y') if r == 4 else str(r)
        return '%s(rank%d,deg%s)' % (t, f2_rank(cols), pkey(deg_type(cols)))

    out = {}
    for a, b in FAMILY_PAIRS:
        c = Counter()
        for i, k in zip(*np.nonzero(adj[(a, b)])):
            c[tag(a, F[a][i][1]) + '|' + tag(b, F[b][k][1])] += 1
        out['%d_%d' % (a, b)] = dict(sorted(c.items()))
    return out



# ---------------------------------------------------------------- (M) identity on built supports
def fibre_words(g, vB, vC, vD, mode):
    words = []
    for e in itertools.product((0, 1), repeat=3):
        if mode[0] == 'parity':
            keep = sum(e) % 2 == mode[1]
        else:  # ('cyl', j, k, equal)
            keep = (e[mode[1]] == e[mode[2]]) == mode[3]
        if keep:
            words.append((g, vB[e[0]], vC[e[1]], vD[e[2]]))
    return words


def support_problems(words, us):
    probs = set()
    if len(words) != 20 or len(set(words)) != 20:
        probs.add('size')
    for x, y in itertools.combinations(words, 2):
        if x[0] == y[0] and hamming(x, y) == 1:
            probs.add('intra_fibre_hamming1')
    for i, j in itertools.combinations(range(4), 2):
        cnt = Counter((w[i], w[j]) for w in words)
        if i == 0:
            if set(cnt.values()) != {2}:
                probs.add('A_pair_%d' % j)
            continue
        ci, cj = us[i - 1][1], us[j - 1][1]
        if any(cnt.get((b, c), 0) != (ci[b] & cj[c]).bit_count() for b in range(len(ci)) for c in range(len(cj))):
            probs.add('M_%d%d' % (i, j))
    return probs


def sec_m_identity(L, F, mutation):
    rng = random.Random(20261029182)
    pos_fail, pos_ok = Counter(), 0
    for _ in range(3000):
        us = [F[r][rng.randrange(len(F[r]))] for r in (rng.choice((2, 3, 4, 5)) for _ in range(3))]
        if mutation == 'cylinder-fibre':
            j, k = sorted(rng.sample(range(3), 2))
            modes = [('cyl', j, k, rng.random() < 0.5)] + [('parity', rng.randrange(2)) for _ in range(NF - 1)]
        else:
            modes = [('parity', rng.randrange(2)) for _ in range(NF)]
        words = [w for g in range(NF) for w in fibre_words(g, us[0][0][g], us[1][0][g], us[2][0][g], modes[g])]
        pr = support_problems(words, us)
        if pr:
            pos_fail[','.join(sorted(pr))] += 1
        else:
            pos_ok += 1
    L.check('M.global_positive_parity_fibres_satisfy_M_exactly', 'M', pos_ok == 3000,
            {'ok': pos_ok, 'failure_reasons': dict(pos_fail)})
    neg_exact, neg_reasons = 0, Counter()
    for _ in range(1000):
        us = [F[r][rng.randrange(len(F[r]))] for r in (rng.choice((2, 3, 4, 5)) for _ in range(3))]
        j, k = sorted(rng.sample(range(3), 2))
        modes = [('cyl', j, k, rng.random() < 0.5)] + [('parity', rng.randrange(2)) for _ in range(NF - 1)]
        words = [w for g in range(NF) for w in fibre_words(g, us[0][0][g], us[1][0][g], us[2][0][g], modes[g])]
        pr = support_problems(words, us)
        neg_reasons[','.join(sorted(pr))] += 1
        neg_exact += pr == {'intra_fibre_hamming1', 'M_%d%d' % (j + 1, k + 1)}
    L.check('M.intended_negative_cylinder_fibre_breaks_M_on_its_own_pair_only', 'M', neg_exact == 1000,
            {'exact': neg_exact, 'reasons': dict(neg_reasons)})
    return {'positive_ok': pos_ok, 'positive_failures': dict(pos_fail), 'negative_exact': neg_exact,
            'negative_reasons': dict(neg_reasons)}


# ---------------------------------------------------------------- section 4: activity counts
def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


def sec_activity(L, profiles):
    out = {}
    for p in profiles:
        S1 = sum(6 * r - RES for r in p)
        S2 = sum(p[a] * p[b] - RES for a, b in itertools.combinations(range(4), 2))
        sols = [n for n in compositions(26, 5)
                if sum(k * n[k] for k in range(5)) == S1 and sum(k * (k - 1) // 2 * n[k] for k in range(5)) == S2]
        out[pkey(p)] = {'S1': S1, 'S2': S2, 'solutions': [list(n) for n in sols]}
    s3444 = out['3,4,4,4']
    L.check('activity.3444_moments_50_24_unique_solution_0_2_24_0_0', 'activity',
            s3444['S1'] == 50 and s3444['S2'] == 24 and s3444['solutions'] == [[0, 2, 24, 0, 0]], s3444)
    f = [k - k * (k - 1) // 2 for k in range(5)]
    L.check('activity.summand_k_minus_binom_k2_is_0_1_1_0_m2', 'activity', f == [0, 1, 1, 0, -2], f)
    # size-4 party of (3,4,4,4): partners 3,4,4
    active = 6 * 4 - RES
    pair_active = (4 * 3 - RES) + 2 * (4 * 4 - RES)
    per_symbol = {d: (6 - d) - ((3 - d) + (4 - d) + (4 - d)) for d in range(0, 11)}
    L.check('activity.3444_size4_party_active_14_pairactive_14_singletons_0', 'activity',
            active == 14 and pair_active == 14, [active, pair_active, active - pair_active])
    L.check('activity.3444_per_symbol_2d_minus_5_never_zero', 'activity',
            all(v == 2 * d - 5 and v != 0 for d, v in per_symbol.items()), per_symbol)
    L.check('activity.3444_Y_forced_by_cap_degrees_2_3_give_m1_p1', 'activity',
            degree_multisets(4, 3) == [(2, 2, 3, 3)] and [per_symbol[2], per_symbol[3]] == [-1, 1])
    L.check('activity.positive_control_4444_not_excluded_by_counting', 'activity',
            len(out['4,4,4,4']['solutions']) > 0, out['4,4,4,4'])
    return out


# ---------------------------------------------------------------- author receipts (data only)
def flatten(obj, path=()):
    if isinstance(obj, dict):
        for k in obj:
            yield from flatten(obj[k], path + (k,))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from flatten(v, path + (i,))
    else:
        yield path, obj


def compare_tree(author, mine, skip):
    """Leaf-by-leaf comparison; `skip(path)` returns a classification string for non-comparable leaves."""
    fa, fm = dict(flatten(author)), dict(flatten(mine))
    rows = {'match': 0, 'mismatch': [], 'author_only': [], 'reviewer_only': [], 'classified': Counter()}
    for path, val in fa.items():
        cls = skip(path)
        if cls:
            rows['classified'][cls] += 1
            continue
        if path not in fm:
            rows['author_only'].append([list(path), val])
        elif fm[path] != val or type(fm[path]) is not type(val):
            rows['mismatch'].append([list(path), val, fm[path]])
        else:
            rows['match'] += 1
    for path in fm:
        if path not in fa:
            rows['reviewer_only'].append(list(path))
    rows['classified'] = dict(rows['classified'])
    rows['author_leaves'] = len(fa)
    return rows


def hist_str(c):
    return {pkey(k) if isinstance(k, tuple) else str(k): v for k, v in sorted(c.items())}


def achievable_cd_hists(F, s, table):
    """Nonzero-cell multiplicity histograms of U_C^T U_D over (B,C,D) with BC and BD compatible."""
    GB = groups_by_colset(F[s[0]])

    def multisets(fam):
        return sorted({tuple(sorted(cols)) for _, cols in fam})

    MC, MD = multisets(F[s[1]]), multisets(F[s[2]])
    pairs = set()
    for SB, _ in GB:
        okC = [m for m in MC if all(table[x][y] for x in SB for y in set(m))]
        okD = [m for m in MD if all(table[x][y] for x in SB for y in set(m))]
        pairs.update((c, d) for c in okC for d in okD)
    hists = set()
    for c, d in pairs:
        h = Counter((x & y).bit_count() for x in c for y in d)
        h.pop(0, None)
        hists.add(tuple(sorted(h.items())))
    return hists


def sec_author(L, F, finfo, main, rel, cube, profiles, allowed, activity):
    a1 = json.loads(AUTHOR_V1_JSON.read_text(encoding='utf-8'))
    a2 = json.loads(AUTHOR_V2_JSON.read_text(encoding='utf-8'))
    fam_sizes = {str(r): finfo[r]['size'] for r in (2, 3, 4, 5)}
    rank_h = {str(r): {str(k): v for k, v in finfo[r]['rank_hist'].items()} for r in (2, 3, 4, 5)}
    deg_h = {str(r): hist_str(finfo[r]['degree_hist']) for r in (2, 3, 4, 5)}
    mp = main['profiles']
    mine2 = {
        'binary_cube_balanced_four_subsets': cube['balanced'],
        'distance_one_free_balanced_subsets': cube['free'],
        'family_degree_multisets': deg_h, 'family_rank_histograms': rank_h, 'family_sizes': fam_sizes,
        'profiles': [list(p) for p in profiles],
        'size5_profiles': {k: {'compatible_BC_pairs': v['pairs_12'], 'compatible_BD_pairs': v['pairs_13'],
                               'compatible_CD_pairs': v['pairs_23'], 'other_sizes': v['partners_sorted'],
                               'triples_all_three_conditions': v['triples_m1']} for k, v in mp.items()},
    }

    def skip2(path):
        if path[0] in ('methods', 'scope'):
            return 'narrative_string_not_evidence'
        return None

    c2 = compare_tree(a2, mine2, skip2)
    s3444 = activity['3,4,4,4']
    mine1 = {
        'allowed_degree_multisets_by_profile': {pkey(p): {str(i): sorted([list(d) for d in allowed[p][i]])
                                                          for i in range(4)} for p in profiles},
        'binary_cube_balanced_four_subsets': cube['balanced'],
        'distance_one_free_balanced_subsets': cube['free'],
        'incidence_families': {str(r): {'degree_multisets': deg_h[str(r)], 'matrices': fam_sizes[str(r)],
                                        'rank_histogram': rank_h[str(r)]} for r in (2, 3, 4, 5)},
        'profile_3444_active_count': {
            'active_incidences': s3444['S1'], 'activity_vector_solutions': s3444['solutions'],
            'pair_incidences': s3444['S2'],
            'per_symbol_singleton_count_by_degree': {str(d): (6 - d) - ((3 - d) + (4 - d) + (4 - d))
                                                     for d in sorted({x for ds in allowed[(3, 4, 4, 4)][1] for x in ds})},
            'size4_party_active_words': 6 * 4 - RES,
            'size4_party_pair_active_words': (4 * 3 - RES) + 2 * (4 * 4 - RES),
            'size4_singletons': (6 * 4 - RES) - ((4 * 3 - RES) + 2 * (4 * 4 - RES)),
            'slack': 26 - (s3444['S1'] - s3444['S2'])},
        'profiles': [list(p) for p in profiles],
        'residual_size': RES,
        'size5_profile_results': {k: {'A_size': 5, 'all_three_pair_conditions_triples': v['triples_m1'],
                                      'compatible_BC_pairs': v['pairs_12'],
                                      'control_without_CD_condition_triples': rel[k]['drop23_m1'],
                                      'other_sizes': v['partners_sorted']} for k, v in mp.items()},
    }
    # normalise author degree-multiset lists (order is not mathematical content)
    a1n = json.loads(json.dumps(a1))
    for pk, parties in a1n['allowed_degree_multisets_by_profile'].items():
        for i in parties:
            parties[i] = sorted(parties[i])

    def skip1(path):
        if path[0] == 'scope':
            return 'narrative_string_not_evidence'
        if path[0] == 'direct_support_cross_checks':
            return 'author_run_metadata_sample_count'
        if path[0] == 'size5_profile_results' and path[2] == 'control_example_CD_multiplicities':
            return 'order_dependent_example_checked_for_achievability'
        return None

    c1 = compare_tree(a1n, mine1, skip1)
    # achievability of the author's order-dependent example histograms
    table02 = rule_table((0, 2))
    ach = {}
    for k, v in a1['size5_profile_results'].items():
        ex = v.get('control_example_CD_multiplicities')
        if ex is None:
            ach[k] = {'example': None, 'drop23_triples': rel[k]['drop23_m1']}
            continue
        h = tuple(sorted((int(m), n) for m, n in ex.items()))
        hs = achievable_cd_hists(F, tuple(v['other_sizes']), table02)
        ach[k] = {'example': ex, 'total_words': sum(m * n for m, n in h), 'achievable': h in hs,
                  'n_achievable_histograms': len(hs)}
    ach_ok = all((x['example'] is None and x['drop23_triples'] == 0) or (x.get('achievable') and x['total_words'] == 20)
                 for x in ach.values())
    # self-test of the comparator: a single planted change must be reported as exactly one mismatch
    planted = json.loads(json.dumps(a2))
    planted['size5_profiles']['4,4,4,5']['compatible_CD_pairs'] += 1
    ct = compare_tree(planted, a2, skip2)
    selftest = (len(ct['mismatch']) == 1 and ct['mismatch'][0][0] == ['size5_profiles', '4,4,4,5', 'compatible_CD_pairs']
                and not ct['author_only'] and not ct['reviewer_only'])
    L.check('author.v2_all_comparable_leaves_match', 'author',
            not c2['mismatch'] and not c2['author_only'] and not c2['reviewer_only'], c2)
    L.check('author.v1_all_comparable_leaves_match', 'author',
            not c1['mismatch'] and not c1['author_only'] and not c1['reviewer_only'], c1)
    L.check('author.v1_example_histograms_achievable_and_sum_20', 'author-example', ach_ok, ach)
    L.check('author.comparator_selftest_planted_change_detected', 'author-selftest', selftest,
            {'planted_mismatches': ct['mismatch']})
    return {'v2': c2, 'v1': c1, 'v1_examples': ach}


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', type=Path)
    ap.add_argument('--no-write', action='store_true')
    ap.add_argument('--mutation', default='none', choices=MUTATIONS)
    args = ap.parse_args()
    if (args.out is None) == (not args.no_write):
        ap.error('exactly one of --out / --no-write')
    if args.out is not None:
        if args.out.exists():
            raise SystemExit('refusing to overwrite ' + str(args.out))
        if args.out.parent.resolve() != WAVE.resolve() or not args.out.name.startswith('reviewer-'):
            raise SystemExit('output must be a reviewer- file inside the wave directory')
    signal.signal(signal.SIGALRM, on_alarm)
    signal.alarm(CAP_SECONDS)
    t0, clock0 = time.monotonic(), time.strftime('%Y-%m-%dT%H:%M:%S%z')
    me = Path(__file__).resolve()
    L = Ledger()
    timings = {}

    def timed(name, fn, *a):
        s = time.monotonic()
        r = fn(*a)
        timings[name] = round(time.monotonic() - s, 3)
        return r

    try:
        pins = timed('pins', sec_pins, L)
        profiles, allowed, deg_ms = timed('profiles', sec_profiles, L)
        cube = timed('cube', sec_cube, L)
        F, finfo = timed('families', sec_families, L, args.mutation)
        lemma_g = timed('lemmaG', sec_lemma_g, L, F)
        adj02 = timed('pairs02', adjacency_set, F, rule_table((0, 2)), (0, 2), L, 'rule02')
        main_res = timed('main', sec_main_enumeration, L, F, args.mutation, adj02)
        lemma_s = timed('lemmaS', sec_lemma_s_f2, L, F)
        rel = timed('relax', sec_cap_and_relaxations, L, F, adj02)
        ptypes = timed('pair_types', sec_integer_pair_types, F, adj02)
        mres = timed('M', sec_m_identity, L, F, args.mutation)
        act = timed('activity', sec_activity, L, profiles)
        auth = timed('author', sec_author, L, F, finfo, main_res, rel, cube, profiles, allowed, act)
    except CapHit as exc:
        print('UNKNOWN:', exc, file=sys.stderr)
        sys.exit(4)
    signal.alarm(0)
    failed = L.failed()
    result = {
        'kind': 'REVIEWER_INDEPENDENT_EXACT_BOUNDED_CONTROL',
        'wave': 'f182-ame46-t26-remaining-profiles-bridge', 'reviewer': 'ReviewF182AME46T26',
        'mutation': args.mutation,
        'script_sha256': hashlib.sha256(me.read_bytes()).hexdigest(),
        'python': platform.python_version(), 'numpy': np.__version__,
        'clock_start_local': clock0, 'clock_end_local': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
        'elapsed_s': round(time.monotonic() - t0, 3), 'section_timings_s': timings,
        'pins': pins,
        'checks_total': len(L.items), 'checks_failed': failed, 'all_checks_passed': not failed,
        'checks': L.items,
        'results': {
            'degree_multisets_by_size': deg_ms,
            'family_info': {str(r): {'size': v['size'], 'rank_hist': {str(k): n for k, n in v['rank_hist'].items()},
                                     'degree_hist': hist_str(v['degree_hist'])} for r, v in finfo.items()},
            'lemmaG_violations': lemma_g, 'main_enumeration': main_res, 'lemmaS_F2': lemma_s,
            'relaxations': rel, 'integer_pair_types': ptypes, 'M_identity': mres, 'activity': act,
            'author_receipt_comparison': auth,
        },
        'scope': ('Reviewer-authored bounded exact control of the candidate normal form (sections 2-7); '
                  'no AME state, no proof certificate, not formal/kernel verification.'),
    }
    blob = json.dumps(result, indent=1, sort_keys=True, default=lambda o: o.item() if hasattr(o, 'item') else str(o)) + '\n'
    if args.out is not None:
        with args.out.open('x', encoding='utf-8') as fh:
            fh.write(blob)
    print(json.dumps({'mutation': args.mutation, 'checks_total': len(L.items), 'checks_failed': failed,
                      'elapsed_s': result['elapsed_s'],
                      'triples': {k: v['triples_m1'] for k, v in main_res['profiles'].items()},
                      'pair_counts': main_res['pair_counts']}, sort_keys=True))
    print('output_sha256', hashlib.sha256(blob.encode()).hexdigest())
    sys.exit(0 if not failed else 3)


if __name__ == '__main__':
    main()
