#!/usr/bin/env python3
"""README B2: weighting (Lemma W) of a Format D certificate by an odd t (standard library, exclusive writes).

Input: FDGDD(3,4,k{m}) or RDGDD(3,4,k{m}) in Format D (its classes are used as given; the output is checked
independently).  Output: the same kind with group size m*t on X x Z_t.  Point (p, beta) with p the a-th point
of group i (GROUPS order) gets label m*t*i + t*a + beta; group i of the output is G_i x Z_t.
Blocks: for every input block B = {b1, b2, b3, b4}, all {(b, beta_b)} with sum of beta_b = 0 (mod t).
Classes at (x, alpha): for every input class P at x and c in Z_t,
  P^c = {{(y1, beta), (y2, beta + c), (y3, -alpha - 2 beta - c)} : {y1 < y2 < y3} in P, beta in Z_t}
(label FRAME y as for P, or PC j*t + c).  Usage: weight_gdd.py IN.txt T OUT.txt"""
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import xopen  # noqa: E402


def read(path):
    L = [l.split("#", 1)[0].split() for l in open(path)]
    L = [l for l in L if l]
    kind, k, m = L[0][1], int(L[0][2]), int(L[0][3])
    groups = [[int(z) for z in L[2 + i]] for i in range(k)]
    assert L[2 + k] == ["BLOCKS"]
    pos, blocks = 3 + k, []
    while pos < len(L) and L[pos][0] != "POINT":
        blocks.append(tuple(int(z) for z in L[pos]))
        pos += 1
    sec, cur = {}, None
    for tok in L[pos:]:
        if tok[0] == "POINT":
            cur = int(tok[1])
            sec[cur] = []
        elif tok[0] in ("FRAME", "PC"):
            sec[cur].append((tok[0], int(tok[1]), []))
        else:
            sec[cur][-1][2].append(tuple(int(z) for z in tok))
    return kind, k, m, groups, blocks, sec


def main():
    inp, t, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    assert t % 2 == 1 and t >= 1
    kind, k, m, groups, blocks, sec = read(inp)
    M = m * t
    pos = {p: (i, a) for i, G in enumerate(groups) for a, p in enumerate(G)}
    lab = lambda p, beta: M * pos[p][0] + t * pos[p][1] + beta % t  # noqa: E731
    nb = set()
    for B in blocks:
        b = sorted(B)
        for b1 in range(t):
            for b2 in range(t):
                for b3 in range(t):
                    b4 = (-(b1 + b2 + b3)) % t
                    nb.add(tuple(sorted((lab(b[0], b1), lab(b[1], b2), lab(b[2], b3), lab(b[3], b4)))))
    assert len(nb) == len(blocks) * t ** 3
    lines = [f"GDD34 {kind} {k} {M}", "GROUPS"] + [" ".join(str(M * i + j) for j in range(M)) for i in range(k)]
    lines += ["BLOCKS"] + [" ".join(map(str, b)) for b in sorted(nb)]
    newsec = {}
    for x, classes in sec.items():
        for alpha in range(t):
            X = lab(x, alpha)
            out_cl = []
            for kw, j, P in classes:
                for c in range(t):
                    tri = []
                    for T in P:
                        y1, y2, y3 = sorted(T)
                        for beta in range(t):
                            tri.append(tuple(sorted((lab(y1, beta), lab(y2, beta + c), lab(y3, -alpha - 2 * beta - c)))))
                    out_cl.append((kw, j if kw == "FRAME" else j * t + c, sorted(tri)))
            if out_cl and out_cl[0][0] == "PC":
                out_cl.sort(key=lambda z: z[1])
            newsec[X] = out_cl
    for X in sorted(newsec):
        lines.append(f"POINT {X}")
        for kw, j, tri in newsec[X]:
            lines.append(f"{kw} {j}")
            lines += [" ".join(map(str, tr)) for tr in tri]
    text = "\n".join(lines) + "\n"
    with xopen(out) as fh:
        fh.write(text)
    print(out, "sha256", hashlib.sha256(text.encode()).hexdigest(), "points", k * M, "blocks", len(nb))


if __name__ == "__main__":
    main()
