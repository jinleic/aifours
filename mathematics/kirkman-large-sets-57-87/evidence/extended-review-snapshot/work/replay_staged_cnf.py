#!/usr/bin/env python3
"""Rebuild an exact staged CNF from saved matching data and blocked candidates.

Example:
  uv run --with ortools==9.15.6755 python work/replay_staged_cnf.py \
    evidence/extended-validate9-kissat-data/matching-00000.json \
    --output /tmp/lkts-replayed.cnf --expect-sha <sts-event-instance-sha256>
For candidate indexk, repeat --block for the preceding k candidate JSON files
in order. Their primary-variable ids refer to the saved matching's row-order seed.
"""
import argparse
import json
from pathlib import Path
from search_staged import CNF, digest, finite_cover, validate_matchings

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("matching",type=Path)
ap.add_argument("--block",type=Path,action="append",default=[])
ap.add_argument("--output",type=Path,required=True)
ap.add_argument("--expect-sha")
args = ap.parse_args()
data = json.loads(args.matching.read_text())
matchings = [[tuple(pair) for pair in matching] for matching in data["matchings"]]
validate_matchings(data["n"],matchings)
rows,columns = finite_cover(data["n"],matchings,data["seed"])
args.output.parent.mkdir(parents=True,exist_ok=True)
cnf = CNF(args.output,len(rows),columns)
for path in args.block:
    candidate = json.loads(path.read_text())
    assert candidate["v"] == data["n"]+2
    cnf.block(candidate["selected_primary_literals"])
sha = digest(args.output)
if args.expect_sha:
    assert sha == args.expect_sha, (sha,args.expect_sha)
print(json.dumps({"instance_sha256":sha,"primary_rows":len(rows),"variables":cnf.variables,
                  "clauses":cnf.clauses,"blocked_candidates":len(args.block),"expected_hash_matches":args.expect_sha is not None},indent=2))
