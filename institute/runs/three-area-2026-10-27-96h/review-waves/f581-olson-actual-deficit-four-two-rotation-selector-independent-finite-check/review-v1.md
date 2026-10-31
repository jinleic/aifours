# F581 FINITE — independent actual-word deficit-four checker

## Disposition

**Scientific execution: NOT_RUN. Finite acceptance gate: NOT_ESTABLISHED.**

The complete independent standard-library checker is supplied below. I did not execute it, edit repository files, invoke an interpreter through another tool, or bypass the read-only role restrictions. Consequently, there are **no observed enumeration counts, mutation outcomes, elapsed time, or machine PASS** in this return.

No evidence-backed defect in the mathematical candidate was established. This is not an executed finite endorsement or parent adoption.

## Access and chronology

Before reading the scientific packet, I completed the twelve listed status/permission controls, manifest, freeze receipt, parent metadata supply, and dispatch receipt, then sent a direct pre-body ACK to Main.

After that ACK, I read the complete literal packet consecutively in raw windows of at most twenty LF, from LF 1–20 through LF 481–491. Its ending was:

S2|33|NoimportfromanunprovidedP2caseargumentorheldepisodeisneeded. AllheldepisodesANDconsumersremainNONINPUT. Same-harnessproof/finiteevidenceisnotindependent-family,human,kernel,novelty,worldwidepriorityororiginal-sourceauthentication.

Derivation and checker authorship began only afterward.

Assigned manifest SHA: `8ea0dcd822885197399400b287ba489f5fd8d32e03d56038c135e789f8098a7b`.

Assigned receipt SHA: `914f346ef6d283642ae63c98ad63e49a096229808bbde930efc4383b5f3a04c4`.

These pins agree with the parent-supplied live-metadata record. I did not perform child-native hashing or clock acquisition. No cited-but-unpasted source, author implementation, sibling return, or held scientific payload was opened. Held episodes and their consumers remained NONINPUT; this is an access chronology, not a cognitive-isolation certificate.

## Exact finite scope encoded

The checker:

- Builds actual words with \(3p-2\) reflections and \(p+1\) rotations in explicitly specified singleton cyclic gaps, preserving original physical indices.
- Exhausts all \(2^{13}\) binary reflection lists at \(p=5\), independently derives their cyclic run lengths, and filters by \(o_\pi=9\). The admitted count is computed, not prescribed.
- Applies four explicit placement/rotation-label controls to every admitted binary list. This is **not** an exhaustion of all placements or rotation labels.
- Adds deterministic cases of all five deficit-four run types at each of \(p=5,7,11\), including two distinct length-three runs.
- Checks both supplied source witnesses at their stated physical positions.
- Searches omissions independently, constructs chronological nonconstant triples, counts internal equal adjacencies, and enumerates every actual rotation’s safe/interior/unsafe/boundary route.
- Retains rotations adjacent to the omitted reflection.
- Computes each block’s alternatives by multiplying its actual selected letters, not by treating an interior rotation as an unconditional exponent shift.
- Chooses two distinct rotations with at most one interior to any block, computes the complete \(p-1\)-set sum DP, reconstructs actual selected indices, and checks their full original-order group product.
- Compares existence with a separate original-order group subsequence DP selecting exactly two rotations and \(2p-2\) reflections.
- Checks cyclic conjugation at every cut of each reconstructed identity witness.
- Separately exhausts the local first/second-interior interfaces for all three reflection-pair choices and all specified raw rotation values at \(p=5,7,11\).
- Includes intended-reason mutation checks for the requested implementation errors.

There cannot be \(p+1\) distinct rotation **group elements** in a group with only \(p\) rotations. Several controls therefore use distinct raw integer labels, including zero and negative integers, without falsely asserting distinct residues. A repeated-label control is included deliberately.

### Mutation status

Every executable mutation below is **NOT_RUN**, not an observed rejection.

The checker encodes intended reasons for:

1. Incorrect sign when an interior rotation precedes both selected reflections.
2. Incorrect sign when it follows both selected reflections.
3. Reversing the safe-gap criterion.
4. Selecting both interior rotations from one triple.
5. Dropping rotations adjacent to the omitted reflection.
6. Promoting the check to an unrequested \(p=3\) theorem.
7. Combining independent exponent choices that are not chronologically realizable.
8. Reporting only three of the five run types.
9. Incorrectly asserting equality, rather than conjugacy, of nonidentity products under cyclic rotation.

**Merely omitting the written cyclic-conjugation explanation is NOTTESTED.** An identity product remains identity at every cyclic cut, so I do not manufacture a counterexample to that proof-only omission.

## Full source

Suggested materialization name: `independent-actual-deficit-four-checker-v1.py`.

Suggested argv: `python3 -I -B independent-actual-deficit-four-checker-v1.py --seconds 55`.

The source is represented below with an exact `PY|` prefix on every source line, including blank lines. Removing that prefix gives the complete Python source. It performs no filesystem/data input, network access, subprocess creation, installation, or deletion; its only output is stdout. The cooperative deadline is checked throughout the finite calculations. Its completion time has **not** been measured.

BEGIN FULL SOURCE

PY|from collections import Counter
PY|from itertools import combinations, product
PY|from sys import argv
PY|from time import monotonic
PY|
PY|
PY|class CheckError(Exception):
PY|    def __init__(self, reason):
PY|        super().__init__(reason)
PY|        self.reason = reason
PY|
PY|
PY|DEADLINE = None
PY|EXPECTED_TYPES = frozenset(((5,), (4,), (3, 3), (3, 2), (2, 2)))
PY|
PY|
PY|def need(condition, reason):
PY|    if not condition:
PY|        raise CheckError(reason)
PY|
PY|
PY|def tick():
PY|    if DEADLINE is not None and monotonic() >= DEADLINE:
PY|        raise CheckError("INCOMPLETE_TIME_LIMIT")
PY|
PY|
PY|def domain(p):
PY|    need(p >= 5, "OUTSIDE_ASSIGNED_PRIME_SCOPE")
PY|    need(p % 2 == 1, "NOT_ODD")
PY|    need(all(p % d for d in range(2, int(p ** 0.5) + 1)), "NOT_PRIME")
PY|
PY|
PY|def mul(g, h, p):
PY|    x, e = g
PY|    y, b = h
PY|    return ((x + (y if e == 0 else -y)) % p, (e + b) % 2)
PY|
PY|
PY|def inverse(g, p):
PY|    x, e = g
PY|    return ((-x if e == 0 else x) % p, e)
PY|
PY|
PY|def group_product(letters, p):
PY|    answer = (0, 0)
PY|    for letter in letters:
PY|        answer = mul(answer, letter, p)
PY|    return answer
PY|
PY|
PY|def build_word(p, raw_refs, gaps, raw_us):
PY|    domain(p)
PY|    raw_refs = tuple(raw_refs)
PY|    gaps = tuple(gaps)
PY|    raw_us = tuple(raw_us)
PY|    f = 3 * p - 2
PY|    need(len(raw_refs) == f, "REFLECTION_INPUT_LENGTH")
PY|    need(len(gaps) == p + 1, "ROTATION_INPUT_COUNT")
PY|    need(len(raw_us) == len(gaps), "ROTATION_LABEL_COUNT")
PY|    need(len(set(gaps)) == len(gaps), "REPEATED_ROTATION_GAP")
PY|    need(all(0 <= gap < f for gap in gaps), "ROTATION_GAP_RANGE")
PY|    placed = dict(zip(gaps, raw_us))
PY|    word = []
PY|    refpos = []
PY|    gap_rot = {}
PY|    for occurrence, raw_a in enumerate(raw_refs):
PY|        refpos.append(len(word) + 1)
PY|        word.append((raw_a % p, 1))
PY|        if occurrence in placed:
PY|            gap_rot[occurrence] = len(word) + 1
PY|            word.append((placed[occurrence] % p, 0))
PY|    return {
PY|        "p": p,
PY|        "raw_refs": raw_refs,
PY|        "gaps": gaps,
PY|        "raw_us": raw_us,
PY|        "word": tuple(word),
PY|        "refpos": tuple(refpos),
PY|        "gap_rot": gap_rot,
PY|    }
PY|
PY|
PY|def actual_projection(case):
PY|    p = case["p"]
PY|    word = case["word"]
PY|    n = len(word)
PY|    refpos = tuple(i for i, g in enumerate(word, 1) if g[1] == 1)
PY|    need(len(refpos) == 3 * p - 2, "ACTUAL_REFLECTION_COUNT")
PY|    need(refpos == case["refpos"], "PHYSICAL_REFLECTION_INDEX_MAP")
PY|    labels = tuple(word[i - 1][0] for i in refpos)
PY|    gap_rot = {}
PY|    for j, pos in enumerate(refpos):
PY|        inside = []
PY|        cursor = pos % n
PY|        while word[cursor][1] == 0:
PY|            inside.append(cursor + 1)
PY|            cursor = (cursor + 1) % n
PY|            need(len(inside) <= 1, "NON_SINGLETON_CYCLIC_GAP")
PY|        need(cursor + 1 == refpos[(j + 1) % len(refpos)],
PY|             "CYCLIC_GAP_ENDPOINT")
PY|        if inside:
PY|            gap_rot[j] = inside[0]
PY|    need(gap_rot == case["gap_rot"], "ACTUAL_ROTATION_INDEX_MAP")
PY|    all_rotations = {i for i, g in enumerate(word, 1) if g[1] == 0}
PY|    need(set(gap_rot.values()) == all_rotations,
PY|         "ROTATION_OCCURRENCE_COVERAGE")
PY|    need(len(all_rotations) == p + 1, "ACTUAL_ROTATION_COUNT")
PY|    return labels, refpos, gap_rot
PY|
PY|
PY|def cyclic_run_lengths(labels):
PY|    labels = tuple(labels)
PY|    n = len(labels)
PY|    need(n > 0, "EMPTY_PROJECTION")
PY|    if len(set(labels)) == 1:
PY|        return (n,)
PY|    start = next(i for i in range(n) if labels[i] != labels[(i - 1) % n])
PY|    lengths = []
PY|    current = 1
PY|    for t in range(1, n):
PY|        now = labels[(start + t) % n]
PY|        before = labels[(start + t - 1) % n]
PY|        if now == before:
PY|            current += 1
PY|        else:
PY|            lengths.append(current)
PY|            current = 1
PY|    lengths.append(current)
PY|    need(sum(lengths) == n, "CYCLIC_RUN_ACCOUNTING")
PY|    return tuple(lengths)
PY|
PY|
PY|def run_type(labels):
PY|    lengths = cyclic_run_lengths(labels)
PY|    odd_runs = sum(length % 2 for length in lengths)
PY|    kind = tuple(sorted((length for length in lengths if length > 1),
PY|                        reverse=True))
PY|    return lengths, odd_runs, kind
PY|
PY|
PY|def verify_indices(case, indices, rotations, reflections):
PY|    p = case["p"]
PY|    word = case["word"]
PY|    indices = tuple(indices)
PY|    need(indices == tuple(sorted(indices)), "NOT_ORIGINAL_PHYSICAL_ORDER")
PY|    need(len(indices) == len(set(indices)), "REUSED_PHYSICAL_OCCURRENCE")
PY|    need(all(1 <= i <= len(word) for i in indices), "PHYSICAL_INDEX_RANGE")
PY|    selected = tuple(word[i - 1] for i in indices)
PY|    need(sum(g[1] == 0 for g in selected) == rotations,
PY|         "SELECTED_ROTATION_COUNT")
PY|    need(sum(g[1] == 1 for g in selected) == reflections,
PY|         "SELECTED_REFLECTION_COUNT")
PY|    need(len(indices) == rotations + reflections, "SELECTED_LENGTH")
PY|    need(group_product(selected, p) == (0, 0), "ORIGINAL_GROUP_PRODUCT")
PY|
PY|
PY|def check_identity_conjugations(case, indices, stats):
PY|    p = case["p"]
PY|    word = case["word"]
PY|    sequence = tuple(word[i - 1] for i in indices)
PY|    base = group_product(sequence, p)
PY|    need(base == (0, 0), "CONJUGATION_INPUT_NOT_IDENTITY")
PY|    for cut in range(len(sequence)):
PY|        tick()
PY|        prefix = group_product(sequence[:cut], p)
PY|        rotated = group_product(sequence[cut:] + sequence[:cut], p)
PY|        conjugate = mul(mul(inverse(prefix, p), base, p), prefix, p)
PY|        need(rotated == conjugate, "CYCLIC_CONJUGATION_IDENTITY")
PY|        need(rotated == (0, 0), "IDENTITY_LOST_AT_CYCLIC_CUT")
PY|        stats["identity_cut_checks"] += 1
PY|
PY|
PY|def partition_row(case, labels, z):
PY|    f = len(labels)
PY|    order = tuple((z + 1 + t) % f for t in range(f - 1))
PY|    blocks = tuple(order[t:t + 3] for t in range(0, f - 1, 3))
PY|    if any(len({labels[i] for i in block}) == 1 for block in blocks):
PY|        return None
PY|    b_count = sum(
PY|        int(labels[block[0]] == labels[block[1]]) +
PY|        int(labels[block[1]] == labels[block[2]])
PY|        for block in blocks
PY|    )
PY|    interior = {}
PY|    potential_unsafe = 0
PY|    for block_id, block in enumerate(blocks):
PY|        a, b, c = block
PY|        need((a + 1) % f == b and (b + 1) % f == c,
PY|             "TRIPLE_GAP_NOT_PHYSICAL")
PY|        safe_first = labels[b] != labels[c]
PY|        safe_second = labels[a] != labels[b]
PY|        interior[a] = (block_id, 1, safe_first)
PY|        interior[b] = (block_id, 2, safe_second)
PY|        potential_unsafe += int(not safe_first) + int(not safe_second)
PY|    need(potential_unsafe == b_count, "UNSAFE_EQUAL_ADJACENCY_COUNT")
PY|    routes = {}
PY|    for gap, physical in case["gap_rot"].items():
PY|        if gap in interior:
PY|            block_id, slot, safe = interior[gap]
PY|            routes[physical] = (
PY|                "safe" if safe else "unsafe", block_id, slot, gap
PY|            )
PY|        else:
PY|            routes[physical] = ("boundary", None, 0, gap)
PY|    need(set(routes) == set(case["gap_rot"].values()),
PY|         "ROTATION_OCCURRENCE_COVERAGE")
PY|    unsafe_actual = sum(route[0] == "unsafe" for route in routes.values())
PY|    need(unsafe_actual <= b_count, "UNSAFE_ROTATION_BOUND")
PY|    return {
PY|        "z": z,
PY|        "blocks": blocks,
PY|        "B": b_count,
PY|        "routes": routes,
PY|    }
PY|
PY|
PY|def legal_rotation_pair(first, second, routes):
PY|    if first == second:
PY|        return False
PY|    route_a = routes[first]
PY|    route_b = routes[second]
PY|    if route_a[0] == "unsafe" or route_b[0] == "unsafe":
PY|        return False
PY|    return not (
PY|        route_a[1] is not None and route_a[1] == route_b[1]
PY|    )
PY|
PY|
PY|def actual_block_options(case, block, interior_rotation, rank):
PY|    p = case["p"]
PY|    word = case["word"]
PY|    refpos = case["refpos"]
PY|    options = {}
PY|    for pair in combinations(block, 2):
PY|        selected = [refpos[pair[0]], refpos[pair[1]]]
PY|        if interior_rotation is not None:
PY|            selected.append(interior_rotation)
PY|        selected.sort(key=rank.__getitem__)
PY|        exponent, parity = group_product(
PY|            (word[i - 1] for i in selected), p
PY|        )
PY|        need(parity == 0, "BLOCK_PRODUCT_NOT_ROTATION")
PY|        if exponent not in options:
PY|            options[exponent] = tuple(selected)
PY|    return options
PY|
PY|
PY|def selector(case, prefer_interior):
PY|    p = case["p"]
PY|    domain(p)
PY|    labels, refpos, gap_rot = actual_projection(case)
PY|    lengths, odd_runs, kind = run_type(labels)
PY|    need(len(labels) - odd_runs == 4, "NOT_DEFICIT_FOUR")
PY|    need(kind in EXPECTED_TYPES, "UNEXPECTED_DEFICIT_FOUR_TYPE")
PY|    rows = []
PY|    for z in range(len(labels)):
PY|        tick()
PY|        row = partition_row(case, labels, z)
PY|        if row is not None and row["B"] <= 2:
PY|            rows.append(row)
PY|    need(rows, "NO_NONCONSTANT_TRIPLE_CERTIFICATE")
PY|    row = min(rows, key=lambda item: (item["B"], item["z"]))
PY|    routes = row["routes"]
PY|    available = [pos for pos, route in routes.items()
PY|                 if route[0] != "unsafe"]
PY|    need(len(available) >= len(gap_rot) - row["B"],
PY|         "SAFE_BOUNDARY_COUNT_BOUND")
PY|    need(len(available) >= 3, "INSUFFICIENT_SAFE_BOUNDARY_ROTATIONS")
PY|    preferred = "safe" if prefer_interior else "boundary"
PY|    available.sort(key=lambda pos: (routes[pos][0] != preferred, pos))
PY|    selected_rotations = next(
PY|        (pair for pair in combinations(available, 2)
PY|         if legal_rotation_pair(pair[0], pair[1], routes)),
PY|        None
PY|    )
PY|    need(selected_rotations is not None, "NO_LEGAL_TWO_ROTATION_PAIR")
PY|    inside = {}
PY|    boundary = []
PY|    for pos in selected_rotations:
PY|        route = routes[pos]
PY|        if route[0] == "boundary":
PY|            boundary.append(pos)
PY|        else:
PY|            need(route[0] == "safe", "SELECTED_UNSAFE_ROTATION")
PY|            block_id = route[1]
PY|            need(block_id not in inside, "ROTATION_BLOCK_COLLISION")
PY|            inside[block_id] = pos
PY|    word = case["word"]
PY|    n = len(word)
PY|    cut_physical = refpos[row["z"]]
PY|    physical_cut_order = (
PY|        tuple(range(cut_physical + 1, n + 1)) +
PY|        tuple(range(1, cut_physical + 1))
PY|    )
PY|    rank = {pos: k for k, pos in enumerate(physical_cut_order)}
PY|    need(len(row["blocks"]) == p - 1, "WRONG_TRIPLE_BLOCK_COUNT")
PY|    option_sets = []
PY|    reachable = {0: ()}
PY|    for block_id, block in enumerate(row["blocks"]):
PY|        tick()
PY|        options = actual_block_options(
PY|            case, block, inside.get(block_id), rank
PY|        )
PY|        need(len(options) >= 2, "BLOCK_EXPONENT_SET_COLLAPSE")
PY|        option_sets.append(tuple(sorted(options)))
PY|        following = {}
PY|        for old_sum, old_indices in reachable.items():
PY|            for exponent, block_indices in options.items():
PY|                new_sum = (old_sum + exponent) % p
PY|                if new_sum not in following:
PY|                    following[new_sum] = old_indices + block_indices
PY|        reachable = following
PY|    need(set(reachable) == set(range(p)), "SUMSET_NOT_FULL_FIELD")
PY|    boundary_sum = sum(word[pos - 1][0] for pos in boundary) % p
PY|    chosen = reachable[(-boundary_sum) % p] + tuple(boundary)
PY|    need(len(chosen) == len(set(chosen)), "REUSED_PHYSICAL_OCCURRENCE")
PY|    need(set(selected_rotations) ==
PY|         {pos for pos in chosen if word[pos - 1][1] == 0},
PY|         "SELECTED_ROTATIONS_NOT_RECONSTRUCTED")
PY|    cut_indices = tuple(sorted(chosen, key=rank.__getitem__))
PY|    need(group_product((word[i - 1] for i in cut_indices), p) == (0, 0),
PY|         "CUT_ORDER_GROUP_PRODUCT")
PY|    original_indices = tuple(sorted(chosen))
PY|    verify_indices(case, original_indices, 2, 2 * p - 2)
PY|    return {
PY|        "indices": original_indices,
PY|        "cut_indices": cut_indices,
PY|        "omitted_reflection": row["z"] + 1,
PY|        "omitted_physical": refpos[row["z"]],
PY|        "blocks": tuple(tuple(i + 1 for i in block)
PY|                        for block in row["blocks"]),
PY|        "B": row["B"],
PY|        "routes": tuple((pos,) + routes[pos] for pos in sorted(routes)),
PY|        "selected_rotations": tuple(sorted(selected_rotations)),
PY|        "sets": tuple(option_sets),
PY|        "kind": kind,
PY|        "runs": lengths,
PY|    }
PY|
PY|
PY|def original_group_dp(case):
PY|    p = case["p"]
PY|    max_reflections = 2 * p - 2
PY|    states = {(0, 0, 0, 0): ()}
PY|    for pos, (value, bit) in enumerate(case["word"], 1):
PY|        tick()
PY|        following = dict(states)
PY|        for (rotations, reflections, x, parity), path in states.items():
PY|            next_rotations = rotations + int(bit == 0)
PY|            next_reflections = reflections + int(bit == 1)
PY|            if next_rotations > 2 or next_reflections > max_reflections:
PY|                continue
PY|            next_x = (x - value if parity else x + value) % p
PY|            next_parity = parity ^ bit
PY|            key = (next_rotations, next_reflections, next_x, next_parity)
PY|            if key not in following:
PY|                following[key] = path + (pos,)
PY|        states = following
PY|    return states.get((2, max_reflections, 0, 0))
PY|
PY|
PY|def check_case(case, prefer_interior, stats, emit=False, tag=""):
PY|    tick()
PY|    result = selector(case, prefer_interior)
PY|    independent = original_group_dp(case)
PY|    need(independent is not None, "ORIGINAL_GROUP_DP_DISAGREEMENT")
PY|    verify_indices(case, independent, 2, 2 * case["p"] - 2)
PY|    check_identity_conjugations(case, result["indices"], stats)
PY|    stats["actual_case_checks"] += 1
PY|    stats["full_group_dp_comparisons"] += 1
PY|    route_lookup = {row[0]: row[1] for row in result["routes"]}
PY|    for pos in result["selected_rotations"]:
PY|        stats["selected_" + route_lookup[pos] + "_rotations"] += 1
PY|    if emit:
PY|        print("CASE", tag)
PY|        print("p/raw_reflections", case["p"], case["raw_refs"])
PY|        print("zero_based_gaps/raw_rotations", case["gaps"], case["raw_us"])
PY|        print("actual_word", case["word"])
PY|        print("certificate", result)
PY|        print("independent_original_dp_indices", independent)
PY|    return result
PY|
PY|
PY|def local_choices(p, a, b, c, u, slot):
PY|    if slot == 1:
PY|        letters = ((a, 1), (u % p, 0), (b, 1), (c, 1))
PY|    else:
PY|        need(slot == 2, "LOCAL_SLOT_RANGE")
PY|        letters = ((a, 1), (b, 1), (u % p, 0), (c, 1))
PY|    reflections = tuple(i for i, g in enumerate(letters) if g[1] == 1)
PY|    rotation = next(i for i, g in enumerate(letters) if g[1] == 0)
PY|    answers = []
PY|    for pair in combinations(reflections, 2):
PY|        selected = tuple(sorted(pair + (rotation,)))
PY|        exponent, parity = group_product((letters[i] for i in selected), p)
PY|        need(parity == 0, "LOCAL_PAIR_PARITY")
PY|        answers.append(exponent)
PY|    return tuple(answers)
PY|
PY|
PY|def exhaustive_local_interfaces(stats):
PY|    for p in (5, 7, 11):
PY|        for a, b, c in product(range(p), repeat=3):
PY|            tick()
PY|            for u in range(-p, p + 1):
PY|                first = local_choices(p, a, b, c, u, 1)
PY|                second = local_choices(p, a, b, c, u, 2)
PY|                expected_first = (
PY|                    (a - u - b) % p,
PY|                    (a - u - c) % p,
PY|                    (u + b - c) % p,
PY|                )
PY|                expected_second = (
PY|                    (a - b + u) % p,
PY|                    (a - u - c) % p,
PY|                    (b - u - c) % p,
PY|                )
PY|                need(first == expected_first, "FIRST_INTERIOR_INTERFACE")
PY|                need(second == expected_second, "SECOND_INTERIOR_INTERFACE")
PY|                if b != c:
PY|                    need(len(set(first)) >= 2, "FIRST_SAFE_GAP_COLLAPSE")
PY|                if a != b:
PY|                    need(len(set(second)) >= 2, "SECOND_SAFE_GAP_COLLAPSE")
PY|                stats["local_slot_interfaces"] += 2
PY|                stats["local_pair_products"] += 6
PY|
PY|
PY|def source_examples(stats):
PY|    refs_one = (0, 0, 0, 0, 0, 1, 2, 3, 4, 1, 2, 3, 4)
PY|    case_one = build_word(5, refs_one, tuple(range(6)), (1,) * 6)
PY|    source_one_indices = (1, 3, 4, 6, 7, 9, 13, 14, 16, 17)
PY|    actual_projection(case_one)
PY|    verify_indices(case_one, source_one_indices, 2, 8)
PY|    check_identity_conjugations(case_one, source_one_indices, stats)
PY|    need(run_type(refs_one)[1] == 9, "SOURCE_ONE_PROJECTION")
PY|    print("SOURCE_S1_GIVEN_IDENTITY", source_one_indices, case_one["word"])
PY|    refs_two = (0, 0, 0, 1, 0, 1, 2, 3, 4, 0, 1, 2, 3)
PY|    case_two = build_word(5, refs_two, tuple(range(6)), (1,) * 6)
PY|    source_two_indices = (1, 3, 5, 7, 11, 13, 14, 16, 18, 19)
PY|    actual_projection(case_two)
PY|    verify_indices(case_two, source_two_indices, 0, 10)
PY|    check_identity_conjugations(case_two, source_two_indices, stats)
PY|    need(run_type(refs_two)[1] == 11, "SOURCE_TWO_PROJECTION")
PY|    print("SOURCE_S2_GIVEN_IDENTITY", source_two_indices, case_two["word"])
PY|    stats["source_example_witnesses"] += 2
PY|    return case_one
PY|
PY|
PY|def expect_rejection(name, reason, action, logs):
PY|    try:
PY|        action()
PY|    except CheckError as error:
PY|        need(error.reason == reason, "WRONG_MUTATION_REJECTION_REASON:" + name)
PY|    else:
PY|        raise CheckError("MUTATION_SURVIVED:" + name)
PY|    logs.append((name, "REJECTED", reason))
PY|
PY|
PY|def require_coverage(covered):
PY|    need(frozenset(covered) == EXPECTED_TYPES, "RUN_TYPE_COVERAGE")
PY|
PY|
PY|def mutation_controls(source_case):
PY|    logs = []
PY|    prefix_actual = local_choices(5, 0, 1, 2, 1, 1)[2]
PY|    prefix_wrong = (1 - 2 - 1) % 5
PY|    expect_rejection(
PY|        "rotation_before_both_selected_reflections",
PY|        "INTERIOR_PREFIX_SIGN",
PY|        lambda: need(prefix_actual == prefix_wrong, "INTERIOR_PREFIX_SIGN"),
PY|        logs,
PY|    )
PY|    suffix_actual = local_choices(5, 0, 1, 2, 1, 2)[0]
PY|    suffix_wrong = (0 - 1 - 1) % 5
PY|    expect_rejection(
PY|        "rotation_after_both_selected_reflections",
PY|        "INTERIOR_SUFFIX_SIGN",
PY|        lambda: need(suffix_actual == suffix_wrong, "INTERIOR_SUFFIX_SIGN"),
PY|        logs,
PY|    )
PY|    need(0 != 1, "BAD_UNSAFE_FIRST_FIXTURE")
PY|    first_collapsed = local_choices(5, 0, 1, 1, 2, 1)
PY|    expect_rejection(
PY|        "first_gap_wrong_safe_comparison",
PY|        "SAFE_GAP_COLLAPSE",
PY|        lambda: need(len(set(first_collapsed)) >= 2, "SAFE_GAP_COLLAPSE"),
PY|        logs,
PY|    )
PY|    need(1 != 0, "BAD_UNSAFE_SECOND_FIXTURE")
PY|    second_collapsed = local_choices(5, 1, 1, 0, 3, 2)
PY|    expect_rejection(
PY|        "second_gap_wrong_safe_comparison",
PY|        "SAFE_GAP_COLLAPSE",
PY|        lambda: need(len(set(second_collapsed)) >= 2, "SAFE_GAP_COLLAPSE"),
PY|        logs,
PY|    )
PY|    double_letters = ((0, 1), (2, 0), (1, 1), (2, 0), (2, 1))
PY|    double_options = set()
PY|    for pair in combinations((0, 2, 4), 2):
PY|        positions = tuple(sorted(pair + (1, 3)))
PY|        double_options.add(group_product(
PY|            (double_letters[i] for i in positions), 5
PY|        ))
PY|    need(double_options == {(4, 0)}, "BAD_DOUBLE_INTERIOR_FIXTURE")
PY|    collision_routes = {
PY|        2: ("safe", 0, 1, 0),
PY|        4: ("safe", 0, 2, 1),
PY|    }
PY|    expect_rejection(
PY|        "both_rotations_inside_one_block",
PY|        "ROTATION_BLOCK_COLLISION",
PY|        lambda: need(legal_rotation_pair(2, 4, collision_routes),
PY|                     "ROTATION_BLOCK_COLLISION"),
PY|        logs,
PY|    )
PY|    labels, _, _ = actual_projection(source_case)
PY|    z = 2
PY|    row = partition_row(source_case, labels, z)
PY|    need(row is not None, "BAD_OMISSION_FIXTURE")
PY|    adjacent_gaps = {(z - 1) % len(labels), z}
PY|    adjacent_rotations = {
PY|        source_case["gap_rot"][gap] for gap in adjacent_gaps
PY|    }
PY|    need(adjacent_rotations == {4, 6}, "BAD_ADJACENT_ROTATION_FIXTURE")
PY|    need(all(row["routes"][pos][0] == "boundary"
PY|             for pos in adjacent_rotations),
PY|         "OMITTED_REFLECTION_ADJACENCY_ROUTE")
PY|    dropped_routes = {
PY|        pos: route for pos, route in row["routes"].items()
PY|        if route[3] not in adjacent_gaps
PY|    }
PY|    expect_rejection(
PY|        "drop_rotations_adjacent_to_omitted_reflection",
PY|        "ROTATION_OCCURRENCE_COVERAGE",
PY|        lambda: need(
PY|            set(dropped_routes) == set(source_case["gap_rot"].values()),
PY|            "ROTATION_OCCURRENCE_COVERAGE"
PY|        ),
PY|        logs,
PY|    )
PY|    expect_rejection(
PY|        "unrequested_p3_theorem_scope",
PY|        "OUTSIDE_ASSIGNED_PRIME_SCOPE",
PY|        lambda: domain(3),
PY|        logs,
PY|    )
PY|    four = ((0, 1), (1, 1), (2, 1), (3, 1))
PY|    first_pair = group_product((four[0], four[2]), 5)
PY|    second_pair = group_product((four[1], four[3]), 5)
PY|    independently_added = mul(first_pair, second_pair, 5)
PY|    chronological = group_product(four, 5)
PY|    need(independently_added == (1, 0) and chronological == (3, 0),
PY|         "BAD_NONREALIZABLE_FIXTURE")
PY|    expect_rejection(
PY|        "interleaved_independent_exponent_choices",
PY|        "NONREALIZABLE_CHRONOLOGICAL_SUM",
PY|        lambda: need(independently_added == chronological,
PY|                     "NONREALIZABLE_CHRONOLOGICAL_SUM"),
PY|        logs,
PY|    )
PY|    expect_rejection(
PY|        "only_three_run_types_reported",
PY|        "RUN_TYPE_COVERAGE",
PY|        lambda: require_coverage(((5,), (4,), (3, 3))),
PY|        logs,
PY|    )
PY|    nonidentity = ((0, 1), (1, 0))
PY|    base = group_product(nonidentity, 5)
PY|    rotated = group_product(nonidentity[1:] + nonidentity[:1], 5)
PY|    prefix = nonidentity[0]
PY|    conjugate = mul(mul(inverse(prefix, 5), base, 5), prefix, 5)
PY|    need(rotated == conjugate, "NONIDENTITY_CONJUGATION_CONTROL")
PY|    need(base == (4, 1) and rotated == (1, 1),
PY|         "BAD_NONIDENTITY_CUT_FIXTURE")
PY|    expect_rejection(
PY|        "false_equality_of_nonidentity_cyclic_products",
PY|        "FALSE_CYCLIC_INVARIANCE",
PY|        lambda: need(base == rotated, "FALSE_CYCLIC_INVARIANCE"),
PY|        logs,
PY|    )
PY|    logs.append((
PY|        "missing_written_cyclic_conjugation_explanation",
PY|        "NOTTESTED",
PY|        "Proof-only omission; identity products cannot supply a counterexample."
PY|    ))
PY|    return logs
PY|
PY|
PY|def deterministic_reflections(p, kind, variant):
PY|    f = 3 * p - 2
PY|    singles = f - sum(kind)
PY|    if len(kind) == 1:
PY|        run_lengths = list(kind) + [1] * singles
PY|    else:
PY|        left = singles // 2
PY|        run_lengths = ([kind[0]] + [1] * left +
PY|                       [kind[1]] + [1] * (singles - left))
PY|    labels = [(2 * j + variant) % p for j in range(len(run_lengths))]
PY|    if labels[-1] == labels[0]:
PY|        labels[-1] = next(value for value in range(p)
PY|                          if value != labels[-2] and value != labels[0])
PY|    refs = []
PY|    for label, length in zip(labels, run_lengths):
PY|        refs.extend([label] * length)
PY|    shift = (3 * sum(kind) + variant) % f
PY|    refs = tuple(refs[shift:] + refs[:shift])
PY|    need(run_type(refs)[2] == kind, "DETERMINISTIC_TYPE_CONSTRUCTION")
PY|    need(len(refs) - run_type(refs)[1] == 4,
PY|         "DETERMINISTIC_DEFICIT_CONSTRUCTION")
PY|    return refs
PY|
PY|
PY|def main():
PY|    global DEADLINE
PY|    need(len(argv) == 3 and argv[1] == "--seconds", "ARGV")
PY|    seconds = float(argv[2])
PY|    need(0 < seconds <= 55, "SECONDS_OUTSIDE_BOUND")
PY|    started = monotonic()
PY|    DEADLINE = started + seconds
PY|    stats = Counter()
PY|    source_case = source_examples(stats)
PY|    mutation_logs = mutation_controls(source_case)
PY|    exhaustive_local_interfaces(stats)
PY|    check_case(source_case, False, stats, True, "source_S1_reconstructed")
PY|    schemes = (
PY|        (
PY|            "p5_contiguous_distinct_raw",
PY|            (0, 1, 2, 3, 4, 5),
PY|            (0, -1, 2, -3, 4, -5),
PY|            False,
PY|        ),
PY|        (
PY|            "p5_even_gaps_distinct_raw",
PY|            (0, 2, 4, 6, 8, 10),
PY|            (-7, 0, 3, 8, -11, 13),
PY|            True,
PY|        ),
PY|        (
PY|            "p5_wrap_gap_repeated_label",
PY|            (1, 3, 5, 7, 9, 12),
PY|            (1, 1, 1, 1, 1, 1),
PY|            False,
PY|        ),
PY|        (
PY|            "p5_spread_wrap_distinct_raw",
PY|            (0, 1, 4, 7, 10, 12),
PY|            (5, -4, 9, 0, -2, 17),
PY|            True,
PY|        ),
PY|    )
PY|    print("BINARY_PLACEMENT_CONTROLS", schemes)
PY|    binary_admitted_types = Counter()
PY|    binary_case_types = Counter()
PY|    emitted_binary = set()
PY|    covered = set()
PY|    for refs in product((0, 1), repeat=13):
PY|        tick()
PY|        stats["binary_lists_scanned"] += 1
PY|        _, odd_runs, kind = run_type(refs)
PY|        if odd_runs != 9:
PY|            continue
PY|        need(kind in EXPECTED_TYPES, "BINARY_TYPE_CLASSIFICATION")
PY|        stats["binary_lists_admitted"] += 1
PY|        binary_admitted_types[kind] += 1
PY|        covered.add(kind)
PY|        for name, gaps, us, prefer_interior in schemes:
PY|            case = build_word(5, refs, gaps, us)
PY|            emission_key = (name, kind)
PY|            emit = emission_key not in emitted_binary
PY|            check_case(case, prefer_interior, stats, emit,
PY|                       "binary_first_witness:" + repr(emission_key))
PY|            emitted_binary.add(emission_key)
PY|            binary_case_types[(name, kind)] += 1
PY|    need(stats["binary_lists_scanned"] == 2 ** 13,
PY|         "BINARY_UNIVERSE_NOT_EXHAUSTED")
PY|    need(stats["binary_lists_admitted"] > 0, "NO_BINARY_CASES")
PY|    deterministic_coverage = Counter()
PY|    ordered_types = ((5,), (4,), (3, 3), (3, 2), (2, 2))
PY|    for p in (5, 7, 11):
PY|        for kind in ordered_types:
PY|            for variant in (0, 1):
PY|                tick()
PY|                refs = deterministic_reflections(p, kind, variant)
PY|                f = len(refs)
PY|                if variant == 0:
PY|                    gaps = tuple(range(p + 1))
PY|                else:
PY|                    gaps = tuple((f - 1 + 2 * j) % f
PY|                                 for j in range(p + 1))
PY|                us = (0,) + tuple(
PY|                    (-1 if j % 2 else 1) * (p + 2 * j + variant)
PY|                    for j in range(1, p + 1)
PY|                )
PY|                case = build_word(p, refs, gaps, us)
PY|                result = check_case(
PY|                    case, variant == 1, stats, True,
PY|                    "deterministic:" + repr((p, kind, variant))
PY|                )
PY|                need(result["kind"] == kind, "DETERMINISTIC_CASE_TYPE")
PY|                covered.add(result["kind"])
PY|                deterministic_coverage[(p, kind)] += 1
PY|    require_coverage(covered)
PY|    for p in (5, 7, 11):
PY|        need({kind for prime, kind in deterministic_coverage if prime == p}
PY|             == EXPECTED_TYPES, "PER_PRIME_RUN_TYPE_COVERAGE")
PY|    need(stats["selected_safe_rotations"] > 0,
PY|         "NO_SELECTED_INTERIOR_ROTATION_CONTROL")
PY|    need(stats["selected_boundary_rotations"] > 0,
PY|         "NO_SELECTED_BOUNDARY_ROTATION_CONTROL")
PY|    tick()
PY|    elapsed = monotonic() - started
PY|    print("BINARY_ADMITTED_TYPES", tuple(sorted(binary_admitted_types.items())))
PY|    print("BINARY_CASE_TYPES", tuple(sorted(binary_case_types.items())))
PY|    print("DETERMINISTIC_COVERAGE",
PY|          tuple(sorted(deterministic_coverage.items())))
PY|    print("MUTATION_OUTCOMES", tuple(mutation_logs))
PY|    print("COUNTERS", tuple(sorted(stats.items())))
PY|    print("ELAPSED_SECONDS", elapsed)
PY|    print("LIMITS",
PY|          "Finite cases only; four p5 placements, not all placements; "
PY|          "no all-prime proof, unrestricted Olson closure, all-group "
PY|          "closure, novelty, independent-family, human, or kernel claim.")
PY|    print("RESULT PASS FINITE_ONLY")
PY|
PY|
PY|if __name__ == "__main__":
PY|    try:
PY|        main()
PY|    except CheckError as error:
PY|        print("RESULT NOT_COMPLETE_OR_FAILED", error.reason)
PY|        raise SystemExit(2 if error.reason == "INCOMPLETE_TIME_LIMIT" else 1)

END FULL SOURCE

## Evidence ceiling and exact unpaid step

The checker is independently authored from the actual group law and the complete frozen mathematical statement. It imports no supplied implementation.

The unpaid finite step is **materialization, static review, and one authorized execution of these exact source bytes**, retaining the actual stdout/stderr, exit status, elapsed time, and source hash. Until that occurs, all enumeration totals and executable mutation results remain unobserved. A future execution failure must be reported as such; the printed PASS branch is not evidence that it was reached.

Even a successful execution would support only its explicit finite cases and interfaces. It would not prove the all-prime theorem, settle the residual high-run interval, establish unrestricted ordered-Olson/all-group closure, or supply independent-family, human, kernel, source-authentication, or novelty credit.

## Findings and verdict

**Candidate F/M/m established here: 0/0/0.** These are established-defect counts, not a claim that the unexecuted finite gate passed.

**Overall correctness: correct.**

**Explanation:** No evidence-backed defect in the frozen mathematical candidate was established by the permitted review. The complete finite checker is returned, but its execution and finite acceptance remain explicitly NOT_RUN.

**Confidence: 0.78.**