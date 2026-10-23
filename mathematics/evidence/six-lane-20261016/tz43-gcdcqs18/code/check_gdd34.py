#!/usr/bin/env python3
"""Route-1 definition-first checker for Format D certificates (README §3): FDGDD(3,4,k{m}) or
RDGDD(3,4,k{m}) (Tan–Zhou LF 237–247) — standard library only, NO symmetry assumed.

Checks (first failure reported with a category prefix):
  FORMAT        header 'GDD34 FDGDD|RDGDD k m', GROUPS (k lines of m points), BLOCKS, POINT sections with
                FRAME j (FDGDD) or PC j (RDGDD, j = 0,1,... in order) classes of triples
  PARTITION     groups partition {0..km-1}
  BLOCK         4 distinct in-range points meeting 4 distinct groups; no repeated block
  COVERAGE      every 3-subset meeting three distinct groups lies in exactly one block (explicit loop)
  COMPLETENESS  exactly one POINT section for every point
  CLASS         at x: every class nonempty, triples T with T ∪ {x} a block, pairwise disjoint, covering
                exactly X∖(G_x ∪ G_j) (FDGDD, j ≠ group of x) or X∖G_x (RDGDD); every derived triple at x
                in exactly one class
Exit 0 and a JSON line with "result": "PASS", or exit 1 with "result": "FAIL" and the failure."""
import hashlib
import json
import sys
from itertools import combinations


class Fail(Exception):
    pass


def ints(tok, ln):
    try:
        return [int(z) for z in tok]
    except ValueError:
        raise Fail(f"FORMAT: line {ln}: non-integer token")


def parse(text):
    lines = []
    for ln, raw in enumerate(text.split("\n"), 1):
        s = raw.split("#", 1)[0].split()
        if s:
            lines.append((ln, s))
    if not lines or lines[0][1][0] != "GDD34" or len(lines[0][1]) != 4 or lines[0][1][1] not in ("FDGDD", "RDGDD"):
        raise Fail("FORMAT: expected 'GDD34 FDGDD|RDGDD k m' on the first line")
    kind = lines[0][1][1]
    k, m = ints(lines[0][1][2:], lines[0][0])
    if len(lines) < 2 or lines[1][1] != ["GROUPS"]:
        raise Fail("FORMAT: expected 'GROUPS'")
    groups = []
    for i in range(k):
        ln, tok = lines[2 + i]
        if len(tok) != m:
            raise Fail(f"FORMAT: line {ln}: group line does not have {m} points")
        groups.append(ints(tok, ln))
    pos = 2 + k
    if lines[pos][1] != ["BLOCKS"]:
        raise Fail(f"FORMAT: line {lines[pos][0]}: expected 'BLOCKS'")
    pos += 1
    blocks = []
    while pos < len(lines) and lines[pos][1][0] != "POINT":
        ln, tok = lines[pos]
        if len(tok) != 4:
            raise Fail(f"FORMAT: line {ln}: block line does not have 4 entries")
        blocks.append((ints(tok, ln), ln))
        pos += 1
    sections, cur = {}, None
    clkw = "FRAME" if kind == "FDGDD" else "PC"
    while pos < len(lines):
        ln, tok = lines[pos]
        pos += 1
        if tok[0] == "POINT":
            if len(tok) != 2:
                raise Fail(f"FORMAT: line {ln}: bad POINT line")
            (x,) = ints(tok[1:], ln)
            if x in sections:
                raise Fail(f"COMPLETENESS: POINT {x} appears twice (line {ln})")
            sections[x], cur = [], x
        elif tok[0] in ("FRAME", "PC"):
            if tok[0] != clkw or cur is None or len(tok) != 2:
                raise Fail(f"FORMAT: line {ln}: class keyword must be {clkw} inside a POINT section")
            (j,) = ints(tok[1:], ln)
            if kind == "RDGDD" and j != len(sections[cur]):
                raise Fail(f"FORMAT: line {ln}: POINT {cur}: PC id {j} out of order")
            sections[cur].append((j, ln, []))
        else:
            if len(tok) != 3 or cur is None or not sections[cur]:
                raise Fail(f"FORMAT: line {ln}: triple line outside a class or not 3 entries")
            sections[cur][-1][2].append((ints(tok, ln), ln))
    return kind, k, m, groups, blocks, sections


def check(kind, k, m, groups, blocks, sections):
    v = k * m
    if sorted(p for G in groups for p in G) != list(range(v)):
        raise Fail("PARTITION: groups do not partition {0..km-1}")
    gid = {p: i for i, G in enumerate(groups) for p in G}
    bset = set()
    for b, ln in blocks:
        if len(set(b)) != 4 or any(p < 0 or p >= v for p in b):
            raise Fail(f"BLOCK: line {ln}: not 4 distinct points of 0..{v - 1}")
        if len({gid[p] for p in b}) != 4:
            raise Fail(f"BLOCK: line {ln}: block meets a group twice")
        fb = frozenset(b)
        if fb in bset:
            raise Fail(f"BLOCK: line {ln}: repeated block")
        bset.add(fb)
    cover = {}
    for fb in bset:
        for tr in combinations(sorted(fb), 3):
            cover[tr] = cover.get(tr, 0) + 1
    ncov = 0
    for tr in combinations(range(v), 3):
        if len({gid[p] for p in tr}) == 3:
            c = cover.get(tr, 0)
            if c != 1:
                raise Fail(f"COVERAGE: transverse triple {tr} lies in {c} blocks")
            ncov += 1
    if sorted(sections) != list(range(v)):
        raise Fail("COMPLETENESS: POINT sections missing or out of range")
    ncls = set()
    for x in range(v):
        der = {frozenset(b - {x}) for b in bset if x in b}
        listed = set()
        for j, ln, C in sections[x]:
            if kind == "FDGDD":
                if not (0 <= j < k) or j == gid[x]:
                    raise Fail(f"CLASS: line {ln}: FRAME index {j} invalid at POINT {x}")
                target = set(range(v)) - set(groups[gid[x]]) - set(groups[j])
            else:
                target = set(range(v)) - set(groups[gid[x]])
            if not C:
                raise Fail(f"CLASS: line {ln}: empty class")
            used = set()
            for tr, tln in C:
                if len(set(tr)) != 3 or any(p < 0 or p >= v for p in tr):
                    raise Fail(f"CLASS: line {tln}: triple not 3 distinct points")
                if used & set(tr):
                    raise Fail(f"CLASS: POINT {x} line {tln}: triples of a class not disjoint")
                used |= set(tr)
                ft = frozenset(tr)
                if ft not in der:
                    raise Fail(f"CLASS: line {tln}: triple ∪ {{{x}}} is not a block")
                if ft in listed:
                    raise Fail(f"CLASS: POINT {x} line {tln}: triple listed twice")
                listed.add(ft)
            if used != target:
                raise Fail(f"CLASS: POINT {x} class at line {ln}: not a parallel class of the required point set")
        if listed != der:
            raise Fail(f"CLASS: POINT {x}: classes do not cover the derived design")
        ncls.add(len(sections[x]))
    return {"kind": kind, "groups": k, "group_size": m, "points": v, "blocks": len(bset),
            "transverse_triples": ncov, "classes_per_point": sorted(ncls)}


def main(argv):
    if len(argv) != 2:
        print("usage: check_gdd34.py CERT", file=sys.stderr)
        return 2
    data = open(argv[1], "rb").read()
    rec = {"certificate": argv[1], "sha256": hashlib.sha256(data).hexdigest(),
           "checker": "check_gdd34.py (route 1, stdlib, definition-based)"}
    try:
        rec.update(check(*parse(data.decode())))
        rec["result"] = "PASS"
        print(json.dumps(rec))
        return 0
    except Fail as e:
        rec["result"] = "FAIL"
        rec["failure"] = str(e)
        print(json.dumps(rec))
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
