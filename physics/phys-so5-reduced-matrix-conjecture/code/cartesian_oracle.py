"""Independent rational S4 harmonic bases and triple-overlap traces.

No Gegenbauer polynomial, Rogers coefficient, or CRW formula is used here.
The basis is unnormalised; norms cancel algebraically in the trace.
"""
from fractions import Fraction as Q
from functools import cache
from itertools import combinations_with_replacement, product
from math import prod

D = 5
ZERO = (0,) * D


def compositions(n, d=D):
    if d == 1:
        yield (n,)
    else:
        for first in range(n + 1):
            for rest in compositions(n - first, d - 1):
                yield (first,) + rest


def add_scaled(p, q, scale):
    result = dict(p)
    for e, value in q.items():
        result[e] = result.get(e, Q(0)) + scale * value
        if not result[e]:
            del result[e]
    return result


def multiply(p, q):
    result = {}
    for e, a in p.items():
        for f, b in q.items():
            exponent = tuple(x + y for x, y in zip(e, f))
            result[exponent] = result.get(exponent, Q(0)) + a * b
    return {e: a for e, a in result.items() if a}


def laplacian(p):
    result = {}
    for e, a in p.items():
        for axis, power in enumerate(e):
            if power >= 2:
                f = list(e)
                f[axis] -= 2
                f = tuple(f)
                result[f] = result.get(f, Q(0)) + a * power * (power - 1)
    return {e: a for e, a in result.items() if a}


@cache
def moment(e):
    """Uniform probability measure on S4, by Gaussian radial factorisation."""
    if any(k % 2 for k in e):
        return Q(0)
    half_degree = sum(e) // 2
    numerator = prod(prod(range(1, k, 2)) for k in e)
    denominator = prod(D + 2 * j for j in range(half_degree))
    return Q(numerator, denominator)


def inner(p, q):
    total = Q(0)
    for e, a in p.items():
        for f, b in q.items():
            m = moment(tuple(x + y for x, y in zip(e, f)))
            if m:
                total += a * b * m
    return total


def harmonic_basis(n):
    """Exact projection and Gram--Schmidt, deliberately limited to n <= 3."""
    if not 0 <= n <= 3:
        raise ValueError("this independent finite oracle covers degrees 0..3")
    r_squared = {tuple(2 if j == i else 0 for j in range(D)): Q(1) for i in range(D)}
    basis = []
    for e in compositions(n):
        p = {e: Q(1)}
        if n >= 2:
            p = add_scaled(p, multiply(r_squared, laplacian(p)), -Q(1, 2 * (D + 2 * n - 4)))
        assert not laplacian(p)
        for h, norm in basis:
            p = add_scaled(p, h, -inner(p, h) / norm)
        norm = inner(p, p)
        assert norm >= 0
        if norm:
            assert not laplacian(p)
            assert all(inner(p, h) == 0 for h, _ in basis)
            basis.append((p, norm))
    return basis


def compute():
    bases = [harmonic_basis(n) for n in range(4)]
    dimensions = [len(b) for b in bases]
    assert dimensions == [1, 5, 14, 30]
    traces = {}
    overlap_count = 0
    for degrees in combinations_with_replacement(range(4), 3):
        total = Q(0)
        for h1, norm1 in bases[degrees[0]]:
            for h2, norm2 in bases[degrees[1]]:
                pair = multiply(h1, h2)
                for h3, norm3 in bases[degrees[2]]:
                    overlap = inner(pair, h3)
                    total += overlap * overlap / (norm1 * norm2 * norm3)
                    overlap_count += 1
        traces[degrees] = total
    values = {}
    for triple in product(range(4), repeat=3):
        values[triple] = Q(3, 16 * dimensions[triple[2]]) * traces[tuple(sorted(triple))]
    return dimensions, overlap_count, values
