#!/usr/bin/env python3
"""Small exact arithmetic research checks; not the acceptance verifier.

No search over completion orders or code candidates is performed.
The all-order arguments are in proof.md, not inferred from these samples.
"""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
import json


PAIRS = ([(0, j) for j in (0, 1, 7, 13, 14)]
         + [(i, j) for i in (3, 8) for j in (0, 2, 4, 6)]
         + [(11, j) for j in (0, 1, 2)])


def word(pair):
    i, j = pair
    return "a" * i + "b" + "a" * j


def main():
    assert len(PAIRS) == len(set(PAIRS)) == 16
    words = {word(pair) for pair in PAIRS}
    assert max(map(len, words)) == 15

    dl = sorted({abs(i - k) for i, _ in PAIRS for k, _ in PAIRS if i != k})
    d0 = sorted({abs(j - ell) for i, j in PAIRS for k, ell in PAIRS
                 if i == k and j != ell})
    assert dl == [3, 5, 8, 11]
    assert d0 == [1, 2, 4, 6, 7, 12, 13, 14]

    # Concrete gcd computations only. The uniform argument is in proof.md.
    # These are arithmetic spot checks, not searches for finite completions.
    gcd_samples = []
    for multiplier in (1, 2, 7, 9, 13, 91):
        n = 1320 * multiplier
        source_gcds = sorted({gcd(d, n) for d in dl})
        target_gcds = sorted({gcd(d, n) for d in d0})
        assert set(source_gcds).isdisjoint(target_gcds)
        gcd_samples.append({"n": n, "source_gcds": source_gcds,
                            "target_gcds": target_gcds})

    # Ordinary two-word decoding collisions after the stated scalings.
    examples = [
        ("left_2", 2, 1, [(0, 1), (3, 0), (0, 7), (0, 0)]),
        ("right_2", 1, 2, [(3, 4), (0, 0), (3, 0), (8, 0)]),
        ("right_3", 1, 3, [(0, 1), (0, 0), (0, 0), (3, 0)]),
        ("right_5", 1, 5, [(0, 1), (3, 0), (0, 0), (8, 0)]),
        ("right_11", 1, 11, [(0, 1), (0, 0), (0, 0), (11, 0)]),
    ]
    identities = []
    for name, p, q, pairs in examples:
        assert all(pair in PAIRS for pair in pairs)
        transformed = [word((p * i, q * j)) for i, j in pairs]
        assert transformed[0] + transformed[1] == transformed[2] + transformed[3]
        assert transformed[:2] != transformed[2:]
        identities.append({"name": name, "left": transformed[:2],
                           "right": transformed[2:]})

    # Boundary-factor collisions, including the corrected 3R equality.
    l0 = {0, 3, 8, 11}
    r0 = {0, 1, 7, 13, 14}
    boundary = [(8, (8, 0), (0, 1)),
                (3, (3, 0), (0, 1)),
                (5, (8, 0), (3, 1)),
                (11, (11, 0), (0, 1))]
    for p, (ell, r), (other_ell, other_r) in boundary:
        assert ell in l0 and other_ell in l0 and r in r0 and other_r in r0
        assert ell + p * r == other_ell + p * other_r
        assert ell != other_ell and p * r != p * other_r
    assert 2 * 3 + 1 == 2 * 0 + 7
    assert 8 + 3 * 0 != 0 + 3 * 1

    # Polynomial identity in the draft-tail counterexample, checked exactly.
    # Its proof as a rational-function identity and its pole are in proof.md.
    rational_samples = []
    for x in (Fraction(1, 2), Fraction(9, 10), Fraction(99, 100)):
        q1 = 2 * x / (1 + x)
        q2 = (1 - x) / (1 + x)
        tail = 2 * q1 * q2 + q2 ** 2
        expected_tail = (1 - x) * (1 + 3 * x) / (1 + x) ** 2
        forced_f = tail * (1 - x ** 2) / (1 - x) ** 3
        assert q1 + q2 == 1
        assert tail == expected_tail
        assert forced_f == (1 + 3 * x) / (1 - x ** 2)
        rational_samples.append({"x": str(x), "tail": str(tail),
                                 "forced_f": str(forced_f)})

    # Compute the trimmed contexts from actual words of X0*, using the
    # source's definition. X0* consists of concatenated length-two blocks.
    x0 = {"".join(letters) for letters in product("ab", repeat=2)}

    def in_x0_star(candidate):
        return (len(candidate) % 2 == 0
                and all(candidate[k:k + 2] in x0
                        for k in range(0, len(candidate), 2)))

    p0 = Counter(range(2))  # exponents of 1+a for n=2
    context_samples = []
    for context in ("b", "bb", "bab", "baab"):
        trimmed = []
        for i, j in product(range(4), repeat=2):
            candidate = "a" * i + context + "a" * j
            if not in_x0_star(candidate):
                continue
            if (candidate.startswith("aa")
                    and in_x0_star(candidate[2:])):
                continue
            if (candidate.endswith("aa")
                    and in_x0_star(candidate[:-2])):
                continue
            trimmed.append((i, j, candidate))
        # Since the context starts and ends with b, stripping a^2 removes
        # every candidate with i>=2 or j>=2; the enumeration is complete.
        assert all(i < 2 and j < 2 for i, j, _ in trimmed)
        coefficients = Counter(i + j for i, j, _ in trimmed)
        assert sum(coefficients.values()) == 2
        assert coefficients != p0
        context_samples.append({
            "context": context,
            "trimmed_words": [candidate for _, _, candidate in trimmed],
            "coefficient_vector": [coefficients[k]
                                   for k in range(max(coefficients) + 1)],
            "p0_coefficient_vector": [p0[k] for k in range(2)],
        })
    kraft = sum((Fraction(1, 2 ** len(w)) for w in words), Fraction())
    assert kraft == Fraction(13763, 16384)
    a_histogram = Counter(i + j for i, j in PAIRS)
    assert a_histogram[7] >= 2

    print(json.dumps({
        "kind": "EXACT_SMALL_ARITHMETIC_RESEARCH_ONLY",
        "not_an_acceptance_certificate": True,
        "original_words": 16,
        "maximum_length": 15,
        "kraft_original": str(kraft),
        "left_difference_support": dl,
        "same_left_right_differences": d0,
        "gcd_samples": gcd_samples,
        "scaled_decoding_identities": identities,
        "x0_context_polynomial_samples": context_samples,
        "draft_tail_rational_samples": rational_samples,
    }, indent=2))


if __name__ == "__main__":
    main()
