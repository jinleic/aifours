#!/usr/bin/env python3
"""route1_report.py (parent moqls7-k1-parent-check-v1): claim section 3 (net-class completeness).
Inputs: lane nets7_classes.json (data), parent C outputs route1/part1.out (per-net frames/|Aut|/canonical form) and
route1/full_run.out (full enumeration of reduced 2-MOLS(7) lists), the parent-fetched Egan-Wanless text.
Own code only. Writes route1/route1-report.json."""
import itertools, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mynet, runlib

D = os.path.dirname(HERE)
LANE = os.path.join(D, "inputs", "lane")
R1 = os.path.join(D, "route1")
nets, data = mynet.load_nets(os.path.join(LANE, "evidence", "nets7_classes.json"))
res = {"started": runlib.now(), "inputs": {}}
for rel in ("inputs/lane/evidence/nets7_classes.json", "route1/c/k1par_nets.c", "route1/c/k1par_nets", "route1/c/k1par_nets_v2.c",
            "route1/c/k1par_nets_v2", "route1/c/nets7.txt", "route1/part1.out", "route1/full_run.out",
            "route1/ew/1406.3681v2.pdf", "route1/ew/1406.3681v2.parent.layout.txt"):
    res["inputs"][rel] = runlib.sha_file(os.path.join(D, rel))

# 1. validity
res["valid_4nets"] = [mynet.check_net(n) for n in nets]
# nets7.txt must be exactly the JSON nets
txt = [list(map(int, l.split())) for l in open(os.path.join(R1, "c", "nets7.txt"))]
res["nets7_txt_matches_json"] = txt == [[v for q in n for v in q] for n in nets]

# 2. part1 parse
part1 = {}
for line in open(os.path.join(R1, "part1.out")):
    t = line.split()
    if t and t[0] == "net" and len(t) > 3 and t[2] == "frames":
        i = int(t[1])
        part1[i] = {"frames": int(t[3]), "invalid": int(t[5]), "distinct": int(t[7]), "aut_explicit": int(t[9]),
                    "key_equal_frames": int(t[11]), "orbit_x_aut": int(t[13]), "canon98": t[15]}
    if t and t[0] == "union_size":
        res["union_size"], res["cross_class_duplicates"] = int(t[1]), int(t[3])
cls = data["classes"]
rows = []
for i in range(7):
    k98 = part1[i]["canon98"]
    L1, L2 = k98[:49], k98[49:]
    k78 = "".join(L1[7 * r + c] for r in range(1, 7) for c in range(1, 7)) + "".join(L2[7 * r + c] for r in range(1, 7) for c in range(7))
    rows.append({"class": i, "claim_par": cls[i]["par"], "claim_orbit": cls[i]["orbit"], "claim_maximal": cls[i]["maximal"],
                 **part1[i], "canon78_from_parent": k78, "lane_key": cls[i]["key"], "canon_equals_lane_key": k78 == cls[i]["key"],
                 "par_matches": part1[i]["aut_explicit"] == cls[i]["par"] == part1[i]["key_equal_frames"],
                 "orbit_matches": part1[i]["distinct"] == cls[i]["orbit"] == 846720 // cls[i]["par"],
                 "orbit_stabiliser": part1[i]["distinct"] * part1[i]["aut_explicit"] == 846720})
res["per_class"] = rows
res["sum_orbits"] = sum(r["distinct"] for r in rows)
res["sum_orbits_maximal_per_claim_flags"] = sum(r["distinct"] for r in rows if r["claim_maximal"])

# 3. own invariants
def transversals(net, classes):
    """point sets meeting every line of the given classes exactly once (one point per class-classes[0] line)"""
    out = []
    first = classes[0]
    byline = [[p for p in range(49) if net[p][first] == b] for b in range(7)]
    def rec(b, chosen, used):
        if b == 7:
            out.append(tuple(chosen))
            return
        for p in byline[b]:
            if all(net[p][c] not in used[c] for c in classes[1:]):
                for c in classes[1:]:
                    used[c].add(net[p][c])
                rec(b + 1, chosen + [p], used)
                for c in classes[1:]:
                    used[c].discard(net[p][c])
    rec(0, [], {c: set() for c in classes})
    return out
def intercalates(net, a, b, c):
    cell = {(net[p][a], net[p][b]): net[p][c] for p in range(49)}
    n = 0
    for r1, r2 in itertools.combinations(range(7), 2):
        for c1, c2 in itertools.combinations(range(7), 2):
            if cell[(r1, c1)] == cell[(r2, c2)] and cell[(r1, c2)] == cell[(r2, c1)]:
                n += 1
    return n
def partitions(T):
    """number of partitions of the 49 points into 7 pairwise disjoint transversals from T"""
    T = [frozenset(t) for t in T]
    cnt = 0
    def rec(covered, start_point):
        nonlocal cnt
        if len(covered) == 49:
            cnt += 1
            return
        p = min(set(range(49)) - covered)
        for t in T:
            if p in t and not (t & covered):
                rec(covered | t, None)
    rec(frozenset(), None)
    return cnt
inv = []
for i, net in enumerate(nets):
    Tc = transversals(net, [0, 1, 2, 3])
    aspects = []
    for omit in range(4):
        cl = [c for c in range(4) if c != omit]
        aspects.append((intercalates(net, *cl), len(transversals(net, cl))))
    inv.append({"class": i, "aut": part1[i]["aut_explicit"], "common_transversals": len(Tc),
                "extensions_to_5net(parallel classes of common transversals)": partitions(Tc),
                "aspects_sorted(intercalates,transversals)": sorted(aspects)})
res["invariants"] = inv
keys = [json.dumps([x["aut"], x["common_transversals"], x["aspects_sorted(intercalates,transversals)"]]) for x in inv]
res["invariants_pairwise_distinct"] = len(set(keys)) == 7
res["maximality_from_own_count"] = [x["extensions_to_5net(parallel classes of common transversals)"] == 0 for x in inv]
res["maximality_matches_claim"] = res["maximality_from_own_count"] == [c["maximal"] for c in cls]
res["lane_transversals_field_matches_own_common_transversals"] = [c["transversals"] for c in cls] == [x["common_transversals"] for x in inv]

# 4. full enumeration
full = {"progress_lines": 0}
fr = os.path.join(R1, "full_run.out")
for line in open(fr):
    t = line.split()
    if not t:
        continue
    if t[0] == "progress":
        full["progress_lines"] += 1
    elif t[0] == "reduced_LS7":
        full.update({t[j]: int(t[j + 1]) for j in range(0, len(t), 2)})
    elif t[0] == "class":
        full.setdefault("class_hits", {})[t[1]] = {"hits": int(t[3]), "orbit": int(t[5])}
    elif t[0] in ("UNLISTED", "CROSS_DUP"):
        full.setdefault("anomalies", []).append(line.strip())
res["full_enumeration"] = full
fe_ok = (full.get("reduced_LS7") == 16942080 and full.get("reduced_lists") == 342480 and full.get("unlisted") == 0
         and full.get("union_elements_never_hit") == 0 and full.get("union_elements_hit_more_than_once") == 0
         and all(v["hits"] == v["orbit"] for v in full.get("class_hits", {}).values()) and len(full.get("class_hits", {})) == 7
         and "anomalies" not in full)
res["full_enumeration_ok"] = fe_ok

# 5. Egan-Wanless quotes (parent-fetched text, 1-based line numbers)
ew = open(os.path.join(R1, "ew", "1406.3681v2.parent.layout.txt")).read().split("\n")
def q(a, b):
    return {"lines": "%d-%d" % (a, b), "text": "\n".join(ew[a - 1:b])}
res["EW_quotes"] = {"paratopism_and_par": q(143, 153), "reduced_definition": q(185, 187), "theorem_3_1": q(355, 361),
                    "theorem_3_2": q(382, 397), "table5_row_7_2": q(708, 708), "table5_caption": q(721, 721),
                    "table6_row_7_2": q(755, 755), "table6_caption": q(776, 776), "table7_row_7_2": q(791, 791),
                    "table7_caption": q(804, 804), "table8_row_7_2": q(839, 839), "table8_caption": q(860, 860),
                    "tables_text": q(726, 738)}
res["EW_numbers_used"] = {"Theorem3.2_factor_n!n(k+2)(k+1)k_for_n7_k2": 5040 * 7 * 4 * 3 * 2,
                          "Table6_RS_2_7": 342480, "Table5_RS_2_7_maximal": 341880, "Table6_species": 7, "Table5_species": 5}
ok = (all(v[0] for v in res["valid_4nets"]) and res["nets7_txt_matches_json"] and all(r["par_matches"] and r["orbit_matches"]
      and r["orbit_stabiliser"] and r["canon_equals_lane_key"] and r["invalid"] == 0 for r in rows)
      and res["union_size"] == 342480 and res["cross_class_duplicates"] == 0 and res["sum_orbits"] == 342480
      and res["sum_orbits_maximal_per_claim_flags"] == 341880 and res["maximality_matches_claim"])
res["route1_mandatory_pass"] = ok
res["finished"] = runlib.now()
with open(os.path.join(R1, "route1-report.json"), "x") as f:
    json.dump(res, f, indent=1)
print(json.dumps({k: res[k] for k in ("valid_4nets", "nets7_txt_matches_json", "union_size", "cross_class_duplicates", "sum_orbits",
                                     "sum_orbits_maximal_per_claim_flags", "invariants_pairwise_distinct", "maximality_matches_claim",
                                     "lane_transversals_field_matches_own_common_transversals", "full_enumeration_ok", "route1_mandatory_pass")}))
for r in rows:
    print(r["class"], r["distinct"], r["aut_explicit"], r["key_equal_frames"], r["par_matches"], r["orbit_matches"], r["canon_equals_lane_key"])
for x in inv:
    print(x)
print(full)
