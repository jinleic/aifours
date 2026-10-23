#!/usr/bin/env python3
"""Small worker-only consistency post-check (metadata only, read-only, under one read-only lane token):
for every chosen split case whose placement list has NO parent replay, compare the stored ext.json (sha256 from
run-v1, raw/num_full) with the worker's own generation receipt (extend-receipt-*.json: helper rc, self-reported
'raw'/'num_full' output line, RSS cap), when such a receipt exists. A match is worker self-consistency only, NOT a
parent binding. Writes postcheck-v1.json (mode 'x')."""
import hashlib
import json
import os
import re
import sys
import time

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from token_ro import ReadOnlyToken  # noqa: E402

LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"


def main():
    rows = [json.loads(l) for l in open(os.path.join(HERE, "run-v1", "cases-A2.jsonl"))]
    worker_only = [(r["tag"], r["chosen"]) for r in rows
                   if r["chosen"]["route"] in ("d", "e") and "worker-only" in r["chosen"]["ext"]["binding"]]
    out = {"started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "cases": []}
    with ReadOnlyToken() as tok:
        out["token"] = {"name": tok.name, "acquired_at": tok.acquired_at, "waited_s": tok.waited_s}
        for tag, c in worker_only:
            d = os.path.join(LANE, c["dir"])
            now_sha = hashlib.sha256(open(os.path.join(d, "ext.json"), "rb").read()).hexdigest()
            recs = sorted(n for n in os.listdir(d) if re.fullmatch(r"extend-receipt-\d{8}T\d{6}\.json", n))
            item = {"tag": tag, "ext_sha256_run_v1": c["ext"]["sha256"], "ext_sha256_now": now_sha,
                    "unchanged_since_run_v1": now_sha == c["ext"]["sha256"], "num_full": c["ext"]["num_full"],
                    "raw": c["ext"]["raw"], "receipts": []}
            for n in recs:
                b = open(os.path.join(d, n), "rb").read()
                r = json.loads(b)
                tail = {}
                try:
                    tail = json.loads((r.get("out_tail") or "").strip().splitlines()[-1])
                except (ValueError, IndexError):
                    pass
                item["receipts"].append({
                    "file": n, "sha256": hashlib.sha256(b).hexdigest(), "rc": r.get("rc"), "cap_hit": r.get("cap_hit"),
                    "peak_rss_kb": r.get("peak_rss_kb"), "tool": r.get("tool"),
                    "cmd_uses_extend_p1q_and_case_spec": ("src/extend_p1q.py" in (r.get("cmd") or "")
                                                          and ("cases19skel/specs/%s.json" % tag) in (r.get("cmd") or "")),
                    "out_raw": tail.get("raw"), "out_num_full": tail.get("num_full"), "out_source": tail.get("source"),
                    "matches_stored_list": (r.get("rc") == 0 and r.get("cap_hit") is False and tail.get("raw") == c["ext"]["raw"]
                                            and tail.get("num_full") == c["ext"]["num_full"]
                                            and tail.get("source") == tag + ".json")})
            item["worker_receipt_consistent"] = any(x["matches_stored_list"] for x in item["receipts"])
            out["cases"].append(item)
    out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    out["summary"] = {"worker_only_lists": len(out["cases"]),
                      "with_consistent_worker_receipt": sum(1 for x in out["cases"] if x["worker_receipt_consistent"]),
                      "without_generation_receipt": [x["tag"] for x in out["cases"] if not x["receipts"]],
                      "inconsistent": [x["tag"] for x in out["cases"] if x["receipts"] and not x["worker_receipt_consistent"]],
                      "changed_since_run_v1": [x["tag"] for x in out["cases"] if not x["unchanged_since_run_v1"]]}
    with open(os.path.join(HERE, "postcheck-v1.json"), "x") as f:
        json.dump(out, f, indent=1)
        f.write("\n")
    print(json.dumps(out["summary"]))


if __name__ == "__main__":
    main()
