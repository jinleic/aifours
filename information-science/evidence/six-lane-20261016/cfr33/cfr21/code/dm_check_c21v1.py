#!/usr/bin/env python3
"""(Z_G, K; 1) difference-matrix checker, dm-raw format (lane cfr33).

Usage: dm_check.py FILE K G
FILE: exactly K LF-terminated lines, each G single-space-separated canonical decimals in 0..G-1.
Definition: for every pair of rows i != j, the G differences D[i][t] - D[j][t] (mod G) are all distinct
(hence every element of Z_G occurs exactly once). Exit 0 with 'DM PASS' only on success.
"""
import hashlib, re, sys

TOK = re.compile(r"(0|[1-9][0-9]*)\Z")


def die(msg):
    print("DM FAIL: " + msg)
    sys.exit(1)


def main():
    path, K, G = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    raw = open(path, "rb").read()
    print("sha256 %s bytes %d" % (hashlib.sha256(raw).hexdigest(), len(raw)))
    try:
        text = raw.decode("ascii")
    except UnicodeDecodeError:
        die("not ASCII")
    if not text.endswith("\n") or "\r" in text:
        die("bad line endings")
    lines = text[:-1].split("\n")
    if len(lines) != K:
        die("rows %d != %d" % (len(lines), K))
    D = []
    for i, ln in enumerate(lines):
        toks = ln.split(" ")
        if len(toks) != G or not all(TOK.match(x) for x in toks):
            die("row %d malformed" % i)
        row = [int(x) for x in toks]
        if max(row) >= G:
            die("row %d entry out of range" % i)
        D.append(row)
    for i in range(K):
        for j in range(i + 1, K):
            diffs = [(D[i][t] - D[j][t]) % G for t in range(G)]
            if len(set(diffs)) != G:
                die("rows %d,%d: differences not all distinct" % (i, j))
    print("K %d G %d: all %d row pairs have differences forming a permutation of Z_%d" % (K, G, K * (K - 1) // 2, G))
    print("DM PASS")


if __name__ == "__main__":
    main()
