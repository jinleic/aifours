#!/usr/bin/env python3
"""summarize_cases.py: markdown summary of engine reports evidence/large_t_gen_t<t>_e<e>.json (lane ame46-support).
Usage: summarize_cases.py t,e [t,e ...]
"""
import json
import os
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))


def reason(r):
    if not r["components_ok"]:
        return "components"
    if r.get("moduli_excluded"):
        return "moduli certificate"
    if r.get("phase_complex_consistent") is False:
        return "2x2 phase obstruction"
    if r.get("completion_status") == "UNSAT":
        return "completion UNSAT"
    return "NOT EXCLUDED"


def main():
    print("| (t, e) | profile | orbits (sizes) | exclusion reasons | final enumeration UNSAT LRAT-checked |")
    print("|---|---|---|---|---|")
    for arg in sys.argv[1:]:
        t, e = map(int, arg.split(","))
        rep = json.load(open(os.path.join(HERE, "..", "evidence", "large_t_gen_t%d_e%d.json" % (t, e))))
        for p in rep["profiles"]:
            prof = " ".join("{" + ",".join(map(str, q)) + "}" for q in p["profile"])
            reps = p.get("reps", [])
            sizes = ",".join(str(r["orbit_size"]) for r in reps) or "-"
            reasons = Counter(reason(r) for r in reps)
            rs = "; ".join("%s ×%d" % (k, v) for k, v in sorted(reasons.items())) or "-"
            print("| (%d, %d) | %s | %d (%s) | %s | %s |" % (t, e, prof, p["orbits"], sizes, rs,
                                                         p.get("final_unsat_lrat_verified", p.get("skipped"))))
        print("| (%d, %d) | **all profiles** | | **excluded = %s** | |" % (t, e, rep["excluded"]))


if __name__ == "__main__":
    main()
