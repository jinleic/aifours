#!/usr/bin/env python3
"""Fixed, cooperative stage1 proposal. Requires exact parent GO before running.

Runs only pinned author checker controls and encodes orders3/4/11. No solver,
no subprocess, no retries. It does not attest to unrestricted target existence.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import runpy
import signal
import sys
import time

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "unrestricted-tuscan-sat-v1.py"
EXPECTED_BASE = "ae060379381e7700d298fd22b7d35e8e41f0e6d6b812bb011a6602bd2c2e5904"
EXPECTED_COUNTS = {3: (123, 366), 4: (520, 1604), 11: (47091, 151250)}


class CooperativeStop(Exception):
    pass


def stop_requested(signum: int, frame: object) -> None:
    raise CooperativeStop(f"signal_{signum}")


def main() -> int:
    if len(sys.argv) != 2:
        print("ERROR: expected one exclusive output directory", file=sys.stderr)
        return 64
    output = Path(sys.argv[1]).resolve()
    if not output.is_relative_to(ROOT):
        print("ERROR: outside owned root", file=sys.stderr)
        return 64
    if hashlib.sha256(BASE.read_bytes()).hexdigest() != EXPECTED_BASE:
        print("HOLD: base source hash mismatch", file=sys.stderr)
        return 2
    output.mkdir()  # Refuse any existing destination; never delete or overwrite.
    signal.signal(signal.SIGINT, stop_requested)
    signal.signal(signal.SIGTERM, stop_requested)
    signal.signal(signal.SIGALRM, stop_requested)
    start = time.monotonic()
    status, detail, exit_code = "COMPLETE", "", 0
    manifests = []
    signal.setitimer(signal.ITIMER_REAL, 60.0)
    try:
        namespace = runpy.run_path(str(BASE), run_name="frozen_tuscan_stage1")
        namespace["controls"]()
        for n, counts in EXPECTED_COUNTS.items():
            destination = output / f"n{n}"
            namespace["encode"](n, destination)
            manifest = json.loads((destination / "manifest.json").read_text())
            if (manifest["variables"], manifest["clauses"]) != counts:
                raise ValueError(f"COUNT_MISMATCH_n{n}")
            if manifest["source_sha256"] != EXPECTED_BASE:
                raise ValueError(f"SOURCE_MISMATCH_n{n}")
            manifests.append(manifest)
    except CooperativeStop as exc:
        status, detail, exit_code = "UNKNOWN", str(exc), 75
    except Exception as exc:
        status, detail, exit_code = "ERROR", f"{type(exc).__name__}: {exc}", 2
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0.0)
    receipt = {
        "stage": "encoding_and_author_controls_only",
        "status": status,
        "detail": detail,
        "elapsed_seconds": time.monotonic() - start,
        "base_source_sha256": EXPECTED_BASE,
        "wrapper_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "manifests": manifests,
        "solver_executed": False,
        "full_target_result": "NONE",
        "independent_verification": False,
    }
    with (output / "stage1-status.json").open("x", encoding="utf-8") as stream:
        json.dump(receipt, stream, indent=2)
        stream.write("\n")
    print(json.dumps(receipt, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
