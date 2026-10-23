#!/usr/bin/env python3
"""[run_m2skel8: = run_m2skel6 with stream_check8 (strict drat-trim verdict, solver metadata), same
output directory cycle2/m2skel_drat (records carry stream_check_revision=8), claims m2d8_*;
cooperative stop: create cycle2/STOP-m2skel8 (no new case is claimed). Parent route A.]
[run_m2skel6: = run_m2skel5 with stream_check5 (CaDiCaL binary DRAT -> drat-trim; lrat-check not used),
results in cycle2/m2skel_drat]
[run_m2skel5: M2 encoder version 2 (encode_skel_b.build_v2, row-major lex-leader incl. row lex),
results in cycle2/m2skel_v2; otherwise = run_m2skel4]
[revision 4: uses stream_check4 (native solver limits, drat-trim -t <= 1200 s, bounded
waits, SIGTERM only, interrupted checkers => UNKNOWN; results carry stream_check_revision=3)]
Method M2 over the gen_skel_b skeleton lists: encode_skel_b CNF (in memory, SHA-256
recorded) solved by CaDiCaL 3.0.1 with LRAT streamed into lrat-check (stream_check).
Results: cycle2/m2skel/msXX_bNNNNN.json (resumable). A SAT answer stops the run.
Usage: run_m2skel.py WORKERS TIMEOUT_S MS_INDEX[:i0-i1] [...]
"""
import concurrent.futures as cf
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_skel_b  # noqa: E402
import stream_check8 as stream_check  # noqa: E402

LANE = os.path.dirname(HERE)
OUT = os.path.join(LANE, "cycle2", "m2skel_drat")
STOP = os.path.join(LANE, "cycle2", "STOP-m2skel8")
SK = os.path.join(LANE, "cycle2", "skel-b")


def one(mi, i, timeout):
    path = os.path.join(OUT, "ms%02d_b%05d.json" % (mi, i))
    if os.path.exists(path):
        return json.load(open(path))
    if os.path.exists(STOP):
        return {"multiset": mi, "b_index": i, "status": "STOPPED", "checked": None, "solve_seconds": 0}
    cdir = os.path.join(LANE, "cycle2", "claims")
    os.makedirs(cdir, exist_ok=True)
    try:
        fd = os.open(os.path.join(cdir, "m2d8_ms%02d_b%05d.claim" % (mi, i)), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.close(fd)
    except FileExistsError:
        return {"multiset": mi, "b_index": i, "status": "CLAIMED-ELSEWHERE", "checked": None, "solve_seconds": 0}
    d = json.load(open(os.path.join(SK, "skeletons-b-ms%02d.json" % mi)))
    sk = d["skeletons"][i]
    special = [p for p in d["profiles"] if list(p) != [4, 3, 3, 3, 3, 3]]
    nv, cl = encode_skel_b.build_v2(d["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special)
    b = encode_skel_b.cnf_bytes(nv, cl)
    r = stream_check.cadical_drat(b, os.path.join(LANE, "scratch", "fifo", "v8m2_%02d_%05d" % (mi, i)), timeout)
    r.update({"multiset": mi, "b_index": i, "encoder": "encode_skel_b.build_v2", "generator": "gen_skel_b.py"})
    if r["status"] == "SAT":
        os.makedirs(os.path.join(LANE, "cycle2", "witness"), exist_ok=True)
        open(os.path.join(LANE, "cycle2", "witness", "m2_ms%02d_b%05d.solver.txt" % (mi, i)), "w").write(r["solver_out"])
    r["solver_out"] = ""
    os.makedirs(OUT, exist_ok=True)
    json.dump(r, open(path, "w"), indent=1)
    return r


def main():
    workers, timeout = int(sys.argv[1]), float(sys.argv[2])
    jobs = []
    for arg in sys.argv[3:]:
        if ":" in arg:
            mi, rng = arg.split(":")
            a, b = rng.split("-")
            idx = range(int(a), int(b) + 1)
        else:
            mi = arg
            d = json.load(open(os.path.join(SK, "skeletons-b-ms%02d.json" % int(mi))))
            idx = range(d["num_skeletons"])
        jobs += [(int(mi), i) for i in idx]
    print("jobs", len(jobs), flush=True)
    with cf.ProcessPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(one, mi, i, timeout): (mi, i) for mi, i in jobs}
        for fu in cf.as_completed(futs):
            r = fu.result()
            print(time.strftime("%H:%M:%S"), r["multiset"], r["b_index"], r["status"], r["checked"],
                  r["solve_seconds"], flush=True)
            if r["status"] == "SAT":
                print("SAT FOUND -- stopping", flush=True)
                os._exit(3)


if __name__ == "__main__":
    main()
