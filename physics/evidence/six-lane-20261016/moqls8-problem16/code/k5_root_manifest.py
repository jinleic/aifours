"""Master manifest of the retained K5 root proofs for parent replay (no live-log scanning needed). For every CERTIFIED
root of the given ledger: root id, literals, leaf-CNF SHA-256 (recomputed from the base), strict receipt (file + line
SHA-256), retained proof path (relative to evidence/k5_split_v1), retained file SHA-256 (re-hashed now), decompressed
SHA-256/bytes and the strict streamed proof SHA-256 they equal, old worker receipt line SHA-256. Also emits a
`shasum -a 256 -c`-compatible list of the proof files. Exclusive-create outputs; nothing else is touched.
python -B k5_root_manifest.py --ledger ../evidence/k5_split_v1/ledger/LEDGER.v003.json --base ../evidence/gram_dev_v1/GA5L_K5_sb2.cnf \\
       --out ../evidence/k5_split_v1/RETAINED_ROOT_PROOFS_MANIFEST_v1
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("k5_cover", os.path.join(HERE, "k5_cover.py"))
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 24), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--base", required=True)
    ap.add_argument("--out", required=True, help="output prefix (.json and .sha256)")
    a = ap.parse_args()
    L, lsha = C.load_ledger(a.ledger)
    base = C.Base(a.base)
    rc = C.Receipts()
    v = C.validate(L, base, rc)
    if v["problems"]:
        raise SystemExit("ledger invalid")
    old = {}
    for sub in ("pilot", "all"):
        for line in open(os.path.join(C.SPLIT_DIR, sub, "RESULTS.jsonl"), "rb").read().split(b"\n"):
            if line.strip():
                r = json.loads(line)
                old[r["cube"]] = (sub, hashlib.sha256(line).hexdigest(), r)
    rows, sums = [], []
    for x in L["leaves"]:
        if x["depth"] != 1 or x["state"] != "CERTIFIED":
            continue
        ev = x["evidence"]
        r = rc.get(ev["file"], ev["line_sha256"])
        b = r["retained_binding"]
        sub, old_line_sha, orec = old[x["index"]]
        pf = os.path.join(C.SPLIT_DIR, b["file"])
        fsha = sha_file(pf)
        ok = (b["equals_strict_stream"] and fsha == b["file_sha256"] == orec["proof_sha256"]
              and b["decompressed_sha256"] == r["proof_stream_sha256"]
              and r["cnf_sha256"] == base.leaf_sha(x["lits"]) == orec["cnf_sha256"])
        rows.append({"id": x["id"], "lits": x["lits"], "leaf_cnf_sha256": r["cnf_sha256"],
                     "leaf_cnf_clauses": r["cnf_clauses"], "strict_receipt": ev, "strict_proof_stream_sha256":
                     r["proof_stream_sha256"], "strict_proof_stream_bytes": r["proof_stream_bytes"],
                     "retained_proof": b["file"], "retained_proof_sha256": fsha,
                     "retained_proof_bytes": os.path.getsize(pf), "decompressed_sha256": b["decompressed_sha256"],
                     "decompressed_bytes": b["decompressed_bytes"], "old_worker_receipt":
                     {"file": sub + "/RESULTS.jsonl", "line_sha256": old_line_sha}, "consistent": ok})
        sums.append("%s  %s" % (fsha, b["file"]))
    out = {"argv": sys.argv, "script_sha256": sha_file(__file__), "ledger": a.ledger, "ledger_sha256": lsha,
           "base_cnf_sha256": base.sha, "paths_relative_to": "evidence/k5_split_v1",
           "replay_recipe": "leaf CNF = 'p cnf %d %d+|lits|' header, the base CNF body (bytes after its first line), "
                            "then one line '<lit> 0' per literal in order; proof = zstd -dc <retained_proof> (binary "
                            "DRAT); check: drat-trim <leaf CNF> <proof> -i (or proof on stdin)" % (base.nv, base.nc),
           "roots": len(rows), "all_consistent": all(r["consistent"] for r in rows), "rows": rows}
    with open(a.out + ".json", "x") as fh:
        json.dump(out, fh, indent=1)
    with open(a.out + ".sha256", "x") as fh:
        fh.write("\n".join(sums) + "\n")
    print(json.dumps({"roots": len(rows), "all_consistent": out["all_consistent"],
                      "total_retained_bytes": sum(r["retained_proof_bytes"] for r in rows)}))


if __name__ == "__main__":
    main()
