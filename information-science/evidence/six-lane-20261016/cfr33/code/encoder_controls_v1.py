#!/usr/bin/env python3
"""Encoder + DRAT-gate controls for the CFR(5,27) sub-lane (lane cfr33).  Usage: encoder_controls_v1.py OUTDIR
OUTDIR is created (must not exist). Quick controls only (each solver call <= 120 s native limit):
 D1 CFR(3,9) M0 UNSAT + DRAT verified; D2 CFR(2,6) M0 UNSAT + DRAT verified;
 D3 SAT CNF CFR(4,5) + empty-clause proof must NOT verify; D4 truncated CFR(3,9) proof must NOT verify.
 P1-P3 planted Kirtchakov CFR(5,25) in M0 / odd (mu=24) / <7> (mu=7) -> SAT, decoded file byte-identical to pinned rows,
 both checkers PASS.  P4 one-swap mutated plant (f_4 values at x=1,2 swapped) in M0 -> UNSAT.
Writes OUTDIR/results.json; exit 1 if any expectation fails.
"""
import hashlib, json, os, subprocess, sys

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = lambda *a: os.path.join(LANE, "code", *a)


def sh(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def wspec(path, d):
    with open(path, "x") as fh:
        json.dump(d, fh, sort_keys=True)


def drat_verified(cnf, proof):
    rc, out = sh([os.path.join(LANE, "bin", "drat-trim"), cnf, proof])
    lines = [ln.strip().replace("\r", "") for ln in out.replace("\r", "\n").split("\n")]
    return ("s VERIFIED" in lines), rc, [ln for ln in lines if ln.startswith("s ")]


def main():
    out = sys.argv[1]
    os.mkdir(out)
    res, ok = [], True

    def enc(name, d):
        sp = os.path.join(out, name + ".spec.json")
        wspec(sp, d)
        rc, o = sh(["python3", C("cfr_cnf.py"), sp, os.path.join(out, name)])
        assert rc == 0, o
        return os.path.join(out, name + ".cnf"), os.path.join(out, name + ".map.json"), json.loads(o.strip().splitlines()[-1])

    def solve(name, cnf, proof=None):
        args = ["python3", C("run_solver.py"), os.path.join(out, name + "-run"), cnf, "kissat", "1", "120"]
        if proof:
            args.append(proof)
        rc, o = sh(args)
        return json.load(open(os.path.join(out, name + "-run", "record.json")))

    # D1, D2
    for name, d in (("D1-cfr3-9", {"n": 9, "r": 3}), ("D2-cfr2-6", {"n": 6, "r": 2})):
        cnf, mp, info = enc(name, d)
        proof = os.path.join(out, name + ".drat")
        rec = solve(name, cnf, proof)
        v, rc, sl = drat_verified(cnf, proof)
        good = rec["verdict"].startswith("UNSAT") and v
        ok &= good
        res.append({"control": name, "expect": "UNSAT + DRAT s VERIFIED", "verdict": rec["verdict"], "drat_s_lines": sl,
                    "cnf_sha256": info["cnf_sha256"], "proof_sha256": hashlib.sha256(open(proof, "rb").read()).hexdigest(),
                    "proof_bytes": os.path.getsize(proof), "as_expected": good})
    # D3 SAT CNF + empty clause proof
    cnf, mp, info = enc("D3-cfr4-5", {"n": 5, "r": 4})
    fake = os.path.join(out, "D3-empty-clause.drat")
    with open(fake, "x") as fh:
        fh.write("0\n")
    v, rc, sl = drat_verified(cnf, fake)
    good = not v
    ok &= good
    res.append({"control": "D3 SAT CNF CFR(4,5) + empty-clause proof", "expect": "NOT verified", "drat_s_lines": sl, "as_expected": good})
    # D4 truncated proof
    full = os.path.join(out, "D1-cfr3-9.drat")
    data = open(full, "rb").read()
    trunc = os.path.join(out, "D4-truncated.drat")
    with open(trunc, "xb") as fh:
        fh.write(data[: len(data) // 3])
    v, rc, sl = drat_verified(os.path.join(out, "D1-cfr3-9.cnf"), trunc)
    good = not v
    ok &= good
    res.append({"control": "D4 CFR(3,9) proof truncated to 1/3", "expect": "NOT verified", "drat_s_lines": sl, "as_expected": good})
    # Planted Kirtchakov
    pinned = os.path.join(LANE, "controls", "kirtchakov-cfr-5-25.raw")
    rows = [list(map(int, ln.split())) for ln in open(pinned).read().split("\n")[:-1]]
    n = 25
    P = []
    for R in rows:
        p = [None] * n
        for c, s in enumerate(R):
            p[s] = c
        P.append(p)
    units = [[j, x, P[j][x]] for j in range(1, 5) for x in range(1, n)]
    for name, rels in (("P1-plant-M0", []), ("P2-plant-odd", [{"mu": 24, "sigma": [1, 2, 3, 4]}]),
                       ("P3-plant-mu7", [{"mu": 7, "sigma": [1, 2, 3, 4]}])):
        cnf, mp, info = enc(name, {"n": 25, "r": 5, "relations": rels, "units": units})
        rec = solve(name, cnf)
        raw = os.path.join(out, name + ".raw")
        good = rec["verdict"] == "SAT"
        if good:
            sh(["python3", C("cfr_decode.py"), mp, os.path.join(out, name + "-run", "solver.out"), raw])
            same = open(raw, "rb").read() == open(pinned, "rb").read()
            ca = sh(["python3", C("cfr_check_events.py"), raw, "5", "25"])[0] == 0
            cb = sh(["python3", C("cfr_check_posdiff.py"), raw, "5", "25"])[0] == 0
            good = same and ca and cb
        ok &= good
        res.append({"control": name, "expect": "SAT, decoded == pinned, A+B PASS", "verdict": rec["verdict"],
                    "cnf_sha256": info["cnf_sha256"], "vars": info["vars"], "clauses": info["clauses"], "as_expected": good})
    mut = [list(u) for u in units]
    i1 = mut.index([4, 1, P[4][1]]); i2 = mut.index([4, 2, P[4][2]])
    mut[i1][2], mut[i2][2] = P[4][2], P[4][1]
    cnf, mp, info = enc("P4-plant-mutated-M0", {"n": 25, "r": 5, "units": mut})
    rec = solve("P4-plant-mutated-M0", cnf)
    good = rec["verdict"].startswith("UNSAT")
    ok &= good
    res.append({"control": "P4 plant with f_4(1), f_4(2) swapped, M0", "expect": "UNSAT", "verdict": rec["verdict"], "as_expected": good})
    with open(os.path.join(out, "results.json"), "x") as fh:
        json.dump({"all_as_expected": ok, "results": res}, fh, indent=1)
    print("ALL_AS_EXPECTED" if ok else "SOME_UNEXPECTED")
    for r_ in res:
        print(r_)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
