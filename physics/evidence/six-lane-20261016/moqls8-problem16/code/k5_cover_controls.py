"""Mutation/positive controls for code/k5_cover.py validate() and load_ledger() (in memory; synthetic receipts are
served by a stub, nothing is written except the result file). Each control states the expected outcome.
python -B k5_cover_controls.py --base ../evidence/gram_dev_v1/GA5L_K5_sb2.cnf --out ../evidence/k5_split_v1/ledger/COVER_CONTROLS_v1.json
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
spec = importlib.util.spec_from_file_location("k5_cover", os.path.join(HERE, "k5_cover.py"))
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


class Stub:
    def __init__(self):
        self.d = {}

    def add(self, rel, rec):
        line = json.dumps(rec).encode()
        s = hashlib.sha256(line).hexdigest()
        self.d[(rel, s)] = rec
        return {"kind": "strict" if "id" in rec else "worker-root", "file": rel, "line_sha256": s}

    def get(self, rel, s):
        r = self.d.get((rel, s))
        return copy.deepcopy(r) if r is not None else None


def strict_rec(x, base, **over):
    r = {"id": x["id"], "depth": x["depth"], "index": x["index"], "ancestor": x["ancestor"], "lits": x["lits"],
         "base_cnf_sha256": base.sha, "cnf_sha256": base.leaf_sha(x["lits"]), "solver_returncode": 20,
         "solver_status_lines": ["s UNSATISFIABLE"], "checker_returncode": 0, "checker_status_lines": ["s VERIFIED"],
         "relay_errors": [], "feed_errors": [], "rss_guard_tripped": False, "self_exit": True}
    r.update(over)
    return r


def init(base):
    return {"schema": C.SCHEMA, "version": 1, "base_cnf_sha256": base.sha, "base_vars": base.nv,
            "base_clauses": base.nc, "chain": {str(k): v for k, v in C.CHAIN.items()},
            "leaves": [{"id": C.root_id(b), "depth": 1, "index": b, "ancestor": None,
                        "lits": C.canon(C.CHAIN[1], b), "state": "UNSTARTED", "evidence": None} for b in range(128)]}


def certify_all(L, base, st, skip=()):
    for x in L["leaves"]:
        if x["state"] == "UNSTARTED" and x["id"] not in skip:
            x["state"], x["evidence"] = "CERTIFIED", st.add("syn.jsonl", strict_rec(x, base))


def refine(L, rid):
    x = next(y for y in L["leaves"] if y["id"] == rid)
    x["state"] = "REFINED"
    for b in range(128):
        L["leaves"].append({"id": C.child_id(rid, x["depth"] + 1, b), "depth": x["depth"] + 1, "index": b,
                            "ancestor": rid, "lits": x["lits"] + C.canon(C.CHAIN[x["depth"] + 1], b),
                            "state": "UNSTARTED", "evidence": None})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    base = C.Base(a.base)
    res = []

    def check(name, L, st, expect_problem, expect_complete=False):
        v = C.validate(L, base, st)
        got_problem = bool(v["problems"])
        ok = (got_problem == expect_problem) and (expect_problem or v["complete"] == expect_complete)
        res.append({"control": name, "expect_problem": expect_problem, "expect_complete": expect_complete,
                    "problems": v["problems"][:3], "complete": v["complete"], "pass": ok})

    st = Stub()
    L0 = init(base)
    check("P0 init ledger valid, incomplete", L0, st, False, False)
    L = copy.deepcopy(L0)
    del L["leaves"][42]
    check("M1 missing root c042", L, st, True)
    L = copy.deepcopy(L0)
    L["leaves"].append(copy.deepcopy(L["leaves"][10]))
    check("M2 duplicate root c010", L, st, True)
    L = copy.deepcopy(L0)
    L["leaves"][5]["lits"][3] *= -1
    check("M3 root literal flipped", L, st, True)
    L = copy.deepcopy(L0)
    L["chain"]["3"][0] += 1
    check("M4 chain altered", L, st, True)
    L = copy.deepcopy(L0)
    L["leaves"][16]["state"], L["leaves"][16]["evidence"] = "UNKNOWN", st.add(
        "w.jsonl", {"cube": 16, "lits": L["leaves"][16]["lits"], "cnf_sha256": base.leaf_sha(L["leaves"][16]["lits"]),
                    "solver_status": "UNKNOWN"})
    check("P5 worker-root UNKNOWN root accepted", L, st, False, False)
    Lr = copy.deepcopy(L)
    refine(Lr, "c016")
    check("P6 refined c016 + 128 children valid", Lr, st, False, False)
    L = copy.deepcopy(Lr)
    L["leaves"].pop()
    check("M7 refined leaf with 127 children", L, st, True)
    L = copy.deepcopy(Lr)
    L["leaves"][-1]["lits"][-1] *= -1
    check("M8 child literal flipped", L, st, True)
    L = copy.deepcopy(Lr)
    L["leaves"][-1]["lits"] = L["leaves"][-1]["lits"][:7] + C.canon(C.CHAIN[3], 127)
    check("M9 child built from the wrong depth list", L, st, True)
    L = copy.deepcopy(L0)
    x = L["leaves"][20]
    x["state"], x["evidence"] = "CERTIFIED", st.add("syn.jsonl", strict_rec(x, base, solver_returncode=0))
    check("M10 CERTIFIED with solver exit 0", L, st, True)
    L = copy.deepcopy(L0)
    x = L["leaves"][21]
    x["state"], x["evidence"] = "CERTIFIED", st.add("syn.jsonl", strict_rec(
        x, base, checker_status_lines=["s VERIFIED", "s NOT VERIFIED"]))
    check("M11 CERTIFIED with NOT VERIFIED line", L, st, True)
    L = copy.deepcopy(L0)
    x = L["leaves"][22]
    x["state"], x["evidence"] = "CERTIFIED", st.add("syn.jsonl", strict_rec(x, base, cnf_sha256="0" * 64))
    check("M12 receipt CNF hash mismatch", L, st, True)
    L = copy.deepcopy(L0)
    x = L["leaves"][23]
    x["state"], x["evidence"] = "CERTIFIED", st.add("syn.jsonl", strict_rec(x, base, base_cnf_sha256="1" * 64))
    check("M13 receipt base hash mismatch", L, st, True)
    L = copy.deepcopy(L0)
    x = L["leaves"][24]
    x["state"], x["evidence"] = "CERTIFIED", st.add("syn.jsonl", strict_rec(L["leaves"][25], base))
    check("M14 receipt of another leaf (stale id/lits)", L, st, True)
    L = copy.deepcopy(L0)
    x = L["leaves"][26]
    x["state"], x["evidence"] = "CERTIFIED", st.add("w.jsonl", {"cube": 26, "lits": x["lits"], "cnf_sha256":
                                                                base.leaf_sha(x["lits"]), "solver_status": "UNSAT"})
    check("M15 CERTIFIED from a worker-root positive record", L, st, True)
    L = copy.deepcopy(L0)
    x = L["leaves"][27]
    x["state"], x["evidence"] = "UNKNOWN", st.add("w.jsonl", {"cube": 27, "lits": x["lits"], "cnf_sha256":
                                                              base.leaf_sha(x["lits"]), "solver_status": "UNSAT"})
    check("M16 UNKNOWN root from a worker-root positive record", L, st, True)
    L = copy.deepcopy(L0)
    x = L["leaves"][28]
    x["state"], x["evidence"] = "CERTIFIED", {"kind": "strict", "file": "syn.jsonl", "line_sha256": "f" * 64}
    check("M17 receipt line not found", L, st, True)
    L = copy.deepcopy(L0)
    x = L["leaves"][29]
    x["state"], x["evidence"] = "UNKNOWN", st.add("syn.jsonl", strict_rec(x, base))
    check("M18 strictly certified leaf recorded UNKNOWN", L, st, True)
    L = copy.deepcopy(L0)
    x = L["leaves"][30]
    x["evidence"] = st.add("syn.jsonl", strict_rec(x, base))
    check("M19 UNSTARTED leaf with evidence", L, st, True)
    L = copy.deepcopy(L0)
    x = L["leaves"][31]
    x["state"], x["evidence"] = "CERTIFIED", st.add("syn.jsonl", strict_rec(x, base, rss_guard_tripped=True))
    check("M20 CERTIFIED after an RSS-guard trip", L, st, True)
    L = copy.deepcopy(L0)
    x = L["leaves"][32]
    rr = strict_rec(x, base)
    del rr["feed_errors"]
    x["state"], x["evidence"] = "CERTIFIED", st.add("syn.jsonl", rr)
    check("M21 CERTIFIED with an absent strict field", L, st, True)
    L = copy.deepcopy(Lr)
    certify_all(L, base, st)
    check("P22 synthetic: all terminal leaves strictly certified -> complete", L, st, False, True)
    L2 = copy.deepcopy(Lr)
    certify_all(L2, base, st, skip={"c016.L2.077"})
    check("P23 synthetic: one child UNSTARTED -> valid but incomplete", L2, st, False, False)
    L = copy.deepcopy(Lr)
    certify_all(L, base, st)
    for y in L["leaves"]:
        if y["id"] == "c016.L2.005":
            y["state"] = "REFINED"
    check("M24 REFINED leaf without children", L, st, True)
    raw = json.dumps({"schema": C.SCHEMA, "leaves": [], "leaves ": []}).replace('"leaves ": []', '"leaves": [1]')
    tmp_ok = False
    try:
        C._nodup(json.loads(raw, object_pairs_hook=lambda p: p))
    except ValueError:
        tmp_ok = True
    res.append({"control": "M25 duplicate JSON key rejected by load hook", "pass": tmp_ok})
    out = {"argv": sys.argv, "k5_cover_sha256": hashlib.sha256(open(os.path.join(HERE, "k5_cover.py"), "rb").read()
                                                               ).hexdigest(),
           "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(), "base_cnf_sha256": base.sha,
           "controls": res, "all_pass": all(r["pass"] for r in res)}
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "x") as fh:
        json.dump(out, fh, indent=1)
    for r in res:
        print(("PASS " if r["pass"] else "FAIL ") + r["control"], json.dumps(r.get("problems", ""))[:120])
    print("all_pass", out["all_pass"])


if __name__ == "__main__":
    main()
