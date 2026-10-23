"""Ledger-driven strict leaf runner (README §8.2). Uses certify() of code/k5_resplit.py UNCHANGED (streamed, non-retained
DRAT: CNF FIFO → CaDiCaL → proof FIFO → engine SHA-256 → drat-trim stdin; strict conjunction; 6 GiB aggregate RSS guard).
1. Loads and fully validates the ledger (k5_cover.validate); aborts on any problem.
2. Resume: every existing receipt in OUTDIR/RESULTS.jsonl must match a ledger leaf on full identity (id, depth, index,
   ancestor, complete literals, base SHA, leaf-CNF SHA recomputed from the base); duplicates or mismatches abort.
   Only identity-matching receipts mark a leaf as done.
3. Runs the selected UNSTARTED leaves in ledger order (selection: all | depth=D | ids=a,b,...), guards before each
   leaf (free ≥ 12e9 bytes, lane ≤ 9.5 GiB); one pipeline at a time.
4. --bind-root-proofs: for a depth-1 leaf, also decompress the retained §8 proof (pilot/ or all/ cubeNNN.drat.zst;
   file SHA-256 must equal the old receipt's proof_sha256) and record whether its SHA-256 equals the streamed proof's
   (retained proof = exactly the strict run's proof). Binding never changes the verdict.
python -B k5_leafrun.py --ledger L.json --base BASE.cnf --outdir ../evidence/k5_split_v1/strict_L1 --select depth=1 \\
       --bind-root-proofs
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


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


C = load("k5_cover")
R = load("k5_resplit")


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 24), b""):
            h.update(chunk)
    return h.hexdigest()


def bind_root(b, stream_sha):
    old = None
    for sub in ("pilot", "all"):
        res = os.path.join(C.SPLIT_DIR, sub, "RESULTS.jsonl")
        if os.path.exists(res):
            for line in open(res):
                r = json.loads(line)
                if r["cube"] == b:
                    old = (sub, r)
    if old is None:
        return {"retained": False}
    sub, r = old
    pf = os.path.join(C.SPLIT_DIR, sub, "cube%03d.drat.zst" % b)
    out = {"retained": os.path.exists(pf), "file": os.path.relpath(pf, C.SPLIT_DIR),
           "old_receipt_proof_sha256": r.get("proof_sha256")}
    if not out["retained"]:
        return out
    out["file_sha256"] = sha_file(pf)
    z = subprocess.Popen(["zstd", "-q", "-dc", pf], stdout=subprocess.PIPE)
    h, n = hashlib.sha256(), 0
    for chunk in iter(lambda: z.stdout.read(1 << 20), b""):
        h.update(chunk)
        n += len(chunk)
    z.wait()
    out.update({"decompress_returncode": z.returncode, "decompressed_sha256": h.hexdigest(),
                "decompressed_bytes": n, "file_matches_old_receipt": out["file_sha256"] == r.get("proof_sha256")})
    out["equals_strict_stream"] = (z.returncode == 0 and out["file_matches_old_receipt"]
                                   and h.hexdigest() == stream_sha)
    return out


def lane_bytes():
    lane = os.path.normpath(os.path.join(HERE, ".."))
    return int(subprocess.run(["du", "-sk", lane], capture_output=True, text=True).stdout.split()[0]) * 1024


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--base", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--select", default="all")
    ap.add_argument("--time", type=int, default=900)
    ap.add_argument("--bind-root-proofs", action="store_true")
    ap.add_argument("--rss-cap", type=int, default=6 * 2 ** 30)
    ap.add_argument("--floor", type=int, default=12_000_000_000)
    ap.add_argument("--lane-budget", type=int, default=int(9.5 * 2 ** 30))
    a = ap.parse_args()
    L, lsha = C.load_ledger(a.ledger)
    base = C.Base(a.base)
    v = C.validate(L, base, C.Receipts())
    if v["problems"]:
        raise SystemExit("ledger invalid: %s" % json.dumps(v["problems"][:20]))
    byid = {x["id"]: x for x in L["leaves"]}
    os.makedirs(a.outdir, exist_ok=True)
    res_path = os.path.join(a.outdir, "RESULTS.jsonl")
    done = set()
    if os.path.exists(res_path):
        for line in open(res_path, "rb").read().split(b"\n"):
            if not line.strip():
                continue
            r = json.loads(line)
            x = byid.get(r.get("id"))
            if x is None or not C.identity_ok("strict", r, x, base):
                raise SystemExit("existing receipt does not match the ledger identity: %s" % r.get("id"))
            if r["id"] in done:
                raise SystemExit("duplicate receipt: %s" % r["id"])
            done.add(r["id"])
    sel = [x for x in L["leaves"] if x["state"] == "UNSTARTED"]
    if a.select.startswith("depth="):
        sel = [x for x in sel if x["depth"] == int(a.select[6:])]
    elif a.select.startswith("ids="):
        want = a.select[4:].split(",")
        if any(byid.get(i, {}).get("state") != "UNSTARTED" for i in want):
            raise SystemExit("ids must be UNSTARTED leaves of the ledger")
        sel = [byid[i] for i in want]
    elif a.select != "all":
        raise SystemExit("bad --select")
    todo = [x for x in sel if x["id"] not in done]
    cad = os.path.realpath(shutil.which("cadical"))
    meta = {"argv": sys.argv, "python": sys.version, "script_sha256": sha_file(__file__),
            "k5_resplit_sha256": sha_file(os.path.join(HERE, "k5_resplit.py")),
            "k5_cover_sha256": sha_file(os.path.join(HERE, "k5_cover.py")), "ledger": a.ledger,
            "ledger_sha256": lsha, "ledger_validation": {k: v[k] for k in ("leaves", "terminal", "counts")},
            "base_cnf_sha256": base.sha, "selected": len(sel), "todo": len(todo), "cadical_binary": cad,
            "cadical_sha256": sha_file(cad),
            "cadical_version": subprocess.run([cad, "--version"], capture_output=True, text=True).stdout.strip(),
            "cadical_seed": "default (no --seed given)", "solver_args": R.SOLVER_ARGS + ["-t", str(a.time)],
            "drat_trim_binary": R.DT, "drat_trim_sha256": sha_file(R.DT), "checker_flags": R.DT_FLAGS,
            "rss_cap": a.rss_cap, "floor": a.floor, "lane_budget": a.lane_budget, "start": time.ctime()}
    with open(os.path.join(a.outdir, "META.%d.json" % int(time.time())), "x") as fh:
        json.dump(meta, fh, indent=1)
    fifos = tuple(os.path.join(a.outdir, "w0.%s.fifo" % s) for s in ("cnf_s", "cnf_c", "proof"))
    for p in fifos:
        if not os.path.exists(p):
            os.mkfifo(p)
    print(json.dumps({"selected": len(sel), "todo": len(todo), "ledger_sha256": lsha}), flush=True)
    for x in todo:
        fb, lb = shutil.disk_usage(a.outdir).free, lane_bytes()
        if fb < a.floor or lb > a.lane_budget:
            with open(os.path.join(a.outdir, "STOP.%d.json" % int(time.time())), "x") as fh:
                json.dump({"before_leaf": x["id"], "free": fb, "lane_bytes": lb}, fh)
            print(json.dumps({"stop_before": x["id"], "free": fb, "lane": lb}), flush=True)
            break
        n = 1
        while os.path.exists(os.path.join(a.outdir, "%s.a%d.solver.log" % (x["id"], n))):
            n += 1
        tag = "%s.a%d" % (x["id"], n)
        rec = {"id": x["id"], "depth": x["depth"], "index": x["index"], "ancestor": x["ancestor"],
               "lits": x["lits"], "base_cnf_sha256": base.sha, "ledger_sha256": lsha, "attempt_tag": tag}
        rec.update(R.certify(tag, x["lits"], base.nv, base.nc, base.body, a.outdir, fifos, a.time, a.rss_cap))
        if rec["cnf_sha256"] != base.leaf_sha(x["lits"]):
            raise SystemExit("internal CNF hash mismatch at %s" % x["id"])
        if a.bind_root_proofs and x["depth"] == 1:
            rec["retained_binding"] = bind_root(x["index"], rec["proof_stream_sha256"])
        rec["strict_ok"] = C.strict_ok(rec)
        with open(res_path, "a") as fh:
            fh.write(json.dumps(rec) + "\n")
        print(json.dumps({"id": x["id"], "strict_ok": rec["strict_ok"], "secs": rec["secs"],
                          "solver_rc": rec["solver_returncode"], "checker_rc": rec["checker_returncode"],
                          "rss_gib": round(rec["aggregate_peak_rss_bytes"] / 2 ** 30, 2),
                          "bind": rec.get("retained_binding", {}).get("equals_strict_stream")}), flush=True)


if __name__ == "__main__":
    main()
