#!/usr/bin/env python3
"""Direct, definition-based checker for an RDSQS(v) certificate (standard library only).

Assumes NO symmetry.  Certificate format (plain text; '#' starts a comment; blank
lines ignored):

    RDSQS v
    BLOCKS
    a b c d            (one 4-subset per line, points 0..v-1)
    ...
    POINT x            (one section for every x in 0..v-1)
    CLASS j            (j = 0..(v-2)/2 - 1, each exactly once per POINT)
    a b c              (triples of the derived design at x)
    ...

Checks, in order (the first failure is reported with a category prefix):
  FORMAT        malformed lines / sections / ids
  BLOCK         v ≡ 4 (mod 6); block count v(v-1)(v-2)/24; 4 distinct in-range points;
                no repeated block
  COVERAGE      every 3-subset of X lies in exactly one block (explicit equality with
                the set of all C(v,3) triples)
  COMPLETENESS  a POINT section exists for every x (and none twice / out of range)
  RESOLUTION    for every x: exactly (v-2)/2 classes; each class has (v-1)/3 triples of
                3 distinct in-range points avoiding x; each class partitions X\\{x};
                every listed triple T has T∪{x} a block; no triple listed twice; the
                listed triples are exactly the derived design {b\\{x}: x∈b∈B}
Exit 0 with a JSON receipt on PASS, 1 with the failure on FAIL.
"""
import hashlib
import json
import sys
from itertools import combinations


class Fail(Exception):
    pass


def parse(text):
    v = None
    blocks = []
    points = {}
    section = None
    cur_x = None
    cur_c = None
    for ln, raw in enumerate(text.splitlines(), 1):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        tok = line.split()
        head = tok[0]
        if head == "RDSQS":
            if v is not None or len(tok) != 2:
                raise Fail(f"FORMAT line {ln}: bad or duplicate header")
            v = int(tok[1])
            continue
        if v is None:
            raise Fail(f"FORMAT line {ln}: data before header")
        if head == "BLOCKS":
            if section is not None or len(tok) != 1:
                raise Fail(f"FORMAT line {ln}: BLOCKS must appear once, before POINT sections")
            section = "BLOCKS"
            continue
        if head == "POINT":
            if section is None or len(tok) != 2:
                raise Fail(f"FORMAT line {ln}: POINT before BLOCKS or malformed")
            section = "POINT"
            cur_x = int(tok[1])
            if cur_x in points:
                raise Fail(f"COMPLETENESS line {ln}: POINT {cur_x} appears twice")
            points[cur_x] = {}
            cur_c = None
            continue
        if head == "CLASS":
            if section != "POINT" or len(tok) != 2:
                raise Fail(f"FORMAT line {ln}: CLASS outside a POINT section or malformed")
            cur_c = int(tok[1])
            if cur_c in points[cur_x]:
                raise Fail(f"RESOLUTION line {ln}: CLASS {cur_c} appears twice at POINT {cur_x}")
            points[cur_x][cur_c] = []
            continue
        nums = tuple(int(t) for t in tok)
        if section == "BLOCKS":
            if len(nums) != 4:
                raise Fail(f"FORMAT line {ln}: a block needs exactly 4 integers")
            blocks.append((ln, nums))
        elif section == "POINT":
            if cur_c is None:
                raise Fail(f"FORMAT line {ln}: triple outside a CLASS")
            if len(nums) != 3:
                raise Fail(f"FORMAT line {ln}: a class triple needs exactly 3 integers")
            points[cur_x][cur_c].append((ln, nums))
        else:
            raise Fail(f"FORMAT line {ln}: data outside any section")
    if v is None:
        raise Fail("FORMAT: missing header")
    return v, blocks, points


def check(v, blocks, points):
    if v < 4 or v % 6 != 4:
        raise Fail(f"BLOCK: v={v} is not ≡ 4 (mod 6)")
    nb = v * (v - 1) * (v - 2) // 24
    if len(blocks) != nb:
        raise Fail(f"BLOCK: {len(blocks)} blocks, an SQS({v}) has {nb}")
    blockset = set()
    owner = {}
    for ln, b in blocks:
        if not all(0 <= p < v for p in b):
            raise Fail(f"BLOCK line {ln}: point out of range")
        if len(set(b)) != 4:
            raise Fail(f"BLOCK line {ln}: repeated point in block")
        key = tuple(sorted(b))
        if key in blockset:
            raise Fail(f"BLOCK line {ln}: block {key} listed twice")
        blockset.add(key)
        for t in combinations(key, 3):
            if t in owner:
                raise Fail(f"COVERAGE: triple {t} lies in two blocks ({owner[t]} and {key})")
            owner[t] = key
    alltrip = set(combinations(range(v), 3))
    if set(owner) != alltrip:
        missing = min(alltrip - set(owner))
        raise Fail(f"COVERAGE: triple {missing} lies in no block")
    # derived designs
    derived = {x: set() for x in range(v)}
    for key in blockset:
        for x in key:
            derived[x].add(tuple(p for p in key if p != x))
    expected_ids = set(range(v))
    got = set(points)
    if got != expected_ids:
        miss = sorted(expected_ids - got)
        extra = sorted(got - expected_ids)
        raise Fail(f"COMPLETENESS: missing resolution for points {miss[:5]}, unexpected point ids {extra[:5]}")
    ncls = (v - 2) // 2
    per = (v - 1) // 3
    nder = (v - 1) * (v - 2) // 6
    for x in range(v):
        cls = points[x]
        if sorted(cls) != list(range(ncls)):
            raise Fail(f"RESOLUTION: point {x} has class ids {sorted(cls)[:6]}..., need 0..{ncls-1}")
        seen = set()
        for c in range(ncls):
            trips = cls[c]
            if len(trips) != per:
                raise Fail(f"RESOLUTION: point {x} class {c} has {len(trips)} triples, need {per}")
            cover = set()
            for ln, t in trips:
                if not all(0 <= p < v for p in t) or len(set(t)) != 3:
                    raise Fail(f"RESOLUTION line {ln}: bad triple")
                if x in t:
                    raise Fail(f"RESOLUTION line {ln}: triple contains the point {x} itself")
                key = tuple(sorted(t))
                if key not in derived[x]:
                    raise Fail(f"RESOLUTION line {ln}: {key} ∪ {{{x}}} is not a block (not a derived triple)")
                if key in seen:
                    raise Fail(f"RESOLUTION line {ln}: derived triple {key} listed twice at point {x}")
                seen.add(key)
                for p in key:
                    if p in cover:
                        raise Fail(f"RESOLUTION: point {x} class {c} does not partition X\\{{{x}}} (point {p} twice)")
                    cover.add(p)
            if len(cover) != v - 1:
                raise Fail(f"RESOLUTION: point {x} class {c} covers {len(cover)} points, need {v-1}")
        if seen != derived[x] or len(seen) != nder:
            raise Fail(f"RESOLUTION: point {x} resolution does not list exactly the derived design")
    return {"v": v, "blocks": len(blockset), "triples_covered": len(owner), "points_resolved": v,
            "classes_per_point": ncls, "triples_per_class": per, "derived_triples_per_point": nder}


def main(argv):
    if len(argv) != 2:
        print("usage: check_rdsqs.py CERT", file=sys.stderr)
        return 2
    data = open(argv[1], "rb").read()
    me = open(__file__, "rb").read()
    rec = {"certificate": argv[1], "certificate_sha256": hashlib.sha256(data).hexdigest(),
           "checker_sha256": hashlib.sha256(me).hexdigest()}
    try:
        v, blocks, points = parse(data.decode())
        rec.update(check(v, blocks, points))
        rec["result"] = "PASS"
        print(json.dumps(rec, indent=1, ensure_ascii=False))
        return 0
    except (Fail, ValueError) as e:
        rec["result"] = "FAIL"
        rec["reason"] = str(e)
        print(json.dumps(rec, indent=1, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
