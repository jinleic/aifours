#!/usr/bin/env python3
"""k1_certify.py: K1 pattern certification for all 7 classes of 4-nets of order 7 (encoder A = k1_sat.build with
families F1-F4 only: no weight-3 clause, no Hall clauses). Lane moqls7-maximum.

For each class: enumerate all models projected on the support variables x by blocking clauses (CaDiCaL), then
write the final CNF (base + one blocking clause per model), prove it UNSAT with a text DRAT proof from CaDiCaL,
and check the proof with the lane-local drat-trim. Output: OUTDIR/c{idx}.final.cnf, c{idx}.drat, summary.json.
Usage: k1_certify.py CLASSFILE OUTDIR
"""
import hashlib
import json
import os
import subprocess
import sys

import k1_sat

HERE = os.path.dirname(os.path.abspath(__file__))
DRAT_TRIM = os.path.join(HERE, "..", "env", "drat-trim", "drat-trim")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def cnf_text(F, extra):
    return "p cnf %d %d\n" % (F.nv, len(F.cl) + len(extra)) + \
        "".join(" ".join(map(str, c)) + " 0\n" for c in F.cl + extra)


def solve(text):
    p = subprocess.run(["cadical", "-q"], input=text, capture_output=True, text=True)
    model = set()
    for line in p.stdout.splitlines():
        if line.startswith("v "):
            model |= {int(t) for t in line.split()[1:] if int(t) > 0}
    return p.returncode, model


def main(classfile, outdir):
    os.makedirs(outdir, exist_ok=True)
    data = json.load(open(classfile))
    summary = {"classfile": os.path.relpath(classfile, outdir), "classfile_sha256": sha(classfile),
               "encoder": "k1_sat.build(w3=False, hall=False)", "k1_sat_sha256": sha(os.path.join(HERE, "k1_sat.py")),
               "drat_trim_sha256": sha(DRAT_TRIM), "classes": []}
    for idx, cls in enumerate(data["classes"]):
        net = [tuple(q) for q in cls["net"]]
        F, vmap, A = k1_sat.build(net, w3=False, hall=False)
        inv = {v: k for k, v in vmap.items()}
        xvars = sorted(vmap.values())
        blocks, models = [], []
        while True:
            st, m = solve(cnf_text(F, blocks))
            if st == 20:
                break
            assert st == 10, st
            models.append(sorted(inv[v] for v in xvars if v in m))
            blocks.append([-v if v in m else v for v in xvars])
        cnf = os.path.join(outdir, "c%d.final.cnf" % idx)
        prf = os.path.join(outdir, "c%d.drat" % idx)
        open(cnf, "w").write(cnf_text(F, blocks))
        p = subprocess.run(["cadical", "-q", "--binary=false", cnf, prf], capture_output=True, text=True)
        assert p.returncode == 20, p.returncode
        d = subprocess.run([DRAT_TRIM, cnf, prf], capture_output=True, text=True)
        lines = [l.strip() for l in d.stdout.replace("\r", "\n").splitlines()]
        verified = "s VERIFIED" in lines and "s NOT VERIFIED" not in lines
        weights = []
        for mdl in models:
            w = {}
            for s in mdl:
                pnt, _ = s.split(":")
                w[pnt] = w.get(pnt, 0) + 1
            weights.append(sorted(set(w.values())))
        rec = {"class": idx, "origin": cls["origin"], "par": cls["par"], "maximal": cls["maximal"],
               "n_models": len(models), "model_weight_sets": weights, "models": models,
               "final_cnf": os.path.basename(cnf), "final_cnf_sha256": sha(cnf),
               "drat": os.path.basename(prf), "drat_sha256": sha(prf), "drat_bytes": os.path.getsize(prf),
               "drat_trim": "s VERIFIED" if verified else "NOT VERIFIED"}
        summary["classes"].append(rec)
        print(json.dumps({k: rec[k] for k in ("class", "origin", "maximal", "n_models", "model_weight_sets",
                                              "drat_trim", "drat_bytes")}), flush=True)
    json.dump(summary, open(os.path.join(outdir, "summary.json"), "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
