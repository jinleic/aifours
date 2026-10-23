"""K3 coverage ledger (README §4): one entry per E–W 2-MOLS(8) representative (2165 = 2127 maximal + 38 non-maximal),
with the catalogue source (file, SHA-256, position), the normalised squares' SHA-256, and for each encoder the exact
DIMACS SHA-256 recorded by run_fixed_k3.py; for encoder A the retained zstd proof (file, SHA-256 re-computed now,
bytes) and the drat-trim verdict; for encoder B the kissat status (no proof). Orphan proof files (instances
interrupted by the two SIGTERM pauses, no RESULTS row) are listed separately as UNKNOWN and are not used.
Fails (exit 1) unless every net has exactly one UNSAT row per encoder and every A row is VERIFIED with an existing
proof whose SHA-256 matches the recorded one.
python -B k3_ledger.py --outdir ../evidence/k3_fixed/all_v1 --out ../evidence/k3_fixed/K3_COVERAGE_LEDGER.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, "..", "sources", "ew_data"))
sys.path.insert(0, HERE)
from run_fixed_k3 import parse, normalize  # noqa: E402  (the batch's own parser)


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 22), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    files = {"max": os.path.join(SRC, "maxMOLS8.2.txt"), "nmax": os.path.join(SRC, "nmaxMOLS8.2.txt")}
    nets = {}
    for kind, path in files.items():
        sq = parse(path)
        for s in range(len(sq) // 2):
            tag = "%s%04d" % (kind, s)
            norm = [normalize(L) for L in sq[2 * s:2 * s + 2]]
            nets[tag] = {"source": os.path.basename(path), "index": s,
                         "squares_sha256": hashlib.sha256(json.dumps(norm).encode()).hexdigest()}
    rows = [json.loads(l) for l in open(os.path.join(a.outdir, "RESULTS.jsonl"))]
    by = {}
    for r in rows:
        by.setdefault((r["net"], r["encoder"]), []).append(r)
    problems = []
    used_proofs = set()
    for tag, e in nets.items():
        for enc in ("a", "b"):
            rs = by.get((tag, enc), [])
            if len(rs) != 1:
                problems.append([tag, enc, "rows=%d" % len(rs)])
                continue
            r = rs[0]
            ent = {"cnf_sha256": r["cnf_sha256"], "cnf_bytes": r["cnf_bytes"], "status": r["status"],
                   "solve_secs": r["secs"]}
            if r["status"] != "UNSAT":
                problems.append([tag, enc, r["status"]])
            if enc == "a":
                p = os.path.join(a.outdir, r["proof"])
                ok = os.path.exists(p) and sha_file(p) == r["proof_sha256"]
                ent.update({"proof": r["proof"], "proof_sha256": r["proof_sha256"], "proof_bytes": r["proof_bytes"],
                            "proof_present_and_hash_ok": ok, "drat_trim": "VERIFIED" if r.get("verified") else "NO",
                            "check_exit": r.get("check_exit")})
                used_proofs.add(r["proof"])
                if not (ok and r.get("verified")):
                    problems.append([tag, enc, "proof/verdict"])
            e[enc] = ent
    orphans = sorted(f for f in os.listdir(a.outdir) if f.endswith(".drat.zst") and f not in used_proofs)
    res = {"argv": sys.argv, "script_sha256": sha_file(__file__),
           "batch_script_sha256": sha_file(os.path.join(HERE, "run_fixed_k3.py")),
           "enc8_a2_sha256": sha_file(os.path.join(HERE, "enc8_a2.py")),
           "enc8_b2_sha256": sha_file(os.path.join(HERE, "enc8_b2.py")),
           "sources": {k: {"path": os.path.relpath(v, os.path.join(HERE, "..")), "sha256": sha_file(v)}
                       for k, v in files.items()},
           "results_jsonl_sha256": sha_file(os.path.join(a.outdir, "RESULTS.jsonl")),
           "nets_total": len(nets), "rows_total": len(rows), "orphan_proofs_UNKNOWN_unused": orphans,
           "problems": problems, "complete": not problems, "nets": nets,
           "regeneration": "CNFs are not stored: run_fixed_k3.py builds them in memory with enc8_a2.build('fixed', (), "
                           "(1,2,3), p3=True, p4=(1,2,3), squares=S) and enc8_b2.encode('fixed', [], False, (1,2,3), "
                           "(1,2,3), None, True, 2, False, S) for the row-0-normalised squares S of each catalogue "
                           "pair, serialises 'p cnf V C' + one clause per line ending in ' 0', and hashes the bytes; "
                           "encoder-A proofs are retained as zstd-compressed binary DRAT and can be checked with "
                           "`zstd -dc PROOF | drat-trim CNF -i`."}
    with open(a.out, "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({k: res[k] for k in ("nets_total", "rows_total", "complete")} |
                     {"problems": problems[:10], "orphans": orphans}))
    if problems:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
