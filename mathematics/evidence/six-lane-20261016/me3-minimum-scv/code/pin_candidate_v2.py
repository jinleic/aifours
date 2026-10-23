"""Bookkeeping: pin the REPAIRED worker candidate, version 2 (pin_candidate_v1.py and its pin are kept; pin v1 is
INVALID because its SWC run d02 used float-rounded corner coefficients). No mathematical computation.

argv[1] = run directory; argv[2:] = extra key files (lane-relative) to bind, e.g. subagent outputs.
Writes, exclusively, <run>/manifest.json (SHA-256 + size of every file under proof/, code/, receipts/, reductions/,
runs/, sources/, independent-float-audit/ and README.md, excluding tmp/ and this run's own directory) and
receipts/me3-candidate-pin-v2.json (key-file hashes, runtime identity, invalid evidence, external citations).
Every key file must exist (assertion), so a missing artifact aborts the pin.
"""
import sys
import os
import json
import hashlib
import time
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402

RUN = sys.argv[1]
EXTRA = sys.argv[2:]
L = "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/me3-minimum-scv/"
R = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/"


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


manifest = {}
runabs = os.path.abspath(RUN)
for top in ("proof", "code", "receipts", "reductions", "runs", "sources", "independent-float-audit"):
    for dirpath, dirnames, filenames in os.walk(L + top):
        dirnames.sort()
        ap = os.path.abspath(dirpath)
        if "/tmp" in ap or ap.startswith(runabs):
            continue
        for fn in sorted(filenames):
            p = os.path.join(dirpath, fn)
            manifest[os.path.relpath(p, L)] = {"sha256": sha(p), "bytes": os.path.getsize(p)}
manifest["README.md"] = {"sha256": sha(L + "README.md"), "bytes": os.path.getsize(L + "README.md"),
                         "note": "append-only log; snapshot at pin time"}
with lane_guard.xopen(RUN + "/manifest.json") as fh:
    json.dump(manifest, fh, indent=0, sort_keys=True)
man_sha = sha(RUN + "/manifest.json")

KEY = [
    # proof documents
    "proof/me3-theorem-v4.md", "proof/charts-spec-v2.md", "proof/float-audit-v1.md",
    # SWC repair: library, driver, spec, freeze receipt, run, receipts, audit, controls
    "code/me3dual_v9.py", "code/cert_dual_v7.py", "code/spec_dual_v3.json", "receipts/spec-dual-freeze-v3.json",
    "runs/d03-SWC/dual.json", "runs/d03-SWC/leaves.txt.gz", "receipts/d03-SWC-pre.json", "receipts/d03-SWC-post.json",
    "code/check_cover_v3.py",
    "runs/b03-cover-P/cover.json", "runs/b03-cover-G/cover.json", "runs/b03-cover-SWB/cover.json",
    "runs/b03-cover-SWC/cover.json", "runs/b03-cover-LW/cover.json", "runs/b03-cover-LD1/cover.json",
    "runs/b03-cover-LD2/cover.json",
    "code/controls_v2.py", "runs/n04-controls-v9/controls.json",
    "code/make_audit_mutants_v2.py", "runs/n06-mutants-v3/mutants.json",
    "runs/n07-audit3-LW_notatest/cover.json", "runs/n07-audit3-LW_fail/cover.json",
    "runs/n07-audit3-LW_deep/cover.json", "runs/n07-audit3-G_corner/cover.json",
    "runs/n07-audit3-LD2_Pskip/cover.json", "runs/n07-audit3-SWC_domain/cover.json",
    "runs/n07-audit3-G_params/cover.json", "runs/n07-audit3-LW_summary/cover.json",
    "runs/n07-audit3-LW_wrongsummary/cover.json",
    # dependency closure: launcher, guard, runtime identity, binding smoke
    "code/run_v1.sh", "code/lane_guard.py", "reductions/code/lane_guard.py",
    "code/runtime_identity_v1.py", "runs/r01-runtime/runtime.json",
    "code/binding_smoke_v2.py", "runs/s02-binding/binding.json",
    # float audit
    "code/audit_float_v1.py", "runs/f01-float-audit/static_sites.json", "runs/f01-float-audit/static_sites.txt",
    "runs/f01-float-audit/trace.json",
    # certificate index
    "code/index_certificates_v3.py", "runs/i02-index/certificate_index.json",
    # other certified charts (unchanged): code, specs, runs
    "code/cert_primal_v3.py", "code/me3lib_v1.py", "code/me3jet_v1.py", "code/me3jet_v2.py",
    "code/spec_primal_P_v1.json", "runs/c03-primalP/primal.json", "runs/c03-primalP/leaves.txt.gz",
    "code/cert_dual_v5.py", "code/me3dual_v7.py", "code/me3dual_v6.py", "code/me3dual_v4.py", "code/me3dual_v3.py",
    "code/spec_dual_v1.json", "receipts/spec-dual-freeze-v1.json",
    "runs/d01-G/dual.json", "runs/d01-G/leaves.txt.gz", "runs/d01-SWB/dual.json", "runs/d01-SWB/leaves.txt.gz",
    "runs/d01-LW/dual.json", "runs/d01-LW/leaves.txt.gz", "runs/d01-LD1/dual.json", "runs/d01-LD1/leaves.txt.gz",
    "runs/d01-LD2/dual.json", "runs/d01-LD2/leaves.txt.gz",
    "code/controls_v1.py", "runs/n01-controls/controls.json",
    # reductions
    "reductions/proof/reductions-v1.md", "reductions/proof/vcos-lower-bound-v1.md", "reductions/STATUS.md",
    "reductions/replay/REPLAY-STATUS-v2.md",
] + EXTRA
INVALID = ["receipts/me3-candidate-pin-v1.json", "runs/p01-pin/manifest.json", "runs/d02-SWC/dual.json",
           "runs/d02-SWC/leaves.txt.gz", "code/me3dual_v8.py", "code/cert_dual_v6.py", "code/spec_dual_v2.json",
           "receipts/spec-dual-freeze-v2.json", "proof/me3-theorem-v3.md"]
missing = [k for k in KEY + INVALID if k not in manifest]
assert not missing, f"missing key files: {missing}"
rt = json.load(open(L + "runs/r01-runtime/runtime.json"))
EXT = {"review/me3-charts-codex-v1.note.md": R + "me3-charts-codex-v1.note.md",
       "review/me3-reductions-codex-v1.note.md": R + "me3-reductions-codex-v1.note.md",
       "review/me3-parent-primal-reductions-v1/RESULT-v1.json": R + "me3-parent-primal-reductions-v1/RESULT-v1.json"}
pin = {
    "event": "ME3 minimum-SCV worker candidate RE-PINNED as v2 after the SWC repair (worker MathPhaseType3); unreviewed "
             "as a whole; correctness only",
    "pinned_at_host_clock": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    "contract": "institute/runs/six-lane-2026-10-16/screening/math-1-me3-minimum-scv-contract.json",
    "claim": ("Every continuous ME(<=3) law has SCV >= v_cos := min over omega>0, phi of SCV(e^{-t}(1-cos(omega t - phi))); "
              "attained in D1; strict (> v_cos) for every D2 cone; real exponents give SCV >= Delta_3 > 0.2765."),
    "status": "CANDIDATE v2 (full statement; no uncovered pole region); parent dual replay of SWC against d03 pending",
    "supersedes": {"receipts/me3-candidate-pin-v1.json": "INVALID: SWC run d02 used me3dual_v8.py:28 float-rounded "
                   "coefficients (hostile review me3-charts-codex-v1 finding 1); kept as failed evidence"},
    "invalid_evidence_kept": {k: manifest[k]["sha256"] for k in INVALID},
    "claim_limits": ["no novelty/priority/'first' claim", "no Lean/kernel check",
                     "trusted import: FLINT/Arb outward-correct ball arithmetic and the python-flint conversions listed "
                     "in proof/float-audit-v1.md (smoke-tested in run s02, not proved)",
                     "not the book's general minimal-representation question"],
    "runtime": {k: rt[k] for k in ("python_version", "executable_realpath", "executable_sha256",
                                    "python_framework_library", "python_framework_library_sha256",
                                    "python_flint_version", "FLINT_version", "platform", "sympy_version",
                                    "mpmath_version")},
    "key_files": {k: manifest[k]["sha256"] for k in KEY},
    "external_citations_sha256": {k: sha(v) for k, v in EXT.items()},
    "manifest": {"path": os.path.relpath(RUN + "/manifest.json", L), "sha256": man_sha, "files": len(manifest)},
}
with lane_guard.xopen(L + "receipts/me3-candidate-pin-v2.json") as fh:
    json.dump(pin, fh, indent=1)
print(json.dumps({"manifest_files": len(manifest), "manifest_sha256": man_sha, "key_files": len(KEY),
                  "pin_sha256": sha(L + "receipts/me3-candidate-pin-v2.json")}))
