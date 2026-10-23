"""K5 split (README §8). Never deletes; FIFO nodes reused; one receipt line per cube (resumable).

cubes: write all 2^|V| complete assignments of the declared variables V (DIMACS ids) as iCNF lines "a l1 .. lk 0",
       cube b sets V[k] to bit k of b; a receipt records V, the count and the file SHA-256.
run:   for the selected cube indices: CNF = base + unit clauses (streamed through a lane FIFO; SHA-256 of the exact bytes
       recorded) -> CaDiCaL (-t LIMIT) under /usr/bin/time -l, binary DRAT -> FIFO -> zstd -3 -> retained proof (size
       watchdog: SIGTERM to the solver if the compressed proof exceeds --cap-bytes => UNKNOWN); then
       zstd -dc PROOF | drat-trim CNF(FIFO) -i -t T under /usr/bin/time -l; strict verdict (line == "s VERIFIED"
       after stripping \\r, no "NOT VERIFIED", solver exit 20).
python -B k5_split.py cubes --vars 57,106,155,204,253,302,351 --out ../evidence/k5_split_v1/cubes_V7.icnf
python -B k5_split.py run --cnf ../evidence/gram_dev_v1/GA5L_K5_sb2.cnf --cubes ../evidence/k5_split_v1/cubes_V7.icnf \\
       --indices 1,8,3,24,9,14 --outdir ../evidence/k5_split_v1/pilot --time 900 --cap-bytes 300000000 --jobs 2
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import re
import signal
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


def cmd_cubes(a):
    V = [int(x) for x in a.vars.split(",")]
    with open(a.out, "x") as fh:
        for b in range(2 ** len(V)):
            fh.write("a " + " ".join(str(v if (b >> k) & 1 else -v) for k, v in enumerate(V)) + " 0\n")
    rec = {"argv": sys.argv, "vars": V, "cubes": 2 ** len(V), "sha256": sha_file(a.out),
           "coverage": "all complete assignments of the declared variables (tautology by construction)"}
    with open(a.out + ".receipt.json", "x") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps(rec))


def rss_from(path):
    m = re.search(r"(\d+)\s+maximum resident set size", open(path).read())
    return int(m.group(1)) if m else None


def feed(fifo, parts):
    with open(fifo, "wb") as fh:
        for p in parts:
            fh.write(p)


def run_cube(b, lits, header_nv, header_nc, body, outdir, fifos, tlim, cap):
    f_cnf, f_proof = fifos
    tail = "".join("%d 0\n" % l for l in lits).encode()
    head = ("p cnf %d %d\n" % (header_nv, header_nc + len(lits))).encode()
    h = hashlib.sha256()
    for part in (head, body, tail):
        h.update(part)
    tag = "cube%03d" % b
    proof = os.path.join(outdir, tag + ".drat.zst")
    rec = {"cube": b, "lits": lits, "cnf_sha256": h.hexdigest()}
    t0 = time.time()
    with open(proof, "xb") as out, open(os.path.join(outdir, tag + ".solver.log"), "x") as slog:
        s = subprocess.Popen(["/usr/bin/time", "-l", "cadical", "-q", "-t", str(tlim), f_cnf, f_proof], stdout=slog,
                             stderr=subprocess.STDOUT)
        th = threading.Thread(target=feed, args=(f_cnf, (head, body, tail)))
        th.start()
        rfd = open(f_proof, "rb")
        z = subprocess.Popen(["zstd", "-q", "-c", "-3"], stdin=rfd, stdout=out)
        rfd.close()
        stopped = False
        while s.poll() is None:
            if os.path.getsize(proof) > cap and not stopped:
                stopped = True
                # SIGTERM the solver (child of /usr/bin/time); cooperative stop only
                for line in subprocess.run(["pgrep", "-P", str(s.pid)], capture_output=True, text=True).stdout.split():
                    os.kill(int(line), signal.SIGTERM)
            time.sleep(2)
        z.wait()
        th.join()
    solve_secs = round(time.time() - t0, 1)
    slog_txt = open(os.path.join(outdir, tag + ".solver.log")).read()
    status = "UNSAT" if re.search(r"^s UNSATISFIABLE", slog_txt, re.M) else \
        ("SAT" if re.search(r"^s SATISFIABLE", slog_txt, re.M) else "UNKNOWN")
    rec.update({"solver_status": status, "solve_secs": solve_secs, "stopped_by_cap": stopped,
                "solver_rss_bytes": rss_from(os.path.join(outdir, tag + ".solver.log")),
                "proof_bytes_zst": os.path.getsize(proof), "proof_sha256": sha_file(proof)})
    if status == "UNSAT" and not stopped:
        t1 = time.time()
        with open(os.path.join(outdir, tag + ".drat-trim.log"), "x") as dlog:
            z2 = subprocess.Popen(["zstd", "-q", "-dc", proof], stdout=subprocess.PIPE)
            d = subprocess.Popen(["/usr/bin/time", "-l", DT, f_cnf, "-i", "-t", "40000"], stdin=z2.stdout,
                                 stdout=dlog, stderr=subprocess.STDOUT)
            z2.stdout.close()
            th = threading.Thread(target=feed, args=(f_cnf, (head, body, tail)))
            th.start()
            d.wait()
            z2.wait()
            th.join()
        txt = open(os.path.join(outdir, tag + ".drat-trim.log")).read()
        lines = [l.replace("\r", "").strip() for l in txt.split("\n")]
        rec.update({"check_secs": round(time.time() - t1, 1), "check_exit": d.returncode,
                    "checker_rss_bytes": rss_from(os.path.join(outdir, tag + ".drat-trim.log")),
                    "verified": ("s VERIFIED" in lines) and ("s NOT VERIFIED" not in lines)})
    else:
        rec["verified"] = False
    return rec


def cmd_run(a):
    os.makedirs(a.outdir, exist_ok=True)
    res_path = os.path.join(a.outdir, "RESULTS.jsonl")
    done = set()
    if os.path.exists(res_path):
        done = {json.loads(l)["cube"] for l in open(res_path)}
    cubes = [[int(t) for t in l.split()[1:-1]] for l in open(a.cubes) if l.startswith("a ")]
    with open(a.cnf, "rb") as fh:
        header = fh.readline().decode().split()
        body = fh.read()
    nv, nc = int(header[2]), int(header[3])
    meta = {"argv": sys.argv, "python": sys.version, "script_sha256": sha_file(__file__), "cnf_sha256": sha_file(a.cnf),
            "cubes_sha256": sha_file(a.cubes),
            "cadical_sha256": sha_file(os.path.realpath("/opt/homebrew/bin/cadical")), "drat_trim_sha256": sha_file(DT)}
    with open(os.path.join(a.outdir, "META.%d.json" % int(time.time())), "x") as fh:
        json.dump(meta, fh, indent=1)
    idx = [int(x) for x in a.indices.split(",")]
    todo = [b for b in idx if b not in done]
    pool = []
    for w in range(a.jobs):
        pair = (os.path.join(a.outdir, "w%d.cnf.fifo" % w), os.path.join(a.outdir, "w%d.proof.fifo" % w))
        for p in pair:
            if not os.path.exists(p):
                os.mkfifo(p)
        pool.append(pair)
    free = list(range(a.jobs))
    lock = threading.Lock()

    def work(b):
        with lock:
            w = free.pop()
        try:
            rec = run_cube(b, cubes[b], nv, nc, body, a.outdir, pool[w], a.time, a.cap_bytes)
            with lock:
                with open(res_path, "a") as fh:
                    fh.write(json.dumps(rec) + "\n")
            print(json.dumps({k: rec.get(k) for k in ("cube", "solver_status", "solve_secs", "proof_bytes_zst",
                                                      "check_secs", "checker_rss_bytes", "verified")}), flush=True)
        finally:
            with lock:
                free.append(w)

    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        list(ex.map(work, todo))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["cubes", "run"])
    ap.add_argument("--vars")
    ap.add_argument("--out")
    ap.add_argument("--cnf")
    ap.add_argument("--cubes")
    ap.add_argument("--indices")
    ap.add_argument("--outdir")
    ap.add_argument("--time", type=int, default=900)
    ap.add_argument("--cap-bytes", type=int, default=300_000_000)
    ap.add_argument("--jobs", type=int, default=2)
    a = ap.parse_args()
    cmd_cubes(a) if a.mode == "cubes" else cmd_run(a)


if __name__ == "__main__":
    main()
