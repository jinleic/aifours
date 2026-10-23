#!/usr/bin/env python3
"""route4_phase.py (parent moqls7-k1-parent-check-v1): exact parent recomputation of claim section 5 (phase cycle).
Own code; lane files read as data only. Integer arithmetic throughout; phases measured in units of pi.
 1. class-6 net == {7x+y : (x, y, y-x, y-3x) mod 7} literally (point index 7x+y);
 2. frame allowed sets A(p) (own mynet) == {y - x t : t in {2,4,5,6}} for every p=(x,y), x != 0;
 3. the 7 table rows: p, q collinear exactly on the stated class, A(p) & A(q) == stated 2-set;
 4. each row gives the relation  th[q,k] - th[p,k] - th[q,k'] + th[p,k'] = 1 (units of pi, mod 2), from
    conj(c_pk) c_qk + conj(c_pk') c_qk' = 0 with all four coefficients nonzero; signed sum with the table signs is the
    zero vector while the right-hand side is sum(signs) (odd) => 0 = odd*pi mod 2pi, contradiction;
    also: enumerate all 2^7 sign vectors and report which cancel (any cancelling +-1 combination of 7 rows has odd RHS);
 5. the non-classical model of class 6 from lane encoders A and B and from the parent enumerator equals the weight-4
    pattern supp(p) = A(p) for p off the frame line;
 6. extra: all collinear 2-overlap relations of the weight-4 pattern, and a GF(2)/integer consistency summary."""
import itertools, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mynet, runlib

D = os.path.dirname(HERE)
LANE = os.path.join(D, "inputs", "lane")
OUT = os.path.join(D, "route4")
nets, data = mynet.load_nets(os.path.join(LANE, "evidence", "nets7_classes.json"))
net = nets[6]
res = {"started": runlib.now(), "checks": {}}
res["checks"]["net6_origin_field"] = data["classes"][6]["origin"]
lit = all(net[7 * x + y] == (x, y, (y - x) % 7, (y - 3 * x) % 7) for x in range(7) for y in range(7))
res["checks"]["1_net6_equals_(x,y,y-x,y-3x)"] = lit
frame, label, A = mynet.frame_allowed(net)
res["checks"]["frame_points"] = sorted(frame)
res["checks"]["frame_labels_are_y"] = all(label[7 * 0 + y] == y for y in range(7))
formula = all(A[7 * x + y] == frozenset((y - x * t) % 7 for t in (2, 4, 5, 6)) for x in range(1, 7) for y in range(7))
res["checks"]["2_A(x,y)=y-x{2,4,5,6}"] = formula
TABLE = [(+1, 29, 28, 0, {5, 6}), (-1, 33, 28, 0, {4, 6}), (+1, 34, 28, 0, {4, 5}), (-1, 34, 29, 0, {0, 5}),
         (+1, 33, 26, 1, {4, 6}), (+1, 34, 26, 2, {0, 4}), (-1, 29, 26, 3, {0, 6})]
coords = {29: (4, 1), 28: (4, 0), 33: (4, 5), 34: (4, 6), 26: (3, 5)}
rows3 = []
rels = []
for sign, p, q, cls, sh in TABLE:
    common = [c for c in range(4) if net[p][c] == net[q][c]]
    ov = set(A[p] & A[q])
    xy_ok = all(divmod(t, 7) == coords[t] for t in (p, q))
    k, k2 = sorted(ov) if len(ov) == 2 else (None, None)
    rel = {(q, k): 1, (p, k): -1, (q, k2): -1, (p, k2): 1} if k is not None else {}
    rels.append((sign, rel))
    rows3.append({"sign": sign, "p": p, "q": q, "xy_ok": xy_ok, "common_classes": common, "stated_class": cls,
                  "overlap": sorted(ov), "stated_overlap": sorted(sh), "p_off_frame": p not in label,
                  "q_off_frame": q not in label,
                  "ok": common == [cls] and ov == sh and xy_ok and p not in label and q not in label})
res["checks"]["3_rows"] = rows3
res["checks"]["3_all_rows_ok"] = all(r["ok"] for r in rows3)
tot = {}
for sign, rel in rels:
    for v, c in rel.items():
        tot[v] = tot.get(v, 0) + sign * c
res["checks"]["4_signed_sum_nonzero_terms"] = {"%d:%d" % v: c for v, c in tot.items() if c != 0}
res["checks"]["4_signed_sum_is_zero_vector"] = all(c == 0 for c in tot.values())
rhs = sum(s for s, _ in rels)
res["checks"]["4_rhs_units_of_pi"] = rhs
res["checks"]["4_rhs_odd"] = rhs % 2 == 1
canc = []
for signs in itertools.product((1, -1), repeat=7):
    t = {}
    for s, (_, rel) in zip(signs, rels):
        for v, c in rel.items():
            t[v] = t.get(v, 0) + s * c
    if all(c == 0 for c in t.values()):
        canc.append(list(signs))
res["checks"]["4_all_cancelling_sign_vectors"] = canc
res["checks"]["4_table_signs_among_them"] = [s for s, _ in rels] in canc
res["checks"]["4_every_cancelling_vector_has_odd_rhs"] = all(sum(s) % 2 == 1 for s in canc)
# verify the derivation numerically on random phases: each relation's LHS is exactly the phase defect of the 2-term
# orthogonality sum (sanity: for random phases, conj(c_pk)c_qk + conj(c_pk')c_qk' = 0 iff LHS = pi mod 2pi)
import cmath, random
random.seed(7)
okn = True
for _ in range(2000):
    th = {v: random.uniform(-3.2, 3.2) for v in itertools.product(range(49), range(7))}
    sign, rel = rels[random.randrange(7)]
    (q, k), (p, _k), (q2, k2), (p2, _k2) = [v for v in rel]
    # make the 2-term sum vanish by construction and check the relation value
    a, b = 0.7, 1.3
    th[(q, k2)] = th[(p, k2)] + (th[(q, k)] - th[(p, k)]) - cmath.pi
    s = a * b * cmath.exp(1j * (th[(q, k)] - th[(p, k)])) + a * b * cmath.exp(1j * (th[(q, k2)] - th[(p, k2)]))
    lhs = sum(c * th[v] for v, c in rel.items())
    okn &= abs(s) < 1e-9 and abs(((lhs / cmath.pi) - 1) % 2) < 1e-9
res["checks"]["4_numeric_sanity_relation_form"] = okn
# 5. non-classical model equality
SA = json.load(open(os.path.join(LANE, "evidence", "k1A", "summary.json")))
SB = json.load(open(os.path.join(LANE, "evidence", "k1B", "summaryB.json")))
w4 = {p: (frozenset([label[p]]) if p in label else A[p]) for p in range(49)}
nA = [m for m, w in zip(SA["classes"][6]["models"], SA["classes"][6]["model_weight_sets"]) if w != [1]]
nB = [m for m, w in zip(SB["classes"][6]["models"], SB["classes"][6]["model_weight_sets"]) if w != [1]]
def pa(m):
    sp = {p: set() for p in range(49)}
    for t in m:
        p, k = t.split(":")
        sp[int(p)].add(int(k))
    return {p: frozenset(v) for p, v in sp.items()}
def pb(m):
    return {int(t.split(":")[0]): frozenset(int(c) for c in t.split(":")[1]) for t in m}
own = json.load(open(os.path.join(D, "route3", "route3-compare.json")))
res["checks"]["5_lane_A_nonclassical_count"] = len(nA)
res["checks"]["5_lane_B_nonclassical_count"] = len(nB)
res["checks"]["5_lane_A_equals_weight4"] = len(nA) == 1 and pa(nA[0]) == w4
res["checks"]["5_lane_B_equals_weight4"] = len(nB) == 1 and pb(nB[0]) == w4
res["checks"]["5_parent_enumerator_equals_weight4"] = own["classes"][6]["nonclassical_equals_A(p)_everywhere"] == [True]
res["checks"]["5_weight4_passes_F1F4_own_evaluator"] = mynet.pattern_violations(net, {p: set(w4[p]) for p in range(49)}, label, A) == []
# 6. all collinear two-overlap relations of the weight-4 pattern
allrel = []
for c, b, pts in mynet.lines(net):
    for p, q in itertools.combinations(pts, 2):
        ov = sorted(w4[p] & w4[q])
        if len(ov) == 2:
            allrel.append((p, q, c, ov))
res["checks"]["6_number_of_two_overlap_collinear_pairs"] = len(allrel)
res["checks"]["6_overlap_size_histogram"] = {}
for c, b, pts in mynet.lines(net):
    for p, q in itertools.combinations(pts, 2):
        n = len(w4[p] & w4[q])
        res["checks"]["6_overlap_size_histogram"][str(n)] = res["checks"]["6_overlap_size_histogram"].get(str(n), 0) + 1
res["route4_pass"] = (lit and formula and res["checks"]["3_all_rows_ok"] and res["checks"]["4_signed_sum_is_zero_vector"]
                      and res["checks"]["4_rhs_odd"] and res["checks"]["4_table_signs_among_them"]
                      and res["checks"]["5_lane_A_equals_weight4"] and res["checks"]["5_lane_B_equals_weight4"]
                      and res["checks"]["5_parent_enumerator_equals_weight4"] and okn
                      and res["checks"]["5_weight4_passes_F1F4_own_evaluator"])
res["finished"] = runlib.now()
with open(os.path.join(OUT, "route4-phase.json"), "x") as f:
    json.dump(res, f, indent=1)
print(json.dumps({k: v for k, v in res["checks"].items() if k not in ("3_rows",)}, default=str))
print("route4_pass", res["route4_pass"])
