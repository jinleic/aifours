#!/usr/bin/env python3
"""brd_run.py -- run kissat (native --time) on a CNF from code/brd_cnf.py, decode, check (README 1.4).

Usage: brd_run.py CNF SECONDS PREFIX [--seed N]
Writes (exclusive) PREFIX.stdout (solver output), PREFIX.json (record) and, on SAT, PREFIX.brd (strict format) and
runs both lane checkers on it.  Exit 10 SAT (decoded), 20 UNSAT (no proof: information only), 0 UNKNOWN.
The solver is started as a direct child; nothing is killed by this driver (kissat stops at its own time limit;
an external SIGTERM to kissat leaves an UNKNOWN record).
"""
import hashlib
import json
import os
import subprocess
import sys
import time

CODE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(CODE)
KISSAT = "/opt/homebrew/bin/kissat"


def parse_output(path):
    status, model = "UNKNOWN", set()
    with open(path) as f:
        for line in f:
            if line.startswith("s "):
                if "UNSATISFIABLE" in line:
                    status = "UNSAT"
                elif "SATISFIABLE" in line:
                    status = "SAT"
            elif line.startswith("v "):
                for t in line.split()[1:]:
                    x = int(t)
                    if x > 0:
                        model.add(x)
    return status, model


def decode(cells, params, model):
    v, b = params[0], params[1]
    rows = []
    for i in range(v):
        row = []
        for j in range(b):
            c = cells[i * b + j]
            if c == 0 or c[0] not in model:
                row.append(0)
            else:
                pos = (c[1] in model) if c[1] is not None else True
                if c[2] == 1:
                    pos = not pos
                row.append(1 if pos else -1)
        rows.append(row)
    return rows


def cert_text(params, rows):
    return "BRD " + " ".join(map(str, params)) + "\n" + "".join(" ".join(map(str, r)) + "\n" for r in rows)


def main(argv):
    args = argv[1:]
    if len(args) < 3:
        print(__doc__, file=sys.stderr)
        return 2
    cnf, secs, pre = args[0], int(args[1]), args[2]
    seed = None
    if "--seed" in args[3:]:
        seed = int(args[args.index("--seed") + 1])
    mp = json.load(open(cnf + ".map.json"))
    params, cells = mp["params"], mp["cells"]
    cmd = [KISSAT, f"--time={secs}"] + ([f"--seed={seed}"] if seed is not None else []) + [cnf]
    t0 = time.time()
    with open(pre + ".stdout", "x") as so:
        p = subprocess.run(cmd, stdout=so, stderr=subprocess.STDOUT)
    el = time.time() - t0
    status, model = parse_output(pre + ".stdout")
    rec = {"command": cmd, "returncode": p.returncode, "status": status, "wall_s": round(el, 3), "cnf": cnf,
           "cnf_sha256": hashlib.sha256(open(cnf, "rb").read()).hexdigest(),
           "map_sha256": hashlib.sha256(open(cnf + ".map.json", "rb").read()).hexdigest(),
           "model": mp["model"], "spec_sha256": mp["spec_sha256"], "params": params,
           "started_host": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(t0)),
           "ended_host": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(t0 + el))}
    rc = 0
    if status == "SAT":
        rows = decode(cells, params, model)
        text = cert_text(params, rows)
        if mp.get("unsigned"):
            text = text.replace("BRD", "DESIGN", 1)
            with open(pre + ".design", "x") as f:
                f.write(text)
            rec["design_sha256"] = hashlib.sha256(text.encode()).hexdigest()
        else:
            with open(pre + ".brd", "x") as f:
                f.write(text)
            rec["witness_sha256"] = hashlib.sha256(text.encode()).hexdigest()
            a = subprocess.run([sys.executable, "-B", os.path.join(CODE, "verify_brd.py"), pre + ".brd",
                                "--expect"] + [str(x) for x in params], capture_output=True, text=True)
            c = subprocess.run([os.path.join(LANE, "bin", "brd_check"), pre + ".brd"] + [str(x) for x in params],
                               capture_output=True, text=True)
            rec["verify_brd"] = a.stdout.strip()
            rec["brd_check"] = c.stdout.strip()
        rc = 10
    elif status == "UNSAT":
        rc = 20
    with open(pre + ".json", "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print(json.dumps({k: rec[k] for k in ("model", "status", "wall_s") if k in rec}
                     | {k: rec[k][:60] for k in ("verify_brd", "brd_check") if k in rec}), flush=True)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))
