"""Independent raw-coordinate checker for the frozen P44 N4 candidate assay.

PREPARATION ONLY: this source has not been executed. Import only after the
parent's exact named GO has been validated by the assay. This file neither
imports the assay nor shares its contraction/column-generation routines.
Numerical block checks are not exact PSD certificates or P44 acceptance.
"""
from __future__ import annotations

if __name__ == "__main__":
    raise SystemExit("No standalone execution: an exact parent GO is required")

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations
from math import factorial, fsum, sqrt
from typing import Callable

import numpy as np
import scipy.sparse as sp

D = 4
N = 4
RAW_DIM = 8 * 8**N


def _row(aux: int, physical: int, bob: tuple[int, ...]) -> int:
    index = aux * D + physical
    for value in bob:
        index = 8 * index + value
    return index


def _bob_sym(states: tuple[int, ...]) -> dict[tuple[int, ...], float]:
    """Distinct occupations with multiplicity, not a sum of 24 duplicates."""
    counts = Counter(states)
    multiplicity = 1
    for count in counts.values():
        multiplicity *= factorial(count)
    coefficient = multiplicity / factorial(N)
    return {value: coefficient for value in sorted(set(permutations(states)))}


def _add(column, aux, physical, states, scale):
    for bob, coefficient in _bob_sym(tuple(states)).items():
        column[_row(aux, physical, bob)] += scale * coefficient


def _without(values: tuple[int, ...], removed: tuple[int, ...]) -> tuple[int, ...]:
    remaining = list(values)
    for value in removed:
        remaining.remove(value)
    return tuple(remaining)


def _columns(spin: str, check_clock: Callable[[], None]):
    for physical in range(D):
        if spin == "J3half":
            for down in range(D):
                for up in combinations_with_replacement(range(D), 3):
                    check_clock()
                    column = defaultdict(float)
                    _add(column, 0, physical, (D + down, *up), 1)
                    _add(column, 1, physical, (down, *up), -1)
                    yield column
        elif spin == "J1half":
            for total in combinations_with_replacement(range(D), N):
                # Independent pair enumeration: position pairs, then deduplicate.
                pairs = sorted({(total[i], total[j])
                                for i, j in combinations(range(N), 2)})
                reference = pairs[0]
                for down in pairs[1:]:
                    check_clock()
                    column = defaultdict(float)
                    up = _without(total, down)
                    up_reference = _without(total, reference)
                    _add(column, 0, physical,
                         (*up, *(D + value for value in down)), 1)
                    _add(column, 0, physical,
                         (*up_reference, *(D + value for value in reference)), -1)
                    for value in reference:
                        _add(column, 1, physical,
                             (D + value, *_without(total, (value,))), 1)
                    for value in down:
                        _add(column, 1, physical,
                             (D + value, *_without(total, (value,))), -1)
                    yield column
        else:
            raise ValueError("unknown frozen spin sector")


def _basis(spin: str, check_clock: Callable[[], None]):
    rows, cols, data = [], [], []
    count = 0
    for count, column in enumerate(_columns(spin, check_clock), start=1):
        clean = {key: value for key, value in column.items() if value != 0}
        norm = sqrt(fsum(value * value for value in clean.values()))
        if norm == 0:
            raise ArithmeticError("zero independent highest-weight column")
        for row, value in sorted(clean.items()):
            rows.append(row)
            cols.append(count - 1)
            data.append(value / norm)
    expected = {"J3half": 320, "J1half": 260}[spin]
    if count != expected:
        raise ArithmeticError(f"independent basis size {count}, expected {expected}")
    return sp.csc_matrix((data, (rows, cols)), shape=(RAW_DIM, expected))


def _apply_raw_operator(basis, witness, check_clock):
    """Apply P(S)_aux tensor witness_AB1 directly to raw tensor coordinates."""
    out_rows, out_cols, out_data = [], [], []
    nonzero = [[(row, float(witness[row, col])) for row in range(16)
                if witness[row, col] != 0] for col in range(16)]
    coo = basis.tocoo()
    for index, (row, col, value) in enumerate(zip(coo.row, coo.col, coo.data)):
        if index % 1024 == 0:
            check_clock()
        left, packed = divmod(int(row), 8**N)
        alice_aux, alice_physical = divmod(left, D)
        bob = []
        for exponent in range(N - 1, -1, -1):
            state, packed = divmod(packed, 8**exponent)
            bob.append(state)
        bob_aux, bob_physical = divmod(bob[0], D)
        if (alice_aux, bob_aux) == (0, 1):
            sign_in = 1.0
        elif (alice_aux, bob_aux) == (1, 0):
            sign_in = -1.0
        else:
            continue
        physical_in = D * alice_physical + bob_physical
        for physical_out, entry in nonzero[physical_in]:
            alice_out, bob_out = divmod(physical_out, D)
            for aux_a, aux_b, sign_out in ((0, 1, 1.0), (1, 0, -1.0)):
                out_rows.append(_row(aux_a, alice_out,
                                     (D * aux_b + bob_out, *bob[1:])))
                out_cols.append(int(col))
                out_data.append(sign_in * sign_out * value * entry)
    result = sp.csc_matrix((out_data, (out_rows, out_cols)), shape=basis.shape)
    result.sum_duplicates()
    return result


class DefinitionChecker:
    """Reconstruct every returned block entry from independent raw definitions."""

    def __init__(self, check_clock: Callable[[], None]):
        self.check_clock = check_clock
        self.bases = {}
        self.grams = {}
        self.identity_lifts = {}
        identity = np.eye(16)
        for spin in ("J3half", "J1half"):
            basis = _basis(spin, check_clock)
            self.bases[spin] = basis
            self.grams[spin] = (basis.T @ basis).toarray()
            self.identity_lifts[spin] = (
                basis.T @ _apply_raw_operator(basis, identity, check_clock)
            ).toarray()

    def blocks(self, witness, mu, *, singlet_scale=1.0, trace_factor=2.0):
        witness = np.asarray(witness, dtype=float)
        if witness.shape != (16, 16) or not np.isfinite(witness).all():
            raise ValueError("independent checker requires a finite16x16 witness")
        if not np.allclose(witness, witness.T, rtol=0, atol=1e-12):
            raise ValueError("independent checker witness is not symmetric")
        if not np.isfinite(mu):
            raise ValueError("independent checker mu is nonfinite")
        result = {}
        for spin, basis in self.bases.items():
            self.check_clock()
            raw = _apply_raw_operator(basis, witness, self.check_clock)
            matrix = singlet_scale * (basis.T @ raw).toarray()
            matrix += mu * (self.grams[spin] -
                            trace_factor * singlet_scale * self.identity_lifts[spin])
            if np.max(np.abs(matrix - matrix.T)) > 1e-9:
                raise ArithmeticError("independent raw block lost symmetry")
            result[spin] = (matrix + matrix.T) / 2
        return result


def _integer_density(vectors, dimension):
    matrix = [[0 for _ in range(dimension)] for _ in range(dimension)]
    for item in vectors:
        weight = item["weight"]
        if not isinstance(weight, int) or weight <= 0:
            raise ValueError("nonpositive or noninteger frozen source weight")
        entries = item["entries"]
        if len({index for index, _ in entries}) != len(entries):
            raise ValueError("duplicate source vector coordinate")
        for index, coefficient in entries:
            if not isinstance(index, int) or not 0 <= index < dimension:
                raise ValueError("source vector coordinate out of range")
            if not isinstance(coefficient, int):
                raise ValueError("frozen source coefficient is not integer")
        for row, left in entries:
            for col, right in entries:
                matrix[row][col] += weight * left * right
    return matrix


def _exact_psd(matrix, check_clock):
    size = len(matrix)
    if any(matrix[row][col] != matrix[col][row]
           for row in range(size) for col in range(size)):
        raise ArithmeticError("integer state matrix is not symmetric")
    work = [[Fraction(value) for value in row] for row in matrix]
    rank = 0
    for pivot in range(size):
        check_clock()
        value = work[pivot][pivot]
        if value < 0:
            raise ArithmeticError("exact state PSD control found a negative pivot")
        if value == 0:
            if any(work[pivot][col] != 0 for col in range(pivot + 1, size)):
                raise ArithmeticError("exact state PSD control found a zero-pivot coupling")
            continue
        rank += 1
        for row in range(pivot + 1, size):
            for col in range(row, size):
                new = work[row][col] - work[row][pivot] * work[pivot][col] / value
                work[row][col] = new
                work[col][row] = new
    return rank


def exact_input_check(packet, check_clock):
    """Independent integer source/filter reconstruction, no floating PSD claim."""
    if packet["physical_dims"] != [4, 4] or packet["x"] != [1, 1, 1, 1]:
        raise ValueError("input is not the single frozen mixed-kernel case")
    direct = _integer_density(packet["vectors"], 16)
    source = _integer_density(packet["source45"]["vectors"], 20)
    compression = packet["bob_compression"]
    if compression != [[1, 0, 0, 0, 1], [0, 1, 0, 0, 1],
                       [0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]:
        raise ValueError("Bob compression is not the frozen x1111 map")
    filtered = [[0 for _ in range(16)] for _ in range(16)]
    for a in range(4):
        check_clock()
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    filtered[4 * a + b][4 * c + d] = sum(
                        compression[b][u] * source[5 * a + u][5 * c + v] *
                        compression[d][v] for u in range(5) for v in range(5))
    if filtered != direct:
        raise ArithmeticError("independent source45/filter matrix differs from target vectors")
    trace = sum(direct[index][index] for index in range(16))
    if trace != packet["normalization"] or trace != 49:
        raise ArithmeticError("target integer trace is not49")
    partial_transpose = [[0 for _ in range(16)] for _ in range(16)]
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    partial_transpose[4 * a + d][4 * c + b] = direct[4 * a + b][4 * c + d]
    return {"integer_source_filter_equal": True, "exact_trace": trace,
            "exact_psd_rank": _exact_psd(direct, check_clock),
            "exact_partial_transpose_psd_rank": _exact_psd(partial_transpose, check_clock),
            "proof_level": "ordinary exact rational arithmetic, not a formal kernel"}
