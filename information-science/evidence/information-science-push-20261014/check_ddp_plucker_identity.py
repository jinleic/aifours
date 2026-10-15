"""Independent exact random-instance check of DDP Plücker linearization.

This reimplements the identities without SymPy or the worker's modules: exact
Fractions, random rational plants/gains/frequencies, direct transfer evaluation.
It checks instances, not the universal theorem.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
from itertools import combinations
import json
from pathlib import Path
import random


def determinant(matrix):
    rows = [row[:] for row in matrix]
    size = len(rows)
    value = Fraction(1)
    for column in range(size):
        pivot = next((r for r in range(column, size) if rows[r][column] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            value = -value
        value *= rows[column][column]
        for row in range(column + 1, size):
            factor = rows[row][column] / rows[column][column]
            if factor:
                for k in range(column, size):
                    rows[row][k] -= factor * rows[column][k]
    return value


def solve(matrix, rhs):
    size = len(matrix)
    augmented = [matrix[r][:] + rhs[r][:] for r in range(size)]
    width = len(rhs[0])
    for column in range(size):
        pivot = next(r for r in range(column, size) if augmented[r][column] != 0)
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [x / scale for x in augmented[column]]
        for row in range(size):
            if row != column and augmented[row][column]:
                factor = augmented[row][column]
                augmented[row] = [x - factor * y for x, y in zip(augmented[row], augmented[column])]
    return [row[size:size + width] for row in augmented]


def multiply(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction()) for j in range(len(b[0]))]
            for i in range(len(a))]


def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def random_matrix(rng, rows, columns, scale=3):
    return [[Fraction(rng.randint(-scale, scale), rng.randint(1, 3)) for _ in range(columns)]
            for _ in range(rows)]


def identity(size):
    return [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]


def zeros(rows, columns):
    return [[Fraction(0)] * columns for _ in range(rows)]


def block(rows):
    return [sum((part[i] for part in row), []) for row in rows for i in range(len(row[0]))]


def plucker(gain, p, m):
    graph = identity(p) + [row[:] for row in gain]
    subsets = list(combinations(range(p + m), p))
    return subsets, [determinant([graph[i] for i in subset]) for subset in subsets]


def check_instance(rng, n, m, p, q, r):
    A, B, E = random_matrix(rng, n, n), random_matrix(rng, n, m), random_matrix(rng, n, q)
    C1, D1 = random_matrix(rng, p, n), random_matrix(rng, p, q)
    C2, D2, D22 = random_matrix(rng, r, n), random_matrix(rng, r, m), random_matrix(rng, r, q)
    K = random_matrix(rng, m, p)
    subsets, delta = plucker(K, p, m)
    lookup = dict(zip(subsets, delta))
    for i in range(m):
        for j in range(p):
            replaced = tuple(sorted(set(range(p)) - {j} | {p + i}))
            if (-1) ** (p - 1 - j) * lookup[replaced] != K[i][j]:
                raise AssertionError("Inverse chart sign or coordinate failed")
    M = add(A, multiply(multiply(B, K), C1))
    G = add(E, multiply(multiply(B, K), D1))
    F = add(C2, multiply(multiply(D2, K), C1))
    J = add(D22, multiply(multiply(D2, K), D1))
    Z = block([[zeros(n, p), [[-x for x in row] for row in B]], [identity(p), zeros(p, m)]])
    for _ in range(3):
        s = Fraction(rng.randint(-20, 20), rng.randint(1, 7))
        pencil = [[(s if i == j else Fraction(0)) - M[i][j] for j in range(n)] for i in range(n)]
        characteristic = determinant(pencil)
        if characteristic == 0:
            continue
        X = [[(s if i == j else Fraction(0)) - A[i][j] for j in range(n)] for i in range(n)]
        X += [[-x for x in row] for row in C1]
        linear_characteristic = sum((determinant([X[row] + [Z[row][k] for k in subset]
                                                  for row in range(n + p)]) * value
                                     for subset, value in zip(subsets, delta)), Fraction())
        if linear_characteristic != characteristic:
            raise AssertionError("Characteristic-polynomial linearization failed")
        transfer = add(J, multiply(F, solve(pencil, G)))
        for alpha in range(r):
            for beta in range(q):
                X_alpha = X + [C2[alpha][:]]
                Z_alpha = Z + [[Fraction(0)] * p + D2[alpha][:]]
                v = [-E[i][beta] for i in range(n)] + [-D1[i][beta] for i in range(p)] + [D22[alpha][beta]]
                bordered = sum((determinant([X_alpha[row] + [Z_alpha[row][k] for k in subset] + [v[row]]
                                             for row in range(n + p + 1)]) * value
                                for subset, value in zip(subsets, delta)), Fraction())
                if bordered != characteristic * transfer[alpha][beta]:
                    raise AssertionError("Bordered transfer-numerator linearization failed")
    return {"n": n, "m": m, "p": p, "q": q, "r": r, "coordinates": len(subsets)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(20261014)
    shapes = [(1, 1, 1, 1, 1), (2, 2, 2, 1, 1), (3, 2, 2, 2, 2), (3, 3, 2, 1, 2),
              (3, 2, 3, 2, 1), (4, 3, 3, 2, 2), (2, 1, 3, 2, 3), (4, 2, 2, 3, 2)]
    checked = [check_instance(rng, *shape) for shape in shapes for _ in range(4)]
    report = {"scope": "independent exact random instances of Theorem A identities; not a universal proof",
              "seed": 20261014, "instances": len(checked), "shapes": shapes,
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "verified": True}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
