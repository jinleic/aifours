#!/usr/bin/env python3
"""Independent LKTS(v) certificate checker (standard library only).

Written for the 2026-10-16 lane; shares no code with the generator or with the
prior dossier's checker.  Assumes NO automorphism group.

Format (plain text, '#' comments, blank lines ignored):
    LKTS v
    KTS i          (i = 0..v-3, each exactly once)
    CLASS j        (j = 0..(v-3)/2 within the current KTS, each exactly once)
    a b c          (one triple per line, integers in 0..v-1)

Checks: v ≡ 3 (mod 6); v-2 constituents; (v-1)/2 classes each; every class is a
partition of X into v/3 triples of 3 distinct points; in every constituent every
unordered pair of X lies in exactly one block; no triple occurs in two places;
the union of all blocks is exactly the set of all C(v,3) triples.
Exit 0 and print JSON receipt on PASS; exit 1 with the first failure otherwise.
"""
import hashlib
import json
import sys
from itertools import combinations


class Fail(Exception):
    pass


def parse(text):
    v = None
    kts = {}
    cur_k = None
    cur_c = None
    for ln, raw in enumerate(text.splitlines(), 1):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        tok = line.split()
        if tok[0] == "LKTS":
            if v is not None or len(tok) != 2:
                raise Fail(f"line {ln}: bad/duplicate header")
            v = int(tok[1])
            continue
        if v is None:
            raise Fail(f"line {ln}: data before header")
        if tok[0] == "KTS":
            if len(tok) != 2:
                raise Fail(f"line {ln}: bad KTS line")
            cur_k = int(tok[1])
            if cur_k in kts:
                raise Fail(f"line {ln}: duplicate KTS {cur_k}")
            kts[cur_k] = {}
            cur_c = None
            continue
        if tok[0] == "CLASS":
            if cur_k is None or len(tok) != 2:
                raise Fail(f"line {ln}: CLASS outside KTS or malformed")
            cur_c = int(tok[1])
            if cur_c in kts[cur_k]:
                raise Fail(f"line {ln}: duplicate CLASS {cur_c} in KTS {cur_k}")
            kts[cur_k][cur_c] = []
            continue
        if cur_c is None:
            raise Fail(f"line {ln}: triple outside a CLASS")
        if len(tok) != 3:
            raise Fail(f"line {ln}: triple must have 3 integers")
        t = tuple(int(x) for x in tok)
        kts[cur_k][cur_c].append((ln, t))
    if v is None:
        raise Fail("missing header")
    return v, kts


def check(v, kts):
    if v < 3 or v % 6 != 3:
        raise Fail(f"v={v} is not 3 mod 6")
    nk = v - 2
    nc = (v - 1) // 2
    per_class = v // 3
    if sorted(kts) != list(range(nk)):
        raise Fail(f"constituent ids {sorted(kts)[:5]}... != 0..{nk-1}")
    owner = {}
    for k in range(nk):
        classes = kts[k]
        if sorted(classes) != list(range(nc)):
            raise Fail(f"KTS {k}: class ids != 0..{nc-1}")
        pair_seen = set()
        nblocks = 0
        for c in range(nc):
            blocks = classes[c]
            if len(blocks) != per_class:
                raise Fail(f"KTS {k} CLASS {c}: {len(blocks)} triples, need {per_class}")
            covered = set()
            for ln, t in blocks:
                a, b, d = t
                if not all(0 <= x < v for x in t):
                    raise Fail(f"line {ln}: point out of range")
                if len({a, b, d}) != 3:
                    raise Fail(f"line {ln}: repeated point in triple")
                for x in t:
                    if x in covered:
                        raise Fail(f"KTS {k} CLASS {c}: point {x} covered twice")
                    covered.add(x)
                key = tuple(sorted(t))
                if key in owner:
                    raise Fail(f"triple {key} occurs twice (KTS {owner[key]} and KTS {k})")
                owner[key] = k
                for p in combinations(key, 2):
                    if p in pair_seen:
                        raise Fail(f"KTS {k}: pair {p} covered twice")
                    pair_seen.add(p)
                nblocks += 1
            if len(covered) != v:
                raise Fail(f"KTS {k} CLASS {c}: covers {len(covered)} points")
        if len(pair_seen) != v * (v - 1) // 2:
            raise Fail(f"KTS {k}: covers {len(pair_seen)} pairs")
        if nblocks != v * (v - 1) // 6:
            raise Fail(f"KTS {k}: {nblocks} blocks")
    total = v * (v - 1) * (v - 2) // 6
    if len(owner) != total:
        raise Fail(f"{len(owner)} distinct triples, need {total}")
    # explicit equality with the set of all triples
    allt = set(combinations(range(v), 3))
    if set(owner) != allt:
        raise Fail("union of blocks differs from the set of all triples")
    return {"v": v, "constituents": nk, "classes_per_constituent": nc,
            "triples_per_class": per_class, "distinct_triples": len(owner)}


def main(argv):
    if len(argv) != 2:
        print("usage: check_lkts57.py CERT", file=sys.stderr)
        return 2
    data = open(argv[1], "rb").read()
    me = open(__file__, "rb").read()
    receipt = {"certificate": argv[1],
               "certificate_sha256": hashlib.sha256(data).hexdigest(),
               "checker_sha256": hashlib.sha256(me).hexdigest()}
    try:
        v, kts = parse(data.decode())
        receipt.update(check(v, kts))
        receipt["result"] = "PASS"
        print(json.dumps(receipt, indent=1))
        return 0
    except (Fail, ValueError) as e:
        receipt["result"] = "FAIL"
        receipt["reason"] = str(e)
        print(json.dumps(receipt, indent=1))
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
