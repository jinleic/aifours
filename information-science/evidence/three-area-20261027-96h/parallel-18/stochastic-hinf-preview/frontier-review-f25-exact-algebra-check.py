#!/usr/bin/env python3
"""Independent exact formal-polynomial checks of f25; standard library only."""
from fractions import Fraction as F
from math import comb
import json


def clean(p):
    return {k: v for k, v in p.items() if v}


def add(*ps):
    z = {}
    for p in ps:
        for k, v in p.items():
            z[k] = z.get(k, F(0)) + v
    return clean(z)


def scale(p, c):
    return clean({k: v * F(c) for k, v in p.items()})


def mul(a, b):
    z = {}
    for x, vx in a.items():
        for y, vy in b.items():
            k = tuple(i + j for i, j in zip(x, y))
            z[k] = z.get(k, F(0)) + vx * vy
    return clean(z)


def power(a, n):
    out = {(0,) * len(next(iter(a))): F(1)}
    for _ in range(n):
        out = mul(out, a)
    return out


def deriv(p, axis):
    out = {}
    for exp, c in p.items():
        if exp[axis]:
            k = list(exp)
            n = k[axis]
            k[axis] -= 1
            out[tuple(k)] = c * n
    return clean(out)


def embed_m(p):
    return {(i[0], 0): a for i, a in p.items()}


def compose_1d(p, mpoly, gpoly):
    out = {}
    for (i, j), coefficient in p.items():
        out = add(out, scale(mul(power(mpoly, i), power(gpoly, j)), coefficient))
    return out


def qadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def qneg(x):
    return (-x[0], -x[1])


def qmul(x, y):
    return (x[0] * y[0] + 3 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def qdiv(x, y):
    den = y[0] * y[0] - 3 * y[1] * y[1]
    if den == 0:
        raise ZeroDivisionError("zero element of Q(sqrt(3))")
    z = qmul(x, (y[0], -y[1]))
    return (z[0] / den, z[1] / den)


def qs(x):
    return (F(x), F(0))


def main():
    one, m, g = {(0,): F(1)}, {(1,): F(1)}, {(0, 1): F(1)}
    # Derive geometric moments from M_(k+1)=m(1+m) M_k' + m M_k.
    moments = [one]
    for _ in range(4):
        moments.append(add(mul(mul(m, add(one, m)), deriv(moments[-1], 0)),
                           mul(m, moments[-1])))
    A, B, C = moments[2:5]
    expected_moments = [
        {(1,): F(1)}, {(1,): F(1), (2,): F(2)},
        {(1,): F(1), (2,): F(6), (3,): F(6)},
        {(1,): F(1), (2,): F(14), (3,): F(36), (4,): F(24)}
    ]
    if moments[1:] != expected_moments:
        raise RuntimeError("geometric moment recurrence mismatch")

    # Construct D=E[(g+I)^2], N=E[(g+I)^4] from binomial sums.
    D = {}
    N = {}
    for k in range(3):
        D = add(D, scale(mul(embed_m(moments[k]), power(g, 2-k)), comb(2, k)))
    for k in range(5):
        N = add(N, scale(mul(embed_m(moments[k]), power(g, 4-k)), comb(4, k)))
    P = scale(add(mul(deriv(N, 1), D), scale(mul(N, deriv(D, 1)), -1)), F(1, 2))
    target = {(0,5):F(1),(1,4):F(5),(1,3):F(2),(2,3):F(12),
              (3,2):F(12),(1,2):F(-2),(1,1):F(-1),(2,1):F(-8),
              (3,1):F(-12),(2,0):F(1),(3,0):F(2)}
    if P != target:
        raise RuntimeError("derivative polynomial differs")

    # Independent exact rational high-m decomposition.
    base = {(2,0):F(12),(1,0):F(12),(0,0):F(1)}
    remainder = add(N, scale(mul(base, D), -1))
    target_rem = {(1,1):F(2),(1,2):F(-6),(1,3):F(4),(0,2):F(-1),(0,4):F(1)}
    if remainder != target_rem:
        raise RuntimeError("high-m exact decomposition differs")

    # Clear denominator at g=2m/(1+4m).
    m1 = {(1,):F(1)}
    h = {(0,):F(1),(1,):F(4)}
    cleared = {}
    for (i,j), coefficient in P.items():
        cleared = add(cleared, scale(mul(mul(power(m1,i), power(scale(m1,2),j)),
                                          power(h,5-j)), coefficient))
    desired = [0,0,-1,-34,-352,-1472,-2944,-2816,-1024]
    got = [cleared.get((i,), F(0)) for i in range(len(desired))]
    if got != desired:
        raise RuntimeError("middle sign polynomial differs")

    # The s=m^(1/4) ansatz and value expansion are tested symbolically.
    s = {(1,): F(1)}
    s4 = power(s, 4)
    gs = {(1,):F(1),(2,):F(1,2),(3,):F(-5,8),(4,):F(-3,2)}
    w_series = {(2,):F(1),(3,):F(2),(4,):F(3,2),(5,):F(-3,4)}
    p_sub = compose_1d(P, s4, gs)
    d_sub, n_sub = compose_1d(D, s4, gs), compose_1d(N, s4, gs)
    value_residual = add(n_sub, scale(mul(d_sub, w_series), -2))
    if any(p_sub.get((i,), 0) for i in range(9)):
        raise RuntimeError("root series fails through degree eight")
    if any(value_residual.get((i,), 0) for i in range(8)):
        raise RuntimeError("value series fails through degree seven")

    # Exact high-privacy root correction in Q(sqrt(3)).
    root = (F(1,2), F(1,6))
    root2 = qmul(root, root)
    root3 = qmul(root2, root)
    f1 = qadd(qadd(qmul(qs(12),root3), qmul(qs(-8),root)), qs(1))
    f0prime = qadd(qmul(qs(24),root), qs(-12))
    root_correction = qneg(qdiv(f1, f0prime))
    high_value_coeff = qdiv(qmul(qmul(root, qadd(qs(1), qneg(root))),
                                 qadd(qs(1), qneg(qmul(qs(2),root)))), qs(2))
    if root_correction != (F(-1,12),F(0)) or high_value_coeff != (F(0),F(-1,36)):
        raise RuntimeError("Q(sqrt(3)) endpoint coefficient differs")

    print(json.dumps({
        "moment_recurrence_through_order_4": "PASS",
        "derivative_full_bivariate_identity": "PASS",
        "high_m_rational_decomposition": "PASS",
        "cleared_middle_sign_coefficients_ascending": [str(x) for x in got],
        "low_m_root_residual_zero_through_s8": True,
        "low_m_value_n_minus_2dW_zero_through_s7": True,
        "high_privacy_gamma_coefficient": "-1/12",
        "high_privacy_value_coefficient": "-sqrt(3)/36",
        "limits": "Formal exact polynomial/field checks only; not a proof of all-law uniqueness, optimizer branch, source import or stochastic privacy."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
