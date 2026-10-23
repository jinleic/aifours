#!/usr/bin/env python3
"""encoding_fix_controls.py -- realistic-size controls for CNF encodings A and B (README 1.6).

For each published BTD (strict-format files from controls/checkers-v1): bring it to double-lex form (S1) by
alternately sorting rows and columns lexicographically until both are sorted (each sort does not increase the
row-major flattening, so this terminates), check S1 directly, then for each encoding:
  fix  : all cells fixed by unit clauses -> must be SAT and decode to the same matrix (passing verify_btd.py);
  flip : the same with one entry changed (row-count preserving is not required; any change must be UNSAT) -> UNSAT.
Solver: cadical with a native 300 s limit per call.  OUTDIR is fresh; nothing is deleted or overwritten.
Usage: encoding_fix_controls.py OUTDIR CERT [CERT ...]
"""
import hashlib
import json
import os
import subprocess
import sys

CODE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(CODE)


def read(path):
    lines = open(path).read().split("\n")
    params = tuple(int(x) for x in lines[0].split()[1:])
    rows = [[int(t) for t in lines[1 + i].split(" ")] for i in range(params[0])]
    return params, rows


def double_lex(rows):
    M = [list(r) for r in rows]
    while True:
        M2 = sorted(M)
        cols = sorted(zip(*M2))
        M3 = [list(r) for r in zip(*cols)]
        if M3 == M:
            return M
        M = M3


def is_s1(M):
    cols = list(zip(*M))
    return all(M[i] <= M[i + 1] for i in range(len(M) - 1)) and all(cols[j] <= cols[j + 1] for j in range(len(cols) - 1))


def cert(params, rows):
    return "BTD " + " ".join(map(str, params)) + "\n" + "".join(" ".join(map(str, r)) + "\n" for r in rows)


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def solve(cnf, pre):
    p = run([sys.executable, os.path.join(CODE, "sat_tools.py"), "run", cnf, "cadical", "300", pre])
    return json.load(open(pre + ".json"))


def main(argv):
    if len(argv) < 3:
        print(__doc__, file=sys.stderr)
        return 2
    out = argv[1]
    os.makedirs(out)
    results, ok = [], True
    for src in argv[2:]:
        params, rows = read(src)
        name = os.path.basename(src)[:-4]
        M = double_lex(rows)
        assert is_s1(M)
        normp = os.path.join(out, name + ".s1.btd")
        with open(normp, "x") as f:
            f.write(cert(params, M))
        v = run([sys.executable, os.path.join(CODE, "verify_btd.py"), normp])
        assert v.stdout.strip().endswith("VALID"), v.stdout
        # a flip that changes one entry of row 1 (row 0 is fixed by S0 in both encodings anyway)
        fi, fj = 1, 0
        fv = (M[fi][fj] + 1) % 3
        for enc in ("A", "B"):
            for mode in ("fix", "flip"):
                cnf = os.path.join(out, f"{name}.{enc}.{mode}.cnf")
                extra = [] if mode == "fix" else (["--fix-flip", str(fi), str(fj), str(fv)] if enc == "A"
                                                  else ["-flip", str(fi), str(fj), str(fv)])
                if enc == "A":
                    g = run([sys.executable, os.path.join(CODE, "btd_cnf_a.py")] + [str(x) for x in params] +
                            [cnf, "--fix", normp] + extra)
                else:
                    g = run([os.path.join(LANE, "bin", "btd_cnf_b")] + [str(x) for x in params] + [cnf, "-fix", normp] + extra)
                assert g.returncode == 0, g.stderr
                rec = solve(cnf, cnf[:-4] + ".solve")
                want = "SAT" if mode == "fix" else "UNSAT"
                good = rec["status"] == want
                if mode == "fix" and good:
                    got = open(cnf[:-4] + ".solve.btd").read()
                    good = got == cert(params, M) and rec.get("verify_btd") == "VALID"
                ok &= good
                results.append({"source": src, "encoding": enc, "mode": mode, "flip": [fi, fj, fv] if mode == "flip" else None,
                                 "expected": want, "status": rec["status"], "wall_s": rec["wall_s"], "as_intended": good})
                print(f"{'ok ' if good else 'BAD'} {name} {enc} {mode}: want {want}, got {rec['status']} ({rec['wall_s']} s)")
    with open(os.path.join(out, "fix-controls.json"), "x") as f:
        json.dump({"script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                   "results": results, "all_as_intended": ok}, f, indent=1)
        f.write("\n")
    print("FIX-CONTROLS", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
