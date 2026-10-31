#!/usr/bin/env python3
"""ReviewF175TuscanOrbit-runner-v1.py

Runs ReviewF175TuscanOrbit-control-v1.py exactly once (standard library only),
with a hard 60-second scientific runtime limit, native /bin/date clocks before
and after, the exit code, and SHA-256 hashes of every input and output. All
outputs are created exclusively (an existing output aborts before any run).
"""
import hashlib
import json
import os
import subprocess
import sys
import time

WAVE = os.path.dirname(os.path.abspath(__file__))
PREFIX = "ReviewF175TuscanOrbit-"
CONTROL = os.path.join(WAVE, PREFIX + "control-v1.py")
RESULTS = os.path.join(WAVE, PREFIX + "control-run-01-results.json")
STDOUT = os.path.join(WAVE, PREFIX + "control-run-01-stdout.txt")
STDERR = os.path.join(WAVE, PREFIX + "control-run-01-stderr.txt")
RECEIPT = os.path.join(WAVE, PREFIX + "control-run-01-receipt.json")
TIMEOUT_S = 60


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        h.update(fh.read())
    return h.hexdigest()


def native_date():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"], capture_output=True,
                          text=True, check=True).stdout.strip()


def write_exclusive(path, data):
    with open(path, "xb") as fh:
        fh.write(data)


def main():
    for p in (RESULTS, STDOUT, STDERR, RECEIPT):
        if os.path.exists(p):
            print("refusing: output exists: " + p, file=sys.stderr)
            return 70
    runner_sha = sha256(os.path.abspath(__file__))
    control_sha_before = sha256(CONTROL)
    cmd = [sys.executable, CONTROL, RESULTS]
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    clock_before = native_date()
    t0 = time.monotonic()
    timed_out = False
    try:
        proc = subprocess.run(cmd, capture_output=True, timeout=TIMEOUT_S,
                              stdin=subprocess.DEVNULL, cwd=WAVE, env=env)
        exit_code = proc.returncode
        out, err = proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as e:
        timed_out = True
        exit_code = None
        out = e.stdout or b""
        err = e.stderr or b""
    wall_s = round(time.monotonic() - t0, 3)
    clock_after = native_date()
    write_exclusive(STDOUT, out)
    write_exclusive(STDERR, err)
    receipt = {
        "kind": "REVIEWER_CONTROL_RUN_RECEIPT",
        "reviewer": "ReviewF175TuscanOrbit",
        "wave": "f175-tuscan-odd-prime-orbit-asymmetry",
        "manifest_sha256": "a8dec6fcd51e1580cfb7cc69eabf0cab9700762c0955eaa698a0f14ecf500ce0",
        "run_label": "run-01 (the single receipted run)",
        "runner": {"path": os.path.abspath(__file__), "sha256": runner_sha},
        "control": {"path": CONTROL, "sha256_before": control_sha_before,
                    "sha256_after": sha256(CONTROL)},
        "python_executable": sys.executable,
        "python_version": sys.version,
        "command": cmd,
        "timeout_s": TIMEOUT_S,
        "native_clock_before": clock_before,
        "native_clock_after": clock_after,
        "monotonic_wall_s": wall_s,
        "timed_out": timed_out,
        "exit_code": exit_code,
        "stdout": {"path": STDOUT, "bytes": len(out), "sha256": hashlib.sha256(out).hexdigest()},
        "stderr": {"path": STDERR, "bytes": len(err), "sha256": hashlib.sha256(err).hexdigest()},
        "results": ({"path": RESULTS, "bytes": os.path.getsize(RESULTS), "sha256": sha256(RESULTS)}
                    if os.path.exists(RESULTS) else {"path": RESULTS, "missing": True}),
        "notes": ("Standard library only; no author code, held material, order-11, T2(11), SAT or "
                  "DRAT step. Earlier unreceipted/reset-kernel prototypes are not evidence. A "
                  "pre-run ast.parse syntax check executed no control logic."),
    }
    data = (json.dumps(receipt, indent=1, sort_keys=True) + "\n").encode("utf-8")
    write_exclusive(RECEIPT, data)
    print(data.decode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
