#!/usr/bin/env python3
"""F640: deterministic, bounded actual-word checks. CHILD SCIENCE NOT RUN.

No input files, generated files, network, subprocesses, third-party packages,
randomness, or imported project code. Output is one JSON object on stdout.
The parent must statically review and separately authorize any one-shot run.
"""

import itertools
import json
import sys
import time

START = time.monotonic()
DEADLINE = START + 45.0
STATS = {"symbolic_types": 0, "actual_words": 0, "dp_calls": 0,
         "selector_witnesses": 0, "allcut_partitions": 0,
         "three_omission_runs": 0, "negative_controls": 0}
RECORDS = []
CONTROLS = []


class CheckFailure(Exception):
    pass


class DeadlineReached(Exception):
    pass


def tick():
    if time.monotonic() >= DEADLINE:
        raise DeadlineReached("45-second cooperative deadline")


def need(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def reject(name, reason, function):
    try:
        function()
    except CheckFailure as exc:
        need(str(exc) == reason, "WRONG_CONTROL_REASON:" + name + ":" + str(exc))
        CONTROLS.append({"name": name, "expected_rejection": reason})
        STATS["negative_controls"] += 1
        return
    raise CheckFailure("MUTATION_NOT_REJECTED:" + name)


def mul(a, b, p):
    return ((a[0] + (b[0] if a[1] == 0 else -b[0])) % p,
            (a[1] + b[1]) % 2)


def inv(a, p):
    return ((-a[0] if a[1] == 0 else a[0]) % p, a[1])


def product(word, positions, p):
    result = (0, 0)
    for pos in positions:
        result = mul(result, word[pos], p)
    return result


def make_word(p, labels, gaps, forced=None, shift=0):
    forced = forced or {}
    need(len(gaps) == len(set(gaps)), "DUPLICATE_GAP_INPUT")
    need(all(0 <= g < len(labels) for g in gaps), "GAP_INPUT_RANGE")
    gaps = set(gaps)
    word = []
    for i, a in enumerate(labels):
        word.append((a % p, 1))
        if i in gaps:
            word.append((forced.get(i, 3 * i + 2) % p, 0))
    shift %= len(word)
    return word[shift:] + word[:shift]


def inspect_word(word, p):
    """Recover projection, positions, and original cyclic gaps from the word."""
    n = len(word)
    need(n > 0 and all(0 <= x < p and e in (0, 1) for x, e in word),
         "BAD_LETTER")
    refs = [i for i, (_, e) in enumerate(word) if e == 1]
    need(len(refs) == 3 * p - 2, "REFLECTION_COUNT")
    labels = [word[i][0] for i in refs]
    gap_pos = {}
    encountered = set()
    for i, pos in enumerate(refs):
        nxt = refs[(i + 1) % len(refs)]
        cursor = (pos + 1) % n
        local = []
        while cursor != nxt:
            need(word[cursor][1] == 0, "BAD_CYCLIC_GAP")
            local.append(cursor)
            encountered.add(cursor)
            cursor = (cursor + 1) % n
        need(len(local) <= 1, "NONSINGLETON_ROTATION_GAP")
        if local:
            gap_pos[i] = local[0]
    rotations = {i for i, (_, e) in enumerate(word) if e == 0}
    need(encountered == rotations and len(rotations) >= p + 1,
         "ROTATION_COVERAGE_OR_COUNT")
    return labels, refs, gap_pos


def runs(labels):
    f = len(labels)
    starts = [i for i in range(f) if labels[i] != labels[(i - 1) % f]]
    need(starts, "CONSTANT_CYCLIC_PROJECTION")
    start = starts[0]
    result = []
    current = start
    length = 0
    for k in range(f):
        i = (start + k) % f
        if k and labels[i] != labels[(i - 1) % f]:
            result.append((current, length))
            current, length = i, 0
        length += 1
    result.append((current, length))
    return result


def triple_set(labels, block, p):
    a, b, c = (labels[i] for i in block)
    return {(a - b) % p, (a - c) % p, (b - c) % p}


def properties(labels, p):
    f = len(labels)
    rr = runs(labels)
    lengths = tuple(sorted((length for _, length in rr if length > 1), reverse=True))
    odd = sum(length % 2 for _, length in rr)
    e = sum(length - 1 for _, length in rr)
    c = sum(max(length - 2, 0) for _, length in rr)
    rich = []
    const = []
    for i in range(f):
        block = (i, (i + 1) % f, (i + 2) % f)
        rich.append(len(triple_set(labels, block, p)) == 3)
        const.append(labels[block[0]] == labels[block[1]] == labels[block[2]])
    need(sum(const) == c, "CYCLIC_CONSTANT_WINDOW_COUNT")
    return {"runs": rr, "type": lengths, "odd": odd, "D": f - odd,
            "E": e, "C": c, "H": sum(rich), "rich": rich, "const": const}


def blocks_for(labels, p, z):
    f = len(labels)
    blocks = [tuple((z + 1 + 3 * j + k) % f for k in range(3))
              for j in range(p - 1)]
    flat = [i for block in blocks for i in block]
    need(len(flat) == f - 1 and len(set(flat)) == f - 1 and z not in flat,
         "OMISSION_PARTITION_NOT_DISJOINT")
    return blocks


def block_counts(labels, blocks, p):
    rich = [j for j, block in enumerate(blocks)
            if len(triple_set(labels, block, p)) == 3]
    const = [j for j, block in enumerate(blocks)
             if labels[block[0]] == labels[block[1]] == labels[block[2]]]
    inside_equal = sum((labels[b[0]] == labels[b[1]]) +
                       (labels[b[1]] == labels[b[2]]) for b in blocks)
    return rich, const, inside_equal


def check_incidence(labels, p, prop):
    """All cuts and every first-three omission in every long run."""
    f = len(labels)
    incidence = [0] * f
    differences = []
    for z in range(f):
        tick()
        blocks = blocks_for(labels, p, z)
        rich, const, _ = block_counts(labels, blocks, p)
        differences.append(len(rich) - len(const))
        for block in blocks:
            incidence[block[0]] += 1
        STATS["allcut_partitions"] += 1
    need(incidence == [p - 1] * f, "ALLCUT_WINDOW_INCIDENCE")
    need(sum(differences) == (p - 1) * (prop["H"] - prop["C"]),
         "ALLCUT_RICH_CONSTANT_SUM")
    if prop["C"] - prop["H"] <= 3:
        need(any(d >= 0 for d in differences), "ALLCUT_THREE_THRESHOLD")

    for start, length in prop["runs"]:
        if length < 3:
            continue
        tick()
        selected = [0] * f
        local_losses = []
        run_edges = {(start + j) % f for j in range(length - 1)}
        chosen_constants = {(start + j) % f for j in range(length - 2)}
        differences3 = []
        for k in (1, 2, 3):
            z = (start + k - 1) % f
            blocks = blocks_for(labels, p, z)
            rich, const, inside_equal = block_counts(labels, blocks, p)
            differences3.append(len(rich) - len(const))
            internal_edges = set()
            for block in blocks:
                selected[block[0]] += 1
                internal_edges.update((block[0], block[1]))
            local_losses.append(length - 1 - len(run_edges & internal_edges))
            need(inside_equal <= prop["E"] - (length + 1) // 3,
                 "THREE_OMISSION_ROTATION_BUDGET")
        ceil3 = lambda x: (x + 2) // 3
        expected_losses = [ceil3(length - 1), 1 + ceil3(length - 2),
                           1 + ceil3(length - 3)]
        need(local_losses == expected_losses, "THREE_OMISSION_EXACT_RUN_LOSSES")
        need(min(local_losses) == (length + 1) // 3, "THREE_OMISSION_MIN_LOSS")
        for i in range(f):
            if prop["rich"][i]:
                need(selected[i] == 1, "THREE_OMISSION_RICH_INCIDENCE")
            if prop["const"][i] and i not in chosen_constants:
                need(selected[i] == 1, "THREE_OMISSION_OTHER_CONSTANT_INCIDENCE")
        need(sum(selected[i] for i in chosen_constants) == length - 3,
             "THREE_OMISSION_CHOSEN_CONSTANT_INCIDENCE")
        need(sum(selected[i] for i in range(f) if prop["rich"][i]) == prop["H"],
             "THREE_OMISSION_RICH_SUM")
        need(sum(selected[i] for i in range(f) if prop["const"][i]) == prop["C"] - 1,
             "THREE_OMISSION_CONSTANT_SUM")
        boundaries = ((start - 2) % f, (start + length - 1) % f)
        need(boundaries[0] != boundaries[1] and
             all(selected[i] == 1 for i in boundaries),
             "THREE_OMISSION_BOUNDARY_WINDOWS")
        if prop["C"] - prop["H"] <= 3:
            need(any(d >= 0 for d in differences3), "THREE_OMISSION_DOMINANCE")
        STATS["three_omission_runs"] += 1
    return differences


def rotate_bits(mask, shift, p):
    shift %= p
    return ((mask << shift) | (mask >> (p - shift))) & ((1 << p) - 1)


def exact_original_dp(word, p):
    """Original linear order, exact 2p letters, exactly two rotations."""
    target = 2 * p
    dp = [[[0, 0] for _ in range(3)] for _ in range(target + 1)]
    dp[0][0][0] = 1
    for seen, (x, is_reflection) in enumerate(word, 1):
        tick()
        for length in range(min(target, seen), 0, -1):
            for nrot in range(3):
                oldrot = nrot - (1 - is_reflection)
                if oldrot < 0:
                    continue
                for parity in (0, 1):
                    old = dp[length - 1][oldrot][parity]
                    if old:
                        new_parity = parity ^ is_reflection
                        signed_x = x if parity == 0 else -x
                        dp[length][nrot][new_parity] |= rotate_bits(old, signed_x, p)
    STATS["dp_calls"] += 1
    return bool(dp[target][2][0] & 1)


def local_products(word, p, refs, gap_pos, z, block, chosen_gaps):
    n = len(word)
    cut = (refs[z] + 1) % n
    rank = lambda pos: (pos - cut) % n
    rotations = [gap_pos[g] for g in chosen_gaps]
    values = {}
    per_pair = {}
    for pair in itertools.combinations(block, 2):
        positions = sorted([refs[i] for i in pair] + rotations, key=rank)
        value = product(word, positions, p)
        need(value[1] == 0, "LOCAL_PAIR_NOT_ROTATION")
        per_pair[pair] = value[0]
        values.setdefault(value[0], tuple(refs[i] for i in pair))
    return values, per_pair


def gap_sets(labels, blocks, protected):
    unsafe = set()
    protected_gaps = set()
    interior_owner = {}
    for j, (a, b, c) in enumerate(blocks):
        interior_owner[a] = j
        interior_owner[b] = j
        if j in protected:
            protected_gaps.update((a, b))
        if not (labels[a] == labels[b] == labels[c]):
            if labels[b] == labels[c]:
                unsafe.add(a)
            if labels[a] == labels[b]:
                unsafe.add(b)
    return unsafe, protected_gaps, interior_owner


def build_selector(word, p, labels, refs, gap_pos, z, protected, mode):
    """Construct and verify physical occurrences, independently of full DP."""
    blocks = blocks_for(labels, p, z)
    rich, const, inside_equal = block_counts(labels, blocks, p)
    unsafe, protected_gaps, owner = gap_sets(labels, blocks, protected)
    forbidden = unsafe | protected_gaps
    if mode == "rich_compensation":
        need(len(protected) == len(const) and set(protected) <= set(rich),
             "BAD_RICH_PROTECTION")
        need(len(forbidden) == inside_equal and inside_equal <= p - 2,
             "BAD_STANDARD_ROTATION_BUDGET")
    eligible = sorted(g for g in gap_pos if g not in forbidden)
    need(len(eligible) >= 3, "FEWER_THAN_THREE_ELIGIBLE_ROTATIONS")
    chosen = None
    for a, b in itertools.combinations(eligible, 2):
        if a not in owner or b not in owner or owner[a] != owner[b]:
            chosen = (a, b)
            break
    need(chosen is not None, "NO_PHYSICAL_ROTATION_PAIR")
    tables = []
    for j, block in enumerate(blocks):
        interior = [g for g in chosen if owner.get(g) == j]
        need(len(interior) <= 1, "TWO_INTERIOR_ROTATIONS")
        values, _ = local_products(word, p, refs, gap_pos, z, block, interior)
        tables.append(values)
        if j not in const:
            need(len(values) >= 2, "UNSAFE_NONCONSTANT_BLOCK")
        if mode == "rich_compensation" and j in protected:
            need(len(values) == 3, "PROTECTED_RICH_COLLAPSED")
    if mode == "rich_compensation":
        need(sum(len(values) - 1 for values in tables) >= p - 1,
             "MISSING_CONSTANT_COMPENSATION")
    else:
        need(mode == "exception_4_plus_4" and set(protected) == {1, 2},
             "UNKNOWN_SELECTOR_MODE")
        need(const == [0], "EXCEPTION_CONSTANT_BLOCK")
        joint = {(x + y) % p for x in tables[1] for y in tables[2]}
        need(len(tables[1]) == len(tables[2]) == 2 and len(joint) == 4,
             "EXCEPTION_TWO_DIRECTION_GROWTH")
        need(len(unsafe) == 2 and len(protected_gaps) == 4 and
             unsafe <= protected_gaps and len(forbidden) == 4,
             "EXCEPTION_FOUR_NOT_SIX")
    boundary = [g for g in chosen if g not in owner]
    offset = sum(word[gap_pos[g]][0] for g in boundary) % p
    states = {0: ()}
    for values in tables:
        new = {}
        for total, positions in states.items():
            for value, pair in values.items():
                new.setdefault((total + value) % p, positions + pair)
        states = new
    need(set(states) == set(range(p)), "BLOCK_SUMSET_NOT_FIELD")
    chosen_refs = states[(-offset) % p]
    positions = sorted(chosen_refs + tuple(gap_pos[g] for g in chosen))
    need(len(positions) == 2 * p and len(set(positions)) == 2 * p,
         "SELECTED_OCCURRENCES_NOT_DISTINCT_2P")
    need(sum(word[i][1] == 0 for i in positions) == 2,
         "SELECTED_ROTATION_COUNT")
    whole = product(word, positions, p)
    need(whole == (0, 0), "SELECTOR_NOT_ORIGINAL_ORDER_IDENTITY")
    # Check the actual conjugation identity, not a commutativity assertion.
    for k in range(len(positions) + 1):
        u = product(word, positions[:k], p)
        v = product(word, positions[k:], p)
        need(mul(v, u, p) == mul(inv(u, p), mul(whole, u, p), p),
             "ACTUAL_CUT_CONJUGATION")
    STATS["selector_witnesses"] += 1
    return {"omitted_reflection_index": z,
            "protected_block_indices": sorted(protected),
            "constant_blocks": len(const), "rich_blocks": len(rich),
            "forbidden_gap_indices": sorted(forbidden),
            "chosen_rotation_gap_indices": list(chosen),
            "selected_original_word_positions_zero_based": positions,
            "block_set_sizes": [len(x) for x in tables],
            "boundary_offset": offset}


def find_selector(word, p, labels, refs, gap_pos):
    for z in range(len(labels)):
        blocks = blocks_for(labels, p, z)
        rich, const, inside_equal = block_counts(labels, blocks, p)
        if len(rich) >= len(const) and inside_equal <= p - 2:
            return build_selector(word, p, labels, refs, gap_pos, z,
                                  set(rich[:len(const)]), "rich_compensation")
    return None


def partitions(n, ceiling):
    if n == 0:
        yield ()
    else:
        for part in range(min(n, ceiling), 0, -1):
            for suffix in partitions(n - part, part):
                yield (part,) + suffix


EXPECTED = {
    (9,): (7, 8, 5), (8,): (6, 7, 4),
    (7, 3): (6, 8, 6), (7, 2): (5, 7, 5),
    (6, 3): (5, 7, 5), (6, 2): (4, 6, 4),
    (5, 5): (6, 8, 6), (5, 4): (5, 7, 5),
    (4, 4): (4, 6, 5), (5, 3, 3): (5, 8, 6),
    (5, 3, 2): (4, 7, 5), (5, 2, 2): (3, 6, 4),
    (4, 3, 3): (4, 7, 6), (4, 3, 2): (3, 6, 5),
    (4, 2, 2): (2, 5, 4), (3, 3, 3, 3): (4, 8, 7),
    (3, 3, 3, 2): (3, 7, 6), (3, 3, 2, 2): (2, 6, 5),
    (3, 2, 2, 2): (1, 5, 4), (2, 2, 2, 2): (0, 4, None),
}
WHOLE_TYPES = {(4, 4), (5, 2, 2), (4, 3, 2), (4, 2, 2),
               (3, 3, 3, 2), (3, 3, 2, 2), (3, 2, 2, 2),
               (2, 2, 2, 2)}


def symbolic_table():
    generated = set()
    for partition in partitions(4, 4):
        for bits in itertools.product((0, 1), repeat=len(partition)):
            generated.add(tuple(sorted((2 * a + b for a, b in zip(partition, bits)),
                                       reverse=True)))
    need(len(generated) == 20 and generated == set(EXPECTED), "D8_TYPE_SET")
    rows = []
    for typ in sorted(generated, reverse=True):
        need(sum((length - 1 if length % 2 else length) for length in typ) == 8,
             "D8_TYPE_DEFICIT")
        c = sum(max(length - 2, 0) for length in typ)
        e = sum(length - 1 for length in typ)
        largest = max(typ)
        k = e - (largest + 1) // 3 if largest >= 3 else None
        need((c, e, k) == EXPECTED[typ], "D8_C_E_K_TABLE:" + str(typ))
        rows.append({"type": list(typ), "C": c, "E": e, "K": k,
                     "whole_type_author_claim": typ in WHOLE_TYPES})
        STATS["symbolic_types"] += 1
    return rows


def generated_labels(p, typ):
    f = 3 * p - 2
    singletons = f - sum(typ)
    need(singletons >= 1, "NEGATIVE_SINGLETON_COUNT")
    lengths = list(typ) + [1] * singletons
    run_labels = [0]
    for i in range(1, len(lengths)):
        step = 1 + (i % 2)
        a = (run_labels[-1] + step) % p
        if i == len(lengths) - 1 and a == run_labels[0]:
            a = (run_labels[-1] + (3 - step)) % p
        need(a != run_labels[-1], "ADJACENT_RUN_LABELS_EQUAL")
        run_labels.append(a)
    need(run_labels[-1] != run_labels[0], "CYCLIC_RUN_LABELS_EQUAL")
    return [a for a, length in zip(run_labels, lengths) for _ in range(length)]


def gap_layout(f, p, variant):
    if variant == 0:
        return [(2 * i + 1) % f for i in range(p + 1)]
    return list(range(p + 1))


def check_case(p, typ, variant, kind):
    tick()
    labels0 = generated_labels(p, typ)
    word = make_word(p, labels0, gap_layout(len(labels0), p, variant),
                     shift=variant)
    labels, refs, gap_pos = inspect_word(word, p)
    prop = properties(labels, p)
    need(prop["type"] == typ and prop["odd"] >= p + 4, "ACTUAL_TYPE_OR_DOMAIN")
    check_incidence(labels, p, prop)
    maxrun = max(typ) if typ else 1
    k = prop["E"] - (maxrun + 1) // 3 if maxrun >= 3 else None
    a_region = prop["C"] - prop["H"] <= 3 and prop["E"] <= p - 2
    b_region = (prop["C"] - prop["H"] <= 3 and k is not None and k <= p - 2)
    whole = kind == "D8" and typ in WHOLE_TYPES
    in_scope = whole or a_region or b_region or kind == "UNIFORM_FAMILY"
    if kind == "D8":
        need(prop["D"] == 8 and (prop["C"], prop["E"], k) == EXPECTED[typ],
             "ACTUAL_D8_TABLE_MISMATCH")
        if p == 11 or whole or typ in {(9,), (8,), (7, 2), (6, 3),
                                       (6, 2), (5, 4), (5, 3, 2)}:
            need(in_scope, "REQUIRED_REPRESENTED_SCOPE_MISSING")
        else:
            need(not in_scope, "UNEXPECTED_SCOPE_CLASSIFICATION")
    selector = find_selector(word, p, labels, refs, gap_pos)
    dp = exact_original_dp(word, p)
    if in_scope:
        need(selector is not None, "IN_SCOPE_SELECTOR_NOT_FOUND")
        need(dp, "SELECTOR_DP_DISAGREEMENT")
    if selector is not None:
        need(dp, "PHYSICAL_SELECTOR_DP_DISAGREEMENT")
    record = {"kind": kind, "p": p, "type": list(typ), "variant": variant,
              "scope": ("WHOLE_TYPE_REPRESENTATIVE" if whole else
                        "CONDITIONAL_OR_UNIFORM_REPRESENTATIVE" if in_scope else
                        "OUT_OF_SCOPE_NOT_AN_AVOIDER"),
              "C": prop["C"], "E": prop["E"], "K": k, "H": prop["H"],
              "allcut_A_hypotheses": a_region, "three_omission_B_hypotheses": b_region,
              "actual_word_x_parity": [list(letter) for letter in word],
              "original_order_exact_2p_two_rotation_dp": dp,
              "physical_selector": selector}
    RECORDS.append(record)
    STATS["actual_words"] += 1


def exception_word(p):
    # u=1, v=3p-11, a=0, d=5, e=1; all values in F_p.
    a, d, e = 0, 5 % p, 1
    b = (a + 2 * d) % p
    v = 3 * p - 11
    labels = [a] * 4 + [(a + d) % p] + [b] * 4
    labels += [(b + (j + 1) * e) % p for j in range(v)]
    f = len(labels)
    selected_gaps = {0, f - 1, 4, 5, 7, 8}
    for g in range(f):
        if len(selected_gaps) >= p + 1:
            break
        selected_gaps.add(g)
    return make_word(p, labels, sorted(selected_gaps), {0: 1, f - 1: 2}), d, e


def check_exception(p):
    word, d, e = exception_word(p)
    labels, refs, gap_pos = inspect_word(word, p)
    prop = properties(labels, p)
    need(prop["type"] == (4, 4) and prop["D"] == 8 and prop["H"] == 0 and
         prop["C"] == 4 and prop["E"] == 6, "EXCEPTION_ACTUAL_SCOPE")
    need(d and e and d != e and d != (-e) % p, "EXCEPTION_BAD_DIRECTIONS")
    need((2 * d + (3 * p - 10) * e) % p == 0, "EXCEPTION_ENDPOINT")
    diffs = check_incidence(labels, p, prop)
    need(all(difference < 0 for difference in diffs), "EXCEPTION_CUT_NOT_DEFICIENT")
    selector = build_selector(word, p, labels, refs, gap_pos, 0, {1, 2},
                              "exception_4_plus_4")
    need(exact_original_dp(word, p), "EXCEPTION_DP_DISAGREEMENT")
    RECORDS.append({"kind": "EXCEPTION_4_PLUS_4_H0", "p": p,
                    "scope": "WHOLE_TYPE_EXCEPTION_REPRESENTATIVE",
                    "u": 1, "v": 3 * p - 11, "d": d, "e": e,
                    "actual_word_x_parity": [list(letter) for letter in word],
                    "C": prop["C"], "E": prop["E"], "H": prop["H"],
                    "allcut_differences": diffs,
                    "original_order_exact_2p_two_rotation_dp": True,
                    "physical_selector": selector})
    STATS["actual_words"] += 1
    return word, labels, refs, gap_pos, prop, diffs


def mutation_controls(exception):
    p = 7
    labels0 = [0] * 9 + [1, 2, 4, 5, 1, 2, 4, 5, 1, 2]
    f = len(labels0)
    gaps = {0, f - 1, 9, 10}
    for g in range(f):
        if len(gaps) >= p + 1:
            break
        gaps.add(g)
    word = make_word(p, labels0, sorted(gaps), {0: 1, f - 1: 2, 9: 3, 10: 3})
    labels, refs, gap_pos = inspect_word(word, p)
    prop = properties(labels, p)
    need(prop["type"] == (9,) and prop["D"] == 8, "CONTROL_WORD_NOT_ACTUAL_D8")
    tri = (9, 10, 11)
    a, b, c, u = labels[9], labels[10], labels[11], word[gap_pos[9]][0]
    plain, _ = local_products(word, p, refs, gap_pos, 0, tri, [])
    first, first_pairs = local_products(word, p, refs, gap_pos, 0, tri, [9])
    second, second_pairs = local_products(word, p, refs, gap_pos, 0, tri, [10])
    need(first_pairs == {(9, 10): (a - u - b) % p,
                         (9, 11): (a - u - c) % p,
                         (10, 11): (u + b - c) % p}, "FIRST_GAP_FORMULA")
    need(second_pairs == {(9, 10): (a - b + u) % p,
                          (9, 11): (a - u - c) % p,
                          (10, 11): (b - u - c) % p}, "SECOND_GAP_FORMULA")
    reject("prefix_rotation_wrong_sign", "PREFIX_SIGN",
           lambda: need(first_pairs[(10, 11)] == (-u + b - c) % p, "PREFIX_SIGN"))
    reject("suffix_rotation_wrong_sign", "SUFFIX_SIGN",
           lambda: need(second_pairs[(9, 10)] == (a - b - u) % p, "SUFFIX_SIGN"))
    need(len(plain) == 3 and len(first) == 2, "RICH_COLLAPSE_FIXTURE")
    reject("unprotected_rich_block_claims_three", "RICH_NOT_PROTECTED",
           lambda: need(len(first) >= 3, "RICH_NOT_PROTECTED"))

    # These are two selected occurrences in the same complete physical word.
    u_group = word[refs[9]]
    v_group = word[refs[10]]
    original = mul(u_group, v_group, p)
    rotated = mul(v_group, u_group, p)
    need(rotated == mul(inv(u_group, p), mul(original, u_group, p), p) and
         original != rotated, "NONIDENTITY_CONJUGATION_FIXTURE")
    reject("false_cyclic_product_invariance", "CUT_NONCOMMUTATIVE",
           lambda: need(original == rotated, "CUT_NONCOMMUTATIVE"))

    z = 0
    blocks = blocks_for(labels, p, z)
    adjacent = (gap_pos[z], gap_pos[(z - 1) % f])
    need(adjacent[0] != adjacent[1], "BOUNDARY_OCCURRENCES_NOT_DISTINCT")
    _, _, owner = gap_sets(labels, blocks, set())
    need(z not in owner and (z - 1) % f not in owner,
         "OMISSION_ADJACENCIES_NOT_BOUNDARY")
    reflection_positions = [refs[i] for block in blocks for i in block[:2]]
    complete = sorted(reflection_positions + list(adjacent))
    need(len(complete) == 2 * p and len(set(complete)) == 2 * p,
         "BOUNDARY_CONTROL_NOT_2P_PHYSICAL")
    original_product = product(word, complete, p)
    for omitted in adjacent:
        need(product(word, [i for i in complete if i != omitted], p) != original_product,
             "BOUNDARY_DROP_DID_NOT_CHANGE_PHYSICAL_PRODUCT")
    def require_both(items):
        need(len(items) == 2 and len(set(items)) == 2 and set(items) == set(adjacent),
             "BOUNDARY_OCCURRENCES")
    require_both(list(adjacent))
    reject("drop_rotation_adjacent_to_omission", "BOUNDARY_OCCURRENCES",
           lambda: require_both([adjacent[0]]))
    reject("merge_two_boundary_occurrences", "BOUNDARY_OCCURRENCES",
           lambda: require_both([adjacent[0], adjacent[0]]))

    ew, elabels, erefs, egaps, eprop, diffs = exception
    eblocks = blocks_for(elabels, p, 0)
    unsafe, protected, _ = gap_sets(elabels, eblocks, {1, 2})
    need(len(unsafe) == 2 and len(protected) == 4 and unsafe <= protected and
         len(unsafe | protected) == 4, "FOUR_VS_SIX_FIXTURE")
    need(len(set(egaps) & protected) == 4, "PROTECTED_GAPS_NOT_PHYSICAL")
    reject("six_claimed_as_distinct_forbidden_gaps", "PROTECTED_OVERCOUNT",
           lambda: need(len(unsafe) + len(protected) == len(unsafe | protected),
                        "PROTECTED_OVERCOUNT"))
    constant, _ = local_products(ew, p, erefs, egaps, 0, eblocks[0], [])
    need(len(constant) == 1, "CONSTANT_BLOCK_FIXTURE")
    reject("constant_block_falsely_has_two_choices", "CONSTANT_NOT_COMPENSATED",
           lambda: need(len(constant) >= 2, "CONSTANT_NOT_COMPENSATED"))
    need(eprop["C"] - eprop["H"] == 4 and all(x < 0 for x in diffs),
         "PHYSICAL_FOUR_THRESHOLD_FIXTURE")
    reject("replace_allcut_three_by_four", "ALLCUT_FOUR_UNSOUND",
           lambda: need(any(x >= 0 for x in diffs), "ALLCUT_FOUR_UNSOUND"))
    RECORDS.append({"kind": "PHYSICAL_MUTATION_CONTROL_WORD", "p": p,
                    "scope": "CONTROL_NOT_AVOIDER",
                    "actual_word_x_parity": [list(letter) for letter in word],
                    "omitted_reflection_index": z,
                    "two_adjacent_boundary_positions_zero_based": list(adjacent),
                    "selected_original_word_positions_zero_based": complete,
                    "selected_product": list(original_product),
                    "plain_rich_size": len(plain), "unprotected_rich_size": len(first)})
    STATS["actual_words"] += 1


def main():
    table = symbolic_table()
    for p in (7, 11):
        for typ in sorted(EXPECTED, reverse=True):
            for variant in (0, 1):
                check_case(p, typ, variant, "D8")
    uniform = {7: [(3, 2), (4,), (5,)],
               11: [(3, 3, 3, 2, 2), (4, 3, 2, 2), (5, 2, 2, 2)]}
    for p in (7, 11):
        for typ in uniform[p]:
            check_case(p, typ, 0, "UNIFORM_FAMILY")
    ex7 = check_exception(7)
    check_exception(11)
    mutation_controls(ex7)
    need(STATS["symbolic_types"] == 20 and STATS["negative_controls"] == 9,
         "INCOMPLETE_TABLE_OR_CONTROL_INVENTORY")
    tick()
    return {"status": "PASS", "scientific_scope": "BOUNDED_ACTUAL_WORDS_ONLY",
            "symbolic_table": table, "statistics": STATS,
            "negative_controls": CONTROLS, "actual_word_records": RECORDS,
            "elapsed_seconds_before_json_output": time.monotonic() - START,
            "limitations": ["No all-prime or whole-deficit-eight conclusion",
                            "OUT_OF_SCOPE is not an avoiding-word certificate",
                            "No deficit-six author-candidate adoption",
                            "No human, kernel, independent-family or novelty claim"]}


if __name__ == "__main__":
    try:
        result = main()
    except DeadlineReached as exc:
        result = {"status": "INCOMPLETE_DEADLINE", "reason": str(exc),
                  "statistics": STATS, "negative_controls": CONTROLS,
                  "completed_actual_word_records": RECORDS}
    except CheckFailure as exc:
        result = {"status": "FAIL", "reason": str(exc), "statistics": STATS,
                  "negative_controls": CONTROLS, "completed_actual_word_records": RECORDS}
    except Exception as exc:
        result = {"status": "ERROR", "exception_type": type(exc).__name__,
                  "reason": str(exc), "statistics": STATS,
                  "negative_controls": CONTROLS, "completed_actual_word_records": RECORDS}
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    if result["status"] != "PASS":
        sys.exit(1)
