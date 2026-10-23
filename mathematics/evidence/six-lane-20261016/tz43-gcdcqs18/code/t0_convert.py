#!/usr/bin/env python3
"""README T0: format converters for calibration objects (standard library, exclusive writes).

gcdcqs IN OUT   old lane GCDCQS format (header 'GCDCQS v n g', empty stem) -> Format S
                ('GCDCQS v n g 0', 'STEM' line with no points); every other line copied verbatim.
fdh IN OUT      E10 FDH format ('FDH k m', POINT/CLASS j) -> Format D ('GDD34 FDGDD k m', POINT/FRAME j)
                where j is the group missed by the class (computed from the class's points; -1 if the class
                does not miss exactly one group other than the group of x — left for the checkers to reject)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import xopen  # noqa: E402


def gcdcqs(inp, out):
    L = open(inp).read().split("\n")
    o, done_head, done_stem = [], False, False
    for line in L:
        tok = line.split("#", 1)[0].split()
        if tok and tok[0] == "GCDCQS" and not done_head:
            assert len(tok) == 4, "expected old header 'GCDCQS v n g'"
            o.append(f"GCDCQS {tok[1]} {tok[2]} {tok[3]} 0")
            done_head = True
            continue
        if tok == ["BLOCKS"] and not done_stem:
            o.append("STEM")
            done_stem = True
        o.append(line)
    assert done_head and done_stem
    with xopen(out) as fh:
        fh.write("\n".join(o))


def fdh(inp, out):
    L = open(inp).read().split("\n")
    head = L[0].split()
    assert head[0] == "FDH"
    k, m = int(head[1]), int(head[2])
    groups = [[int(z) for z in L[2 + i].split()] for i in range(k)]
    gid = {p: i for i, G in enumerate(groups) for p in G}
    o = [f"GDD34 FDGDD {k} {m}"] + L[1:]
    # second pass: replace CLASS j lines by FRAME (missed group)
    res, x, i = [], None, 0
    while i < len(o):
        tok = o[i].split()
        if tok and tok[0] == "POINT":
            x = int(tok[1])
            res.append(o[i]); i += 1
        elif tok and tok[0] == "CLASS":
            j = i + 1
            pts = []
            while j < len(o) and o[j].split() and o[j].split()[0] not in ("CLASS", "POINT"):
                pts += [int(z) for z in o[j].split()]
                j += 1
            met = {gid[p] for p in pts}
            miss = set(range(k)) - met - {gid[x]}
            res.append(f"FRAME {miss.pop() if len(miss) == 1 else -1}")
            i += 1
        else:
            res.append(o[i]); i += 1
    with xopen(out) as fh:
        fh.write("\n".join(res))


if __name__ == "__main__":
    {"gcdcqs": gcdcqs, "fdh": fdh}[sys.argv[1]](sys.argv[2], sys.argv[3])
