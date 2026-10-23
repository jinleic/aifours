#!/usr/bin/env python3
"""[run_m2_11.py = run_m2_10.py on stream_check11 (revision 11): SIGTERM handler installed; stop file cycle2/STOP-m2r11 and the
free-disk floor are re-checked after every token acquisition and before every construction/helper/solver/checker
admission (stream_check11.admitted_reason); a refused admission writes no record for the unrun case/batch,
releases the claim (archive/claims-released + archive/MANIFEST.tsv) and ends the runner; helpers run through
stream_check11.run_helper under a token; the token is never released while an owned child is alive.]
M2 runner revision 10, staged token-gated pipeline (stream_check10.cadical_staged: CaDiCaL 3.0.1
binary DRAT buffered zstd-1 in memory, then drat-trim -i; one lane CPU token per pipeline covers CNF
construction, solve and check). Independent of the M1 code: gen_skel_b skeleton lists
(cycle2/skel-b), encode_skel_b.build_v2 / build_partbatch, extend_b.py placements.
  direct MS:I0-I1 | MS:I ...  -> cycle2/m2skel_drat/msXX_bNNNNN.json (claims m2d9_*, shared with
                                 run_m2skel9.py; existing records are skipped)
  split  MS:B ...             -> cycle2/m2part_drat/msXX_bNNNNN/{ext.json,batch_*.json,summary_batched.json}
                                 (claims m2pbd9_*, shared with run_m2partbatch5.py)
A SAT answer writes the solver output to cycle2/witness/ and stops the runner. Stop file
cycle2/STOP-m2r10 (checked before every case/batch; released claims are moved to
archive/claims-released/ with a line in archive/MANIFEST.tsv); parent disk floor checked likewise.
Usage: run_m2_10.py MODE LIMIT_S CHECK_BUDGET_S BATCH ARG [ARG ...]
"""
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_skel_b  # noqa: E402
import stream_check11 as S  # noqa: E402

LANE = os.path.dirname(HERE)
C2 = os.path.join(LANE, "cycle2")
SK = os.path.join(C2, "skel-b")
STOP = os.path.join(C2, "STOP-m2r11")
P0 = [4, 3, 3, 3, 3, 3]
_cache = {}


def skel(mi):
    if mi not in _cache:
        _cache[mi] = json.load(open(os.path.join(SK, "skeletons-b-ms%02d.json" % mi)))
    return _cache[mi]


def claim(name):
    d = os.path.join(C2, "claims")
    os.makedirs(d, exist_ok=True)
    try:
        fd = os.open(os.path.join(d, name + ".claim"), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    os.write(fd, ("%d %s run_m2_11\n" % (os.getpid(), time.strftime("%Y-%m-%dT%H:%M:%S%z"))).encode())
    os.close(fd)
    return True


def release(name, why):
    src = os.path.join(C2, "claims", name + ".claim")
    rel = os.path.join(LANE, "archive", "claims-released")
    os.makedirs(rel, exist_ok=True)
    dst = os.path.join(rel, name + ".%s.claim" % time.strftime("%Y%m%dT%H%M%S"))
    if os.path.exists(dst):
        raise SystemExit("archive destination exists: " + dst)
    os.rename(src, dst)
    h = hashlib.sha256(open(dst, "rb").read()).hexdigest()
    with open(os.path.join(LANE, "archive", "MANIFEST.tsv"), "a") as f:
        f.write("%s\t%s\t%s\t%s\t%s\n" % (time.strftime("%Y-%m-%dT%H:%M:%S%z"), os.path.relpath(src, LANE),
                                          os.path.relpath(dst, LANE), h, why))


def aborted_path():
    d = os.path.join(C2, "aborted")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, "%s-%d-%d.json" % (os.path.basename(__file__)[:-3], os.getpid(), time.time_ns()))


def must_stop():
    if not os.path.exists(STOP) and not S.disk_free_ok():
        with open(STOP, "w") as f:
            f.write("%s disk floor: free %d < %d bytes\n" % (time.strftime("%Y-%m-%dT%H:%M:%S%z"), S.disk_free_bytes(),
                                                            S.DISK_FLOOR))
    return os.path.exists(STOP)


def witness(name, r):
    os.makedirs(os.path.join(C2, "witness"), exist_ok=True)
    open(os.path.join(C2, "witness", name + ".solver.txt"), "w").write(r["solver_out"])


def run_direct(mi, i, limit, budget):
    path = os.path.join(C2, "m2skel_drat", "ms%02d_b%05d.json" % (mi, i))
    if os.path.exists(path):
        return None
    d = skel(mi)
    sk = d["skeletons"][i]
    special = [p for p in d["profiles"] if list(p) != P0]

    def build():
        nv, cl = encode_skel_b.build_v2(d["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special)
        return encode_skel_b.cnf_bytes(nv, cl)

    r = S.cadical_staged(build, os.path.join(LANE, "scratch", "fifo", "v11m2_%02d_%05d" % (mi, i)), limit, budget)
    if (r.get("admission_denied") or r.get("aborted_by_sigterm")) and r.get("status") != "SAT":
        S.write_json(aborted_path(), dict(r, solver_out=""))
        return {"stopped": True, "reason": r.get("admission_denied") or "sigterm"}
    r.update({"multiset": mi, "b_index": i, "encoder": "encode_skel_b.build_v2", "generator": "gen_skel_b.py",
              "runner": "run_m2_11.py"})
    if r["status"] == "SAT":
        witness("m2_11_ms%02d_b%05d" % (mi, i), r)
    r["solver_out"] = ""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    S.write_json(path, r)
    return r


def run_split(mi, bi, limit, budget, bsize):
    name = "ms%02d_b%05d" % (mi, bi)
    dd = os.path.join(C2, "m2part_drat", name)
    if os.path.exists(os.path.join(dd, "summary_batched.json")):
        return None
    os.makedirs(dd, exist_ok=True)
    skp = os.path.join(SK, "skeletons-b-ms%02d.json" % mi)
    ext = os.path.join(dd, "ext.json")
    if not os.path.exists(ext):
        with S.Token(stage="extend_b"):
            rc, out = S.run_helper([sys.executable, os.path.join(HERE, "extend_b.py"), skp, str(bi), ext])
        if rc != 0:
            raise RuntimeError("extend_b failed rc=%s %s" % (rc, out[-300:]))
    E = json.load(open(ext))
    D = skel(mi)
    sk = D["skeletons"][bi]
    special = [p for p in D["profiles"] if list(p) != P0]
    n = E["num_placements"]
    st = {"batches": 0, "UNSAT_checked": 0, "other": 0, "SAT": 0}
    for j in range(0, n, bsize):
        idx = list(range(j, min(n, j + bsize)))
        bp = os.path.join(dd, "batch_%05d_%05d.json" % (idx[0], idx[-1]))
        if not os.path.exists(bp) and must_stop():
            return {"stopped": True}
        if os.path.exists(bp):
            r = json.load(open(bp))
        else:
            def build():
                nv, cl = encode_skel_b.build_partbatch(D["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special,
                                                       [E["placements"][i] for i in idx])
                return encode_skel_b.cnf_bytes(nv, cl)

            r = S.cadical_staged(build, os.path.join(LANE, "scratch", "fifo", "v11m2pb_%s_%05d" % (name, idx[0])), limit,
                                 budget)
            if (r.get("admission_denied") or r.get("aborted_by_sigterm")) and r.get("status") != "SAT":
                S.write_json(aborted_path(), dict(r, solver_out=""))
                return {"stopped": True, "reason": r.get("admission_denied") or "sigterm"}
            r.update({"multiset": mi, "b_index": bi, "indices": [idx[0], idx[-1]],
                      "encoder": "encode_skel_b.build_partbatch", "enumerator": "extend_b.py", "runner": "run_m2_11.py"})
            if r["status"] == "SAT":
                witness("m2pb11_%s_%05d" % (name, idx[0]), r)
            r["solver_out"] = ""
            S.write_json(bp, r)
        st["batches"] += 1
        if r["status"] == "UNSAT" and r["checked"]:
            st["UNSAT_checked"] += len(idx)
        elif r["status"] == "SAT":
            st["SAT"] += 1
            break
        else:
            st["other"] += len(idx)
    res = {"multiset": mi, "b_index": bi, "num_sub": n, **st, "runner": "run_m2_11.py"}
    res["decided_unsat"] = st["UNSAT_checked"] == n and st["SAT"] == 0
    S.write_json(os.path.join(dd, "summary_batched.json"), res)
    return res


def main():
    mode, limit, budget, bsize = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
    jobs = []
    for arg in sys.argv[5:]:
        mi, rng = arg.split(":")
        if "-" in rng:
            a, b = rng.split("-")
            jobs += [(int(mi), i) for i in range(int(a), int(b) + 1)]
        else:
            jobs.append((int(mi), int(rng)))
    S.install_sigterm_handler()
    S.set_stop_files([STOP])
    for mi, i in jobs:
        if S.ABORT[0]:
            print(time.strftime("%H:%M:%S"), "ABORT -- stopping", flush=True)
            return
        if must_stop():
            print(time.strftime("%H:%M:%S"), "STOP -- stopping", flush=True)
            return
        cn = ("m2d9_" if mode == "direct" else "m2pbd9_") + "ms%02d_b%05d" % (mi, i)
        if mode == "direct" and os.path.exists(os.path.join(C2, "m2skel_drat", "ms%02d_b%05d.json" % (mi, i))):
            continue
        if not claim(cn):
            continue
        try:
            r = run_direct(mi, i, limit, budget) if mode == "direct" else run_split(mi, i, limit, budget, bsize)
        except (S.AdmissionDenied, SystemExit) as e:
            r = {"stopped": True, "reason": repr(e)}
        if r is None:
            continue
        if r.get("stopped"):
            release(cn, "run_m2_11 stop: claim released (stop/abort/admission refused)")
            print(time.strftime("%H:%M:%S"), "stopped inside", cn, "-- claim released", flush=True)
            return
        keep = ("multiset", "b_index", "status", "checked", "solve_seconds", "check_seconds", "drat_bytes", "token",
                "num_sub", "batches", "UNSAT_checked", "other", "SAT", "decided_unsat")
        print(time.strftime("%H:%M:%S"), json.dumps({k: r.get(k) for k in keep if k in r}), flush=True)
        if r.get("status") == "SAT" or r.get("SAT"):
            print("SAT FOUND -- stopping this runner", flush=True)
            return


if __name__ == "__main__":
    main()
