#!/usr/bin/env python3
"""Cross-check of the strict LRAT pipeline (stream_check6.cadical_lrat_strict) against the
drat-trim pipeline on the same CNFs, plus timing. Writes cycle2/lratstrict-crosscheck.json.
  * E0 graph g000 (encode_q0b CNF, the slowest E0 M2' case; DRAT result m2q0c/results/g000.json)
  * M2 build_v2 ms01 b00000..b00049 (DRAT results in cycle2/m2skel_drat)
  * M2 build_v2 ms07 b00000..b00004 and ms08 b00000..b00004 (timing only)
Usage: crosscheck_lratstrict.py
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_skel_b  # noqa: E402
import stream_check6 as S  # noqa: E402

LANE = os.path.dirname(HERE)
FD = os.path.join(LANE, "scratch", "fifo", "xls")


def m2cnf(mi, i):
    d = json.load(open(os.path.join(LANE, "cycle2", "skel-b", "skeletons-b-ms%02d.json" % mi)))
    sk = d["skeletons"][i]
    special = [p for p in d["profiles"] if list(p) != [4, 3, 3, 3, 3, 3]]
    nv, cl = encode_skel_b.build_v2(d["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special)
    return encode_skel_b.cnf_bytes(nv, cl)


def keep(r):
    return {k: r.get(k) for k in ("status", "checked", "solve_seconds", "check_seconds", "lrat_bytes", "cnf_sha256",
                                   "lratstrict", "events")}


def main():
    out = {}
    gs = [l.strip() for l in open(os.path.join(LANE, "data", "quadgraphs-8v-13to16e-D4.g6")) if l.strip()]
    enc = subprocess.run([sys.executable, os.path.join(HERE, "encode_q0b.py"), gs[0], "/dev/stdout"], capture_output=True)
    lines = enc.stdout.split(b"\n")
    while lines and not lines[-1].strip():
        lines.pop()
    lines.pop()
    cnf = b"\n".join(lines) + b"\n"
    r = keep(S.cadical_lrat_strict(cnf, FD + "_g000", 1800))
    dr = json.load(open(os.path.join(LANE, "m2q0c", "results", "g000.json")))
    r["drat_pipeline"] = {k: dr.get(k) for k in ("status", "checked", "solve_seconds", "check_seconds", "cnf_sha256")}
    r["same_cnf"] = r["cnf_sha256"] == dr["cnf_sha256"]
    out["E0_g000"] = r
    agree = []
    for i in range(50):
        r = keep(S.cadical_lrat_strict(m2cnf(1, i), FD + "_m2", 600))
        dr = json.load(open(os.path.join(LANE, "cycle2", "m2skel_drat", "ms01_b%05d.json" % i)))
        agree.append({"b": i, "strict": (r["status"], r["checked"], r["solve_seconds"], r["check_seconds"]),
                      "drat": (dr["status"], dr["checked"], dr["solve_seconds"], dr.get("check_seconds")),
                      "same_cnf": r["cnf_sha256"] == dr["cnf_sha256"]})
    out["M2_ms01_b0_49"] = agree
    out["M2_ms01_all_agree"] = all(a["strict"][0] == a["drat"][0] == "UNSAT" and a["strict"][1] and a["drat"][1]
                                   and a["same_cnf"] for a in agree)
    for mi in (7, 8):
        out["M2_ms%02d_timing" % mi] = [dict(keep(S.cadical_lrat_strict(m2cnf(mi, i), FD + "_t", 600)), b=i) for i in range(5)]
    json.dump(out, open(os.path.join(LANE, "cycle2", "lratstrict-crosscheck.json"), "w"), indent=1)
    print(json.dumps({"E0_g000": {k: out["E0_g000"][k] for k in ("status", "checked", "solve_seconds", "check_seconds", "lrat_bytes", "same_cnf")},
                      "E0_g000_drat": out["E0_g000"]["drat_pipeline"],
                      "M2_ms01_all_agree": out["M2_ms01_all_agree"],
                      "ms07": [(x["status"], x["checked"], x["solve_seconds"], x["check_seconds"]) for x in out["M2_ms07_timing"]],
                      "ms08": [(x["status"], x["checked"], x["solve_seconds"], x["check_seconds"]) for x in out["M2_ms08_timing"]]}, indent=1))


if __name__ == "__main__":
    main()
