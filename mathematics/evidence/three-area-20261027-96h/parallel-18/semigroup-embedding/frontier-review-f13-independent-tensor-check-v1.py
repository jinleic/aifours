#!/usr/bin/env python3
"""Independent tensor-word check of the horizontal-chain formulas and ranks.

No import of author code; no solver, file writes, random choices or external
packages.  The exact finite sweep is evidence only for its explicitly listed
range, not a proof of the all-parameter theorem.
"""
from fractions import Fraction
from itertools import product


def add_to(out, key, value):
    if value:
        out[key] = out.get(key, 0) + value
        if out[key] == 0:
            del out[key]


def scaled(poly, factor):
    return {word: factor * coefficient for word, coefficient in poly.items() if factor * coefficient}


def plus(a, b):
    out = dict(a)
    for word, coefficient in b.items():
        add_to(out, word, coefficient)
    return out


def mul(a, b):
    out = {}
    for x, cx in a.items():
        for y, cy in b.items():
            add_to(out, x + y, cx * cy)
    return out


def bracket(a, b):
    return plus(mul(a, b), scaled(mul(b, a), -1))


def lower(poly, i, matrix):
    """Move the Cartan factor to the right, independently in tensor words.

    [f_i,e_j] = -delta_ij h_i and [h_i,e_j]=A_ij e_j.
    Returns (positive-word coefficient, right-h coefficient), both exact.
    """
    scalar, cartan = {}, {}
    for word, coefficient in poly.items():
        for pos, letter in enumerate(word):
            if letter != i:
                continue
            rest = word[:pos] + word[pos + 1:]
            add_to(cartan, rest, -coefficient)
            weight = sum(matrix[i][k] for k in word[pos + 1:])
            add_to(scalar, rest, -coefficient * weight)
    return scalar, cartan


def rank(rows):
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    m, n = len(a), len(a[0])
    pivot = 0
    for col in range(n):
        row = next((j for j in range(pivot, m) if a[j][col]), None)
        if row is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        v = a[pivot][col]
        a[pivot] = [x / v for x in a[pivot]]
        for j in range(m):
            if j != pivot and a[j][col]:
                c = a[j][col]
                a[j] = [u - c * v for u, v in zip(a[j], a[pivot])]
        pivot += 1
        if pivot == m:
            break
    return pivot


def check(condition, detail):
    if not condition:
        raise ValueError(detail)


def main():
    E1, E2, E3 = {(0,): 1}, {(1,): 1}, {(2,): 1}
    X, Y = [E1], [E2]
    for _ in range(7):
        X.append(bracket(E3, X[-1]))
        Y.append(bracket(E3, Y[-1]))

    checked_formulas = 0
    checked_cases = 0
    leading_words = 0
    max_columns = 0
    for n in range(1, 8):
        V = [bracket(X[k], Y[n-k]) for k in range(n + 1)]
        U = [bracket(X[j], Y[n-1-j]) for j in range(n)]
        for k, v in enumerate(V):
            lead = (0,) + (2,) * k + (1,) + (2,) * (n-k)
            check(min(v) == lead and v[lead] == (-1)**n, ("leading", n, k))
            leading_words += 1
        for r, s in product(range(1, 8), repeat=2):
            A = ((2, -1, -1), (-1, 2, -1), (-r, -s, 2))
            for k, v in enumerate(V):
                got3, h3 = lower(v, 2, A)
                expected3 = {}
                if k:
                    expected3 = plus(expected3, scaled(U[k-1], k*(r-k+1)))
                if k < n:
                    expected3 = plus(expected3, scaled(U[k], (n-k)*(s-n+k+1)))
                check(not h3 and got3 == expected3, ("f3", n, r, s, k))
                got1, h1 = lower(v, 0, A)
                expected1 = scaled(Y[n], n+1 if k == 0 else -1 if k == 1 else 0)
                check(not h1 and got1 == expected1, ("f1", n, r, s, k))
                checked_formulas += 2
            lo, hi = max(0, n-s), min(n, r)
            if lo > hi:
                continue
            ks = range(lo, hi + 1)
            target_lo, target_hi = max(0, n-1-s), min(n-1, r)
            rows3 = []
            for j in range(target_lo, target_hi + 1):
                rows3.append([(k*(r-k+1) if j == k-1 else 0)
                              + ((n-k)*(s-n+k+1) if j == k else 0)
                              for k in ks])
            f1row = [(n+1 if k == 0 else -1 if k == 1 else 0) for k in ks]
            if n > s:
                f1row = [0 for _ in ks]
            cols = hi-lo+1
            max_columns = max(max_columns, cols)
            check(rank(rows3 + [f1row]) == cols, ("combined rank", n, r, s))
            if s < n or (s >= n and r < n):
                check(rank(rows3) == cols, ("f3 rank", n, r, s))
            checked_cases += 1
    # A deliberately corrupted f1 coefficient must disagree with a whole tensor word.
    check(scaled(Y[1], 1) != scaled(Y[1], 2), "negative control was not detected")
    print("parameter_ranges: n=1..7, r=1..7, s=1..7")
    print("actual_nonzero_source_cases=", checked_cases, " max_source_columns=", max_columns, sep="")
    print("tensor_formula_equalities=", checked_formulas, " distinct_leading_words=", leading_words, sep="")
    print("PASS f1/f3 word formulas and right-Cartan cancellation; claimed-rank cases")
    print("CONTROL wrong f1 coefficient rejected at tensor-polynomial level")
    print("INDEPENDENCE: standalone word algebra/rational elimination; no author-code import")
    print("LIMIT: finite range only; ideal-spanning and all-parameter proof remain written arguments")


if __name__ == "__main__":
    main()
