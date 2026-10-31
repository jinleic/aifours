#!/usr/bin/env python3
"""Exact local checks for the v1 QOA cube audit; stdlib only.

q=7 checks every triple reduction of the paper's Example 4.9 by reducing
integer coefficients modulo Phi_7.  q=8 constructs a GF(8) Reed-Solomon
example, applies the additive-character Hadamard to the first address, and
checks every triple reduction with signed integer arithmetic.  No numerical
approximation is used.
"""
from collections import defaultdict
from itertools import combinations, product


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def index_tuple(row, positions):
    return tuple(row[i] for i in positions)


def source_seven():
    q = 7
    states = []
    for i, j, k, ell in product(range(q), repeat=4):
        row = (i, k, (i+j+k) % q, (i+2*j+4*k) % q,
               (ell+j) % q, (ell+2*j+5*k) % q, ell)
        states.append((row, i*ell % q))
    require(len({row for row, _ in states}) == q**4, "q7 duplicate ket")
    max_group = 0
    total_pairs = 0
    for kept in combinations(range(7), 3):
        traced = tuple(i for i in range(7) if i not in kept)
        groups = defaultdict(list)
        for row, exponent in states:
            groups[index_tuple(row, traced)].append((index_tuple(row, kept), exponent))
        coeffs = defaultdict(lambda: [0]*q)
        for group in groups.values():
            max_group = max(max_group, len(group))
            total_pairs += len(group)**2
            for (a, x), (b, y) in product(group, repeat=2):
                coeffs[(a, b)][(x-y) % q] += 1
        for (a, b), v in coeffs.items():
            # 1+z+...+z^6=0, and Phi_7 is z^6+...+1.
            reduced = tuple(v[i]-v[6] for i in range(6))
            target = (q, 0, 0, 0, 0, 0) if a == b else (0,)*6
            require(reduced == target, f"q7 reduction failed S={kept}, ({a},{b}): {reduced}")
        diagonal = {a for (a, b), v in coeffs.items() if a == b and v[0]-v[6] == q}
        require(len(diagonal) == q**3, f"q7 missing diagonals S={kept}")
    print(f"q7 source Example 4.9: 35/35 exact triple reductions = I_343; "
          f"{len(states)} distinct support kets, max trace-group={max_group}, "
          f"pair terms={total_pairs}; exact in Z[z]/(Phi_7), including 1/7 amplitude-square")


def gf8_mul(a, b):
    out = 0
    for _ in range(3):
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 0b1011  # x^3+x+1
    return out


def gf8_trace(a):
    a2 = gf8_mul(a, a)
    value = a ^ a2 ^ gf8_mul(a2, a2)
    require(value in (0, 1), f"GF(8) trace not in GF(2): {value}")
    return value


def gf8_eval(a, b, c, x):
    return a ^ gf8_mul(b, x) ^ gf8_mul(c, gf8_mul(x, x))


def original_eight():
    points = (0, 1, 2, 4, 3, 6, 7)  # 0,1,alpha,...,alpha^5
    require(len(set(points)) == 7, "duplicate evaluation point")
    words = [tuple(gf8_eval(a, b, c, x) for x in points)
             for a, b, c in product(range(8), repeat=3)]
    require(len(set(words)) == 512, "q8 duplicate codeword")
    for kept in combinations(range(7), 3):
        require(len({index_tuple(w, kept) for w in words}) == 512,
                f"q8 Vandermonde projection failed S={kept}")
    # First address a=0: four ordinary classical QLS(8), checked directly.
    addr = {(w[0], w[1], w[2]): w for w in words}
    require(len(addr) == 512, "q8 first three labels are not bijective")
    for s in range(3, 7):
        for b in range(8):
            require(len({addr[(0, b, c)][s] for c in range(8)}) == 8,
                    f"q8 classical row s={s}, b={b}")
        for c in range(8):
            require(len({addr[(0, b, c)][s] for b in range(8)}) == 8,
                    f"q8 classical column s={s}, c={c}")
    for s, t in combinations(range(3, 7), 2):
        require(len({(addr[(0, b, c)][s], addr[(0, b, c)][t])
                     for b, c in product(range(8), repeat=2)}) == 64,
                f"q8 classical orthogonality s,t={s,t}")
    print("q8 classical seed: 35/35 strength-three projections bijective; "
          "at a=0: four Latin squares and 6/6 orthogonal pairs")
    return words


def transformed_eight(words):
    q = 8
    states = []
    for w in words:
        for x in range(q):
            sign = -1 if gf8_trace(gf8_mul(x, w[0])) else 1
            states.append(((x,) + w[1:], sign))
    require(len({row for row, _ in states}) == q**4, "q8 transformed duplicate ket")
    max_group = 0
    total_pairs = 0
    for kept in combinations(range(7), 3):
        traced = tuple(i for i in range(7) if i not in kept)
        groups = defaultdict(list)
        for row, sign in states:
            groups[index_tuple(row, traced)].append((index_tuple(row, kept), sign))
        coeffs = defaultdict(int)
        for group in groups.values():
            max_group = max(max_group, len(group))
            total_pairs += len(group)**2
            for (a, x), (b, y) in product(group, repeat=2):
                coeffs[(a, b)] += x*y
        for (a, b), value in coeffs.items():
            target = q if a == b else 0
            require(value == target, f"q8 reduction failed S={kept}, ({a},{b}): {value}")
        diagonal = {a for (a, b), v in coeffs.items() if a == b and v == q}
        require(len(diagonal) == q**3, f"q8 missing diagonals S={kept}")
    # For the fixed x=0 plane, test every cell and every one-output reduction.
    cells = defaultdict(dict)
    for row, sign in states:
        if row[0] == 0:
            cells[(row[1], row[2])][row[3:]] = sign
    require(len(cells) == q**2 and all(len(v) == q for v in cells.values()),
            "q8 plane has missing cells or terms")
    for label, cell in cells.items():
        for s in range(4):
            groups = defaultdict(list)
            for ket, sign in cell.items():
                groups[ket[:s] + ket[s+1:]].append((ket[s], sign))
            coeffs = defaultdict(int)
            for group in groups.values():
                for (a, x), (b, y) in product(group, repeat=2):
                    coeffs[(a, b)] += x*y
            require(all(coeffs.get((a, b), 0) == (1 if a == b else 0)
                        for a, b in product(range(q), repeat=2)),
                    f"q8 cell={label}, subsystem={s}: marginal != I_8/8")
    labels = tuple(cells)
    for u, v in product(labels, repeat=2):
        overlap = sum(cells[u][ket]*cells[v].get(ket, 0) for ket in cells[u])
        require(overlap == (q if u == v else 0), f"q8 plane overlap {u},{v}")
    print(f"q8 transformed: 35/35 exact triple reductions = I_512; "
          f"{len(states)} distinct support kets, max trace-group={max_group}, "
          f"pair terms={total_pairs}; exact signed integers including 1/8 amplitude-square")
    print("q8 fixed-x=0 plane: 64/64 cells mutually orthonormal; "
          "256/256 one-output marginals equal I_8/8 (Schmidt rank 8)")


if __name__ == '__main__':
    source_seven()
    transformed_eight(original_eight())
