#!/usr/bin/env python3
"""gram_certify.py: DRAT certification of Gram-support UNSAT instances with FIFO-streamed proofs (no proof file is
stored). Lane moqls7-maximum. Exactly two busy processes per instance (solver + drat-trim), instances sequential.

Instances:
  k2A:<idx>   encoder A (gram_enc.build(2, L_idx, heavy=True)), CaDiCaL proof
  k2B:<idx>   encoder B (gram_encB.py --squares 2 --net-L L_idx --heavy), kissat proof
  k3A         encoder A K3 (gram_enc.build(3, None, heavy=True, sym=True)), CaDiCaL proof
  k3B         encoder B K3 (gram_encB.py --squares 3 --heavy --sym), kissat proof
The CNF is written to explore/scratch/cert_current.cnf (scratch, reused) and its SHA-256 recorded.
drat-trim output is parsed after stripping carriage returns; only an exact 's VERIFIED' line counts.
Usage: gram_certify.py CLASSES.txt OUT.jsonl INSTANCE [INSTANCE ...]   (k2A:all / k2B:all expand to all classes)
"""
import hashlib
import json
import os
import subprocess
import sys
import time

import gram_enc
from k2_classes import square_from_key

HERE = os.path.dirname(os.path.abspath(__file__))
DRAT = os.path.join(HERE, "..", "env", "drat-trim", "drat-trim")
SCR = os.path.join(HERE, "..", "explore", "scratch")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def make_cnf(inst, rows, cnf):
    kind, _, arg = inst.partition(":")
    if kind in ("k2A", "k3A"):
        if kind == "k2A":
            F, _ = gram_enc.build(2, square_from_key(rows[int(arg)][0]), True, False, None)
        else:
            F, _ = gram_enc.build(3, None, True, True, None)
        with open(cnf, "w") as f:
            f.write(F.text())
        return ["cadical", "-q", cnf]
    if kind == "k2B":
        lj = os.path.join(SCR, "cert_L.json")
        with open(lj, "w") as f:
            json.dump(square_from_key(rows[int(arg)][0]), f)
        args = ["--squares", "2", "--net-L", lj, "--heavy"]
    else:
        args = ["--squares", "3", "--heavy", "--sym"]
    subprocess.run(["/usr/bin/python3", "-B", os.path.join(HERE, "gram_encB.py")] + args + ["--out", cnf],
                   check=True, capture_output=True)
    return ["kissat", "-q", cnf]


def certify(inst, rows):
    os.makedirs(SCR, exist_ok=True)
    cnf = os.path.join(SCR, "cert_current.cnf")
    fifo = os.path.join(SCR, "cert_proof.fifo")
    solver = make_cnf(inst, rows, cnf)
    h = sha(cnf)
    if os.path.exists(fifo):
        os.rename(fifo, os.path.join(SCR, "cert_proof.fifo.stale.%d" % int(time.time())))
    os.mkfifo(fifo)
    t0 = time.time()
    checker = subprocess.Popen([DRAT, cnf, fifo], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    sp = subprocess.Popen(solver + [fifo], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    sout, _ = sp.communicate()
    cout, _ = checker.communicate()
    lines = [l.strip() for l in cout.replace("\r", "\n").splitlines()]
    verified = "s VERIFIED" in lines and "s NOT VERIFIED" not in lines
    os.rename(fifo, os.path.join(SCR, "cert_proof.fifo.used.%d" % int(time.time())))
    return {"instance": inst, "cnf_sha256": h, "solver": solver[0], "solver_rc": sp.returncode,
            "drat_trim": "s VERIFIED" if verified else "NOT VERIFIED", "sec": round(time.time() - t0, 1),
            "drat_tail": [l for l in lines if l.startswith("s ") or "verified" in l.lower()][-3:]}


if __name__ == "__main__":
    rows = [l.split() for l in open(sys.argv[1]) if l.strip()]
    insts = []
    for a in sys.argv[3:]:
        if a.endswith(":all"):
            insts += ["%s:%d" % (a.split(":")[0], i) for i in range(len(rows))]
        else:
            insts.append(a)
    with open(sys.argv[2], "a") as out:
        for inst in insts:
            rec = certify(inst, rows)
            out.write(json.dumps(rec) + "\n")
            out.flush()
            print(json.dumps(rec), flush=True)
