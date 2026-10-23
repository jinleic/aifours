"""K4 orbit-certificate extension of the cover ledger (review/K4_ORBIT_REDUCTION.r1.md §3; NOT IN FORCE before the
parent's GO(b)). install(C) wraps C.validate (the unchanged k5_cover logic with K4 constants) so that leaves with
evidence kind "orbit" are checked by the contract instead:
 (a) automorphism receipt = pinned path and SHA-256, verdict fields all true, receipt cnf_sha256 = ledger base SHA;
 (b) π_w recomputed on g-variables from the generator definitions and the pinned name table; π_w(lits(R)) = lits(L)
     as literal sets;
 (c) the source R is SETTLED (strict CERTIFIED; REFINED with all children settled; or orbit-CERTIFIED from a settled
     source), with cycle detection over child and orbit edges;
 (d) an orbit-certified leaf has no children.
All other leaves go through C.validate unchanged (orbit leaves are presented to it as UNSTARTED without evidence, which
is structurally neutral). complete ⇔ no problem and every terminal leaf CERTIFIED (strict or orbit).
CLI (new ledger version, exclusive create): python -B k4_orbit.py orbit-certify --base F4 --ledger L --leaf ID
       --source ID --word g1[,g2,...]
"""
from __future__ import annotations

import copy
import gzip
import hashlib
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NAMES = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-encoder-binding-v1/K4.names.json.gz"
NAMES_SHA = "ed0462bc4de7fdcbc34397e1b05304160e47b9ba4a1bd1c858c5f997df3f8e2d"
AUTO = os.path.normpath(os.path.join(HERE, "..", "evidence", "k4_split_v1", "AUTOMORPHISM_S3_567_r2.json"))
AUTO_SHA = "d688277f10096cd652293c31b7dc8ae337bb647fa914382d09c2d9c11844357c"
GENS = {"g1": ([0, 1, 2, 3, 4, 6, 5, 7], {1: 1, 2: 3, 3: 2, 4: 4, 5: 5}),
        "g2": ([0, 1, 2, 3, 4, 5, 7, 6], {1: 1, 2: 2, 3: 4, 4: 3, 5: 5})}
_G = {}


def sha_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def gmaps():
    if not _G:
        if sha_file(NAMES) != NAMES_SHA:
            raise SystemExit("name table hash mismatch")
        idx, inv = {}, {}
        for v, name in json.load(gzip.open(NAMES)):
            if name[0] == "g":
                key = (int(name[1]), frozenset((tuple(name[2]), tuple(name[3]))))
                idx[key] = v
                inv[v] = key
        _G["idx"], _G["inv"] = idx, inv
    return _G["idx"], _G["inv"]


def apply_word(word, lits):
    idx, inv = gmaps()
    out = []
    for l in lits:
        v = abs(l)
        for h in reversed(word):
            sigma, rho = GENS[h]
            s, pq = inv[v]
            v = idx[(rho[s], frozenset((sigma[p[0]], sigma[p[1]]) for p in pq))]
        out.append(v if l > 0 else -v)
    return out


def receipt_ok(base_sha):
    if not os.path.exists(AUTO) or sha_file(AUTO) != AUTO_SHA:
        return False
    r = json.load(open(AUTO))
    v = r.get("verdict", {})
    return (r.get("cnf_sha256") == base_sha and v.get("controls_as_intended") is True
            and v.get("generators_automorphisms") is True and v.get("S3_of_order_6") is True)


def install(C):
    base_validate = C.validate

    def validate(L, base, receipts):
        orbit = [x for x in L["leaves"] if (x.get("evidence") or {}).get("kind") == "orbit"]
        Ln = copy.deepcopy(L)
        oid = {x["id"] for x in orbit}
        for x in Ln["leaves"]:
            if x["id"] in oid:
                x["state"], x["evidence"] = "UNSTARTED", None
        v = base_validate(Ln, base, receipts)
        problems = v["problems"]
        byid = {x["id"]: x for x in L["leaves"]}
        kids = {}
        for x in L["leaves"]:
            if x["ancestor"] is not None:
                kids.setdefault(x["ancestor"], []).append(x["id"])
        if orbit and not receipt_ok(base.sha):
            problems.append(["automorphism receipt not pinned/valid"])
        for x in orbit:
            ev = x["evidence"]
            if x["state"] != "CERTIFIED" or x["id"] in kids:
                problems.append(["orbit leaf not a terminal CERTIFIED leaf", x["id"]])
            if ev.get("automorphism_receipt", {}).get("sha256") != AUTO_SHA:
                problems.append(["orbit evidence names another receipt", x["id"]])
            src = byid.get(ev.get("source"))
            word = ev.get("word") or []
            if src is None or any(h not in GENS for h in word):
                problems.append(["orbit source/word invalid", x["id"]])
                continue
            try:
                img = apply_word(word, src["lits"])
            except KeyError:
                problems.append(["orbit word leaves the g-variables", x["id"]])
                continue
            if sorted(img) != sorted(x["lits"]):
                problems.append(["orbit image mismatch", x["id"]])
        state = {}

        def settled(i, stack):
            if i in state:
                return state[i]
            if i in stack:
                problems.append(["cycle in settlement graph", i])
                return False
            stack.add(i)
            x = byid[i]
            ev = x.get("evidence") or {}
            if x["state"] == "CERTIFIED" and ev.get("kind") == "strict":
                r = True
            elif x["state"] == "CERTIFIED" and ev.get("kind") == "orbit":
                r = ev.get("source") in byid and settled(ev["source"], stack)
            elif x["state"] == "REFINED":
                r = all(settled(k, stack) for k in kids.get(i, []))
            else:
                r = False
            stack.discard(i)
            state[i] = r
            return r

        for x in orbit:
            if not settled(x["evidence"]["source"], set()):
                problems.append(["orbit source not settled", x["id"]])
        term = [x for x in L["leaves"] if x["state"] != "REFINED"]
        counts = {s: sum(x["state"] == s for x in L["leaves"]) for s in C.STATES}
        v.update({"problems": problems, "counts": counts, "orbit_certified": len(orbit),
                  "complete": (not problems) and all(x["state"] == "CERTIFIED" for x in term)})
        return v

    C.validate = validate
    return C


def main():
    import argparse
    K = importlib.util.spec_from_file_location("k4_cover", os.path.join(HERE, "k4_cover.py"))
    K4 = importlib.util.module_from_spec(K)
    K.loader.exec_module(K4)
    C = install(K4.configure(K4.load_cover()))
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["orbit-certify", "validate"])
    ap.add_argument("--base", required=True)
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--leaf")
    ap.add_argument("--source")
    ap.add_argument("--word")
    a = ap.parse_args()
    base = C.Base(a.base)
    L, lsha = C.load_ledger(a.ledger)
    v = C.validate(L, base, C.Receipts())
    if v["problems"]:
        raise SystemExit("input ledger invalid: %s" % json.dumps(v["problems"][:20]))
    if a.mode == "validate":
        print(json.dumps({k: v[k] for k in ("problems", "counts", "orbit_certified", "complete")}))
        return
    x = next(y for y in L["leaves"] if y["id"] == a.leaf)
    if x["state"] != "UNSTARTED":
        raise SystemExit("only UNSTARTED leaves can be orbit-certified")
    x["state"] = "CERTIFIED"
    x["evidence"] = {"kind": "orbit", "source": a.source, "word": a.word.split(","),
                     "automorphism_receipt": {"path": os.path.relpath(AUTO, HERE), "sha256": AUTO_SHA}}
    v2 = C.validate(L, base, C.Receipts())
    if v2["problems"]:
        raise SystemExit("orbit-certify would produce an invalid ledger: %s" % json.dumps(v2["problems"][:20]))
    print(json.dumps(C.write_next(L, lsha, "orbit-certify %s from %s via %s" % (a.leaf, a.source, a.word))))


if __name__ == "__main__":
    main()
