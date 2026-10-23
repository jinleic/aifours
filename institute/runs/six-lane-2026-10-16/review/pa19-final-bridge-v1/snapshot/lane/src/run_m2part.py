#!/usr/bin/env python3
"""M2 partial split runner (independent of the M1 A3/A3' code): for a gen_skel_b skeleton of
an all-P1 multiset, enumerate one-column placements with extend_b.py, encode each subcase with
encode_skel_b.build_part and solve with CaDiCaL (-t LIMIT) + LRAT streamed into lrat-check
(stream_check4: native limits, SIGTERM only, interrupted checkers => UNKNOWN). Claims per
skeleton (cycle2/claims/m2_msXX_bNNNNN.claim) allow several runner processes.
Results: cycle2/m2part/msXX_bNNNNN/{ext.json,fNNNNN.json,summary.json}.
Usage: run_m2part.py LIMIT_S CHECK_BUDGET_S MS:B [MS:B ...]
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_skel_b  # noqa: E402
import stream_check4 as S  # noqa: E402

LANE = os.path.dirname(HERE)
OUT = os.path.join(LANE, "cycle2", "m2part")


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


def run(mi, bi, limit, budget):
    name = "ms%02d_b%05d" % (mi, bi)
    d = os.path.join(OUT, name)
    summ = os.path.join(d, "summary.json")
    if os.path.exists(summ):
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
    st = {"UNSAT_checked": 0, "UNSAT_unchecked": 0, "SAT": 0, "UNKNOWN": 0}
    for i, pl in enumerate(E["placements"]):
        rp = os.path.join(d, "f%05d.json" % i)
        if os.path.exists(rp):
            r = json.load(open(rp))
        else:
            nv, cl = encode_skel_b.build_part(D["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special, [pl])
            r = S.cadical_stream(encode_skel_b.cnf_bytes(nv, cl),
                                 os.path.join(LANE, "scratch", "fifo", "m2p_%s_%05d" % (name, i)), limit, budget)
            r.update({"multiset": mi, "b_index": bi, "sub_index": i, "encoder": "encode_skel_b.build_part",
                      "enumerator": "extend_b.py"})
            if r["status"] == "SAT":
                os.makedirs(os.path.join(LANE, "cycle2", "witness"), exist_ok=True)
                open(os.path.join(LANE, "cycle2", "witness", "m2part_%s_f%05d.solver.txt" % (name, i)), "w").write(
                    r["solver_out"])
            r["solver_out"] = ""
            json.dump(r, open(rp, "w"), indent=1)
        if r["status"] == "UNSAT":
            st["UNSAT_checked" if r["checked"] else "UNSAT_unchecked"] += 1
        else:
            st[r["status"]] += 1
        if r["status"] == "SAT":
            break
    res = {"multiset": mi, "b_index": bi, "num_sub": E["num_placements"], **st}
    res["decided_unsat"] = st["UNSAT_checked"] == E["num_placements"]
    json.dump(res, open(summ, "w"), indent=1)
    return res


def main():
    limit, budget = float(sys.argv[1]), float(sys.argv[2])
    for arg in sys.argv[3:]:
        mi, bi = (int(x) for x in arg.split(":"))
        if not claim("m2_ms%02d_b%05d" % (mi, bi)):
            continue
        r = run(mi, bi, limit, budget)
        if r is None:
            continue
        print(time.strftime("%H:%M:%S"), json.dumps(r), flush=True)
        if r["SAT"]:
            print("SAT FOUND -- stopping this runner", flush=True)
            return


if __name__ == "__main__":
    main()
