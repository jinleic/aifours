#!/usr/bin/env python3
"""Summarise all 147 K2 certificate receipts of one encoder without rerunning solvers.

Checks expected indices, frozen pins, both log hashes and exact status bindings.
The summary is an evidence inventory, not an independent mathematical proof.
Usage: gram_cert_summary.py A|B CERTDIR OUTPUT.json
"""
import argparse
import datetime
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for part in iter(lambda: f.read(1 << 20), b""):
            h.update(part)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("encoder", choices=("A", "B"))
    ap.add_argument("certdir")
    ap.add_argument("out")
    a = ap.parse_args()
    if os.path.exists(a.out):
        raise FileExistsError(a.out)
    rows, pinned = [], None
    for i in range(147):
        label = "k2%s_%d" % (a.encoder, i)
        receipt = os.path.join(a.certdir, label + ".json")
        with open(receipt) as f:
            r = json.load(f)
        assert r["instance"] == "k2%s:%d" % (a.encoder, i), receipt
        assert r["verified_unsat"] is True and r["solver_rc"] == 20 and r["checker_rc"] == 0, receipt
        assert r["safety_stop_reason"] is None, receipt
        assert r["checker_status_lines"] == ["s VERIFIED"], receipt
        if pinned is None:
            pinned = r["pins"]
        assert r["pins"] == pinned, receipt
        for name in ("solver", "checker"):
            log = os.path.join(a.certdir, label + "." + name + ".log")
            assert sha(log) == r[name + "_log_sha256"], log
        with open(os.path.join(a.certdir, label + ".checker.log")) as f:
            statuses = [s.strip() for s in f.read().replace("\r", "\n").splitlines() if s.strip().startswith("s ")]
        assert statuses == ["s VERIFIED"], receipt
        rows.append({"class": i, "receipt": os.path.basename(receipt), "receipt_sha256": sha(receipt),
                     "cnf_sha256": r["cnf_sha256"], "checker_log_sha256": r["checker_log_sha256"],
                     "seconds": r["seconds"], "peak_sampled_aggregate_rss_bytes": r["peak_sampled_aggregate_rss_bytes"],
                     "started_at": r["started_at"], "finished_at": r["finished_at"]})
    for path, h in pinned.items():
        if path.endswith(".py"):
            assert sha(os.path.join(HERE, path)) == h, path
    assert sha(os.path.join(LANE, "evidence", "ls7_main_classes.txt")) == pinned["classfile"]
    summary = {"recorded_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
               "encoder": a.encoder, "status": "147/147 verified UNSAT receipts; bridge still requires independent review",
               "expected_class_indices": [0, 146], "certificates": 147, "pins": pinned,
               "summary_code_sha256": sha(__file__),
               "total_native_pipeline_seconds": round(sum(r["seconds"] for r in rows), 3),
               "max_sampled_aggregate_rss_bytes": max(r["peak_sampled_aggregate_rss_bytes"] for r in rows),
               "rows": rows, "proof_storage": "FIFO-only, reproducible from pinned generators"}
    with open(a.out, "x") as f:
        json.dump(summary, f, indent=2)
        f.write("\n")
    print(json.dumps({k: summary[k] for k in ("encoder", "certificates", "total_native_pipeline_seconds", "max_sampled_aggregate_rss_bytes")}))
    print("summary_sha256", sha(a.out))


if __name__ == "__main__":
    main()
