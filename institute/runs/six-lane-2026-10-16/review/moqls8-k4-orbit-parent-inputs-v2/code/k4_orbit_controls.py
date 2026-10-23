"""In-memory controls for code/k4_orbit_r2.py (nothing is written except the result file; the K4 ledger v001 and the
strict pilot receipts are read only). Ledger states are modified IN MEMORY to exercise the orbit rule:
positive: c021 ← c037 via g1; c069 ← c037 via g2; chained c069 ← c021 via (g2, g1);
mutations: wrong word; source = leaf; unsettled source (UNKNOWN c016); two-node cycle; unknown generator; orbit leaf
with a child; tampered array pin; extra evidence field; foreign receipt hash.
python -B k4_orbit_controls.py --out ../evidence/k4_split_v1/auto_r3/ORBIT_VALIDATOR_CONTROLS.json
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
    O = load("k4_orbit_r2")
    K = load("k4_cover")
    C = O.install(K.configure(K.load_cover()))
    base = C.Base(F4)
    L0, _ = C.load_ledger(LEDGER)
    byid = {x["id"]: x for x in L0["leaves"]}
    rel = "pilot/RESULTS.jsonl"
    for line in open(os.path.join(C.SPLIT_DIR, rel), "rb").read().split(b"\n"):
        if line.strip():
            r = json.loads(line)
            x = byid[r["id"]]
            x["state"] = "CERTIFIED" if C.strict_ok(r) else "UNKNOWN"
            x["evidence"] = {"kind": "strict", "file": rel, "line_sha256": hashlib.sha256(line).hexdigest()}
    rc = C.Receipts()
    res = []

    def orb(L, leaf, src, word, **extra):
        x = next(y for y in L["leaves"] if y["id"] == leaf)
        x["state"] = "CERTIFIED"
        x["evidence"] = {"kind": "orbit", "source": src, "word": word,
                         "automorphism_receipt": {"path": "evidence/k4_split_v1/auto_r3/RECEIPT.json",
                                                  "sha256": O.PINS["receipt"][1]}}
        x["evidence"].update(extra)

    def check(name, L, expect_problem):
        v = C.validate(L, base, rc)
        ok = bool(v["problems"]) == expect_problem
        res.append({"control": name, "expect_problem": expect_problem, "problems": v["problems"][:3],
                    "orbit_certified": v.get("orbit_certified"), "pass": ok})

    check("P0 v001 + strict pilot receipts", copy.deepcopy(L0), False)
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"])
    check("P1 c021 <- c037 via g1", L, False)
    orb(L, "c069", "c037", ["g2"])
    check("P2 + c069 <- c037 via g2", L, False)
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"])
    orb(L, "c069", "c021", ["g2", "g1"])
    check("P3 chained c069 <- c021 via (g2, g1)", L, False)
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g2"])
    check("M1 wrong word", L, True)
    L = copy.deepcopy(L0)
    orb(L, "c021", "c021", ["g1", "g1"])
    check("M2 source = leaf", L, True)
    L = copy.deepcopy(L0)
    orb(L, "c032", "c016", ["g1"])
    check("M3 unsettled source (UNKNOWN c016)", L, True)
    L = copy.deepcopy(L0)
    orb(L, "c021", "c069", ["g1", "g2", "g1"])
    orb(L, "c069", "c021", ["g1", "g2", "g1"])
    check("M4 two-node cycle", L, True)
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g3"])
    check("M5 unknown generator", L, True)
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"])
    L["leaves"].append({"id": "c021.L2.000", "depth": 2, "index": 0, "ancestor": "c021",
                        "lits": byid["c021"]["lits"] + C.canon(C.CHAIN[2], 0), "state": "UNSTARTED", "evidence": None})
    check("M6 orbit leaf with a child", L, True)
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"])
    saved = O.PINS["g1"]
    O.PINS["g1"] = (saved[0], "0" * 64)
    O._A.clear()
    check("M7 tampered array pin", L, True)
    O.PINS["g1"] = saved
    O._A.clear()
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"], extra=1)
    check("M8 extra evidence field", L, True)
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"])
    next(y for y in L["leaves"] if y["id"] == "c021")["evidence"]["automorphism_receipt"]["sha256"] = "1" * 64
    check("M9 foreign receipt hash", L, True)
    L = copy.deepcopy(L0)
    orb(L, "c021", "c037", ["g1"])
    check("P4 after restoring pins (regression)", L, False)
    out = {"argv": sys.argv, "k4_orbit_r2_sha256": hashlib.sha256(open(os.path.join(HERE, "k4_orbit_r2.py"), "rb")
                                                                  .read()).hexdigest(),
           "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(), "controls": res,
           "all_pass": all(r["pass"] for r in res)}
    with open(a.out, "x") as fh:
        json.dump(out, fh, indent=1)
    for r in res:
        print(("PASS " if r["pass"] else "FAIL ") + r["control"], json.dumps(r["problems"])[:150])
    print("all_pass", out["all_pass"])


if __name__ == "__main__":
    main()
