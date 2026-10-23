#!/usr/bin/env python3
"""[revision 4: uses stream_check4 (native solver limits, drat-trim -t <= 1200 s, bounded
waits, SIGTERM only, interrupted checkers => UNKNOWN; results carry stream_check_revision=3)]
M1 proof pass, cycle-2 version (no new proof files): for every A2 case classified UNSAT by
pass 1 that has no checked proof yet (no cases19skel/proofcheck/<tag>.json), read the stored
pass-1 CNF, check its SHA-256 against pass 1, run kissat 4.0.4 --seed=1 with the binary DRAT
streamed into drat-trim -i, whose LRAT is streamed into lrat-check (stream_check.py).
Results: cycle2/proofstream/<tag>.json (resumable). Usage: run_proofpass_stream.py WORKERS
TIMEOUT_S [TAG_PREFIX ...]
"""
import concurrent.futures as cf
import hashlib
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import stream_check4 as stream_check  # noqa: E402

LANE = os.path.dirname(HERE)
CS = os.path.join(LANE, "cases19skel")
OUT = os.path.join(LANE, "cycle2", "proofstream")


def one(tag, timeout):
    path = os.path.join(OUT, tag + ".json")
    if os.path.exists(path):
        return json.load(open(path))
    p1 = json.load(open(os.path.join(CS, "results", tag + ".json")))
    cnf = open(os.path.join(LANE, p1["cnf"]), "rb").read()
    r = stream_check.kissat_stream(cnf, os.path.join(LANE, "scratch", "fifo", "v4ps_" + tag), timeout)
    r.update({"tag": tag, "cnf_file": p1["cnf"], "cnf_matches_pass1_sha": r["cnf_sha256"] == p1["cnf_sha256"]})
    r["ok"] = r["checked"] and r["cnf_matches_pass1_sha"]
    r["solver_out"] = ""
    os.makedirs(OUT, exist_ok=True)
    json.dump(r, open(path, "w"), indent=1)
    return r


def main():
    workers, timeout = int(sys.argv[1]), float(sys.argv[2])
    prefixes = sys.argv[3:]
    tags = []
    for fn in sorted(os.listdir(os.path.join(CS, "results"))):
        tag = fn[:-5]
        if prefixes and not any(tag.startswith(p) for p in prefixes):
            continue
        if os.path.exists(os.path.join(CS, "proofcheck", tag + ".json")):
            continue
        if json.load(open(os.path.join(CS, "results", fn)))["status"] == "UNSAT":
            tags.append(tag)
    print("to prove:", len(tags), flush=True)
    with cf.ProcessPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(one, t, timeout): t for t in tags}
        for fu in cf.as_completed(futs):
            r = fu.result()
            print(time.strftime("%H:%M:%S"), r["tag"], "ok" if r["ok"] else "NOT-OK", r["solve_seconds"],
                  r["check_seconds"], flush=True)


if __name__ == "__main__":
    main()
