#!/usr/bin/env python3
"""lrat_soundness_tests.py: soundness negatives and positives for both LRAT checkers of lane ame46-support:
code/lratcheck (C, skips satisfied hints) and code/lratcheck_py.py (Python; tested in --allow-satisfied mode and in
strict mode). Requested by the parent after an upstream lrat-check was found to verify an empty clause on a
satisfiable CNF.

Cases (expected outcome):
 N1  sat CNF {1}, proof "2 0 0" (empty clause, no hints)                                  FAIL
 N2  sat CNF {1}, proof "2 0 1 0" (hint is unit, no conflict)                              FAIL
 N3  CNF {1 2, -1 2}, proof "3 0 1 0" (hint not unit / not RUP)                            FAIL
 N4  CNF {1, -1}, proof "3 0 9 0" (hint id out of range)                                   FAIL
 N5  CNF {1 2}, proof "2 -1 0 1 0" (only hint satisfied, no conflict; lemma not implied)   FAIL
 N6  CNF {1, -1}, proof "3 0 2 1 0" then nothing (hint 2 = {-1} unit, hint 1 = {1} conflict, i.e. a valid
     derivation of the empty clause), but with the hint list truncated to "3 0 2 0"           FAIL
 N7  CNF {1}, proof "2 1 0 0" then "3 0 0" (lemma {1} is a tautology-free copy; empty clause without hints) FAIL
 P1  CNF {1, -1}, proof "3 0 1 2 0"                                                        VERIFY
 P2  CNF {1 2, -1, -2}, proof "4 0 2 2 3 1 0" (second hint 2 is satisfied and skipped; real conflict at hint 1)
                                                                                           VERIFY (C, Python lenient)
                                                                                           FAIL   (Python strict)
Skipping a satisfied hint never sets the success flag: success requires a falsified hint (all literals false),
i.e. an actual conflict (lratcheck.c line "if (unassigned == 0) { ok = 1; ... }" after the satisfied test).
Writes evidence/lrat_soundness_tests.json; exit status 0 iff every outcome matches.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "explore", "lrat_tests")

CASES = [
    ("N1", "p cnf 1 1\n1 0\n", "2 0 0\n", {"C": False, "py": False, "py_strict": False}),
    ("N2", "p cnf 1 1\n1 0\n", "2 0 1 0\n", {"C": False, "py": False, "py_strict": False}),
    ("N3", "p cnf 2 2\n1 2 0\n-1 2 0\n", "3 0 1 0\n", {"C": False, "py": False, "py_strict": False}),
    ("N4", "p cnf 1 2\n1 0\n-1 0\n", "3 0 9 0\n", {"C": False, "py": False, "py_strict": False}),
    ("N5", "p cnf 2 1\n1 2 0\n", "2 -1 0 1 0\n", {"C": False, "py": False, "py_strict": False}),
    ("N6", "p cnf 1 2\n1 0\n-1 0\n", "3 0 2 0\n", {"C": False, "py": False, "py_strict": False}),
    ("N7", "p cnf 1 1\n1 0\n", "2 1 0 1 0\n3 0 0\n", {"C": False, "py": False, "py_strict": False}),
    ("P1", "p cnf 1 2\n1 0\n-1 0\n", "3 0 1 2 0\n", {"C": True, "py": True, "py_strict": True}),
    ("P2", "p cnf 2 3\n1 2 0\n-1 0\n-2 0\n", "4 0 2 2 3 1 0\n", {"C": True, "py": True, "py_strict": False}),
]


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    ok = r.returncode == 0 and "s VERIFIED" in r.stdout
    return ok, (r.stdout + r.stderr).strip().replace("\n", " | ")


def main():
    os.makedirs(OUT, exist_ok=True)
    res, allok = [], True
    for name, cnf, proof, want in CASES:
        cp, pp = os.path.join(OUT, name + ".cnf"), os.path.join(OUT, name + ".lrat")
        with open(cp, "w") as fh:
            fh.write(cnf)
        with open(pp, "w") as fh:
            fh.write(proof)
        got = {}
        got["C"], mc = run([os.path.join(HERE, "lratcheck"), cp, pp])
        got["py"], mp = run([sys.executable, "-B", os.path.join(HERE, "lratcheck_py.py"), cp, pp, "--allow-satisfied"])
        got["py_strict"], ms = run([sys.executable, "-B", os.path.join(HERE, "lratcheck_py.py"), cp, pp])
        match = got == want
        allok &= match
        res.append({"case": name, "cnf": cnf, "proof": proof, "expected_verified": want, "got_verified": got,
                    "match": match, "C_output": mc, "py_output": mp, "py_strict_output": ms})
        print(name, "match" if match else "MISMATCH", got)
    out = {"cases": res, "all_required_true": bool(allok), "python": sys.version.split()[0]}
    with open(os.path.join(HERE, "..", "evidence", "lrat_soundness_tests.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print("all_required_true:", allok)
    sys.exit(0 if allok else 1)


if __name__ == "__main__":
    main()
