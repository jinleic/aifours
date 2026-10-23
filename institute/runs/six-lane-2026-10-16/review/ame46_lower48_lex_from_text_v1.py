#!/usr/bin/env python3
"""Regenerate the 37 load-bearing LOWER48 final CNFs from the WRITTEN r2 schema.

Base clauses still come from the pinned base generator (bound for LOWER46). The
generator list, lex-leader chains, variable numbering, blocking clauses and
composition are written here from LOWER48 r2 section 3 only; large_t_lex.py is
not imported. Matching SHA-256 values show the RUP-verified CNFs are exactly the
written ones.
"""
import hashlib
import itertools
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SNAP = HERE / "ame46-lower48-parent-inputs-v1"
REPLAY = HERE / "ame46-lower48-parent-replay-v1/result.json"
sys.path.insert(0, str(SNAP / "code"))
import large_t_gen as base


def written_generators(prof, points):
    """r2: coordinate swaps (i,i+1) of equal parts, then value swaps inside d-classes."""
    out = []
    for i in range(3):
        if tuple(prof[i]) == tuple(prof[i + 1]):
            out.append({x: tuple(x[i + 1] if k == i else x[i] if k == i + 1 else x[k] for k in range(4))
                        for x in points})
    for i in range(4):
        values = list(range(6 - len(prof[i]), 6))
        deficit = dict(zip(values, prof[i]))
        classes = {}
        for a in values:
            classes.setdefault(deficit[a], []).append(a)
        for members in classes.values():
            for a, b in zip(members, members[1:]):
                out.append({x: tuple((b if x[k] == a else a if x[k] == b else x[k]) if k == i else x[k]
                                     for k in range(4)) for x in points})
    return out


def lex_clauses(points, var, g, nv):
    """r2 schema: comparison clause plus fresh q_k <-> q_{k-1} and (x <-> y)."""
    clauses, previous = [], None
    for p in points:
        x, y = var[p], var[g[p]]
        if x == y:
            continue
        clauses.append([-x, y] if previous is None else [-previous, -x, y])
        nv += 1
        q = nv
        if previous is None:
            clauses += [[-x, -y, q], [x, y, q]]
        else:
            clauses += [[-q, previous], [-previous, -x, -y, q], [-previous, x, y, q]]
        clauses += [[-q, -x, y], [-q, x, -y]]
        previous = q
    return clauses, nv


def main():
    replay = json.loads(REPLAY.read_text())
    reports = {}
    rows = []
    for item in replay["proofs"]:
        t, e, prof = item["t"], item["e"], item["profile"]
        h = 36 - t
        key = f"evidence/large_t_lex_t{t}_e{e}.json"
        report = reports.setdefault(key, json.loads((SNAP / key).read_text()))
        entry = [p for p in report["profiles"] if p["profile"] == prof]
        if len(entry) != 1:
            raise ValueError("profile not unique in report")
        S = base.SmallGen(prof)
        S.build_gen(e, h)
        clauses, nv = list(S.cl), S.nv
        for g in written_generators(prof, S.points):
            extra, nv = lex_clauses(S.points, S.var, g, nv)
            clauses += extra
        clauses += [[-S.var[tuple(map(int, s))] for s in rep["N"]] for rep in entry[0]["reps"]]
        text = "p cnf %d %d\n" % (nv, len(clauses)) + "".join(" ".join(map(str, c)) + " 0\n" for c in clauses)
        digest = hashlib.sha256(text.encode()).hexdigest()
        rows.append({"t": t, "e": e, "profile": prof, "expected": item["cnf_sha256"], "regenerated": digest,
                     "match": digest == item["cnf_sha256"]})
    passed = len(rows) == 37 and all(r["match"] for r in rows)
    result = {"recorded_at_pt": subprocess.check_output(["date", "+%Y-%m-%d %H:%M:%S %Z"], text=True).strip(),
              "driver_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "source": "LOWER48 r2 section 3 schema; large_t_lex.py not imported; base from pinned build_gen",
              "rows": rows, "matches": sum(r["match"] for r in rows), "verdict": "PASS" if passed else "FAIL"}
    out = HERE / "ame46-lower48-lex-from-text-v1.json"
    with out.open("x") as f:
        json.dump(result, f, indent=1)
        f.write("\n")
    print(json.dumps({"verdict": result["verdict"], "matches": result["matches"], "rows": len(rows)}))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
