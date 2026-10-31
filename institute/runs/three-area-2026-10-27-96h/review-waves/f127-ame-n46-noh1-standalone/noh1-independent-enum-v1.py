#!/usr/bin/env python3
"""noh1-independent-enum-v1.py  (f127 reviewer-written control; no author code imported)

Exact, standard-library-only reconstruction of the finite part of the N=46, t=26,
(4,4,4,4) residual branch of the standalone no-Hamming-1 packet:

  1. P-count normal form (n_0..n_4) from |P|=26, active incidences 56, pair-active 36.
  2. Labelled Y-Y and X-Y incidence graphs, their orbits under the within-class
     relabelling groups, and comparison with the packet's listed representatives.
  3. High-fibre catalogs: Y six-point fibres on {0,1,2}^3 and X eight-point fibres
     on {0,1,2,3}^3 (each symbol twice per coordinate, all pair projections injective).
  4. All-Y branch: packet normalisation (5 reps x C(34+1,2)) AND the fully labelled
     34^3 enumeration; multiplicity-0/2 condition on BC, BD, CD; complete supports;
     unitary-overlap obstruction per cut; cross-fibre Hamming-1 census.
  5. One-X branch: packet normalisation (2 reps x C(15+1,2)) AND fully labelled 15^3;
     required 2-regular high-fibre projections; exact lookup against the X catalog;
     compatible-triple inspection.
  6. Side controls: m=8 complement incidence brute force; spin-flip sign identity
     (numeric, numpy optional); ratio involution fixed-point check; recount and
     mutation controls on every found support.

Usage: python3 -B noh1-independent-enum-v1.py <new-receipt.json>
Refuses to overwrite an existing receipt.
"""
import hashlib
import itertools
import json
import os
import sys
import time
from collections import Counter

T0 = time.time()


def clock():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z', time.localtime())


def sha256_path(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()


R = {'program': os.path.basename(__file__), 'start_clock': clock()}

# ----------------------------------------------------------------------------
# 1. P-count normal form
# ----------------------------------------------------------------------------
pc = []
for n4 in range(27):
    for n3 in range(27 - n4):
        for n2 in range(27 - n4 - n3):
            for n1 in range(27 - n4 - n3 - n2):
                n0 = 26 - n1 - n2 - n3 - n4
                if n1 + 2 * n2 + 3 * n3 + 4 * n4 != 56:
                    continue
                if n2 + 3 * n3 + 6 * n4 != 36:
                    continue
                pc.append((n0, n1, n2, n3, n4))
R['pcount_solutions'] = pc
assert sorted(pc) == sorted([(0, 2, 18, 6, 0), (0, 1, 21, 3, 1), (0, 0, 24, 0, 2)]), pc

# degree-class identity s - q - 2h = 2d - 6 checked symbolically for d in {2,3,4}:
# P words at symbol a: 6-d; other-active incidences: 3(4-d) = p+2q+3h; s+p+q+h = 6-d.
for d in (2, 3, 4):
    assert (6 - d) - 3 * (4 - d) == 2 * d - 6

# ----------------------------------------------------------------------------
# 2. Incidence graphs and orbits
# ----------------------------------------------------------------------------


def bip_graphs(degA, degB):
    choices = [[frozenset(c) for c in itertools.combinations(range(4), d)] for d in degA]
    out = []
    for rows in itertools.product(*choices):
        cols = [0, 0, 0, 0]
        for r in rows:
            for b in r:
                cols[b] += 1
        if tuple(cols) == tuple(degB):
            out.append(tuple(rows))
    return out


def class_perms(classes):
    perms = []
    for parts in itertools.product(*[itertools.permutations(c) for c in classes]):
        p = [None] * 4
        for cls, img in zip(classes, parts):
            for x, y in zip(cls, img):
                p[x] = y
        perms.append(tuple(p))
    return perms


def relabel(G, pa, pb):
    rows = [None] * 4
    for a in range(4):
        rows[pa[a]] = frozenset(pb[b] for b in G[a])
    return tuple(rows)


def gkey(G):
    return tuple(tuple(sorted(r)) for r in G)


def gfmt(k):
    return '(' + ','.join(''.join(str(x) for x in r) for r in k) + ')'


def orbits(graphs, pa_list, pb_list):
    seen = set()
    reps = []
    for G in graphs:
        k = gkey(G)
        if k in seen:
            continue
        orb = {gkey(relabel(G, pa, pb)) for pa in pa_list for pb in pb_list}
        seen |= orb
        reps.append((min(orb), len(orb)))
    assert sum(sz for _, sz in reps) == len(graphs)
    return reps


YY = bip_graphs((2, 2, 3, 3), (2, 2, 3, 3))
XY = bip_graphs((2, 2, 2, 4), (2, 2, 3, 3))
R['labelled_YY_graphs'] = len(YY)
R['labelled_XY_graphs'] = len(XY)

Y_perms = class_perms([[0, 1], [2, 3]])          # Z2 x Z2 (within low / within high)
X_perms = class_perms([[0, 1, 2], [3]])          # S3 on the three low symbols
yy_reps = orbits(YY, Y_perms, Y_perms)
xy_reps = orbits(XY, X_perms, Y_perms)
R['YY_orbits'] = [{'rep_min': gfmt(k), 'size': s} for k, s in yy_reps]
R['XY_orbits'] = [{'rep_min': gfmt(k), 'size': s} for k, s in xy_reps]

PACKET_YY = ['(01,23,023,123)', '(02,03,123,123)', '(02,13,023,123)', '(02,23,013,123)', '(23,23,012,013)']
PACKET_XY = ['(01,23,23,0123)', '(02,13,23,0123)']


def parse_rep(s):
    s = s.strip('()')
    return tuple(frozenset(int(ch) for ch in part) for part in s.split(','))


def orbit_of(G, pa_list, pb_list):
    return {gkey(relabel(G, pa, pb)) for pa in pa_list for pb in pb_list}


# Do the packet's listed representatives hit every orbit exactly once?
def check_reps(packet_list, graphs, pa_list, pb_list):
    orbs = [orbit_of(G, pa_list, pb_list) for G in graphs]
    distinct = []
    for o in orbs:
        if o not in distinct:
            distinct.append(o)
    hit = [0] * len(distinct)
    bad = []
    for s in packet_list:
        G = parse_rep(s)
        if gkey(G) not in {gkey(H) for H in graphs}:
            bad.append(s)
            continue
        for i, o in enumerate(distinct):
            if gkey(G) in o:
                hit[i] += 1
    return {'orbit_count': len(distinct), 'hits_per_orbit': hit, 'not_a_valid_graph': bad,
            'complete_and_irredundant': (len(bad) == 0 and all(h == 1 for h in hit))}


R['packet_YY_reps_check'] = check_reps(PACKET_YY, YY, Y_perms, Y_perms)
R['packet_XY_reps_check'] = check_reps(PACKET_XY, XY, X_perms, Y_perms)
assert R['packet_YY_reps_check']['complete_and_irredundant']
assert R['packet_XY_reps_check']['complete_and_irredundant']

# ----------------------------------------------------------------------------
# 3. High-fibre catalogs
# ----------------------------------------------------------------------------


def pair_injective(words):
    for i, j in ((0, 1), (0, 2), (1, 2)):
        if len({(w[i], w[j]) for w in words}) != len(words):
            return False
    return True


def balanced(words, k, mult):
    for i in range(3):
        c = Counter(w[i] for w in words)
        if any(c[s] != mult for s in range(k)):
            return False
    return True


Y6 = []
for sub in itertools.combinations(list(itertools.product(range(3), repeat=3)), 6):
    if balanced(sub, 3, 2) and pair_injective(sub):
        Y6.append(tuple(sub))
R['Y6_fibre_count'] = len(Y6)

# X eight-point fibres: BC graph 2-regular on 4+4, then D assignment.
two_regular_44 = []
for rows in itertools.product([frozenset(c) for c in itertools.combinations(range(4), 2)], repeat=4):
    cols = Counter(b for r in rows for b in r)
    if all(cols[b] == 2 for b in range(4)):
        two_regular_44.append(rows)
R['two_regular_4x4_graphs'] = len(two_regular_44)

X8 = []
for rows in two_regular_44:
    nbrs = [sorted(rows[b]) for b in range(4)]
    for dchoice in itertools.product(itertools.permutations(range(4), 2), repeat=4):
        words = []
        for b in range(4):
            c1, c2 = nbrs[b]
            d1, d2 = dchoice[b]
            words.append((b, c1, d1))
            words.append((b, c2, d2))
        if balanced(words, 4, 2) and pair_injective(words):
            X8.append(tuple(sorted(words)))
X8 = sorted(set(X8))
R['X8_fibre_count'] = len(X8)


def projs(words):
    return (frozenset((w[0], w[1]) for w in words),
            frozenset((w[0], w[2]) for w in words),
            frozenset((w[1], w[2]) for w in words))


Y6_by_proj = Counter(projs(F) for F in Y6)
R['Y6_distinct_projection_triples'] = len(Y6_by_proj)
R['Y6_max_fibres_per_projection_triple'] = max(Y6_by_proj.values())
X8_by_proj = {}
for F in X8:
    X8_by_proj.setdefault(projs(F), []).append(F)
R['X8_distinct_projection_triples'] = len(X8_by_proj)
R['X8_max_fibres_per_projection_triple'] = max(len(v) for v in X8_by_proj.values())

# embedded Y fibres cached per (nb,nc,nd) 3-subsets
EMB = {}
for nb in itertools.combinations(range(4), 3):
    for nc in itertools.combinations(range(4), 3):
        for nd in itertools.combinations(range(4), 3):
            lst = []
            for F in Y6:
                W = tuple((nb[i], nc[j], nd[k]) for (i, j, k) in F)
                lst.append((W, projs(W)))
            EMB[(nb, nc, nd)] = lst

# ----------------------------------------------------------------------------
# 4. All-Y branch
# ----------------------------------------------------------------------------


def rect(G1, G2):
    return frozenset(itertools.product(G1, G2))


def low_contrib(GB, GC, GD, lows):
    L = [Counter(), Counter(), Counter()]
    for a in lows:
        for cell in rect(GB[a], GC[a]):
            L[0][cell] += 1
        for cell in rect(GB[a], GD[a]):
            L[1][cell] += 1
        for cell in rect(GC[a], GD[a]):
            L[2][cell] += 1
    return L


def solve_Y_pattern(GB, GC, GD):
    """Return list of (F2words, F3words) with BC/BD/CD multiplicities all in {0,2}."""
    L = low_contrib(GB, GC, GD, (0, 1))
    twos = [frozenset(c for c, m in Li.items() if m == 2) for Li in L]
    if any(m > 2 for Li in L for m in Li.values()):
        return []
    key3 = (tuple(sorted(GB[3])), tuple(sorted(GC[3])), tuple(sorted(GD[3])))
    key2 = (tuple(sorted(GB[2])), tuple(sorted(GC[2])), tuple(sorted(GD[2])))
    d3 = {}
    for W, P in EMB[key3]:
        d3.setdefault(P, []).append(W)
    sols = []
    for W2, P2 in EMB[key2]:
        if any(P2[i] & twos[i] for i in range(3)):
            continue
        req = tuple(frozenset(c for c in set(L[i]) | P2[i] if (L[i][c] + (c in P2[i])) % 2 == 1) for i in range(3))
        for W3 in d3.get(req, ()):
            sols.append((W2, W3))
    return sols


def low_fibre(GB, GC, GD, a, parity):
    nb, nc, nd = sorted(GB[a]), sorted(GC[a]), sorted(GD[a])
    return tuple((a, nb[i], nc[j], nd[k]) for i in range(2) for j in range(2) for k in range(2) if (i + j + k) % 2 == parity)


def full_support(GB, GC, GD, W2, W3, p0, p1):
    words = list(low_fibre(GB, GC, GD, 0, p0)) + list(low_fibre(GB, GC, GD, 1, p1))
    words += [(2,) + w for w in W2] + [(3,) + w for w in W3]
    return tuple(sorted(words))


CUTS = {'AB|CD': ((0, 1), (2, 3)), 'AC|BD': ((0, 2), (1, 3)), 'AD|BC': ((0, 3), (1, 2))}


def recount_ok(words):
    """Independent recount: 20 distinct words, every one of the six pair projections has
    exactly 10 cells each with exactly 2 extensions."""
    if len(set(words)) != 20:
        return False
    for i, j in itertools.combinations(range(4), 2):
        c = Counter((w[i], w[j]) for w in words)
        if len(c) != 10 or any(m != 2 for m in c.values()):
            return False
    return True


def cut_report(words, rowidx, colidx):
    rows, cols = {}, {}
    for w in words:
        r = tuple(w[i] for i in rowidx)
        c = tuple(w[i] for i in colidx)
        rows.setdefault(r, set()).add(c)
        cols.setdefault(c, set()).add(r)
    deg_ok = len(rows) == 10 and len(cols) == 10 and all(len(s) == 2 for s in rows.values()) and all(len(s) == 2 for s in cols.values())
    bad_rows = [(r1, r2) for r1, r2 in itertools.combinations(sorted(rows), 2) if len(rows[r1] & rows[r2]) == 1]
    bad_cols = [(c1, c2) for c1, c2 in itertools.combinations(sorted(cols), 2) if len(cols[c1] & cols[c2]) == 1]
    return deg_ok, bad_rows, bad_cols


def hamming1_pairs(words):
    within, cross = 0, 0
    for u, v in itertools.combinations(words, 2):
        if sum(x != y for x, y in zip(u, v)) == 1:
            if u[0] == v[0]:
                within += 1
            else:
                cross += 1
    return within, cross


# 4a. packet normalisation: 5 reps (min of orbit) x 34 x 34 with C<=D
rep_graphs = [tuple(frozenset(r) for r in parse_rep(s)) for s in PACKET_YY]
patterns_norm = 0
sols_norm = []
for ri, GB in enumerate(rep_graphs):
    for ci in range(len(YY)):
        for di in range(ci, len(YY)):
            patterns_norm += 1
            for W2, W3 in solve_Y_pattern(GB, YY[ci], YY[di]):
                sols_norm.append((ri, ci, di, W2, W3))
R['Y_normalised_pattern_count'] = patterns_norm
R['Y_normalised_highfibre_solutions'] = len(sols_norm)
R['Y_normalised_distinct_signature_pairs'] = len({(projs(W2), projs(W3)) for _, _, _, W2, W3 in sols_norm})
R['Y_normalised_patterns_with_solutions'] = sorted({(ri, ci, di) for ri, ci, di, _, _ in sols_norm})

supports = []
for ri, ci, di, W2, W3 in sols_norm:
    for p0 in (0, 1):
        for p1 in (0, 1):
            supports.append(((ri, ci, di, p0, p1), full_support(rep_graphs[ri], YY[ci], YY[di], W2, W3, p0, p1)))
R['Y_normalised_support_count'] = len(supports)
R['Y_normalised_distinct_supports'] = len({s for _, s in supports})

sup_reports = []
all_fail_every_cut = True
cross_h1_count = 0
for tag, S in supports:
    assert recount_ok(S), ('recount failed', tag)
    cr = {}
    fails = 0
    for name, (ri_, ci_) in CUTS.items():
        deg_ok, br, bc = cut_report(S, ri_, ci_)
        assert deg_ok, (tag, name)
        cr[name] = {'row_pairs_sharing_exactly_one': len(br), 'col_pairs_sharing_exactly_one': len(bc),
                    'witness': [list(map(list, br[0]))] if br else [list(map(list, bc[0]))]}
        if br or bc:
            fails += 1
    if fails != 3:
        all_fail_every_cut = False
    w1, c1 = hamming1_pairs(S)
    assert w1 == 0, tag
    if c1 > 0:
        cross_h1_count += 1
    sup_reports.append({'tag': list(tag), 'words': [list(w) for w in S], 'cuts': cr, 'cross_fibre_hamming1_pairs': c1})
R['Y_all_supports_fail_in_every_cut'] = all_fail_every_cut
R['Y_supports_with_cross_fibre_hamming1'] = cross_h1_count
R['Y_supports'] = sup_reports

# mutation control: replace one word of the first support, recount must fail
if supports:
    S0 = list(supports[0][1])
    mutated = tuple(sorted(S0[:-1] + [(S0[-1][0], S0[-1][1], S0[-1][2], (S0[-1][3] + 1) % 4)]))
    R['mutation_control_recount_rejects'] = (not recount_ok(mutated))
    assert R['mutation_control_recount_rejects']

# 4b. fully labelled 34^3 enumeration (no orbit reduction at all)
t1 = time.time()
labelled_solutions = []
for bi in range(len(YY)):
    for ci in range(len(YY)):
        for di in range(len(YY)):
            for W2, W3 in solve_Y_pattern(YY[bi], YY[ci], YY[di]):
                labelled_solutions.append((bi, ci, di, W2, W3))
R['Y_fully_labelled_patterns'] = len(YY) ** 3
R['Y_fully_labelled_highfibre_solutions'] = len(labelled_solutions)
R['Y_fully_labelled_seconds'] = round(time.time() - t1, 2)

# every labelled solution's supports fail in all three cuts; and canonicalise to the normalised set
norm_support_set = {s for _, s in supports}


def canon_support(S):
    """Minimum over the full within-class relabelling group at A,B,C,D and S3 on (B,C,D)
    of the sorted word tuple -- used only to compare labelled vs normalised solutions."""
    best = None
    for pa in Y_perms:
        for pb in Y_perms:
            for pc_ in Y_perms:
                for pd in Y_perms:
                    base = [(pa[a], pb[b], pc_[c], pd[d]) for a, b, c, d in S]
                    for perm in itertools.permutations((1, 2, 3)):
                        T = tuple(sorted(tuple((w[0], w[perm[0]], w[perm[1]], w[perm[2]])) for w in base))
                        if best is None or T < best:
                            best = T
    return best


lab_fail_all = True
lab_canon = set()
lab_support_total = 0
for bi, ci, di, W2, W3 in labelled_solutions:
    for p0 in (0, 1):
        for p1 in (0, 1):
            S = full_support(YY[bi], YY[ci], YY[di], W2, W3, p0, p1)
            lab_support_total += 1
            assert recount_ok(S)
            fails = sum(1 for (ri_, ci_) in CUTS.values() if any(cut_report(S, ri_, ci_)[1:]))
            if fails != 3:
                lab_fail_all = False
            lab_canon.add(canon_support(S))
norm_canon = {canon_support(s) for s in norm_support_set}
R['Y_fully_labelled_support_total'] = lab_support_total
R['Y_fully_labelled_all_fail_every_cut'] = lab_fail_all
R['Y_canonical_classes_labelled'] = len(lab_canon)
R['Y_canonical_classes_normalised'] = len(norm_canon)
R['Y_canonical_classes_equal'] = (lab_canon == norm_canon)

# ----------------------------------------------------------------------------
# 5. One-X branch
# ----------------------------------------------------------------------------


def is_two_regular(cells):
    if len(cells) != 8:
        return False
    rc = Counter(c[0] for c in cells)
    cc = Counter(c[1] for c in cells)
    return all(rc[x] == 2 for x in range(4)) and all(cc[x] == 2 for x in range(4))


def solve_X_pattern(GB, GC, GD):
    assert GB[3] == frozenset(range(4)) and GC[3] == frozenset(range(4)) and GD[3] == frozenset(range(4))
    L = low_contrib(GB, GC, GD, (0, 1, 2))
    if any(m > 2 for Li in L for m in Li.values()):
        return None, []
    req = tuple(frozenset(c for c, m in L[i].items() if m == 1) for i in range(3))
    if not all(is_two_regular(r) for r in req):
        return None, []
    return req, X8_by_proj.get(req, [])


def compatible_triples(req):
    bc, bd, cd = req
    return sorted((b, c, d) for b in range(4) for c in range(4) for d in range(4) if (b, c) in bc and (b, d) in bd and (c, d) in cd)


x_rep_graphs = [tuple(frozenset(r) for r in parse_rep(s)) for s in PACKET_XY]
x_patterns = 0
x_graph_triples = {}
x_matches = 0
for ri, GB in enumerate(x_rep_graphs):
    for ci in range(len(XY)):
        for di in range(ci, len(XY)):
            x_patterns += 1
            req, found = solve_X_pattern(GB, XY[ci], XY[di])
            if req is not None:
                x_matches += len(found)
                ct = compatible_triples(req)
                x_graph_triples.setdefault(req, []).append({'pattern': [ri, ci, di], 'compatible_triples': len(ct),
                                                             'compatible_pair_injective': pair_injective(ct) and len(ct) == 8,
                                                             'distinct_edges_per_projection': [len({(w[0], w[1]) for w in ct}), len({(w[0], w[2]) for w in ct}), len({(w[1], w[2]) for w in ct})],
                                                             'x8_fibres_with_these_projections': len(found)})
R['X_normalised_pattern_count'] = x_patterns
R['X_normalised_two_regular_requirement_graph_triples'] = len(x_graph_triples)
R['X_normalised_patterns_passing_two_regular'] = sum(len(v) for v in x_graph_triples.values())
R['X_normalised_eightfibre_matches'] = x_matches
R['X_normalised_graph_triple_details'] = [{'bc': sorted(map(list, k[0])), 'bd': sorted(map(list, k[1])), 'cd': sorted(map(list, k[2])), 'occurrences': v} for k, v in x_graph_triples.items()]

# fully labelled 15^3
xl_patterns = 0
xl_matches = 0
xl_pass = 0
for bi in range(len(XY)):
    for ci in range(len(XY)):
        for di in range(len(XY)):
            xl_patterns += 1
            req, found = solve_X_pattern(XY[bi], XY[ci], XY[di])
            if req is not None:
                xl_pass += 1
                xl_matches += len(found)
R['X_fully_labelled_patterns'] = xl_patterns
R['X_fully_labelled_patterns_passing_two_regular'] = xl_pass
R['X_fully_labelled_eightfibre_matches'] = xl_matches

# positive control for the X lookup machinery: every catalog fibre must be found from its own projections
assert all(F in X8_by_proj[projs(F)] for F in X8)
# positive control for the Y machinery: build a pattern from a known solution and re-solve
if sols_norm:
    ri, ci, di, W2, W3 = sols_norm[0]
    assert (W2, W3) in solve_Y_pattern(rep_graphs[ri], YY[ci], YY[di])

# ----------------------------------------------------------------------------
# 6. Side controls
# ----------------------------------------------------------------------------
# m=8 complement: 4 words, six pair projections of size exactly 2, each cell exactly 2 extensions.
# Projection size 2 forces <=2 symbols per coordinate, so {0,1}^4 is exhaustive up to relabelling.
m8_hits = 0
for sub in itertools.combinations(list(itertools.product(range(2), repeat=4)), 4):
    ok = True
    for i, j in itertools.combinations(range(4), 2):
        c = Counter((w[i], w[j]) for w in sub)
        if len(c) != 2 or any(m != 2 for m in c.values()):
            ok = False
            break
    if ok:
        m8_hits += 1
R['m8_complement_binary_bruteforce_hits'] = m8_hits
assert m8_hits == 0

# m=6 complement: 8 words in {0,1}^4 with every pair projection full and each cell twice -- these DO
# exist combinatorially (e.g. even-weight words); the exclusion is the spin-flip argument, not support.
m6_hits = 0
for sub in itertools.combinations(list(itertools.product(range(2), repeat=4)), 8):
    ok = True
    for i, j in itertools.combinations(range(4), 2):
        c = Counter((w[i], w[j]) for w in sub)
        if len(c) != 4 or any(m != 2 for m in c.values()):
            ok = False
            break
    if ok:
        m6_hits += 1
R['m6_complement_binary_supports_exist'] = m6_hits

# ratio involution f(r) = -1/conj(r): involution, fixed-point free
import cmath
import random
random.seed(20261028)
inv_ok = True
for _ in range(1000):
    r = complex(random.uniform(-3, 3), random.uniform(-3, 3))
    if r == 0:
        continue
    f = -1 / r.conjugate()
    ff = -1 / f.conjugate()
    if abs(ff - r) > 1e-9 or abs(f - r) < 1e-9:
        inv_ok = False
R['ratio_involution_numeric_ok'] = inv_ok
# algebraic: f(r)=r  <=>  r*conj(r) = -1, impossible for complex r.

# spin-flip sign identity on random 4-qubit states (numpy optional)
try:
    import numpy as np
    I2 = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    paulis = [I2, X, Y, Z]

    def kron_all(ms):
        out = np.array([[1]], dtype=complex)
        for m in ms:
            out = np.kron(out, m)
        return out
    rng = np.random.default_rng(20261028)
    maxerr = 0.0
    for _ in range(5):
        v = rng.normal(size=16) + 1j * rng.normal(size=16)
        v /= np.linalg.norm(v)
        rho = np.outer(v, v.conj())
        Y4 = kron_all([Y] * 4)
        rho_t = Y4 @ rho.conj() @ Y4
        lhs = np.trace(rho @ rho_t).real
        rhs = 0.0
        for idx in itertools.product(range(4), repeat=4):
            P = kron_all([paulis[i] for i in idx])
            rP = np.trace(rho @ P).real
            w = sum(1 for i in idx if i != 0)
            rhs += ((-1) ** w) * rP * rP
        rhs /= 16
        maxerr = max(maxerr, abs(lhs - rhs))
    R['spinflip_sign_identity_max_abs_error'] = float(maxerr)
    R['spinflip_sign_identity_ok'] = bool(maxerr < 1e-9)
    # weight-sum bookkeeping used by the packet: (1 - 12 + 3)/16 = -1/2
    R['spinflip_two_uniform_overlap'] = (1 - 12 + 3) / 16
except Exception as e:  # pragma: no cover
    R['spinflip_sign_identity_ok'] = 'numpy unavailable: ' + repr(e)

R['end_clock'] = clock()
R['elapsed_seconds'] = round(time.time() - T0, 2)
R['self_sha256'] = sha256_path(os.path.abspath(__file__))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    out = sys.argv[1]
    if os.path.exists(out):
        print('refusing to overwrite', out)
        sys.exit(3)
    with open(out, 'x') as f:
        json.dump(R, f, indent=1, sort_keys=True, default=list)
        f.write('\n')
    brief = {k: v for k, v in R.items() if k not in ('Y_supports', 'X_normalised_graph_triple_details', 'Y_normalised_patterns_with_solutions')}
    print(json.dumps(brief, indent=1, sort_keys=True, default=list))
