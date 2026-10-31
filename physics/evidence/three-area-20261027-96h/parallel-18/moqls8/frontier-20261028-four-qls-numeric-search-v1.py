#!/usr/bin/env python3
"""Bounded four-MOQLS(8) full-Gram numerical search; never certifies a witness.

Each vector is normalized and each first row fixed by allowed output unitaries.
An intermediate overlap target forces a nonclassical-looking candidate. Every
reported defect uses all original rows, columns and all six product Gram
matrices. An exact independent verifier is required for any witness claim.
"""
import argparse
import hashlib
import json
import pathlib
import time
import numpy as np

N, M, N2 = 8, 4, 64
TARGET = 0.5
WEIGHT = 20.0
ANCHOR_X, ANCHOR_Y = 0, 9  # cells (0,0), (1,1)
RNG_SEED = 2026102817


def gf8mul(a, b):
    out = 0
    for _ in range(3):
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 11
    return out


def classical_input():
    V = np.zeros((M, N, N2), dtype=np.complex128)
    for a in range(M):
        for i in range(N):
            for j in range(N):
                V[a, gf8mul(a+1, i) ^ j, i*N+j] = 1.0
    return V


cell = np.arange(N2)
row = cell // N
col = cell % N
OFF = ~np.eye(N2, dtype=bool)
LINES = OFF & ((row[:, None] == row[None, :]) | (col[:, None] == col[None, :]))
ROW_MASK = OFF & (row[:, None] == row[None, :])
COL_MASK = OFF & (col[:, None] == col[None, :])


def grams(V):
    return np.einsum('aik,ail->akl', V.conj(), V, optimize=True)


def loss_grad(V):
    G = grams(V)
    mag = np.abs(G)**2
    line_loss = float(np.sum(mag * LINES[None, :, :]))
    pair_loss = 0.0
    for a in range(M):
        for b in range(a+1, M):
            pair_loss += float(np.sum(mag[a] * mag[b] * OFF))
    overlap2 = float(mag[0, ANCHOR_X, ANCHOR_Y])
    target_loss = WEIGHT * (overlap2-TARGET)**2
    grad = np.empty_like(V)
    for a in range(M):
        multiplier = LINES.astype(np.float64).copy()
        for b in range(M):
            if b != a:
                multiplier += mag[b] * OFF
        K = multiplier * G[a]
        if a == 0:
            K[ANCHOR_X, ANCHOR_Y] += WEIGHT*(overlap2-TARGET)*G[a, ANCHOR_X, ANCHOR_Y]
            K[ANCHOR_Y, ANCHOR_X] += WEIGHT*(overlap2-TARGET)*G[a, ANCHOR_Y, ANCHOR_X]
        grad[a] = 2.0 * (V[a] @ K)
    return line_loss+pair_loss+target_loss, grad


def physical_diagnostics(V):
    G = grams(V)
    norm_error = float(np.max(np.abs(np.diagonal(G, axis1=1, axis2=2)-1)))
    row_error = float(np.max(np.abs(G * ROW_MASK[None, :, :])))
    col_error = float(np.max(np.abs(G * COL_MASK[None, :, :])))
    pair_error = 0.0
    pair_counts = 0
    for a in range(M):
        for b in range(a+1, M):
            pair_gram = G[a] * G[b]
            pair_error = max(pair_error, float(np.max(np.abs(pair_gram-np.eye(N2)))))
            pair_counts += pair_gram.size
    intermediate = float(np.abs(G[0, ANCHOR_X, ANCHOR_Y])**2)
    return {'norm_max_abs_error': norm_error, 'row_max_abs_error': row_error,
            'column_max_abs_error': col_error, 'pair_product_gram_max_abs_error': pair_error,
            'pair_product_entries_checked': pair_counts,
            'forced_intermediate_overlap_squared': intermediate,
            'target_abs_error': abs(intermediate-TARGET)}


def normalize_and_anchor(V):
    norm = np.sqrt(np.sum(np.abs(V)**2, axis=1))
    if not np.all(np.isfinite(norm)) or np.any(norm < 1e-14):
        raise ValueError('nonfinite or vanishing vector')
    V = V / norm[:, None, :]
    for a in range(M):
        V[a, :, :N] = np.eye(N, dtype=np.complex128)
    return V


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--candidate', required=True)
    args = parser.parse_args()
    start = time.monotonic()
    rng = np.random.default_rng(RNG_SEED)
    baseline = classical_input()
    control = physical_diagnostics(baseline)
    if any(control[k] > 1e-14 for k in ('norm_max_abs_error','row_max_abs_error',
                                       'column_max_abs_error','pair_product_gram_max_abs_error')):
        raise ValueError('positive classical control failed')
    bad = baseline.copy()
    bad[1] = bad[0]
    negative = physical_diagnostics(bad)
    if negative['row_max_abs_error'] > 1e-14 or negative['column_max_abs_error'] > 1e-14 or negative['pair_product_gram_max_abs_error'] < .9:
        raise ValueError('duplicate-square negative control failed')
    gradient_point = normalize_and_anchor(rng.normal(size=baseline.shape)+1j*rng.normal(size=baseline.shape))
    direction = (rng.normal(size=baseline.shape)+1j*rng.normal(size=baseline.shape)) / np.sqrt(baseline.size)
    base_loss, grad = loss_grad(gradient_point)
    step = 1e-6
    finite_difference = (loss_grad(gradient_point+step*direction)[0] - loss_grad(gradient_point-step*direction)[0]) / (2*step)
    analytic = float(2*np.vdot(grad, direction).real)
    gradient_relative_error = abs(finite_difference-analytic)/(1+abs(finite_difference))
    if not np.isfinite(gradient_relative_error) or gradient_relative_error > 1e-5:
        raise ValueError(f'directional gradient check failed: {gradient_relative_error}')
    runs = []
    global_best = None
    global_score = float('inf')
    total_limit = 24.0
    for restart in range(3):
        if time.monotonic()-start > total_limit:
            break
        if restart == 0:
            V = normalize_and_anchor(baseline + 0.23*(rng.normal(size=baseline.shape)+1j*rng.normal(size=baseline.shape)))
        else:
            V = normalize_and_anchor(rng.normal(size=baseline.shape)+1j*rng.normal(size=baseline.shape))
        momentum = np.zeros_like(V)
        velocity = np.zeros(V.shape, dtype=np.float64)
        first = time.monotonic()
        local_best = float('inf')
        best_diag = None
        steps = 0
        for step_index in range(1, 3001):
            if time.monotonic()-start > total_limit or time.monotonic()-first > 8.0:
                break
            value, gradient = loss_grad(V)
            if not np.isfinite(value) or not np.all(np.isfinite(gradient)):
                raise ValueError('nonfinite optimizer state')
            if value < local_best:
                local_best = float(value)
                best_diag = physical_diagnostics(V)
            if value < global_score:
                global_score = float(value)
                global_best = V.copy()
            momentum = 0.9*momentum + 0.1*gradient
            velocity = 0.999*velocity + 0.001*np.abs(gradient)**2
            mh = momentum/(1-0.9**step_index)
            vh = velocity/(1-0.999**step_index)
            V = normalize_and_anchor(V - 0.015*mh/(np.sqrt(vh)+1e-8))
            steps = step_index
        runs.append({'restart': restart, 'iterations': steps, 'best_objective': local_best,
                     'best_full_physical_diagnostics': best_diag,
                     'elapsed_seconds': time.monotonic()-first})
    if global_best is None:
        raise ValueError('no optimizer state')
    final_diag = physical_diagnostics(global_best)
    candidate = {'shape': list(global_best.shape),
                 'real': global_best.real.tolist(), 'imag': global_best.imag.tolist(),
                 'note': 'Floating-point numerical candidate only; not an exact witness.'}
    candidate_path = pathlib.Path(args.candidate)
    with candidate_path.open('x', encoding='utf-8') as handle:
        json.dump(candidate, handle, separators=(',', ':'))
        handle.write('\n')
    candidate_sha = hashlib.sha256(candidate_path.read_bytes()).hexdigest()
    report = {'result': 'BOUNDED_FLOATING_POINT_EXPLORATION_NOT_A_CERTIFICATE',
              'source_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'candidate_sha256': candidate_sha, 'numpy_version': np.__version__,
              'seed': RNG_SEED, 'parameterized_shape': [M,N,N2],
              'positive_classical_control': control, 'duplicate_square_control': negative,
              'gradient_directional_relative_error': gradient_relative_error,
              'forced_overlap_squared_target': TARGET, 'target_penalty_weight': WEIGHT,
              'runs': runs, 'best_objective': global_score, 'best_full_diagnostics': final_diag,
              'elapsed_seconds': time.monotonic()-start,
              'limits': 'One forced overlap target, 3 bounded restarts, floating point; no exhaustive result or exact witness.'}
    with pathlib.Path(args.output).open('x', encoding='utf-8') as handle:
        json.dump(report, handle, indent=2, allow_nan=False)
        handle.write('\n')
    print(json.dumps(report, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
