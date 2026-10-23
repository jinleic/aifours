#!/usr/bin/env python3
"""lower46_phase_certs.py: explicit phase certificates for the LOWER46 phase-excluded representatives.
Lane ame46-support.

The frozen engine large_t_gen.py stored only booleans for phase exclusions (parent audit finding M1). This script
reads the pinned reports (evidence/large_t_gen_t30_e0.json and evidence/large_t_gen_t28_e0.json, which hold every
representative's N) and, for each representative reported as a phase obstruction:
 - extracts an explicit certificate in the parent's format (code/phase_cert.py);
 - verifies it with phase_cert.verify_certificate, which does not use phase_check.py;
 - for completion representatives, records N and the counting margin.
Output: evidence/lower46_phase_certificates.json. No search, no solver.
"""
import hashlib
import json
import os
import sys

import phase_cert as pcert

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
REPORTS = ["evidence/large_t_gen_t30_e0.json", "evidence/large_t_gen_t28_e0.json"]


def sha_file(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main():
    out = {"script": "lower46_phase_certs.py", "phase_cert_sha256": sha_file(os.path.join(HERE, "phase_cert.py")),
           "reports": [], "python": sys.version.split()[0]}
    n_phase = n_ok = 0
    for rp in REPORTS:
        rep = json.load(open(os.path.join(LANE, rp)))
        t = rep.get("t")
        h = 36 - t
        ro = {"report": rp, "report_sha256": sha_file(os.path.join(LANE, rp)), "t": t, "e": rep.get("e"),
              "representatives": []}
        for pr in rep["profiles"]:
            margin = pcert.counting_margin(pr["profile"], t, h)
            for k, r in enumerate(pr.get("reps", [])):
                N = [pcert.unpt(s) for s in r["N"]]
                entry = {"profile": pr["profile"], "k": k, "N": r["N"], "counting_margin": margin}
                if r.get("phase_complex_consistent") is False:
                    n_phase += 1
                    cert = pcert.extract_certificate(N)
                    ok, why = pcert.verify_certificate(N, cert) if cert else (False, "no certificate")
                    n_ok += ok
                    entry.update({"reason": "phase obstruction", "certificate": cert,
                                  "certificate_entries": len(cert) if cert else 0, "certificate_check": why,
                                  "ok": ok})
                else:
                    entry.update({"reason": "completion UNSAT (proof pinned in lower46_receipt.json)",
                                  "completion_status": r.get("completion_status")})
                ro["representatives"].append(entry)
        out["reports"].append(ro)
    out["phase_representatives"] = n_phase
    out["phase_certificates_verified"] = n_ok
    out["all_required_true"] = n_phase == n_ok and n_phase > 0
    with open(os.path.join(LANE, "evidence", "lower46_phase_certificates.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print("phase representatives:", n_phase, "verified certificates:", n_ok, "all:", out["all_required_true"])


if __name__ == "__main__":
    main()
