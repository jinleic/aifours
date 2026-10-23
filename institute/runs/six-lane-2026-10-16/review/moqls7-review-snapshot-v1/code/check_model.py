"""Direct (encoder-independent) check of a decoded pattern JSON (output of k2_encode_a.py --decode).

python -B check_model.py PATTERN.json [--w3 1234] [--no-p3]
Checks: classical squares are Latin, first row identity, pairwise orthogonal; patterns satisfy (P1)-(P4)
via k2_controls.check (direct evaluation from the definitions).
"""
from __future__ import annotations

import argparse
import itertools
import json

from k2_controls import N, check


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pattern")
    ap.add_argument("--w3", default="")
    ap.add_argument("--no-p3", action="store_true", help="ignore P3 violations (for --no-p3 encoder runs)")
    a = ap.parse_args()
    d = json.load(open(a.pattern))
    squares = [d[k] for k in sorted(d) if k.startswith("L")]
    pats = {int(k[1:]): d[k] for k in sorted(d) if k.startswith("S")}
    ok_latin = all(sorted(row) == list(range(N)) for sq in squares for row in sq) and \
        all(sorted(sq[i][j] for i in range(N)) == list(range(N)) for sq in squares for j in range(N)) and \
        all(sq[0] == list(range(N)) for sq in squares)
    ok_orth = all(len({(A[i][j], B[i][j]) for i in range(N) for j in range(N)}) == N * N
                  for A, B in itertools.combinations(squares, 2))
    bad = check(squares, pats, tuple(int(ch) for ch in a.w3))
    if a.no_p3:
        bad = [b for b in bad if not b.startswith("P3")]
    weights = {s: sorted({len(P[i][j]) for i in range(1, N) for j in range(N)}) for s, P in pats.items()}
    cell10 = {s: P[1][0] for s, P in pats.items()}
    col0 = {k: [d[k][i][0] for i in range(N)] for k in sorted(d) if k.startswith("L")}
    print(json.dumps({"latin_standard": ok_latin, "orthogonal": ok_orth, "violations": len(bad),
                      "first": bad[:5], "weights": weights, "cell_1_0": cell10, "classical_col0": col0}))


if __name__ == "__main__":
    main()
