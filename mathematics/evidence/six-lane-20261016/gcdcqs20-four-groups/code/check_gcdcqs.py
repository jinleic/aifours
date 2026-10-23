#!/usr/bin/env python3
"""Definition-first checker for a gcDCQS(g^n : 0) certificate (standard library only; assumes
NO symmetry).  Definitions: Tan–Zhou arXiv:2503.11934v1 lines 211–220 (gcSTS), 256–266
(candelabra system), 281–288 (gcDCQS); chi' from (1.1).

Format ('#' starts a comment; blank lines ignored):
    GCDCQS v n g          (v = n*g points 0..v-1, stem empty)
    COLOURS r
    HOLEFREE s
    GROUPS                (then n lines with g points each)
    BLOCKS                (then one 4-subset per line)
    POINT x               (one section for every x)
    CLASS j               (j = 0..r-1 in order, each exactly once per POINT)
    a b c                 (triples of the derived design at x)

Checks (first failure reported with a category prefix):
  FORMAT        malformed lines, sections, ids
  PARAMS        v = n*g, n >= 3, w = v-1 and h = g-1 admissible STS orders (≡ 1,3 mod 6);
                r == chi'(w) (Tan–Zhou (1.1)) and s == r - (w-h)/2 (gcSTS definition)
  GROUPS        n disjoint groups of size g covering all points (empty stem)
  BLOCK         4 distinct in-range points; no three points in one group; no repeated block;
                block count (C(v,3) - n*C(g,3))/4
  COVERAGE      every 3-subset not inside a group lies in exactly one block (explicit equality
                with that triple universe); no 3-subset of a group lies in a block
  COMPLETENESS  a POINT section for every x (none twice / out of range)
  COLOURING     at every x: exactly r nonempty classes; triples of 3 distinct in-range points
                avoiding x; triples of one class pairwise disjoint (partial parallel class of
                X minus x); each listed triple T has T ∪ {x} a block; no triple listed twice;
                listed triples = derived design {B - {x}: x in B}; exactly s classes contain no
                point of the hole G(x) - {x}
Exit 0 with a JSON receipt on PASS, 1 with the failure on FAIL.
"""
import hashlib
import json
import sys
from itertools import combinations


class Fail(Exception):
    pass


def chi(w):
    if w % 6 == 3:
        return (w - 1) // 2
    if w % 6 == 1:
        return {7: 7, 13: 8}.get(w, (w + 1) // 2)
    raise Fail(f"PARAMS: {w} is not an STS order")


def ints(tok, ln):
    try:
        return [int(x) for x in tok]
    except ValueError:
        raise Fail(f"FORMAT: non-integer token on line {ln}")


def parse(text):
    head = {}
    groups, blocks, points = [], [], {}
    state, cur = "head", None
    expect = ["GCDCQS", "COLOURS", "HOLEFREE", "GROUPS"]
    for ln, raw in enumerate(text.splitlines(), 1):
        s = raw.split("#", 1)[0].strip()
        if not s:
            continue
        tok = s.split()
        if state == "head":
            want = expect[len(head)]
            if tok[0] != want:
                raise Fail(f"FORMAT: expected '{want}' on line {ln}")
            if want == "GCDCQS":
                if len(tok) != 4:
                    raise Fail(f"FORMAT: 'GCDCQS v n g' expected on line {ln}")
                head[want] = ints(tok[1:], ln)
            elif want in ("COLOURS", "HOLEFREE"):
                if len(tok) != 2:
                    raise Fail(f"FORMAT: '{want} k' expected on line {ln}")
                head[want] = ints(tok[1:], ln)[0]
            else:
                if len(tok) != 1:
                    raise Fail(f"FORMAT: bare 'GROUPS' expected on line {ln}")
                head[want] = True
                state = "groups"
            continue
        if state == "groups":
            if tok == ["BLOCKS"]:
                state = "blocks"
                continue
            groups.append((ints(tok, ln), ln))
            continue
        if state == "blocks" and tok[0] not in ("POINT", "CLASS"):
            if len(tok) != 4:
                raise Fail(f"FORMAT: block line {ln} does not have 4 entries")
            blocks.append((ints(tok, ln), ln))
            continue
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
    if len(head) != 4:
        raise Fail("FORMAT: incomplete header")
    return head, groups, blocks, points


def check(head, groups, blocks, points):
    v, n, g = head["GCDCQS"]
    r, s = head["COLOURS"], head["HOLEFREE"]
    if v != n * g or n < 3 or g < 2:
        raise Fail(f"PARAMS: need v = n*g with n >= 3 (got v={v}, n={n}, g={g})")
    w, h = v - 1, g - 1
    if w % 6 not in (1, 3) or h % 6 not in (1, 3):
        raise Fail(f"PARAMS: derived orders w={w}, h={h} are not both ≡ 1, 3 (mod 6)")
    if r != chi(w):
        raise Fail(f"PARAMS: COLOURS {r} differs from chi'({w}) = {chi(w)}")
    s_need = chi(w) - (w - h) // 2
    if s != s_need:
        raise Fail(f"PARAMS: HOLEFREE {s} differs from chi'(w) - (w-h)/2 = {s_need}")
    # groups
    if len(groups) != n:
        raise Fail(f"GROUPS: {len(groups)} groups listed, expected {n}")
    group_of = {}
    for gi, (G, ln) in enumerate(groups):
        if len(G) != g or len(set(G)) != g:
            raise Fail(f"GROUPS: line {ln}: group does not have {g} distinct points")
        for p in G:
            if p < 0 or p >= v:
                raise Fail(f"GROUPS: line {ln}: point {p} out of range")
            if p in group_of:
                raise Fail(f"GROUPS: line {ln}: point {p} in two groups")
            group_of[p] = gi
    if len(group_of) != v:
        raise Fail("GROUPS: groups do not cover all points")
    # blocks
    nb = (v * (v - 1) * (v - 2) // 6 - n * g * (g - 1) * (g - 2) // 6) // 4
    if len(blocks) != nb:
        raise Fail(f"BLOCK: {len(blocks)} blocks, expected {nb}")
    bset = set()
    for b, ln in blocks:
        if len(set(b)) != 4 or any(p < 0 or p >= v for p in b):
            raise Fail(f"BLOCK: line {ln}: not 4 distinct points of 0..{v-1}")
        cnt = {}
        for p in b:
            cnt[group_of[p]] = cnt.get(group_of[p], 0) + 1
        if max(cnt.values()) >= 3:
            raise Fail(f"BLOCK: line {ln}: three points in one group")
        fb = frozenset(b)
        if fb in bset:
            raise Fail(f"BLOCK: line {ln}: repeated block")
        bset.add(fb)
    count = {}
    for fb in bset:
        for t in combinations(sorted(fb), 3):
            count[t] = count.get(t, 0) + 1
    universe = {t for t in combinations(range(v), 3) if len({group_of[p] for p in t}) > 1}
    if set(count) != universe:
        if set(count) - universe:
            raise Fail("COVERAGE: a 3-subset of a group lies in a block")
        raise Fail("COVERAGE: some 3-subset not inside a group lies in no block")
    if any(c != 1 for c in count.values()):
        raise Fail("COVERAGE: some 3-subset lies in two blocks")
    # colourings
    if sorted(points) != list(range(v)):
        raise Fail(f"COMPLETENESS: POINT sections {sorted(set(range(v)) - set(points))} missing "
                   f"or out of range")
    nder = (w * (w - 1) - h * (h - 1)) // 6
    profiles = set()
    for x in range(v):
        classes = points[x]
        if len(classes) != r:
            raise Fail(f"COLOURING: POINT {x} has {len(classes)} classes, expected {r}")
        hole = {p for p in range(v) if group_of[p] == group_of[x] and p != x}
        listed = set()
        avoid = 0
        sizes = []
        for j, C in enumerate(classes):
            if not C:
                raise Fail(f"COLOURING: POINT {x} class {j} is empty")
            used = set()
            for t, ln in C:
                if len(set(t)) != 3 or any(p < 0 or p >= v for p in t) or x in t:
                    raise Fail(f"COLOURING: line {ln}: triple is not 3 distinct points of X\\{{{x}}}")
                if used & set(t):
                    raise Fail(f"COLOURING: POINT {x} class {j} line {ln}: triples not disjoint")
                used |= set(t)
                if frozenset(t + [x]) not in bset:
                    raise Fail(f"COLOURING: line {ln}: triple ∪ {{{x}}} is not a block")
                ft = frozenset(t)
                if ft in listed:
                    raise Fail(f"COLOURING: POINT {x} line {ln}: triple listed twice")
                listed.add(ft)
            if not used & hole:
                avoid += 1
            sizes.append(len(C))
        der = {frozenset(b - {x}) for b in bset if x in b}
        if listed != der or len(der) != nder:
            raise Fail(f"COLOURING: POINT {x}: listed triples are not the derived design")
        if avoid != s:
            raise Fail(f"COLOURING: POINT {x}: {avoid} classes avoid the hole, expected exactly {s}")
        profiles.add(tuple(sorted(sizes, reverse=True)))
    return {"v": v, "n": n, "g": g, "blocks": nb, "triples_covered": len(universe), "points": v,
            "colours": r, "hole_avoiding": s, "derived_triples_per_point": nder,
            "class_size_profiles": [list(p) for p in sorted(profiles)]}


def main(argv):
    if len(argv) != 2:
        print("usage: check_gcdcqs.py CERT", file=sys.stderr)
        return 2
    data = open(argv[1], "rb").read()
    rec = {"certificate": argv[1], "sha256": hashlib.sha256(data).hexdigest(),
           "checker": "check_gcdcqs.py (stdlib, definition-first)"}
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
