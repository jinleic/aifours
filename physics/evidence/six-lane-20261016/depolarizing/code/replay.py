"""Replay sectors with the SAME cert.py and compare recorded fields (v3.1).

python replay.py WITNESS.json PART*.sectors.jsonl --ptail 1e-13 --pitail 1e-40 (--sectors N,N,... | --random k --seed s | --all)

v3.1 (Codex re-review fixes): the record set is first validated by combine.combine() (named rejections for
provenance, parameters, duplicates, missing/extra sectors, malformed records); an empty selection is rejected;
--all replays every record (complete verification), otherwise the output states "sampled".
Comparison = exact equality of the decoded JSON values of FIELDS (Python ==, so +0.0 == -0.0); elapsed time
("secs") is excluded. It is not a byte-level comparison of the files.
Exit 0 = validated and all replayed sectors equal; exit 2 = REJECT <reason>.
"""
from __future__ import annotations

import argparse
import io
import json
import random

import cert
from combine import Reject, combine

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
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    w = json.load(open(a.witness))
    try:
        combine(w, a.parts, a.ptail, a.pitail)            # full structural validation first
    except Reject as e:
        print(str(e))
        raise SystemExit(2)
    allN = sorted({json.loads(l)["N"] for f in a.parts for l in open(f) if l.strip()})
    ns = [int(x) for x in a.sectors.split(",")] if a.sectors else []
    if a.random:
        ns += random.Random(a.seed).sample(allN, a.random)
    if a.all:
        ns = allN
    if not ns:
        print("REJECT empty_selection: no sectors requested")
        raise SystemExit(2)
    res = replay(w, a.parts, a.ptail, a.pitail, ns)
    mode = "complete" if set(ns) >= set(allN) else "sampled"
    print(json.dumps({"mode": mode, "requested": len(ns), "records": len(allN), "results": res}))
    if not all(r["identical"] for r in res):
        print("REJECT replay_mismatch:", [r for r in res if not r["identical"]])
        raise SystemExit(2)
