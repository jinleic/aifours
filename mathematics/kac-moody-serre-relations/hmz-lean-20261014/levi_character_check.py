"""Exact, small Laurent-character corroboration, not a Serre-ideal checker.

All work concerns the fixed adjoint sl3 module, at free-Lie levels 1--4.
No Cartan matrices are searched and no previous finite-height run is replayed.
The representation-theoretic justification is given in STRUCTURAL.md.
"""
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def add(*terms):
    result = Counter()
    for scalar, poly in terms:
        for weight, coefficient in poly.items():
            result[weight] += scalar * coefficient
    return {w: c for w, c in result.items() if c}


def mul(left, right):
    result = Counter()
    for (a, b), c in left.items():
        for (x, y), d in right.items():
            result[a + x, b + y] += c * d
    return dict(result)


def power(poly, n):
    result = {(0, 0): 1}
    for _ in range(n):
        result = mul(result, poly)
    return result


def adams(poly, d):
    return {(d * a, d * b): c for (a, b), c in poly.items()}


def exact_divide(poly, d):
    result = {}
    for w, c in poly.items():
        assert c % d == 0, (w, c, d)
        result[w] = c // d
    return result


def trivial_multiplicity(poly):
    # Weyl denominator of type A2: prod_{positive roots}(1-exp(-alpha)).
    denominator = {(0, 0): 1}
    for alpha in [(1, 0), (0, 1), (1, 1)]:
        denominator = mul(denominator, {(0, 0): 1, (-alpha[0], -alpha[1]): -1})
    return mul(poly, denominator).get((0, 0), 0)


def summarize(poly):
    assert all(isinstance(c, int) and c >= 0 for c in poly.values())
    return {"dimension": sum(poly.values()),
            "trivial_multiplicity": trivial_multiplicity(poly)}


def main():
    V = {(0, 0): 2, (1, 0): 1, (0, 1): 1, (1, 1): 1,
         (-1, 0): 1, (0, -1): 1, (-1, -1): 1}
    exterior2 = exact_divide(add((1, power(V, 2)), (-1, adams(V, 2))), 2)
    exterior3 = exact_divide(add((1, power(V, 3)),
                                (-3, mul(V, adams(V, 2))),
                                (2, adams(V, 3))), 6)
    # Weighted PBW/logarithm gives the free-Lie character formula.
    free = {
        1: V,
        2: exterior2,
        3: exact_divide(add((1, power(V, 3)), (-1, adams(V, 3))), 3),
        4: exact_divide(add((1, power(V, 4)), (-1, power(adams(V, 2), 2))), 4),
    }
    # Check the full degree-three presentation character, not only its dimension.
    assert add((1, free[3]), (-1, mul(V, exterior2)), (1, exterior3)) == {}
    output = {
        "scope": "fixed adjoint sl3 Laurent characters only; no Serre equality computation",
        "field": "Q, with characteristic-zero representation theory in the written proof",
        "independent_serre_checker_run": False,
        "free_Lie": {str(k): summarize(p) for k, p in free.items()},
        "V_tensor_exterior2": summarize(mul(V, exterior2)),
        "exterior3": summarize(exterior3),
        "degree3_character_identity": True,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    assert output["free_Lie"]["3"] == {"dimension": 168, "trivial_multiplicity": 0}
    assert output["free_Lie"]["4"] == {"dimension": 1008, "trivial_multiplicity": 1}
    assert output["V_tensor_exterior2"] == {"dimension": 224, "trivial_multiplicity": 1}
    assert output["exterior3"] == {"dimension": 56, "trivial_multiplicity": 1}
    destination = Path(__file__).resolve().parent / "levi-character-result.json"
    destination.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
