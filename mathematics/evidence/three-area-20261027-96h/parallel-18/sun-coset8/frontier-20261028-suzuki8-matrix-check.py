#!/usr/bin/env python3
"""Exact GF(8) matrix check for the Suzuki root subgroup and normalizer.

The finite check is not a proof of the all-q maximal-subgroup classification.
"""
from collections import deque


def gf_mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 0b1011  # x^3+x+1
    return out


M = [[gf_mul(a, b) for b in range(8)] for a in range(8)]
INV = [0] + [next(b for b in range(1, 8) if M[a][b] == 1) for a in range(1, 8)]


def power(a, n):
    out = 1
    for _ in range(n):
        out = M[out][a]
    return out


def multiply(a, b):
    return tuple(
        M[a[4*i]][b[j]] ^ M[a[4*i+1]][b[4+j]] ^
        M[a[4*i+2]][b[8+j]] ^ M[a[4*i+3]][b[12+j]]
        for i in range(4) for j in range(4)
    )


def inverse(a):
    rows = [[a[4*i+j] for j in range(4)] + [int(i == j) for j in range(4)]
            for i in range(4)]
    for col in range(4):
        pivot = next((i for i in range(col, 4) if rows[i][col]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        rows[col], rows[pivot] = rows[pivot], rows[col]
        rows[col] = [M[INV[rows[col][col]]][v] for v in rows[col]]
        for i in range(4):
            if i != col:
                v = rows[i][col]
                rows[i] = [x ^ M[v][y] for x, y in zip(rows[i], rows[col])]
    return tuple(rows[i][4+j] for i in range(4) for j in range(4))


def root(a, b):
    return (1, 0, 0, 0,
            a, 1, 0, 0,
            b, power(a, 4), 1, 0,
            power(a, 6) ^ M[a][b] ^ power(b, 4), power(a, 5) ^ b, a, 1)


I = tuple(int(i == j) for i in range(4) for j in range(4))
C = tuple((power(2, (3, 2, 5, 4)[i]) if i == j else 0)
          for i in range(4) for j in range(4))
T = tuple(int(i + j == 3) for i in range(4) for j in range(4))
GENERATORS = (root(1, 0), root(0, 1), C, T)


def closure(gens, cap):
    seen = {I}
    queue = deque([I])
    while queue:
        x = queue.popleft()
        for g in gens:
            y = multiply(x, g)
            if y not in seen:
                seen.add(y)
                if len(seen) > cap:
                    raise RuntimeError("resource bound exceeded")
                queue.append(y)
    return seen


def main():
    U = frozenset(root(a, b) for a in range(8) for b in range(8))
    if len(U) != 64 or I not in U:
        raise SystemExit("FAIL root set cardinality")
    if any(multiply(x, y) not in U for x in U for y in U):
        raise SystemExit("FAIL root subgroup closure")
    B = closure(GENERATORS[:3], 1000)
    if not U <= B:
        raise SystemExit("FAIL root subgroup not in generated B")
    for g in GENERATORS[:3]:
        if {multiply(g, u) for u in U} != {multiply(u, g) for u in U}:
            raise SystemExit("FAIL B generator does not normalize U")
    G = closure(GENERATORS, 35000)
    if len(G) != 29120 or len(B) != 448:
        raise SystemExit(f"FAIL group sizes G={len(G)} B={len(B)}")
    inverses = [inverse(g) for g in GENERATORS]
    if any(multiply(g, inv) != I for g, inv in zip(GENERATORS, inverses)):
        raise SystemExit("FAIL generator inverse")
    conjugates = {U}
    queue = deque([U])
    while queue:
        subgroup = queue.popleft()
        for g, inv in zip(GENERATORS, inverses):
            v = frozenset(multiply(multiply(g, u), inv) for u in subgroup)
            if v not in conjugates:
                conjugates.add(v)
                if len(conjugates) > 100:
                    raise RuntimeError("conjugacy resource bound exceeded")
                queue.append(v)
    print("GF8_polynomial: x^3+x+1")
    print("root_subgroup_size:", len(U))
    print("generated_B_size:", len(B))
    print("generated_G_size:", len(G))
    print("root_conjugacy_orbit_size:", len(conjugates))
    print("normalizer_size_from_orbit:", len(G) // len(conjugates))
    if len(conjugates) != 65 or len(G) // len(conjugates) != len(B):
        raise SystemExit("FAIL conjugacy/normalizer size")
    print("PASS: exact Sz(8) model, Sylow root and normalizer cardinalities")


if __name__ == "__main__":
    main()
