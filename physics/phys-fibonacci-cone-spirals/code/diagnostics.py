#!/usr/bin/env python3
"""Non-certifying high-precision controls in polar coordinates, fixed protocol."""
import json
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
mp.mp.dps = 80
BETA = mp.mpf(1) / 6
A = 2 * mp.pi * BETA
PHI = (1 + mp.sqrt(5)) / 2
GAMMA = (3 - mp.sqrt(5)) / 2
FIB = [0, 1]
for _ in range(31):
    FIB.append(FIB[-1] + FIB[-2])


def distance2(r2, s2, offset):
    delta = offset * GAMMA - mp.nint(offset * GAMMA)
    # Stable form, not the subtractive expression in the exact verifier.
    return (mp.sqrt(s2) - mp.sqrt(r2)) ** 2 + 4 * mp.sqrt(r2 * s2) * mp.sin(A * delta / 2) ** 2


def branch_length(k, t):
    return mp.mpf(FIB[k]) ** 2 / (4 * t) + A * A * t * PHI ** (-2 * k)


def pair_transition(k):
    # Switch (F_{k-1},F_k) -> (F_k,F_{k+1}); k >= 3.
    return mp.sqrt((mp.mpf(FIB[k + 1]) ** 2 - FIB[k - 1] ** 2) /
                   (4 * A * A * (PHI ** (-2 * (k - 1)) - PHI ** (-2 * (k + 1)))))


def main():
    pair = distance2(mp.mpf(9700) / 91, mp.mpf(10900) / 91, 8)
    convergence = []
    for k in range(4, 25):
        q = FIB[k]
        eps = PHI ** (-k)
        n = int(mp.nint(q / (2 * A * eps)))
        value = distance2(mp.mpf(n), mp.mpf(n + q), q)
        convergence.append({"k": k, "offset": q, "n": n,
                            "distance_squared_c_equals_1": mp.nstr(value, 30)})
    phases = []
    for k in range(2, 15):
        lower = pair_transition(k) if k > 2 else mp.mpf(0)
        upper = pair_transition(k + 1)
        t = mp.sqrt(lower * upper) if lower else upper / 2
        best = sorted(range(2, 25), key=lambda j: branch_length(j, t))[:2]
        assert sorted(best) == [k, k + 1]
        # An independent brute force over integer offsets checks the local model.
        lengths = []
        for q in range(1, 1001):
            delta = q * GAMMA - mp.nint(q * GAMMA)
            lengths.append((mp.mpf(q) ** 2 / (4 * t) + A * A * t * delta * delta, q))
        shortest = sorted(q for _, q in sorted(lengths)[:2])
        assert shortest == [FIB[k], FIB[k + 1]]
        phases.append({"pair": shortest,
                       "larger_family_sign": (-1) ** (k + 1),
                       "sample_t": mp.nstr(t, 30),
                       "analytic_t_interval_for_fibonacci_family_model": [mp.nstr(lower, 25), mp.nstr(upper, 25)],
                       "fibonacci_indices_tested": [2, 24],
                       "integer_offsets_tested_at_sample": [1, 1000]})
    output = {
        "evidence_label": "Empirical evidence",
        "mpmath_version": mp.__version__, "decimal_precision": mp.mp.dps,
        "seed": "none; deterministic enumeration",
        "cone_beta": "1/6",
        "golden_finite_pair_distance_squared": mp.nstr(pair, 50),
        "asymptotic_distance_squared_upper_limit": mp.nstr(A / mp.sqrt(5), 50),
        "golden_density_upper_bound": mp.nstr(mp.pi / (2 * mp.sqrt(5)), 50),
        "triangular_density": mp.nstr(mp.pi / (2 * mp.sqrt(3)), 50),
        "density_ratio_lower_bound": mp.nstr(mp.sqrt(mp.mpf(5) / 3), 50),
        "convergence": convergence,
        "reduced_parastichy_phases": phases,
        "scope": "Not global optimization, interval arithmetic, or a sequential cone-growth experiment.",
    }
    (ROOT / "results" / "diagnostics.json").write_text(json.dumps(output, indent=2) + "\n")
    print(f"EMPIRICAL: golden pair squared distance={mp.nstr(pair, 18)}")
    print(f"EMPIRICAL: density upper bound={mp.nstr(mp.pi/(2*mp.sqrt(5)), 16)}, lattice={mp.nstr(mp.pi/(2*mp.sqrt(3)), 16)}")
    print(f"EMPIRICAL: {len(convergence)} asymptotic controls; {len(phases)} consecutive chirality phases, q=1..1000")


if __name__ == "__main__":
    main()
