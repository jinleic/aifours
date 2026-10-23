#!/usr/bin/env python3
"""result_v1.py -- final RESULT of the ME3ParentDual desk (no evaluation; assembles frozen run outputs).

Usage: python -I -B result_v1.py OUT.json --pin PIN.json --closure CLOSURE.json CLOSURE_SHA
          --chart LW=r.json --chart LD1=r.json --chart LD2=r.json --chart SWB=r.json --chart SWC=r.json
          --g-assembly G.json --controls C.json --controls-extra C4G.json --identities I.json [I.json ...]
          --float-audit F.json
Acceptance per chart: full-chart result (or, for G, the shard assembly) with verdict PASS, run on the given pin,
zero failures, no tiling errors, hashes matching the claim, post receipt binding leaves and dual.json.  Aggregate PASS
iff all six charts accepted, the controls pass (C4.1-C4.3 of controls_v2 may be replaced by the supplementary
control file, which must then pass in full), and the identity runs report all items true (r02 item I15 is accepted
only via the I15 addendum file).  Writes OUT (exclusive).
"""
import sys
import json
import hashlib
import time

argv = sys.argv[1:]
OUT = argv.pop(0)
opts = {"chart": [], "identities": []}
i = 0
while i < len(argv):
    a = argv[i]
    if a == "--chart":
        opts["chart"].append(argv[i + 1]); i += 2
    elif a == "--identities":
        i += 1
        while i < len(argv) and not argv[i].startswith("--"):
            opts["identities"].append(argv[i]); i += 1
    elif a == "--closure":
        opts["closure"] = (argv[i + 1], argv[i + 2]); i += 3
    else:
        opts[a[2:]] = argv[i + 1]; i += 2


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


pin_sha = sha(opts["pin"])
pin = json.load(open(opts["pin"]))
INEQ = {
    "LW": "SMALL: |W|_box < exp(-2 pi delta_h nu_h) (nu = 1/omega)",
    "LD1": "fallback |W| < exp(-(1-d_l) 2pi/tan beta_l); principal Re P>0, alpha=beta+atan(Im P/Re P)>=0, "
           "|W| < exp(-(1-d_l) alpha_h/tan beta_l); mvt0 (beta_l=0) Re P>0, U=1+Im(P_beta/P)>=0, |W| < exp(-(1-d_l) U_h)",
    "LD2": "same three tests for Phat with factor 1 >= 1-d; SKIP-s chi_l rho_l > 1/16 exact; SKIP-d (1-chi_h) rho_l > cos(beta_l)/65",
    "G": "SMALL |W| < exp(-2pi delta_h/omega_l); RADIAL on a certified branch (Im W>0 | Im W<0 | Re W<0): "
         "omega log|W| + delta alpha < 0 naive or MVF; TRIANGLE in balls; SKIP omega_h<=40, omega_l>=1/5, delta_h<=3 omega_l exact",
    "SWB": "Taylor in omega: S = (g - delta g') + omega^2(-g''/2 + delta g'''/6), S + omega_h^4(M4/24 + delta_h M5/120) < 0 and "
           "-g' + omega^2 g'''/6 - omega_h^4 M5/120 > 0 (naive or MVF on the smooth part); M_k by the root form",
    "SWC": "series with N=20 and tails: Psi_N + tailPsi < 0 and Ig_N - tailIg > 0 (naive or MVF on the polynomial part); "
           "exact coefficients (-2 Re p^j + 3(-1)^j)/j, rho x < 1, x < 1",
}
charts, problems = {}, []
for item in opts["chart"]:
    name, path = item.split("=", 1)
    r = json.load(open(path))
    b = r["binding"]
    ok = (r.get("verdict") == "PASS" and r.get("scope_full_chart") and r["n_failures"] == 0 and not r["tiling_errors"]
          and not r["spec_problems"] and r["leaf_lines_match"] and r["claimed_counts_match_dual"]
          and r["leaves_rehash_after"]["unchanged"] and b["post_receipt_binds_leaves"] and b["post_receipt_binds_dual"]
          and b["post_receipt_exit_code"] == 0 and r["chart"] == name and r["pin"]["sha256"] == pin_sha)
    if not ok:
        problems.append("chart %s not accepted" % name)
    charts[name] = {
        "accepted": bool(ok), "result_file": path, "result_sha256": sha(path), "checker": r["tool"],
        "checker_sha256": r["tool_sha256"], "run": pin["charts"][name]["run"],
        "inputs_sha256": {k: b[k]["sha256"] for k in ("spec", "leaves", "dual", "post_receipt")},
        "leaf_file_bytes": b["leaves"]["bytes"], "leaf_lines_sha256": r["leaf_lines_sha256"],
        "coverage": {"cells": r["cells"], "lines": r["lines"], "evaluated_leaves": r["evaluated_leaves"],
                     "tiling_errors": len(r["tiling_errors"]), "max_depth_seen": r["max_depth_seen"]},
        "claimed_counts": r["claimed_counts"], "verification_table": r["verification_table"],
        "skip_rule_ok": r["skip_rule_ok"], "subdivision": r["subdivision"], "failures": r["n_failures"],
        "inequalities": INEQ[name], "wall_seconds": r["wall_seconds"]}
g = json.load(open(opts["g-assembly"]))
gok = g["verdict"] == "PASS" and g["pin_sha256"] == pin_sha and not g["problems"]
if not gok:
    problems.append("G assembly not accepted")
charts["G"] = {"accepted": bool(gok), "result_file": opts["g-assembly"], "result_sha256": sha(opts["g-assembly"]),
               "checker_sha256": g["tool_sha256"], "run": pin["charts"]["G"]["run"], "inputs_sha256": g["inputs"],
               "leaf_lines_sha256": g["leaf_lines_sha256"],
               "coverage": {"cells": g["cells"], "lines": g["lines"], "evaluated_leaves": g["evaluated_leaves"],
                            "shards": [s["cells"] for s in g["shards"]], "max_depth_seen": g["max_depth_seen"]},
               "claimed_counts": g["claimed_counts"], "verification_table": g["verification_table"],
               "skip_rule_ok": g["skip_rule_ok"], "subdivision": g["subdivision"], "failures": 0 if gok else None,
               "inequalities": INEQ["G"]}
missing = [c for c in ("LW", "LD1", "LD2", "G", "SWB", "SWC") if c not in charts]
if missing:
    problems.append("missing charts %r" % missing)
ctl = json.load(open(opts["controls"]))
ext = json.load(open(opts["controls-extra"]))
replaced = {"C4.1 G principal Arg on an Im W<0 box", "C4.2 G branch 'up' forced on an Im W<0 box",
            "C4.3 same box, checker's own branch logic (positive)"}
failed = [k for k, v in ctl["controls"].items() if v["pass"] is False]
ctl_ok = all(k in replaced for k in failed) and (not failed or ext["all_pass"])
if not ctl_ok:
    problems.append("controls not passing: %r" % failed)
ids = {}
ids_ok = True
for p in opts["identities"]:
    j = json.load(open(p))
    false_items = [k for k, v in j.items() if v is False and k not in ("all_true",)]
    ids[p] = {"sha256": sha(p), "false_items": false_items}
    ids_ok = ids_ok and all(k == "I15_f0_moments" or k.startswith("I15") for k in false_items)
i15_ok = any(json.load(open(p)).get("antiderivative_t^k_e^{-zt}_k0..2") is True and json.load(open(p)).get("all_true")
             for p in opts["identities"])
if not (ids_ok and i15_ok):
    problems.append("identities not all established")
cl_path, cl_sha = opts["closure"]
cl_ok = sha(cl_path) == cl_sha
if not cl_ok:
    problems.append("parent closure sha mismatch")
res = {
    "event": "ME3ParentDual FINAL RESULT (dual charts LW, LD1, LD2, G, SWB, SWC; not P, not reductions)",
    "at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
    "pin": {"path": opts["pin"], "sha256": pin_sha, "candidate_pin": pin["candidate_pin"], "index": pin.get("index")},
    "parent_pin_closure": {"path": cl_path, "sha256": cl_sha, "verified": cl_ok},
    "not_used": "worker candidate pin v1 (receipts/me3-candidate-pin-v1.json) and SWC run d02 are not used for any verdict "
                "here; every chart result cited below was produced with the desk pin above (candidate pin v2).",
    "charts": charts,
    "controls": {"file": opts["controls"], "sha256": sha(opts["controls"]), "failed_items": failed,
                 "not_applicable": ctl["not_applicable"], "supplement": {"file": opts["controls-extra"],
                 "sha256": sha(opts["controls-extra"]), "all_pass": ext["all_pass"]}, "accepted": bool(ctl_ok)},
    "identities": ids,
    "float_audit": {"file": opts["float-audit"], "sha256": sha(opts["float-audit"])},
    "trusted": ["Arb ball arithmetic via python-flint 0.9.0 at 128 bits (same library as the worker: not an independent "
                "numerical kernel)", "CPython 3.14.3 / sympy 1.14.0 for exact identities"],
    "format_dependency": "leaf-line serialization and split order taken from the producer (labelled in dualcheck_v2.py); "
                         "boxes rebuilt independently; tiling audited by the DFS successor rule",
    "scope_limits": ["primal chart P, Lemma M, reductions L1-L6, Delta_3 and v_cos are not covered by this desk",
                     "global assembly and gate decision belong to the parent"],
    "problems": problems,
    "aggregate": "PASS" if not problems else ("INCOMPLETE" if missing else "FAIL"),
}
with open(OUT, "x") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({"aggregate": res["aggregate"], "problems": problems,
                  "accepted": {c: charts[c]["accepted"] for c in charts}}))
