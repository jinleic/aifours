#!/usr/bin/env python3
"""Bounded exact Z3 model of actual linear Tuscan-2(11) permutation rows.

Full mode fixes only the first row to 0..10 by a common bijective symbol
relabeling. This is WLOG: relabeling preserves both directed event equalities.
It does not impose a Latin column, cyclic wrap, or an order on other rows.

Repair mode fixes selected rows of an independently saved candidate, leaving
all other complete rows free. UNSAT in repair mode rules out only that fixed
neighborhood. An UNKNOWN is not an infeasibility result in either mode.

Usage:
  python3 SCRIPT OUTPUT.json TIMEOUT_MS SEED full
  python3 SCRIPT OUTPUT.json TIMEOUT_MS SEED repair CANDIDATE.json FREE_ROWS
FREE_ROWS is a comma-separated list of 1-based row indices. Output is exclusive.
Any SAT table must be checked by frontier-20261028-tuscan-check-v1.py.
"""

import hashlib
import json
import sys
import time
from pathlib import Path

import z3

N = 11


def parse_args(argv):
    if len(argv) not in (5, 7):
        raise ValueError("OUTPUT.json TIMEOUT_MS SEED full | repair CANDIDATE.json FREE_ROWS")
    out = Path(argv[1])
    timeout_ms = int(argv[2])
    seed = int(argv[3])
    mode = argv[4]
    if timeout_ms <= 0 or timeout_ms > 600000 or seed < 0 or seed > 4294967295:
        raise ValueError("timeout must be 1..600000 ms; seed must be 0..2^32-1")
    if mode == "full" and len(argv) == 5:
        return out, timeout_ms, seed, mode, None, set()
    if mode != "repair" or len(argv) != 7:
        raise ValueError("mode or argument count invalid")
    candidate = Path(argv[5])
    free = {int(value) - 1 for value in argv[6].split(",")}
    if not free or not free.issubset(set(range(N))):
        raise ValueError("FREE_ROWS must list 1-based rows in 1..11")
    return out, timeout_ms, seed, mode, candidate, free


def main(argv):
    out, timeout_ms, seed, mode, candidate, free = parse_args(argv)
    candidate_data = None
    candidate_sha = None
    if candidate is not None:
        raw = candidate.read_bytes()
        candidate_sha = hashlib.sha256(raw).hexdigest()
        candidate_data = json.loads(raw)
        old_rows = candidate_data.get("rows")
        if (not isinstance(old_rows, list) or len(old_rows) != N or
                any(not isinstance(row, list) or len(row) != N or
                    any(type(x) is not int for x in row) or sorted(row) != list(range(N))
                    for row in old_rows)):
            raise ValueError("candidate is not eleven permutations of 0..10")

    # Claim output exclusively before starting a bounded search; never overwrite.
    with out.open("x", encoding="utf-8") as stream:
        started = time.monotonic()
        solver = z3.Solver()
        solver.set(timeout=timeout_ms, random_seed=seed)
        rows = [[z3.Int(f"r{r}_c{c}") for c in range(N)] for r in range(N)]
        for row in rows:
            solver.add(*(z3.And(x >= 0, x < N) for x in row))
            solver.add(z3.Distinct(*row))
        if mode == "full":
            solver.add(*(rows[0][c] == c for c in range(N)))
        else:
            for r in range(N):
                if r not in free:
                    solver.add(*(rows[r][c] == old_rows[r][c] for c in range(N)))
        for d in (1, 2):
            events = [N * rows[r][c] + rows[r][c + d]
                      for r in range(N) for c in range(N - d)]
            solver.add(z3.Distinct(*events))
        construction_ms = round((time.monotonic() - started) * 1000)
        solving_started = time.monotonic()
        verdict = solver.check()
        solve_ms = round((time.monotonic() - solving_started) * 1000)
        status = str(verdict)
        result = {
            "schema": 1,
            "kind": "bounded_z3_actual_tuscan2_row_constraints",
            "n": N,
            "mode": mode,
            "timeout_ms": timeout_ms,
            "random_seed": seed,
            "z3_version": z3.get_version_string(),
            "solver_status": status,
            "construction_ms": construction_ms,
            "solve_ms": solve_ms,
            "original_symmetry": "row 1 = 0..10 by common symbol relabeling" if mode == "full" else None,
            "candidate_sha256": candidate_sha,
            "fixed_rows_1based": [] if mode == "full" else [r + 1 for r in range(N) if r not in free],
            "no_column_latin_or_wrap_assumption": True,
            "interpretation": (
                "Full model: UNSAT would exclude all arrays modulo proven symbol relabeling; "
                "external proof/certificate and independent audit still required for acceptance. "
                "Repair model: UNSAT excludes only this frozen-row neighborhood. "
                "UNKNOWN is not a nonexistence result. SAT requires independent row verification."
            ),
        }
        if verdict == z3.sat:
            model = solver.model()
            result["rows"] = [[model.eval(x).as_long() for x in row] for row in rows]
            result.update({
                "zero_score_claim": True,
                "best_pair_collision_score": 0,
                "d1_pair_collisions": 0,
                "d2_pair_collisions": 0,
                "d1_excess_events": 0,
                "d2_excess_events": 0,
            })
        elif verdict == z3.unknown:
            result["reason_unknown"] = solver.reason_unknown()
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({
        "output": str(out), "mode": mode, "status": status,
        "reason_unknown": result.get("reason_unknown"),
        "construction_ms": construction_ms, "solve_ms": solve_ms,
        "fixed_rows_1based": result["fixed_rows_1based"],
    }, sort_keys=True))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        raise SystemExit(str(exc)) from exc
