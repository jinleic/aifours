#!/usr/bin/env python3
"""Independently regenerate the four LOWER46 completion CNFs; import no lane code.

N determines six sets of hole lines. An officer may occupy exactly those points
lying on none of these lines. Every non-hole line must contain exactly one
officer. For byte binding, encode at-most-one with a sequential prefix counter
in the documented pair/point order. Exhaustive controls check that counter's
existential projection; the order-three orthogonal-array control checks a
mathematically valid completion, including its auxiliary assignment.
"""
import argparse
import hashlib
import itertools
import json
import subprocess
from pathlib import Path

PAIRS = ((0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (1, 2))
HERE = Path(__file__).resolve().parent
SNAP = HERE / "ame46-lower46-parent-inputs-v1"


def at_most_one(literals, next_var):
    """s_i records whether any of x_0,...,x_i is true."""
    if len(literals) <= 1:
        return [], next_var, []
    prefix = list(range(next_var + 1, next_var + len(literals)))
    clauses = [[-literals[0], prefix[0]]]
    for i in range(1, len(literals) - 1):
        clauses.extend(([-literals[i], prefix[i]],
                        [-prefix[i - 1], prefix[i]],
                        [-literals[i], -prefix[i - 1]]))
    clauses.append([-literals[-1], -prefix[-1]])
    return clauses, prefix[-1], prefix


def completion(N, q=6):
    universe = list(itertools.product(range(q), repeat=4))
    holes = {p: {tuple(x[i] for i in p) for x in N} for p in PAIRS}
    allowed = [x for x in universe
               if all(tuple(x[i] for i in p) not in holes[p] for p in PAIRS)]
    variable = {x: i + 1 for i, x in enumerate(allowed)}
    clauses, counters = [], []
    nv = len(allowed)
    for p in PAIRS:
        for z in itertools.product(range(q), repeat=2):
            if z in holes[p]:
                continue
            literals = [variable[x] for x in allowed if tuple(x[i] for i in p) == z]
            clauses.append(literals)
            counter, nv, prefix = at_most_one(literals, nv)
            clauses.extend(counter)
            counters.append((literals, prefix))
    data = (f"p cnf {nv} {len(clauses)}\n" +
            "".join(" ".join(map(str, c)) + " 0\n" for c in clauses)).encode()
    return data, allowed, clauses, counters, nv


def satisfied(clauses, assignment):
    return all(any(assignment[abs(l)] == (l > 0) for l in clause) for clause in clauses)


def controls():
    rows = []
    for n in range(9):
        cl, nv, _ = at_most_one(list(range(1, n + 1)), n)
        projections = set()
        for bits in itertools.product((False, True), repeat=nv):
            a = {i + 1: bit for i, bit in enumerate(bits)}
            if satisfied(cl, a):
                projections.add(bits[:n])
        expected = {b for b in itertools.product((False, True), repeat=n) if sum(b) <= 1}
        rows.append({"n": n, "existential_projection_equal": projections == expected,
                     "projected_assignments": len(projections)})
    _, allowed, clauses, counters, nv = completion(set(), 3)
    T = {(a, b, (a + b) % 3, (a + 2 * b) % 3)
         for a in range(3) for b in range(3)}
    a = {i + 1: x in T for i, x in enumerate(allowed)}
    for literals, prefix in counters:
        v = False
        for lit, aux in zip(literals, prefix):
            v |= a[lit]
            a[aux] = v
    positive = satisfied(clauses, a)
    bad = dict(a)
    first = next(i for i, x in enumerate(allowed, 1) if x in T)
    bad[first] = False
    negative = not satisfied(clauses, bad)
    return {"counter_projection_controls": rows,
            "order3_orthogonal_array_completion_satisfies": positive,
            "removing_one_required_officer_rejected": negative,
            "pass": all(r["existential_projection_equal"] for r in rows) and positive and negative}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    rows = []
    for report in sorted((SNAP / "evidence").glob("large_t_gen_t*_e*.json")):
        j = json.loads(report.read_text())
        for profile in j["profiles"]:
            tag = f't{j["t"]}_e{j["e"]}_' + "_".join(
                "-".join(map(str, p)) for p in profile["profile"])
            for i, rep in enumerate(profile["reps"]):
                path = SNAP / "explore/large_t_gen" / f"{tag}_rep{i}_completion.cnf"
                if not path.exists():
                    continue
                N = {tuple(map(int, s)) for s in rep["N"]}
                data, allowed, clauses, _, nv = completion(N)
                expected = path.read_bytes()
                rows.append({"cnf": str(path.relative_to(SNAP)), "allowed_points": len(allowed),
                             "variables": nv, "clauses": len(clauses),
                             "pinned_sha256": hashlib.sha256(expected).hexdigest(),
                             "regenerated_sha256": hashlib.sha256(data).hexdigest(),
                             "byte_equal": data == expected,
                             "closed_form_header": nv == 7 * len(allowed) - 6 * j["t"] and
                             len(clauses) == 18 * len(allowed) - 18 * j["t"]})
    control = controls()
    passed = len(rows) == 4 and all(r["byte_equal"] and r["closed_form_header"] for r in rows) and control["pass"]
    receipt = {"recorded_at_pt": subprocess.check_output(["date", "+%Y-%m-%d %H:%M:%S %Z"], text=True).strip(),
               "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "rows": rows, "controls": control, "verdict": "PASS" if passed else "FAIL",
               "scope": "completion-CNF binding and counter semantics; UNSAT proof verification is a separate receipt"}
    with args.output.open("x") as f:
        json.dump(receipt, f, indent=1)
        f.write("\n")
    print(json.dumps({"verdict": receipt["verdict"], "cnfs": len(rows), "controls_pass": control["pass"]}))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
