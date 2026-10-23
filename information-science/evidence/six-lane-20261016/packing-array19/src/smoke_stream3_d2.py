#!/usr/bin/env python3
"""Smoke test D2 for stream_check3: checker budget exhaustion handled by drat-trim's native
-t. Case cases19skel ms01_s00890 (cycle-1 DRAT 78.7 MB, check 49 s) with check_budget=5:
drat-trim must stop on its own (native timeout), the case must be UNKNOWN (not checked),
and no signal may be needed. Writes cycle2/smoke-stream3-D2.json.
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import stream_check3 as S  # noqa: E402

LANE = os.path.dirname(HERE)


def main():
    p1 = json.load(open(os.path.join(LANE, "cases19skel", "results", "ms01_s00890.json")))
    cnf = open(os.path.join(LANE, p1["cnf"]), "rb").read()
    r = S.kissat_stream(cnf, os.path.join(LANE, "scratch", "fifo", "smoke3d2_%d" % int(time.time())), 120,
                        check_budget=5)
    keep = {k: r.get(k) for k in ("status", "checked", "solver_stop", "solve_seconds", "check_seconds",
                                   "checker_interrupted", "drat_trim", "lrat_check", "events", "drat_bytes",
                                   "lrat_bytes", "cnf_sha256")}
    keep["cnf_matches_pass1"] = r["cnf_sha256"] == p1["cnf_sha256"]
    keep["expected"] = (r["status"] == "UNSAT" and not r["checked"] and r["drat_trim"]["stop"] == "self"
                        and r["drat_trim"]["rc"] != 0 and not r["events"])
    json.dump(keep, open(os.path.join(LANE, "cycle2", "smoke-stream3-D2.json"), "w"), indent=1)
    print(json.dumps(keep, indent=1))


if __name__ == "__main__":
    main()
