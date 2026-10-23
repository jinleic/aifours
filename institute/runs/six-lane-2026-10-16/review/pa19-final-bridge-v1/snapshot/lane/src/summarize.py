#!/usr/bin/env python3
"""Summarize lane status from result files into STATUS.json (read-only over results)."""
import collections
import glob
import json
import os

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(pattern):
    out = []
    for f in sorted(glob.glob(os.path.join(LANE, pattern))):
        if f.endswith(".check.json"):
            continue
        out.append(json.load(open(f)))
    return out


def main():
    st = {}
    q0 = load("cases19q0/results/g*.json")
    chk = {json.load(open(f))["tag"]: json.load(open(f))
           for f in glob.glob(os.path.join(LANE, "cases19q0/results/*.check.json"))}
    m2 = load("m2q0b/results/g*.json")
    st["E0_ms00"] = {
        "cases": 486,
        "M1_q0_status": dict(collections.Counter(r["status"] for r in q0)),
        "M1_q0_drat_and_lrat_checked_ok": sum(1 for t, c in chk.items() if c["ok"]),
        "M2_q0b_status": dict(collections.Counter(r["status"] for r in m2)),
        "M2_q0b_lrat_checked_ok": sum(1 for r in m2 if r.get("lrat_verified")),
    }
    sk = load("cases19skel/results/ms*.json")
    pc = {}
    for f in glob.glob(os.path.join(LANE, "cases19skel/proofcheck/*.json")):
        o = json.load(open(f))
        pc[o["tag"]] = o
    idx = json.load(open(os.path.join(LANE, "cases19skel/index.json")))
    per = collections.defaultdict(lambda: {"cases": 0, "pass1": collections.Counter(), "proof_ok": 0,
                                           "proof_fail": 0})
    for c in idx["cases"]:
        per[c["multiset"]]["cases"] += 1
    for r in sk:
        m = r["multiset"]
        per[m]["pass1"][r["status"]] += 1
        o = pc.get(r["tag"])
        if o is not None:
            per[m]["proof_ok" if o["ok"] else "proof_fail"] += 1
    st["skeleton_split"] = {"ms%02d" % m: {"cases": v["cases"], "pass1_noproof_30s": dict(v["pass1"]),
                                           "not_run": v["cases"] - sum(v["pass1"].values()),
                                           "drat_lrat_checked_ok": v["proof_ok"],
                                           "proof_check_failures": v["proof_fail"]}
                            for m, v in sorted(per.items())}
    st["unknown_tags"] = sorted(r["tag"] for r in sk if r["status"] == "UNKNOWN")
    st["sat_tags"] = sorted(r["tag"] for r in sk + q0 if r["status"] == "SAT")
    json.dump(st, open(os.path.join(LANE, "STATUS.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in st.items() if k != "unknown_tags"}, indent=1))
    print("unknown:", len(st["unknown_tags"]))


if __name__ == "__main__":
    main()
