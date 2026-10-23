#!/usr/bin/env python3
"""One-shot lane gate for a (Z_n, k; 1)-DM candidate written by dmorbit_xc_c21v1 / keq_clique_c21v1 (sub-lane cfr21,
worker InfoCFR27Lift; README section 1.1). Usage:
  candidate_gate_c21v1.py dm DMRAW K N SPEC.json OUTDIR     (DM candidate with its claimed symmetry spec)
  candidate_gate_c21v1.py cfr CFRRAW R N OUTDIR             (CFR candidate written directly, e.g. by keq/v7)
OUTDIR is created (must not exist). Steps (each a separate copied program; outputs and exit codes kept in
OUTDIR/receipt.json together with the sha256 of every input and program):
  dm mode : dm_check_c21v1 (K, N) -> dm_to_cfr_c21v1 (writes OUTDIR/cfr.raw) -> checker A and checker B on cfr.raw
            (R = K - 1) -> witness_gate_c21v1 (mutations) -> audit_group_invariance_c21v1 with the control
            (1, swap rows 0 and 1) (column-multiset invariance of the DM, not CFR row isotopy).
  cfr mode: checker A, checker B, witness_gate_c21v1.
Exit 0 iff every step meets its expectation. This is the LANE gate only; the parent's independent routes decide.
"""
import hashlib, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    return {"cmd": cmd, "rc": p.returncode, "stdout": p.stdout, "stderr": p.stderr[-2000:]}


def main():
    mode = sys.argv[1]
    P = lambda name: os.path.join(HERE, name)
    rec = {"mode": mode, "steps": [], "programs": {}}
    ok = True
    if mode == "dm":
        dm, K, N, spec, out = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6]
        os.mkdir(out)
        rec["inputs"] = {"dm": dm, "dm_sha256": sha(dm), "spec": spec, "spec_sha256": sha(spec), "K": K, "N": N}
        s = run(["python3", P("dm_check_c21v1.py"), dm, str(K), str(N)]); rec["steps"].append(s); ok &= s["rc"] == 0 and "DM PASS" in s["stdout"]
        cfr = os.path.join(out, "cfr.raw")
        s = run(["python3", P("dm_to_cfr_c21v1.py"), dm, str(K), str(N), cfr]); rec["steps"].append(s); ok &= s["rc"] == 0
        R = K - 1
        if os.path.exists(cfr):
            rec["cfr_sha256"] = sha(cfr)
        ctrl = os.path.join(out, "controls.json")
        with open(ctrl, "x") as fh:
            json.dump([[1, [1, 0] + list(range(2, K))]], fh)
        audit = ["python3", P("audit_group_invariance_c21v1.py"), dm, str(K), str(N), spec, ctrl, os.path.join(out, "audit.json")]
    else:
        cfr, R, N, out = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        os.mkdir(out)
        rec["inputs"] = {"cfr": cfr, "cfr_sha256": sha(cfr), "R": R, "N": N}
        audit = None
    for chk in ("cfr_check_events_c21v1.py", "cfr_check_posdiff_c21v1.py"):
        s = run(["python3", P(chk), cfr, str(R), str(N)]); rec["steps"].append(s)
        ok &= s["rc"] == 0 and s["stdout"].strip().endswith("PASS")
    s = run(["python3", P("witness_gate_c21v1.py"), cfr, str(R), str(N), os.path.join(out, "gate")]); rec["steps"].append(s)
    ok &= s["rc"] == 0
    if audit:
        s = run(audit); rec["steps"].append(s); ok &= s["rc"] == 0
    for name in ("dm_check_c21v1.py", "dm_to_cfr_c21v1.py", "cfr_check_events_c21v1.py", "cfr_check_posdiff_c21v1.py",
                 "witness_gate_c21v1.py", "controls_c21v1.py", "audit_group_invariance_c21v1.py", "candidate_gate_c21v1.py"):
        rec["programs"][name] = sha(P(name))
    rec["all_as_expected"] = bool(ok)
    with open(os.path.join(out, "receipt.json"), "x") as fh:
        json.dump(rec, fh, indent=1)
    print("LANE GATE " + ("PASS" if ok else "FAIL"))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
