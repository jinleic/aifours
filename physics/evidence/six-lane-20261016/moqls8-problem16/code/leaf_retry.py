"""Retry-once runner and ledger ingest (review/AMENDMENT_RETRY_ONCE.md). Never deletes; proofs streamed, not stored.
run:    for each requested leaf that is a terminal UNKNOWN leaf on its FIRST attempt (no "prior_attempts"; its evidence is a
        strict 900 s receipt or an old worker-root timeout record), re-run the SAME leaf CNF (base + path units) once with
        certify() of code/k5_resplit_r2.py: CaDiCaL -q -t 1800 (default seed), binary DRAT streamed into drat-trim
        -i -t 3600, strict conjunction, 6 GiB aggregate RSS guard; disk floor 12e9 and lane ≤ 9.5 GiB before each leaf.
        Receipts carry attempt = 2 and the full identity; resume only on exact identity.
ingest: new ledger version: a leaf with an attempt-2 receipt becomes CERTIFIED (strict_ok) or stays UNKNOWN; its new
        evidence is the attempt-2 receipt, the attempt-1 evidence is kept in "prior_attempts", and "attempt": 2 is set.
        Refinement (k5_cover refine) is applied only to leaves whose attempt-2 receipt is UNKNOWN (procedural rule).
--problem k5: code/k5_cover.py; --problem k4: code/k4_cover.py constants + the pinned orbit validator code/k4_orbit_r3.py.
python -B leaf_retry.py run --problem k5 --ledger L --base B --outdir ../evidence/k5_split_v1/retry_A --ids a,b
python -B leaf_retry.py ingest --problem k5 --ledger L --base B --results retry_A/RESULTS.jsonl
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, ".."))
TLIM, CHECK_LIMIT, RSS_CAP = 1800, 3600, 6 * 2 ** 30


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def cover(problem):
    if problem == "k5":
        return load("k5_cover")
    K = load("k4_cover")
    C = K.configure(K.load_cover())
    load("k4_orbit_r3").install(C)
    return C


def eligible(x):
    ev = x.get("evidence") or {}
    return (x["state"] == "UNKNOWN" and "prior_attempts" not in x and x.get("attempt", 1) == 1
            and ev.get("kind") in ("strict", "worker-root"))


def lane_bytes():
    return int(subprocess.run(["du", "-sk", LANE], capture_output=True, text=True).stdout.split()[0]) * 1024


def cmd_run(a, C):
    R = load("k5_resplit_r2")
    L, lsha = C.load_ledger(a.ledger)
    base = C.Base(a.base)
    v = C.validate(L, base, C.Receipts())
    if v["problems"]:
        raise SystemExit("ledger invalid: %s" % json.dumps(v["problems"][:10]))
    byid = {x["id"]: x for x in L["leaves"]}
    ids = a.ids.split(",")
    for i in ids:
        if i not in byid or not eligible(byid[i]) or any(y["ancestor"] == i for y in L["leaves"]):
            raise SystemExit("not an eligible first-attempt terminal UNKNOWN leaf: %s" % i)
    os.makedirs(a.outdir, exist_ok=True)
    res_path = os.path.join(a.outdir, "RESULTS.jsonl")
    done = set()
    if os.path.exists(res_path):
        for line in open(res_path, "rb").read().split(b"\n"):
            if line.strip():
                r = json.loads(line)
                x = byid.get(r.get("id"))
                if x is None or r.get("attempt") != 2 or not C.identity_ok("strict", r, x, base) or r["id"] in done:
                    raise SystemExit("existing retry receipt does not match: %s" % r.get("id"))
                done.add(r["id"])
    cad = os.path.realpath(shutil.which("cadical"))
    meta = {"argv": sys.argv, "script_sha256": sha(__file__), "k5_resplit_r2_sha256": sha(os.path.join(HERE,
            "k5_resplit_r2.py")), "ledger": a.ledger, "ledger_sha256": lsha, "base_cnf_sha256": base.sha,
            "problem": a.problem, "ids": ids, "solver_limit": TLIM, "checker_limit": CHECK_LIMIT, "rss_cap": RSS_CAP,
            "cadical_binary": cad, "cadical_sha256": sha(cad), "drat_trim_sha256": sha(R.DT), "start": time.ctime()}
    with open(os.path.join(a.outdir, "META.%d.json" % int(time.time())), "x") as fh:
        json.dump(meta, fh, indent=1)
    fifos = tuple(os.path.join(a.outdir, "w0.%s.fifo" % s) for s in ("cnf_s", "cnf_c", "proof"))
    for p in fifos:
        if not os.path.exists(p):
            os.mkfifo(p)
    for i in ids:
        if i in done:
            continue
        fb, lb = shutil.disk_usage(a.outdir).free, lane_bytes()
        if fb < 12_000_000_000 or lb > int(9.5 * 2 ** 30):
            with open(os.path.join(a.outdir, "STOP.%d.json" % int(time.time())), "x") as fh:
                json.dump({"before_leaf": i, "free": fb, "lane_bytes": lb}, fh)
            break
        x = byid[i]
        n = 1
        while os.path.exists(os.path.join(a.outdir, "%s.r%d.solver.log" % (i, n))):
            n += 1
        tag = "%s.r%d" % (i, n)
        rec = {"id": i, "depth": x["depth"], "index": x["index"], "ancestor": x["ancestor"], "lits": x["lits"],
               "base_cnf_sha256": base.sha, "ledger_sha256": lsha, "attempt": 2, "attempt_tag": tag,
               "prior_evidence": x["evidence"]}
        rec.update(R.certify(tag, x["lits"], base.nv, base.nc, base.body, a.outdir, fifos, TLIM, RSS_CAP,
                             checker_limit=CHECK_LIMIT))
        if rec["cnf_sha256"] != base.leaf_sha(x["lits"]):
            raise SystemExit("internal CNF hash mismatch")
        rec["strict_ok"] = C.strict_ok(rec)
        with open(res_path, "a") as fh:
            fh.write(json.dumps(rec) + "\n")
        print(json.dumps({"id": i, "strict_ok": rec["strict_ok"], "secs": rec["secs"],
                          "solver_rc": rec["solver_returncode"], "checker_rc": rec["checker_returncode"],
                          "rss_gib": round(rec["aggregate_peak_rss_bytes"] / 2 ** 30, 2)}), flush=True)


def cmd_ingest(a, C):
    L, lsha = C.load_ledger(a.ledger)
    base = C.Base(a.base)
    v = C.validate(L, base, C.Receipts())
    if v["problems"]:
        raise SystemExit("ledger invalid")
    byid = {x["id"]: x for x in L["leaves"]}
    seen, changed = set(), 0
    for line in open(os.path.join(C.SPLIT_DIR, a.results), "rb").read().split(b"\n"):
        if not line.strip():
            continue
        r = json.loads(line)
        x = byid.get(r.get("id"))
        if x is None or r.get("attempt") != 2 or not C.identity_ok("strict", r, x, base) or r["id"] in seen:
            raise SystemExit("retry receipt does not match the ledger: %s" % r.get("id"))
        seen.add(r["id"])
        if not eligible(x) or r.get("prior_evidence") != x["evidence"]:
            raise SystemExit("leaf is not on its first attempt or prior evidence differs: %s" % r["id"])
        x["prior_attempts"] = [x["evidence"]]
        x["attempt"] = 2
        x["evidence"] = {"kind": "strict", "file": a.results, "line_sha256": hashlib.sha256(line).hexdigest()}
        x["state"] = "CERTIFIED" if C.strict_ok(r) else "UNKNOWN"
        changed += 1
    v2 = C.validate(L, base, C.Receipts())
    if v2["problems"]:
        raise SystemExit("ingest would produce an invalid ledger: %s" % json.dumps(v2["problems"][:10]))
    print(json.dumps({"changed": changed, "counts": v2["counts"]}))
    print(json.dumps(C.write_next(L, lsha, "retry ingest %s" % a.results)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["run", "ingest"])
    ap.add_argument("--problem", choices=["k5", "k4"], required=True)
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--base", required=True)
    ap.add_argument("--outdir")
    ap.add_argument("--ids")
    ap.add_argument("--results")
    a = ap.parse_args()
    C = cover(a.problem)
    cmd_run(a, C) if a.mode == "run" else cmd_ingest(a, C)


if __name__ == "__main__":
    main()
