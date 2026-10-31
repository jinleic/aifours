#!/usr/bin/env python3
"""reviewer-binomial-gcd-control-v1.py

Independent exact control written by the f132 same-harness reviewer.
Standard library only. No author code is imported, read or executed here.

Checks (all exact integer / rational arithmetic):
  P1  pairwise binomial lemma, hypothesis n > 7j (j <= t < n/7), 1 <= i < j:
        identity      C(n,i)*C(n-i,j-i) == C(n,j)*C(j,i)
        divisibility  (C(n,i)/g) | C(j,i)            with g = gcd(C(n,i),C(n,j))
        ratio         C(n,i)/C(j,i) >= n/j  and  n/j > 7
        conclusion    g > 7
  P2  equal-index case: C(n,u) >= n > 7 for 1 <= u <= t
  P3  Dusart-threshold arithmetic for n = 500000 (exact rationals)
  N1  negative control, hypothesis violated (7j >= n): explicit pairs with gcd <= 7,
      including the boundary n = 14 = 7*2 where gcd(C(14,1),C(14,2)) = 7 exactly
  N2  negative control at n = 5: all subgroups of A5 by closure enumeration;
      proper indices 5, 6, 15 are three proper subgroups with pairwise gcd <= 7
  S1  consistency of the candidate's example degree n = 510510, r = 510481, t = 29
"""
import hashlib
import json
import math
import os
import platform
import sys
import time
from fractions import Fraction
from itertools import combinations, permutations

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "reviewer-binomial-gcd-control-v1.receipt.json")


def stamp():
    return time.strftime("%Y-%m-%dT%H:%M:%S%z %Z", time.localtime())


receipt = {
    "control": os.path.basename(__file__),
    "clock_start": stamp(),
    "python": sys.version.split()[0],
    "platform": platform.platform(),
}

# ---------------------------------------------------------------- P1 / P2
def pair_checks(n, i, j):
    A = math.comb(n, i)
    B = math.comb(n, j)
    g = math.gcd(A, B)
    identity_ok = (A * math.comb(n - i, j - i) == B * math.comb(j, i))
    divisibility_ok = (math.comb(j, i) % (A // g) == 0)
    ratio = Fraction(A, math.comb(j, i))
    ratio_ok = (ratio >= Fraction(n, j)) and (Fraction(n, j) > 7)
    return identity_ok, divisibility_ok, ratio_ok, (g > 7), g


def run_pairs(label, cases):
    total = 0
    failures = []
    min_g = None
    for (n, i, j) in cases:
        assert 1 <= i < j and 7 * j < n, ("hypothesis", n, i, j)
        ident, div, ratio_ok, gcd_ok, g = pair_checks(n, i, j)
        total += 1
        if not (ident and div and ratio_ok and gcd_ok):
            failures.append({"n": n, "i": i, "j": j, "identity": ident,
                             "divisibility": div, "ratio": ratio_ok,
                             "gcd_gt7": gcd_ok, "gcd": str(g)})
        if min_g is None or g < min_g[0]:
            min_g = (g, n, i, j)
    return {"label": label, "pairs": total, "failures": failures,
            "min_gcd_observed": {"gcd": str(min_g[0]), "n": min_g[1],
                                 "i": min_g[2], "j": min_g[3]}}


def run_equal(label, cases):
    total = 0
    failures = []
    for (n, u) in cases:
        assert 1 <= u and 7 * u < n
        total += 1
        if not (math.comb(n, u) >= n > 7):
            failures.append({"n": n, "u": u})
    return {"label": label, "cases": total, "failures": failures}


# (a) exhaustive: every n in [22, 300], t = (n-1)//7 (largest t with 7t < n), all i<j<=t
cases_a = [(n, i, j) for n in range(22, 301)
           for (i, j) in combinations(range(1, (n - 1) // 7 + 1), 2)]
# (b) candidate example degree n = 510510 with t = 29, all pairs
cases_b = [(510510, i, j) for (i, j) in combinations(range(1, 30), 2)]
# (c) minimum claimed degree n = 500000: all pairs with j <= 80, plus boundary pairs at t_max
n0 = 500000
tmax = (n0 - 1) // 7
cases_c = [(n0, i, j) for (i, j) in combinations(range(1, 81), 2)] + \
          [(n0, 1, tmax), (n0, 2, tmax), (n0, tmax - 1, tmax), (n0, 1, tmax - 1)]

P1 = [run_pairs("a: n in [22,300], t=(n-1)//7, all pairs", cases_a),
      run_pairs("b: n=510510, t=29, all pairs", cases_b),
      run_pairs("c: n=500000, j<=80 all pairs + boundary pairs at t_max=71428", cases_c)]
P2 = [run_equal("a: n in [22,300], u<=t", [(n, u) for n in range(22, 301)
                                           for u in range(1, (n - 1) // 7 + 1)]),
      run_equal("c: n=500000, u<=80 and u=t_max", [(n0, u) for u in range(1, 81)] + [(n0, tmax)])]
receipt["P1_pairwise_lemma"] = P1
receipt["P2_equal_index"] = P2
receipt["P1_P2_all_pass"] = all(not r["failures"] for r in P1 + P2)

# ---------------------------------------------------------------- P3  Dusart arithmetic (exact)
DUSART_X0 = 396738
x = Fraction(6 * n0, 7)
n_min_for_dusart = -((-DUSART_X0 * 7) // 6)          # ceil(396738*7/6)
upper_crude = Fraction(156 * n0, 175)                 # x*(26/25); valid once ln x > 1
P3 = {
    "x_equals_6n_over_7": str(x),
    "x_ge_396738": x >= DUSART_X0,
    "smallest_n_with_6n_over_7_ge_396738": n_min_for_dusart,
    "check_6*n_min/7": str(Fraction(6 * n_min_for_dusart, 7)),
    "ln_x_at_x0": math.log(DUSART_X0),
    "log10_x_at_x0": math.log10(DUSART_X0),
    "crude_upper_156n_over_175": str(upper_crude),
    "crude_upper_lt_n_minus_3": upper_crude < n0 - 3,
    "19n_gt_525_equivalent_threshold_n_ge": 28,
    "t_ge_4_follows": (n0 - upper_crude) > 3,
    "t_lt_n_over_7_follows_from_r_gt_x": True,
    "x_never_prime_note": "if 7|n then x=6n/7 is a multiple of 6 (composite); else x is not an integer",
    "numerical_dusart_window_at_n0": {
        "x": float(x),
        "x_times_1_plus_1_over_25ln2x": float(x) * (1 + 1 / (25 * math.log(float(x)) ** 2)),
        "implied_t_range": [n0 - math.floor(float(x) * (1 + 1 / (25 * math.log(float(x)) ** 2))),
                            n0 - math.floor(float(x)) - 1],
    },
}
receipt["P3_dusart_threshold"] = P3

# ---------------------------------------------------------------- N1  negative control: 7j >= n
neg = []
for n in range(8, 201):
    for j in range((n + 6) // 7, n // 2 + 1):      # 7j >= n : hypothesis violated for the pair
        for i in range(1, j):
            g = math.gcd(math.comb(n, i), math.comb(n, j))
            if g <= 7:
                neg.append((n, i, j, g))
explicit = {
    "n=14,i=1,j=2 (boundary n=7t)": math.gcd(math.comb(14, 1), math.comb(14, 2)),
    "n=10,i=1,j=2": math.gcd(math.comb(10, 1), math.comb(10, 2)),
    "n=64,i=1,j=16": math.gcd(math.comb(64, 1), math.comb(64, 16)),
    "n=64,i=1,j=8 (allowed, 7*8<64; tight)": math.gcd(math.comb(64, 1), math.comb(64, 8)),
}
N1 = {
    "scan": "n in [8,200], j in [ceil(n/7), n//2], 1<=i<j",
    "violating_pairs_found": len(neg),
    "distinct_n_with_violation": len({v[0] for v in neg}),
    "first_twelve": [{"n": a, "i": b, "j": c, "gcd": d} for (a, b, c, d) in neg[:12]],
    "explicit": explicit,
    "negative_control_present": len(neg) > 0 and explicit["n=14,i=1,j=2 (boundary n=7t)"] == 7
    and explicit["n=10,i=1,j=2"] == 5,
}
assert N1["negative_control_present"]
receipt["N1_negative_hypothesis_violated"] = N1

# ---------------------------------------------------------------- N2  A5 subgroup indices
def compose(p, q):
    return tuple(p[q[k]] for k in range(5))


def even(p):
    return sum(1 for a in range(5) for b in range(a + 1, 5) if p[a] > p[b]) % 2 == 0


A5 = [p for p in permutations(range(5)) if even(p)]
assert len(A5) == 60
E = tuple(range(5))


def closure(gens):
    S = {E}
    frontier = [E]
    while frontier:
        new = []
        for s in frontier:
            for g in gens:
                y = compose(s, g)
                if y not in S:
                    S.add(y)
                    new.append(y)
        frontier = new
    return frozenset(S)


subgroups = {closure([])}
changed = True
while changed:                      # every subgroup arises by adjoining generators one at a time
    changed = False
    for H in list(subgroups):
        for g in A5:
            if g in H:
                continue
            K = closure(list(H) + [g])
            if K not in subgroups:
                subgroups.add(K)
                changed = True
orders = sorted({len(H) for H in subgroups})
proper_indices = sorted({60 // len(H) for H in subgroups if len(H) < 60})
triple = (5, 6, 15)
quad = (5, 6, 15, 20)
N2 = {
    "subgroup_count": len(subgroups),
    "subgroup_orders": orders,
    "proper_subgroup_indices": proper_indices,
    "note_indices_5_6_15_20_all_present": all(v in proper_indices for v in quad),
    "pairwise_gcd_5_6_15_20": {f"{a},{b}": math.gcd(a, b) for a, b in combinations(quad, 2)},
    "three_proper_indices_with_pairwise_gcd_le_7": list(triple),
    "three_index_statement_false_at_n5": all(math.gcd(a, b) <= 7 for a, b in combinations(triple, 2)),
    "why_argument_cannot_start_at_n5": "t>=3 and 7t<n force n>=22; n=5 admits no such prime r",
}
assert N2["three_index_statement_false_at_n5"]
receipt["N2_A5_small_n_falsity"] = N2

# ---------------------------------------------------------------- S1  candidate example degree
def is_prime_trial(m):
    if m < 2:
        return False
    for d in range(2, math.isqrt(m) + 1):
        if m % d == 0:
            return False
    return True


n1, r1 = 510510, 510481
t1 = n1 - r1
S1 = {
    "r_prime_by_trial_division": is_prime_trial(r1),
    "t": t1,
    "3_le_t": t1 >= 3,
    "7t_lt_n": 7 * t1 < n1,
    "r_gt_n_over_2": 2 * r1 > n1,
    "r_in_dusart_window_for_x=6n/7": (Fraction(6 * n1, 7) < r1 <= Fraction(6 * n1, 7) * Fraction(26, 25)),
    "note": "r=510481 is NOT the Dusart-window prime for x=6n/7; it is a different prime meeting 3<=t<n/7, as Section 4 of the candidate allows",
    "gcd_of_C(n,u)_u_1_to_29": str(math.gcd(*[math.comb(n1, u) for u in range(1, 30)])),
    "min_pairwise_gcd_u_1_to_29": str(min(math.gcd(math.comb(n1, u), math.comb(n1, v))
                                         for u, v in combinations(range(1, 30), 2))),
}
receipt["S1_candidate_example_degree"] = S1

# ---------------------------------------------------------------- receipt
with open(os.path.abspath(__file__), "rb") as fh:
    receipt["script_sha256"] = hashlib.sha256(fh.read()).hexdigest()
receipt["clock_end"] = stamp()
receipt["overall"] = {
    "P1_P2_pass": receipt["P1_P2_all_pass"],
    "P3_pass": all([P3["x_ge_396738"], P3["crude_upper_lt_n_minus_3"], P3["t_ge_4_follows"]]),
    "N1_negative_present": N1["negative_control_present"],
    "N2_negative_present": N2["three_index_statement_false_at_n5"],
}
with open(OUT, "w") as fh:
    json.dump(receipt, fh, indent=1)
print(json.dumps(receipt["overall"]))
print("P1:", [(r["label"], r["pairs"], len(r["failures"]), r["min_gcd_observed"]) for r in P1])
print("P2:", [(r["label"], r["cases"], len(r["failures"])) for r in P2])
print("P3:", {k: P3[k] for k in ("x_ge_396738", "smallest_n_with_6n_over_7_ge_396738",
                                "crude_upper_156n_over_175", "crude_upper_lt_n_minus_3",
                                "numerical_dusart_window_at_n0")})
print("N1:", N1["violating_pairs_found"], N1["distinct_n_with_violation"], N1["explicit"], N1["first_twelve"][:6])
print("N2:", N2["subgroup_count"], N2["subgroup_orders"], N2["proper_subgroup_indices"], N2["pairwise_gcd_5_6_15_20"])
print("S1:", S1)
print("script_sha256:", receipt["script_sha256"])
print("clock:", receipt["clock_start"], "->", receipt["clock_end"])
