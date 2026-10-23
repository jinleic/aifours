#!/usr/bin/env python3
"""Route-1 definition-first checker for Format S certificates (README §3): a CQS(g^n : s) with good
colourable derived designs (Tan–Zhou LF 256–288) — standard library only, NO symmetry assumed.

Checks (first failure reported with a category prefix):
  FORMAT        header/sections/ids/line shapes; POINT sections before STEMPOINT sections
  PARAM         v = g n + s; v-1 ≡ 1, 3 (mod 6); r = chi'(v-1) by (1.1); t = r - (v-g-s)/2; header equal
  PARTITION     groups (n of size g) and stem (size s) partition {0..v-1}
  BLOCK         4 distinct in-range points per block; no repeated block
  COVERAGE      every 3-subset of X not inside any S ∪ G lies in exactly one block, none inside S ∪ G lies
                in a block (explicit loop over all C(v,3) triples)
  COMPLETENESS  one POINT section per group point, one STEMPOINT section per stem point
  COLOURING     group point x: exactly r nonempty classes CLASS 0..r-1; triples of 3 distinct points of
                X∖{x}; pairwise disjoint inside a class; T ∪ {x} a block; no triple twice; all derived
                triples listed
  HOLEFREE      exactly t classes at x contain no point of (G_x ∪ S)∖{x}
  FRAME         stem point α: classes FRAME k (0 ≤ k < n); T ∪ {α} a block; each class covers every point of
                X∖(S ∪ G_k) exactly once and nothing else; every derived triple at α in exactly one class
Exit 0 and a JSON line with "result": "PASS", or exit 1 with "result": "FAIL" and the failure."""
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
    raise Fail(f"PARAM: {w} is not an STS order")


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
    pos = 0

    def take(expect_kw, nargs):
        nonlocal pos
        if pos >= len(lines):
            raise Fail(f"FORMAT: missing '{expect_kw}'")
        ln, s = lines[pos]
        if s[0] != expect_kw or len(s) != nargs + 1:
            raise Fail(f"FORMAT: line {ln}: expected '{expect_kw}' with {nargs} integers")
        pos += 1
        return ints(s[1:], ln)

    v, n, g, s = take("GCDCQS", 4)
    (r,) = take("COLOURS", 1)
    (t,) = take("HOLEFREE", 1)
    take("GROUPS", 0)
    groups = []
    for _ in range(n):
        if pos >= len(lines):
            raise Fail("FORMAT: missing group lines")
        ln, tok = lines[pos]
        if len(tok) != g:
            raise Fail(f"FORMAT: line {ln}: group line does not have {g} points")
        groups.append(ints(tok, ln))
        pos += 1
    take("STEM", 0)
    stem = []
    if s > 0:
        ln, tok = lines[pos]
        if len(tok) != s:
            raise Fail(f"FORMAT: line {ln}: stem line does not have {s} points")
        stem = ints(tok, ln)
        pos += 1
    take("BLOCKS", 0)
    blocks = []
    while pos < len(lines) and lines[pos][1][0] not in ("POINT", "STEMPOINT"):
        ln, tok = lines[pos]
        if len(tok) != 4:
            raise Fail(f"FORMAT: line {ln}: block line does not have 4 entries")
        blocks.append((ints(tok, ln), ln))
        pos += 1
    points, stempoints = {}, {}
    cur, kind = None, None
    while pos < len(lines):
        ln, tok = lines[pos]
        pos += 1
        if tok[0] == "POINT":
            if kind == "stem":
                raise Fail(f"FORMAT: line {ln}: POINT section after a STEMPOINT section")
            if len(tok) != 2:
                raise Fail(f"FORMAT: line {ln}: bad POINT line")
            (x,) = ints(tok[1:], ln)
            if x in points:
                raise Fail(f"COMPLETENESS: POINT {x} appears twice (line {ln})")
            points[x], cur, kind = [], x, "point"
        elif tok[0] == "STEMPOINT":
            if len(tok) != 2:
                raise Fail(f"FORMAT: line {ln}: bad STEMPOINT line")
            (a,) = ints(tok[1:], ln)
            if a in stempoints:
                raise Fail(f"COMPLETENESS: STEMPOINT {a} appears twice (line {ln})")
            stempoints[a], cur, kind = [], a, "stem"
        elif tok[0] == "CLASS":
            if kind != "point" or len(tok) != 2:
                raise Fail(f"FORMAT: line {ln}: CLASS outside a POINT section or malformed")
            (j,) = ints(tok[1:], ln)
            if j != len(points[cur]):
                raise Fail(f"FORMAT: line {ln}: POINT {cur}: class id {j} out of order")
            points[cur].append([])
        elif tok[0] == "FRAME":
            if kind != "stem" or len(tok) != 2:
                raise Fail(f"FORMAT: line {ln}: FRAME outside a STEMPOINT section or malformed")
            (k,) = ints(tok[1:], ln)
            stempoints[cur].append((k, ln, []))
        else:
            if len(tok) != 3:
                raise Fail(f"FORMAT: line {ln}: triple line does not have 3 entries")
            tri = (ints(tok, ln), ln)
            if kind == "point" and points[cur]:
                points[cur][-1].append(tri)
            elif kind == "stem" and stempoints[cur]:
                stempoints[cur][-1][2].append(tri)
            else:
                raise Fail(f"FORMAT: line {ln}: triple outside a class")
    return (v, n, g, s, r, t), groups, stem, blocks, points, stempoints


def check(head, groups, stem, blocks, points, stempoints):
    v, n, g, s, r, t = head
    if v != g * n + s or n < 1 or g < 1 or s < 0:
        raise Fail(f"PARAM: v={v} differs from g n + s = {g * n + s}")
    w = v - 1
    if w % 6 not in (1, 3):
        raise Fail(f"PARAM: v-1 = {w} is not ≡ 1, 3 (mod 6)")
    if r != chi(w):
        raise Fail(f"PARAM: COLOURS {r} differs from chi'({w}) = {chi(w)}")
    if (v - g - s) % 2 or t != r - (v - g - s) // 2:
        raise Fail(f"PARAM: HOLEFREE {t} differs from r - (v-g-s)/2 = {r - (v - g - s) // 2}")
    allp = [p for G in groups for p in G] + list(stem)
    if sorted(allp) != list(range(v)):
        raise Fail("PARTITION: groups and stem do not partition {0..v-1}")
    gid = {p: i for i, G in enumerate(groups) for p in G}
    S = set(stem)
    bset = set()
    for b, ln in blocks:
        if len(set(b)) != 4 or any(p < 0 or p >= v for p in b):
            raise Fail(f"BLOCK: line {ln}: not 4 distinct points of 0..{v - 1}")
        fb = frozenset(b)
        if fb in bset:
            raise Fail(f"BLOCK: line {ln}: repeated block")
        bset.add(fb)
    cover = {}
    for fb in bset:
        for tr in combinations(sorted(fb), 3):
            cover[tr] = cover.get(tr, 0) + 1

    def inside(tr):  # tr inside S ∪ G for some group G
        gs = {gid[p] for p in tr if p not in S}
        return len(gs) <= 1

    ncov = 0
    for tr in combinations(range(v), 3):
        c = cover.get(tr, 0)
        if inside(tr):
            if c:
                raise Fail(f"COVERAGE: triple {tr} inside S ∪ G lies in {c} block(s)")
        else:
            if c != 1:
                raise Fail(f"COVERAGE: triple {tr} lies in {c} blocks")
            ncov += 1
    if len(cover) != ncov:
        raise Fail("COVERAGE: a block contains a triple outside the coverable set")
    gpts = sorted(gid)
    if sorted(points) != gpts:
        raise Fail(f"COMPLETENESS: POINT sections {sorted(set(gpts) ^ set(points))[:5]} missing or not group points")
    if sorted(stempoints) != sorted(S):
        raise Fail("COMPLETENESS: STEMPOINT sections do not match the stem")
    sizes = []
    nder_group = set()
    for x in gpts:
        classes = points[x]
        if len(classes) != r:
            raise Fail(f"COLOURING: POINT {x} has {len(classes)} classes, expected {r}")
        hole = (set(groups[gid[x]]) | S) - {x}
        der = {frozenset(b - {x}) for b in bset if x in b}
        listed, avoid, prof = set(), 0, []
        for j, C in enumerate(classes):
            if not C:
                raise Fail(f"COLOURING: POINT {x} class {j} is empty")
            used = set()
            for tr, ln in C:
                if len(set(tr)) != 3 or any(p < 0 or p >= v for p in tr) or x in tr:
                    raise Fail(f"COLOURING: line {ln}: triple not 3 distinct points of X∖{{{x}}}")
                if used & set(tr):
                    raise Fail(f"COLOURING: POINT {x} class {j} line {ln}: triples not disjoint")
                used |= set(tr)
                ft = frozenset(tr)
                if ft not in der:
                    raise Fail(f"COLOURING: line {ln}: triple ∪ {{{x}}} is not a block")
                if ft in listed:
                    raise Fail(f"COLOURING: POINT {x} line {ln}: triple listed twice")
                listed.add(ft)
            if not used & hole:
                avoid += 1
            prof.append(len(C))
        if listed != der:
            raise Fail(f"COLOURING: POINT {x}: listed triples are not the derived design")
        if avoid != t:
            raise Fail(f"HOLEFREE: POINT {x}: {avoid} classes avoid the hole, expected exactly {t}")
        nder_group.add(len(der))
        sizes.append(tuple(sorted(prof, reverse=True)))
    nframes = set()
    for a in sorted(S):
        der = {frozenset(b - {a}) for b in bset if a in b}
        listed = set()
        for k, ln, C in stempoints[a]:
            if not (0 <= k < n):
                raise Fail(f"FRAME: line {ln}: missed-group index {k} out of range")
            target = set(range(v)) - S - set(groups[k])
            used = set()
            if not C:
                raise Fail(f"FRAME: line {ln}: empty class")
            for tr, tln in C:
                if len(set(tr)) != 3 or any(p < 0 or p >= v for p in tr):
                    raise Fail(f"FRAME: line {tln}: triple not 3 distinct points")
                if used & set(tr):
                    raise Fail(f"FRAME: STEMPOINT {a} line {tln}: triples of a frame class not disjoint")
                used |= set(tr)
                ft = frozenset(tr)
                if ft not in der:
                    raise Fail(f"FRAME: line {tln}: triple ∪ {{{a}}} is not a block")
                if ft in listed:
                    raise Fail(f"FRAME: STEMPOINT {a} line {tln}: triple listed twice")
                listed.add(ft)
            if used != target:
                raise Fail(f"FRAME: STEMPOINT {a} class at line {ln}: not a parallel class of X∖(S ∪ G_{k})")
        if listed != der:
            raise Fail(f"FRAME: STEMPOINT {a}: frame classes do not cover the derived design")
        nframes.add(len(stempoints[a]))
    prof = sorted(set(sizes))
    return {"v": v, "n": n, "g": g, "s": s, "blocks": len(bset), "covered_triples": ncov, "colours": r,
            "holefree": t, "group_point_derived_triples": sorted(nder_group), "stem_frame_classes": sorted(nframes),
            "class_size_profiles": [" ".join(f"{z}^{p.count(z)}" for z in sorted(set(p), reverse=True)) for p in prof]}


def main(argv):
    if len(argv) != 2:
        print("usage: check_gcdcqs_s.py CERT", file=sys.stderr)
        return 2
    data = open(argv[1], "rb").read()
    rec = {"certificate": argv[1], "sha256": hashlib.sha256(data).hexdigest(),
           "checker": "check_gcdcqs_s.py (route 1, stdlib, definition-based)"}
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
