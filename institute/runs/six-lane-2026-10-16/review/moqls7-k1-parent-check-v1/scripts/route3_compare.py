#!/usr/bin/env python3
"""route3_compare.py (parent moqls7-k1-parent-check-v1): compare the parent's own non-SAT enumerations (k1par_enum fc and
plain modes) with the lane's SAT model lists (encoders A and B) and with the frame lemma (own mynet.frame_allowed).
Lane files are read as data only."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mynet, runlib

D = os.path.dirname(HERE)
LANE = os.path.join(D, "inputs", "lane")
R3 = os.path.join(D, "route3")


def parse(path):
    sols, init, meta = {}, {}, {}
    for line in open(path):
        t = line.split()
        if not t:
            continue
        if t[0] == "net" and t[2] == "initdom":
            init[int(t[1])] = {int(a): (int(b), int(c)) for a, b, c in (x.split(":") for x in t[3:])}
        elif t[0] == "net" and t[2] == "mode":
            meta[int(t[1])] = {"mode": t[3], "solutions": int(t[5]), "nodes": int(t[7])}
            sols.setdefault(int(t[1]), [])
        elif t[0] == "sol":
            sols.setdefault(int(t[1]), []).append(tuple(frozenset(k for k in range(7) if int(v) >> k & 1) for v in t[3:]))
    return sols, init, meta


nets, data = mynet.load_nets(os.path.join(LANE, "evidence", "nets7_classes.json"))
SA = json.load(open(os.path.join(LANE, "evidence", "k1A", "summary.json")))
SB = json.load(open(os.path.join(LANE, "evidence", "k1B", "summaryB.json")))
fc, init, mfc = parse(os.path.join(R3, "enum_fc.out"))
pl, _, mpl = parse(os.path.join(R3, "enum_plain.out"))
res = {"started": runlib.now(), "inputs": {
    "enum_fc.out": runlib.sha_file(os.path.join(R3, "enum_fc.out")),
    "enum_plain.out": runlib.sha_file(os.path.join(R3, "enum_plain.out")),
    "k1par_enum.c": runlib.sha_file(os.path.join(R3, "c", "k1par_enum.c")),
    "k1par_enum(bin)": runlib.sha_file(os.path.join(R3, "c", "k1par_enum")),
    "lane summary.json": runlib.sha_file(os.path.join(LANE, "evidence", "k1A", "summary.json")),
    "lane summaryB.json": runlib.sha_file(os.path.join(LANE, "evidence", "k1B", "summaryB.json"))}, "classes": []}
allok = True
for i in range(7):
    net = nets[i]
    frame, label, allowed = mynet.frame_allowed(net)
    # frame lemma as it emerged from F2 propagation: off-frame domains = all 15 nonempty subsets of a 4-set = A(p)
    fl = all((init[i][p] == (1, 1 << label[p])) if p in label else
             (init[i][p][0] == 15 and init[i][p][1] == sum(1 << k for k in allowed[p]) and len(allowed[p]) == 4)
             for p in range(49))
    A = set()
    for m in SA["classes"][i]["models"]:
        sp = {p: set() for p in range(49)}
        for t in m:
            p, k = t.split(":")
            sp[int(p)].add(int(k))
        A.add(tuple(frozenset(sp[p]) for p in range(49)))
    B = set()
    for m in SB["classes"][i]["models"]:
        sp = {int(t.split(":")[0]): frozenset(int(c) for c in t.split(":")[1]) for t in m}
        B.add(tuple(sp[p] for p in range(49)))
    F, Pn = set(fc.get(i, [])), set(pl.get(i, []))
    viol = [len(mynet.pattern_violations(net, {p: set(s[p]) for p in range(49)}, label, allowed)) for s in F]
    w4 = [s for s in F if any(len(x) > 1 for x in s)]
    w4_is_A = [all(s[p] == allowed[p] for p in range(49)) for s in w4]
    rec = {"class": i, "frame_lemma_emerges_from_F2": fl, "n_fc": len(F), "n_plain": len(Pn), "n_lane_A": len(A),
           "n_lane_B": len(B), "fc_eq_plain": F == Pn, "fc_eq_A": F == A, "fc_eq_B": F == B,
           "no_duplicate_solutions": len(F) == mfc[i]["solutions"] and len(Pn) == mpl[i]["solutions"],
           "own_evaluator_violations": viol, "weight_sets": sorted(sorted({len(x) for x in s}) for s in F),
           "nonclassical_patterns": len(w4), "nonclassical_equals_A(p)_everywhere": w4_is_A,
           "nodes_fc": mfc[i]["nodes"], "nodes_plain": mpl[i]["nodes"]}
    ok = fl and F == Pn == A == B and rec["no_duplicate_solutions"] and all(v == 0 for v in viol)
    rec["pass"] = ok
    allok &= ok
    res["classes"].append(rec)
res["counts_fc"] = [r["n_fc"] for r in res["classes"]]
res["expected_counts"] = [0, 0, 0, 0, 0, 4, 5]
res["route3_pass"] = allok and res["counts_fc"] == res["expected_counts"]
res["finished"] = runlib.now()
with open(os.path.join(R3, "route3-compare.json"), "x") as f:
    json.dump(res, f, indent=1)
print(json.dumps({"counts": res["counts_fc"], "pass": res["route3_pass"]}))
for r in res["classes"]:
    print({k: v for k, v in r.items() if k not in ("own_evaluator_violations",)})
