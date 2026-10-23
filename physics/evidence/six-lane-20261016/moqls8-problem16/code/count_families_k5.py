"""Family counts for the K5 base CNF (Claude review M2/C6/C7): rebuild in memory with gram_a.py build() (recorded
arguments), confirm the SHA-256 equals the stored base, and count: P4 at-least-one clauses (clauses made only of
positive w3 flags), w3 squares and frames, lexeq variables and the rows they relate, SB2 unit clauses on (1,0) cells.
python -B count_families_k5.py --stored ../evidence/gram_dev_v1/GA5L_K5_sb2.cnf --out ../evidence/k5_split_v1/FAMILY_COUNTS.json
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
    hs = hashlib.sha256(open(a.stored, "rb").read()).hexdigest()
    keys = [k for k in f.names if isinstance(k, tuple)]
    w3 = {f.names[k] for k in keys if k[0] == "w3"}
    alo = [cl for cl in f.clauses if all(l > 0 and l in w3 for l in cl)]
    inv = {v: k for k, v in f.names.items()}
    alo_desc = sorted({(inv[cl[0]][1], inv[cl[0]][2]) for cl in alo})
    gid = {f.names[k]: k for k in keys if k[0] == "g"}
    units = [cl[0] for cl in f.clauses if len(cl) == 1]
    sb2 = sorted((gid[abs(u)][1], gid[abs(u)][2], gid[abs(u)][3], u > 0) for u in units if abs(u) in gid)
    rec = {"argv": sys.argv, "gram_a_sha256": hashlib.sha256(open(os.path.join(HERE, "gram_a.py"), "rb").read()
                                                             ).hexdigest(),
           "regenerated_sha256": h.hexdigest(), "stored_sha256": hs, "byte_equal": h.hexdigest() == hs,
           "p4_at_least_one_clauses": len(alo), "p4_alo_square_frame_pairs": alo_desc,
           "w3_squares": sorted({k[1] for k in keys if k[0] == "w3"}),
           "w3_frames(row index)": sorted({k[2] for k in keys if k[0] == "w3"}),
           "lexeq_variables": sum(1 for k in keys if k[0] == "lexeq"),
           "lexeq_rows_i": sorted({k[1] for k in keys if k[0] == "lexeq"}),
           "unit_clauses_total": len(units), "unit_clauses_on_g": [list(map(str, x)) for x in sb2],
           "other_aux_families": sorted({k[0] for k in keys} - {"g", "b3", "c4", "u5", "w3", "lexeq"})}
    with open(a.out, "x") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({k: rec[k] for k in ("byte_equal", "p4_at_least_one_clauses", "p4_alo_square_frame_pairs",
                                          "w3_squares", "w3_frames(row index)", "lexeq_variables", "lexeq_rows_i",
                                          "unit_clauses_total", "other_aux_families")}))
    print(len(rec["unit_clauses_on_g"]), rec["unit_clauses_on_g"][:3])


if __name__ == "__main__":
    main()
