#!/usr/bin/env python3
"""UNRUN exact necessary-support scrutiny; not an AME feasibility solver.

One-shot parent permission and a full parent source read are required before use.
No input files, subprocesses, randomness, floating-point mathematics, network,
external packages, or result files.  Only monotonic time uses floating point.
The parent must supervise with an outer limit at most 55 seconds; this program
self-interrupts by 39 seconds and emits INCOMPLETE rather than a partial PASS.
"""

from collections import Counter, defaultdict
from itertools import combinations, product
import json
import signal
import time

START = time.monotonic()
INTERNAL_SECONDS = 39.0
CUTS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
PAIRS = tuple(combinations(range(4), 2))
WORDS = tuple(product(range(2), repeat=4))
AB_FULL = frozenset(((0, 0), (1, 1)))
AB_OTHER = tuple(p for p in product(range(4), repeat=2) if p not in AB_FULL)
LOW_CD = tuple(product((2, 3), repeat=2))
PARTITIONS = (
    ("axis_C", ((0, 1), (2, 3))),
    ("axis_D", ((0, 2), (1, 3))),
    ("diagonal", ((0, 3), (1, 2))),
)
PROGRESS = {"phase": "starting"}


class Deadline(Exception):
    pass


def alarm_handler(_signum, _frame):
    raise Deadline("internal deadline")


def guard():
    if time.monotonic() - START >= INTERNAL_SECONDS:
        raise Deadline("internal deadline")


def emit(kind, **fields):
    print(json.dumps({"status": kind, **fields}, sort_keys=True), flush=True)


def pair_of(word, pair):
    return (word[pair[0]], word[pair[1]])


def complement(pair):
    return tuple(i for i in range(4) if i not in pair)


def mask_cut_type(mask, left, right):
    n = mask.bit_count()
    if n not in (8, 12):
        return "other"
    rows = [0, 0, 0, 0]
    for k, w in enumerate(WORDS):
        if mask & (1 << k):
            r = 2 * w[left[0]] + w[left[1]]
            c = 2 * w[right[0]] + w[right[1]]
            rows[r] |= 1 << c
    if n == 12:
        cols = [sum(bool(r & (1 << c)) for r in rows) for c in range(4)]
        return "Y" if all(r.bit_count() == 3 for r in rows) and cols == [3] * 4 else "other"
    if any(r.bit_count() != 2 for r in rows):
        return "other"
    distinct = set(rows)
    if len(distinct) != 2 or any(rows.count(r) != 2 for r in distinct):
        return "other"
    a, b = tuple(distinct)
    return "X" if a & b == 0 and a | b == 15 else "other"


def high_support_scrutiny():
    by_count_and_cuts = Counter()
    x_all = []
    y_all = []
    for mask in range(1 << 16):
        if mask % 1024 == 0:
            guard()
        types = tuple(mask_cut_type(mask, l, r) for l, r in CUTS)
        by_count_and_cuts[(mask.bit_count(), *types)] += 1
        if types == ("X", "X", "X"):
            x_all.append(mask)
        if types == ("Y", "Y", "Y"):
            y_all.append(mask)
    parity_masks = set()
    for coordinates in combinations(range(4), 3):
        for parity in (0, 1):
            parity_masks.add(sum(1 << k for k, w in enumerate(WORDS)
                                 if sum(w[i] for i in coordinates) % 2 == parity))
    for parity in (0, 1):
        parity_masks.add(sum(1 << k for k, w in enumerate(WORDS)
                             if sum(w) % 2 == parity))
    zero_patterns = []
    for chosen in combinations(range(16), 4):
        if all(len({pair_of(WORDS[k], p) for k in chosen}) == 4 for p in PAIRS):
            zero_patterns.append(chosen)
    if set(x_all) != parity_masks or len(parity_masks) != 10:
        raise AssertionError("three-cut X classification differs from ten parity supports")
    if y_all or zero_patterns:
        raise AssertionError("unexpected four-word six-pair-bijective zero pattern")
    return {
        "masks_visited": 1 << 16,
        "count_cut_type_table": [
            {"size": k[0], "cuts": list(k[1:]), "count": n}
            for k, n in sorted(by_count_and_cuts.items())
        ],
        "three_cut_X_masks": x_all,
        "three_cut_X_parity_masks": sorted(parity_masks),
        "three_cut_Y_masks": y_all,
        "four_word_zero_sets_checked": 1820,
        "six_pair_bijective_zero_sets": zero_patterns,
    }


def cap(pair, value):
    if pair == (0, 1):
        return 4 if value in AB_FULL else 2
    return 3 if value[0] < 2 and value[1] < 2 else 2


def projections(words, pair):
    other = complement(pair)
    out = defaultdict(set)
    for word in words:
        out[pair_of(word, pair)].add(pair_of(word, other))
    return out


def saturated_one_overlap(words):
    for pair in PAIRS:
        rows = projections(words, pair)
        saturated = [(p, v) for p, v in rows.items() if len(v) == cap(pair, p)]
        for (p, v), (q, z) in combinations(saturated, 2):
            common = v & z
            if len(common) == 1:
                return {"pair": pair, "rows": (p, q), "common": tuple(common)}
    return None


def partial_status(words, enforce_one_overlap=True):
    if len(set(words)) != len(words):
        return False, "duplicate_word"
    for pair in PAIRS:
        rows = projections(words, pair)
        for p, support in rows.items():
            if len(support) > cap(pair, p):
                return False, "pair_multiplicity"
        # The high C,D degrees are three and their low degrees two.  The
        # corresponding E-neighbor bound is required in every other party.
        for side, party in enumerate(pair):
            if party not in (2, 3):
                continue
            for symbol in range(4):
                neighbors = {p[1 - side] for p in rows if p[side] == symbol}
                if len(neighbors) > (3 if symbol < 2 else 2):
                    return False, "CD_degree"
    if enforce_one_overlap:
        bad = saturated_one_overlap(words)
        if bad is not None:
            return False, "saturated_one_overlap"
    return True, "ok"


def core_words(row0, row1, support0, support1):
    words = [(a, b, c, d) for a, b in sorted(AB_FULL)
             for c, d in product(range(2), repeat=2)]
    for (a, b), support in ((row0, support0), (row1, support1)):
        words.extend((a, b, p // 2, p % 2) for p in support)
    return tuple(sorted(words))


def row_type(row):
    a, b = row
    return ("X" if a < 2 and b < 2 else
            "Y" if a < 2 else "Z" if b < 2 else "W")


def closed_high_box(core):
    if any(any(x >= 2 for x in w) for w in core):
        return False
    for pair in PAIRS:
        rows = projections(core, pair)
        for value in product(range(2), repeat=2):
            if len(rows.get(value, ())) != cap(pair, value):
                return False
    return True


def context_options(core, varying_party, high_symbol):
    """Two extra AB values for one high-C/low-D or low-C/high-D slice."""
    a_count = Counter(w[0] for w in core if w[varying_party] == high_symbol)
    b_count = Counter(w[1] for w in core if w[varying_party] == high_symbol)
    options = set()
    for low_a, low_b in product((2, 3), repeat=2):
        deficits = []
        valid = True
        for counts, low in ((a_count, low_a), (b_count, low_b)):
            target = {0: 3, 1: 3, low: 2, 5 - low: 0}
            delta = [target[x] - counts[x] for x in range(4)]
            if min(delta) < 0 or sum(delta) != 2:
                valid = False
                break
            deficits.append(tuple(x for x in range(4) for _ in range(delta[x])))
        if not valid:
            continue
        aa, bb = deficits
        for second in (bb, bb[::-1]):
            cells = tuple(sorted(((aa[0], second[0]), (aa[1], second[1]))))
            if cells[0] != cells[1]:
                options.add(cells)
    return tuple(sorted(options))


def context_words(party, symbol, low_partner, cells):
    if party == 2:
        return tuple((a, b, symbol, low_partner) for a, b in cells)
    return tuple((a, b, low_partner, symbol) for a, b in cells)


def ab_degree_candidates(words):
    """All AB graphs of ten edges compatible with these twenty words."""
    counts = Counter((w[0], w[1]) for w in words)
    if any(counts[p] != 4 for p in AB_FULL):
        return
    used = {p for p in AB_OTHER if counts[p]}
    if any(counts[p] > 2 for p in used):
        return
    missing = 8 - len(used)
    if not 0 <= missing <= 2:
        return
    once = [p for p in used if counts[p] == 1]
    if len(once) + 2 * missing != 4:
        return
    for added in combinations((p for p in AB_OTHER if p not in used), missing):
        edges = set(AB_FULL) | used | set(added)
        da = [sum(a == x for a, _ in edges) for x in range(4)]
        db = [sum(b == x for _, b in edges) for x in range(4)]
        if sorted(da) not in ([2, 2, 2, 4], [2, 2, 3, 3]):
            continue
        if sorted(db) not in ([2, 2, 2, 4], [2, 2, 3, 3]):
            continue
        deficits = tuple(sorted(once + [p for p in added for _ in range(2)]))
        yield edges, deficits


def low_cd_choices(words):
    rows = projections(words, (2, 3))
    count_c = Counter(w[2] for w in words)
    count_d = Counter(w[3] for w in words)
    for p, q in combinations(LOW_CD, 2):
        if any(count_c[c] + 2 * ((p[0] == c) + (q[0] == c)) != 4 for c in (2, 3)):
            continue
        if any(count_d[d] + 2 * ((p[1] == d) + (q[1] == d)) != 4 for d in (2, 3)):
            continue
        vals = set(rows) | {p, q}
        if any(len({d for c0, d in vals if c0 == c}) != 2 for c in (2, 3)):
            continue
        if any(len({c for c, d0 in vals if d0 == d}) != 2 for d in (2, 3)):
            continue
        yield p, q


def full_pair_degree_check(words):
    if len(words) != 24 or len(set(words)) != 24:
        return False
    for pair in PAIRS:
        rows = projections(words, pair)
        if len(rows) != 10:
            return False
        if any(len(support) != cap(pair, p) for p, support in rows.items()):
            return False
        if pair != (0, 1):
            if any(p not in rows for p in product(range(2), repeat=2)):
                return False
        elif any(p not in rows for p in AB_FULL):
            return False
    for i in range(4):
        for x in range(4):
            degrees = [len({w[j] for w in words if w[i] == x})
                       for j in range(4) if j != i]
            if len(set(degrees)) != 1 or not 2 <= degrees[0] <= 4:
                return False
            if i in (2, 3) and degrees[0] != (3 if x < 2 else 2):
                return False
            if sum(w[i] == x for w in words) != 2 * degrees[0] + (2 if x < 2 else 0):
                return False
    return True


def cut_shape(words, left, right):
    graph = projections(words, left)
    columns = {v for values in graph.values() for v in values}
    unseen_rows = set(graph)
    comps = []
    while unseen_rows:
        stack = [(0, next(iter(unseen_rows)))]
        rr, cc = set(), set()
        while stack:
            side, value = stack.pop()
            if side == 0:
                if value in rr:
                    continue
                rr.add(value)
                unseen_rows.discard(value)
                stack.extend((1, x) for x in graph[value])
            else:
                if value in cc:
                    continue
                cc.add(value)
                stack.extend((0, r) for r, vs in graph.items() if value in vs)
        edges = sum(len(graph[r] & cc) for r in rr)
        comps.append((len(rr), len(cc), edges))
    if len(columns) != 10 or len(graph) != 10:
        return "other"
    shapes = sorted(comps)
    if shapes == [(2, 2, 4), (2, 2, 4), (3, 3, 8), (3, 3, 8)]:
        return "X"
    if shapes == [(2, 2, 4), (2, 2, 4), (2, 2, 4), (4, 4, 12)]:
        return "Y"
    return "other"


def complete_boundary(words):
    """Append all four low-C/low-D words; every CD low line has size two."""
    for _edges, deficits in ab_degree_candidates(words):
        for p, q in low_cd_choices(words):
            partitions_seen = set()
            for indices in combinations(range(4), 2):
                first = tuple(sorted(deficits[k] for k in indices))
                second = tuple(sorted(deficits[k] for k in range(4) if k not in indices))
                if first[0] == first[1] or second[0] == second[1]:
                    continue
                assignment = (first, second)
                if assignment in partitions_seen:
                    continue
                partitions_seen.add(assignment)
                added = tuple((a, b, *p) for a, b in first) + tuple((a, b, *q) for a, b in second)
                result = tuple(sorted(words + added))
                if full_pair_degree_check(result):
                    yield result


def sparse_scrutiny():
    counts = Counter()
    samples = {}
    contexts = ((2, 0), (2, 1), (3, 0), (3, 1))
    for row0, row1 in combinations(AB_OTHER, 2):
        label = "/".join(sorted((row_type(row0), row_type(row1))))
        for partition, (s0, s1) in PARTITIONS:
            for support0, support1 in ((s0, s1), (s1, s0)):
                guard()
                key = label + ":" + partition
                counts["core:" + key] += 1
                core = core_words(row0, row1, support0, support1)
                ok, reason = partial_status(core)
                if not ok:
                    counts["core_reject_" + reason + ":" + key] += 1
                    continue
                if closed_high_box(core):
                    counts["closed_binary_box:" + key] += 1
                    continue
                options = [context_options(core, party, symbol) for party, symbol in contexts]
                if any(not opts for opts in options):
                    counts["context_marginal_reject:" + key] += 1
                    continue

                def walk(depth, words):
                    guard()
                    if depth == len(contexts):
                        counts["high_boundary:" + key] += 1
                        for full in complete_boundary(words):
                            guard()
                            counts["pair_degree_completion:" + key] += 1
                            if saturated_one_overlap(full) is not None:
                                counts["final_one_overlap_reject:" + key] += 1
                                continue
                            types = tuple(cut_shape(full, l, r) for l, r in CUTS)
                            if types[0] != "Y" or any(t not in ("X", "Y") for t in types[1:]):
                                counts["final_cut_shape_reject:" + key] += 1
                                continue
                            counts["strict_survivor:" + key] += 1
                            samples.setdefault(key, {"cuts": types, "E": full})
                        return
                    party, symbol = contexts[depth]
                    for cells in options[depth]:
                        for low_partner in (2, 3):
                            addition = context_words(party, symbol, low_partner, cells)
                            grown = words + addition
                            ok, reason = partial_status(grown)
                            if not ok:
                                counts["branch_reject_" + reason + ":" + key] += 1
                                continue
                            walk(depth + 1, grown)

                walk(0, core)
    return {"candidate_core_assignments": sum(v for k, v in counts.items() if k.startswith("core:")),
            "counts_by_stage_and_row_type_partition": dict(sorted(counts.items())),
            "strict_survivor_examples": samples}


def matching_cases():
    m0 = ((1, 0), (2, 2))
    m1 = ((1, 2), (2, 0))
    cases = {"I": ((0, 1), (2, 2)), "II": ((0, 2), (2, 1))}
    expected_a = (2, 3, 3, 2)
    expected_b = (3, 2, 3, 2)
    result = {}
    for name, sparse in cases.items():
        surviving = []
        graph_completions = []
        for choices in product((0, 1), repeat=4):
            counts = Counter({(0, 0): 4, (1, 1): 4, sparse[0]: 2, sparse[1]: 2})
            for choice in choices:
                counts.update(m0 if choice == 0 else m1)
            if any(n > (4 if p in AB_FULL else 2) for p, n in counts.items()):
                continue
            surviving.append(choices)
            used = {p for p, n in counts.items() if n}
            need = 10 - len(used)
            if need < 0:
                continue
            for added in combinations((p for p in product(range(4), repeat=2) if p not in used), need):
                graph = used | set(added)
                da = tuple(sum(a == i for a, _ in graph) for i in range(4))
                db = tuple(sum(b == i for _, b in graph) for i in range(4))
                if da == expected_a and db == expected_b:
                    graph_completions.append((choices, tuple(sorted(added))))
        result[name] = {"capacity_surviving_context_assignments": surviving,
                        "degree_graph_completions": graph_completions}
    if result["I"]["capacity_surviving_context_assignments"]:
        raise AssertionError("case I should fail AB line capacity")
    if len(result["II"]["capacity_surviving_context_assignments"]) != 6:
        raise AssertionError("case II should have exactly six matching assignments")
    if result["II"]["degree_graph_completions"]:
        raise AssertionError("case II should fail the prescribed AB degree graph")
    return result


def star_scrutiny():
    orientations = []
    for bits in product((0, 1), repeat=6):
        endpoint = {edge: edge[bits[k]] for k, edge in enumerate(PAIRS)}
        if all(all(endpoint[e] == vertex for e in PAIRS if vertex in e)
               for edge, vertex in endpoint.items()):
            orientations.append(bits)
    if orientations:
        raise AssertionError("unexpected four-party propagated star orientation")
    return {"orientations_examined": 64, "propagated_orientations": orientations,
            "mutant_drop_propagation": 64}


def reason_mutants():
    x = sum(1 << k for k, w in enumerate(WORDS) if (w[0] ^ w[1] ^ w[2]) == 0)
    # For AC|BD the omitted four words are indexed by AC=(a,c), BD=(a,c).
    y = sum(1 << k for k, w in enumerate(WORDS) if not (w[0] == w[1] and w[2] == w[3]))
    if mask_cut_type(x, *CUTS[0]) != "X" or mask_cut_type(y, *CUTS[1]) != "Y":
        raise AssertionError("independent-cut control construction")
    if x.bit_count() == y.bit_count():
        raise AssertionError("common-support cardinality control")
    fixture = core_words((0, 2), (1, 2), (0, 3), (1, 2))
    relaxed_ok, _ = partial_status(fixture, False)
    strict_ok, strict_reason = partial_status(fixture, True)
    witness = saturated_one_overlap(fixture)
    if not relaxed_ok or strict_ok or strict_reason != "saturated_one_overlap" or witness is None:
        raise AssertionError("one-overlap reason control")
    return {
        "drop_common_tensor": {"independent_cut_X_mask": x, "independent_cut_Y_mask": y,
                               "separate_sizes": [x.bit_count(), y.bit_count()],
                               "relaxed_independent_cuts_accepted": True,
                               "common_support_rejected": True},
        "drop_one_overlap": {"core_E": fixture, "without_one_overlap": relaxed_ok,
                             "with_one_overlap": strict_ok, "reason": strict_reason,
                             "saturated_rows_witness": witness},
    }


def main():
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, INTERNAL_SECONDS)
    emit("START", internal_seconds=INTERNAL_SECONDS, parent_outer_limit_at_most=55,
         model="necessary-support only; no P enumeration, phases, or AME feasibility")
    try:
        PROGRESS["phase"] = "high_support"
        high = high_support_scrutiny()
        emit("PHASE_COMPLETE", phase="high_support", result=high)
        PROGRESS["phase"] = "matching_star_mutants"
        matching = matching_cases()
        stars = star_scrutiny()
        mutants = reason_mutants()
        emit("PHASE_COMPLETE", phase="matching_star_mutants", matching=matching,
             stars=stars, mutants=mutants)
        PROGRESS["phase"] = "single_F_sparse"
        sparse = sparse_scrutiny()
        emit("PHASE_COMPLETE", phase="single_F_sparse", result=sparse)
        signal.setitimer(signal.ITIMER_REAL, 0)
        emit("COMPLETE_NECESSARY_LOCAL_MODELS", elapsed_seconds=time.monotonic() - START,
             qualification="conditional finite necessary-support model, not global E/P or AME enumeration")
    except Deadline:
        signal.setitimer(signal.ITIMER_REAL, 0)
        emit("INCOMPLETE_TIMEOUT", phase=PROGRESS["phase"], elapsed_seconds=time.monotonic() - START,
             qualification="partial output is not exhaustive and is not a PASS")
        raise SystemExit(124)
    except Exception as error:
        signal.setitimer(signal.ITIMER_REAL, 0)
        emit("ERROR", phase=PROGRESS["phase"], error=repr(error),
             qualification="not exhaustive and not a PASS")
        raise


if __name__ == "__main__":
    main()
