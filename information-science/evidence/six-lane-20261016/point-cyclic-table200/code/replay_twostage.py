#!/usr/bin/env python3
"""replay_twostage.py -- producer and expansion replay for a witness found by code/t2_twostage.c (README 2.3).

Steps, all inside OUTDIR (must not exist; nothing is deleted or overwritten):
  1. compile code/t2_twostage.c with `cc -O2` into OUTDIR/t2_twostage (records source/binary SHA-256, compiler);
  2. run OUTDIR/t2_twostage q seed seconds OUTDIR/replay (stdout -> OUTDIR/replay.log);
  3. compare OUTDIR/replay.seed with the pinned seed byte for byte;
  4. expand it with code/pc_expand_general.py into OUTDIR/replay.cert and compare with the pinned certificate;
  5. run code/pc_check.py on OUTDIR/replay.cert (receipt OUTDIR/check.json); 6. write OUTDIR/receipt.json.
Usage: replay_twostage.py OUTDIR q seed seconds PINNED_SEED PINNED_CERT
"""
from datetime import datetime
import hashlib
import json
import os
import subprocess
import sys
from zoneinfo import ZoneInfo

CODE = os.path.dirname(os.path.abspath(__file__))


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main(argv):
    if len(argv) != 7:
        print(__doc__, file=sys.stderr)
        return 2
    out, q, seed, secs, pseed, pcert = argv[1:]
    os.makedirs(out)
    rec = {"started_at_pt": datetime.now(ZoneInfo("America/Los_Angeles")).isoformat(),
           "args": {"q": q, "seed": seed, "seconds": secs},
           "pinned_seed": {"path": pseed, "sha256": sha(pseed)}, "pinned_cert": {"path": pcert, "sha256": sha(pcert)}}
    src = os.path.join(CODE, "t2_twostage.c")
    binp = os.path.join(out, "t2_twostage")
    cc = subprocess.run(["cc", "-O2", "-o", binp, src], capture_output=True, text=True)
    ver = subprocess.run(["cc", "--version"], capture_output=True, text=True).stdout.split("\n")[0]
    rec["build"] = {"source_sha256": sha(src), "rc": cc.returncode, "stderr": cc.stderr, "compiler": ver}
    ok = cc.returncode == 0
    if ok:
        rec["build"]["binary_sha256"] = sha(binp)
        with open(os.path.join(out, "replay.log"), "x") as log:
            run = subprocess.run([binp, q, seed, secs, os.path.join(out, "replay")], stdout=log,
                                 stderr=subprocess.STDOUT)
        rec["run_rc"] = run.returncode
        rseed = os.path.join(out, "replay.seed")
        ok = run.returncode == 0 and os.path.exists(rseed)
        if ok:
            rec["seed_byte_identical"] = open(rseed, "rb").read() == open(pseed, "rb").read()
            rcert = os.path.join(out, "replay.cert")
            ex = subprocess.run([sys.executable, os.path.join(CODE, "pc_expand_general.py"), rseed, rcert],
                                capture_output=True, text=True)
            rec["expand"] = {"rc": ex.returncode, "stdout": ex.stdout.strip()}
            ok = rec["seed_byte_identical"] and ex.returncode == 0
            if ex.returncode == 0:
                rec["cert_byte_identical"] = open(rcert, "rb").read() == open(pcert, "rb").read()
                ch = subprocess.run([sys.executable, os.path.join(CODE, "pc_check.py"), rcert, "--json",
                                     os.path.join(out, "check.json")], capture_output=True, text=True)
                rec["check"] = {"rc": ch.returncode, "verdict": ch.stdout.strip().split("\n")[-1],
                                "checker_sha256": sha(os.path.join(CODE, "pc_check.py"))}
                ok = ok and rec["cert_byte_identical"] and ch.returncode == 0
        rec["run_log_tail"] = open(os.path.join(out, "replay.log")).read().strip().split("\n")[-2:]
    rec["status"] = "REPLAY_PASS" if ok else "REPLAY_FAIL"
    rec["finished_at_pt"] = datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()
    with open(os.path.join(out, "receipt.json"), "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print(json.dumps({k: rec.get(k) for k in ["status", "seed_byte_identical", "cert_byte_identical", "run_log_tail"]}))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
