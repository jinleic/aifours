"""Implementation 2 (independent of impl 1): Möbius charts, difference sets, closed-form Latin squares,
and exact root-of-unity checks of the Corollary-7 pair (stdlib only).

(L') Class c is linear for free set F  <=>  in the affine chart where c is the point at infinity (Möbius map
     phi(t) = 1/(t - c), phi(c) = inf), the image phi(F) is a subset of F_7 all of whose pairwise differences are
     distinct (a 3-subset of F_7 that is not an arithmetic progression). Also cross-checked against the harmonic
     conjugate prediction: c is NON-linear iff c is the harmonic conjugate of one point of F w.r.t. the other two.
(C') Closed form: AG(2,7) Latin squares are isotopic to L(x,y) = y - m x (m != 0); symbol pairs -> components
     computed by union-find on the formula (no geometry objects).
(K)  Control showing the linearity mechanism does not over-claim: the Corollary 7 pair of order 7 (Example 15,
     H = {1,2,4}) is checked EXACTLY: a sum of 7 seventh roots of unity zeta^{d_x} is 0 iff (d_x) is a permutation
     of Z_7, and has modulus 7 iff d_x is constant. QLS, orthogonality to the classical square, ray count (> 7).
     Mutations: an affine f must give ray count 7; a determined direction must break orthogonality.

python -B impl2_chart.py --out ../evidence/impl2.json [--impl1 ../evidence/impl1.json]
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
import time

P = 7
INF = "inf"


def inv(a):
    return pow(a % P, P - 2, P)


def mobius_to_inf(c, t):
    """phi_c(t) with phi_c(c) = inf; c = inf -> identity."""
    if c == INF:
        return t
    if t == INF:
        return 0
    if t == c:
        return INF
    return inv(t - c)


def distinct_differences(S):
    d = [(a - b) % P for a in S for b in S if a != b]
    return len(d) == len(set(d))


def harmonic_conj(x, a, b):
    """h with cross-ratio (a, b; x, h) = -1 over F_7 (points may be inf)."""
    # move a -> inf with phi_a, solve in chart: harmonic conj of x wrt inf, b' is 2 b' - x'
    xa, ba = mobius_to_inf(a, x), mobius_to_inf(a, b)
    ha = (2 * ba - xa) % P
    # invert phi_a: t = a + 1/ha (ha != 0); ha == 0 -> t = inf
    if a == INF:
        return ha
    return INF if ha == 0 else (a + inv(ha)) % P


def linear_chart(F, c):
    img = [mobius_to_inf(c, f) for f in F]
    assert INF not in img
    return distinct_differences(img)


def components_closed_form(m, a, b):
    """cells (x,y) of L(x,y)=y-mx with symbol in {a,b}; union-find over row/column pairing."""
    cells = [(x, y) for x in range(P) for y in range(P) if (y - m * x) % P in (a, b)]
    parent = {c: c for c in cells}

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    byrow, bycol = {}, {}
    for c in cells:
        byrow.setdefault(c[0], []).append(c)
        bycol.setdefault(c[1], []).append(c)
    for grp in list(byrow.values()) + list(bycol.values()):
        assert len(grp) == 2
        parent[find(grp[0])] = find(grp[1])
    return len({find(c) for c in cells})


# ------------------------------------------------------------------ exact Corollary-7 control
def is_perm(seq):
    return sorted(s % P for s in seq) == list(range(P))


def cor7_pair(fmap):
    """returns (M, m0, exponents of Psi^(f0), classical slope m')."""
    M = [m for m in range(P) if is_perm([(fmap[x] - m * x) for x in range(P)])]
    return M


def check_fourier_square(f0, mprime):
    e = {(i, j): [(i * f0[x] + j * x) % P for x in range(P)] for i in range(P) for j in range(P)}

    def ortho(c1, c2):
        return is_perm([e[c2][x] - e[c1][x] for x in range(P)])

    def same_ray(c1, c2):
        d = [(e[c2][x] - e[c1][x]) % P for x in range(P)]
        return len(set(d)) == 1
    qls = all(ortho((i, j), (i, k)) for i in range(P) for j, k in itertools.combinations(range(P), 2)) and \
        all(ortho((i, j), (k, j)) for j in range(P) for i, k in itertools.combinations(range(P), 2))
    orth = None
    if mprime is not None:
        orth = True
        for c1, c2 in itertools.combinations(e, 2):
            if (mprime * c1[0] + c1[1]) % P == (mprime * c2[0] + c2[1]) % P:   # same classical symbol |m'i+j>
                if not ortho(c1, c2):
                    orth = False
                    break
    reps = []
    for c in e:
        if not any(same_ray(c, r) for r in reps):
            reps.append(c)
    return {"qls": qls, "orthogonal_to_classical": orth, "rays": len(reps)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--impl1", default=None)
    a = ap.parse_args()
    t0 = time.time()
    cls = list(range(P)) + [INF]
    out = {"implementation": "2 (Möbius charts / closed forms / exact root-of-unity sums)", "python": sys.version.split()[0],
           "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()}
    lin3, harm_ok = [], True
    for F in itertools.combinations(cls, 3):
        L = sorted(str(c) for c in cls if c not in F and linear_chart(F, c))
        H = set()
        for x in F:
            o = [y for y in F if y != x]
            H.add(harmonic_conj(x, o[0], o[1]))
        nonlin_pred = sorted(str(h) for h in H)
        nonlin = sorted(str(c) for c in cls if c not in F and str(c) not in L)
        harm_ok &= (nonlin_pred == nonlin)
        lin3.append({"F": [str(x) for x in F], "linear_classes": L})
    out["linear_by_F_size3"] = lin3
    out["count_linear_per_F_size3"] = sorted({len(r["linear_classes"]) for r in lin3})
    out["harmonic_prediction_matches"] = harm_ok
    # sizes 4,5: a k-subset of F_7 with k >= 4 cannot have distinct differences (k(k-1) > 6)
    out["any_linear_size4"] = any(linear_chart(F, c) for F in itertools.combinations(cls, 4) for c in cls if c not in F)
    out["any_linear_size5"] = any(linear_chart(F, c) for F in itertools.combinations(cls, 5) for c in cls if c not in F)
    out["closed_form_components"] = sorted({components_closed_form(m, x, y) for m in range(1, P)
                                            for x, y in itertools.combinations(range(P), 2)})
    if a.impl1:
        i1 = json.load(open(a.impl1))
        m1 = {tuple(r["F"]): r["linear_classes"] for r in i1["linear_by_F_size3"]}
        m2 = {tuple(r["F"]): r["linear_classes"] for r in lin3}
        out["agrees_with_impl1"] = m1 == m2
    # exact Corollary-7 control (Example 15, q = 7, H = {1,2,4})
    Hs = {1, 2, 4}
    fmap = [x if x in Hs else 0 for x in range(P)]
    M = cor7_pair(fmap)
    out["cor7_undetermined_directions"] = M
    m0 = M[0]
    f0 = [(fmap[x] - m0 * x) % P for x in range(P)]
    mprime = (M[1] - m0) % P
    out["cor7_f0"] = f0
    out["cor7_classical_slope"] = mprime
    out["cor7_check"] = check_fourier_square(f0, mprime)
    out["mutation_affine_f"] = check_fourier_square([(2 * x + 3) % P for x in range(P)], None)
    det = next(m for m in range(1, P) if m not in [(x - m0) % P for x in M])
    out["mutation_determined_direction"] = {"slope": det, **check_fourier_square(f0, det)}
    out["classical_6MOLS_rays"] = [len({tuple(((mm * i + j) % P,)) for i in range(P) for j in range(P)}) for mm in range(1, P)]
    pairs_ok = all(len({((m1 * i + j) % P, (m2 * i + j) % P) for i in range(P) for j in range(P)}) == P * P
                   for m1, m2 in itertools.combinations(range(1, P), 2))
    out["classical_6MOLS_mutually_orthogonal"] = pairs_ok
    out["secs"] = round(time.time() - t0, 2)
    json.dump(out, open(a.out, "w"), indent=1)
    print(json.dumps({k: out.get(k) for k in ("count_linear_per_F_size3", "harmonic_prediction_matches", "any_linear_size4",
                                              "any_linear_size5", "closed_form_components", "agrees_with_impl1",
                                              "cor7_undetermined_directions", "cor7_check", "mutation_affine_f",
                                              "mutation_determined_direction", "classical_6MOLS_rays",
                                              "classical_6MOLS_mutually_orthogonal", "secs")}))


if __name__ == "__main__":
    main()
