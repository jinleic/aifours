#!/usr/bin/env python3
"""v5_receipt.py: replay receipt for engine-v5 proof-mode reports (code/large_t_joint5.py). Lane ame46-support.
Reproducibility only: same-author code. The independent route is the parent's.

For each report (evidence/large_t_joint5_t<t>_e<e>.json, --proof, --joint, [--triangles iff e = 0]), it checks:
 1. header: engine v5, proof mode, joint, triangles == (e == 0), outcome EXCLUDED, no guard trip, no candidates;
 2. profile completeness: the report's indices are exactly 0..len(profiles(h))-1, in order, with matching profiles;
 3. EXCLUDED-BY-LEMMA profiles: Lemma 17's f(alpha) < 0 for some alpha in 0..4, recomputed;
 4. ENUMERATED profiles:
    - regenerates the final CNF exactly (review/V4_PROOF_SCHEMA.r1.md, via v5.build with its assertions, v2
      generators and lex-leader, blocks in report order) and compares its SHA-256 with final_cnf_sha256;
    - checks the gzip LRAT stream with the C checker and the Python checker in skip mode (FIFO + gzip pipe; nothing
      uncompressed is stored), and records the stream SHA-256 and strict mode for information;
    - for every recorded Y: |Y| = 2h + e, Y lies in Π V_i, and an exact rejection is re-verified. The rejection is a
      component failure (recomputed), a moduli certificate (re-verified exactly), or a phase certificate
      (phase_cert.verify_certificate on the stored certificate, plus the compact form's weight sum odd and equal to
      it).
Usage: v5_receipt.py OUT.json REPORT.json [REPORT.json ...]
"""
import hashlib
import json
import os
import sys

import large_t_e0 as lte
import large_t_gen as ltg
import large_t_joint5 as v5
import large_t_lex as v2
import large_t_lex3 as v3
import phase_cert as pcert
import v2_receipt_r2 as r2

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)


def sha_file(p):
    return r2.sha_file(p)


def replay(path):
    rep = json.load(open(path))
    t, e, h = rep["t"], rep["e"], rep["h"]
    out = {"report": os.path.relpath(path, LANE), "report_sha256": sha_file(path), "t": t, "e": e, "profiles": []}
    ok = (rep.get("engine") == "large_t_joint5 v5" and rep.get("mode") == "proof" and rep.get("joint") is True and
          rep.get("triangles") == (e == 0) and rep.get("outcome") == "EXCLUDED" and rep.get("guard_tripped") is None
          and not rep.get("candidates"))
    out["header_ok"] = ok
    profs = lte.profiles(h)
    idx = [p["index"] for p in rep["profiles"]]
    out["profile_completeness"] = idx == list(range(len(profs))) and all(
        [list(q) for q in profs[p["index"]]] == p["profile"] for p in rep["profiles"])
    ok &= out["profile_completeness"]
    for pr in rep["profiles"]:
        prof = [tuple(q) for q in pr["profile"]]
        po = {"index": pr["index"], "status": pr["status"]}
        if pr["status"] == "EXCLUDED-BY-LEMMA":
            fam = v3.alpha_family(prof, t, h)
            po["lemma17_f"] = fam
            po["ok"] = min(fam) < 0
        elif pr["status"] == "EMPTY":
            S0 = ltg.SmallGen(prof)
            po["ok"] = 2 * h + e > len(S0.points)
        elif pr["status"] == "ENUMERATED":
            S, ntri = v5.build(prof, e, h, True, e == 0)
            for g in v2.generators(S):
                v2.add_lex_leader(S, g)
            ptidx = {pcert.pt(x): x for x in S.points}
            sols = [[ptidx[s] for s in r["N"]] for r in pr["reps"]]
            text = v2.dimacs(S.nv, S.cl + [[-S.var[x] for x in N] for N in sols])
            po["final_cnf_sha256"] = hashlib.sha256(text.encode()).hexdigest()
            po["cnf_sha_match"] = po["final_cnf_sha256"] == pr["final_cnf_sha256"]
            chk = r2.check_all(text, pr["final_proof"]["proof"])
            po["stream"] = {k: chk[k] for k in ("proof", "proof_gz_sha256", "proof_gz_bytes", "verified_by_both")}
            po["stream"]["strict_info"] = chk["py_strict_info"]["verified"]
            po["stream"]["satisfied_hints"] = chk["C"]["satisfied_hints"]
            rej = []
            for r, N in zip(pr["reps"], sols):
                rr = {"size_ok": len(N) == 2 * h + e and len(set(N)) == len(N)}
                okc, why = ltg.component_checks(N)
                if not okc:
                    rr["reason"], rr["ok"] = "components: " + why, rr["size_ok"]
                elif r.get("moduli_certificate"):
                    rr["reason"] = "moduli"
                    rr["ok"] = rr["size_ok"] and bool(ltg.verify_moduli_certificate(N, r["moduli_certificate"]["w"]))
                elif r.get("phase_certificate"):
                    cok, cwhy = pcert.verify_certificate(N, r["phase_certificate"])
                    comp = r.get("phase_certificate_compact") or []
                    wsum = sum(c["w"] for c in comp)
                    rr["reason"] = "phase"
                    rr["ok"] = rr["size_ok"] and cok and wsum % 2 == 1 and wsum == sum(
                        c["sign"] for c in r["phase_certificate"])
                    rr["check"] = cwhy
                else:
                    rr["reason"], rr["ok"] = "no rejection", False
                rej.append(rr)
            po["rejections"] = rej
            po["ok"] = po["cnf_sha_match"] and chk["verified_by_both"] and all(x["ok"] for x in rej)
        else:
            po["ok"] = False
        ok &= po["ok"]
        out["profiles"].append(po)
        print(json.dumps({"t": t, "e": e, "index": pr["index"], "status": pr["status"], "ok": po["ok"]}), flush=True)
    out["all_ok"] = bool(ok)
    return out


def main():
    dest, reports = sys.argv[1], sys.argv[2:]
    res = {"receipt": "v5_receipt.py", "receipt_sha256": sha_file(os.path.abspath(__file__)),
           "engine_sha256": sha_file(os.path.join(HERE, "large_t_joint5.py")),
           "cases": [replay(r) for r in reports]}
    res["all_required_true"] = all(c["all_ok"] for c in res["cases"])
    with open(dest, "w") as fh:
        json.dump(res, fh, indent=1)
    print("all_required_true:", res["all_required_true"])


if __name__ == "__main__":
    main()
