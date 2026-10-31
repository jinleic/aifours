
import itertools
import time


START = time.monotonic()
DEADLINE = START + 55.0


class InvariantFailure(RuntimeError):
    def __init__(self, invariant, witness=None):
        self.invariant = invariant
        self.witness = witness
        super().__init__(invariant + ": " + repr(witness))


class CalculationDeadline(RuntimeError):
    pass


def tick():
    if time.monotonic() >= DEADLINE:
        raise CalculationDeadline("55-second cooperative calculation limit")


def require(condition, invariant, witness=None):
    if not condition:
        raise InvariantFailure(invariant, witness)


def negative(invariant, operation):
    try:
        operation()
    except InvariantFailure as error:
        require(
            error.invariant == invariant,
            "NEGATIVE_CONTROL_WRONG_REASON",
            (invariant, error.invariant, error.witness),
        )
        print("REJECTED", invariant, repr(error.witness))
        return
    raise InvariantFailure("NEGATIVE_CONTROL_NOT_REJECTED", invariant)


def rotate(mask, g, n):
    g %= n
    result = 0
    for atom in range(n):
        if mask & (1 << atom):
            result |= 1 << ((atom + g) % n)
    return result


def source_model(n):
    width = 1 << n
    source = tuple((a, g) for a in range(width) for g in range(n))
    idempotents = tuple((a, 0) for a in range(width))

    def multiply(s, t):
        return (
            s[0] & rotate(t[0], s[1], n),
            (s[1] + t[1]) % n,
        )

    def inverse(s):
        return (rotate(s[0], -s[1], n), (-s[1]) % n)

    return source, idempotents, multiply, inverse


def validate_source(n, source, idempotents, multiply, inverse):
    universe = set(source)
    expected_e = set(idempotents)
    identity = ((1 << n) - 1, 0)

    require(len(source) == n * (1 << n), "SOURCE_CARDINALITY", n)
    require(
        {s for s in source if multiply(s, s) == s} == expected_e,
        "SOURCE_IDEMPOTENTS",
    )
    require(len(expected_e) > 1, "SOURCE_NON_GROUP")
    require({s[1] for s in source} == set(range(n)), "Q_ONTO")

    for s in source:
        tick()
        si = inverse(s)
        require(si in universe, "INVERSE_CLOSURE", s)
        require(inverse(si) == s, "INVERSE_INVOLUTION", s)
        require(multiply(multiply(s, si), s) == s, "INVERSE_FIRST", s)
        require(multiply(multiply(si, s), si) == si, "INVERSE_SECOND", s)
        require(multiply(s, si) in expected_e, "RANGE_IDEMPOTENT", s)
        require(multiply(si, s) in expected_e, "DOMAIN_IDEMPOTENT", s)
        require(
            multiply(identity, s) == s and multiply(s, identity) == s,
            "SOURCE_IDENTITY",
            s,
        )
        candidates = tuple(
            t for t in source
            if multiply(multiply(s, t), s) == s
            and multiply(multiply(t, s), t) == t
        )
        require(candidates == (si,), "INVERSE_UNIQUE", (s, candidates))
        require((s[1] == 0) == (s in expected_e), "NORMALIZED_Q_PURITY", s)

        for t in source:
            st = multiply(s, t)
            require(st in universe, "SOURCE_CLOSURE", (s, t))
            require(
                inverse(st) == multiply(inverse(t), inverse(s)),
                "INVERSE_ANTIMULTIPLICATIVE",
                (s, t),
            )
            require(
                st[1] == (s[1] + t[1]) % n,
                "NORMALIZED_Q_HOMOMORPHISM",
                (s, t),
            )
            for u in source:
                require(
                    multiply(st, u) == multiply(s, multiply(t, u)),
                    "SOURCE_ASSOCIATIVITY",
                    (s, t, u),
                )

    for e in idempotents:
        for f in idempotents:
            require(
                multiply(e, f) == multiply(f, e),
                "IDEMPOTENTS_COMMUTE",
                (e, f),
            )


def make_iota(n, multiply, inverse, use_range=False, forget_group=False):
    width = 1 << n

    def coordinate(s):
        if use_range:
            e = multiply(s, inverse(s))
        else:
            e = multiply(inverse(s), s)
        g = 0 if forget_group else s[1]
        return g * width + e[0]

    return coordinate


def derive_ranges(source, multiply, inverse, coordinate, use_domain=False):
    ranges = {}
    for s in source:
        tick()
        if use_domain:
            e = multiply(inverse(s), s)
        else:
            e = multiply(s, inverse(s))
        mask = 0
        for x in source:
            if multiply(e, x) == x:
                mask |= 1 << coordinate(x)
        ranges[s] = mask
    return ranges


def shift(mask, g, n):
    width = 1 << n
    result = 0
    for point in range(n * width):
        if mask & (1 << point):
            layer, e = divmod(point, width)
            image = ((layer + g) % n) * width + e
            result |= 1 << image
    return result


def validate_action(n, enumerate_whole_band):
    width = 1 << n
    points = n * width
    point_universe = set(range(points))

    for g in range(n):
        tick()
        permutation = tuple(
            ((point // width + g) % n) * width + point % width
            for point in range(points)
        )
        require(set(permutation) == point_universe, "POINT_PERMUTATION", g)
        for point in range(points):
            singleton = 1 << point
            require(
                shift(singleton, g, n) == 1 << permutation[point],
                "POINT_ACTION_IMPLEMENTATION",
                (g, point),
            )
            for h in range(n):
                require(
                    shift(shift(singleton, h, n), g, n)
                    == shift(singleton, (g + h) % n, n),
                    "POINT_ACTION_GROUP_LAW",
                    (g, h, point),
                )

    if not enumerate_whole_band:
        return

    band_size = 1 << points
    transforms = tuple(
        tuple(shift(mask, g, n) for mask in range(band_size))
        for g in range(n)
    )

    for g in range(n):
        for u in range(band_size):
            tick()
            require(transforms[0][u] == u, "BAND_ACTION_IDENTITY", u)
            require(
                transforms[(-g) % n][transforms[g][u]] == u,
                "BAND_ACTION_INVERSE",
                (g, u),
            )
            for v in range(band_size):
                require(
                    transforms[g][u & v]
                    == (transforms[g][u] & transforms[g][v]),
                    "BAND_ACTION_INTERSECTION",
                    (g, u, v),
                )


def check_range_identity(n, source, multiply, ranges, twist, invariant):
    for s in source:
        tick()
        for t in source:
            expected = ranges[multiply(s, t)]
            actual = ranges[s] & shift(ranges[t], twist(s, t), n)
            require(
                actual == expected,
                invariant,
                (s, t, actual, expected),
            )


def check_purity(source, multiply, target_idempotents, quotient, invariant):
    for s in source:
        require(
            (quotient(s) in target_idempotents) == (multiply(s, s) == s),
            invariant,
            s,
        )


def validate_physical_c2(source, multiply, inverse, ranges, p):
    def q(s):
        return (s[1] - p) % 2

    def actor_multiply(h, k):
        return (h + p + k) % 2

    def physical_multiply(left, right):
        u, h = left
        v, k = right
        return (
            u & shift(v, (h + p) % 2, 2),
            actor_multiply(h, k),
        )

    actor_e = {
        h for h in range(2) if actor_multiply(h, h) == h
    }
    require(actor_e == {(-p) % 2}, "PHYSICAL_ACTOR_IDEMPOTENTS", p)
    require({q(s) for s in source} == {0, 1}, "PHYSICAL_Q_ONTO", p)
    check_purity(source, multiply, actor_e, q, "PHYSICAL_Q_PURITY")

    for h, k, ell in itertools.product(range(2), repeat=3):
        require(
            actor_multiply(actor_multiply(h, k), ell)
            == actor_multiply(h, actor_multiply(k, ell)),
            "PHYSICAL_ACTOR_ASSOCIATIVITY",
            (p, h, k, ell),
        )

    def physical_iota(s):
        domain = multiply(inverse(s), s)
        return ((q(s) + p) % 2) * 4 + domain[0]

    physical_ranges = derive_ranges(
        source, multiply, inverse, physical_iota
    )
    require(
        physical_ranges == ranges,
        "SANDWICH_COORDINATE_CONVERSION",
        p,
    )

    image = {s: (physical_ranges[s], q(s)) for s in source}
    require(
        len(set(image.values())) == len(source),
        "PHYSICAL_F_INJECTIVE",
        p,
    )

    for s in source:
        tick()
        require(image[s][1] == q(s), "EXACT_ACTOR_PROJECTION", (p, s))
        for t in source:
            require(
                q(multiply(s, t)) == actor_multiply(q(s), q(t)),
                "PHYSICAL_Q_HOMOMORPHISM",
                (p, s, t),
            )
            require(
                physical_multiply(image[s], image[t])
                == image[multiply(s, t)],
                "PHYSICAL_HOST_MULTIPLICATION",
                (p, s, t),
            )

    for u in range(256):
        tick()
        for h in range(2):
            host_element = (u, h)
            require(
                (physical_multiply(host_element, host_element) == host_element)
                == (h in actor_e),
                "WHOLE_HOST_PROJECTION_PURITY",
                (p, u, h),
            )

    print(
        "PRIMARY_PHYSICAL",
        "p=", p,
        "source_image=", len(image),
        "pair_products=", len(source) ** 2,
        "host_elements=", 512,
    )


def primary_checks():
    source, idempotents, multiply, inverse = source_model(2)
    validate_source(2, source, idempotents, multiply, inverse)
    validate_action(2, True)

    expected_table = (
        (0, 1, 0, 1, 0, 1, 0, 1),
        (1, 0, 1, 0, 1, 0, 1, 0),
        (0, 1, 2, 3, 0, 1, 2, 3),
        (1, 0, 1, 0, 3, 2, 3, 2),
        (0, 1, 0, 1, 4, 5, 4, 5),
        (1, 0, 5, 4, 1, 0, 5, 4),
        (0, 1, 2, 3, 4, 5, 6, 7),
        (1, 0, 5, 4, 3, 2, 7, 6),
    )
    index = {s: i for i, s in enumerate(source)}
    actual_table = tuple(
        tuple(index[multiply(s, t)] for t in source)
        for s in source
    )
    require(actual_table == expected_table, "EXPLICIT_SOURCE_TABLE")
    require(
        tuple(index[inverse(s)] for s in source)
        == (0, 1, 2, 5, 4, 3, 6, 7),
        "EXPLICIT_INVERSE_TABLE",
    )

    coordinate = make_iota(2, multiply, inverse)
    require(
        tuple(coordinate(s) for s in source)
        == (0, 4, 1, 6, 2, 5, 3, 7),
        "EXPLICIT_IOTA_TABLE",
    )
    require(
        {coordinate(s) for s in source} == set(range(8)),
        "IOTA_EXACT_POINT_UNIVERSE",
    )

    ranges = derive_ranges(source, multiply, inverse, coordinate)
    require(
        tuple(ranges[s] for s in source)
        == (0x11, 0x11, 0x53, 0x53, 0x35, 0x35, 0xff, 0xff),
        "EXPLICIT_RANGE_TABLE",
    )
    require(all(ranges[s] != 0 for s in source), "RANGES_NONEMPTY")
    require(
        shift(ranges[(1, 0)], 1, 2) == ranges[(2, 0)]
        and ranges[(1, 0)] != ranges[(2, 0)],
        "NONTRIVIAL_ACTION_ON_SOURCE_COORDINATES",
    )
    check_range_identity(
        2, source, multiply, ranges,
        lambda s, t: s[1],
        "CORRECT_C2_RANGE_IDENTITY",
    )

    for p in (0, 1):
        validate_physical_c2(source, multiply, inverse, ranges, p)

    negative(
        "SECOND_FACTOR_TWIST_MULTIPLICATION",
        lambda: check_range_identity(
            2, source, multiply, ranges,
            lambda s, t: t[1],
            "SECOND_FACTOR_TWIST_MULTIPLICATION",
        ),
    )

    wrong_coordinate = make_iota(
        2, multiply, inverse, use_range=True
    )
    require(
        len({wrong_coordinate(s) for s in source}) == 8,
        "RANGE_COORDINATE_MUTANT_STILL_INJECTIVE",
    )
    wrong_ranges = derive_ranges(
        source, multiply, inverse, wrong_coordinate
    )
    require(
        len({(wrong_ranges[s], s[1]) for s in source}) == 8,
        "RANGE_COORDINATE_MUTANT_F_STILL_INJECTIVE",
    )
    negative(
        "RANGE_COORDINATE_HOST_MULTIPLICATION",
        lambda: check_range_identity(
            2, source, multiply, wrong_ranges,
            lambda s, t: s[1],
            "RANGE_COORDINATE_HOST_MULTIPLICATION",
        ),
    )

    domain_ranges = derive_ranges(
        source, multiply, inverse, coordinate, use_domain=True
    )
    require(
        len({(domain_ranges[s], s[1]) for s in source}) == 8,
        "DOMAIN_IDEAL_MUTANT_F_STILL_INJECTIVE",
    )
    negative(
        "DOMAIN_IDEAL_HOST_MULTIPLICATION",
        lambda: check_range_identity(
            2, source, multiply, domain_ranges,
            lambda s, t: s[1],
            "DOMAIN_IDEAL_HOST_MULTIPLICATION",
        ),
    )

    negative(
        "OMITTED_SANDWICH_TWIST",
        lambda: check_range_identity(
            2, source, multiply, ranges,
            lambda s, t: (s[1] - 1) % 2,
            "OMITTED_SANDWICH_TWIST",
        ),
    )

    check_range_identity(
        2, source, multiply, ranges,
        lambda s, t: (-s[1]) % 2,
        "C2_INVERSE_TWIST_IS_IDENTICAL",
    )
    print("NONDISCRIMINATING_CONTROL", "inverse twist on C2")

    trivial_q = lambda s: 0
    require({trivial_q(s) for s in source} == {0}, "TRIVIAL_Q_ONTO")
    require(
        all(
            trivial_q(multiply(s, t)) == 0
            for s in source for t in source
        ),
        "TRIVIAL_Q_HOMOMORPHISM",
    )
    negative(
        "TRIVIAL_Q_PURITY",
        lambda: check_purity(
            source, multiply, {0}, trivial_q, "TRIVIAL_Q_PURITY"
        ),
    )

    collapsed_coordinate = make_iota(
        2, multiply, inverse, forget_group=True
    )
    negative(
        "TRIVIAL_IOTA_INJECTIVE",
        lambda: require(
            len({collapsed_coordinate(s) for s in source}) == len(source),
            "TRIVIAL_IOTA_INJECTIVE",
        ),
    )
    collapsed_ranges = derive_ranges(
        source, multiply, inverse, collapsed_coordinate
    )
    negative(
        "TRIVIAL_F_INJECTIVE",
        lambda: require(
            len({(collapsed_ranges[s], 0) for s in source}) == len(source),
            "TRIVIAL_F_INJECTIVE",
        ),
    )


def inverse_twist_c3_control():
    source, idempotents, multiply, inverse = source_model(3)
    validate_source(3, source, idempotents, multiply, inverse)
    validate_action(3, False)

    coordinate = make_iota(3, multiply, inverse)
    require(
        {coordinate(s) for s in source} == set(range(24)),
        "C3_IOTA_EXACT_POINT_UNIVERSE",
    )
    ranges = derive_ranges(source, multiply, inverse, coordinate)
    require(
        len({(ranges[s], s[1]) for s in source}) == 24,
        "C3_CORRECT_F_INJECTIVE",
    )
    check_range_identity(
        3, source, multiply, ranges,
        lambda s, t: s[1],
        "CORRECT_C3_RANGE_IDENTITY",
    )

    s = (7, 1)
    t = (1, 0)
    require(multiply(s, t) == (2, 1), "C3_SELECTED_PRODUCT")
    require(
        ranges[s] & shift(ranges[t], 1, 3) == ranges[(2, 1)],
        "C3_SELECTED_CORRECT_TWIST",
    )
    require(
        ranges[s] & shift(ranges[t], -1, 3) == ranges[(4, 1)],
        "C3_SELECTED_REVERSED_TWIST",
    )
    require(
        ranges[(2, 1)] != ranges[(4, 1)],
        "C3_CONTROL_DISCRIMINATES",
    )

    negative(
        "INVERSE_TWIST_C3_HOST_MULTIPLICATION",
        lambda: check_range_identity(
            3, source, multiply, ranges,
            lambda s, t: (-s[1]) % 3,
            "INVERSE_TWIST_C3_HOST_MULTIPLICATION",
        ),
    )
    print("C3_CONTROL", "source=24", "points=24", "pair_products=576")


def enumerate_homomorphisms(m, n):
    retained = []
    total = 0
    for values in itertools.product(range(n), repeat=m):
        tick()
        total += 1
        if all(
            values[(a + b) % m] == (values[a] + values[b]) % n
            for a in range(m) for b in range(m)
        ):
            retained.append(values)
    require(total == n ** m, "ALL_FUNCTIONS_ENUMERATED", (m, n, total))
    return total, tuple(retained)


def cyclic_group_checks(m):
    elements = tuple(range(m))
    multiply = lambda a, b: (a + b) % m
    require(
        {a for a in elements if multiply(a, a) == a} == {0},
        "CYCLIC_IDEMPOTENTS",
        m,
    )
    for a in elements:
        tick()
        require(
            multiply(a, (-a) % m) == 0
            and multiply((-a) % m, a) == 0,
            "CYCLIC_INVERSE",
            (m, a),
        )
        for b in elements:
            for c in elements:
                require(
                    multiply(multiply(a, b), c)
                    == multiply(a, multiply(b, c)),
                    "CYCLIC_ASSOCIATIVITY",
                    (m, a, b, c),
                )


def subgroup_host_checks():
    cyclic_group_checks(4)
    cyclic_group_checks(2)

    source = (0, 2)
    multiply = lambda a, b: (a + b) % 4
    r = {0: 0, 2: 2}
    q = {0: 0, 2: 1}
    f = {s: (0, s) for s in source}

    def initial_product(left, right):
        return (0, (left[1] + right[1]) % 4)

    require(
        {s for s in source if multiply(s, s) == s} == {0},
        "SUBGROUP_SOURCE_IDEMPOTENTS",
    )
    require(
        all((-s) % 4 in source for s in source),
        "SUBGROUP_INVERSE_CLOSURE",
    )
    require(len(set(f.values())) == 2, "INITIAL_HOST_EMBEDDING_INJECTIVE")
    require(set(r.values()) == {0, 2}, "INITIAL_ACTOR_SOURCE_IMAGE")
    require(set(r.values()) != set(range(4)), "INITIAL_ACTOR_NOT_SATURATED")
    require(set(q.values()) == {0, 1}, "SUBGROUP_Q_ONTO")

    for s in source:
        for t in source:
            st = multiply(s, t)
            require(st in source, "SUBGROUP_SOURCE_CLOSURE", (s, t))
            require(
                initial_product(f[s], f[t]) == f[st],
                "INITIAL_PHYSICAL_HOST_MULTIPLICATION",
                (s, t),
            )
            require(r[st] == (r[s] + r[t]) % 4, "SUBGROUP_R_HOM", (s, t))
            require(q[st] == (q[s] + q[t]) % 2, "SUBGROUP_Q_HOM", (s, t))

    check_purity(source, multiply, {0}, q.__getitem__, "SUBGROUP_Q_PURITY")
    check_purity(source, multiply, {0}, r.__getitem__, "SUBGROUP_R_PURITY")

    ker_r = {(s, t) for s in source for t in source if r[s] == r[t]}
    ker_q = {(s, t) for s in source for t in source if q[s] == q[t]}
    diagonal = {(s, s) for s in source}
    require(ker_r == ker_q == diagonal, "EXACT_KERNEL_EQUALITY")
    require(ker_r <= ker_q, "KERNEL_INCLUSION")

    total, homomorphisms = enumerate_homomorphisms(4, 2)
    require(total == 16, "C4_TO_C2_FUNCTION_COUNT")
    require(
        homomorphisms == ((0, 0, 0, 0), (0, 1, 0, 1)),
        "EXACT_C4_TO_C2_HOMOMORPHISMS",
        homomorphisms,
    )
    matching = tuple(
        values for values in homomorphisms
        if all(values[r[s]] == q[s] for s in source)
    )
    require(matching == (), "C4_NO_MATCHING_ACTOR_EXTENSION", matching)

    source_only = {s: (0, q[s]) for s in source}
    require(
        len(set(source_only.values())) == 2,
        "SOURCE_ONLY_EMBEDDING_INJECTIVE",
    )
    for s in source:
        for t in source:
            actual = (
                0,
                (source_only[s][1] + source_only[t][1]) % 2,
            )
            require(
                actual == source_only[multiply(s, t)],
                "SOURCE_ONLY_PHYSICAL_MULTIPLICATION",
                (s, t),
            )

    q_zero = {s: 0 for s in source}
    require(
        all(
            q_zero[multiply(s, t)] == (q_zero[s] + q_zero[t]) % 2
            for s in source for t in source
        ),
        "ALTERED_C2_QUOTIENT_STILL_HOM",
    )
    require(set(q_zero.values()) != {0, 1}, "ALTERED_C2_QUOTIENT_NOT_ONTO")
    require(
        {s for s in source if q_zero[s] == 0} != {0},
        "ALTERED_C2_QUOTIENT_NOT_PURE",
    )
    altered_kernel = {
        (s, t) for s in source for t in source if q_zero[s] == q_zero[t]
    }
    require(ker_r <= altered_kernel, "ALTERED_QUOTIENT_KERNEL_INCLUSION")
    altered_matching = tuple(
        values for values in homomorphisms
        if all(values[r[s]] == q_zero[s] for s in source)
    )
    require(len(altered_matching) == 2, "ALTERED_C2_EXTENSION_COUNT")
    negative(
        "ALTERED_C2_QUOTIENT_NO_EXTENSION",
        lambda: require(
            not altered_matching,
            "ALTERED_C2_QUOTIENT_NO_EXTENSION",
            altered_matching,
        ),
    )

    _, trivial_homomorphisms = enumerate_homomorphisms(4, 1)
    require(
        trivial_homomorphisms == ((0, 0, 0, 0),),
        "TRIVIAL_TARGET_UNIQUE_EXTENSION",
    )
    require({q_zero[s] for s in source} == {0}, "ALTERED_TRIVIAL_Q_ONTO")
    negative(
        "ALTERED_TRIVIAL_QUOTIENT_NO_EXTENSION",
        lambda: require(
            not trivial_homomorphisms,
            "ALTERED_TRIVIAL_QUOTIENT_NO_EXTENSION",
            trivial_homomorphisms,
        ),
    )

    cyclic_group_checks(6)
    source6 = (0, 3)
    multiply6 = lambda a, b: (a + b) % 6
    q6 = {0: 0, 3: 1}
    require(set(q6.values()) == {0, 1}, "C6_SUBGROUP_Q_ONTO")
    check_purity(
        source6, multiply6, {0}, q6.__getitem__, "C6_SUBGROUP_Q_PURITY"
    )
    require(
        all(
            q6[multiply6(s, t)] == (q6[s] + q6[t]) % 2
            for s in source6 for t in source6
        ),
        "C6_SUBGROUP_Q_HOM",
    )
    total6, homomorphisms6 = enumerate_homomorphisms(6, 2)
    require(total6 == 64, "C6_TO_C2_FUNCTION_COUNT")
    matching6 = tuple(
        values for values in homomorphisms6
        if all(values[s] == q6[s] for s in source6)
    )
    require(
        matching6 == ((0, 1, 0, 1, 0, 1),),
        "C6_MATCHING_EXTENSION",
        matching6,
    )
    phi6 = matching6[0]
    require(
        {a for a in range(6) if phi6[a] == 0} == {0, 2, 4},
        "C6_EXTENSION_EXACT_KERNEL",
    )
    negative(
        "C6_MATCHING_EXTENSION_PURITY",
        lambda: check_purity(
            tuple(range(6)), multiply6, {0},
            lambda a: phi6[a],
            "C6_MATCHING_EXTENSION_PURITY",
        ),
    )

    _, homomorphisms2 = enumerate_homomorphisms(2, 2)
    matching2 = tuple(
        values for values in homomorphisms2
        if values == (0, 1)
    )
    require(matching2 == ((0, 1),), "WHOLE_ACTOR_POSITIVE_EXTENSION")
    check_purity(
        (0, 1), lambda a, b: (a + b) % 2, {0},
        lambda a: matching2[0][a],
        "WHOLE_ACTOR_POSITIVE_EXTENSION_PURITY",
    )

    print(
        "SUBGROUP_HOST",
        "functions_C4_C2=", total,
        "homomorphisms=", homomorphisms,
        "matching_extensions=", matching,
        "source_only_image=", tuple(source_only[s] for s in source),
    )


def main():
    primary_checks()
    inverse_twist_c3_control()
    subgroup_host_checks()
    tick()
    print(
        "COMPLETED_ALL_NAMED_INVARIANTS",
        "elapsed_seconds=%.6f" % (time.monotonic() - START),
    )


if __name__ == "__main__":
    main()

