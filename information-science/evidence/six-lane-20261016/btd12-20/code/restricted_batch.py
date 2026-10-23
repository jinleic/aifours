#!/usr/bin/env python3
"""restricted_batch.py -- RESTRICTED batch search for BTD(12,20;4,3,10;6,4): for every given 1-pattern A, CP-SAT
decides the 2-pattern D exactly as in code/restricted_afix.py (same model; README 1.3, 1.4).  Information only:
INFEASIBLE / UNKNOWN for an A-pattern is not an exclusion of the target unless a separate written argument proves
that the list of A-patterns is complete AND each infeasibility is certified independently.

Input formats (one structure per line):
  --mg FILE    nauty `multig -T` lines (nv ne {v1 v2 mult}); vertex v -> columns 2v, 2v+1; edge uv -> tetrad
               {2u, 2u+1, 2v, 2v+1} repeated mult times (d-type A-pattern; columns >= 2 nv are free).
  --rows FILE  JSON lines {"name": ..., "rows": [[4 columns] x 12]}.
Usage: restricted_batch.py (--mg FILE | --rows FILE) OUT.jsonl --time S
Writes OUT.jsonl (exclusive): one record per structure; witnesses also as OUT.jsonl.witness-N.btd (exclusive).
"""
import hashlib
import json
import sys
import time

from ortools.sat.python import cp_model

V, B, P1, P2, R, K, L = 12, 20, 4, 3, 10, 6, 4


def solve(rows, tlim):
    A = [[1 if j in r else 0 for j in range(B)] for r in rows]
    a = [sum(A[i][j] for i in range(V)) for j in range(B)]
    if not all(0 <= K - aj and (K - aj) % 2 == 0 for aj in a):
        return "INFEASIBLE_PRECHECK", None, 0.0
    m = cp_model.CpModel()
    d = [[m.NewBoolVar(f"d{i}_{j}") if not A[i][j] else None for j in range(B)] for i in range(V)]
    for i in range(V):
        m.Add(sum(d[i][j] for j in range(B) if d[i][j] is not None) == P2)
    for j in range(B):
        m.Add(a[j] + 2 * sum(d[i][j] for i in range(V) if d[i][j] is not None) == K)
    for i in range(V):
        for k in range(i + 1, V):
            x = sum(A[i][j] * A[k][j] for j in range(B))
            terms = []
            for j in range(B):
                if A[i][j] and d[k][j] is not None:
                    terms.append(2 * d[k][j])
                if A[k][j] and d[i][j] is not None:
                    terms.append(2 * d[i][j])
                if d[i][j] is not None and d[k][j] is not None:
                    p = m.NewBoolVar(f"p{i}_{k}_{j}")
                    m.AddBoolAnd([d[i][j], d[k][j]]).OnlyEnforceIf(p)
                    m.AddBoolOr([d[i][j].Not(), d[k][j].Not()]).OnlyEnforceIf(p.Not())
                    terms.append(4 * p)
            m.Add(x + sum(terms) == L)
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = tlim
    s.parameters.num_workers = 1
    t0 = time.time()
    st = s.Solve(m)
    el = time.time() - t0
    Mx = None
    if st in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        Mx = [[A[i][j] + (2 * s.Value(d[i][j]) if d[i][j] is not None else 0) for j in range(B)] for i in range(V)]
    return s.StatusName(st), Mx, el


def mg_rows(line):
    t = line.split()
    nv, ne = int(t[0]), int(t[1])
    rows = []
    for q in range(ne):
        u, v, mu = int(t[2 + 3 * q]), int(t[3 + 3 * q]), int(t[4 + 3 * q])
        rows += [[2 * u, 2 * u + 1, 2 * v, 2 * v + 1]] * mu
    if 2 * nv > B or len(rows) != V:
        raise SystemExit(f"bad multigraph line {line!r}")
    return rows


def main(argv):
    if len(argv) != 6 or argv[1] not in ("--mg", "--rows") or argv[4] != "--time":
        print(__doc__, file=sys.stderr)
        return 2
    mode, inp, out, tlim = argv[1], argv[2], argv[3], float(argv[5])
    data = open(inp, "rb").read()
    lines = [ln for ln in data.decode().splitlines() if ln.strip()]
    meta = {"program": "restricted_batch.py", "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
            "input": inp, "input_sha256": hashlib.sha256(data).hexdigest(), "mode": mode, "time_limit_s": tlim,
            "workers": 1, "restricted": True, "n_structures": len(lines)}
    counts = {}
    nwit = 0
    with open(out, "x") as f:
        f.write(json.dumps(meta) + "\n")
        for idx, ln in enumerate(lines):
            if mode == "--mg":
                rows, name = mg_rows(ln), f"mg#{idx}"
            else:
                obj = json.loads(ln)
                rows, name = [sorted(r) for r in obj["rows"]], obj.get("name", f"rows#{idx}")
            st, Mx, el = solve([set(r) for r in rows], tlim)
            counts[st] = counts.get(st, 0) + 1
            rec = {"idx": idx, "name": name, "status": st, "wall_s": round(el, 4)}
            if Mx is not None:
                txt = f"BTD {V} {B} {P1} {P2} {R} {K} {L}\n" + "".join(" ".join(map(str, r)) + "\n" for r in Mx)
                wpath = f"{out}.witness-{nwit}.btd"
                with open(wpath, "x", newline="") as g:
                    g.write(txt)
                rec["witness"] = wpath
                rec["witness_sha256"] = hashlib.sha256(txt.encode()).hexdigest()
                nwit += 1
            f.write(json.dumps(rec) + "\n")
            f.flush()
        f.write(json.dumps({"summary": counts, "witnesses": nwit}) + "\n")
    print(json.dumps({"input": inp, "summary": counts, "witnesses": nwit}))
    return 10 if nwit else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
