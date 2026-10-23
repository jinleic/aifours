#!/usr/bin/env python3
"""Enumerate all signed permutations H with H W H^T = W for a strict SW file (SAT + blocking clauses).

Usage: python3 -B code/symaut.py STRICT.sw OUTDIR [MAXSOL]
Each solver call gets the CNF (base clauses plus blocking clauses) on stdin (kissat --time=600), no CNF files;
results in OUTDIR/symaut.json (OUTDIR must not exist).
H e_j = s_j e_{pi(j)}; condition W[pi i][pi j] = s_i s_j W[i][j] for all i <= j.
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sw_common as C  # noqa: E402


def cycle_type(perm, sign):
    n = len(perm)
    seen = [False] * n
    out = []
    for i in range(n):
        if seen[i]:
            continue
        L, prod, j = 0, 1, i
        while not seen[j]:
            seen[j] = True
            prod *= sign[j]
            j = perm[j]
            L += 1
        out.append((L, prod))
    return sorted(out)


def order(perm, sign):
    n = len(perm)
    cp, cs = list(range(n)), [1] * n
    for k in range(1, 4 * n * n):
        cs = [cs[j] * sign[cp[j]] for j in range(n)]
        cp = [perm[cp[j]] for j in range(n)]
        if cp == list(range(n)) and all(x == 1 for x in cs):
            return k
    return None


def main():
    path, out = sys.argv[1], sys.argv[2]
    maxsol = int(sys.argv[3]) if len(sys.argv) > 3 else 100000
    n, w, W = C.read_strict(path)
    os.mkdir(out)
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
        for k in range(n):
            if W[k][k] != W[i][i]:
                cls.append([-x(i, k)])
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(n):
                for l in range(n):
                    if k == l:
                        continue
                    a, b = W[i][j], W[k][l]
                    if a == 0 and b == 0:
                        continue
                    if a == 0 or b == 0:
                        cls.append([-x(i, k), -x(j, l)])
                    elif a == b:
                        cls.append([-x(i, k), -x(j, l), -e(i), e(j)])
                        cls.append([-x(i, k), -x(j, l), e(i), -e(j)])
                    else:
                        cls.append([-x(i, k), -x(j, l), e(i), e(j)])
                        cls.append([-x(i, k), -x(j, l), -e(i), -e(j)])
    sols = []
    status = "MAXSOL"
    base = "".join(" ".join(map(str, c)) + " 0\n" for c in cls)
    blocks = []
    while len(sols) < maxsol:
        text = f"p cnf {nv} {len(cls) + len(blocks)}\n" + base + "".join(blocks)
        r = subprocess.run(["kissat", "--time=600", "-q"], input=text, capture_output=True, text=True)
        if r.returncode != 10:
            status = {20: "UNSAT", 0: "UNKNOWN"}.get(r.returncode, str(r.returncode))
            break
        tv = set()
        for line in r.stdout.splitlines():
            if line.startswith("v "):
                tv.update(int(t) for t in line.split()[1:] if int(t) > 0)
        perm = [next(k for k in range(n) if x(i, k) in tv) for i in range(n)]
        sign = [-1 if e(i) in tv else 1 for i in range(n)]
        ok = all(W[perm[i]][perm[j]] == sign[i] * sign[j] * W[i][j] for i in range(n) for j in range(n))
        sols.append({"perm": perm, "sign": sign, "verified": ok, "order": order(perm, sign),
                     "cycle_type": cycle_type(perm, sign)})
        blk = [-x(i, perm[i]) for i in range(n)] + [(e(i) if sign[i] == 1 else -e(i)) for i in range(n)]
        blocks.append(" ".join(map(str, blk)) + " 0\n")
    res = {"file": path, "n": n, "w": w, "group_order": len(sols), "final_status": status, "elements": sols}
    with open(os.path.join(out, "symaut.json"), "x") as f:
        json.dump(res, f)
        f.write("\n")
    from collections import Counter
    cnt = Counter((s["order"], str(s["cycle_type"])) for s in sols)
    print("group order", len(sols), "final", status, "all verified", all(s["verified"] for s in sols))
    for (o, ct), m in sorted(cnt.items()):
        print(o, m, ct)


if __name__ == "__main__":
    main()
