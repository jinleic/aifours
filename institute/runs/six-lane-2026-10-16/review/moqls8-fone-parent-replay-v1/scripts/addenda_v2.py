#!/usr/bin/env python3
"""Addenda v2 for the parent F_one replay desk (review/moqls8-fone-parent-replay-v1). Launches no child processes.

  addenda_v2.py drain OUT                 record the parent DRAIN request, the drain at a pipeline boundary and the ack
  addenda_v2.py result OUT PREEXEC...     RESULT over receipts, run summaries and every addendum; lists every desk
                                          script. Replaces addenda_v1.py `result` (v1's correction and inventory
                                          outputs stay as written).

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
SCRIPTS = (("scripts/replay_v1.py", REPLAY_SHA, "pre-exec pins and sequential replay runs"),
           ("scripts/addenda_v1.py", "85d774cf45d66df575080da14239f9b79f0a1a28106b42cea3c702b3a9b632aa",
            "CONTROL-CORRECTION-v1.json and INVENTORY-v2.json"),
           ("scripts/drain_v1.py", "d47a9e2c8316aa74ad45d5500a354c410aadbc0c9f65143cbfe0a955872b7c1e",
            "one SIGTERM to the run-2 driver at a pipeline boundary (parent drain request)"))
SELF = os.path.realpath(__file__)
SELF_REL = "scripts/addenda_v2.py"
CORRECTION_REL = "CONTROL-CORRECTION-v1.json"
INVENTORY_REL = "INVENTORY-v2.json"
DRAIN_REL = "DRAIN-v1.json"
RUN2_REL = "runs/run-20261018T025815.json"
DRAIN_RECORD_REL = "logs/drain-20261018T025815.json"
PARENT_DRAIN = (
    "Main: Parent requests DRAIN AT NEXT NATURAL PIPELINE BOUNDARY (do not terminate a good active replay). Once no "
    "native replay child remains, stop admitting new native replays and send an explicit DRAINED/IDLE ack with "
    "host-clock timestamp, active-child count and actual desk path. PhysDepolarizing needs one shared8GiB lane "
    "reservation for the P1-B1 refinement pilot, pending source-review GO. Parent will write the requested immutable "
    "DRAINED_RESERVED admission only after your ack. Keep all completed receipts; finish static aggregation while "
    "reserved, then resume remaining12 direct replays only after explicit parent release. This is coordination, no "
    "proof retry or predicate/cap change.")
ACK_AT = "2026-10-18T03:10:41-07:00"
ACK_TEXT = (
    "DRAINED/IDLE ack from N8FoneParentReplay at 2026-10-18T03:10:41-07:00 (host clock). Active native children: 0. "
    "No desk process is running. Desk: "
    "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-fone-parent-replay-v1. The driver "
    "stopped at a pipeline boundary: SIGTERM at 03:10:19.189, sent right after the P2-C2 receipt was written with no "
    "child alive; the driver exited at 03:10:21.462. One deviation: P2-C2 was admitted at 03:06:58, after your drain "
    "request. My drain helper only started at 03:06:17, after the P2-C1/P2-C2 boundary (03:05:53). P2-C2 ran to "
    "completion and PASSed. Not run: P2-C3 (STOPPED at its first gate sample) and P2-C4 (NOT_ATTEMPTED). All receipts "
    "are kept. I will admit no new native replay until you explicitly release me; in the meantime I am doing static "
    "aggregation only.")


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
    for relp, sha, _role in SCRIPTS:
        if mod.sha_file(os.path.join(DESK, relp)) != sha:
            die("script sha256 changed: " + relp)
    os.chdir(DESK + "/tmp")
    return mod


def cmd_drain(argv):
    R = load_replay()
    out = os.path.abspath(argv[0])
    if out != os.path.join(DESK, DRAIN_REL) or os.path.lexists(out):
        die("output must be the new " + DRAIN_REL)
    run2 = json.loads(R.read_bytes(os.path.join(DESK, RUN2_REL)))
    rec = json.loads(R.read_bytes(os.path.join(DESK, DRAIN_RECORD_REL)))
    log2 = os.path.join(DESK, run2["driver_log"])
    if R.sha_file(log2) != run2["driver_log_sha256_at_close"]:
        die("run-2 driver log changed")
    sent = [e for e in rec["events"] if e["event"].startswith("SIGTERM sent")]
    if len(sent) != 1 or rec["driver_alive_at_end"] or rec["native_children_of_driver_at_end"]:
        die("drain record")
    status = {e["label"]: {k: e.get(k) for k in ("status", "verdict", "receipt", "receipt_sha256", "reason")}
              for e in run2["items"]}
    add = {"schema": "moqls8-fone-parent-replay-addendum/1", "kind": "parent DRAIN request and drain record",
           "written_at": R.now(), "desk": DESK, "script": {"path": SELF_REL, "sha256": R.sha_file(SELF)},
           "parent_drain_request_verbatim": PARENT_DRAIN,
           "request_timing": ("Delivered while P2-C1 ran (launched 2026-10-18T03:02:28-07:00); the desk's first host-clock "
                              "read after delivery was 2026-10-18T03:05:40-07:00, before the P2-C1/P2-C2 boundary at "
                              "03:05:53."),
           "mechanism": ("scripts/drain_v1.py watched the run-2 driver log and sent the driver exactly one SIGTERM on "
                         "the first new '<label> verdict' or 'gate <label>: projected' line (printed only after the "
                         "previous pipeline's children were reaped) with no native child alive. The driver's gate "
                         "then returned 'stopped' after its first sample, so no new native replay was admitted. No "
                         "active replay was terminated, no SIGKILL."),
           "drain_helper": {"script": "scripts/drain_v1.py", "script_sha256": SCRIPTS[2][1],
                            "record": DRAIN_RECORD_REL,
                            "record_sha256": R.sha_file(os.path.join(DESK, DRAIN_RECORD_REL)),
                            "helper_started_at": rec["started_at"], "events": rec["events"]},
           "deviation": ("P2-C2 was admitted at 2026-10-18T03:06:58-07:00, after the drain request: the helper started "
                         "at 03:06:17.930, after the P2-C1/P2-C2 boundary (03:05:53), while the driver's P2-C2 gate "
                         "was in its 60 s stability wait (first sample streak=1 at 03:05:55). Signalling then would "
                         "have made the driver launch and immediately SIGTERM P2-C2, so the helper waited for the next "
                         "boundary. P2-C2 ran to completion (verdict %s)." % status["P2-C2"]["verdict"]),
           "run2": {"summary": RUN2_REL, "summary_sha256": R.sha_file(os.path.join(DESK, RUN2_REL)),
                    "stopped_reason": run2["stopped_reason"], "finished_at": run2["finished_at"],
                    "driver_log": run2["driver_log"], "driver_log_sha256": run2["driver_log_sha256_at_close"],
                    "items": status},
           "ack": {"sent_to": "agent://Main", "host_clock": ACK_AT, "active_native_children": 0, "text": ACK_TEXT},
           "state_after": ("DRAINED/IDLE: no native replay admitted until explicit parent release; remaining direct "
                           "replays P2-C3 and P2-C4 (PRE-EXEC.v2.json) wait for that release. No proof retry, no "
                           "predicate or cap change."),
           "scope": R.SCOPE}
    print("DRAIN ADDENDUM %s sha256 %s" % (out, R.write_json_x(out, add)))


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
                                "expected_cnf_sha256": it.get("expected_solver_feed_sha256"),
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
    if not_run:
        counts["NOT_RUN"] = len([x for x in not_run if not x["label"].startswith(("control-", "selftest-"))])
    deferrals = [dict(e, run=rn["run_tag"]) for _f, _x, rn in runs for e in rn["events"]
                 if e.get("event") in ("deferred", "stopped")]
    guards = [dict(e, run=rn["run_tag"]) for _f, _x, rn in runs for e in rn["events"]
              if e.get("event") not in ("deferred", "stopped")]
    allx = groups["selftest"] + groups["leaf"] + groups["control"]
    first = pres[0][2]
    addenda = []
    for relp in (CORRECTION_REL, INVENTORY_REL, DRAIN_REL) + tuple(
            sorted(R.rel(p) for p in glob.glob(os.path.join(DESK, "RELEASE-*.json")))):
        p = os.path.join(DESK, relp)
        if os.path.exists(p):
            addenda.append({"path": relp, "sha256": R.sha_file(p)})
    state = ("COMPLETE: every pre-exec item has a receipt" if not not_run else
             "INCOMPLETE: %s without receipt (see not_run)" % ", ".join(x["label"] for x in not_run))
    result = {
        "schema": "moqls8-fone-parent-replay-result/2", "assembled_at": R.now(), "desk": DESK, "scope": R.SCOPE,
        "statement": "Parent replay of individual leaves only; it establishes no F4/n=8 conclusion and no theorem "
                     "claim. The parent has not accepted any cover theorem from it.",
        "state": state,
        "scripts": [{"path": relp, "sha256": sha, "role": role} for relp, sha, role in SCRIPTS] +
                   [{"path": SELF_REL, "sha256": R.sha_file(SELF), "role": "DRAIN-v1.json and this RESULT"}],
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
        "selftests": groups["selftest"], "not_run": not_run, "deferrals_and_stops": deferrals,
        "guard_events": guards,
        "peak_rss": {
            "max_desk_aggregate_sampled_bytes": max([e["peak_desk_aggregate_rss_bytes"] or 0 for e in allx],
                                                    default=None),
            "max_lane_total_sampled_bytes": max([e["peak_lane_total_rss_bytes"] or 0 for e in allx], default=None),
            "max_child_maxrss_bytes": max([max(e["solver"]["maxrss_bytes"] or 0, e["checker"]["maxrss_bytes"] or 0)
                                           for e in allx], default=None)}}
    print("RESULT %s sha256 %s" % (out, R.write_json_x(out, result)))
    print(state)
    for e in groups["leaf"] + groups["control"]:
        print(e["label"], e["verdict"], e["receipt_sha256"], e["pipeline_seconds"], e["peak_desk_aggregate_rss_bytes"],
              e.get("correction", {}).get("corrected_outcome", ""))


def main(argv):
    if len(argv) < 3:
        die(__doc__)
    cmd = {"drain": cmd_drain, "result": cmd_result}.get(argv[1])
    if cmd is None:
        die("unknown subcommand " + argv[1])
    cmd(argv[2:])


if __name__ == "__main__":
    main(sys.argv)
