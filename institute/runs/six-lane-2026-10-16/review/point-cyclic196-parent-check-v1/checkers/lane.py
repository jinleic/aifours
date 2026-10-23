#!/usr/bin/env python3
"""pc_check.py -- direct checker for point-cyclic resolutions (lane point-cyclic100, README 1.3).

Reads a certificate in the strict format

    POINT-CYCLIC-RESOLUTION v k nclasses blocks_per_class
    c p_1 ... p_k            (nclasses * blocks_per_class lines)

(class index c in [0, nclasses), points strictly ascending in [0, v), lines in ascending (c, block) order, decimal
integers without sign or leading zeros, single spaces, LF line ends, final newline, nothing else) and checks,
directly from the listed blocks and without any base-block or difference-family structure:

  F  format as above;
  D1 b = v(v-1)/(k(k-1)) blocks, all pairwise distinct, each of k distinct points of Z_v;
  D2 every unordered pair of points lies in exactly one block (all v(v-1)/2 pairs counted);
  R1 nclasses = (v-1)/(k-1), blocks_per_class = v/k, every class is a partition of Z_v;
  R2 the classes partition the block set (each block listed once, in exactly one class);
  C1 x -> x+1 (mod v) maps the block set onto itself;
  C2 x -> x+1 maps every class onto a class.
Exit status 0 and final line "PASS" iff all checks hold; otherwise "FAIL <check>: <reason>" and exit 1.
Informational (not acceptance): blocks with nontrivial translation stabilizer, class stabilizer orders and class
orbit lengths, number of short blocks per class (the source's types T1/T2/T3).
Usage: pc_check.py CERT [--json OUT]
Stdlib only; written independently of pc_expand.py (no shared code).
"""
import hashlib
import json
import re
import sys

DEC = re.compile(r"0|[1-9][0-9]*\Z")


class Fail(Exception):
    pass


def need(cond, check, msg):
    if not cond:
        raise Fail(f"{check}: {msg}")


def parse(data):
    need(data.endswith(b"\n"), "F", "missing final newline")
    need(b"\r" not in data, "F", "CR character")
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError:
        raise Fail("F: non-ASCII byte")
    lines = text[:-1].split("\n")
    head = lines[0].split(" ")
    need(len(head) == 5 and head[0] == "POINT-CYCLIC-RESOLUTION", "F", "bad header line")
    for tok in head[1:]:
        need(DEC.fullmatch(tok) is not None, "F", f"bad header integer {tok!r}")
    v, k, ncl, bpc = (int(t) for t in head[1:])
    need(v >= 2 and k >= 2, "F", "v, k too small")
    body = lines[1:]
    need(len(body) == ncl * bpc, "F", f"expected {ncl * bpc} block lines, found {len(body)}")
    rows = []
    for ln, line in enumerate(body, start=2):
        toks = line.split(" ")
        need(len(toks) == k + 1, "F", f"line {ln}: expected {k + 1} fields")
        for tok in toks:
            need(DEC.fullmatch(tok) is not None, "F", f"line {ln}: bad integer {tok!r}")
        c = int(toks[0])
        pts = tuple(int(t) for t in toks[1:])
        need(0 <= c < ncl, "F", f"line {ln}: class index {c} out of range")
        need(all(0 <= p < v for p in pts), "F", f"line {ln}: point out of range")
        need(all(pts[i] < pts[i + 1] for i in range(k - 1)), "F", f"line {ln}: points not strictly ascending")
        rows.append((c, pts))
    need(all(rows[i] < rows[i + 1] for i in range(len(rows) - 1)), "F",
         "lines not in strictly ascending (class, block) order")
    return v, k, ncl, bpc, rows


def shift(block, d, v):
    return tuple(sorted((p + d) % v for p in block))


def check(data):
    v, k, ncl, bpc, rows = parse(data)
    info = {"v": v, "k": k, "nclasses": ncl, "blocks_per_class": bpc}
    # D1
    need(v * (v - 1) % (k * (k - 1)) == 0, "D1", "k(k-1) does not divide v(v-1)")
    b = v * (v - 1) // (k * (k - 1))
    need(len(rows) == b, "D1", f"{len(rows)} blocks, expected {b}")
    blocks = [pts for _, pts in rows]
    bset = set(blocks)
    need(len(bset) == b, "D1", f"{b - len(bset)} repeated block(s)")
    # D2
    cnt = [[0] * v for _ in range(v)]
    for B in blocks:
        for i in range(k):
            for j in range(i + 1, k):
                cnt[B[i]][B[j]] += 1
    bad = [(x, y, cnt[x][y]) for x in range(v) for y in range(x + 1, v) if cnt[x][y] != 1]
    need(not bad, "D2", f"{len(bad)} pair(s) not covered exactly once, e.g. {bad[:3]}")
    info["pairs_checked"] = v * (v - 1) // 2
    # R1, R2
    need((v - 1) % (k - 1) == 0 and ncl == (v - 1) // (k - 1), "R1", f"nclasses {ncl} != (v-1)/(k-1)")
    need(v % k == 0 and bpc == v // k, "R1", f"blocks_per_class {bpc} != v/k")
    classes = [[] for _ in range(ncl)]
    for c, pts in rows:
        classes[c].append(pts)
    for c, P in enumerate(classes):
        need(len(P) == bpc, "R1", f"class {c} has {len(P)} blocks")
        seen = sorted(p for B in P for p in B)
        need(seen == list(range(v)), "R1", f"class {c} is not a partition of Z_{v}")
    # every block is on exactly one line (distinctness, D1) and every line has one class index: R2
    info["R2"] = "each of the b distinct blocks is listed exactly once, with one class index"
    # C1
    need({shift(B, 1, v) for B in blocks} == bset, "C1", "block set not invariant under x -> x+1")
    # C2
    cls_sets = [frozenset(P) for P in classes]
    index = {P: c for c, P in enumerate(cls_sets)}
    need(len(index) == ncl, "C2", "two classes coincide")
    image = []
    for c, P in enumerate(cls_sets):
        Q = frozenset(shift(B, 1, v) for B in P)
        need(Q in index, "C2", f"class {c} + 1 is not a class")
        image.append(index[Q])
    need(sorted(image) == list(range(ncl)), "C2", "x -> x+1 does not permute the classes")
    # informational orbit data
    def stab_order(blockset_or_block, is_class):
        n = 0
        for d in range(v):
            if is_class:
                if frozenset(shift(B, d, v) for B in blockset_or_block) == blockset_or_block:
                    n += 1
            else:
                if shift(blockset_or_block, d, v) == blockset_or_block:
                    n += 1
        return n
    short = [B for B in blocks if stab_order(B, False) > 1]
    info["short_blocks"] = len(short)
    info["short_block_stabilizer_orders"] = sorted({stab_order(B, False) for B in short})
    shortset = set(short)
    seen_c = set()
    orbits = []
    for c in range(ncl):
        if c in seen_c:
            continue
        orb = [c]
        seen_c.add(c)
        x = image[c]
        while x != c:
            orb.append(x)
            seen_c.add(x)
            x = image[x]
        P = cls_sets[c]
        orbits.append({"length": len(orb), "stabilizer_order": stab_order(P, True),
                       "short_blocks_per_class": sum(1 for B in P if B in shortset)})
    info["class_orbits"] = sorted(orbits, key=lambda o: (o["length"], o["short_blocks_per_class"]))
    m = [o["short_blocks_per_class"] for o in orbits if o["short_blocks_per_class"] > 0]
    if len(short) == v // k and len(m) == 1:
        info["type"] = {1: "T2", v // k: "T1"}.get(m[0], "T3")
    return info


def main(argv):
    if len(argv) not in (2, 4) or (len(argv) == 4 and argv[2] != "--json"):
        print("usage: pc_check.py CERT [--json OUT]", file=sys.stderr)
        return 2
    data = open(argv[1], "rb").read()
    res = {"certificate": argv[1], "sha256": hashlib.sha256(data).hexdigest(),
           "checker_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()}
    try:
        info = check(data)
        res.update(info)
        res["verdict"] = "PASS"
        out = 0
    except Fail as e:
        res["verdict"] = f"FAIL {e}"
        out = 1
    for key in sorted(res):
        if key != "verdict":
            print(f"{key}: {res[key]}")
    print(res["verdict"])
    if len(argv) == 4:
        with open(argv[3], "w") as f:
            json.dump(res, f, indent=1, sort_keys=True)
            f.write("\n")
    return out


if __name__ == "__main__":
    sys.exit(main(sys.argv))
