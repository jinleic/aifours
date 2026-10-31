#!/usr/bin/env python3
"""Bounded actual-vector search for a fixed published OLS(10) incidence.

Alternates the polar projections of the 30 required bases.  This is numerical
exploration, never a proof of existence or absence; a candidate would need an
independent exact or rigorously bounded verifier.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import time

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('published_ols', HERE / 'frontier-20261028-ols10-switch-v1.py')
ols = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ols)
ols.check_table()
N = ols.N


def blocks():
    out = []
    out.extend([tuple(r * N + c for c in range(N)) for r in range(N)])
    out.extend([tuple(r * N + c for r in range(N)) for c in range(N)])
    out.extend([tuple(r * N + c for r in range(N) for c in range(N)
                      if ols.TABLE[r][c][1] == label) for label in range(N)])
    assert len(out) == 3 * N and all(len(block) == N for block in out)
    return tuple(out)


BLOCKS = blocks()


def score(v):
    # v[:, x] is the ACTUAL complex vector at cell x.
    gram = v.conj().T @ v
    diagonal = np.real(np.diag(gram))
    block_error = max(float(np.max(np.abs(gram[np.ix_(b, b)] - np.eye(N)))) for b in BLOCKS)
    off = np.abs(gram.copy())
    np.fill_diagonal(off, 0.0)
    max_pair = float(np.max(off))
    # This count is tolerance-based and is not an exact ray count.
    near_parallel = int(np.count_nonzero(np.triu(off >= 1.0 - 1e-8, 1)))
    return {'max_block_gram_error': block_error,
            'max_norm_error': float(np.max(np.abs(diagonal - 1))),
            'max_distinct_pair_overlap': max_pair,
            'near_parallel_pair_count': near_parallel}


def polar(block):
    u, _, vh = np.linalg.svd(block, full_matrices=False)
    return u @ vh


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--restarts', type=int, default=4)
    parser.add_argument('--sweeps', type=int, default=400)
    parser.add_argument('--seconds', type=float, default=90)
    args = parser.parse_args()
    if args.restarts < 1 or args.sweeps < 1 or args.seconds <= 0:
        raise ValueError('positive bounded restart/sweep/time limits required')
    start = time.monotonic()
    records = []
    best_score, best_v, best_where = float('inf'), None, None
    # Deterministic seeds permit independent replay; they are not an exhaustive search.
    for seed in range(args.restarts):
        rng = np.random.default_rng(seed)
        v = rng.normal(size=(N, N*N)) + 1j * rng.normal(size=(N, N*N))
        for sweep in range(1, args.sweeps + 1):
            for block in BLOCKS:
                idx = list(block)
                v[:, idx] = polar(v[:, idx])
            if sweep == 1 or sweep % 25 == 0 or sweep == args.sweeps:
                result = score(v)
                current = result['max_block_gram_error']
                if current < best_score:
                    best_score, best_v, best_where = current, v.copy(), (seed, sweep)
                if current < 1e-10 and result['max_distinct_pair_overlap'] < 1.0 - 1e-8:
                    print('NUMERIC_CANDIDATE_REQUIRES_INDEPENDENT_CERTIFICATION', seed, sweep, result, flush=True)
                    break
            if time.monotonic() - start >= args.seconds:
                break
        result = score(v)
        records.append({'seed': seed, 'sweeps': sweep, **result})
        print('restart', seed, 'sweeps', sweep, 'result', result, flush=True)
        if time.monotonic() - start >= args.seconds:
            break
    artifact = HERE / 'frontier-20261028-coupled-projection-best-v1.npy'
    np.save(artifact, best_v, allow_pickle=False)
    summary = {'method': '30-block polar alternating projections', 'n': N,
               'fixed_incidence': 'Weisner 1963 Fig. 1, second digit',
               'restarts_requested': args.restarts, 'sweeps_per_restart_limit': args.sweeps,
               'time_limit_seconds': args.seconds, 'elapsed_seconds': time.monotonic() - start,
               'runs': records, 'best_seed_sweep': best_where, 'best_score': score(best_v),
               'candidate_file': artifact.name,
               'caveat': 'floating point search, no exhaustive or exact certification'}
    outfile = HERE / 'frontier-20261028-coupled-projection-result-v1.json'
    outfile.write_text(json.dumps(summary, indent=2, sort_keys=True) + '\n')
    print('best', best_where, summary['best_score'], flush=True)
    print('wrote', outfile.name, 'and', artifact.name, flush=True)


if __name__ == '__main__':
    main()
