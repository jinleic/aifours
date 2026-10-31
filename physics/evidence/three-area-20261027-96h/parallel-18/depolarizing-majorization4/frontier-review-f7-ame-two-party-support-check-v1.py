#!/usr/bin/env python3
"""Independent exact Q(sqrt(2)) checks of the public AME witness and slices.

The explicit 36-cell transcription below was compared to Pandya's Table 1;
the pinned file is read once and must agree with it cell by cell. No author
checker is imported. Same-harness finite evidence, not a global classification.
"""

import hashlib
import itertools
import json
import re
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).parent
INPUT = ROOT / "frontier-review-f7-ame-two-party-support-input-v1.txt"
PIN = "cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38"
# Source: https://arxiv.org/html/2610.16673v1 Section II, Table 1.
SOURCE = (
    ("-12 +21", "-02 +20", "-01 +10", "s44", "s55", "s33"),
    ("-01 -10", "+00 +54", "+35 +43", "-15 -32", "-23 +41", "-24 +52"),
    ("+02 +20", "-35 +43", "+00 -54", "-25 +31", "-13 +42", "+14 +51"),
    ("s34", "-23 -41", "+13 +42", "s50", "-11 +22", "s05"),
    ("s53", "+15 -32", "+25 +31", "+11 +22", "s04", "s40"),
    ("s45", "-14 +51", "+24 +52", "s03", "s30", "+12 +21"),
)
ZERO = (F(0), F(0))
ONE = (F(1), F(0))
SQRT2 = (F(0), F(1))


class WitnessError(Exception):
    pass


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def neg(x):
    return -x[0], -x[1]


def mul(x, y):
    return x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def inv(x):
    denominator = x[0] * x[0] - 2 * x[1] * x[1]
    if not denominator:
        raise WitnessError("FIELD_ZERO")
    return x[0] / denominator, -x[1] / denominator


def parse(data, bind_hash=True):
    if bind_hash and hashlib.sha256(data).hexdigest() != PIN:
        raise WitnessError("INPUT_HASH")
    lines = data.decode("utf-8").splitlines()
    headers = ("# Pandya arXiv:2610.16673v1 Table 1; a b followed by unnormalized CD kets.", "# +xy/-xy = +/-|xy>, sxy = sqrt(2)|xy>; whole tensor /sqrt(72).")
    if len(lines) != 38 or tuple(lines[:2]) != headers:
        raise WitnessError("FORMAT_HEADERS_OR_COUNT")
    state = {}
    for position, line in enumerate(lines[2:]):
        tokens = line.split()
        a, b = divmod(position, 6)
        if len(tokens) not in (3, 4) or tokens[:2] != [str(a), str(b)]:
            raise WitnessError("FORMAT_CELL_ORDER")
        for token in tokens[2:]:
            if re.fullmatch(r"[+\-s][0-5][0-5]", token) is None:
                raise WitnessError("FORMAT_TOKEN")
        if " ".join(tokens[2:]) != SOURCE[a][b]:
            raise WitnessError("SOURCE_CELL_MISMATCH")
        if (tokens[2].startswith("s")) != (len(tokens) == 3):
            raise WitnessError("FORMAT_COEFFICIENT_COUNT")
        for token in tokens[2:]:
            key = (a, b, int(token[1]), int(token[2]))
            if key in state:
                raise WitnessError("DUPLICATE_TUPLE")
            state[key] = SQRT2 if token[0] == "s" else ONE if token[0] == "+" else neg(ONE)
    return state


def norm_numerator(state):
    value = ZERO
    for coefficient in state.values():
        value = add(value, mul(coefficient, coefficient))
    return value


def marginals(state):
    if norm_numerator(state) != (F(72), F(0)):
        raise WitnessError("NORM")
    results = []
    for active in itertools.combinations(range(4), 2):
        spectator = tuple(i for i in range(4) if i not in active)
        buckets = defaultdict(list)
        for index, coeff in state.items():
            label = tuple(index[i] for i in spectator)
            row = 6 * index[active[0]] + index[active[1]]
            buckets[label].append((row, coeff))
        matrix = [[ZERO for _ in range(36)] for _ in range(36)]
        for group in buckets.values():
            for row, c in group:
                for col, d in group:
                    matrix[row][col] = add(matrix[row][col], mul(c, d))
        for row in range(36):
            for col in range(36):
                expected = (F(2), F(0)) if row == col else ZERO
                if matrix[row][col] != expected:
                    raise WitnessError("MARGINAL_ENTRY")
        results.append({"parties_zero_based": list(active), "exact_diagonal_count_2": 36, "exact_offdiagonal_zero_count": 1260})
    return results


def hamming_one_pairs(support):
    return sum(sum(a != b for a, b in zip(x, y)) == 1 for x, y in itertools.combinations(support, 2))


def exact_rank(matrix):
    a = [row[:] for row in matrix]
    rank = 0
    for col in range(6):
        pivot = next((row for row in range(rank, 6) if a[row][col] != ZERO), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        reciprocal = inv(a[rank][col])
        a[rank] = [mul(entry, reciprocal) for entry in a[rank]]
        for row in range(rank + 1, 6):
            factor = a[row][col]
            if factor != ZERO:
                a[row] = [add(a[row][j], neg(mul(factor, a[rank][j]))) for j in range(6)]
        rank += 1
        if rank == 6:
            break
    return rank


def slice_histograms(state):
    result = []
    for active in itertools.combinations(range(4), 2):
        spectator = tuple(i for i in range(4) if i not in active)
        matrices = {(i, j): [[ZERO for _ in range(6)] for _ in range(6)] for i in range(6) for j in range(6)}
        for index, coeff in state.items():
            mat = matrices[tuple(index[k] for k in spectator)]
            row, col = index[active[0]], index[active[1]]
            if mat[row][col] != ZERO:
                raise WitnessError("DUPLICATE_SLICE_CELL")
            mat[row][col] = coeff
        hist = Counter()
        support_count = 0
        for mat in matrices.values():
            nz = [(i, j) for i in range(6) for j in range(6) if mat[i][j] != ZERO]
            if len({i for i, _ in nz}) != len(nz) or len({j for _, j in nz}) != len(nz):
                raise WitnessError("SLICE_NOT_PARTIAL_PERMUTATION")
            rank = exact_rank(mat)
            if rank != len(nz):
                raise WitnessError("SLICE_RANK")
            hist[rank] += 1
            support_count += len(nz)
        result.append({"active_zero_based": list(active), "rank_histogram": dict(sorted(hist.items())), "sum_of_ranks": support_count})
    return result


def rotate_03(state, site):
    h = (F(0), F(1, 2))
    entries = {(0, 0): h, (0, 3): h, (3, 0): h, (3, 3): neg(h)}
    for j in (1, 2, 4, 5):
        entries[j, j] = ONE
    transformed = {}
    for index, coeff in state.items():
        old = index[site]
        for new in range(6):
            factor = entries.get((new, old), ZERO)
            if factor != ZERO:
                target = list(index)
                target[site] = new
                target = tuple(target)
                transformed[target] = add(transformed.get(target, ZERO), mul(factor, coeff))
    return {index: coeff for index, coeff in transformed.items() if coeff != ZERO}


def failure(label, callback, expected):
    try:
        callback()
    except WitnessError as error:
        if str(error) != expected:
            raise WitnessError(f"CONTROL_WRONG_REASON_{label}:{error}") from error
        return {"control": label, "rejected_as": str(error)}
    raise WitnessError(f"CONTROL_NOT_REJECTED_{label}")


def main():
    payload = INPUT.read_bytes()
    state = parse(payload)
    if len(state) != 60:
        raise WitnessError("SUPPORT")
    if sum(coeff == SQRT2 for coeff in state.values()) != 12:
        raise WitnessError("SQRT2_COUNT")
    all_marginals = marginals(state)
    original_hamming = hamming_one_pairs(tuple(state))
    if original_hamming:
        raise WitnessError("HAMMING_ONE")
    level_counts = []
    spectator_counts = []
    for site in range(4):
        levels = [sum(index[site] == j for index in state) for j in range(6)]
        spectators = {tuple(index[k] for k in range(4) if k != site) for index in state}
        level_counts.append(levels)
        spectator_counts.append(len(spectators))
        if levels != [9, 12, 12, 9, 9, 9] or len(spectators) != 60:
            raise WitnessError("LOCAL_FIBER")
    slices = slice_histograms(state)
    for entry in slices:
        if entry["rank_histogram"] != {1: 12, 2: 24} or entry["sum_of_ranks"] != 60:
            raise WitnessError("SLICE_HISTOGRAM")

    one_party = []
    for site in range(4):
        rotated = rotate_03(state, site)
        rotated_marginals = marginals(rotated)
        assert len(rotated_marginals) == 6
        one_party.append({"site_zero_based": site, "support": len(rotated), "hamming_one_pairs": hamming_one_pairs(tuple(rotated)), "all_six_marginals_exact": True})
        if len(rotated) != 78 or not one_party[-1]["hamming_one_pairs"]:
            raise WitnessError("ONE_PARTY_ROTATION")
    two_party = []
    for i, j in itertools.combinations(range(4), 2):
        rotated = rotate_03(rotate_03(state, i), j)
        assert len(marginals(rotated)) == 6
        two_party.append({"sites_zero_based": [i, j], "support": len(rotated), "all_six_marginals_exact": True})
        if len(rotated) < 60:
            raise WitnessError("TWO_PARTY_ROTATION")

    first = next(iter(state))
    norm_bad = dict(state)
    norm_bad[first] = (F(-2), F(0))
    sign_bad = dict(state)
    sign_bad[first] = neg(sign_bad[first])
    corrupt = payload.replace(b"-12 +21", b"-1X +21", 1)
    support_bad = set(state)
    support_bad.remove((5, 5, 2, 1))
    support_bad.add((1, 0, 1, 2))
    if len(support_bad) != 60 or not hamming_one_pairs(tuple(support_bad)):
        raise WitnessError("HAMMING_CONTROL_FAILED")
    controls = [failure("norm-amplitude", lambda: marginals(norm_bad), "NORM"), failure("sign-only", lambda: marginals(sign_bad), "MARGINAL_ENTRY"), failure("bad-token", lambda: parse(corrupt, bind_hash=False), "FORMAT_TOKEN"), {"control": "same-size-hamming-neighbor", "detected_as": "HAMMING_ONE"}]
    print(json.dumps({"scope": "exact finite witness and selected local-unitary checks; not a global minimum or independent-model review", "source_table_cells_exactly_compared": 36, "input_sha256": hashlib.sha256(payload).hexdigest(), "support": len(state), "sqrt2_terms": 12, "unit_terms": 48, "norm_numerator": "72", "marginals": all_marginals, "hamming_one_pairs": original_hamming, "level_counts": level_counts, "distinct_spectator_triples": spectator_counts, "six_slice_histograms": slices, "one_party_03_rotations": one_party, "two_party_03_rotations": two_party, "controls": controls}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
