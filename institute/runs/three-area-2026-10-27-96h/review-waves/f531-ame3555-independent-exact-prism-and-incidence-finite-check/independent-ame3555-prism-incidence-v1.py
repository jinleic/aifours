from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product
from time import monotonic

START = monotonic()
Q = (3, 5, 5, 5)
B = tuple(6 - x for x in Q)
I = (1, 2, 3)
H = (3, 4)
PAIRS = tuple(combinations(range(4), 2))
GEDGES = tuple(combinations(I, 2))
CUBE_PAIRS = tuple(combinations(range(3), 2))
VSETS = tuple(combinations(range(5), 3))
GRAPHS = ()
BY_GRAPH = {}

class Bad(Exception):
    pass

def tick():
    if monotonic() - START >= 55:
        raise RuntimeError("INCOMPLETE_55_SECOND_DEADLINE")

def need(ok, reason):
    if not ok:
        raise Bad(reason)

def accepted(fn):
    try:
        fn()
    except Bad:
        return False
    return True

def expect_bad(reason, fn):
    try:
        fn()
    except Bad as exc:
        need(str(exc) == reason, "WRONG_REJECTION_REASON")
        return reason
    raise Bad("NEGATIVE_CONTROL_ACCEPTED")

def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, length - 1):
            yield (first,) + rest

def moment_profiles(second):
    found = []
    for v in compositions(24, 5):
        tick()
        if sum(s * v[s] for s in range(5)) != 60:
            continue
        if sum(s * (s - 1) // 2 * v[s] for s in range(5)) == second:
            found.append(v)
    return tuple(sorted(found))

def check_moment_profile(v):
    need(len(v) == 5 and all(type(x) is int and x >= 0 for x in v),
         "PROFILE_DOMAIN")
    need(sum(v) == 24, "WORD_TOTAL")
    need(sum(s * v[s] for s in range(5)) == 60, "FIRST_MOMENT")
    need(sum(s * (s - 1) // 2 * v[s] for s in range(5)) == 48,
         "SECOND_MOMENT")

def degree_profiles(i):
    upper = min(Q[j] for j in range(4) if j != i)
    out = []
    for rs in product(range(2, upper + 1), repeat=Q[i]):
        tick()
        if sum(rs) != 12:
            continue
        if all(r - B[i] >= 0 and 6 + B[i] - 2 * r >= 0 for r in rs):
            out.append(rs)
    return tuple(out)

def pair_tables(words):
    return {p: Counter((w[p[0]], w[p[1]]) for w in words) for p in PAIRS}

def check_pair_interface(words, projection_size):
    need(len(set(words)) == len(words), "DISTINCT_TENSOR_WORDS")
    for counts in pair_tables(words).values():
        need(all(n == 2 for n in counts.values()), "PAIR_EXTENSION_TWO")
        need(len(counts) == projection_size, "PAIR_PROJECTION_SIZE")

def check_rows(rows):
    need(all(len(nbrs) == 2 for nbrs in rows.values()), "ROW_DEGREE_TWO")
    cols = Counter(c for nbrs in rows.values() for c in nbrs)
    need(all(n == 2 for n in cols.values()), "COLUMN_DEGREE_TWO")
    for r, s in combinations(rows, 2):
        need(len(rows[r] & rows[s]) != 1, "ONE_COLUMN_OVERLAP")
    groups = Counter(frozenset(nbrs) for nbrs in rows.values())
    need(all(n == 2 for n in groups.values()), "NOT_K22_COMPONENTS")
    return len(groups)

def block_counts(words):
    out = []
    for left in ((0, 1), (0, 2), (0, 3)):
        right = tuple(i for i in range(4) if i not in left)
        rows = defaultdict(set)
        for w in words:
            rows[tuple(w[i] for i in left)].add(tuple(w[i] for i in right))
        out.append(check_rows(rows))
    return tuple(out)

def make_stars():
    out = []
    for i in I:
        a = i - 1
        d = [a, 5, 5, 5]
        d[i] = a
        t = [a, a, a, a]
        t[i] = 5
        out.extend((tuple(d), tuple(t)))
    return tuple(out)

def check_gauge(stars, maps):
    need(len(maps) == 3 and all(set(p) == {0, 1, 2} for p in maps),
         "LOW_LABEL_MAP_DOMAIN")
    for j in I:
        actual = {(w[0], w[j]) for w in stars if w[j] < 5}
        expected = {(a, maps[j - 1][a]) for a in range(3)}
        need(actual == expected, "COMMON_PHYSICAL_LOW_GAUGE")

def transform_stars(stars, maps):
    out = []
    for w in stars:
        v = list(w)
        for j in I:
            if v[j] < 3:
                v[j] = maps[j - 1][v[j]]
        out.append(tuple(v))
    return tuple(out)

def check_w(w):
    need(len(w) == 6, "SIX_COLORED_TRIPLES")
    need(len(set(w)) == 6, "SIX_DISTINCT_COLORED_TRIPLES")
    need(all(all(x in range(3) for x in e) for e in w), "PRISM_ALPHABET")
    need(len({(j, k) for a, j, k in w}) == 6, "REPEATED_JK_EDGE")
    need(Counter(a for a, j, k in w) == Counter({0: 2, 1: 2, 2: 2}),
         "COLOR_MULTIPLICITY_TWO")
    need(Counter(j for a, j, k in w) == Counter({0: 2, 1: 2, 2: 2}),
         "PRISM_LEFT_DEGREE_TWO")
    need(Counter(k for a, j, k in w) == Counter({0: 2, 1: 2, 2: 2}),
         "PRISM_RIGHT_DEGREE_TWO")
    need(len({(a, j) for a, j, k in w}) == 6, "REPEATED_0J_PAIR")
    need(len({(a, k) for a, j, k in w}) == 6, "REPEATED_0K_PAIR")
    adj = defaultdict(set)
    for a, j, k in w:
        adj[(0, j)].add((1, k))
        adj[(1, k)].add((0, j))
    seen = {(0, 0)}
    todo = [(0, 0)]
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    need(len(seen) == 6, "NOT_SIX_CYCLE")

def enumerate_prisms():
    graphs = []
    by_graph = {}
    for edges in combinations(tuple(product(range(3), repeat=2)), 6):
        tick()
        if Counter(j for j, k in edges) != Counter({0: 2, 1: 2, 2: 2}):
            continue
        if Counter(k for j, k in edges) != Counter({0: 2, 1: 2, 2: 2}):
            continue
        graphs.append(edges)
        colored = []
        for colors in product(range(3), repeat=6):
            if Counter(colors) != Counter({0: 2, 1: 2, 2: 2}):
                continue
            w = tuple((a, j, k) for a, (j, k) in zip(colors, edges))
            if accepted(lambda: check_w(w)):
                colored.append(w)
        by_graph[edges] = tuple(colored)
    need(len(graphs) == 6, "BARE_CYCLE_COUNT")
    need(all(len(by_graph[g]) == 24 for g in graphs), "BALANCED_COLOR_COUNT")
    for g in graphs:
        for w in by_graph[g]:
            lift = tuple((a, j, k, h) for a, j, k in w for h in range(2))
            check_pair_interface(lift, 6)
            need(block_counts(lift) == (3, 3, 3), "PRISM_BLOCK_COUNTS")
    return tuple(graphs), by_graph

@lru_cache(maxsize=100)
def degree_graphs(rd, cd):
    need(sum(rd) == 6 and sum(cd) == 6, "OUTSIDE_EDGE_TOTAL")
    out = []
    def visit(row, rem, edges):
        tick()
        if row == 5:
            if not any(rem):
                out.append(frozenset(edges))
            return
        available = tuple(c for c in range(5) if rem[c] > 0)
        if len(available) < rd[row]:
            return
        for selected in combinations(available, rd[row]):
            new = list(rem)
            for c in selected:
                new[c] -= 1
            remaining_positive_rows = sum(x > 0 for x in rd[row + 1:])
            if any(x > remaining_positive_rows for x in new):
                continue
            visit(row + 1, tuple(new),
                  edges + tuple((row, c) for c in selected))
    visit(0, cd, ())
    return tuple(out)

def edge(a, b):
    return tuple(sorted((a, b)))

def active_centers(g):
    return {next(x for x in I if x not in e) for e in g}

def local_interfaces(g, l):
    centers = active_centers(g)
    j, k = tuple(x for x in I if x != l)
    count = 0
    shapes = set()
    for u, v in product(VSETS, repeat=2):
        tick()
        hu = sum(x in H for x in u)
        hv = sum(x in H for x in v)
        if hu and edge(j, l) not in g:
            continue
        if hv and edge(k, l) not in g:
            continue
        if (j in centers and hu == 1) or (k in centers and hv == 1):
            continue
        rd = tuple((2 if x < 3 else 3) - 2 * (x in u) for x in range(5))
        cd = tuple((2 if x < 3 else 3) - 2 * (x in v) for x in range(5))
        outside_graphs = degree_graphs(rd, cd)
        for bare in GRAPHS:
            inside = frozenset((u[r], v[c]) for r, c in bare)
            if not any(x < 3 and y < 3 and x != y for x, y in inside):
                continue
            color_ok = any(
                all((u[r] >= 3 or a != u[r]) and
                    (v[c] >= 3 or a != v[c]) for a, r, c in w)
                for w in BY_GRAPH[bare])
            if not color_ok:
                continue
            for outside in outside_graphs:
                if inside & outside:
                    continue
                whole = inside | outside
                if any(x < 3 and y < 3 and
                       ((x == y == l - 1) or
                        (x != y and edge(j, k) not in g))
                       for x, y in whole):
                    continue
                if j in centers:
                    if {y for x, y in whole if x == 3} != \
                       {y for x, y in whole if x == 4}:
                        continue
                if k in centers:
                    if {x for x, y in whole if y == 3} != \
                       {x for x, y in whole if y == 4}:
                        continue
                count += 1
                shapes.add((hu, hv))
    return count, shapes

def cube_table(t):
    return {p: len({(w[p[0]], w[p[1]]) for w in t}) for p in CUBE_PAIRS}

def check_cube_coverage(table):
    need(set(table) == set(CUBE_PAIRS), "ALL_THREE_PAIR_PROJECTIONS")

def make_f(i, hj, hk, ownj, ownk):
    j, k = tuple(x for x in I if x != i)
    low = i - 1
    assignments = (
        {i: low, j: low, k: hk},
        {i: low, j: hj, k: low},
        {i: ownj, j: low, k: 7 - hk},
        {i: ownk, j: 7 - hj, k: low})
    return tuple(tuple(a[x] for x in I) for a in assignments)

def assemble(fs):
    return tuple((a,) + t for i, f in enumerate(fs)
                 for a in range(3) if a != i for t in f)

def fixture_from_targets(p):
    need(len(p) == 3 and all(p[i] in range(3) and p[i] != i
                            for i in range(3)), "TARGET_MAP_DOMAIN")
    fs = []
    for i in I:
        j, k = tuple(x for x in I if x != i)
        ownj = 4 if p[i - 1] == j - 1 else 3
        ownk = 4 if p[i - 1] == k - 1 else 3
        fs.append(make_f(i, 3, 3, ownj, ownk))
    return assemble(tuple(fs))

def check_zero_case():
    allowed = tuple((j, k, s) for j, k in GEDGES
                    for s in range(3) if s != 5 - j - k)
    need(len(allowed) == 6, "SIX_ALLOWED_LL_PAIRS")
    for s in range(3):
        star = {(j, k) for j, k, t in allowed if t == s}
        expected = {edge(s + 1, x) for x in I if x != s + 1}
        need(star == expected, "PHYSICAL_LL_STAR")
    shadows = []
    for n0, n1, n2 in compositions(24, 3):
        for m in range(7):
            if n1 + 2 * n2 == 36 and n2 == 2 * m:
                shadows.append((n0, n1, n2, m))
    need(shadows == [(0, 12, 12, 6)], "ZERO_CASE_COUNT_SHADOW")
    subset_survivors = []
    for mask in range(64):
        chosen = {allowed[t] for t in range(6) if mask & (1 << t)}
        if len(chosen) == shadows[0][3]:
            subset_survivors.append(chosen)
    need(subset_survivors == [set(allowed)], "FULL_LL_STAR_UNIVERSE")
    f_solutions = tuple(f for f in product(range(5), repeat=3)
                        if all(sum(f[i] for i in range(3) if i != s) == 2
                               for s in range(3)))
    need(f_solutions == ((1, 1, 1),), "HIGH_F_COUNTS")
    choices = tuple(tuple(make_f(i, *z) for z in product(H, repeat=4))
                    for i in I)
    weak = 0
    overlap_rejections = 0
    for fs in product(*choices):
        tick()
        words = assemble(fs)
        if not accepted(lambda: check_pair_interface(words, 12)):
            continue
        weak += 1
        for j in I:
            for h in H:
                f = tuple(sum(t[j - 1] == h for t in family) for family in fs)
                need(f == (1, 1, 1), "DERIVED_HIGH_F_COUNTS")
        expect_bad("ONE_COLUMN_OVERLAP", lambda: block_counts(words))
        overlap_rejections += 1
    need(weak > 0 and overlap_rejections == weak, "ZERO_WEAK_INTERFACE_AUDIT")
    return weak

def main():
    global GRAPHS, BY_GRAPH
    print("START: exact finite checker; cooperative limit 55 seconds")
    m48 = moment_profiles(48)
    m49 = moment_profiles(49)
    need(m48 == ((0, 0, 12, 12, 0),), "MOMENT_48_EXHAUSTION")
    need(set(m49) == {(0, 1, 10, 13, 0), (0, 0, 13, 10, 1)},
         "MOMENT_49_CONTROL_EXHAUSTION")
    profiles = tuple(degree_profiles(i) for i in range(4))
    need(profiles[0] == ((4, 4, 4),), "PARTY_ZERO_DEGREES")
    need(all(len(profiles[i]) == 10 and
             all(tuple(sorted(r)) == (2, 2, 2, 3, 3) for r in profiles[i])
             for i in I), "FIVE_SYMBOL_DEGREES")
    doubles = {}
    for p in PAIRS:
        k, l = tuple(i for i in range(4) if i not in p)
        doubles[p] = B[k] * B[l]
    triples = tuple(6 * B[i] - B[i] * sum(B[j] for j in range(4) if j != i)
                    for i in range(4))
    need(tuple(doubles[p] for p in PAIRS) == (1, 1, 1, 3, 3, 3),
         "MAXIMAL_DOUBLE_COUNTS")
    need(triples == (9, 1, 1, 1), "MAXIMAL_TRIPLE_COUNTS")
    oo = {p: B[p[0]] * B[p[1]] for p in PAIRS}
    io = {(i, j): Q[i] * B[j] for i in range(4)
          for j in range(4) if i != j}
    print("moments", m48, "degree_vector_counts", tuple(map(len, profiles)))
    print("double_counts", doubles, "triple_counts", triples)
    print("outside_outside", oo, "internal_outside", io)
    stars = make_stars()
    need(len(set(stars)) == 6 and
         all(len({(w[i], w[j]) for w in stars}) == 6 for i, j in PAIRS),
         "STAR_POSITIVE_PAIR_INJECTIVITY")
    perms = tuple(permutations(range(3)))
    literal = 0
    covariant = 0
    for maps in product(perms, repeat=3):
        literal += accepted(lambda: check_gauge(stars, maps))
        check_gauge(transform_stars(stars, maps), maps)
        covariant += 1
    need(literal == 1 and covariant == 216, "GAUGE_CONTROL_COUNTS")
    GRAPHS, BY_GRAPH = enumerate_prisms()
    prism_count = sum(len(BY_GRAPH[g]) for g in GRAPHS)
    need(prism_count == 144, "TOTAL_COLORED_PRISMS")
    cube = tuple(product(range(2), repeat=3))
    hist = Counter()
    for t in combinations(cube, 6):
        tick()
        table = cube_table(t)
        check_cube_coverage(table)
        hist[tuple(table[p] for p in CUBE_PAIRS)] += 1
    need(hist == Counter({(3, 4, 4): 4, (4, 3, 4): 4,
                          (4, 4, 3): 4, (4, 4, 4): 16}),
         "BINARY_SIX_SUBSET_HISTOGRAM")
    need(hist[(3, 3, 3)] == 0, "BINARY_HIGH_TRIPLE_IMPOSSIBILITY")
    print("abstract_prisms", prism_count, "binary_histogram", dict(hist))
    for mask in range(8):
        tick()
        g = {GEDGES[t] for t in range(3) if mask & (1 << t)}
        summary = {l: local_interfaces(g, l) for l in sorted(active_centers(g))}
        if 0 < mask < 7:
            need(all(n == 0 for n, shapes in summary.values()),
                 "UNEXPECTED_ONE_OR_TWO_EDGE_INTERFACE")
        if mask == 7:
            need(all(shapes <= {(2, 2)} for n, shapes in summary.values()),
                 "NONFULL_HIGH_BLOCK_SURVIVED")
        print("G_mask", mask, "local_necessary_interfaces", summary)
    weak_zero = check_zero_case()
    print("zero_case_pair_interface_fixtures", weak_zero,
          "all rejected for one-column overlap")
    base = ((0, 0, 0), (1, 1, 1), (2, 2, 2),
            (2, 0, 1), (0, 1, 2), (1, 2, 0))
    check_w(base)
    positive_weak = fixture_from_targets((1, 2, 0))
    check_pair_interface(positive_weak, 12)
    controls = []
    controls.append(expect_bad("SECOND_MOMENT",
                    lambda: check_moment_profile((0, 1, 10, 13, 0))))
    bad_maps = ((1, 0, 2), (0, 1, 2), (0, 1, 2))
    controls.append(expect_bad("COMMON_PHYSICAL_LOW_GAUGE",
                    lambda: check_gauge(stars, bad_maps)))
    repeated_edge = base[:-1] + ((1, 0, 0),)
    controls.append(expect_bad("REPEATED_JK_EDGE",
                    lambda: check_w(repeated_edge)))
    wrong_cycle = fixture_from_targets((1, 0, 0))
    controls.append(expect_bad("PAIR_EXTENSION_TWO",
                    lambda: check_pair_interface(wrong_cycle, 12)))
    partial_table = cube_table(cube[:6])
    del partial_table[(1, 2)]
    controls.append(expect_bad("ALL_THREE_PAIR_PROJECTIONS",
                    lambda: check_cube_coverage(partial_table)))
    rows = {r: {c for c in range(3) if c != r} for r in range(3)}
    need(all(len(rows[r] & rows[s]) == 1 for r, s in combinations(rows, 2)),
         "ONE_OVERLAP_CONTROL_SHAPE")
    controls.append(expect_bad("ONE_COLUMN_OVERLAP",
                    lambda: check_rows(rows)))
    fake_six = ((0, 0, 0), (1, 1, 1), (2, 2, 2)) * 2
    controls.append(expect_bad("SIX_DISTINCT_COLORED_TRIPLES",
                    lambda: check_w(fake_six)))
    bad_0j = ((2, 0, 0), (1, 1, 1), (0, 2, 2),
              (2, 0, 1), (0, 1, 2), (1, 2, 0))
    controls.append(expect_bad("REPEATED_0J_PAIR",
                    lambda: check_w(bad_0j)))
    need(len(controls) == 8 and len(set(controls)) == 8,
         "REASON_SPECIFIC_CONTROL_COUNT")
    tick()
    print("negative_control_reasons", tuple(controls))
    print("COMPLETE: all declared finite checks and eight controls completed")
    print("LIMIT: weak interfaces only; no physical AME or complex-phase witness")

if __name__ == "__main__":
    main()
