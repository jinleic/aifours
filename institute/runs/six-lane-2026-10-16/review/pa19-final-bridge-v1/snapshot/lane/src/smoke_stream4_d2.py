#!/usr/bin/env python3
"""Smoke test D2 for stream_check4: post-solve checker budget exhaustion on a real proof.
Case cases19skel ms06_s00028 (kissat about 64 s) with solver limit 300 s and check_budget
30 s: drat-trim gets -t 330 (its clock includes the solve) and a post-solve wall bound of
30 + 60 s; if its check needs longer it is sent SIGTERM (never SIGKILL) and the case must be
UNKNOWN (checked = False). If the check finishes inside the bound the test is reported as
inconclusive rather than passed. Writes cycle2/smoke-stream4-D2.json.
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import stream_check4 as S  # noqa: E402

LANE = os.path.dirname(HERE)


def main():
    p1 = json.load(open(os.path.join(LANE, "cases19skel", "results", "ms06_s00028.json")))
    cnf = open(os.path.join(LANE, p1["cnf"]), "rb").read()
    r = S.kissat_stream(cnf, os.path.join(LANE, "scratch", "fifo", "smoke4d2_%d" % int(time.time())), 300,
                        check_budget=30)
    keep = {k: r.get(k) for k in ("status", "checked", "solver_stop", "solve_seconds", "check_seconds",
                                   "checker_interrupted", "drat_trim", "lrat_check", "events", "drat_bytes",
                                   "lrat_bytes", "cnf_sha256", "solver")}
    keep["cnf_matches_pass1"] = r["cnf_sha256"] == p1["cnf_sha256"]
    if r["checked"]:
        keep["verdict"] = "inconclusive (check finished inside the budget)"
    else:
        keep["verdict"] = "pass" if (r["status"] == "UNSAT" and r["checker_interrupted"]) else "other"
    json.dump(keep, open(os.path.join(LANE, "cycle2", "smoke-stream4-D2.json"), "w"), indent=1)
    print(json.dumps(keep, indent=1))


if __name__ == "__main__":
    main()
