#!/usr/bin/env python3
"""v2_receipt.py: replay receipt for engine-v2 (code/large_t_lex.py) proof-mode reports. Lane ame46-support.

For each report (evidence/large_t_lex_t<t>_e<e>.json, written in --proof mode), this script:
 1. checks the report header: engine v2, proof mode, outcome EXCLUDED, no guard trip;
 2. for every ENUMERATED profile:
    - regenerates in memory the exact final CNF the engine solved: SmallGen.build_gen, then the lex-leader
      constraints for the generators, then one blocking clause per found solution in report order;
    - records its SHA-256;
    - checks the stored gzip LRAT stream with the C checker and with the Python checker in skip mode, both through a
      FIFO and a pipe, and once more with the Python checker in strict mode, for information;
    - records satisfied-hint counts;
 3. for every found solution, recomputes the exclusion reason: components, moduli certificate, exact phase obstruction,
    or completion UNSAT. For a completion UNSAT it regenerates the completion CNF (SHA-256) and checks its stream the
    same way;
 4. asserts that the blocking clauses are exactly the solutions it re-excluded.
Nothing uncompressed is written. Usage: v2_receipt.py OUT.json REPORT.json [REPORT.json ...]
"""
import gzip
import hashlib
import json
import os
import re
import subprocess
import sys
import threading

import large_t_e0 as lte
import large_t_gen as ltg
import large_t_lex as eng
import phase_check as pc

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)


def sha_text(text):
    return hashlib.sha256(text.encode()).hexdigest()


def sha_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def run_checker(cmd, text, gz_path, fifo):
    if not os.path.exists(fifo):
        os.mkfifo(fifo)

    def feed():
        with open(fifo, "w") as fh:
            fh.write(text)
    th = threading.Thread(target=feed, daemon=True)
    th.start()
    gz = subprocess.Popen(["gzip", "-dc", gz_path], stdout=subprocess.PIPE)
    p = subprocess.Popen(cmd + [fifo, "/dev/stdin"] if cmd[-1] != "--allow-satisfied" else
                         cmd[:-1] + [fifo, "/dev/stdin", "--allow-satisfied"],
                         stdin=gz.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    gz.stdout.close()
    out, err = p.communicate()
    gz.wait()
    th.join(timeout=5)
    msg = " | ".join(out.strip().splitlines()) or err.strip()
    m = re.search(r"satisfied hints skipped (\d+)", msg)
    return {"verified": p.returncode == 0 and "s VERIFIED" in out, "msg": msg,
            "satisfied_hints": int(m.group(1)) if m else None}


def check_all(text, gz_rel):
    gz_path = os.path.join(LANE, gz_rel)
    fifo = gz_path + ".receipt.fifo"
    C = run_checker([os.path.join(HERE, "lratcheck")], text, gz_path, fifo)
    P = run_checker([sys.executable, "-B", os.path.join(HERE, "lratcheck_py.py"), "--allow-satisfied"], text, gz_path,
                    fifo)
    S = run_checker([sys.executable, "-B", os.path.join(HERE, "lratcheck_py.py")], text, gz_path, fifo)
    return {"proof": gz_rel, "proof_gz_sha256": sha_file(gz_path), "proof_gz_bytes": os.path.getsize(gz_path),
            "cnf_sha256": sha_text(text), "C": C, "py_skip": P, "py_strict_info": S,
            "verified_by_both": C["verified"] and P["verified"]}


def replay(report_path):
    rep = json.load(open(report_path))
    out = {"report": os.path.relpath(report_path, LANE), "report_sha256": sha_file(report_path),
           "t": rep["t"], "e": rep["e"], "profiles": []}
    header_ok = (rep.get("engine") == "large_t_lex v2" and rep.get("mode") == "proof" and
                 rep.get("outcome") == "EXCLUDED" and rep.get("guard_tripped") is None)
    out["header_ok"] = header_ok
    all_ok = header_ok
    h, e = rep["h"], rep["e"]
    for pr in rep["profiles"]:
        prof = [tuple(p) for p in pr["profile"]]
        po = {"profile": pr["profile"], "status": pr["status"]}
        if pr["status"] == "EMPTY":
            S = ltg.SmallGen([list(p) for p in prof])
            po["empty_ok"] = 2 * h + e > len(S.points)
            all_ok &= po["empty_ok"]
            out["profiles"].append(po)
            continue
        if pr["status"] != "ENUMERATED":
            po["ok"] = False
            all_ok = False
            out["profiles"].append(po)
            continue
        S = ltg.SmallGen([list(p) for p in prof])
        S.build_gen(e, h)
        for g in eng.generators(S):
            eng.add_lex_leader(S, g)
        idx = {"".join(map(str, x)): x for x in S.points}
        sols = [[idx[s] for s in r["N"]] for r in pr["reps"]]
        blocks = [[-S.var[x] for x in N] for N in sols]
        text = eng.dimacs(S.nv, S.cl + blocks)
        po["final"] = check_all(text, pr["final_proof"]["proof"])
        po["solutions"] = len(sols)
        reasons = []
        for k, N in enumerate(sols):
            okc, why = ltg.component_checks(N)
            if not okc:
                reasons.append({"k": k, "reason": "components", "detail": why, "ok": True})
                continue
            cert = ltg.moduli_certificate(N)
            if cert is not None and cert["verified"]:
                reasons.append({"k": k, "reason": "moduli certificate", "ok": True})
                continue
            eqs = pc.block_equations(set(N))
            elems = sorted({x for _, tt in eqs for x, _ in tt})
            ph = pc.phase_consistency(eqs, elems)
            if not ph["complex_consistent"]:
                reasons.append({"k": k, "reason": "phase obstruction", "ok": bool(ph.get("obstruction_verified"))})
                continue
            ctext, nall = eng.completion_text(N)
            cp = pr["reps"][k].get("completion_proof")
            if cp is None:
                reasons.append({"k": k, "reason": "completion: no proof stream", "ok": False})
                continue
            chk = check_all(ctext, cp["proof"])
            reasons.append({"k": k, "reason": "completion UNSAT", "allowed_points": nall, "check": chk,
                            "ok": chk["verified_by_both"]})
        po["reasons"] = reasons
        po["ok"] = po["final"]["verified_by_both"] and all(r["ok"] for r in reasons) and len(reasons) == len(blocks)
        all_ok &= po["ok"]
        out["profiles"].append(po)
        print(json.dumps({"t": rep["t"], "e": e, "profile": pr["profile"], "solutions": len(sols), "ok": po["ok"],
                          "final": po["final"]["C"]["msg"]}), flush=True)
    out["all_ok"] = bool(all_ok)
    return out


def main():
    dest, reports = sys.argv[1], sys.argv[2:]
    res = {"receipt": "v2_receipt.py", "engine_sha256": sha_file(os.path.join(HERE, "large_t_lex.py")),
           "checkers": {"lratcheck": sha_file(os.path.join(HERE, "lratcheck")),
                        "lratcheck_py.py": sha_file(os.path.join(HERE, "lratcheck_py.py"))},
           "cases": [replay(r) for r in reports]}
    res["all_required_true"] = all(c["all_ok"] for c in res["cases"])
    with open(dest, "w") as fh:
        json.dump(res, fh, indent=1)
    print("all_required_true:", res["all_required_true"])


if __name__ == "__main__":
    main()
