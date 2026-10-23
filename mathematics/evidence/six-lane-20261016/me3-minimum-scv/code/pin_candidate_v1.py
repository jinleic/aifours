"""Bookkeeping: pin the worker candidate (hash manifest). No mathematical computation.

argv[1] = run directory. Writes, exclusively, <run>/manifest.json and receipts/me3-candidate-pin-v1.json.
The manifest hashes every file under proof/, code/, receipts/ (as of this moment), reductions/ and every runs/*/ output
file (leaf files included), so later appends (README log, new receipts) are distinguishable from the pinned state.
"""
import sys
import os
import json
import hashlib
import time
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402

RUN = sys.argv[1]
L = "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/me3-minimum-scv/"


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


manifest = {}
for top in ("proof", "code", "receipts", "reductions", "runs", "sources"):
    for dirpath, dirnames, filenames in os.walk(L + top):
        dirnames.sort()
        if "/tmp" in dirpath or os.path.abspath(dirpath).startswith(os.path.abspath(RUN)):
            continue
        for fn in sorted(filenames):
            p = os.path.join(dirpath, fn)
            rel = os.path.relpath(p, L)
            manifest[rel] = {"sha256": sha(p), "bytes": os.path.getsize(p)}
manifest["README.md"] = {"sha256": sha(L + "README.md"), "bytes": os.path.getsize(L + "README.md"),
                         "note": "append-only log; snapshot at pin time"}
with lane_guard.xopen(RUN + "/manifest.json") as fh:
    json.dump(manifest, fh, indent=0, sort_keys=True)
man_sha = sha(RUN + "/manifest.json")

KEY = ["proof/me3-theorem-v3.md", "proof/charts-spec-v1.md", "reductions/proof/reductions-v1.md",
       "reductions/proof/vcos-lower-bound-v1.md", "reductions/STATUS.md", "reductions/replay/REPLAY-STATUS-v2.md",
       "code/spec_primal_P_v1.json", "code/spec_dual_v1.json", "code/spec_dual_v2.json",
       "receipts/spec-dual-freeze-v1.json", "receipts/spec-dual-freeze-v2.json",
       "code/cert_primal_v3.py", "code/me3lib_v1.py", "code/me3jet_v1.py", "code/me3jet_v2.py",
       "code/cert_dual_v5.py", "code/cert_dual_v6.py", "code/me3dual_v3.py", "code/me3dual_v4.py",
       "code/me3dual_v6.py", "code/me3dual_v7.py", "code/me3dual_v8.py", "code/check_cover_v1.py",
       "code/check_cover_v2.py", "code/controls_v1.py", "code/make_audit_mutants_v1.py",
       "code/index_certificates_v2.py", "code/run_v1.sh", "code/lane_guard.py",
       "runs/i01-index/certificate_index.json", "runs/n01-controls/controls.json"]
pin = {
    "event": "ME3 minimum-SCV worker candidate pinned (worker MathPhaseType3); unreviewed; correctness only",
    "pinned_at_host_clock": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    "contract": "institute/runs/six-lane-2026-10-16/screening/math-1-me3-minimum-scv-contract.json",
    "claim": ("Every continuous ME(<=3) law has SCV >= v_cos := min over omega>0, phi of SCV(e^{-t}(1-cos(omega t - phi))); "
              "attained in D1; strict (> v_cos) for every D2 cone; real exponents give SCV >= Delta_3 > 0.2765."),
    "status": "CANDIDATE (full statement; no uncovered pole region); parent replay and hostile reviews pending",
    "claim_limits": ["no novelty/priority/'first' claim", "no Lean/kernel check",
                     "depends on Arb ball-arithmetic correctness and on code implementing stated formulas",
                     "not the book's general minimal-representation question"],
    "key_files": {k: manifest[k]["sha256"] for k in KEY},
    "manifest": {"path": os.path.relpath(RUN + "/manifest.json", L), "sha256": man_sha, "files": len(manifest)},
}
with lane_guard.xopen(L + "receipts/me3-candidate-pin-v1.json") as fh:
    json.dump(pin, fh, indent=1)
print(json.dumps({"manifest_files": len(manifest), "manifest_sha256": man_sha,
                  "pin_sha256": sha(L + "receipts/me3-candidate-pin-v1.json")}))
