#!/usr/bin/env python3
"""Unrun, finite 4555 interface author-candidate; standard library only.

The full same-P/same-E interface checker is included, but no positive complete
4555 P/E fixture is claimed. All exhaustive classifications below are projected
necessary conditions or explicitly local fixtures, not a global tensor proof.
"""
from collections import Counter
from itertools import combinations, permutations, product
from time import monotonic


class CheckFailure(Exception):
    pass


# Cooperative bound; timeout means INCOMPLETE, never a scientific PASS.
DEADLINE = monotonic() + 50.0


def guard():
    if monotonic() >= DEADLINE:
        raise CheckFailure("DEADLINE_INCOMPLETE")


def need(condition, message):
    if not condition:
        raise CheckFailure(message)


def expect_failure(label, function, *args):
    try:
        function(*args)
    except CheckFailure as exc:
        need(str(exc) == label, "wrong failure: expected " + label + ", got " + str(exc))
        return
    raise CheckFailure("mutation was not rejected: " + label)


PAIRS = tuple(combinations(range(4), 2))
CUTS = ((0, 1), (0, 2), (0, 3))


def projection(words, ij):
    i, j = ij
    return Counter((w[i], w[j]) for w in words)


def pair_label(ij):
    return str(ij[0]) + str(ij[1])


def validate_words(words):
    need(len(words) == len(set(words)), "DUPLICATE_WORD")
    need(all(len(w) == 4 and all(isinstance(x, int) and 0 <= x < 6 for x in w)
             for w in words), "BAD_WORD")


def pair_capacity(words, capacity):
    validate_words(words)
    for ij in PAIRS:
        if any(c > capacity for c in projection(words, ij).values()):
            raise CheckFailure("PAIR_CAPACITY_" + pair_label(ij))


def local_interface(P, E, expected_E_pairs=None):
    """Check all six projections of the SAME supplied local word sets.

    Expected E pairs, when provided, are checked before multiplicity, so an
    omitted pair is diagnosed as such even if other pair degrees also change.
    """
    validate_words(P)
    validate_words(E)
    if expected_E_pairs is not None:
        for ij in PAIRS:
            if set(projection(E, ij)) != expected_E_pairs[ij]:
                raise CheckFailure("MISSING_OR_EXTRA_E_PAIR_" + pair_label(ij))
    for ij in PAIRS:
        p, e = projection(P, ij), projection(E, ij)
        if any(v != 1 for v in p.values()):
            raise CheckFailure("P_DUPLICATE_" + pair_label(ij))
        if any(v != 2 for v in e.values()):
            raise CheckFailure("E_MULTIPLICITY_" + pair_label(ij))
        if set(p) & set(e):
            raise CheckFailure("P_E_COLLISION_" + pair_label(ij))


def blocks(E):
    """List actual 2x2 support blocks in each of the three physical cuts."""
    result = []
    for row_coords in CUTS:
        guard()
        col_coords = tuple(i for i in range(4) if i not in row_coords)
        rows, cols, entry = {}, {}, {}
        for w in E:
            r = tuple(w[i] for i in row_coords)
            c = tuple(w[i] for i in col_coords)
            rows.setdefault(r, set()).add(c)
            cols.setdefault(c, set()).add(r)
            need((r, c) not in entry, "CUT_DUPLICATE")
            entry[r, c] = w
        need(all(len(x) == 2 for x in rows.values()), "CUT_ROW_DEGREE")
        need(all(len(x) == 2 for x in cols.values()), "CUT_COLUMN_DEGREE")
        seen = set()
        these = []
        for r in sorted(rows):
            cc = tuple(sorted(rows[r]))
            rr = tuple(sorted(cols[cc[0]]))
            need(len(rr) == 2 and r in rr and all(rows[x] == set(cc) for x in rr),
                 "CUT_NOT_FULL_2X2")
            key = (rr, cc)
            if key not in seen:
                seen.add(key)
                these.append(tuple(tuple(entry[rr[i], cc[j]] for j in range(2))
                                   for i in range(2)))
        result.append(these)
    return result


def full_projected_interface(P, E):
    """Actual-size support interface only: NOT a tensor/unitarity verifier."""
    need(len(P) == 24 and len(E) == 24, "FULL_WORD_COUNTS")
    local_interface(P, E)
    universe = set(product(range(6), repeat=2))
    for ij in PAIRS:
        p, e = projection(P, ij), projection(E, ij)
        need(len(p) == 24 and len(e) == 12 and set(p) | set(e) == universe,
             "FULL_COVERAGE_" + pair_label(ij))
    b = blocks(E)
    need(all(len(x) == 6 for x in b), "FULL_BLOCK_COUNT")


def profiles_and_moments():
    aa = [x for x in product(range(2, 6), repeat=4) if sum(x) == 12]
    bb = [x for x in product(range(2, 5), repeat=5) if sum(x) == 12]
    A = {tuple(sorted(x, reverse=True)) for x in aa}
    B = {tuple(sorted(x, reverse=True)) for x in bb}
    need(A == {(3, 3, 3, 3), (4, 3, 3, 2), (4, 4, 2, 2), (5, 3, 2, 2)},
         "A_PROFILES")
    need(B == {(3, 3, 2, 2, 2), (4, 2, 2, 2, 2)}, "FIVE_PROFILES")
    need(len(aa) == 31 and len(bb) == 15, "LABELLED_PROFILE_COUNT")
    count = 0
    for a, b, c, d in product(aa, bb, bb, bb):
        if count % 1024 == 0:
            guard()
        need(sum(a) == sum(b) == sum(c) == sum(d) == 12, "PROFILE_SUM")
        count += 1
    need(count == 104625 and len(A) * len(B) ** 3 == 32, "ALL_PROFILE_PRODUCTS")

    raw = set()
    for n0 in range(25):
        guard()
        for n1 in range(25 - n0):
            for n2 in range(25 - n0 - n1):
                for n3 in range(25 - n0 - n1 - n2):
                    n4 = 24 - n0 - n1 - n2 - n3
                    n = (n0, n1, n2, n3, n4)
                    if sum(k * n[k] for k in range(5)) == 66 and sum(
                            k * (k - 1) // 2 * n[k] for k in range(5)) == 63:
                        raw.add(n)
    need(len(raw) == 5, "RAW_MOMENT_HISTOGRAMS")
    return A, B, raw


def footprint_classification(raw):
    """Enumerate all disjoint covers of the nine letter-valued outside pairs."""
    letters = ((0, 0), (0, 1), (1, 0), (2, 0), (3, 0))
    universe = {tuple(sorted((x, y))) for x, y in combinations(letters, 2)
                if x[0] != y[0]}
    need(len(universe) == 9, "OUTSIDE_CELLS")
    footprints = []
    for size in (2, 3, 4):
        for coords in combinations(range(4), size):
            for aletter in ((0, 1) if 0 in coords else (0,)):
                f = frozenset((i, aletter if i == 0 else 0) for i in coords)
                cells = frozenset(tuple(sorted(x)) for x in combinations(sorted(f), 2))
                footprints.append((f, cells))

    covers = []
    def visit(remaining, chosen):
        guard()
        if not remaining:
            covers.append(tuple(chosen))
            return
        first = min(remaining)
        for f, cells in footprints:
            if first in cells and cells <= remaining:
                visit(remaining - cells, chosen + [f])
    visit(universe, [])
    need(len(covers) == 16, "FOOTPRINT_COVER_COUNT")
    histograms, classes = set(), Counter()
    for cover in covers:
        quad = [f for f in cover if len(f) == 4]
        triple = [f for f in cover if len(f) == 3]
        two = [f for f in cover if len(f) == 2]
        singleton = {x: 6 - sum(x in f for f in cover) for x in letters}
        need(all(v >= 0 for v in singleton.values()), "NEGATIVE_SINGLETON")
        n3 = sum(singleton.values())
        n4 = 24 - len(cover) - n3
        n = (len(quad), len(triple), len(two), n3, n4)
        need(n4 >= 0 and n in raw, "FOOTPRINT_MOMENTS")
        histograms.add(n)
        classes[len(quad), len(triple)] += 1
        if quad:
            need(len(quad) == 1 and not triple and len(two) == 3, "QUAD_CLASS")
            used_a = next(x for x in quad[0] if x[0] == 0)
            other_a = (0, 1 - used_a[1])
            need(set(two) == {frozenset((other_a, (j, 0))) for j in (1, 2, 3)},
                 "QUAD_A_LETTER")
        elif len(triple) == 2:
            need(all(any(x[0] == 0 for x in f) for f in triple), "TWO_TRIPLES_A")
            a0 = next(x for x in triple[0] if x[0] == 0)
            a1 = next(x for x in triple[1] if x[0] == 0)
            s0 = {x[0] for x in triple[0] if x[0] != 0}
            s1 = {x[0] for x in triple[1] if x[0] != 0}
            need(a0 != a1 and len(s0 & s1) == 1 and len(two) == 3,
                 "TWO_TRIPLES_LETTERS")
        elif len(triple) == 1:
            coords = {x[0] for x in triple[0]}
            need((coords == {1, 2, 3} or (0 in coords and len(coords) == 3))
                 and len(two) == 6, "ONE_TRIPLE_CLASS")
        else:
            need(not triple and len(two) == 9, "ONLY_TWO_OUTSIDE")
    expected = {(1, 0, 3, 20, 0), (0, 2, 3, 18, 1),
                (0, 1, 6, 15, 2), (0, 0, 9, 12, 3)}
    need(histograms == expected, "COMPLETE_ACTUAL_HISTOGRAMS")
    need(classes == Counter({(1, 0): 2, (0, 2): 6, (0, 1): 7, (0, 0): 1}),
         "FOOTPRINT_CLASSES")


def perfect_matchings(vertices):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for k in range(1, len(vertices)):
        second = vertices[k]
        rest = vertices[1:k] + vertices[k + 1:]
        for m in perfect_matchings(rest):
            yield ((first, second),) + m


def twin_graph(n):
    """All three-coordinate equality matchings, first fixed by relabeling."""
    matchings = list(perfect_matchings(tuple(range(n))))
    fixed = tuple((i, i + 1) for i in range(0, n, 2))
    positive = negative = 0
    representative = None
    for m1 in matchings:
        guard()
        if set(fixed) & set(m1):
            continue
        for m2 in matchings:
            if set(fixed) & set(m2) or set(m1) & set(m2):
                continue
            ms = (fixed, m1, m2)
            adj = [set() for _ in range(n)]
            for m in ms:
                for x, y in m:
                    adj[x].add(y)
                    adj[y].add(x)
            need(all(len(neighbors) == 3 for neighbors in adj), "NOT_SIMPLE_CUBIC")
            color = [None] * n
            bipartite = True
            for root in range(n):
                if color[root] is not None:
                    continue
                color[root] = 0
                stack = [root]
                while stack:
                    x = stack.pop()
                    for y in adj[x]:
                        if color[y] is None:
                            color[y] = 1 - color[x]
                            stack.append(y)
                        elif color[y] == color[x]:
                            bipartite = False
            coord_values = []
            for m in ms:
                values = [None] * n
                for label, (x, y) in enumerate(m):
                    values[x] = values[y] = label
                coord_values.append(values)
            T = [tuple(coord_values[k][v] for k in range(3)) for v in range(n)]
            for ij in combinations(range(3), 2):
                need(len({(t[ij[0]], t[ij[1]]) for t in T}) == n,
                     "TWIN_PHYSICAL_PAIR_DUPLICATE")
            if not bipartite:
                negative += 1
                continue
            positive += 1
            need(color.count(0) == color.count(1) == n // 2, "TWIN_BIPARTITION")
            # z=x*conj(y)=(0,2)/4 is nonreal; opposite colors negate z.
            z = [(0, 2 if color[v] == 0 else -2) for v in range(n)]
            for v in range(n):
                for u in adj[v]:
                    need(z[v][0] + z[u][0] == z[v][1] + z[u][1] == 0,
                         "NONREAL_EDGE_ORTHOGONALITY")
            if representative is None:
                representative = (T, color)
    return positive, negative, representative


def multiply_conjugate(z, w):
    a, b = z
    c, d = w
    return (a * c + b * d, b * c - a * d)


def sum_complex(values):
    return (sum(x for x, _ in values), sum(y for _, y in values))


def check_unitary_blocks(E, amplitudes):
    need(set(amplitudes) == set(E), "AMPLITUDE_KEYS")
    for cut_blocks in blocks(E):
        for block in cut_blocks:
            M = [[amplitudes[block[i][j]] for j in range(2)] for i in range(2)]
            for row in M:
                need(sum(a * a + b * b for a, b in row) == 4, "ROW_NORM")
            for j in range(2):
                need(sum(M[i][j][0] ** 2 + M[i][j][1] ** 2 for i in range(2)) == 4,
                     "COLUMN_NORM")
            need(sum_complex(multiply_conjugate(M[0][j], M[1][j]) for j in range(2))
                 == (0, 0), "ROW_ORTHOGONALITY")
            need(sum_complex(multiply_conjugate(M[i][0], M[i][1]) for i in range(2))
                 == (0, 0), "COLUMN_ORTHOGONALITY")


def twin_components():
    for n in (2, 4):
        pos, _, _ = twin_graph(n)
        need(pos == 0, "SMALL_CUBIC_BIPARTITE_TWIN")
    for n in (6, 8):
        pos, neg, rep = twin_graph(n)
        need(pos > 0 and neg > 0 and rep is not None, "TWIN_ENUMERATION")
        T, color = rep
        E = [(a,) + tuple(t) for a in (0, 1) for t in T]
        amplitudes = {}
        for a in (0, 1):
            for t, c in zip(T, color):
                # Gaussian integer numerators /2; nonreal z=U0*conj(U1).
                amplitudes[(a,) + tuple(t)] = ((1, 1) if c == 0 else (-1, -1)) if a == 0 else (1, -1)
        check_unitary_blocks(E, amplitudes)
    need(multiply_conjugate((1, 1), (1, -1)) == (0, 2), "PHASE_CONJUGATION")
    # A 6-triple overlap saturates three values twice. A degree-four slice
    # has only one unused value per coordinate: two extra distinct words
    # cannot fit. A degree-five slice has two per coordinate and is separate.
    need(1 ** 3 < 2 and 2 ** 3 >= 4, "TWIN_SATURATION_BOX")


def parity_phase():
    E = [w for w in product((0, 1), repeat=4) if sum(w) % 2 == 0]
    need(len(E) == 8, "PARITY_SIZE")
    for ij in PAIRS:
        p = projection(E, ij)
        need(len(p) == 4 and all(v == 2 for v in p.values()), "PARITY_CLOSED_PAIR")
    cut_blocks = blocks(E)
    need(all(len(b) == 2 for b in cut_blocks), "PARITY_SIX_BLOCKS")
    index = {w: i for i, w in enumerate(E)}
    equations, wrong_conjugate = [], []
    for cut in cut_blocks:
        for block in cut:
            eq, wrong = [0] * 8, [0] * 8
            for i, j, sign in ((0, 0, 1), (0, 1, -1), (1, 0, -1), (1, 1, 1)):
                eq[index[block[i][j]]] += sign
                wrong[index[block[i][j]]] += 1
            equations.append(eq)
            wrong_conjugate.append(wrong)

    def odd_certificate(rows):
        for c in product((-1, 0, 1), repeat=len(rows)):
            guard()
            if sum(c) % 2 and all(sum(c[k] * rows[k][j] for k in range(len(rows))) == 0
                                   for j in range(8)):
                return c
        return None
    cert = odd_certificate(equations)
    need(cert is not None, "COMPLEX_PARITY_CERTIFICATE")
    need(odd_certificate(wrong_conjugate) is None, "WRONG_CONJUGATE_CERTIFICATE")
    # Units are pi/4. This assignment solves the deliberately WRONG all-plus
    # equations, but not the actual conjugate-phase equations.
    units = [1] * 8
    def solves(rows):
        return all(sum(a * b for a, b in zip(row, units)) % 8 == 4 for row in rows)
    need(solves(wrong_conjugate) and not solves(equations), "CONJUGATE_PHASE_MUTATION")


def binary_twin_restrictions():
    triples = list(product((0, 1), repeat=3))
    for w in triples:
        complement = tuple(1 - x for x in w)
        for z in triples:
            need(any(sum(x == y for x, y in zip(z, q)) >= 2 for q in (w, complement)),
                 "FULL_44_P_PAIR")
    # The maximal a word is all outside; enumerate all eight ways to label
    # the three b words. P is ONE set and checked on all six physical pairs.
    for b, c, d in product((0, 1), repeat=3):
        P = [(0, 2, 2, 2), (1, 2, c, d),
             (1, b, 2, 1 - d), (1, 1 - b, 1 - c, 2)]
        validate_words(P)
        need(all(max(projection(P, ij).values()) == 1 for ij in PAIRS), "PARTIAL_53_P")
        allowed = []
        for t in triples:
            w = (0,) + t
            if all((w[i], w[j]) not in projection(P, (i, j)) for i, j in PAIRS):
                allowed.append(t)
        need(len(allowed) == 2, "PARTIAL_53_TWO_OF_EIGHT")


def common_P_stars():
    """All six-word P configurations of one full degree-three A twin."""
    perms = list(permutations(range(3)))
    V = {3, 4, 5}
    M = {3, 4}
    total = 0
    for p, q, r, s in product(perms, repeat=4):
        guard()
        P = [(0, 3 + i, 3 + p[i], 3 + q[i]) for i in range(3)]
        P += [(1, 3 + i, 3 + r[i], 3 + s[i]) for i in range(3)]
        if any(any(v > 1 for v in projection(P, ij).values()) for ij in PAIRS):
            continue
        total += 1
        for ij in ((1, 2), (1, 3), (2, 3)):
            remaining = set(product(V, repeat=2)) - set(projection(P, ij))
            need(len(remaining) == 3 and all(sum(x == a for x, _ in remaining) == 1
                                              for a in V)
                 and all(sum(y == a for _, y in remaining) == 1 for a in V),
                 "COMMON_P_MATCHING")
            box = list(product(sorted(M), repeat=2))
            for mask in range(1 << len(box)):
                edges = {box[k] for k in range(len(box)) if mask & (1 << k)}
                if edges & set(projection(P, ij)):
                    continue
                need(all(sum(x == a for x, _ in edges) <= 1 for a in M)
                     and all(sum(y == a for _, y in edges) <= 1 for a in M),
                     "MATCHING_STAR")
    need(total == 72, "COMMON_P_CONFIGURATIONS")


def two_twin_residuals():
    """Enumerate actual two-full-A-twin E components after the matching star.

    In each component each coordinate has a high value 0 and lows 1,2.
    If the other twin's common-P matching permits at most one low-low
    neighbor, both lows must meet the high, exhausting its two slots. Thus
    high/high is absent. Each high occurs twice in the six triples, so with
    high/high absent every triple has exactly one high. The eight binary
    pairings below enumerate all such six-triple supports, not selected ones.
    """
    legal = []
    for eb, ec, ed in product((0, 1), repeat=3):
        guard()
        T = []
        for i in range(2):
            T.append((0, 1 + i, 1 + (i ^ eb)))
            T.append((1 + i, 0, 1 + (i ^ ec)))
            T.append((1 + i, 1 + (i ^ ed), 0))
        need(len(set(T)) == 6, "TWO_TWIN_SIX_TRIPLES")
        for ij in combinations(range(3), 2):
            need(len({(t[ij[0]], t[ij[1]]) for t in T}) == 6,
                 "TWO_TWIN_PAIR_INJECTIVITY")
            need(all((t[ij[0]], t[ij[1]]) != (0, 0) for t in T),
                 "TWO_TWIN_HIGH_HIGH_EDGE")
        adj = [set() for _ in T]
        for u, v in combinations(range(6), 2):
            if any(T[u][i] == T[v][i] for i in range(3)):
                adj[u].add(v)
                adj[v].add(u)
        need(all(len(neighbors) == 3 for neighbors in adj), "TWO_TWIN_CUBIC")
        color = [None] * 6
        color[0] = 0
        stack = [0]
        bipartite = True
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if color[v] is None:
                    color[v] = 1 - color[u]
                    stack.append(v)
                elif color[v] == color[u]:
                    bipartite = False
        need(all(c is not None for c in color), "TWO_TWIN_CONNECTED")
        if bipartite:
            legal.append((T, color))
    need(legal, "NO_LOCAL_TWO_TWIN_COMPONENT")
    checked = 0
    for first, second in product(legal, repeat=2):
        guard()
        (T1, c1), (T2, c2) = first, second
        T2 = [tuple(0 if x == 0 else x + 2 for x in t) for t in T2]
        E, U = [], {}
        for pair, T, colors in (((0, 1), T1, c1), ((2, 3), T2, c2)):
            for a in pair:
                for t, color in zip(T, colors):
                    w = (a,) + tuple(t)
                    E.append(w)
                    U[w] = (((1, 1) if color == 0 else (-1, -1))
                            if a == pair[0] else (1, -1))
        need(len(E) == 24, "TWO_TWIN_E_SIZE")
        local_interface([], E)
        need(all(len(cut) == 6 for cut in blocks(E)), "TWO_TWIN_E_BLOCKS")
        check_unitary_blocks(E, U)
        need(Counter(w[0] for w in E) == Counter({0: 6, 1: 6, 2: 6, 3: 6}),
             "TWO_TWIN_A_OCCURRENCES")
        for i in (1, 2, 3):
            need(Counter(w[i] for w in E) == Counter({0: 8, 1: 4, 2: 4, 3: 4, 4: 4}),
                 "TWO_TWIN_FIVE_OCCURRENCES")
        for ij in ((1, 2), (1, 3), (2, 3)):
            need((0, 0) not in projection(E, ij), "TWO_TWIN_SAME_E_HIGH_HIGH")
        checked += 1
    need(checked == len(legal) ** 2, "TWO_TWIN_COMPONENT_PAIRS")


def P_injective(P, cap=1):
    return all(all(n <= cap for n in projection(P, ij).values()) for ij in PAIRS)


def two_A_twins():
    """Complete high/high/outside P shadow with both A-outside letters."""
    types = [t for t in product((0, 1), repeat=3) if 0 in t]  # 0=high, 1=outside
    patterns = []
    for mask in range(1 << len(types)):
        guard()
        words = [types[k] for k in range(len(types)) if mask & (1 << k)]
        if all(sum(t[i] == 0 for t in words) == 2 for i in range(3)) and all(
                sum(t[i] == 0 and t[j] == 0 for t in words) == 1
                for i, j in combinations(range(3), 2)):
            patterns.append(words)
    need(len(patterns) == 2 and sorted(map(len, patterns)) == [3, 4], "HIGH_HIGH_PATTERNS")
    colorable = physically_injective = 0
    star_example = None
    for words in patterns:
        for colors in product((0, 1), repeat=len(words)):
            P = [(colors[k],) + words[k] for k in range(len(words))]
            if not all({colors[k] for k, t in enumerate(words) if t[i] == 0} == {0, 1}
                       for i in range(3)):
                continue
            colorable += 1
            if len(words) == 4 and star_example is None:
                star_example = P
            if P_injective(P):
                physically_injective += 1
    need(colorable == 2 and physically_injective == 0, "TWO_A_TWIN_COLORING")
    need(star_example is not None and not P_injective(star_example, 1)
         and P_injective(star_example, 2), "P_PAIR_CAPACITY_MUTATION")


def local_fixture():
    """A non-global physical local component plus six compatible P words."""
    T = [(s, s, s) for s in range(3)]
    T += [(t, (t - 1) % 3, (t - 2) % 3) for t in range(3)]
    E = [(a,) + t for a in (0, 1) for t in T]
    U = {}
    for a in (0, 1):
        for k, t in enumerate(T):
            U[(a,) + t] = ((1, 1) if k < 3 else (-1, -1)) if a == 0 else (1, -1)
    P = [(0, 3 + i, 3 + i, 3 + i) for i in range(3)]
    P += [(1, 3 + i, 3 + (i + 1) % 3, 3 + (i + 2) % 3) for i in range(3)]
    expected = {}
    for ij in PAIRS:
        if ij[0] == 0:
            expected[ij] = set(product((0, 1), range(3)))
        else:
            expected[ij] = {(t[ij[0] - 1], t[ij[1] - 1]) for t in T}
    local_interface(P, E, expected)
    check_unitary_blocks(E, U)
    expect_failure("FULL_WORD_COUNTS", full_projected_interface, P, E)
    # A missing actual E pair, not just a changed abstract matching.
    missing = [w for w in E if (w[1], w[2]) != (0, 0)]
    expect_failure("MISSING_OR_EXTRA_E_PAIR_12", local_interface, P, missing, expected)
    # Hypothetical pair-capacity-three mutant; invalid as an actual tensor.
    extra = E + [(0, 0, 0, 1)]
    expect_failure("PAIR_CAPACITY_01", pair_capacity, extra, 2)
    pair_capacity(extra, 3)
    # Forgetting the common P matching duplicates a physical BC pair.
    bad_P = P[:3] + [(1, 3 + i, 3 + i, 3 + (i + 2) % 3) for i in range(3)]
    expect_failure("P_DUPLICATE_12", local_interface, bad_P, E, expected)
    return P, E


def low_group(group, low_axis, other_axis, other_highs):
    need(len(group) == 4, "LOW_GROUP_SIZE")
    need(all(w[low_axis] == 3 for w in group), "LOW_GROUP_SYMBOL")
    for b in (0, 4):
        fiber = [w for w in group if w[1] == b]
        need(len(fiber) == 2 and {w[other_axis] for w in fiber} == set(other_highs),
             "LOW_GROUP_FIBER")


def all_h_and_same_E(P, component):
    # All 2^3 ordinary/exceptional combinations in the no-A-twin branch.
    for choices in product(((3, 2), (4, 1)), repeat=3):
        low_occurrences = 4 * sum(x[0] for x in choices)
        need(low_occurrences > 24, "NO_TWIN_LOW_COUNT")
        need(4 * choices[2][0] > 2 * choices[0][1] * choices[1][1],
             "ONE_TWIN_HIGH_HIGH_CAPACITY")
    even_A = {a for a in ((3, 3, 3, 3), (4, 3, 3, 2), (4, 4, 2, 2), (5, 3, 2, 2))
              if all(x % 2 == 0 for x in a)}
    even_B = {b for b in ((3, 3, 2, 2, 2), (4, 2, 2, 2, 2))
              if all(x % 2 == 0 for x in b)}
    need(even_A == {(4, 4, 2, 2)} and even_B == {(4, 2, 2, 2, 2)},
         "TWO_COMPONENT_EVEN_DEGREES")
    valid_h = []
    for h in product(range(3), repeat=3):
        if sum(h) > 3:
            continue
        if any(h[i] > 0 and any(h[j] == 0 for j in range(3) if j != i)
               for i in range(3)):
            continue
        valid_h.append(h)
    need(set(valid_h) == {(0, 0, 0), (1, 1, 1)}, "ALL_H_CASES")
    need(12 > 2 * 2 * 2, "ZERO_H_EIGHT_VS_TWELVE")
    need(4 + 2 + 2 == 8 and 8 > 2 * 3, "FINAL_EIGHT_VS_SIX")

    # Selected shadow cases use one SAME component, P, and the C- and D-low
    # groups. They are not physically accepted fixtures: all collide with P.
    # The universal 4+2+2 count above is independent of this selected shadow.
    assignments = [v for v in product((2, 3), repeat=4) if v.count(2) == 2]
    need(len(assignments) == 6, "LOW_A_ASSIGNMENTS")
    seen = 0
    for ac in assignments:
        guard()
        for ad in assignments:
            C = [(ac[k], b, 3, d) for k, (b, d) in enumerate(product((0, 4), (2, 4)))]
            D = [(ad[k], b, c, 3) for k, (b, c) in enumerate(product((0, 4), (1, 4)))]
            low_group(C, 2, 3, (2, 4))
            low_group(D, 3, 2, (1, 4))
            E = component + C + D
            need(len(E) == len(set(E)) == 20, "SAME_E_DISJOINT_GROUPS")
            need(sum(w[1] == 0 for w in component) == 4
                 and sum(w[1] == 0 for w in C) == 2
                 and sum(w[1] == 0 for w in D) == 2
                 and sum(w[1] == 0 for w in E) == 8, "SAME_E_OCCURRENCES")
            need((4, 4) in projection(P, (1, 2))
                 and (4, 4) in projection(E, (1, 2)), "SHADOW_P_E_COLLISION")
            C_missing = list(C)
            C_missing.remove(next(w for w in C_missing if w[1] == 0))
            expect_failure("LOW_GROUP_SIZE", low_group, C_missing, 2, 3, (2, 4))
            D_missing = list(D)
            D_missing.remove(next(w for w in D_missing if w[1] == 0))
            expect_failure("LOW_GROUP_SIZE", low_group, D_missing, 3, 2, (1, 4))
            need(sum(w[1] == 0 for w in component + C_missing + D_missing) == 6,
                 "OCCURRENCE_ASSUMPTION_MUTATION")
            seen += 1
    need(seen == 36, "SAME_E_SHADOW_ASSIGNMENTS")


def main():
    guard()
    _, _, raw = profiles_and_moments()
    print("OK complete degree profiles and raw moments")
    footprint_classification(raw)
    print("OK sixteen letter-valued outside-footprint covers")
    twin_components()
    print("OK cubic twin matchings and nonreal local phases")
    parity_phase()
    print("OK closed eight-word complex-phase contradiction")
    binary_twin_restrictions()
    print("OK full 4,4 and partial 5,3 binary restrictions")
    common_P_stars()
    print("OK seventy-two common-P matching configurations")
    two_twin_residuals()
    print("OK same-E two-twin residual supports")
    two_A_twins()
    print("OK two-A-twin high-high coloring obstruction")
    P, E = local_fixture()
    print("OK local six-pair interface and targeted mutations")
    all_h_and_same_E(P, E)
    print("OK all h-count cases and same-E occurrence shadows")
    print("DONE: projected/local interfaces only; no global tensor witness or proof")


if __name__ == "__main__":
    main()
