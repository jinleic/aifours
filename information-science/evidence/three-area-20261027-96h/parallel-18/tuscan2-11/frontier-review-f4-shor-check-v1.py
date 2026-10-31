#!/usr/bin/env python3
"""Independent finite checks of the f4 Shor proof's displayed invariants.

No author checker is imported. The all-order statements still need the written
proof and are not inferred from a finite sweep. Output is exclusively created.
Usage: python3 SCRIPT OUTPUT.json MAX_N
"""
import itertools
import json
import sys
import time
from collections import Counter
from pathlib import Path

A = {0, 3, 8, 11}
Y = {0: {0, 1, 7, 13, 14}, 3: {0, 2, 4, 6},
     8: {0, 2, 4, 6}, 11: {0, 1, 2}}
S = [(head, tail) for head in sorted(A) for tail in sorted(Y[head])]


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def exact_tiling(n, cap):
    if n % 4:
        return {"n": n, "status": "no_by_cardinality", "nodes": 0}
    full = (1 << n) - 1
    masks = [sum(1 << ((a + j) % n) for a in A) for j in range(n)]
    choices = [[j for j in range(n) if masks[j] & (1 << pos)] for pos in range(n)]
    nodes = 0
    unknown = False

    def search(covered):
        nonlocal nodes, unknown
        nodes += 1
        if nodes > cap:
            unknown = True
            return False
        if covered == full:
            return True
        best = None
        for pos in range(n):
            if covered & (1 << pos):
                continue
            fits = [j for j in choices[pos] if not masks[j] & covered]
            if not fits:
                return False
            if best is None or len(fits) < len(best):
                best = fits
                if len(best) == 1:
                    break
        for j in best:
            if search(covered | masks[j]):
                return True
            if unknown:
                return False
        return False

    found = search(0)
    return {"n": n, "status": "yes" if found else ("unknown_node_cap" if unknown else "no_exhausted"),
            "nodes": nodes}


def word(pair):
    return "a" * pair[0] + "b" + "a" * pair[1]


def main(argv):
    if len(argv) != 3:
        raise ValueError("usage: SCRIPT OUTPUT.json MAX_N")
    out, max_n = Path(argv[1]), int(argv[2])
    if not 48 <= max_n <= 1000:
        raise ValueError("MAX_N must be 48..1000")
    started = time.monotonic()
    check(len(S) == 16 and len(set(S)) == 16, "original source expansion")
    d = {abs(x-y) for tails in Y.values() for x in tails for y in tails if x != y}
    e = {abs(x-y) for x in A for y in A if x != y}
    expected_d = {1, 2, 4, 6, 7, 12, 13, 14}
    expected_e = {3, 5, 8, 11}
    check(d == expected_d and e == expected_e, "difference sets")
    sums = {x+y for x in d for y in e}
    check(sums == set(range(4, 26)) - {8}, "D+E coverage")
    check(all(any(v % n == 0 for v in sums) for n in range(1, 26)), "small-n exclusion")

    hole_cases = 0
    for n in range(26, max_n + 1):
        for head, targets in ((0, (6, 19)), (11, (6, 7))):
            old = Y[head]
            old_sums = {(j+a) % n for j in old for a in A}
            for target in targets:
                check(target % n not in old_sums, f"target already covered n={n},head={head}")
                for a in A:
                    j = (target-a) % n
                    check(j not in {y % n for y in old}, "candidate already in old row")
                    check(any((j+v) % n == (anchor+w) % n
                              for anchor in old for v in A for w in A),
                          f"unblocked hole n={n},head={head}")
                hole_cases += 1

    # Independent direct concatenation for every member of the rectangle in a
    # bounded n range. Events/keys use the full actual source expansion.
    signed = {x-y for tails in Y.values() for x in tails for y in tails if x != y}
    tail_offsets = {j+v-w for j in Y[0] for v in A for w in A}
    old_columns = set().union(*Y.values())
    rectangle_checks = 0
    for n in range(37, max_n + 1):
        heads = {x % n for x in signed}
        tails = {x % n for x in tail_offsets} - {x % n for x in old_columns}
        check(len(heads) == 16 and len(tails) == 25, "rectangle size")
        for i, s in itertools.product(sorted(heads), sorted(tails)):
            atoms = S + [(i, s)]
            keys = [(u, (v+x) % n, y) for (u, v) in atoms for (x, y) in atoms]
            check(len(keys) == len(set(keys)), f"two-boundary collision n={n},i={i},s={s}")
            first = next((t, p, q) for t in A for p in Y[t] for q in Y[t]
                         if p != q and (p-q) % n == i)
            j, v, w = next((j, v, w) for j in Y[0] for v in A for w in A
                           if (j+v-w) % n == s)
            t, p, q = first
            gap1_left, gap1_right = p, q+i
            gap2_left, gap2_right = j+v, s+w
            cap1, cap2 = max(gap1_left, gap1_right), max(gap2_left, gap2_right)
            check((cap1-gap1_left) % n == 0 and (cap1-gap1_right) % n == 0, "pad1")
            check((cap2-gap2_left) % n == 0 and (cap2-gap2_right) % n == 0, "pad2")
            left = (word((t,p)) + "a"*(cap1-gap1_left) + word((0,j))
                    + "a"*(cap2-gap2_left) + word((v,0)))
            right = (word((t,q)) + "a"*(cap1-gap1_right) + word((i,s))
                     + "a"*(cap2-gap2_right) + word((w,0)))
            check(left == right and (i, s) not in S, f"raw ambiguity n={n},i={i},s={s}")
            rectangle_checks += 1
    left = word((0,1)) + word((0,0)) + word((3,0))
    right = word((0,0)) + word((1,3)) + word((0,0))
    check(left == right, "un-padded ambiguity")

    parity_cases = Counter()
    tilings = 0
    for n in range(26, max_n + 1):
        k, t = 0, n
        while t % 2 == 0:
            k += 1
            t //= 2
        if 1 <= k <= 3:
            residue_counts = Counter(a % (2**k) for a in A)
            check(all(v % 2 == 0 for v in residue_counts.values()) and n // (2**k) % 2 == 1,
                  "parity-class premise")
            parity_cases[k] += 1
        if n % 16 == 0:
            jset = {v+16*k for k in range(n//16) for v in (0,2,4,6)}
            sums_list = [(a+j) % n for a in A for j in jset]
            check(len(sums_list) == n and len(set(sums_list)) == n, "explicit cyclic tiling")
            tilings += 1

    exact_tilings = [exact_tiling(n, 100000) for n in range(12, 49)]
    for item in exact_tilings:
        if item["status"] != "unknown_node_cap":
            check((item["status"] == "yes") == (item["n"] % 16 == 0), "exact tiling discrepancy")
    result = {
        "kind": "independent_f4_bounded_symbolic_checks", "max_n": max_n,
        "source_atoms": len(S), "row_difference_positive": sorted(d),
        "column_difference_positive": sorted(e), "tail_offsets": sorted(tail_offsets),
        "n_1_to_25_excluded_by_sum_divisibility": True,
        "row_hole_claims_checked": hole_cases,
        "rectangle_pair_n_checks": rectangle_checks,
        "each_rectangle_case_verified": "two-boundary keys and explicit equal raw concatenations",
        "un_padded_actual_word_equality": left,
        "parity_orders_by_v2": dict(parity_cases),
        "explicit_tilings_checked": tilings,
        "exact_cover_tilings_12_to_48": exact_tilings,
        "elapsed_ms": round((time.monotonic()-started)*1000),
        "scope": "Bounded exact checks only; not a substitute for all-order proof or independent-model/formal review.",
    }
    with out.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"output": str(out), "max_n": max_n,
                      "row_hole_claims_checked": hole_cases,
                      "rectangle_pair_n_checks": rectangle_checks,
                      "parity_orders_by_v2": dict(parity_cases),
                      "explicit_tilings_checked": tilings,
                      "exact_cover_status_counts": dict(Counter(x["status"] for x in exact_tilings)),
                      "elapsed_ms": result["elapsed_ms"]}, sort_keys=True))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except (ValueError, OSError) as exc:
        raise SystemExit(str(exc)) from exc
