#!/usr/bin/env python3
"""run_controls.py - replay the route-C control set against checker_c.py.

Usage:  python3 -I -B run_controls.py NEW_RUN_DIR [--checker FILE] [--expected FILE]
NEW_RUN_DIR is relative to this directory and must not exist; it is created and
receives results.json (mode "x") plus any --output receipts the cases request.
Every case of controls/expected.json runs as its own
`python3 -I -B checker_c.py ...` process (no timeout).  Its exit status, its single
JSON stdout line, an empty stderr and the expected verdict fields are compared with
the hand-derived expectations.  Exit 0 iff every case matches.
"""

import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
USAGE = "usage: run_controls.py NEW_RUN_DIR [--checker FILE] [--expected FILE]"


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    with open(path, "rb") as handle:
        return sha256_bytes(handle.read())


def extract(out):
    """The fields of a checker verdict object that the expectations refer to."""
    got = {"verdict": out.get("verdict")}
    checks = out.get("checks")
    if isinstance(checks, dict):
        oa = checks["oa_strength2"]
        cfr = checks["cfr"]
        dm = checks["dm_definition"]
        got["checks"] = dict((name, checks[name]["verdict"]) for name in checks)
        got["dm_failing_row_pairs"] = sorted(entry["rows"] for entry in dm["failing_row_pairs"])
        got["dm_distinct_values"] = sorted(set(entry["distinct_differences"] for entry in dm["failing_row_pairs"]))
        got["oa_failing_coordinate_pairs"] = sorted(entry["coordinates"] for entry in oa["failing_coordinate_pairs"])
        got["oa_missing_pairs_values"] = sorted(set(entry["missing_pairs"] for entry in oa["failing_coordinate_pairs"]))
        got["cfr_rows_not_permutation"] = sorted(entry["row"] for entry in cfr["rows_not_permutation"])
        got["cfr_conflicting_row_pairs"] = sorted(cfr["conflicting_row_pairs"])
        got["cfr_conflicting_triples"] = cfr["conflicting_triples"]
        got["bridge_consistent"] = out.get("bridge_consistent")
        got["blank_lines_ignored"] = out.get("blank_lines_ignored")
    malformed = out.get("malformed")
    if isinstance(malformed, dict):
        got["malformed_kind"] = malformed.get("kind")
        got["malformed_line"] = malformed.get("line")
    return got


def run_case(case, run_dir, checker, checker_sha, stdout_by_id):
    argv = [arg.replace("@RUN@", run_dir) for arg in case["argv"]]
    problems = []
    if case.get("sha256"):
        actual = sha256_file(os.path.join(HERE, case["file"]))
        if actual != case["sha256"]:
            problems.append("control file changed: sha256 %s" % actual)
    if case.get("absent") and os.path.lexists(os.path.join(HERE, case["file"])):
        problems.append("a file that must be absent exists")
    proc = subprocess.run([sys.executable, "-I", "-B", checker] + argv,
                          cwd=HERE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_by_id[case["id"]] = proc.stdout
    stdout = proc.stdout.decode("ascii", "replace")
    stderr = proc.stderr.decode("ascii", "replace")
    lines = stdout.splitlines()
    out = None
    if len(lines) != 1 or not stdout.endswith("\n"):
        problems.append("stdout is not exactly one line")
    if lines:
        try:
            out = json.loads(lines[0])
        except ValueError:
            problems.append("stdout line is not JSON")
    if stderr:
        problems.append("stderr is not empty")
    expect = case["expect"]
    if proc.returncode != expect["exit"]:
        problems.append("exit status %d, expected %d" % (proc.returncode, expect["exit"]))
    verdict = None
    if isinstance(out, dict):
        verdict = out.get("verdict")
        if out.get("exit_code") != proc.returncode:
            problems.append("JSON exit_code %r differs from the exit status" % out.get("exit_code"))
        if out.get("checker_sha256") != checker_sha:
            problems.append("checker_sha256 field differs from the checker file")
        if case.get("sha256") and verdict != "USAGE_ERROR" and out.get("file_sha256") != case["sha256"]:
            problems.append("file_sha256 field differs from the control file")
        got = extract(out)
        for key in sorted(expect):
            if key == "exit":
                continue
            want = expect[key]
            have = got.get(key, "<absent>")
            if isinstance(want, list):
                want = sorted(want)
            if have != want:
                problems.append("%s: expected %s, got %s" % (key, json.dumps(want), json.dumps(have)))
    elif out is not None:
        problems.append("stdout JSON is not an object")
    if case.get("receipt"):
        path = os.path.join(HERE, case["receipt"].replace("@RUN@", run_dir))
        try:
            with open(path, "rb") as handle:
                content = handle.read()
        except OSError as exc:
            problems.append("receipt unreadable: %s" % exc)
        else:
            if content != stdout_by_id.get(case["receipt_matches"]):
                problems.append("receipt differs from the stdout of %s" % case["receipt_matches"])
    return {
        "id": case["id"],
        "class": case["class"],
        "task_ref": case["task_ref"],
        "intended": case["intended"],
        "argv": argv,
        "exit_code": proc.returncode,
        "verdict": verdict,
        "stdout": stdout,
        "stderr": stderr,
        "problems": problems,
        "ok": not problems,
    }


def main(argv):
    run_dir = None
    checker = "checker_c.py"
    expected = os.path.join("controls", "expected.json")
    index = 0
    while index < len(argv):
        if argv[index] in ("--checker", "--expected") and index + 1 < len(argv):
            if argv[index] == "--checker":
                checker = argv[index + 1]
            else:
                expected = argv[index + 1]
            index += 2
        elif run_dir is None and not argv[index].startswith("-"):
            run_dir = argv[index]
            index += 1
        else:
            sys.stdout.write(USAGE + "\n")
            return 2
    if run_dir is None:
        sys.stdout.write(USAGE + "\n")
        return 2
    os.mkdir(os.path.join(HERE, run_dir))  # never reuse a run directory
    started = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    with open(os.path.join(HERE, expected), "rb") as handle:
        spec_bytes = handle.read()
    spec = json.loads(spec_bytes)
    checker_sha = sha256_file(os.path.join(HERE, checker))
    records = []
    stdout_by_id = {}
    for case in spec["cases"]:
        record = run_case(case, run_dir, checker, checker_sha, stdout_by_id)
        records.append(record)
        status = "ok" if record["ok"] else "MISMATCH " + "; ".join(record["problems"])
        sys.stdout.write("%-4s %-9s exit=%d verdict=%s %s\n"
                         % (record["id"], record["class"], record["exit_code"], record["verdict"], status))
    all_ok = all(record["ok"] for record in records)
    doc = {
        "runner": "run_controls.py",
        "runner_sha256": sha256_file(os.path.abspath(__file__)),
        "checker": checker,
        "checker_sha256": checker_sha,
        "expected": expected,
        "expected_sha256": sha256_bytes(spec_bytes),
        "python_executable": sys.executable,
        "python_version": sys.version,
        "started": started,
        "finished": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "cases": records,
        "all_ok": all_ok,
    }
    with open(os.path.join(HERE, run_dir, "results.json"), "x", encoding="ascii") as handle:
        handle.write(json.dumps(doc, indent=1, sort_keys=True) + "\n")
    matched = sum(1 for record in records if record["ok"])
    sys.stdout.write("%s %d/%d cases match; results in %s/results.json\n"
                     % ("ALL_OK" if all_ok else "MISMATCH", matched, len(records), run_dir))
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
