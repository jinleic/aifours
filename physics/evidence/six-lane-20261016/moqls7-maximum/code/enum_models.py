#!/usr/bin/env python3
"""enum_models.py: enumerate the models of a pattern CNF projected on its support variables x (by blocking clauses),
up to a cap. Lane moqls7-maximum. Uses CaDiCaL on stdin (native -t limit; no Python-level timeouts).
Usage: enum_models.py CNF MAP.json --cap N --out F.json
"""
import argparse
import json
import subprocess


def solve(text, tl=600):
    p = subprocess.run(["cadical", "-q", "-t", str(tl)], input=text, capture_output=True, text=True)
    model = set()
    for line in p.stdout.splitlines():
        if line.startswith("v "):
            model |= {int(t) for t in line.split()[1:] if int(t) > 0}
    return p.returncode, model


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cnf")
    ap.add_argument("map")
    ap.add_argument("--cap", type=int, default=1000)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    lines = open(a.cnf).read().splitlines()
    head = lines[0].split()
    nv, nc = int(head[2]), int(head[3])
    body = "\n".join(lines[1:]) + "\n"
    xmap = json.load(open(a.map))["x"]
    xvars = sorted(xmap.values())
    inv = {v: k for k, v in xmap.items()}
    blocks = []
    models = []
    status = "cap"
    while len(models) < a.cap:
        text = "p cnf %d %d\n" % (nv, nc + len(blocks)) + body + "".join(" ".join(map(str, b)) + " 0\n" for b in blocks)
        st, m = solve(text)
        if st == 20:
            status = "complete"
            break
        if st != 10:
            status = "solver status %d" % st
            break
        sup = sorted(inv[v] for v in xvars if v in m)
        models.append(sup)
        blocks.append([-v if v in m else v for v in xvars])
    json.dump({"status": status, "n_models": len(models), "models": models}, open(a.out, "w"))
    print(json.dumps({"status": status, "n_models": len(models)}))
