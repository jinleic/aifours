#!/usr/bin/env python3
"""drat_pipeline.py -- run kissat with a binary DRAT proof streamed through a FIFO into zstd (lane btd12-15).

kissat writes its binary DRAT proof into OUTPREFIX.drat.fifo (a named pipe created here); `zstd -q -T1 -3` reads the
pipe and writes OUTPREFIX.drat.zst.  This keeps the proof on disk compressed.  The proof is later checked with
`zstd -dc OUTPREFIX.drat.zst | drat-trim CNF -i -t SECONDS` (proof read from stdin in forced binary mode).
kissat runs with its native --time limit; nothing is killed, no subprocess timeouts, nothing deleted or overwritten
(all outputs are created exclusively; the FIFO stays in place as an empty special file).
Usage: drat_pipeline.py CNF SECONDS OUTPREFIX [extra kissat options ...]
Writes OUTPREFIX.stdout (kissat log), OUTPREFIX.drat.zst, OUTPREFIX.json (receipt).  Exit 20 UNSAT, 10 SAT, 0 other.
"""
import hashlib
import json
import os
import subprocess
import sys
import time

KISSAT = "/opt/homebrew/bin/kissat"
ZSTD = "/opt/homebrew/bin/zstd"


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 22), b""):
            h.update(chunk)
    return h.hexdigest()


def main(argv):
    if len(argv) < 4:
        print(__doc__, file=sys.stderr)
        return 2
    cnf, secs, pre = argv[1], int(argv[2]), argv[3]
    extra = argv[4:]
    fifo, zst = pre + ".drat.fifo", pre + ".drat.zst"
    for p in (fifo, zst, pre + ".stdout", pre + ".json"):
        if os.path.exists(p):
            raise SystemExit(f"exists: {p}")
    os.mkfifo(fifo)
    zout = open(zst, "xb")
    t0 = time.time()
    zp = subprocess.Popen([ZSTD, "-q", "-T1", "-3", "-c", fifo], stdout=zout)
    cmd = [KISSAT, f"--time={secs}"] + extra + [cnf, fifo]
    with open(pre + ".stdout", "x") as so:
        kp = subprocess.Popen(cmd, stdout=so, stderr=subprocess.STDOUT)
        krc = kp.wait()
    zrc = zp.wait()
    zout.close()
    t1 = time.time()
    text = open(pre + ".stdout").read()
    status = "UNKNOWN"
    for line in text.split("\n"):
        if line.startswith("s "):
            status = {"SATISFIABLE": "SAT", "UNSATISFIABLE": "UNSAT"}.get(line[2:].strip(), "UNKNOWN")
    rec = {"program": "drat_pipeline.py", "script_sha256": sha(os.path.abspath(__file__)),
           "kissat_command": cmd, "kissat_returncode": krc, "zstd_command": [ZSTD, "-q", "-T1", "-3", "-c", fifo],
           "zstd_returncode": zrc, "status": status, "cnf": cnf, "cnf_sha256": sha(cnf),
           "proof_zst": zst, "proof_zst_bytes": os.path.getsize(zst), "proof_zst_sha256": sha(zst),
           "started_host": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(t0)),
           "ended_host": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(t1)), "wall_s": round(t1 - t0, 3)}
    with open(pre + ".json", "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print(json.dumps({k: rec[k] for k in ("status", "wall_s", "proof_zst_bytes")}))
    return {"UNSAT": 20, "SAT": 10}.get(status, 0)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
