#!/usr/bin/env python3
"""Exact source-block local Haar frame; formal 60-dimensional operator algebra only.

No target C/state is evaluated. Uses the standard four-copy U(4) commutant / permutation
projection identity and exact fractions; output records every algebraic check's scope.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from pathlib import Path
import hashlib
import json

here = Path(__file__).resolve().parent
perms = list(permutations(range(4)))
words = list(product(range(4), repeat=4))


def inv(p):
    z = [0] * len(p)
    for i, j in enumerate(p):
        z[j] = i
    return tuple(z)


def cycles(p):
    seen, result = set(), 0
    for start in range(len(p)):
        if start not in seen:
            result += 1
            at = start
            while at not in seen:
                seen.add(at)
                at = p[at]
    return result


def act(p, word):
    return tuple(word[p[i]] for i in range(4))


G = [[Q(4 ** cycles(tuple(inv(p)[q[i]] for i in range(4)))) for q in perms] for p in perms]
gram_by_word = all(
    G[i][j] == sum(act(p, w) == act(q, w) for w in words)
    for i, p in enumerate(perms) for j, q in enumerate(perms)
)

basis = []
for i in range(4):
    for j in range(i, 4):
        sym = {(i, j): 1} if i == j else {(i, j): 1, (j, i): 1}
        for k in range(4):
            for l in range(k + 1, 4):
                anti = {(k, l): 1, (l, k): -1}
                basis.append({a + b: x * y for a, x in sym.items() for b, y in anti.items()})

lookup = {w: (i, c) for i, vector in enumerate(basis) for w, c in vector.items()}
metric = [Q(sum(c * c for c in vector.values())) for vector in basis]


def matrix_for(vector):
    b = [Q(sum(vector.get(act(p, w), 0) * coeff for w, coeff in vector.items())) for p in perms]
    aug = [row[:] + [b[i]] for i, row in enumerate(G)]
    for i in range(24):
        pivot = next(k for k in range(i, 24) if aug[k][i])
        aug[i], aug[pivot] = aug[pivot], aug[i]
        scale = aug[i][i]
        aug[i] = [x / scale for x in aug[i]]
        for j in range(24):
            if j != i:
                scale = aug[j][i]
                if scale:
                    aug[j] = [x - scale * y for x, y in zip(aug[j], aug[i])]
    c = [aug[i][-1] for i in range(24)]
    residual = [sum(G[i][j] * c[j] for j in range(24)) - b[i] for i in range(24)]
    H = [[Q(0) for _ in basis] for __ in basis]
    for j, vector_j in enumerate(basis):
        for p, coeff in zip(perms, c):
            if coeff:
                for w, sign in vector_j.items():
                    target = act(p, w)
                    if target in lookup:
                        i, left_sign = lookup[target]
                        H[i][j] += coeff * sign * left_sign
    return c, residual, H


def polynomial_residual_count(H, h_linear=-60):
    count = 0
    for i in range(len(basis)):
        for j in range(len(basis)):
            h2 = sum(H[i][k] * H[k][j] / metric[k] for k in range(len(basis)))
            value = 675 * h2 + h_linear * H[i][j] + (metric[i] if i == j else 0)
            count += value != 0
    return count


v = {(3, 3, 1, 0): 1, (3, 3, 0, 1): -1}
coeff, residual, H = matrix_for(v)
symmetric = all(H[i][j] == H[j][i] for i in range(60) for j in range(60))
trace = sum(H[i][i] / metric[i] for i in range(60))
trace2 = sum(H[i][j] * H[j][i] / metric[i] / metric[j] for i in range(60) for j in range(60))
poly_residual = polynomial_residual_count(H)
_, _, fault_H = matrix_for({(3, 3, 1, 0): 1, (3, 3, 0, 1): 1})
fault_wrong_wedge = polynomial_residual_count(fault_H)
fault_wrong_polynomial = polynomial_residual_count(H, h_linear=60)
checks = {
    'gram_cycle_formula_matches_all_word_traces': gram_by_word,
    'basis_dimension_is_60': len(basis) == 60,
    'basis_word_supports_are_disjoint': len(lookup) == sum(len(vv) for vv in basis),
    'all_24_projection_normal_equations_zero': all(x == 0 for x in residual),
    'frame_matrix_is_symmetric': symmetric,
    'frame_trace_is_2': trace == 2,
    'frame_trace_square_is_4_over_45': trace2 == Q(4, 45),
    'all_3600_metric_polynomial_residuals_zero': poly_residual == 0,
    'wrong_wedge_sign_fault_detected': fault_wrong_wedge > 0,
    'wrong_polynomial_linear_sign_fault_detected': fault_wrong_polynomial > 0,
}
result = {
    'status': 'PASS' if all(checks.values()) else 'FAIL',
    'arithmetic': 'Python fractions.Fraction integers/rationals only; standard-library exact',
    'source_frame': 'e3⊗e3⊗(e1⊗e0−e0⊗e1), zero-based site basis labels',
    'commutant_formula_assumption': 'Standard four-copy U(4) Schur-Weyl/permutation-commutant twirl; 24×24 Gram solved exactly.',
    'dimension': 60,
    'metric_diagonal_value_counts': {str(x): metric.count(x) for x in sorted(set(metric))},
    'trace': str(trace),
    'trace_square': str(trace2),
    'operator_polynomial': '675 T^2 − 60 T + I = 0',
    'derived_spectrum_with_multiplicity': {'1/45': 45, '1/15': 15},
    'exact_matrix_residuals': poly_residual,
    'fault_wrong_wedge_residuals': fault_wrong_wedge,
    'fault_wrong_polynomial_residuals': fault_wrong_polynomial,
    'checks': checks,
    'scope': 'Exact matrix calculation conditional on named standard Haar/Schur-Weyl identity; no target state/value, source identity, source positivity, independent reviewer, formal kernel or novelty verification.',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
out = here / 'frontier-20261028-d4-local-haar-frame-rational-check-results-v1.json'
out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
print(json.dumps(result, sort_keys=True))
if result['status'] != 'PASS':
    raise SystemExit(1)
