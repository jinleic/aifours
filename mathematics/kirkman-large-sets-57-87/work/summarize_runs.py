#!/usr/bin/env python3
"""Rebuild the finite-search ledger from completed, immutable per-run receipts.
Run from target dir: python3 work/summarize_runs.py
"""
from collections import Counter
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
names = ["cyclic9","cyclic15","reflection9","reflection15","multiplier9-a2","multiplier15-a3","multiplier21-a7",
         "reflection57","multiplier57-a12","multiplier57-a32","multiplier57-a34","cyclic57",
         "multiplier87-a4","multiplier87-a33","multiplier87-a69","cyclic87"]
runs = []
for name in names:
    path = root / "evidence" / (name+".json")
    data = json.loads(path.read_text())
    assert data["result"] in ("OPTIMAL","FEASIBLE","INFEASIBLE","UNKNOWN"), (name,data["result"])
    assert data["threads"] <= 16
    if data["result"] in ("OPTIMAL","FEASIBLE"):
        assert data["checker_exit_code"] == 0
        cert = root / "evidence" / (name+".txt")
        assert hashlib.sha256(cert.read_bytes()).hexdigest() == data["certificate_sha256"]
    runs.append({"name":name,"receipt_sha256":hashlib.sha256(path.read_bytes()).hexdigest(), **data})
result = {"run_count":len(runs),"status_counts":dict(Counter(r["result"] for r in runs)),
          "sum_solver_wall_seconds":sum(r["solver_wall_seconds"] for r in runs),
          "scope":"Each row is one explicitly restricted cyclic search. UNKNOWN is not UNSAT. No target certificate found.",
          "stronger_later_proof":"proof.md Sections7–8 exclude all nonidentity multiplier-invariant resolutions at57/87; recorded solver statuses remain unchanged.",
          "runs":runs}
(root/"evidence/search-summary.json").write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!="runs"},indent=2))
