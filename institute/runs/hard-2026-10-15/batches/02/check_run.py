#!/usr/bin/env python3
"""Read-only parent check of a bounded parallel institute run."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile

import run_parallel


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))




def replay(engine, snapshot: Path, claims: list[dict], timeout: int) -> list[dict]:
    with tempfile.TemporaryDirectory(prefix="aifours-check-") as temporary:
        copy = (Path(temporary) / "snapshot").resolve()
        shutil.copytree(snapshot, copy, symlinks=True)
        results = []
        for number, claim in enumerate(claims):
            result = {"cid": claim["cid"]}
            for kind in ("verify", "check", "control"):
                command = (claim.get(f"{kind}_command") or "").strip()
                if not command:
                    result[f"{kind}_rc"] = None
                    continue
                base = Path(temporary) / f"replay-{number}-{kind}"
                run = engine.sandboxed(command, copy, base, timeout)
                result[f"{kind}_rc"] = "timeout" if run["timed_out"] else run["rc"]
                result[f"{kind}_stdout_tail"] = engine.tail(base.with_suffix(".out"), 2000)
                result[f"{kind}_stderr_tail"] = engine.tail(base.with_suffix(".err"), 2000)
            result["replay_matches_claim_contract"] = (
                (result["verify_rc"] in (None, 0)) and (result["check_rc"] in (None, 0))
                and (result["control_rc"] is None or result["control_rc"] not in (0, "timeout"))
            )
            results.append(result)
        return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run", type=Path)
    parser.add_argument("--replay-timeout", type=int, default=600)
    args = parser.parse_args()
    root = args.run.resolve()
    selection = read_json(root / "selection.json")
    run = read_json(root / "run.json")
    if run.get("status") == "running":
        parser.error("the research run is still active; do not replay live snapshots")
    engine = run_parallel.load_engine(selection)
    run_parallel.check_inputs(root, selection)
    allowed_seconds = selection["hours_per_problem_ceiling"] * 3600
    report = {"run_status": run.get("status"), "selection_sha256": hashlib.sha256(
        (root / "selection.json").read_bytes()).hexdigest(), "problems": []}
    stage_counts = Counter()
    failures = []
    if run.get("status") != "done":
        failures.append("not all requested visits completed; inspect per-lane outcomes")
    for pick in selection["problems"]:
        record = read_json(root / "problems" / pick["id"] / "record.json")
        lifetime_attempts = [entry for entry in record["log"] if entry.get("t") == "attempt"]
        epoch = engine.epoch_start(record)[0]
        attempts = [entry for entry in lifetime_attempts if entry.get("epoch", 0) == epoch]
        outcomes = [entry for entry in record["log"] if entry.get("t") == "outcome"
                    and entry.get("epoch", 0) == epoch]
        stage_counts.update(entry["stage"] for entry in attempts)
        spent = round(sum(entry.get("seconds") or 0 for entry in attempts), 1)
        item = {"id": pick["id"], "epoch": epoch, "outcome": outcomes[-1] if outcomes else None,
                "attempts": [{key: entry.get(key) for key in ("stage", "status", "quota", "seconds")}
                             for entry in attempts], "attempt_seconds": spent,
                "lifetime_attempt_seconds": round(sum(entry.get("seconds") or 0 for entry in lifetime_attempts), 1)}
        if spent > allowed_seconds + 60:
            failures.append(f"{pick['id']} exceeded its six-hour allocation")
        attack_dirs = [root / "problems" / pick["id"] / f"attack-e{epoch}"]
        attack_dirs = [path for path in attack_dirs if path.is_dir()]
        if attack_dirs:
            claims_path = attack_dirs[-1] / "claims.json"
            if claims_path.is_file():
                claims = read_json(claims_path)
                item["attack_snapshot"] = str(attack_dirs[-1])
                item["attack_sha256"] = engine.sha256_tree(attack_dirs[-1])
                item["claims_outcome"] = claims.get("outcome")
                item["parent_replay"] = replay(engine, attack_dirs[-1], claims.get("claims", []),
                                              args.replay_timeout)
                bad = [x["cid"] for x in item["parent_replay"] if not x["replay_matches_claim_contract"]]
                if bad:
                    failures.append(f"{pick['id']} replay contract failed: {bad}")
        report["problems"].append(item)
    report["stage_attempt_counts"] = dict(stage_counts)
    report["failures"] = failures
    report["limits"] = [
        "A replay demonstrates repeatability only. Mathematical correctness requires independent proof review.",
        "Search verdicts are dated. Model referee acceptance is not human peer review.",
    ]
    output = root / "parent-check.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"status": "FAIL" if failures else "PASS", "failures": failures,
                      "output": str(output)}, indent=1))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
