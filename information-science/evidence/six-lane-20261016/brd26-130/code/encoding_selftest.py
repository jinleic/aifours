#!/usr/bin/env python3
"""encoding_selftest.py -- completeness self-test of code/brd_cnf.py on a known valid matrix (README 1.6).

Given a CNF + map from code/brd_cnf.py and a strict-format BRD file whose matrix satisfies the model's invariance,
this appends unit clauses fixing every orbit variable (A, S) to the values read from the matrix and runs kissat.  A
correct encoding must return SAT (the auxiliary counter/Tseitin variables are then forced).  A cell whose orbit is
forced to zero, or two cells of one orbit with values that do not match their relative parity, make the test FAIL
before the solver is called (the matrix is not invariant under the model).
Usage: encoding_selftest.py CNF BRDFILE OUTPREFIX     writes OUTPREFIX.cnf (exclusive), OUTPREFIX.json (exclusive).
Exit 0 iff SAT.
"""
import hashlib
import json
import subprocess
import sys

KISSAT = "/opt/homebrew/bin/kissat"


def main(argv):
    if len(argv) != 4:
        print(__doc__, file=sys.stderr)
        return 2
    cnf, brd, pre = argv[1], argv[2], argv[3]
    mp = json.load(open(cnf + ".map.json"))
    v, b = mp["params"][0], mp["params"][1]
    lines = open(brd).read().split("\n")
    rows = [[int(t) for t in ln.split(" ")] for ln in lines[1:1 + v]]
    units, ok, why = {}, True, ""
    for i in range(v):
        for j in range(b):
            c = mp["cells"][i * b + j]
            x = rows[i][j]
            if c == 0:
                if x != 0:
                    ok, why = False, f"cell ({i},{j}) forced zero but matrix has {x}"
                continue
            a, s, p = c
            want_a = 1 if x != 0 else 0
            if units.get(a, want_a) != want_a:
                ok, why = False, f"orbit A var {a} inconsistent at ({i},{j})"
            units[a] = want_a
            if x != 0 and s is not None:
                pos = 1 if x == 1 else 0
                sval = pos ^ p
                if units.get(s, sval) != sval:
                    ok, why = False, f"orbit S var {s} inconsistent at ({i},{j})"
                units[s] = sval
    rec = {"cnf": cnf, "cnf_sha256": hashlib.sha256(open(cnf, "rb").read()).hexdigest(), "brd": brd,
           "brd_sha256": hashlib.sha256(open(brd, "rb").read()).hexdigest(), "units": len(units)}
    if not ok:
        rec.update({"status": "NOT-INVARIANT", "detail": why})
    else:
        text = open(cnf).read().split("\n", 1)
        nv, nc = (int(t) for t in text[0].split()[2:4])
        with open(pre + ".cnf", "x") as f:
            f.write(f"p cnf {nv} {nc + len(units)}\n")
            f.write(text[1])
            for var, val in sorted(units.items()):
                f.write(f"{var if val else -var} 0\n")
        p = subprocess.run([KISSAT, "--time=300", "-q", pre + ".cnf"], capture_output=True, text=True)
        st = "SAT" if p.returncode == 10 else ("UNSAT" if p.returncode == 20 else "UNKNOWN")
        rec.update({"status": st, "kissat_rc": p.returncode})
    with open(pre + ".json", "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print(json.dumps(rec))
    return 0 if rec["status"] == "SAT" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
