#!/usr/bin/env python3
"""Addenda for the parent F_one replay desk (review/moqls8-fone-parent-replay-v1). Launches no child processes.

  addenda_v1.py correction OUT           append the parent's control-design correction for the already-run
                                         controls (receipts retained unchanged; no relabel; no native re-run)
  addenda_v1.py inventory OUT            pin the added-six inventory/delta before its run
  addenda_v1.py result OUT PREEXEC...    final RESULT.json over receipts, run summaries and addenda

Loads this desk's own scripts/replay_v1.py by path after checking its sha256 against PRE-EXEC.json; imports no lane
code. Run as /usr/bin/python3 -I -B with TMPDIR=<desk>/tmp/.
"""
import glob
import hashlib
import importlib.util
import json
import os
import sys

DESK = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-fone-parent-replay-v1"
REPLAY = DESK + "/scripts/replay_v1.py"
REPLAY_SHA = "16cba374241636885d71f2e91dd3969d35779ccbe27eca4fc2bee3c8781f486d"
PRE1 = DESK + "/PRE-EXEC.json"
PRE1_SHA = "28dd7b34ebdec158abe1de80b49b43f0110fa24b7adb8f68460a80fc38306e9f"
SELF = os.path.realpath(__file__)
SELF_REL = "scripts/addenda_v1.py"
CORRECTION_REL = "CONTROL-CORRECTION-v1.json"
INVENTORY_REL = "INVENTORY-v2.json"
CONTROL_IDS = ("P0-B4", "P0-B5")
UNIT_DELETION_WARNING = b"ignores deletion of (pseudo) unit clause"
UP_LINE = b"c UNSAT via unit propagation on the input instance"

PARENT_CORRECTION = (
    "Parent control-design correction: first-template-unit sign flip is guaranteed to change the checker-feed HASH, "
    "but NOT guaranteed to make the formula SAT or invalidate the original proof (the contradiction may not use that "
    "unit). Therefore the scientifically sound acceptance expectation is `feed binding rejects mismatched checker "
    "hash`, with native proof outcome recorded honestly; `s VERIFIED` alone on that mutated input is not necessarily "
    "a checker defect. If controls already ran under the earlier expectation, retain their FAIL/anomaly receipts and "
    "append this correction; do not relabel old expected outcomes. If not yet run, preregister this correction before "
    "them. Existing SAT+bogus-proof parent checker controls already exercise unsound proof rejection. No duplicate "
    "native run merely to repair the label.")
PARENT_ADDED = (
    "Main: F_one16 producer pass is DONE. Worker is now static-only preparing refinement controller; no native "
    "pipeline until its new delta is parent-reviewed. This is an opportunity for your hard direct replays under the "
    "same guards-worker phase later regains priority. Expand your deterministic replay inventory to the other SIX "
    "strict producer candidates after the original six: P1-B4, P1-B6, P2-C1, P2-C2, P2-C3, P2-C4. Final worker "
    "RESULTS.jsonl SHAbcfeb441f49971e4c8241fbccdfec99a41c274e8b8af4261d17796ac4327ac19; LEDGER.v01740d8e7e7...2fac; "
    "META unchangedfec1ff0b...5e9a. UNKNOWN=P1-B1/B2/B3/B5-do NOT direct-rerun them. Extra producer solve/check"
    "total seconds4.1/48.5/198.3/202.2/48.5/34.4; maxpasspeak4.606GB(decimal). No old-F transfer, every new replay "
    "regenerates F_one and measures both actual CNF feeds. Pin new inventory/delta before added6 start; original "
    "snapshots unchanged. Refinement/native FIFO paths will be under "
    "LANE/evidence/n8_one_p4_template_runs_v1/refine_v2/<case>, so retain your joint path-marker scanner. Parent has "
    "NOT accepted the16-cover theorem; all12 direct leaves plus4 refinement covers remain necessary.")
ADDED = ("P1-B4", "P1-B6", "P2-C1", "P2-C2", "P2-C3", "P2-C4")
PARENT_SECONDS = {"P1-B4": 4.1, "P1-B6": 48.5, "P2-C1": 198.3, "P2-C2": 202.2, "P2-C3": 48.5, "P2-C4": 34.4}
UNKNOWN_NOT_RERUN = ("P1-B1", "P1-B2", "P1-B3", "P1-B5")
FINAL_RESULTS_SHA = "bcfeb441f49971e4c8241fbccdfec99a41c274e8b8af4261d17796ac4327ac19"
LEDGER_REL = "evidence/n8_one_p4_template_runs_v1/LEDGER.v017.json"
LEDGER_AFFIXES = ("40d8e7e7", "2fac")
META_REL = "evidence/n8_one_p4_template_runs_v1/META.1792312147.json"
META_SHA = "fec1ff0bdbd68f6eabffa3e674950793ad6102de741ac01943eb9b285a485e9a"
PARENT_MAX_PEAK = 4606066688


def die(msg):
    raise SystemExit("ABORT: %s" % msg)


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def load_replay():
    if os.environ.get("TMPDIR") != DESK + "/tmp/":
        die("TMPDIR must be %s/tmp/" % DESK)
    with open(REPLAY, "rb") as f:
        if sha_bytes(f.read()) != REPLAY_SHA:
            die("replay_v1.py sha256 changed")
    with open(PRE1, "rb") as f:
        raw = f.read()
    if sha_bytes(raw) != PRE1_SHA or json.loads(raw)["script"]["sha256"] != REPLAY_SHA:
        die("PRE-EXEC.json pin")
    spec = importlib.util.spec_from_file_location("replay_v1_desk", REPLAY)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    os.chdir(DESK + "/tmp")
    return mod


def cmd_correction(argv):
    R = load_replay()
    out = os.path.abspath(argv[0])
    if out != os.path.join(DESK, CORRECTION_REL) or os.path.lexists(out):
        die("output must be the new " + CORRECTION_REL)
    pre1 = json.loads(R.read_bytes(PRE1))
    prereg = {it["item"]: it for it in pre1["items"]}
    entries = []
    for cid in CONTROL_IDS:
        rpath = os.path.join(DESK, "receipts", "control-%s.json" % cid)
        lpath = os.path.join(DESK, "receipts", "%s.json" % cid)
        r = json.loads(R.read_bytes(rpath))
        leaf = json.loads(R.read_bytes(lpath))
        it, pl = r["item"], r["pipeline"]
        pit = prereg["control:" + cid]
        leaf_sha, mut_sha = pit["expected_solver_feed_sha256"], pit["expected_checker_feed_sha256"]
        mut_len = pit["expected_checker_feed_bytes"]
        if (it["expected_solver_feed_sha256"], it["expected_checker_feed_sha256"]) != (leaf_sha, mut_sha):
            die("receipt item differs from PRE-EXEC.json for " + cid)
        if leaf["verdict"] != "PASS" or leaf["item"]["expected_solver_feed_sha256"] != leaf_sha:
            die("leaf receipt for " + cid)
        cw, sw = pl["writers"]["checker_feed"], pl["writers"]["solver_feed"]
        logb = R.read_bytes(os.path.join(DESK, pl["checker_log"]))
        if sha_bytes(logb) != pl["checker_log_sha256"]:
            die("checker log differs from its receipt hash for " + cid)
        all_lines = [ln for ln in logb.replace(b"\r", b"").split(b"\n") if ln]
        kept = [ln.decode("ascii", "replace").rstrip() for ln in all_lines if UNIT_DELETION_WARNING not in ln]
        binding = (cw.get("ok") is True and cw.get("written") == mut_len and cw.get("sha256") == mut_sha
                   and cw.get("sha256") != leaf_sha)
        up = UP_LINE in all_lines
        entries.append({
            "id": cid, "receipt": R.rel(rpath), "receipt_sha256": R.sha_file(rpath),
            "leaf_receipt": R.rel(lpath), "leaf_receipt_sha256": R.sha_file(lpath), "leaf_verdict": leaf["verdict"],
            "recorded_verdict_unchanged": r["verdict"], "recorded_reasons_unchanged": r["reasons"],
            "original_preregistered_expectation_unchanged": pit["preregistered_expectation"],
            "mutation": pit["mutation"],
            "corrected_expectation": "feed binding rejects mismatched checker hash",
            "corrected_outcome": "BINDING_REJECTS_MISMATCH" if binding else "BINDING_DID_NOT_REJECT",
            "binding_evidence": {
                "expected_leaf_sha256": leaf_sha, "preregistered_mutant_sha256": mut_sha,
                "measured_checker_feed": {k: cw.get(k) for k in ("ok", "written", "expected_len", "sha256")},
                "measured_solver_feed": {k: sw.get(k) for k in ("ok", "written", "expected_len", "sha256")},
                "checker_feed_sha256_differs_from_leaf": cw.get("sha256") != leaf_sha,
                "checker_feed_sha256_equals_preregistered_mutant": cw.get("sha256") == mut_sha,
                "solver_feed_sha256_equals_leaf": sw.get("sha256") == leaf_sha,
                "strict_leaf_acceptance_would_reject": cw.get("sha256") != leaf_sha},
            "native_outcome_as_recorded": {
                "solver_rc": pl["children"].get("solver", {}).get("rc"),
                "solver_status_lines": pl["solver_status_lines"],
                "checker_rc": pl["children"].get("checker", {}).get("rc"),
                "checker_status_lines": pl["checker_status_lines"],
                "checker_log": pl["checker_log"], "checker_log_sha256": pl["checker_log_sha256"],
                "checker_log_lines_without_unit_deletion_warnings": kept,
                "unit_deletion_warning_lines_omitted": len(all_lines) - len(kept),
                "checker_reported_unsat_by_unit_propagation_on_input": up},
            "reading": ("drat-trim printed '%s' for the mutated checker-side formula (core of 4 input clauses, 1 lemma): "
                        "flipping the first template unit made that formula UNSAT by unit propagation alone, so "
                        "'s VERIFIED' there is what a sound checker prints; it is not a checker defect. The proof bytes "
                        "were not needed for that verdict." % UP_LINE.decode()) if up else
                       "native outcome recorded as observed; see the checker log lines above."})
    st = json.loads(R.read_bytes(os.path.join(DESK, "receipts", "selftest-sat-checker.json")))
    add = {"schema": "moqls8-fone-parent-replay-addendum/1",
           "kind": "control-design correction, appended after the controls ran; recorded verdicts not relabelled",
           "written_at": R.now(), "desk": DESK,
           "script": {"path": SELF_REL, "sha256": R.sha_file(SELF)}, "replay_script_sha256": REPLAY_SHA,
           "pre_exec": {"path": "PRE-EXEC.json", "sha256": PRE1_SHA},
           "parent_correction_verbatim": PARENT_CORRECTION,
           "timing": ("Both controls ran 2026-10-18T02:35:48-07:00 to 02:37:04-07:00 (receipts) under the expectation "
                      "pre-registered in PRE-EXEC.json at 02:29:36. The correction reached the desk later, while P0-B3 "
                      "ran (launched 02:52:49); the desk's nearest host-clock read was 2026-10-18T02:53:23-07:00."),
           "policy": ("Receipts and logs are retained unchanged and keep their recorded verdict ANOMALY_VERIFIED under "
                      "the original expectation 'not s VERIFIED'. This addendum evaluates the corrected criterion from "
                      "data already recorded in those receipts and the retained checker logs. No native re-run."),
           "corrected_criterion": ("feed binding rejects mismatched checker hash: the sha256 that the checker-feed "
                                   "writer thread measured over the bytes it actually wrote differs from the expected "
                                   "leaf hash (and equals the pre-registered mutant hash), so the strict per-leaf "
                                   "acceptance, which requires both measured feed hashes to equal the leaf hash, "
                                   "rejects such a run whatever the native checker prints. Native outcome recorded as "
                                   "observed."),
           "controls": entries,
           "unsound_proof_rejection_evidence": {
               "this_desk_selftest": {"receipt": "receipts/selftest-sat-checker.json",
                                      "receipt_sha256": R.sha_file(os.path.join(DESK, "receipts",
                                                                                "selftest-sat-checker.json")),
                                      "verdict": st["verdict"],
                                      "checker_rc": st["pipeline"]["children"].get("checker", {}).get("rc"),
                                      "checker_status_lines": st["pipeline"]["checker_status_lines"],
                                      "what": "solver fed an UNSAT 3-variable formula, checker fed a satisfiable one; "
                                              "the parent drat-trim rejected the proof"},
               "parent_note": "Existing SAT+bogus-proof parent checker controls already exercise unsound proof "
                              "rejection (parent message)."},
           "scope": R.SCOPE}
    print("ADDENDUM %s sha256 %s" % (out, R.write_json_x(out, add)))
    for e in entries:
        print(e["id"], e["recorded_verdict_unchanged"], e["corrected_outcome"],
              e["native_outcome_as_recorded"]["checker_status_lines"])


def cmd_inventory(argv):
    R = load_replay()
    out = os.path.abspath(argv[0])
    if out != os.path.join(DESK, INVENTORY_REL) or os.path.lexists(out):
        die("output must be the new " + INVENTORY_REL)
    b = R.read_bytes(R.WORKER_RESULTS)
    if sha_bytes(b) != FINAL_RESULTS_SHA or b.count(b"\n") != 16 or not b.endswith(b"\n"):
        die("final worker RESULTS.jsonl pin")
    lines = b.split(b"\n")[:16]
    if sha_bytes(b"".join(ln + b"\n" for ln in lines[:R.WORKER_PREFIX[0]])) != R.WORKER_PREFIX[1]:
        die("original prefix-7 snapshot changed")
    recs = {}
    for ln in lines:
        r = json.loads(ln)
        recs[r["id"]] = {k: r.get(k) for k in ("tag", "secs", "aggregate_peak_rss_bytes", "strict_ok", "cnf_sha256",
                                               "solver_returncode", "checker_returncode", "checker_status_lines")}
    for cid in ADDED:
        if recs[cid]["strict_ok"] is not True or recs[cid]["secs"] != PARENT_SECONDS[cid]:
            die("added record " + cid)
    for cid in UNKNOWN_NOT_RERUN:
        if recs[cid]["strict_ok"] is not False:
            die("unknown record " + cid)
    peak = max(r["aggregate_peak_rss_bytes"] for r in recs.values())
    if peak != PARENT_MAX_PEAK:
        die("max pass peak %d" % peak)
    ledger_sha = R.sha_file(os.path.join(R.LANE, LEDGER_REL))
    if not (ledger_sha.startswith(LEDGER_AFFIXES[0]) and ledger_sha.endswith(LEDGER_AFFIXES[1])):
        die("ledger sha256 " + ledger_sha)
    if R.sha_file(os.path.join(R.LANE, META_REL)) != META_SHA:
        die("META sha256")
    originals = {"PRE-EXEC.json": PRE1_SHA}
    for f in sorted(glob.glob(os.path.join(DESK, "receipts", "*.json")) + glob.glob(os.path.join(DESK, "runs", "*.json"))):
        originals[R.rel(f)] = R.sha_file(f)
    added = []
    for cid in ADDED:
        p = recs[cid]["aggregate_peak_rss_bytes"]
        added.append({"id": cid, "worker_record": recs[cid], "parent_message_seconds": PARENT_SECONDS[cid],
                      "projected_peak_bytes": max(3 * p // 2, R.FLOOR_HIGH),
                      "projected_rule": "max(1.5 x worker aggregate peak %d, 4.6 GiB floor %d)" % (p, R.FLOOR_HIGH)})
    inv = {"schema": "moqls8-fone-parent-replay-inventory/2", "written_at": R.now(), "desk": DESK,
           "scripts": {"scripts/replay_v1.py": REPLAY_SHA, SELF_REL: R.sha_file(SELF)},
           "parent_message_verbatim": PARENT_ADDED,
           "worker_final": {"results": R.WORKER_RESULTS, "results_sha256": FINAL_RESULTS_SHA, "complete_records": 16,
                            "prefix7_sha256_still": R.WORKER_PREFIX[1], "ledger": LEDGER_REL,
                            "ledger_sha256": ledger_sha, "meta": META_REL, "meta_sha256": META_SHA,
                            "max_aggregate_peak_rss_bytes": peak, "records": recs,
                            "use": "read only to learn IDs, solve seconds and peaks"},
           "added_six_leaves": added,
           "not_rerun_unknown": list(UNKNOWN_NOT_RERUN),
           "original_snapshots_unchanged": originals,
           "plan": ("PRE-EXEC.v2.json from scripts/replay_v1.py preexec --worker-prefix 16 %s with leaf items %s, "
                    "then one sequential replay_v1.py run under the same gate, stops and acceptance; every leaf is "
                    "regenerated from the pinned F_one source and both CNF feeds are measured. No controls in this "
                    "batch. The lane scanner's '/moqls8-problem16' marker covers the worker's future "
                    "refine_v2/<case> FIFO paths." % (FINAL_RESULTS_SHA, ", ".join(ADDED))),
           "scope": R.SCOPE}
    print("INVENTORY %s sha256 %s" % (out, R.write_json_x(out, inv)))
    for a in added:
        print(a["id"], a["worker_record"]["cnf_sha256"][:12], a["projected_peak_bytes"])


def cmd_result(argv):
    R = load_replay()
    if len(argv) < 2:
        die("result OUT PREEXEC...")
    out = os.path.abspath(argv[0])
    if not out.startswith(DESK + "/") or os.path.lexists(out):
        die("result path must be new and inside the desk")
    pres = []
    for p in argv[1:]:
        p = os.path.abspath(p)
        pre = json.loads(R.read_bytes(p))
        if pre["script"]["sha256"] != REPLAY_SHA:
            die("pre-exec script pin " + p)
        pres.append((p, R.sha_file(p), pre))
    runs = [(f, R.sha_file(f), json.loads(R.read_bytes(f)))
            for f in sorted(glob.glob(os.path.join(DESK, "runs", "*.json")))]
    receipts = {}
    for f in sorted(glob.glob(os.path.join(DESK, "receipts", "*.json"))):
        r = json.loads(R.read_bytes(f))
        receipts[r["label"]] = (r, f)
    corr_path = os.path.join(DESK, CORRECTION_REL)
    corr = json.loads(R.read_bytes(corr_path))
    corr_by_id = {e["id"]: e for e in corr["controls"]}
    groups = {"selftest": [], "leaf": [], "control": []}
    not_run = []
    for _p, _h, pre in pres:
        for it in pre["items"]:
            label = R.item_label(it)
            if label not in receipts:
                why = [dict(e, run=rn["run_tag"]) for _f, _x, rn in runs for e in rn["items"] if e["label"] == label]
                not_run.append({"item": it["item"], "label": label,
                                "run_entries": [{k: e.get(k) for k in ("run", "status", "reason")} for e in why]})
                continue
            r, f = receipts[label]
            e = R._summ(r, f)
            if it["kind"] == "control":
                c = corr_by_id[it["id"]]
                e["verdict_recorded_unchanged"] = e["verdict"]
                e["correction"] = {"addendum": CORRECTION_REL, "addendum_sha256": R.sha_file(corr_path),
                                   "corrected_expectation": c["corrected_expectation"],
                                   "corrected_outcome": c["corrected_outcome"],
                                   "checker_reported_unsat_by_unit_propagation_on_input":
                                       c["native_outcome_as_recorded"]["checker_reported_unsat_by_unit_propagation_on_input"]}
            groups[it["kind"]].append(e)
    counts = {}
    for e in groups["leaf"]:
        counts[e["verdict"]] = counts.get(e["verdict"], 0) + 1
    deferrals = [dict(e, run=rn["run_tag"]) for _f, _x, rn in runs for e in rn["events"]
                 if e.get("event") in ("deferred", "stopped")]
    guards = [dict(e, run=rn["run_tag"]) for _f, _x, rn in runs for e in rn["events"]
              if e.get("event") not in ("deferred", "stopped")]
    allx = groups["selftest"] + groups["leaf"] + groups["control"]
    first = pres[0][2]
    addenda = []
    for relp in (CORRECTION_REL, INVENTORY_REL):
        p = os.path.join(DESK, relp)
        if os.path.exists(p):
            addenda.append({"path": relp, "sha256": R.sha_file(p)})
    result = {
        "schema": "moqls8-fone-parent-replay-result/1", "assembled_at": R.now(), "desk": DESK, "scope": R.SCOPE,
        "statement": "Parent replay of individual leaves only; it establishes no F4/n=8 conclusion and no theorem "
                     "claim. The parent has not accepted any cover theorem from it.",
        "scripts": [{"path": "scripts/replay_v1.py", "sha256": REPLAY_SHA, "role": "pre-exec, replay runs"},
                    {"path": SELF_REL, "sha256": R.sha_file(SELF), "role": "addenda and this RESULT"}],
        "pre_exec": [{"path": R.rel(p), "sha256": h} for p, h, _ in pres],
        "addenda": addenda,
        "binaries": first["binaries"], "inputs": first["inputs"],
        "worker_results_pins": [{k: pre["worker_results"][k] for k in ("path", "prefix_records", "prefix_sha256", "use")}
                                for _p, _h, pre in pres],
        "runs": [{"path": R.rel(f), "sha256": h, "run_tag": rn["run_tag"], "started_at": rn["started_at"],
                  "finished_at": rn.get("finished_at"), "wait_used_seconds": rn.get("wait_used_seconds"),
                  "stopped_reason": rn.get("stopped_reason"), "driver_log": rn.get("driver_log"),
                  "driver_log_sha256": rn.get("driver_log_sha256_at_close")} for f, h, rn in runs],
        "started_at": min([rn["started_at"] for _f, _x, rn in runs], default=None),
        "finished_at": max([rn.get("finished_at") or "" for _f, _x, rn in runs], default=None),
        "acceptance": first["acceptance"], "gate": first["gate"], "in_flight_stops": first["in_flight_stops"],
        "leaf_verdict_counts": counts, "leaves": groups["leaf"], "controls": groups["control"],
        "selftests": groups["selftest"], "not_run": not_run, "deferrals": deferrals, "guard_events": guards,
        "peak_rss": {
            "max_desk_aggregate_sampled_bytes": max([e["peak_desk_aggregate_rss_bytes"] or 0 for e in allx],
                                                    default=None),
            "max_lane_total_sampled_bytes": max([e["peak_lane_total_rss_bytes"] or 0 for e in allx], default=None),
            "max_child_maxrss_bytes": max([max(e["solver"]["maxrss_bytes"] or 0, e["checker"]["maxrss_bytes"] or 0)
                                           for e in allx], default=None)}}
    print("RESULT %s sha256 %s" % (out, R.write_json_x(out, result)))
    for e in groups["leaf"] + groups["control"]:
        print(e["label"], e["verdict"], e["receipt_sha256"], e.get("correction", {}).get("corrected_outcome", ""))


def main(argv):
    if len(argv) < 3:
        die(__doc__)
    cmd = {"correction": cmd_correction, "inventory": cmd_inventory, "result": cmd_result}.get(argv[1])
    if cmd is None:
        die("unknown subcommand " + argv[1])
    cmd(argv[2:])


if __name__ == "__main__":
    main(sys.argv)
