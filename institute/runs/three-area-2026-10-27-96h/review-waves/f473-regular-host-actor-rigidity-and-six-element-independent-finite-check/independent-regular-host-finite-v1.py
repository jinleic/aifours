from itertools import product
from time import monotonic

DEADLINE = monotonic() + 55.0
REJECTIONS = []


class AuditFault(RuntimeError):
    def __init__(self, label, detail):
        self.label = label
        super().__init__(label + ": " + detail)


def need(condition, label, detail):
    if not condition:
        raise AuditFault(label, detail)


def guard():
    need(monotonic() < DEADLINE, "DEADLINE", "55-second bound reached")


def reject(label, operation):
    guard()
    try:
        operation()
    except AuditFault as exc:
        if exc.label != label:
            raise
        REJECTIONS.append(label)
        return
    raise AuditFault("MUTANT_ACCEPTED", label)


def band(c, d):
    return d if c == 0 else c


def action(g, c, swapping):
    if swapping and g % 2 and c:
        return 3 - c
    return c


def check_band():
    for c, d, e in product(range(3), repeat=3):
        need(band(band(c, d), e) == band(c, band(d, e)),
             "BAND_ASSOCIATIVITY", str((c, d, e)))
    for c in range(3):
        need(band(c, c) == c, "BAND_IDEMPOTENCE", str(c))
    for g, h, c in product(range(2), range(2), range(3)):
        need(action(g, action(h, c, True), True)
             == action((g + h) % 2, c, True),
             "BAND_ACTION_LAW", str((g, h, c)))
    for g, c, d in product(range(2), range(3), range(3)):
        need(action(g, band(c, d), True)
             == band(action(g, c, True), action(g, d, True)),
             "BAND_AUTOMORPHISM", str((g, c, d)))


def make_model(label, states, modulus, swapping):
    states = tuple(states)
    need(not swapping or modulus == 2, "ACTION_DOMAIN", label)
    index = {state: i for i, state in enumerate(states)}
    need(len(index) == len(states), "DUPLICATE_STATE", label)
    rows = []
    for c, g in states:
        row = []
        for d, h in states:
            target = (band(c, action(g, d, swapping)),
                      (g + h) % modulus)
            need(target in index, "SOURCE_CLOSURE", str(target))
            row.append(index[target])
        rows.append(tuple(row))
    return {"label": label, "states": states, "m": modulus,
            "swapping": swapping, "T": tuple(rows)}


def classes(keys):
    return tuple(sorted(set(
        tuple(j for j in range(len(keys)) if keys[j] == keys[i])
        for i in range(len(keys))
    )))


def least_group_congruence(T, E):
    n = len(T)
    parent = list(range(n))

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def join(x, y):
        x, y = root(x), root(y)
        if x == y:
            return False
        parent[y] = x
        return True

    first = min(E)
    for e in E:
        join(first, e)
    changed = True
    while changed:
        guard()
        changed = False
        for i, j in product(range(n), repeat=2):
            if root(i) == root(j):
                for z in range(n):
                    changed |= join(T[i][z], T[j][z])
                    changed |= join(T[z][i], T[z][j])
    return tuple(root(i) for i in range(n))


def check_hom(T, values, modulus, label):
    for i, j in product(range(len(T)), repeat=2):
        need(values[T[i][j]] == (values[i] + values[j]) % modulus,
             label, str((i, j)))


def check_product(T, images, multiply, label):
    for i, j in product(range(len(T)), repeat=2):
        need(images[T[i][j]] == multiply(images[i], images[j]),
             label, str((i, j)))


def audit_model(M):
    guard()
    T, n, m = M["T"], len(M["T"]), M["m"]
    q = tuple(g for c, g in M["states"])
    need(all(len(row) == n for row in T), "TABLE_SHAPE", M["label"])
    need(all(0 <= x < n for row in T for x in row),
         "TABLE_RANGE", M["label"])
    triples = 0
    for i, j, k in product(range(n), repeat=3):
        guard()
        need(T[T[i][j]][k] == T[i][T[j][k]],
             "SOURCE_ASSOCIATIVITY", str((i, j, k)))
        triples += 1
    need(all(T[0][s] == s and T[s][0] == s for s in range(n)),
         "SOURCE_IDENTITY", M["label"])
    E = frozenset(s for s in range(n) if T[s][s] == s)
    need(all(T[e][f] in E for e, f in product(E, repeat=2)),
         "IDEMPOTENT_BAND_CLOSURE", M["label"])
    unit_inverse = {}
    for s in range(n):
        candidates = [r for r in range(n)
                      if T[s][r] == 0 and T[r][s] == 0]
        need(len(candidates) <= 1, "UNIT_INVERSE_UNIQUENESS", str(s))
        if candidates:
            unit_inverse[s] = candidates[0]
    V = tuple(tuple(r for r in range(n)
                    if T[T[s][r]][s] == s and T[T[r][s]][r] == r)
              for s in range(n))
    need(all(V), "SOURCE_REGULARITY", M["label"])
    check_hom(T, q, m, "PRESCRIBED_QUOTIENT_HOM")
    need(set(q) == set(range(m)), "PRESCRIBED_QUOTIENT_ONTO", M["label"])
    need({s for s in range(n) if q[s] == 0} == set(E),
         "PRESCRIBED_QUOTIENT_PURITY", M["label"])
    R = tuple(frozenset({s} | {T[s][z] for z in range(n)})
              for s in range(n))
    L = tuple(frozenset({s} | {T[z][s] for z in range(n)})
              for s in range(n))
    need(len(set(zip(q, R, L))) == n,
         "GREEN_SEPARATION", M["label"])
    sigma = least_group_congruence(T, E)
    need(all((sigma[i] == sigma[j]) == (q[i] == q[j])
             for i, j in product(range(n), repeat=2)),
         "LEAST_GROUP_KERNEL", M["label"])
    unit_regular = tuple(
        any(T[T[s][u]][s] == s for u in unit_inverse)
        for s in range(n)
    )
    return {"E": E, "ui": unit_inverse, "V": V, "q": q,
            "R": R, "L": L, "sigma": sigma,
            "unit_regular": unit_regular, "triples": triples}


def unit_realization(M, A):
    T, m, q, E = M["T"], M["m"], A["q"], A["E"]
    ug = {q[u]: u for u in A["ui"]}
    need(len(ug) == len(A["ui"]), "UNIT_QUOTIENT_INJECTIVE", M["label"])
    need(set(ug) == set(range(m)), "UNIT_QUOTIENT_ONTO", M["label"])

    def alpha(g, e):
        return T[T[ug[g]][e]][A["ui"][ug[g]]]

    def multiply(left, right):
        e, g = left
        f, h = right
        return (T[e][alpha(g, f)], (g + h) % m)

    F = tuple((T[s][A["ui"][ug[q[s]]]], q[s]) for s in range(len(T)))
    need(all(e in E for e, g in F), "UNIT_F_IDEMPOTENT", M["label"])
    need(len(set(F)) == len(T), "UNIT_F_INJECTIVE", M["label"])
    need(set(F) == set(product(E, range(m))),
         "UNIT_F_SURJECTIVE", M["label"])
    for g in range(m):
        need({alpha(g, e) for e in E} == set(E),
             "CONJUGATION_PERMUTATION", str(g))
        for e, f in product(E, repeat=2):
            need(alpha(g, T[e][f]) == T[alpha(g, e)][alpha(g, f)],
                 "CONJUGATION_MULTIPLICATION", str((g, e, f)))
    for g, h, e in product(range(m), range(m), E):
        need(alpha(g, alpha(h, e)) == alpha((g + h) % m, e),
             "CONJUGATION_ACTION", str((g, h, e)))
    check_product(T, F, multiply, "UNIT_F_PHYSICAL_PRODUCT")
    for e, g in product(E, range(m)):
        need(F[T[e][ug[g]]] == (e, g), "UNIT_F_EXPLICIT_INVERSE", str((e, g)))
    return {"F": F, "ug": ug, "alpha": alpha, "multiply": multiply}


def enumerate_group_maps(M, A, modulus):
    T, n, E = M["T"], len(M["T"]), A["E"]
    total = homs = onto_count = pure_count = both_count = 0
    for values in product(range(modulus), repeat=n):
        guard()
        total += 1
        if any(values[T[i][j]] != (values[i] + values[j]) % modulus
               for i, j in product(range(n), repeat=2)):
            continue
        homs += 1
        image = set(values)
        need(0 in image and all((-g) % modulus in image for g in image),
             "ACTOR_IMAGE_INVERSES", str(values))
        need(all((g + h) % modulus in image for g, h in product(image, repeat=2)),
             "ACTOR_IMAGE_CLOSURE", str(values))
        for i, j in product(range(n), repeat=2):
            if values[i] == values[j]:
                for z in range(n):
                    need(values[T[i][z]] == values[T[j][z]]
                         and values[T[z][i]] == values[T[z][j]],
                         "KERNEL_CONGRUENCE", str((i, j, z)))
        onto = image == set(range(modulus))
        pure = {s for s in range(n) if values[s] == 0} == set(E)
        onto_count += int(onto)
        pure_count += int(pure)
        both_count += int(onto and pure)
        if pure:
            need(all((values[i] == values[j])
                     == (A["sigma"][i] == A["sigma"][j])
                     for i, j in product(range(n), repeat=2)),
                 "PURE_MAP_KERNEL_RIGIDITY", str(values))
            need(len(set(zip(values, A["R"], A["L"]))) == n,
                 "PURE_MAP_GREEN_SEPARATION", str(values))
    return total, homs, onto_count, pure_count, both_count


def evaluate(M, word):
    value = 0
    for g, s in word:
        value = band(value, action(g, M["states"][s][0], M["swapping"]))
    return value


def presentation_checks(M, A):
    T, n, m = M["T"], len(M["T"]), M["m"]
    alphabet = tuple(product(range(m), range(n)))
    contexts = ((),) + tuple((letter,) for letter in alphabet)
    words = square_checks = cocycle_checks = equivariance_checks = 0
    for length in (1, 2, 3):
        for word in product(alphabet, repeat=length):
            guard()
            words += 1
            value = evaluate(M, word)
            for h in range(m):
                translated = tuple(((h + g) % m, s) for g, s in word)
                need(evaluate(M, translated)
                     == action(h, value, M["swapping"]),
                     "PRESENTATION_EQUIVARIANCE", str((h, word)))
                equivariance_checks += 1
            for left, right in product(contexts, repeat=2):
                need(evaluate(M, left + word + word + right)
                     == evaluate(M, left + word + right),
                     "PRESENTATION_WORD_SQUARE", str(word))
                square_checks += 1
    for g, s, t in product(range(m), range(n), range(n)):
        guard()
        lhs = ((g, T[s][t]),)
        rhs = ((g, s), ((g + A["q"][s]) % m, t))
        for left, right in product(contexts, repeat=2):
            need(evaluate(M, left + lhs + right)
                 == evaluate(M, left + rhs + right),
                 "PRESENTATION_COCYCLE", str((g, s, t)))
            cocycle_checks += 1
    size = len(alphabet)
    expected_words = sum(size ** length for length in (1, 2, 3))
    need((words, square_checks, cocycle_checks, equivariance_checks)
         == (expected_words, expected_words * (size + 1) ** 2,
             m * n * n * (size + 1) ** 2, m * expected_words),
         "PRESENTATION_COVERAGE", M["label"])
    return words, square_checks, cocycle_checks, equivariance_checks


def actor_transport(N, A):
    T = N["T"]
    J = tuple((c, 2 * g) for c, g in N["states"])
    F = N["states"]

    def product4(left, right):
        return band(left[0], right[0]), (left[1] + right[1]) % 4

    def product2(left, right):
        return band(left[0], right[0]), (left[1] + right[1]) % 2

    need(len(set(J)) == len(T), "C4_SOURCE_INJECTION", "N")
    check_product(T, J, product4, "C4_SOURCE_EMBEDDING")
    check_product(T, F, product2, "IMAGE_ONLY_TRANSPORT")
    r = tuple(h for c, h in J)
    check_hom(T, r, 4, "C4_SOURCE_ACTOR_HOM")
    need(set(r) == {0, 2}, "ACTOR_IMAGE_PROPER_SUBGROUP", "N")
    need({s for s, h in enumerate(r) if h == 0} == set(A["E"]),
         "ACTOR_IMAGE_PURITY", "N")
    for g, h in product(range(2), repeat=2):
        need(2 * ((g + h) % 2) == (2 * g + 2 * h) % 4,
             "THETA_GROUP_ISOMORPHISM", str((g, h)))
    functions = homs = extensions = 0
    for f in product(range(2), repeat=4):
        functions += 1
        if all(f[(a + b) % 4] == (f[a] + f[b]) % 2
               for a, b in product(range(4), repeat=2)):
            homs += 1
            extensions += int(f[0] == 0 and f[2] == 1)
    need((functions, homs, extensions) == (16, 2, 0),
         "WHOLE_ACTOR_NONEXTENSION", str((functions, homs, extensions)))
    return functions, homs, extensions


def rees_checks(M, A, U, p):
    T, m = M["T"], M["m"]
    actor_identity = (-p) % m
    for h in range(m):
        need((actor_identity + p + h) % m == h
             and (h + p + actor_identity) % m == h,
             "REES_IDENTITY", str(h))
    for h, k, ell in product(range(m), repeat=3):
        need((((h + p + k) % m) + p + ell) % m
             == (h + p + ((k + p + ell) % m)) % m,
             "REES_ASSOCIATIVITY", str((h, k, ell)))
    for h, k in product(range(m), repeat=2):
        need((h + p + k + p) % m == ((h + p) + (k + p)) % m,
             "REES_RHO_HOM", str((h, k)))

    def multiply(left, right):
        e, h = left
        f, k = right
        return T[e][U["alpha"]((h + p) % m, f)], (h + p + k) % m

    FD = tuple((e, (g - p) % m) for e, g in U["F"])
    need(all(FD[s][1] == (A["q"][s] - p) % m for s in range(len(T))),
         "LITERAL_REES_ACTOR", M["label"])
    check_product(T, FD, multiply, "REES_PHYSICAL_SOURCE_PRODUCT")
    host = tuple(product(sorted(A["E"]), range(m)))
    for x in host:
        need((multiply(x, x) == x) == (x[1] == actor_identity),
             "REES_HOST_PROJECTION_PURITY", str(x))
    for x, y, z in product(host, repeat=3):
        guard()
        need(multiply(multiply(x, y), z) == multiply(x, multiply(y, z)),
             "REES_HOST_ASSOCIATIVITY", str((x, y, z)))
    return FD, multiply


def missing_cocycle_shift(M, A):
    T, n, m = M["T"], len(M["T"]), M["m"]
    for g, s, t in product(range(m), range(n), range(n)):
        lhs = ((g, T[s][t]),)
        rhs = ((g, s), (g, t))
        need(evaluate(M, lhs) == evaluate(M, rhs),
             "COCYCLE_SHIFT", str((g, s, t)))


def wrong_inverse_coordinates(M, A, U):
    T = M["T"]
    return tuple((T[s][U["ug"][A["q"][s]]], A["q"][s])
                 for s in range(len(T)))


def main():
    check_band()
    M = make_model("six", ((0, 0), (0, 1), (1, 0), (2, 0),
                           (1, 1), (2, 1)), 2, True)
    N = make_model("five", ((0, 0), (1, 0), (2, 0),
                            (1, 1), (2, 1)), 2, False)
    C3 = make_model("C3-control", tuple(product(range(3), range(3))),
                    3, False)
    AM, AN, A3 = audit_model(M), audit_model(N), audit_model(C3)
    need(M["T"] == ((0, 1, 2, 3, 4, 5), (1, 0, 5, 4, 3, 2),
                    (2, 4, 2, 2, 4, 4), (3, 5, 3, 3, 5, 5),
                    (4, 2, 4, 4, 2, 2), (5, 3, 5, 5, 3, 3)),
         "SIX_LITERAL_TABLE", "formula versus frozen table")
    need(N["T"] == ((0, 1, 2, 3, 4), (1, 1, 1, 3, 3),
                    (2, 2, 2, 4, 4), (3, 3, 3, 1, 1),
                    (4, 4, 4, 2, 2)),
         "FIVE_LITERAL_TABLE", "formula versus displayed table")
    need(AM["E"] == {0, 2, 3} and set(AM["ui"]) == {0, 1},
         "SIX_IDEMPOTENTS_UNITS", "exact sets")
    need(AN["E"] == {0, 1, 2} and set(AN["ui"]) == {0},
         "FIVE_IDEMPOTENTS_UNITS", "exact sets")
    need(AM["V"] == ((0,), (1,), (2, 3), (2, 3), (4, 5), (4, 5)),
         "SIX_ALL_INVERSES", str(AM["V"]))
    need(AN["V"] == ((0,), (1, 2), (1, 2), (3, 4), (3, 4)),
         "FIVE_ALL_INVERSES", str(AN["V"]))
    need(classes(AM["R"]) == ((0, 1), (2, 4), (3, 5))
         and classes(AM["L"]) == ((0, 1), (2, 3, 4, 5)),
         "SIX_GREEN_CLASSES", "exact classes")
    need(classes(AN["R"]) == ((0,), (1, 3), (2, 4))
         and classes(AN["L"]) == ((0,), (1, 2, 3, 4)),
         "FIVE_GREEN_CLASSES", "exact classes")
    need(classes(AM["sigma"]) == ((0, 2, 3), (1, 4, 5))
         and classes(AN["sigma"]) == ((0, 1, 2), (3, 4)),
         "EXACT_LEAST_GROUP_CONGRUENCES", "exact classes")
    need(all(AM["unit_regular"])
         and AN["unit_regular"] == (True, True, True, False, False),
         "UNIT_REGULAR_BOUNDARY", "six versus five")
    need(M["T"][2][3] != M["T"][3][2]
         and M["T"][1][2] != M["T"][2][1]
         and M["T"][M["T"][1][2]][1] == 3,
         "NONCOMMUTATION", "ab, ba, ta, at, tat")
    UM, U3 = unit_realization(M, AM), unit_realization(C3, A3)
    need(UM["alpha"](1, 2) == 3 and UM["alpha"](1, 3) == 2,
         "ACTUAL_NONTRIVIAL_CONJUGATION", "swap a and b")
    map_rows = []
    expected_counts = {1: (1, 1, 0, 0), 2: (2, 1, 1, 1),
                       3: (1, 0, 0, 0), 4: (2, 0, 1, 0)}
    for model, audit in ((M, AM), (N, AN)):
        for modulus in (1, 2, 3, 4):
            row = enumerate_group_maps(model, audit, modulus)
            need(row == (modulus ** len(model["T"]),)
                 + expected_counts[modulus],
                 "CYCLIC_MAP_EXHAUSTION", str((model["label"], modulus, row)))
            map_rows.append((model["label"], modulus, row))
    transport = actor_transport(N, AN)
    presentation_M = presentation_checks(M, AM)
    presentation_N = presentation_checks(N, AN)
    FD, rees_multiply = rees_checks(M, AM, UM, 1)
    T = M["T"]
    reject("TRIVIAL_ACTION", lambda: check_product(
        T, UM["F"], lambda l, r: (T[l[0]][r[0]], (l[1] + r[1]) % 2),
        "TRIVIAL_ACTION"))
    reject("BAND_ORDER", lambda: check_product(
        T, UM["F"],
        lambda l, r: (T[UM["alpha"](l[1], r[0])][l[0]],
                      (l[1] + r[1]) % 2), "BAND_ORDER"))
    bad2 = wrong_inverse_coordinates(M, AM, UM)
    need(bad2 == UM["F"], "C2_INVERSE_NONDISCRIMINATION", "expected equality")
    bad3 = wrong_inverse_coordinates(C3, A3, U3)
    reject("WRONG_UNIT_INVERSE_C3", lambda: need(
        all(e in A3["E"] for e, g in bad3),
        "WRONG_UNIT_INVERSE_C3", "first coordinate is not idempotent"))
    reject("GREEN_R_COLLAPSE", lambda: need(
        len(set(zip(AM["q"], AM["L"]))) == len(T),
        "GREEN_R_COLLAPSE", "q and L alone collide"))
    reject("GREEN_Q_COLLAPSE", lambda: need(
        len(set(zip(AM["R"], AM["L"]))) == len(T),
        "GREEN_Q_COLLAPSE", "R and L alone collide"))
    trivial = (0,) * len(T)
    check_hom(T, trivial, 1, "TRIVIAL_QUOTIENT_HOM")
    need(set(trivial) == {0}, "TRIVIAL_QUOTIENT_ONTO", "C1")
    reject("QUOTIENT_PURITY", lambda: need(
        {s for s, g in enumerate(trivial) if g == 0} == set(AM["E"]),
        "QUOTIENT_PURITY", "onto trivial quotient is not pure"))
    reject("UNITS_NECESSARY", lambda: need(
        {AN["q"][u] for u in AN["ui"]} == {0, 1},
        "UNITS_NECESSARY", "proper embedding already verified"))
    reject("REES_TWIST_P", lambda: check_product(
        T, FD,
        lambda l, r: (T[l[0]][UM["alpha"](l[1], r[0])],
                      (l[1] + 1 + r[1]) % 2), "REES_TWIST_P"))
    reject("REES_ACTOR_P", lambda: check_product(
        T, FD,
        lambda l, r: (T[l[0]][UM["alpha"]((l[1] + 1) % 2, r[0])],
                      (l[1] + r[1]) % 2), "REES_ACTOR_P"))
    reject("COCYCLE_SHIFT", lambda: missing_cocycle_shift(M, AM))
    need(len(REJECTIONS) == 10 and len(set(REJECTIONS)) == 10,
         "CONTROL_COVERAGE", str(REJECTIONS))
    guard()
    print("COMPLETE: finite instance audit; no general presentation claim")
    print("source triples:", AM["triples"], AN["triples"], A3["triples"])
    print("six inverse sets:", AM["V"])
    print("five inverse sets:", AN["V"])
    for row in map_rows:
        print("group maps:", row)
    print("C4 functions, homomorphisms, extensions:", transport)
    print("presentation six:", presentation_M)
    print("presentation five:", presentation_N)
    print("reason-specific rejections:", tuple(REJECTIONS))
    print("nondiscriminating: inverse orientation on C2")
    print("not tested: noncentral sandwich-order discrimination")
    print("not claimed: all-regular host existence or universal injectivity")


if __name__ == "__main__":
    main()
