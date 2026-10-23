#!/usr/bin/env python3
"""[run_m2partbatch2: stream_check5 (CaDiCaL binary DRAT -> drat-trim), results cycle2/m2part_drat]
M2 batched partial-split runner (independent of the M1 code): placements from extend_b.py,
batch CNFs from encode_skel_b.build_partbatch, CaDiCaL (-t LIMIT) with LRAT streamed into
lrat-check (stream_check4). Results: cycle2/m2part/msXX_bNNNNN/{ext.json,batch_*.json,
summary_batched.json}; claims cycle2/claims/m2pb_msXX_bNNNNN.claim. A SAT batch stops the run
(its solver output is written to cycle2/witness/).
Usage: run_m2partbatch.py LIMIT_S CHECK_BUDGET_S BATCH MS:B [MS:B ...]
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_skel_b  # noqa: E402
import stream_check5 as S  # noqa: E402

LANE = os.path.dirname(HERE)
OUT = os.path.join(LANE, "cycle2", "m2part_drat")


def claim(name):
    d = os.path.join(LANE, "cycle2", "claims")
    os.makedirs(d, exist_ok=True)
    try:
        fd = os.open(os.path.join(d, name + ".claim"), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    os.write(fd, ("%d %s\n" % (os.getpid(), time.strftime("%Y-%m-%dT%H:%M:%S%z"))).encode())
    os.close(fd)
    return True


def run(mi, bi, limit, budget, bsize):
    name = "ms%02d_b%05d" % (mi, bi)
    d = os.path.join(OUT, name)
    if os.path.exists(os.path.join(d, "summary_batched.json")):
        return None
    os.makedirs(d, exist_ok=True)
    skp = os.path.join(LANE, "cycle2", "skel-b", "skeletons-b-ms%02d.json" % mi)
    ext = os.path.join(d, "ext.json")
    if not os.path.exists(ext):
        subprocess.run([sys.executable, os.path.join(HERE, "extend_b.py"), skp, str(bi), ext], check=True,
                       capture_output=True)
    E = json.load(open(ext))
    D = json.load(open(skp))
    sk = D["skeletons"][bi]
    special = [p for p in D["profiles"] if list(p) != [4, 3, 3, 3, 3, 3]]
    n = E["num_placements"]
    st = {"batches": 0, "UNSAT_checked": 0, "other": 0, "SAT": 0}
    for j in range(0, n, bsize):
        idx = list(range(j, min(n, j + bsize)))
        bp = os.path.join(d, "batch_%05d_%05d.json" % (idx[0], idx[-1]))
        if os.path.exists(bp):
            r = json.load(open(bp))
        else:
            nv, cl = encode_skel_b.build_partbatch(D["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special,
                                                   [E["placements"][i] for i in idx])
            r = S.cadical_drat(encode_skel_b.cnf_bytes(nv, cl),
                                 os.path.join(LANE, "scratch", "fifo", "m2pbd_%s_%05d" % (name, idx[0])), limit, budget)
            r.update({"multiset": mi, "b_index": bi, "indices": [idx[0], idx[-1]],
                      "encoder": "encode_skel_b.build_partbatch", "enumerator": "extend_b.py"})
            if r["status"] == "SAT":
                os.makedirs(os.path.join(LANE, "cycle2", "witness"), exist_ok=True)
                open(os.path.join(LANE, "cycle2", "witness", "m2pb_%s_%05d.solver.txt" % (name, idx[0])), "w").write(
                    r["solver_out"])
            r["solver_out"] = ""
            json.dump(r, open(bp, "w"), indent=1)
        st["batches"] += 1
        if r["status"] == "UNSAT" and r["checked"]:
            st["UNSAT_checked"] += len(idx)
        elif r["status"] == "SAT":
            st["SAT"] += 1
            break
        else:
            st["other"] += len(idx)
    res = {"multiset": mi, "b_index": bi, "num_sub": n, **st}
    res["decided_unsat"] = st["UNSAT_checked"] == n and st["SAT"] == 0
    json.dump(res, open(os.path.join(d, "summary_batched.json"), "w"), indent=1)
    return res


def main():
    limit, budget, bsize = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])
    for arg in sys.argv[4:]:
        mi, bi = (int(x) for x in arg.split(":"))
        if not claim("m2pbd_ms%02d_b%05d" % (mi, bi)):
            continue
        r = run(mi, bi, limit, budget, bsize)
        if r is None:
            continue
        print(time.strftime("%H:%M:%S"), json.dumps(r), flush=True)
        if r["SAT"]:
            print("SAT FOUND -- stopping this runner", flush=True)
            return


if __name__ == "__main__":
    main()
