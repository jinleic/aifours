#!/usr/bin/env python3
"""UNRUN prospective finite assay, not a proof of the Kac radical conjecture.

The source uses only stdlib rational arithmetic and ordered associative words.
The specified examples are exactly (r,s) in SAMPLES plus the (2,2) case
(3,4); no interpolation or assertion for other parameters is made. The
whole-ideal/free-source bridge and the identification of these actions with
the actual displayed Chevalley quotient are mathematical imports, not proved
by executing this file. Input: none. Output: one JSON object on stdout; it
does not read or write files, use stdin, network, or subprocesses.

The caller must first read this entire source and obtain a NEW named parent GO
for one run with an external limit at most 55 seconds. The 42-second monotonic
cooperative limit returns INCOMPLETE, not PASS. This source was never run,
compiled, or tested by its author. All controls are actual calculations:
whole-module loss, negative-Cartan sign, the E12 sign, root-degree
misassignment, and loss of genuine lowest-copy image rank.
"""
from collections import deque
from fractions import Fraction as Rat
from itertools import product
import json
import sys
import time

START = time.monotonic()
END = START + 42.0
NAMES = ("x", "a", "b", "c", "d", "e", "f", "g")
DEG = ((0, 0), (1, 0), (0, 1), (1, 1),
       (1, 1), (2, 1), (1, 2), (2, 2))
SAMPLES = ((1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
           (2, 3), (2, 4), (2, 5), (2, 6),
           (3, 4), (3, 5), (3, 6))


class Incomplete(Exception):
    pass


class CheckFailure(Exception):
    pass


def tick():
    if time.monotonic() >= END:
        raise Incomplete("42-second cooperative deadline")


def need(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def axpy(dst, src, factor):
    factor = Rat(factor)
    if not factor:
        return
    for key, value in src.items():
        new = dst.get(key, Rat(0)) + factor * value
        if new:
            dst[key] = new
        else:
            dst.pop(key, None)


def scale(vec, factor):
    factor = Rat(factor)
    return {key: factor * value for key, value in vec.items()
            if factor * value}


def combine(*terms):
    out = {}
    for factor, vec in terms:
        axpy(out, vec, factor)
    return out


def one(i):
    return {(i,): Rat(1)}


def bracket(left, right):
    out = {}
    for u, a in left.items():
        tick()
        for v, b in right.items():
            coefficient = a * b
            axpy(out, {u + v: coefficient,}, 1)
            axpy(out, {v + u: coefficient,}, -1)
    return out


def table(entries):
    return tuple({i: Rat(c) for i, c in col if c} for col in entries)


# Columns are action on the indicated letter, not 3-by-3 matrix products.
E1 = table((((1, 1),), (), ((3, 1),), ((5, -2),), ((5, -1),),
            (), ((7, 1),), ()))
E2 = table((((2, 1),), ((4, 1),), (), ((6, 1),), ((6, 2),),
            ((7, -1),), (), ()))
F1 = table(((), ((0, 1),), (), ((2, 2),), ((2, 1),),
            ((3, -1),), (), ((6, 1),)))
F2 = table(((), (), ((0, 1),), ((1, 1),), ((1, 2),),
            (), ((4, 1),), ((5, -1),)))


def table_apply(tab, letter_vector):
    out = {}
    for j, c in letter_vector.items():
        axpy(out, tab[j], c)
    return out


def comm_column(left, right, j):
    return combine((1, table_apply(left, right[j])),
                   (-1, table_apply(right, left[j])))


E12 = tuple(comm_column(E1, E2, j) for j in range(8))


def action(tab, vec):
    """Levi derivation on ordered tensors."""
    out = {}
    for word, c in vec.items():
        tick()
        for pos, j in enumerate(word):
            for k, d in tab[j].items():
                new = word[:pos] + (k,) + word[pos + 1:]
                axpy(out, {new: c * d}, 1)
    return out


def degree_violations(degrees):
    bad = []
    for name, tab, shift in (("E1", E1, (1, 0)), ("E2", E2, (0, 1)),
                             ("F1", F1, (-1, 0)), ("F2", F2, (0, -1))):
        for j, col in enumerate(tab):
            for k, value in col.items():
                if value and degrees[k] != (degrees[j][0] + shift[0],
                                            degrees[j][1] + shift[1]):
                    bad.append((name, NAMES[j], NAMES[k]))
    return bad


def check_actions():
    need(not degree_violations(DEG), "actual Levi action root degrees")
    for j, (a, b) in enumerate(DEG):
        tick()
        h1 = {} if 2 * a - b - 1 == 0 else {j: Rat(2 * a - b - 1)}
        h2 = {} if 2 * b - a - 1 == 0 else {j: Rat(2 * b - a - 1)}
        need(comm_column(E1, F1, j) == h1, "[E1,F1]=H1")
        need(comm_column(E2, F2, j) == h2, "[E2,F2]=H2")
        need(not comm_column(E1, F2, j), "[E1,F2]=0")
        need(not comm_column(E2, F1, j), "[E2,F1]=0")
        need(not combine((1, table_apply(E1, E12[j])),
                         (-1, table_apply(E12, E1[j]))), "E1 Serre")
        need(not combine((1, table_apply(E2, E12[j])),
                         (-1, table_apply(E12, E2[j]))), "E2 Serre")


def d_letter(i, j, r, s, bad_cartan=False, bad_sign=False):
    """[F3,u_i] acting on u_j, including -h3 and the two E12 signs."""
    if i == 0:
        v = r * DEG[j][0] + s * DEG[j][1] - 2
        if bad_cartan:
            v = -v
        return {} if not v else {j: Rat(v)}
    if i == 1:
        return scale(E1[j], -r)
    if i == 2:
        return scale(E2[j], -s)
    if i == 3:
        return scale(E12[j], s if bad_sign else -s)
    if i == 4:
        return scale(E12[j], r)
    return {}


def delta(vec, r, s, bad_cartan=False, bad_sign=False):
    """F3 on a Lie tensor, by moving its degree-zero terms to the right.

    Sum over i<j of D_(letter i) applied at j, deleting position i. The
    remaining rightmost degree-zero terms cancel for a genuine Lie element.
    This routine is used only on brackets/linear combinations of brackets.
    """
    out = {}
    for word, c in vec.items():
        tick()
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                for k, d in d_letter(word[i], word[j], r, s,
                                     bad_cartan, bad_sign).items():
                    new = word[:i] + word[i + 1:j] + (k,) + word[j + 1:]
                    axpy(out, {new: c * d}, 1)
    return out


class Span:
    """Sparse row-echelon basis; tags reconstruct quotient coordinates."""
    def __init__(self):
        self.rows = {}

    def add(self, vec, tag=None):
        u = {k: Rat(v) for k, v in vec.items() if v}
        t = {} if tag is None else {k: Rat(v) for k, v in tag.items() if v}
        while u:
            tick()
            p = min(u)
            c = u[p]
            if p not in self.rows:
                self.rows[p] = (scale(u, 1 / c), scale(t, 1 / c))
                return True
            row, rowtag = self.rows[p]
            axpy(u, row, -c)
            axpy(t, rowtag, -c)
        return False

    def contains(self, vec):
        u = {k: Rat(v) for k, v in vec.items() if v}
        while u:
            tick()
            p = min(u)
            if p not in self.rows:
                return False
            axpy(u, self.rows[p][0], -u[p])
        return True

    def project(self, vec, dimension):
        u = {k: Rat(v) for k, v in vec.items() if v}
        tags = {}
        while u:
            tick()
            p = min(u)
            if p not in self.rows:
                raise CheckFailure("image is outside the claimed target Lie space")
            c = u[p]
            row, rowtag = self.rows[p]
            axpy(u, row, -c)
            axpy(tags, rowtag, c)
        return [tags.get(i, Rat(0)) for i in range(dimension)]


def span_of(vectors):
    space = Span()
    for vec in vectors:
        space.add(vec)
    return space


def same_span(left, right):
    a, b = span_of(left), span_of(right)
    return (len(a.rows) == len(b.rows)
            and all(a.contains(v) for v in right)
            and all(b.contains(v) for v in left))


def nested(word):
    vec = one(word[-1])
    for i in reversed(word[:-1]):
        vec = bracket(one(i), vec)
    return vec


def free_basis(n, weight):
    """All right-nested words span Lie_n; select exact independent tensors."""
    span, basis = Span(), []
    for word in product(range(8), repeat=n):
        tick()
        if (sum(DEG[i][0] for i in word),
            sum(DEG[i][1] for i in word)) != weight:
            continue
        v = nested(word)
        if span.add(v):
            basis.append((word, v))
    return span, basis


def seed(arm, power):
    v = one(arm)
    for _ in range(power):
        v = bracket(one(0), v)
    return v


def make_ideal(arm, power, maxgrade, maxweight, translates=True):
    """Close the seed under all bounded Levi raises and outer letters.

    Repeated ad(letter) spans outer bracketing by every free Lie word by
    Jacobi. Weight clipping is safe because all letter and raising degrees are
    nonnegative. In the intentional mutant, only Levi translates are omitted.
    """
    level = power + 1
    initial_weight = DEG[arm]
    if level > maxgrade or any(initial_weight[i] > maxweight[i] for i in (0, 1)):
        return {}
    spans, basis, todo = {}, {}, deque()

    def offer(n, wt, v):
        if not v:
            return
        key = (n, wt)
        if key not in spans:
            spans[key] = Span()
            basis[key] = []
        if spans[key].add(v):
            basis[key].append(v)
            todo.append((n, wt, v))

    offer(level, initial_weight, seed(arm, power))
    while todo:
        tick()
        n, wt, v = todo.popleft()
        if translates:
            for tab, shift in ((E1, (1, 0)), (E2, (0, 1))):
                next_weight = (wt[0] + shift[0], wt[1] + shift[1])
                if all(next_weight[i] <= maxweight[i] for i in (0, 1)):
                    offer(n, next_weight, action(tab, v))
        if n < maxgrade:
            for j, dj in enumerate(DEG):
                next_weight = (wt[0] + dj[0], wt[1] + dj[1])
                if all(next_weight[i] <= maxweight[i] for i in (0, 1)):
                    offer(n + 1, next_weight, bracket(one(j), v))
    return basis


def relations(ideals, n, weight):
    return [v for ideal in ideals for v in ideal.get((n, weight), ())]


class Quotient:
    def __init__(self, n, weight, ideals, preferred=None):
        free, free_vectors = free_basis(n, weight)
        self.free_rank = len(free.rows)
        self.rel = relations(ideals, n, weight)
        need(all(free.contains(v) for v in self.rel), "relation not in free Lie space")
        self.projector = Span()
        for v in self.rel:
            self.projector.add(v)
        self.relation_rank = len(self.projector.rows)
        choices = free_vectors if preferred is None else preferred
        self.vectors, self.labels = [], []
        for label, vec in choices:
            need(free.contains(vec), "preferred vector not in free Lie space")
            index = len(self.vectors)
            if self.projector.add(vec, {index: Rat(1)}):
                self.vectors.append(vec)
                self.labels.append(label)
            elif preferred is not None:
                raise CheckFailure("preferred quotient vectors are dependent")
        self.dim = len(self.vectors)
        need(self.dim == self.free_rank - self.relation_rank,
             "preferred quotient vectors do not cover the entire quotient")

    def coords(self, vec):
        return self.projector.project(vec, self.dim)


def matrix_from_columns(columns, row_count):
    return [[columns[j][i] for j in range(len(columns))]
            for i in range(row_count)]


def rref(matrix, ncols):
    a = [[Rat(x) for x in row] for row in matrix]
    need(all(len(row) == ncols for row in a), "matrix column count")
    pivots = []
    at = 0
    for j in range(ncols):
        tick()
        p = next((i for i in range(at, len(a)) if a[i][j]), None)
        if p is None:
            continue
        a[at], a[p] = a[p], a[at]
        div = a[at][j]
        a[at] = [x / div for x in a[at]]
        for i in range(len(a)):
            if i != at and a[i][j]:
                f = a[i][j]
                a[i] = [x - f * y for x, y in zip(a[i], a[at])]
        pivots.append(j)
        at += 1
        if at == len(a):
            break
    return a, pivots


def rank(matrix, ncols):
    return len(rref(matrix, ncols)[1])


def nullspace(matrix, ncols):
    rows, pivots = rref(matrix, ncols)
    result = []
    for j in range(ncols):
        if j in pivots:
            continue
        v = [Rat(0) for _ in range(ncols)]
        v[j] = Rat(1)
        for i, p in enumerate(pivots):
            v[p] = -rows[i][j]
        result.append(v)
    return result


def matvec(matrix, vector):
    return [sum((a * b for a, b in zip(row, vector)), Rat(0)) for row in matrix]


def determinant(rows):
    n = len(rows)
    need(all(len(row) == n for row in rows), "determinant not square")
    a = [[Rat(x) for x in row] for row in rows]
    answer = Rat(1)
    for j in range(n):
        tick()
        p = next((i for i in range(j, n) if a[i][j]), None)
        if p is None:
            return Rat(0)
        if p != j:
            a[j], a[p] = a[p], a[j]
            answer = -answer
        pivot = a[j][j]
        answer *= pivot
        for i in range(j + 1, n):
            f = a[i][j] / pivot
            for k in range(j, n):
                a[i][k] -= f * a[j][k]
    return answer


def frac_list(v):
    return [str(x) for x in v]


def low_words():
    x, a, b, c, d = (one(i) for i in range(5))
    def xx(v):
        return bracket(x, bracket(x, v))
    c4, d4 = bracket(x, xx(c)), bracket(x, xx(d))
    p4 = xx(bracket(a, b))
    q4 = bracket(x, bracket(a, bracket(x, b)))
    r4 = bracket(a, xx(b))
    c3, d3 = xx(c), xx(d)
    aa, bb = bracket(x, bracket(a, b)), bracket(a, bracket(x, b))
    b3 = bracket(x, xx(b))
    e4 = combine((1, c4), (1, p4), (1, q4), (1, r4))
    return c4, d4, p4, q4, r4, c3, d3, aa, bb, b3, e4


def target_formulas(r, s, words):
    c4, d4, p4, q4, r4, c3, d3, aa, bb, b3, e4 = words
    return (
        combine((3*r + 4*s - 12, c3), (-s, d3)),
        combine((-r, c3), (4*r + 3*s - 12, d3)),
        combine((-r, c3), (s, d3), (2*(r+s-5), aa)),
        combine((-r, c3), (2*s-2-r, aa), (r+s-6, bb)),
        combine((-r, c3), (-r, aa), (3*s-6-r, bb)),
    )


def check_low_case(r, s, words):
    c4, d4, p4, q4, r4, c3, d3, aa, bb, b3, e4 = words
    first = make_ideal(1, r, 4, (1, 1))
    second = make_ideal(2, s, 4, (1, 1))
    ideals = (first, second)
    first_expected = {
        1: (combine((1, d4), (-1, p4)), combine((1, q4), (-1, p4)),
            combine((-1, p4), (2, q4), (-1, r4))),
        2: (combine((1, d4), (-2, p4), (1, q4)),
            combine((-1, p4), (2, q4), (-1, r4))),
        3: (combine((1, d4), (-3, p4), (3, q4), (-1, r4)),),
    }[r]
    if s == 2:
        second_expected = (combine((1, c4), (1, p4), (1, q4)), r4)
    elif s == 3:
        second_expected = (e4,)
    else:
        second_expected = ()
    first_at = first.get((4, (1, 1)), ())
    second_at = second.get((4, (1, 1)), ())
    need(same_span(first_at, first_expected), "whole first Serre module relations")
    need(same_span(second_at, second_expected), "whole second Serre module relations")
    rf, rs = len(span_of(first_at).rows), len(span_of(second_at).rows)
    union = len(span_of(list(first_at) + list(second_at)).rows)
    overlap = rf + rs - union
    need(overlap == 0, "actual first/second relation overlap at (1,1)")

    need(len(span_of((c4, d4, p4, q4, r4)).rows) == 5, "five free basis vectors")
    free, _ = free_basis(4, (1, 1))
    need(len(free.rows) == 5 and all(free.contains(v) for v in
         (c4, d4, p4, q4, r4)), "five vectors cover the genuine free Lie weight")
    need(action(E1, b3) == e4, "E1 B3 relation")
    need(action(F1, e4) == scale(b3, 5), "F1 E1 B3")
    for actual, expected in zip((c4, d4, p4, q4, r4),
                                target_formulas(r, s, words)):
        need(delta(actual, r, s) == expected, "quoted F3 free tensor image")
    need(delta(b3, r, s) == scale(bracket(one(0), bracket(one(0), one(2))),
                                 4*(s-3)), "F3 B3")

    l1 = combine((1, c4), (-2, p4))
    l2 = combine((1, q4), (-1, p4))
    if r == 1:
        pref4 = [("L", l1)]
    elif r == 2:
        pref4 = [("L1", l1), ("L2", l2)]
    else:
        pref4 = [("K1", combine((1, c4), (-2, d4))),
                 ("K2", combine((1, p4), (-1, d4))),
                 ("K3", combine((1, q4), (-1, d4)))]
    if s >= 4:
        pref4.append(("E", e4))
    if (r, s) == (1, 2):
        pref4 = []
    source = Quotient(4, (1, 1), ideals, pref4)
    if s == 2:
        target = Quotient(3, (1, 1), ideals)
    else:
        pref3 = {1: [("C", c3), ("A", aa)],
                 2: [("C", c3), ("A", aa), ("B", bb)],
                 3: [("C", c3), ("D", d3), ("A", aa), ("B", bb)]}[r]
        target = Quotient(3, (1, 1), ideals, pref3)
    need(source.dim == 5-union, "actual (1,1) source dimension")
    need(target.dim == (1 if s == 2 else r+1), "actual (1,1) target dimension")
    for relation in relations(ideals, 4, (1, 1)):
        need(not any(target.coords(delta(relation, r, s))), "F3 must descend through whole relation")
    columns = [target.coords(delta(v, r, s)) for v in source.vectors]
    actual_map = matrix_from_columns(columns, target.dim)
    map_rank = rank(actual_map, source.dim)
    need(map_rank == source.dim, "full (1,1) F3 map rank")

    down1 = Quotient(4, (0, 1), ideals)
    down2 = Quotient(4, (1, 0), ideals)
    zero = Quotient(4, (0, 0), ideals)
    need(zero.dim == 0 and down2.dim == 0, "zero low-weight source components")
    need(down1.dim == (1 if s >= 4 else 0), "whole (0,1) component")
    down_cols = [down1.coords(action(F1, v)) + down2.coords(action(F2, v))
                 for v in source.vectors]
    lowering = matrix_from_columns(down_cols, down1.dim + down2.dim)
    lowest = nullspace(lowering, source.dim)
    lowest_expected = 0 if (r, s) == (1, 2) else r
    need(len(lowest) == lowest_expected, "all-copy lowest multiplicity")
    low_images = [matvec(actual_map, v) for v in lowest]
    low_rank = rank(matrix_from_columns(low_images, target.dim), len(low_images))
    need(low_rank == len(lowest), "F3 on the entire lowest multiplicity space")
    if s >= 4:
        target01 = Quotient(3, (0, 1), ideals)
        need(any(target01.coords(delta(b3, r, s))), "F3 on surviving B3")

    determinant_value = None
    if s >= 4:
        rows = [list(col) for col in columns]
        rows[-1] = [v / Rat(4*(s-3)) for v in rows[-1]]
        determinant_value = determinant(rows)
        expected_det = {1: 15*(s-2), 2: -30*(s-1)*(s-2),
                        3: 30*s*(s-1)*(s-2)}[r]
        need(determinant_value == expected_det, "quoted normalized minor")
    elif s == 3:
        expected_rows = {1: [[5, -5]], 2: [[10, -18, 9], [0, -4, 2]]}[r]
        need(columns == [[Rat(x) for x in row] for row in expected_rows],
             "s=3 image rows")

    copy_mutant = None
    if (r, s) == (3, 4):
        need(not any(down_cols[0]), "selected single vector is not actually lowest")
        one_rank = rank(matrix_from_columns([columns[0]], target.dim), 1)
        need(one_rank == 1 and low_rank == 3,
             "copy-selection mutant must lose two actual image directions")
        copy_mutant = {"selected_image_rank": one_rank,
                       "whole_lowest_image_rank": low_rank,
                       "reason": "two genuine lowest-copy image directions omitted"}
    return {"r": r, "s": s, "first_relation_rank": rf,
            "second_relation_rank": rs, "combined_relation_rank": union,
            "actual_overlap_rank": overlap, "source_dim": source.dim,
            "target_dim": target.dim, "F3_rank": map_rank,
            "all_copy_lowest_dim": len(lowest), "all_copy_F3_rank": low_rank,
            "normalized_minor": None if determinant_value is None else str(determinant_value),
            "copy_selection_mutant": copy_mutant}


def check_mutants(words):
    c4, d4, p4, q4, r4, c3, d3, aa, bb, b3, e4 = words
    deficient = make_ideal(1, 1, 4, (1, 1), translates=False)
    bad_space = span_of(deficient.get((4, (1, 1)), ()))
    needed_translate = combine((1, d4), (-1, p4))
    need(not bad_space.contains(needed_translate),
         "whole-module mutant did not expose missing Levi translate")
    xb = bracket(one(0), one(2))
    cartan_good = delta(xb, 3, 4)
    cartan_bad = delta(xb, 3, 4, bad_cartan=True)
    need(cartan_good == scale(one(2), 6) and cartan_bad != cartan_good,
         "negative-Cartan mutant did not break actual F3[x,b]")
    sign_good = target_formulas(3, 4, words)[0]
    sign_bad = delta(c4, 3, 4, bad_sign=True)
    need(delta(c4, 3, 4) == sign_good and sign_bad != sign_good,
         "E12-sign mutant did not break actual F3 C4")
    wrong_degree = list(DEG)
    wrong_degree[3] = (1, 0)
    violations = degree_violations(wrong_degree)
    need(bool(violations), "root-degree mutant did not break Levi weight action")
    return {"whole_module": {"detected_by": "missing E2-translated relation D4-P",
                              "seed_only_relation_rank": len(bad_space.rows)},
            "negative_cartan": {"detected_by": "F3[x,b] identity at (3,4)",
                                "correct_coefficient_b": str(cartan_good.get((2,), 0)),
                                "mutant_coefficient_b": str(cartan_bad.get((2,), 0))},
            "sign": {"detected_by": "F3 C4 tensor identity at (3,4)",
                     "nonzero_difference": bool(combine((1, sign_bad), (-1, sign_good)))},
            "root_degree": {"detected_by": "actual Levi weight transition",
                            "first_violation": violations[0]}}


def actual_22():
    r, s, weight = 3, 4, (2, 2)
    first = make_ideal(1, r, 4, weight)
    second = make_ideal(2, s, 4, weight)
    ideals = (first, second)
    source = Quotient(4, weight, ideals)
    target = Quotient(3, weight, ideals)
    need(source.free_rank == 25 and source.relation_rank == 2 and source.dim == 23,
         "(2,2) actual grade-four dimensions")
    need(target.free_rank == 13 and target.relation_rank == 0 and target.dim == 13,
         "(2,2) actual grade-three dimensions")
    need(len(span_of(first.get((4, weight), ())).rows) == 2 and
         not second.get((4, weight), ()), "entire bounded (2,2) Serre module")
    for relation in source.rel:
        need(not any(target.coords(delta(relation, r, s))),
             "(2,2) F3 does not descend through a whole relation")
    cols = [target.coords(delta(v, r, s)) for v in source.vectors]
    mat = matrix_from_columns(cols, target.dim)
    actual_rank = rank(mat, source.dim)
    kernel = nullspace(mat, source.dim)
    need(actual_rank + len(kernel) == source.dim and len(kernel) >= 10,
         "(2,2) exact rank-nullity")
    need(all(not any(matvec(mat, k)) for k in kernel), "(2,2) kernel vectors")
    labels = lambda space: [[NAMES[i] for i in word] for word in space.labels]
    return {"parameter": [3, 4], "weight": [2, 2],
            "free_grade4_dim": source.free_rank, "relation_grade4_rank": source.relation_rank,
            "actual_grade4_dim": source.dim, "actual_grade3_dim": target.dim,
            "F3_rank": actual_rank, "F3_kernel_dim": len(kernel),
            "grade4_right_nested_basis": labels(source),
            "grade3_right_nested_basis": labels(target),
            "F3_matrix_rows_grade3_columns_grade4": [frac_list(row) for row in mat],
            "kernel_basis_in_listed_grade4_coordinates": [frac_list(v) for v in kernel],
            "scope": "whole root-space F3 kernel; NOT a radical or lowest-space assertion"}


def main():
    check_actions()
    words = low_words()
    low = [check_low_case(r, s, words) for r, s in SAMPLES]
    controls = check_mutants(words)
    controls["copy_selection"] = next(row["copy_selection_mutant"] for row in low
                                       if row["copy_selection_mutant"] is not None)
    weight22 = actual_22()
    tick()
    return {"status": "PASS_FINITE_CHECKS_ONLY", "sample_domain": [list(x) for x in SAMPLES],
            "parameter_polynomials": "checked only at the explicitly listed samples; no universal interpolation",
            "whole_module": "all bounded E1/E2 translates and all ordered outer-letter brackets, with union overlap",
            "source": "ordinary free Lie embedded in ordered associative tensors",
            "imports": ["displayed eight-letter actions", "actual whole-Serre/free-source bridge"],
            "low_weight_cases": low, "intended_reason_mutants": controls,
            "actual_22": weight22,
            "not_established": ["global or entire grade-four radical", "formal/kernel proof",
                                "human or independent-family review", "novelty", "all parameters"],
            "elapsed_seconds": time.monotonic() - START}


if __name__ == "__main__":
    try:
        print(json.dumps(main(), sort_keys=True, separators=(",", ":")))
    except Incomplete as exc:
        print(json.dumps({"status": "INCOMPLETE", "reason": str(exc)}))
        sys.exit(3)
    except CheckFailure as exc:
        print(json.dumps({"status": "FAIL", "reason": str(exc)}))
        sys.exit(1)
    except Exception as exc:
        print(json.dumps({"status": "ERROR", "type": type(exc).__name__, "reason": str(exc)}))
        sys.exit(2)
