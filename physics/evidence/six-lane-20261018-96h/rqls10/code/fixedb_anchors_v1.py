#!/usr/bin/env python3
"""fixedb_anchors_v1: EXACT stdlib construction and verification of the positive anchors for the proposed fixed-B unitary
model (lane note evidence/fixedb-unitary-model-proposal-v1.md): q_ij = U_i e_j with U_0 = I (rows exact).

Anchor v = 7 (Huang-Li, arXiv:2606.27758, Theorem "Construction--complete mapping" and the pan-diagonal transversals):
  phi_(i,j)(t) = omega^(t j + i mu(t)) / sqrt7, mu a complete mapping of Z_7 (mu and mu + id permutations) that is not
  affine (condition (*) for prime v); resolution B(i,j) = (j - i) mod 7. Converted to U-form: U_i = F^* [phi_(i,0) ...
  phi_(i,6)] with F = U_0 (the Fourier matrix), so U_0 = I.
Anchor v = 8 (Zhang-Cao, arXiv:2608.29201v2, Example 3.3): the printed 8 x 8 array (omega = e^(i pi/4)), resolution
  B(i,j) = i XOR j (the printed transversals T_k = {(i,j): i XOR j = k}); row 0 is the computational basis, so U_0 = I.
For each anchor: every row, column and B-class is an orthonormal basis (exact Gram = I in Q(zeta_N), N = 7 resp. 8, all
entries scaled to algebraic integers); exact distinct-ray count (q ~ q' iff |<q,q'>|^2 = |q|^2 |q'|^2); B is Latin;
the anchor is written as exact coefficient lists (entry = (1/den) * sum_k c_k zeta_N^k) for later float use.
Controls: one mutated entry must break orthogonality; the affine complete mapping mu(x) = 2x gives a 1-RQLS(7) with
fewer than 49 rays. Standard library; budget 250 s; output JSON (exclusive) argv[1].
"""
import itertools, json, sys, time

T0 = time.monotonic()
OUT = sys.argv[1]


class Cyc:
    """elements of Z[zeta_N] as integer coefficient lists modulo the cyclotomic polynomial (zero test exact)."""

    def __init__(self, N):
        self.N = N
        self.phi = self.cyclo(N)

    def cyclo(self, n):
        def pdiv(a, b):
            a = list(a)
            db = len(b) - 1
            q = [0] * (len(a) - db)
            for i in range(len(a) - 1, db - 1, -1):
                c = a[i]
                if c:
                    q[i - db] = c
                    for j in range(db + 1):
                        a[i - db + j] -= c * b[j]
            assert not any(a[:db])
            return q
        num = [-1] + [0] * (n - 1) + [1]
        for d in range(1, n):
            if n % d == 0:
                num = pdiv(num, self.cyclo(d))
        return num

    def zero(self, v):
        a = list(v)
        b = self.phi
        db = len(b) - 1
        for i in range(len(a) - 1, db - 1, -1):
            c = a[i]
            if c:
                for j in range(db + 1):
                    a[i - db + j] -= c * b[j]
        return not any(a[:db])

    def mul(self, a, b):
        N = self.N
        c = [0] * N
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        c[(i + j) % N] += x * y
        return c

    def conj(self, a):
        N = self.N
        return [a[(-k) % N] for k in range(N)]

    def add(self, a, b):
        return [x + y for x, y in zip(a, b)]

    def unit(self, e, c=1):
        v = [0] * self.N
        v[e % self.N] = c
        return v


def ip(K, u, v):
    s = [0] * K.N
    for x, y in zip(u, v):
        s = K.add(s, K.mul(K.conj(x), y))
    return s


def check(K, Q, B, den2):
    """Q[i][j] = vector (list of field elements) scaled so that <q,q> = den2; lines orthonormal iff Gram = den2 * I."""
    v = len(Q)
    lines = [[(i, j) for j in range(v)] for i in range(v)] + [[(i, j) for i in range(v)] for j in range(v)] + \
            [[(i, j) for i in range(v) for j in range(v) if B[i][j] == s] for s in range(v)]
    bad = 0
    for L in lines:
        for a in range(len(L)):
            for b in range(a, len(L)):
                g = ip(K, Q[L[a][0]][L[a][1]], Q[L[b][0]][L[b][1]])
                target = K.unit(0, den2) if a == b else [0] * K.N
                if not K.zero([x - y for x, y in zip(g, target)]):
                    bad += 1
    cells = [(i, j) for i in range(v) for j in range(v)]
    reps = []
    for c in cells:
        q = Q[c[0]][c[1]]
        for r in reps:
            g = ip(K, r, q)
            if K.zero([x - y for x, y in zip(K.mul(K.conj(g), g), K.unit(0, den2 * den2))]):
                break
        else:
            reps.append(q)
    latin = all(sorted(row) == list(range(v)) for row in B) and all(sorted(B[i][j] for i in range(v)) == list(range(v)) for j in range(v))
    return bad, len(reps), latin, len(lines)


out = {"probe": "fixedb_anchors_v1", "arithmetic": "integer cyclotomic (exact)"}

# ---------------- v = 7: Huang-Li complete-mapping construction
K7 = Cyc(7)
v = 7
cms = []
for perm in itertools.permutations(range(v)):
    if sorted((perm[x] + x) % v for x in range(v)) == list(range(v)):
        cms.append(perm)
affine = {tuple((a * x + b) % v for x in range(v)) for a in range(v) for b in range(v)}
nonaff = [m for m in cms if m not in affine]
mu = nonaff[0]


def huang_li(mu):
    # sqrt7 * phi_(i,j)(t) = zeta^(t j + i mu(t)); in U-form U_i = F^* Phi_i: (F^* phi_(i,j))(s) = (1/7) sum_t zeta^(-s t) zeta^(t j + i mu(t))
    Q = [[[K7.unit(t * j + i * mu[t]) for t in range(v)] for j in range(v)] for i in range(v)]
    QU = [[None] * v for _ in range(v)]
    for i in range(v):
        for j in range(v):
            vec = []
            for s in range(v):
                acc = [0] * v
                for t in range(v):
                    acc[(t * j + i * mu[t] - s * t) % v] += 1
                vec.append(acc)
            QU[i][j] = vec                      # = 7 * (F^* phi_(i,j)), norm^2 = 49
    return Q, QU


B7 = [[(j - i) % v for j in range(v)] for i in range(v)]
Q7, QU7 = huang_li(mu)
r7 = check(K7, Q7, B7, 7)
r7u = check(K7, QU7, B7, 49)
u0_identity = all(K7.zero([x - y for x, y in zip(QU7[0][j][s], K7.unit(0, 7 if s == j else 0))]) for j in range(v) for s in range(v))
mut = [row[:] for row in Q7]
mut[1] = [list(x) for x in Q7[1]]
mut[1][2] = [K7.unit(1) if k == 0 else K7.unit(0) for k in range(v)]
r7m = check(K7, mut, B7, 7)
Qa, _ = huang_li(tuple((2 * x) % v for x in range(v)))
r7a = check(K7, Qa, B7, 7)
out["v7"] = {"complete_mappings_of_Z7": len(cms), "non_affine": len(nonaff), "mu": list(mu),
             "bad_gram_entries": r7[0], "rays": r7[1], "B_latin": r7[2], "lines": r7[3],
             "U_form_bad_gram_entries": r7u[0], "U_form_rays": r7u[1], "U0_is_identity": u0_identity,
             "mutation_bad_gram_entries": r7m[0], "affine_mu_2x_rays": r7a[1], "affine_mu_2x_bad": r7a[0],
             "B": B7,
             "U_form_entries_note": "q_ij = U_i e_j; entry s of U_i e_j = (1/7) * sum_k c_k zeta_7^k with c below",
             "U_form": [[QU7[i][j] for j in range(v)] for i in range(v)]}

# ---------------- v = 8: Zhang-Cao Example 3.3 (scaled by 2: entries 2 q = sum of terms with coefficient 1, sqrt2 or 2)
K8 = Cyc(8)
S2 = [0, 1, 0, 0, 0, 0, 0, 1]                    # sqrt2 = zeta + zeta^7
ONE8 = K8.unit(0)


def term(coef, k):
    base = K8.unit(k)
    if coef == "s2":
        return K8.mul(S2, base)
    return [coef * x for x in base]


def vec8(spec):
    """spec: list of (component, coef, omega power); returns 2*q as 8 field elements."""
    q = [[0] * 8 for _ in range(8)]
    for comp, coef, k in spec:
        q[comp] = K8.add(q[comp], term(coef, k))
    return q


# rows transcribed from the printed array; (a|b) halves: 1/sqrt2 rows use coefficient "s2" (2/sqrt2 = sqrt2),
# 1/2 rows use coefficient 1, sqrt2 terms inside 1/2 rows use "s2"
R = []
R.append([vec8([(j, 2, 0)]) for j in range(8)])
R.append([vec8([(2, "s2", 0), (3, "s2", 3)]), vec8([(2, "s2", 0), (3, "s2", 7)]), vec8([(0, "s2", 0), (1, "s2", 6)]),
          vec8([(0, "s2", 0), (1, "s2", 2)]), vec8([(6, "s2", 0), (7, "s2", 4)]), vec8([(6, "s2", 0), (7, "s2", 0)]),
          vec8([(4, "s2", 0), (5, "s2", 6)]), vec8([(4, "s2", 0), (5, "s2", 2)])])
R.append([vec8([(4, 1, 0), (5, 1, 0), (6, 1, 7), (7, 1, 5)]), vec8([(4, 1, 0), (5, 1, 0), (6, 1, 3), (7, 1, 1)]),
          vec8([(4, 1, 0), (5, 1, 4), (6, 1, 3), (7, 1, 5)]), vec8([(4, 1, 0), (5, 1, 4), (6, 1, 7), (7, 1, 1)]),
          vec8([(0, 1, 0), (1, 1, 0), (2, 1, 2), (3, 1, 7)]), vec8([(0, 1, 0), (1, 1, 0), (2, 1, 6), (3, 1, 3)]),
          vec8([(0, 1, 0), (1, 1, 4), (2, 1, 6), (3, 1, 7)]), vec8([(0, 1, 0), (1, 1, 4), (2, 1, 2), (3, 1, 3)])])
R.append([vec8([(4, 1, 0), (5, 1, 4), (6, 1, 1), (7, 1, 3)]), vec8([(4, 1, 0), (5, 1, 4), (6, 1, 5), (7, 1, 7)]),
          vec8([(4, 1, 0), (5, 1, 0), (6, 1, 5), (7, 1, 3)]), vec8([(4, 1, 0), (5, 1, 0), (6, 1, 1), (7, 1, 7)]),
          vec8([(0, 1, 0), (1, 1, 4), (2, 1, 4), (3, 1, 5)]), vec8([(0, 1, 0), (1, 1, 4), (2, 1, 0), (3, 1, 1)]),
          vec8([(0, 1, 0), (1, 1, 0), (2, 1, 0), (3, 1, 5)]), vec8([(0, 1, 0), (1, 1, 0), (2, 1, 4), (3, 1, 1)])])
R.append([vec8([(1, "s2", 0), (2, 1, 7), (3, 1, 6)]), vec8([(0, "s2", 0), (2, 1, 5), (3, 1, 0)]),
          vec8([(0, 1, 0), (1, 1, 2), (3, "s2", 4)]), vec8([(0, 1, 0), (1, 1, 6), (2, "s2", 1)]),
          vec8([(5, "s2", 0), (6, 1, 4), (7, 1, 4)]), vec8([(4, "s2", 0), (6, 1, 2), (7, 1, 6)]),
          vec8([(4, 1, 0), (5, 1, 2), (7, "s2", 2)]), vec8([(4, 1, 0), (5, 1, 6), (6, "s2", 6)])])
R.append([vec8([(1, "s2", 0), (2, 1, 3), (3, 1, 2)]), vec8([(0, "s2", 0), (2, 1, 1), (3, 1, 4)]),
          vec8([(0, 1, 0), (1, 1, 2), (3, "s2", 0)]), vec8([(0, 1, 0), (1, 1, 6), (2, "s2", 5)]),
          vec8([(5, "s2", 0), (6, 1, 0), (7, 1, 0)]), vec8([(4, "s2", 0), (6, 1, 6), (7, 1, 2)]),
          vec8([(4, 1, 0), (5, 1, 2), (7, "s2", 6)]), vec8([(4, 1, 0), (5, 1, 6), (6, "s2", 2)])])
R.append([vec8([(4, 1, 0), (5, 1, 6), (7, "s2", 0)]), vec8([(4, 1, 0), (5, 1, 2), (6, "s2", 0)]),
          vec8([(5, "s2", 0), (6, 1, 2), (7, 1, 6)]), vec8([(4, "s2", 0), (6, 1, 4), (7, 1, 4)]),
          vec8([(0, 1, 0), (1, 1, 6), (3, "s2", 2)]), vec8([(0, 1, 0), (1, 1, 2), (2, "s2", 3)]),
          vec8([(1, "s2", 0), (2, 1, 5), (3, 1, 0)]), vec8([(0, "s2", 0), (2, 1, 7), (3, 1, 6)])])
R.append([vec8([(4, 1, 0), (5, 1, 2), (6, "s2", 4)]), vec8([(4, 1, 0), (5, 1, 6), (7, "s2", 4)]),
          vec8([(4, "s2", 0), (6, 1, 0), (7, 1, 0)]), vec8([(5, "s2", 0), (6, 1, 6), (7, 1, 2)]),
          vec8([(0, 1, 0), (1, 1, 2), (2, "s2", 7)]), vec8([(0, 1, 0), (1, 1, 6), (3, "s2", 6)]),
          vec8([(0, "s2", 0), (2, 1, 3), (3, 1, 2)]), vec8([(1, "s2", 0), (2, 1, 1), (3, 1, 4)])])
B8 = [[i ^ j for j in range(8)] for i in range(8)]
r8 = check(K8, R, B8, 4)
mut8 = [row[:] for row in R]
mut8[3] = list(R[3])
mut8[3][3] = R[3][2]
r8m = check(K8, mut8, B8, 4)
u0_identity8 = all(K8.zero([x - y for x, y in zip(R[0][j][s], K8.unit(0, 2 if s == j else 0))]) for j in range(8) for s in range(8))
out["v8"] = {"bad_gram_entries": r8[0], "rays": r8[1], "B_latin": r8[2], "lines": r8[3],
             "U0_is_identity": u0_identity8, "mutation_bad_gram_entries": r8m[0], "B": B8,
             "U_form_entries_note": "q_ij = U_i e_j; entry s of U_i e_j = (1/2) * sum_k c_k zeta_8^k with c below",
             "U_form": R}
out["gates"] = {"v7_anchor_exact_maximal": r7[0] == 0 and r7[1] == 49 and r7[2] and r7u[0] == 0 and r7u[1] == 49 and u0_identity,
                "v8_anchor_exact_maximal": r8[0] == 0 and r8[1] == 64 and r8[2] and u0_identity8,
                "mutations_break": r7m[0] > 0 and r8m[0] > 0,
                "affine_control_non_maximal": r7a[0] == 0 and r7a[1] < 49}
out["elapsed_s"] = round(time.monotonic() - T0, 3)
with open(OUT, "x", encoding="utf-8") as fh:
    json.dump(out, fh)
print(json.dumps({"v7": {k: out["v7"][k] for k in ("complete_mappings_of_Z7", "non_affine", "mu", "bad_gram_entries", "rays",
                                                    "B_latin", "U_form_bad_gram_entries", "U_form_rays", "U0_is_identity",
                                                    "mutation_bad_gram_entries", "affine_mu_2x_rays", "affine_mu_2x_bad")},
                  "v8": {k: out["v8"][k] for k in ("bad_gram_entries", "rays", "B_latin", "mutation_bad_gram_entries")},
                  "gates": out["gates"], "elapsed_s": out["elapsed_s"]}))
