"""Smoke controls for code/k5_resplit.py certify() (not part of any cover): (1) pigeonhole PHP(6 pigeons, 5 holes) —
UNSAT, must be VERIFIED; (2) PHP(5,5) — SAT, must NOT be verified; (3) one real leaf of the K5 base (depth-1 cube 0
∧ all-negative V2) — expected trivial UNSAT, must be VERIFIED; (4) fail-closed: the real leaf with a 1-second solver
limit on a hard parent (cube 16 ∧ all-negative V2), expected UNKNOWN unless solved. Receipts to OUTDIR/SMOKE.jsonl.
python -B k5_resplit_smoke.py --cnf ../evidence/gram_dev_v1/GA5L_K5_sb2.cnf --outdir ../evidence/k5_split_v1/resplit_smoke
"""
from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("k5_resplit", os.path.join(HERE, "k5_resplit.py"))
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)


def php(p, h):
    v = lambda i, j: i * h + j + 1
    cls = [[v(i, j) for j in range(h)] for i in range(p)]
    for j in range(h):
        for i1, i2 in itertools.combinations(range(p), 2):
            cls.append([-v(i1, j), -v(i2, j)])
    body = "".join(" ".join(map(str, c)) + " 0\n" for c in cls).encode()
    return p * h, len(cls), body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cnf", required=True)
    ap.add_argument("--outdir", required=True)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    fifos = tuple(os.path.join(a.outdir, "w0.%s.fifo" % x) for x in ("cnf_s", "cnf_c", "proof"))
    for p in fifos:
        if not os.path.exists(p):
            os.mkfifo(p)
    out = open(os.path.join(a.outdir, "SMOKE.jsonl"), "a")
    cases = []
    nv, nc, body = php(6, 5)
    cases.append(("php65_unsat", [], nv, nc, body, 60, True))
    nv, nc, body = php(5, 5)
    cases.append(("php55_sat", [], nv, nc, body, 60, False))
    with open(a.cnf, "rb") as fh:
        header = fh.readline().decode().split()
        kbody = fh.read()
    knv, knc = int(header[2]), int(header[3])
    V1 = [57, 106, 155, 204, 253, 302, 351]
    V2 = R.CHAIN[2]
    c0 = [-v for v in V1]
    c16 = [v if (16 >> k) & 1 else -v for k, v in enumerate(V1)]
    cases.append(("k5_c000_L2_000", c0 + [-v for v in V2], knv, knc, kbody, 900, True))
    cases.append(("k5_c016_L2_000_t1", c16 + [-v for v in V2], knv, knc, kbody, 1, None))
    for tag, lits, nv, nc, body, tl, expect in cases:
        rec = R.certify("smoke_" + tag, lits, nv, nc, body, a.outdir, fifos, tl, 6 * 2 ** 30)
        rec.update({"case": tag, "expected_verified": expect,
                    "control_pass": (rec["verified"] == expect) if expect is not None else (True if rec["verified"]
                                                                                             else rec["verified"] is False)})
        out.write(json.dumps(rec) + "\n")
        out.flush()
        print(json.dumps({k: rec[k] for k in ("case", "verified", "expected_verified", "control_pass",
                                              "solver_returncode", "checker_returncode", "checker_status_lines",
                                              "proof_stream_bytes", "secs", "aggregate_peak_rss_bytes")}))


if __name__ == "__main__":
    main()
