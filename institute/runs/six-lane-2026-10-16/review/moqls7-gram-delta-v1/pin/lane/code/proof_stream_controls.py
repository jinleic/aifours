#!/usr/bin/env python3
"""End-to-end controls of the nonblocking-startup binary FIFO proof transport.

Both real solvers: non-UP UNSAT must verify, SAT must retain a valid model and
must not be accepted as UNSAT. Binary empty-clause proof on SAT must be rejected.
A writer that exits before opening its proof must not hang the reader.
No scientific CNF or previous receipt is changed. Two busy native processes max.
Usage: proof_stream_controls.py OUTDIR
"""
import hashlib
import json
import os
import subprocess
import sys

from gram_certify_r4 import CHECKER, sha
from proof_stream import run_pair



def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    formulas = {"UNSAT": [[1, 2], [1, -2], [-1, 2], [-1, -2]],
                "SAT": [[1, 2], [1, -2], [-1, 2]]}
    paths = {}
    for name, clauses in formulas.items():
        path = os.path.join(outdir, name + ".cnf")
        with open(path, "x") as f:
            f.write("p cnf 2 %d\n" % len(clauses))
            for cl in clauses:
                f.write(" ".join(map(str, cl)) + " 0\n")
        paths[name] = path
    records = []
    for solver in ("cadical", "kissat"):
        for name in ("UNSAT", "SAT"):
            cnf = paths[name]
            prefix = ([solver, "-q", "-t", "30", cnf] if solver == "cadical"
                      else [solver, "-q", "-f", "--time=30", cnf])
            log_prefix = os.path.join(outdir, solver + "_" + name)
            result = run_pair(cnf, prefix, log_prefix, 30, 30)
            result.update({"control": name, "solver": solver})
            if name == "UNSAT":
                assert result["verified_unsat"] and result["solver_rc"] == 20
            else:
                assert not result["verified_unsat"] and result["solver_rc"] == 10
                assert result["checker_status_lines"] == ["s NOT VERIFIED"]
                values = set()
                with open(log_prefix + ".solver.log") as f:
                    for line in f:
                        if line.startswith("v "):
                            values.update(int(x) for x in line.split()[1:] if int(x))
                assert values and not any(-x in values for x in values)
                assert all(any(x in values for x in cl) for cl in formulas["SAT"])
                result["retained_SAT_model_satisfies_CNF"] = True
            records.append(result)
            with open(log_prefix + ".json", "x") as f:
                json.dump(result, f, indent=2)
                f.write("\n")
            print(json.dumps({"solver": solver, "control": name, "verified_unsat": result["verified_unsat"]}), flush=True)
    # Controlled premature writer exit. The parent closes its keepalive writer
    # on child exit, delivering EOF even if no native proof file was opened.
    early = run_pair(paths["SAT"], ["/usr/bin/false"], os.path.join(outdir, "early_writer"), 30, 30)
    assert early["solver_rc"] != 20 and not early["verified_unsat"] and early["seconds"] < 10
    records.append({"control": "premature writer exit", **early})
    with open(os.path.join(outdir, "early_writer.json"), "x") as f:
        json.dump(early, f, indent=2)
        f.write("\n")
    bad = b"a\x00"              # binary DRAT empty-clause addition, invalid on SAT
    with open(os.path.join(outdir, "invalid_empty_clause.drat"), "xb") as f:
        f.write(bad)
    p = subprocess.run([CHECKER, paths["SAT"], "-i", "-t", "30"], input=bad,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log = os.path.join(outdir, "invalid_empty_clause.checker.log")
    with open(log, "xb") as f:
        f.write(p.stdout)
    lines = [line.strip() for line in p.stdout.decode().replace("\r", "\n").splitlines()]
    statuses = [line for line in lines if line.startswith("s ")]
    assert p.returncode != 0 and statuses == ["s NOT VERIFIED"]
    records.append({"control": "SAT plus binary empty-clause proof", "checker_rc": p.returncode,
                    "checker_status_lines": statuses, "proof_sha256": hashlib.sha256(bad).hexdigest(),
                    "checker_log_sha256": sha(log)})
    summary = {"status": "PASS", "controls": records, "control_code_sha256": sha(__file__),
               "transport_code_sha256": sha(os.path.join(os.path.dirname(__file__), "proof_stream.py")),
               "scope": "Transport/admissibility/failure controls only, not a quantum witness or theorem verdict"}
    with open(os.path.join(outdir, "summary.json"), "x") as f:
        json.dump(summary, f, indent=2)
        f.write("\n")
    print("PASS: both UNSAT streams verified; both SAT models retained and validated; invalid binary proof and premature writer rejected")


if __name__ == "__main__":
    main(sys.argv[1])
