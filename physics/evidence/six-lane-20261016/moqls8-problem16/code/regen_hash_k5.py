"""Regenerate the unconditional K5 CNF in memory with code/gram_a.py's build() (same arguments as recorded in the map
meta: --order 8 --mode generic --quantum 12345 --ngeneric 0 --p4 12345 --sb2 --g5 --rowlex), serialise it exactly as
gram_a.py's writer does, and compare its SHA-256 with the stored base CNF (README §8). Nothing is written except the
receipt.
python -B regen_hash_k5.py --stored ../evidence/gram_dev_v1/GA5L_K5_sb2.cnf --out ../evidence/k5_split_v1/REGEN_RECEIPT.json
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stored", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    spec = importlib.util.spec_from_file_location("gram_a", os.path.join(HERE, "gram_a.py"))
    G = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(G)
    f = G.build(8, "generic", [], [1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5], False, True, None, True, True)
    h = hashlib.sha256()
    h.update(("p cnf %d %d\n" % (f.nv, len(f.clauses))).encode())
    for cl in f.clauses:
        h.update((" ".join(map(str, cl)) + " 0\n").encode())
    hs = hashlib.sha256()
    with open(a.stored, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 24), b""):
            hs.update(chunk)
    rec = {"argv": sys.argv, "gram_a_sha256": hashlib.sha256(open(os.path.join(HERE, "gram_a.py"), "rb").read()).hexdigest(),
           "build_args": "build(8, 'generic', [], [1,2,3,4,5], 0, [1,2,3,4,5], p4_all_rows=False, sb2=True, fixg=None, "
                         "g5=True, rowlex=True)",
           "regenerated_sha256": h.hexdigest(), "stored_sha256": hs.hexdigest(), "vars": f.nv, "clauses": len(f.clauses)}
    rec["byte_equal"] = rec["regenerated_sha256"] == rec["stored_sha256"]
    with open(a.out, "x") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps(rec))
    if not rec["byte_equal"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
