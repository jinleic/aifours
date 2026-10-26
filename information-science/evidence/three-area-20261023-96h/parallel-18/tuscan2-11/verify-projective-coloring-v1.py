"""Read-only exact verifier for the PGL(2,11) restricted-family obstruction.

Usage (future replay only): python3 verify-projective-coloring-v1.py CERTIFICATE.json
The author executed verify_certificate in its existing eval kernel, not a native CLI.
No all-permutation Tuscan-2(11) impossibility follows from this certificate.
"""

import json
import sys
from itertools import combinations
from pathlib import Path


class CertificateError(ValueError):
    pass


def projective_row(matrix):
    a, b, c, d = matrix
    if (a * d - b * c) % 11 == 0:
        raise CertificateError("singular matrix")

    def successor(x):
        if x == 11:
            return 11 if c == 0 else a * pow(c, -1, 11) % 11
        denominator = (c * x + d) % 11
        return 11 if denominator == 0 else (a * x + b) * pow(denominator, -1, 11) % 11

    orbit = [11]
    x = successor(11)
    while x not in orbit:
        orbit.append(x)
        x = successor(x)
    if len(orbit) != 12 or x != 11:
        return None
    return tuple(orbit[1:])


def row_events(row, distance):
    return {(row[i], row[i + distance]) for i in range(11 - distance)}


def compatible(left, right):
    return (
        left[0] != right[0]
        and left[-1] != right[-1]
        and row_events(left, 1).isdisjoint(row_events(right, 1))
        and row_events(left, 2).isdisjoint(row_events(right, 2))
    )


def verify_certificate(certificate):
    if certificate.get("field_prime") != 11 or certificate.get("infinity_label") != 11:
        raise CertificateError("wrong field")
    family = {}
    for a in range(11):
        for b in range(11):
            for d in range(11):
                if (a * d - b) % 11 == 0:
                    continue
                matrix = (a, b, 1, d)
                row = projective_row(matrix)
                if row is not None:
                    family[matrix] = row
    if len(family) != 220 or len(set(family.values())) != 220:
        raise CertificateError("Hamilton-family count")
    normalized = {matrix for matrix, row in family.items() if row[:2] == (0, 1)}
    expected_seeds = {(0, 3, 1, 3), (0, 4, 1, 4)}
    if normalized != expected_seeds:
        raise CertificateError("normalization enumeration")
    cases = certificate.get("cases", [])
    seeds = [tuple(case["seed_matrix"]) for case in cases]
    if len(seeds) != 2 or set(seeds) != expected_seeds:
        raise CertificateError("seed set")
    bounds = []
    reports = []
    for case in cases:
        seed = tuple(case["seed_matrix"])
        expected = {matrix for matrix, row in family.items() if compatible(family[seed], row)}
        classes = [[tuple(matrix) for matrix in color] for color in case["color_classes"]]
        flat = [matrix for color in classes for matrix in color]
        if len(flat) != len(set(flat)) or set(flat) != expected:
            raise CertificateError("neighbor cover")
        if case["neighbor_count"] != len(expected):
            raise CertificateError("neighbor count")
        if case["color_count"] != len(classes) or not classes or any(not color for color in classes):
            raise CertificateError("color count")
        for color in classes:
            for left, right in combinations(color, 2):
                if compatible(family[left], family[right]):
                    raise CertificateError("color class contains compatible rows")
        bound = 1 + len(classes)
        if bound > 10 or case["family_size_bound_if_seed_selected"] != bound:
            raise CertificateError("bound does not exclude eleven")
        bounds.append(bound)
        reports.append({"seed": seed, "neighbors": len(expected), "colors": len(classes), "row_bound": bound})
    return {"status": "VALID_RESTRICTED_FAMILY_OBSTRUCTION", "Hamilton_rows": len(family), "cases": reports, "maximum_row_bound": max(bounds), "unrestricted_T2_11_verdict": "UNRESOLVED"}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Expected one certificate JSON path")
    result = verify_certificate(json.loads(Path(sys.argv[1]).read_text()))
    print(json.dumps(result, sort_keys=True))
