#!/usr/bin/env python3
"""PA18 positive control for the M2 version-2 encoder (encode_skel_b.build_v2g, 18-row variant:
five (3^6) base columns, three (4,3,3,3,3,2) columns, row-major lex-leader symmetry breaking).
The CPro1 array in the normal form produced by control18.py m1 (row-major repairs of value
swaps, row transpositions and special-column swaps; cycle2/control18/cpro1-canonical-m1.txt)
must satisfy the CNF with every cell fixed; corrupted arrays must not.
Usage: control18_v2.py OUT_JSON
"""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_skel_b  # noqa: E402

LANE = os.path.dirname(HERE)
KISSAT = "/opt/homebrew/bin/kissat"


def solve(nv, cl, units):
    parts = ["p cnf %d %d\n" % (nv, len(cl) + len(units))]
    parts.extend(" ".join(map(str, c)) + " 0\n" for c in cl)
    parts.extend("%d 0\n" % u for u in units)
    return subprocess.run([KISSAT, "-q", "-n"], input="".join(parts).encode(), capture_output=True).returncode


def main():
    src = os.path.join(LANE, "cycle2", "control18", "cpro1-canonical-m1.txt")
    A = [list(map(int, l.split())) for l in open(src)]
    nv, cl = encode_skel_b.build_v2g(5, [], 18, [[4, 3, 3, 3, 3, 2]] * 3, N=18, K=8, Q=6, base_quad=False)
    v = lambda r, c, s: 1 + 48 * r + 6 * c + s  # noqa: E731
    units = lambda B: [v(r, c, B[r][c]) for r in range(18) for c in range(8)]  # noqa: E731
    res = {"source": src, "source_sha256": hashlib.sha256(open(src, "rb").read()).hexdigest(),
           "canonical_rc": solve(nv, cl, units(A))}
    muts = {}
    B = [row[:] for row in A]
    B[1][5], B[1][6] = B[0][5], B[0][6]
    muts["rows01_two_extra_agreements"] = B
    B = [row[:] for row in A]
    B[17] = B[0][:]
    muts["duplicate_row"] = B
    B = [row[:] for row in A]
    B[3][2] = (B[3][2] + 1) % 6
    muts["single_cell_change"] = B
    res["mutations"] = {k: solve(nv, cl, units(Bm)) for k, Bm in muts.items()}
    res["ok"] = res["canonical_rc"] == 10 and all(x == 20 for x in res["mutations"].values())
    json.dump(res, open(sys.argv[1], "w"), indent=1)
    print(json.dumps(res))


if __name__ == "__main__":
    main()
