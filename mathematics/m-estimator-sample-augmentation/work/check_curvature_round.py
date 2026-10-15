#!/usr/bin/env python3
"""Finite exact checks for the focused nested-design round.
Run: python3 work/check_curvature_round.py
The asymptotic theorem is proved in proof.md, not by this finite grid.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def positive(x):
    return max(Q(0), x)


def geometry(a, b, t, v):
    return (2*positive(a-t)+2*positive(-a-t)
            +2*positive(b+v-t)+2*positive(-b+v-t)
            +(positive(t)+positive(t-v))/2)


def huber(x):
    return x*x/2 if abs(x) <= 1 else abs(x)-Q(1, 2)


def matrix(rows, weights):
    return tuple(tuple(sum(w*x[i]*x[j] for x, w in zip(rows, weights))
                       for j in range(2)) for i in range(2))


def inverse(a):
    det = a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert det > 0
    return ((a[1][1]/det, -a[0][1]/det), (-a[1][0]/det, a[0][0]/det))


def quadratic(a, x):
    return sum(x[i]*a[i][j]*x[j] for i in range(2) for j in range(2))


def apply(a, x):
    return tuple(sum(a[i][j]*x[j] for j in range(2)) for i in range(2))


def subtract(a, b, scale=Q(1)):
    return tuple(tuple(a[i][j]-scale*b[i][j] for j in range(2)) for i in range(2))


def psd(a):
    return (a[0][0] >= 0 and a[1][1] >= 0
            and a[0][0]*a[1][1]-a[0][1]*a[1][0] >= 0)


def main():
    scale_profiles = []
    for exponent in (1, 4, 16, 64):
        r = Q(1, 2**exponent)
        base = geometry(r, r, r, Q(0))
        plus = geometry(r, r, r, Q(1))-base
        minus = geometry(r, r, r, Q(-1))-base
        assert base == r and plus == 4-Q(9, 2)*r and minus == Q(1, 2)
        t, v = r, r-1
        assert geometry(r, Q(1), t, v) == (r+1)/2
        scale_profiles.append({"strong_scale_ratio": str(r),
                               "old_penalty_at_v_plus_one": str(plus),
                               "old_penalty_at_v_minus_one": str(minus),
                               "isolated_intermediate_prefix_optimal_v": str(v)})
    lipschitz_checks = 0
    old = [(Q(1), Q(1), Q(-1)), (Q(2), Q(-1, 2), Q(0)),
           (Q(-4), Q(0), Q(1))]
    for loss, exponent, z, v in product((abs, huber), (1, 4, 16, 64),
                                       map(Q, (-2, -1, 0, 1, 2)), map(Q, (-1, 0, 1))):
        scale = 2**exponent
        actual = sum(loss(e-a*z/scale-b*v)-loss(e-b*v) for a, b, e in old)
        bound = abs(z)*sum(abs(a) for a, _, _ in old)/scale
        assert abs(actual) <= bound
        lipschitz_checks += 1
    matrix_checks = slope_checks = norm_checks = trace_checks = 0
    for a, b in product(map(Q, (-2, -1, 0, 1, 2)), repeat=2):
        rows = [(Q(1), Q(0)), (Q(0), Q(1)), (a, b)]
        s = matrix(rows, [Q(1)]*3)
        si = inverse(s)
        assert sum(quadratic(si, x) for x in rows) == 2
        doubled = tuple(tuple(2*entry for entry in row) for row in s)
        doubled_inv = inverse(doubled)
        assert sum(quadratic(doubled_inv, x) for x in rows*2) == 2
        trace_checks += 2
        for weights in product(map(Q, (1, 2, 3)), repeat=3):
            h = matrix(rows, weights)
            hi = inverse(h)
            assert psd(subtract(h, s))
            assert psd(subtract(s, h, Q(1, 3)))
            assert psd(subtract(hi, si, Q(1, 3)))
            matrix_checks += 1
            for x, w in zip(rows, weights):
                assert w*quadratic(hi, x) >= quadratic(si, x)/3
                slope_checks += 1
            for d in product(map(Q, (-2, -1, 0, 1, 2)), repeat=2):
                z = apply(h, d)
                assert quadratic(s, d) <= quadratic(si, z)
                norm_checks += 1
    persistent = []
    for n in (2, 4, 16, 256):
        s = ((Q(1), Q(0)), (Q(0), Q(n-1)))
        leverage = quadratic(inverse(s), (Q(1), Q(0)))
        assert leverage == 1
        persistent.append({"n": n, "first_row_leverage": str(leverage),
                           "uniform_slope_lower_bound_m1_M3": str(leverage/3)})
    result = {"verdict": "PASS", "scope": "finite exact arithmetic, not an asymptotic proof",
              "scale_profiles": scale_profiles,
              "lipschitz_retained_row_checks": lipschitz_checks,
              "hessian_comparison_checks": matrix_checks,
              "own_row_influence_checks": slope_checks,
              "normalized_gradient_checks": norm_checks,
              "original_and_replicated_trace_checks": trace_checks,
              "persistent_fixed_row_example": persistent,
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'evidence/curvature-exact-checks.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
