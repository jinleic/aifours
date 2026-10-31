#!/usr/bin/env python3
"""f151 reviewer-authored exact control (independent design; no author code read or imported).

Scope: the integer-divisor relaxation that underlies bounds 1-4 of
frontier-20261028-source-free-support-consolidated-v1.md.  A disjoint-coset
family with pairwise index gcds <= 7 yields a set of DISTINCT integers m_i | |G|,
m_i >= mu, pairwise gcd in [2,7] (coprime-index cosets intersect).  Capping
exponents (2^4, 3^3, 5^2, 7^2, large primes to power 1) and relabelling the k
large primes to the first k primes > 7 preserves pairwise gcd in [2,7], the
small-prime supports, distinctness and m >= mu for every mu <= 13 tested, so the
maximum clique over divisors of M(Y,k) is the exact relaxation maximum.

Parts: A type-family exhaustiveness; B relaxation maxima vs candidate bounds
(positive) plus intended-reason mutations (negative); C integer witnesses;
D alternating-group arithmetic facts used by the simple-group remark.
"""
import itertools, math, json, sys, time

SMALL = (2, 3, 5, 7)
LARGE = (11, 13, 17)
CAP = {2: 4, 3: 3, 5: 2, 7: 2}
out = {"observed_start_epoch": time.time(), "start_local": time.strftime("%Y-%m-%dT%H:%M:%S%z")}

# ---------- Part A: pairwise-intersecting support families ----------
def type_family_max(universe, prod_cap, min_size=2):
    subsets = [frozenset(c) for r in range(min_size, len(universe) + 1)
               for c in itertools.combinations(universe, r)]
    def ok(a, b):
        i = a & b
        return bool(i) and math.prod(i) <= prod_cap
    best, maximal = 0, []
    for r in range(1, len(subsets) + 1):
        for fam in itertools.combinations(subsets, r):
            if all(ok(a, b) for a, b in itertools.combinations(fam, 2)) and not frozenset.intersection(*fam):
                if r > best:
                    best, maximal = r, [fam]
                elif r == best:
                    maximal.append(fam)
    return best, [sorted(sorted(s) for s in fam) for fam in maximal]

A = {}
A["cap7_universe2357"] = type_family_max(SMALL, 7)
A["cap15_mutation"] = type_family_max(SMALL, 15)          # negative control: allow {3,5} intersections
A["cap7_min_size1_mutation"] = type_family_max(SMALL, 7, 1)  # negative control: singletons allowed
out["A_type_families"] = {k: {"max": v[0], "n_max_families": len(v[1]), "max_families": v[1]} for k, v in A.items()}

# ---------- Part B: exact relaxation maxima ----------
def divisors_capped(Y, k):
    parts = [(p, CAP[p]) for p in Y] + [(q, 1) for q in LARGE[:k]]
    divs = [1]
    for p, e in parts:
        divs = [d * p ** i for d in divs for i in range(e + 1)]
    return divs

def max_clique(n, adj):
    best = [0, []]
    def expand(R, P):
        if P == 0:
            if len(R) > best[0]:
                best[0], best[1] = len(R), list(R)
            return
        if len(R) + bin(P).count("1") <= best[0]:
            return
        u = max((i for i in range(n) if P >> i & 1), key=lambda i: bin(P & adj[i]).count("1"))
        cand = P & ~adj[u]
        while cand:
            v = (cand & -cand).bit_length() - 1
            expand(R + [v], P & adj[v])
            P &= ~(1 << v)
            cand &= ~(1 << v)
    expand([], (1 << n) - 1)
    return best

def relaxation_max(Y, k, mu, gcd_lo=2, gcd_hi=7):
    divs = [d for d in divisors_capped(Y, k) if d >= mu and any(d % p == 0 for p in Y)]
    n = len(divs)
    adj = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            g = math.gcd(divs[i], divs[j])
            if gcd_lo <= g <= gcd_hi:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    size, idx = max_clique(n, adj)
    return size, sorted(divs[i] for i in idx), n

def candidate_bounds(Y, k, mu):
    b = {}
    if mu >= 8:
        b["item1_k+5"] = k + 5
    if mu >= 8 and (2 not in Y or 3 not in Y):
        b["item2_k+|Y|"] = k + len(Y)
    if mu >= 13 and len(Y) <= 2:
        b["item3_k+2"] = k + 2
    if mu >= 13 and len(Y) <= 3:
        b["item4_k+4"] = k + 4
    return b

positive = []
violations = []
for r in range(1, 5):
    for Y in itertools.combinations(SMALL, r):
        for k in range(0, 4):
            for mu in (8, 13):
                size, wit, nv = relaxation_max(Y, k, mu)
                b = candidate_bounds(Y, k, mu)
                tight = min(b.values())
                rec = {"Y": list(Y), "k": k, "mu": mu, "relax_max": size, "witness": wit,
                       "n_vertices": nv, "bounds": b, "tightest_bound": tight, "attained": size == tight}
                positive.append(rec)
                if size > tight:
                    violations.append(rec)
out["B_positive"] = positive
out["B_violations_of_candidate_bounds"] = violations

neg = {}
neg["mu6_fullY_item1"] = [dict(zip(("relax_max", "witness", "n"), relaxation_max(SMALL, k, 6))) | {"k": k, "candidate_k+5": k + 5} for k in range(3)]
neg["mu7_fullY_item1"] = [dict(zip(("relax_max", "witness", "n"), relaxation_max(SMALL, k, 7))) | {"k": k, "candidate_k+5": k + 5} for k in range(3)]
neg["mu12_Y23_item3"] = [dict(zip(("relax_max", "witness", "n"), relaxation_max((2, 3), k, 12))) | {"k": k, "candidate_k+2": k + 2} for k in range(3)]
neg["mu13_fullY_vs_item4"] = [dict(zip(("relax_max", "witness", "n"), relaxation_max(SMALL, k, 13))) | {"k": k, "item4_would_be_k+4": k + 4} for k in range(3)]
neg["mu8_Y235_item4_hypothesis_probe"] = [dict(zip(("relax_max", "witness", "n"), relaxation_max((2, 3, 5), k, 8))) | {"k": k, "k+4": k + 4} for k in range(3)]
neg["mu8_Y237_item4_hypothesis_probe"] = [dict(zip(("relax_max", "witness", "n"), relaxation_max((2, 3, 7), k, 8))) | {"k": k, "k+4": k + 4} for k in range(3)]
neg["gcdcap8_fullY_mu8"] = [dict(zip(("relax_max", "witness", "n"), relaxation_max(SMALL, k, 8, 2, 8))) | {"k": k, "candidate_k+5": k + 5} for k in range(2)]
neg["Y2357_vs_Y257_mu8_item2"] = {"Y257": dict(zip(("relax_max", "witness", "n"), relaxation_max((2, 5, 7), 1, 8))),
                                  "Y2357": dict(zip(("relax_max", "witness", "n"), relaxation_max(SMALL, 1, 8)))}
out["B_negative_controls"] = neg

# ---------- Part C: candidate integer witnesses ----------
def check_witness(vals, mu, Yclaim):
    pairs = [(a, b, math.gcd(a, b)) for a, b in itertools.combinations(vals, 2)]
    supp = set()
    for v in vals:
        d = 2
        x = v
        while d * d <= x:
            while x % d == 0:
                supp.add(d); x //= d
            d += 1
        if x > 1:
            supp.add(x)
    return {"values": vals, "count": len(vals), "all_ge_mu": all(v >= mu for v in vals),
            "gcds_in_2_7": all(2 <= g <= 7 for _, _, g in pairs), "distinct": len(set(vals)) == len(vals),
            "small_support": sorted(p for p in supp if p <= 7), "claimed_Y": sorted(Yclaim),
            "support_within_claim": all(p in Yclaim for p in supp if p <= 7)}
P = (11, 13, 17)
C = {
    "k+5_mu8": check_witness([8, 12, 18, 20, 28] + [6 * p for p in P], 8, (2, 3, 5, 7)),
    "k+3_mu8_no3": check_witness([8, 10, 14] + [2 * p for p in P], 8, (2, 5, 7)),
    "k+2_mu13_Y23": check_witness([16, 18] + [6 * p for p in P], 13, (2, 3)),
    "k+4_mu13_Y235": check_witness([24, 18, 20, 15] + [6 * p for p in P], 13, (2, 3, 5)),
    "reviewer_k+5_mu13_fullY": check_witness([24, 18, 20, 15, 42] + [6 * p for p in P], 13, (2, 3, 5, 7)),
}
out["C_witnesses"] = C

# ---------- Part D: alternating-group arithmetic facts ----------
def prime_factors(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f
D = []
for n in range(5, 18):
    order = math.factorial(n) // 2
    pf = prime_factors(order)
    k = sum(1 for p in pf if p > 7)
    Y = sorted(p for p in pf if p <= 7)
    m = 1
    while math.factorial(m) % order:
        m += 1
    r = max(pf)
    cond_i = (m >= 8 and k <= 2)
    cond_iv = (m >= 13 and len(Y) <= 3 and k <= 3)
    D.append({"n": n, "order": order, "k": k, "Y": Y, "largest_prime": r,
              "least_m_with_order_dividing_m_factorial": m, "mu_lower_bound_ge_n": m >= n,
              "largest_prime_bound_only": r, "cond_i_mu8_k_le2": cond_i, "cond_iv": cond_iv})
out["D_alternating_facts"] = D

out["end_local"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
out["elapsed_s"] = round(time.time() - out["observed_start_epoch"], 3)
json.dump(out, sys.stdout, indent=1, sort_keys=True)
print()
