#!/usr/bin/env python3
"""Witness gate for a CFR(r,n) candidate in cfr-raw-v1 (copy of cfr33/code/witness_gate_v1.py, sha256 9274ae4c...53b9, for
sub-lane cfr21; only change: it imports controls_c21v1 and runs the byte-identical copies cfr_check_events_c21v1.py and
cfr_check_posdiff_c21v1.py from cfr21/code). Usage: witness_gate_c21v1.py RAW R N OUTDIR
OUTDIR is created (must not exist). Runs checker A (direct events) and checker B (position differences) on the
unmodified file (both must PASS), then the 9 mutations of controls_v1.py (intended reasons must appear; the
swap-two-symbols mutation is report-only), writes OUTDIR/receipt.json (sha256 of input, checkers, outputs) and the
mutated files. Exit 0 iff every expectation holds.
"""
import hashlib, json, os, subprocess, sys

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(LANE, "code"))
from controls_c21v1 import mutations  # byte-identical copy of cfr33/code/controls_v1.py

A = os.path.join(LANE, "code", "cfr_check_events_c21v1.py")
B = os.path.join(LANE, "code", "cfr_check_posdiff_c21v1.py")


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout


def main():
    raw, r, n, outdir = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    os.mkdir(outdir)
    data = open(raw, "rb").read()
    rec = {"input": os.path.abspath(raw), "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), "r": r, "n": n,
           "expected_events": r * n * (n - 1),
           "checker_sha256": {os.path.basename(x): hashlib.sha256(open(x, "rb").read()).hexdigest() for x in (A, B)},
           "unmodified": {}, "mutations": []}
    ok = True
    for chk in (A, B):
        rc, out = run(["python3", chk, raw, str(r), str(n)])
        rec["unmodified"][os.path.basename(chk)] = {"rc": rc, "output": out}
        ok &= rc == 0 and out.strip().endswith("PASS")
    text = data.decode("ascii")
    for case, mtext, ra, rb in mutations(text, n):
        fp = os.path.join(outdir, case.split("(")[0] + ".raw")
        with open(fp, "x", newline="") as fh:
            fh.write(mtext)
        for chk, reason in ((A, ra), (B, rb)):
            rc, out = run(["python3", chk, fp, str(r), str(n)])
            last = out.strip().splitlines()[-1] if out.strip() else ""
            good = True if reason is None else (rc == 1 and reason in last)
            ok &= good
            rec["mutations"].append({"case": case, "checker": os.path.basename(chk), "rc": rc, "last": last,
                                     "expected_reason": reason, "as_expected": good})
    rec["all_as_expected"] = ok
    with open(os.path.join(outdir, "receipt.json"), "x") as fh:
        json.dump(rec, fh, indent=1)
    print("GATE PASS" if ok else "GATE FAIL", rec["sha256"])
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
