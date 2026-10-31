#!/usr/bin/env python3
"""F585 independent exact finite interfaces. Authored here; NOT_RUN by author.

Fixed in-memory inputs only. No author imports, files, network, children or writes.
Stdout is the sole result channel. Cooperative internal deadline: 53 seconds.
All generated global arrays are projected/local fixtures, NOT actual callers.
Requires Python >= 3.10 (int.bit_count).
"""
from itertools import combinations, permutations, product
from time import monotonic

START = monotonic()
LIMIT = 53.0
Y = (7, 1, 2, 4)
Q = (1, -1, -1, -1)
ZERO8 = (0,) * 8
CONTROL_NAMES = []


class FiniteError(Exception):
    def __init__(self, code, detail=""):
        self.code = code
        super().__init__(code + (": " + detail if detail else ""))


def need(condition, code, detail=""):
    if not condition:
        raise FiniteError(code, detail)


def tick():
    need(monotonic() - START <= LIMIT, "DEADLINE")


def dot(x, y):
    return (x & y).bit_count() & 1


def chi(x, y):
    return -1 if dot(x, y) else 1


def multiply(values):
    result = 1
    for value in values:
        result *= value
    return result


def fwht(values):
    result = list(values)
    size = len(result)
    need(size > 0 and size & (size - 1) == 0, "TRANSFORM_LENGTH")
    half = 1
    while half < size:
        for base in range(0, size, 2 * half):
            for j in range(half):
                left = result[base + j]
                right = result[base + j + half]
                result[base + j] = left + right
                result[base + j + half] = left - right
        half *= 2
    return tuple(result)


def direct_walsh(values):
    return tuple(sum(value * chi(p, x) for x, value in enumerate(values))
                 for p in range(len(values)))


def rejection(name, code, operation):
    tick()
    try:
        operation()
    except FiniteError as error:
        need(error.code == code, "WRONG_CONTROL_REASON", name + ": " + error.code)
    else:
        raise FiniteError("CONTROL_ACCEPTED", name)
    CONTROL_NAMES.append(name)


def inverse_block(fibres):
    numerators = fwht(fibres)
    need(all(x % 4 == 0 for x in numerators), "NONTERNARY_BLOCK")
    row = tuple(x // 4 for x in numerators)
    need(all(x in (-1, 0, 1) for x in row), "NONTERNARY_BLOCK")
    return row


def local_fibre_catalogue():
    actual = set()
    restricted = set()
    for row in product((-1, 0, 1), repeat=4):
        tick()
        fibres = fwht(row)
        need(fibres == direct_walsh(row), "FOUR_POINT_CONVENTION")
        need(inverse_block(fibres) == row, "FOUR_POINT_INVERSE")
        if fibres[1] in (-3, 0, 3):
            actual.add(fibres)
            if not (fibres[1] == 0 and abs(fibres[0]) == 4):
                restricted.add(fibres)
    predicted = set()
    for a, g, h0, h3 in product((-1, 1), repeat=4):
        if h0 * h3 == -a * g:
            predicted.add((h0, 3 * a, g, h3))
    for g in (-4, 4):
        predicted.add((0, 0, g, 0))
    for g, h in product((-2, 2), repeat=2):
        predicted.add((h, 0, g, 0))
        predicted.add((0, 0, g, h))
    predicted.add((0, 0, 0, 0))
    for h0, h3 in product((-2, 2), repeat=2):
        predicted.add((h0, 0, 0, h3))
    for h3 in (-4, 4):
        predicted.add((0, 0, 0, h3))
    need(len(actual) == 27 and len(restricted) == 25, "LOCAL_CATALOGUE_COUNT")
    need(restricted == predicted, "LOCAL_CATALOGUE_EQUALITY")
    need(inverse_block((1, 3, 1, -1)) == (1, 0, 1, -1), "PHYSICAL_POSITIVE")
    rejection("wrong-local-inverse-sign", "NONTERNARY_BLOCK",
              lambda: inverse_block((1, 3, 1, 1)))
    print("LOCAL: all81 ternary blocks; 27 U1-admissible; 25 local-H-admissible")


def check_q(q):
    need(len(q) == 4 and all(x in (-1, 1) for x in q)
         and multiply(q) == -1, "Q_SIGN_PRODUCT")


def odd_flat(d, q=Q):
    return all(abs(sum(q[k] * d[k] * chi(p, Y[k]) for k in range(4))) == 4
               for p in range(8))


def kind(d):
    nonzero = [i for i in range(4) if d[i] != 0]
    if len(nonzero) == 1 and abs(d[nonzero[0]]) == 4:
        return "C"
    if all(abs(x) == 2 for x in d) and multiply(x // 2 for x in d) == 1:
        return "B"
    return None


def recover_levels(d0, d1):
    need(all((x + y) % 2 == 0 and (x - y) % 2 == 0
             for x, y in zip(d0, d1)), "LEVEL_PARITY")
    left = tuple((x + y) // 2 for x, y in zip(d0, d1))
    right = tuple((x - y) // 2 for x, y in zip(d0, d1))
    need(all(x in (-2, 0, 2) for x in left + right), "LEVEL_ALPHABET")
    return left, right


def projected_patterns():
    check_q(Q)
    shapes = set()
    shape_counts = {"C": 0, "B": 0}
    for signs in product((-1, 1), repeat=4):
        tick()
        inverse = fwht(signs)
        need(fwht(inverse) == tuple(4 * x for x in signs), "FOUR_SIGN_INVERSION")
        d = tuple(Q[i] * inverse[i] for i in range(4))
        need(odd_flat(d) and kind(d) is not None, "FOUR_SIGN_SHAPE")
        shapes.add(d)
        shape_counts[kind(d)] += 1
    direct_shapes = set()
    for d in product((-4, -2, 0, 2, 4), repeat=4):
        tick()
        need(odd_flat(d) == (kind(d) is not None), "PROJECTED_CLASSIFICATION")
        if odd_flat(d):
            direct_shapes.add(d)
    need(shapes == direct_shapes and shape_counts == {"C": 8, "B": 8},
         "FOUR_SIGN_COMPLETE")
    counts = {"CC": 0, "BB": 0}
    inspected = 0
    for values in product((-2, 0, 2), repeat=8):
        tick()
        inspected += 1
        left, right = values[:4], values[4:]
        d0 = tuple(x + y for x, y in zip(left, right))
        d1 = tuple(x - y for x, y in zip(left, right))
        k0, k1 = kind(d0), kind(d1)
        need(odd_flat(d0) == (k0 is not None), "LEVEL_FOURIER_ZERO")
        need(odd_flat(d1) == (k1 is not None), "LEVEL_FOURIER_ONE")
        if k0 is None or k1 is None:
            continue
        need(k0 == k1, "MIXED_CC_BB")
        need(recover_levels(d0, d1) == (left, right), "LEVEL_INVERSION")
        if k0 == "B":
            need(all((x != 0) + (y != 0) == 1 for x, y in zip(left, right)),
                 "BB_ACTIVE_LEVELS")
            need(multiply(x // 2 for x in d0) == 1
                 and multiply(x // 2 for x in d1) == 1, "BB_PRODUCTS")
            counts["BB"] += 1
        else:
            double = {i for i in range(4) if left[i] and right[i]}
            empty = {i for i in range(4) if left[i] == right[i] == 0}
            first = next(i for i, x in enumerate(d0) if x)
            second = next(i for i, x in enumerate(d1) if x)
            need(len(double) == len(empty) == 2 and first != second
                 and {first, second} == double, "CC_OPPOSITE_ROUTING")
            counts["CC"] += 1
    need(inspected == 6561 and counts == {"CC": 48, "BB": 64}, "LEVEL_COUNTS")
    need(odd_flat((2, 2, 2, 2))
         and not odd_flat((2, 2, 2, 2), (1, 1, 1, 1)), "Q_SIGN_SENSITIVITY")
    rejection("wrong-q-product", "Q_SIGN_PRODUCT", lambda: check_q((1, 1, 1, 1)))
    rejection("mixed-C-B-levels", "LEVEL_ALPHABET",
              lambda: recover_levels((4, 0, 0, 0), (2, 2, 2, 2)))
    print("PROJECTED: all16 signs=8C+8B; all625 d-vectors; all6561 levels=48CC+64BB")


def check_cube_zeros(signs):
    transformed = fwht(signs)
    need(all(transformed[y] == 0 for y in (3, 5, 6)), "CUBE_MISSING_VANISH")
    return transformed


def cube_rows():
    accepted = set()
    alternatives = {"constant": 0, "C": 0, "B": 0}
    for signs in product((-1, 1), repeat=8):
        tick()
        transformed = fwht(signs)
        need(transformed == direct_walsh(signs), "CUBE_CONVENTION")
        if any(transformed[y] for y in (3, 5, 6)):
            continue
        accepted.add(signs)
        constant = len(set(signs)) == 1
        anti = all(signs[p ^ 7] == -signs[p] for p in range(8))
        need(constant != anti, "CUBE_CONSTANT_OR_ANTI")
        a0 = transformed[0] // 2
        a_y = tuple(transformed[y] // 2 for y in Y)
        if constant:
            need(abs(a0) == 4 and a_y == (0, 0, 0, 0), "CUBE_E_CONSTANT")
            alternatives["constant"] += 1
        elif sum(x != 0 for x in a_y) == 1:
            need(a0 == 0 and max(abs(x) for x in a_y) == 4, "CUBE_A_SPIKE")
            alternatives["C"] += 1
        else:
            need(a0 == 0 and all(abs(x) == 2 for x in a_y)
                 and multiply(x // 2 for x in a_y) == -1, "CUBE_A_BENT_SIGN")
            alternatives["B"] += 1
    predicted = {(-1,) * 8, (1,) * 8}
    for four in product((-1, 1), repeat=4):
        signs = [0] * 8
        for p in range(4):
            signs[p], signs[p ^ 7] = four[p], -four[p]
        predicted.add(tuple(signs))
    need(accepted == predicted and len(accepted) == 18
         and alternatives == {"constant": 2, "C": 8, "B": 8}, "CUBE_COMPLETE")
    rejection("drop-one-cube-vanishing", "CUBE_MISSING_VANISH",
              lambda: check_cube_zeros(tuple(chi(3, p) for p in range(8))))
    print("CUBE: all256 signs; exactly18 admissible=2 constant+8C+8B")


def linear_image(x, first, second):
    return (first if x & 1 else 0) ^ (second if x & 2 else 0)


def matching_valid(mapping):
    need(tuple(sorted(mapping)) == (0, 1, 2, 3), "MATCHING_NOT_PERMUTATION")
    need(len({x ^ mapping[x] for x in range(4)}) == 4, "DIRECTION_COVER")


def embed_c(x, delta):
    return (x << 1) | dot(x, delta)


def matchings():
    good = []
    endpoint_counts = [0] * 4
    for mapping in permutations(range(4)):
        tick()
        b = mapping[0]
        first, second = mapping[1] ^ b, mapping[2] ^ b
        need(all(mapping[x] == (linear_image(x, first, second) ^ b)
                 for x in range(4)), "PERMUTATION_NOT_AFFINE")
        linear = tuple(linear_image(x, first, second) for x in range(4))
        cover = len({x ^ mapping[x] for x in range(4)}) == 4
        order_three = (linear != (0, 1, 2, 3)
                       and all(linear[linear[linear[x]]] == x for x in range(4)))
        need(cover == order_three, "ORDER_THREE_EQUIVALENCE")
        if cover:
            matching_valid(mapping)
            fixed = [x for x in range(4) if mapping[x] == x]
            need(len(fixed) == 1, "E_ENDPOINT_UNIQUENESS")
            endpoint_counts[fixed[0]] += 1
            need(b == (fixed[0] ^ linear[fixed[0]]), "E_ENDPOINT_TRANSLATION")
            good.append(mapping)
        for delta in range(4):
            d = 1 | (delta << 1)
            pairs = [(embed_c(x, delta), 1 ^ embed_c(mapping[x], delta))
                     for x in range(4)]
            need({a for a, _ in pairs} == {e for e in range(8) if dot(e, d) == 0}
                 and {b0 for _, b0 in pairs} == {e for e in range(8) if dot(e, d) == 1},
                 "BIPARTITE_MATCHING")
            directions = {a ^ b0 for a, b0 in pairs}
            need((directions == {e for e in range(8) if dot(e, d) == 1}) == cover,
                 "GEOMETRIC_DIRECTION_COVER")
    need(len(good) == 8 and endpoint_counts == [2, 2, 2, 2], "MATCHING_COUNTS")
    rejection("arbitrary-GL-order-two", "DIRECTION_COVER",
              lambda: matching_valid((0, 2, 1, 3)))
    print("MATCHING: all24 permutations affine; 8 direction covers; 2 per fixed E endpoint")
    return tuple(good)


def affine_rank(points):
    anchor = points[0]
    basis = {}
    for point in points[1:]:
        value = point ^ anchor
        while value:
            pivot = value.bit_length() - 1
            if pivot in basis:
                value ^= basis[pivot]
            else:
                basis[pivot] = value
                break
    return len(basis)


def signed_row(points, signs):
    row = [0] * 8
    for point, sign in zip(points, signs):
        row[point] = sign
    return tuple(row)


def signed_support_catalogue():
    counts = {"line": 0, "plane_character": 0, "plane_bent": 0, "nonplanar": 0}
    support_counts = {2: 0, 3: 0}
    endpoint_checks = 0
    for size in (2, 4):
        for points in combinations(range(8), size):
            rank = affine_rank(points)
            if size == 4:
                support_counts[rank] += 1
            for signs in product((-1, 1), repeat=size):
                tick()
                row = signed_row(points, signs)
                transformed = fwht(row)
                need(transformed == direct_walsh(row), "SIGNED_ROW_CONVENTION")
                need(fwht(transformed) == tuple(8 * x for x in row)
                     and sum(x * x for x in transformed) == 8 * size, "SIGNED_ROW_PARSEVAL")
                if size == 2:
                    direction = points[0] ^ points[1]
                    parity = 0 if signs[0] == signs[1] else 1
                    hyperplane = {e for e in range(8) if dot(e, direction) == parity}
                    need({e for e in range(8) if transformed[e]} == hyperplane
                         and all(abs(transformed[e]) == 2 for e in hyperplane),
                         "SIGNED_LINE_HYPERPLANE")
                    for normal in range(1, 8):
                        if dot(normal, direction):
                            continue
                        for theta in range(8):
                            if transformed[theta]:
                                continue
                            endpoint_checks += 1
                            need(transformed[theta ^ normal] == 0
                                 and hyperplane == {e for e in range(8)
                                                    if dot(e, direction) == (1 ^ dot(theta, direction))},
                                 "SIGNED_LINE_E_PAIR")
                    counts["line"] += 1
                elif rank == 2:
                    normals = [e for e in range(1, 8)
                               if len({dot(e, x) for x in points}) == 1]
                    need(len(normals) == 1, "PLANE_NORMAL")
                    peaks = [e for e in range(8) if abs(transformed[e]) == 4]
                    if len(peaks) == 2:
                        need(peaks[0] ^ peaks[1] == normals[0]
                             and all(transformed[e] == 0 for e in range(8) if e not in peaks),
                             "PLANE_CHARACTER_PAIR")
                        phase = peaks[0]
                        need(all(row[x] == (transformed[phase] // 4) * chi(phase, x)
                                 for x in points), "PLANE_ACTUAL_SIGNS")
                        counts["plane_character"] += 1
                    else:
                        need(not peaks and all(abs(x) == 2 for x in transformed), "PLANE_BENT")
                        counts["plane_bent"] += 1
                else:
                    need(rank == 3, "FOUR_POINT_AFFINE_RANK")
                    direction = points[0] ^ points[1] ^ points[2] ^ points[3]
                    need(direction != 0, "NONPLANAR_XOR")
                    peaks = [e for e in range(8) if abs(transformed[e]) == 4]
                    need(len(peaks) == 1, "NONPLANAR_UNIQUE_PEAK")
                    theta = peaks[0]
                    need(all(row[x] == (transformed[theta] // 4) * chi(theta, x)
                             for x in points), "NONPLANAR_ACTUAL_SIGNS")
                    hyperplane = {e for e in range(8)
                                  if dot(e, direction) == (1 ^ dot(theta, direction))}
                    need({e for e in range(8) if abs(transformed[e]) == 2} == hyperplane
                         and all(transformed[e] == 0 for e in range(8)
                                 if e not in hyperplane and e != theta), "NONPLANAR_BENT_HYPERPLANE")
                    counts["nonplanar"] += 1
    need(support_counts == {2: 14, 3: 56}, "SUPPORT_GEOMETRY_COUNTS")
    need(counts == {"line": 112, "plane_character": 112,
                    "plane_bent": 112, "nonplanar": 896}
         and endpoint_checks == 1344, "SIGNED_SUPPORT_COUNTS")
    print("SUPPORT: 112 signed lines; 112 plane characters; 112 plane bent; 896 nonplanar rows")


def odd_tally_ok(tally):
    need(len(tally) == 4 and all(isinstance(x, int) and x >= 0 for x in tally), "ODD_TALLY_DOMAIN")
    need(sum(tally) == 256, "ODD_TALLY_TOTAL")
    need(sum(n * a * a for n, a in zip(tally, (2, 6, 10, 14))) == 256 * 140, "ODD_ENERGY")


def require_minimum(claim, tallies):
    need(claim == min(t[3] for t in tallies), "MINIMUM_MISMATCH")


def odd_tallies():
    first, second, parameterized = set(), set(), set()
    for n2 in range(257):
        for n6 in range(257 - n2):
            tick()
            numerator = 320 + 2 * n6
            if numerator % 3:
                continue
            n14 = n2 + numerator // 3
            n10 = 256 - n2 - n6 - n14
            if n10 >= 0:
                tally = (n2, n6, n10, n14)
                odd_tally_ok(tally)
                first.add(tally)
    for n14 in range(257):
        for n6 in range(257 - n14):
            tick()
            numerator = 3 * n14 - 2 * n6 - 320
            if numerator < 0 or numerator % 3:
                continue
            n2 = numerator // 3
            n10 = 256 - n2 - n6 - n14
            if n10 >= 0:
                tally = (n2, n6, n10, n14)
                odd_tally_ok(tally)
                second.add(tally)
    for k in range(30):
        for n2 in range((146 - 5 * k) // 2 + 1):
            parameterized.add((n2, 2 + 3 * k, 146 - 2 * n2 - 5 * k, n2 + 108 + 2 * k))
    need(first == second == parameterized and len(first) == 1125, "ODD_TALLY_COMPLETENESS")
    need(min(t[3] for t in first) == 108
         and {t for t in first if t[3] == 108} == {(0, 2, 146, 108)}, "ODD_EQUALITY_CASE")
    rejection("false-107-cap-tally", "ODD_ENERGY", lambda: odd_tally_ok((0, 2, 147, 107)))
    rejection("false-declared-minimum-107", "MINIMUM_MISMATCH", lambda: require_minimum(107, first))
    print("ODD: all1125 integer energy tallies; minimum N14=108; unique tally=(0,2,146,108)")


def rows_to_vector(rows):
    return tuple(rows.get(y, ZERO8)[z] for z in range(8) for y in range(8))


def check_ag(a_rows, g_rows):
    a, g = rows_to_vector(a_rows), rows_to_vector(g_rows)
    need(all(x in (-1, 0, 1) for x in a) and sum(x != 0 for x in a) == 16,
         "A_SPATIAL_DOMAIN")
    need(all(abs(x) == 4 for x in fwht(a)), "A_FULL_FLATNESS")
    need(all(abs(g[i]) == 1 for i in range(64) if a[i]), "SHARED_A_G_SUPPORT")
    need({m: sum(abs(x) == m for x in g) for m in (0, 1, 2, 4)}
         == {0: 24, 1: 16, 2: 22, 4: 2}, "G_OCCUPANCIES")
    transformed = fwht(g)
    need(all(transformed[r] == 4 if r in (0, 1, 2, 4) else abs(transformed[r]) == 12
             for r in range(64)), "G_FULL_SHELL")
    need(sum(x * x for x in g) == 136, "G_ENERGY")
    return a, g


def complement_guard(u, v, require_caps=False):
    need(len(u) == len(v) == 256 and all(x in (-1, 0, 1) for x in u + v),
         "PAIR_DOMAIN")
    need(all(x * x + y * y == 1 and x * y == 0 for x, y in zip(u, v)),
         "COMPLEMENT_SUPPORT")
    need(all(x + y in (-1, 1) and x - y in (-1, 1) for x, y in zip(u, v)),
         "BOOLEAN_PAIR_INVERSE")
    if require_caps:
        need(all(abs(x) in (2, 6, 10, 14) for x in fwht(v)), "ODD_CAP")


def h0_spectrum_guard(spectrum, transported_balance):
    need(len(spectrum) == 64 and all(x in (-8, 0, 8) for x in spectrum)
         and spectrum.count(0) == 8, "H0_SPECTRAL_SHELL")
    need(0 <= transported_balance < 64 and spectrum[transported_balance] == 0,
         "TRANSPORTED_BALANCE")


def local_completion_scope_controls(a, g):
    h0, h3 = [0] * 64, [0] * 64
    magnitude_two = [i for i in range(64) if abs(g[i]) == 2]
    zero = [i for i in range(64) if g[i] == 0]
    for i in range(64):
        if a[i]:
            h0[i], h3[i] = 1, -a[i] * g[i]
    for position, i in enumerate(magnitude_two):
        if position < 4:
            h0[i] = 2
        else:
            h3[i] = 2
    for i in zero[:6]:
        h0[i] = h3[i] = 2
    h3[zero[6]] = 4
    u = tuple(value for i in range(64)
              for value in inverse_block((h0[i], 3 * a[i], g[i], h3[i])))
    need(sum(x != 0 for x in u) == 116
         and sum(x * x for x in h0) == 56
         and sum(x * x for x in h3) == 128
         and h3.count(0) == 23, "LOCAL_COMPLETION_COUNTS")
    v = tuple(1 if x == 0 else 0 for x in u)
    need(sum(x != 0 for x in v) == 140, "LOCAL_COMPLEMENT_COUNT")
    complement_guard(u, v)
    need(fwht(v)[0] == 140, "LOCAL_COMPLEMENT_DC")
    fake = list(v)
    occupied = next(i for i, x in enumerate(u) if x)
    empty = next(i for i, x in enumerate(u) if x == 0)
    fake[occupied], fake[empty] = 1, 0
    need(sum(x != 0 for x in fake) == 140, "FAKE_COMPLEMENT_COUNT")
    rejection("SCOPE_GUARD-V-without-actual-complement", "COMPLEMENT_SUPPORT",
              lambda: complement_guard(u, tuple(fake)))
    rejection("SCOPE_GUARD-actual-complement-without-cap", "ODD_CAP",
              lambda: complement_guard(u, v, True))
    spectrum = (0,) * 8 + (8,) * 56
    h0_spectrum_guard(spectrum, 0)
    rejection("SCOPE_GUARD-dropped-transported-balance", "TRANSPORTED_BALANCE",
              lambda: h0_spectrum_guard(spectrum, 8))
    print("SCOPE_GUARD: one actual local ternary U has116 support; its + complement fails DC cap")


def coupled_fixtures(good_matchings):
    together_count = 0
    first_ag = None
    for delta in range(4):
        g_rows = {0: tuple(1 if z & 1 == 0 else -2 for z in range(8))}
        full = {0, 1 | (delta << 1)}
        g_rows[Y[0]] = tuple(Q[0] * (6 if z in full else 0) - 2 * Q[0]
                                  for z in range(8))
        for index, ell in enumerate((1, 2, 3), start=1):
            normal = ((1 ^ dot(ell, delta)) | (ell << 1))
            g_rows[Y[index]] = tuple(Q[index] * (3 * int(dot(normal, z) == 0) - 2)
                                          for z in range(8))
        for mapping in good_matchings:
            fixed = next(x for x in range(4) if mapping[x] == x)
            base_rows = {0: tuple(chi(embed_c(fixed, delta), z) if z & 1 == 0 else 0
                                  for z in range(8)), Y[0]: ZERO8}
            for index, ell in enumerate((1, 2, 3), start=1):
                normal = ((1 ^ dot(ell, delta)) | (ell << 1))
                x = next(x for x in range(4) if x ^ mapping[x] == ell)
                phase = embed_c(x, delta)
                base_rows[Y[index]] = tuple(chi(phase, z) if dot(normal, z) == 0 else 0
                                                 for z in range(8))
            for signs in product((-1, 1), repeat=4):
                tick()
                a_rows = dict(base_rows)
                for y, sign in zip((0,) + Y[1:], signs):
                    a_rows[y] = tuple(sign * value for value in base_rows[y])
                a, g = check_ag(a_rows, g_rows)
                need(affine_rank(tuple(i for i, x in enumerate(a) if x)) == 6,
                     "TOGETHER_SIX_SPAN")
                if first_ag is None:
                    first_ag = (a, g)
                together_count += 1
    split_count = 0
    for lam in (1, 2, 3):
        for mu in (1, 2, 3):
            if mu == lam:
                continue
            nu = lam ^ mu
            supports = {
                0: {z for z in range(8) if z & 1 == 0},
                Y[0]: {z for z in range(8) if z & 1 and dot(lam, z >> 1) == 0},
                Y[1]: {z for z in range(8) if z & 1 and dot(lam, z >> 1) == 1},
                Y[2]: {z for z in range(8)
                       if (z & 1 == 0 and dot(mu, z >> 1) == 0)
                       or (z & 1 and dot(nu, z >> 1) == 0)},
            }
            supports[Y[3]] = set(supports[Y[2]])
            g_rows = {0: tuple(3 * int(z in supports[0]) - 2 for z in range(8))}
            for index, y in enumerate(Y):
                g_rows[y] = tuple(Q[index] * (3 * (int(z in supports[y])
                                       + 2 * int(index < 2 and z == 0)) - 2)
                                       for z in range(8))
            phases = {0: 0, Y[0]: mu << 1, Y[1]: mu << 1,
                      Y[2]: lam << 1, Y[3]: (lam << 1) ^ 1}
            base_rows = {y: tuple(chi(phases[y], z) if z in supports[y] else 0
                                   for z in range(8)) for y in (0,) + Y}
            direction = next(t << 1 for t in (1, 2, 3) if dot(lam, t) == 0)
            for theta in range(8):
                for e_sign in (-1, 1):
                    for first_three in product((-1, 1), repeat=3):
                        tick()
                        signs = first_three + (multiply(first_three),)
                        a_rows = {0: tuple(e_sign * chi(theta, z) * base_rows[0][z]
                                           for z in range(8))}
                        for y, sign in zip(Y, signs):
                            a_rows[y] = tuple(sign * chi(theta, z) * base_rows[y][z]
                                              for z in range(8))
                        a, g = check_ag(a_rows, g_rows)
                        need(affine_rank(tuple(i for i, x in enumerate(a) if x)) == 6,
                             "SPLIT_SIX_SPAN")
                        transformed_rows = {y: fwht(a_rows[y]) for y in (0,) + Y}
                        e_pair = {eta for eta in range(8) if transformed_rows[0][eta]}
                        h_a = {eta for eta in range(8) if dot(eta, direction) == (1 ^ dot(theta, direction))}
                        last_pair = {theta ^ (lam << 1), theta ^ (lam << 1) ^ 1}
                        need(e_pair == {theta, theta ^ 1}
                             and e_pair.isdisjoint(h_a) and last_pair.isdisjoint(h_a)
                             and e_pair | last_pair | h_a == set(range(8)), "SPLIT_COMMON_PARTITION")
                        for eta in h_a:
                            need(all(abs(transformed_rows[y][eta]) == 2 for y in Y)
                                 and multiply(transformed_rows[y][eta] // 2 for y in Y) == -1,
                                 "SPLIT_COMMON_ACTUAL_SIGNS")
                        peaks = [{eta for eta in range(8) if abs(transformed_rows[y][eta]) == 4}
                                 for y in Y[2:]]
                        need(all(len(p) == 1 for p in peaks) and peaks[0].isdisjoint(peaks[1])
                             and peaks[0] | peaks[1] == last_pair, "SPLIT_DISTINCT_LAST_ENDPOINTS")
                        split_count += 1
    need(together_count == 512 and split_count == 768, "COUPLED_FIXTURE_COUNTS")
    need(first_ag is not None, "NO_LOCAL_FIXTURE")
    local_completion_scope_controls(*first_ag)
    print("COUPLED: 512 together+768 split shared signed (a,g) fixtures; no original caller certification")


def main():
    local_fibre_catalogue()
    projected_patterns()
    cube_rows()
    good_matchings = matchings()
    signed_support_catalogue()
    odd_tallies()
    coupled_fixtures(good_matchings)
    tick()
    need(len(CONTROL_NAMES) == 10 and len(set(CONTROL_NAMES)) == 10, "CONTROL_COUNTS")
    print("CONTROLS: 10 intended-reason rejections: " + "; ".join(CONTROL_NAMES))
    print("FINITE_INTERFACES_COMPLETE; NO_ACTUAL_CALLER; SAME_HARNESS_ONLY")
    print("elapsed_seconds=" + format(monotonic() - START, ".6f"))


if __name__ == "__main__":
    main()

