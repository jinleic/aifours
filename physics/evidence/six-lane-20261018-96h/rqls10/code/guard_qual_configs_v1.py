#!/usr/bin/env python3
"""guard_qual_configs_v1: write ONE guard-qualification config for code/owned_supervisor_v5.py (plan
evidence/owned_supervisor_v5-guard-qualification-plan-v1.md). Metadata only: creates the scenario run directory
(mkdir, never deletes) and the config file (exclusive create); starts no process. Intended to be run by the
integration owner immediately before each scenario so that the GO and the fresh stability receipt are bound.
Usage: guard_qual_configs_v1.py SCENARIO BASE_DIR GO_PATH GO_SHA STAB_PATH STAB_SHA CHILD_SRC CHILD_SHA PY_REAL PY_SHA
Prints the config path and its sha256.
"""
import hashlib, json, os, sys

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
SC = {
    # name: (mode, life_s, max_wall_s, settle_s, fault, out_required, rss_trip_bytes, stdout_cap_bytes)
    "ok": ("ok", 5, 60, 20, None, True, 2147483648, 1048576),
    "flood": ("flood", 60, 60, 20, None, False, 2147483648, 1048576),
    "deadline": ("sleep", 120, 10, 20, None, False, 2147483648, 1048576),
    "ignore": ("ignore_term", 60, 10, 20, None, False, 2147483648, 1048576),
    "identity": ("sleep", 60, 10, 20, "identity_check_fails", False, 2147483648, 1048576),
    "escape_slow": ("escape_slow", 40, 60, 20, None, True, 2147483648, 1048576),
    "escape_fast": ("escape_fast", 40, 60, 20, None, True, 2147483648, 1048576),
    "busy": ("busy3", 60, 60, 20, None, False, 2147483648, 1048576),
    "rss": ("rss", 60, 60, 20, None, False, 268435456, 1048576),
    "date_fault": ("ok", 5, 60, 20, "date_helper_fails", True, 2147483648, 1048576),
}


def main():
    (name, base, go, go_sha, stab, stab_sha, child, child_sha, py, py_sha) = sys.argv[1:11]
    mode, life, wall, settle, fault, req, rss_trip, out_cap = SC[name]
    run = os.path.join(os.path.abspath(base), name)
    os.makedirs(run, exist_ok=False)
    out = os.path.join(run, "child-out.json")
    cfg = {
        "item": "owned_supervisor_v5 guard qualification: %s" % name, "owner": "ContinueRQLS10b",
        "purpose": "guard-qualification", "lane": LANE,
        "argv": [py, "-I", "-B", child, mode, out, str(life)],
        "env": {"TMPDIR": LANE + "/tmp", "PYTHONDONTWRITEBYTECODE": "1", "OPENBLAS_NUM_THREADS": "1",
                "OMP_NUM_THREADS": "1", "VECLIB_MAXIMUM_THREADS": "1", "MKL_NUM_THREADS": "1"},
        "stdout": os.path.join(run, "stdout.txt"), "stderr": os.path.join(run, "stderr.txt"),
        "stdout_cap_bytes": out_cap, "stderr_cap_bytes": 1048576,
        "outputs": [{"path": out, "required": req}],
        "launch_record": os.path.join(run, "launch.json"), "samples": os.path.join(run, "samples.jsonl"),
        "samples_cap_bytes": 2097152, "receipt": os.path.join(run, "supervisor-receipt.json"),
        "settlement_record": os.path.join(run, "settlement.json"), "output_roots": [run],
        "pins": [{"path": child, "sha256": child_sha}, {"path": py, "sha256": py_sha}],
        "max_wall_s": wall, "settle_s": settle, "sample_s": 1.0, "max_chunk_seconds": 10800,
        "owned_compute_settled_by_epoch": 1792731393.0, "rss_trip_bytes": rss_trip, "free_trip_bytes": 12200000000,
        "output_trip_bytes": 9437184, "launch_free_min_bytes": 12200000000, "lane_roots": [LANE, run],
        "lane_disk_root": LANE, "lane_disk_baseline_bytes": 0, "lane_disk_ceiling_bytes": 10737418240,
        "lane_walk_s": 5.0, "busy_limit": 2, "busy_cpu_fraction": 0.5, "rss_projection_bytes": 67108864,
        "admission": {"go_path": go, "go_sha256": go_sha, "reservation_bytes": 4194304,
                      "outstanding_reservations_bytes": 0, "lane_outstanding_reservations_bytes": 0,
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
