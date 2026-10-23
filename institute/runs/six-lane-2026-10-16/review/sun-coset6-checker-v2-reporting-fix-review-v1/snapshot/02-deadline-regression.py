#!/usr/bin/env python3
"""
test_deadline_injection_v1.py -- regression for the deadline reporting defect of checker_v1.py
(final Codex composition review, sun-coset6-composition-final-v1-codex-v1.note.md, MAJOR at
lines 7-13).

One run of the given checker's main() on the pinned engine-v3 inputs, inside this process, with a
clock injection and nothing else changed:
  * check_orbit_coverage is wrapped; when its 8th call (coverage of the LAST type) returns, a flag
    is set;
  * from then on the checker module's time.time() returns real time + 1e6 s, so the time budget
    has expired before the witness loop starts (all other time functions stay real);
  * check_rule is wrapped only to count calls (expected: 0).

--expect bug-reproduced  (checker_v1): main returns 0 and the verdict is PASS although the per-rule
                          tallies show all 61124 witnesses incomplete and 0 verified.
--expect fixed           (checker_v2): main returns non-zero, the verdict is INCOMPLETE, and all
                          61124 skipped witnesses are listed in the global incomplete list.

Standard library only; one process; all outputs are new files in a new directory (open mode 'x').
Usage:
  TMPDIR=<own tmp dir> PYTHONDONTWRITEBYTECODE=1 python3 test_deadline_injection_v1.py \
      --checker checker_vN.py --checker-sha256 HEX --engine-dir DIR --out-dir NEWDIR --expect MODE
"""
import argparse
import hashlib
import importlib.util
import json
import os
import resource
import sys
import time as real_time

PINNED_INPUTS = {
    "run.json": "6d8dc91dc6160a9a141da7e9bd0edba1b446aa2aaf9959e92fd05ac14babe754",
    "orbits.jsonl.gz": "a580c5801b03ed84edcdf9f58618b4fb0c0d390549dab31527d8a9da20f4dc49",
    "rlp_duals.json": "bbf91e057072d2840ee478a813dbebdc2266e6587e20e1c876b8da16177895ef",
    "survivors.json": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
}
N_LINES = 61124
N_TYPES = 8
JUMP_SECONDS = 1.0e6
SKIP_SUFFIX = "witness not checked before deadline"


def sha256_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--checker", required=True)
    ap.add_argument("--checker-sha256", required=True)
    ap.add_argument("--engine-dir", required=True)
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--expect", required=True, choices=("bug-reproduced", "fixed"))
    args = ap.parse_args(argv)
    sys.dont_write_bytecode = True
    tmpdir = os.environ.get("TMPDIR", "")
    if not (tmpdir and os.path.isdir(tmpdir)):
        raise SystemExit("TMPDIR must be set to an existing own directory")
    inputs = {}
    for name, want in PINNED_INPUTS.items():
        p = os.path.join(args.engine_dir, name)
        got = sha256_file(p)
        inputs[p] = got
        if got != want:
            raise SystemExit("pinned input mismatch: %s %s != %s" % (p, got, want))
    checker_sha = sha256_file(args.checker)
    if checker_sha != args.checker_sha256:
        raise SystemExit("checker sha256 %s != pinned %s" % (checker_sha, args.checker_sha256))
    os.makedirs(args.out_dir, exist_ok=False)

    spec = importlib.util.spec_from_file_location("checker_under_injection", args.checker)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    state = {"coverage_calls": 0, "flag": False, "check_rule_calls": 0,
             "check_rule_calls_after_flag": 0, "clock_reads_after_flag": 0}
    real_coverage = mod.check_orbit_coverage
    real_check_rule = mod.check_rule

    def wrapped_coverage(*a, **kw):
        r = real_coverage(*a, **kw)
        state["coverage_calls"] += 1
        if state["coverage_calls"] == N_TYPES:
            state["flag"] = True
        return r

    def counted_check_rule(*a, **kw):
        state["check_rule_calls"] += 1
        if state["flag"]:
            state["check_rule_calls_after_flag"] += 1
        return real_check_rule(*a, **kw)

    class InjectedClock:
        """The checker module's view of the time module: real, except time() after the flag."""

        def __getattr__(self, name):
            return getattr(real_time, name)

        def time(self):
            if state["flag"]:
                state["clock_reads_after_flag"] += 1
                return real_time.time() + JUMP_SECONDS
            return real_time.time()

    mod.check_orbit_coverage = wrapped_coverage
    mod.check_rule = counted_check_rule
    mod.time = InjectedClock()

    paths = {x: os.path.join(args.out_dir, x) for x in ("REPORT.json", "REPORT.md", "RUNLOG.txt")}
    t0 = real_time.time()
    error = None
    try:
        rc = mod.main(["--engine-dir", args.engine_dir, "--out-json", paths["REPORT.json"],
                       "--out-md", paths["REPORT.md"], "--log", paths["RUNLOG.txt"]])
    except Exception as e:
        rc = None
        error = repr(e)
    wall = round(real_time.time() - t0, 1)

    obs = {"checker_return_code": rc, "checker_exception": error, "real_wall_seconds": wall,
           "injection": dict(state)}
    rep = None
    if os.path.exists(paths["REPORT.json"]):
        with open(paths["REPORT.json"]) as f:
            rep = json.load(f)
    if rep is not None:
        pts = rep.get("per_type", {})
        g = rep.get("global", {})
        inc = rep.get("incomplete", [])
        obs["verdict"] = rep.get("verdict")
        obs["failures_total"] = rep.get("failures_total")
        obs["global_incomplete_entries"] = len(inc)
        obs["global_incomplete_skip_entries"] = sum(1 for x in inc if str(x.get("what", "")).endswith(SKIP_SUFFIX))
        obs["lines_totals"] = g.get("lines_totals")
        obs["per_rule"] = g.get("per_rule")
        obs["pass_gate"] = g.get("pass_gate")
        obs["types_with_coverage_ok"] = sum(1 for pt in pts.values() if pt.get("orbit_coverage", {}).get("ok") is True)
        obs["types_with_hash_match"] = sum(1 for pt in pts.values() if pt.get("hash_match") is True)
        obs["report_checker_sha256"] = rep.get("checker", {}).get("sha256")
        obs["elapsed_seconds_seen_by_checker"] = rep.get("environment", {}).get("elapsed_seconds")
    obs["output_sha256"] = {os.path.basename(p): sha256_file(p) for p in paths.values() if os.path.exists(p)}

    common = {
        "flag_set_after_8th_coverage_call": state["coverage_calls"] == N_TYPES and state["flag"],
        "no_witness_checked": state["check_rule_calls"] == 0,
        "all_8_types_covered_and_hash_matched": (obs.get("types_with_coverage_ok") == N_TYPES
                                                 and obs.get("types_with_hash_match") == N_TYPES),
        "all_lines_skipped_in_tallies": obs.get("lines_totals") == {"lines": N_LINES, "verified": 0,
                                                                    "failed": 0, "incomplete": N_LINES},
        "no_failures": obs.get("failures_total") == 0,
        "report_from_pinned_checker": obs.get("report_checker_sha256") == checker_sha,
    }
    if args.expect == "bug-reproduced":
        specific = {"checker_returned_0": rc == 0, "verdict_PASS": obs.get("verdict") == "PASS",
                    "global_incomplete_list_empty": obs.get("global_incomplete_entries") == 0}
    else:
        specific = {"checker_returned_nonzero": rc not in (0, None),
                    "verdict_INCOMPLETE": obs.get("verdict") == "INCOMPLETE",
                    "all_skips_recorded_globally": obs.get("global_incomplete_skip_entries") == N_LINES}
    conds = dict(common, **specific)
    ok = all(conds.values())
    me = os.path.abspath(__file__)
    result = {"test": me, "test_sha256": sha256_file(me),
              "checker": os.path.abspath(args.checker), "checker_sha256": checker_sha,
              "expect": args.expect, "expectation_met": ok, "conditions": conds,
              "observed": obs, "pinned_inputs": inputs, "python": sys.version,
              "max_rss_bytes_self": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              "finished": real_time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    with open(os.path.join(args.out_dir, "INJECTION-RESULT.json"), "x") as f:
        json.dump(result, f, indent=1, default=str)
        f.write("\n")
    print(json.dumps({"expect": args.expect, "expectation_met": ok, "conditions": conds,
                      "checker_return_code": rc, "verdict": obs.get("verdict"),
                      "lines_totals": obs.get("lines_totals"),
                      "global_incomplete_entries": obs.get("global_incomplete_entries")}, indent=1))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
