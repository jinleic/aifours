from collections import Counter
from itertools import combinations, product
from sys import argv
from time import monotonic


class CheckError(Exception):
    def __init__(self, reason):
        super().__init__(reason)
        self.reason = reason


DEADLINE = None
EXPECTED_TYPES = frozenset(((5,), (4,), (3, 3), (3, 2), (2, 2)))


def need(condition, reason):
    if not condition:
        raise CheckError(reason)


def tick():
    if DEADLINE is not None and monotonic() >= DEADLINE:
        raise CheckError("INCOMPLETE_TIME_LIMIT")


def domain(p):
    need(p >= 5, "OUTSIDE_ASSIGNED_PRIME_SCOPE")
    need(p % 2 == 1, "NOT_ODD")
    need(all(p % d for d in range(2, int(p ** 0.5) + 1)), "NOT_PRIME")


def mul(g, h, p):
    x, e = g
    y, b = h
    return ((x + (y if e == 0 else -y)) % p, (e + b) % 2)


def inverse(g, p):
    x, e = g
    return ((-x if e == 0 else x) % p, e)


def group_product(letters, p):
    answer = (0, 0)
    for letter in letters:
        answer = mul(answer, letter, p)
    return answer


def build_word(p, raw_refs, gaps, raw_us):
    domain(p)
    raw_refs = tuple(raw_refs)
    gaps = tuple(gaps)
    raw_us = tuple(raw_us)
    f = 3 * p - 2
    need(len(raw_refs) == f, "REFLECTION_INPUT_LENGTH")
    need(len(gaps) == p + 1, "ROTATION_INPUT_COUNT")
    need(len(raw_us) == len(gaps), "ROTATION_LABEL_COUNT")
    need(len(set(gaps)) == len(gaps), "REPEATED_ROTATION_GAP")
    need(all(0 <= gap < f for gap in gaps), "ROTATION_GAP_RANGE")
    placed = dict(zip(gaps, raw_us))
    word = []
    refpos = []
    gap_rot = {}
    for occurrence, raw_a in enumerate(raw_refs):
        refpos.append(len(word) + 1)
        word.append((raw_a % p, 1))
        if occurrence in placed:
            gap_rot[occurrence] = len(word) + 1
            word.append((placed[occurrence] % p, 0))
    return {
        "p": p,
        "raw_refs": raw_refs,
        "gaps": gaps,
        "raw_us": raw_us,
        "word": tuple(word),
        "refpos": tuple(refpos),
        "gap_rot": gap_rot,
    }


def actual_projection(case):
    p = case["p"]
    word = case["word"]
    n = len(word)
    refpos = tuple(i for i, g in enumerate(word, 1) if g[1] == 1)
    need(len(refpos) == 3 * p - 2, "ACTUAL_REFLECTION_COUNT")
    need(refpos == case["refpos"], "PHYSICAL_REFLECTION_INDEX_MAP")
    labels = tuple(word[i - 1][0] for i in refpos)
    gap_rot = {}
    for j, pos in enumerate(refpos):
        inside = []
        cursor = pos % n
        while word[cursor][1] == 0:
            inside.append(cursor + 1)
            cursor = (cursor + 1) % n
            need(len(inside) <= 1, "NON_SINGLETON_CYCLIC_GAP")
        need(cursor + 1 == refpos[(j + 1) % len(refpos)],
             "CYCLIC_GAP_ENDPOINT")
        if inside:
            gap_rot[j] = inside[0]
    need(gap_rot == case["gap_rot"], "ACTUAL_ROTATION_INDEX_MAP")
    all_rotations = {i for i, g in enumerate(word, 1) if g[1] == 0}
    need(set(gap_rot.values()) == all_rotations,
         "ROTATION_OCCURRENCE_COVERAGE")
    need(len(all_rotations) == p + 1, "ACTUAL_ROTATION_COUNT")
    return labels, refpos, gap_rot


def cyclic_run_lengths(labels):
    labels = tuple(labels)
    n = len(labels)
    need(n > 0, "EMPTY_PROJECTION")
    if len(set(labels)) == 1:
        return (n,)
    start = next(i for i in range(n) if labels[i] != labels[(i - 1) % n])
    lengths = []
    current = 1
    for t in range(1, n):
        now = labels[(start + t) % n]
        before = labels[(start + t - 1) % n]
        if now == before:
            current += 1
        else:
            lengths.append(current)
            current = 1
    lengths.append(current)
    need(sum(lengths) == n, "CYCLIC_RUN_ACCOUNTING")
    return tuple(lengths)


def run_type(labels):
    lengths = cyclic_run_lengths(labels)
    odd_runs = sum(length % 2 for length in lengths)
    kind = tuple(sorted((length for length in lengths if length > 1),
                        reverse=True))
    return lengths, odd_runs, kind


def verify_indices(case, indices, rotations, reflections):
    p = case["p"]
    word = case["word"]
    indices = tuple(indices)
    need(indices == tuple(sorted(indices)), "NOT_ORIGINAL_PHYSICAL_ORDER")
    need(len(indices) == len(set(indices)), "REUSED_PHYSICAL_OCCURRENCE")
    need(all(1 <= i <= len(word) for i in indices), "PHYSICAL_INDEX_RANGE")
    selected = tuple(word[i - 1] for i in indices)
    need(sum(g[1] == 0 for g in selected) == rotations,
         "SELECTED_ROTATION_COUNT")
    need(sum(g[1] == 1 for g in selected) == reflections,
         "SELECTED_REFLECTION_COUNT")
    need(len(indices) == rotations + reflections, "SELECTED_LENGTH")
    need(group_product(selected, p) == (0, 0), "ORIGINAL_GROUP_PRODUCT")


def check_identity_conjugations(case, indices, stats):
    p = case["p"]
    word = case["word"]
    sequence = tuple(word[i - 1] for i in indices)
    base = group_product(sequence, p)
    need(base == (0, 0), "CONJUGATION_INPUT_NOT_IDENTITY")
    for cut in range(len(sequence)):
        tick()
        prefix = group_product(sequence[:cut], p)
        rotated = group_product(sequence[cut:] + sequence[:cut], p)
        conjugate = mul(mul(inverse(prefix, p), base, p), prefix, p)
        need(rotated == conjugate, "CYCLIC_CONJUGATION_IDENTITY")
        need(rotated == (0, 0), "IDENTITY_LOST_AT_CYCLIC_CUT")
        stats["identity_cut_checks"] += 1


def partition_row(case, labels, z):
    f = len(labels)
    order = tuple((z + 1 + t) % f for t in range(f - 1))
    blocks = tuple(order[t:t + 3] for t in range(0, f - 1, 3))
    if any(len({labels[i] for i in block}) == 1 for block in blocks):
        return None
    b_count = sum(
        int(labels[block[0]] == labels[block[1]]) +
        int(labels[block[1]] == labels[block[2]])
        for block in blocks
    )
    interior = {}
    potential_unsafe = 0
    for block_id, block in enumerate(blocks):
        a, b, c = block
        need((a + 1) % f == b and (b + 1) % f == c,
             "TRIPLE_GAP_NOT_PHYSICAL")
        safe_first = labels[b] != labels[c]
        safe_second = labels[a] != labels[b]
        interior[a] = (block_id, 1, safe_first)
        interior[b] = (block_id, 2, safe_second)
        potential_unsafe += int(not safe_first) + int(not safe_second)
    need(potential_unsafe == b_count, "UNSAFE_EQUAL_ADJACENCY_COUNT")
    routes = {}
    for gap, physical in case["gap_rot"].items():
        if gap in interior:
            block_id, slot, safe = interior[gap]
            routes[physical] = (
                "safe" if safe else "unsafe", block_id, slot, gap
            )
        else:
            routes[physical] = ("boundary", None, 0, gap)
    need(set(routes) == set(case["gap_rot"].values()),
         "ROTATION_OCCURRENCE_COVERAGE")
    unsafe_actual = sum(route[0] == "unsafe" for route in routes.values())
    need(unsafe_actual <= b_count, "UNSAFE_ROTATION_BOUND")
    return {
        "z": z,
        "blocks": blocks,
        "B": b_count,
        "routes": routes,
    }


def legal_rotation_pair(first, second, routes):
    if first == second:
        return False
    route_a = routes[first]
    route_b = routes[second]
    if route_a[0] == "unsafe" or route_b[0] == "unsafe":
        return False
    return not (
        route_a[1] is not None and route_a[1] == route_b[1]
    )


def actual_block_options(case, block, interior_rotation, rank):
    p = case["p"]
    word = case["word"]
    refpos = case["refpos"]
    options = {}
    for pair in combinations(block, 2):
        selected = [refpos[pair[0]], refpos[pair[1]]]
        if interior_rotation is not None:
            selected.append(interior_rotation)
        selected.sort(key=rank.__getitem__)
        exponent, parity = group_product(
            (word[i - 1] for i in selected), p
        )
        need(parity == 0, "BLOCK_PRODUCT_NOT_ROTATION")
        if exponent not in options:
            options[exponent] = tuple(selected)
    return options


def selector(case, prefer_interior):
    p = case["p"]
    domain(p)
    labels, refpos, gap_rot = actual_projection(case)
    lengths, odd_runs, kind = run_type(labels)
    need(len(labels) - odd_runs == 4, "NOT_DEFICIT_FOUR")
    need(kind in EXPECTED_TYPES, "UNEXPECTED_DEFICIT_FOUR_TYPE")
    rows = []
    for z in range(len(labels)):
        tick()
        row = partition_row(case, labels, z)
        if row is not None and row["B"] <= 2:
            rows.append(row)
    need(rows, "NO_NONCONSTANT_TRIPLE_CERTIFICATE")
    row = min(rows, key=lambda item: (item["B"], item["z"]))
    routes = row["routes"]
    available = [pos for pos, route in routes.items()
                 if route[0] != "unsafe"]
    need(len(available) >= len(gap_rot) - row["B"],
         "SAFE_BOUNDARY_COUNT_BOUND")
    need(len(available) >= 3, "INSUFFICIENT_SAFE_BOUNDARY_ROTATIONS")
    preferred = "safe" if prefer_interior else "boundary"
    available.sort(key=lambda pos: (routes[pos][0] != preferred, pos))
    selected_rotations = next(
        (pair for pair in combinations(available, 2)
         if legal_rotation_pair(pair[0], pair[1], routes)),
        None
    )
    need(selected_rotations is not None, "NO_LEGAL_TWO_ROTATION_PAIR")
    inside = {}
    boundary = []
    for pos in selected_rotations:
        route = routes[pos]
        if route[0] == "boundary":
            boundary.append(pos)
        else:
            need(route[0] == "safe", "SELECTED_UNSAFE_ROTATION")
            block_id = route[1]
            need(block_id not in inside, "ROTATION_BLOCK_COLLISION")
            inside[block_id] = pos
    word = case["word"]
    n = len(word)
    cut_physical = refpos[row["z"]]
    physical_cut_order = (
        tuple(range(cut_physical + 1, n + 1)) +
        tuple(range(1, cut_physical + 1))
    )
    rank = {pos: k for k, pos in enumerate(physical_cut_order)}
    need(len(row["blocks"]) == p - 1, "WRONG_TRIPLE_BLOCK_COUNT")
    option_sets = []
    reachable = {0: ()}
    for block_id, block in enumerate(row["blocks"]):
        tick()
        options = actual_block_options(
            case, block, inside.get(block_id), rank
        )
        need(len(options) >= 2, "BLOCK_EXPONENT_SET_COLLAPSE")
        option_sets.append(tuple(sorted(options)))
        following = {}
        for old_sum, old_indices in reachable.items():
            for exponent, block_indices in options.items():
                new_sum = (old_sum + exponent) % p
                if new_sum not in following:
                    following[new_sum] = old_indices + block_indices
        reachable = following
    need(set(reachable) == set(range(p)), "SUMSET_NOT_FULL_FIELD")
    boundary_sum = sum(word[pos - 1][0] for pos in boundary) % p
    chosen = reachable[(-boundary_sum) % p] + tuple(boundary)
    need(len(chosen) == len(set(chosen)), "REUSED_PHYSICAL_OCCURRENCE")
    need(set(selected_rotations) ==
         {pos for pos in chosen if word[pos - 1][1] == 0},
         "SELECTED_ROTATIONS_NOT_RECONSTRUCTED")
    cut_indices = tuple(sorted(chosen, key=rank.__getitem__))
    need(group_product((word[i - 1] for i in cut_indices), p) == (0, 0),
         "CUT_ORDER_GROUP_PRODUCT")
    original_indices = tuple(sorted(chosen))
    verify_indices(case, original_indices, 2, 2 * p - 2)
    return {
        "indices": original_indices,
        "cut_indices": cut_indices,
        "omitted_reflection": row["z"] + 1,
        "omitted_physical": refpos[row["z"]],
        "blocks": tuple(tuple(i + 1 for i in block)
                        for block in row["blocks"]),
        "B": row["B"],
        "routes": tuple((pos,) + routes[pos] for pos in sorted(routes)),
        "selected_rotations": tuple(sorted(selected_rotations)),
        "sets": tuple(option_sets),
        "kind": kind,
        "runs": lengths,
    }


def original_group_dp(case):
    p = case["p"]
    max_reflections = 2 * p - 2
    states = {(0, 0, 0, 0): ()}
    for pos, (value, bit) in enumerate(case["word"], 1):
        tick()
        following = dict(states)
        for (rotations, reflections, x, parity), path in states.items():
            next_rotations = rotations + int(bit == 0)
            next_reflections = reflections + int(bit == 1)
            if next_rotations > 2 or next_reflections > max_reflections:
                continue
            next_x = (x - value if parity else x + value) % p
            next_parity = parity ^ bit
            key = (next_rotations, next_reflections, next_x, next_parity)
            if key not in following:
                following[key] = path + (pos,)
        states = following
    return states.get((2, max_reflections, 0, 0))


def check_case(case, prefer_interior, stats, emit=False, tag=""):
    tick()
    result = selector(case, prefer_interior)
    independent = original_group_dp(case)
    need(independent is not None, "ORIGINAL_GROUP_DP_DISAGREEMENT")
    verify_indices(case, independent, 2, 2 * case["p"] - 2)
    check_identity_conjugations(case, result["indices"], stats)
    stats["actual_case_checks"] += 1
    stats["full_group_dp_comparisons"] += 1
    route_lookup = {row[0]: row[1] for row in result["routes"]}
    for pos in result["selected_rotations"]:
        stats["selected_" + route_lookup[pos] + "_rotations"] += 1
    if emit:
        print("CASE", tag)
        print("p/raw_reflections", case["p"], case["raw_refs"])
        print("zero_based_gaps/raw_rotations", case["gaps"], case["raw_us"])
        print("actual_word", case["word"])
        print("certificate", result)
        print("independent_original_dp_indices", independent)
    return result


def local_choices(p, a, b, c, u, slot):
    if slot == 1:
        letters = ((a, 1), (u % p, 0), (b, 1), (c, 1))
    else:
        need(slot == 2, "LOCAL_SLOT_RANGE")
        letters = ((a, 1), (b, 1), (u % p, 0), (c, 1))
    reflections = tuple(i for i, g in enumerate(letters) if g[1] == 1)
    rotation = next(i for i, g in enumerate(letters) if g[1] == 0)
    answers = []
    for pair in combinations(reflections, 2):
        selected = tuple(sorted(pair + (rotation,)))
        exponent, parity = group_product((letters[i] for i in selected), p)
        need(parity == 0, "LOCAL_PAIR_PARITY")
        answers.append(exponent)
    return tuple(answers)


def exhaustive_local_interfaces(stats):
    for p in (5, 7, 11):
        for a, b, c in product(range(p), repeat=3):
            tick()
            for u in range(-p, p + 1):
                first = local_choices(p, a, b, c, u, 1)
                second = local_choices(p, a, b, c, u, 2)
                expected_first = (
                    (a - u - b) % p,
                    (a - u - c) % p,
                    (u + b - c) % p,
                )
                expected_second = (
                    (a - b + u) % p,
                    (a - u - c) % p,
                    (b - u - c) % p,
                )
                need(first == expected_first, "FIRST_INTERIOR_INTERFACE")
                need(second == expected_second, "SECOND_INTERIOR_INTERFACE")
                if b != c:
                    need(len(set(first)) >= 2, "FIRST_SAFE_GAP_COLLAPSE")
                if a != b:
                    need(len(set(second)) >= 2, "SECOND_SAFE_GAP_COLLAPSE")
                stats["local_slot_interfaces"] += 2
                stats["local_pair_products"] += 6


def source_examples(stats):
    refs_one = (0, 0, 0, 0, 0, 1, 2, 3, 4, 1, 2, 3, 4)
    case_one = build_word(5, refs_one, tuple(range(6)), (1,) * 6)
    source_one_indices = (1, 3, 4, 6, 7, 9, 13, 14, 16, 17)
    actual_projection(case_one)
    verify_indices(case_one, source_one_indices, 2, 8)
    check_identity_conjugations(case_one, source_one_indices, stats)
    need(run_type(refs_one)[1] == 9, "SOURCE_ONE_PROJECTION")
    print("SOURCE_S1_GIVEN_IDENTITY", source_one_indices, case_one["word"])
    refs_two = (0, 0, 0, 1, 0, 1, 2, 3, 4, 0, 1, 2, 3)
    case_two = build_word(5, refs_two, tuple(range(6)), (1,) * 6)
    source_two_indices = (1, 3, 5, 7, 11, 13, 14, 16, 18, 19)
    actual_projection(case_two)
    verify_indices(case_two, source_two_indices, 0, 10)
    check_identity_conjugations(case_two, source_two_indices, stats)
    need(run_type(refs_two)[1] == 11, "SOURCE_TWO_PROJECTION")
    print("SOURCE_S2_GIVEN_IDENTITY", source_two_indices, case_two["word"])
    stats["source_example_witnesses"] += 2
    return case_one


def expect_rejection(name, reason, action, logs):
    try:
        action()
    except CheckError as error:
        need(error.reason == reason, "WRONG_MUTATION_REJECTION_REASON:" + name)
    else:
        raise CheckError("MUTATION_SURVIVED:" + name)
    logs.append((name, "REJECTED", reason))


def require_coverage(covered):
    need(frozenset(covered) == EXPECTED_TYPES, "RUN_TYPE_COVERAGE")


def mutation_controls(source_case):
    logs = []
    prefix_actual = local_choices(5, 0, 1, 2, 1, 1)[2]
    prefix_wrong = (1 - 2 - 1) % 5
    expect_rejection(
        "rotation_before_both_selected_reflections",
        "INTERIOR_PREFIX_SIGN",
        lambda: need(prefix_actual == prefix_wrong, "INTERIOR_PREFIX_SIGN"),
        logs,
    )
    suffix_actual = local_choices(5, 0, 1, 2, 1, 2)[0]
    suffix_wrong = (0 - 1 - 1) % 5
    expect_rejection(
        "rotation_after_both_selected_reflections",
        "INTERIOR_SUFFIX_SIGN",
        lambda: need(suffix_actual == suffix_wrong, "INTERIOR_SUFFIX_SIGN"),
        logs,
    )
    need(0 != 1, "BAD_UNSAFE_FIRST_FIXTURE")
    first_collapsed = local_choices(5, 0, 1, 1, 2, 1)
    expect_rejection(
        "first_gap_wrong_safe_comparison",
        "SAFE_GAP_COLLAPSE",
        lambda: need(len(set(first_collapsed)) >= 2, "SAFE_GAP_COLLAPSE"),
        logs,
    )
    need(1 != 0, "BAD_UNSAFE_SECOND_FIXTURE")
    second_collapsed = local_choices(5, 1, 1, 0, 3, 2)
    expect_rejection(
        "second_gap_wrong_safe_comparison",
        "SAFE_GAP_COLLAPSE",
        lambda: need(len(set(second_collapsed)) >= 2, "SAFE_GAP_COLLAPSE"),
        logs,
    )
    double_letters = ((0, 1), (2, 0), (1, 1), (2, 0), (2, 1))
    double_options = set()
    for pair in combinations((0, 2, 4), 2):
        positions = tuple(sorted(pair + (1, 3)))
        double_options.add(group_product(
            (double_letters[i] for i in positions), 5
        ))
    need(double_options == {(4, 0)}, "BAD_DOUBLE_INTERIOR_FIXTURE")
    collision_routes = {
        2: ("safe", 0, 1, 0),
        4: ("safe", 0, 2, 1),
    }
    expect_rejection(
        "both_rotations_inside_one_block",
        "ROTATION_BLOCK_COLLISION",
        lambda: need(legal_rotation_pair(2, 4, collision_routes),
                     "ROTATION_BLOCK_COLLISION"),
        logs,
    )
    labels, _, _ = actual_projection(source_case)
    z = 2
    row = partition_row(source_case, labels, z)
    need(row is not None, "BAD_OMISSION_FIXTURE")
    adjacent_gaps = {(z - 1) % len(labels), z}
    adjacent_rotations = {
        source_case["gap_rot"][gap] for gap in adjacent_gaps
    }
    need(adjacent_rotations == {4, 6}, "BAD_ADJACENT_ROTATION_FIXTURE")
    need(all(row["routes"][pos][0] == "boundary"
             for pos in adjacent_rotations),
         "OMITTED_REFLECTION_ADJACENCY_ROUTE")
    dropped_routes = {
        pos: route for pos, route in row["routes"].items()
        if route[3] not in adjacent_gaps
    }
    expect_rejection(
        "drop_rotations_adjacent_to_omitted_reflection",
        "ROTATION_OCCURRENCE_COVERAGE",
        lambda: need(
            set(dropped_routes) == set(source_case["gap_rot"].values()),
            "ROTATION_OCCURRENCE_COVERAGE"
        ),
        logs,
    )
    expect_rejection(
        "unrequested_p3_theorem_scope",
        "OUTSIDE_ASSIGNED_PRIME_SCOPE",
        lambda: domain(3),
        logs,
    )
    four = ((0, 1), (1, 1), (2, 1), (3, 1))
    first_pair = group_product((four[0], four[2]), 5)
    second_pair = group_product((four[1], four[3]), 5)
    independently_added = mul(first_pair, second_pair, 5)
    chronological = group_product(four, 5)
    need(independently_added == (1, 0) and chronological == (3, 0),
         "BAD_NONREALIZABLE_FIXTURE")
    expect_rejection(
        "interleaved_independent_exponent_choices",
        "NONREALIZABLE_CHRONOLOGICAL_SUM",
        lambda: need(independently_added == chronological,
                     "NONREALIZABLE_CHRONOLOGICAL_SUM"),
        logs,
    )
    expect_rejection(
        "only_three_run_types_reported",
        "RUN_TYPE_COVERAGE",
        lambda: require_coverage(((5,), (4,), (3, 3))),
        logs,
    )
    nonidentity = ((0, 1), (1, 0))
    base = group_product(nonidentity, 5)
    rotated = group_product(nonidentity[1:] + nonidentity[:1], 5)
    prefix = nonidentity[0]
    conjugate = mul(mul(inverse(prefix, 5), base, 5), prefix, 5)
    need(rotated == conjugate, "NONIDENTITY_CONJUGATION_CONTROL")
    need(base == (4, 1) and rotated == (1, 1),
         "BAD_NONIDENTITY_CUT_FIXTURE")
    expect_rejection(
        "false_equality_of_nonidentity_cyclic_products",
        "FALSE_CYCLIC_INVARIANCE",
        lambda: need(base == rotated, "FALSE_CYCLIC_INVARIANCE"),
        logs,
    )
    logs.append((
        "missing_written_cyclic_conjugation_explanation",
        "NOTTESTED",
        "Proof-only omission; identity products cannot supply a counterexample."
    ))
    return logs


def deterministic_reflections(p, kind, variant):
    f = 3 * p - 2
    singles = f - sum(kind)
    if len(kind) == 1:
        run_lengths = list(kind) + [1] * singles
    else:
        left = singles // 2
        run_lengths = ([kind[0]] + [1] * left +
                       [kind[1]] + [1] * (singles - left))
    labels = [(2 * j + variant) % p for j in range(len(run_lengths))]
    if labels[-1] == labels[0]:
        labels[-1] = next(value for value in range(p)
                          if value != labels[-2] and value != labels[0])
    refs = []
    for label, length in zip(labels, run_lengths):
        refs.extend([label] * length)
    shift = (3 * sum(kind) + variant) % f
    refs = tuple(refs[shift:] + refs[:shift])
    need(run_type(refs)[2] == kind, "DETERMINISTIC_TYPE_CONSTRUCTION")
    need(len(refs) - run_type(refs)[1] == 4,
         "DETERMINISTIC_DEFICIT_CONSTRUCTION")
    return refs


def main():
    global DEADLINE
    need(len(argv) == 3 and argv[1] == "--seconds", "ARGV")
    seconds = float(argv[2])
    need(0 < seconds <= 55, "SECONDS_OUTSIDE_BOUND")
    started = monotonic()
    DEADLINE = started + seconds
    stats = Counter()
    source_case = source_examples(stats)
    mutation_logs = mutation_controls(source_case)
    exhaustive_local_interfaces(stats)
    check_case(source_case, False, stats, True, "source_S1_reconstructed")
    schemes = (
        (
            "p5_contiguous_distinct_raw",
            (0, 1, 2, 3, 4, 5),
            (0, -1, 2, -3, 4, -5),
            False,
        ),
        (
            "p5_even_gaps_distinct_raw",
            (0, 2, 4, 6, 8, 10),
            (-7, 0, 3, 8, -11, 13),
            True,
        ),
        (
            "p5_wrap_gap_repeated_label",
            (1, 3, 5, 7, 9, 12),
            (1, 1, 1, 1, 1, 1),
            False,
        ),
        (
            "p5_spread_wrap_distinct_raw",
            (0, 1, 4, 7, 10, 12),
            (5, -4, 9, 0, -2, 17),
            True,
        ),
    )
    print("BINARY_PLACEMENT_CONTROLS", schemes)
    binary_admitted_types = Counter()
    binary_case_types = Counter()
    emitted_binary = set()
    covered = set()
    for refs in product((0, 1), repeat=13):
        tick()
        stats["binary_lists_scanned"] += 1
        _, odd_runs, kind = run_type(refs)
        if odd_runs != 9:
            continue
        need(kind in EXPECTED_TYPES, "BINARY_TYPE_CLASSIFICATION")
        stats["binary_lists_admitted"] += 1
        binary_admitted_types[kind] += 1
        covered.add(kind)
        for name, gaps, us, prefer_interior in schemes:
            case = build_word(5, refs, gaps, us)
            emission_key = (name, kind)
            emit = emission_key not in emitted_binary
            check_case(case, prefer_interior, stats, emit,
                       "binary_first_witness:" + repr(emission_key))
            emitted_binary.add(emission_key)
            binary_case_types[(name, kind)] += 1
    need(stats["binary_lists_scanned"] == 2 ** 13,
         "BINARY_UNIVERSE_NOT_EXHAUSTED")
    need(stats["binary_lists_admitted"] > 0, "NO_BINARY_CASES")
    deterministic_coverage = Counter()
    ordered_types = ((5,), (4,), (3, 3), (3, 2), (2, 2))
    for p in (5, 7, 11):
        for kind in ordered_types:
            for variant in (0, 1):
                tick()
                refs = deterministic_reflections(p, kind, variant)
                f = len(refs)
                if variant == 0:
                    gaps = tuple(range(p + 1))
                else:
                    gaps = tuple((f - 1 + 2 * j) % f
                                 for j in range(p + 1))
                us = (0,) + tuple(
                    (-1 if j % 2 else 1) * (p + 2 * j + variant)
                    for j in range(1, p + 1)
                )
                case = build_word(p, refs, gaps, us)
                result = check_case(
                    case, variant == 1, stats, True,
                    "deterministic:" + repr((p, kind, variant))
                )
                need(result["kind"] == kind, "DETERMINISTIC_CASE_TYPE")
                covered.add(result["kind"])
                deterministic_coverage[(p, kind)] += 1
    require_coverage(covered)
    for p in (5, 7, 11):
        need({kind for prime, kind in deterministic_coverage if prime == p}
             == EXPECTED_TYPES, "PER_PRIME_RUN_TYPE_COVERAGE")
    need(stats["selected_safe_rotations"] > 0,
         "NO_SELECTED_INTERIOR_ROTATION_CONTROL")
    need(stats["selected_boundary_rotations"] > 0,
         "NO_SELECTED_BOUNDARY_ROTATION_CONTROL")
    tick()
    elapsed = monotonic() - started
    print("BINARY_ADMITTED_TYPES", tuple(sorted(binary_admitted_types.items())))
    print("BINARY_CASE_TYPES", tuple(sorted(binary_case_types.items())))
    print("DETERMINISTIC_COVERAGE",
          tuple(sorted(deterministic_coverage.items())))
    print("MUTATION_OUTCOMES", tuple(mutation_logs))
    print("COUNTERS", tuple(sorted(stats.items())))
    print("ELAPSED_SECONDS", elapsed)
    print("LIMITS",
          "Finite cases only; four p5 placements, not all placements; "
          "no all-prime proof, unrestricted Olson closure, all-group "
          "closure, novelty, independent-family, human, or kernel claim.")
    print("RESULT PASS FINITE_ONLY")


if __name__ == "__main__":
    try:
        main()
    except CheckError as error:
        print("RESULT NOT_COMPLETE_OR_FAILED", error.reason)
        raise SystemExit(2 if error.reason == "INCOMPLETE_TIME_LIMIT" else 1)
