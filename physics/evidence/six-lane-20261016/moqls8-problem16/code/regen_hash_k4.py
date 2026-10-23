"""Regenerate the K4 weight-1 base CNF in memory with code/gram_a_r3.py's build() using the arguments recorded in
evidence/k4_w1_v1/GA3_K4w1.map.json (--order 8 --mode generic --quantum 12345 --ngeneric 0 --p4 1234 --p4-all-rows
--p4-all-cols --sb2 --g5 --weight1 5; no --rowlex), serialise exactly as gram_a_r3.py's writer does and compare the
SHA-256 with the stored file. Also counts the P4 at-least-one clauses (clauses consisting only of w3 flag variables).
python -B regen_hash_k4.py --stored ../evidence/k4_w1_v1/GA3_K4w1.cnf --out ../evidence/k4_split_v1/REGEN_RECEIPT.json
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
    spec = importlib.util.spec_from_file_location("gram_a_r3", os.path.join(HERE, "gram_a_r3.py"))
    G = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(G)
    f = G.build(8, "generic", [], [1, 2, 3, 4, 5], 0, [1, 2, 3, 4], True, True, None, True, False, True, 5)
    h = hashlib.sha256()
    h.update(("p cnf %d %d\n" % (f.nv, len(f.clauses))).encode())
    for cl in f.clauses:
        h.update((" ".join(map(str, cl)) + " 0\n").encode())
    hs = hashlib.sha256()
    with open(a.stored, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 24), b""):
            hs.update(chunk)
    w3 = {v for k, v in f.names.items() if isinstance(k, tuple) and k[0] == "w3"}
    lex = [k for k in f.names if isinstance(k, tuple) and k[0] == "lexeq"]
    w3_squares = sorted({k[1] for k in f.names if isinstance(k, tuple) and k[0] == "w3"})
    alo = sum(1 for cl in f.clauses if all(l > 0 and l in w3 for l in cl))
    rec = {"argv": sys.argv,
           "gram_a_r3_sha256": hashlib.sha256(open(os.path.join(HERE, "gram_a_r3.py"), "rb").read()).hexdigest(),
           "build_args": "build(8, 'generic', [], [1,2,3,4,5], 0, [1,2,3,4], p4_all_rows=True, sb2=True, fixg=None, "
                         "g5=True, rowlex=False, p4_all_cols=True, weight1=5)",
           "regenerated_sha256": h.hexdigest(), "stored_sha256": hs.hexdigest(), "vars": f.nv, "clauses": len(f.clauses),
           "p4_at_least_one_clauses": alo, "w3_squares": w3_squares, "lexeq_variables": len(lex)}
    rec["byte_equal"] = rec["regenerated_sha256"] == rec["stored_sha256"]
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "x") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps(rec))
    if not rec["byte_equal"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
