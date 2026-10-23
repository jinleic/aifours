"""Parse and check the Egan–Wanless species representatives of 3-MOLS(8) (Wayback copies in sources/ew_data:
maxMOLS8.3.txt (38 maximal species) and nmaxMOLS8.3.txt (1 non-maximal species)).

Checks per set: three Latin squares of order 8, mutually orthogonal; symbols relabelled per square so that row 0 is
0..7 (a symbol relabelling of a classical square does not change its net). Maximality: a 4th Latin square
orthogonal to all three exists?  (exact SAT check with CaDiCaL; expected UNSAT for the 38 maximal, SAT for the
non-maximal species). Isomorphism invariants of the 5-net {rows, columns, 3 symbol classes}: for each of the 10
triples of classes the number of intercalates (2x2 subsquares) of the Latin square they define (a main-class
invariant), sorted; plus the number of common transversals of the three squares. Distinct invariants => distinct
classes.
python -B ew_nets.py --out ../evidence/k2_fixed/ew_nets.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, "..", "sources", "ew_data"))
N = 8


def parse(path):
    lines = open(path).read().split("\n")
    header = lines[0].split()
    n, k = int(header[0]), int(header[1])
    m = int(header[2])
    sq, cur = [], []
    for line in lines[1:]:
        s = line.strip()
        if not s:
            if cur:
                sq.append(cur)
                cur = []
            continue
        if not all("a" <= ch <= "h" for ch in s) or len(s) != n:
            break
        cur.append([ord(ch) - 97 for ch in s])
    if cur:
        sq.append(cur)
    assert len(sq) == m and all(len(x) == k for x in sq), (path, len(sq), m)
    return sq


def normalize(L):
    perm = {L[0][j]: j for j in range(N)}
    return [[perm[x] for x in row] for row in L]


def latin(L):
    return all(sorted(r) == list(range(N)) for r in L) and all(sorted(L[i][j] for i in range(N)) == list(range(N))
                                                              for j in range(N))


def orth(A, B):
    return len({(A[i][j], B[i][j]) for i in range(N) for j in range(N)}) == N * N


def net_classes(sqs):
    cells = [(i, j) for i in range(N) for j in range(N)]
    cls = [{c: c[0] for c in cells}, {c: c[1] for c in cells}]
    for L in sqs:
        cls.append({c: L[c[0]][c[1]] for c in cells})
    return cls


def intercalates(M):
    cnt = 0
    for r1, r2 in itertools.combinations(range(N), 2):
        for c1, c2 in itertools.combinations(range(N), 2):
            if M[r1][c1] == M[r2][c2] and M[r1][c2] == M[r2][c1]:
                cnt += 1
    return cnt


def triple_square(cls, A, B, C):
    cells = list(cls[0])
    M = [[None] * N for _ in range(N)]
    for c in cells:
        M[cls[A][c]][cls[B][c]] = cls[C][c]
    return M


def common_transversals(sqs):
    cnt = 0
    for perm in itertools.permutations(range(N)):
        if all(len({L[i][perm[i]] for i in range(N)}) == N for L in sqs):
            cnt += 1
    return cnt


def extendable(sqs, tag, outdir):
    """SAT: a Latin square X (first row identity w.l.o.g. by symbol relabelling) orthogonal to all of sqs."""
    var = lambda i, j, x: 1 + (i * N + j) * N + x
    nv = N * N * N
    cls = []
    for i in range(N):
        for j in range(N):
            cls.append([var(i, j, x) for x in range(N)])
            for x, y in itertools.combinations(range(N), 2):
                cls.append([-var(i, j, x), -var(i, j, y)])
    for x in range(N):
        for i in range(N):
            for j1, j2 in itertools.combinations(range(N), 2):
                cls.append([-var(i, j1, x), -var(i, j2, x)])
        for j in range(N):
            for i1, i2 in itertools.combinations(range(N), 2):
                cls.append([-var(i1, j, x), -var(i2, j, x)])
    for j in range(N):
        cls.append([var(0, j, j)])
    cells = [(i, j) for i in range(N) for j in range(N)]
    for L in sqs:
        for c1, c2 in itertools.combinations(cells, 2):
            if L[c1[0]][c1[1]] == L[c2[0]][c2[1]]:
                for x in range(N):     # cells sharing an L-symbol must get different X-symbols
                    cls.append([-var(c1[0], c1[1], x), -var(c2[0], c2[1], x)])
    path = os.path.join(outdir, "ext_%s.cnf" % tag)
    with open(path, "x") as fh:
        fh.write("p cnf %d %d\n" % (nv, len(cls)))
        for cl in cls:
            fh.write(" ".join(map(str, cl)) + " 0\n")
    r = subprocess.run(["cadical", "-q", "-t", "600", path], capture_output=True, text=True)
    return {10: "SAT", 20: "UNSAT"}.get(r.returncode, "UNKNOWN(%d)" % r.returncode)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    outdir = os.path.dirname(a.out)
    os.makedirs(outdir, exist_ok=True)
    files = {"max": os.path.join(SRC, "maxMOLS8.3.txt"), "nmax": os.path.join(SRC, "nmaxMOLS8.3.txt")}
    res = {"argv": sys.argv, "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "sources": {k: {"path": os.path.relpath(v, os.path.join(HERE, "..")),
                           "sha256": hashlib.sha256(open(v, "rb").read()).hexdigest()} for k, v in files.items()},
           "nets": []}
    for kind, path in files.items():
        sq = parse(path)
        assert len(sq) % 3 == 0
        for s in range(len(sq) // 3):
            raw = sq[3 * s:3 * s + 3]
            sqs = [normalize(L) for L in raw]
            tag = "%s%02d" % (kind, s)
            cls = net_classes(sqs)
            inv = sorted(intercalates(triple_square(cls, *t)) for t in itertools.combinations(range(5), 3))
            item = {"tag": tag, "kind": kind, "squares": sqs, "latin": all(latin(L) for L in sqs),
                    "orthogonal": all(orth(A, B) for A, B in itertools.combinations(sqs, 2)),
                    "intercalate_multiset": inv, "common_transversals": common_transversals(sqs),
                    "fourth_square": extendable(sqs, tag, outdir)}
            res["nets"].append(item)
            print(json.dumps({k: item[k] for k in ("tag", "latin", "orthogonal", "intercalate_multiset",
                                                     "common_transversals", "fourth_square")}), flush=True)
    keys = [(tuple(x["intercalate_multiset"]), x["common_transversals"]) for x in res["nets"]]
    res["summary"] = {"nets": len(res["nets"]), "all_latin_orthogonal": all(x["latin"] and x["orthogonal"]
                                                                            for x in res["nets"]),
                      "maximal_fourth_UNSAT": all(x["fourth_square"] == "UNSAT" for x in res["nets"]
                                                  if x["kind"] == "max"),
                      "nonmax_fourth_SAT": all(x["fourth_square"] == "SAT" for x in res["nets"] if x["kind"] == "nmax"),
                      "distinct_invariant_keys": len(set(keys))}
    with open(a.out, "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res["summary"]))


if __name__ == "__main__":
    main()
