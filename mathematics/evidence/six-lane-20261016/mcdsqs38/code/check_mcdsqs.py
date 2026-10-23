#!/usr/bin/env python3
"""Direct, definition-based checker for an mcDSQS(v) certificate (standard library only).

Assumes NO symmetry.  Certificate format (plain text; '#' starts a comment; blank lines
ignored):

    MCDSQS v
    COLOURS r
    BLOCKS
    a b c d            (one 4-subset per line, points 0..v-1)
    ...
    POINT x            (one section for every x in 0..v-1)
    CLASS j            (j = 0..r-1 in this order, each exactly once per POINT)
    a b c              (triples of the derived design at x)
    ...

Checks (the first failure is reported with a category prefix):
  FORMAT        malformed lines / sections / ids
  BLOCK         v ≡ 2, 4 (mod 6), v >= 4; block count v(v-1)(v-2)/24; 4 distinct in-range
                points per block; no repeated block
  COVERAGE      every 3-subset of X lies in exactly one block (explicit equality with the
                set of all C(v,3) triples)
  COLOURS       r = χ′(v-1) from Tan–Zhou (1.1); r >= ceil(#derived triples / floor((v-1)/3))
  COMPLETENESS  a POINT section for every x (none twice / out of range)
  COLOURING     for every x: exactly r classes (ids 0..r-1), each nonempty; every triple has 3
                distinct in-range points avoiding x; triples of one class pairwise
                point-disjoint (partial parallel class); every listed triple T has T∪{x} a
                block; no triple listed twice at x; the listed triples are exactly the derived
                design {b∖{x} : x∈b∈B}
Exit 0 with a JSON receipt on PASS, 1 with the failure on FAIL.
"""
import hashlib
import json
import sys
from itertools import combinations


class Fail(Exception):
    pass


def chi_index(w):
    if w % 6 == 3:
        return (w - 1) // 2
    if w % 6 == 1:
        return {7: 7, 13: 8}.get(w, (w + 1) // 2)
    raise Fail(f"COLOURS: {w} is not an STS order")


def ints(tok, ln):
    try:
        return [int(x) for x in tok]
    except ValueError:
        raise Fail(f"FORMAT: non-integer token on line {ln}")


def parse(text):
    v = r = None
    blocks = []
    points = {}            # x -> list of classes (list of triples)
    state = "head"
    cur = None
    for ln, raw in enumerate(text.splitlines(), 1):
        s = raw.split("#", 1)[0].strip()
        if not s:
            continue
        tok = s.split()
        if state == "head":
            if tok[0] != "MCDSQS" or len(tok) != 2:
                raise Fail(f"FORMAT: expected 'MCDSQS v' on line {ln}")
            v = ints(tok[1:], ln)[0]
            state = "colours"
        elif state == "colours":
            if tok[0] != "COLOURS" or len(tok) != 2:
                raise Fail(f"FORMAT: expected 'COLOURS r' on line {ln}")
            r = ints(tok[1:], ln)[0]
            state = "blocks_kw"
        elif state == "blocks_kw":
            if tok != ["BLOCKS"]:
                raise Fail(f"FORMAT: expected 'BLOCKS' on line {ln}")
            state = "blocks"
        elif state == "blocks" and tok[0] not in ("POINT", "CLASS"):
            if len(tok) != 4:
                raise Fail(f"FORMAT: block line {ln} does not have 4 entries")
            blocks.append((ints(tok, ln), ln))
        else:
            if tok[0] == "POINT":
                if len(tok) != 2:
                    raise Fail(f"FORMAT: bad POINT line {ln}")
                x = ints(tok[1:], ln)[0]
                if x in points:
                    raise Fail(f"COMPLETENESS: POINT {x} appears twice (line {ln})")
                points[x] = []
                cur = x
                state = "point"
            elif tok[0] == "CLASS":
                if cur is None or len(tok) != 2:
                    raise Fail(f"FORMAT: CLASS outside POINT or malformed (line {ln})")
                j = ints(tok[1:], ln)[0]
                if j != len(points[cur]):
                    raise Fail(f"FORMAT: POINT {cur}: class id {j} out of order (line {ln})")
                points[cur].append([])
            else:
                if state != "point" or not points[cur]:
                    raise Fail(f"FORMAT: triple outside a CLASS (line {ln})")
                if len(tok) != 3:
                    raise Fail(f"FORMAT: triple line {ln} does not have 3 entries")
                points[cur][-1].append((ints(tok, ln), ln))
    if v is None or r is None:
        raise Fail("FORMAT: missing header")
    return v, r, blocks, points


def check(v, r, blocks, points):
    if v < 4 or v % 6 not in (2, 4):
        raise Fail(f"BLOCK: v={v} is not ≡ 2, 4 (mod 6)")
    nb = v * (v - 1) * (v - 2) // 24
    if len(blocks) != nb:
        raise Fail(f"BLOCK: {len(blocks)} blocks, expected {nb}")
    bset = set()
    for b, ln in blocks:
        if len(set(b)) != 4 or any(p < 0 or p >= v for p in b):
            raise Fail(f"BLOCK: line {ln}: points not 4 distinct in 0..{v-1}")
        fb = frozenset(b)
        if fb in bset:
            raise Fail(f"BLOCK: line {ln}: repeated block")
        bset.add(fb)
    count = {}
    for fb in bset:
        for t in combinations(sorted(fb), 3):
            count[t] = count.get(t, 0) + 1
    alltrip = set(combinations(range(v), 3))
    if set(count) != alltrip:
        raise Fail("COVERAGE: some 3-subset lies in no block")
    if any(c != 1 for c in count.values()):
        raise Fail("COVERAGE: some 3-subset lies in two blocks")
    w = v - 1
    if r != chi_index(w):
        raise Fail(f"COLOURS: r={r} differs from chi'({w})={chi_index(w)}")
    nder = w * (w - 1) // 6
    cap = w // 3
    if r * cap < nder:
        raise Fail("COLOURS: r classes of at most floor((v-1)/3) triples cannot hold the derived design")
    if sorted(points) != list(range(v)):
        raise Fail(f"COMPLETENESS: POINT sections {sorted(set(range(v)) - set(points))} missing "
                   f"or out of range")
    sizes = {}
    for x in range(v):
        classes = points[x]
        if len(classes) != r:
            raise Fail(f"COLOURING: POINT {x} has {len(classes)} classes, expected {r}")
        listed = set()
        for j, C in enumerate(classes):
            if not C:
                raise Fail(f"COLOURING: POINT {x} class {j} is empty")
            used = set()
            for t, ln in C:
                if len(set(t)) != 3 or any(p < 0 or p >= v for p in t) or x in t:
                    raise Fail(f"COLOURING: line {ln}: triple not 3 distinct points of X\\{{{x}}}")
                if used & set(t):
                    raise Fail(f"COLOURING: POINT {x} class {j} line {ln}: triples not disjoint")
                used |= set(t)
                if frozenset(t + [x]) not in bset:
                    raise Fail(f"COLOURING: line {ln}: triple ∪ {{{x}}} is not a block")
                ft = frozenset(t)
                if ft in listed:
                    raise Fail(f"COLOURING: POINT {x} line {ln}: triple listed twice")
                listed.add(ft)
            sizes.setdefault(x, []).append(len(C))
        der = {frozenset(b - {x}) for b in bset if x in b}
        if listed != der or len(der) != nder:
            raise Fail(f"COLOURING: POINT {x}: listed triples are not the derived design")
    profile = sorted({tuple(sorted(s, reverse=True)) for s in sizes.values()})
    return {"v": v, "blocks": nb, "triples_covered": len(alltrip), "points": v, "colours": r,
            "derived_triples_per_point": nder, "class_size_profiles": [list(p) for p in profile]}


def main(argv):
    if len(argv) != 2:
        print("usage: check_mcdsqs.py CERT", file=sys.stderr)
        return 2
    data = open(argv[1], "rb").read()
    rec = {"certificate": argv[1], "sha256": hashlib.sha256(data).hexdigest(),
           "checker": "check_mcdsqs.py (stdlib, definition-based)"}
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
