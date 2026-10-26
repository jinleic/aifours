#!/usr/bin/env python3
"""Unexecuted proposal: exact parent GO required. No solver or subprocess.

At most220 single-relative-3-cycle switches of one pinned decomposition.
A no-hit is never unrestricted Tuscan-2(11) nonexistence.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
import signal
import sys
import time

ROOT = Path(__file__).resolve().parent
INPUT = ROOT / "sources" / "etzion-example2-tuscan1-11.table"
INPUT_SHA = "a50fc2994053f669973f91b61ed64824d30afe390527e74d62e9e6beee6f1a20"


class Invalid(ValueError):
    pass


class CooperativeStop(Exception):
    pass


def stop(signum: int, frame: object) -> None:
    raise CooperativeStop(f"signal_{signum}")


def table_check(table: list[list[int]], n: int, depth: int) -> None:
    if len(table) != n or any(len(row) != n for row in table):
        raise Invalid("TABLE_SHAPE")
    universe = set(range(n))
    if any(any(type(x) is not int for x in row) or set(row) != universe for row in table):
        raise Invalid("ROW_PERMUTATION")
    for d in range(1, depth + 1):
        seen = set()
        for row in table:
            for c in range(n - d):
                edge = (row[c], row[c + d])
                if edge in seen:
                    raise Invalid(f"DISTANCE_{d}_REPEAT")
                seen.add(edge)
        if d == 1 and seen != {(a, b) for a in range(n) for b in range(n) if a != b}:
            raise Invalid("ADJACENT_UNIVERSE")


def hamiltonian(p: list[int]) -> bool:
    n = len(p)
    if set(p) != set(range(n)):
        return False
    seen, x = set(), 0
    while x not in seen:
        seen.add(x)
        x = p[x]
    return x == 0 and len(seen) == n


def decomposition_check(cycles: list[list[int]]) -> None:
    n = len(cycles) + 1
    seen = set()
    for p in cycles:
        if len(p) != n or set(p) != set(range(n)):
            raise Invalid("CYCLE_PERMUTATION")
        if not hamiltonian(p):
            raise Invalid("NON_HAMILTONIAN")
        for a, b in enumerate(p):
            if a == b or (a, b) in seen:
                raise Invalid("EDGE_REPEAT")
            seen.add((a, b))
    if seen != {(a, b) for a in range(n) for b in range(n) if a != b}:
        raise Invalid("EDGE_UNIVERSE")


def from_table(table: list[list[int]]) -> list[list[int]]:
    n = len(table)
    result = []
    for row in table:
        vertices = row + [n]
        p = [-1] * (n + 1)
        for a, b in zip(vertices, vertices[1:] + vertices[:1]):
            p[a] = b
        result.append(p)
    return result


def good_roots(cycles: list[list[int]]) -> set[int]:
    n = len(cycles[0])
    centers: dict[tuple[int, int], set[int]] = {}
    for p in cycles:
        for a in range(n):
            c, b = p[a], p[p[a]]
            witnesses = centers.setdefault((a, b), set())
            if c in witnesses:
                raise Invalid("REPEATED_CENTER")
            witnesses.add(c)
    allowed = set(range(n))
    for (a, b), witnesses in centers.items():
        if len(witnesses) == 2:
            allowed.intersection_update({a, b} | witnesses)
        elif len(witnesses) >= 3:
            allowed.intersection_update({a, b})
    return allowed


def cut_table(cycles: list[list[int]], root: int) -> list[list[int]]:
    symbols = [a for a in range(len(cycles[0])) if a != root]
    labels = {a: i for i, a in enumerate(symbols)}
    table = []
    for p in cycles:
        row, x = [], p[root]
        for _ in symbols:
            if x == root:
                raise Invalid("CUT_EARLY_RETURN")
            row.append(labels[x])
            x = p[x]
        if x != root:
            raise Invalid("CUT_NOT_CLOSED")
        table.append(row)
    return table


def inverse(p: list[int]) -> list[int]:
    result = [-1] * len(p)
    for a, b in enumerate(p):
        result[b] = a
    return result


def permutation_cycles(p: list[int]) -> list[list[int]]:
    seen, result = set(), []
    for start in range(len(p)):
        if start in seen:
            continue
        part, x = [], start
        while x not in seen:
            seen.add(x)
            part.append(x)
            x = p[x]
        if x != start:
            raise Invalid("NOT_A_PERMUTATION")
        result.append(part)
    return result


def return_map(p: list[int], tails: list[int]) -> dict[int, int]:
    domain, result = set(tails), {}
    for a in tails:
        x = p[a]
        for _ in range(len(p)):
            if x in domain:
                result[a] = x
                break
            x = p[x]
        else:
            raise Invalid("RETURN_MAP")
    return result


def one_cycle(mapping: dict[int, int], tails: list[int]) -> bool:
    seen, x = set(), tails[0]
    while x not in seen:
        seen.add(x)
        x = mapping[x]
    return x == tails[0] and seen == set(tails)


def switch(p: list[int], q: list[int], tails: list[int]) -> tuple[list[int], list[int], bool]:
    iq = inverse(q)
    relative = [iq[p[a]] for a in range(len(p))]
    ir = inverse(relative)
    ap, aq = return_map(p, tails), return_map(q, tails)
    predicted = one_cycle({a: ap[ir[a]] for a in tails}, tails) and one_cycle({a: aq[relative[a]] for a in tails}, tails)
    pp, qq = p[:], q[:]
    for a in tails:
        pp[a], qq[a] = q[a], p[a]
    actual = hamiltonian(pp) and hamiltonian(qq)
    if actual != predicted:
        raise Invalid("SWITCH_CRITERION_MISMATCH")
    return pp, qq, actual


def cycle_successor(vertices: list[int]) -> list[int]:
    result = [-1] * len(vertices)
    for a, b in zip(vertices, vertices[1:] + vertices[:1]):
        result[a] = b
    return result


def controls() -> list[dict[str, object]]:
    receipts = []
    def record(name: str, actual: object, expected: object) -> None:
        receipts.append({"name": name, "actual": actual, "expected": expected, "pass": actual == expected})
        if actual != expected:
            raise Invalid("CONTROL_FAILURE_" + name)
    field5 = [[(a + r) % 5 for a in range(5)] for r in range(1, 5)]
    decomposition_check(field5)
    record("circular_C5_all_roots", sorted(good_roots(field5)), list(range(5)))
    for root in range(5):
        table_check(cut_table(field5, root), 4, 2)
    bad = [p[:] for p in field5]
    bad[0][0] = bad[0][1]
    try:
        decomposition_check(bad)
        result = "VALID"
    except Invalid as exc:
        result = str(exc)
    record("duplicate_cycle_image", result, "CYCLE_PERMUTATION")
    bad = [p[:] for p in field5]
    bad[0] = bad[3][:]
    try:
        decomposition_check(bad)
        result = "VALID"
    except Invalid as exc:
        result = str(exc)
    record("duplicate_hamilton_cycle", result, "EDGE_REPEAT")
    p = cycle_successor([0, 1, 2, 3, 4])
    q = cycle_successor([0, 2, 1, 3, 4])
    record("positive_three_switch", switch(p, q, [0, 1, 2])[2], True)
    p = cycle_successor([0, 3, 1, 4, 2, 5])
    q = cycle_successor([0, 5, 2, 4, 1, 3])
    record("wrong_opposite_orientation", switch(p, q, [0, 1, 2])[2], False)
    return receipts


def main() -> int:
    if len(sys.argv) != 2:
        print("ERROR expected exclusive output directory", file=sys.stderr)
        return 64
    output = Path(sys.argv[1]).resolve()
    if not output.is_relative_to(ROOT):
        return 64
    raw = INPUT.read_bytes()
    if hashlib.sha256(raw).hexdigest() != INPUT_SHA:
        print("HOLD input hash mismatch", file=sys.stderr)
        return 2
    output.mkdir()
    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGALRM, stop)
    signal.setitimer(signal.ITIMER_REAL, 30.0)
    start = time.monotonic()
    status, detail, exit_code = "NEIGHBORHOOD_EXHAUSTED_NO_WITNESS", "", 0
    tested = hamilton_switches = 0
    control_receipts = []
    candidate = None
    try:
        control_receipts = controls()
        table = [[int(x) for x in line.split()] for line in raw.decode("ascii").splitlines()]
        table_check(table, 11, 1)
        cycles = from_table(table)
        decomposition_check(cycles)
        if good_roots(cycles):
            raise Invalid("SOURCE_NEGATIVE_ROOT_CONTROL")
        for a, c, b in [(11,10,2),(11,6,2),(11,3,2),(1,3,5),(1,6,5),(1,11,5)]:
            if not any(p[a] == c and p[c] == b for p in cycles):
                raise Invalid("SOURCE_SIX_TRIPLE_CONTROL")
        control_receipts.append({"name": "published_source_six_triple_obstruction", "pass": True})
        for i, j in itertools.combinations(range(11), 2):
            p, q = cycles[i], cycles[j]
            iq = inverse(q)
            relative = [iq[p[a]] for a in range(12)]
            for tails in permutation_cycles(relative):
                if len(tails) != 3:
                    continue
                tested += 1
                if tested > 220:
                    raise Invalid("NEIGHBORHOOD_BOUND")
                pp, qq, valid = switch(p, q, tails)
                if not valid:
                    continue
                hamilton_switches += 1
                changed = cycles[:]
                changed[i], changed[j] = pp, qq
                decomposition_check(changed)
                roots = good_roots(changed)
                if not roots:
                    continue
                root = min(roots)
                witness = cut_table(changed, root)
                table_check(witness, 11, 2)
                with (output / "candidate-table.json").open("x") as stream:
                    json.dump(witness, stream)
                    stream.write("\n")
                with (output / "candidate-cycles.json").open("x") as stream:
                    json.dump(changed, stream)
                    stream.write("\n")
                candidate = {"rows_0based": [i, j], "tails": tails, "root": root,
                             "table_sha256": hashlib.sha256((output / "candidate-table.json").read_bytes()).hexdigest()}
                status = "CANDIDATE_FOUND_AUTHOR_CHECK_ONLY"
                break
            if candidate is not None:
                break
    except CooperativeStop as exc:
        status, detail, exit_code = "UNKNOWN", str(exc), 75
    except Exception as exc:
        status, detail, exit_code = "ERROR", f"{type(exc).__name__}: {exc}", 2
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.0)
    receipt = {"status": status, "detail": detail, "elapsed_seconds": time.monotonic() - start,
               "controls": control_receipts, "tested_three_cycles": tested,
               "hamilton_switches": hamilton_switches, "candidate": candidate,
               "input_sha256": INPUT_SHA,
               "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "full_target_negative": False, "independent_verification": False,
               "solver_executed": False, "neighborhood_radius": 1}
    with (output / "settlement.json").open("x") as stream:
        json.dump(receipt, stream, indent=2)
        stream.write("\n")
    print(json.dumps(receipt, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
