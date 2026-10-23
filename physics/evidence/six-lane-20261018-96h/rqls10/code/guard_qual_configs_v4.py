#!/usr/bin/env python3
"""guard_qual_configs_v4: write ONE guard-qualification config for code/owned_supervisor_v7.py (plan
evidence/owned_supervisor_v7-guard-qualification-plan-v4.md). Supersedes guard_qual_configs_v3.py (never run) after the
parent's pre-review: the busy scenario runs child mode busy2 (two CPU-bound processes in total) with busy_limit 1, so
the first observed excess trips BUSY while the lane never exceeds the unchanged limit of 2 busy processes; every other
scenario keeps busy_limit 2. mutate_* targets are fixtures created for this scenario only (RUN/pinned-scratch.txt;
RUN/out/launch.json written by this scenario's supervisor). v7 schema (no pinned GO/stability sha256 in the config, no
require_settled, no lane_disk_baseline_bytes), an EMPTY output root RUN/out, TMPDIR RUN/tmp, stability receipt path
RUN/stability.json (written later by the stability gate), reservation 20971520 bytes. Metadata only: creates RUN,
RUN/out and RUN/tmp (mkdir, never deletes; RUN must not exist), for mutate_pin one scratch file to be pinned (in RUN,
outside the output root), and RUN/config.json (exclusive create); starts no process.
Usage: guard_qual_configs_v4.py SCENARIO BASE_DIR GO_PATH CHILD_SRC CHILD_SHA PY_REAL PY_SHA OUTSTANDING_BYTES
       LANE_OUTSTANDING_BYTES
Prints one JSON line: config path, config sha256 and the GO entry the parent would list under "configs" for this sha256
(the parent deliberately omits the go_unlisted entry). All configs share one item string so one GO file can cover them.
"""
import hashlib, json, os, sys

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
ITEM = "owned_supervisor_v7 guard qualification"
RESERVATION = 20971520
SC = {
    # name: (mode, life_s, max_wall_s, fault, out_required, rss_trip_bytes, target)
    "date_fault": ("ok", 5, 60, "date_helper_fails", True, 2147483648, None),
    "go_unlisted": ("ok", 5, 60, None, True, 2147483648, None),
    "ok": ("ok", 5, 60, None, True, 2147483648, None),
    "rc_nonzero": ("rc_nonzero", 5, 60, None, True, 2147483648, None),
    "missing_output": ("no_output", 5, 60, None, True, 2147483648, None),
    "mutate_pin": ("mutate_pin", 5, 60, None, True, 2147483648, "PIN"),
    "mutate_evidence": ("mutate_evidence", 5, 60, None, True, 2147483648, "LAUNCH_RECORD"),
    "stray_file": ("stray_file", 5, 60, None, True, 2147483648, None),
    "deadline": ("sleep", 120, 10, None, False, 2147483648, None),
    "flood": ("flood", 60, 60, None, False, 2147483648, None),
    "busy": ("busy2", 60, 60, None, False, 2147483648, None),
    "rss": ("rss", 60, 60, None, False, 268435456, None),
    "zombie_hold": ("zombie_hold", 10, 60, None, True, 2147483648, None),
    "escape_slow": ("escape_slow", 40, 60, None, True, 2147483648, None),
    "escape_fast": ("escape_fast", 40, 60, None, True, 2147483648, None),
    "double_fork_escape": ("double_fork_escape", 40, 60, None, True, 2147483648, None),
    "ignore": ("ignore_term", 60, 10, None, False, 2147483648, None),
    "identity": ("sleep", 60, 10, "identity_check_fails", False, 2147483648, None),
}


def main():
    (name, base, go, child, child_sha, py, py_sha, outst, lane_outst) = sys.argv[1:10]
    mode, life, wall, fault, req, rss_trip, target = SC[name]
    run = os.path.join(os.path.abspath(base), name)
    os.makedirs(run, exist_ok=False)
    outd = os.path.join(run, "out")
    os.mkdir(outd)
    os.mkdir(os.path.join(run, "tmp"))
    out = os.path.join(outd, "child-out.json")
    launch = os.path.join(outd, "launch.json")
    pins = [{"path": child, "sha256": child_sha}, {"path": py, "sha256": py_sha}]
    argv = [py, "-I", "-B", child, mode, out, str(life)]
    if target == "PIN":
        scratch = os.path.join(run, "pinned-scratch.txt")
        data = b"pinned scratch file for the mutate_pin scenario\n"
        with open(scratch, "xb") as fh:
            fh.write(data)
        pins.append({"path": scratch, "sha256": hashlib.sha256(data).hexdigest()})
        argv.append(scratch)
    elif target == "LAUNCH_RECORD":
        argv.append(launch)
    outstanding, lane_outstanding = int(outst), int(lane_outst)
    cfg = {
        "item": ITEM, "owner": "ContinueRQLS10b", "purpose": "guard-qualification", "lane": LANE, "argv": argv,
        "env": {"TMPDIR": os.path.join(run, "tmp"), "PYTHONDONTWRITEBYTECODE": "1", "OPENBLAS_NUM_THREADS": "1",
                "OMP_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1", "MKL_NUM_THREADS": "1"},
        "stdout": os.path.join(outd, "stdout.txt"), "stderr": os.path.join(outd, "stderr.txt"),
        "stdout_cap_bytes": 1048576, "stderr_cap_bytes": 1048576,
        "outputs": [{"path": out, "required": req}],
        "launch_record": launch, "samples": os.path.join(outd, "samples.jsonl"),
        "samples_cap_bytes": 2097152, "receipt": os.path.join(outd, "supervisor-receipt.json"),
        "settlement_record": os.path.join(outd, "settlement.json"), "output_roots": [outd], "pins": pins,
        "max_wall_s": wall, "settle_s": 20, "sample_s": 1.0, "max_chunk_seconds": 10800,
        "owned_compute_settled_by_epoch": 1792731393.0, "rss_trip_bytes": rss_trip, "free_trip_bytes": 12200000000,
        "output_trip_bytes": 9437184, "launch_free_min_bytes": 12200000000, "lane_roots": [LANE],
        "lane_disk_root": LANE, "lane_disk_ceiling_bytes": 10737418240, "lane_walk_s": 5.0,
        "busy_limit": 1 if name == "busy" else 2,
        "busy_cpu_fraction": 0.5, "rss_projection_bytes": 67108864,
        "admission": {"go_path": go, "reservation_bytes": RESERVATION, "outstanding_reservations_bytes": outstanding,
                      "lane_outstanding_reservations_bytes": lane_outstanding,
                      "stability_receipt_path": os.path.join(run, "stability.json"), "stability_max_age_s": 300},
        "helper_budget": {"max_calls": 8, "call_budget_s": 5.0, "term_grace_s": 5.0},
        "fault_injection": ({fault: True} if fault else {})}
    path = os.path.join(run, "config.json")
    data = (json.dumps(cfg, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(path, "xb") as fh:
        fh.write(data)
    go_entry = {"output_roots": [outd], "argv": argv, "max_wall_s": wall, "reservation_bytes": RESERVATION,
                "outstanding_reservations_bytes": outstanding, "lane_outstanding_reservations_bytes": lane_outstanding}
    print(json.dumps({"scenario": name, "config": path, "config_sha256": hashlib.sha256(data).hexdigest(),
                      "item": ITEM, "go_entry": go_entry, "list_in_go": name != "go_unlisted"}, sort_keys=True))


if __name__ == "__main__":
    main()
