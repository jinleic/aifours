#!/usr/bin/env python3
"""Assemble the item receipt, deviations, RESULT.json and REPORT.md of the parent B-side K3 cube replay desk
(review/moqls7-k3-B-cube-parent-replay-v1). Written after the B/C321 run.

Usage: assemble_B_v1.py ITEM          (ITEM: B_C321)

Reads the desk's receipts and logs (never modifies them), re-hashes every referenced file, checks the hash bindings
recorded at run time, re-hashes the read-only lane inputs and both binaries, and writes receipts/ITEM.json,
deviations-v1.json, RESULT.json and REPORT.md, each created exclusively. No native or other subprocess launch.
Item status: PASS only if every driver condition and every supervisor/binding condition holds; otherwise UNKNOWN.
"""
import json
import os
import stat
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bklib_v1 as K  # noqa: E402

DEVIATIONS = [
    {"id": "D1-wrapper-make-not-run",
     "what": "k3_cubes.make() was not executed: it calls os.makedirs(<lane>/explore/scratch), runs encoder B as a "
             "subprocess writing explore/scratch/k3_cube_B_base.cnf, and writes OUT.cnf/OUT.json as files, all "
             "forbidden here. scripts/compose_B_v1.py executes the hash-verified bytes of gram_enc.py, k3_cubes.py "
             "and gram_encB.py as modules and calls the pinned coverage(), variable_map(), cube_clauses() and "
             "gram_encB.main() unchanged; only make's encoder-B composition (header 'p cnf <nv> <nc+len(extra)>', "
             "base body, extra clauses) is restated. The producer's regeneration code k3_cube_certify_r3.py "
             "(da9c210e...ac78) and its drivers were not imported or run.",
     "evidence": "regenerated SHA-256 8b7b8124...12c6 equals the pin; base CNF 42a5f304...0aac equals the pin; support "
                 "sets, 18 cube units, same-ray identity and 88 extra clauses equal the producer metadata."},
    {"id": "D2-encoder-B-in-process",
     "what": "gram_encB.main() ran in the compose process with argv '--squares 3 --heavy --sym --out /dev/fd/<W>' "
             "(W: write end of an in-process anonymous pipe read into memory by a thread); its closing 'vars N "
             "clauses M' print went to an in-memory buffer and was checked against the header. make() runs the "
             "encoder as a subprocess writing a scratch file; the producer's r3 regeneration used --out /dev/stdout."},
    {"id": "D3-interpreter",
     "what": "CommandLineTools python3 3.9.6 (-I -B; realpath sha256 4c0dd940...6a60), environment reset to PATH="
             "/usr/bin:/bin:/usr/sbin:/sbin, TMPDIR=HOME=desk tmp/, LC_ALL=C, PYTHONDONTWRITEBYTECODE=1, cwd desk "
             "tmp/ (plus the supervisor's K3_SUPERVISOR_* variables for the run)."},
    {"id": "D4-native-limits",
     "what": "kissat -q -f --time=5400 and drat-trim -i -t 9000 per the brief; the producer r6 used --time=3600 and "
             "-t 7200. Driver wall backstop 9300 s; supervisor wall 10200 s, grace 180 s. None was reached."},
    {"id": "D5-transport",
     "what": "The CNF bytes stayed in driver memory and reached kissat and drat-trim through two anonymous pipes "
             "(/dev/fd/N), each written by a measured writer (bytes and SHA-256 of exactly what os.write accepted); "
             "the producer gave both programs the lane CNF file path. The binary DRAT proof went kissat -> desk FIFO "
             "-> drat-trim stdin (-i) with a driver-held keepalive write end. Proofs were neither retained nor "
             "hashed; zero-length FIFO nodes remain in fifo/."},
    {"id": "D6-checker-binary",
     "what": "The parent-built drat-trim (a46c0c71...8e37) was used per the brief, not the producer's lane build "
             "(111b0405...d5e4). No lrat-check."},
    {"id": "D7-capacity-rule-changes",
     "what": "The brief's launch condition (a) was replaced by Main twice: about 04:05 PDT (route-A-running or "
             "route-B-started rule) and about 04:20 PDT (this desk owns lane slot 2; launch once regeneration and "
             "self-checks pass, with a fresh free-space gate >= 12.2e9 + growth and a fresh scan showing <= 2 busy "
             "lane processes). launch_B_v1.py implements the slot-2 rule (<= 2 busy lane natives, lane RSS + 2 GiB "
             "projected peak <= 8 GiB, computable cap >= 2.5 GiB, free >= 12,201,048,576 B, before 15:30 PDT); route "
             "flags are recorded for information only. The self-checks passed the same gate (selfcheck.gate.json)."},
    {"id": "D8-rss-cap",
     "what": "Supervisor --rss-cap and driver --rss-stop 3,758,096,384 B = min(3.5 GiB, 8 GiB - reservations - "
             "128 MiB); reservations = declared --rss-cap of other supervised lane runs (route A C311: 3.5 GiB) + "
             "3.5 GiB per unsupervised lane native group (none) + current RSS of other lane processes + 256 MiB. "
             "With both runs inside their caps the lane total stays <= 7.5 GiB plus small uncapped processes."},
    {"id": "D9-selfcheck-limits",
     "what": "Self-checks used the same binaries and transport code with kissat --time=60, drat-trim -t 60, a 180 s "
             "backstop and a 1 GiB RSS stop, under the driver's own guards, not under the supervisor. They test this "
             "desk's plumbing and verdict code only."},
    {"id": "D10-strict-pass-rule",
     "what": "PASS needs: CNF SHA-256 = pin; supervised by the pinned supervise_r3.py; pins and binaries equal at "
             "start, spawn and end; solver rc 20 and status lines exactly ['s UNSATISFIABLE']; checker rc 0 and "
             "exactly ['s VERIFIED'] (only CR removed); 'NOT VERIFIED' and 'TIMEOUT' absent from both logs; both "
             "measured feeds complete with length and SHA-256 = pin; no deferral, no stop, no SIGTERM, no driver "
             "signal; all children reaped; supervisor completed cleanly with no trip and no quarantine. Otherwise "
             "UNKNOWN."},
    {"id": "D11-bmap-oracle-cited",
     "what": "The B-map oracle receipt evidence/k3cubes/bmap_oracle_r1.json (6e2bd95e...952c, status PASS, encoder "
             "pins equal) is cited, not rerun. This desk did not re-derive encoder B's variable map; the K3 cube "
             "clauses use k3_cubes.variable_map()."},
    {"id": "D12-incident-stale-fifo-open",
     "what": "Before the desk existed (about 04:03-04:09 PDT), a read-only 'shasum -a 256 cert_B_r6/*' glob opened "
             "the stale producer FIFO cert_B_r6/B_C321.drat.fifo (no writer; that run had ended 03:58) and blocked "
             "until the tool's 300 s deadline ended it. It had hashed only B_C321.checker.log and "
             "B_C321.checkpoints.jsonl and never reached the live B_C411.drat.fifo; no FIFO data was read. Since "
             "then every lane read in this desk is guarded by lstat S_ISREG."},
    {"id": "D13-floor-stop",
     "what": "The native run was stopped by the supervisor's free-space floor trip (free 11,972,313,088 < "
             "12,000,000,000 B) at 04:53:03 PDT, 1839.8 s into the pipeline: killpg SIGTERM to the driver's group, "
             "kissat and drat-trim exited by signal 15, no survivors, no quarantine. Status UNKNOWN. Not retried "
             "(Main: no retry without parent GO). This desk retained about 0.2 MB in total, and no CNF or proof went "
             "to disk. Observed after the stop (04:53:41 PDT, outside the receipts): vm.swapusage reported 160.94M "
             "used of 1024.00M; tmutil listed local snapshots 2026-10-18-005459, -015506, -025516, -035521 and "
             "-040955; df then showed 12,097,780 KiB available. The cause of the drop was not established."},
    {"id": "D14-lane-cnf-copy-hashed",
     "what": "The lane CNF copy explore/k3cubes/B_C321.cnf was hashed read-only (= pin) for the record only; it was "
             "never given to the solver or the checker."},
    {"id": "D15-assembler-after-run",
     "what": "scripts/assemble_B_v1.py was created after the run (the four run scripts were unchanged from the "
             "regeneration check to the end of the run); REPORT.md is generated from the same data as RESULT.json."},
]


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


def item_receipt(item):
    it = K.ITEMS[item]
    pre, pre_sha = load("receipts/%s.pre.json" % item)
    launch, launch_sha = load("receipts/%s.launch.json" % item)
    drv, drv_sha = load("receipts/%s.driver.json" % item)
    sup, sup_sha = load("receipts/%s.supervisor.json" % item)
    gate, gate_sha = load("receipts/%s.gate.json" % item)
    outc, outc_sha = load("receipts/%s.launch-outcome.json" % item)
    regen_r, regen_sha = load("receipts/regen-%s.json" % item)
    summ, summ_sha = load("receipts/selfcheck-summary.json")
    rec = drv.get("pipeline") or {}
    ch = rec.get("children") or {}
    logs = {}
    for key in ("solver_log", "checker_log", "checkpoints"):
        e = file_entry(rec[key])
        e["equals_driver_receipt"] = e["sha256"] == rec.get(key + "_sha256" if key != "checkpoints"
                                                             else "checkpoints_sha256")
        logs[key] = e
    for rel in ("logs/driver-run-%s.log" % item, "logs/%s.supervisor-stdout.log" % item,
                "logs/launch-run-%s.log" % item):
        logs[os.path.basename(rel)] = file_entry(rel)
    quarantine = os.path.join(K.RECEIPTS, item + ".QUARANTINE.json")
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
                                "note": ("the driver received the group SIGTERM; both children had already exited "
                                         "by signal 15 at its next sample, so it sent no SIGTERM of its own and "
                                         "reaped both")},
                "quarantine": sup.get("quarantine_record"), "survivors": (sup.get("stop") or {}).get("survivors")}
    prod = pre["producer"]["receipt_fields"]
    return {
        "item": item, "encoder": it["encoder"], "cube": it["cube"], "status": status,
        "status_rule": "PASS only if every condition below holds; otherwise UNKNOWN (deviations D10, D13)",
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
        "receipts": {"pre": {"path": "receipts/%s.pre.json" % item, "sha256": pre_sha},
                     "launch": {"path": "receipts/%s.launch.json" % item, "sha256": launch_sha},
                     "driver": {"path": "receipts/%s.driver.json" % item, "sha256": drv_sha},
                     "supervisor": {"path": "receipts/%s.supervisor.json" % item, "sha256": sup_sha},
                     "gate": {"path": "receipts/%s.gate.json" % item, "sha256": gate_sha},
                     "launch_outcome": {"path": "receipts/%s.launch-outcome.json" % item, "sha256": outc_sha},
                     "regen_precheck": {"path": "receipts/regen-%s.json" % item, "sha256": regen_sha},
                     "selfcheck_summary": {"path": "receipts/selfcheck-summary.json", "sha256": summ_sha}},
        "logs": logs,
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
        "scope": ("Instance-level replay record for the exact B/C321 CNF only (SHA-256 8b7b8124...12c6). Status "
                  "UNKNOWN means this desk neither confirms nor refutes the producer's certificate. No K3, M(7), "
                  "coverage, bridge or theorem verdict."),
    }


def fmt(n):
    return "{:,}".format(n) if isinstance(n, int) else str(n)


def report(result, result_sha, item_row, item_sha):
    r = item_row
    sf = r["strict_fields"]
    t = r["times"]
    lines = [
        "# Parent replay of the phys-2 K3 cube certificate B/C321 (MOQLS(7), encoder B)", "",
        "Desk: `review/moqls7-k3-B-cube-parent-replay-v1/`, 2026-10-18 PDT. RESULT.json sha256 `%s`." % result_sha,
        "Generated by `scripts/assemble_B_v1.py` from the same data as RESULT.json.", "",
        "## Verdict", "",
        "| item | status | regenerated CNF sha256 = pin | solver rc / status lines | checker rc / status lines | stop |",
        "|---|---|---|---|---|---|",
        "| B_C321 | **%s** | `%s` %s | %s / `%s` | %s / `%s` | %s |" % (
            r["status"], sf["regenerated_cnf_sha256"], "yes" if sf["cnf_hash_match"] else "NO", sf["solver_rc"],
            sf["solver_status_lines"], sf["checker_rc"], sf["checker_status_lines"],
            (r["stop"] or {}).get("reason", "none")), "",
        "Item receipt `receipts/B_C321.json` sha256 `%s`." % item_sha, "",
        "Failed conditions: %s." % (", ".join("`%s`" % c for c in r["failed_conditions"]) or "none"),
        "Observed outcome: %s." % r["observed_outcome"], "",
        "Scope: %s" % r["scope"], "",
        "## What happened", "",
        "- Regeneration (desk composition driver, pinned encoder B + cube wrapper, in memory): `%s`, %s bytes, "
        "header `%s`, %s s." % (sf["regenerated_cnf_sha256"], fmt(sf["cnf_bytes"]), sf["cnf_header"],
                                t["regeneration_seconds"]),
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
        "- Producer r6 for comparison: %s s, solver rc %s, checker rc %s, %s, peak %s B." % (
            r["producer_receipt"]["fields"]["seconds"], r["producer_receipt"]["fields"]["solver_rc"],
            r["producer_receipt"]["fields"]["checker_rc"], r["producer_receipt"]["fields"]["checker_status_lines"],
            fmt(r["producer_receipt"]["fields"]["peak_sampled_aggregate_rss_bytes"])), "",
        "## Checks before the native run", "",
        "- Regeneration-only precheck: %s (`receipts/regen-B_C321.json` `%s`)." % (
            result["regeneration_precheck"]["result"], result["regeneration_precheck"]["sha256"]),
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
    lines.append("- The four run scripts were recorded at %s; all recordings equal: %s; equal now: %s." % (
        ", ".join(result["run_scripts"]["recording_points"]), result["run_scripts"]["all_recordings_equal"],
        result["run_scripts"]["equal_now_excluding_assembler"]))
    lines += ["", "## Receipts and logs of the item (sha256)", ""]
    for k, v in r["receipts"].items():
        lines.append("- %s `%s` `%s`" % (k, v["path"], v["sha256"]))
    for k, v in r["logs"].items():
        lines.append("- %s `%s` %s B `%s`" % (k, v["path"], fmt(v["bytes"]), v["sha256"]))
    lines += ["", "## Deviations (full text: `deviations-v1.json`)", ""]
    for d in DEVIATIONS:
        lines.append("- %s: %s" % (d["id"], d["what"]))
    lines += ["", "## Integrity", "",
              "Receipts, logs, RESULT.json, REPORT.md and deviations-v1.json were created exclusively (mode 'x' / "
              "O_EXCL). The scripts were created with the editor before their first use. bklib_v1.py was edited "
              "once, before any script hash was recorded, to apply Main's slot-2 admission rule. From the first "
              "recorded hash on, nothing in the desk was modified, deleted or renamed. No lane file was written. "
              "There were no /tmp writes and no Git, network or model CLI. __pycache__ present: %s. Desk regular "
              "files before RESULT.json: %d, %s bytes in total. FIFO nodes, never opened outside the pipeline: %s." % (
                  result["pycache_present"], len(result["desk_files_before_result"]),
                  fmt(result["desk_bytes_before_result"]), ", ".join(result["fifo_nodes"])), ""]
    lines += ["| file | bytes | sha256 |", "|---|---|---|"]
    for e in result["desk_files_before_result"]:
        lines.append("| `%s` | %s | `%s` |" % (e["path"], fmt(e.get("bytes")), e.get("sha256")))
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in K.ITEMS:
        raise SystemExit(__doc__)
    item = sys.argv[1]
    paths = {"item": os.path.join(K.RECEIPTS, item + ".json"), "dev": os.path.join(K.DESK, "deviations-v1.json"),
             "result": os.path.join(K.DESK, "RESULT.json"), "report": os.path.join(K.DESK, "REPORT.md")}
    for p in paths.values():
        if os.path.lexists(p):
            raise SystemExit("exists: " + p)
    row = item_receipt(item)
    item_sha = K.write_json_x(paths["item"], row)
    dev_sha = K.write_json_x(paths["dev"], DEVIATIONS)
    regen_r, regen_sha = load("receipts/regen-%s.json" % item)
    summ, summ_sha = load("receipts/selfcheck-summary.json")
    sgate, sgate_sha = load("receipts/selfcheck.gate.json")
    ro = [os.path.join(K.CODE, n) for n in ("gram_enc.py", "k3_cubes.py", "gram_encB.py", "supervise_r3.py")]
    ro += [K.ITEMS[item]["producer_receipt"], K.ITEMS[item]["meta"], K.ORACLE_RECEIPT,
           K.ITEMS[item]["producer_checker_log"], K.ITEMS[item]["producer_solver_log"], K.ITEMS[item]["lane_cnf"]]
    files, fifos, total = desk_listing(exclude=("RESULT.json", "REPORT.md"))
    seen = {"regen.pre": regen_r.get("scripts_sha256"), "regen.end": regen_r.get("scripts_sha256_end"),
            "selfcheck.gate": sgate.get("scripts_sha256"),
            "selfcheck.pre": load("receipts/selfcheck.pre.json")[0].get("scripts_sha256"),
            "selfcheck.end": summ.get("scripts_sha256_end"),
            "run.gate": load("receipts/%s.gate.json" % item)[0].get("scripts_sha256"),
            "run.pre": load("receipts/%s.pre.json" % item)[0].get("scripts_sha256"),
            "run.end": load("receipts/%s.driver.json" % item)[0].get("scripts_sha256_end")}
    now_run = {n: h for n, h in K.script_hashes().items() if n != "assemble_B_v1.py"}
    run_scripts = {"recorded": seen["regen.pre"], "all_recordings_equal": all(v == seen["regen.pre"]
                                                                                for v in seen.values()),
                   "equal_now_excluding_assembler": now_run == seen["regen.pre"],
                   "recording_points": sorted(seen)}
    result = {
        "desk": "review/moqls7-k3-B-cube-parent-replay-v1",
        "scope": row["scope"],
        "verdicts": {item: row["status"]},
        "items": {item: {"receipt": "receipts/%s.json" % item, "receipt_sha256": item_sha, "status": row["status"],
                         "failed_conditions": row["failed_conditions"], "observed_outcome": row["observed_outcome"],
                         "stop": row["stop"], "strict_fields": row["strict_fields"], "times": row["times"],
                         "rss": row["rss"], "free_bytes": row["free_bytes"]}},
        "regeneration_precheck": {"receipt": "receipts/regen-%s.json" % item, "sha256": regen_sha,
                                  "result": regen_r.get("result"),
                                  "cnf_sha256": (regen_r.get("regen") or {}).get("cnf_sha256"),
                                  "producer_checks_all_true": (regen_r.get("producer") or {}).get("consistent")},
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
        "deviations": {"path": "deviations-v1.json", "sha256": dev_sha, "count": len(DEVIATIONS)},
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
    print(json.dumps({"item_receipt_sha256": item_sha, "status": row["status"], "deviations_sha256": dev_sha,
                      "RESULT.json": result_sha, "REPORT.md": K.sha_file(paths["report"]),
                      "failed_conditions": row["failed_conditions"]}))


if __name__ == "__main__":
    main()
