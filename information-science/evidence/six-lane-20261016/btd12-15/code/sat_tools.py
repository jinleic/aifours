#!/usr/bin/env python3
"""sat_tools.py -- run a SAT solver on a BTD CNF (encoding A or B) and decode, or enumerate all solutions on tiny
instances (lane btd12-15, README 1.6).  Stdlib only.  Solvers run with their own native time limits; this script
never kills anything and never uses subprocess timeouts.  All outputs are created exclusively.

The CNF's companion OUT.cnf.map.json must give, for each cell (i, j), the primary variables in one of two forms:
  {"a": [[...]], "b": [[...]]}            thermometer (encoding A): m = a + b
  {"z1": [[...]], "z2": [[...]]}          one-hot (encoding B): m = 1 if z1, 2 if z2, else 0
Commands:
  run CNF SOLVER SECONDS OUTPREFIX [--proof PROOFFILE] [--lrat]
      SOLVER in {kissat, cadical}; writes OUTPREFIX.stdout, OUTPREFIX.json and, when SAT, OUTPREFIX.btd (strict
      format) checked by verify_btd.py.  Exit 10 SAT, 20 UNSAT, 0 unknown.
  enum CNF OUTDIR CAP
      repeatedly solves with cadical (60 s native limit per call) adding a blocking clause over the primary variables
      after each solution; OUTDIR fresh; writes OUTDIR/enum.json with the count (or "cap reached").
"""
import hashlib
import json
import os
import subprocess
import sys
import time

CODE = os.path.dirname(os.path.abspath(__file__))
SOLVERS = {"kissat": "/opt/homebrew/bin/kissat", "cadical": "/opt/homebrew/bin/cadical"}


def load_map(cnf):
    mp = json.load(open(cnf + ".map.json"))
    params = mp["params"]
    V, B = params[0], params[1]
    if "a" in mp:
        cells = [[("A", mp["a"][i][j], mp["b"][i][j]) for j in range(B)] for i in range(V)]
    else:
        cells = [[("B", mp["z1"][i][j], mp["z2"][i][j]) for j in range(B)] for i in range(V)]
    return mp, params, cells


def decode(model, cells):
    def val(v):
        return model.get(v, False)
    rows = []
    for row in cells:
        r = []
        for kind, u, w in row:
            if kind == "A":
                x = int(val(u)) + int(val(w))
                if val(w) and not val(u):
                    raise ValueError("thermometer violated")
            else:
                if val(u) and val(w):
                    raise ValueError("one-hot violated")
                x = 1 if val(u) else (2 if val(w) else 0)
            r.append(x)
        rows.append(r)
    return rows


def parse_output(text):
    status, model = "UNKNOWN", {}
    for line in text.split("\n"):
        if line.startswith("s "):
            s = line[2:].strip()
            status = {"SATISFIABLE": "SAT", "UNSATISFIABLE": "UNSAT"}.get(s, "UNKNOWN")
        elif line.startswith("v "):
            for t in line[2:].split():
                x = int(t)
                if x != 0:
                    model[abs(x)] = x > 0
    return status, model


def solver_cmd(solver, cnf, secs, proof=None, lrat=False):
    if solver == "kissat":
        cmd = [SOLVERS["kissat"], f"--time={int(secs)}", cnf]
        if proof:
            cmd.append(proof)
    else:
        cmd = [SOLVERS["cadical"], "-t", str(int(secs)), cnf]
        if proof:
            if lrat:
                cmd.insert(1, "--lrat")
            cmd.append(proof)
    return cmd


def cert_text(params, rows):
    return "BTD " + " ".join(map(str, params)) + "\n" + "".join(" ".join(map(str, r)) + "\n" for r in rows)


def cmd_run(args):
    cnf, solver, secs, pre = args[0], args[1], float(args[2]), args[3]
    proof, lrat = None, False
    rest = args[4:]
    while rest:
        o = rest.pop(0)
        if o == "--proof":
            proof = rest.pop(0)
        elif o == "--lrat":
            lrat = True
        else:
            raise SystemExit(f"bad option {o}")
    if proof and os.path.exists(proof):
        raise SystemExit("proof file exists")
    mp, params, cells = load_map(cnf)
    cmd = solver_cmd(solver, cnf, secs, proof, lrat)
    t0 = time.time()
    with open(pre + ".stdout", "x") as so:
        p = subprocess.run(cmd, stdout=so, stderr=subprocess.STDOUT)
    el = time.time() - t0
    text = open(pre + ".stdout").read()
    status, model = parse_output(text)
    rec = {"command": cmd, "returncode": p.returncode, "status": status, "wall_s": round(el, 3),
           "cnf": cnf, "cnf_sha256": hashlib.sha256(open(cnf, "rb").read()).hexdigest(),
           "map_sha256": hashlib.sha256(open(cnf + ".map.json", "rb").read()).hexdigest(),
           "params": params, "proof": proof, "lrat": lrat,
           "started_host": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(t0)),
           "ended_host": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(t0 + el))}
    rc = 0
    if status == "SAT":
        rows = decode(model, cells)
        content = cert_text(params, rows)
        with open(pre + ".btd", "x") as f:
            f.write(content)
        rec["witness_sha256"] = hashlib.sha256(content.encode()).hexdigest()
        v = subprocess.run([sys.executable, os.path.join(CODE, "verify_btd.py"), pre + ".btd"],
                           capture_output=True, text=True)
        rec["verify_btd"] = v.stdout.strip().split("\n")[-1]
        rc = 10
    elif status == "UNSAT":
        rc = 20
    if proof and os.path.exists(proof):
        rec["proof_bytes"] = os.path.getsize(proof)
    with open(pre + ".json", "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print(json.dumps({k: rec[k] for k in ("status", "wall_s", "params") if k in rec}
                     | ({"verify_btd": rec["verify_btd"]} if "verify_btd" in rec else {})))
    return rc


def cmd_enum(args):
    cnf, outdir, cap = args[0], args[1], int(args[2])
    os.makedirs(outdir)
    mp, params, cells = load_map(cnf)
    prim = sorted({v for row in cells for (_, u, w) in row for v in (u, w)})
    header, body = None, []
    for line in open(cnf):
        if line.startswith("p cnf"):
            header = line.split()
        elif line.startswith("c") or not line.strip():
            continue
        else:
            body.append(line)
    nv = int(header[2])
    blocks, sols = [], []
    k = 0
    while True:
        path = os.path.join(outdir, f"iter{k:04d}.cnf")
        with open(path, "x") as f:
            f.write(f"p cnf {nv} {len(body) + len(blocks)}\n")
            f.writelines(body)
            f.writelines(blocks)
        p = subprocess.run([SOLVERS["cadical"], "-t", "60", path], capture_output=True, text=True)
        status, model = parse_output(p.stdout)
        if status == "UNSAT":
            break
        if status != "SAT":
            sols = None
            break
        rows = decode(model, cells)
        sols.append(rows)
        blocks.append(" ".join(str(-v if model.get(v, False) else v) for v in prim) + " 0\n")
        k += 1
        if k >= cap:
            break
    res = {"cnf": cnf, "cnf_sha256": hashlib.sha256(open(cnf, "rb").read()).hexdigest(), "params": params,
           "count": len(sols) if sols is not None else None, "complete": sols is not None and k < cap,
           "solutions": [cert_text(params, r) for r in sols] if sols else []}
    with open(os.path.join(outdir, "enum.json"), "x") as f:
        json.dump(res, f, indent=1)
        f.write("\n")
    print(json.dumps({"cnf": cnf, "count": res["count"], "complete": res["complete"]}))
    return 0


def main(argv):
    if len(argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    if argv[1] == "run":
        return cmd_run(argv[2:])
    if argv[1] == "enum":
        return cmd_enum(argv[2:])
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
