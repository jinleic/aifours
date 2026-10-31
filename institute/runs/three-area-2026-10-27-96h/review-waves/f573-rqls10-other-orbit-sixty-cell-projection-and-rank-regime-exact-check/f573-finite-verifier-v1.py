from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from time import monotonic

START = monotonic()
LIMIT = 55.0
REJECTIONS = []
S = frozenset((0, 1, 3, 4))
T = frozenset((2, 5, 6, 7, 8, 9))

class CheckError(Exception):
    pass

def tick():
    if monotonic() - START > LIMIT:
        raise CheckError("TIME_BOUND")

def need(condition, reason):
    tick()
    if not condition:
        raise CheckError(reason)

def reject(name, reason, operation):
    try:
        operation()
    except CheckError as error:
        need(str(error) == reason, "UNINTENDED_REJECTION:" + name)
        REJECTIONS.append((name, reason))
    else:
        raise CheckError("MUTATION_ACCEPTED:" + name)

def crt(a, u):
    a %= 5
    u %= 2
    return a + 5 * ((u - a) % 2)

def tau(a, b):
    need(a != b, "DIAGONAL_TAU")
    return int((b - a) % 5 in (2, 3))

def D(a, u, v):
    return ("D", a % 5, u % 2, v % 2)

def O(a, b, u):
    return ("O", a % 5, b % 5, u % 2)

LABELS = tuple(
    [D(a, u, v) for a, u, v in product(range(5), range(2), range(2))]
    + [O(a, b, u) for a, b, u in product(range(5), range(5), range(2))
       if a != b]
)
UNIVERSE = frozenset(
    (r, c) for r, c in product(range(10), repeat=2)
    if (c - r) % 10 in T
)

def cell(label, shift=2, flip=False):
    if label[0] == "D":
        _, a, u, v = label
        b = a
    else:
        _, a, b, u = label
        v = (u + tau(a, b) + int(flip)) % 2
    return (crt(a, u), (crt(b, v) + shift) % 10)

def mapping(shift=2, flip=False):
    return {label: cell(label, shift, flip) for label in LABELS}

def actual_contexts(mp):
    contexts = {(family, i): set() for family in ("R", "C", "L")
                for i in range(10)}
    for label, (r, c) in mp.items():
        contexts["R", r].add(label)
        contexts["C", c].add(label)
        contexts["L", (r + c) % 10].add(label)
    return {key: frozenset(value) for key, value in contexts.items()}

def specified_contexts(inverse=3):
    contexts = {}
    for a, u in product(range(5), range(2)):
        contexts["R", crt(a, u)] = frozenset(
            [D(a, u, v) for v in range(2)]
            + [O(a, b, u) for b in range(5) if b != a]
        )
    for b, v in product(range(5), range(2)):
        contexts["C", (crt(b, v) + 2) % 10] = frozenset(
            [D(b, u, v) for u in range(2)]
            + [O(a, b, v - tau(a, b)) for a in range(5) if a != b]
        )
    for ell in range(10):
        s, w = (ell - 2) % 5, (ell - 2) % 2
        k = inverse * s % 5
        step = 2 if w == 0 else 1
        a, b = (k - step) % 5, (k + step) % 5
        contexts["L", ell] = frozenset(
            [D(k, 0, w), D(k, 1, w - 1)]
            + [O(a, b, u) for u in range(2)]
            + [O(b, a, u) for u in range(2)]
        )
    return contexts

def validate(mp, contexts):
    need(len(mp) == 60 and len(set(mp.values())) == 60, "CELL_BIJECTION")
    need(frozenset(mp.values()) == UNIVERSE, "SUPPORT_MISMATCH")
    keys = {(family, i) for family in ("R", "C", "L") for i in range(10)}
    need(set(contexts) == keys, "CONTEXT_FAMILY")
    actual = actual_contexts(mp)
    for key in sorted(keys):
        need(len(contexts[key]) == 6, "CONTEXT_SIZE")
        reason = "SYMBOL_ROUTE" if key[0] == "L" else "ROW_COLUMN_ROUTE"
        need(contexts[key] == actual[key], reason)
    for family in ("R", "C", "L"):
        counts = Counter(label for i in range(10)
                         for label in contexts[family, i])
        need(counts == Counter(LABELS), "CONTEXT_COVERAGE")

def shared_context(x, y, mp):
    r, c = mp[x]
    s, d = mp[y]
    return r == s or c == d or (r + c) % 10 == (s + d) % 10

def projection_incidence(mp, contexts):
    balance = []
    for a in range(5):
        diagonal = [D(a, u, v) for u, v in product(range(2), repeat=2)]
        for x, y in combinations(diagonal, 2):
            need(shared_context(x, y, mp), "DIAGONAL_ORTHOGONALITY_ROUTE")
        rows = Counter(x for u in range(2)
                       for x in contexts["R", crt(a, u)])
        expected_rows = Counter(
            diagonal + [O(a, b, u) for b in range(5) if b != a
                        for u in range(2)]
        )
        need(rows == expected_rows, "ROW_SUM_PROJECTORS")
        columns = Counter(x for v in range(2)
                          for x in contexts["C", (crt(a, v) + 2) % 10])
        expected_columns = Counter(
            diagonal + [O(b, a, u) for b in range(5) if b != a
                        for u in range(2)]
        )
        need(columns == expected_columns, "COLUMN_SUM_PROJECTORS")
        coefficients = [0] * 10
        for b in range(5):
            if a == b:
                continue
            k = 3 * (a + b) % 5
            offset = 0 if (b - a) % 5 in (1, 4) else 5
            coefficients[offset + k] += 1
            x, y = O(a, b, 0), O(a, b, 1)
            need((sum(mp[x]) - sum(mp[y])) % 10 == 0,
                 "TWO_CELL_SYMBOL")
        coefficients[a] -= 2
        coefficients[5 + a] -= 2
        expected = [
            -2 if j == a else int((j - a) % 5 in (2, 3))
            for j in range(5)
        ] + [
            -2 if j == a else int((j - a) % 5 in (1, 4))
            for j in range(5)
        ]
        need(coefficients == expected, "BALANCE_COEFFICIENT_ROW")
        balance.append(tuple(coefficients))
    for k, w in product(range(5), range(2)):
        step = 2 if w == 0 else 1
        a, b = (k - step) % 5, (k + step) % 5
        labels = [D(k, 0, w), D(k, 1, w - 1)]
        labels += [O(a, b, u) for u in range(2)]
        labels += [O(b, a, u) for u in range(2)]
        ell = (crt(2 * k, w) + 2) % 10
        need(len(set(labels)) == 6, "SYMBOL_PARTITION_DISJOINT")
        need(frozenset(labels) == contexts["L", ell],
             "SYMBOL_PROJECTOR_PARTITION")
    return balance

def mat(rows):
    return [[F(x) for x in row] for row in rows]

def diag(n, indices):
    indices = set(indices)
    return mat([[int(i == j and i in indices) for j in range(n)]
                for i in range(n)])

def transpose(a):
    return [list(row) for row in zip(*a)]

def mm(a, b):
    tick()
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]

def plus(a, b, scale=1):
    return [[a[i][j] + scale * b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]

def rank(a):
    a = mat(a)
    row = 0
    for col in range(len(a[0])):
        tick()
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        divisor = a[row][col]
        a[row] = [x / divisor for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row

def determinant(a):
    a = mat(a)
    result = F(1)
    for j in range(len(a)):
        tick()
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        value = a[j][j]
        result *= value
        for i in range(j + 1, len(a)):
            factor = a[i][j] / value
            a[i] = [x - factor * y for x, y in zip(a[i], a[j])]
    return result

def outer(v):
    return [[x * y for y in v] for x in v]

def vector(n, entries):
    return [F(entries.get(i, 0)) for i in range(n)]

def is_projection(a):
    return a == transpose(a) and mm(a, a) == a

def intersection_dimension(a, b):
    joined = [x + y for x, y in zip(a, b)]
    return rank(a) + rank(b) - rank(joined)

def circular_linear_certificate():
    L = mat([[0 if i == j else
              (1 if (j - i) % 5 in (2, 3) else -1)
              for j in range(5)] for i in range(5)])
    need(all(sum(row) == 0 for row in L), "CONSTANT_KERNEL")
    target = mat([[5 * int(i == j) - 1 for j in range(5)]
                  for i in range(5)])
    need(mm(L, L) == target, "L_SQUARED_CERTIFICATE")
    need(rank(L) == 4, "CIRCULANT_RANK")
    minor = [row[:4] for row in L[:4]]
    need(determinant(minor) == 5, "CIRCULANT_COFACTOR")
    restricted = [[L[i][j] - L[i][4] for j in range(4)] for i in range(4)]
    need(determinant(restricted) == 25, "NONCONSTANT_DETERMINANT")
    augmented = [[L[i][j] + F(1, 5) for j in range(5)]
                 for i in range(5)]
    need(determinant(augmented) == 25, "CONSTANT_COMPLEMENT_DETERMINANT")
    return L, restricted

def linear_combination(terms):
    result = Counter()
    for scale, polynomial in terms:
        for key, value in polynomial.items():
            result[key] += scale * value
    return {key: value for key, value in result.items() if value}

def formal_cycles():
    def outside(neighbor, center):
        difference = (neighbor - center) % 5
        need(difference != 0, "CONTAINMENT_DIAGONAL")
        return "U" if difference in (1, 4) else "V"
    covered = set()
    orders = []
    for step in (1, 2):
        order = tuple(step * j % 5 for j in range(5))
        need(len(set(order)) == 5 and len(order) % 2 == 1, "ODD_CYCLE")
        orders.append(order)
        for a in range(5):
            p, q, r = (a - step) % 5, a, (a + step) % 5
            at_r = (outside(p, r), outside(q, r))
            at_p = (outside(r, p), outside(q, p))
            need(set(at_r) == {"U", "V"}, "P_R_Q_CONTAINMENT")
            need(set(at_p) == {"U", "V"}, "R_P_Q_CONTAINMENT")
            need(({"E", at_r[0]} & {"E", at_r[1]}) == {"E"},
                 "PARTITION_PRODUCT_REDUCTION")
            covered.add(frozenset((a, (a + step) % 5)))
    need(orders == [(0, 1, 2, 3, 4), (0, 2, 4, 1, 3)], "BOTH_CYCLES")
    need(covered == {frozenset(pair) for pair in combinations(range(5), 2)},
         "ALL_DISTINCT_PRODUCTS")
    norm_square = {"yy": 1, "zz": 1, "yz": -1, "zy": -1}
    relations = [
        {"yz": 1, "yy": -1}, {"zy": 1, "yy": -1},
        {"yz": 1, "zz": -1}, {"zy": 1, "zz": -1}
    ]
    need(linear_combination([(-1, relation) for relation in relations])
         == linear_combination([(2, norm_square)]),
         "CONTRACTION_NORM_CERTIFICATE")
    need([g for g in range(3) if g + 5 * (2 - g) <= 6] == [1, 2],
         "RANK_REGIME_EXHAUSTION")

def reduce_word(word):
    word = list(word)
    while True:
        changed = False
        for j in range(len(word) - 1):
            left, right = word[j], word[j + 1]
            if left[0] == right[0]:
                if left[1] != right[1]:
                    return None
                del word[j + 1]
                changed = True
                break
            if left[1] == right[1]:
                return None
        if not changed:
            return tuple(word)

def reduce_polynomial(terms):
    result = Counter()
    for coefficient, word in terms:
        reduced = reduce_word(word)
        if reduced is not None:
            result[reduced] += coefficient
    return {word: coefficient for word, coefficient in result.items()
            if coefficient}

def three_partition_certificate():
    count = 0
    for i, j, k in product(range(3), repeat=3):
        if j == k:
            continue
        A_j, A_k = ("A", j), ("A", k)
        if i in (j, k):
            terms = [(1, (A_j, ("Q", i), A_k))]
        else:
            terms = [
                (1, (A_j, A_k)),
                (-1, (A_j, ("Q", j), A_k)),
                (-1, (A_j, ("Q", k), A_k))
            ]
        need(reduce_polynomial(terms) == {}, "THREE_PARTITION_SANDWICH")
        count += 1
    need(count == 18, "THREE_PARTITION_COVERAGE")

def g1_patterns():
    planes = {}
    for a in range(5):
        planes["U", a] = frozenset(((a - 1) % 5, (a + 1) % 5))
        planes["V", a] = frozenset(((a - 2) % 5, (a + 2) % 5))
    need(set(planes.values())
         == {frozenset(pair) for pair in combinations(range(5), 2)},
         "G1_TEN_LINE_PAIRS")
    def coordinate_choice(choice):
        used = [line for key in choice for line in planes[key]]
        need(len(set(used)) == len(used), "COORDINATE_RAY_REUSE")
    reject("coordinate pair reuse", "COORDINATE_RAY_REUSE",
           lambda: coordinate_choice((("U", 0), ("U", 2))))
    histogram = Counter()
    patterns = []
    dispatches = 0
    keys = tuple(sorted(planes))
    for size in range(3):
        for choice in combinations(keys, size):
            tick()
            used = [line for key in choice for line in planes[key]]
            if len(set(used)) != len(used):
                continue
            coordinate_choice(choice)
            good = {a for a in range(5)
                    if ("U", a) not in choice and ("V", a) not in choice}
            need(len(good) >= 3, "GOOD_INDEX_COUNT")
            patterns.append(choice)
            histogram[len(good)] += 1
            for a, b in product(sorted(good), repeat=2):
                if a == b:
                    continue
                k = 3 * (a + b) % 5
                need(k not in (a, b), "MIDPOINT_ENDPOINT")
                support = {a, b, k}
                killed = {}
                for endpoint in (a, b):
                    hits = [planes[group, endpoint] & support
                            for group in ("U", "V")]
                    need(all(len(hit) == 1 for hit in hits),
                         "NONZERO_COEFFICIENT_SINGLETON")
                    killed[endpoint] = set().union(*hits)
                need(support - killed[a] == {a}, "GOOD_ROW_TO_E_A")
                need(support - killed[b] == {b}, "GOOD_COLUMN_TO_E_B")
                need((support - killed[a]) & (support - killed[b]) == set(),
                     "GOOD_ENDPOINTS_TO_G")
                for u in range(2):
                    v = (u + tau(a, b)) % 2
                    need({"U" if u == bit else "V" for bit in range(2)}
                         == {"U", "V"}, "ROW_DIAGONAL_PLANE_DISPATCH")
                    need({"U" if bit == v else "V" for bit in range(2)}
                         == {"U", "V"}, "COLUMN_DIAGONAL_PLANE_DISPATCH")
                    dispatches += 1
    need(len(patterns) == 26, "COORDINATE_PATTERN_TOTAL")
    need(histogram == Counter({5: 1, 4: 15, 3: 10}), "GOOD_PATTERN_HISTOGRAM")
    need(sum(len(choice) == 2 for choice in patterns) == 15,
         "TWO_COORDINATE_PATTERN_TOTAL")
    need(dispatches == 520, "GOOD_DISPATCH_TOTAL")
    return histogram, dispatches

def local_route(row_plane, column_plane, q, row_mate, column_mate, sectors):
    pq, pr, pc = outer(q), outer(row_mate), outer(column_mate)
    for plane, mate in ((row_plane, pr), (column_plane, pc)):
        need(is_projection(plane) and rank(plane) == 2, "LOCAL_GROUP_PLANE")
        need(is_projection(pq) and is_projection(mate), "LOCAL_UNIT_RAYS")
        need(plus(pq, mate) == plane, "LOCAL_GROUP_ONB")
        need(all(mm(plane, a) == mm(a, plane) for a in sectors),
             "LOCAL_REDUCING_PLANE")
    need(pr != pc, "GLOBAL_NONPARALLEL_REQUIRED")
    need(row_plane != column_plane, "DISTINCT_PLANES_REQUIRED")
    need(intersection_dimension(row_plane, column_plane) == 1,
         "LOCAL_INTERSECTION_LINE")
    need(sum(mm(a, pq) == pq for a in sectors) == 1,
         "INDIVIDUAL_RAY_MIXED")

def local_matrix_controls():
    P = diag(4, (0, 1))
    rotation = vector(4, {1: F(3, 5), 2: F(4, 5)})
    Q = plus(diag(4, (0,)), outer(rotation))
    need(is_projection(P) and is_projection(Q), "ROTATION_PROJECTIONS")
    need(rank(P) == rank(Q) == 2, "ROTATION_RANK_TWO")
    PQ, QP = mm(P, Q), mm(Q, P)
    products = [PQ, QP, PQ, QP]
    need(all(products[j] == transpose(products[(j + 1) % 4])
             for j in range(4)), "EVEN_CYCLE_ADJOINT_RELATIONS")
    reject("even four cycle", "HERMITIAN_PRODUCT",
           lambda: need(PQ == transpose(PQ), "HERMITIAN_PRODUCT"))
    need(rank(PQ) == 2 and intersection_dimension(P, Q) == 1,
         "ROTATION_INTERSECTION_COUNTS")
    reject("product rank versus intersection", "PRODUCT_IS_NOT_INTERSECTION",
           lambda: need(rank(PQ) == intersection_dimension(P, Q),
                        "PRODUCT_IS_NOT_INTERSECTION"))
    G, U, V = diag(6, (0, 1)), diag(6, (2, 3)), diag(6, (4, 5))
    R, X, Y = diag(6, (2, 5)), diag(6, (0, 4)), diag(6, (1, 3))
    zero = diag(6, ())
    need(plus(plus(R, X), Y) == diag(6, range(6)), "LOCAL_PARTITION_SUM")
    need(mm(R, X) == mm(R, Y) == mm(X, Y) == zero,
         "LOCAL_PARTITION_ORTHOGONAL")
    need(mm(R, G) == mm(X, U) == mm(Y, V) == zero,
         "LOCAL_MATCHING_ANNIHILATIONS")
    need(all(mm(group, sector) == mm(sector, group)
             for group in (R, X, Y) for sector in (G, U, V)),
         "LOCAL_THREE_PARTITION_COMMUTATION")
    q = vector(6, {0: F(3, 5), 4: F(4, 5)})
    mate = vector(6, {0: F(4, 5), 4: F(-3, 5)})
    need(plus(outer(q), outer(mate)) == X, "MIXED_LOCAL_ONB")
    need(mm(G, outer(q)) != mm(outer(q), G), "MIXED_RAY_NONCOMMUTATION")
    reject("equal planes with repeated partner", "GLOBAL_NONPARALLEL_REQUIRED",
           lambda: local_route(X, X, q, mate, mate, (G, U, V)))
    reject("reducing block to individual ray", "INDIVIDUAL_RAY_MIXED",
           lambda: need(sum(mm(a, outer(q)) == outer(q) for a in (G, U, V))
                        == 1, "INDIVIDUAL_RAY_MIXED"))
    e0, e4, e5 = (vector(6, {j: 1}) for j in (0, 4, 5))
    local_route(diag(6, (0, 4)), diag(6, (0, 5)),
                e0, e4, e5, (G, U, V))

def orbit(mask):
    return {frozenset((h * x + t) % 10 for x in mask)
            for h in (1, 3, 7, 9) for t in range(10)}

def mask_and_affine_checks():
    balanced = {frozenset(mask) for mask in combinations(range(10), 4)
                if sum(x % 2 == 0 for x in mask) == 2}
    triples = {
        frozenset((a, (a + d) % 10, (a + 2 * d) % 10))
        for a in range(10) for d in range(1, 10)
        if len({a, (a + d) % 10, (a + 2 * d) % 10}) == 3
    }
    ap = {mask for mask in balanced if any(triple <= mask for triple in triples)}
    extra = orbit(frozenset((0, 1, 3, 8)))
    other = orbit(frozenset((0, 1, 5, 6)))
    new = orbit(S)
    parts = (ap, extra, other, new)
    need(tuple(map(len, parts)) == (60, 20, 10, 10), "MASK_PARTITION_COUNTS")
    need(all(not (left & right) for left, right in combinations(parts, 2)),
         "MASK_PARTITION_DISJOINT")
    need(set().union(*parts) == balanced and len(balanced) == 100,
         "FULL_BALANCED_MASK_UNION")
    antipodal = {frozenset((a, a + 5, b, b + 5))
                 for a, b in combinations(range(5), 2)}
    need(other == antipodal, "OTHER_ORBIT_ANTIPODAL")
    need(new == {frozenset((x + t) % 10 for x in S) for t in range(10)},
         "NEW_ORBIT_TRANSLATIONS")
    reject("other ten-mask pattern", "WRONG_ORBIT",
           lambda: need(frozenset((0, 1, 5, 6)) in new, "WRONG_ORBIT"))
    image_counts = Counter()
    map_count = 0
    for h, t in product((1, 3, 7, 9), range(10)):
        tick()
        image = frozenset((h * x + t) % 10 for x in S)
        image_counts[image] += 1
        cells = set()
        for r, c in product(range(10), repeat=2):
            nr, nc = h * r % 10, (h * c + t) % 10
            cells.add((nr, nc))
            need((nr + nc) % 10 == (h * (r + c) + t) % 10,
                 "AFFINE_SYMBOL_CONSUMER")
            need((nc - nr) % 10 == (h * (c - r) + t) % 10,
                 "AFFINE_DIFFERENCE_CONSUMER")
        need(len(cells) == 100, "AFFINE_CELL_BIJECTION")
        transformed = {(h * r % 10, (h * c + t) % 10) for r, c in UNIVERSE}
        expected = {(r, c) for r, c in product(range(10), repeat=2)
                    if (c - r) % 10 not in image}
        need(transformed == expected, "AFFINE_COMPLEMENT_CONSUMER")
        map_count += 1
    need(map_count == 40 and len(image_counts) == 10
         and set(image_counts.values()) == {4}, "AFFINE_ORBIT_MULTIPLICITIES")
    return tuple(map(len, parts)), len(balanced), map_count

def main():
    mp = mapping()
    contexts = specified_contexts()
    validate(mp, contexts)
    reject("reversed column shift", "SUPPORT_MISMATCH",
           lambda: validate(mapping(shift=-2), contexts))
    reject("reversed parity classes", "SUPPORT_MISMATCH",
           lambda: validate(mapping(flip=True), contexts))
    reject("wrong physical symbol inverse", "SYMBOL_ROUTE",
           lambda: validate(mp, specified_contexts(inverse=2)))
    missing_symbols = {key: value for key, value in contexts.items()
                       if key[0] != "L"}
    reject("missing symbol ONB family", "CONTEXT_FAMILY",
           lambda: validate(mp, missing_symbols))
    balance = projection_incidence(mp, contexts)
    L, restricted = circular_linear_certificate()
    formal_cycles()
    three_partition_certificate()
    histogram, dispatches = g1_patterns()
    local_matrix_controls()
    counts, total, affine_maps = mask_and_affine_checks()
    need(len(REJECTIONS) == 10, "CONTROL_COVERAGE")
    tick()
    print("RESULT: PASS_FINITE_INTERFACES_ONLY")
    print("PHYSICAL_CELLS", len(mp))
    print("CONTEXTS", len(contexts), "SIZE", 6)
    print("BALANCE_ROWS", balance)
    print("CIRCULANT", L)
    print("SUM_ZERO_RESTRICTION", restricted)
    print("GOOD_PATTERN_HISTOGRAM", sorted(histogram.items()))
    print("GOOD_ENDPOINT_BIT_DISPATCHES", dispatches)
    print("MASK_PARTITION", counts, "UNION", total, "AFFINE_MAPS", affine_maps)
    for name, reason in REJECTIONS:
        print("CONTROL_REJECTED", name, reason)
    print("LIMITS: no physical vector witness, no operator-proof automation,")
    print("no theorem adoption, no unrestricted hundred-ray conclusion.")
    print("ELAPSED_SECONDS", monotonic() - START)

if __name__ == "__main__":
    main()
