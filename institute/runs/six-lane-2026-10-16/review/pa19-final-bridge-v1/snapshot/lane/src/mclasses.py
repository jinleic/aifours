#!/usr/bin/env python3
"""Enumerate 0/1 matrices M (q x q) with row sums ra and column sums cb (both
non-increasing), up to permutations of rows inside equal-row-sum groups and of
columns inside equal-column-sum groups. Representative = lexicographically
smallest row-major flattening in the orbit (normalization step 2).
"""
import itertools
import json
import sys


def groups(sums):
    out, start = [], 0
    for i in range(1, len(sums) + 1):
        if i == len(sums) or sums[i] != sums[start]:
            out.append(list(range(start, i)))
            start = i
    return out


def all_matrices(ra, cb):
    q_r, q_c = len(ra), len(cb)
    rows_by_sum = {}
    for s in set(ra):
        rows_by_sum[s] = [t for t in itertools.product((0, 1), repeat=q_c) if sum(t) == s]
    res = []

    def rec(i, colrem, acc):
        if i == q_r:
            if all(c == 0 for c in colrem):
                res.append(tuple(acc))
            return
        remaining_rows = q_r - i
        for row in rows_by_sum[ra[i]]:
            ok = True
            new = []
            for j in range(q_c):
                v = colrem[j] - row[j]
                if v < 0 or v > remaining_rows - 1:
                    ok = False
                    break
                new.append(v)
            if ok:
                rec(i + 1, new, acc + [row])

    rec(0, list(cb), [])
    return res


def canonical(mat, rgroups, cperms):
    best = None
    for cp in cperms:
        rows = [tuple(r[j] for j in cp) for r in mat]
        out = []
        for g in rgroups:
            out.extend(sorted(rows[i] for i in g))
        t = tuple(out)
        if best is None or t < best:
            best = t
    return best


def column_perms(cb):
    gs = groups(cb)
    for choice in itertools.product(*[itertools.permutations(g) for g in gs]):
        perm = []
        for c in choice:
            perm.extend(c)
        yield perm


def classes(ra, cb):
    rg = groups(ra)
    cps = list(column_perms(cb))
    seen = {}
    for m in all_matrices(ra, cb):
        c = canonical(m, rg, cps)
        seen[c] = seen.get(c, 0) + 1
    return sorted(seen.items())


if __name__ == "__main__":
    ra = [int(x) for x in sys.argv[1].split(",")]
    cb = [int(x) for x in sys.argv[2].split(",")]
    cl = classes(ra, cb)
    print(json.dumps({"rows": ra, "cols": cb, "num_classes": len(cl),
                      "num_matrices": sum(n for _, n in cl)}))
