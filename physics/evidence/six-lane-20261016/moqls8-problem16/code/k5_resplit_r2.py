"""k5_resplit.py revision r2 = byte copy of k5_resplit.py (4aed8e43…7069) except: certify() takes checker_limit (the
drat-trim native -t, stated explicitly by the caller; default = the r1 value max(4·tlim, 20000)). Used by the
retry-once amendment (review/AMENDMENT_RETRY_ONCE.md). Pipeline, strict predicate and guards are unchanged.
K5 re-split with STREAMED, non-retained DRAT certification (README §8.1). Never deletes; no proofs stored.

Leaves: for each UNKNOWN parent leaf (ancestor id, depth d, literal list c) the children are c ∧ a for ALL 2^7 complete
assignments a of the pre-declared variable list V_{d+1} (§8.1 table); their disjunction is c (coverage by construction).
Per leaf: CNF = base + one unit clause per literal (header V, C + |lits|), streamed through a lane FIFO into CaDiCaL
(binary DRAT to a second FIFO); this engine reads the proof FIFO, hashes it (SHA-256, byte count) and relays it into
drat-trim's stdin (binary mode -i) while drat-trim reads the same CNF from a third FIFO. Combined RSS guard (engine +
solver + checker, sampled every 2 s): above --rss-cap SIGTERM to solver and checker, bounded wait, leaf UNKNOWN.
Disk guards before each leaf: filesystem free ≥ 12e9 bytes and lane size ≤ 9.5 GiB, else stop (receipt).
Strict verdict: solver exited by itself with code 20 and "s UNSATISFIABLE"; checker exited by itself with code 0 and a
line equal to "s VERIFIED" after stripping "\\r", and no "s NOT VERIFIED"; no feed/relay error. Else UNKNOWN.
Note (smoke 14:48): drat-trim alone prints "s VERIFIED" for an EMPTY proof when the leaf CNF is refuted by unit
propagation, so the solver-side conditions are indispensable.
python -B k5_resplit.py --cnf BASE --parents-json P.json --level 2 --outdir DIR --time 900
  (P.json: [{"id": "c016", "depth": 1, "lits": [...]} ...]; --level picks V_level from the §8.1 table)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, ".."))
DT = os.path.normpath(os.path.join(HERE, "..", "..", "moqls7-problem16", "env", "drat-trim", "drat-trim"))
# README §8.1 pre-declared refinement chain (DIMACS ids in the unconditional K5 base CNF, coordinates k = 1..7)
CHAIN = {
    2: [64, 113, 162, 211, 260, 309, 358],        # g_1((0,k),(3,0))
    3: [71, 120, 169, 218, 267, 316, 365],        # g_1((0,k),(4,0))
    4: [78, 127, 176, 225, 274, 323, 372],        # g_1((0,k),(5,0))
    5: [85, 134, 183, 232, 281, 330, 379],        # g_1((0,k),(6,0))
    6: [92, 141, 190, 239, 288, 337, 386],        # g_1((0,k),(7,0))
    7: [1625, 1674, 1723, 1772, 1821, 1870, 1919],  # g_2((0,k),(2,0))
    8: [1632, 1681, 1730, 1779, 1828, 1877, 1926],  # g_2((0,k),(3,0))
}
SOLVER_ARGS = ["-q"]          # CaDiCaL defaults otherwise (default seed), plus -t LIMIT
DT_FLAGS = ["-i"]             # binary proof from stdin; plus -t


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 24), b""):
            h.update(chunk)
    return h.hexdigest()


def rss_kb(pids):
    pids = [p for p in pids if p]
    if not pids:
        return 0
    out = subprocess.run(["ps", "-o", "rss=", "-p", ",".join(map(str, pids))], capture_output=True, text=True).stdout
    return sum(int(x) for x in out.split() if x.isdigit())


def lane_bytes():
    return int(subprocess.run(["du", "-sk", LANE], capture_output=True, text=True).stdout.split()[0]) * 1024


def certify(tag, lits, nv, nc, body, outdir, fifos, tlim, rss_cap, checker_limit=None):
    climit = max(4 * tlim, 20000) if checker_limit is None else int(checker_limit)
    f_s, f_c, f_p = fifos
    tail = "".join("%d 0\n" % l for l in lits).encode()
    head = ("p cnf %d %d\n" % (nv, nc + len(lits))).encode()
    h = hashlib.sha256()
    for part in (head, body, tail):
        h.update(part)

    feed_errors = []

    def feed(fifo):
        try:
            with open(fifo, "wb") as fh:
                fh.write(head)
                fh.write(body)
                fh.write(tail)
        except OSError as e:  # reader exited early (e.g. solver interrupted while parsing): leaf cannot certify
            feed_errors.append([os.path.basename(fifo), repr(e)])

    t0 = time.time()
    scmd = ["cadical"] + SOLVER_ARGS + ["-t", str(tlim), f_s, f_p]
    dcmd = [DT, f_c] + DT_FLAGS + ["-t", str(climit)]
    s = subprocess.Popen(scmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    th_s = threading.Thread(target=feed, args=(f_s,))
    th_s.start()
    d = subprocess.Popen(dcmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=False)
    th_c = threading.Thread(target=feed, args=(f_c,))
    th_c.start()
    ph = hashlib.sha256()
    pbytes = [0]
    relay_err = []

    def relay():
        try:
            with open(f_p, "rb") as rp:
                for chunk in iter(lambda: rp.read(1 << 20), b""):
                    ph.update(chunk)
                    pbytes[0] += len(chunk)
                    d.stdin.write(chunk)
            d.stdin.close()
        except Exception as e:  # checker died early etc.
            relay_err.append(repr(e))
            try:
                d.stdin.close()
            except Exception:
                pass
    th_r = threading.Thread(target=relay)
    th_r.start()
    sout = []
    dout = []
    th_so = threading.Thread(target=lambda: sout.append(s.stdout.read()))
    th_do = threading.Thread(target=lambda: dout.append(d.stdout.read()))
    th_so.start()
    th_do.start()
    peak = 0
    tripped = False
    while s.poll() is None or d.poll() is None:
        kb = rss_kb([os.getpid(), s.pid if s.poll() is None else 0, d.pid if d.poll() is None else 0])
        peak = max(peak, kb)
        if kb * 1024 > rss_cap and not tripped:
            tripped = True
            for p in (s, d):
                if p.poll() is None:
                    p.send_signal(signal.SIGTERM)
        time.sleep(2)
    for t in (th_s, th_c, th_r, th_so, th_do):
        t.join(timeout=60)
    stxt = (sout[0] if sout else "")
    dtxt = (dout[0].decode(errors="replace") if dout else "")
    with open(os.path.join(outdir, tag + ".solver.log"), "x") as fh:
        fh.write(stxt)
    with open(os.path.join(outdir, tag + ".drat-trim.log"), "x") as fh:
        fh.write(dtxt)
    s_lines = [l.replace("\r", "").strip() for l in stxt.split("\n") if l.startswith("s ")]
    d_lines = [l.replace("\r", "").strip() for l in dtxt.split("\n") if l.replace("\r", "").strip().startswith("s ")]
    self_exit = (not tripped) and s.returncode >= 0 and d.returncode >= 0
    verified = (self_exit and s.returncode == 20 and "s UNSATISFIABLE" in s_lines and d.returncode == 0
                and "s VERIFIED" in d_lines and "s NOT VERIFIED" not in d_lines and not relay_err and not feed_errors)
    return {"cnf_sha256": h.hexdigest(), "cnf_clauses": nc + len(lits), "cnf_vars": nv,
            "solver_argv": ["cadical"] + SOLVER_ARGS + ["-t", str(tlim), "<cnf>", "<proof>"],
            "solver_returncode": s.returncode, "solver_status_lines": s_lines,
            "proof_stream_sha256": ph.hexdigest(), "proof_stream_bytes": pbytes[0],
            "checker_argv": ["drat-trim", "<cnf>"] + DT_FLAGS + ["-t", str(climit)],
            "checker_returncode": d.returncode, "checker_status_lines": d_lines, "relay_errors": relay_err,
            "feed_errors": feed_errors,
            "rss_guard_tripped": tripped, "self_exit": self_exit, "aggregate_peak_rss_bytes": peak * 1024,
            "secs": round(time.time() - t0, 1), "verified": verified}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cnf", required=True)
    ap.add_argument("--parents-json", required=True)
    ap.add_argument("--level", type=int, required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--time", type=int, default=900)
    ap.add_argument("--rss-cap", type=int, default=6 * 2 ** 30)
    ap.add_argument("--floor", type=int, default=12_000_000_000)
    ap.add_argument("--lane-budget", type=int, default=int(9.5 * 2 ** 30))
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    V = CHAIN[a.level]
    parents = json.load(open(a.parents_json))
    leaves = []
    for p in parents:
        for b in range(128):
            leaves.append({"id": "%s.L%d.%03d" % (p["id"], a.level, b), "ancestor": p["id"], "depth": a.level,
                           "lits": p["lits"] + [v if (b >> k) & 1 else -v for k, v in enumerate(V)]})
    cad = os.path.realpath("/opt/homebrew/bin/cadical")
    meta = {"argv": sys.argv, "python": sys.version, "script_sha256": sha_file(__file__),
            "base_cnf_sha256": sha_file(a.cnf), "parents_json_sha256": sha_file(a.parents_json), "level": a.level,
            "V": V, "leaves": len(leaves), "cadical_binary": cad, "cadical_sha256": sha_file(cad),
            "cadical_version": subprocess.run(["cadical", "--version"], capture_output=True, text=True).stdout.strip(),
            "cadical_seed": "default (no --seed given)", "drat_trim_binary": DT, "drat_trim_sha256": sha_file(DT),
            "rss_cap": a.rss_cap, "floor": a.floor, "lane_budget": a.lane_budget}
    with open(os.path.join(a.outdir, "META.L%d.%d.json" % (a.level, int(time.time()))), "x") as fh:
        json.dump(meta, fh, indent=1)
    res_path = os.path.join(a.outdir, "RESULTS.jsonl")
    done = set()
    if os.path.exists(res_path):
        done = {json.loads(l)["id"] for l in open(res_path)}
    with open(a.cnf, "rb") as fh:
        header = fh.readline().decode().split()
        body = fh.read()
    nv, nc = int(header[2]), int(header[3])
    fifos = tuple(os.path.join(a.outdir, "w0.%s.fifo" % x) for x in ("cnf_s", "cnf_c", "proof"))
    for p in fifos:
        if not os.path.exists(p):
            os.mkfifo(p)
    for leaf in leaves:
        if leaf["id"] in done:
            continue
        fb = shutil.disk_usage(a.outdir).free
        lb = lane_bytes()
        if fb < a.floor or lb > a.lane_budget:
            with open(os.path.join(a.outdir, "STOP.%d.json" % int(time.time())), "x") as fh:
                json.dump({"before_leaf": leaf["id"], "free": fb, "lane_bytes": lb}, fh)
            print(json.dumps({"stop_before": leaf["id"], "free": fb, "lane": lb}), flush=True)
            break
        rec = dict(leaf)
        rec.update(certify(leaf["id"].replace("/", "_"), leaf["lits"], nv, nc, body, a.outdir, fifos, a.time,
                           a.rss_cap))
        with open(res_path, "a") as fh:
            fh.write(json.dumps(rec) + "\n")
        print(json.dumps({k: rec[k] for k in ("id", "verified", "solver_returncode", "secs",
                                              "aggregate_peak_rss_bytes", "proof_stream_bytes")}), flush=True)


if __name__ == "__main__":
    main()
