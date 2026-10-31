#!/usr/bin/env python3
"""Explicit exact SR<=2 decompositions of two coordinate grid projections.

All state/Schur arithmetic is rational; amplitudes are Gaussian rationals
represented by pairs of Fractions. Each lifted ket is independently checked
by its sixteen 3x3 minors and the resulting projector sum by every entry.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import runpy


src = runpy.run_path(str(Path(__file__).with_name("frontier-20261028-grid-state-sr2-check.py")))
ZERO = (F(0), F(0))
ROOTS = ((1, 0), (0, 1), (-1, 0), (0, -1))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def scale(a, c):
    return (a[0] * c, a[1] * c)


def conj(a):
    return (a[0], -a[1])


def neg(a):
    return (-a[0], -a[1])


def vec(*terms):
    v = [ZERO] * 20
    for a, b, z in terms:
        v[5 * a + b] = add(v[5 * a + b], (F(z[0]), F(z[1])))
    return v


def inverse(m):
    n = len(m)
    a = [[F(m[i][j]) for j in range(n)] + [F(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        p = next(i for i in range(j, n) if a[i][j])
        a[j], a[p] = a[p], a[j]
        t = a[j][j]
        a[j] = [v / t for v in a[j]]
        for i in range(n):
            if i != j:
                t = a[i][j]
                a[i] = [x - t * y for x, y in zip(a[i], a[j])]
    return [row[n:] for row in a]


def principal_pivots(m):
    schur = [[F(x) for x in row] for row in m]
    labels = list(range(len(m)))
    selected = []
    while schur:
        p = next((j for j in range(len(schur)) if schur[j][j] > 0), None)
        if p is None:
            if any(x for row in schur for x in row):
                raise AssertionError("core is not PSD")
            break
        selected.append(labels[p])
        piv = schur[p][p]
        remaining = [j for j in range(len(schur)) if j != p]
        schur = [[schur[i][j] - schur[i][p] * schur[p][j] / piv for j in remaining]
                 for i in remaining]
        labels = [labels[j] for j in remaining]
    return selected


def rank_two(v, kept_b):
    rows = [[v[5 * a + b] for b in kept_b] for a in range(4)]
    for rr in combinations(range(4), 3):
        for cc in combinations(range(4), 3):
            a, b, c = rr
            x, y, z = cc
            first = mul(rows[a][x], add(mul(rows[b][y], rows[c][z]), neg(mul(rows[b][z], rows[c][y]))))
            second = mul(rows[a][y], add(mul(rows[b][x], rows[c][z]), neg(mul(rows[b][z], rows[c][x]))))
            third = mul(rows[a][z], add(mul(rows[b][x], rows[c][y]), neg(mul(rows[b][y], rows[c][x]))))
            if add(add(first, neg(second)), third) != ZERO:
                return False
    return True


def term_vectors(kind):
    out = []
    for k, z in enumerate(ROOTS):
        z2, z3 = ROOTS[(2 * k) % 4], ROOTS[(3 * k) % 4]
        if kind == "drop_B3_peel_A0":
            v = vec((1, 0, neg(z2)), (1, 1, z), (1, 2, (1, 0)),
                    (2, 0, neg(z3)), (2, 1, z2), (2, 2, z))
        else:
            v = vec((0, 1, z2), (1, 1, z), (2, 1, (1, 0)),
                    (0, 2, z3), (1, 2, z2), (2, 2, z))
        out.append((F(1, 4), v))
    extras = ([(2, 0, 2), (3, 4, 3), (3, 0, 3), (3, 2, 3)]
              if kind == "drop_B3_peel_A0"
              else [(0, 2, 2), (3, 3, 3), (2, 3, 3), (3, 2, 3)])
    out.extend((F(weight), vec((a, b, (1, 0)))) for a, b, weight in extras)
    return out


def describe(v):
    return [{"a": j // 5, "b_original": j % 5, "real": str(x[0]), "imag": str(x[1])}
            for j, x in enumerate(v) if x != ZERO]


def check(kind, rho):
    if kind == "drop_B3_peel_A0":
        kept_b = (0, 1, 2, 4)
        core = [5*a+b for a in (1, 2, 3) for b in kept_b]
        edge = [b for b in kept_b]
    else:
        kept_b = (0, 1, 2, 3)
        core = [5*a+b for a in range(4) for b in (1, 2, 3)]
        edge = [5*a for a in range(4)]
    keep = [5*a+b for a in range(4) for b in kept_b]
    C = [[F(rho[i][j]) for j in core] for i in core]
    J = principal_pivots(C)
    inv = inverse([[C[i][j] for j in J] for i in J])
    X = [[F(rho[i][j]) for j in edge] for i in core]
    # Y = X_J^T (C_JJ)^(-1): yields the peeled-side amplitude from v_J.
    Y = [[sum(X[J[k]][r] * inv[k][l] for k in range(len(J)))
          for l in range(len(J))] for r in range(len(edge))]
    terms = []
    for weight, product_v in term_vectors(kind):
        lifted = list(product_v)
        for r, pos in enumerate(edge):
            value = ZERO
            for l in range(len(J)):
                value = add(value, scale(product_v[core[J[l]]], Y[r][l]))
            lifted[pos] = value
        if not rank_two(lifted, kept_b):
            raise AssertionError("lifted vector has Schmidt rank >2")
        terms.append((weight, lifted))
    reconstructed = [[ZERO for _ in range(20)] for _ in range(20)]
    for weight, v in terms:
        for i in keep:
            for j in keep:
                reconstructed[i][j] = add(reconstructed[i][j], scale(mul(v[i], conj(v[j])), weight))
    residual = [[add((F(rho[i][j]), F(0)), neg(reconstructed[i][j])) for j in edge] for i in edge]
    if any(residual[i][j][1] for i in range(len(edge)) for j in range(len(edge))):
        raise AssertionError("non-real residual")
    r = [[residual[i][j][0] for j in range(len(edge))] for i in range(len(edge))]
    p = next((i for i in range(len(edge)) if r[i][i] > 0), None)
    if p is None:
        if any(x for row in r for x in row):
            raise AssertionError("invalid zero residual")
        residual_weight = F(0)
        product_residual = [ZERO] * 20
    else:
        residual_weight = 1 / r[p][p]
        product_residual = [ZERO] * 20
        for i, pos in enumerate(edge):
            product_residual[pos] = (r[i][p], F(0))
        if not rank_two(product_residual, kept_b):
            raise AssertionError("residual is not low rank")
        terms.append((residual_weight, product_residual))
    # Independent complete entrywise comparison, not only a Schur check.
    reconstructed = [[ZERO for _ in range(20)] for _ in range(20)]
    for weight, v in terms:
        for i in keep:
            for j in keep:
                reconstructed[i][j] = add(reconstructed[i][j], scale(mul(v[i], conj(v[j])), weight))
    mismatch = [(i,j) for i in keep for j in keep if reconstructed[i][j] != (F(rho[i][j]),F(0))]
    if mismatch:
        raise AssertionError({"case": kind, "entry_mismatches": mismatch})
    return {"case":kind, "kept_b_original":kept_b, "core_rank":len(J),
            "matrix_entries_checked":len(keep)**2, "entry_mismatches":len(mismatch),
            "terms":[{"weight":str(w), "nonzero_ket_entries":describe(v)} for w,v in terms]}


def main():
    rho = src["state"]()
    print(json.dumps({"cases":[check("drop_B3_peel_A0",rho), check("drop_B4_peel_B0",rho)]}, indent=2))


if __name__ == "__main__":
    main()
