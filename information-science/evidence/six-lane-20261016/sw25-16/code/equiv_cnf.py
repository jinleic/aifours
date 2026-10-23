#!/usr/bin/env python3
"""CNF for: exists a signed permutation M with M W symmetric (notes/facts-v1.md F3).

Usage: python3 -B code/equiv_cnf.py MATRIXFILE FORMAT OUT.cnf
  FORMAT in {magma, bracket, strict}.  Writes OUT.cnf (mode x) and OUT.cnf.map.json (mode x).
Variables: x(i,k) <-> pi(i) = k (row i of M W is +-row k of W), e(i) <-> sign of row i of M W is -1.
Constraints: pi is a permutation (exactly one k per i, exactly one i per k; pairwise at-most-one);
for i < j and k != l: x(i,k) & x(j,l) -> e_i W[k][j] = e_j W[l][i]  (that is (M W)_{ij} = (M W)_{ji}).
Symmetry breaking E0: e(0) false (if M works then -M works).
Decode: python3 -B code/equiv_cnf.py --decode MATRIXFILE FORMAT MAP.json SOLVER_STDOUT OUT.sw
"""
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sw_common as C  # noqa: E402


def load(path, fmt):
    if fmt == "magma":
        return C.parse_magma(path)
    if fmt == "bracket":
        return C.parse_bracket(path)
    if fmt == "strict":
        return C.read_strict(path)[2]
    raise ValueError(fmt)


def build(W):
    n = len(W)
    x = lambda i, k: 1 + i * n + k  # noqa: E731
    e = lambda i: 1 + n * n + i  # noqa: E731
    nv = n * n + n
    cls = []
    for i in range(n):
        cls.append([x(i, k) for k in range(n)])
        for k in range(n):
            for l in range(k + 1, n):
                cls.append([-x(i, k), -x(i, l)])
    for k in range(n):
        cls.append([x(i, k) for i in range(n)])
        for i in range(n):
            for j in range(i + 1, n):
                cls.append([-x(i, k), -x(j, k)])
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(n):
                for l in range(n):
                    if k == l:
                        continue
                    a, b = W[k][j], W[l][i]
                    if a == 0 and b == 0:
                        continue
                    if a == 0 or b == 0:
                        cls.append([-x(i, k), -x(j, l)])
                    elif a == b:  # need e_i == e_j
                        cls.append([-x(i, k), -x(j, l), -e(i), e(j)])
                        cls.append([-x(i, k), -x(j, l), e(i), -e(j)])
                    else:  # need e_i != e_j
                        cls.append([-x(i, k), -x(j, l), e(i), e(j)])
                        cls.append([-x(i, k), -x(j, l), -e(i), -e(j)])
    cls.append([-e(0)])
    return nv, cls


def main():
    if sys.argv[1] == "--decode":
        _, _, mpath, fmt, mapf, sol, out = sys.argv
        W = load(mpath, fmt)
        n = len(W)
        vals = set()
        for line in open(sol):
            if line.startswith("v "):
                vals.update(int(t) for t in line.split()[1:])
        perm = [next(k for k in range(n) if (1 + i * n + k) in vals) for i in range(n)]
        sgn = [-1 if (1 + n * n + i) in vals else 1 for i in range(n)]
        S = [[sgn[i] * W[perm[i]][j] for j in range(n)] for i in range(n)]
        with open(out, "x") as f:
            f.write(C.to_strict(S, n, 16))
        print("decoded perm", perm, "signs", sgn)
        return
    mpath, fmt, out = sys.argv[1], sys.argv[2], sys.argv[3]
    W = load(mpath, fmt)
    n = len(W)
    nv, cls = build(W)
    body = "".join(" ".join(map(str, c)) + " 0\n" for c in cls)
    text = f"p cnf {nv} {len(cls)}\n" + body
    with open(out, "x") as f:
        f.write(text)
    rec = {"matrix_file": mpath, "matrix_sha256": hashlib.sha256(open(mpath, "rb").read()).hexdigest(),
           "format": fmt, "n": n, "vars": nv, "clauses": len(cls),
           "cnf_sha256": hashlib.sha256(text.encode()).hexdigest(),
           "x(i,k)": "1 + i*n + k", "e(i)": "1 + n*n + i", "symmetry_breaking": "E0: e(0) false"}
    with open(out + ".map.json", "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print(json.dumps(rec))


if __name__ == "__main__":
    main()
