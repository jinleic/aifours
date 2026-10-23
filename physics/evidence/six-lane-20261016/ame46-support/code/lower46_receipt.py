#!/usr/bin/env python3
"""lower46_receipt.py: receipt for review/SUPPORT_LOWER46.r1.md (lane ame46-support).

For each computer-assisted case (t, e) the receipt does the following:
- reads the engine report evidence/large_t_gen_t<t>_e<e>.json and requires excluded = true;
- lists every CNF/LRAT pair the report relies on (each profile's final enumeration UNSAT, and each completion
  UNSAT) with their SHA-256;
- re-checks every pair with both LRAT checkers: code/lratcheck (C) and code/lratcheck_py.py (Python), in lenient
  mode, which skips satisfied hints.
It also pins the e = 0 cross-check reports, the engine controls and the code files.
Writes evidence/lower46_receipt.json; exit status 0 iff everything holds.
"""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
CASES = [(30, 0), (30, 2), (30, 3), (29, 2), (28, 0)]


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def check_pair(cnf, lrat):
    import re
    c = subprocess.run([os.path.join(HERE, "lratcheck"), cnf, lrat], capture_output=True, text=True)
    p = subprocess.run([sys.executable, "-B", os.path.join(HERE, "lratcheck_py.py"), cnf, lrat, "--allow-satisfied"],
                       capture_output=True, text=True)
    q = subprocess.run([sys.executable, "-B", os.path.join(HERE, "lratcheck_py.py"), cnf, lrat],
                       capture_output=True, text=True)
    mc = re.search(r"satisfied hints skipped (\d+)", c.stdout)
    mp = re.search(r"satisfied hints skipped (\d+)", p.stdout)
    return {"C_verified": c.returncode == 0 and "s VERIFIED" in c.stdout,
            "py_verified": p.returncode == 0 and "s VERIFIED" in p.stdout,
            "py_strict_verified": q.returncode == 0 and "s VERIFIED" in q.stdout,
            "satisfied_hints_C": int(mc.group(1)) if mc else None,
            "satisfied_hints_py": int(mp.group(1)) if mp else None,
            "C_msg": " | ".join(c.stdout.strip().splitlines()) or c.stderr.strip(),
            "py_msg": " | ".join(p.stdout.strip().splitlines()) or p.stderr.strip()}

def main():
    out = {"cases": [], "code": {}, "other": {}}
    ok = True
    gdir = os.path.join(LANE, "explore", "large_t_gen")
    for t, e in CASES:
        rp = os.path.join(LANE, "evidence", "large_t_gen_t%d_e%d.json" % (t, e))
        rep = json.load(open(rp))
        case = {"t": t, "e": e, "report": os.path.relpath(rp, LANE), "report_sha256": sha(rp),
                "excluded": rep["excluded"], "profiles": []}
        ok &= rep["excluded"]
        for prof in rep["profiles"]:
            tag = "t%d_e%d_" % (t, e) + "_".join("-".join(map(str, p)) for p in prof["profile"])
            pr = {"profile": prof["profile"], "orbits": prof["orbits"], "pairs": []}
            if "skipped" in prof:
                pr["skipped"] = prof["skipped"]
            else:
                pairs = [(tag + ".cnf", tag + ".final.lrat", "enumeration final UNSAT")]
                for k, r in enumerate(prof["reps"]):
                    reason = ("components: " + r["components_reason"]) if not r["components_ok"] else \
                        ("moduli LP optimum " + r["moduli_lp_max_eps"]) if not r.get("moduli_ok", True) else \
                        "phase obstruction" if r.get("phase_complex_consistent") is False else \
                        "completion " + str(r.get("completion_status"))
                    pr.setdefault("rep_reasons", []).append({"N": r["N"], "orbit_size": r["orbit_size"],
                                                            "excluded_by": reason, "excluded": r["excluded"]})
                    ok &= r["excluded"]
                    if r.get("completion_status") == "UNSAT":
                        pairs.append((tag + "_rep%d_completion.cnf" % k, tag + "_rep%d_completion.lrat" % k,
                                      "completion UNSAT rep %d" % k))
                for cnf, lrat, what in pairs:
                    cp, lp = os.path.join(gdir, cnf), os.path.join(gdir, lrat)
                    res = check_pair(cp, lp)
                    pr["pairs"].append({"what": what, "cnf": "explore/large_t_gen/" + cnf, "cnf_sha256": sha(cp),
                                        "lrat": "explore/large_t_gen/" + lrat, "lrat_sha256": sha(lp), **res})
                    ok &= res["C_verified"] and res["py_verified"]
            case["profiles"].append(pr)
        out["cases"].append(case)
        print("t=%d e=%d excluded=%s" % (t, e, case["excluded"]), flush=True)
    for name in ["large_t_gen.py", "large_t_e0.py", "ame_e0_cnf.py", "phase_check.py", "lratcheck.c",
                 "lratcheck_py.py", "engine_control.py", "lower46_receipt.py", "pandya_control.py"]:
        out["code"][name] = sha(os.path.join(HERE, name))
    for rel in ["evidence/engine_control.json", "evidence/large_t_e0_t30_nophase.json",
                "evidence/large_t_e0_t28_nophase.json"]:
        p = os.path.join(LANE, rel)
        out["other"][rel] = sha(p) if os.path.exists(p) else None
    ec = json.load(open(os.path.join(LANE, "evidence", "engine_control.json")))
    out["engine_control_all_required_true"] = ec["all_required_true"]
    ok &= ec["all_required_true"]
    out["cadical_version"] = subprocess.run(["cadical", "--version"], capture_output=True, text=True).stdout.strip()
    out["python"] = sys.version.split()[0]
    out["all_required_true"] = bool(ok)
    with open(os.path.join(LANE, "evidence", "lower46_receipt.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print("all_required_true:", ok)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
