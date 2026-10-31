#!/usr/bin/env python3
"""Exact bounded search for SR<=2 spanning the projected 4x5 source range.

Rows are tested by integer 3x3 minors, and vector-space independence by
Fraction row elimination. A full span is a certificate of range-criterion
failure for the specific reported local projection, not of state SN<=2.
"""
from fractions import Fraction
from itertools import combinations, product
import json


VALUES = (0, 1, -1)
NAMES = ("a", "b", "c", "d", "e", "f", "g", "i", "h")
NORMALS = (
    (1, 0, 0, 0, 0), (0, 1, 0, 0, 0), (0, 0, 1, 0, 0),
    (0, 0, 0, 1, 0), (0, 0, 0, 0, 1),
    (1, 1, 1, 1, 1), (1, 0, 0, 1, 1), (0, 0, 0, 1, 1),
    (1, 2, 3, 4, 5), (0, 1, 0, 2, -1),
)


def matrix(t):
    a, b, c, d, e, f, g, i, h = t
    return [[a, b, c, 0, h], [d, a, b, 0, 0],
            [e, -d, a, f, 0], [g, 0, i, e, c]]


def project(m, normal):
    pivot = next(i for i, val in enumerate(normal) if val)
    keep = [j for j in range(5) if j != pivot]
    return [[row[j] * normal[pivot] - row[pivot] * normal[j]
             for j in keep] for row in m]


def det3(m, r, c):
    a, b, d = r
    x, y, z = c
    return (m[a][x] * (m[b][y] * m[d][z] - m[b][z] * m[d][y])
            - m[a][y] * (m[b][x] * m[d][z] - m[b][z] * m[d][x])
            + m[a][z] * (m[b][x] * m[d][y] - m[b][y] * m[d][x]))


def sr2(m):
    return all(det3(m, r, c) == 0 for r in combinations(range(4), 3)
               for c in combinations(range(4), 3))


class LinearSpan:
    def __init__(self):
        self.basis = {}

    def add(self, values):
        v = [Fraction(x) for x in values]
        for p, b in sorted(self.basis.items()):
            if v[p]:
                f = v[p]
                v = [x - f * y for x, y in zip(v, b)]
        p = next((j for j, x in enumerate(v) if x), None)
        if p is None:
            return False
        f = v[p]
        self.basis[p] = [x / f for x in v]
        return True


def flatten(m):
    return [x for row in m for x in row]


def main():
    result = {"source": "https://arxiv.org/html/2509.07086v1 Eq. (11)",
              "search_domain": VALUES, "variables": NAMES, "cases": []}
    for normal in NORMALS:
        ambient = LinearSpan()
        for j in range(len(NAMES)):
            t = [0] * len(NAMES)
            t[j] = 1
            ambient.add(flatten(project(matrix(t), normal)))
        target = len(ambient.basis)
        lowrank = LinearSpan()
        basis_tuples = []
        tested = hits = 0
        for t in product(VALUES, repeat=len(NAMES)):
            tested += 1
            projected = project(matrix(t), normal)
            if sr2(projected):
                hits += 1
                if lowrank.add(flatten(projected)):
                    basis_tuples.append(t)
                if len(lowrank.basis) == target:
                    break
        result["cases"].append({"annihilator": normal,
                                "range_dimension": target,
                                "sr2_span_dimension": len(lowrank.basis),
                                "assignments_examined": tested,
                                "sr2_hits_examined": hits,
                                "basis_tuples": basis_tuples})
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
