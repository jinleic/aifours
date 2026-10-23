#!/usr/bin/env python3
"""R6 intended-reason mutation controls for the parent binding checks (in memory only).

Each control corrupts one stored list (or one input of the independent semantics) in memory and
records whether the R6 checks reject it for the intended reason. Lane files are read once
(read-only) and never modified. Writes OUT/<name> with mode x.
Inputs: ms01_s01260 with its stored M1 list (a3) and stored M2 list (m2part_drat/ms01_b01554);
ms09_s00001 with its stored M1 list (part) and, as M2 control input only, the worker check copy
cycle2/part/check2-extb-ms09_b9.json (not a production file; its payload is compared with the R6
regeneration in the aggregate).
Usage: python -B r6_mutations.py mutation-controls-v1.json
"""
import copy
import hashlib
import itertools
import json
import os
import sys
import time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import r6_indep as I  # noqa: E402
from r6_replay import S, L, list_diff, m1_entries, m2_entries  # noqa: E402


def sha(b):
    return hashlib.sha256(b).hexdigest()


def frame(tag, bi):
    mi = int(tag[2:4])
    spec = json.load(open(os.path.join(S, "cases19skel", "specs", tag + ".json")))
    D = json.load(open(os.path.join(S, "cycle2", "skel-b", "skeletons-b-ms%02d.json" % mi)))
    sk = D["skeletons"][bi]
    c0, Lv, N = spec["c0"], spec["L"], spec["N"]
    left = len(spec["special"]) - 1
    ra = I.m1_rows(c0, spec["skeleton"], N)
    rb = I.m2_rows(c0, sk["types"], sk["empty"], N)
    auts_a, auts_b = I.automorphisms(c0, ra), I.automorphisms(c0, rb)
    Xa, _ = I.count_vectors(ra, Lv, left)
    Xb, _ = I.count_vectors(rb, Lv, left)
    ca, na = I.orbit_components(Xa, I.generating_set(auts_a, c0))
    cb, nb = I.orbit_components(Xb, I.generating_set(auts_b, c0))
    return {"tag": tag, "bi": bi, "mi": mi, "c0": c0, "L": Lv, "left": left, "ra": ra, "rb": rb, "auts_a": auts_a,
            "auts_b": auts_b, "Xa": Xa, "Xb": Xb, "ca": ca, "na": na, "cb": cb, "nb": nb,
            "isos": I.isomorphisms(c0, ra, rb)}


def m1_check(F, obj):
    ents, badfmt = m1_entries(obj)
    res, _ = I.check_list(F["ra"], F["L"], F["left"], F["Xa"], F["ca"], F["na"], ents)
    res["format_errors"] = badfmt
    res["raw_equals_X"] = obj.get("raw") == len(F["Xa"])
    res["num_full_equals_len"] = obj.get("num_full") == len(obj.get("full", []))
    res["num_full_equals_orbits"] = obj.get("num_full") == F["na"]
    return res


def m2_check(F, obj):
    ents, badfmt = m2_entries(obj)
    res, comp_of = I.check_list(F["rb"], F["L"], F["left"], F["Xb"], F["cb"], F["nb"], ents)
    res["format_errors"] = badfmt
    res["raw_equals_X"] = obj.get("raw_class_assignments") == len(F["Xb"])
    res["automorphisms_equal"] = obj.get("automorphisms") == len(F["auts_b"])
    res["num_equals_len"] = obj.get("num_placements") == len(obj.get("placements", []))
    res["num_equals_orbits"] = obj.get("num_placements") == F["nb"]
    return res, comp_of


def transport_bijection(F, m1_obj, m2_obj, iso):
    """Same matching rule as r6_replay.process_case (M1 entry -> orbit in the M2 frame -> M2 index)."""
    m1_ents, _ = m1_entries(m1_obj)
    _, comp_of2 = m2_check(F, m2_obj)
    comp_to_j = {}
    for j, cc in enumerate(comp_of2):
        if cc is not None:
            comp_to_j.setdefault(cc, j)
    match = []
    for (A, B, P) in m1_ents:
        if I.row_errors(F["ra"], F["L"], F["left"], A, B, P):
            match.append(None)
            continue
        match.append(comp_to_j.get(F["cb"].get(I.transport(iso, I.vec_of(F["ra"], A, B, P)))))
    unmatched = [i for i, j in enumerate(match) if j is None]
    twice = sorted(j for j, k in Counter(x for x in match if x is not None).items() if k > 1)
    return {"bijection": not unmatched and not twice and len(match) == len(comp_of2),
            "unmatched_m1_indices": unmatched[:20], "m2_indices_hit_twice": twice[:20]}


def single_defect(F, entries, kind):
    """First single-row substitution (any block, first 50 entries) whose only row-level defects are of
    `kind` ('share a P0 quad' or 'budget')."""
    N = len(F["ra"])
    for i, (A, B, P) in enumerate(entries[:50]):
        blocks = [list(A), list(B), list(P)]
        used = set(A) | set(B) | set(P)
        for bk in range(3):
            for pos in range(len(blocks[bk])):
                for x in range(N):
                    if x in used:
                        continue
                    nb = [list(b) for b in blocks]
                    nb[bk] = sorted(nb[bk][:pos] + [x] + nb[bk][pos + 1:])
                    errs = I.row_errors(F["ra"], F["L"], F["left"], *nb)
                    if errs and all(kind in e for e in errs):
                        return i, "ABP"[bk], nb, errs
    return None, None, None, None


def main():
    name = sys.argv[1]
    controls = []
    baselines = []

    def add(case, cname, mutation, expected, observed, rejected):
        controls.append({"case": case, "control": cname, "mutation": mutation, "expected_rejection": expected,
                         "observed": observed, "rejected_for_intended_reason": bool(rejected)})

    def base(case, cname, observed, accepted):
        baselines.append({"case": case, "baseline": cname, "observed": observed, "accepted": bool(accepted)})

    inputs = {}
    for tag, bi, m2rel in (("ms01_s01260", 1554, "cycle2/m2part_drat/ms01_b01554/ext.json"),
                           ("ms09_s00001", 9, "cycle2/part/check2-extb-ms09_b9.json")):
        F = frame(tag, bi)
        sub = "a3" if tag.startswith("ms01") else "part"
        m1rel = "cycle2/%s/%s/ext.json" % (sub, tag)
        b1 = open(os.path.join(L, m1rel), "rb").read()
        b2 = open(os.path.join(L, m2rel), "rb").read()
        inputs[tag] = {"m1": {"path": m1rel, "sha256": sha(b1)}, "m2": {"path": m2rel, "sha256": sha(b2)}}
        E = json.loads(b1)
        E2 = json.loads(b2)
        inputs[tag]["m2"]["placements_payload_sha256"] = sha(json.dumps(E2["placements"]).encode())
        r = m1_check(F, E)
        base(tag, "m1_stored", {k: r[k] for k in ("bijective_with_orbits", "raw_equals_X", "num_full_equals_orbits")},
             r["bijective_with_orbits"] and r["raw_equals_X"] and r["num_full_equals_orbits"])
        r2, _ = m2_check(F, E2)
        base(tag, "m2_input", {k: r2[k] for k in ("bijective_with_orbits", "raw_equals_X", "automorphisms_equal")},
             r2["bijective_with_orbits"] and r2["raw_equals_X"] and r2["automorphisms_equal"])
        t = transport_bijection(F, E, E2, F["isos"][0])
        base(tag, "m1_m2_transport", t, t["bijection"])
        ents, _ = m1_entries(E)
        A, B, P = [list(x) for x in ents[0]]

        # M1: duplicate orbit by A/B swap
        M = copy.deepcopy(E)
        M["full"][1] = [[B, A, P]]
        r = m1_check(F, M)
        add(tag, "m1_duplicate_orbit_ab_swap", "full[1] := A/B swap of full[0]",
            "duplicate_orbit_groups contains [0,1]; missing_orbits == 1; no row-level defect",
            {"duplicate_orbit_groups": r["duplicate_orbit_groups"], "missing_orbits": r["missing_orbits"],
             "invalid": r["invalid"]},
            [0, 1] in r["duplicate_orbit_groups"] and r["missing_orbits"] == 1 and not r["invalid"])
        # M1: duplicate orbit by a row symmetry of the skeleton
        by = {}
        for rr, ty in enumerate(F["ra"]):
            by.setdefault(ty, []).append(rr)
        sig = list(range(len(F["ra"])))
        p = next((q for q in F["auts_a"] if list(q) != list(range(F["c0"]))), None)
        if p is not None:
            for ty, rs in by.items():
                for a_, b_ in zip(rs, by[I.perm_set(p, ty)]):
                    sig[a_] = b_
            how = "lifted skeleton automorphism %s" % (list(p),)
        else:
            ty, rs = next((ty, rs) for ty, rs in by.items() if len(rs) >= 2 and (set(rs) & (set(A) | set(B) | set(P))))
            sig[rs[0]], sig[rs[1]] = rs[1], rs[0]
            how = "within-type transposition of rows %d,%d" % (rs[0], rs[1])
        M = copy.deepcopy(E)
        M["full"][1] = [[sorted(sig[x] for x in A), sorted(sig[x] for x in B), sorted(sig[x] for x in P)]]
        r = m1_check(F, M)
        add(tag, "m1_duplicate_orbit_row_symmetry", "full[1] := image of full[0] under " + how,
            "duplicate_orbit_groups contains [0,1]; no row-level defect",
            {"duplicate_orbit_groups": r["duplicate_orbit_groups"], "missing_orbits": r["missing_orbits"],
             "invalid": r["invalid"]}, [0, 1] in r["duplicate_orbit_groups"] and not r["invalid"])
        # M1: dropped entry
        M = copy.deepcopy(E)
        M["full"].pop()
        r = m1_check(F, M)
        add(tag, "m1_drop_last_entry", "full.pop()", "missing_orbits == 1; num_full != len(full)",
            {"missing_orbits": r["missing_orbits"], "num_full_equals_len": r["num_full_equals_len"],
             "bijective": r["bijective_with_orbits"]},
            r["missing_orbits"] == 1 and not r["num_full_equals_len"] and not r["bijective_with_orbits"])
        # M1: agreement-only and budget-only row defects
        for kind, cname in (("share a P0 quad", "m1_agreement_violation"), ("budget", "m1_budget_violation")):
            i, blk, nb, errs = single_defect(F, ents, kind)
            if i is None:
                add(tag, cname, "no single-row substitution in the first 50 entries isolates this defect",
                    "n/a", {}, False)
                continue
            M = copy.deepcopy(E)
            M["full"][i] = [nb]
            r = m1_check(F, M)
            add(tag, cname, "full[%d] block %s := %s" % (i, blk, nb[["A", "B", "P"].index(blk)]),
                "entry %d invalid with '%s' defects only" % (i, kind), {"invalid": r["invalid"]},
                len(r["invalid"]) == 1 and r["invalid"][0][0] == i and all(kind in e for e in r["invalid"][0][1]))
        # M1: overlapping blocks
        M = copy.deepcopy(E)
        M["full"][0] = [[sorted([B[0]] + A[1:]), B, P]]
        r = m1_check(F, M)
        add(tag, "m1_overlap", "full[0] A[0] := B[0]", "entry 0 invalid with 'blocks not disjoint'",
            {"invalid": r["invalid"][:1]},
            bool(r["invalid"]) and r["invalid"][0][0] == 0 and any("not disjoint" in e for e in r["invalid"][0][1]))
        # M1: header fields
        M = copy.deepcopy(E)
        M["raw"] += 1
        r = m1_check(F, M)
        add(tag, "m1_raw_field", "raw += 1", "raw_equals_X false; list still bijective",
            {"raw_equals_X": r["raw_equals_X"], "bijective": r["bijective_with_orbits"]},
            not r["raw_equals_X"] and r["bijective_with_orbits"])
        M = copy.deepcopy(E)
        M["num_full"] += 1
        r = m1_check(F, M)
        add(tag, "m1_num_full_field", "num_full += 1", "num_full_equals_len and num_full_equals_orbits false",
            {"num_full_equals_len": r["num_full_equals_len"], "num_full_equals_orbits": r["num_full_equals_orbits"]},
            not r["num_full_equals_len"] and not r["num_full_equals_orbits"])
        # strict byte layer vs semantic layer
        ws = json.dumps(E, indent=1).encode()
        d = list_diff(E["full"], json.loads(ws)["full"])
        add(tag, "m1_whitespace_only", "re-serialized with indent=1", "sha differs from stored; ordered_equal true",
            {"sha_equal": sha(ws) == sha(b1), "ordered_equal": d["ordered_equal"]},
            sha(ws) != sha(b1) and d["ordered_equal"])
        M = copy.deepcopy(E)
        M["full"][0], M["full"][1] = M["full"][1], M["full"][0]
        d = list_diff(E["full"], M["full"])
        r = m1_check(F, M)
        add(tag, "m1_order_swap", "swap full[0] and full[1]",
            "ordered_equal false, set_equal true, first difference index 0, payload sha changes; orbit bijection holds",
            {"ordered_equal": d["ordered_equal"], "set_equal": d["set_equal"], "first": d["first_order_difference_index"],
             "bijective": r["bijective_with_orbits"],
             "payload_sha_changed": sha(json.dumps(M["full"]).encode()) != sha(json.dumps(E["full"]).encode())},
            not d["ordered_equal"] and d["set_equal"] and d["first_order_difference_index"] == 0 and
            r["bijective_with_orbits"] and sha(json.dumps(M["full"]).encode()) != sha(json.dumps(E["full"]).encode()))
        # transport with a non-isomorphism
        isos = set(F["isos"])
        wrong = next(q for q in itertools.permutations(range(F["c0"])) if q not in isos)
        tX = {I.transport(wrong, v) for v in F["Xa"]}
        add(tag, "transport_non_isomorphism", "transport X_a with %s (not an isomorphism)" % (list(wrong),),
            "transported X_a != X_b", {"equal": tX == F["Xb"]}, tX != F["Xb"])
        # wrong b-index
        D = json.load(open(os.path.join(S, "cycle2", "skel-b", "skeletons-b-ms%02d.json" % F["mi"])))
        wb = (bi + 1) % len(D["skeletons"])
        swb = D["skeletons"][wb]
        rwb = I.m2_rows(F["c0"], swb["types"], swb["empty"], len(F["ra"]))
        n_iso = len(I.isomorphisms(F["c0"], F["ra"], rwb))
        add(tag, "wrong_b_index", "pair with b=%d instead of b=%d" % (wb, bi), "no skeleton isomorphism exists",
            {"isomorphisms": n_iso}, n_iso == 0)
        # drop one count vector from X_a
        v0 = sorted(F["Xa"], key=lambda v: sorted((sorted(ty), c) for ty, c in v))[0]
        X2 = set(F["Xa"]) - {v0}
        try:
            I.orbit_components(X2, I.generating_set(F["auts_a"], F["c0"]))
            closure_detected = False
        except ValueError:
            closure_detected = True
        wdiff = I.weight_sum(X2, F["ra"]) != I.weight_sum(F["Xa"], F["ra"])
        add(tag, "X_drop_vector", "remove one count vector from X_a",
            "union-find reports X not closed (unless a fixed point) and the labeled weight sum no longer matches",
            {"closure_detected": closure_detected, "weight_sum_differs": wdiff}, wdiff)
        # M2 list controls
        M = copy.deepcopy(E2)
        a_, b_, p_ = M["placements"][0]
        M["placements"][1] = [b_, a_, p_]
        r, _ = m2_check(F, M)
        t = transport_bijection(F, E, M, F["isos"][0])
        add(tag, "m2_duplicate_orbit_ab_swap", "placements[1] := A/B swap of placements[0]",
            "M2 duplicate_orbit_groups contains [0,1], missing_orbits == 1, M1->M2 transport bijection false",
            {"duplicate_orbit_groups": r["duplicate_orbit_groups"], "missing_orbits": r["missing_orbits"],
             "transport": t},
            [0, 1] in r["duplicate_orbit_groups"] and r["missing_orbits"] == 1 and not t["bijection"])
        M = copy.deepcopy(E2)
        M["automorphisms"] += 1
        r, _ = m2_check(F, M)
        add(tag, "m2_automorphisms_field", "automorphisms += 1", "automorphisms_equal false",
            {"automorphisms_equal": r["automorphisms_equal"]}, not r["automorphisms_equal"])
        M = copy.deepcopy(E2)
        M["source"] = "/elsewhere/skeletons-b.json"
        add(tag, "m2_source_field", "source := other path", "strict bytes differ; placements ordered_equal",
            {"bytes_equal": json.dumps(M).encode() == b2,
             "ordered_equal": list_diff(E2["placements"], M["placements"])["ordered_equal"]},
            json.dumps(M).encode() != b2 and list_diff(E2["placements"], M["placements"])["ordered_equal"])
        # order-free transport: reversing the M2 list must keep the orbit bijection
        t = transport_bijection(F, E, {"placements": E2["placements"][::-1]}, F["isos"][0])
        base(tag, "m2_reversed_order_transport_still_bijective", t, t["bijection"])
    res = {"recorded_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
           "script_sha256": sha(open(os.path.abspath(__file__), "rb").read()),
           "indep_sha256": sha(open(os.path.join(HERE, "r6_indep.py"), "rb").read()),
           "replay_module_sha256": sha(open(os.path.join(HERE, "r6_replay.py"), "rb").read()),
           "inputs": inputs, "baselines": baselines, "controls": controls,
           "all_baselines_accepted": all(b["accepted"] for b in baselines),
           "all_rejected_for_intended_reason": all(c["rejected_for_intended_reason"] for c in controls
                                                   if c["expected_rejection"] != "n/a"),
           "not_applicable": [c["case"] + ":" + c["control"] for c in controls if c["expected_rejection"] == "n/a"]}
    with open(os.path.join(OUT, name), "x") as f:
        json.dump(res, f, indent=1)
    for b in baselines:
        print("BASELINE", b["case"], b["baseline"], b["accepted"])
    for c in controls:
        print(c["case"], c["control"], c["rejected_for_intended_reason"], json.dumps(c["observed"])[:160])
    print("all_baselines_accepted", res["all_baselines_accepted"], "all_rejected_for_intended_reason",
          res["all_rejected_for_intended_reason"], "n/a", res["not_applicable"])


if __name__ == "__main__":
    main()
