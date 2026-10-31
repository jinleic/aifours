#!/usr/bin/env python3
"""Exact scalar Haar-moment arithmetic only; no selected physical target operator."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

N, k, d, copies = 64, 2, 4, 3
alpha = Q(k * (k * N - 1), N * (N * N - 1))
beta = Q(k * (N - k), N * (N * N - 1))
# Keep the half rational, with no floating-point inputs.
trace_K = (Q(d * d) - Q(d, 2)) ** copies
trace_FK = (Q(d) - Q(d * d, 2)) ** copies
mean = (alpha * trace_FK + beta * trace_K) / 4
wrong_missing_global_swap = (alpha * trace_K + beta * trace_FK) / 4
checks = {
    'dimension_and_rank': N == d ** copies and k == 2,
    'haar_trace_constraint': alpha * N * N + beta * N == k * k,
    'haar_swap_trace_constraint': alpha * N + beta * N * N == k,
    'trace_K_is_2744': trace_K == 2744,
    'trace_FK_is_minus_64': trace_FK == -64,
    'normalized_mean_is_positive_225_over_728': mean == Q(225, 728),
    'missing_global_swap_fault_detected': wrong_missing_global_swap != mean,
}
result = {
    'status': 'PASS' if all(checks.values()) else 'FAIL',
    'alpha': str(alpha), 'beta': str(beta),
    'trace_K': str(trace_K), 'trace_FK': str(trace_FK),
    'mean_q3_normalized_rank2_projection': str(mean),
    'checks': checks,
    'scope': 'Exact Fraction algebra for the Haar-average formula assuming the written two-copy unitary twirl and swap trick; no selected projection, target value, global positivity, source identity, formal or independent review.',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
out = Path(__file__).resolve().parent / 'frontier-20261028-d4-rank2-projector-haar-mean-check-results-v1.json'
out.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
print(json.dumps(result, sort_keys=True))
if result['status'] != 'PASS':
    raise SystemExit(1)
