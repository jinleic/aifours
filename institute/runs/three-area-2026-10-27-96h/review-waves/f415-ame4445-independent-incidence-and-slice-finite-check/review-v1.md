overall_correctness: correct

explanation: The finite combinatorial obstruction is valid by the independent written reconstruction below. Scientific execution is **NOTRUN** under this role’s read-only execution restrictions; the complete checker is supplied without claiming an executed gate, adoption, or a broader AME exclusion.

confidence: 0.97

# author-candidate-v1.md

## F415 — Independent incidence and slice finite gate

**Status:** COMPLETE WRITTEN FINITE-QUOTIENT RECONSTRUCTION; CHECKER NOTRUN; UNREVIEWED; NOT ADOPTED.

**Result:** The combinatorial quotient specified in this wave has no solutions. This conclusion follows from the written argument below, independently of the proposed enumeration. All enumeration totals below are **written-derived expectations, not observed program output**.

**Materialization:** No file was written. This response contains the complete manuscript and complete checker for parent materialization.

## 1. Bindings, reading, and execution status

Assigned wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f415-ame4445-independent-incidence-and-slice-finite-check/`

Bindings supplied by the assignment and parent metadata:

| Artifact | SHA-256 |
|---|---|
| Manifest | `72479f6c28b90ab3cb6fdefa5eac824aab935ca9978ff13c0f123040c4daa454` |
| Freeze receipt | `8b9baf7ff355f0a8f9eb656f88ceec0de632ee58be490b3200ecadb4c58dc87c` |
| Literal packet | `49b26766e4bb68d655ee8cdf23897cb47343c0ff36dd3443b95f32c2bd3abc49` |
| S1, complete f403 author manuscript | `9b34af34d7849c3911e6e77f9043a933dfaf1a69e421d4823bfa61e4f2b5a479` |

These hashes were **not independently computed by this child**. Their live-observation attribution is the parent’s `parent-live-metadata-supply-v1.json`, carrying the observation `2026-10-30T10:53:31-0700 PDT`. That observation is not my native start, derivation, or completion time.

Actual chronology:

1. Read the required memory summary and relevant verification/protocol skills.
2. Read the wave directory, complete manifest, and freeze receipt. The manifest’s initially truncated research-task line was subsequently read in full using raw mode.
3. Read all seven named permission/status controls in full, followed by parent metadata and dispatch receipt.
4. Read the complete ordered literal packet, packet lines **1–483**, in contiguous raw windows of at most twenty lines, including S1’s final status at logical line 481.
5. Independently reconstructed the quotient, derived the counts below, constructed controls, and authored the checker.
6. Read the independent-snapshot-review skill. No external-model review was launched.

No held scientific payload, held consumer, outside sibling outcome, or author checker code was opened or used. The controls were status/permission inputs only. No public source was opened; no novelty inference is made.

**Execution:** No interpreter, solver, scientific executable, shell calculation, build, test, formatter, or external-model CLI was run. The higher-priority role restricts shell use to read-only review commands and prohibits file edits; the wave expressly permits **NOTRUN** in that situation. No alternate execution device or file-write bypass was attempted.

Therefore there are no observed elapsed-time measurements, RSS measurements, execution outputs, or checker-file hashes to report.

## 2. Exact caller and finite quantifiers

The actual caller in S1 is:

- \(U=6\psi\), where \(\psi\in(\mathbb C^6)^{\otimes4}\) is normalized;
- all three balanced flattenings of \(U\) are unitary;
- exactly 48 tensor entries are nonzero;
- exactly 24 entries have modulus one;
- \(P\) is that set of 24 modulus-one words;
- \(E\) is the set of the other 24 nonzero words;
- the residual coordinate alphabets have sizes \(4,4,4,5\), after one party permutation;
- amplitudes may be arbitrary complex numbers.

The **finite program does not take a tensor as input**. Its exact necessary quotient is:

1. Three disjoint four-element sets \(A_1,A_2,A_3\).
2. A perfect matching \(M_{ij}\) between each pair of these sets.
3. A subset
   \[
   T\subset M_{12}\cup M_{13}\cup M_{23}
   \]
   that is a perfect matching on all twelve vertices, with exactly two edges in each party pair.
4. For a selected low symbol, a two-edge subset \(C\subset T\).
5. Independently chosen two-subsets \(N_i\subset A_i\), with \(S_i=A_i\setminus N_i\).
6. Both endpoints of every edge of \(C\) belong to the corresponding \(S\)-sets.
7. At most one party pair \(ij\) has
   \[
   M_{ij}\cap(S_i\times S_j)\ne\varnothing.
   \]

The finite statement is:

> For every matching system, every such global \(T\), every two-edge choice \(C\), and every triple of two-subsets \(N_i\), conditions 1–7 are inconsistent.

The checker also enumerates all assignments of the six \(T\)-edges to **three labeled low symbols**, with two edges per symbol. It uses the proven single-color impossibility rather than enumerating an unnecessary Cartesian product of all three colors’ \(N\)-choices.

The missing high-symbol incidences, external symbols, full maximal-word packing, amplitudes, and tensor entries are **not** declared sufficient or reconstructed by the program. Omitting those extra constraints enlarges the feasible set; proving even this enlarged quotient empty is the relevant necessary-condition obstruction.

## 3. Four labeled words: complete partition classification

Label the four word positions \(0,1,2,3\). At one binary coordinate, balance requires a \(2+2\) partition. The three unordered partitions are

\[
01|23,\qquad 02|13,\qquad 03|12.
\]

Each partition has two choices of which block receives binary symbol zero.

Consequently:

- unordered partition triples: \(3^3=27\);
- oriented, labeled binary arrays: \(27\cdot2^3=216\).

The cases are exhaustive:

| Coordinate-partition pattern | Unordered triples | Oriented arrays | Distinct words? | Nonfull coordinate pairs |
|---|---:|---:|---|---:|
| Three distinct | 6 | 48 | Yes | 0 |
| Exactly two equal | 18 | 144 | Yes | 1 |
| All three equal | 3 | 24 | No | 3 |

For distinct partitions, every intersection of their two blocks has size one, giving all four binary coordinate-pair values. For equal partitions, only two coordinate-pair values occur.

If all three partitions coincide, the two members of each partition block have the same three-coordinate word. Thus that case produces duplicates, despite preserving coordinate balance.

It follows that all **192 distinct-word oriented arrays** have at most one nonfull pair projection. In particular, the exactly-two-equal case is retained; no no-distance-one assumption has been inserted.

## 4. Complete global gauge, rather than independent pair gauges

Start with arbitrary bijections defining the three matchings.

Choose labels on \(A_1\). Label the \(M_{12}\)-partner of \(a\in A_1\) by the same label in \(A_2\), and label its \(M_{13}\)-partner by the same label in \(A_3\). These are simultaneous relabelings of the **three vertex sets**, giving

\[
M_{12}=\{(a,a):a\in[4]\},\qquad
M_{13}=\{(a,a):a\in[4]\}.
\]

The remaining matching is

\[
M_{23}=\{(a,\sigma(a)):a\in[4]\}
\]

for one permutation \(\sigma\in S_4\).

Thus all 24 permutations are a complete gauge-covered list. A remaining simultaneous relabeling conjugates \(\sigma\); the checker deliberately keeps all 24 instead of choosing conjugacy representatives. It never separately normalizes all three pair matchings.

All \(T\)-edges, low-symbol colors, and \(N_i\) are transported by the same vertex relabelings. Therefore this reduction does not lose a configuration.

## 5. Alternating components and exact matching counts

The union of the three pair matchings is a degree-two graph. A cycle of length \(r\) in \(\sigma\) produces a graph cycle of length \(3r\).

The complete list is:

| Cycle type of \(\sigma\) | Permutations | Graph components | Admissible \(T\) per system |
|---|---:|---|---:|
| \(1+1+1+1\) | 1 | \(C_3^4\) | 0 |
| \(2+1+1\) | 6 | \(C_6\sqcup C_3^2\) | 0 |
| \(2+2\) | 3 | \(C_6\sqcup C_6\) | 4 |
| \(3+1\) | 8 | \(C_9\sqcup C_3\) | 0 |
| \(4\) | 6 | \(C_{12}\) | 2 |

An odd cycle has no perfect matching. Each even cycle has exactly two alternating perfect matchings. In a \(C_6\), either alternating choice uses one edge of each party pair; in a \(C_{12}\), it uses two of each. Hence all these perfect matchings satisfy the required pair counts.

Totals:

- 24 gauge-covered systems;
- 9 systems admitting \(T\);
- 24 admissible \((M,T)\) records;
- 12 records on \(C_6\sqcup C_6\);
- 12 records on \(C_{12}\).

The independent enumeration checks all

\[
24\binom42^3=5,184
\]

choices taking two edges from each pair matching, and retains exactly the globally degree-one \(T\)'s. This explicitly checks the common-incidence requirement rather than merely checking three independent pair matchings.

## 6. Single-color impossibility: independent double-cover argument

Let \(C\) be the two \(T\)-edges carrying one low-symbol color.

If its edges lie in two different party pairs, endpoint membership immediately gives \(S\)-to-\(S\) matching edges in two pairs, violating condition 7.

It remains to consider both edges in the same pair, say \(12\). Since \(T\) has exactly two edges in that pair, \(C=T_{12}\). Their endpoints exhaust \(S_1,S_2\).

Because \(T\) is a perfect matching:

- the two edges of \(T_{13}\) exhaust \(N_1\);
- the two edges of \(T_{23}\) exhaust \(N_2\).

The pair \(12\) already has \(S\)-to-\(S\) edges. Condition 7 therefore requires both \(M_{13}\) and \(M_{23}\) to have no \(S\)-to-\(S\) edges.

For a perfect matching between two sets partitioned into equal halves, no \(S\)-to-\(S\) edges means that it maps the first \(S\)-half onto the other \(N\)-half, and the first \(N\)-half onto the other \(S\)-half.

It follows that:

- \(T_{13}\), whose party-1 endpoints exhaust \(N_1\), exhausts \(S_3\);
- \(T_{23}\), whose party-2 endpoints exhaust \(N_2\), also exhausts \(S_3\).

That gives every vertex of \(S_3\) two incident \(T\)-edges, contradicting the global degree-one requirement.

This proves the finite quotient empty without an executable and without assuming either allowed alternating component type sufficient for a common \(P\).

## 7. Why the slice supplies condition 7

For a low symbol \(\ell\), the actual residual slice contains four distinct words. Each of its three coordinates uses two symbols twice. Section 3 therefore gives at most one nonfull coordinate-pair projection.

For any perfect matching \(M_{ij}\) and two-subsets \(N_i,N_j\), direct matching balance gives

\[
|M_{ij}\cap(N_i\times N_j)|
=
|M_{ij}\cap(S_i\times S_j)|.
\]

Indeed, if the first count is \(x\), the two cross-quadrant counts are both \(2-x\), leaving \(x\) in the other diagonal quadrant.

If the actual slice projection onto \(ij\) is full, every member of \(N_i\times N_j\) is residual, so none can belong to the missing matching. The displayed equality then excludes \(S_i\)-to-\(S_j\) matching edges.

The program directly checks the quadrant-count equality for every enumerated \(N\)-triple. It does **not** assume that an arbitrary quotient candidate has a materializable residual slice.

## 8. Enumeration totals and labeled-color coverage

These are written-derived expected totals.

For each admissible \((M,T)\), there are \(\binom62=15\) choices of one color’s two edges:

- 3 same-pair choices;
- 12 split-pair choices.

There are \(6^3=216\) triples of two-subsets \(N_i\). Therefore the independent local enumeration contains

\[
24\cdot15\cdot216=77,760
\]

tests.

Endpoint membership leaves:

- same-pair color: \(6\) choices, because \(S_i,S_j\) are forced and the remaining \(S_k\) is arbitrary;
- split-pair color: \(9\) choices, because the shared party’s \(S\)-set is forced and each other \(S\)-set has three choices.

Thus:

| Stage | Expected count |
|---|---:|
| Two-edge color choices | 360 |
| Local \(C,N\) tests | 77,760 |
| Same-pair tests before endpoint filtering | 15,552 |
| Split-pair tests before endpoint filtering | 62,208 |
| Direct quadrant-equality checks | 233,280 |
| Endpoint-consistent local cases | 3,024 |
| Same-pair endpoint-consistent cases | 432 |
| Split-pair endpoint-consistent cases | 2,592 |
| Same-pair cases rejected by slice shadow | 432 |
| Split-pair cases rejected by slice shadow | 2,592 |
| Survivors | 0 |

For three **labeled** low symbols, each appearing twice, there are

\[
\binom62\binom42=90
\]

colorings per \((M,T)\), or 2,160 overall.

Their incidence families have counts:

| Family | Per \((M,T)\) | Overall |
|---|---:|---:|
| Three concentrated rows | 6 | 144 |
| One concentrated row | 36 | 864 |
| No concentrated row | 48 | 1,152 |

Every particular two-edge subset appears as one color in exactly \(3\cdot6=18\) of the 90 colorings. The checker verifies that coverage explicitly.

No coloring has even independently selectable local options for all its colors: every local option count is zero. No cross-color Cartesian enumeration or full-tensor support enumeration is needed.

## 9. Genuine controls and their intended failure reasons

Write \(A_a,B_a,C_a\) for vertices in the three parties.

### Positive weak matching system

Take

\[
M_{12}=M_{13}=\mathrm{id},\qquad
\sigma=(1,0,3,2),
\]

and

\[
T=\{
A_0B_0,\ A_2B_2,\
A_1C_1,\ A_3C_3,\
B_1C_0,\ B_3C_2
\}.
\]

This is an actual perfect matching on all twelve vertices, has two edges per party pair, is contained in the actual union of the three matchings, and has a complementary perfect matching \(F\). The checker accepts these weak matching conditions. It is not claimed to extend to a common maximal-word packing or tensor.

### Positive actual four-word slice

Use instead \(\sigma=(2,3,0,1)\), and

\[
N_1=N_2=\{1,3\},\qquad N_3=\{0,2\}.
\]

The four actual words

\[
(1,3,0),\ (1,3,2),\ (3,1,0),\ (3,1,2)
\]

are distinct, balanced at each coordinate, avoid all three missing matchings, and have exactly one nonfull pair projection. This is a genuine positive slice control, not an assertion that the slice and a selected triple color extend to the impossible full quotient.

### Negative: balanced duplicate words

The words

\[
(0,0,0),\ (0,0,0),\ (1,1,1),\ (1,1,1)
\]

preserve coordinate balance but violate distinctness. Expected rejection: **DUPLICATE_WORDS**.

### Negative: omitted slice-shadow condition

Use the positive weak \(M,T\), select \(C=\{A_0B_0,A_2B_2\}\), and take all three \(N_i=\{1,3\}\).

All individual matchings, global \(T/F\) incidence, color size, subset balance, and color-endpoint conditions hold. The \(S\)-to-\(S\) counts are \((2,2,0)\). Expected rejection: **SLICE_SHADOW**.

### Negative: omitted shared incidence

Keep that same \(T,C\), replace \(\sigma\) by \((2,3,0,1)\), and use the positive-slice \(N\)-sets above.

Every pair matching remains perfect; \(T\) remains an abstract degree-one matching with two edges per pair; subset balance, color endpoints, actual slice, and slice shadow all hold. But the two \(T_{23}\)-edges are no longer edges of the actual \(M_{23}\). Expected rejection: **T_SHARED_INCIDENCE**.

“Only” here refers to the explicitly checked quotient interfaces, not to unmodeled full-tensor conditions. Negative controls count only when the named invariant-specific exception occurs; an arbitrary exception is not accepted.

## 10. Complete standalone checker — NOTRUN

Intended invocation after parent materialization:

`python3 -B f415_independent_finite_v1.py`

No arguments or input files are required. The generated permutations, labeled partitions, subsets, and explicit control objects are its complete inputs. It uses the standard library, no file/network/subprocess operations, no randomness, and no scientific assertions that disappear under optimization.

The guard checks elapsed time against 55 seconds and observed peak RSS against 128 MiB. It is a cooperative guard, not an OS-enforced resource reservation. A guard failure gives INCOMPLETE, not a negative mathematical result.

The following plain-text source between the markers is the complete code.

BEGIN FILE f415_independent_finite_v1.py

from collections import Counter
from itertools import combinations, permutations, product
import resource
import sys
import time


class CheckError(Exception):
    pass


START = time.monotonic()
TIME_LIMIT = 55.0
RSS_LIMIT = 128 * 1024 * 1024
PAIRS = ((0, 1), (0, 2), (1, 2))
VERTICES = tuple((i, a) for i in range(3) for a in range(4))
ONE_EACH = Counter({v: 1 for v in VERTICES})
UNIVERSE = frozenset(range(4))


def require(condition, reason):
    if not condition:
        raise CheckError(reason)


def peak_rss_bytes():
    require(sys.platform in ("darwin", "linux"), "UNSUPPORTED_RSS_UNITS")
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def guard():
    if time.monotonic() - START >= TIME_LIMIT:
        raise CheckError("BUDGET_TIME")
    if peak_rss_bytes() > RSS_LIMIT:
        raise CheckError("BUDGET_RSS")


def edge(i, a, j, b):
    return tuple(sorted(((i, a), (j, b))))


def edge_pair(e):
    return (e[0][0], e[1][0])


def make_system(sigma):
    return (
        frozenset(edge(0, a, 1, a) for a in range(4)),
        frozenset(edge(0, a, 2, a) for a in range(4)),
        frozenset(edge(1, a, 2, sigma[a]) for a in range(4)),
    )


def union_edges(system):
    return frozenset(e for matching in system for e in matching)


def check_system(system):
    require(len(system) == 3, "SYSTEM_SIZE")
    for pair, matching in zip(PAIRS, system):
        require(len(matching) == 4, "PAIR_MATCHING_SIZE")
        require(
            all(edge_pair(e) == pair for e in matching),
            "PAIR_MATCHING_PARTIES",
        )
        expected = Counter(
            {(i, a): 1 for i in pair for a in range(4)}
        )
        observed = Counter(v for e in matching for v in e)
        require(observed == expected, "PAIR_MATCHING_DEGREE")


def check_t_shape(t):
    require(len(t) == 6, "T_SIZE")
    require(
        Counter(v for e in t for v in e) == ONE_EACH,
        "T_DEGREE",
    )
    require(
        Counter(edge_pair(e) for e in t)
        == Counter({pair: 2 for pair in PAIRS}),
        "T_PAIR_COUNT",
    )


def check_shared_incidence(system, t):
    whole = union_edges(system)
    require(t <= whole, "T_SHARED_INCIDENCE")
    f = whole - t
    require(len(f) == 6, "F_SIZE")
    require(
        Counter(v for e in f for v in e) == ONE_EACH,
        "F_DEGREE",
    )


def complements(n_sets):
    require(
        len(n_sets) == 3
        and all(len(n) == 2 and n <= UNIVERSE for n in n_sets),
        "N_BALANCE",
    )
    return tuple(UNIVERSE - n for n in n_sets)


def endpoint_ok(color, s_sets):
    return all(
        all(a in s_sets[i] for i, a in e)
        for e in color
    )


def quadrant_counts(system, sets):
    return tuple(
        sum(all(a in sets[i] for i, a in e) for e in matching)
        for matching in system
    )


def shadow_ok(counts):
    return sum(value > 0 for value in counts) <= 1


def check_local(system, t, color, n_sets):
    check_system(system)
    check_t_shape(t)
    require(len(color) == 2 and color <= t, "COLOR")
    s_sets = complements(n_sets)
    require(endpoint_ok(color, s_sets), "COLOR_ENDPOINTS")
    require(
        shadow_ok(quadrant_counts(system, s_sets)),
        "SLICE_SHADOW",
    )
    check_shared_incidence(system, t)


def check_binary_rows(rows):
    require(
        len(rows) == 4 and all(len(row) == 3 for row in rows),
        "BINARY_SHAPE",
    )
    require(
        all(value in (0, 1) for row in rows for value in row),
        "BINARY_ALPHABET",
    )
    require(
        all(sum(row[i] for row in rows) == 2 for i in range(3)),
        "BINARY_BALANCE",
    )
    require(len(set(rows)) == 4, "DUPLICATE_WORDS")
    return sum(
        len({(row[i], row[j]) for row in rows}) < 4
        for i, j in PAIRS
    )


def check_actual_slice(system, n_sets, rows):
    complements(n_sets)
    require(
        len(rows) == 4 and all(len(row) == 3 for row in rows),
        "SLICE_SHAPE",
    )
    require(len(set(rows)) == 4, "SLICE_DUPLICATES")
    for i in range(3):
        expected = Counter({a: 2 for a in n_sets[i]})
        require(
            Counter(row[i] for row in rows) == expected,
            "SLICE_BALANCE",
        )
    sizes = []
    for (i, j), matching in zip(PAIRS, system):
        projection = {(row[i], row[j]) for row in rows}
        require(
            all(edge(i, a, j, b) not in matching for a, b in projection),
            "SLICE_FORBIDDEN_PAIR",
        )
        sizes.append(len(projection))
    nonfull = sum(size < 4 for size in sizes)
    require(nonfull <= 1, "SLICE_PARTITION_LEMMA")
    return nonfull


def component_signature(system):
    adjacency = {v: set() for v in VERTICES}
    for e in union_edges(system):
        a, b = e
        adjacency[a].add(b)
        adjacency[b].add(a)
    require(
        all(len(adjacency[v]) == 2 for v in VERTICES),
        "UNION_DEGREE",
    )
    seen = set()
    sizes = []
    for start in VERTICES:
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        size = 0
        while stack:
            v = stack.pop()
            size += 1
            for w in adjacency[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        sizes.append(size)
    return tuple(sorted(sizes))


def expect_error(label, reason, operation):
    try:
        operation()
    except CheckError as exc:
        require(str(exc) == reason, "WRONG_CONTROL_REASON_" + label)
        return label
    raise CheckError("CONTROL_ACCEPTED_" + label)


def partition_checks():
    bases = (
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (0, 1, 1, 0),
    )
    categories = {
        1: "all_equal",
        2: "exactly_two_equal",
        3: "all_distinct",
    }
    partitions = Counter()
    orientations = Counter()
    valid_nonfull = Counter()
    duplicates = 0

    for choices in product(range(3), repeat=3):
        guard()
        category = categories[len(set(choices))]
        partitions[category] += 1
        for flips in product(range(2), repeat=3):
            rows = tuple(
                tuple(
                    bases[choices[i]][r] ^ flips[i]
                    for i in range(3)
                )
                for r in range(4)
            )
            orientations[category] += 1
            require(
                all(sum(row[i] for row in rows) == 2 for i in range(3)),
                "GENERATED_BINARY_BALANCE",
            )
            sizes = tuple(
                len({(row[i], row[j]) for row in rows})
                for i, j in PAIRS
            )
            expected_sizes = tuple(
                2 if choices[i] == choices[j] else 4
                for i, j in PAIRS
            )
            require(sizes == expected_sizes, "PARTITION_INTERSECTION")
            if len(set(choices)) == 1:
                require(len(set(rows)) == 2, "ALL_EQUAL_DUPLICATION")
                duplicates += 1
            else:
                nonfull = check_binary_rows(rows)
                require(nonfull <= 1, "FOUR_WORD_LEMMA")
                valid_nonfull[nonfull] += 1

    require(
        partitions == Counter({
            "all_equal": 3,
            "exactly_two_equal": 18,
            "all_distinct": 6,
        }),
        "PARTITION_TOTALS",
    )
    require(
        orientations == Counter({
            "all_equal": 24,
            "exactly_two_equal": 144,
            "all_distinct": 48,
        }),
        "ORIENTATION_TOTALS",
    )
    require(valid_nonfull == Counter({0: 48, 1: 144}), "VALID_WORD_TOTALS")
    require(duplicates == 24, "DUPLICATE_TOTAL")
    return partitions, orientations, valid_nonfull, duplicates


def matching_records():
    graphs = Counter()
    t_count_distribution = Counter()
    records_by_graph = Counter()
    records = []
    t_candidates = 0

    for sigma in permutations(range(4)):
        guard()
        system = make_system(sigma)
        check_system(system)
        signature = component_signature(system)
        graphs[signature] += 1
        choices = [
            tuple(combinations(sorted(matching), 2))
            for matching in system
        ]
        accepted_here = 0
        for groups in product(*choices):
            guard()
            t_candidates += 1
            t = frozenset(e for group in groups for e in group)
            if Counter(v for e in t for v in e) != ONE_EACH:
                continue
            check_t_shape(t)
            check_shared_incidence(system, t)
            accepted_here += 1
            records.append((system, t))
            records_by_graph[signature] += 1
        t_count_distribution[accepted_here] += 1

    require(
        graphs == Counter({
            (3, 3, 3, 3): 1,
            (3, 3, 6): 6,
            (6, 6): 3,
            (3, 9): 8,
            (12,): 6,
        }),
        "GRAPH_CLASSIFICATION",
    )
    require(t_candidates == 5184, "T_CANDIDATE_TOTAL")
    require(
        t_count_distribution == Counter({0: 15, 2: 6, 4: 3}),
        "T_COUNT_DISTRIBUTION",
    )
    require(len(records) == 24, "T_RECORD_TOTAL")
    require(
        records_by_graph == Counter({(6, 6): 12, (12,): 12}),
        "ALTERNATING_COMPONENT_TOTALS",
    )
    return graphs, t_count_distribution, records_by_graph, records, t_candidates


def local_and_coloring_checks(records):
    two_subsets = tuple(
        frozenset(values) for values in combinations(range(4), 2)
    )
    n_triples = tuple(product(two_subsets, repeat=3))
    require(len(n_triples) == 216, "N_TRIPLE_TOTAL")
    totals = Counter()
    color_families = Counter()
    colorings = 0
    colorings_with_local_options = 0

    for system, t in records:
        ordered = tuple(sorted(t))
        option_counts = {}
        for selected in combinations(ordered, 2):
            guard()
            color = frozenset(selected)
            totals["color_choices"] += 1
            same_pair = edge_pair(selected[0]) == edge_pair(selected[1])
            key = "same" if same_pair else "split"
            options = 0
            for n_sets in n_triples:
                guard()
                totals["tested"] += 1
                totals[key + "_tested"] += 1
                s_sets = complements(n_sets)
                nn = quadrant_counts(system, n_sets)
                ss = quadrant_counts(system, s_sets)
                require(nn == ss, "MATCHING_QUADRANT_IDENTITY")
                totals["identity_checks"] += 3
                if not endpoint_ok(color, s_sets):
                    continue
                totals["endpoint_pass"] += 1
                totals[key + "_endpoint"] += 1
                if shadow_ok(ss):
                    options += 1
                    totals["slice_shadow_survivors"] += 1
                else:
                    totals[key + "_shadow_rejected"] += 1
            option_counts[color] = options

        coverage = Counter()
        for first in combinations(range(6), 2):
            remaining = tuple(i for i in range(6) if i not in first)
            for second in combinations(remaining, 2):
                guard()
                third = tuple(i for i in remaining if i not in second)
                groups = (first, second, third)
                colors = tuple(
                    frozenset(ordered[i] for i in group)
                    for group in groups
                )
                require(
                    frozenset().union(*colors) == t
                    and sum(len(c) for c in colors) == 6,
                    "COLOR_PARTITION",
                )
                matrix = tuple(
                    tuple(
                        sum(edge_pair(e) == pair for e in color)
                        for pair in PAIRS
                    )
                    for color in colors
                )
                require(
                    all(sum(row) == 2 for row in matrix)
                    and all(
                        sum(matrix[r][c] for r in range(3)) == 2
                        for c in range(3)
                    ),
                    "COLOR_INCIDENCE_BALANCE",
                )
                concentrated = sum(2 in row for row in matrix)
                require(concentrated in (0, 1, 3), "COLOR_FAMILY")
                color_families[concentrated] += 1
                coverage.update(colors)
                colorings += 1
                if all(option_counts[color] > 0 for color in colors):
                    colorings_with_local_options += 1
        require(
            set(coverage) == set(option_counts)
            and all(value == 18 for value in coverage.values()),
            "LABELED_COLOR_COVERAGE",
        )

    expected = {
        "color_choices": 360,
        "tested": 77760,
        "same_tested": 15552,
        "split_tested": 62208,
        "identity_checks": 233280,
        "endpoint_pass": 3024,
        "same_endpoint": 432,
        "split_endpoint": 2592,
        "slice_shadow_survivors": 0,
        "same_shadow_rejected": 432,
        "split_shadow_rejected": 2592,
    }
    require(totals == Counter(expected), "LOCAL_ENUMERATION_TOTALS")
    require(colorings == 2160, "LABELED_COLORING_TOTAL")
    require(
        color_families == Counter({3: 144, 1: 864, 0: 1152}),
        "COLOR_FAMILY_TOTALS",
    )
    require(
        colorings_with_local_options == 0,
        "GLOBAL_COLORING_SURVIVOR",
    )
    return totals, color_families, colorings, colorings_with_local_options


def control_checks():
    guard()
    distinct_partitions = (
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
    )
    two_equal_partitions = (
        (0, 0, 0),
        (0, 0, 1),
        (1, 1, 0),
        (1, 1, 1),
    )
    require(check_binary_rows(distinct_partitions) == 0, "POSITIVE_BINARY_0")
    require(check_binary_rows(two_equal_partitions) == 1, "POSITIVE_BINARY_1")

    system = make_system((1, 0, 3, 2))
    t = frozenset((
        edge(0, 0, 1, 0),
        edge(0, 2, 1, 2),
        edge(0, 1, 2, 1),
        edge(0, 3, 2, 3),
        edge(1, 1, 2, 0),
        edge(1, 3, 2, 2),
    ))
    color = frozenset((
        edge(0, 0, 1, 0),
        edge(0, 2, 1, 2),
    ))
    check_system(system)
    check_t_shape(t)
    check_shared_incidence(system, t)

    mutated = make_system((2, 3, 0, 1))
    n_incidence = (
        frozenset((1, 3)),
        frozenset((1, 3)),
        frozenset((0, 2)),
    )
    actual_rows = (
        (1, 3, 0),
        (1, 3, 2),
        (3, 1, 0),
        (3, 1, 2),
    )
    check_system(mutated)
    require(
        check_actual_slice(mutated, n_incidence, actual_rows) == 1,
        "POSITIVE_ACTUAL_SLICE",
    )
    s_incidence = complements(n_incidence)
    require(endpoint_ok(color, s_incidence), "CONTROL_ENDPOINTS")
    require(
        quadrant_counts(mutated, s_incidence) == (2, 0, 0),
        "CONTROL_INCIDENCE_SHADOW",
    )
    require(not t <= union_edges(mutated), "CONTROL_NOT_MUTATED")

    n_shadow = tuple(frozenset((1, 3)) for _ in range(3))
    require(endpoint_ok(color, complements(n_shadow)), "CONTROL_SHADOW_ENDPOINTS")
    require(
        quadrant_counts(system, complements(n_shadow)) == (2, 2, 0),
        "CONTROL_SHADOW_COUNTS",
    )
    check_shared_incidence(system, t)

    rejected = []
    rejected.append(expect_error(
        "duplicate_binary",
        "DUPLICATE_WORDS",
        lambda: check_binary_rows((
            (0, 0, 0),
            (0, 0, 0),
            (1, 1, 1),
            (1, 1, 1),
        )),
    ))
    rejected.append(expect_error(
        "slice_shadow",
        "SLICE_SHADOW",
        lambda: check_local(system, t, color, n_shadow),
    ))
    rejected.append(expect_error(
        "shared_incidence",
        "T_SHARED_INCIDENCE",
        lambda: check_local(mutated, t, color, n_incidence),
    ))
    return rejected


def main():
    require(len(sys.argv) == 1, "UNEXPECTED_ARGUMENTS")
    guard()
    partitions, orientations, valid_nonfull, duplicates = partition_checks()
    graphs, distribution, by_graph, records, t_candidates = matching_records()
    totals, families, colorings, global_survivors = local_and_coloring_checks(records)
    rejected = control_checks()
    guard()

    print("status: COMPLETE_FINITE_QUOTIENT_CHECK")
    print("partition_triples:", sorted(partitions.items()))
    print("oriented_arrays:", sorted(orientations.items()))
    print("valid_arrays_by_nonfull_pairs:", sorted(valid_nonfull.items()))
    print("duplicate_arrays:", duplicates)
    print("graph_signatures:", sorted(graphs.items()))
    print("T_candidates:", t_candidates)
    print("systems_by_number_of_T:", sorted(distribution.items()))
    print("accepted_T_by_graph:", sorted(by_graph.items()))
    print("accepted_M_T_records:", len(records))
    for name in (
        "color_choices",
        "tested",
        "same_tested",
        "split_tested",
        "identity_checks",
        "endpoint_pass",
        "same_endpoint",
        "split_endpoint",
        "same_shadow_rejected",
        "split_shadow_rejected",
        "slice_shadow_survivors",
    ):
        print(name + ":", totals[name])
    print("labeled_colorings:", colorings)
    print("color_families_by_concentrated_rows:", sorted(families.items()))
    print("colorings_with_local_options:", global_survivors)
    print("intended_negative_controls:", ", ".join(rejected))
    print("elapsed_seconds_observed:", time.monotonic() - START)
    print("peak_rss_bytes_observed:", peak_rss_bytes())
    print("scope: necessary combinatorial quotient only")


if __name__ == "__main__":
    try:
        main()
    except CheckError as exc:
        print("status: INCOMPLETE")
        print("reason:", str(exc))
        raise SystemExit(1)

END FILE f415_independent_finite_v1.py

## 11. Acceptance and target boundaries

| Question | This return |
|---|---|
| Complete frozen packet and status controls read? | Yes, as documented above. |
| Independent balanced four-word classification? | Complete written classification and complete unexecuted enumeration code. |
| Global gauge completeness? | Proved for all three pair matchings simultaneously. |
| Alternating component classification? | Complete written classification; program directly reconstructs components. |
| All global \(T\)'s and low-color incidences covered? | Yes in the written counting and supplied code. |
| No-survivor quotient result? | Proved in writing by the double-cover contradiction. |
| Executed finite gate? | **No — NOTRUN.** |
| Universal tensor-to-interface derivation certified by this program? | No. It remains a separate written implication, not a computational conclusion. |
| Actual common maximal-word packing constructed? | No; weak positive controls do not claim one. |
| No-OLS(6) used? | No. No earlier no-OLS-dependent profile list is certified or broadened. |
| No-distance-one used? | No; the exactly-two-equal partition case is included. |
| Actual Tuscan \(T_2\) versus abstract rows audited? | No. This AME-only wave supplies no f398/Tuscan disposition. |
| Other residual profiles, all \(t=24\), support 48, or \(N\ge49\) settled? | No. |
| Novelty or original printed-target equivalence established? | No public-source audit was performed. |
| Parent adoption or independent-family/kernel verification? | Not claimed. |

There is no residual combinatorial subcase inside the stated quotient: split-color choices fail immediately, and same-pair choices fail by the independent double-cover argument.

The outstanding acceptance item for **this finite gate** is actual execution and its receipt, if performed by an execution-capable authorized parent. The complete code and precise predicted counts are supplied here; this is not an assertion that that execution occurred. Parent materialization, pinning, and disposition remain separate from both the written result and any later execution.

**Final status: COMPLETE SELF-CONTAINED FINITE-QUOTIENT WRITTEN RESULT AND RUNNABLE CHECKER; EXECUTION NOTRUN; UNREVIEWED; NOT ADOPTED.**