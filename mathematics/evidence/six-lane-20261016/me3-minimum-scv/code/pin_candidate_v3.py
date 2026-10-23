"""Bookkeeping: pin the worker candidate, version 3. No mathematical computation; no certificate or evaluator changed
since pin v2. pin_candidate_v1.py and pin_candidate_v2.py and their pins are kept. Pin v1 is INVALID (SWC run d02).
Pin v2 is SUPERSEDED: theorem v4 has a cone-definition regression in §2 and wording issues, per hostile delta review
me3-charts-v2-delta-codex-v1. Pin v3 adds proof v5, reductions v4 (resultant normalization plus the Claude reductions
review fixes), the float-audit erratum, the provenance binding audit b04 with its controls, comparison-contract smoke
s04, and explicit key-file entries for charts-spec-v1 and for every receipt of the active runs and audits.

argv[1] = run directory; argv[2:] = extra lane-relative key files (e.g. subagent outputs).
Writes, exclusively, <run>/manifest.json (SHA-256 + size of every file under proof/, code/, receipts/, reductions/,
runs/, sources/, independent-float-audit/ and README.md, excluding tmp/ and this run's directory) and
receipts/me3-candidate-pin-v3.json. Every key file must exist in the manifest; a missing artifact aborts the pin.
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

ACTIVE_RUNS = ["c03-primalP", "d01-G", "d01-SWB", "d01-LW", "d01-LD1", "d01-LD2", "d03-SWC",
               "b03-cover-P", "b03-cover-G", "b03-cover-SWB", "b03-cover-SWC", "b03-cover-LW", "b03-cover-LD1",
               "b03-cover-LD2", "b04-bind", "i02-index", "r01-runtime", "s02-binding", "s04-binding",
               "f01-float-audit", "n01-controls", "n04-controls-v9", "n06-mutants-v3", "p02-pin"] + \
              [f"n07-audit3-{m}" for m in ("LW_notatest", "LW_fail", "LW_deep", "G_corner", "LD2_Pskip", "SWC_domain",
                                           "G_params", "LW_summary", "LW_wrongsummary")]
RED_RUNS = ["exact-certs-v1", "resultant-check-v1", "ctl-f-main-v1", "ctl-f-gradsym-v1", "audit-bnb-v2"]
KEY = [
    # proof documents (charts-spec-v1 explicit: inherited definitions, delta review finding 2)
    "proof/me3-theorem-v5.md", "proof/me3-theorem-v5.diff-from-v4.txt", "proof/charts-spec-v1.md",
    "proof/charts-spec-v2.md", "proof/float-audit-v1.md", "proof/float-audit-v1-erratum-1.md",
    # provenance binding audit and comparison-contract smoke
    "code/bind_audit_v1.py", "runs/b04-bind/binding.json", "runs/b04-bind/mutant_spec_dual_v3_interior.json",
    "runs/b04-bind/mutant_spec_primal_P_swapsplit.json", "runs/b04-bind/mutant_pin_v2.json",
    "code/binding_smoke_v4.py", "runs/s04-binding/binding.json",
    # SWC repair
    "code/me3dual_v9.py", "code/cert_dual_v7.py", "code/spec_dual_v3.json", "receipts/spec-dual-freeze-v3.json",
    "runs/d03-SWC/dual.json", "runs/d03-SWC/leaves.txt.gz",
    # geometry checker and its outputs
    "code/check_cover_v3.py",
    "runs/b03-cover-P/cover.json", "runs/b03-cover-G/cover.json", "runs/b03-cover-SWB/cover.json",
    "runs/b03-cover-SWC/cover.json", "runs/b03-cover-LW/cover.json", "runs/b03-cover-LD1/cover.json",
    "runs/b03-cover-LD2/cover.json",
    # controls
    "code/controls_v1.py", "runs/n01-controls/controls.json", "code/controls_v2.py", "runs/n04-controls-v9/controls.json",
    "code/make_audit_mutants_v2.py", "runs/n06-mutants-v3/mutants.json",
    # dependency closure
    "code/run_v1.sh", "code/lane_guard.py", "reductions/code/lane_guard.py",
    "code/runtime_identity_v1.py", "runs/r01-runtime/runtime.json", "code/binding_smoke_v2.py",
    "runs/s02-binding/binding.json",
    # float audits
    "code/audit_float_v1.py", "runs/f01-float-audit/static_sites.json", "runs/f01-float-audit/static_sites.txt",
    "runs/f01-float-audit/trace.json", "independent-float-audit/report-v1.md",
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
    # previous pin (superseded; anchor of the binding audit)
    "receipts/me3-candidate-pin-v2.json", "runs/p02-pin/manifest.json",
    # reductions
    "reductions/proof/reductions-v1.md", "reductions/proof/vcos-lower-bound-v1.md", "reductions/STATUS.md",
    "reductions/proof/reductions-v2.md", "reductions/STATUS-v2.md", "reductions/proof/reductions-v3.md",
    "reductions/STATUS-v3.md", "reductions/proof/reductions-v3.diff-from-v2.txt",
    "reductions/code/exact_certs_v1.py", "reductions/runs/exact-certs-v1/exact_certs.json",
    "reductions/code/resultant_check_v1.py", "reductions/runs/resultant-check-v1/resultant_check.json",
    "reductions/code/ctl_f_d1bnb_v1.py", "reductions/code/ctl_f_gradsym_v1.py",
    "reductions/runs/ctl-f-main-v1/ctl_f.json", "reductions/runs/ctl-f-gradsym-v1/ctl_f_gradsym.json",
    "reductions/code/audit_bnb_v2.py", "reductions/runs/audit-bnb-v2/audit_bnb.json",
    "reductions/replay/REPLAY-STATUS-v2.md",
]
KEY += [f"receipts/{r}-{s}.json" for r in ACTIVE_RUNS for s in ("pre", "post")]
KEY += [f"reductions/receipts/{r}-{s}.json" for r in RED_RUNS for s in ("pre", "post")]
KEY += [f"runs/n07-audit3-{m}/cover.json" for m in ("LW_notatest", "LW_fail", "LW_deep", "G_corner", "LD2_Pskip",
                                                     "SWC_domain", "G_params", "LW_summary", "LW_wrongsummary")]
KEY += [k for k in EXTRA if k not in KEY]
INVALID = ["receipts/me3-candidate-pin-v1.json", "runs/p01-pin/manifest.json", "runs/d02-SWC/dual.json",
           "runs/d02-SWC/leaves.txt.gz", "code/me3dual_v8.py", "code/cert_dual_v6.py", "code/spec_dual_v2.json",
           "receipts/spec-dual-freeze-v2.json", "proof/me3-theorem-v3.md"]
SUPERSEDED = {"receipts/me3-candidate-pin-v2.json": "pin v2: theorem v4 cone-definition regression and wording "
                                                     "(delta review me3-charts-v2-delta-codex-v1); no certificate changed",
              "proof/me3-theorem-v4.md": "replaced by proof v5 (cone definition, CERT-leaf wording, comparison "
                                         "contract, D1 citation, strictness citation)",
              "reductions/proof/reductions-v2.md": "replaced by reductions-v4",
              "reductions/proof/reductions-v3.md": "resultant fix only; replaced by reductions-v4 (all fixes)",
              "code/binding_smoke_v3.py": "failed attempt (wrong B10a expectation); replaced by binding_smoke_v4.py"}
missing = [k for k in KEY + INVALID + list(SUPERSEDED) if k not in manifest]
assert not missing, f"missing key files: {missing}"
rt = json.load(open(L + "runs/r01-runtime/runtime.json"))
bind = json.load(open(L + "runs/b04-bind/binding.json"))
assert bind["all_bound"] is True and bind["controls_ok"] is True, "binding audit not clean"
EXT = {"review/me3-charts-codex-v1.note.md": R + "me3-charts-codex-v1.note.md",
       "review/me3-reductions-codex-v1.note.md": R + "me3-reductions-codex-v1.note.md",
       "review/me3-charts-v2-delta-codex-v1.note.md": R + "me3-charts-v2-delta-codex-v1.note.md",
       "review/me3-reductions-claude-v1.note.md": R + "me3-reductions-claude-v1.note.md",
       "review/me3-parent-primal-reductions-v1/RESULT-v1.json": R + "me3-parent-primal-reductions-v1/RESULT-v1.json",
       "review/me3-v2-parent-pin-closure-v1.json": R + "me3-v2-parent-pin-closure-v1.json"}
pin = {
    "event": "ME3 minimum-SCV worker candidate RE-PINNED as v3 (worker MathPhaseType3): document fixes and provenance "
             "binding after the hostile delta and reductions reviews; no certificate or evaluator changed since pin v2",
    "pinned_at_host_clock": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    "contract": "institute/runs/six-lane-2026-10-16/screening/math-1-me3-minimum-scv-contract.json",
    "claim": ("Every continuous ME(<=3) law has SCV >= v_cos := min over omega>0, phi of SCV(e^{-t}(1-cos(omega t - phi))); "
              "attained in D1; strict (> v_cos) for every D2 cone; real exponents give SCV >= Delta_3 > 553/2000."),
    "status": "CANDIDATE v3 (full statement; no uncovered pole region); unreviewed as a whole; correctness only",
    "supersedes": SUPERSEDED,
    "invalid_evidence_kept": {k: manifest[k]["sha256"] for k in INVALID},
    "claim_limits": ["no novelty/priority/'first' claim", "no Lean/kernel check",
                     "trusted import: FLINT/Arb outward-correct ball arithmetic and the python-flint conversion and "
                     "comparison semantics of proof/me3-theorem-v5.md section 6 (smoke-tested in runs s02/s04, not proved)",
                     "receipts are written by the lane's own launcher; binding audit b04 checks their mutual consistency "
                     "and their agreement with the pre-run freeze receipts and pin v2",
                     "not the book's general minimal-representation question"],
    "binding_audit": {"run": "b04-bind", "all_bound": bind["all_bound"], "controls_ok": bind["controls_ok"],
                      "anchor_pin_v2_sha256": bind["anchor_pin"]["sha256"]},
    "runtime": {k: rt[k] for k in ("python_version", "executable_realpath", "executable_sha256",
                                    "python_framework_library", "python_framework_library_sha256",
                                    "python_flint_version", "FLINT_version", "platform", "sympy_version",
                                    "mpmath_version")},
    "key_files": {k: manifest[k]["sha256"] for k in KEY},
    "external_citations_sha256": {k: sha(v) for k, v in EXT.items()},
    "manifest": {"path": os.path.relpath(RUN + "/manifest.json", L), "sha256": man_sha, "files": len(manifest)},
}
with lane_guard.xopen(L + "receipts/me3-candidate-pin-v3.json") as fh:
    json.dump(pin, fh, indent=1)
print(json.dumps({"manifest_files": len(manifest), "manifest_sha256": man_sha, "key_files": len(KEY),
                  "pin_sha256": sha(L + "receipts/me3-candidate-pin-v3.json")}))
