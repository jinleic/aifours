#!/usr/bin/env python3
"""pc_expand_general.py -- expand a PC-SEED (README 1.5) into a strict POINT-CYCLIC-RESOLUTION certificate.

Seed format (strict): line 1 "PC-SEED v"; line 2 "SHORT t"; then (t-1)/4 lines "X a b c d"; then, for each entry k
of K in nonincreasing order of k, a line "GROUP k" followed by k lines "Y a b c d". Integers are decimal without sign
or leading zeros, in [0, v), each block line strictly ascending, single spaces, final newline, nothing else.

Checked here directly in Z_v (GENERAL-REDUCTION.md Section 4), with n = v/4 and H = <n>:
  v = 4 (mod 12); t | n and t = 1 (mod 4); every k | n;
  (R1) the residue sets mod t of the X blocks are pairwise disjoint 4-sets with union Z_t \\ {0};
  (R2) for each group, the residue sets mod 4k of its Y blocks are pairwise disjoint 4-sets with union Z_{4k};
  (D)  the ordered differences of all X and Y blocks are exactly Z_v \\ H, each once.
The expansion is R(t, K, X, Y) of Theorem C':
  P_0 = {a + H : a in <t>} u {X_i + c : c in <t>}, classes P_0 + i (0 <= i < t);
  Q_j = {Y_{j,l} + c : c in <4k_j>},              classes Q_j + i (0 <= i < 4k_j).
Blocks are sorted inside each class and classes are sorted by their sorted block lists, so the certificate bytes do
not depend on the order of the seed lines. Acceptance is NOT decided here: run pc_check.py on the output.
Writes only the given output path and refuses to overwrite it; never deletes anything.
Usage: pc_expand_general.py SEED OUT
"""
import hashlib
import os
import re
import sys

DEC = re.compile(r"0|[1-9][0-9]*")


def die(msg):
    print(f"SEED-FAIL {msg}")
    sys.exit(1)


def parse_seed(data):
    if not data.endswith(b"\n") or b"\r" in data:
        die("line ends")
    try:
        lines = data.decode("ascii")[:-1].split("\n")
    except UnicodeDecodeError:
        die("non-ASCII")
    head = lines[0].split(" ")
    if len(head) != 2 or head[0] != "PC-SEED" or not DEC.fullmatch(head[1]):
        die("header")
    v = int(head[1])
    if v < 16 or v % 12 != 4:
        die("v must be 4 mod 12 and >= 16")
    n = v // 4
    if len(lines) < 2:
        die("missing SHORT line")
    sh = lines[1].split(" ")
    if len(sh) != 2 or sh[0] != "SHORT" or not DEC.fullmatch(sh[1]):
        die("SHORT line")
    t = int(sh[1])
    if t < 1 or n % t or t % 4 != 1:
        die("t must divide n and be 1 mod 4")

    def block(line, tag, ln):
        toks = line.split(" ")
        if len(toks) != 5 or toks[0] != tag or not all(DEC.fullmatch(x) for x in toks[1:]):
            die(f"line {ln}: expected '{tag} a b c d'")
        pts = [int(x) for x in toks[1:]]
        if not all(0 <= p < v for p in pts) or any(pts[i] >= pts[i + 1] for i in range(3)):
            die(f"line {ln}: points out of range or not strictly ascending")
        return pts

    pos = 2
    X = []
    for _ in range((t - 1) // 4):
        if pos >= len(lines):
            die("missing X lines")
        X.append(block(lines[pos], "X", pos + 1))
        pos += 1
    groups = []
    while pos < len(lines):
        g = lines[pos].split(" ")
        if len(g) != 2 or g[0] != "GROUP" or not DEC.fullmatch(g[1]) or int(g[1]) < 1:
            die(f"line {pos + 1}: expected 'GROUP k'")
        k = int(g[1])
        if n % k:
            die(f"line {pos + 1}: k = {k} does not divide n = {n}")
        if groups and k > groups[-1][0]:
            die(f"line {pos + 1}: groups not in nonincreasing order of k")
        pos += 1
        Y = []
        for _ in range(k):
            if pos >= len(lines):
                die("missing Y lines")
            Y.append(block(lines[pos], "Y", pos + 1))
            pos += 1
        groups.append((k, Y))
    return v, n, t, X, groups


def main(argv):
    if len(argv) != 3:
        print("usage: pc_expand_general.py SEED OUT", file=sys.stderr)
        return 2
    if os.path.exists(argv[2]):
        print(f"refusing to overwrite {argv[2]}", file=sys.stderr)
        return 2
    data = open(argv[1], "rb").read()
    v, n, t, X, groups = parse_seed(data)
    H = {0, n, 2 * n, 3 * n}
    # (R1)
    if any(len({p % t for p in B}) != 4 for B in X):
        die("(R1) an X block has repeated residues mod t")
    if sorted(p % t for B in X for p in B) != list(range(1, t)):
        die("(R1) residues mod t of the X blocks are not a partition of Z_t minus {0}")
    # (R2)
    for k, Y in groups:
        s = 4 * k
        if any(len({p % s for p in B}) != 4 for B in Y) or sorted(p % s for B in Y for p in B) != list(range(s)):
            die(f"(R2) group k = {k}: residues mod {s} are not a partition of Z_{s}")
    # (D)
    allb = X + [B for _, Y in groups for B in Y]
    diffs = sorted((a - b) % v for B in allb for a in B for b in B if a != b)
    if diffs != sorted(set(range(v)) - H):
        die("(D) ordered differences are not Z_v minus <n>, each once")
    # (E) is implied by (R1), (R2), (D); recorded for the report
    r = (v - 1) // 3
    if t + 4 * sum(k for k, _ in groups) != r:
        die("(E) class count mismatch (cannot happen when (R1), (R2), (D) hold)")
    seed_sha = hashlib.sha256(data).hexdigest()
    print(f"seed sha256 {seed_sha}: v={v} n={n} t={t} K={[k for k, _ in groups]} X={len(X)} "
          f"Y={sum(len(Y) for _, Y in groups)}: (R1) (R2) (D) (E) hold")

    def tr(B, d):
        return tuple(sorted((p + d) % v for p in B))

    sub_t = [c for c in range(v) if c % t == 0]
    P0 = [tuple(sorted({(a + h) % v for h in H})) for a in sub_t if a < n] + \
         [tr(B, c) for B in X for c in sub_t]
    # the short blocks of P0: cosets a + H with a in <t>; representatives a in <t>, 0 <= a < n
    classes = [sorted(tr(B, i) for B in P0) for i in range(t)]
    for k, Y in groups:
        s = 4 * k
        sub_s = [c for c in range(v) if c % s == 0]
        Q = [tr(B, c) for B in Y for c in sub_s]
        classes += [sorted(tr(B, i) for B in Q) for i in range(s)]
    classes.sort()
    if len(classes) != r or any(len(P) != n for P in classes):
        die("internal: class shape")
    out = [f"POINT-CYCLIC-RESOLUTION {v} 4 {r} {n}"]
    for c, P in enumerate(classes):
        out += [f"{c} " + " ".join(map(str, B)) for B in P]
    text = ("\n".join(out) + "\n").encode("ascii")
    with open(argv[2], "xb") as f:
        f.write(text)
    print(f"wrote {argv[2]} sha256 {hashlib.sha256(text).hexdigest()} classes={len(classes)} lines={len(out) - 1}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
