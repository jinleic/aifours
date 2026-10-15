"""CRW (2009), Eq. (29), evaluated as the rational number pi**2 * R**2.

The arguments are (v1, v2, v3); R = <v3 || Y_v2 || v1>.
The Bohr measure has mass 16*pi**2/3, not the standard S4 area.
"""
from fractions import Fraction
from math import factorial, prod


def dimension(v):
    return (v + 1) * (v + 2) * (2 * v + 3) // 6


def admissible(v1, v2, v3):
    total = v1 + v2 + v3
    return total % 2 == 0 and 2 * max(v1, v2, v3) <= total


def square_pi(v1, v2, v3):
    """Nonnegative square in the paper's positive reduced-element convention."""
    if any(type(v) is not int or v < 0 for v in (v1, v2, v3)):
        raise ValueError("seniorities must be nonnegative integers")
    if not admissible(v1, v2, v3):
        return Fraction(0)
    s = (v1 + v2 + v3) // 2
    j = (s - v1, s - v2, s - v3)
    return (
        Fraction(factorial(s + 1) ** 2, prod(factorial(k) ** 2 for k in j))
        * Fraction((2 * v1 + 3) * (2 * v2 + 3), 16 * (v3 + 1) * (v3 + 2))
        * Fraction((2 * s + 4) * prod(factorial(2 * k + 1) for k in j), factorial(2 * s + 3))
    )
