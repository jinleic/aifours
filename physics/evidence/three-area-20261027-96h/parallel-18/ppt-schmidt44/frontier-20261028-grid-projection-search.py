#!/usr/bin/env python3
"""Exact bounded sanity search in the published 4x5 grid-state range.

Reference: Krebs--Gachechiladze, arXiv:2509.07086v1, equation (11).
For each of the five coordinate projections from Bob dimension five to four,
seek a matrix of rank <=2 in the projected published range with psi00=1.
Such a matrix defeats the *inherited range-functional proof*, not necessarily
Schmidt-number-3 for the projected state. All arithmetic here is integer or
Fraction; the finite domain and exhaustiveness are reported explicitly.
"""
from fractions import Fraction
from itertools import combinations, product
import json


VALUES = (0, 1, -1)
VARNAMES = ("b", "c", "d", "e", "f", "g", "i", "h")


def published_range_matrix(t):
    b, c, d, e, f, g, i, h = t
    return [[1, b, c, 0, h],
            [d, 1, b, 0, 0],
            [e, -d, 1, f, 0],
            [g, 0, i, e, c]]


def det3(m, rows, cols):
    a, b, c = rows
    x, y, z = cols
    return (m[a][x] * (m[b][y] * m[c][z] - m[b][z] * m[c][y])
            - m[a][y] * (m[b][x] * m[c][z] - m[b][z] * m[c][x])
            + m[a][z] * (m[b][x] * m[c][y] - m[b][y] * m[c][x]))


def all_three_minors_zero(m):
    return all(det3(m, rs, cs) == 0
               for rs in combinations(range(4), 3)
               for cs in combinations(range(4), 3))


def independent_fraction_rank(m):
    a = [[Fraction(x) for x in row] for row in m]
    pivot = 0
    for column in range(4):
        row = next((j for j in range(pivot, 4) if a[j][column]), None)
        if row is None:
            continue
        a[pivot], a[row] = a[row], a[pivot]
        divisor = a[pivot][column]
        a[pivot] = [v / divisor for v in a[pivot]]
        for j in range(pivot + 1, 4):
            factor = a[j][column]
            a[j] = [v - factor * p for v, p in zip(a[j], a[pivot])]
        pivot += 1
        if pivot == 4:
            break
    return pivot


def main():
    result = {"reference": "https://arxiv.org/html/2509.07086v1, Eq. (11)",
              "a_fixed": 1, "other_variable_values": VALUES,
              "variables": VARNAMES, "cases": []}
    for removed in range(5):
        kept = [j for j in range(5) if j != removed]
        examined = 0
        found = None
        for t in product(VALUES, repeat=len(VARNAMES)):
            examined += 1
            full = published_range_matrix(t)
            projected = [[row[j] for j in kept] for row in full]
            if all_three_minors_zero(projected):
                rank = independent_fraction_rank(projected)
                if rank > 2:
                    raise AssertionError("minor and independent rank disagree")
                found = {"parameters": dict(zip(VARNAMES, t)),
                         "full_4x5": full, "projected_4x4": projected,
                         "fraction_gaussian_rank": rank,
                         "checked_3x3_minors": 16}
                break
        result["cases"].append({"removed_bob_column": removed,
                                "kept_columns": kept,
                                "assignments_examined": examined,
                                "witness": found})
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
