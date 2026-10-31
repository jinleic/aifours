#!/usr/bin/env python3
"""Exact checks of a 4x5 grid state and five coordinate compressions.

State, partial transposes, and Schur pivots use Fraction. The two explicit
four-phase separable-core identities use Gaussian-integer pair arithmetic
with all denominators cleared. Nothing is inferred from a floating spectrum.
"""
from fractions import Fraction
import json


def ket(*terms):
    v = [0] * 20
    for row, col, coefficient in terms:
        v[5 * row + col] += coefficient
    return v


def add_outer(rho, weight, v):
    for i, vi in enumerate(v):
        if vi:
            for j, vj in enumerate(v):
                if vj:
                    rho[i][j] += weight * vi * vj


def state():
    rho = [[0] * 20 for _ in range(20)]
    terms = [
        (1, ket((0, 0, 1), (1, 1, 1), (2, 2, 1))),
        (1, ket((0, 1, 1), (1, 2, 1))),
        (1, ket((1, 0, 1), (2, 1, -1))),
        (3, ket((0, 2, 1), (3, 4, 1))),
        (3, ket((2, 0, 1), (3, 3, 1))),
        (3, ket((2, 3, 1))), (3, ket((3, 0, 1))),
        (3, ket((3, 2, 1))), (3, ket((0, 4, 1))),
    ]
    for weight, v in terms:
        add_outer(rho, weight, v)
    return rho


def submatrix(m, keep):
    return [[m[i][j] for j in keep] for i in keep]


def partial_transpose(m, dim_a, dim_b):
    out = [[0] * (dim_a * dim_b) for _ in range(dim_a * dim_b)]
    for a in range(dim_a):
        for b in range(dim_b):
            for c in range(dim_a):
                for d in range(dim_b):
                    out[a * dim_b + d][c * dim_b + b] = m[a * dim_b + b][c * dim_b + d]
    return out


def exact_psd_pivots(m):
    a = [[Fraction(x) for x in row] for row in m]
    pivots = []
    while a:
        if any(a[i][i] < 0 for i in range(len(a))):
            raise AssertionError("negative Schur diagonal: not PSD")
        p = next((i for i in range(len(a)) if a[i][i] > 0), None)
        if p is None:
            if any(v != 0 for row in a for v in row):
                raise AssertionError("zero diagonal with nonzero Schur block")
            break
        piv = a[p][p]
        pivots.append(piv)
        rem = [i for i in range(len(a)) if i != p]
        a = [[a[i][j] - a[i][p] * a[p][j] / piv for j in rem] for i in rem]
    return [str(x) for x in pivots]


def zadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def zmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def zneg(a):
    return (-a[0], -a[1])


def gvec(*terms):
    out = [(0, 0)] * 20
    for row, col, val in terms:
        idx = 5 * row + col
        out[idx] = zadd(out[idx], val)
    return out


def four_phase_sum(vectors):
    out = [[(0, 0) for _ in range(20)] for _ in range(20)]
    for v in vectors:
        for i, vi in enumerate(v):
            for j, vj in enumerate(v):
                out[i][j] = zadd(out[i][j], zmul(vi, (vj[0], -vj[1])))
    return out


def check_core(rho, removed_bob, removed_alice, kind):
    roots = ((1, 0), (0, 1), (-1, 0), (0, -1))
    vectors = []
    for k, z in enumerate(roots):
        z2 = roots[(2 * k) % 4]
        z3 = roots[(3 * k) % 4]
        if kind == "remove_bob3_alice0":
            # (|1>+z|2>) tensor (-z^2|0>+z|1>+|2>).
            vectors.append(gvec((1, 0, zneg(z2)), (1, 1, z), (1, 2, (1, 0)),
                                (2, 0, zneg(z3)), (2, 1, z2), (2, 2, z)))
        else:
            # (z^2|0>+z|1>+|2>) tensor (|1>+z|2>).
            vectors.append(gvec((0, 1, z2), (1, 1, z), (2, 1, (1, 0)),
                                (0, 2, z3), (1, 2, z2), (2, 2, z)))
    rhs = four_phase_sum(vectors)
    extra = ([(2, 0, 8), (3, 4, 12), (3, 0, 12), (3, 2, 12)]
             if kind == "remove_bob3_alice0"
             else [(0, 2, 8), (3, 3, 12), (2, 3, 12), (3, 2, 12)])
    for a, b, weight in extra:
        j = 5 * a + b
        rhs[j][j] = zadd(rhs[j][j], (weight, 0))
    mismatch = []
    for i in range(20):
        ai, bi = divmod(i, 5)
        for j in range(20):
            aj, bj = divmod(j, 5)
            included = (bi != removed_bob and bj != removed_bob
                        and ai != removed_alice and aj != removed_alice
                        and (kind != "remove_bob4_bob0" or (bi != 0 and bj != 0)))
            expected = (4 * rho[i][j], 0) if included else (0, 0)
            if rhs[i][j] != expected:
                mismatch.append((i, j, expected, rhs[i][j]))
    if mismatch:
        raise AssertionError({"case": kind, "mismatches": mismatch})
    return {"case": kind, "matrix_entries_checked": 400,
            "identity": "4*core = sum of 4 product projectors + stated 4*residual", "mismatches": 0}


def main():
    rho = state()
    out = {"unnormalized_trace": sum(rho[i][i] for i in range(20)),
           "source_state_psd_pivots": exact_psd_pivots(rho),
           "source_state_partial_transpose_psd_pivots": exact_psd_pivots(partial_transpose(rho, 4, 5)),
           "coordinate_projections": []}
    for removed in range(5):
        keep = [5 * a + b for a in range(4) for b in range(5) if b != removed]
        projected = submatrix(rho, keep)
        out["coordinate_projections"].append({
            "removed_bob_column": removed,
            "trace": sum(projected[i][i] for i in range(16)),
            "psd_pivots": exact_psd_pivots(projected),
            "partial_transpose_psd_pivots": exact_psd_pivots(partial_transpose(projected, 4, 4))})
    out["separable_core_identities"] = [
        check_core(rho, 3, 0, "remove_bob3_alice0"),
        check_core(rho, 4, None, "remove_bob4_bob0")]
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
