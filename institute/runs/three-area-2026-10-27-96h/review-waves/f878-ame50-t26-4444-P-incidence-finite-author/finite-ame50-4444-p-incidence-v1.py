#!/usr/bin/env python3
"""UNRUN author source: necessary local projections for AME(4,6), N50 t26.

No command, import, or output in this file establishes a P/E support, a phase
solution, an AME state, or the completeness of the global incidence search.
The inputs are the displayed counting and actual-pair-injectivity assumptions
in the accompanying author candidate.  Degree-two even-surplus and the r=2
no-surplus-four restrictions are conditional on the unitary lemmas there.

Parent must first read ALL source bytes and record a separate one-shot GO.
For that GO an independent outer supervisor MUST impose at most 55 seconds.
The script imposes a 40-second SIGALRM plus monotonic checks, prints flushed
JSON-lines partial status, and exits nonzero on timeout or a failed check.
It creates no files, starts no subprocesses, uses no network or non-stdlib
modules, and does not inspect any input files.
"""

from collections import Counter, defaultdict
from itertools import combinations, permutations, product
import json
import signal
import sys
import time

LIMIT_SECONDS = 40.0
START = time.monotonic()
COMPLETED = []
PAIRS4 = tuple(combinations(range(4), 2))
PAIRS3 = tuple(combinations(range(3), 2))


class Deadline(Exception):
    pass


class CheckFailure(Exception):
    pass


def alarm_handler(_signum, _frame):
    raise Deadline("internal-40-second-deadline")


def tick():
    if time.monotonic() - START >= LIMIT_SECONDS:
        raise Deadline("internal-40-second-deadline")


def emit(event, **fields):
    print(json.dumps({"event": event, **fields}, sort_keys=True), flush=True)


def must(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def expect(actual, expected, name):
    must(actual == expected, name + ": expected " + repr(expected) +
         ", got " + repr(actual))


def run_stage(name, fn):
    tick()
    emit("stage-start", stage=name, elapsed=time.monotonic() - START)
    details = fn()
    COMPLETED.append(name)
    emit("stage-complete", stage=name, details=details,
         elapsed=time.monotonic() - START)


def moment_reason(n, skip=None):
    if len(n) != 5 or any(not isinstance(x, int) or x < 0 for x in n):
        return "moment-domain"
    if skip != "total" and sum(n) != 26:
        return "moment-total"
    if skip != "first" and sum(k * n[k] for k in range(5)) != 56:
        return "moment-first"
    if skip != "pair" and sum(k * (k - 1) // 2 * n[k]
                              for k in range(5)) != 36:
        return "moment-pair"
    return None


def compositions(total, width):
    for xs in product(range(total + 1), repeat=width):
        if sum(xs) == total:
            yield xs


def moments_and_party_counts():
    profiles = set()
    for n0 in range(27):
        for n4 in range(27):
            # These formulas follow by eliminating n1,n2,n3 from the
            # three original moment equations; no separate P sets are used.
            n1 = 2 - 3 * n0 - n4
            n3 = 6 - n0 - 3 * n4
            n2 = 18 + 3 * n0 + 3 * n4
            n = (n0, n1, n2, n3, n4)
            if moment_reason(n) is None:
                profiles.add(n)
        tick()
    expected = {(0, 2, 18, 6, 0), (0, 1, 21, 3, 1),
                (0, 0, 24, 0, 2)}
    expect(profiles, expected, "moment-profile-set")
    cases = {}
    for n in sorted(profiles):
        r = n[4]
        found = []
        for u in compositions(n[1], 4):
            for v in compositions(n[3], 4):
                p = {}
                for i, j in PAIRS4:
                    other = [k for k in range(4) if k not in (i, j)]
                    p[i, j] = 6 - r - v[other[0]] - v[other[1]]
                if min(p.values()) < 0 or sum(p.values()) != n[2]:
                    continue
                if any(u[i] + sum(p[min(i, j), max(i, j)]
                                  for j in range(4) if j != i) +
                       sum(v[j] for j in range(4) if j != i) + r != 14
                       for i in range(4)):
                    continue
                must(all(u[i] + v[i] == 2 - r for i in range(4)),
                     "party-u-plus-v")
                found.append((u, v))
        expect(len(found), {0: 10, 1: 4, 2: 1}[r], "party-count")
        cases[str(r)] = len(found)
    bad = (0, 3, 16, 7, 0)  # total and first moment correct; pair moment 37.
    expect(moment_reason(bad), "moment-pair", "control-pair-moment-reason")
    expect(moment_reason(bad, skip="pair"), None, "mutant-omits-pair-moment")
    return {"profiles": sorted(profiles), "party_assignments": cases,
            "controls": ["pair-moment"]}


def symbol_options(r, u, degree):
    n2 = 18 + 3 * r
    triple_at_party = 4 - 2 * r + u
    options = []
    for z1 in range(u + 1):
        for z2 in range(min(n2, 6 - degree) + 1):
            for z3 in range(triple_at_party + 1):
                for z4 in range(r + 1):
                    z = (z1, z2, z3, z4)
                    if sum(z) != 6 - degree:
                        continue
                    if z2 + 2 * z3 + 3 * z4 != 3 * (4 - degree):
                        continue
                    must(z1 - z3 - 2 * z4 == 2 * (degree - 3),
                         "symbol-elimination-identity")
                    options.append(z)
    return options


def symbols_and_surplus():
    patterns = ((2, 2, 2, 4), (2, 2, 3, 3))
    rows = []
    realized_options = defaultdict(set)
    for r in range(3):
        for u in range(3 - r):
            triple = 4 - 2 * r + u
            target = (u, 14 - u - triple - r, triple, r)
            for degrees in patterns:
                options = [symbol_options(r, u, d) for d in degrees]
                count = 0
                for assignment in product(*options):
                    if tuple(sum(z[m] for z in assignment)
                             for m in range(4)) != target:
                        continue
                    count += 1
                    for d, z in zip(degrees, assignment):
                        realized_options[r, u, d].add(z)
                        if d == 4:
                            expect((r, u, z), (0, 2, (2, 0, 0, 0)),
                                   "degree-four-symbol")
                        if z[0] == 2:
                            expect(d, 4, "two-singletons-same-symbol")
                        if r == 1 and z[3] == 1:
                            expect(d, 2, "r1-allinside-degree")
                        if r == 2:
                            expect(z, (0, 3, 0, 3 - d),
                                   "r2-symbol-identity")
                    if r == 2:
                        expect(tuple(z[3] for z in assignment), (1, 1, 0, 0),
                               "r2-two-degree-two-symbols")
                rows.append({"r": r, "u": u, "degrees": degrees,
                             "assignments": count})
                tick()
    for r in range(3):
        must(any(row["r"] == r and row["assignments"] for row in rows),
             "empty-symbol-projection-r" + str(r))
    must(not any(row["r"] in (1, 2) and row["degrees"] == (2, 2, 2, 4)
                 and row["assignments"] for row in rows),
         "degree-four-with-too-few-singletons")
    h_counts = {}
    for r in range(3):
        for degrees in patterns:
            if r and degrees == (2, 2, 2, 4):
                continue
            count = 0
            for h in product(range(5), repeat=4):
                if sum(h) != 4:
                    continue
                if any(d == 2 and x not in (0, 2, 4)
                       for d, x in zip(degrees, h)):
                    continue
                if r == 2 and max(h) > 3:
                    continue
                count += 1
            h_counts[str((r, degrees))] = count
    h2 = [h for h in product(range(5), repeat=4)
          if r2_surplus_reason(h) is None]
    classes = Counter(classify_h(h) for h in h2)
    expect(dict(classes), {"A": 6, "B": 2, "C": 2}, "r2-h-classes")
    expect(r2_surplus_reason((1, 1, 1, 1)), "d2-odd-surplus",
           "control-d2-surplus-reason")
    expect(r2_surplus_reason((1, 1, 1, 1), skip="d2"), None,
           "mutant-omits-d2-surplus")
    expect(r2_surplus_reason((0, 0, 4, 0)), "r2-surplus-four",
           "control-no-four-reason")
    expect(r2_surplus_reason((0, 0, 4, 0), skip="max"), None,
           "mutant-omits-no-four")
    expect(r2_surplus_reason((0, 0, 0, 0)), "surplus-total",
           "control-surplus-total-reason")
    expect(r2_surplus_reason((0, 0, 0, 0), skip="total"), None,
           "mutant-omits-surplus-total")
    serialized = [{"r": k[0], "u": k[1], "degree": k[2],
                   "z_options": sorted(v)}
                  for k, v in sorted(realized_options.items())]
    return {"symbol_assignment_counts": rows, "symbol_options": serialized,
            "surplus_projection_counts": h_counts,
            "r2_classes": dict(classes),
            "controls": ["d2-parity", "r2-no-four", "surplus-total"]}


def r2_surplus_reason(h, skip=None):
    if len(h) != 4 or any(not isinstance(x, int) or x < 0 or x > 4 for x in h):
        return "surplus-domain"
    if skip != "total" and sum(h) != 4:
        return "surplus-total"
    if skip != "d2" and (h[0] % 2 or h[1] % 2):
        return "d2-odd-surplus"
    if skip != "max" and max(h) > 3:
        return "r2-surplus-four"
    return None


def classify_h(h):
    if sorted(h) == [0, 0, 2, 2]:
        return "A"
    if h[:2] == (0, 0) and sorted(h[2:]) == [1, 3]:
        return "B"
    if sorted(h[:2]) == [0, 2] and h[2:] == (1, 1):
        return "C"
    return "unclassified"


def pair_collision(words):
    for i, j in PAIRS4:
        seen = {}
        for index, word in enumerate(words):
            key = (word[i], word[j])
            if key in seen:
                return (i, j, seen[key], index)
            seen[key] = index
    return None


def r1_reason(words, skip=None):
    if len(words) != 3:
        return "r1-word-count"
    for index, word in enumerate(words):
        missing = index + 1
        if (len(word) != 4 or not 0 <= word[0] < 4 or
                not 4 <= word[missing] < 6 or
                any(not 0 <= word[j] < 4 for j in range(1, 4)
                    if j != missing)):
            return "r1-word-shape"
    if skip != "repeat" and sum(word[0] == 0 for word in words) < 2:
        return "r1-repeat-at-h"
    if skip != "forced" and any(word[j] != 0
                                for index, word in enumerate(words)
                                for j in range(1, 4) if j != index + 1):
        return "r1-forced-b"
    if skip != "injective" and pair_collision(words) is not None:
        return "r1-pair-collision"
    return None


def r1_words(hs, outside):
    words = []
    for index in range(3):
        word = [hs[index], 0, 0, 0]
        word[index + 1] = 4 + outside[index]
        words.append(tuple(word))
    return tuple(words)


def r1_abstract_triples():
    eligible = 0
    rejected = 0
    for hs in product(range(4), repeat=3):
        for outside in product(range(2), repeat=3):
            words = r1_words(hs, outside)
            reason = r1_reason(words)
            if hs.count(0) >= 2:
                eligible += 1
                expect(reason, "r1-pair-collision", "r1-pigeonhole")
                rejected += 1
            else:
                expect(reason, "r1-repeat-at-h", "r1-noneligible")
        tick()
    expect((eligible, rejected), (320, 320), "r1-exhaustion-count")
    no_repeat = r1_words((0, 1, 2), (0, 0, 0))
    expect(r1_reason(no_repeat), "r1-repeat-at-h", "control-r1-repeat")
    expect(r1_reason(no_repeat, skip="repeat"), None, "mutant-r1-repeat")
    no_forced = ((0, 4, 0, 0), (0, 0, 4, 1), (1, 0, 0, 4))
    expect(r1_reason(no_forced), "r1-forced-b", "control-r1-forced")
    expect(r1_reason(no_forced, skip="forced"), None, "mutant-r1-forced")
    collision = r1_words((0, 0, 0), (0, 0, 0))
    expect(r1_reason(collision), "r1-pair-collision", "control-r1-injective")
    expect(r1_reason(collision, skip="injective"), None, "mutant-r1-injective")
    return {"enumerated": 512, "eligible": eligible,
            "eligible_pair_collision": rejected,
            "controls": ["repeat", "forced-symbol", "pair-injectivity"]}


def r2_word_reason(word, skip=None):
    if len(word) != 4 or any(not isinstance(x, int) or x not in range(4)
                             for x in word):
        return "r2-word-domain"
    for i, j in PAIRS4:
        if skip != "w0" and (word[i], word[j]) == (0, 0):
            return "w0-pair-" + str(i) + str(j)
        if skip != "w1" and (word[i], word[j]) == (1, 1):
            return "w1-pair-" + str(i) + str(j)
    return None


def bit_reason(bits, skip_pair=None):
    if len(bits) != 3 or any(bit not in (0, 1) for bit in bits):
        return "bit-domain"
    for i, j in PAIRS3:
        if (i, j) != skip_pair and bits[i] == bits[j]:
            return "same-bit-" + str(i) + str(j)
    return None


def r2_inside_bits():
    allowed_by_d_count = Counter()
    for word in product(range(4), repeat=4):
        if r2_word_reason(word) is None:
            allowed_by_d_count[sum(x in (0, 1) for x in word)] += 1
    expect([allowed_by_d_count[k] for k in range(5)], [16, 64, 48, 0, 0],
           "r2-allowed-q4-word-counts")
    for bits in product(range(2), repeat=3):
        must(bit_reason(bits) is not None, "three-pairwise-distinct-bits")
    expect(bit_reason((0, 1, 0)), "same-bit-02", "control-three-bits")
    expect(bit_reason((0, 1, 0), skip_pair=(0, 2)), None,
           "mutant-three-bits-missing-pair")
    for bit in (0, 1):
        word = (bit, bit, 2, 3)
        expect(r2_word_reason(word), "w" + str(bit) + "-pair-01",
               "control-forbidden-P-pair")
        expect(r2_word_reason(word, skip="w" + str(bit)), None,
               "mutant-omits-P-word-pairs")
    return {"allowed_q4_by_degree_two_count":
            [allowed_by_d_count[k] for k in range(5)],
            "three_binary_bits_accepted": 0,
            "controls": ["each-allinside-P-word", "third-bit-pair"]}


def layer_reason(f, g, skip=None):
    if len(f) != 4 or len(g) != 4 or any(x not in range(4) for x in f + g):
        return "layer-domain"
    if skip != "f" and len(set(f)) != 4:
        return "f-not-bijective"
    if skip != "g" and len(set(g)) != 4:
        return "g-not-bijective"
    if skip != "inside" and (f[0] == 0 or f[1] == 1):
        return "allinside-P-pair-collision"
    return None


def layer_words(f, g):
    words = [(0, 0, 0, 0), (1, 1, 1, 1)]
    for a in range(4):
        words.append((a, f[a], 4 + (g[a] >> 1), 4 + (g[a] & 1)))
    return tuple(words)


def star_reason(signatures, skip_pair=None):
    if len(signatures) != 4 or any(len(s) != 3 or any(b not in (0, 1) for b in s)
                                  for s in signatures):
        return "star-domain"
    for i, j in PAIRS3:
        if (i, j) != skip_pair:
            pairs = {(s[i], s[j]) for s in signatures}
            if len(pairs) != 4:
                return "star-projection-" + str(i) + str(j)
    return None


def layer_and_star():
    valid_f = []
    layers = 0
    for f in permutations(range(4)):
        if layer_reason(f, (0, 1, 2, 3)) is not None:
            continue
        valid_f.append(f)
        for g in permutations(range(4)):
            expect(layer_reason(f, g), None, "local-layer-guard")
            expect(pair_collision(layer_words(f, g)), None,
                   "local-layer-actual-pair-injectivity")
            layers += 1
        tick()
    expect((len(valid_f), layers), (14, 336), "local-layer-count")
    bad_f = (2, 2, 0, 1)
    identity = (0, 1, 2, 3)
    expect(layer_reason(bad_f, identity), "f-not-bijective", "control-f")
    expect(layer_reason(bad_f, identity, skip="f"), None, "mutant-f")
    must(pair_collision(layer_words(bad_f, identity)) is not None,
         "mutant-f-actual-collision")
    good_f = (1, 0, 2, 3)
    bad_g = (0, 0, 2, 3)
    expect(layer_reason(good_f, bad_g), "g-not-bijective", "control-g")
    expect(layer_reason(good_f, bad_g, skip="g"), None, "mutant-g")
    must(pair_collision(layer_words(good_f, bad_g)) is not None,
         "mutant-g-actual-collision")
    expect(layer_reason(identity, identity), "allinside-P-pair-collision",
           "control-layer-allinside")
    expect(layer_reason(identity, identity, skip="inside"), None,
           "mutant-layer-allinside")
    must(pair_collision(layer_words(identity, identity)) is not None,
         "mutant-layer-allinside-actual-collision")
    signatures = tuple(product(range(2), repeat=3))
    parity_counts = Counter()
    accepted = 0
    for ss in product(signatures, repeat=4):
        if star_reason(ss) is None:
            accepted += 1
            parity = [sum(s) % 2 for s in ss]
            must(len(set(parity)) == 1, "star-common-parity")
            for a, b in combinations(range(4), 2):
                expect(sum(x != y for x, y in zip(ss[a], ss[b])), 2,
                       "star-pair-distance-two")
            parity_counts[parity[0]] += 1
        if accepted % 32 == 0:
            tick()
    expect((accepted, parity_counts[0], parity_counts[1]), (48, 24, 24),
           "star-parity-classes")
    bad_star = ((0, 0, 0), (0, 1, 0), (1, 0, 1), (1, 1, 1))
    expect(star_reason(bad_star), "star-projection-02", "control-star-pair")
    expect(star_reason(bad_star, skip_pair=(0, 2)), None, "mutant-star-pair")
    must(len({sum(s) % 2 for s in bad_star}) != 1, "mutant-star-parity")
    repeated_even = ((0, 0, 0),) * 4
    expect(star_reason(repeated_even), "star-projection-01",
           "control-parity-alone-insufficient")
    return {"valid_f": len(valid_f), "local_f_g_layers": layers,
            "star_ordered_signatures": accepted,
            "star_parity_counts": dict(parity_counts),
            "controls": ["f-bijection", "g-bijection", "inside-P-pair",
                         "star-each-projection", "parity-alone"]}


def high_edges():
    accepted3 = Counter()
    accepted4 = Counter()
    bc = 0
    cb = 0
    for f in permutations(range(4)):
        if layer_reason(f, (0, 1, 2, 3)) is not None:
            continue
        forbidden = {(0, 0), (1, 1)} | {(a, f[a]) for a in range(4)}
        edges = tuple((a, b) for a in range(4) for b in range(4)
                      if (a, b) not in forbidden)
        expect(len(edges), 10, "r2-local-E-value-count")
        expect(tuple(sum(a == i for a, _ in edges) for i in range(4)),
               (2, 2, 3, 3), "r2-local-row-degrees")
        expect(tuple(sum(b == j for _, b in edges) for j in range(4)),
               (2, 2, 3, 3), "r2-local-column-degrees")
        for high in combinations(edges, 4):
            hr = tuple(sum(a == i for a, _ in high) for i in range(4))
            hc = tuple(sum(b == j for _, b in high) for j in range(4))
            if r2_surplus_reason(hr) is not None or r2_surplus_reason(hc) is not None:
                continue
            tr, tc = classify_h(hr), classify_h(hc)
            must(tr != "unclassified" and tc != "unclassified", "high-class")
            accepted3[tr + tc] += 1
            if tr == "B":
                expect(tc, "C", "type-B-opposite-C")
                c = 2 if hr[2] == 3 else 3
                t = 3 if c == 2 else 2
                bj = 0 if hc[0] == 2 else 1
                expect({b for a, b in high if a == c},
                       {j for j in range(4) if hc[j] > 0}, "B-c-neighbors")
                expect({b for a, b in high if a == t}, {bj}, "B-t-neighbor")
                bc += 1
            if tc == "B":
                expect(tr, "C", "type-B-opposite-C-transpose")
                c = 2 if hc[2] == 3 else 3
                t = 3 if c == 2 else 2
                bi = 0 if hr[0] == 2 else 1
                expect({a for a, b in high if b == c},
                       {i for i in range(4) if hr[i] > 0}, "BT-c-neighbors")
                expect({a for a, b in high if b == t}, {bi}, "BT-t-neighbor")
                cb += 1
        for high in combinations(edges, 2):
            hr = tuple(2 * sum(a == i for a, _ in high) for i in range(4))
            hc = tuple(2 * sum(b == j for _, b in high) for j in range(4))
            if r2_surplus_reason(hr) is not None or r2_surplus_reason(hc) is not None:
                continue
            expect((classify_h(hr), classify_h(hc)), ("A", "A"),
                   "two-four-both-type-A")
            must(high[0][0] != high[1][0] and high[0][1] != high[1][1],
                 "two-four-disjoint-symbols")
            accepted4["AA"] += 1
        tick()
    must(bc > 0 and cb > 0 and accepted4["AA"] > 0,
         "high-edge-projections-not-vacuous")
    # A B row has odd surplus and cannot arise from increments of two.
    b = (0, 0, 3, 1)
    c = (2, 0, 1, 1)
    expect(two_four_reason(b, c), "two-four-odd-surplus", "control-two-four")
    expect(two_four_reason(b, c, skip="parity"), None, "mutant-two-four")
    return {"four-three_edge_class_counts": dict(accepted3),
            "two-four_edge_class_counts": dict(accepted4),
            "B_C_witnesses": bc, "C_B_witnesses": cb,
            "controls": ["two-four-even-increments"]}


def two_four_reason(hr, hc, skip=None):
    if (len(hr) != 4 or len(hc) != 4 or
            any(x < 0 or x > 3 for x in hr + hc)):
        return "two-four-domain"
    if sum(hr) != 4 or sum(hc) != 4:
        return "two-four-total"
    if skip != "parity" and any(x % 2 for x in hr + hc):
        return "two-four-odd-surplus"
    return None


def line_reason(bits, masks, skip=None):
    if len(bits) != 3 or any(x not in (0, 1) for x in bits) or len(masks) != 3:
        return "line-domain"
    if any(not isinstance(m, int) or m < 0 for m in masks):
        return "line-domain"
    if skip != "bound" and any(m & ~127 for m in masks):
        return "line-outside-seven"
    if skip != "size" and any(m.bit_count() != 3 for m in masks):
        return "line-size-not-three"
    if skip != "overlap":
        for i, j in PAIRS3:
            if bits[i] == bits[j] and masks[i] & masks[j]:
                return "line-equal-bit-overlap-" + str(i) + str(j)
    return None


def type_b_line_pigeonhole():
    masks = tuple(sum(1 << x for x in subset)
                  for subset in combinations(range(7), 3))
    feasible = {}
    for bits in product(range(2), repeat=3):
        count = 0
        for index, triple in enumerate(product(masks, repeat=3)):
            if line_reason(bits, triple) is None:
                count += 1
            if index % 1024 == 0:
                tick()
        feasible["".join(str(x) for x in bits)] = count
        if len(set(bits)) == 1:
            expect(count, 0, "B-monochrome-impossible")
        else:
            must(count > 0, "B-mixed-bit-projection-nonvacuous")
    bad = (7, 25, 42)
    expect(line_reason((0, 0, 0), bad), "line-equal-bit-overlap-01",
           "control-line-overlap")
    expect(line_reason((0, 0, 0), bad, skip="overlap"), None,
           "mutant-line-overlap")
    short = (3, 25, 100)
    expect(line_reason((0, 1, 0), short), "line-size-not-three",
           "control-line-size")
    expect(line_reason((0, 1, 0), short, skip="size"), None,
           "mutant-line-size")
    nine = (7, 56, 448)
    expect(line_reason((0, 0, 0), nine), "line-outside-seven",
           "control-seven-words")
    expect(line_reason((0, 0, 0), nine, skip="bound"), None,
           "mutant-seven-words")
    return {"seven_word_line_assignments": feasible,
            "controls": ["same-bit-disjoint", "three-per-line", "seven-total"]}


def main():
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, LIMIT_SECONDS)
    try:
        emit("begin", scope="necessary-local-projections-only",
             internal_deadline_seconds=LIMIT_SECONDS,
             required_outer_supervisor_seconds=55)
        run_stage("moments-and-party-counts", moments_and_party_counts)
        run_stage("per-symbol-and-surplus", symbols_and_surplus)
        run_stage("r1-actual-pair-pigeonhole", r1_abstract_triples)
        run_stage("r2-allinside-symbol-bits", r2_inside_bits)
        run_stage("r2-local-layer-and-star", layer_and_star)
        run_stage("r2-high-edge-projections", high_edges)
        run_stage("type-B-seven-word-pigeonhole", type_b_line_pigeonhole)
        emit("complete", completed=COMPLETED, elapsed=time.monotonic() - START,
             result="NECESSARY_LOCAL_PROJECTIONS_ONLY_NOT_GLOBAL_P_E_OR_AME")
        return 0
    except Deadline as error:
        emit("incomplete", reason=str(error), completed=COMPLETED,
             elapsed=time.monotonic() - START)
        return 2
    except CheckFailure as error:
        emit("check-failed", reason=str(error), completed=COMPLETED,
             elapsed=time.monotonic() - START)
        return 1
    except Exception as error:
        emit("error", error_type=type(error).__name__, reason=str(error),
             completed=COMPLETED, elapsed=time.monotonic() - START)
        return 1
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)


if __name__ == "__main__":
    sys.exit(main())
