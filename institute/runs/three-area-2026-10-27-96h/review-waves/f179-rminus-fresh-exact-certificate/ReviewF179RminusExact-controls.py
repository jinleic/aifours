#!/usr/bin/env python3
"""ReviewF179RminusExact: one-shot receipted control driver.

Runs every case as its own subprocess (max 120 s each; a reached cap is UNKNOWN, never
acceptance), records real UTC clock, monotonic duration, exit code and SHA-256 of the
captured stdout, writes each stdout to an exclusive-create reviewer file and judges each
control against its PRE-STATED intended reason.  Writes one exclusive-create receipt file.
"""
import datetime
import hashlib
import json
import subprocess
import sys
import time

DIR = "/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f179-rminus-fresh-exact-certificate/"
PY = sys.executable
VER = DIR + "ReviewF179RminusExact-verify.py"
SELF = DIR + "ReviewF179RminusExact-semantic-selftest.py"
FIG = DIR + "ReviewF179RminusExact-fig2-vector-extract.py"
CAP = 120

# name, argv, expected status, expected exit, required codes, forbidden codes, need delta check, intent
CASES = [
    ("none", [VER], "VALID", 0, [], [], False, "positive: unmutated certificate must be VALID"),
    ("flip_sign_cmi", [VER, "--mutate", "flip_sign_cmi"], "INVALID", 1,
     ["SIGN_GE0_POSITIVE", "IDENTITY_RESIDUAL"], [], True, "multiplier sign on a >=0 row"),
    ("cap_value", [VER, "--mutate", "cap_value"], "INVALID", 1,
     ["IDENTITY_RESIDUAL", "BOUND_MISMATCH"], [], True, "cap multiplier 280/107 -> 281/107"),
    ("cap_vertex", [VER, "--mutate", "cap_vertex"], "INVALID", 1,
     ["IDENTITY_RESIDUAL"], ["BOUND_MISMATCH"], True, "cap row moved from X4 to X3 (sum unchanged)"),
    ("program_overset_drop", [VER, "--mutate", "program_overset_drop"], "INVALID", 1,
     ["COPY_U_NOT_IN_OVERSET"], [], False, "program m4 step 0 over-set loses X10 used by mcopy U"),
    ("program_overset_add", [VER, "--mutate", "program_overset_add"], "INVALID", 1,
     ["IDENTITY_RESIDUAL"], ["COPY_U_NOT_IN_OVERSET"], False, "program m4 step 0 over-set gains X3"),
    ("future_copy_ref", [VER, "--mutate", "future_copy_ref"], "INVALID", 1,
     ["PROGRAM_FUTURE_REFERENCE"], [], False, "m4 step 1 over-set references future copy c2"),
    ("future_copy_self", [VER, "--mutate", "future_copy_self"], "INVALID", 1,
     ["PROGRAM_FUTURE_REFERENCE"], [], False, "m4 step 1 over-set references its own copy c1"),
    ("chronology_final_E", [VER, "--mutate", "chronology_final_E"], "INVALID", 1,
     ["IDENTITY_RESIDUAL"], [], False, "independence taken against final (future) variable set"),
    ("graph_fd_nbr", [VER, "--mutate", "graph_fd_nbr"], "INVALID", 1,
     ["IDENTITY_RESIDUAL"], ["GRAPH_AUTOMORPHISM_FAIL"], False, "FD row of X1 uses N(1) minus 7"),
    ("graph_edge_9_10", [VER, "--mutate", "graph_edge_9_10"], "INVALID", 1,
     ["GRAPH_AUTOMORPHISM_FAIL", "IDENTITY_RESIDUAL"], [], False, "graph R (edge 9-10 added)"),
    ("graph_drop_3_4", [VER, "--mutate", "graph_drop_3_4"], "INVALID", 1,
     ["GRAPH_AUTOMORPHISM_FAIL", "IDENTITY_RESIDUAL"], [], False, "edge 3-4 removed"),
    ("drop_row_dfz", [VER, "--mutate", "drop_row_dfz"], "INVALID", 1,
     ["IDENTITY_RESIDUAL", "SUPPORT_COUNT_MISMATCH"], [], True, "the single DFZ row dropped"),
    ("drop_row_cmi", [VER, "--mutate", "drop_row_cmi"], "INVALID", 1,
     ["IDENTITY_RESIDUAL", "SUPPORT_COUNT_MISMATCH"], [], True, "first cmi row dropped"),
    ("dup_json_key", [VER, "--mutate", "dup_json_key"], "INVALID", 1,
     ["JSON_DUPLICATE_KEY"], [], False, "duplicate top-level key injected into raw bytes"),
    ("cross_branch_varlist", [VER, "--mutate", "cross_branch_varlist"], "INVALID", 1,
     ["VARLIST_NOT_A_BRANCH", "IDENTITY_RESIDUAL"], [], True, "P3 cmi row given P2 copy g'2"),
    ("dfz_coeff", [VER, "--mutate", "dfz_coeff"], "INVALID", 1,
     ["DFZ_TUPLE_NOT_IN_SOURCE", "DFZ_TUPLE_NOT_DECLARED", "IDENTITY_RESIDUAL"], [], True,
     "DFZ tuple a: 3 -> 4"),
    ("copy_u_outside", [VER, "--mutate", "copy_u_outside"], "INVALID", 1,
     ["COPY_U_NOT_IN_OVERSET", "IDENTITY_RESIDUAL"], [], True, "publisher copy row U gains X4"),
    ("xcopy_u_outside", [VER, "--mutate", "xcopy_u_outside"], "INVALID", 1,
     ["COPY_U_NOT_IN_OVERSET", "IDENTITY_RESIDUAL"], [], True, "extra-copy row U gains X1"),
    ("hash_pin_wrong", [VER, "--mutate", "hash_pin_wrong"], "BINDING_FAILURE", 3,
     ["INPUT_HASH_MISMATCH"], [], False, "wrong pinned certificate SHA-256"),
    ("probe_sym_sigma_inverse", [VER, "--mutate", "sym_sigma_inverse"], "INVALID", 1,
     ["IDENTITY_RESIDUAL"], ["GRAPH_AUTOMORPHISM_FAIL"], False,
     "encoding probe: sym rows read with sigma^-1 (still valid rows) must not balance"),
    ("probe_qmask_bit_order", [VER, "--mutate", "qmask_bit_order"], "INVALID", 1,
     ["IDENTITY_RESIDUAL"], [], False, "encoding probe: two-entry Q bit order swapped"),
    ("probe_indep_orientation_plus", [VER, "--mutate", "indep_orientation_plus"], "INVALID", 1,
     ["IDENTITY_RESIDUAL"], [], False, "encoding probe: independence rows read as +I"),
    ("timeout_probe", [VER, "--sleep", "10"], "TIMEOUT", None, [], [], False,
     "driver cap probe with 3 s cap: must be UNKNOWN, never acceptance"),
    ("semantic_selftest", [SELF], "SELFTEST", 0, [], [], False, "float self-test on genuine copy laws"),
    ("fig2_vector_extract", [FIG], "FIG2", 0, [], [], False, "Fig. 2 vector edge extraction"),
]


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="microseconds")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    rec = {"driver_sha256": sha(open(__file__, "rb").read()), "python": sys.version,
           "verifier_sha256": sha(open(VER, "rb").read()), "selftest_sha256": sha(open(SELF, "rb").read()),
           "fig2_sha256": sha(open(FIG, "rb").read()), "started_utc": now(), "cases": []}
    allpass = True
    for name, argv, est, eexit, req, forb, need_delta, intent in CASES:
        cap = 3 if name == "timeout_probe" else CAP
        out_path = DIR + "ReviewF179RminusExact-control-%s.json" % name
        t_start, m0 = now(), time.monotonic()
        try:
            p = subprocess.run([PY] + argv, capture_output=True, timeout=cap, cwd=DIR)
            code, so, se, timed = p.returncode, p.stdout, p.stderr, False
        except subprocess.TimeoutExpired as e:
            code, so, se, timed = None, e.stdout or b"", e.stderr or b"", True
        dur = round(time.monotonic() - m0, 3)
        t_end = now()
        with open(out_path, "xb") as f:
            f.write(so)
        c = {"case": name, "intent": intent, "argv": [PY] + argv, "cap_s": cap, "start_utc": t_start,
             "end_utc": t_end, "duration_s": dur, "exit": code, "timed_out": timed,
             "stdout_file": out_path, "stdout_sha256": sha(so), "stdout_bytes": len(so),
             "stderr_sha256": sha(se), "stderr_head": se[:400].decode("utf-8", "replace")}
        verdict, why = False, ""
        if timed:
            c["classification"] = "UNKNOWN (cap reached; never acceptance)"
            verdict = est == "TIMEOUT"
            why = "timed out as designed" if verdict else "unexpected timeout"
        else:
            try:
                d = json.loads(so)
            except ValueError:
                d = None
            if est in ("SELFTEST", "FIG2"):
                key = "selftest_pass" if est == "SELFTEST" else "equals_hand_transcription"
                ok = d is not None and d.get(key) is True and code == eexit
                c["classification"] = "PASS" if ok else "FAIL"
                verdict, why = ok, "%s=%r exit=%r" % (key, None if d is None else d.get(key), code)
            elif d is None:
                c["classification"] = "UNPARSEABLE"
                why = "stdout not JSON"
            else:
                codes = d.get("reason_codes", [])
                info = d.get("info", {})
                c["status"], c["reason_codes"] = d.get("status"), codes
                c["residual_equals_intended_delta"] = info.get("residual_equals_intended_delta")
                c["cap_sum"], c["total_at_target"] = info.get("cap_sum"), info.get("total_at_target")
                ok = (d.get("status") == est and code == eexit and all(r in codes for r in req)
                      and not any(r in codes for r in forb))
                if need_delta:
                    ok = ok and info.get("residual_equals_intended_delta") is True
                if name == "none":
                    ok = ok and info.get("cap_sum") == "716/107" and info.get("total_at_target") == "1" \
                        and info.get("residual_nonzero_coordinates") == 0 and info.get("records") == 2377
                verdict = ok
                why = "status=%s exit=%s codes=%s" % (d.get("status"), code, codes)
                c["classification"] = d.get("status")
        c["control_as_intended"] = verdict
        c["judgement"] = why
        allpass = allpass and verdict
        rec["cases"].append(c)
    rec["finished_utc"] = now()
    rec["all_controls_as_intended"] = allpass
    rp = DIR + "ReviewF179RminusExact-control-receipts.json"
    body = (json.dumps(rec, indent=1, sort_keys=True) + "\n").encode()
    with open(rp, "xb") as f:
        f.write(body)
    print(json.dumps({"receipts": rp, "receipts_sha256": sha(body), "all_controls_as_intended": allpass,
                      "cases": [[c["case"], c["control_as_intended"], c.get("classification"), c["duration_s"]]
                                for c in rec["cases"]]}, indent=1))
    return 0 if allpass else 1


if __name__ == "__main__":
    sys.exit(main())
