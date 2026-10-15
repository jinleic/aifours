#!/usr/bin/env python3
"""Aggregate only finalized extended target-run receipts without rerunning searches.
Run after all owned searches finish: python3 work/summarize_extended.py
"""
from collections import Counter
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
prefixes = [
    "extended-57-kissat-101", "extended-57-cadical-102", "extended-87-kissat-103",
    "extended-87-cadical-104", "extended-57-cpsat-105", "extended-87-cpsat-106",
    "extended-modular57-57007", "c19-17-staged", "c19-17-staged-u5",
    "group-reflection57", "group-frobenius57-extended",
    "extended-modular87-87007", "c19-paircover-kissat", "c19-paircover-cadical",
    "c19-paircover-cpsat",
]
runs = []
for prefix in prefixes:
    path = root/"evidence"/(prefix+".json")
    raw = path.read_bytes()
    receipt = json.loads(raw)
    state = receipt["status"] if "status" in receipt else receipt.get("result")
    if state is None or "RUNNING" in state:
        raise RuntimeError(f"{prefix}: receipt is not finalized")
    if "CHECKER_FAIL" in state or state == "ERROR":
        raise RuntimeError(f"{prefix}: unresolved run failure")
    wall = next((receipt[key] for key in ("wall_seconds","total_seconds","runtime_seconds") if key in receipt),None)
    if wall is None:
        raise RuntimeError(f"{prefix}: no observed overall wall time")
    ledger = root/"evidence"/(prefix+".jsonl")
    if ledger.is_file():
        events = [json.loads(line) for line in ledger.read_text().splitlines() if line.strip()]
    else:
        events = receipt.get("phases",receipt.get("solver_calls",[]))
    counts = Counter(f'{e.get("phase","solver")}:{e.get("status",e.get("result","RECORDED"))}' for e in events)
    runs.append({"prefix":prefix,"status":state,"wall_seconds":wall,"event_count":len(events),
                 "phase_status_counts":dict(counts),"receipt_sha256":hashlib.sha256(raw).hexdigest(),
                 "ledger_sha256":hashlib.sha256(ledger.read_bytes()).hexdigest() if ledger.is_file() else None,
                 "receipt":receipt})
proof = root/"evidence/c19-36-obstruction.json"
result = {"target_runs":len(runs),"statuses":dict(Counter(r["status"] for r in runs)),
          "sum_observed_run_wall_seconds":sum(r["wall_seconds"] for r in runs),
          "time_interpretation":"Runs overlap. This sum is not elapsed session time or CPU time.",
          "scope":"Bounded configurations only; UNKNOWN is not UNSAT; frozen matching/packing assumptions remain in per-run receipts and notes.",
          "early_structural_obstruction":{"receipt":"evidence/c19-36-obstruction.json",
                                          "sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),
                                          "status":json.loads(proof.read_bytes())["status"]},
          "runs":runs}
(root/"evidence/extended-summary.json").write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!="runs"},indent=2))
