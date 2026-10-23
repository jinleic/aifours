"""In-memory control suite for code/k4_orbit_r3.py (Codex delta review v2: single-buffer regression + the missing r2
controls). Reads (never writes) the K4 ledger v001, the strict pilot receipts and the pinned automorphism artifacts;
ledger states are modified only in memory; writes one result file. Every mutation must produce the NAMED problem.
python -B k4_orbit_controls_r3.py --out ../evidence/k4_split_v1/auto_r3/ORBIT_VALIDATOR_CONTROLS_r3.json
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, ".."))
F4 = os.path.join(LANE, "evidence", "k4_w1_v1", "GA3_K4w1.cnf")
LEDGER = os.path.join(LANE, "evidence", "k4_split_v1", "ledger", "LEDGER.v001.json")


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    O = load("k4_orbit_r3")
    K = load("k4_cover")
    C = O.install(K.configure(K.load_cover()))
    base = C.Base(F4)
    L0, _ = C.load_ledger(LEDGER)
    by0 = {x["id"]: x for x in L0["leaves"]}
    rel = "pilot/RESULTS.jsonl"
    for line in open(os.path.join(C.SPLIT_DIR, rel), "rb").read().split(b"\n"):
        if line.strip():
            r = json.loads(line)
            x = by0[r["id"]]
            x["state"] = "CERTIFIED" if C.strict_ok(r) else "UNKNOWN"
            x["evidence"] = {"kind": "strict", "file": rel, "line_sha256": hashlib.sha256(line).hexdigest()}
    rc = C.Receipts()
    res = []

    def leaf(L, i):
        return next(y for y in L["leaves"] if y["id"] == i)

    def orb(L, lf, src, word, **extra):
        x = leaf(L, lf)
        x["state"] = "CERTIFIED"
        x["evidence"] = {"kind": "orbit", "source": src, "word": word,
                         "automorphism_receipt": {"path": "evidence/k4_split_v1/auto_r3/RECEIPT.json",
                                                  "sha256": O.PINS["receipt"][1]}}
        x["evidence"].update(extra)

    def refine(L, rid, n=128):
        x = leaf(L, rid)
        x["state"] = "REFINED"
        for b in range(n):
            L["leaves"].append({"id": C.child_id(rid, x["depth"] + 1, b), "depth": x["depth"] + 1, "index": b,
                                "ancestor": rid, "lits": x["lits"] + C.canon(C.CHAIN[x["depth"] + 1], b),
                                "state": "UNSTARTED", "evidence": None})

    def check(name, L, expect, receipts=None):
        v = C.validate(L, base, receipts or rc)
        tags = {p[0] for p in v["problems"]}
        ok = (not v["problems"]) if not expect else set(expect) <= tags
        res.append({"control": name, "expect": sorted(expect), "problems": v["problems"][:4], "pass": ok})

    def fresh():
        O._BUF.clear()
        O._A.clear()

    fresh()
    check("P0 v001 + strict pilot receipts", copy.deepcopy(L0), [])
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"])
    check("P1 c021 <- c037 via g1", L, [])
    orb(L, "c069", "c037", ["g2"])
    check("P2 + c069 <- c037 via g2", L, [])
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"])
    orb(L, "c069", "c021", ["g2", "g1"])
    check("P3 chained c069 <- c021 via (g2, g1)", L, [])
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g2"])
    check("M1 wrong word", L, ["orbit image mismatch"])
    L = copy.deepcopy(L0)
    orb(L, "c022", "c037", ["g1"])
    check("M1b Codex exploit target c022 <- c037 via g1", L, ["orbit image mismatch"])
    L = copy.deepcopy(L0)
    orb(L, "c021", "c021", ["g1", "g1"])
    check("M2 source = leaf", L, ["orbit source/word invalid"])
    L = copy.deepcopy(L0)
    orb(L, "c032", "c016", ["g1"])
    check("M3 unsettled source (UNKNOWN c016)", L, ["orbit source not settled"])
    L = copy.deepcopy(L0)
    orb(L, "c021", "c069", ["g1", "g2", "g1"])
    orb(L, "c069", "c021", ["g1", "g2", "g1"])
    check("M4 two-node orbit cycle", L, ["cycle in the combined dependency graph"])
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g3"])
    check("M5 unknown generator", L, ["orbit source/word invalid"])
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"])
    L["leaves"].append({"id": "c021.L2.000", "depth": 2, "index": 0, "ancestor": "c021",
                        "lits": by0["c021"]["lits"] + C.canon(C.CHAIN[2], 0), "state": "UNSTARTED", "evidence": None})
    check("M6 orbit leaf with a child", L, ["orbit leaf must be a terminal CERTIFIED leaf with one orbit record"])
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"], extra=1)
    check("M7 extra evidence field", L, ["orbit leaf must be a terminal CERTIFIED leaf with one orbit record"])
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"])
    leaf(L, "c021")["evidence"]["automorphism_receipt"]["sha256"] = "1" * 64
    check("M8 foreign receipt hash", L, ["orbit evidence names another receipt"])
    # single-buffer regressions
    real = O._reader
    calls = {}
    g1path = O.PINS["g1"][0]
    pinned_g1 = real(g1path)
    swapped = bytearray(pinned_g1)
    swapped[57 * 4:58 * 4], swapped[106 * 4:107 * 4] = pinned_g1[106 * 4:107 * 4], pinned_g1[57 * 4:58 * 4]

    def counting_reader(path):
        calls[path] = calls.get(path, 0) + 1
        if path == g1path and calls[path] > 1:
            return bytes(swapped)
        return real(path)

    O._reader = counting_reader
    fresh()
    L = copy.deepcopy(L0)
    orb(L, "c022", "c037", ["g1"])
    check("R1 replace-between-reads: 2nd g1 read would be swapped; exploit still rejected", L, ["orbit image mismatch"])
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"])
    check("R2 replace-between-reads: genuine certificate still valid", L, [])
    res.append({"control": "R3 each artifact read exactly once", "calls": {os.path.basename(k): v for k, v in calls.items()},
                "pass": bool(calls) and all(v == 1 for v in calls.values()) and len(calls) == 4})

    def first_swapped(path):
        return bytes(swapped) if path == g1path else real(path)

    O._reader = first_swapped
    fresh()
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"])
    check("R4 substituted g1 bytes at the (only) read -> pin mismatch", L, ["automorphism pins"])
    O._reader = real
    fresh()
    # missing r2 regressions
    L = copy.deepcopy(L0)
    refine(L, "c016")
    orb(L, "c016.L2.032", "c016.L2.016", ["g1"])
    check("N1 full-path vs incremental literals (g1 moves root c016 to c032)", L, ["orbit image mismatch"])
    L = copy.deepcopy(L0)
    refine(L, "c016")
    orb(L, "c016.L2.064", "c016.L2.032", ["g2"])
    check("N1b stabiliser word with full path, source unsettled", L, ["orbit source not settled"])

    class BadReceipts:
        def get(self, f, s):
            r = rc.get(f, s)
            if r is not None and r.get("id") == "c037":
                r = dict(r)
                r["lits"] = list(r["lits"])
                r["lits"][0] = -r["lits"][0]
            return r

    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"])
    check("N2 strict source receipt literals differ from tree path", L,
          ["strict source literals differ from its leaf-CNF units", "receipt identity mismatch"], BadReceipts())
    P, V = O.arrays(base.sha)
    try:
        O.apply_word(P, V, ["g1"], [V + 1])
        bounds = False
    except ValueError:
        bounds = True
    try:
        O.apply_word(P, V, ["g1"], [0])
        bounds0 = False
    except ValueError:
        bounds0 = True
    res.append({"control": "N3 literal bounds (V+1 and 0 rejected)", "pass": bounds and bounds0})
    r = json.loads(O.verified("receipt"))
    s = json.loads(O.verified("secondpath"))
    t1 = copy.deepcopy(r)
    t1["verdict"]["S3_of_order_6"] = "True"
    t2 = copy.deepcopy(s)
    t2["verdict"] = 1
    t3 = copy.deepcopy(r)
    t3["verdict"]["controls_as_intended"] = "False"
    res.append({"control": "N4 truthy non-bool verdicts rejected; genuine accepted",
                "pass": (O.verdict_ok(r, s, base.sha) is True and O.verdict_ok(t1, s, base.sha) is False
                         and O.verdict_ok(r, t2, base.sha) is False and O.verdict_ok(t3, s, base.sha) is False)})
    L = copy.deepcopy(L0)
    refine(L, "c016", n=127)
    orb(L, "c032", "c016", ["g1"])
    check("N5 refined source with 127 children", L,
          ["REFINED leaf without exactly the 128 children", "orbit source not settled"])
    L = copy.deepcopy(L0)
    refine(L, "c016")
    orb(L, "c032", "c016", ["g1"])
    orb(L, "c016.L2.000", "c032", ["g1"])
    check("N6 combined refinement+orbit cycle", L, ["cycle in the combined dependency graph"])
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"])
    check("P4 regression after restoring the reader", L, [])
    out = {"argv": sys.argv, "k4_orbit_r3_sha256": hashlib.sha256(open(os.path.join(HERE, "k4_orbit_r3.py"), "rb")
                                                                  .read()).hexdigest(),
           "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(), "controls": res,
           "all_pass": all(x["pass"] for x in res)}
    with open(a.out, "x") as fh:
        json.dump(out, fh, indent=1)
    for x in res:
        print(("PASS " if x["pass"] else "FAIL ") + x["control"], json.dumps(x.get("problems", x.get("calls", "")))[:140])
    print("all_pass", out["all_pass"], len(res))


if __name__ == "__main__":
    main()
