import sys
import time
START = time.monotonic()
LIMIT = 54.0
from fractions import Fraction as Q
from collections import Counter, deque


class Failure(Exception):
    def __init__(self, reason, detail=""):
        self.reason = reason
        self.detail = detail
        super().__init__(reason + ": " + detail)


class Deadline(Exception):
    pass


def guard():
    if time.monotonic() - START >= LIMIT:
        raise Deadline()


def require(ok, reason, detail=""):
    guard()
    if not ok:
        raise Failure(reason, detail)


def bump(out, key, value):
    if value:
        new = out.get(key, 0) + value
        if new:
            out[key] = new
        else:
            out.pop(key, None)


def accumulate(out, factor, vector):
    guard()
    if factor:
        for key, value in vector.items():
            bump(out, key, factor * value)


def linear(*terms):
    out = {}
    for factor, vector in terms:
        accumulate(out, factor, vector)
    return out


def scale(vector, factor):
    return linear((factor, vector))


def unit(i):
    return {i: Q(1)}


def sparse_text(vector):
    return repr([(key, str(vector[key])) for key in sorted(vector)])


def apply(matrix, vector):
    out = {}
    for index, coefficient in vector.items():
        accumulate(out, coefficient, matrix[index])
    return out


def compose(left, right):
    return [apply(left, column) for column in right]


def matadd(left, right, factor=1):
    require(len(left) == len(right), "matrix_size")
    return [
        linear((1, a), (factor, b))
        for a, b in zip(left, right)
    ]


def comm(left, right):
    return matadd(compose(left, right), compose(right, left), -1)


def matrix_zero(matrix):
    return all(not column for column in matrix)


def power(matrix, exponent, vector):
    result = vector
    for _ in range(exponent):
        result = apply(matrix, result)
    return result


class Span:
    def __init__(self):
        self.rows = {}

    def reduce(self, vector):
        guard()
        result = dict(vector)
        for pivot in sorted(self.rows):
            coefficient = result.get(pivot, 0)
            if coefficient:
                accumulate(result, -coefficient, self.rows[pivot])
        return result

    def insert(self, vector):
        result = self.reduce(vector)
        if not result:
            return None
        pivot = min(result)
        result = scale(result, Q(1) / result[pivot])
        self.rows[pivot] = result
        return result

    def __len__(self):
        return len(self.rows)


def closure(seed, operators):
    result = Span()
    first = result.insert(seed)
    require(first is not None, "closure_zero_seed")
    queue = deque([first])
    while queue:
        guard()
        vector = queue.popleft()
        for operator in operators:
            new = result.insert(apply(operator, vector))
            if new is not None:
                queue.append(new)
    return result


def invariant(space, operators, reason):
    for name, operator in operators.items():
        for vector in space.rows.values():
            residual = space.reduce(apply(operator, vector))
            require(not residual, reason, name + " " + sparse_text(residual))


def triples(total):
    return [
        (a, b, total - a - b)
        for a in range(total + 1)
        for b in range(total - a + 1)
    ]


def plus_index(p, index):
    out = list(p)
    out[index] += 1
    return tuple(out)


def grade_from_weight(h1, h3, b):
    aa = 2 * h1 + h3 + 5 * b
    nn = h1 + 2 * h3 + 7 * b
    require(aa % 3 == 0 and nn % 3 == 0, "nonintegral_grade")
    return aa // 3, nn // 3


def homogeneous(vector, grades):
    require(bool(vector), "zero_homogeneous_vector")
    values = {grades[index] for index in vector}
    require(len(values) == 1, "inhomogeneous_vector", repr(values))
    return next(iter(values))


def character(vectors, grades):
    result = Counter()
    for vector in vectors:
        result[homogeneous(vector, grades)] += 1
    return dict(result)


def gt_character(p, q, shift=(0, 0)):
    result = Counter()
    for m1 in range(p, p + q + 1):
        for m2 in range(p + 1):
            for k in range(m2, m1 + 1):
                guard()
                w1 = k
                w2 = m1 + m2 - k
                w3 = 2 * p + q - m1 - m2
                h1, h3 = w1 - w2, w2 - w3
                aa = 2 * h1 + h3 + 2 * p + q
                nn = h1 + 2 * h3 + p + 2 * q
                require(aa % 3 == 0 and nn % 3 == 0, "GT_integrality")
                result[(aa // 3 + shift[0], nn // 3 + shift[1])] += 1
    return dict(result)


def exterior_character(char):
    grades = []
    for grade, multiplicity in sorted(char.items()):
        grades.extend([grade] * multiplicity)
    result = Counter()
    for i, first in enumerate(grades):
        for second in grades[i + 1:]:
            result[(first[0] + second[0], first[1] + second[1])] += 1
    return dict(result)


def check_char(actual, expected, reason):
    difference = {}
    for key in set(actual) | set(expected):
        value = actual.get(key, 0) - expected.get(key, 0)
        if value:
            difference[key] = value
    require(not difference, reason, repr(sorted(difference.items())))


def check_laws(ops, tag):
    e1, f1 = ops["E1"], ops["F1"]
    e3, f3 = ops["E3"], ops["F3"]
    h1, h3 = ops["H1"], ops["H3"]
    require(comm(e1, f1) == h1, tag + "_E1F1")
    require(comm(e3, f3) == h3, tag + "_E3F3")
    require(matrix_zero(comm(e1, f3)), tag + "_E1F3")
    require(matrix_zero(comm(e3, f1)), tag + "_E3F1")
    require(matrix_zero(comm(h1, h3)), tag + "_Cartan")
    for h, weights in ((h1, (2, -1)), (h3, (-1, 2))):
        for e, f, weight in ((e1, f1, weights[0]), (e3, f3, weights[1])):
            require(
                comm(h, e) == [scale(c, weight) for c in e],
                tag + "_HE"
            )
            require(
                comm(h, f) == [scale(c, -weight) for c in f],
                tag + "_HF"
            )
    for first, second in ((e1, e3), (e3, e1), (f1, f3), (f3, f1)):
        require(
            matrix_zero(comm(first, comm(first, second))),
            tag + "_simple_Serre"
        )


def build_kernel():
    monomials = [(p, j) for p in triples(3) for j in range(3)]
    index = {monomial: i for i, monomial in enumerate(monomials)}
    require(len(monomials) == 30, "ambient_dimension")

    def delta(vector):
        out = {}
        for k, coefficient in vector.items():
            p, j = monomials[k]
            if p[j]:
                beta = list(p)
                beta[j] -= 1
                bump(out, tuple(beta), coefficient * p[j])
        return out

    basis = []
    descriptors = []
    for k, (p, j) in enumerate(monomials):
        if p[j] == 0:
            basis.append({k: Q(1)})
            descriptors.append((k, 1))
    for beta in triples(2):
        pivot = index[(plus_index(beta, 0), 0)]
        for j in (1, 2):
            free = index[(plus_index(beta, j), j)]
            basis.append({
                free: Q(beta[0] + 1),
                pivot: Q(-(beta[j] + 1))
            })
            descriptors.append((free, beta[0] + 1))
    require(len(basis) == 24, "kernel_basis_dimension")
    require(len({k for k, _ in descriptors}) == 24, "kernel_free_coordinates")
    for vector in basis:
        require(not delta(vector), "kernel_basis_contraction")

    def coordinates(vector):
        require(not delta(vector), "operator_preserves_contraction_kernel")
        result = {}
        reconstructed = {}
        for k, (ambient_free, divisor) in enumerate(descriptors):
            coefficient = Q(vector.get(ambient_free, 0)) / divisor
            if coefficient:
                result[k] = coefficient
                accumulate(reconstructed, coefficient, basis[k])
        require(
            reconstructed == vector,
            "kernel_coordinate_reconstruction",
            sparse_text(linear((1, vector), (-1, reconstructed)))
        )
        return result

    def ambient_action(vector, i, j):
        out = {}
        for k, coefficient in vector.items():
            p, dual = monomials[k]
            if p[j]:
                moved = list(p)
                moved[j] -= 1
                moved[i] += 1
                bump(out, index[(tuple(moved), dual)], coefficient * p[j])
            if dual == i:
                bump(out, index[(p, j)], -coefficient)
        return out

    def monomial_weight(monomial):
        p, dual = monomial
        d = [p[i] - int(i == dual) for i in range(3)]
        return d[0] - d[1], d[1] - d[2]

    weights = []
    for vector in basis:
        ws = {monomial_weight(monomials[k]) for k in vector}
        require(len(ws) == 1, "kernel_weight_basis")
        weights.append(next(iter(ws)))
    grades = [grade_from_weight(h1, h3, 1) for h1, h3 in weights]
    require(all(a >= 0 and n >= 0 for a, n in grades), "kernel_positive_grades")
    ops = {}
    for name, i, j in (
        ("E1", 0, 1), ("F1", 1, 0),
        ("E3", 1, 2), ("F3", 2, 1)
    ):
        ops[name] = [coordinates(ambient_action(c, i, j)) for c in basis]
    for name, component in (("H1", 0), ("H3", 1)):
        ops[name] = [
            {i: Q(weight[component])} if weight[component] else {}
            for i, weight in enumerate(weights)
        ]
    v = coordinates({index[((0, 0, 3), 0)]: Q(1)})
    return ops, grades, weights, v


def build_wedge(mops, mgrades, mweights):
    pairs = [(i, j) for i in range(24) for j in range(i + 1, 24)]
    pair_index = {pair: k for k, pair in enumerate(pairs)}

    def wedge(left, right):
        out = {}
        for i, a in left.items():
            for j, b in right.items():
                if i < j:
                    bump(out, pair_index[(i, j)], a * b)
                elif i > j:
                    bump(out, pair_index[(j, i)], -a * b)
        return out

    grades = [
        (mgrades[i][0] + mgrades[j][0], mgrades[i][1] + mgrades[j][1])
        for i, j in pairs
    ]
    weights = [
        (mweights[i][0] + mweights[j][0], mweights[i][1] + mweights[j][1])
        for i, j in pairs
    ]
    for grade, weight in zip(grades, weights):
        require(grade == grade_from_weight(*weight, 2), "wedge_Cartan_grade")
    ops = {}
    for name, matrix in mops.items():
        ops[name] = [
            linear(
                (1, wedge(matrix[i], unit(j))),
                (1, wedge(unit(i), matrix[j]))
            )
            for i, j in pairs
        ]
    return ops, grades, wedge


def poly_multiply(left, right):
    out = {}
    for first, a in left.items():
        for second, b in right.items():
            bump(out, first + second, a * b)
    return out


def poly_bracket(left, right):
    return linear(
        (1, poly_multiply(left, right)),
        (-1, poly_multiply(right, left))
    )


def poly_ad(t, exponent, vector):
    for _ in range(exponent):
        vector = poly_bracket(t, vector)
    return vector


def actual_F2_normal_order(poly):
    out = {}
    cartan_weight = {"t": -1, "v": 2}
    for word, coefficient in poly.items():
        require(
            all(letter in cartan_weight for letter in word),
            "rewrite_positive_word"
        )
        for i, letter in enumerate(word):
            if letter == "v":
                prefix, suffix = word[:i], word[i + 1:]
                positive_word = prefix + suffix
                bump(out, positive_word + ("h",), -coefficient)
                weight = sum(cartan_weight[x] for x in suffix)
                bump(out, positive_word, -coefficient * weight)
    return out


CONTROLS = []


def expect_control(name, reason, action):
    try:
        action()
    except Failure as error:
        require(
            error.reason == reason,
            "control_wrong_reason",
            name + ": " + error.reason
        )
        CONTROLS.append((name, reason, error.detail))
        return
    raise Failure("control_not_rejected", name)


def scalar_check(matrix, indices, scalar, reason):
    for i in indices:
        residual = linear((1, matrix[i]), (-scalar, unit(i)))
        require(not residual, reason, sparse_text(residual))


def main():
    mops, mgrades, mweights, v = build_kernel()
    check_laws(mops, "M")
    require(not apply(mops["F1"], v), "v_F1_lowest")
    require(not apply(mops["F3"], v), "v_F3_lowest")
    require(apply(mops["H1"], v) == scale(v, -1), "v_H1")
    require(apply(mops["H3"], v) == scale(v, -3), "v_H3")
    require(not power(mops["E1"], 2, v), "v_E1_Serre")
    require(not power(mops["E3"], 4, v), "v_E3_Serre")
    cyclic = closure(v, [mops["E1"], mops["E3"]])
    require(len(cyclic) == 24, "M_cyclic_dimension")
    mchar = dict(Counter(mgrades))
    check_char(mchar, gt_character(1, 3), "M_grade_character")
    require(max(n for a, n in mgrades) == 4, "M_maximum_grade")

    wops, wgrades, wedge = build_wedge(mops, mgrades, mweights)
    require(len(wgrades) == 276, "wedge_dimension")
    q1 = wedge(v, apply(mops["E1"], v))
    q3 = wedge(v, apply(mops["E3"], v))
    for q, expected_grade, h1, h3, name in (
        (q1, (1, 0), 0, -7, "q1"),
        (q3, (0, 1), -3, -4, "q3")
    ):
        require(bool(q), name + "_nonzero")
        require(homogeneous(q, wgrades) == expected_grade, name + "_start_grade")
        require(not apply(wops["F1"], q), name + "_F1_lowest")
        require(not apply(wops["F3"], q), name + "_F3_lowest")
        require(apply(wops["H1"], q) == scale(q, h1), name + "_H1")
        require(apply(wops["H3"], q) == scale(q, h3), name + "_H3")

    r1 = closure(q1, [wops["E1"], wops["E3"]])
    r3 = closure(q3, [wops["E1"], wops["E3"]])
    require(len(r1) == 36, "q1_whole_module_dimension")
    require(len(r3) == 90, "q3_whole_module_dimension")
    invariant(r1, wops, "q1_full_g_invariance")
    invariant(r3, wops, "q3_full_g_invariance")
    r1char = character(r1.rows.values(), wgrades)
    r3char = character(r3.rows.values(), wgrades)
    check_char(r1char, gt_character(0, 7, (1, 0)), "relation_q1_grade_character")
    check_char(r3char, gt_character(3, 4, (0, 1)), "relation_q3_grade_character")

    relations = Span()
    for space in (r1, r3):
        for row in space.rows.values():
            relations.insert(row)
    require(len(relations) == 126, "relation_sum_dimension")
    require(len(r1) + len(r3) - len(relations) == 0, "relation_intersection")

    def relation_check(space):
        for q, reason in ((q1, "missing_relation_q1"), (q3, "missing_relation_q3")):
            residual = space.reduce(q)
            require(not residual, reason, sparse_text(residual))
        invariant(space, wops, "whole_relation_invariance")
        require(len(space) == 126, "whole_relation_dimension")

    relation_check(relations)
    require(276 - len(r3) == 186, "omit_q1_control_dimension")
    require(276 - len(r1) == 240, "omit_q3_control_dimension")
    expect_control("omit_whole_q1_module", "missing_relation_q1", lambda: relation_check(r3))
    expect_control("omit_whole_q3_module", "missing_relation_q3", lambda: relation_check(r1))
    expect_control(
        "wrong_q1_start_grade",
        "relation_q1_grade_character",
        lambda: check_char(
            r1char, gt_character(0, 7, (0, 0)), "relation_q1_grade_character"
        )
    )
    expect_control(
        "wrong_q3_start_grade",
        "relation_q3_grade_character",
        lambda: check_char(
            r3char, gt_character(3, 4, (0, 0)), "relation_q3_grade_character"
        )
    )

    free = [i for i in range(276) if i not in relations.rows]
    free_index = {ambient: i for i, ambient in enumerate(free)}
    require(len(free) == 150, "quotient_dimension")

    def quotient(vector):
        reduced = relations.reduce(vector)
        require(all(i in free_index for i in reduced), "quotient_pivot_remains")
        return {free_index[i]: coefficient for i, coefficient in reduced.items()}

    ngrades = [wgrades[i] for i in free]
    nops = {
        name: [quotient(apply(matrix, unit(i))) for i in free]
        for name, matrix in wops.items()
    }
    nchar = dict(Counter(ngrades))
    expected = Counter(exterior_character(gt_character(1, 3)))
    expected.subtract(gt_character(0, 7, (1, 0)))
    expected.subtract(gt_character(3, 4, (0, 1)))
    require(all(value >= 0 for value in expected.values()), "negative_expected_character")
    expected = {key: value for key, value in expected.items() if value}
    check_char(nchar, expected, "quotient_full_grade_character")
    require(sum(nchar.values()) == 150, "quotient_character_dimension")
    check_laws(nops, "N")

    shifts = {"E1": (1, 0), "F1": (-1, 0), "E3": (0, 1), "F3": (0, -1)}
    for name, (da, dn) in shifts.items():
        for i, column in enumerate(nops[name]):
            a, n = ngrades[i]
            require(
                all(ngrades[j] == (a + da, n + dn) for j in column),
                "quotient_action_grade_routing",
                name
            )
    for i, (a, n) in enumerate(ngrades):
        h1, h3 = 2 * a - 2 - n, -a - 6 + 2 * n
        require(nops["H1"][i] == scale(unit(i), h1), "N_actual_H1")
        require(nops["H3"][i] == scale(unit(i), h3), "N_actual_H3")

    z = comm(nops["E1"], nops["E3"])
    d = comm(nops["F3"], nops["F1"])
    tf = compose(nops["E3"], nops["F3"])
    zd = compose(z, d)
    a0 = matadd(tf, zd)
    require(comm(z, d) == matadd(nops["H1"], nops["H3"]), "ZD_Cartan_commutator")
    top = [i for i, grade in enumerate(ngrades) if grade[1] == 8]
    require(len(top) == 1, "top_grade_dimension")
    require(ngrades[top[0]] == (5, 8), "top_horizontal_placement")
    require(max(n for a, n in ngrades) == 8, "N_maximum_grade")
    scalar_check(a0, top, 10, "top_scalar_10")
    scalar_check(tf, top, 5, "active_TF3_top_scalar")
    scalar_check(zd, top, 5, "active_ZD_top_scalar")
    expect_control(
        "reversed_theta_dual_commutator",
        "reversed_dual_top_scalar",
        lambda: scalar_check(matadd(tf, zd, -1), top, 10, "reversed_dual_top_scalar")
    )
    expect_control(
        "omit_active_ZD_consumer",
        "omitted_Z_top_scalar",
        lambda: scalar_check(tf, top, 10, "omitted_Z_top_scalar")
    )

    def degree_add(first, second):
        return tuple(a + b for a, b in zip(first, second))

    f_degree, g_degree, r_degree = (0, 0, 1), (1, 0, 0), (0, 1, 0)
    wd = [f_degree]
    wd.append(degree_add(wd[0], g_degree))
    wd.append(degree_add(wd[0], r_degree))
    wd.append(degree_add(wd[2], g_degree))
    wd.append(degree_add(wd[1], r_degree))
    wd.append(degree_add(wd[3], g_degree))
    wd.append(degree_add(wd[4], r_degree))
    wd.append(degree_add(wd[6], g_degree))
    roots13 = {(1, 0), (0, 1), (1, 1)}

    def other_arm_target_exists(a, n, j):
        da, db, dn = wd[j]
        aa, bb, nn = a - da, 2 - db, n - dn
        require(n >= 2 and nn >= 1, "consumer_target_domain")
        if aa < 0:
            return False
        if bb == 1:
            return bool(mchar.get((aa, nn), 0))
        if bb == 0:
            return (aa, nn) in roots13
        raise Failure("unhandled_consumer_target_b", repr((j, aa, bb, nn)))

    high_ranks = []
    for n in (6, 7, 8):
        indices = [i for i, grade in enumerate(ngrades) if grade[1] == n]
        require(bool(indices), "high_grade_nonempty", str(n))
        image = Span()
        for i in indices:
            a, _ = ngrades[i]
            for j in range(2, 8):
                require(
                    not other_arm_target_exists(a, n, j),
                    "discarded_consumer_has_actual_target",
                    repr((a, n, j))
                )
            require(
                all(ngrades[k][1] == n for k in a0[i]),
                "A0_grade_routing"
            )
            image.insert(a0[i])
        require(len(image) == len(indices), "high_grade_exact_rank", str(n))
        high_ranks.append((n, len(indices), len(image)))

    tword, vword = {("t",): 1}, {("v",): 1}
    tvword = poly_ad(tword, 1, vword)
    t2vword = poly_ad(tword, 2, vword)
    t3vword = poly_ad(tword, 3, vword)
    yword = poly_bracket(tvword, t2vword)
    require(actual_F2_normal_order(vword) == {("h",): -1}, "actual_F2_v")
    require(actual_F2_normal_order(tvword) == {("t",): -1}, "actual_F2_Tv")
    require(not actual_F2_normal_order(t2vword), "actual_F2_T2v")
    require(
        actual_F2_normal_order(yword) == scale(t3vword, -1),
        "actual_formal_F2_y"
    )
    require(
        not actual_F2_normal_order(poly_bracket(vword, tvword)),
        "actual_F2_repeated_node2_relation"
    )

    tv = apply(mops["E3"], v)
    t2v = apply(mops["E3"], tv)
    t3v = apply(mops["E3"], t2v)
    require(bool(t3v), "T3v_nonzero")
    require(power(mops["F3"], 3, t3v) == scale(v, 36), "actual_string_36")
    y = quotient(wedge(tv, t2v))
    require(bool(y), "actual_y_quotient_nonzero")
    require(homogeneous(y, ngrades) == (0, 3), "actual_y_grade")
    require(not apply(nops["F1"], y), "actual_y_F1_lowest")
    require(not apply(nops["F3"], y), "actual_y_F3_lowest")
    require(not apply(a0, y), "actual_y_A0_zero")
    for j in range(3, 8):
        require(not other_arm_target_exists(0, 3, j), "actual_y_other_target_zero")
    w2y = scale(apply(mops["F3"], t3v), -1)
    require(w2y == scale(t2v, -3), "actual_W2_y")
    w2_consumer = quotient(wedge(scale(tv, -1), w2y))
    residual = linear((1, w2_consumer), (-3, y))
    require(not residual, "actual_full_y_scalar_3", sparse_text(residual))

    def omitted_w2_check():
        residual = linear((1, apply(a0, y)), (-3, y))
        require(
            not residual,
            "omitted_active_W2_consumer_y",
            sparse_text(residual)
        )

    expect_control(
        "omit_active_other_arm_W2_consumer",
        "omitted_active_W2_consumer_y",
        omitted_w2_check
    )
    x = power(nops["E3"], 5, power(nops["E1"], 5, y))
    require(bool(x), "explicit_top_vector_nonzero")
    require(homogeneous(x, ngrades) == (5, 8), "explicit_top_vector_grade")
    require(set(x).issubset(set(top)), "explicit_top_vector_full_component")
    require(len(CONTROLS) == 7, "control_count")
    guard()

    print("RESULT: PASS_FIXED_FINITE_MODEL")
    print("SCOPE: r=1 s=3; conditional actual-source bridge; no global conclusion")
    print("DIMENSIONS: M=24 wedge=276 R1=36 R3=90 intersection=0 N=150")
    print("TOP: a=5 b=2 n=8 dimension=1 full_normalized_contraction=10I")
    print("ACTUAL_REWRITE: F2[y]=-T^3v; F3^3T^3v=36v")
    print("ACTIVE_OTHER_ARM: ad(u2)W2[y]=3y; A0[y]=0")
    print("HIGH_GRADE_RANKS:", repr(high_ranks))
    for name, reason, detail in CONTROLS:
        print("CONTROL_REJECT:", name, reason, detail)
    print("MIXED_GRAM_MUTATION: NOT_TESTED_IN_THIS_SCOPE")
    print("N_CHARACTER:", repr(sorted(nchar.items())))
    print("ELAPSED_MONOTONIC_SECONDS:", format(time.monotonic() - START, ".6f"))


if __name__ == "__main__":
    try:
        main()
    except Deadline:
        print("RESULT: INCOMPLETE_COOPERATIVE_DEADLINE", file=sys.stderr)
        sys.exit(3)
    except KeyboardInterrupt:
        print("RESULT: INCOMPLETE_INTERRUPTED", file=sys.stderr)
        sys.exit(3)
    except Failure as error:
        print("RESULT: FAIL", error.reason, error.detail, file=sys.stderr)
        sys.exit(2)
