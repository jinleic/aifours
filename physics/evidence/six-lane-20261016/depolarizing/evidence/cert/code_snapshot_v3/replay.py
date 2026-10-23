"""Replay sectors with the SAME cert.py and compare every recorded field bitwise (detects altered records).

python replay.py WITNESS.json PART*.sectors.jsonl --ptail 1e-13 --pitail 1e-40 --sectors 1452,1460 | --random 3 --seed 0
Exit 0 = all replayed sectors identical; exit 2 = "REJECT replay_mismatch" (or a combine-level rejection).
"""
from __future__ import annotations

import argparse
import io
import json
import random

import cert

FIELDS = ("N", "lo", "hi", "ic_trunc", "eps_tail", "w_tail", "relE", "smin", "nsteps", "D", "pN",
          "witness_sha256", "cert_py_sha256", "dd_py_sha256", "M", "p", "D_param", "ptail", "pitail")


def replay(w, parts, ptail, pitail, sectors):
    recs = {}
    for f in parts:
        for line in open(f):
            if line.strip():
                r = json.loads(line)
                recs[r["N"]] = r
    out = []
    for N in sectors:
        buf = io.StringIO()
        cert.certify(w, {N}, ptail, pitail, False, buf)
        new = json.loads(buf.getvalue().strip().splitlines()[-1])
        old = recs.get(N)
        diff = [k for k in FIELDS if old is None or old.get(k) != new.get(k)]
        out.append({"N": N, "identical": not diff, "diff_fields": diff})
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("witness")
    ap.add_argument("parts", nargs="+")
    ap.add_argument("--ptail", type=float, required=True)
    ap.add_argument("--pitail", type=float, required=True)
    ap.add_argument("--sectors", default=None)
    ap.add_argument("--random", type=int, default=0)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    w = json.load(open(a.witness))
    ns = [int(x) for x in a.sectors.split(",")] if a.sectors else []
    if a.random:
        allN = sorted({json.loads(l)["N"] for f in a.parts for l in open(f) if l.strip()})
        ns += random.Random(a.seed).sample(allN, a.random)
    res = replay(w, a.parts, a.ptail, a.pitail, ns)
    print(json.dumps(res))
    if not all(r["identical"] for r in res):
        print("REJECT replay_mismatch:", [r for r in res if not r["identical"]])
        raise SystemExit(2)
