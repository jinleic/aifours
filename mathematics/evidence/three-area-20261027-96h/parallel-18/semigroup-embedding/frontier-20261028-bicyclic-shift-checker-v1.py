#!/usr/bin/env python3
"""Bounded exact checks for bicyclic multiplication and its shifted-tail host.

The infinite proof is separate. Finite ranges generate checks, not a finite
semigroup or evidence that bounded checking alone establishes a theorem.
"""
from itertools import product


def multiply(s, t):
    i, j = s
    k, ell = t
    return (i + max(k - j, 0), ell + max(j - k, 0))


def q(s):
    return s[0] - s[1]


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def main():
    # This is a finite check range; products may leave the range and are not truncated.
    words = list(product(range(5), repeat=2))
    shifts = range(-3, 4)
    unit = (0, 0)
    require(all(multiply(unit, s) == s == multiply(s, unit) for s in words), "unit")
    require(all(multiply(multiply(a, b), c) == multiply(a, multiply(b, c))
                for a, b, c in product(words, repeat=3)), "associativity")
    require(all(multiply(multiply(s, (s[1], s[0])), s) == s for s in words), "inverse")
    require(all(q(multiply(s, t)) == q(s) + q(t) for s, t in product(words, repeat=2)),
            "group quotient homomorphism")
    require(all((q(s) == 0) == (multiply(s, s) == s) for s in words), "q purity")

    # A_k={z in Z:z>=k}; intersection is max, integer translation adds the shift.
    def letter(u, s):
        return u + s[0]

    require(all(max(letter(u, s), letter(u + q(s), t)) == letter(u, multiply(s, t))
                for u, s, t in product(shifts, words, words)), "canonical relation")
    require(len({(letter(0, s), q(s)) for s in words}) == len(words), "host injectivity")
    require(len({letter(0, (n, n)) for n in range(5)}) == 5, "idempotent separation")
    p, qgen = (0, 1), (1, 0)
    require(multiply(p, qgen) == unit, "pq identity")
    require(multiply(qgen, p) == (1, 1) != unit, "qp distinct idempotent")

    # Wrong shift direction must be caught by the canonical relation.
    wrong_failures = sum(max(letter(u, s), letter(u - q(s), t))
                         != letter(u, multiply(s, t)) for u, s, t in product(shifts, words, words))
    require(wrong_failures > 0, "negative shift-direction control")
    print("bounded_source_labels=", len(words), " shifts=", len(shifts), sep="")
    print("PASS exact unit, associativity, inverse, quotient purity, canonical relations, host injection")
    print("PASS five distinct idempotent tails; p*q=1 and q*p=(1,1)!=1")
    print("CONTROL wrong-shift-direction mismatches=", wrong_failures, sep="")
    print("SCOPE: bounded integer-label checks only; infinite proof must be read separately")


if __name__ == "__main__":
    main()
