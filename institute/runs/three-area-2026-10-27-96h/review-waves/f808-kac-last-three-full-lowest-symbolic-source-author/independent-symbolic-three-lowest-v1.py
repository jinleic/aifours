#!/usr/bin/env python3
"""UNRUN proposal: exact complete-lowest F3 pencils for three r=3 types.

No input, subprocess, network or filesystem access. JSON Lines on stdout only.
The parent must whole-read and separately authorize any execution. A cooperative
39-second stop leaves a one-second margin under the requested 40-second limit;
external supervision and continuous output capture are the parent's duties.
"""

from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import gcd
import json
import signal
import sys
import time

START = time.monotonic()
DEADLINE = START + 39.0
STOP_SIGNAL = None
COMPLETED = []
CONTEXTS = []
LETTERS = "xabcdefg"
DEGREES = ((0, 0), (1, 0), (0, 1), (1, 1), (1, 1), (2, 1), (1, 2), (2, 2))
TARGETS = (((2, 3), (3, 0), 6), ((3, 2), (0, 3), 6), ((3, 3), (1, 1), 8))

# Tables are column actions on the actual eight-letter Levi module, not
# products of matrices in the free Lie algebra.
E1 = ({1: 1}, {}, {3: 1}, {5: -2}, {5: -1}, {}, {7: 1}, {})
E2 = ({2: 1}, {4: 1}, {}, {6: 1}, {6: 2}, {7: -1}, {}, {})
F1 = ({}, {0: 1}, {}, {2: 2}, {2: 1}, {3: -1}, {}, {6: 1})
F2 = ({}, {}, {0: 1}, {1: 1}, {1: 2}, {}, {4: 1}, {5: -1})


class Stopped(Exception):
    pass


class CheckFailure(Exception):
    pass


def latch(signum, _frame):
    global STOP_SIGNAL
    STOP_SIGNAL = signum


def guard():
    if STOP_SIGNAL is not None:
        raise Stopped("signal " + str(STOP_SIGNAL))
    if time.monotonic() >= DEADLINE:
        raise Stopped("cooperative 39-second deadline")


def require(condition, message):
    if not condition:
        raise CheckFailure(message)


def emit(record):
    sys.stdout.write(json.dumps(record, sort_keys=True, separators=(",", ":")))
    sys.stdout.write("\n")
    sys.stdout.flush()


def put(d, key, value):
    if value:
        value += d.get(key, 0)
        if value:
            d[key] = value
        else:
            d.pop(key, None)


def add_scaled(dst, src, factor):
    if factor:
        for k, v in src.items():
            put(dst, k, factor * v)


def weight(word):
    return (sum(DEGREES[i][0] for i in word), sum(DEGREES[i][1] for i in word))


def bracket(left, right):
    out = {}
    for u, a in left.items():
        guard()
        for v, b in right.items():
            put(out, u + v, a * b)
            put(out, v + u, -a * b)
    return out


def lyndon(word):
    return all(word < word[i:] for i in range(1, len(word)))


@lru_cache(maxsize=None)
def lyndon_bracket(word):
    if len(word) == 1:
        return {word: 1}
    # The first Lyndon suffix is the longest proper Lyndon suffix.
    for i in range(1, len(word)):
        if lyndon(word[i:]):
            return bracket(lyndon_bracket(word[:i]), lyndon_bracket(word[i:]))
    raise CheckFailure("missing standard Lyndon factorization")


def action(table, vector):
    out = {}
    for word, coefficient in vector.items():
        guard()
        for i, letter in enumerate(word):
            for replacement, c in table[letter].items():
                put(out, word[:i] + (replacement,) + word[i + 1:], coefficient * c)
    return out


def letter_compose(first, second, letter):
    out = {}
    for middle, b in second[letter].items():
        for last, a in first[middle].items():
            put(out, last, a * b)
    return out


def commutator_on_letter(letter):
    out = letter_compose(E1, E2, letter)
    add_scaled(out, letter_compose(E2, E1, letter), -1)
    return out


def degree_zero_action(u, v, part, reverse_cartan=False):
    """[f3,u] acting on v, coefficient of t**part for s=4+t."""
    if u == 0:
        i, j = DEGREES[v]
        value = (3 * i + 4 * j - 2) if part == 0 else j
        if reverse_cartan:
            value = -value
        return {v: value} if value else {}
    if u == 1 and part == 0:
        return {k: -3 * c for k, c in E1[v].items()}
    if u == 2:
        factor = -4 if part == 0 else -1
        return {k: factor * c for k, c in E2[v].items()}
    if u == 3:
        factor = -4 if part == 0 else -1
        return {k: factor * c for k, c in commutator_on_letter(v).items()}
    if u == 4 and part == 0:
        return {k: 3 * c for k, c in commutator_on_letter(v).items()}
    return {}


def contract(vector, part, reverse_cartan=False):
    """Actual F3 on a Lie tensor: move each grade-zero term to the right.

    On an associative word only pairs i<j contribute: [f3,u_i] acts
    as a grade-zero derivation on u_j. The remaining term at the right
    annihilates the cyclic vacuum. Restricted to Lie words this is exactly
    delta[u,v]=D_u(v)-D_v(u) and its bracket derivation recursion.
    """
    out = {}
    for word, coefficient in vector.items():
        guard()
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                for replacement, c in degree_zero_action(word[i], word[j], part, reverse_cartan).items():
                    new = word[:i] + word[i + 1:j] + (replacement,) + word[j + 1:]
                    put(out, new, coefficient * c)
    return out


class Span:
    """Sparse rational echelon basis indexed by its least nonzero row."""

    def __init__(self):
        self.pivots = {}

    def reduce(self, vector):
        v = dict(vector)
        for p in sorted(self.pivots):
            guard()
            if p in v:
                add_scaled(v, self.pivots[p], -v[p])
        return v

    def add(self, vector):
        v = self.reduce(vector)
        if not v:
            return None
        p = min(v)
        scale = Fraction(v[p])
        v = {k: Fraction(c) / scale for k, c in v.items()}
        self.pivots[p] = v
        return v

    def contains(self, vector):
        return not self.reduce(vector)


def tensor_string(word):
    return "".join(LETTERS[i] for i in word)


def encode_vector(v):
    return [[tensor_string(k), str(Fraction(c))] for k, c in sorted(v.items())]


def encode_column_family(columns):
    return [encode_vector(v) for v in columns]


def poly_count(n):
    """Independent Witt character count in the ordered tensor alphabet."""
    tensor = Counter()
    for word in product(range(8), repeat=n):
        guard()
        tensor[weight(word)] += 1
    correction = Counter()
    if n == 4:
        for word in product(range(8), repeat=2):
            a, b = weight(word)
            correction[(2 * a, 2 * b)] += 1
    elif n == 3:
        for a, b in DEGREES:
            correction[(3 * a, 3 * b)] += 1
    else:
        raise CheckFailure("Witt count requested in unsupported degree")
    ans = {}
    for w in set(tensor) | set(correction):
        numerator = tensor[w] - correction[w]
        require(numerator % n == 0, "nonintegral Witt coefficient")
        if numerator:
            ans[w] = numerator // n
    return ans


def free_lie(n):
    by_weight = defaultdict(list)
    for word in product(range(8), repeat=n):
        guard()
        if lyndon(word):
            by_weight[weight(word)].append(lyndon_bracket(word))
    expected = poly_count(n)
    actual = {w: len(cols) for w, cols in by_weight.items()}
    require(actual == expected, "Lyndon/Witt weight mismatch in degree " + str(n))
    require(sum(actual.values()) == {3: 168, 4: 1008}[n], "free Lie dimension mismatch")
    return by_weight, actual


def relation_module(seed):
    spaces = {}
    queue = deque()

    def add(w, vector):
        space = spaces.setdefault(w, Span())
        new = space.add(vector)
        if new is not None:
            queue.append((w, new))

    add((1, 0), seed)
    while queue:
        guard()
        w, vector = queue.popleft()
        add((w[0] + 1, w[1]), action(E1, vector))
        add((w[0], w[1] + 1), action(E2, vector))
    require(sum(len(s.pivots) for s in spaces.values()) == 81, "whole seed module is not dimension 81")
    for w, space in sorted(spaces.items()):
        for vector in space.pivots.values():
            guard()
            for table, dw in ((E1, (1, 0)), (E2, (0, 1)), (F1, (-1, 0)), (F2, (0, -1))):
                target = spaces.get((w[0] + dw[0], w[1] + dw[1]))
                image = action(table, vector)
                require((not image) if target is None else target.contains(image), "relation is not Levi-stable")
            require(not contract(vector, 0), "F3 constant does not annihilate whole relation")
            require(not contract(vector, 1), "F3 coefficient does not annihilate whole relation")
    return spaces


def quotient_columns(free, relation, w):
    span = Span()
    rel = relation.get(w)
    if rel is not None:
        for v in rel.pivots.values():
            require(span.add(v) is not None, "dependent relation basis")
    basis = []
    for v in free.get(w, ()):
        if span.add(v) is not None:
            basis.append(v)
    return basis


def relation_reduce(relation, w, vector):
    space = relation.get(w)
    return dict(vector) if space is None else space.reduce(vector)


def nullspace_from_columns(columns):
    """Return independent kernel combinations, retaining every free column."""
    pivots = {}
    kernel = []
    for j, original in enumerate(columns):
        guard()
        v = dict(original)
        combination = {j: Fraction(1)}
        for p in sorted(pivots):
            if p in v:
                c = -v[p]
                add_scaled(v, pivots[p][0], c)
                add_scaled(combination, pivots[p][1], c)
        if not v:
            kernel.append(combination)
        else:
            p = min(v)
            d = Fraction(v[p])
            pivots[p] = ({k: Fraction(c) / d for k, c in v.items()},
                         {k: Fraction(c) / d for k, c in combination.items()})
    return kernel


def primitive(vector):
    if not vector:
        return {}
    denominator = 1
    for value in vector.values():
        q = Fraction(value).denominator
        denominator = denominator // gcd(denominator, q) * q
    integers = {k: int(Fraction(v) * denominator) for k, v in vector.items()}
    common = 0
    for value in integers.values():
        common = gcd(common, abs(value))
    integers = {k: v // common for k, v in integers.items()}
    if integers[min(integers)] < 0:
        integers = {k: -v for k, v in integers.items()}
    return integers


def rank(columns):
    space = Span()
    for v in columns:
        guard()
        space.add(v)
    return len(space.pivots)


def combine(a, b):
    out = dict(a)
    add_scaled(out, b, 1)
    return out


def actual_lowest(free4, free3, relation, w, label, expected_m):
    B = quotient_columns(free4, relation, w)
    equations = []
    for vector in B:
        guard()
        left = relation_reduce(relation, (w[0] - 1, w[1]), action(F1, vector))
        right = relation_reduce(relation, (w[0], w[1] - 1), action(F2, vector))
        column = {(0, k): c for k, c in left.items()}
        column.update({(1, k): c for k, c in right.items()})
        equations.append(column)
    combinations_kernel = nullspace_from_columns(equations)
    emit({"stage": "LOWEST_DIMENSION", "weight": w, "type": label,
          "quotient_dimension": len(B), "lowest_dimension": len(combinations_kernel),
          "expected_lowest_dimension": expected_m})
    require(len(combinations_kernel) == expected_m, "complete lowest multiplicity mismatch at " + str(w))
    lowest = []
    for coeffs in combinations_kernel:
        vector = {}
        for j, c in coeffs.items():
            add_scaled(vector, B[j], c)
        vector = primitive(vector)
        require(bool(vector), "zero lowest representative")
        require(not relation_reduce(relation, (w[0] - 1, w[1]), action(F1, vector)), "F1 nonzero modulo whole relation")
        require(not relation_reduce(relation, (w[0], w[1] - 1), action(F2, vector)), "F2 nonzero modulo whole relation")
        lowest.append(vector)
    require(rank([relation_reduce(relation, w, v) for v in lowest]) == expected_m,
            "lowest representatives dependent in quotient")

    target = Span()
    for v in free3.get(w, ()):
        require(target.add(v) is not None, "degree-three Lyndon dependence")
    pencil0 = [contract(v, 0) for v in lowest]
    pencil1 = [contract(v, 1) for v in lowest]
    for v in pencil0 + pencil1:
        require(target.contains(v), "F3 image is not in the actual free Lie degree-three target")
    rank4 = rank(pencil0)
    at5 = [combine(a, b) for a, b in zip(pencil0, pencil1)]
    rank5 = rank(at5)
    lost4 = rank(pencil0[:-1])
    lost5 = rank(at5[:-1])
    ctx = {"weight": w, "type": label, "m": expected_m, "quotient": B,
           "lowest": lowest, "pencil0": pencil0, "pencil1": pencil1,
           "rank4": rank4, "rank5": rank5, "lost4": lost4, "lost5": lost5,
           "attempts": 0, "last": None, "certificate": None, "exhausted": False}
    emit({"stage": "COMPLETE_PENCIL", "weight": w, "type": label,
          "m": len(lowest), "quotient_basis": encode_column_family(B),
          "lowest_tensors": encode_column_family(lowest),
          "F3_constant_columns": encode_column_family(pencil0),
          "F3_t_coefficient_columns": encode_column_family(pencil1),
          "rank_at_s4": rank4, "rank_at_s5": rank5,
          "rank_after_losing_last_copy_at_s4": lost4,
          "rank_after_losing_last_copy_at_s5": lost5})
    COMPLETED.append("complete-pencil-" + str(w))
    require(rank4 == expected_m and rank5 == expected_m,
            "finite full-rank control failed at " + str(w))
    require(lost4 == expected_m - 1 and lost5 == expected_m - 1,
            "lost-copy mutation not detected for its intended rank reason at " + str(w))
    emit({"stage": "CONTROL_LOST_COPY", "weight": w, "original_ranks": [rank4, rank5],
          "mutated_ranks": [lost4, lost5], "reason": "omitting an independent lowest direction loses one actual F3 image direction"})
    return ctx


def determinant(matrix):
    """Fraction-free exact Bareiss determinant on an integer square matrix."""
    a = [list(row) for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        guard()
        pivot_row = next((i for i in range(k, n) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            guard()
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                require(numerator % previous == 0, "Bareiss divisibility failure")
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def trim(poly):
    while poly and not poly[-1]:
        poly.pop()
    return poly


def minor_polynomial(rows0, rows1, rowset, m, value0):
    """Interpolation at 0..m followed by an independent m+1 check."""
    def value(t):
        return determinant([[rows0[row][j] + t * rows1[row][j] for j in range(m)] for row in rowset])

    values = [value0] + [value(t) for t in range(1, m + 1)]
    diffs = [Fraction(v) for v in values]
    basis = [Fraction(1)]
    result = [Fraction(0)] * (m + 1)
    for k in range(m + 1):
        guard()
        for j, c in enumerate(basis):
            result[j] += diffs[0] * c
        diffs = [diffs[j + 1] - diffs[j] for j in range(len(diffs) - 1)]
        if k < m:
            new = [Fraction(0)] * (len(basis) + 1)
            for j, c in enumerate(basis):
                new[j] -= k * c / (k + 1)
                new[j + 1] += c / (k + 1)
            basis = new
    require(all(c.denominator == 1 for c in result), "nonintegral determinant polynomial")
    ints = trim([int(c) for c in result])
    require(bool(ints) and ints[0] == value0, "zero or misinterpolated minor")
    require(sum(c * (m + 1) ** k for k, c in enumerate(ints)) == value(m + 1),
            "minor interpolation extra-point control failed")
    return ints


def primitive_poly(poly):
    poly = trim([Fraction(c) for c in poly])
    if not poly:
        return []
    denominator = 1
    for c in poly:
        denominator = denominator // gcd(denominator, c.denominator) * c.denominator
    ints = [int(c * denominator) for c in poly]
    common = 0
    for c in ints:
        common = gcd(common, abs(c))
    return [c // common for c in ints]


def remainder(a, b):
    a = trim([Fraction(x) for x in a])
    b = trim([Fraction(x) for x in b])
    require(bool(b), "polynomial division by zero")
    while a and len(a) >= len(b):
        guard()
        offset = len(a) - len(b)
        c = a[-1] / b[-1]
        for j, bj in enumerate(b):
            a[offset + j] -= c * bj
        trim(a)
    return a


def variations(signs):
    signs = [1 if x > 0 else -1 for x in signs if x]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def positivity_certificate(coefficients):
    """Either coefficient sign or exact Sturm count on (0,infinity)."""
    require(coefficients and coefficients[0], "minor must be nonzero at t=0")
    if all(c >= 0 for c in coefficients) or all(c <= 0 for c in coefficients):
        return {"method": "SAME_SIGN_SHIFT_COEFFICIENTS", "positive_roots": 0}
    p = primitive_poly(coefficients)
    derivative = primitive_poly([i * p[i] for i in range(1, len(p))])
    sequence = [p]
    if derivative:
        sequence.append(derivative)
        while True:
            guard()
            rem = remainder(sequence[-2], sequence[-1])
            if not rem:
                break
            sequence.append(primitive_poly([-c for c in rem]))
    at_zero = variations([poly[0] for poly in sequence])
    at_infinity = variations([poly[-1] for poly in sequence])
    count = at_zero - at_infinity
    require(count >= 0, "invalid Sturm variation count")
    return {"method": "EXACT_STURM", "sequence_ascending": sequence,
            "variations_at_zero": at_zero, "variations_at_positive_infinity": at_infinity,
            "positive_roots": count}


def row_data(ctx):
    m = ctx["m"]
    keys = sorted(set().union(*(set(v) for v in ctx["pencil0"] + ctx["pencil1"])))
    rows0 = {k: [int(v.get(k, 0)) for v in ctx["pencil0"]] for k in keys}
    rows1 = {k: [int(v.get(k, 0)) for v in ctx["pencil1"]] for k in keys}
    row_span = Span()
    base = []
    for k in keys:
        guard()
        if row_span.add({j: c for j, c in enumerate(rows0[k]) if c}) is not None:
            base.append(k)
            if len(base) == m:
                break
    require(len(base) == m, "cannot select s=4 pivot rows")
    return keys, rows0, rows1, tuple(sorted(base))


def row_candidates(keys, base):
    """Quick one-row alternatives first, then exhaustive deterministic subsets."""
    seen = {base}
    yield base
    base_set = set(base)
    for old in base:
        for new in keys:
            guard()
            if new in base_set:
                continue
            trial = tuple(sorted((base_set - {old}) | {new}))
            if trial not in seen:
                seen.add(trial)
                yield trial
    for trial in combinations(keys, len(base)):
        guard()
        if trial not in seen:
            seen.add(trial)
            yield trial


def attempt(ctx):
    rows = next(ctx["candidates"])
    ctx["attempts"] += 1
    m, rows0, rows1 = ctx["m"], ctx["rows0"], ctx["rows1"]
    value0 = determinant([[rows0[row][j] for j in range(m)] for row in rows])
    if not value0:
        return
    coefficients = minor_polynomial(rows0, rows1, rows, m, value0)
    result = positivity_certificate(coefficients)
    record = {"weight": ctx["weight"], "type": ctx["type"],
              "tensor_rows": [tensor_string(r) for r in rows],
              "determinant_coefficients_ascending_in_t": coefficients,
              "proof": result, "attempts_including_zero_minors": ctx["attempts"]}
    ctx["last"] = record
    if result["positive_roots"] == 0:
        ctx["certificate"] = record
        emit({"stage": "UNIFORM_MAXIMAL_MINOR_CERTIFICATE", **record})
        COMPLETED.append("uniform-certificate-" + str(ctx["weight"]))


def main():
    emit({"stage": "START", "scope": "r=3; s=4+t, t>=0; three complete lowest spaces",
          "targets": TARGETS, "cooperative_seconds": 39,
          "qualification": "A completed output is still subject to parent source audit and independent mathematical disposition."})
    free3, counts3 = free_lie(3)
    free4, counts4 = free_lie(4)
    emit({"stage": "FREE_LIE_WITT", "degree3_total": sum(counts3.values()),
          "degree4_total": sum(counts4.values()),
          "degree3_weight_counts": [[list(w), n] for w, n in sorted(counts3.items())],
          "degree4_weight_counts": [[list(w), n] for w, n in sorted(counts4.items())]})
    COMPLETED.append("free-lie-and-witt-characters")

    seed = bracket({(0,): 1}, bracket({(0,): 1}, bracket({(0,): 1}, {(1,): 1})))
    require(bool(seed) and not action(F1, seed) and not action(F2, seed), "seed is not a nonzero lowest word")
    relation = relation_module(seed)
    emit({"stage": "WHOLE_81_RELATION", "dimension": 81,
          "weights_and_basis": [{"weight": w, "vectors": encode_column_family(list(s.pivots.values()))}
                                 for w, s in sorted(relation.items())],
          "checked": "E1,E2,F1,F2 stability and both coefficients of actual F3 annihilation"})
    COMPLETED.append("whole-81-relation")

    xb = bracket({(0,): 1}, {(2,): 1})
    actual = contract(xb, 0)
    mutant = contract(xb, 0, reverse_cartan=True)
    emit({"stage": "CONTROL_CARTAN_SIGN", "input": "[x,b] at (r,s)=(3,4)",
          "actual": encode_vector(actual), "reversed_cartan_delta": encode_vector(mutant)})
    require(actual == {(2,): 6} and mutant == {(2,): 2},
            "reversed Cartan control failed for its intended coefficient reason")
    translated = action(E2, seed)
    only_seed = Span()
    only_seed.add(seed)
    rel11 = relation.get((1, 1))
    in_actual = rel11 is not None and rel11.contains(translated)
    in_mutant = only_seed.contains(translated)
    emit({"stage": "CONTROL_MISSING_TRANSLATE", "E2_seed": encode_vector(translated),
          "nonzero": bool(translated), "in_full_relation": in_actual, "in_seed_only_mutant": in_mutant})
    require(bool(translated) and in_actual and not in_mutant,
            "missing relation translate not detected for its intended reason")
    COMPLETED.append("cartan-and-translate-controls")

    for w, label, m in TARGETS:
        guard()
        CONTEXTS.append(actual_lowest(free4, free3, relation, w, label, m))
    COMPLETED.append("all-three-s4-s5-and-lost-copy-controls")

    for ctx in CONTEXTS:
        keys, rows0, rows1, base = row_data(ctx)
        ctx.update({"rows0": rows0, "rows1": rows1,
                    "candidates": row_candidates(keys, base)})
    while any(not c["certificate"] and not c["exhausted"] for c in CONTEXTS):
        for ctx in CONTEXTS:
            guard()
            if ctx["certificate"] or ctx["exhausted"]:
                continue
            try:
                attempt(ctx)
            except StopIteration:
                ctx["exhausted"] = True
                emit({"stage": "OPEN_EXHAUSTED_SINGLE_MINORS", "weight": ctx["weight"],
                      "attempts": ctx["attempts"],
                      "qualification": "No single searched minor avoids all positive real roots; this is not a rank-drop witness."})
    all_certified = all(c["certificate"] for c in CONTEXTS)
    return "COMPLETE_THREE_UNIFORM_MINOR_CERTIFICATES" if all_certified else "INCOMPLETE_NO_SINGLE_MINOR_CERTIFICATE"


def summary(status, detail=None):
    return {"stage": "END", "status": status, "detail": detail,
            "elapsed_seconds": time.monotonic() - START, "completed_stages": COMPLETED,
            "types": [{"weight": c["weight"], "type": c["type"],
                       "attempts": c["attempts"], "certificate": c["certificate"],
                       "last_nonzero_minor": c["last"], "exhausted": c["exhausted"]}
                      for c in CONTEXTS]}


if __name__ == "__main__":
    status = "FAILURE"
    detail = None
    try:
        signal.signal(signal.SIGTERM, latch)
        signal.signal(signal.SIGINT, latch)
        status = main()
    except Stopped as exc:
        status, detail = "INCOMPLETE", str(exc)
    except Exception as exc:
        status, detail = "FAILURE", type(exc).__name__ + ": " + str(exc)
    finally:
        emit(summary(status, detail))
    sys.exit(0 if status == "COMPLETE_THREE_UNIFORM_MINOR_CERTIFICATES" else 2)
