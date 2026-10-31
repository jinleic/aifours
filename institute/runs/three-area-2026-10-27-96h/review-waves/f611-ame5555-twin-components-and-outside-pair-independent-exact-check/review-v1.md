# F611 — Independent exact-interface review of the entire \(5555\) candidate

**Findings: none.**

**Written mathematical assessment:** the frozen candidate’s fixed-profile contradiction is correct. Its common-twin saturation, low-low complex-phase obstruction, zero-/one-twin exclusions, and final same-\(P\) collision fit together without an additional mathematical assumption.

**FINITE execution status: NOT RUN.** My higher-priority role prohibits scientific execution and filesystem edits. Accordingly, I supply the complete independent standard-library checker below, with its exact invocation, without claiming any observed checker result or elapsed time. This does **not** complete an executed FINITE acceptance gate or adopt the candidate.

## 1. Input and chronology record

Before accessing the mathematical packet, I read through the endings of:

- The manifest, logical lines 1–122.
- The freeze receipt, logical lines 1–47.
- All thirteen manifest-listed permission/status controls.

I then sent the required direct `PREBODYACK` to `agent://Main`; delivery was reported by the messaging tool.

Only afterward, I read the entire literal packet sequentially in exact raw ranges of at most twenty lines: 1–20, 21–40, …, 561–580, and 581–600. The last call returned the packet’s final two lines, ending at `S2|49`. This covered all 531 logical lines of S1 and all 49 logical lines of S2 before derivation.

I subsequently read the complete parent-supplied metadata and dispatch receipt. These provide **parent-observed**, not child-recomputed, pins:

- Manifest: `d4c565e28daf107b28dcf13f174a27d7ad96f5c712a1e3d17c25b641d7dcdc6b`.
- Freeze receipt: `bcf61faf6839c0c041e70551b28f723444d757528ae79d7e16febd3a4975e089`.
- Literal packet: `1368fc0bb2da980d8b74dbdf1c24c58f636f937a71c269ae62e4aee50f90ebcf`.
- S1, the full f597 candidate: `9cd3311e6ae8eb98b9437f0ae6652f5ce9552a26e94213af47e01500a8fa25af`.
- S2, the complete prior \(4455\) disposition: `faadf4777ac1b3f0e57d484624080a08835c9d71de980b87ad823866531f3bb4`.

No linked scientific source, prior checker, sibling review, held scientific payload, or held consumer was opened. No external source or model was used. No scientific program was executed and no repository file was written. These are access/tool-record statements, not a cognitive-isolation certificate.

## 2. Independent mathematical reconstruction

### 2.1 Same actual tensor and all six physical pairs

Assume the candidate’s hypotheses for one complex tensor \(U\). Let \(P\) be its 24 modulus-one positions and \(E\) its 24 remaining nonzero positions.

At every physical pair, a modulus-one entry exhausts both its flattening row and column. Consequently:

1. The physical pair projection of \(P\) is injective.
2. No residual word uses a pair occupied by \(P\).
3. The other twelve pair values must each have at least two residual extensions.
4. Since \(|E|=24\), each has exactly two extensions.

In each balanced flattening, two residual rows sharing one column cannot have different second columns: their inner product would contain exactly one nonzero summand. The residual support therefore consists of full \(2\times2\) blocks in **each of the three actual cuts**.

For a residual symbol \(a\) at party \(i\), its occurrence count is \(2r_i(a)\), independently of which other party defines the neighborhood degree. A degree-one symbol would have only one possible value at every other coordinate, making its two occurrences identical. Thus all five degrees are at least two and sum to twelve.

The only unordered profiles are:

\[
(3,3,2,2,2),\qquad (4,2,2,2,2).
\]

There are fifteen ordered degree assignments: ten ordinary assignments and five exceptional assignments.

### 2.2 Moments and outside footprints

At each party the residual symbols occur eighteen times in \(P\); at each physical pair thirteen maximal pairs are internal. Hence

\[
\sum k\,n_k=72,\qquad
\sum \binom{k}{2}n_k=78,\qquad
\sum n_k=24.
\]

Every outside pair occurs exactly once in \(P\), so

\[
6n_0+3n_1+n_2=6.
\]

Two words each having three outside coordinates would repeat an outside pair, giving \(n_1\le1\). These constraints yield exactly the three necessary histograms:

\[
(1,0,0,20,3),\quad
(0,0,6,12,6),\quad
(0,1,3,15,5).
\]

These are necessary integer histograms, not realizability assertions.

For a fixed internal symbol of degree \(r\), its \(6-r\) maximal occurrences have a total of three outside incidences. For \(r=4\), the two outside occupancies must therefore be \(\{0,3\}\) or \(\{1,2\}\). This also validates the stated exclusion of exceptional parties from histogram A.

### 2.3 Common-twin saturation

A distance-one pair with differing symbols \(a,a'\) has a nonempty common three-coordinate slice \(T\). Actual block closure makes \(T\) closed under the three equality matchings.

Those matchings cannot share an edge: two common triples agreeing at two coordinates, together with their copies at \(a,a'\), would produce four extensions of a physical pair.

For the actual nonzero complex products

\[
z_t=U_{a,t}\overline{U_{a',t}},
\]

every matching edge gives \(z_t+z_{t'}=0\). The resulting simple cubic graph is bipartite. Its order is therefore at least six; the symbol-slice bound gives order six or eight.

- Order eight requires **two distinct degree-four symbols**, which neither five-symbol degree profile permits.
- At order six, each remaining coordinate has three values, each appearing twice. If a complete slice had two more triples, both additional triples would have to use the unique fourth value at all three coordinates. They would coincide.

Thus both full slices are the same six triples, and the differing symbols form the ordinary party’s degree-three high pair.

Different-coordinate twin components are word-disjoint: otherwise both independent twin replacements produce four words sharing the complementary physical pair. Each component has twelve words, so there are at most two twin coordinates.

### 2.4 Actual low-low closure and arbitrary complex phases

Consider the two extensions of a low-low pair. If they differ at both complementary coordinates, the four-word slice of either low symbol has three distinct balanced equality partitions.

In the relevant starting configuration, coincidence of the two complementary partitions would give a distance-one pair varying through the specified low symbol, contradicting the preceding saturation result.

The two actual low slices and actual block closure force the eight binary even-parity words:

\[
0000,\ 0011,\ 0101,\ 0110,\ 1001,\ 1010,\ 1100,\ 1111.
\]

Every used physical pair already has two extensions inside this set. It is therefore closed in all three actual cuts.

For their nonzero amplitudes, let \(\epsilon_w=u_w/|u_w|\) and set

\[
X=\epsilon_{0000}\epsilon_{1111},\quad
Y=\epsilon_{0011}\epsilon_{1100},\quad
Z=\epsilon_{0101}\epsilon_{1010}.
\]

Three actual row-orthogonality equations, one from each cut, give

\[
X=-Y,\qquad X=-Z,\qquad Y=-Z.
\]

Their integer exponent rows satisfy

\[
R_1-R_2+R_3=0,
\]

while the corresponding negative-sign exponent is \(1-1+1=1\), an odd integer. Multiplication of the three relations with these integer coefficients therefore gives \(1=-1\).

This is a certificate in integer exponents for arbitrary nonzero complex phases. It does not replace phases by real signs or reduce exponents modulo two. Normalization of a nonzero two-term cancellation justifies the phase equations without an equal-modulus assumption.

Consequently every low-low pair routes through a twin at a complementary coordinate.

### 2.5 Zero and one twin are impossible

With no twins, no low-low edge is permitted. Every party must then have two highs, hence be ordinary. Degree saturation forces every pair graph to consist exactly of low-high and high-low edges. Four binary low/high statuses cannot be pairwise opposite, so no residual word can exist.

With exactly one twin coordinate \(i\), the pair graphs incident to \(i\) have no low-low edges. Again all parties are ordinary. The twelve residual words whose \(i\)-coordinate is low must be high at all three other coordinates. Any two of those coordinates offer only four high-high pair values, with capacity two each: capacity eight, not twelve.

There are therefore exactly two twin coordinates.

### 2.6 Two components and the common-\(P\) endpoint

Let the twins be at \(i,j\). Their twelve-word components partition the **same** \(E\). At either remaining coordinate, each component uses three symbols, four times each. Their union is the residual alphabet of size five, so their intersection has size one. That remaining party is exceptional.

No residual word can contain both an \(H_i\) symbol and an \(H_j\) symbol. Thus every one of the four \(H_i\times H_j\) pairs requires a maximal word in the **same** \(P\).

At coordinate \(k\), such a maximal word must avoid both component alphabets: its pair with the \(i\)-high excludes one alphabet, and its pair with the \(j\)-high excludes the other. Their union is all five residual symbols. Hence the word must use \(o_k\). Likewise it must use \(o_\ell\).

All four distinct maximal words therefore have the same complementary physical pair \((o_k,o_\ell)\), contradicting injectivity of \(\pi_{k\ell}(P)\).

This final step consumes actual residual neighborhoods and actual maximal words. Separate per-cut complements cannot satisfy the required same-word binding.

## 3. Finite-check scope and result distinctions

The source below independently implements:

- All ordered five-symbol degree compositions with minimum two and sum twelve.
- The \(72/78\) moment equations, outside-pair footprint, and all three histograms.
- The degree-four symbol’s two possible outside-occupancy patterns.
- All three-color perfect-matching configurations on six labelled vertices, filtering edge overlap and odd cycles, reconstructing actual coordinate triples, and checking all six pair projections and all three cuts for every twin placement.
- The impossible attempt to enlarge a six-triple common slice to eight.
- The eight-common-triple branch by its necessary two-distinct-degree-four demand, checked against every degree composition. Eight-vertex matching enumeration is unnecessary for this branch and is not claimed.
- All 216 labelled balanced three-coordinate partitions on four word labels, including all 48 relevant low-distance-one cases and all 48 all-distinct closure cases.
- Actual eight-word closure, all six pair multiplicities, all three physical cuts, and the integer complex-phase certificate.
- A genuinely nonreal exact control with \(q=(3+4i)/5\): two cuts are scaled-unitary and the third is not.
- All no-low-low pair graphs for every ordered degree-profile pair.
- The zero-twin status obstruction and one-twin capacity \(12>8\).
- All ordered pairs of three-symbol component alphabets whose union is five, at both remaining coordinates, and every physical choice of twin-coordinate pair.
- Eight intended-reason rejection controls.

Analytically derived enumeration expectations, **not observed execution results**, include:

- Fifteen ordered degree profiles.
- Three maximal-word histograms.
- 120 bipartite six-vertex ordered matching triples.
- 216 labelled low-slice partition triples, with 48 all-distinct closures.
- Thirty ordered alphabet-pair choices per remaining coordinate; 900 combined choices and 5,400 physical twin-role assignments.

The weak components, phase controls, projection-binding mutants, and forced four-word maps are **not complete \(E/P/U\) objects**. No actual global tensor mutant is supplied. In particular, the independent-per-cut, overlapping-component, and dropped-\(P\)-injectivity controls test local/formal interface rejection, not corrupted physical AME tensors.

## 4. Complete checker source — NOT RUN

Suggested filename: `independent-whole-ame5555-physical-interfaces-v1.py`

Exact invocation: `python3 -B independent-whole-ame5555-physical-interfaces-v1.py`

The program has a cooperative 55-second deadline, uses only the standard library, reads no files, makes no network calls, spawns no children, and writes only to standard output. No source hash or runtime is claimed here.

For literal recovery, remove exactly the initial `PY|` from every source line below and retain the remaining text and line endings.

PY|from collections import Counter
PY|from fractions import Fraction
PY|from itertools import combinations, permutations, product
PY|from time import monotonic
PY|import sys
PY|
PY|PAIRS = tuple(combinations(range(4), 2))
PY|CUTS = (
PY|    ((0, 1), (2, 3)),
PY|    ((0, 2), (1, 3)),
PY|    ((0, 3), (1, 2)),
PY|)
PY|ZERO = (Fraction(0), Fraction(0))
PY|TWO = (Fraction(2), Fraction(0))
PY|DEADLINE = 0.0
PY|
PY|
PY|class CheckFailure(Exception):
PY|    def __init__(self, reason):
PY|        self.reason = reason
PY|        super().__init__(reason)
PY|
PY|
PY|def need(condition, reason):
PY|    if not condition:
PY|        raise CheckFailure(reason)
PY|
PY|
PY|def tick():
PY|    need(monotonic() <= DEADLINE, "cooperative-55-second-budget-exhausted")
PY|
PY|
PY|def project(word, coordinates):
PY|    return tuple(word[i] for i in coordinates)
PY|
PY|
PY|def compositions(total, parts, minimum):
PY|    if parts == 1:
PY|        if total >= minimum:
PY|            yield (total,)
PY|        return
PY|    upper = total - minimum * (parts - 1)
PY|    for first in range(minimum, upper + 1):
PY|        for tail in compositions(total - first, parts - 1, minimum):
PY|            yield (first,) + tail
PY|
PY|
PY|def pair_counters(words):
PY|    need(len(set(words)) == len(words), "duplicate-support-word")
PY|    return {
PY|        pair: Counter(project(word, pair) for word in words)
PY|        for pair in PAIRS
PY|    }
PY|
PY|
PY|def require_pair_multiplicity(words, multiplicity):
PY|    counters = pair_counters(words)
PY|    for pair in PAIRS:
PY|        need(bool(counters[pair]), "empty-pair-projection")
PY|        need(
PY|            set(counters[pair].values()) == {multiplicity},
PY|            "physical-pair-multiplicity",
PY|        )
PY|    return counters
PY|
PY|
PY|def require_injective_pair(words, pair):
PY|    values = tuple(project(word, pair) for word in words)
PY|    need(len(set(values)) == len(values), "maximal-pair-collision")
PY|
PY|
PY|def actual_claims(words):
PY|    return {
PY|        pair: tuple(project(word, pair) for word in words)
PY|        for pair in PAIRS
PY|    }
PY|
PY|
PY|def require_bound_claims(words, claims):
PY|    need(set(claims) == set(PAIRS), "missing-pair-claim")
PY|    for pair in PAIRS:
PY|        need(len(claims[pair]) == len(words), "pair-claim-length")
PY|        need(
PY|            tuple(claims[pair]) ==
PY|            tuple(project(word, pair) for word in words),
PY|            "same-word-projection",
PY|        )
PY|
PY|
PY|def block_count(words, cut):
PY|    row_coordinates, column_coordinates = cut
PY|    rows = {}
PY|    columns = {}
PY|    for word in words:
PY|        row = project(word, row_coordinates)
PY|        column = project(word, column_coordinates)
PY|        rows.setdefault(row, set()).add(column)
PY|        columns.setdefault(column, set()).add(row)
PY|    need(all(len(values) == 2 for values in rows.values()),
PY|         "physical-row-degree")
PY|    need(all(len(values) == 2 for values in columns.values()),
PY|         "physical-column-degree")
PY|    blocks = set()
PY|    for row, values in rows.items():
PY|        c0, c1 = sorted(values)
PY|        need(columns[c0] == columns[c1], "non-rectangular-actual-cut")
PY|        need(len(columns[c0]) == 2, "physical-block-row-count")
PY|        block_rows = frozenset(columns[c0])
PY|        for other in block_rows:
PY|            need(rows[other] == values, "physical-block-closure")
PY|        blocks.add((block_rows, frozenset(values)))
PY|    return len(blocks)
PY|
PY|
PY|def check_degrees_and_moments(stats):
PY|    profiles = tuple(compositions(12, 5, 2))
PY|    need(len(profiles) == 15, "ordered-degree-profile-count")
PY|    need(
PY|        {tuple(sorted(p)) for p in profiles} ==
PY|        {(2, 2, 2, 3, 3), (2, 2, 2, 2, 4)},
PY|        "degree-profile-classification",
PY|    )
PY|    c = 4 * (5 * 6 - 12)
PY|    m = len(PAIRS) * (5 * 5 - 12)
PY|    need((c, m) == (72, 78), "5555-maximal-moments")
PY|    histograms = set()
PY|    for n in compositions(24, 5, 0):
PY|        tick()
PY|        if sum(k * n[k] for k in range(5)) != c:
PY|            continue
PY|        if sum(k * (k - 1) // 2 * n[k] for k in range(5)) != m:
PY|            continue
PY|        if 6 * n[0] + 3 * n[1] + n[2] != 6:
PY|            continue
PY|        if n[1] > 1:
PY|            continue
PY|        need(3 * n[0] + n[1] + n[4] == 6,
PY|             "moment-elimination-one")
PY|        need(n[4] == 3 * n[0] + 2 * n[1] + n[2],
PY|             "moment-elimination-two")
PY|        histograms.add(n)
PY|    expected = {
PY|        (1, 0, 0, 20, 3),
PY|        (0, 0, 6, 12, 6),
PY|        (0, 1, 3, 15, 5),
PY|    }
PY|    need(histograms == expected, "moment-outside-histograms")
PY|    exceptional_occupancies = set()
PY|    for degree in (2, 3, 4):
PY|        for occupancy in compositions(6 - degree, 4, 0):
PY|            if sum(h * occupancy[h] for h in range(4)) != 3:
PY|                continue
PY|            need(
PY|                degree ==
PY|                3 - occupancy[0] + occupancy[2] + 2 * occupancy[3],
PY|                "local-outside-identity",
PY|            )
PY|            if degree == 4:
PY|                exceptional_occupancies.add(tuple(
PY|                    h
PY|                    for h in range(4)
PY|                    for unused in range(occupancy[h])
PY|                ))
PY|    need(exceptional_occupancies == {(0, 3), (1, 2)},
PY|         "exceptional-outside-occupancies")
PY|    need(all(max(values) >= 2 for values in exceptional_occupancies),
PY|         "exceptional-needs-two-outside")
PY|    for p in profiles:
PY|        need(not any(
PY|            p[a] >= 4 and p[b] >= 4
PY|            for a, b in combinations(range(5), 2)
PY|        ), "two-degree-four-profile")
PY|    stats["ordered_degree_profiles"] = len(profiles)
PY|    stats["maximal_histograms"] = len(histograms)
PY|    return profiles
PY|
PY|
PY|def require_distinct_slice_demands(profile, demands):
PY|    need(len(profile) == 5 and min(profile) >= 2 and sum(profile) == 12,
PY|         "invalid-degree-profile")
PY|    fits = any(
PY|        all(profile[index] >= demand
PY|            for index, demand in zip(indices, demands))
PY|        for indices in permutations(range(5), len(demands))
PY|    )
PY|    need(fits, "two-degree4-slices")
PY|
PY|
PY|def perfect_matchings(vertices):
PY|    if not vertices:
PY|        yield ()
PY|        return
PY|    first = vertices[0]
PY|    for index in range(1, len(vertices)):
PY|        second = vertices[index]
PY|        rest = vertices[1:index] + vertices[index + 1:]
PY|        for tail in perfect_matchings(rest):
PY|            yield ((first, second),) + tail
PY|
PY|
PY|def require_colours(colours, order):
PY|    need(len(colours) == 3, "matching-colour-count")
PY|    used_edges = set()
PY|    for matching in colours:
PY|        vertices = tuple(v for edge in matching for v in edge)
PY|        need(len(vertices) == order, "matching-size")
PY|        need(set(vertices) == set(range(order)), "matching-vertex-coverage")
PY|        need(len(set(vertices)) == order, "matching-vertex-repeat")
PY|        edges = {tuple(sorted(edge)) for edge in matching}
PY|        need(all(a != b for a, b in edges), "matching-loop")
PY|        need(not (used_edges & edges), "matching-edge-repeat")
PY|        used_edges.update(edges)
PY|
PY|
PY|def bipartition(colours, order):
PY|    adjacency = [[] for unused in range(order)]
PY|    for matching in colours:
PY|        for a, b in matching:
PY|            adjacency[a].append(b)
PY|            adjacency[b].append(a)
PY|    need(all(len(row) == 3 for row in adjacency), "cubic-degree")
PY|    colour = [-1] * order
PY|    for root in range(order):
PY|        if colour[root] != -1:
PY|            continue
PY|        colour[root] = 0
PY|        stack = [root]
PY|        while stack:
PY|            vertex = stack.pop()
PY|            for other in adjacency[vertex]:
PY|                if colour[other] == -1:
PY|                    colour[other] = 1 - colour[vertex]
PY|                    stack.append(other)
PY|                elif colour[other] == colour[vertex]:
PY|                    return None
PY|    return tuple(colour)
PY|
PY|
PY|def triples_from_colours(colours, order):
PY|    triples = [[None, None, None] for unused in range(order)]
PY|    for coordinate, matching in enumerate(colours):
PY|        for label, edge in enumerate(matching):
PY|            for vertex in edge:
PY|                triples[vertex][coordinate] = label
PY|    need(all(value is not None for row in triples for value in row),
PY|         "unassigned-coordinate-value")
PY|    return tuple(tuple(row) for row in triples)
PY|
PY|
PY|def require_slice(triples, degree):
PY|    need(len(set(triples)) == len(triples), "slice-duplicate")
PY|    need(len(triples) == 2 * degree, "slice-size")
PY|    for coordinate in range(3):
PY|        counts = Counter(row[coordinate] for row in triples)
PY|        need(len(counts) == degree and set(counts.values()) == {2},
PY|             "slice-coordinate-degree")
PY|
PY|
PY|def place_component(triples, twin_coordinate):
PY|    remaining = tuple(i for i in range(4) if i != twin_coordinate)
PY|    words = []
PY|    for high in (0, 1):
PY|        for triple in triples:
PY|            word = [None] * 4
PY|            word[twin_coordinate] = high
PY|            for coordinate, value in zip(remaining, triple):
PY|                word[coordinate] = value
PY|            words.append(tuple(word))
PY|    return tuple(words)
PY|
PY|
PY|def check_common_twins(profiles, stats):
PY|    pool = tuple(perfect_matchings(tuple(range(6))))
PY|    need(len(pool) == 15, "six-vertex-perfect-matching-count")
PY|    masks = tuple(frozenset(matching) for matching in pool)
PY|    edge_distinct = 0
PY|    accepted = 0
PY|    component_placements = 0
PY|    first_triples = None
PY|    q = (Fraction(3, 5), Fraction(4, 5))
PY|    for ia, a in enumerate(pool):
PY|        tick()
PY|        for ib, b in enumerate(pool):
PY|            if masks[ia] & masks[ib]:
PY|                continue
PY|            used = masks[ia] | masks[ib]
PY|            for ic, c in enumerate(pool):
PY|                if used & masks[ic]:
PY|                    continue
PY|                colours = (a, b, c)
PY|                require_colours(colours, 6)
PY|                edge_distinct += 1
PY|                sides = bipartition(colours, 6)
PY|                if sides is None:
PY|                    continue
PY|                accepted += 1
PY|                triples = triples_from_colours(colours, 6)
PY|                require_slice(triples, 3)
PY|                for pair in combinations(range(3), 2):
PY|                    need(len({project(t, pair) for t in triples}) == 6,
PY|                         "common-triple-pair-injectivity")
PY|                z = tuple(q if side == 0 else (-q[0], -q[1])
PY|                          for side in sides)
PY|                for matching in colours:
PY|                    for u, v in matching:
PY|                        need(gadd(z[u], z[v]) == ZERO,
PY|                             "complex-edge-alternation")
PY|                for twin_coordinate in range(4):
PY|                    component = place_component(triples, twin_coordinate)
PY|                    require_pair_multiplicity(component, 2)
PY|                    for cut in CUTS:
PY|                        need(block_count(component, cut) == 3,
PY|                             "twin-component-actual-cut")
PY|                    component_placements += 1
PY|                forced_remainder = tuple(
PY|                    next(iter(set(range(4)) -
PY|                              {t[coordinate] for t in triples}))
PY|                    for coordinate in range(3)
PY|                )
PY|                need(forced_remainder == (3, 3, 3),
PY|                     "six-to-eight-remainder-labels")
PY|                leftovers = (forced_remainder, forced_remainder)
PY|                need(len(set(leftovers)) == 1,
PY|                     "six-to-eight-leftovers-not-identical")
PY|                if first_triples is None:
PY|                    first_triples = triples
PY|    need(accepted == 120, "bipartite-six-vertex-coloured-count")
PY|    need(first_triples is not None, "missing-six-triple-control")
PY|    for profile in profiles:
PY|        fits_eight_overlap = any(
PY|            profile[a] >= 4 and profile[b] >= 4
PY|            for a, b in combinations(range(5), 2)
PY|        )
PY|        need(not fits_eight_overlap, "eight-overlap-degree-demand")
PY|    stats["edge_distinct_six_vertex_colour_triples"] = edge_distinct
PY|    stats["bipartite_six_vertex_colour_triples"] = accepted
PY|    stats["twin_component_physical_placements"] = component_placements
PY|    stats["eight_overlap_degree_profiles_checked"] = len(profiles)
PY|    return first_triples, pool
PY|
PY|
PY|def rectangle_closure(initial):
PY|    words = set(initial)
PY|    while True:
PY|        tick()
PY|        additions = set()
PY|        for row_coordinates, column_coordinates in CUTS:
PY|            rows = {}
PY|            for word in words:
PY|                rows.setdefault(project(word, row_coordinates), set()).add(
PY|                    project(word, column_coordinates)
PY|                )
PY|            need(all(len(columns) <= 2 for columns in rows.values()),
PY|                 "closure-row-overflow")
PY|            for left, right in combinations(rows, 2):
PY|                if not (rows[left] & rows[right]):
PY|                    continue
PY|                columns = rows[left] | rows[right]
PY|                need(len(columns) <= 2, "closure-incompatible-columns")
PY|                for row in (left, right):
PY|                    for column in columns:
PY|                        word = [None] * 4
PY|                        for coordinate, value in zip(row_coordinates, row):
PY|                            word[coordinate] = value
PY|                        for coordinate, value in zip(
PY|                                column_coordinates, column):
PY|                            word[coordinate] = value
PY|                        additions.add(tuple(word))
PY|        additions -= words
PY|        if not additions:
PY|            return frozenset(words)
PY|        words.update(additions)
PY|        need(len(words) <= 16, "binary-closure-universe")
PY|        counters = pair_counters(tuple(words))
PY|        need(all(value <= 2 for counts in counters.values()
PY|                 for value in counts.values()),
PY|             "closure-pair-overflow")
PY|
PY|
PY|def partition_key(column):
PY|    groups = (
PY|        tuple(i for i, value in enumerate(column) if value == 0),
PY|        tuple(i for i, value in enumerate(column) if value == 1),
PY|    )
PY|    return tuple(sorted(groups))
PY|
PY|
PY|def check_low_slices(stats):
PY|    columns = tuple(
PY|        tuple(0 if i in zeros else 1 for i in range(4))
PY|        for zeros in combinations(range(4), 2)
PY|    )
PY|    classification = Counter()
PY|    relevant_low_distance = 0
PY|    closures = 0
PY|    examined = 0
PY|    for chosen in product(columns, repeat=3):
PY|        tick()
PY|        examined += 1
PY|        triples = tuple(zip(*chosen))
PY|        keys = tuple(partition_key(column) for column in chosen)
PY|        distinct = len(set(keys))
PY|        classification[distinct] += 1
PY|        if distinct == 2:
PY|            need(any(
PY|                sum(x != y for x, y in zip(a, b)) == 1
PY|                for a, b in combinations(triples, 2)
PY|            ), "equal-partitions-distance-one")
PY|        relevant = keys[0] != keys[1] and keys[0] != keys[2]
PY|        if not relevant:
PY|            continue
PY|        if keys[1] == keys[2]:
PY|            reference = triples[0]
PY|            need(any(
PY|                other[0] != reference[0] and
PY|                other[1:] == reference[1:]
PY|                for other in triples[1:]
PY|            ), "specified-low-distance-one")
PY|            relevant_low_distance += 1
PY|            continue
PY|        need(distinct == 3, "low-slice-partition-routing")
PY|        a_slice = tuple((0,) + triple for triple in triples)
PY|        b = a_slice[0][1]
PY|        extensions = tuple(word for word in a_slice if word[1] == b)
PY|        need(len(extensions) == 2, "low-low-two-extensions")
PY|        left, right = extensions
PY|        need(left[2] != right[2] and left[3] != right[3],
PY|             "low-low-both-complements-differ")
PY|        seed = a_slice + (
PY|            (1, b, left[2], right[3]),
PY|            (1, b, right[2], left[3]),
PY|        )
PY|        closed = rectangle_closure(seed)
PY|        parity = sum(a_slice[0]) % 2
PY|        expected = frozenset(
PY|            word for word in product((0, 1), repeat=4)
PY|            if sum(word) % 2 == parity
PY|        )
PY|        need(closed == expected, "actual-eight-word-parity-closure")
PY|        require_pair_multiplicity(tuple(closed), 2)
PY|        for cut in CUTS:
PY|            need(block_count(closed, cut) == 2,
PY|                 "eight-word-physical-cut-blocks")
PY|        closures += 1
PY|    need(examined == 216, "labelled-low-slice-count")
PY|    need(dict(classification) == {1: 24, 2: 144, 3: 48},
PY|         "low-slice-partition-classification")
PY|    need(relevant_low_distance == 48, "relevant-low-distance-count")
PY|    need(closures == 48, "all-distinct-closure-count")
PY|    stats["labelled_low_slice_partition_triples"] = examined
PY|    stats["specified_low_distance_rejections"] = relevant_low_distance
PY|    stats["actual_eight_word_closures"] = closures
PY|
PY|
PY|def gadd(a, b):
PY|    return (a[0] + b[0], a[1] + b[1])
PY|
PY|
PY|def gmul(a, b):
PY|    return (a[0] * b[0] - a[1] * b[1],
PY|            a[0] * b[1] + a[1] * b[0])
PY|
PY|
PY|def gconj(a):
PY|    return (a[0], -a[1])
PY|
PY|
PY|def gnorm(a):
PY|    return a[0] * a[0] + a[1] * a[1]
PY|
PY|
PY|def gaussian_sum(values):
PY|    result = ZERO
PY|    for value in values:
PY|        result = gadd(result, value)
PY|    return result
PY|
PY|
PY|def cut_is_scaled_unitary(amplitudes, cut):
PY|    row_coordinates, column_coordinates = cut
PY|    rows = tuple(sorted({
PY|        project(word, row_coordinates) for word in amplitudes
PY|    }))
PY|    columns = tuple(sorted({
PY|        project(word, column_coordinates) for word in amplitudes
PY|    }))
PY|    if len(rows) != 4 or len(columns) != 4:
PY|        return False
PY|    matrix = {
PY|        (project(word, row_coordinates),
PY|         project(word, column_coordinates)): value
PY|        for word, value in amplitudes.items()
PY|    }
PY|    for a, b in product(rows, repeat=2):
PY|        value = gaussian_sum(
PY|            gmul(matrix.get((a, c), ZERO),
PY|                 gconj(matrix.get((b, c), ZERO)))
PY|            for c in columns
PY|        )
PY|        if value != (TWO if a == b else ZERO):
PY|            return False
PY|    for a, b in product(columns, repeat=2):
PY|        value = gaussian_sum(
PY|            gmul(gconj(matrix.get((r, a), ZERO)),
PY|                 matrix.get((r, b), ZERO))
PY|            for r in rows
PY|        )
PY|        if value != (TWO if a == b else ZERO):
PY|            return False
PY|    return True
PY|
PY|
PY|def orthogonality_exponent_row(words, cut, p, q, r, s):
PY|    row_coordinates, column_coordinates = cut
PY|    need(project(p, row_coordinates) == project(q, row_coordinates),
PY|         "phase-first-actual-row")
PY|    need(project(r, row_coordinates) == project(s, row_coordinates),
PY|         "phase-second-actual-row")
PY|    need(project(p, row_coordinates) != project(r, row_coordinates),
PY|         "phase-distinct-actual-rows")
PY|    need(project(p, column_coordinates) == project(r, column_coordinates),
PY|         "phase-first-shared-column")
PY|    need(project(q, column_coordinates) == project(s, column_coordinates),
PY|         "phase-second-shared-column")
PY|    need(project(p, column_coordinates) != project(q, column_coordinates),
PY|         "phase-distinct-columns")
PY|    coefficients = Counter()
PY|    coefficients[p] += 1
PY|    coefficients[s] += 1
PY|    coefficients[r] -= 1
PY|    coefficients[q] -= 1
PY|    return tuple(coefficients[word] for word in words)
PY|
PY|
PY|def require_integer_certificate(rows, coefficients):
PY|    need(len(rows) == len(coefficients), "phase-certificate-length")
PY|    need(all(type(value) is int for value in coefficients),
PY|         "noninteger-phase-certificate")
PY|    residual = tuple(
PY|        sum(c * row[index] for c, row in zip(coefficients, rows))
PY|        for index in range(len(rows[0]))
PY|    )
PY|    need(all(value == 0 for value in residual), "integer-exponents")
PY|    need(sum(coefficients) % 2 == 1, "phase-sign-not-contradictory")
PY|
PY|
PY|def require_all_physical_cuts(flags):
PY|    need(len(flags) == 3 and all(flags), "missing-physical-cut")
PY|
PY|
PY|def check_complex_phases(stats):
PY|    words = tuple(
PY|        word for word in product((0, 1), repeat=4)
PY|        if sum(word) % 2 == 0
PY|    )
PY|    require_pair_multiplicity(words, 2)
PY|    for cut in CUTS:
PY|        need(block_count(words, cut) == 2, "phase-support-actual-cut")
PY|    a = (0, 0, 0, 0)
PY|    b = (0, 0, 1, 1)
PY|    c = (0, 1, 0, 1)
PY|    f = (1, 0, 1, 0)
PY|    g = (1, 1, 0, 0)
PY|    h = (1, 1, 1, 1)
PY|    rows = (
PY|        orthogonality_exponent_row(words, CUTS[0], a, b, g, h),
PY|        orthogonality_exponent_row(words, CUTS[1], a, c, f, h),
PY|        orthogonality_exponent_row(words, CUTS[2], b, c, f, g),
PY|    )
PY|    require_integer_certificate(rows, (1, -1, 1))
PY|    wrong_residual = tuple(sum(row[index] for row in rows)
PY|                           for index in range(len(words)))
PY|    need(any(value != 0 for value in wrong_residual),
PY|         "wrong-real-only-certificate-control")
PY|    need(all(value % 2 == 0 for value in wrong_residual),
PY|         "wrong-certificate-is-not-F2-only")
PY|    q = (Fraction(3, 5), Fraction(4, 5))
PY|    need(gnorm(q) == 1 and q[1] != 0, "nonreal-unit-phase")
PY|    one = (Fraction(1), Fraction(0))
PY|    minus_one = (Fraction(-1), Fraction(0))
PY|    amplitudes = {
PY|        word: q if word[0] == 0 else
PY|        (minus_one if word in (f, g) else one)
PY|        for word in words
PY|    }
PY|    need(all(gnorm(value) == 1 for value in amplitudes.values()),
PY|         "two-cut-control-unit-moduli")
PY|    flags = tuple(cut_is_scaled_unitary(amplitudes, cut) for cut in CUTS)
PY|    need(flags == (True, True, False),
PY|         "nonreal-two-cut-positive-and-third-cut-negative")
PY|    stats["complex_phase_integer_relations"] = len(rows)
PY|    stats["nonreal_scaled_unitary_control_cuts"] = sum(flags)
PY|    return rows, flags
PY|
PY|
PY|def check_no_low_low_graphs(profiles, stats):
PY|    ordinary_graphs = 0
PY|    profile_pairs = 0
PY|    for left in profiles:
PY|        for right in profiles:
PY|            tick()
PY|            profile_pairs += 1
PY|            row_options = tuple(
PY|                tuple(combinations(
PY|                    tuple(b for b in range(5)
PY|                          if not (left[a] == 2 and right[b] == 2)),
PY|                    left[a],
PY|                ))
PY|                for a in range(5)
PY|            )
PY|            valid = []
PY|            for rows in product(*row_options):
PY|                degrees = [0] * 5
PY|                for row in rows:
PY|                    for b in row:
PY|                        degrees[b] += 1
PY|                if tuple(degrees) == right:
PY|                    valid.append(frozenset(
PY|                        (a, b) for a, row in enumerate(rows) for b in row
PY|                    ))
PY|            ordinary = max(left) == 3 and max(right) == 3
PY|            need(bool(valid) == ordinary, "no-low-low-profile-feasibility")
PY|            if ordinary:
PY|                expected = frozenset(
PY|                    (a, b) for a in range(5) for b in range(5)
PY|                    if (left[a] == 2) != (right[b] == 2)
PY|                )
PY|                need(valid == [expected], "ordinary-graph-forced-cross-status")
PY|                ordinary_graphs += 1
PY|    zero_twin_statuses = tuple(
PY|        status for status in product((0, 1), repeat=4)
PY|        if all(status[i] != status[j] for i, j in PAIRS)
PY|    )
PY|    need(not zero_twin_statuses, "zero-twin-four-status-obstruction")
PY|    required_words = 3 * (2 * 2)
PY|    capacities = tuple(product(range(3), repeat=4))
PY|    need(required_words == 12, "one-twin-low-word-count")
PY|    need(max(map(sum, capacities)) == 8, "one-twin-pair-capacity")
PY|    need(all(sum(values) < required_words for values in capacities),
PY|         "one-twin-capacity-contradiction")
PY|    stats["no_low_low_ordered_profile_pairs"] = profile_pairs
PY|    stats["ordinary_no_low_low_graphs"] = ordinary_graphs
PY|    stats["one_twin_pair_occupancy_vectors"] = len(capacities)
PY|
PY|
PY|def remap_word(word, coordinate_order):
PY|    result = [None] * 4
PY|    for source, target in enumerate(coordinate_order):
PY|        result[target] = word[source]
PY|    return tuple(result)
PY|
PY|
PY|def check_component_alphabets_and_common_p(stats):
PY|    alphabet = frozenset(range(5))
PY|    subsets = tuple(frozenset(values)
PY|                    for values in combinations(range(5), 3))
PY|    choices = tuple(
PY|        (a, b) for a, b in product(subsets, repeat=2)
PY|        if a | b == alphabet and len(a & b) == 1
PY|    )
PY|    need(len(choices) == 30, "ordered-component-alphabet-pair-count")
PY|    base_cases = 0
PY|    physical_cases = 0
PY|    forced_word_labels = 0
PY|    first_words = None
PY|    for (ki, kj), (li, lj) in product(choices, repeat=2):
PY|        tick()
PY|        base_cases += 1
PY|        for bi, bj in ((ki, kj), (li, lj)):
PY|            degrees = tuple(
PY|                2 * (int(value in bi) + int(value in bj))
PY|                for value in range(5)
PY|            )
PY|            need(tuple(sorted(degrees)) == (2, 2, 2, 2, 4),
PY|                 "two-components-force-exceptional-party")
PY|        forced = []
PY|        for a, b in product((0, 1), repeat=2):
PY|            allowed = tuple(
PY|                (a, b, c, d)
PY|                for c, d in product(range(6), repeat=2)
PY|                if c not in ki and c not in kj and
PY|                d not in li and d not in lj
PY|            )
PY|            need(allowed == ((a, b, 5, 5),),
PY|                 "same-P-forced-outside-completion")
PY|            forced.append(allowed[0])
PY|        forced = tuple(forced)
PY|        if first_words is None:
PY|            first_words = forced
PY|        for twins in PAIRS:
PY|            remaining = tuple(i for i in range(4) if i not in twins)
PY|            coordinate_order = twins + remaining
PY|            words = tuple(remap_word(word, coordinate_order)
PY|                          for word in forced)
PY|            require_bound_claims(words, actual_claims(words))
PY|            counters = pair_counters(words)
PY|            need(len(counters[twins]) == 4,
PY|                 "four-distinct-maximal-high-pair-labels")
PY|            need(counters[remaining] == Counter({(5, 5): 4}),
PY|                 "same-complementary-outside-pair-collision")
PY|            need(all(pair in counters for pair in PAIRS),
PY|                 "missing-physical-pair-consumer")
PY|            physical_cases += 1
PY|            forced_word_labels += len(words)
PY|    need(base_cases == 900, "two-remaining-coordinate-alphabet-count")
PY|    need(physical_cases == 5400, "all-physical-twin-role-count")
PY|    stats["ordered_component_alphabet_pairs"] = len(choices)
PY|    stats["two_coordinate_alphabet_configurations"] = base_cases
PY|    stats["physical_twin_role_configurations"] = physical_cases
PY|    stats["forced_local_maximal_word_labels"] = forced_word_labels
PY|    return first_words
PY|
PY|
PY|def require_disjoint_components(left, right):
PY|    need(not (set(left) & set(right)), "component-overlap")
PY|
PY|
PY|def expect_rejection(results, name, reason, operation):
PY|    try:
PY|        operation()
PY|    except CheckFailure as failure:
PY|        need(failure.reason == reason,
PY|             "wrong-control-reason:" + name + ":" + failure.reason)
PY|        results.append(name)
PY|        return
PY|    raise CheckFailure("control-not-rejected:" + name)
PY|
PY|
PY|def check_negative_controls(triples, pool, rows, flags, forced_words):
PY|    results = []
PY|    expect_rejection(
PY|        results, "reused-colour-edge", "matching-edge-repeat",
PY|        lambda: require_colours((pool[0], pool[0], pool[0]), 6),
PY|    )
PY|    expect_rejection(
PY|        results, "six-triple-slice-pretends-eight", "slice-duplicate",
PY|        lambda: require_slice(
PY|            triples + ((3, 3, 3), (3, 3, 3)), 4
PY|        ),
PY|    )
PY|    expect_rejection(
PY|        results, "eight-overlap-two-degree-four-symbols", "two-degree4-slices",
PY|        lambda: require_distinct_slice_demands((4, 2, 2, 2, 2), (4, 4)),
PY|    )
PY|    expect_rejection(
PY|        results, "F2-only-real-sign-certificate", "integer-exponents",
PY|        lambda: require_integer_certificate(rows, (1, 1, 1)),
PY|    )
PY|    expect_rejection(
PY|        results, "drop-third-physical-cut", "missing-physical-cut",
PY|        lambda: require_all_physical_cuts(flags),
PY|    )
PY|    left = place_component(triples, 0)
PY|    right = place_component(triples, 1)
PY|    need(bool(set(left) & set(right)), "overlap-control-not-overlapping")
PY|    expect_rejection(
PY|        results, "allow-overlapping-local-components", "component-overlap",
PY|        lambda: require_disjoint_components(left, right),
PY|    )
PY|    claims = actual_claims(forced_words)
PY|    require_bound_claims(forced_words, claims)
PY|    independent_claims = dict(claims)
PY|    independent_claims[(2, 3)] = tuple(product((0, 1), repeat=2))
PY|    need(len(set(independent_claims[(2, 3)])) == 4,
PY|         "independent-projection-control-not-injective")
PY|    expect_rejection(
PY|        results, "independent-P-per-cut-evasion", "same-word-projection",
PY|        lambda: require_bound_claims(forced_words, independent_claims),
PY|    )
PY|    expect_rejection(
PY|        results, "drop-maximal-pair-injectivity", "maximal-pair-collision",
PY|        lambda: require_injective_pair(forced_words, (2, 3)),
PY|    )
PY|    need(len(results) == 8, "intended-reason-control-count")
PY|    return tuple(results)
PY|
PY|
PY|def main():
PY|    global DEADLINE
PY|    started = monotonic()
PY|    DEADLINE = started + 55.0
PY|    need(len(sys.argv) == 1, "unexpected-command-line-arguments")
PY|    stats = {}
PY|    profiles = check_degrees_and_moments(stats)
PY|    triples, pool = check_common_twins(profiles, stats)
PY|    check_low_slices(stats)
PY|    rows, flags = check_complex_phases(stats)
PY|    check_no_low_low_graphs(profiles, stats)
PY|    forced_words = check_component_alphabets_and_common_p(stats)
PY|    controls = check_negative_controls(
PY|        triples, pool, rows, flags, forced_words
PY|    )
PY|    tick()
PY|    print("RESULT: PASS_EXACT_LOCAL_INTERFACES_ONLY")
PY|    for key in sorted(stats):
PY|        print(key + " = " + str(stats[key]))
PY|    print("intended_reason_controls = " + str(len(controls)))
PY|    for name in controls:
PY|        print("CONTROL_REJECTED_FOR_INTENDED_REASON: " + name)
PY|    print("NOT_AN_AME_CERTIFICATE: no complete global E/P/U was constructed")
PY|    print("NOT_TESTED: actual global tensor mutants for these controls")
PY|    print("NOT_ENUMERATED: global supports, continuous moduli or phases")
PY|    print("COMPLEX_SCOPE: integer exponent identity plus written normalization")
PY|    print("SAME_P_SCOPE: four forced words only, not a full maximal support")
PY|    print("NO_CLAIM: other profiles, all t24, all support48, minimum or novelty")
PY|    print("elapsed_seconds = " + format(monotonic() - started, ".6f"))
PY|    return 0
PY|
PY|
PY|if __name__ == "__main__":
PY|    try:
PY|        status = main()
PY|    except CheckFailure as failure:
PY|        print("RESULT: INCOMPLETE_OR_FAILED")
PY|        print("reason = " + failure.reason)
PY|        status = 1
PY|    sys.exit(status)

## 5. Disposition and limits

The full frozen fixed-\(5555\) argument survives this independent static reconstruction. I found no missing consumer branch between the twin lemma, low-low routing, component count, alphabet union, and same-\(P\) completion contradiction.

The executable above has **not** been run, syntax-checked, timed, or hashed by me. Its possible successful output is not evidence until actually obtained. Materialization, source pinning, any authorized parent execution, the other written gates, and parent adoption remain separate actions.

No conclusion here excludes \(4555\), establishes unconditional profile completeness, rules out every \(t=24\) or support-\(48\) tensor, proves \(N\ge49\), determines the AME minimum, or establishes novelty. This is same-harness work, not independent-family, human, or kernel verification.

**Overall correctness:** correct — for the frozen candidate’s written fixed-\(5555\) theorem only.

**Explanation:** The proof consistently uses the same actual \(U,E,P\), all six pair projections, and all three complex orthogonality cuts. The FINITE execution gate remains unfulfilled because execution was prohibited in this role; the complete independent source is supplied without a fabricated run.

**Confidence:** 0.96.