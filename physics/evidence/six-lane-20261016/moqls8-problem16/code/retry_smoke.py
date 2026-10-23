"""Smoke controls for certify() of code/k5_resplit_r2.py before first production use of the RETRY-ONCE amendment:
PHP(6,5) UNSAT → verified (tlim 60, checker 60); PHP(5,5) SAT → not verified; PHP(8,7) UNSAT with checker limit 1 s →
expected NOT verified (checker timeout), recorded as observed. Receipts: OUTDIR/SMOKE.jsonl.
python -B retry_smoke.py --outdir ../evidence/k5_split_v1/retry_smoke
"""
from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("k5_resplit_r2", os.path.join(HERE, "k5_resplit_r2.py"))
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)


def php(p, h):
    v = lambda i, j: i * h + j + 1
    cls = [[v(i, j) for j in range(h)] for i in range(p)]
    for j in range(h):
        for i1, i2 in itertools.combinations(range(p), 2):
            cls.append([-v(i1, j), -v(i2, j)])
    return p * h, len(cls), "".join(" ".join(map(str, c)) + " 0\n" for c in cls).encode()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", required=True)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=False)
    fifos = tuple(os.path.join(a.outdir, "w0.%s.fifo" % x) for x in ("cnf_s", "cnf_c", "proof"))
    for p in fifos:
        os.mkfifo(p)
    out = open(os.path.join(a.outdir, "SMOKE.jsonl"), "x")
    for tag, (p, h), tl, cl, expect in (("php65", (6, 5), 60, 60, True), ("php55", (5, 5), 60, 60, False),
                                         ("php87_checker1s", (8, 7), 300, 1, False)):
        nv, nc, body = php(p, h)
        rec = R.certify(tag, [], nv, nc, body, a.outdir, fifos, tl, 6 * 2 ** 30, checker_limit=cl)
        rec.update({"case": tag, "expected_verified": expect, "control_pass": rec["verified"] == expect})
        out.write(json.dumps(rec) + "\n")
        out.flush()
        print(json.dumps({k: rec[k] for k in ("case", "verified", "expected_verified", "control_pass",
                                              "solver_returncode", "checker_returncode", "checker_status_lines",
                                              "checker_argv", "proof_stream_bytes", "secs")}))


if __name__ == "__main__":
    main()
