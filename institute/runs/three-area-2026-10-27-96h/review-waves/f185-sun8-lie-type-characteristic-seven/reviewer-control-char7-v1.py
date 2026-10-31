#!/usr/bin/env python3
"""Reviewer-authored exact controls for review wave f185 (characteristic-7 Lie-type candidate).

Independent of the author checker: nothing is imported from or executed of author code.
Pure integer arithmetic.  Cyclotomic values come from exact integer polynomial division
(not the Moebius product), factorizations are complete trial division (so every reported
prime is proven prime), multiplicative orders are computed from the factorization of n.

Sections (P = positive control, N = intended-reason negative control):
  A  Phi_n(7) factorizations, primality, p-primitive primes                (P + N tamper)
  B  BBGT Table C rows used, evaluated literally at q=7 and q=49           (P + N)
  C  alpha/beta conditions for every row, all f<=240 (cyclic-group model)  (P + N)
  D  Maslova items: residue exclusions for q=7^f and 7-adic index
     valuations of every non-parabolic odd-index family (exact orders)     (P + N)
  E  Lemma P facts: D(S) mod 7, D(S)>=2, and flag-count divisibility        (P + N)
  F  Statement 3 (PSL2(49)) and Lemma U order facts                        (P + N)
  G  literal source-row presence in the reviewer's pinned BBGT extraction  (P)
A JSON receipt is written with exclusive create.
"""
import hashlib
import json
import os
import sys
import time
from functools import lru_cache

T0 = time.time()
WAVE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(WAVE, "reviewer-control-char7-v1.json")
BBGT_TXT = os.path.join(WAVE, "reviewer-bbgt-extracted-text-v1.txt")
BBGT_TXT_SHA = "8cea608d969578b8f18c089ceefa99991037cd7e68e9438c3986f86d71f88f88"
DEADLINE = 110.0

RESULTS = {"positive": [], "negative": []}


def record(kind, name, ok, detail):
    RESULTS[kind].append({"name": name, "ok": bool(ok), "detail": detail})


def check_time():
    if time.time() - T0 > DEADLINE:
        raise SystemExit("INTERNAL DEADLINE EXCEEDED -> UNKNOWN")


# ----------------------------------------------------------------------------- basics
def v_p(p, x):
    """Exact p-adic valuation, O(log v) big-integer operations (binary extraction)."""
    x = abs(x)
    if x == 0:
        raise ValueError("valuation of 0")
    if x % p:
        return 0
    pw = [p]                      # pw[i] = p^(2^i)
    while x % pw[-1] == 0:
        pw.append(pw[-1] * pw[-1])
    k = 0
    for i in range(len(pw) - 2, -1, -1):
        if x % pw[i] == 0:
            x //= pw[i]
            k += 1 << i
    if x % p == 0:
        raise AssertionError("valuation extraction incomplete")
    return k


def factor_trial(n):
    """Complete factorization by trial division; every returned factor is prime."""
    out = []
    m = n
    d = 2
    while d * d <= m:
        while m % d == 0:
            out.append(d)
            m //= d
        d = 3 if d == 2 else d + 2
    if m > 1:
        out.append(m)
    return out


def is_prime_trial(n):
    return n >= 2 and factor_trial(n) == [n]


def prime_divisors(n):
    return sorted(set(factor_trial(n)))


def mult_order(a, r):
    """Order of a modulo prime r, from the factorization of r-1."""
    o = r - 1
    for pr in prime_divisors(r - 1):
        while o % pr == 0 and pow(a, o // pr, r) == 1:
            o //= pr
    return o


def has_order_exactly(a, r, n):
    if pow(a, n, r) != 1:
        return False
    return all(pow(a, n // pr, r) != 1 for pr in prime_divisors(n))


def legendre(a, p):
    t = pow(a % p, (p - 1) // 2, p)
    return 0 if t == 0 else (1 if t == 1 else -1)


# ------------------------------------------------------------- cyclotomic polynomials
def pdiv_exact(a, b):
    a = list(a)
    db = len(b) - 1
    if b[-1] != 1:
        raise ValueError("divisor not monic")
    qt = [0] * (len(a) - db)
    for i in range(len(a) - 1, db - 1, -1):
        c = a[i]
        if c:
            qt[i - db] = c
            for j in range(db + 1):
                a[i - db + j] -= c * b[j]
    if any(a):
        raise ValueError("non-exact polynomial division")
    return qt


@lru_cache(maxsize=None)
def cyclo(n):
    num = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            num = pdiv_exact(num, list(cyclo(d)))
    return tuple(num)


def peval(poly, x):
    s = 0
    for c in reversed(poly):
        s = s * x + c
    return s


def Phi(n, x):
    return peval(cyclo(n), x)


# ============================================================================ A
def section_A():
    claimed = {6: [43], 12: [13, 181], 8: [2, 1201], 16: [2, 17, 169553],
               9: [3, 37, 1063], 18: [117307], 36: [13841169553], 30: [6568801],
               60: [61, 555915824341]}
    data = {}
    all_ok = True
    for n, cl in claimed.items():
        check_time()
        val = Phi(n, 7)
        # independent identity check: prod_{d|n} Phi_d(7) == 7^n - 1
        prod_all = 1
        for d in range(1, n + 1):
            if n % d == 0:
                prod_all *= Phi(d, 7)
        ident = prod_all == 7 ** n - 1
        fs = factor_trial(val)
        prod = 1
        for x in fs:
            prod *= x
        orders = {str(r): mult_order(7, r) for r in sorted(set(fs)) if r != 7}
        prim = sorted(r for r in set(fs) if has_order_exactly(7, r, n))
        ok = ident and prod == val and fs == sorted(cl) and all(is_prime_trial(x) for x in fs)
        all_ok = all_ok and ok
        data[n] = {"Phi_n(7)": val, "factors": fs, "claimed": cl, "product_ok": prod == val,
                   "identity_prod_Phi_d_eq_7^n-1": ident, "orders_of_7": orders,
                   "p_primitive": prim, "match": ok}
    record("positive", "A1 nine Phi_n(7) factorizations reproduced, all factors proven prime", all_ok,
           {str(k): v for k, v in data.items()})
    # A2: which factors are p-primitive (ord_r(7)=n)
    expect_prim = {6: [43], 12: [13, 181], 8: [1201], 16: [17, 169553], 9: [37, 1063],
                   18: [117307], 36: [13841169553], 30: [6568801], 60: [61, 555915824341]}
    ok2 = all(data[n]["p_primitive"] == expect_prim[n] for n in expect_prim)
    record("positive", "A2 p-primitive prime factors (ord_r(7)=n) as used by candidate", ok2,
           {str(n): data[n]["p_primitive"] for n in expect_prim})
    # N-A: tamper controls -- false claims must be rejected by the same machinery
    t1 = is_prime_trial(2353)            # Phi_12(7) is NOT prime
    t2 = Phi(18, 7) == 117307 + 2        # wrong value must not match
    t3 = has_order_exactly(7, 3, 9)      # 3 | Phi_9(7) but ord_3(7)=1, not primitive
    t4 = has_order_exactly(7, 2, 8)      # 2 | Phi_8(7) is not primitive
    t5 = factor_trial(Phi(30, 7) + 2) == [Phi(30, 7) + 2]  # a perturbed value is checked honestly
    record("negative", "A3 tamper: 2353 composite, wrong Phi_18 rejected, 3 and 2 not primitive",
           (not t1) and (not t2) and (not t3) and (not t4),
           {"2353_prime": t1, "Phi18_eq_117309": t2, "ord3_is_9": t3, "ord2_is_8": t4,
            "perturbed_Phi30_plus2_prime?": t5, "factor(2353)": factor_trial(2353)})
    return data


# ============================================================================ B
def exc_order_factors(typ, q):
    """(list of integer factors whose product times 1/div is |S|, div)."""
    if typ == "G2":
        return [q ** 6, q ** 6 - 1, q ** 2 - 1], 1
    if typ == "3D4":
        return [q ** 12, q ** 8 + q ** 4 + 1, q ** 6 - 1, q ** 2 - 1], 1
    if typ == "F4":
        return [q ** 24, q ** 12 - 1, q ** 8 - 1, q ** 6 - 1, q ** 2 - 1], 1
    if typ == "E6":
        return [q ** 36, q ** 12 - 1, q ** 9 - 1, q ** 8 - 1, q ** 6 - 1, q ** 5 - 1, q ** 2 - 1], \
            __import__("math").gcd(3, q - 1)
    if typ == "2E6":
        return [q ** 36, q ** 12 - 1, q ** 9 + 1, q ** 8 - 1, q ** 6 - 1, q ** 5 + 1, q ** 2 - 1], \
            __import__("math").gcd(3, q + 1)
    if typ == "E7":
        return [q ** 63, q ** 18 - 1, q ** 14 - 1, q ** 12 - 1, q ** 10 - 1, q ** 8 - 1, q ** 6 - 1,
                q ** 2 - 1], __import__("math").gcd(2, q - 1)
    if typ == "E8":
        return [q ** 120, q ** 30 - 1, q ** 24 - 1, q ** 20 - 1, q ** 18 - 1, q ** 14 - 1,
                q ** 12 - 1, q ** 8 - 1, q ** 2 - 1], 1
    raise KeyError(typ)


def sylow_order(typ, q, r):
    fs, div = exc_order_factors(typ, q)
    return r ** (sum(v_p(r, x) for x in fs) - v_p(r, div) if div % r == 0 else sum(v_p(r, x) for x in fs))


def alpha_actual(p, f, r, m, eps, excluded):
    """BBGT alpha/beta: (q^{1/k})^m != eps (mod r) for all primes k|f, k not in excluded, k != r."""
    bad = []
    for k in prime_divisors(f) if f > 1 else []:
        if k in excluded or k == r:
            continue
        x = pow(p, f // k, r)
        if pow(x, m, r) == eps % r:
            bad.append(k)
    return (not bad), bad


# Literal encodings of the Table C rows used (G = T, so G/T trivial).
def row_G2_r6(p, f, q, r, R):
    a_ok, _ = alpha_actual(p, f, r, 3, -1, set())
    size = (p >= 5) and (f > 3 or R > r or r > 13
                         or (f == 3 and (r == 13 or p % 9 in (1, 8, 3, 6)))
                         or (f == 2 and legendre(p, 13) == 1)
                         or (f == 1 and r == 13 and legendre(p, 13) == -1))
    return a_ok and size, {"alpha(3,-1)": a_ok, "size_branch": size}


def row_3D4_r12(p, f, q, r, R):
    a_ok, _ = alpha_actual(p, f, r, 6, -1, {3})
    return a_ok, {"(q^(1/k))^6!=-1, k notin {3,r}": a_ok}


def row_F4_r8(p, f, q, r, R):
    a_ok, _ = alpha_actual(p, f, r, 4, -1, set())
    size = (p >= 3) and (f > 2 or r > 17 or R > r
                         or (f == 2 and (p == 3 or legendre(p, 17) == 1))
                         or (f == 1 and legendre(p, 17) == -1))
    return a_ok and size, {"alpha(4,-1)": a_ok, "size_branch": size}


def row_E6_r9(p, f, q, r, R):
    a_ok, _ = alpha_actual(p, f, r, 9, 1, set())
    size = (f > 2 or r > 19 or R > r
            or (f == 2 and legendre(p, 5) == 1)
            or (f == 1 and (legendre(p, 5) == -1 or legendre(p, 19) == -1)))
    return a_ok and size, {"alpha(9,1)": a_ok, "size_branch": size}


def row_2E6_r18(p, f, q, r, R):
    b_ok, _ = alpha_actual(p, f, r, 9, 1, {2})
    b_ok_other_sign, _ = alpha_actual(p, f, r, 9, -1, {2})
    size = (f > 1 or r > 19 or R > r
            or (f == 1 and (legendre(p, 5) == -1 or legendre(p, 19) == 1)))
    return b_ok and size, {"beta(9,1)": b_ok, "beta(9,-1)_textual_variant": b_ok_other_sign,
                           "size_branch": size}


def row_E7_r18(p, f, q, r, R):
    a_ok, _ = alpha_actual(p, f, r, 18, 1, set())
    size = (f > 2 or r > 37 or R > r
            or (f == 2 and legendre(p, 37) == 1)
            or (f == 1 and ((q, r) == (2, 19) or (r == 37 and legendre(p, 37) == -1))))
    return a_ok and size, {"alpha(18,1)": a_ok, "size_branch": size}


def row_E8_r30(p, f, q, r, R):
    a_ok, _ = alpha_actual(p, f, r, 30, 1, set())
    i = mult_order(q % r, r)
    dpr = mult_order(p, r)
    size = (r > 61 or R > r
            or (R == r == 61 and (f > 2 or (f == 2 and i == 15 and dpr in (15, 30)))))
    return a_ok and size, {"alpha(30,1)": a_ok, "size_branch": size, "i=d_q(r)": i, "d_p(r)": dpr}


ROWS = [("G2", 6, row_G2_r6), ("3D4", 12, row_3D4_r12), ("F4", 8, row_F4_r8),
        ("E6", 9, row_E6_r9), ("2E6", 18, row_2E6_r18), ("E7", 18, row_E7_r18),
        ("E8", 30, row_E8_r30)]
CANDIDATE_R = {("G2", 1): [43], ("G2", 2): [181], ("3D4", 1): [13, 181], ("3D4", 2): None,
               ("F4", 1): [1201], ("F4", 2): [169553], ("E6", 1): [37, 1063], ("E6", 2): [117307],
               ("2E6", 1): [117307], ("2E6", 2): None, ("E7", 1): [117307],
               ("E7", 2): [13841169553], ("E8", 1): [6568801], ("E8", 2): [555915824341]}


def section_B(adata):
    p = 7
    table = []
    pos_ok = True
    neg = []
    for typ, e, fn in ROWS:
        for f in (1, 2):
            check_time()
            n = e * f
            q = p ** f
            if n not in adata:
                table.append({"S": typ, "f": f, "e": e, "note": "Phi_%d(7) not factored; size condition "
                              "met through f or r>=ef+1 (see section C/report)" % n})
                continue
            for r in adata[n]["p_primitive"]:
                R = sylow_order(typ, q, r)
                d_q = mult_order(q % r, r)
                ok, detail = fn(p, f, q, r, R)
                rowrec = {"S": typ, "f": f, "q": q, "e": e, "r": r, "d_q(r)": d_q, "|R|": R,
                          "row_satisfied": ok, "detail": detail,
                          "candidate_choice": r in (CANDIDATE_R.get((typ, f)) or [])}
                table.append(rowrec)
                if d_q != e:
                    pos_ok = False
                if rowrec["candidate_choice"] and not ok:
                    pos_ok = False
                if not ok:
                    neg.append(rowrec)
    # every (typ,f) with a candidate choice must have a satisfied candidate r
    for (typ, f), rs in CANDIDATE_R.items():
        if rs is None:
            continue
        got = [t for t in table if t.get("S") == typ and t.get("f") == f and t.get("r") in rs]
        if not got or not all(t["row_satisfied"] for t in got):
            pos_ok = False
    record("positive", "B1 Table C rows satisfied at q=7,49 by the candidate's chosen r", pos_ok, table)
    expected_neg = {("G2", 2, 13), ("F4", 2, 17), ("E8", 2, 61)}
    got_neg = {(t["S"], t["f"], t["r"]) for t in neg}
    record("negative", "B2 other p-primitive r fail the row for the intended reason "
           "(|R|=r and residue / i-condition)", got_neg == expected_neg,
           {"failing": sorted(map(list, got_neg)), "expected": sorted(map(list, expected_neg)),
            "legendre(7,13)": legendre(7, 13), "legendre(7,17)": legendre(7, 17)})
    # B3: a 7-primitive prime at level e (not ef) is NOT an r_e for q=7^f, f>1 (E6, f=3: r=37)
    r = 37
    dq = mult_order(pow(7, 3, r), r)
    record("negative", "B3 choosing r primitive for 7^e-1 instead of 7^(ef)-1 gives the wrong d_q(r)",
           dq != 9, {"E6,f=3,r=37": {"d_q(r)": dq, "needed": 9}})


# ============================================================================ C
ROW_ALPHA = [("G2 alpha(3,-1)", 6, 3, -1, set()), ("3D4 (.)^6!=-1 k!=3", 12, 6, -1, {3}),
             ("F4 alpha(4,-1)", 8, 4, -1, set()), ("E6 alpha(9,1)", 9, 9, 1, set()),
             ("2E6 beta(9,1)", 18, 9, 1, {2}), ("2E6 beta(9,-1) [text variant]", 18, 9, -1, {2}),
             ("E7 alpha(18,1)", 18, 18, 1, set()), ("E8 alpha(30,1)", 30, 30, 1, set())]


def cyclic_model_violation(e, m, eps, excluded, f):
    """In <7> mod r (cyclic of order N=ef): q^(1/k) -> f/k, so (q^(1/k))^m -> m*f/k mod N.
    1 -> 0; -1 lies in <7> iff N even, and is N/2."""
    N = e * f
    viol = []
    for k in (prime_divisors(f) if f > 1 else []):
        if k in excluded:
            continue
        t = (m * (f // k)) % N
        is_one = t == 0
        is_minus = (N % 2 == 0) and t == N // 2
        if (eps == 1 and is_one) or (eps == -1 and is_minus):
            viol.append(k)
    return viol


def section_C():
    FMAX = 240
    viol_total = {}
    for name, e, m, eps, excl in ROW_ALPHA:
        v = []
        for f in range(1, FMAX + 1):
            w = cyclic_model_violation(e, m, eps, excl, f)
            if w:
                v.append((f, w))
        viol_total[name] = v
    ok = all(not v for v in viol_total.values())
    record("positive", "C1 every alpha/beta condition used holds for all f<=240 (cyclic model)", ok,
           {k: len(v) for k, v in viol_total.items()})
    # C2 negative: hypothetical sign flips with m=e must fail exactly for even f (k=2)
    hyp = [("E6 alpha(9,-1) [hypothetical]", 9, 9, -1), ("E7 alpha(18,-1) [hypothetical]", 18, 18, -1),
           ("E8 alpha(30,-1) [hypothetical]", 30, 30, -1)]
    det = {}
    ok2 = True
    for name, e, m, eps in hyp:
        fs = [f for f in range(1, 61) if cyclic_model_violation(e, m, eps, set(), f)]
        det[name] = fs[:12]
        ok2 = ok2 and fs == [f for f in range(1, 61) if f % 2 == 0]
    record("negative", "C2 hypothetical eps=-1 with m=e fails exactly at even f (k=2)", ok2, det)
    # C3: the candidate's literal intermediate 'ek | 2m fails in each row' is FALSE for k=2 in
    #     E6, E7, E8 (ek = 2m); the alpha conclusion still holds because eps=+1 there.
    lit = []
    for name, e, m, eps, excl in ROW_ALPHA:
        for k in (2, 3, 5, 7):
            if k in excl:
                continue
            if (2 * m) % (e * k) == 0:
                lit.append({"row": name, "k": k, "ek": e * k, "2m": 2 * m, "eps": eps})
    record("negative", "C3 literal 'ek|2m fails in each row' is false (expected instances found)",
           {d["row"] for d in lit} == {"E6 alpha(9,1)", "E7 alpha(18,1)", "E8 alpha(30,1)"}
           and all(d["k"] == 2 and d["eps"] == 1 for d in lit), lit)
    # C4: actual-number witness at f=2, k=2: 7^9 mod 117307 == -1 (so +-1 occurs) while alpha(9,1) holds
    w = pow(7, 9, 117307)
    record("positive", "C4 actual E6, q=49, r=117307: (q^(1/2))^9 = -1 mod r, so alpha(9,1) holds",
           w == 117306, {"7^9 mod 117307": w})


# ============================================================================ D
def gl(n, q):
    return [q ** (n * (n - 1) // 2)] + [q ** i - 1 for i in range(1, n + 1)]


def gu(n, q):
    return [q ** (n * (n - 1) // 2)] + [q ** i - (-1) ** i for i in range(1, n + 1)]


def sp(n, q):
    h = n // 2
    return [q ** (h * h)] + [q ** (2 * i) - 1 for i in range(1, h + 1)]


def so_odd(n, q):
    c = (n - 1) // 2
    return [q ** (c * c)] + [q ** (2 * i) - 1 for i in range(1, c + 1)]


def so_even(n, eps, q):
    a = n // 2
    return [q ** (a * (a - 1)), q ** a - eps] + [q ** (2 * i) - 1 for i in range(1, a)]


def V(factors):
    return sum(v_p(7, x) for x in factors)


def vfact(k):
    return sum(v_p(7, i) for i in range(1, k + 1) if i % 7 == 0)


def section_D():
    # D1 residue exclusions for q = 7^f, f = 1..48
    rows = []
    bad = []
    for f in range(1, 49):
        q = 7 ** f
        prime = (f == 1)
        it = {
            "(9)/(10ii)/(21)-(23) q prime, q=+-3 mod 8": prime and q % 8 in (3, 5),
            "(12) q prime, q=5 or q=+-3,+-13 mod 40": prime and (q == 5 or q % 40 in (3, 37, 13, 27)),
            "(14) q prime, q=+-11,+-19 mod 40": prime and q % 40 in (11, 29, 19, 21),
            "(16) q=5": q == 5,
            "(17) q prime, q=5 mod 8": prime and q % 8 == 5,
            "(19) q prime, q=3 mod 8": prime and q % 8 == 3,
            "(13) q prime, q=+-7 mod 16": prime and q % 16 in (7, 9),
            "(15) 7<q=3 mod 4": q > 7 and q % 4 == 3,
            "(6ii)/(20) q=1 mod 4": q % 4 == 1,
            "(7ii)/(18) q=3 mod 4": q % 4 == 3,
            "(11) q square": f % 2 == 0,
        }
        for key in list(it)[:6]:
            if it[key]:
                bad.append((f, key))
        if it["(13) q prime, q=+-7 mod 16"] and f != 1:
            bad.append((f, "(13) beyond f=1"))
        if it["(15) 7<q=3 mod 4"] != (f % 2 == 1 and f >= 3):
            bad.append((f, "(15) parity"))
        if it["(6ii)/(20) q=1 mod 4"] != (f % 2 == 0):
            bad.append((f, "(6ii) parity"))
        if f <= 4:
            rows.append({"f": f, "q mod 8": q % 8, "q mod 16": q % 16, "q mod 40": q % 40,
                         **{k: v for k, v in it.items()}})
    record("positive", "D1 Maslova residue items impossible for q=7^f (f<=48); (13) only f=1; "
           "(15) iff f odd>=3; (6ii) iff f even", not bad, {"violations": bad, "sample": rows})

    # D2 7-adic index valuations from exact order factor lists vs the candidate's closed forms
    mism = []
    minval = {}
    count = 0

    def chk(family, params, val, formula, floor):
        nonlocal count
        count += 1
        if val != formula:
            mism.append({"family": family, "params": params, "val": val, "formula": formula})
        key = family
        minval[key] = min(minval.get(key, 10 ** 9), val)
        if val < floor:
            mism.append({"family": family, "params": params, "val": val, "below_floor": floor})

    for f in (1, 2, 3, 4):
        q = 7 ** f
        check_time()
        # (3) unitary
        for n in range(3, 15):
            for m in range(1, n):
                chk("(3) PSU_n nondeg m-space", [n, m, f], V(gu(n, q)) - V(gu(m, q) + gu(n - m, q)),
                    f * m * (n - m), 2)
        # (3) symplectic
        for n in range(4, 21, 2):
            for m in range(2, n - 1, 2):
                chk("(3) PSp_n nondeg m-space", [n, m, f], V(sp(n, q)) - V(sp(m, q) + sp(n - m, q)),
                    f * m * (n - m) // 2, 2)
        # (4) odd orthogonal
        for n in range(7, 22, 2):
            for b in range(1, (n - 1) // 2 + 1):
                for eps in (1, -1):
                    chk("(4) POmega_n nondeg 2b-space", [n, b, eps, f],
                        V(so_odd(n, q)) - V(so_even(2 * b, eps, q) + so_odd(n - 2 * b, q)),
                        f * b * (n - 2 * b), 2)
        # (5) even orthogonal
        for a in range(4, 11):
            for eps in (1, -1):
                for mm in range(1, 2 * a):
                    if mm % 2 == 1:
                        b = (mm - 1) // 2
                        c = a - 1 - b
                        chk("(5) POmega^e_2a odd m", [a, mm, eps, f],
                            V(so_even(2 * a, eps, q)) - V(so_odd(mm, q) + so_odd(2 * a - mm, q)),
                            f * (2 * b * c + b + c), 2)
                    else:
                        b = mm // 2
                        for e1 in (1, -1):
                            chk("(5) POmega^e_2a even m", [a, mm, eps, e1, f],
                                V(so_even(2 * a, eps, q)) - V(so_even(mm, e1, q) + so_even(2 * a - mm, e1 * eps, q)),
                                f * 2 * b * (a - b), 6)
        # (6i)/(7i)/(8)/(10i) wreath decompositions, m = 2^w >= 2
        for m in (2, 4, 8):
            for k in range(2, 33):
                n = m * k
                if n > 64:
                    break
                lin = f * m * m * k * (k - 1) // 2 - vfact(k)
                chk("(6i) PSL_n GL_m wr S_k", [m, k, f], V(gl(n, q)) - (k * V(gl(m, q)) + vfact(k)), lin, 2)
                chk("(7i) PSU_n GU_m wr S_k", [m, k, f], V(gu(n, q)) - (k * V(gu(m, q)) + vfact(k)), lin, 2)
                sym = f * m * m * k * (k - 1) // 4 - vfact(k)
                chk("(8) PSp_n Sp_m wr S_k", [m, k, f], V(sp(n, q)) - (k * V(sp(m, q)) + vfact(k)), sym, 2)
                if n >= 8:
                    for ei in (1, -1):
                        epsn = ei ** k
                        chk("(10i) POmega_n O_m wr S_k", [m, k, ei, f],
                            V(so_even(n, epsn, q)) - (k * V(so_even(m, ei, q)) + vfact(k)), sym, 2)
        # (6ii)/(7ii) m = 1
        for n in range(3, 50):
            val = f * n * (n - 1) // 2 - vfact(n)
            chk("(6ii) PSL_n GL_1 wr S_n", [n, f], V(gl(n, q)) - (V([q - 1] * n) + vfact(n)), val, 3)
            chk("(7ii) PSU_n GU_1 wr S_n", [n, f], V(gu(n, q)) - (V([q + 1] * n) + vfact(n)), val, 3)
        chk("(6ii) n=2 D_{q-1}", [2, f], V(gl(2, q)) - V([q - 1, q - 1, 2]), f, 1)
        # (18)/(20)
        chk("(18) PSL4 > PSp4.2", [f], V(gl(4, q)) - V(sp(4, q) + [2]), 2 * f, 2)
        chk("(20) PSU4 > PSp4.2", [f], V(gu(4, q)) - V(sp(4, q) + [2]), 2 * f, 2)
    # (1) subfield subgroups, r odd prime dividing f
    for f in (3, 5, 6, 9, 10, 15):
        q = 7 ** f
        for r in prime_divisors(f):
            if r == 2:
                continue
            q0 = 7 ** (f // r)
            for n in range(2, 13):
                N = n * (n - 1) // 2
                chk("(1) subfield PSL_n", [n, f, r], V(gl(n, q)) - V(gl(n, q0)), f * N - f * N // r, 2)
                if n >= 3:
                    chk("(1) subfield PSU_n", [n, f, r], V(gu(n, q)) - V(gu(n, q0)), f * N - f * N // r, 2)
            for h in range(2, 9):
                chk("(1) subfield PSp_2h", [2 * h, f, r], V(sp(2 * h, q)) - V(sp(2 * h, q0)),
                    f * h * h - f * h * h // r, 2)
            for c in range(3, 9):
                chk("(1) subfield Omega_2c+1", [2 * c + 1, f, r], V(so_odd(2 * c + 1, q)) - V(so_odd(2 * c + 1, q0)),
                    f * c * c - f * c * c // r, 2)
            for a in range(4, 9):
                for eps in (1, -1):
                    chk("(1) subfield POmega^e_2a", [2 * a, eps, f, r],
                        V(so_even(2 * a, eps, q)) - V(so_even(2 * a, eps, q0)),
                        f * a * (a - 1) - f * a * (a - 1) // r, 2)
    # (15) D_{q+1}, f odd >= 3
    for f in (3, 5, 7, 9):
        q = 7 ** f
        chk("(15) PSL2 > D_{q+1}", [f], V(gl(2, q)) - V([q + 1, 2, q - 1]), f, 3)
    # (11) for f >= 4 even -- OMITTED by the candidate; valuation f/2 >= 2
    for f in (4, 6, 8, 10):
        q0 = 7 ** (f // 2)
        q = q0 * q0
        val = V([q, q * q - 1]) - V([q0, q0 * q0 - 1])   # |PSL2(q)|=q(q^2-1)/2, |PGL2(q0)|=q0(q0^2-1)
        chk("(11) PSL2(q0^2) > PGL2(q0), f>=4", [f], val, f // 2, 2)
    ok = not mism
    record("positive", "D2 exact 7-adic valuations equal closed forms and meet floors "
           "(families (1),(3)-(8),(10i),(11 f>=4),(15),(18),(20))", ok,
           {"checks": count, "mismatches": mism[:20], "min_by_family": minval})
    # D3 negative: the two genuine valuation-1 exceptions
    v_s4 = v_p(7, 168) - v_p(7, 24)
    v_pgl = v_p(7, 58800) - v_p(7, 336)
    v11_f2 = V([49, 49 * 49 - 1]) - V([7, 48])
    record("negative", "D3 valuation-1 exceptions reproduced: S4<PSL2(7) [168/24=7], PGL2(7)<PSL2(49) "
           "[58800/336=175], item (11) at f=2", v_s4 == 1 and v_pgl == 1 and v11_f2 == 1
           and 168 // 24 == 7 and 58800 // 336 == 175,
           {"S4<PSL2(7)": v_s4, "PGL2(7)<PSL2(49)": v_pgl, "item(11) f=2": v11_f2})


# ============================================================================ E
def gauss_binom(n, k, Q):
    num = 1
    den = 1
    for i in range(k):
        num *= Q ** (n - i) - 1
        den *= Q ** (i + 1) - 1
    if num % den:
        raise ValueError("non-integral Gaussian binomial")
    return num // den


def polar_count(n, k, q, kind):
    """Number of totally singular k-spaces in a polar space of rank n.
    kind: 'Sp'/'Oodd' (e=1), 'O+' (e=0), 'O-' (e=2, rank n => O^-_{2n+2}), 'U_even' (U_{2n}), 'U_odd' (U_{2n+1})."""
    if kind in ("Sp", "Oodd", "O+", "O-"):
        e = {"Sp": 1, "Oodd": 1, "O+": 0, "O-": 2}[kind]
        g = gauss_binom(n, k, q)
        t = 1
        for i in range(k):
            t *= q ** (n - i - 1 + e) + 1
        return g * t
    e2 = 1 if kind == "U_even" else 3
    g = gauss_binom(n, k, q * q)
    t = 1
    for i in range(k):
        t *= q ** (2 * (n - i - 1) + e2) + 1
    return g * t


def section_E():
    # E1: D(S) in Lemma P never in {1,7} for q=7^f: D = 1 mod 7 and D >= 2
    bad = []
    count = 0
    for f in range(1, 7):
        q = 7 ** f
        for e in range(2, 61):
            D = Phi(e, q)
            count += 1
            if D % 7 != 1 or D < 2 or D in (1, 7):
                bad.append((f, e, D % 7))
    record("positive", "E1 Phi_e(7^f) = 1 mod 7 and >= 2 (so not in {1,7}) for 2<=e<=60, f<=6",
           not bad, {"checked": count, "bad": bad})
    # E2: Lemma 2 divisibility (import) re-checked by independent flag counts at q=7,49
    fails = []
    checks = 0
    for q in (7, 49):
        for n in range(1, 13):           # A_n : PSL_{n+1}
            D = Phi(n + 1, q)
            for k in range(1, n + 1):
                checks += 1
                if gauss_binom(n + 1, k, q) % D:
                    fails.append(("A", n, k, q))
        for n in range(2, 11):           # B_n, C_n
            D = Phi(2 * n, q)
            for k in range(1, n + 1):
                for kind in ("Sp", "Oodd"):
                    checks += 1
                    if polar_count(n, k, q, kind) % D:
                        fails.append((kind, n, k, q))
        for n in range(4, 11):           # D_n : O^+_{2n}; maximal parabolics k<=n-2 and two half-spin
            D = Phi(2 * n - 2, q)
            idx = [polar_count(n, k, q, "O+") for k in range(1, n - 1)]
            idx.append(polar_count(n, n, q, "O+") // 2)
            for x in idx:
                checks += 1
                if x % D:
                    fails.append(("D", n, q))
        for n in range(4, 11):           # 2D_n : O^-_{2n}, polar rank n-1
            D = Phi(2 * n, q)
            for k in range(1, n):
                checks += 1
                if polar_count(n - 1, k, q, "O-") % D:
                    fails.append(("2D", n, k, q))
        for m in range(3, 13):           # 2A_{m-1} : PSU_m
            D = Phi(2 * m, q) if m % 2 else Phi(2 * (m - 1), q)
            rank = m // 2
            kind = "U_odd" if m % 2 else "U_even"
            for k in range(1, rank + 1):
                checks += 1
                if polar_count(rank, k, q, kind) % D:
                    fails.append(("2A", m, k, q))
    record("positive", "E2 D(S) divides every maximal-parabolic index via flag counts (finite, q=7,49)",
           not fails, {"checks": checks, "fails": fails[:10]})
    # E3 negatives: (a) wrong cyclotomic for A_n fails at k=1; (b) at q=3, D=Phi_6(3)=7 (Lemma P breaks)
    wrong = [(n, gauss_binom(n + 1, 1, 7) % Phi(n, 7) != 0) for n in range(2, 9)]
    d3 = Phi(6, 3)
    sanity = polar_count(2, 1, 3, "Sp") == (3 + 1) * (9 + 1) and polar_count(1, 1, 7, "U_odd") == 7 ** 3 + 1
    record("negative", "E3 wrong D (Phi_n for A_n) fails; at q=3 D=Phi_6(3)=7 so 'D|7' is no contradiction",
           all(w for _, w in wrong) and d3 == 7 and sanity,
           {"Phi_n_fails_k1": wrong, "Phi_6(3)": d3, "formula_sanity": sanity})


# ============================================================================ F
def section_F():
    o = 49 * (49 * 49 - 1) // 2
    cof = o // 7
    divs = [d for d in range(2, cof + 1) if cof % d == 0]
    best = []

    def dfs(start, chosen):
        nonlocal best
        if len(chosen) > len(best):
            best = list(chosen)
        for i in range(start, len(divs)):
            d = divs[i]
            if all(__import__("math").gcd(d, c) == 1 for c in chosen):
                chosen.append(d)
                dfs(i + 1, chosen)
                chosen.pop()

    dfs(0, [])
    ok = (o == 58800 and cof == 8400 and factor_trial(cof) == [2, 2, 2, 2, 3, 5, 5, 7]
          and len(best) == 4 and 2520 % o != 0 and 5040 % o != 0)
    record("positive", "F1 |PSL2(49)|=58800 does not divide 7!; 8400=2^4*3*5^2*7; "
           "max pairwise-coprime divisors >1 of 8400 is 4 < 8", ok,
           {"order": o, "cofactor": cof, "max_coprime_set_size": len(best), "example": best})
    # F2 negative: if index-7 subgroups existed, cofactor 1 repeated is pairwise coprime (unbounded)
    ones = [1] * 8
    rep = all(__import__("math").gcd(a, b) == 1 for i, a in enumerate(ones) for b in ones[i + 1:])
    record("negative", "F2 repeated cofactor 1 is pairwise coprime: the no-index<=7 step is load-bearing",
           rep, {"eight_ones_pairwise_coprime": rep})
    # F3 Lemma U: |S| does not divide 2520 (no proper subgroup of index <= 7) for exceptional S at q=7
    res = {}
    ok3 = True
    for typ in ("G2", "3D4", "F4", "E6", "2E6", "E7", "E8"):
        fs, div = exc_order_factors(typ, 7)
        prod = 1
        for x in fs:
            prod *= x
        o = prod // div
        res[typ] = {"v7": v_p(7, o), "divides_2520": 2520 % o == 0}
        ok3 = ok3 and 2520 % o != 0 and v_p(7, o) >= 6
    record("positive", "F3 exceptional |S| at q=7 never divides 2520 (v_7(|S|)>=6)", ok3, res)


# ============================================================================ G
def section_G():
    raw = open(BBGT_TXT, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    txt = raw.decode("utf-8")
    needles = {
        "Theorem2(iii)": "$T$ is an exceptional group of Lie type and $(G,r,H)$ is recorded in Table C.",
        "alpha_def": "$(q^{1/k})^{m}\\not\\equiv\\epsilon\\allowbreak\\mkern 4.0mu({\\operator@font mod}\\,\\,r)$ for all $k\\in\\pi(f)\\setminus\\{r\\}$",
        "beta_def": "we write $\\beta(m,\\epsilon)$ for the same condition, but restricted to the odd primes in $\\pi(f)\\setminus\\{r\\}$",
        "G2": "G_{2}(q)&r_{(3-\\epsilon)/2}&A_{2}^{\\epsilon}(q)&",
        "G2_r6": "&r_{3(3-\\epsilon)/2}&A_{2}^{\\epsilon}(q)&\\mbox{$\\alpha(3,\\epsilon)$ and either $p=2$ and $(\\epsilon,q)\\neq(-1,4)$, or}",
        "G2_size": "\\mbox{$p\\geqslant 5$ and either $f>3$, or $|R|>r$, or $r>13$, or}",
        "3D4": "&r_{12}&q^{4}-q^{2}+1&\\mbox{$(q^{1/k})^{6}\\not\\equiv-1\\allowbreak\\mkern 4.0mu({\\operator@font mod}\\,\\,r)$ for all $k\\in\\pi(f)\\setminus\\{3,r\\}$}",
        "F4": "F_{4}(q)&r_{8}&\\Omega_{9}(q)&\\mbox{$p\\geqslant 3$, $\\alpha(4,-1)$ and either $f>2$, or $r>17$, or $|R|>r$, or}",
        "E6": "E_{6}(q)&r_{9}&A_{2}(q^{3})&\\mbox{$\\alpha(9,1)$ and either $f>2$, or $r>19$, or $|R|>r$, or}",
        "2E6": "{}^{2}E_{6}(q)&r_{18}&A_{2}^{-}(q^{3})&\\mbox{$\\beta(9,1)$ and either $f>1$, or $r>19$, or $|R|>r$, or}",
        "2E6_text_variant": "there are no subfield subgroups in $\\mathcal{M}(R)$ if and only if $\\beta(9,-1)$ holds",
        "E7": "E_{7}(q)&r_{18}&{}^{2}\\!E_{6}(q)\\times(q+1)&\\mbox{$\\alpha(18,1)$ and either $f>2$, or $r>37$, or $|R|>r$, or}",
        "E8": "E_{8}(q)&r_{15(3-\\epsilon)/2}&q^{8}-\\epsilon q^{7}+\\epsilon q^{5}-q^{4}+\\epsilon q^{3}-\\epsilon q+1&\\mbox{$\\alpha(30,1)$ and either $r>61$, or $|R|>r$, or $|R|=r=61$ and}",
        "Zsigmondy": "such a prime $r$ exists unless $(d,q)=(6,2)$ , or if $d=2$ and $q$ is a Mersenne prime.",
    }
    found = {k: (txt.count(v)) for k, v in needles.items()}
    ok = sha == BBGT_TXT_SHA and all(c >= 1 for c in found.values())
    record("positive", "G1 every used Table C row/definition string is present in the pinned extraction",
           ok, {"extraction_sha256": sha, "counts": found})


def main():
    started = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    adata = section_A()
    section_B(adata)
    section_C()
    section_D()
    section_E()
    section_F()
    section_G()
    pos_ok = all(r["ok"] for r in RESULTS["positive"])
    neg_ok = all(r["ok"] for r in RESULTS["negative"])
    receipt = {"script": os.path.abspath(__file__),
               "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
               "started_utc": started,
               "elapsed_seconds": round(time.time() - T0, 3),
               "all_positive_pass": pos_ok,
               "all_negative_as_intended": neg_ok,
               "results": RESULTS}
    with open(OUT, "x", encoding="utf-8") as fh:
        json.dump(receipt, fh, indent=1, default=str)
        fh.write("\n")
    for kind in ("positive", "negative"):
        for r in RESULTS[kind]:
            print(f"[{kind[:3].upper()}] {'OK ' if r['ok'] else 'BAD'} {r['name']}")
    print(f"ALL_POSITIVE_PASS={pos_ok} ALL_NEGATIVE_AS_INTENDED={neg_ok} "
          f"elapsed={receipt['elapsed_seconds']}s")
    return 0 if (pos_ok and neg_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
