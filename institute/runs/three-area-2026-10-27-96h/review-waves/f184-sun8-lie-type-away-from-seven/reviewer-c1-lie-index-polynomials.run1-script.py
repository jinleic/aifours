#!/usr/bin/env python3
"""Reviewer control C1 for wave f184-sun8-lie-type-away-from-seven.

Independently authored by the reviewer (ReviewF184SunLieAway7). Does not import,
open or execute any author code. Exact integer arithmetic only.

Routes used (all independent of the candidate's Levi-order route):
  * Maximal-parabolic index polynomials of untwisted types are computed as the
    Poincare polynomial of the W-orbit of the fundamental weight(s) omega_O,
    graded by Coxeter length (BFS over positive-coordinate reflections).
  * Twisted simply-laced types (2A, 2D, 3D4, 2E6): index polynomial
    = sum over sigma-fixed minimal coset representatives of x^length
    (sigma-fixed W-orbit points of omega_O, O a sigma-orbit).
  * Suzuki-Ree (2B2, 2G2, 2F4): enumerate W, sigma-fixed elements and their
    minimal-coset property; weight t^length with t^2 = q.
These are compared with the candidate's displayed Pi_G / Pi_L formulas
(transcribed by the reviewer from the candidate text), and the cyclotomic
divisibility / coprimality / Lemma 3 / q=3 table claims are checked.
Negative controls must FAIL for their intended reason.
"""
import json, sys, time, math
from fractions import Fraction

T0 = time.time()
OUT = {"control": "reviewer-c1-lie-index-polynomials", "checks": {}, "negative": {}, "notes": []}
FAIL = []

def check(name, ok, detail=None):
    OUT["checks"][name] = {"ok": bool(ok), "detail": detail}
    if not ok:
        FAIL.append(name)

# ---------------- integer polynomials (little-endian lists) ----------------
def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p

def padd(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])

def pmul(a, b):
    if not a or not b:
        return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return trim(r)

def pdivmod(a, b):
    """Division by a polynomial with leading coefficient +-1 (stays in Z[x])."""
    a = trim(a); b = trim(b)
    assert b and b[-1] in (1, -1)
    r = a[:]
    q = [0] * max(len(a) - len(b) + 1, 1)
    while r and len(r) >= len(b):
        c = r[-1] * b[-1]
        k = len(r) - len(b)
        q[k] = c
        for i, bi in enumerate(b):
            r[k + i] -= c * bi
        r = trim(r)
    return trim(q), r

def pexact(a, b):
    q, r = pdivmod(a, b)
    assert not r, "inexact division"
    return q

def peval(p, x):
    v = 0
    for c in reversed(p):
        v = v * x + c
    return v

def xm(n, c):
    """x^n - c"""
    p = [0] * (n + 1)
    p[n] = 1
    p[0] -= c
    return trim(p)

def prod(ps):
    r = [1]
    for p in ps:
        r = pmul(r, p)
    return r

CYC = {}
def cyclo(n):
    if n not in CYC:
        p = xm(n, 1)
        for d in range(1, n):
            if n % d == 0:
                p = pexact(p, cyclo(d))
        CYC[n] = p
    return CYC[n]

def divides(phi, p):
    return not pdivmod(p, phi)[1]

def totient(n):
    return sum(1 for k in range(1, n + 1) if math.gcd(k, n) == 1)

# ---------------- Cartan matrices (row i = alpha_i in fundamental weights) ----------------
def cartan(typ, n):
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        A[i][i] = 2
    def link(i, j, aij=-1, aji=-1):
        A[i][j] = aij; A[j][i] = aji
    if typ == 'A':
        for i in range(n - 1): link(i, i + 1)
    elif typ == 'B':
        for i in range(n - 2): link(i, i + 1)
        link(n - 2, n - 1, -2, -1)
    elif typ == 'C':
        for i in range(n - 2): link(i, i + 1)
        link(n - 2, n - 1, -1, -2)
    elif typ == 'D':
        for i in range(n - 2): link(i, i + 1)
        link(n - 3, n - 1)
    elif typ == 'E':  # Bourbaki: 1-3-4-5-6-7-8, 2-4 (0-indexed below)
        link(0, 2); link(2, 3); link(1, 3)
        for i in range(3, n - 1): link(i, i + 1)
    elif typ == 'F':
        link(0, 1); link(1, 2, -2, -1); link(2, 3)
    elif typ == 'G':
        link(0, 1, -1, -3)
    else:
        raise ValueError(typ)
    return A

def orbit_levels(A, O, sigma=None):
    """BFS over W.omega_O; returns (all-count per length, sigma-fixed count per length)."""
    n = len(A)
    start = tuple(1 if j in O else 0 for j in range(n))
    seen = {start}
    frontier = [start]
    allc, fixc = [], []
    while frontier:
        allc.append(len(frontier))
        if sigma is not None:
            fixc.append(sum(1 for mu in frontier if all(mu[sigma[j]] == mu[j] for j in range(n))))
        nxt = []
        for lam in frontier:
            for i in range(n):
                c = lam[i]
                if c > 0:
                    Ai = A[i]
                    mu = tuple(lam[j] - c * Ai[j] for j in range(n))
                    if mu not in seen:
                        seen.add(mu)
                        nxt.append(mu)
        frontier = nxt
    return trim(allc), (trim(fixc) if sigma is not None else None)

def sub_cartan(A, nodes):
    return [[A[i][j] for j in nodes] for i in nodes]

def weyl_poincare(A):
    """Poincare polynomial of W via a chain of maximal parabolic orbits."""
    n = len(A)
    if n == 0:
        return [1]
    # remove the last node; orbit of omega_last
    allc, _ = orbit_levels(A, {n - 1})
    rest = list(range(n - 1))
    return pmul(allc, weyl_poincare(sub_cartan(A, rest)))

def positive_roots(A):
    """Positive roots in simple-root coordinates (generated by simple reflections)."""
    n = len(A)
    simple = [tuple(1 if j == i else 0 for j in range(n)) for i in range(n)]
    roots = set(simple)
    frontier = list(simple)
    while frontier:
        nxt = []
        for r in frontier:
            # <r, alpha_i^vee> = sum_k r_k A[k][i]
            for i in range(n):
                pairing = sum(r[k] * A[k][i] for k in range(n))
                s = list(r)
                s[i] -= pairing
                s = tuple(s)
                if all(x >= 0 for x in s) and any(s) and s not in roots:
                    roots.add(s); nxt.append(s)
        frontier = nxt
    return roots

def qbracket(d):
    return [1] * d  # (x^d - 1)/(x - 1)

DEGREES = {
    ('A', None): lambda n: list(range(2, n + 2)),
    ('B', None): lambda n: list(range(2, 2 * n + 1, 2)),
    ('C', None): lambda n: list(range(2, 2 * n + 1, 2)),
    ('D', None): lambda n: list(range(2, 2 * n - 1, 2)) + [n],
    ('E', 6): lambda n: [2, 5, 6, 8, 9, 12],
    ('E', 7): lambda n: [2, 6, 8, 10, 12, 14, 18],
    ('E', 8): lambda n: [2, 8, 12, 14, 18, 20, 24, 30],
    ('F', 4): lambda n: [2, 6, 8, 12],
    ('G', 2): lambda n: [2, 6],
}

def degrees(typ, n):
    if (typ, n) in DEGREES:
        return DEGREES[(typ, n)](n)
    return DEGREES[(typ, None)](n)

# Candidate Table 1, untwisted e(S): transcribed from the candidate text
def table_e_untwisted(typ, n):
    return {'A': n + 1, 'B': 2 * n, 'C': 2 * n, 'D': 2 * n - 2}.get(typ) or {('G', 2): 6, ('F', 4): 12, ('E', 6): 12, ('E', 7): 18, ('E', 8): 30}[(typ, n)]

# ================= Part 1: untwisted types =================
untw_cases = [('A', n) for n in range(1, 15)] + [('B', n) for n in range(2, 10)] + [('C', n) for n in range(2, 10)] \
    + [('D', n) for n in range(4, 10)] + [('G', 2), ('F', 4), ('E', 6), ('E', 7), ('E', 8)]
untw = {}
UNTW_INDEX = {}
for typ, n in untw_cases:
    A = cartan(typ, n)
    name = f"{typ}{n}"
    Wx = weyl_poincare(A)
    deg = degrees(typ, n)
    chev = prod(qbracket(d) for d in deg)
    roots = positive_roots(A)
    N = len(roots)
    hroot = max(sum(r) for r in roots)
    h = max(deg)
    e = table_e_untwisted(typ, n)
    Phi = cyclo(e)
    rec = {"|Phi+|": N, "W(1)": peval(Wx, 1), "chevalley_degrees_match": Wx == chev,
           "h=maxdeg": h, "ht(theta)+1": hroot + 1, "table_e": e, "e==h": e == h}
    ok = (Wx == chev) and (h == hroot + 1) and (e == h) and (2 * N == sum(d - 1 for d in deg) * 2)
    idx_list = []
    divs_all = True; coprime_all = True; levi_ok = True; chain_ok = True
    for k in range(n):
        Ik, _ = orbit_levels(A, {k})
        WJ = pexact(Wx, Ik)
        # independent cross-check: W_J computed directly from the sub-diagram by its own orbit chain
        WJ_direct = weyl_poincare(sub_cartan(A, [j for j in range(n) if j != k]))
        chain_ok &= (WJ_direct == WJ)
        # Levi p'-order route: Pi_L = (x-1)^n W_J, Pi_G = (x-1)^n W
        PiG = pmul(prod([xm(1, 1)] * n), Wx)
        PiL = pmul(prod([xm(1, 1)] * n), WJ)
        levi_ok &= (pexact(PiG, PiL) == Ik)
        d1 = divides(Phi, Ik)
        c1 = not divides(Phi, WJ)  # Phi irreducible over Q
        divs_all &= d1; coprime_all &= c1
        idx_list.append(Ik)
    rec["W_J_direct_chain_matches_W/I_J"] = chain_ok
    ok = ok and chain_ok
    rec.update({"Phi_e_divides_every_maximal_index": divs_all, "Phi_e_coprime_to_every_W_J": coprime_all,
                "num_maximal_parabolics": n})
    ok = ok and divs_all and coprime_all and levi_ok
    # common cyclotomic divisors (for negative control): e' <= 2h+2
    common = [ep for ep in range(2, 2 * h + 3) if all(divides(cyclo(ep), I) for I in idx_list)]
    rec["all_e_with_Phi_e_dividing_all_maximal_indices(e<=2h+2)"] = common
    rec["wrong_e_h-1_rejected"] = (h - 1 < 2) or ((h - 1) not in common)
    rec["wrong_e_h+1_rejected"] = (h + 1) not in common
    untw[name] = rec
    UNTW_INDEX[name] = idx_list
    check(f"untwisted:{name}", ok, rec)
OUT["untwisted"] = untw

# ================= Part 2: twisted simply-laced types =================
def candidate_PSU(m):
    """Candidate formulas: Pi_G and Levi p'-orders for PSU_m(q)."""
    PiG = prod(xm(c, (-1) ** c) for c in range(2, m + 1))
    res = {}
    for k in range(1, m // 2 + 1):
        if 2 * k < m:
            PiL = pmul(prod(xm(2 * c, 1) for c in range(1, k + 1)), prod(xm(c, (-1) ** c) for c in range(2, m - 2 * k + 1)))
        else:
            PiL = pmul(xm(1, 1), prod(xm(2 * c, 1) for c in range(2, k + 1)))
        res[k] = (PiG, PiL)
    return res

def candidate_Ominus(n):
    PiG = pmul(xm(n, -1), prod(xm(2 * c, 1) for c in range(1, n)))
    res = {}
    for k in range(1, n):
        if k <= n - 2:
            PiL = prod([xm(1, 1), prod(xm(c, 1) for c in range(2, k + 1)), xm(n - k, -1), prod(xm(2 * c, 1) for c in range(1, n - k))])
        else:
            PiL = pmul(xm(2, 1), prod(xm(c, 1) for c in range(2, n)))
        res[k] = (PiG, PiL)
    return res

twisted = {}
TW_INDEX = {}
# 2A_{m-1} = PSU_m
for m in range(3, 13):
    n = m - 1
    A = cartan('A', n)
    sigma = [n - 1 - j for j in range(n)]
    e = 2 * m if m % 2 == 1 else 2 * (m - 1)
    Phi = cyclo(e)
    cand = candidate_PSU(m)
    per = {}
    ok = True
    idxs = []
    for k in range(1, m // 2 + 1):
        O = {k - 1, m - k - 1}
        allc, fixc = orbit_levels(A, O, sigma)
        PiG, PiL = cand[k]
        qq, rr = pdivmod(PiG, PiL)
        match = (not rr) and (qq == fixc)
        dv = divides(Phi, fixc)
        cp = not divides(Phi, PiL)
        per[k] = {"index_poly_matches_candidate_PiG/PiL": match, "Phi_e_divides": dv, "Phi_e_coprime_to_Levi": cp,
                  "value_q2": peval(fixc, 2), "value_q3": peval(fixc, 3)}
        ok &= match and dv and cp
        idxs.append(fixc)
    common = [ep for ep in range(2, 2 * e + 1) if all(divides(cyclo(ep), I) for I in idxs)]
    twisted[f"PSU{m}"] = {"e": e, "per_k": per, "common_e": common, "untwisted_e_m_rejected": m not in common}
    TW_INDEX[f"PSU{m}"] = idxs
    check(f"twisted:PSU{m}", ok, twisted[f"PSU{m}"])

# 2D_n = POmega^-_{2n}
for n in range(4, 10):
    A = cartan('D', n)
    sigma = list(range(n)); sigma[n - 2], sigma[n - 1] = n - 1, n - 2
    e = 2 * n
    Phi = cyclo(e)
    cand = candidate_Ominus(n)
    per = {}; ok = True; idxs = []
    for k in range(1, n):
        O = {k - 1} if k <= n - 2 else {n - 2, n - 1}
        allc, fixc = orbit_levels(A, O, sigma)
        PiG, PiL = cand[k]
        qq, rr = pdivmod(PiG, PiL)
        match = (not rr) and (qq == fixc)
        dv = divides(Phi, fixc); cp = not divides(Phi, PiL)
        per[k] = {"index_poly_matches_candidate_PiG/PiL": match, "Phi_e_divides": dv, "Phi_e_coprime_to_Levi": cp,
                  "value_q2": peval(fixc, 2), "value_q3": peval(fixc, 3)}
        ok &= match and dv and cp
        idxs.append(fixc)
    common = [ep for ep in range(2, 2 * e + 1) if all(divides(cyclo(ep), I) for I in idxs)]
    twisted[f"2D{n}"] = {"e": e, "per_k": per, "common_e": common}
    TW_INDEX[f"2D{n}"] = idxs
    check(f"twisted:2D{n}", ok, twisted[f"2D{n}"])

# 3D4: nodes (Bourbaki) 1,2,3,4 -> 0,1,2,3; sigma: 1->3->4->1, 2 fixed
A = cartan('D', 4)
sigma = [2, 1, 3, 0]
PiG = prod([xm(2, 1), [1, 0, 0, 0, 1, 0, 0, 0, 1], xm(6, 1)])
cand3 = {"J={a2} (remove orbit {a1,a3,a4})": (PiG, pmul(xm(2, 1), xm(3, 1)), {0, 2, 3}),
         "J={a1,a3,a4} (remove orbit {a2})": (PiG, pmul(xm(6, 1), xm(1, 1)), {1})}
per = {}; ok = True; idxs = []
for lab, (PG, PL, O) in cand3.items():
    allc, fixc = orbit_levels(A, O, sigma)
    qq, rr = pdivmod(PG, PL)
    match = (not rr) and (qq == fixc)
    dv = divides(cyclo(12), fixc); cp = not divides(cyclo(12), PL)
    per[lab] = {"match": match, "Phi12_divides": dv, "Phi12_coprime_Levi": cp, "index_poly": fixc}
    ok &= match and dv and cp; idxs.append(fixc)
# candidate's displayed index products
disp = [pmul(xm(3, -1), [1, 0, 0, 0, 1, 0, 0, 0, 1]), pmul(xm(1, -1), [1, 0, 0, 0, 1, 0, 0, 0, 1])]
ok &= sorted(map(tuple, disp)) == sorted(map(tuple, idxs))
twisted["3D4"] = {"per": per, "displayed_index_products_match": sorted(map(tuple, disp)) == sorted(map(tuple, idxs))}
TW_INDEX["3D4"] = idxs
check("twisted:3D4", ok, twisted["3D4"])

# 2E6: Bourbaki 1..6 -> 0..5 ; sigma 1<->6, 3<->5, 2,4 fixed
A = cartan('E', 6)
sigma = [5, 1, 4, 3, 2, 0]
PiG = prod([xm(2, 1), xm(5, -1), xm(6, 1), xm(8, 1), xm(9, -1), xm(12, 1)])
levis = {
    "2A5 (remove {2})": (prod([xm(1, 1), xm(2, 1), xm(3, -1), xm(4, 1), xm(5, -1), xm(6, 1)]), {1}),
    "A2(q^2)A1(q) (remove {4})": (prod([xm(1, 1), xm(2, 1), xm(4, 1), xm(6, 1)]), {3}),
    "A1(q^2)A2(q) (remove {3,5})": (prod([xm(1, 1), xm(1, -1), xm(4, 1), xm(2, 1), xm(3, 1)]), {2, 4}),
    "2D4 (remove {1,6})": (prod([xm(1, 1), xm(1, -1), xm(2, 1), xm(4, 1), xm(4, -1), xm(6, 1)]), {0, 5}),
}
per = {}; ok = True; idxs = []
for lab, (PL, O) in levis.items():
    allc, fixc = orbit_levels(A, O, sigma)
    qq, rr = pdivmod(PiG, PL)
    match = (not rr) and (qq == fixc)
    dv = divides(cyclo(18), fixc); cp = not divides(cyclo(18), PL)
    per[lab] = {"match": match, "Phi18_divides": dv, "Phi18_coprime_Levi": cp, "value_q2": peval(fixc, 2)}
    ok &= match and dv and cp; idxs.append(fixc)
twisted["2E6"] = per
TW_INDEX["2E6"] = idxs
check("twisted:2E6", ok, per)

# ================= Part 3: Suzuki-Ree via W enumeration =================
def weyl_elements(A):
    n = len(A)
    S = []
    for i in range(n):
        # matrix acting on weight coordinates (row vectors lam -> lam M): lam_j - lam_i A[i][j]
        M = [[(1 if r == c else 0) for c in range(n)] for r in range(n)]
        for j in range(n):
            M[i][j] -= A[i][j]
        S.append(tuple(tuple(r) for r in M))
    def mul(X, Y):
        return tuple(tuple(sum(X[r][k] * Y[k][c] for k in range(n)) for c in range(n)) for r in range(n))
    I = tuple(tuple(1 if r == c else 0 for c in range(n)) for r in range(n))
    length = {I: 0}; word = {I: ()}
    frontier = [I]
    while frontier:
        nxt = []
        for X in frontier:
            for i in range(n):
                Y = mul(X, S[i])
                if Y not in length:
                    length[Y] = length[X] + 1; word[Y] = word[X] + (i,); nxt.append(Y)
        frontier = nxt
    return S, mul, I, length, word

def suzuki_ree(A, sigma, Js):
    S, mul, I, length, word = weyl_elements(A)
    fixed = []
    for X, wd in word.items():
        Y = I
        for i in wd:
            Y = mul(Y, S[sigma[i]])
        if Y == X:
            fixed.append(X)
    res = {"|W|": len(length), "|W^sigma|": len(fixed)}
    polys = {}
    for lab, J in Js.items():
        tl = {}
        for X in fixed:
            if all(length[mul(X, S[j])] > length[X] for j in J):
                tl[length[X]] = tl.get(length[X], 0) + 1
        assert all(l % 2 == 0 for l in tl), "odd t-exponent"
        qp = [0] * (max(tl) // 2 + 1)
        for l, c in tl.items():
            qp[l // 2] += c
        polys[lab] = trim(qp)
    res["index_polys_in_q"] = polys
    return res

sr = {}
r = suzuki_ree(cartan('B', 2), [1, 0], {"B (J=empty)": set()})
okB = r["index_polys_in_q"]["B (J=empty)"] == [1, 0, 1]
sr["2B2"] = r; check("suzuki:2B2 index q^2+1", okB, r)
r = suzuki_ree(cartan('G', 2), [1, 0], {"B (J=empty)": set()})
okG = r["index_polys_in_q"]["B (J=empty)"] == [1, 0, 0, 1]
sr["2G2"] = r; check("ree:2G2 index q^3+1", okG, r)
r = suzuki_ree(cartan('F', 4), [3, 2, 1, 0], {"J={a2,a3} Levi 2B2(q)x(q-1)": {1, 2}, "J={a1,a4} Levi SL2(q)x(q-1)": {0, 3}, "B (J=empty)": set()})
PiG = prod([xm(6, -1), xm(4, 1), xm(3, -1), xm(1, 1)])
L_a = prod([xm(2, -1), xm(1, 1), xm(1, 1)])
L_b = pmul(xm(2, 1), xm(1, 1))
pa = r["index_polys_in_q"]["J={a2,a3} Levi 2B2(q)x(q-1)"]
pb = r["index_polys_in_q"]["J={a1,a4} Levi SL2(q)x(q-1)"]
pB = r["index_polys_in_q"]["B (J=empty)"]
okF = (pexact(PiG, L_a) == pa) and (pexact(PiG, L_b) == pb) and divides(cyclo(12), pa) and divides(cyclo(12), pb) \
    and (not divides(cyclo(12), L_a)) and (not divides(cyclo(12), L_b)) and pexact(PiG, prod([xm(1, 1), xm(1, 1)])) == pB \
    and pexact(xm(6, -1), cyclo(12)) == [1, 0, 1]
r["candidate_match"] = okF
sr["2F4"] = r; check("ree:2F4 two maximal parabolics", okF, {"pa": pa, "pb": pb, "pB": pB})
OUT["suzuki_ree"] = sr
OUT["twisted"] = twisted

# ================= Part 4: Lemma 3 =================
def prime_powers(limit):
    pp = []
    for q in range(2, limit):
        m = q; p = None
        for d in range(2, int(q ** 0.5) + 2):
            if m % d == 0:
                p = d; break
        if p is None:
            p = q
        while m % p == 0:
            m //= p
        if m == 1:
            pp.append(q)
    return pp

PP = prime_powers(2000)
# all e occurring in Table 1 for wide parameter ranges
E_TABLE = set()
rows_e = {}
def addrow(lbl, e):
    E_TABLE.add(e); rows_e.setdefault(e, []).append(lbl)
for n in range(1, 200): addrow(f"A{n}", n + 1)
for n in range(2, 200): addrow(f"B{n}", 2 * n); addrow(f"C{n}", 2 * n)
for n in range(4, 200): addrow(f"D{n}", 2 * n - 2)
for lbl, e in [("G2", 6), ("F4", 12), ("E6", 12), ("E7", 18), ("E8", 30), ("3D4", 12), ("2E6", 18), ("2F4", 12)]: addrow(lbl, e)
for m in range(3, 200):
    addrow(f"PSU{m}", 2 * m if m % 2 else 2 * (m - 1))
for n in range(4, 200): addrow(f"2D{n}", 2 * n)
hits = []
for e in sorted(E_TABLE):
    if e > 400: continue
    ph = cyclo(e)
    for q in PP:
        if (q - 1) ** totient(e) > 7:
            break
        v = peval(ph, q)
        if v in (1, 7):
            hits.append((e, q, v))
# Suzuki-Ree values
srvals_ok = all(q * q + 1 not in (1, 7) for q in [2 ** (2 * m + 1) for m in range(1, 12)]) and \
    all(q ** 3 + 1 not in (1, 7) for q in [3 ** (2 * m + 1) for m in range(1, 8)]) and \
    all(peval(cyclo(12), q) not in (1, 7) for q in [2 ** (2 * m + 1) for m in range(1, 12)])
check("lemma3:only (3,2),(6,3) give 7; none gives 1", sorted(hits) == [(3, 2, 7), (6, 3, 7)] and srvals_ok, {"hits": hits})
check("lemma3:e=3 rows", rows_e.get(3) == ["A2"], rows_e.get(3))
check("lemma3:e=6 rows", sorted(rows_e.get(6)) == sorted(["A5", "B3", "C3", "D4", "G2", "PSU3", "PSU4"]), rows_e.get(6))
# general scan over all e<=300 and prime powers q<2000 (not only Table e's)
hits_all = []
for e in range(2, 301):
    ph = cyclo(e)
    for q in PP:
        if (q - 1) ** totient(e) > 7:
            break
        v = peval(ph, q)
        if v in (1, 7):
            hits_all.append((e, q, v))
check("lemma3:scan all e<=300", sorted(hits_all) == [(3, 2, 7), (6, 3, 7)], hits_all)
# unpruned scan (does not rely on the (q-1)^phi(e) bound): every e<=60, every prime power q<2000
hits_np = []
for e in range(2, 61):
    ph = cyclo(e)
    for q in PP:
        if peval(ph, q) in (1, 7):
            hits_np.append((e, q))
check("lemma3:unpruned scan e<=60, q<2000", sorted(hits_np) == [(3, 2), (6, 3)], hits_np)
vals2 = {e: peval(cyclo(e), 2) for e in [2, 3, 4, 5, 6, 8, 10, 12]}
check("lemma3:q=2 values", vals2 == {2: 3, 3: 7, 4: 5, 5: 31, 6: 3, 8: 17, 10: 11, 12: 13}, vals2)
vals3 = {e: peval(cyclo(e), 3) for e in [2, 3, 4, 6]}
check("lemma3:q=3 values", vals3 == {2: 4, 3: 13, 4: 10, 6: 7}, vals3)
phi_le4 = [e for e in range(1, 1000) if totient(e) <= 4]
check("lemma3:phi(e)<=4 list", phi_le4 == [1, 2, 3, 4, 5, 6, 8, 10, 12], phi_le4)
check("lemma3:product constant 147/512>0.28", Fraction(21, 64) * Fraction(7, 8) == Fraction(147, 512) and Fraction(147, 512) > Fraction(28, 100))
bound_ok = all(25 * peval(cyclo(e), 2) > 7 * 2 ** totient(e) for e in range(2, 401))
check("lemma3:Phi_e(2)>0.28*2^phi(e) for 2<=e<=400", bound_ok)
# lower bound (q-1)^phi(e) for q>=3 spot check
lb_ok = all(peval(cyclo(e), q) >= (q - 1) ** totient(e) for e in range(2, 61) for q in [3, 4, 5, 7, 8, 9, 11, 13])
check("lemma3:(q-1)^phi(e) lower bound spot", lb_ok)
check("lemma3:Phi_e(q)=1 mod q", all(peval(cyclo(e), q) % q == 1 for e in range(2, 61) for q in [2, 3, 4, 5, 7, 8, 9]))

# ================= Part 5: Theorem B q=3 table =================
def gcdset(vals):
    s = set()
    for i in range(len(vals)):
        for j in range(i, len(vals)):
            s.add(math.gcd(vals[i], vals[j]))
    return sorted(s)

mine = {
    "PSL6(3)": [peval(p, 3) for p in UNTW_INDEX["A5"]],
    "Omega7(3)": [peval(p, 3) for p in UNTW_INDEX["B3"]],
    "PSp6(3)": [peval(p, 3) for p in UNTW_INDEX["C3"]],
    "POmega8+(3)": [peval(p, 3) for p in UNTW_INDEX["D4"]],
    "G2(3)": [peval(p, 3) for p in UNTW_INDEX["G2"]],
    "PSU3(3)": [peval(p, 3) for p in TW_INDEX["PSU3"]],
    "PSU4(3)": [peval(p, 3) for p in TW_INDEX["PSU4"]],
}
cand_tbl = {  # transcribed from candidate Section 6 table
    "PSL6(3)": ([364, 11011, 33880, 11011, 364], [28, 91, 364, 847, 11011, 33880]),
    "Omega7(3)": ([364, 3640, 1120], [28, 280, 364, 1120, 3640]),
    "PSp6(3)": ([364, 3640, 1120], [28, 280, 364, 1120, 3640]),
    "POmega8+(3)": ([1120, 36400, 1120, 1120], [560, 1120, 36400]),
    "G2(3)": ([364, 364], [364]),
    "PSU3(3)": ([28], [28]),
    "PSU4(3)": ([280, 112], [56, 112, 280]),
}
tb = {}
okt = True
for g, vals in mine.items():
    cvals, cg = cand_tbl[g]
    gs = gcdset(vals)
    same_multiset = sorted(vals) == sorted(cvals)
    same_g = gs == sorted(cg)
    none7 = all(7 % x != 0 for x in gs)
    tb[g] = {"reviewer_indices": vals, "multiset_match": same_multiset, "reviewer_gcds": gs, "gcd_match": same_g, "no_g_divides_7": none7}
    okt &= same_multiset and same_g and none7
check("thmB:q=3 table", okt, tb)
# D(S)=7 for these seven groups (consistency)
okd = all(peval(cyclo(e), 3) == 7 for e in [6]) and all(v % 7 == 0 for vals in mine.values() for v in vals)
check("thmB:all q=3 maximal parabolic indices divisible by 7", okd)

# ================= Negative controls (must fail for intended reason) =================
# NEG1: PSL3(2) = A2(2): maximal parabolic indices, pairwise gcds -> 7 occurs (Lemma 3 exception)
a2 = [peval(p, 2) for p in UNTW_INDEX["A2"]]
g2 = gcdset(a2)
OUT["negative"]["NEG1_PSL3(2)_gcd7"] = {"indices": a2, "gcds": g2, "detected_gcd_dividing_7": any(7 % x == 0 for x in g2)}
check("NEG1 detected (expected)", any(7 % x == 0 for x in g2) and a2 == [7, 7])
# NEG2: wrong D assignments rejected (for every tested type, e=h+1 not a common divisor; for PSU_m the untwisted e=m rejected)
neg2 = all(rec["wrong_e_h+1_rejected"] for rec in untw.values()) and all(twisted[f"PSU{m}"]["untwisted_e_m_rejected"] for m in range(3, 13))
OUT["negative"]["NEG2_wrong_cyclotomic_rejected"] = neg2
check("NEG2 wrong cyclotomic assignments rejected (expected)", neg2)
# NEG3: mutated O^- Levi (x^{n-k}-1 in place of x^{n-k}+1) must break the index match
mut_fail = []
for n in range(4, 8):
    A = cartan('D', n); sigma = list(range(n)); sigma[n - 2], sigma[n - 1] = n - 1, n - 2
    k = 1
    _, fixc = orbit_levels(A, {0}, sigma)
    PiG = pmul(xm(n, -1), prod(xm(2 * c, 1) for c in range(1, n)))
    PiLmut = prod([xm(1, 1), xm(n - k, 1), prod(xm(2 * c, 1) for c in range(1, n - k))])
    qq, rr = pdivmod(PiG, PiLmut)
    mut_fail.append(bool(rr) or qq != fixc)
OUT["negative"]["NEG3_mutated_Ominus_Levi_mismatch"] = mut_fail
check("NEG3 mutated Levi rejected (expected)", all(mut_fail))
# NEG4: plus-type (untwisted D_n) orbit index for k=1 does not equal the minus-type candidate index
neg4 = []
for n in range(4, 8):
    plus = UNTW_INDEX[f"D{n}"][0]
    minus = TW_INDEX[f"2D{n}"][0]
    neg4.append(plus != minus)
check("NEG4 plus-type != minus-type (expected)", all(neg4))

OUT["fail"] = FAIL
OUT["all_ok"] = not FAIL
OUT["elapsed_s"] = round(time.time() - T0, 3)
json.dump(OUT, sys.stdout, indent=1, sort_keys=True, default=str)
sys.stdout.write("\n")
sys.exit(0 if not FAIL else 1)
