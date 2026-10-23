#!/usr/bin/env python3
"""Addenda v3 for the parent F_one replay desk (review/moqls8-fone-parent-replay-v1). Launches no child processes.

  addenda_v3.py release OUT   record the parent release of the drained desk (verbatim messages, verified admission and
                              release file sha256s, fresh disk and lane state) BEFORE the resumed run
  addenda_v3.py result OUT    RESULT addendum after the resumed run: the resumed leaves P2-C3 and P2-C4 in full (raw
                              status lines, receipt and log sha256s, binding checks) plus a roll-up of all twelve direct
                              leaves and both controls. RESULT.json and every earlier desk file stay unchanged.

Executes this desk's own scripts/replay_v1.py from hash-verified bytes; imports no lane code.
Run as /usr/bin/python3 -I -B with TMPDIR=<desk>/tmp/.
"""
import glob
import hashlib
import importlib.util
import json
import os
import sys

DESK = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-fone-parent-replay-v1"
REVIEW = os.path.dirname(DESK)
REPLAY = DESK + "/scripts/replay_v1.py"
REPLAY_SHA = "16cba374241636885d71f2e91dd3969d35779ccbe27eca4fc2bee3c8781f486d"
SCRIPTS = (("scripts/replay_v1.py", REPLAY_SHA, "pre-exec pins and sequential replay runs"),
           ("scripts/addenda_v1.py", "85d774cf45d66df575080da14239f9b79f0a1a28106b42cea3c702b3a9b632aa",
            "CONTROL-CORRECTION-v1.json and INVENTORY-v2.json"),
           ("scripts/drain_v1.py", "d47a9e2c8316aa74ad45d5500a354c410aadbc0c9f65143cbfe0a955872b7c1e",
            "one SIGTERM to the run-2 driver at a pipeline boundary (parent drain request)"),
           ("scripts/addenda_v2.py", "c555bedd627b69d8d80bc813470a99b3d109a6c79f56b7df9999dfed0b7d6884",
            "DRAIN-v1.json and RESULT.json"))
FILES = (("PRE-EXEC.json", "28dd7b34ebdec158abe1de80b49b43f0110fa24b7adb8f68460a80fc38306e9f"),
         ("PRE-EXEC.v2.json", "6cc220c1956bece314b79d9490000fad6243c16f96973897ff71c7fd33c6f8e0"),
         ("CONTROL-CORRECTION-v1.json", "e53a552c7fb5ed58e38b2dc23ed1e1b53bed778a552865c6fad449871caa7b33"),
         ("INVENTORY-v2.json", "79782bfa91d6c0dc46e1a646cd190491fef34c9187392ebea7ce5ef54910bcd7"),
         ("DRAIN-v1.json", "7d8cf153d680b05856956e354993974236a3a624dee4acc73246a1016fd726fa"),
         ("RESULT.json", "f63dbeebe2d1728a25520d2af1fa7babab15221e2b01f1e74581b6985979ee0c"),
         ("runs/run-20261018T023009.json", "78732750f136da6b242bbb9523c5df1883001b4d9a8dfe4cfc904295a2a8af48"),
         ("runs/run-20261018T025815.json", "345d133be4c9b50c48a26678f0643b50dee3dd9e0daa0b11b3ed139dcbdda798"),
         ("logs/drain-20261018T025815.json", "54ad944f894a6843443332d168932f5d85a6d5b1b860a7d119e08f06956b3c80"))
RESULT1_REL, RESULT1_SHA = "RESULT.json", "f63dbeebe2d1728a25520d2af1fa7babab15221e2b01f1e74581b6985979ee0c"
RUN2_REL = "runs/run-20261018T025815.json"
SELF = os.path.realpath(__file__)
SELF_REL = "scripts/addenda_v3.py"
RELEASE_REL = "RELEASE-v1.json"
PRE3_REL = "PRE-EXEC.v3.json"
ADMISSION = REVIEW + "/moqls8-lane-admissions-v1/pilot-P1-B1-admission-v1.json"
ADMISSION_SHA = "7ff6aa677a9ac2acb63a382d37d1fd0281484cd96519f97e9d0f51ed301ae206"
RELEASE_FILE = REVIEW + "/moqls8-lane-admissions-v1/pilot-P1-B1-release-v1.json"
RELEASE_FILE_SHA = "721c0eda656a6e023cbe9b2cae506143f505a5a8788f84d4a7ccc7efc0539050"
RESUMED = (("P2-C3", "5fc6827fa9cb2856ae1ad14d1aa319f51305296ede72acb7b188060288ae5597"),
           ("P2-C4", "32c4d3db7af5da46151238836dfb14f36e782ca87d139c8ae38211a1ab663b94"))
WORKER_FINAL = (16, "bcfeb441f49971e4c8241fbccdfec99a41c274e8b8af4261d17796ac4327ac19")
ORDER = ("P0-B4", "P0-B5", "P0-B6", "P0-B1", "P0-B2", "P0-B3", "P1-B4", "P1-B6", "P2-C1", "P2-C2", "P2-C3", "P2-C4")
PRODUCER_UNKNOWN = ("P1-B1", "P1-B2", "P1-B3", "P1-B5")
PARENT_RESERVATION = (
    "Drain ack received; one-family resource reservation now R/moqls8-lane-admissions-v1/pilot-P1-B1-admission-v1.json "
    "SHA7ff6aa677a9ac2acb63a382d37d1fd0281484cd96519f97e9d0f51ed301ae206. PhysDepolarizing P1-B1 pilot only, still "
    "source-review pending; no native parent admission until explicit release. Static aggregation may proceed. Parent "
    "recorded P2-C2 late admission as deviation, no successful rerun/backfill. P2-C3 STOPPED-before-native and P2-C4 "
    "NOT_ATTEMPTED remain pending; they'll resume under explicit release/new output names, not overwrite prior "
    "receipts. Please send static result of the10 completed direct cases/controls, all exact hashes and provenance "
    "now; do not wait for remaining2 to report usable evidence.")
PARENT_RELEASE = (
    "Release issued: R/moqls8-lane-admissions-v1/pilot-P1-B1-release-v1.json, sha "
    "721c0eda656a6e023cbe9b2cae506143f505a5a8788f84d4a7ccc7efc0539050. The P1-B1 pilot is stopped and quarantined, "
    "with no active children. GO: run ONLY the two remaining direct measured-feed parent replays P2-C3 "
    "(5fc6827f\u20265597) and P2-C4 (32c4d3db\u20263b94) with your reviewed driver replay_v1.py (16cba374\u2026486d) "
    "and the parent drat-trim. Same strict predicate, binding checks against the parent formula binding and manifest, "
    "fresh gate \u226512.2e9 plus growth, lane caps (\u22644 busy, \u22648 GiB) and SIGTERM-only stops.\n"
    "Then stop, assemble a RESULT addendum as NEW files (never edit the existing RESULT), and report raw status "
    "lines, receipt and log SHAs.")
PLAN = (
    "1) PRE-EXEC.v3.json from `scripts/replay_v1.py preexec PRE-EXEC.v3.json --worker-prefix 16 %s leaf:P2-C3 "
    "leaf:P2-C4` (re-verifies every pin, the parent binding RESULT, the MANIFEST and both binaries, and regenerates the "
    "two leaves in memory). 2) Exactly one `scripts/replay_v1.py run PRE-EXEC.v3.json`: P2-C3 then P2-C4, one "
    "pipeline at a time, unchanged strict predicate; binding checks (pre-launch buffer sha256 == parent binding RESULT "
    "leaf hash == MANIFEST case hash; both measured feeds == that hash); fresh two-sample gate (free >= 12,200,000,000 "
    "+ 10 MiB, lane busy + 2 <= 4, lane RSS + projected <= 7.6 GiB); in-flight SIGTERM-only stops with a bounded "
    "120 s wait. 3) Stop. 4) RESULT addendum RESULT-ADDENDUM-v1.json from `scripts/addenda_v3.py result`; RESULT.json "
    "and every earlier desk file unchanged." % WORKER_FINAL[1])


def die(msg):
    raise SystemExit("ABORT: %s" % msg)


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def load_replay():
    if os.environ.get("TMPDIR") != DESK + "/tmp/":
        die("TMPDIR must be %s/tmp/" % DESK)
    with open(REPLAY, "rb") as f:
        src = f.read()
    if sha_bytes(src) != REPLAY_SHA:
        die("replay_v1.py sha256 changed")
    spec = importlib.util.spec_from_file_location("replay_v1_desk", REPLAY)
    mod = importlib.util.module_from_spec(spec)
    exec(compile(src, REPLAY, "exec"), mod.__dict__)
    for relp, sha, _role in SCRIPTS:
        if mod.sha_file(os.path.join(DESK, relp)) != sha:
            die("script sha256 changed: " + relp)
    for relp, sha in FILES:
        if mod.sha_file(os.path.join(DESK, relp)) != sha:
            die("desk file sha256 changed: " + relp)
    os.chdir(DESK + "/tmp")
    return mod


def output_names(cid):
    return [os.path.join(DESK, "receipts", cid + ".json"), os.path.join(DESK, "logs", cid + ".solver.log"),
            os.path.join(DESK, "logs", cid + ".checker.log"), os.path.join(DESK, "fifo", cid + ".drat.fifo")]


def cmd_release(argv):
    R = load_replay()
    if len(argv) != 1:
        die("release OUT")
    out = os.path.abspath(argv[0])
    if out != os.path.join(DESK, RELEASE_REL) or os.path.lexists(out):
        die("output must be the new " + RELEASE_REL)
    if os.path.lexists(os.path.join(DESK, PRE3_REL)):
        die(PRE3_REL + " must not exist before the release record")
    raw = R.read_bytes(RELEASE_FILE)
    if sha_bytes(raw) != RELEASE_FILE_SHA:
        die("release file sha256")
    release = json.loads(raw)
    if release.get("releases_sha256") != ADMISSION_SHA or R.sha_file(ADMISSION) != ADMISSION_SHA:
        die("admission file sha256")
    pre2 = json.loads(R.read_bytes(os.path.join(DESK, "PRE-EXEC.v2.json")))
    pre2_items = {it.get("id"): it for it in pre2["items"]}
    run2 = json.loads(R.read_bytes(os.path.join(DESK, RUN2_REL)))
    run2_status = {e["label"]: e.get("status") for e in run2["items"]}
    if (run2_status.get("P2-C3"), run2_status.get("P2-C4")) != ("STOPPED", "NOT_ATTEMPTED"):
        die("run-2 statuses of P2-C3/P2-C4")
    names, authorized = [], []
    for cid, h in RESUMED:
        it = pre2_items[cid]
        if (it["expected_solver_feed_sha256"], it["expected_checker_feed_sha256"],
                it["parent_binding_result_cnf_sha256"], it["manifest_cnf_sha256"]) != (h, h, h, h):
            die("PRE-EXEC.v2.json hashes for " + cid)
        for p in output_names(cid):
            if os.path.lexists(p):
                die("output name already used: " + p)
            names.append(R.rel(p))
        authorized.append({"id": cid, "cnf_sha256": h, "status_in_" + RUN2_REL: run2_status[cid]})
    fb = R.free_bytes()
    busy, other, scan = R.gate_scan()
    rec = {"schema": "moqls8-fone-parent-replay-addendum/1",
           "kind": "parent release of the drained desk for exactly two resumed direct replays; written before the run",
           "written_at": R.now(), "desk": DESK, "script": {"path": SELF_REL, "sha256": R.sha_file(SELF)},
           "parent_reservation_message_verbatim": PARENT_RESERVATION,
           "parent_release_message_verbatim": PARENT_RELEASE,
           "admission_file": {"path": ADMISSION, "sha256": ADMISSION_SHA},
           "release_file": {"path": RELEASE_FILE, "sha256": RELEASE_FILE_SHA, "content": release},
           "authorized_items": authorized,
           "not_authorized": ("anything else: no other leaf, no control, no retry of a completed leaf, no producer-UNKNOWN "
                              "leaf (%s)" % ", ".join(PRODUCER_UNKNOWN)),
           "new_output_names_unused_before_run": names,
           "unchanged_desk_files_verified": dict(FILES),
           "scripts_verified": {relp: sha for relp, sha, _role in SCRIPTS},
           "plan": PLAN,
           "fresh_state": {"at": R.now(), "free_bytes": fb, "lane_other_busy": busy, "lane_other_rss_bytes": other,
                           "lane_scan": [R.compact(c) for c in (scan or [])]},
           "scope": R.SCOPE}
    print("RELEASE %s sha256 %s" % (out, R.write_json_x(out, rec)))
    print("fresh: free=%d lane_other_busy=%s lane_other_rss=%s" % (fb, busy, other))


def raw_status(b):
    return [seg.decode("ascii", "backslashreplace") for seg in b.split(b"\n")
            if seg.replace(b"\r", b"").startswith(b"s")]


def log_info(R, p, kind, label):
    relp = p[kind + "_log"]
    b = R.read_bytes(os.path.join(DESK, relp))
    h = sha_bytes(b)
    if h != p[kind + "_log_sha256"]:
        die("%s %s log differs from its receipt hash" % (label, kind))
    return {"path": relp, "sha256": h, "bytes": len(b), "raw_status_lines": raw_status(b),
            "status_lines_cr_stripped": p[kind + "_status_lines"]}


def compact_entry(R, r, rpath):
    p = r["pipeline"]
    s, c = p["children"].get("solver", {}), p["children"].get("checker", {})
    sw, cw = p["writers"].get("solver_feed", {}), p["writers"].get("checker_feed", {})
    return {"id": r.get("id"), "label": r["label"], "verdict": r["verdict"], "reasons": r["reasons"],
            "expected_solver_feed_sha256": r["item"]["expected_solver_feed_sha256"],
            "expected_checker_feed_sha256": r["item"]["expected_checker_feed_sha256"],
            "receipt": R.rel(rpath), "receipt_sha256": R.sha_file(rpath), "pre_exec": r["pre_exec"],
            "run_tag": r["run_tag"], "solver_log": log_info(R, p, "solver", r["label"]),
            "checker_log": log_info(R, p, "checker", r["label"]), "solver_rc": s.get("rc"), "checker_rc": c.get("rc"),
            "measured_solver_feed": [sw.get("ok"), sw.get("written"), sw.get("sha256")],
            "measured_checker_feed": [cw.get("ok"), cw.get("written"), cw.get("sha256")],
            "started_at": p.get("started_at"), "finished_at": p.get("finished_at"),
            "solver_wall_seconds": s.get("wall_seconds"), "checker_wall_seconds": c.get("wall_seconds"),
            "pipeline_seconds": p.get("pipeline_seconds"),
            "peak_desk_aggregate_rss_bytes": p.get("peak_desk_aggregate_rss_bytes"),
            "safety_stop_reason": p.get("safety_stop_reason")}


def cmd_result(argv):
    R = load_replay()
    if len(argv) != 1:
        die("result OUT")
    out = os.path.abspath(argv[0])
    if not out.startswith(DESK + "/") or os.path.lexists(out):
        die("result path must be new and inside the desk")
    self_sha = R.sha_file(SELF)
    rel_path = os.path.join(DESK, RELEASE_REL)
    release = json.loads(R.read_bytes(rel_path))
    if release["script"]["sha256"] != self_sha:
        die("addenda_v3.py changed after RELEASE-v1.json was written")
    pre3_path = os.path.join(DESK, PRE3_REL)
    pre3_sha = R.sha_file(pre3_path)
    pre3 = json.loads(R.read_bytes(pre3_path))
    if pre3["script"]["sha256"] != REPLAY_SHA:
        die("PRE-EXEC.v3.json script pin")
    if [it["item"] for it in pre3["items"]] != ["leaf:" + cid for cid, _h in RESUMED]:
        die("PRE-EXEC.v3.json items")
    for it, (cid, h) in zip(pre3["items"], RESUMED):
        if (it["expected_solver_feed_sha256"], it["expected_checker_feed_sha256"],
                it["parent_binding_result_cnf_sha256"], it["manifest_cnf_sha256"]) != (h, h, h, h):
            die("PRE-EXEC.v3.json hashes for " + cid)
    if (pre3["worker_results"]["prefix_records"], pre3["worker_results"]["prefix_sha256"]) != WORKER_FINAL:
        die("PRE-EXEC.v3.json worker pin")
    runs3 = []
    for f in sorted(glob.glob(os.path.join(DESK, "runs", "*.json"))):
        rn = json.loads(R.read_bytes(f))
        if rn["pre_exec"]["path"] == PRE3_REL:
            runs3.append((f, rn))
    if len(runs3) != 1:
        die("expected exactly one run of %s, found %d" % (PRE3_REL, len(runs3)))
    f3, run3 = runs3[0]
    if run3["pre_exec"]["sha256"] != pre3_sha:
        die("run summary pre-exec sha256")
    dlog = os.path.join(DESK, run3["driver_log"])
    if R.sha_file(dlog) != run3["driver_log_sha256_at_close"]:
        die("resumed driver log changed after close")
    status3 = {e["label"]: e for e in run3["items"]}
    resumed, not_run, rolled = [], [], {}
    for cid, h in RESUMED:
        rpath = os.path.join(DESK, "receipts", cid + ".json")
        e3 = status3.get(cid, {})
        if e3.get("status") != "RECEIPT" or not os.path.exists(rpath):
            not_run.append({"id": cid, "cnf_sha256": h, "run_entry": e3})
            continue
        r = json.loads(R.read_bytes(rpath))
        if r["pre_exec"]["sha256"] != pre3_sha or r["run_tag"] != run3["run_tag"]:
            die("receipt provenance for " + cid)
        if R.sha_file(rpath) != e3["receipt_sha256"]:
            die("receipt differs from the run summary for " + cid)
        full = R._summ(r, rpath)
        p = r["pipeline"]
        full.update({"solver_log": log_info(R, p, "solver", cid), "checker_log": log_info(R, p, "checker", cid),
                     "criteria": r["criteria"], "pre_launch_buffer_check": r["pre_launch_buffer_check"],
                     "parent_binding_result_cnf_sha256": r["item"]["parent_binding_result_cnf_sha256"],
                     "manifest_cnf_sha256": r["item"]["manifest_cnf_sha256"],
                     "binaries_checked_at_launch": r["binaries"], "gate_samples": r["gate"]["samples"],
                     "solver_argv": p["solver_argv"], "checker_argv": p["checker_argv"],
                     "checker_info_lines": p["checker_info_lines"], "run_tag": r["run_tag"], "pre_exec": r["pre_exec"],
                     "min_free_bytes_in_flight": p["min_free_bytes_in_flight"],
                     "max_lane_other_busy_in_flight": p["max_lane_other_busy_in_flight"],
                     "peak_lane_other_rss_bytes": p["peak_lane_other_rss_bytes"]})
        resumed.append(full)
        rolled[cid] = compact_entry(R, r, rpath)
    res1 = json.loads(R.read_bytes(os.path.join(DESK, RESULT1_REL)))
    for e in res1["leaves"]:
        rpath = os.path.join(DESK, e["receipt"])
        if R.sha_file(rpath) != e["receipt_sha256"]:
            die("earlier receipt changed: " + e["receipt"])
        rolled[e["id"]] = compact_entry(R, json.loads(R.read_bytes(rpath)), rpath)
    rollup, counts = [], {}
    for cid in ORDER:
        if cid in rolled:
            rollup.append(rolled[cid])
            v = rolled[cid]["verdict"]
        else:
            rollup.append({"id": cid, "verdict": "NO_RECEIPT"})
            v = "NO_RECEIPT"
        counts[v] = counts.get(v, 0) + 1
    controls = []
    for e in res1["controls"]:
        rpath = os.path.join(DESK, e["receipt"])
        if R.sha_file(rpath) != e["receipt_sha256"]:
            die("control receipt changed: " + e["receipt"])
        ce = compact_entry(R, json.loads(R.read_bytes(rpath)), rpath)
        ce["verdict_recorded_unchanged"] = ce.pop("verdict")
        ce["correction"] = e["correction"]
        controls.append(ce)
    events = run3.get("events", [])
    peaks_resumed = {
        "max_desk_aggregate_sampled_bytes": max([x["peak_desk_aggregate_rss_bytes"] or 0 for x in resumed], default=None),
        "max_lane_total_sampled_bytes": max([x["peak_lane_total_rss_bytes"] or 0 for x in resumed], default=None),
        "max_child_maxrss_bytes": max([max(x["solver"]["maxrss_bytes"] or 0, x["checker"]["maxrss_bytes"] or 0)
                                       for x in resumed], default=None)}
    p1 = res1["peak_rss"]
    peaks_all = {k: max(v for v in (p1.get(k), peaks_resumed.get(k)) if v is not None) for k in p1}
    result = {
        "schema": "moqls8-fone-parent-replay-result-addendum/1", "assembled_at": R.now(), "desk": DESK,
        "scope": R.SCOPE,
        "statement": ("Parent replay of individual leaves only; it establishes no F4/n=8 conclusion and no theorem "
                      "claim. The four producer-UNKNOWN leaves (%s) were not replayed here (parent instruction); "
                      "refinement covers are outside this desk." % ", ".join(PRODUCER_UNKNOWN)),
        "supplements": {"path": RESULT1_REL, "sha256": RESULT1_SHA, "unchanged": True,
                        "relation": "RESULT.json covers the first ten direct leaves, both controls and the self-tests; "
                                    "this addendum adds the resumed leaves and a twelve-leaf roll-up."},
        "release": {"path": RELEASE_REL, "sha256": R.sha_file(rel_path), "release_file": RELEASE_FILE,
                    "release_file_sha256": RELEASE_FILE_SHA},
        "pre_exec": {"path": PRE3_REL, "sha256": pre3_sha, "at": pre3["at"],
                     "items": [it["item"] for it in pre3["items"]],
                     "projected_peak_bytes": {it["id"]: it["projected_peak_bytes"] for it in pre3["items"]},
                     "fresh_check": {k: pre3["fresh_check"][k] for k in
                                     ("free_bytes", "lane_other_busy", "lane_other_rss_bytes")}},
        "scripts": [{"path": relp, "sha256": sha, "role": role} for relp, sha, role in SCRIPTS] +
                   [{"path": SELF_REL, "sha256": self_sha, "role": "RELEASE-v1.json and this RESULT addendum"}],
        "binaries_at_pre_exec": pre3["binaries"], "inputs_at_pre_exec": pre3["inputs"],
        "worker_results_pin": {k: pre3["worker_results"][k] for k in
                               ("path", "prefix_records", "prefix_sha256", "complete_records_at_read", "use")},
        "run": {"path": R.rel(f3), "sha256": R.sha_file(f3), "run_tag": run3["run_tag"],
                "started_at": run3["started_at"], "finished_at": run3["finished_at"],
                "stopped_reason": run3["stopped_reason"], "wait_used_seconds": run3["wait_used_seconds"],
                "driver_log": run3["driver_log"], "driver_log_sha256": run3["driver_log_sha256_at_close"],
                "items": [{k: e.get(k) for k in ("label", "status", "verdict", "receipt", "receipt_sha256", "reason",
                                                   "gate_waited_seconds", "pipeline_seconds")} for e in run3["items"]]},
        "resumed_leaves": resumed, "resumed_not_run": not_run,
        "deferrals_and_stops": [e for e in events if e.get("event") in ("deferred", "stopped")],
        "guard_events": [e for e in events if e.get("event") not in ("deferred", "stopped")],
        "all_direct_leaves_rollup": rollup, "direct_leaf_verdict_counts": counts,
        "controls_rollup": controls,
        "peak_rss_resumed": peaks_resumed, "peak_rss_all_runs": peaks_all,
        "unchanged_desk_files_verified": dict(FILES)}
    print("RESULT ADDENDUM %s sha256 %s" % (out, R.write_json_x(out, result)))
    print("counts", counts, "not_run", [x["id"] for x in not_run])
    for x in resumed:
        print(x["label"], x["verdict"], "receipt", x["receipt_sha256"], "solver_log", x["solver_log"]["sha256"],
              x["solver_log"]["raw_status_lines"], "checker_log", x["checker_log"]["sha256"],
              x["checker_log"]["raw_status_lines"])


def main(argv):
    if len(argv) < 3:
        die(__doc__)
    cmd = {"release": cmd_release, "result": cmd_result}.get(argv[1])
    if cmd is None:
        die("unknown subcommand " + argv[1])
    cmd(argv[2:])


if __name__ == "__main__":
    main(sys.argv)
