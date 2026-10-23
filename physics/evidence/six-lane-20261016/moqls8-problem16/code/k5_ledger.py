"""K5 split coverage ledger (README §8): checks that the cube file is exactly the 2^|V| complete assignments of the
declared variables V (re-generated here independently and compared line by line), that every cube index has exactly one
receipt with solver status UNSAT and a strict drat-trim VERIFIED, that each retained proof file exists with the recorded
SHA-256, and that the recorded CNF SHA-256 equals the SHA-256 of (base CNF with header clause count + |cube|, followed
by the cube's unit clauses) recomputed here from the base CNF. Exit 1 unless complete.
python -B k5_ledger.py --cnf ../evidence/gram_dev_v1/GA5L_K5_sb2.cnf --cubes ../evidence/k5_split_v1/cubes_V7.icnf \\
   --vars 57,106,155,204,253,302,351 --results ../evidence/k5_split_v1/all/RESULTS.jsonl[,MORE.jsonl] --out LEDGER.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 24), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cnf", required=True)
    ap.add_argument("--cubes", required=True)
    ap.add_argument("--vars", required=True)
    ap.add_argument("--results", required=True, help="comma-separated RESULTS.jsonl files (pilot + batch)")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    V = [int(x) for x in a.vars.split(",")]
    expect = ["a " + " ".join(str(v if (b >> k) & 1 else -v) for k, v in enumerate(V)) + " 0"
              for b in range(2 ** len(V))]
    got = [l.rstrip("\n") for l in open(a.cubes) if l.startswith("a ")]
    cube_file_ok = got == expect
    with open(a.cnf, "rb") as fh:
        header = fh.readline().decode().split()
        body = fh.read()
    nv, nc = int(header[2]), int(header[3])
    body_hash = hashlib.sha256(body)
    rows = {}
    for path in a.results.split(","):
        base = os.path.dirname(path)
        for line in open(path):
            r = json.loads(line)
            r["_dir"] = base
            rows.setdefault(r["cube"], []).append(r)
    problems = []
    entries = {}
    for b in range(2 ** len(V)):
        rs = rows.get(b, [])
        good = [r for r in rs if r.get("solver_status") == "UNSAT" and r.get("verified")]
        if not good:
            problems.append([b, "no verified receipt", [r.get("solver_status") for r in rs]])
            continue
        r = good[0]
        lits = [int(t) for t in expect[b].split()[1:-1]]
        h = hashlib.sha256(("p cnf %d %d\n" % (nv, nc + len(lits))).encode())
        h2 = body_hash.copy()
        hh = hashlib.sha256()
        hh.update(("p cnf %d %d\n" % (nv, nc + len(lits))).encode())
        hh.update(body)
        hh.update("".join("%d 0\n" % l for l in lits).encode())
        proof = os.path.join(r["_dir"], "cube%03d.drat.zst" % b)
        ok_cnf = hh.hexdigest() == r["cnf_sha256"] and r["lits"] == lits
        ok_proof = os.path.exists(proof) and sha_file(proof) == r["proof_sha256"]
        if not (ok_cnf and ok_proof):
            problems.append([b, "binding", ok_cnf, ok_proof])
        entries[b] = {"cnf_sha256": r["cnf_sha256"], "proof": os.path.relpath(proof, os.path.dirname(a.out)),
                      "proof_sha256": r["proof_sha256"], "proof_bytes_zst": r["proof_bytes_zst"],
                      "solve_secs": r["solve_secs"], "check_secs": r.get("check_secs"),
                      "checker_rss_bytes": r.get("checker_rss_bytes"), "receipts_for_cube": len(rs)}
    res = {"argv": sys.argv, "script_sha256": sha_file(__file__), "base_cnf_sha256": sha_file(a.cnf),
           "cubes_sha256": sha_file(a.cubes), "vars": V, "cube_file_equals_full_product": cube_file_ok,
           "cubes": 2 ** len(V), "verified_cubes": len(entries) - sum(1 for p in problems if p[1] == "binding"),
           "problems": problems, "complete": cube_file_ok and not problems, "entries": entries}
    with open(a.out, "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({k: res[k] for k in ("cube_file_equals_full_product", "cubes", "verified_cubes", "complete")} |
                     {"problems": problems[:10]}))
    if not res["complete"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
