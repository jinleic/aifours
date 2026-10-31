#!/usr/bin/env python3
"""UNRUN corrected author verifier: necessary 4444 local projections only.

The checked domains are explicit relaxations, not all shared P/E supports,
phase assignments, or AME tensors. Degree-two surplus and r=2 no-surplus-four
filters are conditional on the actual-unitary lemmas stated in the narrative.
Parent must read every source byte and issue a separate one-shot GO before any
execution. Parent's independent outer supervisor must cap execution at 55s.
Python >=3.10 on a POSIX system with SIGALRM/setitimer is required. The 39s
internal monotonic/alarm bound and flushed JSON-lines preserve partial status.
No files, subprocesses, network, randomness, or third-party packages are used.
"""

from collections import Counter, defaultdict
from itertools import combinations, permutations, product
import json
import signal
import sys
import time

START = time.monotonic()
INTERNAL = 39.0
P4 = tuple(combinations(range(4), 2))
P3 = tuple(combinations(range(3), 2))
DONE = []


class Deadline(Exception):
    pass


class Failure(Exception):
    pass


def alarm(_number, _frame):
    raise Deadline("internal-deadline")


def tick():
    if time.monotonic() - START >= INTERNAL:
        raise Deadline("internal-deadline")


def emit(event, **data):
    print(json.dumps({"event": event, **data}, sort_keys=True), flush=True)


def eq(actual, expected, reason):
    if actual != expected:
        raise Failure(reason + ": expected " + repr(expected) +
                      "; got " + repr(actual))


def need(condition, reason):
    if not condition:
        raise Failure(reason)


def stage(name, fn):
    tick()
    emit("stage-start", stage=name, elapsed=time.monotonic() - START)
    result = fn()
    DONE.append(name)
    emit("stage-complete", stage=name, result=result,
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


def compositions(n):
    return [v for v in product(range(n + 1), repeat=4) if sum(v) == n]


def moments():
    profiles = set()
    for n0 in range(27):
        for r in range(27):
            n = (n0, 2 - 3 * n0 - r, 18 + 3 * n0 + 3 * r,
                 6 - n0 - 3 * r, r)
            if moment_reason(n) is None:
                profiles.add(n)
        tick()
    eq(profiles, {(0, 2, 18, 6, 0), (0, 1, 21, 3, 1),
                  (0, 0, 24, 0, 2)}, "moment-profiles")
    party_counts = {}
    for n in sorted(profiles):
        r = n[4]
        count = 0
        for u in compositions(n[1]):
            for v in compositions(n[3]):
                p = {}
                for i, j in P4:
                    k, l = (a for a in range(4) if a not in (i, j))
                    p[i, j] = 6 - r - v[k] - v[l]
                if min(p.values()) < 0 or sum(p.values()) != n[2]:
                    continue
                if any(u[i] + sum(p[min(i, j), max(i, j)]
                                  for j in range(4) if j != i) +
                       sum(v[j] for j in range(4) if j != i) + r != 14
                       for i in range(4)):
                    continue
                need(all(u[i] + v[i] == 2 - r for i in range(4)),
                     "party-u-plus-v")
                count += 1
        eq(count, {0: 10, 1: 4, 2: 1}[r], "party-assignment-count")
        party_counts[str(r)] = count
    wrong_pair = (0, 3, 16, 7, 0)
    eq(moment_reason(wrong_pair), "moment-pair", "control-moment-pair")
    eq(moment_reason(wrong_pair, skip="pair"), None, "mutant-moment-pair")
    return {"profiles": sorted(profiles), "party_assignments": party_counts,
            "controls": ["pair-moment"]}


def symbol_options(r, u, d):
    triple = 4 - 2 * r + u
    out = []
    for z1 in range(u + 1):
        for z2 in range(6 - d + 1):
            for z3 in range(triple + 1):
                for z4 in range(r + 1):
                    z = (z1, z2, z3, z4)
                    if sum(z) != 6 - d:
                        continue
                    if z2 + 2 * z3 + 3 * z4 != 3 * (4 - d):
                        continue
                    eq(z1 - z3 - 2 * z4, 2 * (d - 3),
                       "symbol-elimination")
                    out.append(z)
    return out


def surplus_reason(h, skip=None):
    if len(h) != 4 or any(not isinstance(x, int) or x < 0 or x > 4 for x in h):
        return "surplus-domain"
    if skip != "total" and sum(h) != 4:
        return "surplus-total"
    if skip != "d2" and (h[0] % 2 or h[1] % 2):
        return "d2-odd-surplus"
    if skip != "max" and max(h) > 3:
        return "r2-surplus-four"
    return None


def h_type(h):
    if sorted(h) == [0, 0, 2, 2]:
        return "A"
    if h[:2] == (0, 0) and sorted(h[2:]) == [1, 3]:
        return "B"
    if sorted(h[:2]) == [0, 2] and h[2:] == (1, 1):
        return "C"
    return "unclassified"


def symbols():
    degree_patterns = ((2, 2, 2, 4), (2, 2, 3, 3))
    rows = []
    options_seen = defaultdict(set)
    for r in range(3):
        for u in range(3 - r):
            triple = 4 - 2 * r + u
            target = (u, 14 - u - triple - r, triple, r)
            for degrees in degree_patterns:
                choices = [symbol_options(r, u, d) for d in degrees]
                count = 0
                for zs in product(*choices):
                    if tuple(sum(z[m] for z in zs) for m in range(4)) != target:
                        continue
                    count += 1
                    for d, z in zip(degrees, zs):
                        options_seen[r, u, d].add(z)
                        if d == 4:
                            eq((r, u, z), (0, 2, (2, 0, 0, 0)),
                               "degree-four-symbol")
                        if z[0] == 2:
                            eq(d, 4, "same-symbol-two-singletons")
                        if r == 1 and z[3] == 1:
                            eq(d, 2, "r1-allinside-degree")
                        if r == 2:
                            eq(z, (0, 3, 0, 3 - d), "r2-symbol-z")
                    if r == 2:
                        eq(tuple(z[3] for z in zs), (1, 1, 0, 0),
                           "r2-allinside-degree-two")
                rows.append({"r": r, "u": u, "degrees": degrees,
                             "assignments": count})
                tick()
    for r in range(3):
        need(any(x["r"] == r and x["assignments"] > 0 for x in rows),
             "empty-r-symbol-domain")
    need(not any(x["r"] in (1, 2) and x["degrees"] == (2, 2, 2, 4)
                 and x["assignments"] for x in rows), "degree-four-r1-r2")
    h_counts = {}
    for r in range(3):
        for degrees in degree_patterns:
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
    hs = [h for h in product(range(5), repeat=4) if surplus_reason(h) is None]
    classes = Counter(h_type(h) for h in hs)
    eq(dict(classes), {"A": 6, "B": 2, "C": 2}, "r2-h-classification")
    for h, skip, reason in [((1, 1, 1, 1), "d2", "d2-odd-surplus"),
                            ((0, 0, 4, 0), "max", "r2-surplus-four"),
                            ((0, 0, 0, 0), "total", "surplus-total")]:
        eq(surplus_reason(h), reason, "control-" + reason)
        eq(surplus_reason(h, skip=skip), None, "mutant-" + reason)
    observed = [{"r": k[0], "u": k[1], "degree": k[2],
                 "z_options": sorted(v)} for k, v in sorted(options_seen.items())]
    return {"symbol_assignments": rows, "symbol_options": observed,
            "surplus_projection_counts": h_counts, "r2_classes": dict(classes),
            "controls": ["d2-parity", "r2-no-four", "surplus-total"]}


def pair_collision(words):
    for i, j in P4:
        seen = {}
        for number, w in enumerate(words):
            cell = (w[i], w[j])
            if cell in seen:
                return (i, j, seen[cell], number)
            seen[cell] = number
    return None


def r1_reason(words, skip=None):
    if len(words) != 3:
        return "r1-count"
    for index, w in enumerate(words):
        missing = index + 1
        if (len(w) != 4 or not 0 <= w[0] < 4 or
                not 4 <= w[missing] < 6 or
                any(not 0 <= w[j] < 4 for j in range(1, 4) if j != missing)):
            return "r1-shape"
    if skip != "repeat" and sum(w[0] == 0 for w in words) < 2:
        return "r1-repeat-at-h"
    if skip != "forced" and any(w[j] != 0 for index, w in enumerate(words)
                                for j in range(1, 4) if j != index + 1):
        return "r1-forced-b"
    if skip != "injective" and pair_collision(words) is not None:
        return "r1-pair-collision"
    return None


def r1_words(h_values, out_bits):
    words = []
    for index in range(3):
        w = [h_values[index], 0, 0, 0]
        w[index + 1] = 4 + out_bits[index]
        words.append(tuple(w))
    return tuple(words)


def r1_triples():
    eligible = rejected = 0
    for hs in product(range(4), repeat=3):
        for outs in product(range(2), repeat=3):
            reason = r1_reason(r1_words(hs, outs))
            if hs.count(0) >= 2:
                eligible += 1
                eq(reason, "r1-pair-collision", "r1-pigeonhole")
                rejected += 1
            else:
                eq(reason, "r1-repeat-at-h", "r1-ineligible")
        tick()
    # Exactly two zeros: 3 positions for the nonzero and 3 values;
    # all three zeros: one choice. Eight outside-bit assignments each.
    eq((eligible, rejected), (80, 80), "r1-exhaustion-count")
    no_repeat = r1_words((0, 1, 2), (0, 0, 0))
    eq(r1_reason(no_repeat), "r1-repeat-at-h", "control-r1-repeat")
    eq(r1_reason(no_repeat, skip="repeat"), None, "mutant-r1-repeat")
    no_forced = ((0, 4, 0, 0), (0, 0, 4, 1), (1, 0, 0, 4))
    eq(r1_reason(no_forced), "r1-forced-b", "control-r1-forced")
    eq(r1_reason(no_forced, skip="forced"), None, "mutant-r1-forced")
    collision = r1_words((0, 0, 0), (0, 0, 0))
    eq(r1_reason(collision), "r1-pair-collision", "control-r1-pair")
    eq(r1_reason(collision, skip="injective"), None, "mutant-r1-pair")
    return {"enumerated": 512, "eligible": eligible, "rejected": rejected,
            "controls": ["repeat", "forced-symbol", "actual-pair-injectivity"]}


def inside_reason(word, skip=None):
    if len(word) != 4 or any(not isinstance(x, int) or x not in range(4)
                             for x in word):
        return "inside-domain"
    for i, j in P4:
        if skip != "w0" and (word[i], word[j]) == (0, 0):
            return "w0-pair-" + str(i) + str(j)
        if skip != "w1" and (word[i], word[j]) == (1, 1):
            return "w1-pair-" + str(i) + str(j)
    return None


def bits_reason(bits, skip_pair=None):
    if len(bits) != 3 or any(b not in (0, 1) for b in bits):
        return "bit-domain"
    for i, j in P3:
        if (i, j) != skip_pair and bits[i] == bits[j]:
            return "same-bit-" + str(i) + str(j)
    return None


def inside_bits():
    counts = Counter()
    for w in product(range(4), repeat=4):
        if inside_reason(w) is None:
            counts[sum(x in (0, 1) for x in w)] += 1
    eq([counts[k] for k in range(5)], [16, 64, 48, 0, 0], "inside-counts")
    for bits in product(range(2), repeat=3):
        need(bits_reason(bits) is not None, "three-distinct-binary-bits")
    eq(bits_reason((0, 1, 0)), "same-bit-02", "control-third-bit-pair")
    eq(bits_reason((0, 1, 0), skip_pair=(0, 2)), None, "mutant-third-bit-pair")
    for b in (0, 1):
        w = (b, b, 2, 3)
        eq(inside_reason(w), "w" + str(b) + "-pair-01", "control-P-bit")
        eq(inside_reason(w, skip="w" + str(b)), None, "mutant-P-bit")
    return {"allowed_by_degree_two_count": [counts[k] for k in range(5)],
            "three_binary_bits_accepted": 0,
            "controls": ["each-P-word", "third-bit-pair"]}


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
    return ((0, 0, 0, 0), (1, 1, 1, 1)) + tuple(
        (a, f[a], 4 + (g[a] >> 1), 4 + (g[a] & 1)) for a in range(4))


def star_reason(ss, skip_pair=None):
    if len(ss) != 4 or any(len(s) != 3 or any(b not in (0, 1) for b in s)
                           for s in ss):
        return "star-domain"
    for i, j in P3:
        if (i, j) != skip_pair and len({(s[i], s[j]) for s in ss}) != 4:
            return "star-projection-" + str(i) + str(j)
    return None


def layer_and_parity():
    valid_f = []
    layers = 0
    identity = (0, 1, 2, 3)
    for f in permutations(range(4)):
        if layer_reason(f, identity) is not None:
            continue
        valid_f.append(f)
        for g in permutations(range(4)):
            eq(layer_reason(f, g), None, "layer-guard")
            eq(pair_collision(layer_words(f, g)), None, "layer-actual-injectivity")
            layers += 1
        tick()
    eq((len(valid_f), layers), (14, 336), "layer-count")
    for f, g, skip, reason in [((2, 2, 0, 1), identity, "f", "f-not-bijective"),
                               ((1, 0, 2, 3), (0, 0, 2, 3), "g", "g-not-bijective"),
                               (identity, identity, "inside", "allinside-P-pair-collision")]:
        eq(layer_reason(f, g), reason, "control-" + reason)
        eq(layer_reason(f, g, skip=skip), None, "mutant-" + reason)
        need(pair_collision(layer_words(f, g)) is not None, "mutant-actual-collision")
    signatures = tuple(product(range(2), repeat=3))
    parity = Counter()
    accepted = 0
    for number, ss in enumerate(product(signatures, repeat=4)):
        if star_reason(ss) is None:
            accepted += 1
            ps = [sum(s) % 2 for s in ss]
            eq(len(set(ps)), 1, "star-common-parity")
            for a, b in combinations(range(4), 2):
                eq(sum(x != y for x, y in zip(ss[a], ss[b])), 2,
                   "star-pair-distance")
            parity[ps[0]] += 1
        if number % 256 == 0:
            tick()
    eq((accepted, parity[0], parity[1]), (48, 24, 24), "star-classes")
    bad = ((0, 0, 0), (0, 1, 0), (1, 0, 1), (1, 1, 1))
    eq(star_reason(bad), "star-projection-02", "control-star-projection")
    eq(star_reason(bad, skip_pair=(0, 2)), None, "mutant-star-projection")
    need(len({sum(s) % 2 for s in bad}) != 1, "mutant-star-mixed-parity")
    eq(star_reason(((0, 0, 0),) * 4), "star-projection-01",
       "control-parity-alone-insufficient")
    return {"valid_f": len(valid_f), "layers": layers,
            "ordered_star_signatures": accepted, "parity_counts": dict(parity),
            "controls": ["f", "g", "inside-P-pair", "star-each-pair",
                         "parity-alone"]}


def two_four_reason(hr, hc, skip=None):
    if (len(hr) != 4 or len(hc) != 4 or
            any(x < 0 or x > 3 for x in hr + hc)):
        return "two-four-domain"
    if sum(hr) != 4 or sum(hc) != 4:
        return "two-four-total"
    if skip != "parity" and any(x % 2 for x in hr + hc):
        return "two-four-odd-surplus"
    return None


def high_edges():
    three = Counter()
    four = Counter()
    bc = cb = 0
    for f in permutations(range(4)):
        if layer_reason(f, (0, 1, 2, 3)) is not None:
            continue
        forbidden = {(0, 0), (1, 1)} | {(a, f[a]) for a in range(4)}
        edges = tuple((a, b) for a in range(4) for b in range(4)
                      if (a, b) not in forbidden)
        eq(len(edges), 10, "local-E-cells")
        eq(tuple(sum(a == i for a, _ in edges) for i in range(4)),
           (2, 2, 3, 3), "local-E-row-degrees")
        eq(tuple(sum(b == j for _, b in edges) for j in range(4)),
           (2, 2, 3, 3), "local-E-column-degrees")
        for high in combinations(edges, 4):
            hr = tuple(sum(a == i for a, _ in high) for i in range(4))
            hc = tuple(sum(b == j for _, b in high) for j in range(4))
            if surplus_reason(hr) is not None or surplus_reason(hc) is not None:
                continue
            tr, tc = h_type(hr), h_type(hc)
            need(tr != "unclassified" and tc != "unclassified", "high-class")
            three[tr + tc] += 1
            if tr == "B":
                eq(tc, "C", "B-opposite-C")
                c = 2 if hr[2] == 3 else 3
                t = 3 if c == 2 else 2
                bj = 0 if hc[0] == 2 else 1
                eq({b for a, b in high if a == c},
                   {j for j in range(4) if hc[j] > 0}, "B-c-neighbors")
                eq({b for a, b in high if a == t}, {bj}, "B-t-neighbor")
                # c has degree three, all its positive neighbors are E cells.
                eq(f[c], 1 - bj, "B-forces-f-c")
                eq(f[1 - bj], bj, "B-forces-f-degree-two")
                need(f[bj] in (2, 3) and f[t] in (2, 3) and f[bj] != f[t],
                     "B-forces-f-T-symbols")
                bc += 1
            if tc == "B":
                eq(tr, "C", "B-opposite-C-transposed")
                c = 2 if hc[2] == 3 else 3
                t = 3 if c == 2 else 2
                bi = 0 if hr[0] == 2 else 1
                eq({a for a, b in high if b == c},
                   {i for i in range(4) if hr[i] > 0}, "BT-c-neighbors")
                eq({a for a, b in high if b == t}, {bi}, "BT-t-neighbor")
                cb += 1
        for high in combinations(edges, 2):
            hr = tuple(2 * sum(a == i for a, _ in high) for i in range(4))
            hc = tuple(2 * sum(b == j for _, b in high) for j in range(4))
            if surplus_reason(hr) is not None or surplus_reason(hc) is not None:
                continue
            eq((h_type(hr), h_type(hc)), ("A", "A"), "two-four-types")
            need(high[0][0] != high[1][0] and high[0][1] != high[1][1],
                 "two-four-disjoint-endpoints")
            four["AA"] += 1
        tick()
    need(bc > 0 and cb > 0 and four["AA"] > 0, "high-edges-nonvacuous")
    b, c = (0, 0, 3, 1), (2, 0, 1, 1)
    eq(two_four_reason(b, c), "two-four-odd-surplus", "control-two-four")
    eq(two_four_reason(b, c, skip="parity"), None, "mutant-two-four")
    return {"four-three_class_counts": dict(three),
            "two-four_class_counts": dict(four), "B_C": bc, "C_B": cb,
            "controls": ["two-four-even-increments"]}


def line_reason(bits, masks, skip=None):
    if len(bits) != 3 or any(b not in (0, 1) for b in bits) or len(masks) != 3:
        return "line-domain"
    if any(not isinstance(m, int) or m < 0 for m in masks):
        return "line-domain"
    if skip != "bound" and any(m & ~127 for m in masks):
        return "line-outside-seven"
    if skip != "size" and any(m.bit_count() != 3 for m in masks):
        return "line-size-not-three"
    if skip != "overlap":
        for i, j in P3:
            if bits[i] == bits[j] and masks[i] & masks[j]:
                return "line-equal-bit-overlap-" + str(i) + str(j)
    return None


def seven_word_lines():
    masks = tuple(sum(1 << x for x in s) for s in combinations(range(7), 3))
    feasible = {}
    for bits in product(range(2), repeat=3):
        count = 0
        for index, ms in enumerate(product(masks, repeat=3)):
            if line_reason(bits, ms) is None:
                count += 1
            if index % 1024 == 0:
                tick()
        feasible["".join(str(b) for b in bits)] = count
        if len(set(bits)) == 1:
            eq(count, 0, "B-monochrome-impossible")
        else:
            need(count > 0, "B-mixed-bit-relaxation-nonvacuous")
    fixtures = [((0, 0, 0), (7, 25, 42), "overlap", "line-equal-bit-overlap-01"),
                ((0, 1, 0), (3, 25, 100), "size", "line-size-not-three"),
                ((0, 0, 0), (7, 56, 448), "bound", "line-outside-seven")]
    for bits, masks, skip, reason in fixtures:
        eq(line_reason(bits, masks), reason, "control-" + reason)
        eq(line_reason(bits, masks, skip=skip), None, "mutant-" + reason)
    return {"line_assignments": feasible,
            "controls": ["same-bit-disjoint", "three-per-line", "seven-words"]}


def main():
    try:
        signal.signal(signal.SIGALRM, alarm)
        remaining = START + INTERNAL - time.monotonic()
        if remaining <= 0:
            raise Deadline("internal-deadline-before-start")
        signal.setitimer(signal.ITIMER_REAL, remaining)
        emit("begin", scope="necessary-local-projections-only",
             internal_deadline_seconds=INTERNAL, required_outer_seconds=55)
        stage("moments-and-party-counts", moments)
        stage("per-symbol-and-surplus", symbols)
        stage("r1-actual-pair-pigeonhole", r1_triples)
        stage("r2-allinside-symbol-bits", inside_bits)
        stage("r2-local-layer-and-star", layer_and_parity)
        stage("r2-high-edge-projections", high_edges)
        stage("type-B-seven-word-pigeonhole", seven_word_lines)
        emit("complete", completed=DONE, elapsed=time.monotonic() - START,
             result="NECESSARY_LOCAL_PROJECTIONS_ONLY_NOT_GLOBAL_P_E_OR_AME")
        return 0
    except Deadline as error:
        emit("incomplete", reason=str(error), completed=DONE,
             elapsed=time.monotonic() - START)
        return 2
    except Failure as error:
        emit("check-failed", reason=str(error), completed=DONE,
             elapsed=time.monotonic() - START)
        return 1
    except Exception as error:
        emit("error", error_type=type(error).__name__, reason=str(error),
             completed=DONE, elapsed=time.monotonic() - START)
        return 1
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)


if __name__ == "__main__":
    sys.exit(main())
