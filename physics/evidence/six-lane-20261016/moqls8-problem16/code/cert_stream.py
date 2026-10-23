"""Streamed certification (parent strategy (b)/(c)): the solver's binary DRAT proof goes through a lane FIFO straight
into drat-trim (proof read from stdin, binary mode forced), so proofs need not be stored; the CNF (optionally with
cube unit clauses, or with the negated cubes for the cover check) is streamed into the solver and into drat-trim
through two more lane FIFOs. No proof is stored.
One JSON line per task in RESULTS.jsonl: deterministic-replay receipt (solver binary SHA-256, version, argv, CNF SHA,
cube literals, solver exit/status, checker exit/verdict, wall times). Resumable; never deletes; FIFO nodes reused.
Timeouts/errors are UNKNOWN; a check without "s VERIFIED" is NOT a certificate.

python -B cert_stream.py cubes --cnf X.cnf --cubes X.icnf --outdir D --jobs 1 --time 3000
python -B cert_stream.py cover --cnf X.cnf --cubes X.icnf --outdir D --time 3000
python -B cert_stream.py whole --cnf X.cnf --outdir D --time 10500
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DT = os.path.normpath(os.path.join(HERE, "..", "..", "moqls7-problem16", "env", "drat-trim", "drat-trim"))


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 24), b""):
            h.update(chunk)
    return h.hexdigest()


def read_cnf(path):
    with open(path, "rb") as fh:
        header = fh.readline().decode()
        body = fh.read()
    _, _, nv, nc = header.split()
    return int(nv), int(nc), body


def read_cubes(path):
    out = []
    for line in open(path):
        if line.startswith("a "):
            lits = [int(t) for t in line.split()[1:]]
            out.append(lits[:-1])
    return out


def feed(fifo, chunks):
    with open(fifo, "wb") as fh:
        for c in chunks:
            fh.write(c)


def certify(task, nv, nc, body, extra, fifos, outdir, tlim):
    """extra: list of clauses appended to the CNF (cube units or negated cubes)."""
    fcnf_s, fcnf_c, fproof = fifos
    tail = "".join(" ".join(map(str, cl)) + " 0\n" for cl in extra).encode()
    header = ("p cnf %d %d\n" % (nv, nc + len(extra))).encode()
    h = hashlib.sha256()
    for part in (header, body, tail):
        h.update(part)
    t0 = time.time()
    log_s = open(os.path.join(outdir, task + ".solver.log"), "x")
    log_c = open(os.path.join(outdir, task + ".drat-trim.log"), "x")
    s = subprocess.Popen(["cadical", "-q", "-t", str(tlim), fcnf_s, fproof], stdout=log_s, stderr=subprocess.STDOUT)
    th_s = threading.Thread(target=feed, args=(fcnf_s, (header, body, tail)))
    th_s.start()
    rfd = open(fproof, "rb")            # blocks until the solver opens its proof file
    d = subprocess.Popen([DT, fcnf_c, "-i", "-t", str(max(tlim * 3, 20000))], stdin=rfd, stdout=log_c,
                         stderr=subprocess.STDOUT)
    rfd.close()
    th_c = threading.Thread(target=feed, args=(fcnf_c, (header, body, tail)))
    th_c.start()
    s.wait()
    t_solve = round(time.time() - t0, 1)
    d.wait()
    th_s.join()
    th_c.join()
    log_s.close()
    log_c.close()
    txt = open(os.path.join(outdir, task + ".drat-trim.log")).read()
    status = {10: "SAT", 20: "UNSAT"}.get(s.returncode, "UNKNOWN")
    return {"task": task, "cnf_sha256": h.hexdigest(), "added_clauses": len(extra), "solver_exit": s.returncode,
            "status": status, "solve_secs": t_solve, "checker_exit": d.returncode,
            "verified": status == "UNSAT" and "s VERIFIED" in txt and "NOT VERIFIED" not in txt,
            "total_secs": round(time.time() - t0, 1)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["cubes", "cover", "whole"])
    ap.add_argument("--cnf", required=True)
    ap.add_argument("--cubes")
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--jobs", type=int, default=1)
    ap.add_argument("--time", type=int, default=3000)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    res_path = os.path.join(a.outdir, "RESULTS.jsonl")
    done = set()
    if os.path.exists(res_path):
        done = {json.loads(l)["task"] for l in open(res_path)}
    cad = os.path.realpath("/opt/homebrew/bin/cadical")
    meta = {"argv": sys.argv, "python": sys.version, "script_sha256": sha_file(__file__), "cnf": a.cnf,
            "cnf_file_sha256": sha_file(a.cnf), "cubes_sha256": sha_file(a.cubes) if a.cubes else None,
            "cadical_binary": cad, "cadical_sha256": sha_file(cad),
            "cadical_version": subprocess.run(["cadical", "--version"], capture_output=True, text=True).stdout.strip(),
            "drat_trim": DT, "drat_trim_sha256": sha_file(DT)}
    with open(os.path.join(a.outdir, "META.%s.%d.json" % (a.mode, int(time.time()))), "x") as fh:
        json.dump(meta, fh, indent=1)
    nv, nc, body = read_cnf(a.cnf)
    tasks = []
    if a.mode == "whole":
        tasks = [("whole", [])]
    elif a.mode == "cover":
        tasks = [("cover", [[-l for l in c] for c in read_cubes(a.cubes)])]
    else:
        tasks = [("cube%05d" % k, [[l] for l in c]) for k, c in enumerate(read_cubes(a.cubes))]
    tasks = [t for t in tasks if t[0] not in done]
    lock = threading.Lock()
    pool = []
    for w in range(a.jobs):
        trip = tuple(os.path.join(a.outdir, "w%d.%s.fifo" % (w, nm)) for nm in ("cnf_s", "cnf_c", "proof"))
        for p in trip:
            if not os.path.exists(p):
                os.mkfifo(p)
        pool.append(trip)
    free = list(range(a.jobs))

    def work(t):
        name, extra = t
        with lock:
            w = free.pop()
        try:
            rec = certify(name, nv, nc, body, extra, pool[w], a.outdir, a.time)
            if a.mode == "cubes":
                rec["cube"] = [c[0] for c in extra]
            with lock:
                with open(res_path, "a") as fh:
                    fh.write(json.dumps(rec) + "\n")
            print(json.dumps({k: rec[k] for k in ("task", "status", "verified", "solve_secs", "total_secs")}),
                  flush=True)
            return rec
        finally:
            with lock:
                free.append(w)

    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        list(ex.map(work, tasks))
    rows = [json.loads(l) for l in open(res_path)]
    print(json.dumps({"tasks_recorded": len(rows), "verified": sum(r["verified"] for r in rows),
                      "non_verified": [r["task"] for r in rows if not r["verified"]][:20]}))


if __name__ == "__main__":
    main()
