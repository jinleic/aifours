#!/usr/bin/env python3
"""Bounded search for an R-minus FD law beating 20/3.

The historical 88-word file is used only as a proposed set of binary words;
every original-neighbour FD is independently checked here. Numerics propose
probability weights; exact integer arithmetic decides the rounded law. This is
not an exhaustive search or an upper bound.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import hashlib
import json
import math
import time

import numpy as np

NEIGHBOURS = {
    1: (2, 3, 4, 5, 6, 7), 2: (1, 3, 7, 9, 10),
    3: (1, 2, 4, 8, 9), 4: (1, 3, 5, 8, 10),
    5: (1, 4, 6, 9, 10), 6: (1, 5, 7, 8, 9),
    7: (1, 2, 6, 8, 10), 8: (3, 4, 6, 7, 9, 10),
    9: (2, 3, 5, 6, 8), 10: (2, 4, 5, 7, 8),
}
CANDIDATE = Path('/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/guessing-number-r-minus/evidence/mis-q2-Rminus-600s.json')
OUTPUT = Path(__file__).with_name('frontier-20261028-fd-law-search-result.json')
SEED = 20261028
TIME_LIMIT_SECONDS = 25.0
MAX_ITERATIONS_PER_RESTART = 6000
MAX_RESTARTS = 12
RATIONAL_TOTAL = 600
TARGET = 20.0 / 3.0


def xlogx(x):
    if x <= 0.0:
        return 0.0
    return x * math.log(x)


def entropies(p, X):
    joint = -float(np.sum(p * np.log(np.maximum(p, 1e-300))))
    one = p @ X
    marginal = np.array([-xlogx(float(x)) - xlogx(float(1-x)) for x in one])
    return joint, marginal, one


def exact_check(weights, words):
    """Check H(joint) > (20/3)*H(v) for every v, using integer powers."""
    total = sum(weights)
    if total <= 1:
        return None
    marginal = [sum(w * ((word >> i) & 1) for w, word in zip(weights, words))
                for i in range(10)]
    base = pow(total, 17 * total)
    for w in weights:
        if w:
            base *= pow(w, 3 * w)
    checks = []
    for a in marginal:
        b = total - a
        left = (pow(a, 20 * a) if a else 1) * (pow(b, 20 * b) if b else 1)
        checks.append(left > base)
    return {"weight_total": total, "marginal_one_counts": marginal,
            "all_10_exact_strict_checks": all(checks),
            "per_vertex_exact_strict_checks": checks,
            "identity": "a^(20a)(N-a)^(20(N-a)) > N^(17N) product_i w_i^(3w_i)"}


def rounded_weights(p, total):
    scaled = p * total
    result = np.floor(scaled).astype(np.int64)
    remainder = total - int(result.sum())
    if remainder:
        indices = np.argsort(-(scaled - result))[:remainder]
        result[indices] += 1
    return [int(x) for x in result]


def main():
    started = time.monotonic()
    raw = CANDIDATE.read_bytes()
    supplied = json.loads(raw)
    words = sorted(set(int(w) for w in supplied['code']))
    assert len(words) == len(supplied['code']) == 88
    assert all(0 <= w < 1024 for w in words)
    masks = {v: sum(1 << (u - 1) for u in neighbours)
             for v, neighbours in NEIGHBOURS.items()}
    for a, b in combinations(words, 2):
        d = a ^ b
        for v, mask in masks.items():
            assert not ((d & (1 << (v - 1))) and not (d & mask)), (a, b, v)
    X = np.array([[(word >> i) & 1 for i in range(10)] for word in words], dtype=float)
    rng = np.random.default_rng(SEED)
    best = None
    trials = 0
    restarts_finished = 0
    initial = np.full(len(words), 1.0 / len(words))
    h0, m0, o0 = entropies(initial, X)
    baseline = {"joint_nats": h0, "max_marginal_nats": float(m0.max()),
                "ratio": h0 / float(m0.max()), "marginal_one_probs": o0.tolist()}

    for restart in range(MAX_RESTARTS):
        if time.monotonic() - started >= TIME_LIMIT_SECONDS:
            break
        if restart == 0:
            logp = np.zeros(len(words))
        else:
            logp = rng.normal(0.0, 0.7 if restart < 7 else 1.5, len(words))
        for iteration in range(MAX_ITERATIONS_PER_RESTART):
            if iteration % 100 == 0 and time.monotonic() - started >= TIME_LIMIT_SECONDS:
                break
            logp -= np.max(logp)
            p = np.exp(np.maximum(logp, -700.0))
            p /= p.sum()
            joint, marginal, one = entropies(p, X)
            cap = float(marginal.max())
            if cap > 0.1:
                ratio = joint / cap
                score = joint - TARGET * cap
                if best is None or ratio > best['ratio']:
                    best = {"ratio": ratio, "joint_nats": joint,
                            "max_marginal_nats": cap, "target_gap_nats": score,
                            "marginal_one_probs": one.tolist(), "p": p.copy(),
                            "restart": restart, "iteration": iteration}
            active = np.flatnonzero(marginal >= cap - 1e-9)
            chosen = int(rng.choice(active))
            observed_probs = np.where(X[:, chosen] > 0.5, one[chosen], 1.0 - one[chosen])
            grad = -np.log(np.maximum(p, 1e-300)) - 1.0
            grad += TARGET * (np.log(np.maximum(observed_probs, 1e-300)) + 1.0)
            rate = 0.012 / math.sqrt(1.0 + iteration / 300.0)
            logp += rate * np.clip(grad, -100.0, 100.0)
            trials += 1
        restarts_finished += 1

    assert best is not None
    weights = rounded_weights(best.pop('p'), RATIONAL_TOTAL)
    exact = exact_check(weights, words)
    result = {
        "candidate_file": str(CANDIDATE),
        "candidate_file_sha256": hashlib.sha256(raw).hexdigest(),
        "candidate_word_count": len(words),
        "candidate_pair_fd_checks": len(words) * (len(words) - 1) // 2 * 10,
        "candidate_reverified_fd": True,
        "support_words_one_based_bitsets": words,
        "seed": SEED, "time_limit_s": TIME_LIMIT_SECONDS,
        "max_restarts": MAX_RESTARTS, "max_iterations_per_restart": MAX_ITERATIONS_PER_RESTART,
        "restarts_started": restarts_finished, "iterations": trials,
        "elapsed_s": time.monotonic() - started,
        "uniform_baseline_float": baseline,
        "best_search_float": best,
        "rounded_probability_numerators": weights,
        "rounded_probability_denominator": RATIONAL_TOTAL,
        "rounded_law_exact_target_check": exact,
        "limits": "Search is only this verified 88-word support; floats propose, exact integer powers decide the rounded strict target. Not an upper bound, exhaustive search, or novelty claim.",
    }
    with OUTPUT.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps({k: result[k] for k in (
        'candidate_file_sha256', 'candidate_word_count', 'candidate_pair_fd_checks',
        'seed', 'iterations', 'elapsed_s', 'uniform_baseline_float', 'best_search_float',
        'rounded_law_exact_target_check', 'limits')}, indent=2))


if __name__ == '__main__':
    main()
