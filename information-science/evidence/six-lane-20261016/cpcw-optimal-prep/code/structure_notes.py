#!/usr/bin/env python3
"""Exact structure notes (necessary conditions only, no search) for optimal (v,k,1) CPCW codes at the candidate
lengths k=5: 143,144,146,162,167 and k=6: 122,123,124,126.

For each (v,k): s, forced uncovered count u = v-1-k(k-1)s, the forced v/2 for even v, the number c of uncovered
+-classes besides v/2, factorization, phi(v), invariant factors of Z_v^*, prime orders available in Q = Z_v^*/{+-1}.
Subgroup counting (index m dividing v, m in {2,3,4}): a codeword whose elements have residue profile r mod m has
S_m = sum C(r_j,2) unordered pairs with difference = 0 mod m.  Every usable class (v/2 excluded for even v) with
d = 0 mod m is covered by exactly one such pair unless uncovered, so
    sum over codewords of S_m = Z_m - z,      z = number of uncovered classes (besides v/2) with d = 0 mod m.
The script enumerates all multisets of s profiles and all z in [0,c] satisfying this, and reports which z are
possible (a necessary condition on how many uncovered classes lie in mZ_v).  For v = k(k-1)t+2 it also solves the
Baicheva-Topalova Theorem 1/2 system (Axioms 15 (2026) 35) for the type counts a_i.
"""
import itertools
import json
import math
import sys


def factor(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def unit_group(v):
    units = [a for a in range(1, v) if math.gcd(a, v) == 1]
    orders = {}
    for a in units:
        x, o = a, 1
        while x != 1:
            x = x * a % v
            o += 1
        orders[a] = o
    exp = 1
    for o in orders.values():
        exp = exp * o // math.gcd(exp, o)
    # class orders in Q
    qprimes = set()
    for a in units:
        j, x = 1, a
        while x not in (1, v - 1):
            x = x * a % v
            j += 1
        if j > 1 and all(j % p for p in range(2, j)):
            qprimes.add(j)
    return len(units), exp, sorted(qprimes)


def profiles(k, m):
    out = set()
    for comp in itertools.product(range(k + 1), repeat=m):
        if sum(comp) == k and all(c <= -(-k // 1) for c in comp):
            out.add(sum(c * (c - 1) // 2 for c in comp))
    return sorted(out)


def usable_zero_classes(v, m):
    H = (v - 1) // 2
    cls = [d for d in range(1, H + 1)] + ([v // 2] if v % 2 == 0 else [])
    usable = [d for d in cls if not (v % 2 == 0 and d == v // 2)]
    return sum(1 for d in usable if d % m == 0), len(usable)


def feasible_z(v, k, s, c, m):
    Zm, _ = usable_zero_classes(v, m)
    P = profiles(k, m)
    sums = {0}
    for _ in range(s):
        sums = {x + p for x in sums for p in P}
    return sorted(z for z in range(0, c + 1) if (Zm - z) in sums), Zm, P


def bt_system(v, k):
    t = (v - 2) // (k * (k - 1))
    sols = []
    S = [i * (i - 1) // 2 + (k - i) * (k - i - 1) // 2 for i in range(k // 2 + 1)]
    X = [i * (k - i) for i in range(k // 2 + 1)]
    if v % 4 == 2:
        same, cross = (v - 2) // 4, (v - 2) // 4
    else:
        same, cross = (v - 4) // 4, v // 4
    for a in itertools.product(range(t + 1), repeat=k // 2 + 1):
        if sum(a) == t and sum(S[i] * a[i] for i in range(len(a))) == same and sum(X[i] * a[i] for i in range(len(a))) == cross:
            sols.append(list(a))
    return dict(t=t, v_mod_4=v % 4, same_parity_classes=same, cross_parity_classes=cross,
                type_counts_a_0_to_floor_k_over_2=sols)


def main():
    cases = [(143, 5), (144, 5), (146, 5), (162, 5), (167, 5), (122, 6), (123, 6), (124, 6), (126, 6)]
    out = []
    for v, k in cases:
        s = (v - 1) // (k * (k - 1))
        u = v - 1 - k * (k - 1) * s
        half = v % 2 == 0
        c = (u - (1 if half else 0)) // 2
        phi, exp, qprimes = unit_group(v)
        row = dict(v=v, k=k, s=s, uncovered_nonzero_count=u, half_v_forced=half, uncovered_classes_besides_half_v=c,
                   factorization={str(p): e for p, e in factor(v).items()}, phi=phi, exponent_of_units=exp,
                   prime_orders_in_Q=qprimes, subgroup_counting={})
        for m in (2, 3, 4):
            if v % m == 0:
                zs, Zm, P = feasible_z(v, k, s, c, m)
                row["subgroup_counting"][str(m)] = dict(usable_classes_in_mZ=Zm, per_codeword_S_values=P,
                                                        feasible_uncovered_in_mZ=zs)
        if (v - 2) % (k * (k - 1)) == 0:
            row["BT_theorem_system"] = bt_system(v, k)
        out.append(row)
        print(json.dumps(row))
    with open(sys.argv[1] if len(sys.argv) > 1 else "/dev/stdout", "w") as fh:
        json.dump(out, fh, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
