#!/usr/bin/env python3
"""Assemble the attempt receipt, deviations, RESULT and REPORT of a labelled replay attempt of the parent B-side K3
cube replay desk (review/moqls7-k3-B-cube-parent-replay-v1), v12.

v12 = assemble_B_v11.py for attempts launched by launch_B_v12.py from scripts-v12/ (bklib_v4). Changes:
  * the route-A item A_C311cuts;
  * the scope, title and regeneration line name the item's encoder and composition instead of 'encoder B';
  * the read-only list adds the producer delta (and the lex metadata for route A);
  * texts D16, D18, D21, D29, D32, D36 and the A_C311cuts deviations D37/D38;
  * result entries for the v11-to-v12 diff, the v12 selftest and the v12 packet.
Acceptance conditions, measured feeds, strict parsing, output names and the regen binding are unchanged.

v11 = assemble_B_v10.py for attempts launched by launch_B_v11.py. It has texts only (D16, D18, D21, D29, D35) and
four result entries: the v10-to-v11 diff, the v11 selftest receipt, the v11 review packet, and the gate receipt's
single-admitter invariant. Acceptance conditions, measured feeds, strict parsing, output names and the v10 regen
binding are unchanged.

v10 = assemble_B_v9.py for attempts launched by launch_B_v10.py, with two changes:
  (a) Codex HOLD item 6: before writing anything, the regeneration precheck receipt selected by ITEM and --regen-tag
      must hash to the gate receipt's regen_receipt_sha256. Otherwise the assembler refuses;
  (b) the deviation texts for the v10 launcher (D16, D18, D21, D29, D33, D34) and four result entries: the v9-to-v10
      diff, the separately identified v5-to-v6 assembler hunk set (Codex HOLD item 5, assembler-v5-to-v6-
      generalization.diff), the v10 selftest receipt and the review packet.
Acceptance conditions, measured feeds, strict parsing and output names are unchanged from v9.

v9 = assemble_B_v8.py with the import bumped to bklib_v3 (B_C311cuts item), the scope naming the cuts kind, the
B_C311cuts item deviations, k3_lex.py and k3_cuts_r1.py in the read-only lane-file list for kind cuts, and the
v8-to-v9 diff (scripts-v8-to-v9-Bcuts.r2.diff) in the result. Nothing else changes.

v8 = assemble_B_v7.py with the deviation texts updated for launch_B_v8.py (stability rule; one launcher for both
items). Nothing else changes.

v7 = assemble_B_v6.py with an import bump for B/C411 (bklib_v2, B_C411 item pin) and one addition matching
launch_B_v7.py: 'ITEM LABEL [--regen-tag TAG]' reads the regeneration precheck from receipts/regen-ITEM-TAG.json.

v6 = assemble_B_v5.py made item-generic for launch_B_v6/v7 attempts: outputs named by label
(receipts/LABEL.json, deviations-LABEL.json, RESULT.LABEL.json, REPORT.LABEL.md, each created exclusively), scope
and title taken from the item pins, the item's attempt-1 summary only where it exists, and the deviation set for the
v6 gate. assemble_B_v7.py is the import-only bump (bklib_v2) for B/C411.

Usage: assemble_B_v12.py ITEM LABEL [--regen-tag TAG]     (e.g. B_C311cuts B_C311cuts-p1)

Reads the desk's receipts and logs (never modifies them), re-hashes every referenced file, checks the hash bindings
recorded at run time, and re-hashes the read-only lane inputs and both binaries. No native or other subprocess launch.
Attempt status: PASS only if every driver condition and every supervisor/binding condition holds; otherwise UNKNOWN.
"""
import json
import os
import stat
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bklib_v4 as K  # noqa: E402

REGEN = {"rel": None}                           # set from argv in main(); see the module docstring

DEVIATIONS = [
    {"id": "D16-versioned-scripts",
     "what": "B_C321 attempt a3 was launched by launch_B_v8.py (bklib_v2, driver replay_B_v3.py) and B_C411-p1 by "
             "launch_B_v11.py from scripts/ (bklib_v3, replay_B_v4.py). B/C311+cuts and A/C311+cuts are launched by "
             "launch_B_v12.py from scripts-v12/ (bklib_v4, replay_B_v5.py, compose_Bcuts_v1.py / compose_Acuts_v1.py). "
             "bklib_v3 pins B_C321 and B_C411 exactly as bklib_v2 did. History: v2 attempt labels "
             "(scripts-v1-to-v2.r2.diff); v3 slot-2-only rule (scripts-v2-to-v3.diff); v4 flag-only signal handling "
             "and owned-child loop (scripts-v3-to-v4.diff); v5 cleanup obligation (scripts-v4-to-v5.diff); v6 "
             "ancestry gate (scripts-v5-to-v6.diff); v7 import bumps and --regen-tag (scripts-v6-to-v7-B_C411.diff); "
             "v8 long-job stability rule (scripts-v7-to-v8.diff); v9 B/C311+cuts item (scripts-v8-to-v9-Bcuts.r2.diff, "
             "superseding scripts-v8-to-v9-Bcuts.diff); v10 Codex HOLD repairs and Main's 07:32 stability amendment "
             "(scripts-v9-to-v10.diff). compose_B_v1.py and supervise_r3.py are unchanged; native limits (kissat "
             "--time=5400, drat-trim -t 9000) and supervisor arguments (wall 10200 s, grace 180 s, floor 12e9) are "
             "unchanged. v11 Codex v10-HOLD repairs and the single-admitter invariant: scripts-v10-to-v11.diff; v12 "
             "slots, admission lock, Codex v11 MINOR and the route-A item: scripts-v11-to-v12.diff."},
    {"id": "D17-selfcheck-reused-and-regen-precheck",
     "what": "Self-checks were not rerun: every attempt reuses receipts/selfcheck-summary.json (ec246769...739b, "
             "all_ok; same binaries, same bklib transport code). The regeneration-only precheck is "
             "receipts/regen-<ITEM>.json (MATCH required by the launcher), and each run regenerates and hash-checks "
             "the CNF again before any native launch."},
    {"id": "D18-v6-gate",
     "what": "launch_B_v11/v12 admission (v12 adds slots: at most one attempt of this desk per slot, slot attributed "
             "through the launcher ancestry, 'unknown' blocks both, and admissions serialized by an flock on "
             "locks/admission.lock held from before the final census to 90 s after the spawn). Lane identity is by "
             "cwd/ancestry (cwd inside moqls7-maximum or a review/moqls7-* "
             "desk, or a descendant) over a validated census: two ps identity snapshots bracket a ps args snapshot "
             "and an lsof cwd listing. A process is consistent only if it is present in both identity snapshots with "
             "equal ppid/pgid/uid/lstart/comm and has args of the same lstart. Helpers are bounded and fail-closed, "
             "readers need explicit EOF, and lsof records must be complete. An unresolved own-uid identity, or any "
             "process (any uid, zombies included) whose argv the B/C411 veto cannot resolve, is retried and then "
             "refused. Conditions: <= 2 busy lane natives; lane RSS + 2 GiB <= 8 GiB; fixed RSS cap 2,797,076,480 B "
             "(Main) with ancestry headroom min(3.5 GiB, 8 GiB - ancestry reservations - 128 MiB) >= that cap; the "
             "slot-2 condition (B/C411 r7 reaped and end-recorded, matched on resolved full argv); no other attempt "
             "process of this desk; every M7-lane native outside this desk's ancestry in the route-A attempt-5 group "
             "(single-admitter invariant); free >= 12,201,048,576 B at the first and the final census, at least 60 s "
             "apart. Main's 07:32 PDT long-job stability amendment is evaluated on the parent monitor before AND "
             "after the final census: last free >= 13.5e9 B; max 300 s peak-to-later drop <= max(300 MB, "
             "(free_last - 13.5e9)/12); >= 25 tz-aware strictly increasing samples spanning >= 290 s; age 0..30 s. "
             "Immediately before spawn the launcher rechecks free bytes, the deadline (no launch after 17:30 PDT, and "
             "launch + 10,380 s <= 17:57 PDT), its signals, quarantine records and the monitor sample age (0..30 s). "
             "The gate receipt is written right after the spawn inside run_owned()'s ownership scope."},
    {"id": "D19-v1-deviations-carried",
     "what": "D1-D12 and D14 of deviations-v1.json (1ec0309c...4afb) apply unchanged."},
    {"id": "D20-disk-cause-unestablished",
     "what": "Per Main, observed floor crossings, snapshot-list changes and later free-space recovery do not establish "
             "which process caused a decline or a reclaim; cause and recurrence period are UNESTABLISHED. Every "
             "floor-stopped attempt is UNKNOWN and never relabelled."},
    {"id": "D21-assembler-before-run",
     "what": "assemble_B_v8.py, v9, v10, v11 and v12 were created before the attempts they assemble were launched; "
             "their SHA-256s are part of every recording made by those runs."},
    {"id": "D25-armed-after-go",
     "what": "Each launcher was armed only after Main's explicit GO; the arming time is the first line of "
             "logs/launch-run-<LABEL>.log."},
    {"id": "D26-D27-launcher-logic-carried",
     "what": "The v4 flag-only signal handling with an owned-child loop (signal smoke receipts/smoke-v4-signal."
             "smoke.json) and the v5 cleanup obligation (exception-path test receipts/test-v5-exception-path."
             "test.json) are carried unchanged."},
    {"id": "D28-v5-marker-attribution",
     "what": "The v5 path-marker scan at the B_C321-a2b gate counted drat-trim pid 11629 as M7; per Main it was PA19's "
             "(shared parent drat-trim path). That overcount was conservative; v6 replaces path markers by "
             "cwd/ancestry identity."},
    {"id": "D33-assembler-v6-generalization-identified",
     "what": "Codex HOLD item 5: the assembler hunks of scripts-v5-to-v6.diff (assemble_B_v5.py -> assemble_B_v6.py) "
             "change executable behaviour beyond the admission. They are identified separately in "
             "assembler-v5-to-v6-generalization.diff and are kept, with this rationale:"
             " (i) output names by label (RESULT.<label>.json, REPORT.<label>.md, deviations-<label>.json), because "
             "v5's fixed names RESULT.v2.json/REPORT.v2.md/deviations-v2.json already exist from attempt 2 and every "
             "output is created exclusively;"
             " (ii) attempt-1 history only where receipts/<ITEM>.json exists, because B/C411 and B/C311+cuts have no "
             "attempt 1 (v5 would raise);"
             " (iii) item-specific deviations and a generic stop entry D30 in place of v5's fixed 'attempt-2' D22;"
             " (iv) item-neutral report wording and regen receipt path, plus result entries for the newer diffs."
             " No acceptance condition, measured feed, strict parser or PASS/UNKNOWN rule changed in those hunks."},
    {"id": "D34-v10-launcher-repairs",
     "what": "Codex reviewed the v6 admission (review/m7-launch-v6-r9-codex-v1.note.md, b9db41b6...4f93) and held it; "
             "the parent addendum is review/m7-launch-v6-r9-parent-addendum-v1.md (595999fb...7c1a). launch_B_v10.py "
             "repairs four items: fail-closed enumeration; a consistent census with full-argv slot matching; "
             "preparation before the final census, with free/deadline/signal/quarantine rechecks immediately before "
             "spawn; and bounded scan helpers in their own sessions instead of bklib's _run_text. It also adopts "
             "Main's 07:32 PDT stability amendment and the 17:57 end-by rule. Helper bounds, signals and session "
             "isolation are demonstrated by receipts/test-v10-selftest.selftest.json. Cross-desk serialization of "
             "admissions is not implemented: it needs the other launchers' cooperation outside this desk."},
    {"id": "D35-v11-launcher-repairs",
     "what": "Codex reviewed v10 (review/m7-launch-v10-codex-v1.note.md, f8f86f0d...53f8) and held it. launch_B_v11.py "
             "repairs it as follows: (1) the monitor is evaluated again after the final census, and its sample age is "
             "rechecked at the pre-spawn guard; (2) identity requires agreement in A/B/C, unresolved argv of any uid "
             "or zombie refuses the B/C411 veto, and there is no comm fallback; (3) readers record explicit EOF and "
             "exceptions, lsof records must be 'p', 'fcwd', 'n<absolute path>', and ps numerics are validated; "
             "(4) Main replaced a shared lock with a single-admitter invariant: this desk is the only M7 admitter, "
             "and any lane native outside this desk that is not in the route-A attempt-5 group refuses. The census "
             "tries rise to 15. Evidence: receipts/test-v11-selftest-r2.selftest.json. receipts/test-v11-selftest."
             "selftest.json is the run before the census-tries change."},
    {"id": "D36-v12-slots-lock-and-route-A",
     "what": "Codex GO-WITH-FIXES on v11 (review/m7-launch-v11-codex-v1.note.md, d7ed4c3a...c61a). Main then "
             "approved slot-aware launching and the route-A item. launch_B_v12.py: (a) '--slot {1,2}', at most one "
             "attempt of this desk per slot; legacy launchers are attributed by label (B_C321-a3 slot 2, B_C411-p1 "
             "slot 1); anything unattributable blocks both slots; (b) an admission flock serializes this desk's "
             "admissions; (c) the Codex v11 MINOR: the unrounded monitor age is compared at the pre-spawn guard; "
             "(d) the set runs from scripts-v12/ (bklib_v4 SCRIPTS = its own directory), so the live v11 run's "
             "scripts/ recording is untouched. Evidence: receipts/test-v12-selftest.selftest.json."},
]
ITEM_DEVIATIONS = {
    "B_C411": [{"id": "D29-B_C411-pins-and-slot",
                "what": "B/C411 pins (bklib_v2) come from PhysEpQutrit's r7 producer receipt cert_B_r7/B_C411.json "
                        "(644b5b23...6f75; VERIFIED_UNSAT_CASE with the lane drat-trim build): CNF 01acf464...8bf8, "
                        "metadata B_C411.meta.json c0f769bb...8a12, base 42a5f304...0aac, encoder c7583efe...2b45. "
                        "Main first assigned this replay to slot 1; it then moved to slot 2 after B_C321-a3, and after "
                        "route A attempt 5 ended (08:3x PDT) back to slot 1. Launched by launch_B_v11.py on Main's GO "
                        "following Codex's v11 review (GO-WITH-FIXES)."},
               {"id": "D31-B_C411-regen-precheck-deferral",
                "what": "The first B_C411 regeneration-only precheck (receipts/regen-B_C411.json, 982f5a0d...35db2) "
                        "was deferred by the driver's free-space gate at 07:12:31 (12,012,662,784 < 12,201,048,576 B) "
                        "with all producer pin checks consistent and no compose run. The precheck was repeated "
                        "under replay_B_v3.py 'regen B_C411 --tag TAG'; the launchers from v8 on and the assemblers from "
                        "v8 on read that tagged receipt (--regen-tag)."}],
    "B_C311cuts": [{"id": "D32-B_C311cuts-pins-and-composition",
                    "what": "B/C311+cuts pins (bklib_v3) come from PhysEpQutrit's route-B r6 receipt "
                            "C311cuts_B_r6/C311cuts_B.json (1f003634...c535; VERIFIED_UNSAT_CASE with the lane drat-trim "
                            "build): strengthened CNF ae3b8309...783a (38,353,647 B, p cnf 461370 1867942), input "
                            "explore/k3cubes/B_C311.cnf b3ec0108...c077 (metadata bfa298ee...a056), cut block "
                            "05f31da4...e6dd (238,140 clauses), base 42a5f304...0aac. compose_Bcuts_v1.py executes the "
                            "hash-verified gram_enc, k3_cubes, k3_lex, k3_cuts_r1 and gram_encB bytes and restates "
                            "only k3_cubes.make's encoder-B composition and k3_cuts_certify_r6.prepare's route-B "
                            "append. The producer's driver and generator are not run. Slot 2, after B_C321-a3 ended, "
                            "under launch_B_v12.py on Main's explicit GO."}],
    "A_C311cuts": [{"id": "D37-A_C311cuts-pins-and-composition",
                    "what": "A/C311+cuts pins (bklib_v4) come from PhysEpQutrit's route-A attempt-5 receipt "
                            "C311cuts_A_r9/C311cuts_A.json (88c154b7...f37f; VERIFIED_UNSAT_CASE, cadical 3.0.1 with the "
                            "lane drat-trim build; driver k3_cuts_certify_r9.py 2f0ced45...7ed3; delta "
                            "K3-CUTS-CERT-DELTA.r9.json 76f68d34...5487): strengthened CNF 18583aab...2e5e "
                            "(24,477,803 B, p cnf 107513 897308), input explore/k3lex/A_C311.cnf 059be616...8c4f (lex "
                            "metadata 7bef0b78...190d), source cube 7fca33f1...2001 (metadata 3b2ab04f...d9ed), base "
                            "d0d884f9...4388, cut block 05f31da4...e6dd (238,140 clauses). compose_Acuts_v1.py executes "
                            "the hash-verified gram_enc, k3_cubes, k3_lex and k3_cuts_r1 bytes and restates only route "
                            "A's composition (base + C311 cube + lex generators + cut block), asserting every pin."},
                   {"id": "D38-A_C311cuts-solver-kissat",
                    "what": "Main approved: the desk replays A/C311+cuts with its pinned kissat 4.0.4 "
                            "(05d6f3e9...a848), not the producer's cadical (601c9fa8...d1fa). The acceptance predicate "
                            "is solver-agnostic, the transport self-checks (kissat + parent drat-trim) apply unchanged, "
                            "and a different solver with the parent drat-trim makes the replay more independent of the "
                            "producer run. The solver-log comparison with the producer is informational only."}]}


def load(rel):
    p = os.path.join(K.DESK, rel)
    b = K.read_regular(p)
    return json.loads(b), K.sha_bytes(b)


def file_entry(rel):
    p = os.path.join(K.DESK, rel)
    h, n = K.sha_regular(p)
    return {"path": rel, "sha256": h, "bytes": n}


def desk_listing(exclude=()):
    out, fifos, total = [], [], 0
    for root, dirs, files in os.walk(K.DESK):
        dirs.sort()
        for name in sorted(files):
            p = os.path.join(root, name)
            rel = os.path.relpath(p, K.DESK)
            if rel in exclude:
                continue
            st = os.lstat(p)
            if stat.S_ISFIFO(st.st_mode):
                fifos.append(rel)
                continue
            if not stat.S_ISREG(st.st_mode):
                out.append({"path": rel, "mode": oct(st.st_mode), "note": "not a regular file; not opened"})
                continue
            e = file_entry(rel)
            total += e["bytes"]
            out.append(e)
    return out, fifos, total


def item_receipt(item, label):
    it = K.ITEMS[item]
    pre, pre_sha = load("receipts/%s.pre.json" % label)
    launch, launch_sha = load("receipts/%s.launch.json" % label)
    drv, drv_sha = load("receipts/%s.driver.json" % label)
    sup, sup_sha = load("receipts/%s.supervisor.json" % label)
    gate, gate_sha = load("receipts/%s.gate.json" % label)
    outc, outc_sha = load("receipts/%s.launch-outcome.json" % label)
    regen_r, regen_sha = load(REGEN["rel"])
    summ, summ_sha = load("receipts/selfcheck-summary.json")
    rec = drv.get("pipeline") or {}
    ch = rec.get("children") or {}
    logs = {}
    for key in ("solver_log", "checker_log", "checkpoints"):
        e = file_entry(rec[key])
        e["equals_driver_receipt"] = e["sha256"] == rec.get(key + "_sha256" if key != "checkpoints"
                                                             else "checkpoints_sha256")
        logs[key] = e
    for rel in ("logs/driver-run-%s.log" % label, "logs/%s.supervisor-stdout.log" % label,
                "logs/launch-run-%s.log" % label):
        logs[os.path.basename(rel)] = file_entry(rel)
    quarantine = os.path.join(K.RECEIPTS, label + ".QUARANTINE.json")
    bins_now = {"kissat": K.binary_record(K.KISSAT), "drat-trim": K.binary_record(K.DRAT)}
    sc = {
        "supervisor_record_sha_bound": outc.get("supervisor_record_sha256") == sup_sha,
        "gate_receipt_sha_bound": outc.get("gate_receipt_sha256") == gate_sha,
        "pre_receipt_sha_bound": drv.get("pre_receipt_sha256") == pre_sha,
        "launch_receipt_sha_bound": drv.get("launch_receipt_sha256") == launch_sha,
        "gate_admission_ok": (gate.get("admission") or {}).get("ok") is True,
        "supervisor_sha_equals_pin": sup.get("supervisor_sha256") == K.SUPERVISOR_SHA256,
        "supervisor_rss_cap_equals_gate_cap": (sup.get("limits") or {}).get("rss_cap_bytes")
                                              == (gate.get("rss_cap") or {}).get("value"),
        "supervisor_completed_cleanly": sup.get("completed_cleanly") is True,
        "supervisor_no_trip": sup.get("trip_reason") is None,
        "supervisor_not_uncertain": sup.get("uncertain") is False,
        "supervisor_no_stop_sent": sup.get("stop") is None,
        "supervisor_no_quarantine": sup.get("quarantine_record") is None and not os.path.lexists(quarantine),
        "supervisor_leader_rc_0": sup.get("leader_returncode") == 0,
        "supervisor_process_rc_0": (outc.get("supervisor") or {}).get("rc") == 0,
        "launcher_received_no_signal": not outc.get("launcher_signals"),
        "launcher_no_marker_no_lost_child": (not os.path.lexists(os.path.join(K.RECEIPTS,
                                                                              label + ".launcher.QUARANTINE.json"))
                                             and (outc.get("owned_child") or {}).get("marker") is None
                                             and (outc.get("owned_child") or {}).get("lost_child") is None),
        "launcher_slot_released_cleanly": outc.get("slot_released") is True and not outc.get("stopped_by_launcher"),
        "logs_unchanged_since_driver_receipt": all(v.get("equals_driver_receipt", True) for v in logs.values()),
        "binaries_at_assembly_equal_pins": all(bins_now[k]["sha256"] == K.BIN_PINS[p]
                                               for k, p in (("kissat", K.KISSAT), ("drat-trim", K.DRAT))),
        "scripts_unchanged_pre_to_end": drv.get("scripts_sha256_end") == pre.get("scripts_sha256"),
        "regen_precheck_match": regen_r.get("result") == "MATCH",
        "selfcheck_all_ok": summ.get("all_ok") is True,
    }
    conditions = dict(drv.get("conditions") or {}, **sc)
    status = "PASS" if conditions and all(conditions.values()) else "UNKNOWN"
    w = rec.get("writers") or {}
    regen = drv.get("regen") or {}
    stop = None
    if sup.get("trip_reason"):
        stop = {"by": "supervise_r3.py (pinned)", "reason": sup["trip_reason"], "uncertain": sup.get("uncertain"),
                "signal": "SIGTERM via killpg to the driver's process group (driver, kissat, drat-trim)",
                "stop_record": sup.get("stop"), "supervisor_finished_at": sup.get("finished_at"),
                "driver_view": {"driver_signal": rec.get("driver_signal"),
                                "driver_safety_stop_reason": rec.get("safety_stop_reason"),
                                "driver_sigterm_sent": rec.get("sigterm_sent"),
                                "note": "driver signal %r; driver-sent SIGTERMs %d; children rc %s" % (
                                    rec.get("driver_signal"), len(rec.get("sigterm_sent") or []),
                                    {k: v.get("rc") for k, v in ch.items()})},
                "quarantine": sup.get("quarantine_record"), "survivors": (sup.get("stop") or {}).get("survivors")}
    prod = pre["producer"]["receipt_fields"]
    return {
        "item": item, "label": label, "encoder": it["encoder"], "cube": it["cube"], "status": status,
        "status_rule": "PASS only if every condition below holds; otherwise UNKNOWN (deviations-v1 D10)",
        "failed_conditions": [k for k, v in conditions.items() if not v],
        "observed_outcome": drv.get("observed_outcome"), "stop": stop,
        "strict_fields": {
            "regenerated_cnf_sha256": regen.get("cnf_sha256"), "pinned_cnf_sha256": it["cnf_sha256"],
            "cnf_hash_match": regen.get("cnf_hash_match"), "cnf_bytes": regen.get("cnf_bytes"),
            "cnf_header": regen.get("cnf_header"), "base_cnf_sha256": regen.get("base_cnf_sha256"),
            "solver_rc": (ch.get("solver") or {}).get("rc"),
            "solver_status_lines": (rec.get("solver_flags") or {}).get("status_lines"),
            "checker_rc": (ch.get("checker") or {}).get("rc"),
            "checker_status_lines": (rec.get("checker_flags") or {}).get("status_lines"),
            "NOT_VERIFIED_anywhere": [(rec.get("solver_flags") or {}).get("not_verified_anywhere"),
                                      (rec.get("checker_flags") or {}).get("not_verified_anywhere")],
            "TIMEOUT_anywhere": [(rec.get("solver_flags") or {}).get("timeout_anywhere"),
                                 (rec.get("checker_flags") or {}).get("timeout_anywhere")],
            "feeds": {k: {x: w.get(k, {}).get(x) for x in ("expected_bytes", "written", "complete", "sha256",
                                                            "finished_at", "thread_alive_after_join")}
                      for k in ("solver_cnf", "checker_cnf")},
            "binaries_at_spawn": {k: v["sha256"] for k, v in (drv.get("binaries_at_spawn") or {}).items()},
            "binaries_after": {k: v["sha256"] for k, v in (drv.get("binaries_after") or {}).items()},
            "binaries_at_assembly": {k: v["sha256"] for k, v in bins_now.items()},
            "solver_argv": rec.get("solver_argv"), "checker_argv": rec.get("checker_argv"),
            "checker_stdin": rec.get("checker_stdin")},
        "conditions": conditions,
        "receipts": {"pre": {"path": "receipts/%s.pre.json" % label, "sha256": pre_sha},
                     "launch": {"path": "receipts/%s.launch.json" % label, "sha256": launch_sha},
                     "driver": {"path": "receipts/%s.driver.json" % label, "sha256": drv_sha},
                     "supervisor": {"path": "receipts/%s.supervisor.json" % label, "sha256": sup_sha},
                     "gate": {"path": "receipts/%s.gate.json" % label, "sha256": gate_sha},
                     "launch_outcome": {"path": "receipts/%s.launch-outcome.json" % label, "sha256": outc_sha},
                     "regen_precheck": {"path": REGEN["rel"], "sha256": regen_sha},
                     "selfcheck_summary": {"path": "receipts/selfcheck-summary.json", "sha256": summ_sha}},
        "logs": logs,
        "checker_log_vs_producer": compare_with_producer(rec, it),
        "admission_slot": (gate.get("admission") or {}).get("slot"),
        "times": {"driver_started_at": drv.get("started_at"), "pipeline_started_at": rec.get("started_at"),
                  "pipeline_finished_at": rec.get("finished_at"), "pipeline_seconds": rec.get("pipeline_seconds"),
                  "solver": {k: (ch.get("solver") or {}).get(k) for k in ("wall_seconds", "user_seconds",
                                                                          "sys_seconds", "ended_at")},
                  "checker": {k: (ch.get("checker") or {}).get(k) for k in ("wall_seconds", "user_seconds",
                                                                            "sys_seconds", "ended_at")},
                  "regeneration_seconds": (regen.get("regen_run") or {}).get("seconds"),
                  "driver_seconds": drv.get("driver_seconds"), "supervisor_seconds": sup.get("seconds"),
                  "supervisor_started_at": sup.get("started_at"), "supervisor_finished_at": sup.get("finished_at")},
        "rss": {"cap_bytes": (gate.get("rss_cap") or {}).get("value"),
                "driver_peak_sampled_aggregate_bytes": rec.get("peak_sampled_aggregate_rss_bytes"),
                "driver_samples": rec.get("rss_samples"),
                "supervisor_peak_sampled_bytes": sup.get("peak_sampled_rss_bytes"),
                "supervisor_samples": sup.get("samples"),
                "solver_maxrss_bytes": (ch.get("solver") or {}).get("maxrss_bytes"),
                "checker_maxrss_bytes": (ch.get("checker") or {}).get("maxrss_bytes"),
                "compose_maxrss_bytes": (regen.get("regen_run") or {}).get("maxrss_bytes")},
        "free_bytes": {"launcher_gate": gate.get("free_bytes"), "driver_gates": rec.get("gates"),
                       "at_pipeline_start": rec.get("free_bytes_start"),
                       "driver_min_sampled": rec.get("min_sampled_free_bytes"),
                       "supervisor_trip_reading": sup.get("trip_reason"),
                       "at_pipeline_end": rec.get("free_bytes_end"), "at_launcher_end": outc.get("free_bytes_end"),
                       "checkpoints": [{k: c.get(k) for k in ("at", "elapsed_seconds", "free_bytes",
                                                              "aggregate_rss_bytes")}
                                       for c in (json.loads(x) for x in K.read_regular(
                                           os.path.join(K.DESK, rec["checkpoints"])).decode().splitlines() if x)]},
        "capacity_at_launch": {"admission": gate.get("admission"),
                               "lane_native_busy": (gate.get("scan") or {}).get("lane_native_busy"),
                               "lane_natives": [{k: n.get(k) for k in ("pid", "comm", "args")}
                                                for n in (gate.get("scan") or {}).get("lane_natives", [])],
                               "lane_rss_bytes": (gate.get("scan") or {}).get("lane_rss_bytes"),
                               "reserved_bytes": (gate.get("scan") or {}).get("reserved_bytes"),
                               "supervised_other_runs": [{k: s.get(k) for k in ("supervisor_pid", "rss_cap")}
                                                         for s in (gate.get("scan") or {}).get("supervised", [])]},
        "producer_receipt": {"path": pre["producer"]["receipt"]["path"], "sha256": pre["producer"]["receipt"]["sha256"],
                             "consistency_checks_all_true": pre["producer"]["consistent"],
                             "fields": {k: prod.get(k) for k in ("seconds", "solver_rc", "checker_rc",
                                                                 "checker_status_lines", "solver_binary_sha256",
                                                                 "checker_binary_sha256", "solver_log_sha256",
                                                                 "checker_log_sha256",
                                                                 "peak_sampled_aggregate_rss_bytes")}},
        "scope": ("Attempt-level replay record (label %s) for the exact %s/%s CNF only (SHA-256 %s). PASS means this "
                  "CNF is UNSAT by a freshly streamed kissat binary DRAT proof accepted by the parent drat-trim; UNKNOWN "
                  "means this attempt neither confirms nor refutes the producer's certificate. No K3, M(7), coverage, "
                  "bridge or theorem verdict." % (
                      label, it["encoder"], it["cube"] + ({"A": " + lex (AMENDMENT-3) + AMENDMENT-4 cuts",
                                                            "B": " + AMENDMENT-4 cuts"}.get(it.get("route"), "")
                                                           if it.get("kind") == "cuts" else ""), it["cnf_sha256"])),
    }


def fmt(n):
    return "{:,}".format(n) if isinstance(n, int) else str(n)


def report(result, result_sha, item_row, item_sha):
    r = item_row
    sf = r["strict_fields"]
    t = r["times"]
    lines = [
        "# Parent replay of the phys-2 K3 cube certificate %s (MOQLS(7), encoder %s), attempt %s" % (
            r["item"], K.ITEMS[r["item"]]["encoder"], r["label"]), "",
        "Desk: `review/moqls7-k3-B-cube-parent-replay-v1/`, 2026-10-18 PDT. RESULT.%s.json sha256 `%s`." % (
            r["label"], result_sha),
        "Generated by `scripts/%s` from the same data as RESULT.%s.json. Attempt 1 of this item: %s." % (
            os.path.basename(__file__), r["label"],
            ("%s, item receipt `%s`, RESULT.json `%s`" % (result["attempt_1"]["status"],
                                                         result["attempt_1"]["item_receipt_sha256"],
                                                         result["attempt_1"]["result_json_sha256"])
             if result["attempt_1"] else "none in this desk")), "",
        "## Verdict", "",
        "| item | status | regenerated CNF sha256 = pin | solver rc / status lines | checker rc / status lines | stop |",
        "|---|---|---|---|---|---|",
        "| %s | **%s** | `%s` %s | %s / `%s` | %s / `%s` | %s |" % (
            r["item"], r["status"], sf["regenerated_cnf_sha256"], "yes" if sf["cnf_hash_match"] else "NO",
            sf["solver_rc"],
            sf["solver_status_lines"], sf["checker_rc"], sf["checker_status_lines"],
            (r["stop"] or {}).get("reason", "none")), "",
        "Attempt receipt `receipts/%s.json` sha256 `%s`." % (r["label"], item_sha), "",
        "Checker log vs producer log (lines other than 'verification time'): %s." % (
            r["checker_log_vs_producer"]["summary"]),
        "Failed conditions: %s." % (", ".join("`%s`" % c for c in r["failed_conditions"]) or "none"),
        "Observed outcome: %s." % r["observed_outcome"], "",
        "Scope: %s" % r["scope"], "",
        "## What happened", "",
        "- Regeneration (desk composition driver %s, pinned lane sources, in memory): `%s`, %s bytes, header `%s`, "
        "%s s." % (K.ITEMS[r["item"]].get("compose", "compose_B_v1.py"), sf["regenerated_cnf_sha256"],
                   fmt(sf["cnf_bytes"]), sf["cnf_header"], t["regeneration_seconds"]),
        "- Pipeline %s to %s (%s s). kissat wall %s s, user %s s, rc %s; drat-trim wall %s s, user %s s, rc %s." % (
            t["pipeline_started_at"], t["pipeline_finished_at"], t["pipeline_seconds"], t["solver"]["wall_seconds"],
            t["solver"]["user_seconds"], sf["solver_rc"], t["checker"]["wall_seconds"], t["checker"]["user_seconds"],
            sf["checker_rc"]),
    ]
    if r["stop"]:
        lines.append("- Stop: %s; %s; survivors %s; quarantine %s. The driver recorded `%s`." % (
            r["stop"]["reason"], r["stop"]["signal"], r["stop"]["survivors"], r["stop"]["quarantine"],
            r["stop"]["driver_view"]["driver_signal"]))
    lines += [
        "- Both measured CNF feeds complete: solver %s / %s bytes, sha256 `%s`; checker %s / %s bytes, sha256 `%s`." % (
            fmt(sf["feeds"]["solver_cnf"]["written"]), fmt(sf["feeds"]["solver_cnf"]["expected_bytes"]),
            sf["feeds"]["solver_cnf"]["sha256"], fmt(sf["feeds"]["checker_cnf"]["written"]),
            fmt(sf["feeds"]["checker_cnf"]["expected_bytes"]), sf["feeds"]["checker_cnf"]["sha256"]),
        "- Both logs are empty (0 bytes): no status line was printed before the stop. `NOT VERIFIED` / `TIMEOUT` "
        "anywhere: %s / %s." % (sf["NOT_VERIFIED_anywhere"], sf["TIMEOUT_anywhere"]),
        "- RSS: cap %s B; peak sampled aggregate %s B (driver view), %s B (supervisor view); ru_maxrss kissat %s B, "
        "drat-trim %s B." % (fmt(r["rss"]["cap_bytes"]), fmt(r["rss"]["driver_peak_sampled_aggregate_bytes"]),
                             fmt(r["rss"]["supervisor_peak_sampled_bytes"]), fmt(r["rss"]["solver_maxrss_bytes"]),
                             fmt(r["rss"]["checker_maxrss_bytes"])),
        "- Free bytes: launcher gate %s; pipeline start %s; driver minimum sample %s; supervisor trip `%s`; "
        "pipeline end %s; launcher end %s." % (
            fmt(r["free_bytes"]["launcher_gate"]), fmt(r["free_bytes"]["at_pipeline_start"]),
            fmt(r["free_bytes"]["driver_min_sampled"]), r["free_bytes"]["supervisor_trip_reading"],
            fmt(r["free_bytes"]["at_pipeline_end"]), fmt(r["free_bytes"]["at_launcher_end"])),
        "- Driver checkpoints (time, elapsed s, free bytes, aggregate RSS B): %s." % "; ".join(
            "%s, %s, %s, %s" % (c["at"][11:19], c["elapsed_seconds"], fmt(c["free_bytes"]),
                                fmt(c["aggregate_rss_bytes"])) for c in r["free_bytes"]["checkpoints"]),
        "- Capacity at launch: %s busy lane natives %s; lane RSS %s B; RSS cap %s B." % (
            r["capacity_at_launch"]["lane_native_busy"],
            [(n["pid"], os.path.basename(n["comm"])) for n in r["capacity_at_launch"]["lane_natives"]],
            fmt(r["capacity_at_launch"]["lane_rss_bytes"]), fmt(r["rss"]["cap_bytes"])),
        "- Producer receipt for comparison: %s s, solver rc %s, checker rc %s, %s, peak %s B." % (
            r["producer_receipt"]["fields"]["seconds"], r["producer_receipt"]["fields"]["solver_rc"],
            r["producer_receipt"]["fields"]["checker_rc"], r["producer_receipt"]["fields"]["checker_status_lines"],
            fmt(r["producer_receipt"]["fields"]["peak_sampled_aggregate_rss_bytes"])), "",
        "## Checks reused (deviation D17)", "",
        "- Regeneration-only precheck: %s (`%s` `%s`)." % (
            result["regeneration_precheck"]["result"], result["regeneration_precheck"]["receipt"],
            result["regeneration_precheck"]["sha256"]),
        "- Transport self-checks (`receipts/selfcheck-summary.json` `%s`, all_ok %s):" % (
            result["transport_selfcheck"]["summary_sha256"], result["transport_selfcheck"]["all_ok"]),
    ]
    for row in result["transport_selfcheck"]["rows"]:
        lines.append("  - %s: expectation met %s; solver rc %s %s; checker rc %s %s; receipt `%s`." % (
            row["label"], row["expectation_met"], row["solver_rc"], row["solver_status_lines"], row["checker_rc"],
            row["checker_status_lines"], row["receipt_sha256"]))
    lines += ["  - %d in-memory parser cases and %d strict-condition logic cases: parser %s, logic %s." % (
        result["transport_selfcheck"]["parser_cases"], result["transport_selfcheck"]["logic_cases"],
        result["transport_selfcheck"]["parser_all_ok"], result["transport_selfcheck"]["logic_ok"]), "",
        "## Binaries and pins (sha256)", ""]
    for k, v in result["binaries_at_assembly"].items():
        if k in sf["binaries_at_spawn"]:
            lines.append("- %s `%s` `%s` (at spawn %s, after the run %s)." % (
                k, v["path"], v["sha256"], sf["binaries_at_spawn"][k], sf["binaries_after"].get(k)))
        else:
            lines.append("- %s `%s` (realpath `%s`) `%s`." % (k, v["path"], v["realpath"], v["sha256"]))
    for p, h in result["read_only_inputs_at_assembly"].items():
        lines.append("- `%s` `%s`" % (p, h))
    lines += ["", "## Scripts (sha256 now)", ""]
    for n, h in result["scripts_sha256_now"].items():
        lines.append("- `scripts/%s` `%s`" % (n, h))
    lines.append("- Run scripts recorded at %s; all recordings equal: %s; equal now: %s; v1 run scripts unchanged "
                 "since attempt 1: %s." % (", ".join(result["run_scripts"]["recording_points"]),
                                           result["run_scripts"]["all_recordings_equal"],
                                           result["run_scripts"]["equal_now"],
                                           result["run_scripts"]["v1_run_scripts_unchanged_since_attempt_1"]))
    lines += ["", "## Receipts and logs of the item (sha256)", ""]
    for k, v in r["receipts"].items():
        lines.append("- %s `%s` `%s`" % (k, v["path"], v["sha256"]))
    for k, v in r["logs"].items():
        lines.append("- %s `%s` %s B `%s`" % (k, v["path"], fmt(v["bytes"]), v["sha256"]))
    lines += ["", "## Deviations (full text: `deviations-%s.json`; D1-D12, D14 of `deviations-v1.json` carried)"
              % r["label"], ""]
    for d in result["deviations"]["items"]:
        lines.append("- %s: %s" % (d["id"], d["what"]))
    lines += ["", "## Integrity", "",
              "Receipts, logs, RESULT.%s.json, REPORT.%s.md and deviations-%s.json were created exclusively (mode "
              "'x' / O_EXCL). The versioned scripts were copied with cp -n and edited before their first recorded use; "
              "diffs scripts-v1-to-v2.r2.diff through scripts-v11-to-v12.diff. No earlier attempt's files were "
              "modified, deleted or renamed. No lane file "
              "was written. There were no /tmp writes and no Git, network or model CLI. __pycache__ present: %s. "
              "Desk regular files before RESULT.%s.json: %d, %s bytes in total. FIFO nodes, never opened outside the "
              "pipeline: %s." % (r["label"], r["label"], r["label"], result["pycache_present"], r["label"],
                                 len(result["desk_files_before_result"]),
                                 fmt(result["desk_bytes_before_result"]), ", ".join(result["fifo_nodes"])), ""]
    lines += ["| file | bytes | sha256 |", "|---|---|---|"]
    for e in result["desk_files_before_result"]:
        lines.append("| `%s` | %s | `%s` |" % (e["path"], fmt(e.get("bytes")), e.get("sha256")))
    return "\n".join(lines) + "\n"


def compare_with_producer(rec, it):
    """Line-by-line comparison of this attempt's checker log with the producer's lane checker log (read-only)."""
    if not rec.get("checker_log"):
        return {"summary": "no checker log"}
    mine = K.read_regular(os.path.join(K.DESK, rec["checker_log"])).split(b"\n")
    prod = K.read_regular(it["producer_checker_log"]).split(b"\n")
    diff = [{"line": i + 1, "parent": a.decode("ascii", "replace"), "producer": b.decode("ascii", "replace")}
            for i, (a, b) in enumerate(zip(mine, prod)) if a != b]
    other = [d for d in diff if b"verification time" not in d["parent"].encode()
             or b"verification time" not in d["producer"].encode()]
    return {"producer_log": it["producer_checker_log"], "line_counts": [len(mine), len(prod)],
            "differing_lines": diff,
            "summary": "%d lines vs %d; %d differing line(s) other than 'verification time'" % (
                len(mine), len(prod), len(other) + abs(len(mine) - len(prod)))}


def main():
    a = sys.argv[1:]
    tagged = len(a) == 4 and a[2] == "--regen-tag" and a[3].isalnum()
    if (len(a) != 2 and not tagged) or a[0] not in K.ITEMS or not a[1].startswith(a[0] + "-"):
        raise SystemExit(__doc__)
    item, label = a[0], a[1]
    REGEN["rel"] = "receipts/regen-%s%s.json" % (item, "-" + a[3] if tagged else "")
    names = {"result": "RESULT.%s.json" % label, "report": "REPORT.%s.md" % label, "dev": "deviations-%s.json" % label}
    paths = {"item": os.path.join(K.RECEIPTS, label + ".json"), "dev": os.path.join(K.DESK, names["dev"]),
             "result": os.path.join(K.DESK, names["result"]), "report": os.path.join(K.DESK, names["report"])}
    for p in paths.values():
        if os.path.lexists(p):
            raise SystemExit("exists: " + p)
    gate0, _ = load("receipts/%s.gate.json" % label)
    regen_bound = K.sha_file(os.path.join(K.DESK, REGEN["rel"]))
    if gate0.get("regen_receipt_sha256") != regen_bound:     # Codex HOLD item 6: refuse before writing anything
        raise SystemExit("refused: %s hashes to %s but the gate receipt bound regen_receipt_sha256 %s" % (
            REGEN["rel"], regen_bound, gate0.get("regen_receipt_sha256")))
    row = item_receipt(item, label)
    item_sha = K.write_json_x(paths["item"], row)
    dev = DEVIATIONS + ITEM_DEVIATIONS.get(item, []) + (
        [{"id": "D30-attempt-stop", "what": "This attempt was stopped: %s (supervisor record %s). Status UNKNOWN; not "
          "retried without parent GO." % (row["stop"]["reason"], row["receipts"]["supervisor"]["sha256"])}]
        if row["stop"] else [])
    dev_sha = K.write_json_x(paths["dev"], dev)
    regen_r, regen_sha = load(REGEN["rel"])
    summ, summ_sha = load("receipts/selfcheck-summary.json")
    sgate, sgate_sha = load("receipts/selfcheck.gate.json")
    it_ro = K.ITEMS[item]
    ro = [os.path.join(K.CODE, n) for n in ("gram_enc.py", "k3_cubes.py", "gram_encB.py", "supervise_r3.py")
          + (("k3_lex.py", "k3_cuts_r1.py") if it_ro.get("kind") == "cuts" else ())]
    ro += [it_ro["producer_receipt"], it_ro["meta"], K.ORACLE_RECEIPT,
           it_ro["producer_checker_log"], it_ro["producer_solver_log"], it_ro["lane_cnf"]]
    ro += [it_ro[k] for k in ("delta", "lex_meta") if k in it_ro]
    files, fifos, total = desk_listing(exclude=(names["result"], names["report"]))
    seen = {"run.gate": load("receipts/%s.gate.json" % label)[0].get("scripts_sha256"),
            "run.pre": load("receipts/%s.pre.json" % label)[0].get("scripts_sha256"),
            "run.end": load("receipts/%s.driver.json" % label)[0].get("scripts_sha256_end")}
    a1_pre = os.path.join(K.RECEIPTS, item + ".pre.json")
    a1 = load("receipts/%s.pre.json" % item)[0].get("scripts_sha256") if os.path.isfile(a1_pre) else None
    run_scripts = {"recorded": seen["run.pre"],
                   "all_recordings_equal": all(v == seen["run.pre"] for v in seen.values()),
                   "equal_now": K.script_hashes() == seen["run.pre"],
                   "v1_run_scripts_unchanged_since_attempt_1": (all((seen["run.pre"] or {}).get(n) == h
                                                                    for n, h in a1.items()) if a1 else None),
                   "recording_points": sorted(seen)}
    a1_path = os.path.join(K.RECEIPTS, item + ".json")
    attempt_1 = None
    if os.path.isfile(a1_path):
        a1_item, a1_item_sha = load("receipts/%s.json" % item)
        attempt_1 = {"label": item, "status": a1_item.get("status"), "item_receipt": "receipts/%s.json" % item,
                     "item_receipt_sha256": a1_item_sha, "stop_reason": (a1_item.get("stop") or {}).get("reason"),
                     "result_json_sha256": file_entry("RESULT.json")["sha256"],
                     "deviations_v1_sha256": file_entry("deviations-v1.json")["sha256"]}
    result = {
        "desk": "review/moqls7-k3-B-cube-parent-replay-v1",
        "scope": row["scope"],
        "verdicts": {label: row["status"]},
        "attempt_1": attempt_1,
        "scripts_diff_v1_to_v2": file_entry("scripts-v1-to-v2.r2.diff"),
        "scripts_diff_v2_to_v3": file_entry("scripts-v2-to-v3.diff"),
        "scripts_diff_v3_to_v4": file_entry("scripts-v3-to-v4.diff"),
        "scripts_diff_v4_to_v5": file_entry("scripts-v4-to-v5.diff"),
        "scripts_diff_v5_to_v6": file_entry("scripts-v5-to-v6.diff"),
        "scripts_diff_v6_to_v7_B_C411": file_entry("scripts-v6-to-v7-B_C411.diff"),
        "scripts_diff_v7_to_v8": file_entry("scripts-v7-to-v8.diff"),
        "scripts_diff_v8_to_v9_Bcuts": file_entry("scripts-v8-to-v9-Bcuts.r2.diff"),
        "scripts_diff_v9_to_v10": file_entry("scripts-v9-to-v10.diff"),
        "assembler_v5_to_v6_generalization_hunks": file_entry("assembler-v5-to-v6-generalization.diff"),
        "v10_selftest": dict(file_entry("receipts/test-v10-selftest.selftest.json"),
                             all_ok=json.loads(K.read_regular(os.path.join(
                                 K.RECEIPTS, "test-v10-selftest.selftest.json"))).get("all_ok")),
        "review_packet_v10": file_entry("review-packet-v10.md"),
        "scripts_diff_v10_to_v11": file_entry("scripts-v10-to-v11.diff"),
        "v11_selftest": dict(file_entry("receipts/test-v11-selftest-r2.selftest.json"),
                             all_ok=json.loads(K.read_regular(os.path.join(
                                 K.RECEIPTS, "test-v11-selftest-r2.selftest.json"))).get("all_ok")),
        "v11_selftest_before_census_tries_change": file_entry("receipts/test-v11-selftest.selftest.json"),
        "review_packet_v11": file_entry("review-packet-v11.md"),
        "scripts_diff_v11_to_v12": file_entry("scripts-v11-to-v12.diff"),
        "v12_selftest": dict(file_entry("receipts/test-v12-selftest.selftest.json"),
                             all_ok=json.loads(K.read_regular(os.path.join(
                                 K.RECEIPTS, "test-v12-selftest.selftest.json"))).get("all_ok")),
        "review_packet_v12": file_entry("review-packet-v12.md"),
        "admitter_invariant": gate0.get("admitter_invariant"),
        "slot": gate0.get("slot"),
        "signal_smoke": dict(file_entry("receipts/smoke-v4-signal.smoke.json"),
                             all_ok=json.loads(K.read_regular(os.path.join(
                                 K.RECEIPTS, "smoke-v4-signal.smoke.json"))).get("all_ok")),
        "exception_path_test": dict(file_entry("receipts/test-v5-exception-path.test.json"),
                                    all_ok=json.loads(K.read_regular(os.path.join(
                                        K.RECEIPTS, "test-v5-exception-path.test.json"))).get("all_ok")),
        "superseded_scripts_diff": file_entry("scripts-v1-to-v2.diff"),
        "disarmed_v2_launcher": {"gate_receipt": file_entry("receipts/B_C321-a2.gate.json"),
                                 "log": file_entry("logs/launch-run-B_C321-a2.log")},
        "arming_line": json.loads(K.read_regular(os.path.join(
            K.LOGS, "launch-run-%s.log" % label)).decode().splitlines()[0]),
        "items": {label: {"receipt": "receipts/%s.json" % label, "receipt_sha256": item_sha, "status": row["status"],
                          "failed_conditions": row["failed_conditions"], "observed_outcome": row["observed_outcome"],
                          "stop": row["stop"], "strict_fields": row["strict_fields"], "times": row["times"],
                          "rss": row["rss"], "free_bytes": row["free_bytes"],
                          "checker_log_vs_producer": row["checker_log_vs_producer"]}},
        "regeneration_precheck": {"receipt": REGEN["rel"], "sha256": regen_sha,
                                  "result": regen_r.get("result"),
                                  "cnf_sha256": (regen_r.get("regen") or {}).get("cnf_sha256"),
                                  "producer_checks_all_true": (regen_r.get("producer") or {}).get("consistent"),
                                  "bound_to_gate_regen_receipt_sha256": regen_sha == gate0.get("regen_receipt_sha256")},
        "transport_selfcheck": {"summary": "receipts/selfcheck-summary.json", "summary_sha256": summ_sha,
                                "gate_receipt_sha256": sgate_sha,
                                "pre_receipt_sha256": file_entry("receipts/selfcheck.pre.json")["sha256"],
                                "all_ok": summ.get("all_ok"), "parser_all_ok": summ.get("parser_all_ok"),
                                "logic_ok": summ.get("logic_ok"), "parser_cases": len(summ.get("parser_cases", [])),
                                "logic_cases": len(summ.get("logic_cases", {})),
                                "rows": [{k: x.get(k) for k in ("label", "expectation_met", "solver_rc",
                                                                "solver_status_lines", "checker_rc",
                                                                "checker_status_lines", "receipt_sha256")}
                                         for x in summ.get("rows", [])],
                                "receipts_rehashed_equal": all(
                                    file_entry("receipts/%s.json" % x["label"])["sha256"] == x["receipt_sha256"]
                                    for x in summ.get("rows", []))},
        "deviations": {"path": names["dev"], "sha256": dev_sha, "count": len(dev),
                       "carried_from": "deviations-v1.json D1-D12, D14", "items": dev},
        "binaries_at_assembly": {"kissat": K.binary_record(K.KISSAT), "drat-trim": K.binary_record(K.DRAT),
                                 "python3": K.binary_record(K.PY)},
        "read_only_inputs_at_assembly": {p: K.sha_file(p) for p in ro},
        "scripts_sha256_now": K.script_hashes(), "run_scripts": run_scripts,
        "desk_files_before_result": files, "fifo_nodes": fifos, "desk_bytes_before_result": total,
        "pycache_present": {"lane_code": os.path.lexists(os.path.join(K.CODE, "__pycache__")),
                            "desk_scripts": os.path.lexists(os.path.join(K.SCRIPTS, "__pycache__"))},
    }
    result_sha = K.write_json_x(paths["result"], result)
    text = report(result, result_sha, row, item_sha)
    with open(paths["report"], "x") as f:
        f.write(text)
    print(json.dumps({"attempt_receipt_sha256": item_sha, "status": row["status"], "deviations_sha256": dev_sha,
                      names["result"]: result_sha, names["report"]: K.sha_file(paths["report"]),
                      "failed_conditions": row["failed_conditions"]}))


if __name__ == "__main__":
    main()
