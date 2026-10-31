#!/usr/bin/env python3
"""f56 independent verifier for the registered level-four full-band certificate.

Review-side program written separately for review wave
f56-levi-full-band-certificate-review.  It imports NO author module and
re-implements every step from the printed definitions:

  A. sl3 adjoint matrix-unit level-one model: relations (2.2), eight vectors
     (3.2)=(4.1), rank 8, weights (4.3), universal relations (3.1), full-Cartan
     identities (5.1)-(5.3).
  B. The eight level-one vectors as bracket trees in the ORIGINAL three-generator
     preliminary algebra; [f1,.],[f2,.],[f3,.],[e1,.],[e2,.],[h3,.] computed by
     tree Leibniz with the Cartan relations only; compared with the matrix-unit
     model modulo the actual K-ideal; level-one dimension table of F/K for
     a,b<=4 for all r,s (independent of r,s at level one).
  C. Eight-letter Levi model for the four critical degrees, all 16 classes
     each: own free source (Lyndon basis + right-nested spanning), own full
     node-3 ideal closure, own target ideals, own f1/f2 derivations, own f3 via
     right-nested recursion, own horizontal kernel, own symbolic k x k minor
     polynomial (exact, in Q[x,y]) compared coefficient-by-coefficient with the
     certificate, degree<=k per variable and total, nonzero constant,
     one-signedness, class constancy of ideals (r0, r0+1, r0+5), affineness of
     f3 (second differences), direct quotient-kernel ranks at sample points,
     exact block/class/replacement-set enforcement, and MIXED status
     re-derivation for the three replaced producer minors.
  D. Levi-weight finite critical sets for n=1..4.

`--corrupt NAME` injects one intended-reason fault for controls.
Output: exclusive new JSON next to this file (refuses to overwrite).
"""
import argparse
import itertools
import json
import sys
import time
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

EVID = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody')
CERT = EVID / 'frontier-20261028-levi-critical-minors-v1.json'
ALT = EVID / 'frontier-20261028-levi-critical-alternates-v1.json'
REPLAY = EVID / 'frontier-20261028-levi-critical-independent-replay-v1.json'
HERE = Path(__file__).resolve().parent
CORRUPT = None
CLASSES = (1, 2, 3, '>=4')
DEGREES = ((3, 2, 4), (3, 3, 3), (3, 3, 4), (4, 4, 4))

# ----------------------------------------------------------------- linear algebra


def vadd(a, b, c=Q(1)):
    for k, x in b.items():
        y = a.get(k, 0) + c * x
        if y:
            a[k] = y
        else:
            a.pop(k, None)
    return a


class Span:
    """Fully reduced sparse Gauss-Jordan span with least-key pivots (canonical normal form)."""

    def __init__(self, vectors=()):
        self.rows = {}
        for v in vectors:
            self.add(v)

    def reduce(self, v):
        v = {k: Q(x) for k, x in v.items() if x}
        for p in list(v):
            if p in self.rows and p in v:
                vadd(v, self.rows[p], -v[p])
        return v

    def add(self, v):
        v = self.reduce(v)
        if not v:
            return None
        # Pivot = lexicographically LEAST key.  This fixes the canonical normal
        # form (standard monomials = words that are not least words of T); the
        # certificate's target-word pivots are coordinates in exactly this form.
        p = min(v)
        d = v[p]
        v = {k: x / d for k, x in v.items()}
        for row in self.rows.values():
            if p in row:
                vadd(row, v, -row[p])
        self.rows[p] = v
        return dict(v)

    def __len__(self):
        return len(self.rows)

    def contains(self, v):
        return not self.reduce(v)

    def same_as(self, other):
        return len(self) == len(other) and all(other.contains(r) for r in self.rows.values()) \
            and all(self.contains(r) for r in other.rows.values())


class Tracked:
    """Gauss-Jordan span remembering each row as a combination of inserted generators."""

    def __init__(self):
        self.rows = {}
        self.count = 0

    def express(self, v):
        v = {k: Q(x) for k, x in v.items() if x}
        combo = {}
        for p in list(v):
            if p in self.rows and p in v:
                row, cmb = self.rows[p]
                c = v[p]
                vadd(v, row, -c)
                vadd(combo, cmb, c)
        return v, combo

    def add(self, v):
        idx = self.count
        self.count += 1
        rem, combo = self.express(v)
        if not rem:
            return None
        cmb = {idx: Q(1)}
        vadd(cmb, combo, Q(-1))
        p = max(rem)
        d = rem[p]
        rem = {k: x / d for k, x in rem.items()}
        cmb = {j: x / d for j, x in cmb.items()}
        for row, c2 in self.rows.values():
            if p in row:
                f = row[p]
                vadd(row, rem, -f)
                vadd(c2, cmb, -f)
        self.rows[p] = (rem, cmb)
        return idx

    def coordinates(self, v):
        rem, combo = self.express(v)
        assert not rem, 'vector outside tracked span'
        return combo

    def __len__(self):
        return len(self.rows)


def nullspace(columns):
    """Basis of {c : sum_j c_j columns[j] = 0}, as dicts over column indices."""
    tr = Tracked()
    out = []
    for j, col in enumerate(columns):
        rem, combo = tr.express(col)
        if not rem:
            c = {j: Q(1)}
            vadd(c, combo, Q(-1))
            out.append(c)
            tr.count += 1
        else:
            assert tr.add(col) == j
    return out


def rank(vectors):
    return len(Span(vectors))


# ----------------------------------------------------------------- tensor algebra


def tbr(a, b):
    out = {}
    for w, x in a.items():
        for u, y in b.items():
            out[w + u] = out.get(w + u, 0) + x * y
            out[u + w] = out.get(u + w, 0) - x * y
    return {w: Q(c) for w, c in out.items() if c}


def letter(i):
    return {(i,): Q(1)}


def is_lyndon(w):
    return all(w < w[k:] for k in range(1, len(w)))


@lru_cache(maxsize=None)
def std_bracket(w):
    if len(w) == 1:
        return letter(w[0])
    for i in range(1, len(w)):
        if is_lyndon(w[i:]):
            res = tbr(std_bracket(w[:i]), std_bracket(w[i:]))
            assert res.get(w) == 1 and min(res) == w
            return res
    raise AssertionError(w)


@lru_cache(maxsize=None)
def nested_poly(w):
    if len(w) == 1:
        return letter(w[0])
    return tbr(letter(w[0]), nested_poly(w[1:]))


# ----------------------------------------------------------------- polynomials Q[x,y]


def pmul(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            key = (i + k, j + l)
            out[key] = out.get(key, 0) + a * b
    return {m: c for m, c in out.items() if c}


def pdet(M):
    n = len(M)

    @lru_cache(maxsize=None)
    def rec(i, mask):
        if i == n:
            return {(0, 0): Q(1)}
        out = {}
        pos = 0
        for j in range(n):
            if mask >> j & 1:
                continue
            if M[i][j]:
                vadd(out, pmul(M[i][j], rec(i + 1, mask | (1 << j))), Q(1 if pos % 2 == 0 else -1))
            pos += 1
        return out
    return dict(rec(0, 0))


def poly_from_cert(entries):
    out = {}
    for t in entries:
        key = (int(t['x_power']), int(t['y_power']))
        assert key not in out, 'duplicate monomial in certificate'
        c = Q(t['coefficient'])
        assert c != 0, 'zero coefficient printed in certificate'
        out[key] = c
    return out


# ----------------------------------------------------------------- Section A: sl3 model


def E(i, j):
    return {(i, j): Q(1)}


def madd(*terms):
    out = {}
    for c, m in terms:
        vadd(out, m, Q(c))
    return out


def mmul(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            if j == k:
                out[(i, l)] = out.get((i, l), 0) + x * y
    return {k: v for k, v in out.items() if v}


def mbr(a, b):
    return madd((1, mmul(a, b)), (-1, mmul(b, a)))


def section_a():
    x, y, f1, f2, v = E(1, 2), E(2, 3), E(2, 1), E(3, 2), E(3, 1)
    h1 = madd((1, E(1, 1)), (-1, E(2, 2)))
    h2 = madd((1, E(2, 2)), (-1, E(3, 3)))
    z = mbr(x, y)
    ad = lambda a, b: mbr(a, b)
    assert z == E(1, 3)
    assert not ad(x, z) and not ad(y, z), '[x,z]=[y,z]=0'
    assert not ad(x, ad(x, v)) and not ad(y, ad(y, v)), 'x^2 v = y^2 v = 0'
    assert not ad(f1, v) and not ad(f2, v), 'f1 v = f2 v = 0'
    assert ad(h1, v) == madd((-1, v)) and ad(h2, v) == madd((-1, v)), 'h weights -1'
    xv, yv, zv = ad(x, v), ad(y, v), ad(z, v)
    eight = [v, xv, yv, zv, ad(x, yv), ad(z, xv), ad(z, yv), ad(z, zv)]
    expected = [E(3, 1), madd((-1, E(3, 2))), E(2, 1), madd((1, E(1, 1)), (-1, E(3, 3))),
                madd((1, E(1, 1)), (-1, E(2, 2))), madd((-1, E(1, 2))), madd((-1, E(2, 3))),
                madd((-2, E(1, 3)))]
    assert eight == expected, 'eight images (4.1)'
    assert rank(eight) == 8, 'rank 8'
    # universal relations (3.1) and consequences inside the model
    assert ad(z, zv) == madd((2, ad(z, ad(x, yv)))), 'z^2 v = 2 z x y v'
    assert not ad(z, ad(z, xv)) and not ad(z, ad(z, yv)) and not ad(z, ad(z, zv)), 'z^2 x v = z^2 y v = z^3 v = 0'
    assert ad(x, ad(x, yv)) == madd((2, ad(z, xv))), 'x^2 y v = 2 z x v'
    # weights -> horizontal increments
    weights = []
    for m in eight:
        w1 = next(iter({c / m[k] for k, c in ad(h1, m).items()} | ({Q(0)} if not ad(h1, m) else set())))
        w2 = next(iter({c / m[k] for k, c in ad(h2, m).items()} | ({Q(0)} if not ad(h2, m) else set())))
        assert ad(h1, m) == madd((w1, m)) and ad(h2, m) == madd((w2, m)), 'eigenvectors of h1,h2'
        a = (2 * (w1 + 1) + (w2 + 1)) / 3
        b = ((w1 + 1) + 2 * (w2 + 1)) / 3
        assert a.denominator == 1 and b.denominator == 1
        weights.append((int(a), int(b)))
    assert tuple(weights) == ((0, 0), (1, 0), (0, 1), (1, 1), (1, 1), (2, 1), (1, 2), (2, 2)), weights
    dims = {}
    for w in weights:
        dims[w] = dims.get(w, 0) + 1
    assert dims == {(0, 0): 1, (1, 0): 1, (0, 1): 1, (1, 1): 2, (2, 1): 1, (1, 2): 1, (2, 2): 1}, '(4.3)'
    # (5.1)-(5.3) identities for several complex-rational rows c_p = (c1,c2,c3)
    H1, H2 = h1, h2
    for c1, c2, c3 in [(Q(-1), Q(-2), Q(2)), (Q(-3), Q(-1), Q(2)), (Q(7, 3), Q(-5, 2), Q(1, 7)), (Q(0), Q(0), Q(1)), (Q(2), Q(-1), Q(-1))]:
        A = (2 * c1 + c2) / 3
        B = (c1 + 2 * c2) / 3
        lam = c3 + A + B
        assert 2 * A - B == c1 and -A + 2 * B == c2 and lam == c3 + c1 + c2, '(5.1)'
        # action (5.3) on each basis vector: ad(A H1 + B H2) + lam
        for m, (a, b) in zip(eight, weights):
            act = madd((1, mbr(madd((A, H1), (B, H2)), m)), (lam, m))
            # expected: (c1 a + c2 b + c3) m  (root (a,b,1) paired with row c)
            assert act == madd((c1 * a + c2 * b + c3, m)), '(5.3) reproduces root pairing'
    # p = 3: c = (-r,-s,2) gives 2 - r a - s b
    for r, s in [(1, 1), (2, 5), (4, 3)]:
        for m, (a, b) in zip(eight, weights):
            A3, B3, l3 = Q(-(2 * r + s), 3), Q(-(r + 2 * s), 3), Q(2 - r - s)
            act = madd((1, mbr(madd((A3, H1), (B3, H2)), m)), (l3, m))
            assert act == madd((2 - r * a - s * b, m))
    return {'eight_images': 'match (4.1)', 'rank': 8, 'weights': weights, 'dims_4_3': {str(k): v for k, v in dims.items()},
            'universal_relations_3_1_in_model': True, 'full_cartan_5_1_to_5_3': True}


# ----------------------------------------------------------------- Section B: original preliminary algebra trees

M_TREES = (3, (1, 3), (2, 3), ((1, 2), 3), (1, (2, 3)), ((1, 2), (1, 3)), ((1, 2), (2, 3)), ((1, 2), ((1, 2), 3)))
WEIGHTS = ((0, 0), (1, 0), (0, 1), (1, 1), (1, 1), (2, 1), (1, 2), (2, 2))


def tree_poly(t):
    if isinstance(t, int):
        return letter(t)
    return tbr(tree_poly(t[0]), tree_poly(t[1]))


def tree_counts(t):
    if isinstance(t, int):
        return tuple(1 if t == i else 0 for i in (1, 2, 3))
    a, b = tree_counts(t[0]), tree_counts(t[1])
    return tuple(x + y for x, y in zip(a, b))


def cartan_matrix(r, s):
    return ((2, -1, -1), (-1, 2, -1), (-r, -s, 2))


def rootval(t, i, A):
    n = tree_counts(t)
    return sum(n[j] * A[i - 1][j] for j in range(3))


def D(t, i, A):
    """[f_i, t] in the preliminary algebra: returns (coefficient of h_i, positive tensor polynomial)."""
    if isinstance(t, int):
        return (Q(-1) if t == i else Q(0)), {}
    L, R = t
    cL, pL = D(L, i, A)
    cR, pR = D(R, i, A)
    out = {}
    if cL:
        vadd(out, tree_poly(R), cL * rootval(R, i, A))
    if pL:
        vadd(out, tbr(pL, tree_poly(R)))
    if cR:
        vadd(out, tree_poly(L), -cR * rootval(L, i, A))
    if pR:
        vadd(out, tbr(tree_poly(L), pR))
    return Q(0), out


def words_counts(counts):
    letters = [i + 1 for i in range(3) for _ in range(counts[i])]
    return sorted(set(itertools.permutations(letters)))


def original_ideal_generators(degree, seeds):
    """All iterated simple adjoints of the given seeds landing at degree (letters 1..3)."""
    out = []
    for poly, sdeg in seeds:
        rest = tuple(degree[k] - sdeg[k] for k in range(3))
        if min(rest) < 0:
            continue
        for prefix in words_counts(rest):
            v = poly
            for a in reversed(prefix):
                v = tbr(letter(a), v)
            if v:
                out.append(v)
    return out


def original_seed(i, j, exponent):
    v = letter(j)
    for _ in range(exponent):
        v = tbr(letter(i), v)
    return v


def fixed_node_seeds():
    return [(original_seed(1, 2, 2), (2, 1, 0)), (original_seed(2, 1, 2), (1, 2, 0)),
            (original_seed(1, 3, 2), (2, 0, 1)), (original_seed(2, 3, 2), (0, 2, 1))]


def all_seeds(r, s):
    return fixed_node_seeds() + [(original_seed(3, 1, r + 1), (1, 0, r + 1)), (original_seed(3, 2, s + 1), (0, 1, s + 1))]


def model_actions():
    """Coordinates of [g, B_j] in basis B, solved (not typed) from the matrix model."""
    x, y, f1, f2, v = E(1, 2), E(2, 3), E(2, 1), E(3, 2), E(3, 1)
    z = mbr(x, y)
    basis = [E(3, 1), madd((-1, E(3, 2))), E(2, 1), madd((1, E(1, 1)), (-1, E(3, 3))),
             madd((1, E(1, 1)), (-1, E(2, 2))), madd((-1, E(1, 2))), madd((-1, E(2, 3))), madd((-2, E(1, 3)))]
    tr = Tracked()
    for b in basis:
        assert tr.add(b) is not None
    ops = {'e1': x, 'e2': y, 'e12': z, 'f1': f1, 'f2': f2}
    if CORRUPT == 'swap_f1_f2':
        ops['f1'], ops['f2'] = ops['f2'], ops['f1']
    act = {}
    for g, op in ops.items():
        act[g] = []
        for b in basis:
            img = mbr(op, b)
            coords = tr.coordinates(img) if img else {}
            act[g].append({int(j): Q(c) for j, c in coords.items() if c})
    return act


ACT = None


def section_b():
    global ACT
    ACT = model_actions()
    polys = [tree_poly(t) for t in M_TREES]
    report = {}
    for r, s in [(1, 1), (2, 3), (4, 4), (3, 7)]:
        A = cartan_matrix(r, s)
        kspan = {}

        def K_at(deg):
            if deg not in kspan:
                kspan[deg] = Span(original_ideal_generators(deg, fixed_node_seeds()))
            return kspan[deg]
        # h3 pairing (3.2)/(4.3)
        for j, t in enumerate(M_TREES):
            a, b = WEIGHTS[j]
            assert tree_counts(t) == (a, b, 1)
            assert rootval(t, 3, A) == 2 - r * a - s * b, 'h3 formula'
        # local f3 table (3.1)/(4.2) derived by tree Leibniz
        c0, p0 = D(M_TREES[0], 3, A)
        assert c0 == -1 and not p0, '[f3,m0] = -h3'
        _, p1 = D(M_TREES[1], 3, A)
        assert p1 == {(1,): Q(-r)}, '[f3,m1] = -r e1'
        _, p2 = D(M_TREES[2], 3, A)
        assert p2 == {(2,): Q(-s)}, '[f3,m2] = -s e2'
        e12 = tbr(letter(1), letter(2))
        _, p3 = D(M_TREES[3], 3, A)
        assert p3 == {w: -(r + s) * c for w, c in e12.items()}, '[f3,m3] = -(r+s)[e1,e2]'
        _, p4 = D(M_TREES[4], 3, A)
        assert p4 == {w: -s * c for w, c in e12.items()}, '[f3,m4] = -s[e1,e2]'
        _, p5 = D(M_TREES[5], 3, A)
        assert p5 and K_at((2, 1, 0)).contains(p5) and len(K_at((2, 1, 0))) == 1, '[f3,m5] in K (Serre (ad e1)^2 e2)'
        _, p6 = D(M_TREES[6], 3, A)
        assert p6 and K_at((1, 2, 0)).contains(p6) and len(K_at((1, 2, 0))) == 1, '[f3,m6] in K (Serre (ad e2)^2 e1)'
        _, p7 = D(M_TREES[7], 3, A)
        assert not p7, '[f3,m7] = 0'
        # f1, f2, e1, e2 actions on m_j equal matrix-unit coordinates modulo K at level one
        for g, i in (('f1', 1), ('f2', 2)):
            for j, t in enumerate(M_TREES):
                c, p = D(t, i, A)
                assert c == 0
                expected = {}
                for l, coef in ACT[g][j].items():
                    vadd(expected, polys[l], coef)
                a, b = WEIGHTS[j]
                deg = (a - (i == 1), b - (i == 2), 1)
                diff = dict(p)
                vadd(diff, expected, Q(-1))
                if min(deg) < 0:
                    assert not p and not expected, (g, j)
                else:
                    assert K_at(deg).contains(diff), ('f action mismatch', g, j, r, s)
        for g, i in (('e1', 1), ('e2', 2), ('e12', None)):
            op = letter(i) if i else tbr(letter(1), letter(2))
            for j, t in enumerate(M_TREES):
                p = tbr(op, polys[j])
                expected = {}
                for l, coef in ACT[g][j].items():
                    vadd(expected, polys[l], coef)
                a, b = WEIGHTS[j]
                deg = (a + (1 if g in ('e1', 'e12') else 0), b + (1 if g in ('e2', 'e12') else 0), 1)
                diff = dict(p)
                vadd(diff, expected, Q(-1))
                assert K_at(deg).contains(diff), ('e action mismatch', g, j)
        # level-one dimension table of F/K for a,b<=4 (all seeds; node-3 seeds have level>=2 so J=K here)
        table = {}
        for a in range(5):
            for b in range(5):
                deg = (a, b, 1)
                lyn = [w for w in words_counts(deg) if is_lyndon(w)]
                free_dim = len(lyn)
                ideal = Span(original_ideal_generators(deg, all_seeds(r, s)))
                for row in ideal.rows.values():
                    assert Span(std_bracket(w) for w in lyn).contains(row)
                table[(a, b)] = free_dim - len(ideal)
        expected_table = {(0, 0): 1, (1, 0): 1, (0, 1): 1, (1, 1): 2, (2, 1): 1, (1, 2): 1, (2, 2): 1}
        assert all(table[k] == expected_table.get(k, 0) for k in table), table
        # the eight trees are a basis of F/K at level one (a,b<=2)
        for a in range(3):
            for b in range(3):
                deg = (a, b, 1)
                ideal = Span(original_ideal_generators(deg, fixed_node_seeds()))
                sp = Span(ideal.rows.values())
                cnt = 0
                for j, t in enumerate(M_TREES):
                    if WEIGHTS[j] == (a, b):
                        assert sp.add(polys[j]) is not None, 'tree dependent modulo K'
                        cnt += 1
                assert len(sp) == len(Span(std_bracket(w) for w in words_counts(deg) if is_lyndon(w))), 'trees + K do not span level one'
                assert cnt == expected_table.get((a, b), 0)
        report[f'r={r},s={s}'] = {'local_f3_table': True, 'h3_formula': True, 'f1_f2_e1_e2_e12_match_model_mod_K': True,
                                  'level_one_dims_a_b_le_4': {str(k): v for k, v in table.items() if v}}
    return report


# ----------------------------------------------------------------- Section C: eight-letter Levi model


def fits(a, b):
    return all(x <= y for x, y in zip(a, b))


def degree_of(word):
    return (sum(WEIGHTS[j][0] for j in word), sum(WEIGHTS[j][1] for j in word), len(word))


@lru_cache(maxsize=None)
def words_at(degree):
    a, b, n = degree
    if min(degree) < 0:
        return ()
    return tuple(w for w in itertools.product(range(8), repeat=n) if degree_of(w) == degree)


def h3_scalar(j, r, s):
    a, b = WEIGHTS[j]
    base = 2 if CORRUPT != 'h3_const' else 1
    return Q(base - r * a - s * b)


def act_letter(g, j, r, s):
    if g == 'h3':
        c = h3_scalar(j, r, s)
        return {j: c} if c else {}
    return ACT[g][j]


def der(vec, g, r, s):
    out = {}
    for w, c in vec.items():
        for k, j in enumerate(w):
            for t, coef in act_letter(g, j, r, s).items():
                nw = w[:k] + (t,) + w[k + 1:]
                out[nw] = out.get(nw, 0) + c * coef
    return {w: c for w, c in out.items() if c}


def local(j, r, s):
    table = ({'h3': -1}, {'e1': -r}, {'e2': -s}, {'e12': -(r + s)}, {'e12': -s}, {}, {}, {})
    if CORRUPT == 'local_m4_r':
        table = ({'h3': -1}, {'e1': -r}, {'e2': -s}, {'e12': -(r + s)}, {'e12': -r}, {}, {}, {})
    return {g: Q(c) for g, c in table[j].items()}


@lru_cache(maxsize=None)
def d3_nested(word, r, s):
    assert len(word) >= 2
    head, rest = word[0], word[1:]
    out = {}
    N = nested_poly(rest)
    for g, c in local(head, r, s).items():
        vadd(out, der(N, g, r, s), c)
    if len(rest) == 1:
        for g, c in local(rest[0], r, s).items():
            vadd(out, der(letter(head), g, r, s), -c)
    else:
        vadd(out, tbr(letter(head), d3_nested(rest, r, s)))
    return out


class Degree:
    """Own free-source data at one degree: Lyndon basis and tracked right-nested spanning set."""

    def __init__(self, degree):
        self.degree = degree
        ws = words_at(degree)
        self.lyndon = tuple(w for w in ws if is_lyndon(w))
        self.nested = Tracked()
        self.nested_words = []
        for w in ws:
            idx = self.nested.add(nested_poly(w))
            self.nested_words.append(w)
        self.dim = len(self.nested)
        assert self.dim == len(self.lyndon), ('Lyndon count vs nested rank', degree)
        assert len(Span(std_bracket(w) for w in self.lyndon)) == self.dim


@lru_cache(maxsize=None)
def degree_data(degree):
    return Degree(degree)


def f3(vec, degree, r, s):
    coords = degree_data(degree).nested.coordinates(vec)
    out = {}
    for idx, c in coords.items():
        vadd(out, d3_nested(degree_data(degree).nested_words[idx], r, s), c)
    return out


def seeds_levi(r, s):
    out = []
    for j, power in ((1, r), (2, s)):
        if CORRUPT == 'drop_rho32' and j == 2:
            continue
        v = letter(j)
        for _ in range(power):
            v = tbr(letter(0), v)
        out.append(((WEIGHTS[j][0], WEIGHTS[j][1], power + 1), {w: -c for w, c in v.items()}))
    return out


def ideal_spaces(bound, r, s):
    spaces = {}
    work = []

    def ins(d, v):
        if not v or not fits(d, bound):
            return
        assert all(degree_of(w) == d for w in v), ('graded action', d)
        row = spaces.setdefault(d, Span()).add(v)
        if row is not None:
            work.append((d, row))
    for d, v in seeds_levi(r, s):
        ins(d, v)
    while work:
        d, v = work.pop()
        ins((d[0] + 1, d[1], d[2]), der(v, 'e1', r, s))
        ins((d[0], d[1] + 1, d[2]), der(v, 'e2', r, s))
        if d[2] < bound[2] and CORRUPT != 'no_letter_closure':
            for j in range(8):
                ins((d[0] + WEIGHTS[j][0], d[1] + WEIGHTS[j][1], d[2] + 1), tbr(letter(j), v))
    return spaces


def target_space(spaces, degree):
    rows = []
    for i in range(3):
        d = list(degree)
        d[i] -= 1
        if min(d) < 0:
            continue
        for row in spaces.get(tuple(d), Span()).rows.values():
            rows.append({(i, w): c for w, c in row.items()})
    return Span(rows)


def delta(vec, degree, r, s):
    out = {(0, w): c for w, c in der(vec, 'f1', r, s).items()}
    out.update({(1, w): c for w, c in der(vec, 'f2', r, s).items()})
    out.update({(2, w): c for w, c in f3(vec, degree, r, s).items()})
    return out


def restrict(v, comps):
    return {k: c for k, c in v.items() if k[0] in comps}


def analyse_class(degree, rc, sc, cert, producer_original=None):
    """Own reconstruction for one class, compared with certificate record `cert`."""
    r0 = 4 if rc == '>=4' else rc
    s0 = 4 if sc == '>=4' else sc
    dd = degree_data(degree)
    spaces = ideal_spaces(degree, r0, s0)
    ideal = spaces.get(degree, Span())
    lyndon_span = Span(std_bracket(w) for w in dd.lyndon)
    for row in ideal.rows.values():
        assert lyndon_span.contains(row), 'ideal row outside free source'
    m = dd.dim - len(ideal)
    out = {'r_class': rc, 's_class': sc, 'own_free_dim': dd.dim, 'own_ideal_dim': len(ideal), 'own_source_dim': m}
    # class constancy: ideal spans identical at r0+1, r0+5 (and s) inside the class
    if rc == '>=4' or sc == '>=4':
        for dr_, ds_ in ((1, 0), (5, 0), (0, 1), (0, 5), (3, 3)):
            if (dr_ and rc != '>=4') or (ds_ and sc != '>=4'):
                continue
            other = ideal_spaces(degree, r0 + dr_, s0 + ds_)
            for d in set(spaces) | set(other):
                assert spaces.get(d, Span()).same_as(other.get(d, Span())), ('ideal not constant in class', degree, rc, sc, d)
        out['class_constancy_checked'] = True
    assert cert['source_dim'] == m, ('source dim', degree, rc, sc, cert['source_dim'], m)
    if m == 0:
        assert cert['status'] == 'ZERO_SOURCE', cert['status']
        assert cert.get('horizontal_kernel_dim', 0) == 0
        out['own_status'] = 'ZERO_SOURCE'
        return out
    assert cert['status'] != 'ZERO_SOURCE'
    words = tuple(tuple(int(ch) for ch in w) for w in cert['source_words'])
    if CORRUPT == 'cert_words':
        other = next(w for w in dd.lyndon if w not in words)
        words = (other,) + words[1:]
    assert len(words) == m and len(set(words)) == m
    comp = Span(ideal.rows.values())
    basis = []
    for w in words:
        assert is_lyndon(w) and degree_of(w) == degree, ('complement word', w)
        v = std_bracket(w)
        assert comp.add(v) is not None, ('complement word dependent modulo ideal', w)
        basis.append(v)
    assert len(comp) == dd.dim, 'complement + ideal do not span the free source'
    target = target_space(spaces, degree)
    out['own_target_ideal_dim'] = len(target)
    points = [(r0, s0)]
    if rc == '>=4':
        points += [(r0 + 1, s0), (r0 + 2, s0)]
    if sc == '>=4':
        points += [(r0, s0 + 1), (r0, s0 + 2)]
    if rc == '>=4' and sc == '>=4':
        points += [(r0 + 1, s0 + 1)]
    cache = {}

    def proj(v, key, r, s):
        k = (key, r, s)
        if k not in cache:
            cache[k] = target.reduce(delta(v, degree, r, s))
        return cache[k]
    for r, s in points:
        for q, row in enumerate(ideal.rows.values()):
            assert not proj(row, ('I', q), r, s), ('ideal derivative escaped target ideal', degree, rc, sc, r, s)
    cols = [proj(v, ('B', j), r0, s0) for j, v in enumerate(basis)]
    hor = [restrict(c, (0, 1)) for c in cols]
    own_kernel = nullspace(hor)
    k = len(own_kernel)
    assert m - rank(hor) == k
    out['own_horizontal_kernel_dim'] = k
    assert cert['horizontal_kernel_dim'] == k, ('horizontal kernel dim', degree, rc, sc, cert['horizontal_kernel_dim'], k)
    # direct simultaneous quotient kernel at sample points (certificate-free)
    direct = {}
    for r, s in points:
        allcols = [proj(v, ('B', j), r, s) for j, v in enumerate(basis)]
        direct[f'{r},{s}'] = m - rank(allcols)
    out['direct_quotient_kernel_at_points'] = direct
    assert all(v == 0 for v in direct.values()), ('nonzero direct kernel', degree, rc, sc, direct)
    if k == 0:
        assert cert['status'] == 'ZERO_HORIZONTAL_KERNEL', cert['status']
        out['own_status'] = 'ZERO_HORIZONTAL_KERNEL'
        return out
    assert cert['status'] in ('CERTIFIED_ONE_SIGN', 'CERTIFIED_ONE_SIGN_ALTERNATE', 'MIXED_SIGNS_NEEDS_ANALYSIS'), cert['status']
    coeffs = [{int(j): Q(c) for j, c in row.items()} for row in cert['horizontal_kernel_coefficients']]
    if CORRUPT == 'cert_kernel' and coeffs:
        j0 = next(iter(coeffs[0]))
        coeffs[0][j0] += 1
    assert len(coeffs) == k and rank(coeffs) == k, 'certificate kernel vectors dependent or wrong count'
    kvecs = []
    for row in coeffs:
        v = {}
        for j, c in row.items():
            assert 0 <= j < m
            vadd(v, basis[j], c)
        kvecs.append(v)
    for r, s in points:
        for q, v in enumerate(kvecs):
            assert not restrict(proj(v, ('K', q), r, s), (0, 1)), ('certificate vector not in horizontal kernel', degree, rc, sc, r, s)
    # own kernel equals certificate kernel as subspaces of coefficient space
    assert Span(coeffs).same_as(Span(own_kernel)), 'kernel subspace mismatch'
    # f3 columns, affineness and symbolic entries
    f3cols = {}
    for r, s in points:
        f3cols[(r, s)] = [restrict(proj(v, ('K', q), r, s), (2,)) for q, v in enumerate(kvecs)]
    base = f3cols[(r0, s0)]
    dr = [dict() for _ in range(k)]
    ds = [dict() for _ in range(k)]
    if rc == '>=4':
        for q in range(k):
            dr[q] = vadd(dict(f3cols[(r0 + 1, s0)][q]), base[q], Q(-1))
            second = vadd(vadd(dict(f3cols[(r0 + 2, s0)][q]), f3cols[(r0 + 1, s0)][q], Q(-2)), base[q])
            assert not second, 'f3 not affine in r'
    if sc == '>=4':
        for q in range(k):
            ds[q] = vadd(dict(f3cols[(r0, s0 + 1)][q]), base[q], Q(-1))
            second = vadd(vadd(dict(f3cols[(r0, s0 + 2)][q]), f3cols[(r0, s0 + 1)][q], Q(-2)), base[q])
            assert not second, 'f3 not affine in s'
    if rc == '>=4' and sc == '>=4':
        for q in range(k):
            cross = vadd(vadd(vadd(dict(f3cols[(r0 + 1, s0 + 1)][q]), f3cols[(r0 + 1, s0)][q], Q(-1)), f3cols[(r0, s0 + 1)][q], Q(-1)), base[q])
            assert not cross, 'f3 has a bilinear r*s term'
    out['f3_affine_checked'] = True

    def minor_poly(pivots):
        rows = [(2, tuple(int(ch) for ch in w)) for w in pivots]
        assert len(rows) == k and len(set(rows)) == k, 'pivot count/duplicates'
        for key in rows:
            assert any(key in base[q] or key in dr[q] or key in ds[q] for q in range(k)), ('pivot row absent from f3 image', key)
        M = []
        for key in rows:
            M.append([{mon: c for mon, c in (((0, 0), base[q].get(key, 0)), ((1, 0), dr[q].get(key, 0)), ((0, 1), ds[q].get(key, 0))) if c} for q in range(k)])
        return pdet(M)
    pivots = list(cert['target_f3_word_pivots'])
    if CORRUPT == 'cert_pivot':
        candidates = sorted({w for q in range(k) for (_, w) in base[q]} - {tuple(int(ch) for ch in p) for p in pivots})
        pivots[0] = ''.join(map(str, candidates[0]))
    own_poly = minor_poly(pivots)
    cert_poly = poly_from_cert(cert['determinant_coefficients'])
    if CORRUPT == 'cert_sign' and len(cert_poly) >= 2:
        key = max(cert_poly)
        cert_poly[key] = -cert_poly[key]
    assert own_poly == cert_poly, ('determinant polynomial mismatch', degree, rc, sc, own_poly, cert_poly)
    const = own_poly.get((0, 0), 0)
    assert const != 0, 'zero constant term'
    signs = {1 if c > 0 else -1 for c in own_poly.values()}
    maxx = max(i for i, _ in own_poly)
    maxy = max(j for _, j in own_poly)
    maxtot = max(i + j for i, j in own_poly)
    assert maxx <= k and maxy <= k and maxtot <= k, ('degree bound', degree, rc, sc, maxx, maxy, maxtot, k)
    if rc != '>=4':
        assert maxx == 0, 'x appears although r is fixed in class'
    if sc != '>=4':
        assert maxy == 0, 'y appears although s is fixed in class'
    # grid binding (independent of the symbolic route): numeric determinants on {0..k}^2
    grid = 0
    for xg, yg in itertools.product(range(k + 1) if rc == '>=4' else range(1), range(k + 1) if sc == '>=4' else range(1)):
        r, s = r0 + xg, s0 + yg
        numeric = [[0] * k for _ in range(k)]
        colsrs = [restrict(target.reduce(delta(v, degree, r, s)), (2,)) for v in kvecs]
        rows = [(2, tuple(int(ch) for ch in w)) for w in pivots]
        mat = [[{(0, 0): colsrs[q].get(key, 0)} if colsrs[q].get(key, 0) else {} for q in range(k)] for key in rows]
        val = pdet(mat).get((0, 0), 0)
        expect = sum(c * Q(xg) ** i * Q(yg) ** j for (i, j), c in own_poly.items())
        assert val == expect, ('grid mismatch', degree, rc, sc, xg, yg)
        grid += 1
    out.update({'own_k': k, 'own_polynomial': {f'{i},{j}': str(c) for (i, j), c in sorted(own_poly.items())},
                'polynomial_matches_certificate': True, 'one_signed': len(signs) == 1, 'constant': str(const),
                'max_x_degree': maxx, 'max_y_degree': maxy, 'max_total_degree': maxtot, 'grid_points_bound': grid})
    if cert['status'] == 'MIXED_SIGNS_NEEDS_ANALYSIS':
        assert len(signs) == 2, 'producer MIXED status but one-signed polynomial'
        out['own_status'] = 'MIXED_SIGNS_CONFIRMED_NOT_A_CERTIFICATE'
        return out
    assert len(signs) == 1, ('mixed signs in a CERTIFIED class', degree, rc, sc)
    out['own_status'] = 'CERTIFIED_ONE_SIGN_OWN'
    if producer_original is not None:
        # re-derive the replaced producer minor and confirm it was genuinely mixed
        orig_poly = minor_poly(producer_original['target_f3_word_pivots'])
        assert orig_poly == poly_from_cert(producer_original['determinant_coefficients']), 'original producer polynomial mismatch'
        assert len({1 if c > 0 else -1 for c in orig_poly.values()}) == 2, 'original producer minor was not mixed'
        assert set(producer_original['target_f3_word_pivots']) != set(pivots), 'alternate pivots identical to original'
        out['replaced_producer_minor'] = {'pivots': producer_original['target_f3_word_pivots'], 'mixed_confirmed': True,
                                          'alternate_pivots': pivots}
    return out


def enforce_sets(producer, alternates, replay):
    """Exact block/class/replacement set enforcement (no blanket PASS adoption)."""
    blocks = producer['degrees']
    assert [tuple(b['degree']) for b in blocks] == list(DEGREES), 'producer degree blocks differ from the four critical degrees'
    expected_classes = [(r, s) for r in CLASSES for s in CLASSES]
    for b in blocks:
        got = [(c['r_class'], c['s_class']) for c in b['cases']]
        assert got == expected_classes, ('class set/order', b['degree'], got)
        assert len(b['cases']) == 16
    mixed = {(tuple(b['degree']), c['r_class'], c['s_class']) for b in blocks for c in b['cases'] if c['status'] == 'MIXED_SIGNS_NEEDS_ANALYSIS'}
    other = {c['status'] for b in blocks for c in b['cases']} - {'ZERO_SOURCE', 'ZERO_HORIZONTAL_KERNEL', 'CERTIFIED_ONE_SIGN', 'MIXED_SIGNS_NEEDS_ANALYSIS'}
    assert not other, ('unexpected producer status', other)
    alts = {(tuple(x['degree']), x['case']['r_class'], x['case']['s_class']) for x in alternates['cases']}
    assert len(alternates['cases']) == len(alts) == 3
    assert alts == mixed == {((3, 2, 4), '>=4', 3), ((3, 2, 4), '>=4', '>=4'), ((4, 4, 4), '>=4', '>=4')}, (alts, mixed)
    for x in alternates['cases']:
        assert x['case']['status'] == 'CERTIFIED_ONE_SIGN_ALTERNATE', x['case']['status']
        base = next(c for b in blocks if tuple(b['degree']) == tuple(x['degree']) for c in b['cases']
                    if (c['r_class'], c['s_class']) == (x['case']['r_class'], x['case']['s_class']))
        for key in ('source_dim', 'horizontal_kernel_dim', 'source_words', 'horizontal_kernel_coefficients'):
            assert x['case'][key] == base[key], ('alternate changed producer data', key)
    # replay output set check (metadata only; not adopted as evidence)
    assert [tuple(b['degree']) for b in replay['degrees']] == list(DEGREES)
    for b in replay['degrees']:
        assert [(c['r_class'], c['s_class']) for c in b['cases']] == expected_classes
    return {'degree_blocks': [list(d) for d in DEGREES], 'classes_per_block': 16, 'mixed_producer_classes_replaced': sorted(str(x) for x in mixed),
            'alternate_count': 3, 'producer_statuses_allowed': True}


def section_d():
    table = {}
    for n in range(1, 5):
        pairs = sorted((a, b) for a in range(0, 2 * n + 1) for b in range(0, 2 * n + 1) if 2 * a - b <= n and 2 * b - a <= n)
        assert all(a <= n and b <= n for a, b in pairs)
        table[n] = pairs
    expected = {1: [(0, 0), (1, 1)], 2: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2)],
                3: [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2), (3, 3)],
                4: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3), (4, 4)]}
    assert table == expected, table
    outside = {n: [p for p in table[n] if max(p) > 2] for n in table}
    assert outside == {1: [], 2: [], 3: [(3, 3)], 4: [(2, 3), (3, 2), (3, 3), (4, 4)]}, outside
    return {str(n): [list(p) for p in v] for n, v in table.items()}


def main():
    global CORRUPT
    ap = argparse.ArgumentParser()
    ap.add_argument('--corrupt', default=None)
    ap.add_argument('--only', default=None, help='restrict to one degree a,b,n for control runs')
    ap.add_argument('--output', default=None)
    args = ap.parse_args()
    CORRUPT = args.corrupt
    if CORRUPT == 'weights_m7':
        global WEIGHTS
        WEIGHTS = WEIGHTS[:7] + ((2, 1),)
    t0 = time.time()
    producer = json.loads(CERT.read_text(encoding='utf-8'))
    alternates = json.loads(ALT.read_text(encoding='utf-8'))
    replay = json.loads(REPLAY.read_text(encoding='utf-8'))
    result = {'corrupt': CORRUPT, 'sets': enforce_sets(producer, alternates, replay)}
    result['A'] = section_a()
    result['B'] = section_b()
    result['D'] = section_d()
    alt = {(tuple(x['degree']), x['case']['r_class'], x['case']['s_class']): x['case'] for x in alternates['cases']}
    only = tuple(int(x) for x in args.only.split(',')) if args.only else None
    blocks = []
    totals = {'classes': 0, 'zero_source': 0, 'zero_horizontal': 0, 'certified': 0, 'grid_points': 0}
    for b in producer['degrees']:
        degree = tuple(b['degree'])
        if only and degree != only:
            continue
        rows = []
        for c in b['cases']:
            key = (degree, c['r_class'], c['s_class'])
            cert = c if CORRUPT == 'use_original_mixed' else alt.get(key, c)
            rec = analyse_class(degree, c['r_class'], c['s_class'], cert, producer_original=c if key in alt else None)
            rows.append(rec)
            totals['classes'] += 1
            st = rec['own_status']
            if st == 'ZERO_SOURCE':
                totals['zero_source'] += 1
            elif st == 'ZERO_HORIZONTAL_KERNEL':
                totals['zero_horizontal'] += 1
            elif st == 'CERTIFIED_ONE_SIGN_OWN':
                totals['certified'] += 1
                totals['grid_points'] += rec['grid_points_bound']
            else:
                raise AssertionError(('unexpected own status', st))
            print('OK', degree, c['r_class'], c['s_class'], st, 'm', rec['own_source_dim'], 'k', rec.get('own_horizontal_kernel_dim', 0), flush=True)
        blocks.append({'degree': list(degree), 'classes': rows})
    result['C'] = {'blocks': blocks, 'totals': totals}
    result['elapsed_seconds'] = round(time.time() - t0, 2)
    result['python'] = sys.version
    text = json.dumps(result, indent=1, default=str) + '\n'
    out = Path(args.output) if args.output else HERE / 'f56-independent-verifier-result-v1.json'
    if not CORRUPT:
        with open(out, 'x', encoding='utf-8') as fh:
            fh.write(text)
        print('WROTE', out.name)
    print('ALL CHECKS PASSED', totals, 'elapsed', result['elapsed_seconds'], 's')


if __name__ == '__main__':
    main()
