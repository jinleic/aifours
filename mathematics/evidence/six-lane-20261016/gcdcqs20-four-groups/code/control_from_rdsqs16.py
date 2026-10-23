#!/usr/bin/env python3
"""C0a positive control: gcDCQS(4^4 : 0) from a known RDSQS(16) (standard library + guard).

Reads an RDSQS certificate (format of ../../rdsqs52/code/check_rdsqs.py), finds the
lexicographically first set of four pairwise disjoint blocks covering all 16 points, uses them as
the groups, deletes them from the block set, and at every point x deletes the hole triple
G(x)∖{x} from the class of the given resolution that contains it (class order kept).  Writes a
GCDCQS certificate (exclusive create).  Usage: control_from_rdsqs16.py RDSQS16_CERT OUT
"""
import lane_guard  # noqa: F401

import hashlib
import sys

from lane_guard import xopen


def read_rdsqs(path):
    v, blocks, res, cur = None, [], {}, None
    for raw in open(path):
        s = raw.split("#")[0].strip()
        if not s:
            continue
        t = s.split()
        if t[0] == "RDSQS":
            v = int(t[1])
        elif t[0] == "BLOCKS":
            continue
        elif t[0] == "POINT":
            cur = int(t[1]); res[cur] = []
        elif t[0] == "CLASS":
            res[cur].append([])
        elif cur is None:
            blocks.append(tuple(sorted(int(x) for x in t)))
        else:
            res[cur][-1].append(tuple(sorted(int(x) for x in t)))
    return v, blocks, res


def first_parallel_class(v, blocks):
    bs = sorted(blocks)

    def rec(left, chosen):
        if not left:
            return chosen
        p = min(left)
        for b in bs:
            if p in b and set(b) <= left:
                out = rec(left - set(b), chosen + [b])
                if out:
                    return out
        return None

    return rec(set(range(v)), [])


def main(src, out):
    v, blocks, res = read_rdsqs(src)
    assert v == 16 and len(blocks) == 140
    groups = first_parallel_class(v, blocks)
    assert groups and len(groups) == 4
    gset = set(groups)
    rest = sorted(b for b in blocks if b not in gset)
    group_of = {p: i for i, G in enumerate(groups) for p in G}
    lines = [f"# control C0a: gcDCQS(4^4:0) from RDSQS(16) {src} (sha256 "
             f"{hashlib.sha256(open(src, 'rb').read()).hexdigest()}); groups = first parallel class of blocks",
             "GCDCQS 16 4 4", "COLOURS 7", "HOLEFREE 1", "GROUPS"]
    lines += [" ".join(map(str, G)) for G in groups]
    lines.append("BLOCKS")
    lines += [" ".join(map(str, b)) for b in rest]
    for x in range(v):
        hole_triple = tuple(sorted(p for p in groups[group_of[x]] if p != x))
        lines.append(f"POINT {x}")
        removed = 0
        for j, C in enumerate(res[x]):
            lines.append(f"CLASS {j}")
            for t in C:
                if t == hole_triple:
                    removed += 1
                    continue
                lines.append(" ".join(map(str, t)))
        assert removed == 1
    data = ("\n".join(lines) + "\n").encode()
    with xopen(out, "xb") as f:
        f.write(data)
    print("groups", groups, "blocks", len(rest), "sha256", hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
