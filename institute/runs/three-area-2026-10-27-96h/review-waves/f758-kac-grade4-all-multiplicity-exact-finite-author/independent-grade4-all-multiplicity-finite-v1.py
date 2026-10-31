#!/usr/bin/env python3
"""UNRUN proposal: ordered-tensor grade-four multiplicity and F3 finite assay.

Fixed coverage is r=3, s=4 and s=5 only.  Stdout is the sole output.
Run only after a separate parent whole-read and explicit bounded GO.  This
source does not establish a radical, any universal parameter assertion, or
any formal/human/independent-family/novelty conclusion.
"""
from collections import defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json
import signal
import sys
import time

START = time.monotonic()
DEADLINE = START + 40.0
STOP_SIGNAL = None
STAGE = "initializing"


class Incomplete(Exception):
    pass


class CheckFailure(Exception):
    pass


def on_signal(signum, _frame):
    global STOP_SIGNAL
    STOP_SIGNAL = signum


signal.signal(signal.SIGTERM, on_signal)
signal.signal(signal.SIGINT, on_signal)


def tick():
    if STOP_SIGNAL is not None:
        raise Incomplete("signal " + str(STOP_SIGNAL))
    if time.monotonic() >= DEADLINE:
        raise Incomplete("40-second cooperative deadline")


def require(condition, reason):
    if not condition:
        raise CheckFailure(reason)


# Letters are actual free generators, not products of 3-by-3 matrices.
NAMES = "xabcdefg"
DEGREE = ((0, 0), (1, 0), (0, 1), (1, 1),
          (1, 1), (2, 1), (1, 2), (2, 2))
# Each dictionary is an actual Levi action on a letter, in the ordered basis.
E1 = ({1: 1}, {}, {3: 1}, {5: -2}, {5: -1}, {}, {7: 1}, {})
E2 = ({2: 1}, {4: 1}, {}, {6: 1}, {6: 2}, {7: -1}, {}, {})
F1 = ({}, {0: 1}, {}, {2: 2}, {2: 1}, {3: -1}, {}, {6: 1})
F2 = ({}, {}, {0: 1}, {1: 1}, {1: 2}, {}, {4: 1}, {5: -1})
E12 = ({3: 1, 4: -1}, {5: -1}, {6: -1}, {7: -1},
       {7: 1}, {}, {}, {})
POSITIONS = ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2),
             (2, 0), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3), (4, 4))
EXPECTED_FREE = (0, 1, 0, 1, 3, 4, 0, 4, 7, 6, 6, 8, 1)
RESIDUAL = ((1, 2), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3), (4, 4))


def add_term(out, word, value):
    if value:
        out[word] = out.get(word, 0) + value
        if not out[word]:
            del out[word]


def combine(vectors, coefficients):
    out = {}
    for vec, coef in zip(vectors, coefficients):
        if coef:
            for word, value in vec.items():
                add_term(out, word, coef * value)
    return out


def bracket(left, right):
    out = {}
    for a, av in left.items():
        for b, bv in right.items():
            add_term(out, a + b, av * bv)
            add_term(out, b + a, -av * bv)
    return out


def action(vector, table):
    out = {}
    for word, coefficient in vector.items():
        for i, letter in enumerate(word):
            for replacement, scale in table[letter].items():
                add_term(out, word[:i] + (replacement,) + word[i + 1:],
                         coefficient * scale)
    return out


def delta(letter, other, r, s, bad_cartan=False):
    if letter == 0:
        a, b = DEGREE[other]
        coefficient = r * a + s * b - 2
        if bad_cartan:
            coefficient = -coefficient
        return {other: coefficient} if coefficient else {}
    if letter == 1:
        return {k: -r * v for k, v in E1[other].items()}
    if letter == 2:
        return {k: -s * v for k, v in E2[other].items()}
    if letter == 3:
        return {k: -s * v for k, v in E12[other].items()}
    if letter == 4:
        return {k: r * v for k, v in E12[other].items()}
    return {}


def f3(vector, r, s, bad_cartan=False):
    # Move each degree-zero delta past every later ordered tensor letter.
    # On a Lie element the uncommuted terminal degree-zero terms cancel.
    out = {}
    for word, coefficient in vector.items():
        for i, letter in enumerate(word):
            for j in range(i + 1, len(word)):
                for replacement, scale in delta(letter, word[j], r, s,
                                                 bad_cartan).items():
                    newword = word[:i] + word[i + 1:j] + (replacement,) + word[j + 1:]
                    add_term(out, newword, coefficient * scale)
    return out


def weight(word):
    return (sum(DEGREE[k][0] for k in word),
            sum(DEGREE[k][1] for k in word))


def homogeneous(vector, expected):
    return all(weight(word) == expected for word in vector)


def packed(vector):
    tick()
    return [["".join(NAMES[i] for i in word), str(coefficient)]
            for word, coefficient in sorted(vector.items()) if coefficient]


class Span:
    # Insertion-order echelon rows: every new row is zero at all old pivots.
    def __init__(self):
        self.rows = []

    def reduce(self, vector):
        value = dict(vector)
        coefficients = []
        for pivot, row in self.rows:
            tick()
            coefficient = value.get(pivot, 0)
            coefficients.append(coefficient)
            if coefficient:
                for word, entry in row.items():
                    add_term(value, word, -coefficient * entry)
        return value, coefficients

    def insert(self, vector):
        value, _ = self.reduce(vector)
        if not value:
            return None
        pivot = min(value)
        coefficient = value[pivot]
        row = {word: Fraction(entry) / coefficient for word, entry in value.items()}
        self.rows.append((pivot, row))
        return row

    def contains(self, vector):
        remainder, _ = self.reduce(vector)
        return not remainder


def is_lyndon(word):
    return all(word < word[i:] for i in range(1, len(word)))


@lru_cache(maxsize=None)
def lyndon_tensor(word):
    if len(word) == 1:
        return {word: 1}
    # Longest proper Lyndon suffix gives the standard Lyndon factorization.
    split = next(i for i in range(1, len(word)) if is_lyndon(word[i:]))
    return bracket(lyndon_tensor(word[:split]), lyndon_tensor(word[split:]))


def build_free(n):
    grouped = defaultdict(list)
    for word in product(range(8), repeat=n):
        tick()
        if is_lyndon(word):
            vector = lyndon_tensor(word)
            require(bool(vector), "zero Lyndon tensor")
            grouped[weight(word)].append(vector)
    return dict(grouped)


def multiply(a, b):
    out = {}
    for (i, j), av in a.items():
        for (k, l), bv in b.items():
            add_term(out, (i + k, j + l), av * bv)
    return out


def power(poly, n):
    result = {(0, 0): 1}
    for _ in range(n):
        result = multiply(result, poly)
    return result


def lie_character(n):
    h = {}
    for w in DEGREE:
        add_term(h, w, 1)
    if n == 4:
        first, second, denominator = power(h, 4), power({(2*a, 2*b): c for (a, b), c in h.items()}, 2), 4
    elif n == 3:
        first, second, denominator = power(h, 3), {(3*a, 3*b): c for (a, b), c in h.items()}, 3
    else:
        raise CheckFailure("unexpected Lie degree")
    keys = set(first) | set(second)
    out = {}
    for key in keys:
        numerator = first.get(key, 0) - second.get(key, 0)
        require(numerator % denominator == 0, "nonintegral Witt coefficient")
        if numerator:
            out[key] = numerator // denominator
    return out


def lowest_multiplicity(character, a, b):
    def c(i, j):
        return character.get((i, j), 0)
    return (c(a, b) - c(a-1, b) - c(a, b-1) + c(a-2, b-1)
            + c(a-1, b-2) - c(a-2, b-2))


def rel_expected(a, b):
    # X times the Weyl character of the lowest (2,5) module.
    a -= 1
    numerator = ((0, 0, 1), (3, 0, -1), (0, 6, -1),
                 (9, 6, 1), (3, 9, 1), (9, 9, -1))
    return sum(sign * (min(a-u, b-v) + 1)
               for u, v, sign in numerator if a >= u and b >= v)


def relation_module():
    x, a = {(0,): 1}, {(1,): 1}
    seed = bracket(x, bracket(x, bracket(x, a)))
    require(bool(seed) and homogeneous(seed, (1, 0)), "invalid first seed")
    spaces = defaultdict(Span)
    queue = deque([((1, 0), seed)])
    while queue:
        tick()
        w, vector = queue.popleft()
        require(homogeneous(vector, w), "relation changed its weight")
        row = spaces[w].insert(vector)
        if row is None:
            continue
        for table, increment in ((E1, (1, 0)), (E2, (0, 1))):
            image = action(row, table)
            if image:
                queue.append(((w[0] + increment[0], w[1] + increment[1]), image))
    return seed, dict(spaces)


def rank_of_columns(columns):
    span = Span()
    for column in columns:
        span.insert({(i,): c for i, c in enumerate(column) if c})
    return len(span.rows)


def nullspace(columns, nrows):
    ncols = len(columns)
    matrix = [[Fraction(columns[j][i]) for j in range(ncols)] for i in range(nrows)]
    row = 0
    pivots = []
    for col in range(ncols):
        tick()
        pivot = next((i for i in range(row, nrows) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        scale = matrix[row][col]
        matrix[row] = [x / scale for x in matrix[row]]
        for i in range(nrows):
            if i != row and matrix[i][col]:
                scale = matrix[i][col]
                matrix[i] = [a - scale*b for a, b in zip(matrix[i], matrix[row])]
        pivots.append(col)
        row += 1
        if row == nrows:
            break
    free = [j for j in range(ncols) if j not in pivots]
    answer = []
    for col in free:
        v = [Fraction(0) for _ in range(ncols)]
        v[col] = Fraction(1)
        for i, pivot in enumerate(pivots):
            v[pivot] = -matrix[i][col]
        answer.append(v)
    return answer


def build_space(n, w, free, relations):
    span = Span()
    nrel = 0
    if n == 4 and w in relations:
        for _, vector in relations[w].rows:
            require(span.insert(vector) is not None, "dependent relation rows")
            nrel += 1
    quotient = []
    for vector in free.get(w, ()):
        row = span.insert(vector)
        if row is not None:
            quotient.append(row)
    return span, nrel, quotient


def coordinates(space, vector):
    span, nrel, _ = space
    remainder, coefficients = span.reduce(vector)
    require(not remainder, "tensor outside target Lie space")
    return coefficients[nrel:]


def vector_strings(vector):
    return [str(x) for x in vector]


def run(report):
    global STAGE
    STAGE = "character and independent ordered-tensor free bases"
    char3, char4 = lie_character(3), lie_character(4)
    free3, free4 = build_free(3), build_free(4)
    for character, spaces, expected_total in ((char3, free3, 168), (char4, free4, 1008)):
        require(sum(character.values()) == expected_total, "Witt total dimension")
        require(set(character) == set(spaces), "Witt/Lyndon weight support mismatch")
        for w, coefficient in character.items():
            require(len(spaces[w]) == coefficient, "Witt/Lyndon weight mismatch")
    positions = tuple((a, b) for a in range(9) for b in range(9)
                      if 4 - 2*a + b >= 0 and 4 + a - 2*b >= 0)
    require(positions == POSITIONS, "13-position enumeration")
    multiplicities = tuple(lowest_multiplicity(char4, *w) for w in positions)
    require(multiplicities == EXPECTED_FREE, "13 complete free multiplicities")
    dimension = sum(m * (5-2*a+b) * (5+a-2*b) * (10-a-b) // 2
                    for (a, b), m in zip(positions, multiplicities))
    require(dimension == 1008, "Weyl dimensions do not sum to 1008")
    report["character"] = {
        "grade3": [[list(w), c] for w, c in sorted(char3.items())],
        "grade4": [[list(w), c] for w, c in sorted(char4.items())],
        "positions": [{"ab": list(w), "pq": [4-2*w[0]+w[1], 4+w[0]-2*w[1]],
                       "free": m, "actual_r3": m - (w == (1, 0))}
                      for w, m in zip(positions, multiplicities)],
        "free_total": 1008, "expected_quotient_total": 927}
    report["completed_stages"].append(STAGE)

    STAGE = "entire first-seed Levi module and descent"
    seed, relations = relation_module()
    require(sum(len(sp.rows) for sp in relations.values()) == 81, "whole relation dimension")
    for a in range(9):
        for b in range(9):
            actual = len(relations[(a, b)].rows) if (a, b) in relations else 0
            require(actual == rel_expected(a, b), "whole relation Weyl weight mismatch")
    for w, space in relations.items():
        for _, vector in space.rows:
            tick()
            for table, dw in ((F1, (-1, 0)), (F2, (0, -1))):
                image = action(vector, table)
                target = relations.get((w[0] + dw[0], w[1] + dw[1]))
                require(not image or (target is not None and target.contains(image)),
                        "relation module not Levi-lowering stable")
            for s in (4, 5):
                require(not f3(vector, 3, s), "F3 does not annihilate whole relation")
    report["first_relation"] = {
        "seed": packed(seed), "dimension": 81,
        "weight_bases": [{"ab": list(w), "basis": [packed(v) for _, v in sp.rows]}
                         for w, sp in sorted(relations.items())],
        "grade3_relation": "none for the two fixed parameter points",
        "second_seed": "grade >= 5 for s=4,5"}
    report["completed_stages"].append(STAGE)

    STAGE = "negative-Cartan and whole-module mutation controls"
    x, b = {(0,): 1}, {(2,): 1}
    xb = bracket(x, b)
    correct = f3(xb, 3, 4)
    mutant = f3(xb, 3, 4, bad_cartan=True)
    require(correct == {(2,): 6}, "negative-Cartan baseline identity")
    require(mutant == {(2,): 2} and mutant != correct,
            "negative-Cartan mutation not detected for intended coefficient")
    translated = action(seed, E2)
    relation11 = relations.get((1, 1))
    seed_only11 = Span()  # The sole unraised seed has weight (1,0), not (1,1).
    require(translated and relation11 is not None and relation11.contains(translated),
            "whole-module translated relation absent")
    require(len(relation11.rows) == 1 and not seed_only11.contains(translated),
            "seed-only mutation did not lose translated relation")
    report["controls"] = {
        "negative_cartan": {"status": "DETECTED", "correct": packed(correct),
                            "mutant": packed(mutant), "witness": "F3([x,b]) at (3,4)"},
        "whole_module": {"status": "DETECTED", "weight": [1, 1],
                         "full_relation_rank": len(relation11.rows),
                         "seed_only_rank": len(seed_only11.rows),
                         "omitted_E2_seed": packed(translated)}}
    report["completed_stages"].append(STAGE)

    cache = {}
    def get_space(n, w):
        key = (n, w)
        if key not in cache:
            cache[key] = build_space(n, w, free4 if n == 4 else free3, relations)
            expected = (char4.get(w, 0) - (len(relations[w].rows) if w in relations else 0)
                        if n == 4 else char3.get(w, 0))
            require(len(cache[key][2]) == expected, "quotient dimension mismatch")
        return cache[key]

    report["types"] = []
    selected_control = None
    for w in RESIDUAL:
        STAGE = "full lowest space and both F3 maps at " + str(w)
        tick()
        source = get_space(4, w)
        lower1 = get_space(4, (w[0] - 1, w[1]))
        lower2 = get_space(4, (w[0], w[1] - 1))
        target = get_space(3, w)
        cols = []
        for vector in source[2]:
            cols.append(coordinates(lower1, action(vector, F1)) +
                        coordinates(lower2, action(vector, F2)))
        kernels = nullspace(cols, len(lower1[2]) + len(lower2[2]))
        expected = multiplicities[POSITIONS.index(w)]
        require(len(kernels) == expected, "whole lowest-copy nullity mismatch")
        lowest = [combine(source[2], vector) for vector in kernels]
        for vector in lowest:
            require(vector and homogeneous(vector, w), "invalid lowest tensor")
            require(not any(coordinates(lower1, action(vector, F1))), "F1 kernel failure")
            require(not any(coordinates(lower2, action(vector, F2))), "F2 kernel failure")
        maps = {}
        for s in (4, 5):
            images = [coordinates(target, f3(vector, 3, s)) for vector in lowest]
            rank = rank_of_columns(images)
            maps[str(s)] = {"rank": rank, "columns": [vector_strings(v) for v in images]}
            if selected_control is None and rank >= 2:
                chosen = next(i for i, image in enumerate(images) if any(image))
                mutant_rank = rank_of_columns([images[chosen]])
                require(mutant_rank == 1 and mutant_rank < rank,
                        "copy-selection mutation did not lose image rank")
                selected_control = {"status": "DETECTED", "weight": list(w), "s": s,
                                    "whole_lowest_dimension": len(lowest),
                                    "selected_basis_index": chosen,
                                    "whole_image_rank": rank,
                                    "selected_image_rank": mutant_rank}
        report["types"].append({
            "ab": list(w), "pq": [4-2*w[0]+w[1], 4+w[0]-2*w[1]],
            "grade4_quotient_dimension": len(source[2]),
            "grade4_quotient_basis": [packed(v) for v in source[2]],
            "full_lowest_dimension": len(lowest),
            "lowest_coordinates_in_quotient": [vector_strings(v) for v in kernels],
            "lowest_ordered_tensors": [packed(v) for v in lowest],
            "grade3_target_basis": [packed(v) for v in target[2]],
            "F3_by_s_columns_in_grade3_target_basis": maps})
        report["completed_stages"].append(STAGE)
    require(selected_control is not None, "no actual multi-copy image available for mutation")
    report["controls"]["copy_multiplicity"] = selected_control
    report["status"] = "PASS_FINITE_CHECKS_ONLY"


report = {
    "status": "INCOMPLETE",
    "coverage_requested": {
        "parameters": [[3, 4], [3, 5]], "free_character": "all 13 lowest positions and all weights",
        "whole_relation": "all 81 ordered-tensor directions, not merely its seed",
        "lowest_spaces_and_F3": [list(w) for w in RESIDUAL],
        "arithmetic": "exact rational; genuine ordered tensor concatenation"},
    "completed_stages": [],
    "not_established": ["universal s", "entire grade-four radical", "global J=tau",
                        "formal/kernel, human or independent-family verification",
                        "original source identity", "novelty"]}
exit_code = 0
try:
    run(report)
except Incomplete as exc:
    report["status"] = "INCOMPLETE"
    report["reason"] = str(exc)
    exit_code = 2
except Exception as exc:
    report["status"] = "FAILURE"
    report["reason"] = type(exc).__name__ + ": " + str(exc)
    exit_code = 1
report["last_stage"] = STAGE
report["elapsed_seconds_before_json"] = time.monotonic() - START
sys.stdout.write(json.dumps(report, separators=(",", ":"), sort_keys=True) + "\n")
sys.exit(exit_code)
