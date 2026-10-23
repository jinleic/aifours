"""RSS-only library successor of k5_resplit_r2.py90b6f592...8484.
certify() below is BYTE-IDENTICAL to the frozen r2 data plane. rss_kb is now
real libproc through darwin_process_metrics, never a setuid helper. Production
requires the pinned external owned-group supervisor; worker successes remain
legacy producer candidates, not parent measured-feed/F4 refutations.
"""
from __future__ import annotations

import hashlib
import os
import signal
import subprocess
import threading
import time
from darwin_process_metrics import rss_kb

HERE = os.path.dirname(os.path.abspath(__file__))
DT = os.path.normpath(os.path.join(HERE, "..", "..", "moqls7-problem16", "env", "drat-trim", "drat-trim"))
SOLVER_ARGS = ["-q"]
DT_FLAGS = ["-i"]


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

