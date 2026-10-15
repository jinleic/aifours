#!/usr/bin/env python3
"""Exact finite checks of the proved algorithms; not a book-level certificate."""
from fractions import Fraction as F
from itertools import product
import hashlib
import json
from pathlib import Path
import platform
import sys
import time

from segmentation import greedy_segments, minimax_segments


def brute_partitions(values):
    n = len(values)
    for mask in range(1 << (n - 1)):
        cuts = [0] + [i for i in range(1, n) if mask & (1 << (i - 1))] + [n]
        pieces = [values[a:b] for a, b in zip(cuts, cuts[1:])]
        # Deliberately independent of the implementation's radius table.
        error = max(F(max(piece) - min(piece), 2) for piece in pieces)
        yield len(pieces), error


def verify():
    cases = greedy_comparisons = dp_comparisons = 0
    for n in range(1, 7):
        for values in product((-1, 0, 1), repeat=n):
            cases += 1
            all_partitions = tuple(brute_partitions(values))
            for eps in (F(0), F(1, 2), F(1)):
                pieces = greedy_segments(values, eps)
                truth = min(k for k, error in all_partitions if error <= eps)
                assert len(pieces) == truth, (values, eps, pieces, truth)
                for a, b, center in pieces:
                    assert all(abs(F(x) - center) <= eps for x in values[a:b])
                greedy_comparisons += 1
            for k in range(1, n + 1):
                error, pieces = minimax_segments(values, k)
                truth = min(e for count, e in all_partitions if count == k)
                assert error == truth and len(pieces) == k, (values, k, error, truth)
                assert pieces[0][0] == 0 and pieces[-1][1] == n
                assert all(x[1] == y[0] for x, y in zip(pieces, pieces[1:]))
                assert max(abs(F(values[i]) - c) for a, b, c in pieces for i in range(a, b)) == error
                dp_comparisons += 1

    # Exact variance of the two-input-piece kernel (proof Counterexample 13).
    variance = []
    for t in (F(-1), F(0), F(1, 4), F(1, 2), F(3, 4), F(1), F(2)):
        positive_length = max(F(0), min(t, F(1)))
        integral = (1 - positive_length) + 4 * positive_length
        formula = F(1) if t <= 0 else F(4) if t >= 1 else 1 + 3 * t
        assert integral == formula
        variance.append({"t": str(t), "variance": str(integral)})
    assert variance[2]["variance"] != variance[4]["variance"]

    # Q slope formula: use q_pi = pi * mean(1/Q), so all arithmetic is rational.
    q_pi, dt, df, delta = F(2, 5), F(3, 2), F(7), F(1, 100)
    true_slope_difference = -2 * df * dt * q_pi
    worst = F(0)
    for signs in product((-1, 1), repeat=4):
        noise = delta * (signs[3] - signs[2] - signs[1] + signs[0])
        q_hat_pi = -(true_slope_difference + noise) / (2 * df * dt)
        worst = max(worst, abs(q_hat_pi - q_pi))
    bound = 2 * delta / (df * dt)
    assert worst == bound

    return {
        "status": "PASS",
        "arithmetic": "fractions.Fraction; no floating-point inference",
        "sequences": cases,
        "greedy_comparisons": greedy_comparisons,
        "minimax_dp_comparisons": dp_comparisons,
        "variance_counterexample": variance,
        "Q_pi_scaled_error": {"maximum": str(worst), "bound": str(bound)},
        "limits": "Finite scalar-grid implementation checks only. Universal claims rely on proof.md; no Lean verification or scientific novelty established.",
    }


if __name__ == "__main__":
    started = time.time()
    result = verify()
    folder = Path(__file__).resolve().parent
    result["receipt"] = {
        "argv": sys.argv,
        "cwd": str(Path.cwd()),
        "python": sys.version,
        "platform": platform.platform(),
        "started_unix": started,
        "elapsed_seconds": time.time() - started,
        "source_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in (folder / "segmentation.py", Path(__file__))},
    }
    serialized = json.dumps(result, indent=2) + "\n"
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(serialized)
    elif len(sys.argv) != 1:
        raise SystemExit("Usage: verify_exact.py [output.json]")
    print(serialized, end="")
