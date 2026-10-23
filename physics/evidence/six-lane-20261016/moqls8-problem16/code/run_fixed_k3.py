"""Fixed-net batch with streamed CNFs (README §4): CNFs are built in memory by the encoders' own build/encode
functions (code/enc8_a2.py build(), code/enc8_b2.py encode()), serialised exactly as their writers do, hashed
(SHA-256 of the DIMACS bytes) and streamed to the solver / checker through reusable lane FIFOs. Not stored.
Encoder A: CaDiCaL with binary DRAT -> zstd (stored), then drat-trim (CNF via FIFO, proof via stdin, -i).
Encoder B: kissat, no proof. Resumable: one JSON line per (net, encoder) in RESULTS.jsonl; finished pairs skipped.
Timeouts/errors are UNKNOWN. Never deletes.

python -B run_fixed_k3.py --catalogue max:../sources/ew_data/maxMOLS8.2.txt,nmax:../sources/ew_data/nmaxMOLS8.2.txt \\
   --k 2 --quantum 123 --outdir ../evidence/k3_fixed/pilot_v1 --limit 2 --jobs 2
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import importlib.util
import io
import json
import os
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DT = os.path.normpath(os.path.join(HERE, "..", "..", "moqls7-problem16", "env", "drat-trim", "drat-trim"))
N = 8


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


A = load("enc8_a2")
B = load("enc8_b2")


def parse(path):
    lines = open(path).read().split("\n")
    n, k, m = (int(x) for x in lines[0].split()[:3])
    sq, cur = [], []
    for line in lines[1:]:
        s = line.strip()
        if not s:
            if cur:
                sq.append(cur)
                cur = []
            continue
        if len(s) != n or not all("a" <= ch <= chr(96 + n) for ch in s):
            break
        cur.append([ord(ch) - 97 for ch in s])
    if cur:
        sq.append(cur)
    assert len(sq) == m
    return sq


def normalize(L):
    perm = {L[0][j]: j for j in range(N)}
    return [[perm[x] for x in row] for row in L]


def dimacs(nv, clauses):
    buf = io.StringIO()
    buf.write("p cnf %d %d\n" % (nv, len(clauses)))
    for cl in clauses:
        buf.write(" ".join(map(str, cl)) + " 0\n")
    return buf.getvalue().encode()


def feed(fifo, data):
    with open(fifo, "wb") as fh:
        fh.write(data)


def solve_a(cnf_bytes, tag, outdir, fifo_cnf, fifo_proof, tlim):
    # a run interrupted before its RESULTS line leaves files behind; never overwrite them: use a fresh suffix
    k = 0
    stem = tag + ".a"
    while os.path.exists(os.path.join(outdir, stem + ".drat.zst")):
        k += 1
        stem = "%s.a.retry%d" % (tag, k)
    proof = os.path.join(outdir, stem + ".drat.zst")
    with open(proof, "xb") as out, open(os.path.join(outdir, stem + ".solve.log"), "x") as slog:
        t0 = time.time()
        s = subprocess.Popen(["cadical", "-q", "-t", str(tlim), fifo_cnf, fifo_proof], stdout=slog,
                             stderr=subprocess.STDOUT)
        th = threading.Thread(target=feed, args=(fifo_cnf, cnf_bytes))
        th.start()
        rfd = open(fifo_proof, "rb")
        z = subprocess.Popen(["zstd", "-q", "-c", "-3"], stdin=rfd, stdout=out)
        rfd.close()
        s.wait()
        z.wait()
        th.join()
        secs = round(time.time() - t0, 2)
    status = {10: "SAT", 20: "UNSAT"}.get(s.returncode, "UNKNOWN")
    rec = {"status": status, "exit": s.returncode, "secs": secs, "proof": os.path.basename(proof),
           "proof_bytes": os.path.getsize(proof), "proof_sha256": hashlib.sha256(open(proof, "rb").read()).hexdigest()}
    if status == "UNSAT":
        with open(os.path.join(outdir, stem + ".drat-trim.log"), "x") as dlog:
            t1 = time.time()
            z2 = subprocess.Popen(["zstd", "-q", "-dc", proof], stdout=subprocess.PIPE)
            d = subprocess.Popen([DT, fifo_cnf, "-i", "-t", "20000"], stdin=z2.stdout, stdout=dlog,
                                 stderr=subprocess.STDOUT)
            z2.stdout.close()
            th = threading.Thread(target=feed, args=(fifo_cnf, cnf_bytes))
            th.start()
            d.wait()
            z2.wait()
            th.join()
        txt = open(os.path.join(outdir, stem + ".drat-trim.log")).read()
        rec.update({"verified": "s VERIFIED" in txt and "NOT VERIFIED" not in txt, "check_exit": d.returncode,
                    "check_secs": round(time.time() - t1, 2)})
    return rec


def solve_b(cnf_bytes, fifo_cnf, tlim):
    t0 = time.time()
    s = subprocess.Popen(["kissat", "-q", "--time=%d" % tlim, fifo_cnf], stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    th = threading.Thread(target=feed, args=(fifo_cnf, cnf_bytes))
    th.start()
    s.communicate()
    th.join()
    return {"status": {10: "SAT", 20: "UNSAT"}.get(s.returncode, "UNKNOWN"), "exit": s.returncode,
            "secs": round(time.time() - t0, 2)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalogue", required=True, help="kind:path,kind:path")
    ap.add_argument("--k", type=int, required=True, help="squares per set (classical squares)")
    ap.add_argument("--quantum", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", default="", help="comma list of tags")
    ap.add_argument("--jobs", type=int, default=2)
    ap.add_argument("--time", type=int, default=1800)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    res_path = os.path.join(a.outdir, "RESULTS.jsonl")
    done = set()
    if os.path.exists(res_path):
        for line in open(res_path):
            r = json.loads(line)
            done.add((r["net"], r["encoder"]))
    meta_path = os.path.join(a.outdir, "META.%d.json" % int(time.time()))
    with open(meta_path, "x") as fh:
        json.dump({"argv": sys.argv, "python": sys.version,
                   "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
                   "enc_a2_sha256": hashlib.sha256(open(os.path.join(HERE, "enc8_a2.py"), "rb").read()).hexdigest(),
                   "enc_b2_sha256": hashlib.sha256(open(os.path.join(HERE, "enc8_b2.py"), "rb").read()).hexdigest(),
                   "drat_trim_sha256": hashlib.sha256(open(DT, "rb").read()).hexdigest()}, fh, indent=1)
    nets = []
    for part in a.catalogue.split(","):
        kind, path = part.split(":", 1)
        sq = parse(path)
        assert len(sq) % a.k == 0
        for s in range(len(sq) // a.k):
            nets.append(("%s%04d" % (kind, s), [normalize(L) for L in sq[a.k * s:a.k * s + a.k]]))
    if a.only:
        keep = set(a.only.split(","))
        nets = [x for x in nets if x[0] in keep]
    if a.limit:
        nets = nets[:a.limit]
    quantum = tuple(int(ch) for ch in a.quantum)
    lock = threading.Lock()
    fifo_pool = []
    for w in range(a.jobs):
        pair = (os.path.join(a.outdir, "w%d.cnf.fifo" % w), os.path.join(a.outdir, "w%d.proof.fifo" % w))
        for p in pair:
            if not os.path.exists(p):
                os.mkfifo(p)
        fifo_pool.append(pair)
    free = list(range(a.jobs))

    def work(job):
        tag, sqs = job
        with lock:
            w = free.pop()
        try:
            fifo_cnf, fifo_proof = fifo_pool[w]
            out = []
            for enc in ("a", "b"):
                if (tag, enc) in done:
                    continue
                if enc == "a":
                    f = A.build("fixed", (), quantum, p3=True, p4=quantum, squares=sqs)
                    data = dimacs(f.nv, f.clauses)
                else:
                    F = B.encode("fixed", [], False, quantum, quantum, None, True, 2, False, sqs)
                    data = dimacs(F.count, F.cls)
                rec = {"net": tag, "encoder": enc, "cnf_sha256": hashlib.sha256(data).hexdigest(),
                       "cnf_bytes": len(data)}
                rec.update(solve_a(data, tag, a.outdir, fifo_cnf, fifo_proof, a.time) if enc == "a"
                           else solve_b(data, fifo_cnf, a.time))
                with lock:
                    with open(res_path, "a") as fh:
                        fh.write(json.dumps(rec) + "\n")
                out.append(rec)
                print(json.dumps({k: rec.get(k) for k in ("net", "encoder", "status", "secs", "verified",
                                                          "proof_bytes")}), flush=True)
            return out
        finally:
            with lock:
                free.append(w)

    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        list(ex.map(work, nets))
    rows = [json.loads(l) for l in open(res_path)]
    summ = {"pairs_recorded": len(rows), "unsat": sum(r["status"] == "UNSAT" for r in rows),
            "a_verified": sum(1 for r in rows if r["encoder"] == "a" and r.get("verified")),
            "non_unsat": [(r["net"], r["encoder"], r["status"]) for r in rows if r["status"] != "UNSAT"]}
    print(json.dumps(summ))


if __name__ == "__main__":
    main()
