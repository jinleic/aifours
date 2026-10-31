#!/usr/bin/env python3
"""Construct and run a bounded SAT model of unrestricted T2(11) rows.

Usage: python3 SCRIPT OUT.json OUT.cnf SECONDS SEED full
   or: python3 SCRIPT OUT.json OUT.cnf SECONDS SEED repair CANDIDATE.json FREE_ROWS

The exact event encoding uses position/symbol variables and one auxiliary per
row-position-pair event. Sequential at-most-one constraints prevent a repeated
ordered event separately at distances 1 and 2. Full mode normalizes row one by
a common symbol relabeling, with no other symmetry or Latin column condition.
Repair mode freezes candidate row slots except the specified 1-based FREE_ROWS;
UNSAT there concerns only that neighborhood. All output files are exclusive.
SAT tables must be checked by the separate actual-row event checker. This tool
runs one single-threaded Kissat invocation with an internal bounded time.
"""

import hashlib
import itertools
import json
import subprocess
import sys
import time
from pathlib import Path

N = 11
XCOUNT = N ** 3


def xvar(r, c, symbol):
    return 1 + (r * N + c) * N + symbol


class CNF:
    def __init__(self):
        self.variables = XCOUNT
        self.clauses = []

    def new(self):
        self.variables += 1
        return self.variables

    def add(self, *literals):
        self.clauses.append(literals)

    def pairwise_amo(self, values):
        for a, b in itertools.combinations(values, 2):
            self.add(-a, -b)

    def sequential_amo(self, values):
        if len(values) < 2:
            return
        seq = [self.new() for _ in range(len(values) - 1)]
        self.add(-values[0], seq[0])
        for i in range(1, len(values) - 1):
            self.add(-values[i], seq[i])
            self.add(-seq[i - 1], seq[i])
            self.add(-values[i], -seq[i - 1])
        self.add(-values[-1], -seq[-1])


def parse(argv):
    if len(argv) not in (6, 8):
        raise ValueError("OUT.json OUT.cnf SECONDS SEED full | repair CANDIDATE FREE_ROWS")
    output, cnf = Path(argv[1]), Path(argv[2])
    seconds, seed = int(argv[3]), int(argv[4])
    mode = argv[5]
    if not 1 <= seconds <= 600 or not 0 <= seed <= 2147483647:
        raise ValueError("SECONDS must be 1..600 and SEED must be 0..2^31-1")
    if mode == "full" and len(argv) == 6:
        return output, cnf, seconds, seed, mode, None, set()
    if mode != "repair" or len(argv) != 8:
        raise ValueError("invalid mode/argument count")
    free = {int(x) - 1 for x in argv[7].split(",")}
    if not free or not free.issubset(set(range(N))):
        raise ValueError("FREE_ROWS must contain row indices in 1..11")
    return output, cnf, seconds, seed, mode, Path(argv[6]), free


def build(mode, candidate_rows, free):
    formula = CNF()
    # Each position has exactly one symbol, and each symbol appears once per row.
    for r in range(N):
        for c in range(N):
            values = [xvar(r, c, a) for a in range(N)]
            formula.add(*values)
            formula.pairwise_amo(values)
        for a in range(N):
            values = [xvar(r, c, a) for c in range(N)]
            formula.add(*values)
            formula.pairwise_amo(values)
    if mode == "full":
        for c in range(N):
            formula.add(xvar(0, c, c))
    else:
        for r in range(N):
            if r not in free:
                for c in range(N):
                    formula.add(xvar(r, c, candidate_rows[r][c]))
    # Event variable iff the two actual symbols occupy its linear endpoints.
    # At distance 1, every ordered unequal pair is constrained to appear once;
    # at distance 2, it may appear at most once. No cross-distance prohibition.
    for d in (1, 2):
        for a in range(N):
            for b in range(N):
                if a == b:
                    continue
                event_vars = []
                for r in range(N):
                    for c in range(N - d):
                        y = formula.new()
                        left, right = xvar(r, c, a), xvar(r, c + d, b)
                        formula.add(-y, left)
                        formula.add(-y, right)
                        formula.add(-left, -right, y)
                        event_vars.append(y)
                formula.sequential_amo(event_vars)
                if d == 1:
                    formula.add(*event_vars)
    return formula


def main(argv):
    output, cnf_path, seconds, seed, mode, candidate, free = parse(argv)
    candidate_sha = None
    candidate_rows = None
    if candidate is not None:
        raw = candidate.read_bytes()
        candidate_sha = hashlib.sha256(raw).hexdigest()
        candidate_rows = json.loads(raw).get("rows")
        if (not isinstance(candidate_rows, list) or len(candidate_rows) != N or
                any(not isinstance(row, list) or len(row) != N or
                    any(type(x) is not int for x in row) or sorted(row) != list(range(N))
                    for row in candidate_rows)):
            raise ValueError("candidate must contain eleven permutations of 0..10")

    # Exclusivity prevents accidental overwrites of earlier evidence.
    with output.open("x", encoding="utf-8") as out, cnf_path.open("x", encoding="ascii") as cnf:
        start = time.monotonic()
        formula = build(mode, candidate_rows, free)
        cnf.write(f"p cnf {formula.variables} {len(formula.clauses)}\n")
        for clause in formula.clauses:
            cnf.write(" ".join(map(str, clause)) + " 0\n")
        cnf.flush()
        construction_ms = round((time.monotonic() - start) * 1000)
        command = ["kissat", "--sat", f"--time={seconds}", f"--seed={seed}", str(cnf_path)]
        solve_start = time.monotonic()
        try:
            process = subprocess.run(command, capture_output=True, text=True,
                                     timeout=seconds + 15, check=False)
            returncode = process.returncode
            stdout, stderr = process.stdout, process.stderr
            supervisory_timeout = False
        except subprocess.TimeoutExpired as exc:
            returncode = None
            stdout = exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")
            stderr = exc.stderr.decode() if isinstance(exc.stderr, bytes) else (exc.stderr or "")
            supervisory_timeout = True
        solve_ms = round((time.monotonic() - solve_start) * 1000)
        if returncode == 10 and "s SATISFIABLE" in stdout:
            status = "sat"
        elif returncode == 20 and "s UNSATISFIABLE" in stdout:
            status = "unsat_unverified"
        elif returncode in (0, None):
            status = "unknown"
        else:
            status = "solver_error"
        result = {
            "schema": 1, "kind": "bounded_kissat_actual_tuscan2_row_constraints",
            "n": N, "mode": mode, "seed": seed, "time_limit_seconds": seconds,
            "cnf_path": str(cnf_path), "cnf_sha256": hashlib.sha256(cnf_path.read_bytes()).hexdigest(),
            "variables": formula.variables, "clauses": len(formula.clauses),
            "solver_command": command, "solver_returncode": returncode,
            "supervisory_timeout": supervisory_timeout, "solver_status": status,
            "construction_ms": construction_ms, "solve_ms": solve_ms,
            "candidate_sha256": candidate_sha,
            "fixed_rows_1based": [] if mode == "full" else [r + 1 for r in range(N) if r not in free],
            "normalization": "row 1 = 0..10 by common symbol relabeling" if mode == "full" else None,
            "no_column_latin_or_wrap_assumption": True,
            "solver_stdout": stdout, "solver_stderr": stderr,
            "scope": "Repair UNSAT concerns only the stated fixed rows. Full UNSAT would still need a separately checked proof and encoding audit. UNKNOWN or resource limits prove nothing. SAT tables require independent event verification.",
        }
        if status == "sat":
            assigned = set()
            for line in stdout.splitlines():
                if line.startswith("v "):
                    assigned.update(int(part) for part in line.split()[1:] if int(part) > 0)
            rows = []
            for r in range(N):
                row = []
                for c in range(N):
                    selected = [a for a in range(N) if xvar(r, c, a) in assigned]
                    if len(selected) != 1:
                        raise ValueError(f"solver model did not assign exactly one symbol at {r},{c}")
                    row.append(selected[0])
                rows.append(row)
            result["rows"] = rows
            result.update({"zero_score_claim": True, "best_pair_collision_score": 0,
                           "d1_pair_collisions": 0, "d2_pair_collisions": 0,
                           "d1_excess_events": 0, "d2_excess_events": 0})
        json.dump(result, out, indent=2, sort_keys=True)
        out.write("\n")
    print(json.dumps({"output": str(output), "cnf_path": str(cnf_path), "mode": mode,
                      "status": status, "returncode": returncode,
                      "construction_ms": construction_ms, "solve_ms": solve_ms,
                      "variables": formula.variables, "clauses": len(formula.clauses)}, sort_keys=True))
    if status == "solver_error":
        raise SystemExit("solver failed; see captured output")


if __name__ == "__main__":
    try:
        main(sys.argv)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        raise SystemExit(str(exc)) from exc
