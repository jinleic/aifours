#!/usr/bin/env python3
"""Finite orbit counts for extended-group-analysis.md; no existence assertion."""
from collections import Counter
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys
import time


def translation_key(block, n):
    finite = tuple(x for x in block if x < n)
    fixed = tuple(x for x in block if x >= n)
    return min(tuple(sorted((x-t) % n for x in finite))+fixed for t in finite)


def order(a, n):
    powers = [a]
    while powers[-1] != 1:
        powers.append(powers[-1]*a % n)
    return powers


def main():
    started = time.monotonic()
    root = Path(__file__).resolve().parent.parent
    output = root / "evidence/group-arithmetic.json"
    if output.exists():
        raise SystemExit("preserve original receipt; choose a new output path for a replay")
    record = {"source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "command": sys.argv, "seed": None, "solver_threads": 0,
              "status": "EXACT_ENUMERATION", "restrictions": "n=55,85 cyclic transversal STS scalar/affine involutions; C29 invariant resolved large sets", "scalar_involutions": [], "all_units": [], "affine_involutions": [], "c29": {}}
    for n in (55, 85):
        triples = tuple(itertools.combinations(range(n+2), 3))
        orbits = {translation_key(b, n) for b in triples}
        assert len(orbits) == (n+2)*(n+1)//6
        for a in range(1, n):
            if math.gcd(a, n) != 1:
                continue
            powers = order(a, n)
            involutions = [p for p in powers if p != 1 and p*p % n == 1]
            fixed_seven = [p for p in powers if math.gcd(p-1, n) == 5]
            reason = "identity" if a == 1 else ("nonidentity involution power: fixed-orbit/fixed-block contradiction" if involutions else "fixed seven-point cyclic transversal subsystem")
            assert a == 1 or involutions or fixed_seven
            record["all_units"].append({"n": n, "multiplier": a, "order": len(powers), "reason": reason,
                                        "involution_powers": involutions, "fixed_seven_powers": fixed_seven})
            if a*a % n != 1:
                continue
            offsets = [b for b in range(n) if (a+1)*b % n == 0]
            for b in offsets:
                c = b*pow(2, -1, n) % n
                assert (a*c+b) % n == c
                assert all((a*(x+c)+b-c) % n == a*x % n for x in range(n))
            record["affine_involutions"].append({"n": n, "a": a, "b_values": offsets, "translation_center": "b/2 mod n"})
            if a == 1:
                continue
            m = math.gcd(a-1, n)
            f, t = m+2, (n-m)//2
            fixed_orbits = sum(translation_key(tuple(sorted(a*x % n if x < n else x for x in b)), n) == b for b in orbits)
            fixed_triples = sum(tuple(sorted(a*x % n if x < n else x for x in b)) == b for b in triples)
            formula_orbits = (math.comb(f, 3)+f*t)//m
            sts_fixed_blocks = f*(f-1)//6+t
            assert fixed_triples == math.comb(f, 3)+f*t
            assert fixed_triples == m*fixed_orbits
            assert fixed_orbits == formula_orbits
            assert fixed_orbits-sts_fixed_blocks == (n-m)//m > 0
            record["scalar_involutions"].append({"n": n, "a": a, "m": m, "fixed_points": f,
                "transpositions": t, "enumerated_fixed_triples": fixed_triples,
                "enumerated_fixed_translation_orbits": fixed_orbits,
                "required_fixed_blocks_in_any_invariant_STS": sts_fixed_blocks,
                "excess": fixed_orbits-sts_fixed_blocks})
    p = 29
    aaa = {translation_key(b, p) for b in itertools.combinations(range(p), 3)}
    bad = sorted(b for b in aaa if len({min((y-x) % p, (x-y) % p) for x, y in itertools.combinations(b, 2)}) != 3)
    assert len(aaa) == 126 and len(bad) == 14
    signatures = []
    for aa in itertools.product(range(5), repeat=3):
        A = sum(aa)
        C = 2*A-13
        if C < 0:
            continue
        out = [14-3*x for x in aa]
        incoming = [3*x+1-C for x in aa]
        if min(incoming) < 0:
            continue
        K = incoming[1]-out[2]+incoming[0]
        low = max(0, K-out[1], K-incoming[0])
        high = min(out[0], K, out[2]+K-incoming[0])
        if low <= high:
            signatures.append({"AAA_per_layer": aa, "AAA_total": A, "AAB_total": 42-3*A,
                               "ABC_free_class_total": C, "AAB_row_sums": out,
                               "AAB_column_sums": incoming, "B01_integer_interval": [low, high]})
    usable = 3*(len(aaa)-len(bad))
    possibilities = [f for f in range(86) if (85-f) % 29 == 0]
    survivors = [f for f in possibilities if 7*f <= usable]
    assert survivors == [27]
    record["c29"] = {"AAA_orbits_per_layer": len(aaa), "unusable_AP_orbits_per_layer": bad,
        "usable_AAA_orbits_all_layers": usable, "fixed_constituent_possibilities_before_incidence": possibilities,
        "minimum_AAA_orbits_per_fixed_resolved_KTS": 7, "remaining_fixed_constituent_counts": survivors,
        "free_constituent_orbits_required": 2, "forced_AP_orbits_in_free_seeds": 3*len(bad),
        "feasible_aggregate_signatures": signatures,
        "signature_counts_by_A": dict(sorted(Counter(x["AAA_total"] for x in signatures).items()))}
    record["instance_sha256"] = hashlib.sha256(json.dumps({"n": [55, 85], "p": p, "action": "specified in source"}, sort_keys=True).encode()).hexdigest()
    record["wall_clock_cap_seconds"] = None
    record["runtime_seconds"] = time.monotonic()-started
    output.write_text(json.dumps(record, indent=2)+"\n")
    print(json.dumps({"scalar_involutions": record["scalar_involutions"], "C29_survivors": survivors,
                      "C29_signature_counts": record["c29"]["signature_counts_by_A"],
                      "runtime_seconds": record["runtime_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
