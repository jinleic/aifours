#!/usr/bin/env python3
"""smoke_stream8 = smoke_stream5 for stream_check8 (strict verdict lines). Writes cycle2/smoke-stream8.json.
Original: Smoke tests for stream_check5 (drat-trim-only acceptance). Writes cycle2/smoke-stream5.json.
  A UNSAT (cases19skel ms04_s00000): kissat_drat and cadical_drat must be checked;
  B SAT ((13,5,4) control ms04_s00000): status SAT, not checked, no signals;
  C native solver limit 3 s (ms09_s00004): UNKNOWN, not checked, no signals;
  D the two subcases whose kissat proofs made drat-trim stall (stream length a multiple of
    64 KiB): ms01_s03171 full skeleton 1788 and ms09_s00010 batch 4300-4399, with cadical_drat
    (different proof) -> expected checked.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_full  # noqa: E402
import encode_partbatch  # noqa: E402
import encode_skel  # noqa: E402
import stream_check8 as S  # noqa: E402

LANE = os.path.dirname(HERE)
FD = os.path.join(LANE, "scratch", "fifo", "smoke8")


def keep(r):
    return {k: r.get(k) for k in ("status", "checked", "solver_stop", "solve_seconds", "check_seconds",
                                   "drat_trim", "events", "drat_bytes", "cnf_sha256", "solver", "solver_info")}


def skel_cnf(rel):
    F, _, _ = encode_skel.build(json.load(open(os.path.join(LANE, rel))))
    return S.cnf_bytes_of(F)


def main():
    out = {}
    b = skel_cnf("cases19skel/specs/ms04_s00000.json")
    out["A_kissat"] = keep(S.kissat_drat(b, FD + "_Ak", 60))
    out["A_cadical"] = keep(S.cadical_drat(b, FD + "_Ac", 60))
    b = skel_cnf("controls/c13skel/specs/ms04_s00000.json")
    out["B_kissat"] = keep(S.kissat_drat(b, FD + "_Bk", 60))
    out["B_cadical"] = keep(S.cadical_drat(b, FD + "_Bc", 60))
    b = skel_cnf("cases19skel/specs/ms09_s00004.json")
    out["C_kissat"] = keep(S.kissat_drat(b, FD + "_Ck", 3))
    out["C_cadical"] = keep(S.cadical_drat(b, FD + "_Cc", 3))
    spec = json.load(open(os.path.join(LANE, "cases19skel", "specs", "ms01_s03171.json")))
    E = json.load(open(os.path.join(LANE, "cycle2", "a3", "ms01_s03171", "ext.json")))
    sub = dict(spec)
    sub["placed"] = E["full"][1788]
    out["D1_cadical_ms01_s03171_f01788"] = keep(S.cadical_drat(S.cnf_bytes_of(encode_full.build(sub)[0]), FD + "_D1", 600))
    spec = json.load(open(os.path.join(LANE, "cases19skel", "specs", "ms09_s00010.json")))
    E = json.load(open(os.path.join(LANE, "cycle2", "part", "ms09_s00010", "ext.json")))
    orig = json.load(open(os.path.join(LANE, "cycle2", "part", "ms09_s00010", "batch_04300_04399.json")))
    F = encode_partbatch.build(spec, [E["full"][i] for i in orig["indices"]])[0]
    out["D2_cadical_ms09_s00010_batch_04300_04399"] = keep(S.cadical_drat(S.cnf_bytes_of(F), FD + "_D2", 600))
    ok = (out["A_kissat"]["checked"] and out["A_cadical"]["checked"]
          and out["B_kissat"]["status"] == "SAT" and out["B_cadical"]["status"] == "SAT"
          and not out["B_kissat"]["checked"] and not out["B_cadical"]["checked"]
          and not out["B_kissat"]["events"] and not out["B_cadical"]["events"]
          and out["C_kissat"]["status"] == "UNKNOWN" and out["C_cadical"]["status"] == "UNKNOWN"
          and not out["C_kissat"]["events"] and not out["C_cadical"]["events"])
    out["ABC_expected"] = bool(ok)
    json.dump(out, open(os.path.join(LANE, "cycle2", "smoke-stream8.json"), "w"), indent=1)
    print(json.dumps({k: (v.get("status"), v.get("checked"), v.get("solve_seconds"), v.get("check_seconds"),
                          (v.get("drat_trim") or {}).get("rc")) if isinstance(v, dict) else v for k, v in out.items()}, indent=1))


if __name__ == "__main__":
    main()
