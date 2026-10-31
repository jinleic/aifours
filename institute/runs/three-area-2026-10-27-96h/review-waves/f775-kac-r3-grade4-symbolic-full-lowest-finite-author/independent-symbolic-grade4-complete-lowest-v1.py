#!/usr/bin/env python3
"""UNRUN prospective r=3 grade-four complete-lowest symbolic certificate.

No inputs, files, network, subprocesses, or deletion.  JSON goes to stdout.
The parent must read this entire source and separately authorize any execution.
The fixed quotient uses the whole positive/negative Serre-ideal bridge as an
external mathematical import, not as a conclusion of this program.
"""

import itertools
import json
import math
import signal
import sys
import time
from fractions import Fraction as Q
from functools import lru_cache

START = time.monotonic()
DEADLINE = START + 40.0
STOP = False


def stop_latch(_signum, _frame):
    global STOP
    STOP = True


for _sig in (signal.SIGINT, signal.SIGTERM):
    signal.signal(_sig, stop_latch)


class Interrupted(Exception):
    pass


def guard():
    if STOP or time.monotonic() >= DEADLINE:
        raise Interrupted("cooperative deadline or signal")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def bump(dst, key, value):
    if value:
        value = dst.get(key, 0) + value
        if value:
            dst[key] = value
        else:
            dst.pop(key, None)


def axpy(dst, src, scale):
    if scale:
        for key, value in src.items():
            bump(dst, key, scale * value)


def scaled(src, scale):
    return {key: value * scale for key, value in src.items() if value * scale}


class Span:
    """Sparse echelon basis; tracked rows retain original-generator labels."""

    def __init__(self, track=False):
        self.rows = {}
        self.track = track
        self.count = 0

    def reduce(self, vector):
        guard()
        work = dict(vector)
        remainder = {}
        used = {}
        steps = 0
        while work:
            steps += 1
            if steps % 32 == 0:
                guard()
            key = min(work)
            value = work.pop(key)
            if not value:
                continue
            entry = self.rows.get(key)
            if entry is None:
                remainder[key] = value
                continue
            row, coordinates = entry
            for other, coefficient in row.items():
                if other != key:
                    bump(work, other, -value * coefficient)
            if self.track:
                axpy(used, coordinates, value)
        return remainder, used

    def add(self, vector):
        remainder, used = self.reduce(vector)
        if not remainder:
            return False
        pivot = min(remainder)
        inverse = Q(1) / remainder[pivot]
        row = scaled(remainder, inverse)
        coordinates = {}
        if self.track:
            coordinates[self.count] = inverse
            axpy(coordinates, used, -inverse)
        self.rows[pivot] = (row, coordinates)
        self.count += 1
        return True


def bracket(left, right):
    out = {}
    for a, ca in left.items():
        for b, cb in right.items():
            bump(out, a + b, ca * cb)
            bump(out, b + a, -ca * cb)
    return out


LETTERS = "xabcdefg"
WEIGHTS = ((0, 0), (1, 0), (0, 1), (1, 1),
           (1, 1), (2, 1), (1, 2), (2, 2))
E1 = ({1: 1}, {}, {3: 1}, {5: -2}, {5: -1}, {}, {7: 1}, {})
E2 = ({2: 1}, {4: 1}, {}, {6: 1}, {6: 2}, {7: -1}, {}, {})
F1 = ({}, {0: 1}, {}, {2: 2}, {2: 1}, {3: -1}, {}, {6: 1})
F2 = ({}, {}, {0: 1}, {1: 1}, {1: 2}, {}, {4: 1}, {5: -1})
E12 = ({3: 1, 4: -1}, {5: -1}, {6: -1}, {7: -1},
       {7: 1}, {}, {}, {})


def derivation(vector, table):
    out = {}
    for word, coefficient in vector.items():
        for i, letter in enumerate(word):
            for replacement, multiplier in table[letter].items():
                new_word = word[:i] + (replacement,) + word[i + 1:]
                bump(out, new_word, coefficient * multiplier)
    return out


def lyndon(word):
    return all(word < word[i:] for i in range(1, len(word)))


@lru_cache(maxsize=None)
def standard_split(word):
    require(len(word) > 1 and lyndon(word), "non-Lyndon standard split")
    for index in range(1, len(word)):
        if lyndon(word[index:]):
            return word[:index], word[index:]
    raise ValueError("missing standard Lyndon factorization")


@lru_cache(maxsize=None)
def lie(word):
    if len(word) == 1:
        return {word: 1}
    left, right = standard_split(word)
    return bracket(lie(left), lie(right))


def weight(word):
    return (sum(WEIGHTS[i][0] for i in word),
            sum(WEIGHTS[i][1] for i in word))


def groups_of_lyndon(length):
    groups = {}
    for word in itertools.product(range(8), repeat=length):
        guard()
        if lyndon(word):
            groups.setdefault(weight(word), []).append(word)
    return groups


def word_counts(length):
    counts = {}
    for word in itertools.product(range(8), repeat=length):
        bump(counts, weight(word), 1)
    return counts


def witt_counts(length):
    counts = word_counts(length)
    correction = {}
    if length == 3:
        for i in range(8):
            a, b = WEIGHTS[i]
            bump(correction, (3 * a, 3 * b), 1)
    elif length == 4:
        for i, j in itertools.product(range(8), repeat=2):
            a = 2 * (WEIGHTS[i][0] + WEIGHTS[j][0])
            b = 2 * (WEIGHTS[i][1] + WEIGHTS[j][1])
            bump(correction, (a, b), 1)
    else:
        raise ValueError("unsupported Witt degree")
    result = {}
    for key in set(counts) | set(correction):
        numerator = counts.get(key, 0) - correction.get(key, 0)
        require(numerator % length == 0, "nonintegral Witt coefficient")
        if numerator:
            result[key] = numerator // length
    return result


def h_coefficient(a, b):
    return min(a, b) + 1 if a >= 0 and b >= 0 else 0


def relation_character(a, b):
    # X * P_{2,5}, including the seed's horizontal degree (1,0).
    a -= 1
    p, q = 2, 5
    d = p + q + 2
    return (h_coefficient(a, b) - h_coefficient(a - p - 1, b)
            - h_coefficient(a, b - q - 1)
            + h_coefficient(a - d, b - q - 1)
            + h_coefficient(a - p - 1, b - d)
            - h_coefficient(a - d, b - d))


def d_table(mutant=False):
    """Return constant and s coefficients of ad([f3,letter]) on V."""
    constant = [[{} for _ in range(8)] for _ in range(8)]
    slope = [[{} for _ in range(8)] for _ in range(8)]
    for j, (a, b) in enumerate(WEIGHTS):
        sign = -1 if mutant else 1
        constant[0][j] = {j: sign * (3 * a - 2)}
        slope[0][j] = {j: sign * b}
        constant[1][j] = scaled(E1[j], -3)
        slope[2][j] = scaled(E2[j], -1)
        slope[3][j] = scaled(E12[j], -1)
        constant[4][j] = scaled(E12[j], 3)
    return constant, slope


D0, D1 = d_table()


def delta_tensor(vector, mutant=False):
    """Move each grade-zero [f3,u_i] right through later tensor letters.

    In the associative enveloping algebra, commuting it past u_j contributes
    [ [f3,u_i], u_j ]; the residual rightmost grade-zero terms cancel for a
    homogeneous Lie vector of degree at least two.  No numerical interpolation
    enters: the two returned tensors are the constant and s coefficients.
    """
    tables = d_table(True) if mutant else (D0, D1)
    out = ({}, {})
    for word, coefficient in vector.items():
        require(len(word) >= 2, "delta requires degree at least two")
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                for power in (0, 1):
                    for replacement, multiplier in tables[power][word[i]][word[j]].items():
                        new_word = word[:i] + word[i + 1:j] + (replacement,) + word[j + 1:]
                        bump(out[power], new_word, coefficient * multiplier)
    return out


def d_action(letter, vector, power):
    table = D0 if power == 0 else D1
    return derivation(vector, table[letter])


@lru_cache(maxsize=None)
def delta_recursive(word):
    """Independent bracket-recursion evaluation of the same affine action."""
    require(len(word) >= 2, "recursive delta requires at least two letters")
    left, right = standard_split(word)
    answer = []
    for power in (0, 1):
        if len(left) == 1 and len(right) == 1:
            part = d_action(left[0], lie(right), power)
            axpy(part, d_action(right[0], lie(left), power), -1)
        elif len(left) == 1:
            part = d_action(left[0], lie(right), power)
            axpy(part, bracket(lie(left), delta_recursive(right)[power]), 1)
        elif len(right) == 1:
            part = bracket(delta_recursive(left)[power], lie(right))
            axpy(part, d_action(right[0], lie(left), power), -1)
        else:
            part = bracket(delta_recursive(left)[power], lie(right))
            axpy(part, bracket(lie(left), delta_recursive(right)[power]), 1)
        answer.append(part)
    return tuple(answer)


class FreeCoordinates:
    def __init__(self, words):
        self.words = list(words)
        self.span = Span(track=True)
        for word in self.words:
            require(self.span.add(lie(word)), "dependent Lyndon basis")

    def coordinates(self, vector):
        remainder, coefficients = self.span.reduce(vector)
        require(not remainder, "target is not in the complete free Lie space")
        return coefficients


class QuotientCoordinates:
    def __init__(self, relation, words):
        self.relation = relation
        self.space = Span(track=True)
        self.words = []
        for word in words:
            remainder, _ = relation.reduce(lie(word))
            if self.space.add(remainder):
                self.words.append(word)

    def coordinates(self, vector):
        remainder, _ = self.relation.reduce(vector)
        residue, coefficients = self.space.reduce(remainder)
        require(not residue, "target is outside its complete quotient basis")
        return coefficients


def rref(rows, ncols):
    a = [[Q(x) for x in row] for row in rows]
    require(all(len(row) == ncols for row in a), "nonrectangular matrix")
    pivots = []
    r = 0
    for c in range(ncols):
        guard()
        chosen = next((i for i in range(r, len(a)) if a[i][c]), None)
        if chosen is None:
            continue
        a[r], a[chosen] = a[chosen], a[r]
        divisor = a[r][c]
        for j in range(c, ncols):
            a[r][j] /= divisor
        for i in range(len(a)):
            if i != r and a[i][c]:
                coefficient = a[i][c]
                for j in range(c, ncols):
                    a[i][j] -= coefficient * a[r][j]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return a, pivots


def kernel(rows, ncols):
    reduced, pivots = rref(rows, ncols)
    pivot_set = set(pivots)
    result = []
    for free in range(ncols):
        if free in pivot_set:
            continue
        vector = {free: Q(1)}
        for i, pivot in enumerate(pivots):
            if reduced[i][free]:
                vector[pivot] = -reduced[i][free]
        result.append(vector)
    return result


def rank(rows, ncols):
    return len(rref(rows, ncols)[1])


def matrix_rows(columns, nrows):
    return [[columns[j].get(i, 0) for j in range(len(columns))]
            for i in range(nrows)]


def determinant_numeric(rows):
    a = [[Q(x) for x in row] for row in rows]
    n = len(a)
    require(all(len(row) == n for row in a), "nonsquare determinant")
    result = Q(1)
    for c in range(n):
        guard()
        pivot = next((i for i in range(c, n) if a[i][c]), None)
        if pivot is None:
            return Q(0)
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            result = -result
        value = a[c][c]
        result *= value
        for i in range(c + 1, n):
            if a[i][c]:
                factor = a[i][c] / value
                for j in range(c + 1, n):
                    a[i][j] -= factor * a[c][j]
                a[i][c] = Q(0)
    return result


# Polynomials are tuples of rational coefficients in ascending powers of s.
def poly(values):
    result = [Q(v) for v in values]
    while result and not result[-1]:
        result.pop()
    return tuple(result)


def pscale(a, k):
    return poly(k * x for x in a)


def psub(a, b):
    return poly((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
                for i in range(max(len(a), len(b))))


def pmul(a, b):
    if not a or not b:
        return ()
    result = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return poly(result)


def pdivmod(a, b):
    require(bool(b), "zero polynomial divisor")
    remainder = list(poly(a))
    quotient = [Q(0)] * max(0, len(remainder) - len(b) + 1)
    while remainder and len(remainder) >= len(b):
        guard()
        offset = len(remainder) - len(b)
        factor = remainder[-1] / b[-1]
        quotient[offset] += factor
        for i, value in enumerate(b):
            remainder[offset + i] -= factor * value
        while remainder and not remainder[-1]:
            remainder.pop()
    return poly(quotient), poly(remainder)


def pdivexact(a, b):
    quotient, remainder = pdivmod(a, b)
    require(not remainder, "Bareiss polynomial division was not exact")
    return quotient


def pderivative(a):
    return poly(i * a[i] for i in range(1, len(a)))


def peval(a, x):
    value = Q(0)
    for coefficient in reversed(a):
        value = value * x + coefficient
    return value


def bareiss(matrix):
    a = [[poly(cell) for cell in row] for row in matrix]
    n = len(a)
    require(n > 0 and all(len(row) == n for row in a), "bad Bareiss shape")
    if n == 1:
        return a[0][0]
    previous = poly((1,))
    sign = 1
    for k in range(n - 1):
        guard()
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return ()
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pk = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = psub(pmul(a[i][j], pk), pmul(a[i][k], a[k][j]))
                a[i][j] = pdivexact(numerator, previous)
            a[i][k] = ()
        previous = pk
    return pscale(a[-1][-1], sign)


def shift_at_four(a):
    if not a:
        return ()
    return poly(sum(a[j] * math.comb(j, k) * 4 ** (j - k)
                    for j in range(k, len(a))) for k in range(len(a)))


def sign_of(x):
    return (x > 0) - (x < 0)


def variations(signs):
    nonzero = [v for v in signs if v]
    return sum(a != b for a, b in zip(nonzero, nonzero[1:]))


def strings(a):
    return [str(x) for x in a]


def no_zero_certificate(p):
    """Certify nonvanishing on the CLOSED real ray [4,infinity)."""
    if not p:
        return {"kind": "INCONCLUSIVE_ZERO_POLYNOMIAL", "certified": False}
    endpoint = peval(p, 4)
    shifted = shift_at_four(p)
    if not endpoint:
        return {"kind": "INCONCLUSIVE_ENDPOINT_ZERO", "endpoint_s4": "0",
                "shifted_coefficients": strings(shifted), "certified": False}
    orientation = 1 if endpoint > 0 else -1
    oriented = pscale(shifted, orientation)
    if oriented and oriented[0] > 0 and all(x >= 0 for x in oriented):
        return {"kind": "NONNEGATIVE_SHIFTED_COEFFICIENTS",
                "orientation": orientation, "endpoint_s4": str(endpoint),
                "shifted_coefficients": strings(oriented), "certified": True}
    # Every normalization below is by a positive scalar and preserves signs.
    def normalize(v):
        return pscale(v, Q(1) / abs(v[-1])) if v else ()
    sequence = [normalize(p)]
    derivative = pderivative(sequence[0])
    if derivative:
        sequence.append(normalize(derivative))
        while True:
            guard()
            _, remainder = pdivmod(sequence[-2], sequence[-1])
            if not remainder:
                break
            sequence.append(normalize(pscale(remainder, -1)))
    endpoint_signs = [sign_of(peval(v, 4)) for v in sequence]
    infinity_signs = [sign_of(v[-1]) for v in sequence]
    left_variations = variations(endpoint_signs)
    right_variations = variations(infinity_signs)
    roots = left_variations - right_variations
    require(roots >= 0, "negative Sturm root count")
    return {"kind": "EXACT_STURM", "endpoint_s4": str(endpoint),
            "endpoint_is_root": False,
            "polynomials_ascending_s": [strings(v) for v in sequence],
            "endpoint_signs_zero_terms_omitted_in_variations": endpoint_signs,
            "positive_infinity_signs": infinity_signs,
            "variations_at_4": left_variations,
            "variations_at_positive_infinity": right_variations,
            "distinct_roots_in_open_4_infinity": roots,
            "certified": roots == 0}


def enc_word(word):
    return "".join(LETTERS[i] for i in word)


def enc_tensor(vector):
    return [[enc_word(word), str(coefficient)]
            for word, coefficient in sorted(vector.items()) if coefficient]


def enc_sparse(vector):
    return [[index, str(value)] for index, value in sorted(vector.items()) if value]


def enc_matrix(rows):
    return [[i, j, str(value)] for i, row in enumerate(rows)
            for j, value in enumerate(row) if value]


def row_selections(rows, ncols):
    """An explicit bounded search; untried minors remain unadjudicated."""
    echelon = Span()
    chosen = []
    for i, row in enumerate(rows):
        if echelon.add({j: x for j, x in enumerate(row) if x}):
            chosen.append(i)
            if len(chosen) == ncols:
                break
    if len(chosen) != ncols:
        return
    selected = tuple(sorted(chosen))
    yield selected
    seen = {selected}
    for alternative in range(len(rows)):
        if alternative in selected:
            continue
        for slot in range(ncols):
            new = tuple(sorted(selected[:slot] + (alternative,) + selected[slot + 1:]))
            if new not in seen:
                seen.add(new)
                yield new


def run(result):
    result["stage"] = "constructing complete free Lie bases"
    free3 = groups_of_lyndon(3)
    free4 = groups_of_lyndon(4)
    w3, w4 = witt_counts(3), witt_counts(4)
    require({k: len(v) for k, v in free3.items()} == w3, "grade-three Witt mismatch")
    require({k: len(v) for k, v in free4.items()} == w4, "grade-four Witt mismatch")
    require(sum(w3.values()) == 168 and sum(w4.values()) == 1008,
            "free Lie total dimension mismatch")
    basis3 = {key: FreeCoordinates(words) for key, words in sorted(free3.items())}
    result["free_dimensions"] = {"grade3": 168, "grade4": 1008}
    result["stage"] = "closing the entire first-seed relation"
    x, a = {(0,): 1}, {(1,): 1}
    seed = bracket(x, bracket(x, bracket(x, a)))
    require(seed and not derivation(seed, F1) and not derivation(seed, F2),
            "seed is not a nonzero simultaneous lowest vector")
    pending = [((1, 0), seed)]
    relation = {}
    relation_generators = {}
    cursor = 0
    while cursor < len(pending):
        guard()
        key, vector = pending[cursor]
        cursor += 1
        if not vector:
            continue
        span = relation.setdefault(key, Span())
        if span.add(vector):
            relation_generators.setdefault(key, []).append(vector)
            for table, shift in ((E1, (1, 0)), (E2, (0, 1))):
                raised = derivation(vector, table)
                if raised:
                    pending.append(((key[0] + shift[0], key[1] + shift[1]), raised))
    require(sum(space.count for space in relation.values()) == 81,
            "whole relation dimension is not 81")
    for a0 in range(9):
        for b0 in range(9):
            key = (a0, b0)
            count = relation[key].count if key in relation else 0
            require(count == relation_character(a0, b0), "relation character mismatch")
    empty = Span()
    for key, generators in relation_generators.items():
        for vector in generators:
            for table, shift in ((E1, (1, 0)), (E2, (0, 1)),
                                 (F1, (-1, 0)), (F2, (0, -1))):
                target = (key[0] + shift[0], key[1] + shift[1])
                remainder, _ = relation.get(target, empty).reduce(derivation(vector, table))
                require(not remainder, "whole relation is not Levi stable")
            c0, c1 = delta_tensor(vector)
            require(not c0 and not c1, "F3 does not kill the whole relation identically")
    result["relation"] = {
        "seed": enc_tensor(seed), "dimension": 81,
        "character": "X*P_(2,5)",
        "basis_by_weight": [{"weight": list(key),
                             "ordered_tensor_generators": [enc_tensor(v) for v in generators]}
                            for key, generators in sorted(relation_generators.items())],
        "E1_E2_F1_F2_stable": True, "F3_constant_and_s_parts_vanish": True}
    result["stage"] = "constructing the whole grade-four quotient"
    quotient = {key: QuotientCoordinates(relation.get(key, empty), words)
                for key, words in sorted(free4.items())}
    require(sum(len(space.words) for space in quotient.values()) == 927,
            "whole grade-four quotient dimension mismatch")
    result["quotient"] = {
        "dimension": 927,
        "basis_by_weight": [{"weight": list(key),
                             "relation_dimension": relation[key].count if key in relation else 0,
                             "quotient_lyndon_words": [enc_word(w) for w in space.words]}
                            for key, space in sorted(quotient.items())]}
    positions = ((1, 2, 4, 1, 4), (2, 1, 1, 4, 4),
                 (2, 2, 2, 2, 7), (2, 3, 3, 0, 6),
                 (3, 2, 0, 3, 6), (3, 3, 1, 1, 8),
                 (4, 4, 0, 0, 1))
    result["types"] = []
    overall = True
    copy_control = None
    for a0, b0, p, q, expected in positions:
        guard()
        key = (a0, b0)
        result["stage"] = "complete lowest space " + str(key)
        source = quotient[key]
        n = len(source.words)
        lower_columns = []
        lower_sizes = []
        for table, shift in ((F1, (-1, 0)), (F2, (0, -1))):
            target_key = (a0 + shift[0], b0 + shift[1])
            target = quotient.get(target_key)
            cols = []
            for word in source.words:
                image = derivation(lie(word), table)
                if target is None:
                    require(not image, "missing nonzero lowering target")
                    cols.append({})
                else:
                    cols.append(target.coordinates(image))
            lower_columns.append(cols)
            lower_sizes.append(len(target.words) if target else 0)
        stacked = (matrix_rows(lower_columns[0], lower_sizes[0]) +
                   matrix_rows(lower_columns[1], lower_sizes[1]))
        lows = kernel(stacked, n)
        require(len(lows) == expected, "complete lowest dimension mismatch")
        target = basis3.get(key)
        require(target is not None, "missing grade-three F3 target")
        constant_columns, slope_columns, low_tensors = [], [], []
        for coefficients in lows:
            guard()
            vector = {}
            independent0, independent1 = {}, {}
            for j, coefficient in coefficients.items():
                word = source.words[j]
                axpy(vector, lie(word), coefficient)
                r0, r1 = delta_recursive(word)
                axpy(independent0, r0, coefficient)
                axpy(independent1, r1, coefficient)
            computed0, computed1 = delta_tensor(vector)
            require(computed0 == independent0 and computed1 == independent1,
                    "tensor and independent bracket-recursion F3 disagree")
            constant_columns.append(target.coordinates(computed0))
            slope_columns.append(target.coordinates(computed1))
            low_tensors.append(enc_tensor(vector))
        rows0 = matrix_rows(constant_columns, len(target.words))
        rows1 = matrix_rows(slope_columns, len(target.words))
        rows4 = [[rows0[i][j] + 4 * rows1[i][j] for j in range(expected)]
                 for i in range(len(rows0))]
        rows5 = [[rows0[i][j] + 5 * rows1[i][j] for j in range(expected)]
                 for i in range(len(rows0))]
        rank4, rank5 = rank(rows4, expected), rank(rows5, expected)
        if rank4 != expected or rank5 != expected:
            overall = False
        record = {"weight": [a0, b0], "levi_type": [p, q],
                  "quotient_dimension": n, "lowest_dimension": len(lows),
                  "expected_lowest_dimension": expected,
                  "lowest_quotient_coordinates": [enc_sparse(v) for v in lows],
                  "lowest_ordered_tensors": low_tensors,
                  "grade3_target_lyndon_words": [enc_word(w) for w in target.words],
                  "F3_constant_sparse": enc_matrix(rows0),
                  "F3_s_coefficient_sparse": enc_matrix(rows1),
                  "independent_bracket_recursion_agrees": True,
                  "fixed_sample": {"s4_rank": rank4, "s5_rank": rank5,
                                   "expected_rank_at_both": expected},
                  "minor_attempts": [], "certificate_status": "INCONCLUSIVE"}
        result["types"].append(record)
        if copy_control is None and expected > 1 and rank4 == expected:
            one_rank = rank([[row[0]] for row in rows4], 1)
            copy_control = {"weight": [a0, b0], "whole_rank": rank4,
                            "one_copy_rank": one_rank,
                            "detected": one_rank < rank4}
        if rank4 != expected:
            record["reason"] = "no full-column minor at s=4 in constructed map"
            continue
        valid_attempts = 0
        for indices in row_selections(rows4, expected):
            guard()
            numeric4 = determinant_numeric([rows4[i] for i in indices])
            if not numeric4:
                continue
            valid_attempts += 1
            minor = [[(rows0[i][j], rows1[i][j]) for j in range(expected)]
                     for i in indices]
            determinant = bareiss(minor)
            require(peval(determinant, 4) == numeric4,
                    "Bareiss polynomial and independent s=4 determinant disagree")
            numeric5 = determinant_numeric([rows5[i] for i in indices])
            require(peval(determinant, 5) == numeric5,
                    "Bareiss polynomial and independent s=5 determinant disagree")
            certificate = no_zero_certificate(determinant)
            attempt = {"row_indices": list(indices),
                       "determinant_coefficients_ascending_s": strings(determinant),
                       "determinant_at_s4": str(numeric4),
                       "determinant_at_s5": str(numeric5),
                       "nonzero_on_closed_real_s_ge_4": certificate}
            record["minor_attempts"].append(attempt)
            if certificate["certified"]:
                record["certificate_status"] = "CERTIFIED_CONDITIONAL_ON_SOURCE_AND_IMPORTS"
                break
            if valid_attempts >= 64:
                break
        if record["certificate_status"] != "CERTIFIED_CONDITIONAL_ON_SOURCE_AND_IMPORTS":
            overall = False
            record["reason"] = ("no certified minor among the greedy and at most 64 "
                                "full-at-s4 single-row replacements; no rank failure inferred")
    result["stage"] = "running in-source mutation controls"
    xb = bracket({(0,): 1}, {(2,): 1})
    good0, good1 = delta_tensor(xb)
    bad0, bad1 = delta_tensor(xb, mutant=True)
    good, bad = dict(good0), dict(bad0)
    axpy(good, good1, 4)
    axpy(bad, bad1, 4)
    cartan_detected = good == {(2,): 6} and bad == {(2,): 2}
    translated = derivation(seed, E2)
    omitted_relation = Span()
    # At weight (1,1), the unraised seed-only subspace is zero.
    omitted_remainder, _ = omitted_relation.reduce(translated)
    whole_remainder, _ = relation.get((1, 1), empty).reduce(translated)
    whole_control = bool(translated) and bool(omitted_remainder) and not whole_remainder
    result["controls"] = {
        "reversed_cartan": {"correct_at_s4": enc_tensor(good),
                            "mutant_at_s4": enc_tensor(bad),
                            "detected": cartan_detected},
        "omit_levi_translates": {"E2_seed": enc_tensor(translated),
                                 "missing_from_seed_only_weight_1_1": bool(omitted_remainder),
                                 "contained_in_whole_relation": not whole_remainder,
                                 "detected": whole_control},
        "discard_copy_multiplicity": copy_control or {"detected": False}}
    require(cartan_detected and whole_control and copy_control is not None
            and copy_control["detected"], "one or more mutation controls not detected")
    result["stage"] = "complete"
    result["status"] = ("CERTIFIED_SEVEN_SYMBOLIC_MINORS_CONDITIONAL"
                        if overall else "INCONCLUSIVE")


result = {
    "status": "INCOMPLETE", "stage": "initialization", "failures": [],
    "coverage": {
        "parameter_domain": "r=3, integer s>=4; polynomial nonvanishing tested on real s>=4",
        "whole_grade4_quotient": "eight-letter free Lie quotient by the complete first seed module",
        "second_seed": "grade at least five on the stated integer domain",
        "types": [[1, 2], [2, 1], [2, 2], [2, 3], [3, 2], [3, 3], [4, 4]],
        "imports": ["actual ordinary free-Lie source and ordered tensor embedding",
                    "full Cartan realization and whole positive/negative Serre-ideal bridge",
                    "the displayed Levi and Chevalley F3 letter actions",
                    "Lyndon basis theorem and characteristic-zero exact arithmetic"],
        "not_claimed": ["grade-four radical theorem or ideal-union conclusion",
                        "r=1 or r=2", "s<=3", "higher grades or global J=tau",
                        "source identity, novelty, human/family/kernel verification"],
        "search_limit_per_type": "greedy minor plus up to 64 full-at-s4 single-row replacements",
        "selected_minor_zero": "never by itself a rank failure",
        "cooperative_seconds": 40,
        "scientific_execution_of_this_source": "only upon separate parent GO"}}
try:
    run(result)
except Interrupted as exc:
    result["status"] = "INCOMPLETE"
    result["failures"].append(str(exc))
except Exception as exc:
    result["status"] = "FAILURE"
    result["failures"].append(type(exc).__name__ + ": " + str(exc))
finally:
    result["elapsed_seconds"] = time.monotonic() - START
    print(json.dumps(result, sort_keys=True, separators=(",", ":")), flush=True)
