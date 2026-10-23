#!/usr/bin/env python3
"""pc_expand.py -- expand a PC-T2-SEED (README 1.3) into a strict POINT-CYCLIC-RESOLUTION certificate.

Seed format (strict): "PC-T2-SEED v"; "H h0 h1 h2 h3" (a coset of <q>, q = v/4); (q-1)/4 lines "X a b c d";
(q-1)/12 lines "Y a b c d"; integers in [0, v), each line strictly ascending, single spaces, final newline.
The seed conditions (REDUCTION.md (S1)-(S3), with the short base block H allowed to be any coset of <q>) are checked
here directly in Z_v and reported; the expansion is the one of REDUCTION.md Theorem C:
  P0 = {H} u {X_i + h : h in <q>}, classes P0 + t (0 <= t < q);
  Q_j = {Y_j + 4m : 0 <= m < q}, classes Q_j + t (0 <= t < 4).
Blocks are sorted inside each class, classes are sorted by their sorted block lists and numbered 0, 1, ... in that
order, so the certificate bytes do not depend on the order of the seed lines.
Acceptance is NOT decided here: run pc_check.py on the output.
Usage: pc_expand.py SEED OUT
"""
import hashlib
import re
import sys

DEC = re.compile(r"0|[1-9][0-9]*")


def die(msg):
    print(f"SEED-FAIL {msg}")
    sys.exit(1)


def parse_seed(data):
    if not data.endswith(b"\n") or b"\r" in data:
        die("line ends")
    lines = data.decode("ascii").rstrip("\n").split("\n")
    head = lines[0].split(" ")
    if len(head) != 2 or head[0] != "PC-T2-SEED" or not DEC.fullmatch(head[1]):
        die("header")
    v = int(head[1])
    if v % 4 or (v // 4) % 2 == 0 or (v // 4) % 12 != 1:
        die("v must be 4q with q odd, q = 1 mod 12")
    q = v // 4
    a, c = (q - 1) // 4, (q - 1) // 12
    want = ["H"] + ["X"] * a + ["Y"] * c
    if len(lines) != 1 + len(want):
        die(f"expected {len(want)} block lines")
    blocks = []
    for ln, (line, tag) in enumerate(zip(lines[1:], want), start=2):
        toks = line.split(" ")
        if len(toks) != 5 or toks[0] != tag or not all(DEC.fullmatch(t) for t in toks[1:]):
            die(f"line {ln}")
        pts = [int(t) for t in toks[1:]]
        if not all(0 <= p < v for p in pts) or pts != sorted(set(pts)):
            die(f"line {ln}: range/order")
        blocks.append(pts)
    return v, q, blocks[0], blocks[1:1 + a], blocks[1 + a:]


def main(argv):
    if len(argv) != 3:
        print("usage: pc_expand.py SEED OUT", file=sys.stderr)
        return 2
    data = open(argv[1], "rb").read()
    v, q, H, X, Y = parse_seed(data)
    Hq = {0, q, 2 * q, 3 * q}
    # H is a coset of <q>
    if sorted(H) != sorted((H[0] + h) % v for h in Hq):
        die("H is not a coset of <q>")
    # (S1): ordered differences of X and Y blocks = Z_v \ <q>, each once
    diffs = [(x - y) % v for B in X + Y for x in B for y in B if x != y]
    if sorted(diffs) != sorted(set(range(v)) - Hq):
        die("(S1) differences are not Z_v minus <q> exactly once")
    # (S2): residues mod q of the X blocks, with res(H), partition Z_q
    res = [p % q for B in X for p in B]
    if any(len({p % q for p in B}) != 4 for B in X) or sorted(res + [H[0] % q]) != list(range(q)):
        die("(S2) residue partition")
    # (S3): each Y block meets every residue class mod 4 once
    if any(sorted(p % 4 for p in B) != [0, 1, 2, 3] for B in Y):
        die("(S3) transversal mod 4")
    print(f"seed sha256 {hashlib.sha256(data).hexdigest()}: (S1) (S2) (S3) hold; v={v} q={q} X={len(X)} Y={len(Y)}")

    def tr(B, d):
        return tuple(sorted((p + d) % v for p in B))

    P0 = [tuple(H)] + [tr(B, h) for B in X for h in sorted(Hq)]
    classes = [sorted(tr(B, t) for B in P0) for t in range(q)]
    for B in Y:
        Q = [tr(B, 4 * m) for m in range(q)]
        classes += [sorted(tr(C, t) for C in Q) for t in range(4)]
    classes.sort()
    out = [f"POINT-CYCLIC-RESOLUTION {v} 4 {len(classes)} {v // 4}"]
    for c, P in enumerate(classes):
        out += [f"{c} " + " ".join(map(str, B)) for B in P]
    text = ("\n".join(out) + "\n").encode("ascii")
    with open(argv[2], "wb") as f:
        f.write(text)
    print(f"wrote {argv[2]} sha256 {hashlib.sha256(text).hexdigest()} classes={len(classes)} lines={len(out) - 1}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
