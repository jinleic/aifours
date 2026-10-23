#!/usr/bin/env python3
"""engine_control.py: positive and negative controls for large_t_e0.Small and large_t_gen.SmallGen (lane ame46-support).

Pandya's 60-term state (pandya_control.TABLE) has t = 12, e = 0, and in every coordinate deficits 6 on the values
{1, 2} and 3 on {0, 3, 4, 5}. The engines put the parts in non-increasing order on increasing values, so the
relabelling sigma: 1 -> 0, 2 -> 1, 0 -> 2, 3 -> 3, 4 -> 4, 5 -> 5 (in every coordinate) maps Pandya's N into the
engine's normal form.
 positive: the CNF for profile (6,6,3,3,3,3)^4 with sigma(N) fixed by unit clauses is SAT (e0 engine with and
           without phase clauses, general engine with e = 0);
 negative: with one element of sigma(N) replaced by a point outside N (support size kept), the CNF is UNSAT.
"""
import json
import os
import subprocess

import large_t_e0 as lte
import large_t_gen as ltg
import pandya_control as pcn

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "explore", "engine_control")
SIGMA = {1: 0, 2: 1, 0: 2, 3: 3, 4: 4, 5: 5}


def check(S, Nfix, path):
    units = [[S.var[x]] if x in Nfix else [-S.var[x]] for x in S.points]
    S.write(path, units)
    r = subprocess.run(["cadical", "-q", path], capture_output=True, text=True)
    return {10: "SAT", 20: "UNSAT"}.get(r.returncode, str(r.returncode))


def main():
    os.makedirs(OUT, exist_ok=True)
    W = pcn.build()
    N = {tuple(SIGMA[c] for c in x) for x, v in W.items() if v != pcn.R2}
    prof = [(6, 6, 3, 3, 3, 3)] * 4
    res = {}
    S1 = lte.Small(prof)
    S1.build(phase=True)
    res["e0_engine_phase_clauses_pandya"] = check(S1, N, os.path.join(OUT, "e0_phase.cnf"))
    S2 = lte.Small(prof)
    S2.build(phase=False)
    res["e0_engine_no_phase_pandya"] = check(S2, N, os.path.join(OUT, "e0_nophase.cnf"))
    S3 = ltg.SmallGen(prof)
    S3.build_gen(0, 24)
    res["gen_engine_e0_pandya"] = check(S3, N, os.path.join(OUT, "gen_e0.cnf"))
    # negative control: move one element to a point outside N
    x0 = sorted(N)[0]
    y0 = next(y for y in S3.points if y not in N and y[0] == x0[0] and y[1] == x0[1])
    Nbad = (N - {x0}) | {y0}
    S4 = ltg.SmallGen(prof)
    S4.build_gen(0, 24)
    res["gen_engine_e0_mutated"] = check(S4, Nbad, os.path.join(OUT, "gen_e0_bad.cnf"))
    S5 = lte.Small(prof)
    S5.build(phase=False)
    res["e0_engine_mutated"] = check(S5, Nbad, os.path.join(OUT, "e0_bad.cnf"))
    res["mutation"] = {"removed": "".join(map(str, x0)), "added": "".join(map(str, y0))}
    res["all_required_true"] = (res["e0_engine_phase_clauses_pandya"] == "SAT" and res["e0_engine_no_phase_pandya"] == "SAT"
                                and res["gen_engine_e0_pandya"] == "SAT" and res["gen_engine_e0_mutated"] == "UNSAT"
                                and res["e0_engine_mutated"] == "UNSAT")
    with open(os.path.join(HERE, "..", "evidence", "engine_control.json"), "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
