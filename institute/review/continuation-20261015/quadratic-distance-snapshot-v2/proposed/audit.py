#!/usr/bin/env python3
"""Finite arithmetic controls for the proposed universal quadratic-distance lemma."""
import argparse
from collections import Counter
import itertools
import json
from pathlib import Path
import time


def canonical(magnitude):
    if magnitude % 4 != 2:
        raise ValueError("Expected an odd-weight Walsh magnitude")
    return magnitude if magnitude % 8 == 2 else -magnitude


def residue(magnitude):
    return ((magnitude * magnitude - 4) // 32) % 2


def transform(values):
    size = len(values)
    return [sum(value * (-1 if (a & x).bit_count() % 2 else 1)
                for a, value in enumerate(values)) for x in range(size)]


def quadratic_normal_form(dimension, rank, constant, radical_linear):
    if rank % 2 or not 0 <= rank <= dimension:
        raise ValueError("invalid alternating rank")
    if radical_linear and rank == dimension:
        raise ValueError("no radical coordinate available")
    values = []
    for x in range(1 << dimension):
        bit = constant
        for i in range(0, rank, 2):
            bit ^= ((x >> i) & 1) * ((x >> (i + 1)) & 1)
        if radical_linear:
            bit ^= (x >> rank) & 1
        values.append(bit)
    return values


def walsh(bits):
    return transform([1 - 2 * bit for bit in bits])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corrupt-majorant", action="store_true")
    args = parser.parse_args()
    started = time.monotonic()
    pairs = []
    equalities = []
    for m, n in itertools.product(range(2, 27, 4), repeat=2):
        if m + n > 28:
            continue
        difference = residue(m) ^ residue(n)
        total = m * m + n * n + 4 * (canonical(m) + canonical(n))
        upper = (407 if args.corrupt_majorant else 408) + 384 * difference
        if total > upper:
            raise ValueError(f"false pointwise majorant at {(m, n)}: {total}>{upper}")
        row = {"m": m, "n": n, "D": difference, "lhs": total, "rhs": upper}
        pairs.append(row)
        if total == upper:
            equalities.append([m, n])
    expected = [[2, 18], [2, 26], [6, 22], [18, 2], [22, 6], [26, 2]]
    if sorted(equalities) != sorted(expected):
        raise ValueError("unexpected equality cases")
    eight_weights = set()
    normal_forms = []
    for rank in range(0, 9, 2):
        for constant in (0, 1):
            for radical_linear in (False, True):
                if radical_linear and rank == 8:
                    continue
                bits = quadratic_normal_form(8, rank, constant, radical_linear)
                weight = sum(bits)
                expected_bias = 0 if radical_linear else (-1 if constant else 1) * (1 << (8 - rank // 2))
                if 256 - 2 * weight != expected_bias:
                    raise ValueError("quadratic normal-form bias mismatch")
                normal_forms.append({"rank": rank, "constant": constant, "radical_linear": radical_linear, "weight": weight})
                eight_weights.add(weight)
    if any(64 < weight < 96 for weight in eight_weights):
        raise ValueError("quadratic weight gap failed")
    six_biases = {}
    for rank in (4, 6):
        possible = set()
        for linear in range(64):
            for constant in (0, 1):
                q = quadratic_normal_form(6, rank, constant, False)
                values = [bit ^ ((x & linear).bit_count() & 1) for x, bit in enumerate(q)]
                possible.add(64 - 2 * sum(values))
        if any(sum(triple) == -64 for triple in itertools.product(possible, repeat=3)):
            raise ValueError("three high-rank biases could sum to -64")
        six_biases[rank] = sorted(possible)
    aggregate_energy = 2 * 65536
    if aggregate_energy - 4 * 512 != 408 * 256 + 384 * 64:
        raise ValueError("weight64 equality arithmetic failed")
    if 64 * 28 + 64 * 20 - 128 * 28 != -512:
        raise ValueError("equality partition arithmetic failed")
    spatial_energy = 64 * 20**2 + 192 * 28**2
    support_bound = 1 << 7
    transformed_energy = 256 * spatial_energy
    upper_energy = support_bound * 512**2
    if spatial_energy != 176128 or transformed_energy <= upper_energy:
        raise ValueError("Fourier-energy contradiction failed")
    # A relaxed quadratic pair meeting the equality count pattern. Its sum
    # spectrum violates the true Boolean-inverse bound, as the theorem predicts.
    relaxed_g = [(a & 1) ^ ((a >> 1) & 1) for a in range(256)]
    relaxed_d = [(a & 1) * ((a >> 1) & 1) for a in range(256)]
    relaxed_s = [20 - 48 * g + 8 * d + 48 * g * d for g, d in zip(relaxed_g, relaxed_d)]
    if sum(relaxed_d) != 64 or Counter(relaxed_s) != Counter({20: 64, -28: 128, 28: 64}):
        raise ValueError("relaxed equality example mismatch")
    inverse = transform(relaxed_s)
    if max(map(abs, inverse)) != 6656 or sum(v != 0 for v in inverse) > 128:
        raise ValueError("relaxed Fourier obstruction was not observed")
    # Actual odd tables show that weight64 difference can occur without the
    # 28-bound hypothesis, so that hypothesis must not be dropped.
    g = [int(x == 0) for x in range(256)]
    h = [int(x in (0, 1, 2)) for x in range(256)]
    G, H = walsh(g), walsh(h)
    true_distance = sum(residue(abs(u)) ^ residue(abs(v)) for u, v in zip(G, H))
    true_peak = max(abs(u) + abs(v) for u, v in zip(G, H))
    if true_distance != 64 or true_peak <= 28:
        raise ValueError("capacity-hypothesis control failed")
    result = {"status": "PASS", "finite_pair_count": len(pairs), "equality_pairs": equalities,
              "quadratic_normal_forms": normal_forms, "six_variable_bias_sets": six_biases,
              "weight64_partition_counts": {"D1": 64, "D0_Jg0": 64, "D0_Jg1": 128},
              "forced_spatial_energy": spatial_energy, "forced_fourier_energy": transformed_energy,
              "maximum_fourier_energy_with_128_support": upper_energy,
              "relaxed_example_inverse_peak": 6656,
              "actual_odd_half_control": {"weights": [sum(g), sum(h)], "residue_distance": true_distance, "capacity_peak": true_peak},
              "seconds": round(time.monotonic() - started, 4),
              "scope": "Exact finite-domain and normal-form arithmetic controls; the universal theorem additionally uses the written rank/coordinate argument. No global NL242 exclusion or novelty claim."}
    Path(__file__).with_name("audit.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
