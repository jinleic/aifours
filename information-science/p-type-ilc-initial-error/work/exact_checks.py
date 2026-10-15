"""Independent rational checks for the pure-P impulse-response identities."""
from fractions import Fraction as Q
from math import comb, factorial


def integrate_polynomial(coefficients, q):
    return [Q(0)] * q + [
        coefficient * Q(factorial(j), factorial(j + q))
        for j, coefficient in enumerate(coefficients)
    ]


def h_formula(n, q):
    if n == 0:
        return Q(1)
    return sum((Q((-1) ** k * comb(n - 1, k - 1), factorial(q * k))
                for k in range(1, n + 1)), Q(0))


def check_polynomial_recursion(q, horizon=10):
    # An impulse initial position a_0=1 followed by zero initial positions.
    # Direct physical relation y_i=a_i+J^q u_i, not the h-formula.
    u = [Q(0)]
    for i in range(horizon + 1):
        y = integrate_polynomial(u, q)
        y[0] += Q(i == 0)
        assert sum(y) == h_formula(i, q), (q, i)
        u += [Q(0)] * (len(y) - len(u))
        u = [uk - yk for uk, yk in zip(u, y)]


def certificates():
    checks = []
    for q in range(1, 6):
        check_polynomial_recursion(q)
        checks.append({"relative_degree": q, "horizon": 10, "identity": "pass"})
    witnesses = []
    for q in (1, 2):
        h = [h_formula(i, q) for i in range(129)]
        for n in (8, 32, 128):
            signs = [1 if v >= 0 else -1 for v in reversed(h[: n + 1])]
            actual = sum((h[n - j] * Q(sign, 20)
                          for j, sign in enumerate(signs)), Q(0))
            predicted = sum(map(abs, h[: n + 1]), Q(0)) / 20
            assert actual == predicted
            witnesses.append({
                "relative_degree": q, "horizon": n, "t_star": 1,
                "epsilon0": "1/20", "a_signs": signs,
                "output_numerator": str(actual.numerator),
                "output_denominator": str(actual.denominator),
                "output_float": float(actual),
                "amplification_float": float(20 * actual),
            })
    # Independent Laguerre recurrence versus the exact binomial impulse formula.
    lag_previous, lag_current = Q(1), Q(0)  # L_0(1), L_1(1)
    assert lag_current - lag_previous == h_formula(1, 1)
    for n in range(2, 30):
        lag_next = (Q(2 * n - 2) * lag_current - Q(n - 1) * lag_previous) / n
        assert lag_next - lag_current == h_formula(n, 1)
        lag_previous, lag_current = lag_current, lag_next
    return {"polynomial_checks": checks, "laguerre_checks": 29,
            "finite_exact_witnesses": witnesses}
