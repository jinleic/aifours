#!/usr/bin/env python3
"""UNRUN p=7 one-nine-run actual-word checker; no third-party imports.

One process only. Enumerates increment patterns, not rotation assignments. Its
40-second cooperative deadline and 55-second SIGALRM outer guard report
partial work, never PASS, on timeout. The parent must review all of this source
and separately authorize one run. Output is JSON Lines on stdout only.
"""
import collections
import itertools
import json
import signal
import sys
import time

P = 7
F = 19
TARGET = 14
FULL = (1 << P) - 1
START = time.monotonic()
DEADLINE = START + 40.0
SUMMARY = {
    "candidate_increment_sequences": 0,
    "closed_patterns": 0,
    "h_counts": collections.Counter(),
    "rich_phase_counts": collections.Counter(),
    "direction_classes": collections.Counter(),
    "phase_cases": collections.Counter(),
    "offset_checks": collections.Counter(),
    "representative_words_completed": 0,
    "representative_word_results": [],
    "controls_passed": [],
    "stage": "initializing",
}


class CheckFailure(Exception):
    pass


class DeadlineExpired(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def check_deadline():
    if time.monotonic() >= DEADLINE:
        raise DeadlineExpired("cooperative-40-second-deadline")


def alarm_handler(_signum, _frame):
    raise DeadlineExpired("outer-55-second-alarm")


def emit(kind, **extra):
    payload = {"event": kind, "elapsed_seconds": round(time.monotonic() - START, 6)}
    payload.update(extra)
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")), flush=True)


def expect_rejection(reason, action):
    try:
        action()
    except CheckFailure as exc:
        require(str(exc) == reason, "control-wrong-reason:" + reason + ":" + str(exc))
    else:
        raise CheckFailure("control-not-rejected:" + reason)
    SUMMARY["controls_passed"].append(reason)


def mask(values):
    result = 0
    for value in values:
        result |= 1 << (value % P)
    return result


def members(bits):
    return [i for i in range(P) if bits & (1 << i)]


def add_masks(left, right):
    return mask((a + b for a in members(left) for b in members(right)))


def add_many(sets):
    result = 1  # {0}
    for item in sets:
        result = add_masks(result, mask(item))
    return result


def sign_class(value):
    value %= P
    require(value != 0, "zero-direction")
    return min(value, P - value)


def is_progression(values, step):
    values = set(values)
    return any({base, (base + step) % P, (base + 2 * step) % P} == values
               for base in range(P))


def progression_base(values, step):
    choices = [base for base in range(P)
               if {base, (base + step) % P, (base + 2 * step) % P} == set(values)]
    require(len(choices) == 1, "progression-base")
    return choices[0]


def pair_base(values, step):
    values = set(values)
    choices = [base for base in values if (base + step) % P in values]
    require(len(values) == 2 and len(choices) == 1, "pair-base")
    return choices[0]


def mul(left, right):
    x, e = left
    y, f = right
    return ((x + (y if e == 0 else -y)) % P, e ^ f)


def product(tokens):
    state = (0, 0)
    for _, _, exponent, parity in tokens:
        state = mul(state, (exponent, parity))
    return state


def validate_pattern(increments):
    require(len(increments) == 11, "increment-length")
    require(all(isinstance(x, int) and 1 <= x < P for x in increments), "zero-increment")
    changes = [i for i in range(1, 11) if increments[i - 1] != increments[i]]
    require(len(changes) <= 3, "too-many-changes")
    require(sum(increments) % P == 0, "closure")
    return changes


def make_reflections(increments):
    changes = validate_pattern(increments)
    x = 0
    outside = []
    for increment in increments[:10]:
        x = (x + increment) % P
        outside.append(x)
    require((x + increments[10]) % P == 0, "reconstruction-closure")
    reflections = [0] * 9 + outside
    equals = {i for i in range(F) if reflections[i] == reflections[(i + 1) % F]}
    require(equals == set(range(8)), "actual-nine-run")
    actual_rich = []
    for i in range(F):
        a, b, c = reflections[(i - 1) % F], reflections[i], reflections[(i + 1) % F]
        if len({(a - b) % P, (a - c) % P, (b - c) % P}) == 3:
            actual_rich.append(i)
    require(actual_rich == [8 + i for i in changes], "true-h")
    return reflections, changes


def blocks_for(reflections, phase):
    # phase j omits A_j, cuts after it; preserve both physical end gaps.
    omitted = phase - 1
    indices = [(omitted + 1 + k) % F for k in range(F - 1)]
    return [tuple(indices[k:k + 3]) for k in range(0, len(indices), 3)]


def analyze_phase(reflections, changes, phase):
    blocks = blocks_for(reflections, phase)
    rows = []
    for indices in blocks:
        a, b, c = (reflections[i] for i in indices)
        differences = {(a - b) % P, (a - c) % P, (b - c) % P}
        constant = a == b == c
        rich = len(differences) == 3
        row = {"indices": indices, "constant": constant, "rich": rich,
               "differences": differences}
        if not constant and not rich:
            require(len(differences) == 2, "nonrich-pair-cardinality")
            u, v = (b - a) % P, (c - b) % P
            require(u == 0 or v == 0 or u == v, "nonrich-adjacent-differences")
            direction = sign_class(u or v)
            require(sign_class((list(differences)[0] - list(differences)[1]) % P)
                    == direction, "direction-from-actual-values")
            row["direction"] = direction
        if rich:
            u, v = (b - a) % P, (c - b) % P
            require(u != 0 and v != 0 and u != v, "rich-increments")
            for d in (1, 2, 3):
                algebra = ((u == 2 * v % P and d in (v, (-v) % P)) or
                           (v == 2 * u % P and d in (u, (-u) % P)) or
                           (v == (-u) % P and d in (u, (-u) % P)))
                require(is_progression(differences, d) == algebra, "rich-progression-52")
        rows.append(row)
    r = sum(row["rich"] for row in rows)
    require(sum(row["constant"] for row in rows) == 2, "two-constant-blocks")
    require(r == sum(1 for i in changes if (i + 1 - phase) % 3 == 0),
            "rich-phase-count")
    directions = [row["direction"] for row in rows if "direction" in row]
    require(len(directions) == 4 - r, "direction-count")
    counts = collections.Counter(directions)
    d = None
    if r >= 2:
        case = "collision"
        succeeds = True
    elif r == 0:
        if len(counts) == 1:
            case = "r0-uniform"
            d = next(iter(counts))
            succeeds = False
        elif max(counts.values()) == 3:
            d = next(key for key, value in counts.items() if value == 3)
            outlier = next(key for key, value in counts.items() if value == 1)
            if outlier == sign_class(2 * d):
                case, succeeds = "r0-outlier-double", False
            else:
                case, succeeds = "r0-outlier-other", True
        else:
            case, succeeds = "r0-balanced", True
    else:
        if len(counts) >= 2:
            case, succeeds = "r1-multiple-directions", True
        else:
            d = next(iter(counts))
            rich_row = next(row for row in rows if row["rich"])
            if is_progression(rich_row["differences"], d):
                case, succeeds = "r1-uniform-progression", False
            else:
                case, succeeds = "r1-uniform-nonprogression", True
    baseline = add_many(row["differences"] for row in rows)
    require((baseline == FULL) == succeeds, "direction-sumset-classification")
    if case == "r0-uniform":
        require(baseline.bit_count() == 5, "r0-uniform-size")
    if case in ("r0-outlier-double", "r1-uniform-progression"):
        require(baseline.bit_count() == 6, "six-point-bad-size")
    return {"phase": phase, "rows": rows, "r": r, "directions": directions,
            "case": case, "succeeds": succeeds, "d": d}


def increments_to_test():
    for h in range(4):
        for changes in itertools.combinations(range(1, 11), h):
            limits = (0,) + changes + (11,)
            lengths = [limits[i + 1] - limits[i] for i in range(h + 1)]
            for slopes in itertools.product(range(1, P), repeat=h + 1):
                if any(slopes[i] == slopes[i + 1] for i in range(h)):
                    continue
                yield tuple(value for length, value in zip(lengths, slopes)
                            for _ in range(length))


def enumerate_patterns():
    SUMMARY["stage"] = "all-increment-patterns"
    representatives = {}
    for increments in increments_to_test():
        check_deadline()
        SUMMARY["candidate_increment_sequences"] += 1
        if SUMMARY["candidate_increment_sequences"] % 4096 == 0:
            emit("partial", stage=SUMMARY["stage"],
                 candidates=SUMMARY["candidate_increment_sequences"],
                 closed=SUMMARY["closed_patterns"],
                 h_counts=dict(SUMMARY["h_counts"]))
        if sum(increments) % P:
            continue
        reflections, changes = make_reflections(increments)
        h = len(changes)
        SUMMARY["closed_patterns"] += 1
        SUMMARY["h_counts"][str(h)] += 1
        phases = [analyze_phase(reflections, changes, j) for j in (1, 2, 3)]
        rich_vector = tuple(item["r"] for item in phases)
        require(sum(rich_vector) == h, "rich-phase-total")
        SUMMARY["rich_phase_counts"]["h%d:%s" % (h, ",".join(map(str, rich_vector)))] += 1
        representatives.setdefault("rich-profile:h%d:%s" % (h, rich_vector), increments)
        for item in phases:
            ds = ",".join(map(str, sorted(item["directions"]))) or "empty"
            SUMMARY["direction_classes"]["r%d:%s" % (item["r"], ds)] += 1
            SUMMARY["phase_cases"][item["case"]] += 1
            representatives.setdefault("phase-case:" + item["case"], increments)
    require(SUMMARY["candidate_increment_sequences"] == 97056, "candidate-total")
    require(dict(SUMMARY["h_counts"]) == {"1": 48, "2": 972, "3": 12744},
            "closed-pattern-counts")
    require(SUMMARY["closed_patterns"] == 13764, "closed-pattern-total")
    return representatives


def make_word(reflections, rotation_items, shift=0):
    gaps = [gap for gap, _ in rotation_items]
    require(len(gaps) == len(set(gaps)), "duplicate-physical-gap")
    require(all(isinstance(gap, int) and 0 <= gap < F for gap in gaps), "physical-gap-range")
    require(len(gaps) >= 8, "rotation-count")
    require(all(isinstance(y, int) and 0 <= y < P for _, y in rotation_items),
            "rotation-exponent")
    rotations = dict(rotation_items)
    tokens = []
    for i, x in enumerate(reflections):
        tokens.append(("f", i, x, 1))
        if i in rotations:
            tokens.append(("r", i, rotations[i], 0))
    shift %= len(tokens)
    return tokens[shift:] + tokens[:shift], rotations


def selection_product(tokens, reflection_ids, rotation_gaps):
    reflection_ids, rotation_gaps = set(reflection_ids), set(rotation_gaps)
    selected = [token for token in tokens
                if (token[0] == "f" and token[1] in reflection_ids) or
                   (token[0] == "r" and token[1] in rotation_gaps)]
    require(len(selected) == len(reflection_ids) + len(rotation_gaps), "missing-occurrence")
    return selected, product(selected)


def check_selection(tokens, reflection_ids, rotation_gaps):
    selected, result = selection_product(tokens, reflection_ids, rotation_gaps)
    require(len(selected) == TARGET, "selection-length")
    require(result == (0, 0), "selection-product")


def word_dp(tokens):
    # Dictionary keys are (number selected, rotations selected, parity, exponent).
    states = {(0, 0, 0, 0): 1}
    for kind, _, exponent, parity in tokens:
        check_deadline()
        updated = states.copy()
        for (k, rotations, e, x), count in states.items():
            if k == TARGET:
                continue
            y, f = mul((x, e), (exponent, parity))
            key = (k + 1, rotations + (kind == "r"), f, y)
            updated[key] = updated.get(key, 0) + count
        states = updated
    return {str(r): states.get((TARGET, r, 0, 0), 0)
            for r in range(0, min(TARGET, sum(t[0] == "r" for t in tokens)) + 1, 2)}


def interior_map(rows):
    return {gap: (i, side) for i, row in enumerate(rows)
            for side, gap in enumerate(row["indices"][:2])}


def block_options(reflections, row, rotations, selected_gaps, restricted):
    indices = row["indices"]
    a, b, c = (reflections[i] for i in indices)
    g1, g2 = indices[:2]
    has1, has2 = g1 in selected_gaps, g2 in selected_gaps
    u, v = rotations[g1] if has1 else 0, rotations[g2] if has2 else 0
    formula = ((b - c + u - v) % P, (a - c - u - v) % P,
               (a - b - u + v) % P)
    omissions = range(3)
    if restricted and not row["constant"]:
        require(not (has1 and has2), "restricted-two-in-one-block")
        if has1:
            omissions = (1, 2)
        elif has2:
            omissions = (0, 1)
    result = []
    for omitted in omissions:
        state = (0, 0)
        chosen = []
        for position, index in enumerate(indices):
            if position != omitted:
                state = mul(state, (reflections[index], 1))
                chosen.append(index)
            if position < 2 and index in selected_gaps:
                state = mul(state, (rotations[index], 0))
        require(state == (formula[omitted], 0), "local-sign")
        result.append((state[0], tuple(chosen)))
    return result


def family_support(reflections, phase, rotations, selected_gaps, restricted):
    rows = phase["rows"]
    interior = interior_map(rows)
    boundary = sum(rotations[gap] for gap in selected_gaps if gap not in interior) % P
    paths = {boundary: ()}
    option_rows = []
    for row in rows:
        options = block_options(reflections, row, rotations, selected_gaps, restricted)
        option_rows.append(options)
        updated = {}
        for previous, chosen in paths.items():
            for value, local_ids in options:
                updated.setdefault((previous + value) % P, chosen + local_ids)
        paths = updated
    return mask(paths), paths, option_rows, boundary


def eligible_pairs(phase, rotations):
    rows = phase["rows"]
    interior = interior_map(rows)
    rich = [i for i, row in enumerate(rows) if row["rich"]]
    protected = set(rich[:min(2, len(rich))])
    forbidden = set()
    for i, row in enumerate(rows):
        a, b, c = row["values"]
        g1, g2 = row["indices"][:2]
        if i in protected:
            forbidden.update((g1, g2))
        if not row["constant"]:
            if b == c:
                forbidden.add(g1)
            if a == b:
                forbidden.add(g2)
    require(len(forbidden) <= 5, "forbidden-gap-budget")
    available = [gap for gap in sorted(rotations) if gap not in forbidden]
    require(len(available) >= 3, "available-rotation-budget")
    pairs = []
    for left, right in itertools.combinations(available, 2):
        if left in interior and right in interior and interior[left][0] == interior[right][0]:
            continue
        pairs.append((left, right))
    require(bool(pairs), "eligible-pair-existence")
    return pairs


def check_offset_identity(phase, option_rows, boundary, support):
    case, d = phase["case"], phase["d"]
    if case not in ("r0-uniform", "r0-outlier-double", "r1-uniform-progression"):
        return
    bases = mask([boundary])
    for row, options in zip(phase["rows"], option_rows):
        values = {value for value, _ in options}
        if row["constant"]:
            bases = add_masks(bases, mask(values))
        elif row["rich"]:
            require(case == "r1-uniform-progression", "unexpected-rich-offset")
            bases = add_masks(bases, mask([progression_base(values, d)]))
        else:
            step = d
            if case == "r0-outlier-double" and row["direction"] != d:
                step = 2 * d % P
            bases = add_masks(bases, mask([pair_base(values, step)]))
    top = 4 if case == "r0-uniform" else 5
    expected = add_masks(bases, mask(k * d for k in range(top + 1)))
    require(support == expected, "offset-exact-support")
    allowed = {d, 2 * d % P} if top == 4 else {d}
    require(((support & 1) == 0) == set(members(bases)).issubset(allowed),
            "offset-zero-containment")
    SUMMARY["offset_checks"][case] += 1


def check_representative(increments, rotation_items, shift, label):
    check_deadline()
    reflections, changes = make_reflections(increments)
    tokens, rotations = make_word(reflections, rotation_items, shift)
    unshifted, _ = make_word(reflections, rotation_items, 0)
    dp = word_dp(tokens)
    require(dp == word_dp(unshifted), "cyclic-cut-dp-invariance")
    pair_successes = 0
    eligible_count = 0
    for j in (1, 2, 3):
        phase = analyze_phase(reflections, changes, j)
        for row in phase["rows"]:
            row["values"] = tuple(reflections[i] for i in row["indices"])
        eligible = set(eligible_pairs(phase, rotations))
        for pair in itertools.combinations(sorted(rotations), 2):
            check_deadline()
            selected_gaps = set(pair)
            full, paths, _, _ = family_support(reflections, phase, rotations, selected_gaps, False)
            if full & 1:
                check_selection(tokens, paths[0], selected_gaps)
                require(dp.get("2", 0) > 0, "selector-vs-group-dp")
                pair_successes += 1
            if pair not in eligible:
                continue
            eligible_count += 1
            restricted, restricted_paths, option_rows, boundary = family_support(
                reflections, phase, rotations, selected_gaps, True)
            require((restricted | full) == full, "restricted-family-subset")
            if restricted & 1:
                check_selection(tokens, restricted_paths[0], selected_gaps)
            if phase["succeeds"]:
                require(restricted == FULL, "protected-direction-selector")
            else:
                check_offset_identity(phase, option_rows, boundary, restricted)
    SUMMARY["representative_words_completed"] += 1
    SUMMARY["representative_word_results"].append({
        "label": label, "increments": increments, "rotation_items": rotation_items,
        "linear_token_shift": shift, "group_dp_identity_counts_by_rotation_count": dp,
        "phase_rotation_pairs_with_full_family_identity": pair_successes,
        "eligible_phase_rotation_pairs": eligible_count,
    })


def controls_and_author_witness():
    SUMMARY["stage"] = "controls-and-author-witness"
    witness = (4, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2)
    refs, changes = make_reflections(witness)
    require(refs[9:] == [4, 5, 6, 0, 2, 4, 6, 1, 3, 5], "author-outside-labels")
    require(changes == [1, 4], "author-rich-centers")
    require([analyze_phase(refs, changes, j)["r"] for j in (1, 2, 3)] == [0, 2, 0],
            "author-rich-phase")
    rotation_items = [(i, 0) for i in range(8)]
    tokens, _ = make_word(refs, rotation_items)
    selected_refs = (2, 3, 5, 6, 8, 10, 11, 13, 14, 16, 17, 18)
    selected_rotations = (2, 5)
    check_selection(tokens, selected_refs, selected_rotations)
    require(word_dp(tokens).get("2", 0) > 0, "author-witness-vs-dp")
    emit("author-witness", checked_occurrences=TARGET, rotation_gaps=list(selected_rotations))

    expect_rejection("zero-increment", lambda: validate_pattern((0,) + witness[1:]))
    expect_rejection("too-many-changes", lambda: validate_pattern((1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1)))
    expect_rejection("closure", lambda: validate_pattern(witness[:-1] + (3,)))
    false_cyclic_h = len(changes) + (witness[-1] != witness[0])
    expect_rejection("artificial-wrap-change", lambda: require(false_cyclic_h == len(changes),
                                                                "artificial-wrap-change"))
    expect_rejection("rich-phase-count", lambda: require(
        [analyze_phase(refs, changes, j)["r"] for j in (1, 2, 3)] == [2, 0, 0],
        "rich-phase-count"))
    expect_rejection("duplicate-physical-gap", lambda: make_word(refs, rotation_items + [(0, 2)]))
    expect_rejection("rotation-count", lambda: make_word(refs, rotation_items[:-1]))
    expect_rejection("selection-length", lambda: check_selection(tokens, selected_refs[:-1], selected_rotations))
    mutated_items = [(gap, 1 if gap == 2 else y) for gap, y in rotation_items]
    mutated_tokens, _ = make_word(refs, mutated_items)
    expect_rejection("selection-product", lambda: check_selection(mutated_tokens, selected_refs,
                                                                   selected_rotations))
    forward = mul((1, 1), (2, 0))
    backward = mul((2, 0), (1, 1))
    require(forward == (6, 1) and backward == (3, 1), "group-convention")
    expect_rejection("group-order", lambda: require(forward == backward, "group-order"))
    # Physical (0,4,5), selected g1 rotation 1, and omission of the first reflection.
    actual = mul(mul((1, 0), (4, 1)), (5, 1))
    wrong = ((4 - 5 - 1) % P, 0)
    require(actual == (0, 0) and wrong == (5, 0), "local-sign-control-fixture")
    expect_rejection("local-sign", lambda: require(actual == wrong, "local-sign"))
    actual_support = add_masks(mask([1]), mask(range(5)))
    wrong_support = add_masks(mask([0]), mask(range(5)))
    expect_rejection("boundary-offset", lambda: require(actual_support == wrong_support,
                                                         "boundary-offset"))
    # For (0,0,4) with a rotation in g2, the unsafe two omissions coincide.
    unsafe_values = {(0 - 4) % P, (0 - 4) % P}
    expect_rejection("unsafe-gap", lambda: require(len(unsafe_values) == 2, "unsafe-gap"))
    constant_values = {1, (-1) % P}
    expect_rejection("constant-choices", lambda: require(constant_values == {1}, "constant-choices"))
    return witness


def rotation_scenario(number):
    if number == 0:
        return [(i, i % P) for i in range(8)], 0
    if number == 1:
        return [((2 * i + 1) % F, (3 * i + 1) % P) for i in range(8)], 7
    return [((5 * i + 3) % F, (2 * i + 4) % P) for i in range(8)], 13


def main():
    # Unix/macOS single-process alarm; no subprocess or external timeout helper.
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, 55.0)
    try:
        witness = controls_and_author_witness()
        representatives = enumerate_patterns()
        representatives.setdefault("author-witness", witness)
        SUMMARY["stage"] = "representative-actual-words"
        for key in sorted(representatives):
            for scenario in range(3):
                rotation_items, shift = rotation_scenario(scenario)
                check_representative(representatives[key], rotation_items, shift,
                                     key + ":scenario%d" % scenario)
            emit("partial", stage=SUMMARY["stage"], completed_key=key,
                 completed_words=SUMMARY["representative_words_completed"])
        SUMMARY["stage"] = "complete"
        emit("PASS", summary=SUMMARY,
             scope="all closed p7 increment patterns with actual H<=3; only listed actual rotation scenarios",
             scientific_status="finite corroboration only, no all-rotation or all-prime claim")
        return 0
    except DeadlineExpired as exc:
        emit("INCOMPLETE_TIMEOUT", reason=str(exc), summary=SUMMARY)
        return 124
    except CheckFailure as exc:
        emit("FAIL", reason=str(exc), summary=SUMMARY)
        return 1
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.0)


if __name__ == "__main__":
    sys.exit(main())
