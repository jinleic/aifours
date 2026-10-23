#!/usr/bin/env python3
"""Checker negative/positive controls (parent finding 2026-10-17 12:2x: lrat-check accepts an
empty-clause step without a conflict). Files are written under cycle2/checker-smoke/.
  N1 lrat-check, SAT CNF 'p cnf 1 1 / 1 0', LRAT '2 0 0'      -> must FAIL (records actual)
  N2 lrat-check, same CNF, LRAT '2 0 1 0'                       -> must FAIL (records actual)
  N3 drat-trim, same CNF, empty DRAT                            -> must be NOT VERIFIED
  N4 drat-trim, same CNF, ASCII DRAT '0' (empty clause only)    -> must be NOT VERIFIED
  N5 drat-trim, same CNF, binary DRAT with only the empty clause -> must be NOT VERIFIED
  P1 drat-trim, 'p cnf 2 4 / 1 2 / 1 -2 / -1 2 / -1 -2', DRAT '1 0 / 0' -> VERIFIED, rc 0
  P2 drat-trim, 'p cnf 1 2 / 1 0 / -1 0', empty DRAT  -> prints VERIFIED (trivial UNSAT); rc noted
  P3 lrat-check, 'p cnf 1 2 / 1 0 / -1 0', LRAT '3 0 1 2 0'     -> VERIFIED
Acceptance in this lane keys on drat-trim (own exit, rc 0, 's VERIFIED'); lrat-check is not an
acceptance criterion from now on.
"""
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
DT = os.path.join(LANE, "tools", "drat-trim", "drat-trim")
LC = os.path.join(LANE, "tools", "drat-trim", "lrat-check")
D = os.path.join(LANE, "cycle2", "checker-smoke")


def w(name, data):
    p = os.path.join(D, name)
    with open(p, "wb") as f:
        f.write(data)
    return p


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    return {"rc": p.returncode, "out": (p.stdout + p.stderr).strip().splitlines()[-4:]}


def main():
    os.makedirs(D, exist_ok=True)
    sat = w("sat1.cnf", b"p cnf 1 1\n1 0\n")
    uns = w("unsat_units.cnf", b"p cnf 1 2\n1 0\n-1 0\n")
    uns4 = w("unsat4.cnf", b"p cnf 2 4\n1 2 0\n1 -2 0\n-1 2 0\n-1 -2 0\n")
    res = {}
    res["N1_lrat_2_0_0"] = run([LC, sat, w("n1.lrat", b"2 0 0\n")])
    res["N2_lrat_2_0_1_0"] = run([LC, sat, w("n2.lrat", b"2 0 1 0\n")])
    res["N3_drat_empty"] = run([DT, sat, w("n3.drat", b"")])
    res["N4_drat_ascii_empty_clause"] = run([DT, sat, w("n4.drat", b"0\n")])
    res["N5_drat_binary_empty_clause"] = run([DT, sat, w("n5.drat", b"a\x00"), "-i"])
    res["P1_drat_unsat4"] = run([DT, uns4, w("p1.drat", b"1 0\n0\n")])
    res["P2_drat_trivial_units"] = run([DT, uns, w("p2.drat", b"")])
    res["P3_lrat_units"] = run([LC, uns, w("p3.lrat", b"3 0 1 2 0\n")])

    def dt_ok(r):
        return r["rc"] == 0 and any("s VERIFIED" in l for l in r["out"])

    def lc_ok(r):
        return r["rc"] == 0 and any(l.strip() == "c VERIFIED" for l in r["out"])

    res["verdicts"] = {
        "lrat_check_unsound_N1": lc_ok(res["N1_lrat_2_0_0"]),
        "lrat_check_unsound_N2": lc_ok(res["N2_lrat_2_0_1_0"]),
        "drat_trim_rejects_N3": not dt_ok(res["N3_drat_empty"]),
        "drat_trim_rejects_N4": not dt_ok(res["N4_drat_ascii_empty_clause"]),
        "drat_trim_rejects_N5": not dt_ok(res["N5_drat_binary_empty_clause"]),
        "drat_trim_accepts_P1": dt_ok(res["P1_drat_unsat4"]),
        "drat_trim_P2_rc": res["P2_drat_trivial_units"]["rc"],
        "lrat_check_accepts_P3": lc_ok(res["P3_lrat_units"]),
    }
    json.dump(res, open(os.path.join(D, "checker-smoke.json"), "w"), indent=1)
    print(json.dumps(res["verdicts"], indent=1))


if __name__ == "__main__":
    main()
