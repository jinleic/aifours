"""Parent item (5): a control that exercises (P4) in the production --squares path with three quantum squares: keep
(P4) ON (--p4 123) and relax another family so that a SAT instance exists; check that the model satisfies every
clause and that the decoded supports of EACH quantum square contain an entry of weight >= 3 (row-0 frame, i >= 1).
Relaxations tried in order (all attempts recorded): R1 (P3) off (--no-p3) on the AG pair; R2 only ONE classical
square (the AG slope-1 square), (P3) on; R3 no classical square, (P3) on. Both encoders (A8r2/CaDiCaL, B8r2/kissat).
Fail-closed: exit 1 unless, for each encoder, some relaxation is SAT with a fully satisfying model whose decoded
quantum squares all carry a weight->=3 entry.
python -B p4_on_control_k3.py --outdir ../evidence/k3_fixed/p4on_ctrl_v1
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from enc8_a2 import gmul  # noqa: E402

N = 8


def read_cnf(path):
    with open(path) as fh:
        header = fh.readline().split()
        return int(header[2]), [[int(t) for t in line.split()][:-1] for line in fh]


def solve(solver, path):
    cmd = ["cadical", "-q", "-t", "1200", path] if solver == "cadical" else ["kissat", "-q", "--time=1200", path]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.returncode, {int(t) for l in r.stdout.splitlines() if l.startswith("v ") for t in l.split()[1:] if t != "0"}


def decode_supports(enc, mapfile, model):
    """returns {s: {(i,j): set(k)}} for quantum labels 1..3, cells with i >= 1."""
    sup = {1: {}, 2: {}, 3: {}}
    tab = json.load(open(mapfile))
    items = tab["vars"].items() if enc == "a" else tab.items()
    for key, v in items:
        k = json.loads(key)
        if enc == "a":
            if not (isinstance(k[0], str) and k[0] in ("S1", "S2", "S3")):
                continue
            s, (i, j), coord = int(k[0][1]), k[1], k[2]
        else:
            if k[0] != "S" or k[1] not in (1, 2, 3):
                continue
            s, i, j, coord = k[1], k[2], k[3], k[4]
        if v in model:
            sup[s].setdefault((i, j), set()).add(coord)
    return sup


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", required=True)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=False)
    ag = {sl: [[j ^ gmul(sl, i) for j in range(N)] for i in range(N)] for sl in (1, 2)}
    relax = [("R1_noP3_AGpair", [ag[1], ag[2]], ["--no-p3"]), ("R2_one_classical", [ag[1]], []),
             ("R3_no_classical", [], [])]
    res = {"argv": sys.argv, "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "attempts": [], "ok": {}}
    for enc, solver in (("a", "cadical"), ("b", "kissat")):
        res["ok"][enc] = False
        for tag, squares, extra in relax:
            sqp = os.path.join(a.outdir, "%s.squares.json" % tag)
            if not os.path.exists(sqp):
                with open(sqp, "x") as fh:
                    json.dump(squares, fh)
            cnf = os.path.join(a.outdir, "%s_%s.cnf" % (enc, tag))
            mode = ["--mode", "fixed", "--slopes", ""] + (["--squares", sqp] if squares else [])
            cmd = [sys.executable, "-B", os.path.join(HERE, "enc8_%s2.py" % enc)] + mode + \
                ["--quantum", "123", "--p4", "123", "--cnf", cnf] + extra
            if enc == "a":
                cmd += ["--map", cnf + ".map.json"]
            r = subprocess.run(cmd, capture_output=True, text=True)
            rec = {"encoder": enc, "relaxation": tag, "encode_exit": r.returncode, "stderr": r.stderr[-300:]}
            if r.returncode == 0:
                nv, clauses = read_cnf(cnf)
                rc, model = solve(solver, cnf)
                rec.update({"cnf_sha256": hashlib.sha256(open(cnf, "rb").read()).hexdigest(), "exit": rc})
                if rc == 10:
                    full = all(any(l in model for l in cl) for cl in clauses)
                    sup = decode_supports(enc, cnf + ".map.json", model)
                    w3 = {s: any(len(v) >= 3 for (i, j), v in sup[s].items() if i >= 1) for s in (1, 2, 3)}
                    rec.update({"model_satisfies_all": full, "weight3_each_quantum": w3,
                                "max_weight": {s: max((len(v) for v in sup[s].values()), default=0) for s in (1, 2, 3)}})
                    if full and all(w3.values()):
                        res["ok"][enc] = True
            res["attempts"].append(rec)
            print(json.dumps({k: rec.get(k) for k in ("encoder", "relaxation", "exit", "model_satisfies_all",
                                                      "weight3_each_quantum", "max_weight")}), flush=True)
            if res["ok"][enc]:
                break
    with open(os.path.join(a.outdir, "RECEIPT.json"), "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({"ok": res["ok"]}))
    if not all(res["ok"].values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
