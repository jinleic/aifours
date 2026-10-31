#!/usr/bin/env python3
"""Metadata-only launcher for one frozen independent-model CLI review.

Reads the frozen manifest, verifies every pinned byte (inputs, prompt, schema)
against its SHA-256, then runs the Claude Code CLI exactly once with the frozen
argv, stdin closed, and writes raw stdout/stderr plus a receipt. It performs no
scientific computation and never prints credentials.
"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time


def sha256_of(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def native_clock():
    return subprocess.run(
        ["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"], capture_output=True, text=True, check=True
    ).stdout.strip()


def main(manifest_path):
    base = os.path.dirname(os.path.abspath(manifest_path))
    with open(manifest_path, "r", encoding="utf-8") as fh:
        manifest = json.load(fh)

    checks = []
    for item in manifest["inputs"] + [manifest["prompt"], manifest["schema"]]:
        observed = sha256_of(item["path"])
        checks.append({"path": item["path"], "expected": item["sha256"], "observed": observed})
        if observed != item["sha256"]:
            raise SystemExit("SHA-256 mismatch for %s" % item["path"])

    with open(manifest["prompt"]["path"], "r", encoding="utf-8") as fh:
        prompt = fh.read()
    with open(manifest["schema"]["path"], "r", encoding="utf-8") as fh:
        schema_text = fh.read()

    argv = list(manifest["argv_prefix"]) + ["--json-schema", schema_text, "-p", prompt]
    workdir = tempfile.mkdtemp(prefix="aifours-independent-cli-")
    stdout_path = os.path.join(base, manifest["outputs"]["stdout"])
    stderr_path = os.path.join(base, manifest["outputs"]["stderr"])
    receipt_path = os.path.join(base, manifest["outputs"]["receipt"])
    if os.path.exists(receipt_path):
        raise SystemExit("receipt already exists: %s" % receipt_path)

    started = native_clock()
    t0 = time.monotonic()
    with open(stdout_path, "wb") as out, open(stderr_path, "wb") as err:
        proc = subprocess.Popen(
            argv, cwd=workdir, stdin=subprocess.DEVNULL, stdout=out, stderr=err,
        )
        pid = proc.pid
        rc = proc.wait()
    elapsed = round(time.monotonic() - t0, 3)
    finished = native_clock()

    parsed = {"parse_ok": False}
    try:
        with open(stdout_path, "r", encoding="utf-8") as fh:
            events = json.load(fh)
        if isinstance(events, dict):
            events = [events]
        init = next((e for e in events if e.get("type") == "system" and e.get("subtype") == "init"), None)
        result = next((e for e in reversed(events) if e.get("type") == "result"), None)
        parsed = {
            "parse_ok": True,
            "event_count": len(events),
            "init_model": init.get("model") if init else None,
            "result_subtype": result.get("subtype") if result else None,
            "result_is_error": result.get("is_error") if result else None,
            "num_turns": result.get("num_turns") if result else None,
            "duration_ms": result.get("duration_ms") if result else None,
            "model_usage_keys": sorted((result.get("modelUsage") or {}).keys()) if result else None,
            "has_structured_output": bool(result and result.get("structured_output") is not None),
        }
    except Exception as exc:  # noqa: BLE001 - receipt must record any parse failure
        parsed = {"parse_ok": False, "error": repr(exc)}

    receipt = {
        "schema_version": 1,
        "kind": "INDEPENDENT_CLI_LAUNCH_RECEIPT",
        "manifest": {"path": os.path.abspath(manifest_path), "sha256": sha256_of(manifest_path)},
        "preflight_sha256_checks": checks,
        "argv_prefix": manifest["argv_prefix"],
        "argv_tail_summary": {
            "json_schema_sha256": manifest["schema"]["sha256"],
            "prompt_sha256": manifest["prompt"]["sha256"],
            "prompt_bytes": len(prompt.encode("utf-8")),
        },
        "workdir": workdir,
        "pid": pid,
        "started_clock": started,
        "finished_clock": finished,
        "elapsed_seconds": elapsed,
        "exit_code": rc,
        "stdout": {"path": stdout_path, "sha256": sha256_of(stdout_path), "bytes": os.path.getsize(stdout_path)},
        "stderr": {"path": stderr_path, "sha256": sha256_of(stderr_path), "bytes": os.path.getsize(stderr_path)},
        "parsed": parsed,
    }
    with open(receipt_path, "w", encoding="utf-8") as fh:
        json.dump(receipt, fh, indent=2)
        fh.write("\n")
    print(json.dumps({k: receipt[k] for k in ("pid", "started_clock", "finished_clock", "elapsed_seconds", "exit_code", "parsed")}))
    return 0 if rc == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
