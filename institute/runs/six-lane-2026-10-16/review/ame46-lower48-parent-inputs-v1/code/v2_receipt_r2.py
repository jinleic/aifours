#!/usr/bin/env python3
"""v2_receipt_r2.py: replay receipt r2 for engine-v2 (code/large_t_lex.py) proof-mode reports. Lane ame46-support.

This is a new file; v2_receipt.py and its output are kept unchanged. r2 adds the parent's binding requirements of
13:2x PDT:
 (1) every phase exclusion stores an explicit certificate in the parent's format (code/phase_cert.py), and the
     certificate is checked by a verifier independent of phase_check.py;
 (2) every completion exclusion stores N, the SHA-256 of the regenerated completion CNF and the SHA-256 of the proof
     stream. It also notes the written counting margin sigma0 - sigma1 + sigma2 for the profile (a negative value
     would exclude the profile on its own).
As in r1, for every ENUMERATED profile the script regenerates in memory the exact final CNF (base, lex-leader
constraints, blocking clauses in report order) and checks the stored gzip LRAT streams with the C checker and with
the Python checker in skip mode; strict mode is recorded for information. It asserts that the blocking clauses are
exactly the re-excluded solutions, and it runs negative controls on the certificate verifier.
Usage: v2_receipt_r2.py OUT.json REPORT.json [REPORT.json ...]
"""
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import threading

import large_t_gen as ltg
import large_t_lex as eng
import phase_cert as pcert

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


def alpha_family(prof, t, h):
    """f(alpha) = sigma2 - alpha*sigma1 + C(alpha+1, 2)*sigma0 for alpha = 0..4. It equals the sum over officers of
    (c - alpha)(c - alpha - 1)/2, which is >= 0 for integer c; alpha = 1 is the parent's sigma0 - sigma1 + sigma2. A
    negative value excludes the profile, for every e."""
    V = [len(p) for p in prof]
    s1 = 6 * sum(V) - 4 * h
    s2 = sum(V[i] * V[j] for i in range(4) for j in range(i + 1, 4)) - 6 * h
    return [s2 - a * s1 + a * (a + 1) // 2 * t for a in range(5)]


def run_checker(cmd, text, gz_path, fifo, allow_sat):
    if not os.path.exists(fifo):
        os.mkfifo(fifo)

    def feed():
        with open(fifo, "w") as fh:
            fh.write(text)
    th = threading.Thread(target=feed, daemon=True)
    th.start()
    gz = subprocess.Popen(["gzip", "-dc", gz_path], stdout=subprocess.PIPE)
    full = cmd + [fifo, "/dev/stdin"] + (["--allow-satisfied"] if allow_sat else [])
    p = subprocess.Popen(full, stdin=gz.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
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
    C = run_checker([os.path.join(HERE, "lratcheck")], text, gz_path, fifo, False)
    P = run_checker([sys.executable, "-B", os.path.join(HERE, "lratcheck_py.py")], text, gz_path, fifo, True)
    S = run_checker([sys.executable, "-B", os.path.join(HERE, "lratcheck_py.py")], text, gz_path, fifo, False)
    return {"proof": gz_rel, "proof_gz_sha256": sha_file(gz_path), "proof_gz_bytes": os.path.getsize(gz_path),
            "cnf_sha256": sha_text(text), "C": C, "py_skip": P, "py_strict_info": S,
            "verified_by_both": C["verified"] and P["verified"]}


def cert_controls(N, cert):
    """Negative controls: each mutation must be rejected."""
    out = []
    muts = []
    if len(cert) >= 2:
        muts.append(("drop last entry", cert[:-1]))
    muts.append(("flip first sign", [dict(cert[0], sign=-cert[0]["sign"])] + cert[1:]))
    muts.append(("duplicate first entry", cert + [cert[0]]))
    muts.append(("change reshaping of first entry", [dict(cert[0], k=(cert[0]["k"] + 1) % 3)] + cert[1:]))
    Nset = {pcert.unpt(x) if isinstance(x, str) else tuple(x) for x in N}
    outside = next(pcert.pt(x) for x in __import__("itertools").product(range(6), repeat=4) if x not in Nset)
    c0 = list(cert[0]["corners"])
    c0[0] = outside
    muts.append(("corner outside N", [dict(cert[0], corners=c0)] + cert[1:]))
    for name, m in muts:
        ok, why = pcert.verify_certificate(N, m)
        out.append({"mutation": name, "rejected": not ok, "reason": why})
    return out


def replay(report_path, controls_done):
    rep = json.load(open(report_path))
    out = {"report": os.path.relpath(report_path, LANE), "report_sha256": sha_file(report_path),
           "t": rep["t"], "e": rep["e"], "profiles": []}
    header_ok = (rep.get("engine") == "large_t_lex v2" and rep.get("mode") == "proof" and
                 rep.get("outcome") == "EXCLUDED" and rep.get("guard_tripped") is None)
    out["header_ok"] = header_ok
    all_ok = header_ok
    t, h, e = rep["t"], rep["h"], rep["e"]
    for pr in rep["profiles"]:
        prof = [list(p) for p in pr["profile"]]
        po = {"profile": prof, "status": pr["status"], "counting_margin": pcert.counting_margin(prof, t, h)}
        po["counting_excludes_profile"] = po["counting_margin"] < 0
        po["counting_alpha_family"] = alpha_family(prof, t, h)
        po["counting_alpha_family_excludes_profile"] = min(po["counting_alpha_family"]) < 0
        if pr["status"] == "EMPTY":
            S = ltg.SmallGen(prof)
            po["empty_ok"] = 2 * h + e > len(S.points)
            all_ok &= po["empty_ok"]
            out["profiles"].append(po)
            continue
        if pr["status"] != "ENUMERATED":
            po["ok"] = False
            all_ok = False
            out["profiles"].append(po)
            continue
        S = ltg.SmallGen(prof)
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
            Nstr = [pcert.pt(x) for x in N]
            okc, why = ltg.component_checks(N)
            if not okc:
                reasons.append({"k": k, "N": Nstr, "reason": "components", "detail": why, "ok": True})
                continue
            mc = ltg.moduli_certificate(N)
            if mc is not None and mc["verified"]:
                reasons.append({"k": k, "N": Nstr, "reason": "moduli certificate", "certificate": mc, "ok": True})
                continue
            cert = pcert.extract_certificate(N)
            if cert is not None:
                cok, cwhy = pcert.verify_certificate(N, cert)
                acc = {}
                for ent in cert:
                    acc[(ent["k"], tuple(ent["corners"]))] = acc.get((ent["k"], tuple(ent["corners"])), 0) + ent["sign"]
                compact = [{"w": w, "k": kk, "corners": list(c)} for (kk, c), w in acc.items() if w != 0]
                entry = {"k": k, "N": Nstr, "reason": "phase obstruction", "certificate": cert,
                         "certificate_compact": compact, "certificate_compact_weight_sum": sum(x["w"] for x in compact),
                         "certificate_entries": len(cert), "certificate_check": cwhy, "ok": cok}
                if not controls_done["done"]:
                    entry["verifier_negative_controls"] = cert_controls(N, cert)
                    controls_done["done"] = True
                    controls_done["all_rejected"] = all(c["rejected"] for c in entry["verifier_negative_controls"])
                reasons.append(entry)
                continue
            ctext, nall = eng.completion_text(N)
            cp = pr["reps"][k].get("completion_proof")
            if cp is None:
                reasons.append({"k": k, "N": Nstr, "reason": "completion: no proof stream", "ok": False})
                continue
            chk = check_all(ctext, cp["proof"])
            reasons.append({"k": k, "N": Nstr, "reason": "completion UNSAT", "allowed_points": nall,
                            "completion_cnf_sha256": chk["cnf_sha256"], "proof_gz_sha256": chk["proof_gz_sha256"],
                            "check": chk, "counting_margin": po["counting_margin"],
                            "counting_excludes_profile": po["counting_excludes_profile"],
                            "counting_alpha_family_excludes_profile": po["counting_alpha_family_excludes_profile"],
                            "ok": chk["verified_by_both"]})
        po["reasons"] = reasons
        po["reason_counts"] = {r: sum(1 for x in reasons if x["reason"] == r) for r in {x["reason"] for x in reasons}}
        po["ok"] = po["final"]["verified_by_both"] and all(r["ok"] for r in reasons) and len(reasons) == len(blocks)
        all_ok &= po["ok"]
        out["profiles"].append(po)
        print(json.dumps({"t": t, "e": e, "profile": prof, "solutions": len(sols), "ok": po["ok"],
                          "reasons": po["reason_counts"], "margin": po["counting_margin"]}), flush=True)
    out["all_ok"] = bool(all_ok)
    return out


def main():
    dest, reports = sys.argv[1], sys.argv[2:]
    cad = subprocess.run(["which", "cadical"], capture_output=True, text=True).stdout.strip()
    cad_real = os.path.realpath(cad)
    controls = {"done": False, "all_rejected": None}
    res = {"receipt": "v2_receipt_r2.py", "receipt_sha256": sha_file(os.path.abspath(__file__)),
           "engine_sha256": sha_file(os.path.join(HERE, "large_t_lex.py")),
           "phase_cert_sha256": sha_file(os.path.join(HERE, "phase_cert.py")),
           "interpreter": {"executable": sys.executable, "version": platform.python_version()},
           "cadical": {"path": cad_real, "sha256": sha_file(cad_real),
                       "version": subprocess.run(["cadical", "--version"], capture_output=True,
                                                 text=True).stdout.strip()},
           "checkers": {"lratcheck": sha_file(os.path.join(HERE, "lratcheck")),
                        "lratcheck.c": sha_file(os.path.join(HERE, "lratcheck.c")),
                        "lratcheck_py.py": sha_file(os.path.join(HERE, "lratcheck_py.py"))},
           "cases": [replay(r, controls) for r in reports]}
    res["certificate_verifier_negative_controls_all_rejected"] = controls["all_rejected"]
    res["all_required_true"] = all(c["all_ok"] for c in res["cases"]) and controls["all_rejected"] in (True, None)
    with open(dest, "w") as fh:
        json.dump(res, fh, indent=1)
    print("all_required_true:", res["all_required_true"], "| cert controls all rejected:", controls["all_rejected"])


if __name__ == "__main__":
    main()
