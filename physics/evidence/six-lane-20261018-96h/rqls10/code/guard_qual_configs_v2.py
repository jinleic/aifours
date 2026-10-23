#!/usr/bin/env python3
"""guard_qual_configs_v2: write ONE guard-qualification config for code/owned_supervisor_v6.py (plan
evidence/owned_supervisor_v6-guard-qualification-plan-v2.md). Supersedes guard_qual_configs_v1.py (never run): adds the
rc_nonzero, missing_output, mutate_pin and mutate_evidence scenarios and takes the outstanding reservations as
arguments. Metadata only: creates the scenario run directory (mkdir, never deletes), for mutate_pin one scratch file
to be pinned, and the config file (exclusive create); starts no process. Run by the integration owner immediately
before each scenario so that the GO and the fresh stability receipt are bound.
Usage: guard_qual_configs_v2.py SCENARIO BASE_DIR GO_PATH GO_SHA STAB_PATH STAB_SHA CHILD_SRC CHILD_SHA PY_REAL PY_SHA
       OUTSTANDING_BYTES LANE_OUTSTANDING_BYTES
Prints the config path and its sha256.
"""
import hashlib, json, os, sys

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
SC = {
    # name: (mode, life_s, max_wall_s, fault, out_required, rss_trip_bytes, target)
    "date_fault": ("ok", 5, 60, "date_helper_fails", True, 2147483648, None),
    "ok": ("ok", 5, 60, None, True, 2147483648, None),
    "rc_nonzero": ("rc_nonzero", 5, 60, None, True, 2147483648, None),
    "missing_output": ("no_output", 5, 60, None, True, 2147483648, None),
    "mutate_pin": ("mutate_pin", 5, 60, None, True, 2147483648, "PIN"),
    "mutate_evidence": ("mutate_evidence", 5, 60, None, True, 2147483648, "LAUNCH_RECORD"),
    "deadline": ("sleep", 120, 10, None, False, 2147483648, None),
    "flood": ("flood", 60, 60, None, False, 2147483648, None),
    "busy": ("busy3", 60, 60, None, False, 2147483648, None),
    "rss": ("rss", 60, 60, None, False, 268435456, None),
    "escape_slow": ("escape_slow", 40, 60, None, True, 2147483648, None),
    "escape_fast": ("escape_fast", 40, 60, None, True, 2147483648, None),
    "ignore": ("ignore_term", 60, 10, None, False, 2147483648, None),
    "identity": ("sleep", 60, 10, "identity_check_fails", False, 2147483648, None),
}


def main():
    (name, base, go, go_sha, stab, stab_sha, child, child_sha, py, py_sha, outst, lane_outst) = sys.argv[1:13]
    mode, life, wall, fault, req, rss_trip, target = SC[name]
    run = os.path.join(os.path.abspath(base), name)
    os.makedirs(run, exist_ok=False)
    out = os.path.join(run, "child-out.json")
    launch = os.path.join(run, "launch.json")
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
    cfg = {
        "item": "owned_supervisor_v6 guard qualification: %s" % name, "owner": "ContinueRQLS10b",
        "purpose": "guard-qualification", "lane": LANE, "argv": argv,
        "env": {"TMPDIR": LANE + "/tmp", "PYTHONDONTWRITEBYTECODE": "1", "OPENBLAS_NUM_THREADS": "1",
                "OMP_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1", "MKL_NUM_THREADS": "1"},
        "stdout": os.path.join(run, "stdout.txt"), "stderr": os.path.join(run, "stderr.txt"),
        "stdout_cap_bytes": 1048576, "stderr_cap_bytes": 1048576,
        "outputs": [{"path": out, "required": req}],
        "launch_record": launch, "samples": os.path.join(run, "samples.jsonl"),
        "samples_cap_bytes": 2097152, "receipt": os.path.join(run, "supervisor-receipt.json"),
        "settlement_record": os.path.join(run, "settlement.json"), "output_roots": [run], "pins": pins,
        "max_wall_s": wall, "settle_s": 20, "sample_s": 1.0, "max_chunk_seconds": 10800,
        "owned_compute_settled_by_epoch": 1792731393.0, "rss_trip_bytes": rss_trip, "free_trip_bytes": 12200000000,
        "output_trip_bytes": 9437184, "launch_free_min_bytes": 12200000000, "lane_roots": [LANE, run],
        "lane_disk_root": LANE, "lane_disk_baseline_bytes": 0, "lane_disk_ceiling_bytes": 10737418240,
        "lane_walk_s": 5.0, "busy_limit": 2, "busy_cpu_fraction": 0.5, "rss_projection_bytes": 67108864,
        "admission": {"go_path": go, "go_sha256": go_sha, "reservation_bytes": 4194304,
                      "outstanding_reservations_bytes": int(outst), "lane_outstanding_reservations_bytes": int(lane_outst),
                      "stability_receipt_path": stab, "stability_receipt_sha256": stab_sha,
                      "stability_max_age_s": 300, "require_settled": []},
        "helper_budget": {"max_calls": 32, "call_budget_s": 5.0, "term_grace_s": 5.0},
        "fault_injection": ({fault: True} if fault else {})}
    path = os.path.join(run, "config.json")
    data = (json.dumps(cfg, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(path, "xb") as fh:
        fh.write(data)
    print(path, hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
