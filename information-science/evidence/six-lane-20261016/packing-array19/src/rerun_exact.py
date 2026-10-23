#!/usr/bin/env python3
"""Run A3 full-skeleton subcases with encode_full2 (exact leave counts, Amendment A3-exact),
kissat_stream (stream_check4). Results: cycle2/a3/<tag>/fNNNNN_exact.json (never overwritten).
Usage: rerun_exact.py TAG LIMIT_S CHECK_BUDGET_S INDEX [INDEX ...]
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_full2  # noqa: E402
import stream_check4 as S  # noqa: E402

LANE = os.path.dirname(HERE)


def main():
    tag, limit, budget = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
    base = os.path.join(LANE, "cycle2", "a3", tag)
    spec = json.load(open(os.path.join(LANE, "cases19skel", "specs", tag + ".json")))
    E = json.load(open(os.path.join(base, "ext.json")))
    for a in sys.argv[4:]:
        i = int(a)
        out = os.path.join(base, "f%05d_exact.json" % i)
        if os.path.exists(out):
            continue
        sub = dict(spec)
        sub["placed"] = E["full"][i]
        F, X, info = encode_full2.build(sub)
        r = S.kissat_stream(S.cnf_bytes_of(F), os.path.join(LANE, "scratch", "fifo", "ex_%s_%05d" % (tag, i)), limit, budget)
        r.update({"tag": tag, "full_index": i, "encoder": "encode_full2.py", "leave": info["leave"],
                  "runner": "rerun_exact.py"})
        if r["status"] == "SAT":
            os.makedirs(os.path.join(LANE, "cycle2", "witness"), exist_ok=True)
            open(os.path.join(LANE, "cycle2", "witness", "exact_%s_%05d.solver.txt" % (tag, i)), "w").write(r["solver_out"])
        r["solver_out"] = ""
        json.dump(r, open(out, "w"), indent=1)
        print(json.dumps({k: r.get(k) for k in ("tag", "full_index", "status", "checked", "solve_seconds",
                                                "check_seconds", "leave")}))


if __name__ == "__main__":
    main()
