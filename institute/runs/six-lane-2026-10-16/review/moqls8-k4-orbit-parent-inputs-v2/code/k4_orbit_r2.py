"""K4 orbit-certificate ledger validator, revision r2 (review/K4_ORBIT_REDUCTION.r2.md §3; Claude orbit review M1, M2,
m4, m5; supersedes the never-run draft code/k4_orbit.py). NOT IN FORCE before the parent's GO(b).
install(C) wraps C.validate (the unchanged k5_cover logic with the K4 constants of code/k4_cover.py). Orbit leaves are
shown to it as UNSTARTED without evidence (structurally neutral); then:
 (a) pins: the r3 receipt, the second-path receipt and both permutation arrays are read from their pinned paths and must
     have the pinned SHA-256; receipt fields script/names/CNF/array hashes must equal the pins (CNF = ledger base) and
     every verdict field must be JSON true (checked with `is True`);
 (b) lits(X) is DERIVED from the tree (root: canonical V1 assignment of its index; child: lits(ancestor) followed by the
     canonical V_d assignment of its index) — exactly the units appended in X's leaf CNF; π_w is the composition of the
     PINNED arrays only (word over {"g1","g2"}, rightmost applied first); every literal must satisfy 1 ≤ |l| ≤ V;
     π_w(lits(source)) = lits(leaf) as literal sets;
 (c) source ≠ leaf; the source is SETTLED (strict CERTIFIED; REFINED with all 128 children settled — the exact 128-way
     partition is enforced by C.validate; or orbit CERTIFIED from a settled source); the combined dependency graph
     (refined node → children, orbit leaf → source) must be acyclic;
 (d) an orbit leaf is CERTIFIED, terminal (no children) and carries exactly one evidence record of kind "orbit".
complete ⇔ no problem and every terminal leaf CERTIFIED (strict or orbit).
CLI: python -B k4_orbit_r2.py validate|orbit-certify --base F4 --ledger L [--leaf ID --source ID --word g1,g2]
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
import sys
from array import array

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, ".."))
D = os.path.join(LANE, "evidence", "k4_split_v1", "auto_r3")
PINS = {
    "receipt": (os.path.join(D, "RECEIPT.json"), "c7154dc32d60e6cb3ab5d409432df1107bd8b1bae0d5b79fc4545af4b07e3ff8"),
    "g1": (os.path.join(D, "PERM_g1.i32le"), "8b09da43870aad811bf45d581a91f813fd0b816ee4859ec38cdb2da2fc115b2a"),
    "g2": (os.path.join(D, "PERM_g2.i32le"), "e0a2bc4c26eaa613389c3d43f68d5bc9771e619cfc0b9b2b2eb213dffc7dcfd3"),
    "secondpath": (os.path.join(D, "SECONDPATH_RECEIPT.json"),
                   "2990e2167116dfdab98f18a15592ec5cab91d19118be17ee8f849aa1400a1275"),
}
SECOND_SHA = PINS["secondpath"][1]
SECOND_SCRIPT_SHA = "ad0ee835b1de13da13251906f94ef19ad5dc06e724c8b222eb64678649a02d45"
CHECKER_SHA = "a03e9d500744c53cb68997e432e99ba296a4409a660138f34b3172b7eedb9866"
NAMES_SHA = "ed0462bc4de7fdcbc34397e1b05304160e47b9ba4a1bd1c858c5f997df3f8e2d"
_A = {}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def arrays(base_sha):
    """Load and pin-check everything once; returns ({'g1': array, 'g2': array}, V) or raises SystemExit."""
    if _A:
        return _A["P"], _A["V"]
    for k in ("receipt", "g1", "g2"):
        p, pin = PINS[k]
        if sha(p) != pin:
            raise SystemExit("pin mismatch: %s" % k)
    if SECOND_SHA is None or sha(PINS["secondpath"][0]) != SECOND_SHA:
        raise SystemExit("second-path receipt not pinned")
    r = json.load(open(PINS["receipt"][0]))
    s = json.load(open(PINS["secondpath"][0]))
    ok = (r.get("script_sha256") == CHECKER_SHA and r.get("names_sha256") == NAMES_SHA
          and r.get("cnf_sha256") == base_sha and s.get("cnf_sha256") == base_sha
          and r["arrays"]["g1"]["sha256"] == PINS["g1"][1] and r["arrays"]["g2"]["sha256"] == PINS["g2"][1]
          and s["arrays"]["g1"]["sha256"] == PINS["g1"][1] and s["arrays"]["g2"]["sha256"] == PINS["g2"][1]
          and all(r["verdict"][k] is True for k in ("arrays_bijective_automorphisms", "controls_as_intended",
                                                     "S3_of_order_6"))
          and s.get("verdict") is True and s.get("script_sha256") == SECOND_SCRIPT_SHA)
    if not ok:
        raise SystemExit("automorphism receipts do not satisfy the pins/verdicts")
    P = {}
    for k in ("g1", "g2"):
        a = array("i")
        a.frombytes(open(PINS[k][0], "rb").read())
        if sys.byteorder != "little":
            a.byteswap()
        P[k] = a
    V = len(P["g1"]) - 1
    _A["P"], _A["V"] = P, V
    return P, V


def apply_word(P, V, word, lits):
    out = []
    for l in lits:
        if not (type(l) is int and 1 <= abs(l) <= V):
            raise ValueError("literal out of range")
        v, sgn = abs(l), (1 if l > 0 else -1)
        for h in reversed(word):
            v = P[h][v]
        out.append(sgn * v)
    return out


def install(C):
    base_validate = C.validate

    def validate(L, base, receipts):
        byid = {x["id"]: x for x in L["leaves"]}
        orbit = [x for x in L["leaves"] if isinstance(x.get("evidence"), dict) and x["evidence"].get("kind") == "orbit"]
        Ln = copy.deepcopy(L)
        oid = {x["id"] for x in orbit}
        for x in Ln["leaves"]:
            if x["id"] in oid:
                x["state"], x["evidence"] = "UNSTARTED", None
        v = base_validate(Ln, base, receipts)
        problems = list(v["problems"])
        kids = {}
        for x in L["leaves"]:
            if x["ancestor"] is not None:
                kids.setdefault(x["ancestor"], []).append(x["id"])

        def lits(i):
            x = byid[i]
            own = C.canon(C.CHAIN[x["depth"]], x["index"])
            return own if x["ancestor"] is None else lits(x["ancestor"]) + own

        if orbit:
            try:
                P, V = arrays(base.sha)
            except SystemExit as e:
                problems.append(["automorphism pins", str(e)])
                P = None
            for x in orbit:
                ev = x["evidence"]
                if x["state"] != "CERTIFIED" or x["id"] in kids or set(ev) != {"kind", "source", "word",
                                                                                 "automorphism_receipt"}:
                    problems.append(["orbit leaf must be a terminal CERTIFIED leaf with one orbit record", x["id"]])
                src = ev.get("source")
                word = ev.get("word")
                if src == x["id"] or src not in byid or not isinstance(word, list) or not word \
                        or any(h not in ("g1", "g2") for h in word):
                    problems.append(["orbit source/word invalid", x["id"]])
                    continue
                if ev.get("automorphism_receipt", {}).get("sha256") != PINS["receipt"][1]:
                    problems.append(["orbit evidence names another receipt", x["id"]])
                if P is None:
                    continue
                try:
                    img = apply_word(P, V, word, lits(src))
                except ValueError:
                    problems.append(["literal out of range", x["id"]])
                    continue
                if sorted(img) != sorted(lits(x["id"])) or len(set(img)) != len(img):
                    problems.append(["orbit image mismatch", x["id"]])
                s = byid[src]
                if s["state"] == "CERTIFIED" and (s.get("evidence") or {}).get("kind") == "strict":
                    r = receipts.get(s["evidence"]["file"], s["evidence"]["line_sha256"])
                    if r is None or r.get("lits") != lits(src):
                        problems.append(["strict source literals differ from its leaf-CNF units", x["id"]])
        deps = {}
        for x in L["leaves"]:
            if x["state"] == "REFINED":
                deps[x["id"]] = kids.get(x["id"], [])
            elif x["id"] in oid:
                deps[x["id"]] = [x["evidence"].get("source")] if x["evidence"].get("source") in byid else []
        color, cyc = {}, []
        for root in deps:
            if color.get(root):
                continue
            stack = [(root, iter(deps.get(root, [])))]
            color[root] = 1
            while stack:
                node, it = stack[-1]
                nxt = next(it, None)
                if nxt is None:
                    color[node] = 2
                    stack.pop()
                elif color.get(nxt) == 1:
                    cyc.append(nxt)
                elif not color.get(nxt):
                    color[nxt] = 1
                    stack.append((nxt, iter(deps.get(nxt, []))))
        if cyc:
            problems.append(["cycle in the combined dependency graph", sorted(set(cyc))[:5]])
        memo = {}

        def settled(i):
            if i in memo:
                return memo[i]
            memo[i] = False
            x = byid[i]
            ev = x.get("evidence") or {}
            if x["state"] == "CERTIFIED" and ev.get("kind") == "strict":
                r = True
            elif x["state"] == "CERTIFIED" and ev.get("kind") == "orbit":
                r = ev.get("source") in byid and settled(ev["source"])
            elif x["state"] == "REFINED":
                r = len(kids.get(i, [])) == 128 and all(settled(k) for k in kids[i])
            else:
                r = False
            memo[i] = r
            return r

        for x in orbit:
            if x["evidence"].get("source") in byid and not settled(x["evidence"]["source"]):
                problems.append(["orbit source not settled", x["id"]])
        term = [x for x in L["leaves"] if x["state"] != "REFINED"]
        v.update({"problems": problems, "counts": {s: sum(x["state"] == s for x in L["leaves"]) for s in C.STATES},
                  "orbit_certified": len(orbit),
                  "complete": (not problems) and all(x["state"] == "CERTIFIED" for x in term)})
        return v

    C.validate = validate
    return C


def main():
    import argparse
    spec = importlib.util.spec_from_file_location("k4_cover", os.path.join(HERE, "k4_cover.py"))
    K4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(K4)
    C = install(K4.configure(K4.load_cover()))
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["validate", "orbit-certify"])
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
                     "automorphism_receipt": {"path": os.path.relpath(PINS["receipt"][0], LANE),
                                              "sha256": PINS["receipt"][1]}}
    v2 = C.validate(L, base, C.Receipts())
    if v2["problems"]:
        raise SystemExit("orbit-certify would produce an invalid ledger: %s" % json.dumps(v2["problems"][:20]))
    print(json.dumps(C.write_next(L, lsha, "orbit-certify %s from %s via %s" % (a.leaf, a.source, a.word))))


if __name__ == "__main__":
    main()
