#!/usr/bin/env python3
"""Bounded joint-vector search; no numerical result is an exact certificate."""
import argparse
import importlib.util
import json
from pathlib import Path
import time

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('projection', HERE / 'frontier-20261028-coupled-projection-v1.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
N = base.N
BLOCKS = base.BLOCKS


def objective_gradient(v, repel_weight, threshold):
    grad = np.zeros_like(v)
    cost = 0.0
    for block in BLOCKS:
        ids = list(block)
        b = v[:, ids]
        error = b.conj().T @ b - np.eye(N)
        cost += float(np.sum(np.abs(error) ** 2))
        grad[:, ids] += 4 * b @ error
    g = v.conj().T @ v
    penalty = np.maximum(np.abs(g) ** 2 - threshold ** 2, 0)
    np.fill_diagonal(penalty, 0)
    cost += float(repel_weight * np.sum(penalty ** 2) / 2)
    grad += 4 * repel_weight * v @ (penalty * g)
    return cost, grad


def run():
    p = argparse.ArgumentParser()
    p.add_argument('--restarts', type=int, default=4)
    p.add_argument('--steps', type=int, default=5000)
    p.add_argument('--seconds', type=float, default=90)
    p.add_argument('--step-size', type=float, default=0.02)
    p.add_argument('--repel', type=float, default=0.05)
    p.add_argument('--threshold', type=float, default=0.98)
    p.add_argument('--start-seed', type=int, default=101)
    args = p.parse_args()
    if args.restarts < 1 or args.steps < 1 or args.seconds <= 0:
        raise ValueError('restart, step and time limits must be positive')
    start = time.monotonic()
    best = None
    runs = []
    for seed in range(args.start_seed, args.start_seed + args.restarts):
        rng = np.random.default_rng(seed)
        v = rng.normal(size=(N, N*N)) + 1j*rng.normal(size=(N, N*N))
        v /= np.linalg.norm(v, axis=0)
        m = np.zeros_like(v)
        h = np.zeros(v.shape, dtype=float)
        for step in range(1, args.steps + 1):
            loss, grad = objective_gradient(v, args.repel, args.threshold)
            m = 0.9*m + 0.1*grad
            h = 0.999*h + 0.001*np.abs(grad)**2
            mh = m / (1-0.9**step)
            hh = h / (1-0.999**step)
            v -= args.step_size * mh / (np.sqrt(hh) + 1e-8)
            v /= np.linalg.norm(v, axis=0)
            if step == 1 or step % 100 == 0 or step == args.steps:
                metrics = base.score(v)
                if best is None or metrics['max_block_gram_error'] < best[0]:
                    best = (metrics['max_block_gram_error'], v.copy(), seed, step, metrics)
                if metrics['max_block_gram_error'] < 1e-10 and metrics['max_distinct_pair_overlap'] < 1 - 1e-8:
                    print('NUMERIC_CANDIDATE_REQUIRES_INDEPENDENT_CERTIFICATION', seed, step, metrics, flush=True)
                    break
            if time.monotonic() - start >= args.seconds:
                break
        final = base.score(v)
        runs.append({'seed': seed, 'steps': step, 'last_preupdate_loss': loss, **final})
        print('restart', seed, 'steps', step, 'loss', loss, 'metrics', final, flush=True)
        if time.monotonic() - start >= args.seconds:
            break
    artifact = HERE / 'frontier-20261028-coupled-adam-best-v1.npy'
    np.save(artifact, best[1], allow_pickle=False)
    record = {'method': 'joint complex Adam with normalized columns and near-parallel penalty',
              'incidence': 'Weisner 1963 Fig.1 second digit', 'parameters': vars(args),
              'elapsed_seconds': time.monotonic() - start, 'runs': runs,
              'best_seed': best[2], 'best_step': best[3], 'best_metrics': best[4],
              'candidate_file': artifact.name,
              'caveat': 'floating point only, not exhaustive and no rigorous witness certificate'}
    output = HERE / 'frontier-20261028-coupled-adam-result-v1.json'
    output.write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
    print('best', best[2], best[3], best[4], flush=True)
    print('wrote', output.name, artifact.name, flush=True)


if __name__ == '__main__':
    run()
