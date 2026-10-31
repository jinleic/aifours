Intended artifact: `review-waves/f417-tuscan-singleton-run-independent-finite-check/author-candidate-v1.md`

# f417: Independent singleton-run finite-check candidate

**Status: AUTHOR CANDIDATE — UNREVIEWED. Scientific execution: NOTRUN_RESTRICTED.**

The complete manuscript and checker source are supplied below for Main materialization. No repository file was written, and no scientific executable was run. The active read-only role permits the complete-source fallback specified in the frozen assignment; this return does not claim an executed finite gate.

## 1. Input binding and chronology

Frozen wave:

`/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f417-tuscan-singleton-run-independent-finite-check/`

Declared pins:

- Manifest: `e591b01e04752533b08675db0495f58586bb2fa978b2408412771de5072fe0ce`.
- Freeze receipt: `92a9a742fe4fdb6fc101ef99d45c1cee3b8a7db525c49adb5f8bfa7be67db7ad`.
- Literal packet: `48df7472f6d193c03d8554bd1e52d368976bc1d7278eeb9cfa7642cc121754d2`.
- Scientific source S1: `review-waves/f398-tuscan11-actual-hamiltonian-row-closure-frontier/review-v1.md`, declared SHA256 `b56de28c6218849e9200689115b0da20bcbf43d6c786a12ae2d06603ef804d85`, complete source lines 1–548.

Actual read sequence:

1. Read the manifest, freeze receipt, parent live-metadata supply, and dispatch receipt.
2. Read all seven listed status controls completely, including their endings.
3. Inspected the assigned source with read-only `git diff`; it produced no patch output.
4. Read the complete literal packet in consecutive, raw, at-most-20-line windows through packet line 550 and S1 line 548.
5. Independently reconstructed the counts and small actual arrays below, then composed the checker.

The declared hashes and clocks are attributed to the supplied **parent metadata**, not to child-native hashing or timing. No independent hash command or native scientific-execution clock was collected.

No sibling current outcome, author checker, held scientific payload, or held proof/method/selection/confidence consumer was opened. The exclusions include PH-v8/cp116 and the held AME-t28 consumers. This documents the read frontier, not cognitive isolation.

No external source was independently opened for this return. The literature statements appearing inside S1 were not independently verified or used as mathematical premises.

## 2. Exact mathematical objects and quantifiers

An actual T1(n) here means **n actual permutation rows on the same n symbols**, with every ordered pair of distinct symbols appearing exactly once at directed linear distance one.

An actual T2(n) additionally requires every ordered pair to appear **at most once** at directed linear distance two.

For every symbol subset B, write:

- b = |B|;
- q: number of maximal black runs in a row;
- s: number of singleton black runs, including either boundary;
- t: number of internal singleton white runs between black runs;
- d: number of original linear distance-two slots with both endpoints black;
- W: sum of s+t over all actual rows;
- M: the missing **ordered**, non-diagonal distance-two pairs;
- μ: |M ∩ (B×B)|.

The finite checker covers exactly:

- Every binary word of every length n = 3,…,11, including every b = 0,…,n: **4,088 words**, not a sample.
- Every first/last white/black combination and the distinguished white infinity boundary.
- One actual T2(4), with all its **16 symbol subsets**.
- A bounded search through at most **120 normalized order-six bases**, followed by direct validation of an actual T1-but-not-T2 control.
- All **19 integer cases m = 2,…,20**.
- Intended-reason rejection controls for omitted boundary singletons, augmented distance-two contamination, doubled μ, and unordered-pair collapse.

These finite quantifiers do not become a universal computational certificate.

## 3. Written reconstruction of the identity

For an arbitrary binary row, a distance-two black-to-black slot has exactly one of two forms:

- BBB, within a black run;
- BWB, across an internal white singleton.

A black run of length ℓ contributes max(ℓ−2,0) = ℓ−2+1[ℓ=1]. Consequently,

d = b − 2q + s + t.

This includes the all-white and all-black words. Boundary black singletons must be included in s.

For actual T1(n), each row has b−q adjacent black-to-black slots. Exhausted adjacency therefore gives

Σq = nb − b(b−1) = b(n+1−b).

Summing the row identity gives

Σd = b(2b−n−2) + W.

For actual T2(n), distance-two injectivity additionally gives

Σd = b(b−1) − μ.

Thus

**W = b(n+1−b) − μ.**

The second equality is precisely where the T2 assumption is needed.

### Infinity convention

Augment a row by a distinguished white infinity vertex. A finite vertex is a singleton precisely when both cycle neighbors have the opposite color.

- A boundary black singleton remains a singleton because infinity is white.
- A boundary white entry joins infinity’s white run and is not a singleton.
- Infinity itself is excluded from W, even when both row endpoints are black.

The augmented square has three slots absent from the original linear distance-two domain:

- infinity → second entry;
- penultimate entry → infinity;
- last entry → first entry.

For black finite endpoints, augmented counting adds exactly the last-to-first event when both endpoints are black. The checker verifies this distinction for every binary word in its finite domain.

This is a written reconstruction, not a separately accepted WRITTEN-gate disposition.

## 4. Actual T2(4) positive control

Use the four additive translates modulo four of (0,3,1,2):

| Row | Actual permutation |
|---|---|
| 0 | 0, 3, 1, 2 |
| 1 | 1, 0, 2, 3 |
| 2 | 2, 1, 3, 0 |
| 3 | 3, 2, 0, 1 |

Their directed distance-one pairs are:

- Row 0: (0,3), (3,1), (1,2).
- Row 1: (1,0), (0,2), (2,3).
- Row 2: (2,1), (1,3), (3,0).
- Row 3: (3,2), (2,0), (0,1).

These are exactly all twelve ordered, non-diagonal pairs.

Their original directed distance-two pairs are:

- Row 0: (0,1), (3,2).
- Row 1: (1,2), (0,3).
- Row 2: (2,3), (1,0).
- Row 3: (3,0), (2,1).

All eight are distinct. Therefore this is an actual T2(4), not an abstract incidence object.

The missing ordered pairs are

**M = {(0,2), (2,0), (1,3), (3,1)}.**

### All sixteen subset results, derived by hand

The W values below are obtained from the actual row colorings; they also satisfy W = b(5−b)−μ.

| B | b | μ | W |
|---|---:|---:|---:|
| ∅ | 0 | 0 | 0 |
| {0} | 1 | 0 | 4 |
| {1} | 1 | 0 | 4 |
| {2} | 1 | 0 | 4 |
| {3} | 1 | 0 | 4 |
| {0,1} | 2 | 0 | 6 |
| {0,2} | 2 | 2 | 4 |
| {0,3} | 2 | 0 | 6 |
| {1,2} | 2 | 0 | 6 |
| {1,3} | 2 | 2 | 4 |
| {2,3} | 2 | 0 | 6 |
| {0,1,2} | 3 | 2 | 4 |
| {0,1,3} | 3 | 2 | 4 |
| {0,2,3} | 3 | 2 | 4 |
| {1,2,3} | 3 | 2 | 4 |
| {0,1,2,3} | 4 | 4 | 0 |

These are **written calculations, not captured program output**.

## 5. Actual T1-but-not-T2 negative control

Use the six additive translates modulo six of

**(0,1,5,2,4,3).**

The rows are:

| Row | Actual permutation |
|---|---|
| 0 | 0, 1, 5, 2, 4, 3 |
| 1 | 1, 2, 0, 3, 5, 4 |
| 2 | 2, 3, 1, 4, 0, 5 |
| 3 | 3, 4, 2, 5, 1, 0 |
| 4 | 4, 5, 3, 0, 2, 1 |
| 5 | 5, 0, 4, 1, 3, 2 |

The base’s successive differences modulo six are (1,4,3,2,5), each nonzero difference exactly once. Translating each slot through all six symbols therefore supplies each of the thirty ordered adjacency pairs exactly once.

The distance-two differences of the base are (5,1,5,1). Hence the twenty-four slots contain only twelve distinct pairs, each twice. For example, (0,1) occurs in:

- Row 4, columns 4→6;
- Row 5, columns 2→4.

Thus the array is actual T1(6), but **not T2(6)**.

For B = {0,1}, the six row contributions to W are

0, 3, 3, 0, 3, 3,

so W = 12. Both ordered pairs internal to B occur, hence μ = 0. The T2 formula would give 2(7−2) = 10 instead.

There is no contradiction to the theorem: the four internal-B distance-two slots contain just two distinct pairs. The equality Σd = b(b−1)−μ fails because distance-two injectivity fails.

The checker independently searches normalized bases, validates the actual adjacency multiset, and requires rejection specifically for `distance_two_injective`. The search itself was **not run**.

## 6. Finite floor arithmetic

For m = 2,…,20, the values of both floor(m²/(2m−1)) and floor(m/2) are, respectively:

| m | Common value |
|---:|---:|
| 2 | 1 |
| 3 | 1 |
| 4 | 2 |
| 5 | 2 |
| 6 | 3 |
| 7 | 3 |
| 8 | 4 |
| 9 | 4 |
| 10 | 5 |
| 11 | 5 |
| 12 | 6 |
| 13 | 6 |
| 14 | 7 |
| 15 | 7 |
| 16 | 8 |
| 17 | 8 |
| 18 | 9 |
| 19 | 9 |
| 20 | 10 |

The source below checks every case using integer division and integer inequalities. This finite arithmetic check is not the universal m≥2 gate.

## 7. Intended-reason mutation controls

Each control first has valid positive prerequisites.

1. **Omit a boundary black singleton.** On 1000 or 0001, the correct row has b=1, q=1, s=1, t=0, d=0. Omitting the boundary singleton gives −1 instead of zero. Required rejection: `row_distance_two_identity`.
2. **Treat augmented finite distance-two slots as original.** The actual T2(4) has eight original slots. Including its four last-to-first slots gives twelve finite-endpoint slots. Required rejection: `original_distance_two_domain`.
3. **Double μ.** For B={0,2}, correct μ=2 and W=4. Substituting μ=4 gives two instead of four. Required rejection: `subset_singleton_budget`.
4. **Collapse missing ordered pairs to unordered pairs.** On the same B, collapsing (0,2) and (2,0) gives μ=1 and the incorrect budget five. Required rejection: `subset_singleton_budget`.
5. **Misclassify the actual T1(6) as T2.** Full unique adjacency must pass first; the repeated distance-two pair must then reject for `distance_two_injective`, not for parsing, row validity, or adjacency failure.

The two boundary fixtures plus the other four controls give six intended rejection checks.

## 8. Complete checker source and exact caller

Intended source filename: `f417_finite_checker.py`.

Exact caller after materialization:

`python3 -I -B f417_finite_checker.py`

No arguments, input files, network calls, child processes, installations, or deletions are used. The program uses standard-library modules and bounded in-memory objects. It checks a **55-second cooperative deadline** throughout the finite work; this is not a claim of measured runtime or a hard scheduling guarantee.

The following is a lossless, unfenced source representation. Remove exactly the literal `PY|` prefix from every source line, preserving the remaining spaces and one LF per line.

PY|import sys
PY|import time
PY|from collections import Counter
PY|from itertools import permutations, product
PY|from math import comb
PY|
PY|START = time.monotonic()
PY|BUDGET_SECONDS = 55.0
PY|
PY|
PY|class CheckFailure(Exception):
PY|    def __init__(self, invariant, detail):
PY|        self.invariant = invariant
PY|        super().__init__(f"{invariant}: {detail}")
PY|
PY|
PY|def require(condition, invariant, detail):
PY|    if not condition:
PY|        raise CheckFailure(invariant, detail)
PY|
PY|
PY|def guard():
PY|    require(
PY|        time.monotonic() - START < BUDGET_SECONDS,
PY|        "cooperative_deadline",
PY|        "55-second calculation budget reached",
PY|    )
PY|
PY|
PY|def word_counts(bits):
PY|    guard()
PY|    n = len(bits)
PY|    require(n >= 3, "word_length", str(n))
PY|    require(all(x in (0, 1) for x in bits), "binary_word", repr(bits))
PY|    runs = []
PY|    start = 0
PY|    for end in range(1, n + 1):
PY|        if end == n or bits[end] != bits[start]:
PY|            runs.append((bits[start], start, end))
PY|            start = end
PY|    b = sum(bits)
PY|    q = sum(color == 1 for color, left, right in runs)
PY|    s = sum(
PY|        color == 1 and right - left == 1
PY|        for color, left, right in runs
PY|    )
PY|    t = sum(
PY|        color == 0 and right - left == 1 and left > 0 and right < n
PY|        for color, left, right in runs
PY|    )
PY|    d = sum(bits[i] == 1 and bits[i + 2] == 1 for i in range(n - 2))
PY|    require(
PY|        d == b - 2 * q + s + t,
PY|        "row_distance_two_identity",
PY|        f"bits={bits}, direct={d}, bqst={(b, q, s, t)}",
PY|    )
PY|    cycle = (0,) + tuple(bits)
PY|    finite_singletons = sum(
PY|        cycle[j - 1] != cycle[j]
PY|        and cycle[(j + 1) % (n + 1)] != cycle[j]
PY|        for j in range(1, n + 1)
PY|    )
PY|    all_singletons = sum(
PY|        cycle[(j - 1) % (n + 1)] != cycle[j]
PY|        and cycle[(j + 1) % (n + 1)] != cycle[j]
PY|        for j in range(n + 1)
PY|    )
PY|    require(
PY|        finite_singletons == s + t,
PY|        "finite_hamiltonian_singletons",
PY|        repr(bits),
PY|    )
PY|    require(
PY|        all_singletons - finite_singletons
PY|        == int(bits[0] == 1 and bits[-1] == 1),
PY|        "infinity_exclusion",
PY|        repr(bits),
PY|    )
PY|    augmented_black_endpoints = sum(
PY|        cycle[j] == 1 and cycle[(j + 2) % (n + 1)] == 1
PY|        for j in range(n + 1)
PY|    )
PY|    require(
PY|        augmented_black_endpoints == d + bits[0] * bits[-1],
PY|        "augmented_wrap_separation",
PY|        repr(bits),
PY|    )
PY|    return b, q, s, t, d
PY|
PY|
PY|def exhaust_words():
PY|    total = 0
PY|    for n in range(3, 12):
PY|        by_b = Counter()
PY|        boundaries = Counter()
PY|        infinity = Counter()
PY|        for bits in product((0, 1), repeat=n):
PY|            b, q, s, t, d = word_counts(bits)
PY|            by_b[b] += 1
PY|            boundaries[(bits[0], bits[-1])] += 1
PY|            infinity[int(bits[0] == 1 and bits[-1] == 1)] += 1
PY|            total += 1
PY|        require(
PY|            all(by_b[b] == comb(n, b) for b in range(n + 1)),
PY|            "all_b_coverage",
PY|            f"n={n}, histogram={dict(by_b)}",
PY|        )
PY|        require(
PY|            all(boundaries[key] == 2 ** (n - 2)
PY|                for key in product((0, 1), repeat=2)),
PY|            "endpoint_coverage",
PY|            f"n={n}",
PY|        )
PY|        require(
PY|            infinity[1] == 2 ** (n - 2)
PY|            and infinity[0] == 3 * 2 ** (n - 2),
PY|            "infinity_coverage",
PY|            f"n={n}",
PY|        )
PY|        print("WORDS", n, 2 ** n, "ALL_B_AND_BOUNDARIES")
PY|    require(total == 4088, "word_total", str(total))
PY|    print("WORD_TOTAL", total)
PY|
PY|
PY|def translates(base):
PY|    n = len(base)
PY|    return tuple(
PY|        tuple((x + shift) % n for x in base)
PY|        for shift in range(n)
PY|    )
PY|
PY|
PY|def validate_t1(rows):
PY|    guard()
PY|    n = len(rows)
PY|    require(n >= 3, "array_order", str(n))
PY|    symbols = set(range(n))
PY|    for index, row in enumerate(rows):
PY|        guard()
PY|        require(
PY|            len(row) == n and sorted(row) == list(range(n)),
PY|            "row_permutation",
PY|            f"row={index}, data={row}",
PY|        )
PY|    universe = {(a, b) for a in symbols for b in symbols if a != b}
PY|    adjacency = Counter(
PY|        (row[i], row[i + 1])
PY|        for row in rows for i in range(n - 1)
PY|    )
PY|    require(
PY|        set(adjacency) == universe
PY|        and sum(adjacency.values()) == n * (n - 1)
PY|        and all(count == 1 for count in adjacency.values()),
PY|        "distance_one_exact",
PY|        f"order={n}, distinct={len(adjacency)}",
PY|    )
PY|    require(
PY|        {row[0] for row in rows} == symbols
PY|        and {row[-1] for row in rows} == symbols,
PY|        "endpoint_permutations",
PY|        f"order={n}",
PY|    )
PY|    events = tuple(
PY|        (row_index, j, row[j - 1], row[j + 1])
PY|        for row_index, row in enumerate(rows)
PY|        for j in range(1, n - 1)
PY|    )
PY|    distance_two = Counter((a, b) for _, _, a, b in events)
PY|    require(
PY|        len(events) == n * (n - 2)
PY|        and set(distance_two).issubset(universe),
PY|        "original_distance_two_slots",
PY|        f"order={n}",
PY|    )
PY|    augmented_adjacency = Counter()
PY|    for row in rows:
PY|        cycle = (n,) + tuple(row)
PY|        for j in range(n + 1):
PY|            augmented_adjacency[
PY|                (cycle[j], cycle[(j + 1) % (n + 1)])
PY|            ] += 1
PY|    augmented_universe = {
PY|        (a, b) for a in range(n + 1) for b in range(n + 1) if a != b
PY|    }
PY|    require(
PY|        set(augmented_adjacency) == augmented_universe
PY|        and all(count == 1 for count in augmented_adjacency.values()),
PY|        "actual_augmented_adjacency_decomposition",
PY|        f"order={n}",
PY|    )
PY|    return {
PY|        "rows": rows, "n": n, "universe": universe,
PY|        "d2": distance_two, "events": events,
PY|    }
PY|
PY|
PY|def require_t2(data):
PY|    guard()
PY|    repeated = sorted(
PY|        (pair, count) for pair, count in data["d2"].items() if count > 1
PY|    )
PY|    require(
PY|        not repeated,
PY|        "distance_two_injective",
PY|        f"repeated={repeated[:3]}",
PY|    )
PY|    require(
PY|        len(data["universe"] - set(data["d2"])) == data["n"],
PY|        "distance_two_missing_count",
PY|        f"order={data['n']}",
PY|    )
PY|
PY|
PY|def measure_subset(data, subset):
PY|    q_total = 0
PY|    w_total = 0
PY|    d_total = 0
PY|    for row in data["rows"]:
PY|        bits = tuple(int(x in subset) for x in row)
PY|        b, q, s, t, d = word_counts(bits)
PY|        require(b == len(subset), "subset_row_cardinality", repr(subset))
PY|        q_total += q
PY|        w_total += s + t
PY|        d_total += d
PY|    b = len(subset)
PY|    n = data["n"]
PY|    require(
PY|        q_total == b * (n + 1 - b),
PY|        "t1_black_run_total",
PY|        f"B={sorted(subset)}, q={q_total}",
PY|    )
PY|    direct_from_pairs = sum(
PY|        count for (a, b), count in data["d2"].items()
PY|        if a in subset and b in subset
PY|    )
PY|    require(
PY|        d_total == direct_from_pairs,
PY|        "actual_pair_slot_agreement",
PY|        repr(sorted(subset)),
PY|    )
PY|    require(
PY|        d_total == b * (2 * b - n - 2) + w_total,
PY|        "summed_row_identity",
PY|        repr(sorted(subset)),
PY|    )
PY|    return q_total, w_total, d_total
PY|
PY|
PY|def missing_mu(data, subset):
PY|    missing = data["universe"] - set(data["d2"])
PY|    return sum(a in subset and b in subset for a, b in missing)
PY|
PY|
PY|def check_budget(data, subset, claimed_mu=None):
PY|    require_t2(data)
PY|    q_total, w_total, d_total = measure_subset(data, subset)
PY|    actual_mu = missing_mu(data, subset)
PY|    b = len(subset)
PY|    require(
PY|        d_total == b * (b - 1) - actual_mu,
PY|        "t2_distinct_pair_budget",
PY|        repr(sorted(subset)),
PY|    )
PY|    used_mu = actual_mu if claimed_mu is None else claimed_mu
PY|    require(
PY|        w_total == b * (data["n"] + 1 - b) - used_mu,
PY|        "subset_singleton_budget",
PY|        f"B={sorted(subset)}, W={w_total}, "
PY|        f"actual_mu={actual_mu}, claimed_mu={used_mu}",
PY|    )
PY|    return w_total, actual_mu
PY|
PY|
PY|def expect_rejection(name, operation, intended_invariant):
PY|    guard()
PY|    try:
PY|        operation()
PY|    except CheckFailure as error:
PY|        require(
PY|            error.invariant == intended_invariant,
PY|            "control_wrong_reason",
PY|            f"{name}: wanted={intended_invariant}, got={error}",
PY|        )
PY|        print("CONTROL_REJECTED", name, intended_invariant)
PY|        return 1
PY|    raise CheckFailure("control_survived", name)
PY|
PY|
PY|def omitted_boundary_mutant(bits):
PY|    b, q, s, t, d = word_counts(bits)
PY|    omitted = int(bits[0] == 1 and bits[1] == 0)
PY|    omitted += int(bits[-1] == 1 and bits[-2] == 0)
PY|    require(omitted > 0, "mutation_fixture", repr(bits))
PY|    require(
PY|        d == b - 2 * q + (s - omitted) + t,
PY|        "row_distance_two_identity",
PY|        f"boundary omitted in {bits}",
PY|    )
PY|
PY|
PY|def check_original_domain(data, supplied_events):
PY|    require_t2(data)
PY|    expected = data["events"]
PY|    require(
PY|        len(supplied_events) == len(expected)
PY|        and set(supplied_events) == set(expected),
PY|        "original_distance_two_domain",
PY|        f"expected={len(expected)}, supplied={len(supplied_events)}",
PY|    )
PY|
PY|
PY|def augmented_finite_events(data):
PY|    n = data["n"]
PY|    events = []
PY|    for row_index, row in enumerate(data["rows"]):
PY|        cycle = (n,) + tuple(row)
PY|        for j in range(n + 1):
PY|            a = cycle[j]
PY|            b = cycle[(j + 2) % (n + 1)]
PY|            if a != n and b != n:
PY|                events.append((row_index, j, a, b))
PY|    return tuple(events)
PY|
PY|
PY|def find_t1_not_t2():
PY|    n = 6
PY|    for tested, tail in enumerate(permutations(range(1, n)), 1):
PY|        guard()
PY|        base = (0,) + tail
PY|        differences = {
PY|            (base[i + 1] - base[i]) % n for i in range(n - 1)
PY|        }
PY|        if differences != set(range(1, n)):
PY|            continue
PY|        data = validate_t1(translates(base))
PY|        if any(count > 1 for count in data["d2"].values()):
PY|            require(tested <= 120, "negative_search_bound", str(tested))
PY|            return data, base, tested
PY|    raise CheckFailure("negative_control_missing", "all 120 bases exhausted")
PY|
PY|
PY|def check_finite_floors():
PY|    count = 0
PY|    for m in range(2, 21):
PY|        guard()
PY|        numerator = m * m
PY|        denominator = 2 * m - 1
PY|        quotient = numerator // denominator
PY|        require(
PY|            quotient == m // 2
PY|            and quotient * denominator <= numerator
PY|            and numerator < (quotient + 1) * denominator,
PY|            "finite_floor_identity",
PY|            f"m={m}",
PY|        )
PY|        print("FINITE_FLOOR", m, quotient)
PY|        count += 1
PY|    require(count == 19, "finite_floor_coverage", str(count))
PY|
PY|
PY|def main():
PY|    require(
PY|        len(sys.argv) == 1,
PY|        "fixed_argv",
PY|        "Use: python3 -I -B f417_finite_checker.py",
PY|    )
PY|    exhaust_words()
PY|    positive = validate_t1(translates((0, 3, 1, 2)))
PY|    require_t2(positive)
PY|    require(
PY|        len(positive["d2"]) == 8,
PY|        "positive_t2_binding",
PY|        repr(positive["d2"]),
PY|    )
PY|    expected_missing = {(0, 2), (2, 0), (1, 3), (3, 1)}
PY|    require(
PY|        positive["universe"] - set(positive["d2"]) == expected_missing,
PY|        "positive_missing_pairs",
PY|        "actual ordered missing-pair set",
PY|    )
PY|    print("ACTUAL_T2", positive["rows"])
PY|    print("MISSING_ORDERED_PAIRS", sorted(expected_missing))
PY|    for mask in range(16):
PY|        guard()
PY|        subset = frozenset(x for x in range(4) if (mask >> x) & 1)
PY|        w_total, mu = check_budget(positive, subset)
PY|        print("SUBSET", sorted(subset), "b", len(subset), "mu", mu, "W", w_total)
PY|    check_original_domain(positive, positive["events"])
PY|    rejected = 0
PY|    for name, bits in (
PY|        ("omit_first_black_singleton", (1, 0, 0, 0)),
PY|        ("omit_last_black_singleton", (0, 0, 0, 1)),
PY|    ):
PY|        rejected += expect_rejection(
PY|            name,
PY|            lambda bits=bits: omitted_boundary_mutant(bits),
PY|            "row_distance_two_identity",
PY|        )
PY|    wrong_events = augmented_finite_events(positive)
PY|    require(
PY|        len(positive["events"]) == 8 and len(wrong_events) == 12,
PY|        "mutation_fixture",
PY|        "original versus augmented finite slot counts",
PY|    )
PY|    rejected += expect_rejection(
PY|        "augmented_wrap_as_original",
PY|        lambda: check_original_domain(positive, wrong_events),
PY|        "original_distance_two_domain",
PY|    )
PY|    subset = frozenset((0, 2))
PY|    w_total, mu = check_budget(positive, subset)
PY|    unordered_mu = len({
PY|        tuple(sorted((a, b))) for a, b in expected_missing
PY|        if a in subset and b in subset
PY|    })
PY|    require(
PY|        w_total == 4 and mu == 2 and unordered_mu == 1,
PY|        "mutation_fixture",
PY|        "directed missing-pair controls",
PY|    )
PY|    rejected += expect_rejection(
PY|        "double_missing_pair_count",
PY|        lambda: check_budget(positive, subset, 2 * mu),
PY|        "subset_singleton_budget",
PY|    )
PY|    rejected += expect_rejection(
PY|        "collapse_ordered_missing_pairs",
PY|        lambda: check_budget(positive, subset, unordered_mu),
PY|        "subset_singleton_budget",
PY|    )
PY|    negative, base, tested = find_t1_not_t2()
PY|    print("ACTUAL_T1_NOT_T2_BASE", base, "BASES_EXAMINED", tested)
PY|    print("ACTUAL_T1_NOT_T2_ROWS", negative["rows"])
PY|    rejected += expect_rejection(
PY|        "actual_t1_fails_t2",
PY|        lambda: require_t2(negative),
PY|        "distance_two_injective",
PY|    )
PY|    repeated_pair = min(
PY|        pair for pair, count in negative["d2"].items() if count > 1
PY|    )
PY|    negative_subset = frozenset(repeated_pair)
PY|    q_total, w_total, d_total = measure_subset(negative, negative_subset)
PY|    mu = missing_mu(negative, negative_subset)
PY|    b = len(negative_subset)
PY|    false_t2_budget = b * (negative["n"] + 1 - b) - mu
PY|    distinct_internal = sum(
PY|        a in negative_subset and b in negative_subset
PY|        for a, b in negative["d2"]
PY|    )
PY|    require(
PY|        d_total > distinct_internal and w_total > false_t2_budget,
PY|        "negative_control_exposes_t2_premise",
PY|        f"slots={d_total}, distinct={distinct_internal}, "
PY|        f"W={w_total}, false_budget={false_t2_budget}",
PY|    )
PY|    print(
PY|        "NEGATIVE_SUBSET", sorted(negative_subset),
PY|        "D_SLOTS", d_total, "D_DISTINCT", distinct_internal,
PY|        "MU", mu, "W", w_total, "FALSE_T2_BUDGET", false_t2_budget,
PY|    )
PY|    check_finite_floors()
PY|    require(rejected == 6, "rejection_control_coverage", str(rejected))
PY|    guard()
PY|    print("CONTROL_REJECTIONS", rejected)
PY|    print("RESULT: FINITE_CHECKS_PASS")
PY|
PY|
PY|if __name__ == "__main__":
PY|    try:
PY|        main()
PY|    except CheckFailure as error:
PY|        print("RESULT: FAIL", str(error), file=sys.stderr)
PY|        sys.exit(1)

**End of source.**

No stdout/stderr transcript exists for this checker. Its success and rejection strings above are source literals, not observed results.

## 9. Scope, remaining gates, and original target

The written derivation supports the universal row identity and explains exactly why the subset budget needs actual T1 adjacency exhaustion and T2 injectivity. The positive and negative arrays are actual rows, independently described and checked by displayed finite reasoning—not arbitrary Latin incidence rows or disconnected cycle covers.

For odd n=2m−1, a row with a fixed odd-position support B contributes 2m−1 to W. The budget therefore yields

(2m−1)k_B ≤ m²−μ_B.

The supplied finite floor cases are consistent with the author’s resulting multiplicity bound. Their execution remains NOTRUN, and they do not replace the independent universal written gate.

For actual T2(11), the claimed branch implication is conditional: four rows sharing one odd-position support would contribute at least 44 against a budget at most 36. This is not an eleven-row witness or unrestricted nonexistence proof.

Explicitly unpaid or unclaimed:

- Executed checker receipt, including actual exit status, output, and elapsed resource observations.
- Parent disposition of this finite candidate.
- Separate acceptance of the universally quantified written theorem.
- Existence or nonexistence of unrestricted actual T2(11).
- Exclusion of the remaining configurations with at least four distinct odd-position supports, each used at most three times.
- The additional M=C three-common-support branch beyond its already stated conditional scope.
- Any OLS result, abstract-row realizability claim, or broader cycle-cover consequence.
- Novelty, priority, independent-family acceptance, human acceptance, or kernel verification.

**Final status:** complete materializable manuscript and independent checker source supplied; execution NOTRUN_RESTRICTED; candidate remains UNREVIEWED pending parent disposition.

Overall correctness: correct

Explanation: No defect was found in the written singleton-run identity or the displayed actual small-array controls. The independent checker has not been executed under the active tool restriction, so this return does not certify a passed finite gate or resolve unrestricted T2(11).

Confidence: 0.96