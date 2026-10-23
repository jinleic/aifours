#!/usr/bin/env python3
"""Smoke tests for stream_check3 (native limits, cooperative stops, checker gating).
Writes cycle2/smoke-stream3.json. Cases:
  A  UNSAT (cases19skel ms04_s00000): kissat_stream and cadical_stream must be checked;
  B  SAT ((13,5,4) control ms04_s00000): status SAT, checkers end by EOF without signals;
  C  native solver limit (ms09_s00004, limit 3 s): UNKNOWN, no signals;
  D  drat-trim native check budget too small (ms01_s00010, check_budget 1): drat-trim must
     stop on its own via -t, the case must be UNKNOWN (not checked);
  E  stop_cooperatively on `sleep 300` with bound 2 s: SIGTERM, exits ('term');
  F  stop_cooperatively on a shell that ignores SIGTERM (sleeps 90 s): left running
     ('running'), pid recorded; it exits by itself after 90 s (no SIGKILL is ever sent).
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_skel  # noqa: E402
import stream_check3 as S  # noqa: E402

LANE = os.path.dirname(HERE)


def cnf_of(rel):
    spec = json.load(open(os.path.join(LANE, rel)))
    F, X, _ = encode_skel.build(spec)
    return S.cnf_bytes_of(F)


def brief(r):
    keys = ("status", "checked", "solver_stop", "solve_seconds", "check_seconds", "checker_interrupted",
            "drat_trim", "lrat_check", "events", "drat_trim_verified", "lrat_verified")
    return {k: r.get(k) for k in keys if k in r}


def main():
    out = {}
    fd = os.path.join(LANE, "scratch", "fifo", "smoke3_%d" % int(time.time()))
    b = cnf_of("cases19skel/specs/ms04_s00000.json")
    out["A_kissat"] = brief(S.kissat_stream(b, fd + "_Ak", 60))
    out["A_cadical"] = brief(S.cadical_stream(b, fd + "_Ac", 60))
    b = cnf_of("controls/c13skel/specs/ms04_s00000.json")
    out["B_kissat"] = brief(S.kissat_stream(b, fd + "_Bk", 60))
    out["B_cadical"] = brief(S.cadical_stream(b, fd + "_Bc", 60))
    b = cnf_of("cases19skel/specs/ms09_s00004.json")
    out["C_kissat"] = brief(S.kissat_stream(b, fd + "_Ck", 3))
    out["C_cadical"] = brief(S.cadical_stream(b, fd + "_Cc", 3))
    b = cnf_of("cases19skel/specs/ms01_s00010.json")
    out["D_kissat_budget1"] = brief(S.kissat_stream(b, fd + "_Dk", 60, check_budget=1))
    ev = []
    p = subprocess.Popen(["sleep", "300"])
    out["E_sleep"] = {"result": S.stop_cooperatively(p, 2, ev, "sleep"), "events": ev}
    ev = []
    p = subprocess.Popen(["sh", "-c", "trap '' TERM; sleep 90"])
    t0 = time.time()
    out["F_ignores_term"] = {"result": S.stop_cooperatively(p, 2, ev, "sh-trap"), "events": ev,
                             "waited_s": round(time.time() - t0, 1), "pid_left_running": p.pid}
    ok = (out["A_kissat"]["checked"] and out["A_cadical"]["checked"]
          and out["B_kissat"]["status"] == "SAT" and out["B_cadical"]["status"] == "SAT"
          and not out["B_kissat"]["events"] and not out["B_cadical"]["events"]
          and out["C_kissat"]["status"] == "UNKNOWN" and out["C_cadical"]["status"] == "UNKNOWN"
          and not out["C_kissat"]["checked"] and not out["C_cadical"]["checked"]
          and not out["D_kissat_budget1"]["checked"]
          and out["E_sleep"]["result"] == "term" and out["F_ignores_term"]["result"] == "running")
    out["all_expected"] = bool(ok)
    json.dump(out, open(os.path.join(LANE, "cycle2", "smoke-stream3.json"), "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
