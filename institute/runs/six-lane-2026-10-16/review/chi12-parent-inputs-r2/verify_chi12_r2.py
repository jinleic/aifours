#!/usr/bin/env python3
"""verify_chi12_r2.py: exact checks for the additions made in review/PROOF_CHI12.r2.md (lane random12reg-colour).

New file for r2; code/verify_chi12.py and its outputs are unchanged. Exact integers, rationals and sympy only; no
floating-point value is used as evidence. Sections:
  M1  KPW Lemma 8's two epsilon-conditions at (k, d) = (5, 12) (Claude review m1, m2): c, the spectrum of
      B = (k-1)^2 I + (J-I)^{(x)2} (exact ranks), c*lambda_min, the damping coefficients, the d-free bounds on eps^2.
  L67 KPW Lemma 6 (a), (b) and Lemma 7 (a), (b), (c) at k = 5, exactly (generic zero-row/column-sum A).
  M4  E X_i = [n]_i (d(d-1))^i / (2i prod_{j<i} (dn-1-2j)) against exhaustive enumeration of all pairings for small
      (n, d) (Claude review m4), and its limit (d-1)^i/(2i).
  M3  KPW's marked space on small instances (Claude review m3): bounds on N_L(P); |Omega| = A_L (dm-2l-1)!!;
      P(B) <= E[#extra pairs] <= C(2l(d-1), 2)/(dm-2l-1); on A = Simple and not-B the map (P, L) -> (G', L) is
      exactly (d!)^m-to-one onto an independently enumerated Omega'_m.
M3 and M4 check finite identities and inequalities only; the asymptotic statements are hand arguments.
"""
import itertools
import json
import os
from collections import Counter
from fractions import Fraction as Fr
from math import comb, factorial, prod

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))


def section_M1():
    d, k = sp.symbols("d k", positive=True)
    q = k**2 - 2 * k + 2
    c = d / (2 * k**2 * (k - 1)**2)                      # KPW l.1393
    lam_min = (k - 1) * (k - 2)                          # KPW Lemma 6(a), smallest eigenvalue of B
    clam = sp.simplify(c * lam_min)
    gauss_identity = sp.simplify(d**2 / (4 * c * k**2 * q) - d * (k - 1)**2 / (2 * q)) == 0   # (3.22) exponent
    D2 = d * (k - 1)**2 * k**2 / (2 * q)    # damping coefficient from Lemma 7(b): ||A||^2 < k^2 eps^2 log^2 n / n
    D1 = d * k**2 * (k - 1)**4 / (2 * q)    # r1 form: lambda_max((J+I)^{(x)2}) = k^2, ||Atilde||^2 < (k-1)^2 eps^2 ...
    thr1 = d / (16 * k**2 * (k - 1)**2)     # KPW l.1356
    ratio1 = sp.factor(sp.simplify(thr1 / D1))
    ratio2 = sp.factor(sp.simplify(clam / D2))
    ratio2_crude = sp.factor(sp.simplify(clam / D1))
    at = {d: 12, k: 5}
    v = {name: sp.Rational(expr.subs(at)) for name, expr in
         [("c", c), ("lam_min", lam_min), ("c_lam_min", clam), ("D2", D2), ("D1", D1), ("thr1", thr1),
          ("eps2_bound_first", ratio1), ("eps2_bound_second", ratio2), ("eps2_bound_second_crude", ratio2_crude)]}
    # Exact spectrum of B at k = 5 via ranks (B is real symmetric, so nullities are multiplicities).
    kk = 5
    B = sp.Matrix(kk * kk, kk * kk, lambda a, b: (16 if a == b else 0)
                  + (1 if (a // kk != b // kk and a % kk != b % kk) else 0))
    nullity = {lam: kk * kk - (B - lam * sp.eye(kk * kk)).rank() for lam in (17, 12, 32)}
    checks = {
        "c(5,12) = 3/200": v["c"] == sp.Rational(3, 200),
        "lambda_min = (k-1)(k-2) = 12": v["lam_min"] == 12,
        "c*lambda_min = d(k-2)/(2k^2(k-1)) symbolic": sp.simplify(clam - d * (k - 2) / (2 * k**2 * (k - 1))) == 0,
        "c*lambda_min(5,12) = 9/50": v["c_lam_min"] == sp.Rational(9, 50),
        "(3.22) exponent coefficient d^2/(4ck^2(k^2-2k+2)) = d(k-1)^2/(2(k^2-2k+2))": gauss_identity,
        "damping coefficient via Lemma 7(b) = 2400/17": v["D2"] == sp.Rational(2400, 17),
        "damping coefficient, r1 eigenvalue form = 38400/17": v["D1"] == sp.Rational(38400, 17),
        "l.1356 threshold d/(16k^2(k-1)^2) = 3/1600": v["thr1"] == sp.Rational(3, 1600),
        "first condition eps^2 < (k^2-2k+2)/(8k^4(k-1)^6) symbolic":
            sp.simplify(ratio1 - q / (8 * k**4 * (k - 1)**6)) == 0,
        "first condition eps^2 < 17/20480000": v["eps2_bound_first"] == sp.Rational(17, 20480000),
        "second condition eps^2 < (k-2)(k^2-2k+2)/(k^4(k-1)^3) symbolic":
            sp.simplify(ratio2 - (k - 2) * q / (k**4 * (k - 1)**3)) == 0,
        "second condition eps^2 < 51/40000": v["eps2_bound_second"] == sp.Rational(51, 40000),
        "second condition with the crude 38400/17: eps^2 < 51/640000":
            v["eps2_bound_second_crude"] == sp.Rational(51, 640000),
        "d cancels in both bounds": sp.diff(ratio1, d) == 0 and sp.diff(ratio2, d) == 0,
        "17/20480000 < 51/40000 (first implies second)": bool(sp.Rational(17, 20480000) < sp.Rational(51, 40000)),
        "17/20480000 < 51/640000 (also with the crude coefficient)":
            bool(sp.Rational(17, 20480000) < sp.Rational(51, 640000)),
        "spectrum of B at k=5: 17 x16, 12 x8, 32 x1 (exact ranks)": nullity == {17: 16, 12: 8, 32: 1},
    }
    return {"values": {a: str(b) for a, b in v.items()}, "nullities": {str(a): b for a, b in nullity.items()},
            "n-power of I from (pi/(cn))^{k^2/2}": "-k^2/2 = -25/2", "checks": checks,
            "M1 ok": all(checks.values())}


def lemma6_basis(k):
    def e(i):
        return sp.Matrix([1 if t == i else 0 for t in range(k)])
    fs = []
    for p in range(1, k):
        vec = sum((e(l) for l in range(p)), sp.zeros(k, 1)) / p - e(p)   # p^{-1} sum_{l<=p} 1^(l) - 1^(p+1)
        fs.append(sp.sqrt(sp.Rational(p, p + 1)) * vec)
    fs.append(sp.ones(k, 1) / sp.sqrt(k))
    return fs


def kron_vec(u, w):
    k = u.shape[0]
    return sp.Matrix([u[i] * w[j] for i in range(k) for j in range(k)])


def section_L67():
    k = 5
    fs = lemma6_basis(k)
    gram_ok = all(sp.simplify((fs[i].T * fs[j])[0] - (1 if i == j else 0)) == 0 for i in range(k) for j in range(k))
    N = k * k
    Bm = sp.Matrix(N, N, lambda a, b: ((k - 1)**2 if a == b else 0)
                   + (1 if (a // k != b // k and a % k != b % k) else 0))
    JI2 = sp.Matrix(N, N, lambda a, b: (2 if a // k == b // k else 1) * (2 if a % k == b % k else 1))
    eig6a, eig6b = True, True
    for p in range(k):
        for qq in range(k):
            f = kron_vec(fs[p], fs[qq])
            last = (p == k - 1) + (qq == k - 1)
            lam = {0: k * k - 2 * k + 2, 1: (k - 1) * (k - 2), 2: 2 * (k - 1)**2}[last]
            mu = {0: 1, 1: k + 1, 2: (k + 1)**2}[last]
            eig6a &= all(sp.simplify(x) == 0 for x in (Bm * f - lam * f))
            eig6b &= all(sp.simplify(x) == 0 for x in (JI2 * f - mu * f))
    a = [[sp.Symbol(f"a{i}{j}") for j in range(k - 1)] for i in range(k - 1)]
    A = [[None] * k for _ in range(k)]
    for i in range(k - 1):
        for j in range(k - 1):
            A[i][j] = a[i][j]
        A[i][k - 1] = -sum(a[i][j] for j in range(k - 1))
    for j in range(k - 1):
        A[k - 1][j] = -sum(a[i][j] for i in range(k - 1))
    A[k - 1][k - 1] = sum(a[i][j] for i in range(k - 1) for j in range(k - 1))
    rows_cols_zero = all(sp.expand(sum(A[i][j] for j in range(k))) == 0 for i in range(k)) and \
        all(sp.expand(sum(A[i][j] for i in range(k))) == 0 for j in range(k))
    vecA = sp.Matrix([A[i][j] for i in range(k) for j in range(k)])
    sumsq = sp.expand(sum(A[i][j]**2 for i in range(k) for j in range(k)))
    proj = {(p, qq): sp.expand((vecA.T * kron_vec(fs[p], fs[qq]))[0]) for p in range(k) for qq in range(k)}
    l7a = all(proj[(i, k - 1)] == 0 and proj[(k - 1, i)] == 0 for i in range(k))
    l7b = sp.expand(sum(proj[(p, qq)]**2 for p in range(k - 1) for qq in range(k - 1)) - sumsq) == 0
    vecAt = sp.Matrix([a[i][j] for i in range(k - 1) for j in range(k - 1)])
    M = sp.Matrix((k - 1)**2, (k - 1)**2,
                  lambda x, y: (2 if x // (k - 1) == y // (k - 1) else 1) * (2 if x % (k - 1) == y % (k - 1) else 1))
    l7c = sp.expand((vecAt.T * M * vecAt)[0] - sumsq) == 0
    checks = {"Lemma 6 basis orthonormal (k=5)": gram_ok,
              "Lemma 6(a) eigen-relations of (J-I)^{(x)2} + 16 I (k=5)": eig6a,
              "Lemma 6(b) eigen-relations of (J+I)^{(x)2} (k=5)": eig6b,
              "generic A has zero row and column sums": rows_cols_zero,
              "Lemma 7(a) at k=5": l7a, "Lemma 7(b) at k=5": l7b, "Lemma 7(c) at k=5": l7c}
    return {"checks": checks, "L67 ok": all(checks.values())}


def all_pairings(points):
    if not points:
        yield ()
        return
    a, rest = points[0], points[1:]
    for idx, b in enumerate(rest):
        for p in all_pairings(rest[:idx] + rest[idx + 1:]):
            yield ((a, b),) + p


def is_cycle(vpairs, i):
    deg = Counter()
    for u, w in vpairs:
        deg[u] += 1
        deg[w] += 1
    if len(deg) != i or any(x != 2 for x in deg.values()):
        return False
    parent = {u: u for u in deg}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for u, w in vpairs:
        parent[find(u)] = find(w)
    return len({find(u) for u in deg}) == 1


def falling(n, i):
    return prod(n - j for j in range(i))


def ex_formula(n, d, i):
    return Fr(falling(n, i) * (d * (d - 1))**i, 2 * i * prod(d * n - 1 - 2 * j for j in range(i)))


def section_M4():
    imax = 4
    res, ok = {}, True
    for n, d in [(2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (2, 3), (4, 3), (2, 4), (3, 4), (2, 5), (2, 6)]:
        tot, npair = Counter(), 0
        combos = {i: list(itertools.combinations(range(d * n // 2), i)) for i in range(1, imax + 1)}
        for P in all_pairings(tuple(range(d * n))):
            npair += 1
            vp = [(x // d, y // d) for x, y in P]
            for i in range(1, imax + 1):
                tot[i] += sum(1 for cmb in combos[i] if is_cycle([vp[t] for t in cmb], i))
        row = {}
        for i in range(1, imax + 1):
            exact, formula = Fr(tot[i], npair), ex_formula(n, d, i)
            row[str(i)] = {"enumerated": str(exact), "formula": str(formula), "equal": exact == formula}
            ok &= exact == formula
        res[f"n={n},d={d} ({npair} pairings)"] = row
    nn, dd = sp.symbols("n d", positive=True)
    lim_ok = all(sp.simplify(sp.limit(sp.ff(nn, i) * (dd * (dd - 1))**i
                                      / (2 * i * sp.Mul(*[dd * nn - 1 - 2 * j for j in range(i)])), nn, sp.oo)
                             - (dd - 1)**i / (2 * i)) == 0 for i in range(1, imax + 1))
    lam12 = [str(Fr(11**i, 2 * i)) for i in range(1, imax + 1)]
    return {"instances": res, "limit (d-1)^i/(2i) for i=1..4 (symbolic in d)": lim_ok,
            "lambda_i at d=12, i=1..4": lam12, "M4 ok": bool(ok and lim_ok)}


def dfact(x):
    return prod(range(x, 0, -2)) if x > 0 else 1


def section_M3():
    res, ok = {}, True
    for m, d, ell in [(4, 3, 1), (4, 3, 2), (5, 2, 1), (5, 2, 2), (6, 2, 1), (6, 2, 2), (6, 2, 3), (3, 4, 1)]:
        npts, half = d * m, d * m // 2
        NL, omega, nB, extra_tot = [], 0, 0, 0
        pre = Counter()
        for P in all_pairings(tuple(range(npts))):
            vp = [(x // d, y // d) for x, y in P]
            vs = [frozenset(t) for t in vp]
            simple = all(u != w for u, w in vp) and len({frozenset(t) for t in vp}) == len(vp)
            cnt = 0
            for L in itertools.permutations(range(half), ell):
                if any(vs[s] & vs[t] for s, t in itertools.combinations(L, 2)):
                    continue
                cnt += 1
                W = set().union(*(vs[t] for t in L))
                extra = sum(1 for t in range(half) if t not in L and vp[t][0] in W and vp[t][1] in W)
                extra_tot += extra
                if extra:
                    nB += 1
                elif simple:
                    edges = frozenset(tuple(sorted(t)) for t in vp)
                    pre[(edges, tuple(tuple(sorted(vp[t])) for t in L))] += 1
            NL.append(cnt)
            omega += cnt
        pts_pairs = list(itertools.combinations(range(npts), 2))
        A_L = sum(1 for L in itertools.permutations(pts_pairs, ell)
                  if all(not ({x // d for x in L[s]} & {x // d for x in L[t]})
                         for s, t in itertools.combinations(range(ell), 2)))
        lower_seq = prod(half - 2 * (j - 1) * d for j in range(1, ell + 1))
        lower_crude = max(0, half - 2 * ell * d)**ell
        bound = Fr(comb(2 * ell * (d - 1), 2), npts - 2 * ell - 1) if npts - 2 * ell - 1 > 0 else None
        # independent enumeration of Omega'_m
        kedges = list(itertools.combinations(range(m), 2))
        omega_prime = set()
        if half <= len(kedges):
            for E in itertools.combinations(kedges, half):
                degc = Counter(v for e in E for v in e)
                if any(degc[v] != d for v in range(m)):
                    continue
                Es = frozenset(E)
                for L in itertools.permutations(E, ell):
                    W = set(v for e in L for v in e)
                    if len(W) != 2 * ell:
                        continue
                    if {e for e in E if e[0] in W and e[1] in W} == set(L):
                        omega_prime.add((Es, tuple(L)))
        c_nl = (min(NL) >= max(0, lower_seq) and min(NL) >= lower_crude and max(NL) <= falling(half, ell)
                and falling(half, ell) <= half**ell)
        c_omega = omega == A_L * dfact(npts - 2 * ell - 1)
        pB, eX = Fr(nB, omega), Fr(extra_tot, omega)
        c_B = bound is None or (pB <= eX <= bound)
        c_map = set(pre) == omega_prime and all(x == factorial(d)**m for x in pre.values())
        row = {"N_L range": [min(NL), max(NL)], "sequential lower bound": lower_seq, "crude lower bound": lower_crude,
               "upper bound [dm/2]_l": falling(half, ell), "|Omega|": omega, "A_L": A_L,
               "(dm-2l-1)!!": dfact(npts - 2 * ell - 1), "P(B)": str(pB), "E[#extra pairs in W]": str(eX),
               "bound C(2l(d-1),2)/(dm-2l-1)": str(bound), "|Omega'_m|": len(omega_prime),
               "preimage counts": sorted(set(pre.values())), "(d!)^m": factorial(d)**m,
               "N_L bounds ok": c_nl, "|Omega| = A_L (dm-2l-1)!!": c_omega, "P(B) <= E <= bound": c_B,
               "exactly (d!)^m-to-one onto Omega'_m": c_map}
        ok &= c_nl and c_omega and c_B and c_map
        res[f"m={m},d={d},l={ell}"] = row
    return {"instances": res, "M3 ok": bool(ok)}


def main():
    out = {"note": "verifier for the r2 additions of review/PROOF_CHI12.r2.md (lane random12reg-colour); exact only"}
    out["M1"] = section_M1()
    out["L67"] = section_L67()
    out["M4"] = section_M4()
    out["M3"] = section_M3()
    out["all_required_true"] = bool(out["M1"]["M1 ok"] and out["L67"]["L67 ok"] and out["M4"]["M4 ok"]
                                    and out["M3"]["M3 ok"])
    path = os.path.join(HERE, "..", "evidence", "verify_chi12_r2.json")
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
