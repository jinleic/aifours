#!/usr/bin/env python3
"""Empirical evidence only: sparse-pilot adaptive tracking and oracle controls."""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import datetime
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def matrix_identity_control():
    a = np.array([[0.1, 0.02], [-0.03, 0.08]])
    b = np.array([[1.04, 0.02], [-0.01, 0.97]])
    lam = np.array([[0.15, -0.04], [0.01, 0.20]])
    errors = []
    for n in (2, 7, 61):
        common = (a + lam) @ b
        private = (a + lam / n) @ b
        m = common @ np.linalg.inv(b)
        d = private @ np.linalg.inv(b)
        ah = (n * d - m) / (n - 1)
        lh = n * (m - d) / (n - 1)
        errors.append(float(max(np.linalg.norm(ah - a), np.linalg.norm(lh - lam))))
    assert max(errors) < 1e-14
    return {'label': 'floating-point algebra smoke, not proof', 'errors': errors}


def simulate(n, p):
    reps, horizon = p['replicates'], p['horizon']
    a, b, lam = (p['parameters'][key] for key in ('A', 'B', 'Lambda'))
    ab, bb, lb = (p['bounds'][key] for key in ('a', 'b', 'ell'))
    sigma, gamma, f = p['noise']['sigma'], p['reference']['gamma'], p['reference']['f']
    rng = np.random.default_rng(p['base_seed'] + n)
    x = np.full((reps, n), p['initial_state'], dtype=float)
    ah, bh, lh = np.zeros_like(x), np.ones_like(x), np.zeros_like(x)
    eta_oracle = np.zeros((reps, 1))
    full = np.zeros(5)
    tail = np.zeros(5)
    tail_start = 3 * horizon // 4
    max_state = float(np.max(np.abs(x)))
    calibration_controls = 0
    updates = []
    epoch = None
    start = None
    m = None
    prev_c = prev_v = None
    for t in range(horizon):
        if t >= 4 and t & (t - 1) == 0:
            epoch = t.bit_length() - 1
            start = t
            m = math.isqrt(1 << epoch)
            sums_b = np.zeros_like(x)
            sums_c = np.zeros_like(x)
            sums_d = np.zeros_like(x)
            samples_b = samples_cd = 0
        calibration = start is not None and t < start + m + 1
        mean = np.mean(x, axis=1, keepdims=True)
        if calibration:
            c = 2.0 * rng.integers(0, 2, size=(reps, 1)) - 1.0
            v = 2.0 * rng.integers(0, 2, size=x.shape) - 1.0
            u = c + v
            calibration_controls += 1
        elif t < 4:
            u = np.zeros_like(x)
        else:
            u = (f - ah * x - lh * f) / bh
        noise = sigma * (2.0 * rng.integers(0, 2, size=x.shape) - 1.0)
        pred = a * x + b * u + lam * mean
        h = pred - (1.0 + gamma * (mean - 1.0))
        xnext = pred + noise
        oracle_h = (lam - gamma) * eta_oracle
        values = np.array([
            np.mean((mean - f) ** 2),
            np.mean((h + noise) ** 2),
            np.mean(h ** 2),
            np.mean(eta_oracle ** 2),
            np.mean(oracle_h ** 2),
        ])
        full += values
        if t >= tail_start:
            tail += values
        eta_oracle = lam * eta_oracle + np.mean(noise, axis=1, keepdims=True)
        if calibration:
            offset = t - start
            if offset < m:
                sums_b += xnext * v
                samples_b += 1
            if offset >= 1:
                sums_c += xnext * prev_c
                sums_d += xnext * prev_v
                samples_cd += 1
            prev_c, prev_v = c, v
            if offset == m:
                assert samples_b == samples_cd == m
                bh = np.clip(sums_b / m, 1.0 - bb, 1.0 + bb)
                mh = sums_c / m / bh
                dh = sums_d / m / bh
                ah = np.clip((n * dh - mh) / (n - 1), -ab, ab)
                lh = np.clip(n * (mh - dh) / (n - 1), -lb, lb)
                updates.append({
                    'epoch': epoch, 'samples': m, 'update_time': t + 1,
                    'rmse_A': float(np.sqrt(np.mean((ah - a) ** 2))),
                    'rmse_B': float(np.sqrt(np.mean((bh - b) ** 2))),
                    'rmse_Lambda': float(np.sqrt(np.mean((lh - lam) ** 2))),
                })
        x = xnext
        max_state = max(max_state, float(np.max(np.abs(x))))
    full /= horizon
    tail /= horizon - tail_start
    r = ab + lb
    kappa = 2 * ab / (1 - bb) + lb
    bound = max(p['initial_state'], (2 * (1 + bb) + sigma) / (1 - r),
                (((1 + bb) / (1 - bb)) * (1 + lb) * abs(f) + sigma) / (1 - kappa))
    assert np.isfinite(full).all() and np.isfinite(tail).all()
    assert max_state <= bound + 1e-12
    names = ['mean_mse', 'original_cost', 'predictable_cost_gap',
             'oracle_mean_mse', 'oracle_predictable_cost_gap']
    return {
        'N': n, 'seed': p['base_seed'] + n, 'replicates': reps,
        'full_time_metrics': dict(zip(names, map(float, full))),
        'preselected_exploitation_tail_metrics': dict(zip(names, map(float, tail))),
        'tail_window': [tail_start, horizon],
        'calibration_controls': calibration_controls,
        'calibration_fraction': calibration_controls / horizon,
        'state_max': max_state, 'theorem_state_bound': bound,
        'oracle_exact_long_run_mean_mse': sigma ** 2 / (n * (1 - lam ** 2)),
        'oracle_exact_predictable_cost_gap': (lam - gamma) ** 2 * sigma ** 2 / (n * (1 - lam ** 2)),
        'updates': updates,
    }


def proxy_bias_control(p):
    c = p['negative_control']
    n, lam, horizon = c['N'], c['lambda'], c['horizon']
    rng = np.random.default_rng(c['seed'])
    x = np.zeros((p['replicates'], n))
    numerator = denominator = 0.0
    for _ in range(horizon):
        noise = p['noise']['sigma'] * (2 * rng.integers(0, 2, size=x.shape) - 1)
        xn = lam * np.mean(x, axis=1, keepdims=True) + noise
        numerator += float(np.sum(x * xn))
        denominator += float(np.sum(x * x))
        x = xn
    return {'label': 'Empirical negative control for proxy LS', 'true_A': 0.0,
            'observed_OLS_A': numerator / denominator,
            'theoretical_pseudotrue_A': lam / (n * (1 - lam ** 2) + lam ** 2), **c}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    protocol_file = ROOT / 'work/protocol.json'
    protocol = json.loads(protocol_file.read_text())
    start = time.monotonic()
    receipt = {'command': [sys.executable, *sys.argv],
               'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'python': platform.python_version(), 'numpy': np.__version__,
               'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'protocol_sha256': hashlib.sha256(protocol_file.read_bytes()).hexdigest(),
               'thread_caps': {key: os.environ[key] for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS')}}
    try:
        result = {'label': 'Empirical evidence; not a proof or an asymptotic-rate certificate',
                  'protocol': protocol, 'matrix_identity_control': matrix_identity_control(),
                  'runs': [simulate(n, protocol) for n in protocol['population_sizes']],
                  'proxy_bias_negative_control': proxy_bias_control(protocol)}
        (args.output / 'smoke.json').write_text(json.dumps(result, indent=2))
        receipt['returncode'] = 0
        print(json.dumps({'runs': [{key: run[key] for key in ('N', 'full_time_metrics', 'preselected_exploitation_tail_metrics', 'state_max', 'calibration_fraction')} for run in result['runs']],
                          'negative_control': result['proxy_bias_negative_control']}, indent=2))
    except Exception as error:
        receipt['returncode'] = 1
        receipt['error'] = repr(error)
        raise
    finally:
        receipt['duration_seconds'] = time.monotonic() - start
        (args.output / 'command.json').write_text(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
