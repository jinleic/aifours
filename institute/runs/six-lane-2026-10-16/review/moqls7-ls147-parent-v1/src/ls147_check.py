#!/usr/bin/env python3
"""ls147_check.py (moqls7-ls147-parent-v1), stdlib only; no lane code imported or executed.

  gencontrols PINNED_CLASSES CONTROLS_DIR
      Build the mutated class lists controls/<name>/input.txt and controls/<name>/spec.json (exclusive creation).
  check CLASSES NORM_OUT AUT_OUT ROUTE1_FULL_RUN_OUT MANIFEST VERDICT_OUT [REF_NORM_OUT REF_AUT_OUT]
      Evaluate one class list against the outputs of ls147_norm (with union) and ls147_autpar; write VERDICT_OUT.
      With the reference outputs, also compare the class invariants line by line (invariance control).
"""
import json
import random
import re
import sys

N = 7
NPARAM = 211680  # 3! * 49 * 6! = 7! * 7 * (k+2)(k+1)k with k = 1
Z7_KEY = "".join(str((i + j) % N) for i in range(1, N) for j in range(1, N))
Z7_PAR_FORMULA = 6 * 7 * 7 * 6  # 3! conjugates (all isotopic for a group table) * |G|^2 * |Aut(Z_7)|


def read_rows(path):
    with open(path) as f:
        return [ln.split() for ln in f if ln.strip()]


def square(key):
    L = [[0] * N for _ in range(N)]
    for j in range(N):
        L[0][j] = j
        L[j][0] = j
    for t, ch in enumerate(key):
        L[1 + t // 6][1 + t % 6] = int(ch)
    return L


def is_latin(L):
    full = set(range(N))
    return all(set(L[i]) == full for i in range(N)) and all({L[i][j] for i in range(N)} == full for j in range(N))


def is_reduced(L):
    return L[0] == list(range(N)) and [L[i][0] for i in range(N)] == list(range(N))


def key_of(L):
    return "".join(str(L[i][j]) for i in range(1, N) for j in range(1, N))


def conj(L, sg):
    M = [[None] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            t = (r, c, L[r][c])
            M[t[sg[0]]][t[sg[1]]] = t[sg[2]]
    return M


def isotope(L, a, b, g):
    M = [[None] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            M[a[r]][b[c]] = g[L[r][c]]
    return M


def reduce_sq(S):
    lam = {S[0][j]: j for j in range(N)}
    T = [[lam[v] for v in row] for row in S]
    return sorted(T, key=lambda row: row[0])


def random_member(L, rng):
    sg = rng.sample(range(3), 3)
    a, b, g = (rng.sample(range(N), N) for _ in range(3))
    R = reduce_sq(isotope(conj(L, sg), a, b, g))
    assert is_latin(R) and is_reduced(R)
    return key_of(R), {"sigma": sg, "alpha": a, "beta": b, "gamma": g}


def write_x(path, text):
    with open(path, "x") as f:
        f.write(text)


def gencontrols(pinned, cdir):
    import os
    rows = read_rows(pinned)
    base = [list(r) for r in rows]
    rng = random.Random(20261017)
    keys = {r[0] for r in base}
    par = [int(r[2]) for r in base]
    p1 = [i for i in range(len(base)) if par[i] == 1]
    p2 = [i for i in range(len(base)) if par[i] == 2]
    specs = {}

    def emit(name, newrows, spec):
        os.mkdir(os.path.join(cdir, name))
        write_x(os.path.join(cdir, name, "input.txt"), "".join(" ".join(r) + "\n" for r in newrows))
        spec["name"] = name
        write_x(os.path.join(cdir, name, "spec.json"), json.dumps(spec, indent=1) + "\n")
        specs[name] = spec

    # 1. exact duplicate: line j := line i, both with |Par| claim 1 (so every summed count is unchanged)
    i, j = p1[0], p1[1]
    rows1 = [list(r) for r in base]
    rows1[j] = list(base[i])
    emit("ctl_dup_exact", rows1, {
        "mutation": {"line_replaced": j, "copied_from": i, "par_claim_both": 1},
        "expect_fail": ["canon_distinct", "raw_keys_distinct", "union_cross_class_duplicates_zero",
                        "union_equals_total", "coverage_verdict"],
        "expect_pass": ["latin_reduced_all", "claim_par_binding", "claim_count_binding", "claims_internally_consistent",
                        "derived_sum_equals_total", "claimed_sum_equals_total"]})
    # 2. disguised duplicate: line j := another reduced member of class i (different string), both |Par| claim 2
    i, j = p2[0], p2[1]
    L = square(base[i][0])
    while True:
        k, g = random_member(L, rng)
        if k not in keys:
            break
    rows2 = [list(r) for r in base]
    rows2[j] = [k, base[i][1], base[i][2]]
    emit("ctl_dup_disguised", rows2, {
        "mutation": {"line_replaced": j, "member_of_class_of_line": i, "new_key": k, "paratopism_applied": g,
                     "then": "reduce: relabel symbols so row 0 is 0..6, sort rows by column 0", "par_claim_both": 2},
        "expect_fail": ["canon_distinct", "union_cross_class_duplicates_zero", "union_equals_total",
                        "coverage_verdict"],
        "expect_pass": ["raw_keys_distinct", "latin_reduced_all", "claim_par_binding", "claim_count_binding",
                        "claims_internally_consistent", "derived_sum_equals_total", "claimed_sum_equals_total"]})
    # 3. corrupt one entry
    kline, pos = 10, 0
    old = base[kline][0]
    newd = str((int(old[pos]) + 1) % N)
    rows3 = [list(r) for r in base]
    rows3[kline] = [old[:pos] + newd + old[pos + 1:], base[kline][1], base[kline][2]]
    assert not is_latin(square(rows3[kline][0]))
    emit("ctl_corrupt_entry", rows3, {
        "mutation": {"line": kline, "interior_position": pos, "cell": [1 + pos // 6, 1 + pos % 6], "old": old[pos],
                     "new": newd},
        "expect_fail": ["latin_reduced_all", "norm_input_valid_all", "aut_input_valid_all", "union_equals_total",
                        "derived_sum_equals_total", "coverage_verdict", "claims_verdict"],
        "expect_fail_lines": {"latin_reduced_all": [kline]},
        "expect_pass": ["format_ok", "claimed_sum_equals_total", "claims_internally_consistent"]})
    # 4. swap the (count, |Par|) claims of a |Par|=1 line and a |Par|=2 line: every summed count is unchanged
    a, b = p1[0], p2[0]
    rows4 = [list(r) for r in base]
    rows4[a] = [base[a][0], base[b][1], base[b][2]]
    rows4[b] = [base[b][0], base[a][1], base[a][2]]
    emit("ctl_par_swap", rows4, {
        "mutation": {"lines_swapped_claims": [a, b], "claims_before": [base[a][1:], base[b][1:]]},
        "expect_fail": ["claim_par_binding", "claim_count_binding", "claims_verdict"],
        "expect_fail_lines": {"claim_par_binding": sorted([a, b]), "claim_count_binding": sorted([a, b])},
        "expect_pass": ["claimed_sum_equals_total", "claims_internally_consistent", "derived_sum_equals_total",
                        "canon_distinct", "union_equals_total", "latin_reduced_all", "coverage_verdict"]})
    # 5. change one |Par| claim (and its count consistently): 1 -> 2, 211680 -> 105840
    c = p1[2]
    rows5 = [list(r) for r in base]
    rows5[c] = [base[c][0], str(NPARAM // 2), "2"]
    emit("ctl_par_change", rows5, {
        "mutation": {"line": c, "claims_before": base[c][1:], "claims_after": rows5[c][1:]},
        "expect_fail": ["claim_par_binding", "claim_count_binding", "claimed_sum_equals_total", "claims_verdict"],
        "expect_fail_lines": {"claim_par_binding": [c], "claim_count_binding": [c]},
        "expect_pass": ["claims_internally_consistent", "derived_sum_equals_total", "canon_distinct",
                        "union_equals_total", "coverage_verdict"]})
    # 6. omit the last class
    rows6 = [list(r) for r in base[:-1]]
    emit("ctl_omit", rows6, {
        "mutation": {"line_dropped": len(base) - 1, "its_claims": base[-1][1:]},
        "expect_fail": ["derived_sum_equals_total", "claimed_sum_equals_total", "union_equals_total", "lines_equal_147",
                        "coverage_verdict"],
        "expect_pass": ["canon_distinct", "claim_par_binding", "claim_count_binding",
                        "union_cross_class_duplicates_zero", "latin_reduced_all"]})
    # 7. invariance: every line replaced by a random other reduced member of its own class (claims kept)
    rows7, applied = [], []
    for r in base:
        L = square(r[0])
        for _ in range(100):
            k, g = random_member(L, rng)
            if k != r[0]:
                break
        rows7.append([k, r[1], r[2]])
        applied.append(g)
    emit("ctl_invariance", rows7, {
        "mutation": {"every_line": "random paratopism then reduce; claims kept", "seed": 20261017,
                     "lines_with_key_changed": sum(1 for x, y in zip(rows7, base) if x[0] != y[0])},
        "expect_fail": ["rep_is_own_canon"],
        "expect_pass": ["coverage_verdict", "claims_verdict", "matches_reference", "canon_distinct",
                        "union_equals_total", "derived_sum_equals_total"]})
    print(json.dumps({"controls": sorted(specs)}))
    return 0


def load_jsonl(path):
    recs, summary = [], None
    with open(path) as f:
        for ln in f:
            if not ln.strip():
                continue
            o = json.loads(ln)
            if o.get("summary"):
                summary = o
            else:
                recs.append(o)
    return recs, summary


def check(classes, norm_out, aut_out, route1_out, manifest_path, verdict_out, ref_norm=None, ref_aut=None):
    rows = read_rows(classes)
    nl = len(rows)
    norm, nsum = load_jsonl(norm_out)
    aut, _ = load_jsonl(aut_out)
    with open(route1_out) as f:
        m = re.search(r"^reduced_LS7 (\d+) L1_with_mate (\d+) ", f.read(), re.M)
    total = int(m.group(1))
    with open(manifest_path) as f:
        manifest_ok = json.load(f)["all_ok"]
    C, fl, info = {}, {}, {}

    def put(name, ok, fails=None):
        C[name] = "PASS" if ok else "FAIL"
        if fails:
            fl[name] = fails

    bad = [i for i, r in enumerate(rows) if not (len(r) == 3 and len(r[0]) == 36 and set(r[0]) <= set("0123456")
                                                 and r[1].isdigit() and r[2].isdigit() and int(r[2]) > 0)]
    put("format_ok", not bad, bad)
    put("lines_equal_147", nl == 147)
    sq = [square(r[0]) if i not in bad else None for i, r in enumerate(rows)]
    bad = [i for i in range(nl) if sq[i] is None or not (is_latin(sq[i]) and is_reduced(sq[i]))]
    put("latin_reduced_all", not bad, bad)
    put("raw_keys_distinct", len({r[0] for r in rows}) == nl)
    put("norm_records_complete", len(norm) == nl and [o["idx"] for o in norm] == list(range(nl)) and nsum is not None
        and nsum["classes"] == nl)
    bad = [i for i, o in enumerate(norm) if not o.get("input_valid")]
    put("norm_input_valid_all", not bad, bad)
    valid = [i for i in range(min(nl, len(norm))) if norm[i].get("input_valid")]
    bad = [i for i in valid if not (norm[i]["input_key"] == rows[i][0] and norm[i]["params"] == NPARAM
                                     and norm[i]["bij_fail"] == 0 and norm[i]["conj_bad"] == 0
                                     and norm[i]["invalid_R"] == 0 and norm[i]["identity_param_seen"] == 1
                                     and norm[i]["identity_param_key_equals_input"] == 1)]
    put("norm_internal_ok", not bad, bad)
    bad = [i for i in valid if not (norm[i]["run_min"] == norm[i]["run_max"] == norm[i]["mult_canon"]
                                     == norm[i]["mult_input"] and norm[i]["distinct"] * norm[i]["mult_canon"] == NPARAM)]
    put("free_action_structure", not bad, bad)
    put("aut_records_complete", len(aut) == nl and [o["idx"] for o in aut] == list(range(nl)))
    bad = [i for i, o in enumerate(aut) if not o.get("input_valid")]
    put("aut_input_valid_all", not bad, bad)
    avalid = [i for i in range(min(nl, len(aut))) if aut[i].get("input_valid")]
    bad = [i for i in avalid if not (aut[i]["candidates"] == NPARAM and aut[i]["anomalies"] == 0
                                      and aut[i]["bad_cell_perms"] == 0 and aut[i]["identity_present"] == 1
                                      and aut[i]["closure_done"] == 1 and aut[i]["closure_failures"] == 0
                                      and aut[i]["closure_pairs"] == aut[i]["par_explicit"] ** 2
                                      and aut[i]["distinct_cell_perms"] == aut[i]["par_explicit"]
                                      and aut[i]["nonzero_sigma_counts_equal_atp"] == 1
                                      and sum(aut[i]["per_sigma"]) == aut[i]["par_explicit"])]
    put("aut_group_ok", not bad, bad)
    both = [i for i in valid if i in set(avalid) and aut[i]["par_explicit"] > 0]
    bad = [i for i in both if aut[i]["par_explicit"] != norm[i]["mult_canon"]]
    put("aut_equals_mult", not bad, bad)
    # claims (fields 2 and 3 of each line) bound to the independently derived values
    claim_ok = [len(r) == 3 and r[1].isdigit() and r[2].isdigit() for r in rows]
    bad = [i for i in range(nl) if i not in both or not claim_ok[i]
           or int(rows[i][2]) != aut[i]["par_explicit"] or int(rows[i][2]) != norm[i]["mult_canon"]]
    put("claim_par_binding", not bad, bad)
    bad = [i for i in range(nl) if i not in both or not claim_ok[i]
           or int(rows[i][1]) != norm[i]["distinct"] or int(rows[i][1]) != NPARAM // aut[i]["par_explicit"]]
    put("claim_count_binding", not bad, bad)
    bad = [i for i, r in enumerate(rows) if not (claim_ok[i] and int(r[1]) * int(r[2]) == NPARAM)]
    put("claims_internally_consistent", not bad, bad)
    canon = [norm[i]["canon_key"] for i in valid]
    dup = sorted({k for k in canon if canon.count(k) > 1})
    put("canon_distinct", not dup, dup)
    sum_distinct = sum(norm[i]["distinct"] for i in valid)
    sum_par = sum(NPARAM // aut[i]["par_explicit"] for i in avalid if aut[i]["par_explicit"] > 0)
    sum_claimed = sum(int(r[1]) for i, r in enumerate(rows) if claim_ok[i])
    put("derived_sum_equals_total", sum_distinct == total and len(valid) == nl)
    put("derived_par_sum_equals_total", sum_par == total and len(avalid) == nl
        and all(aut[i]["par_explicit"] > 0 for i in avalid))
    put("claimed_sum_equals_total", sum_claimed == total)
    put("union_ok", nsum is not None and nsum["union_overflow"] == 0 and nsum["union_appended"] == sum_distinct
        and nsum["union_capacity"] > 0)
    put("union_cross_class_duplicates_zero", nsum is not None and nsum["union_adjacent_duplicates"] == 0)
    put("union_equals_total", nsum is not None and nsum["union_distinct"] == total)
    put("route1_binding_ok", manifest_ok and total == 16942080)
    bad = [i for i in valid if norm[i]["canon_key"] != rows[i][0]]
    put("rep_is_own_canon", not bad, bad)
    z7 = [i for i in valid if rows[i][0] == Z7_KEY]
    put("z7_par_formula", len(z7) == 1 and norm[z7[0]]["mult_canon"] == Z7_PAR_FORMULA
        and aut[z7[0]]["par_explicit"] == Z7_PAR_FORMULA)
    coverage_keys = ["format_ok", "latin_reduced_all", "norm_records_complete", "norm_input_valid_all",
                     "norm_internal_ok", "free_action_structure", "canon_distinct", "derived_sum_equals_total",
                     "union_ok", "union_cross_class_duplicates_zero", "union_equals_total", "route1_binding_ok"]
    claims_keys = ["aut_records_complete", "aut_input_valid_all", "aut_group_ok", "aut_equals_mult",
                   "claim_par_binding", "claim_count_binding", "claims_internally_consistent",
                   "derived_par_sum_equals_total"]
    put("coverage_verdict", all(C[k] == "PASS" for k in coverage_keys))
    put("claims_verdict", all(C[k] == "PASS" for k in claims_keys))
    if ref_norm:
        rn, _ = load_jsonl(ref_norm)
        ra, _ = load_jsonl(ref_aut)
        bad = [i for i in range(nl) if not (i in both and norm[i]["canon_key"] == rn[i]["canon_key"]
                                            and norm[i]["mult_canon"] == rn[i]["mult_canon"]
                                            and norm[i]["distinct"] == rn[i]["distinct"]
                                            and aut[i]["par_explicit"] == ra[i]["par_explicit"]
                                            and aut[i]["atp_explicit"] == ra[i]["atp_explicit"])]
        put("matches_reference", not bad, bad)
        info["lines_with_input_key_different_from_reference_input"] = sum(
            1 for i in range(nl) if i in both and norm[i]["input_key"] != rn[i]["input_key"])
    pars = [aut[i]["par_explicit"] for i in both]
    hist = {}
    for p in pars:
        hist[p] = hist.get(p, 0) + 1
    info.update({
        "lines": nl, "route1_reduced_LS7": total, "route1_L1_with_mate": int(m.group(2)),
        "sum_distinct_normalised": sum_distinct, "sum_211680_over_par_explicit": sum_par, "sum_claimed_counts": sum_claimed,
        "union": nsum, "par_histogram": {str(k): hist[k] for k in sorted(hist)},
        "atp_histogram": {}, "z7_line": z7[0] if z7 else None, "z7_par_formula": Z7_PAR_FORMULA,
        "per_class": [{"line": i, "key": rows[i][0], "claimed_count": rows[i][1] if len(rows[i]) > 1 else None,
                       "claimed_par": rows[i][2] if len(rows[i]) > 2 else None,
                       "canon_key": norm[i]["canon_key"] if i in valid else None,
                       "distinct": norm[i]["distinct"] if i in valid else None,
                       "mult_canon": norm[i]["mult_canon"] if i in valid else None,
                       "par_explicit": aut[i]["par_explicit"] if i in avalid else None,
                       "atp_explicit": aut[i]["atp_explicit"] if i in avalid else None,
                       "per_sigma": aut[i]["per_sigma"] if i in avalid else None} for i in range(nl)]})
    for i in avalid:
        a = aut[i]["atp_explicit"]
        info["atp_histogram"][str(a)] = info["atp_histogram"].get(str(a), 0) + 1
    out = {"classes_file": classes, "norm_out": norm_out, "aut_out": aut_out, "checks": C, "fail_detail": fl,
           "info": info}
    write_x(verdict_out, json.dumps(out, indent=1) + "\n")
    print(json.dumps({"coverage_verdict": C["coverage_verdict"], "claims_verdict": C["claims_verdict"],
                      "fails": sorted(k for k, v in C.items() if v == "FAIL")}))
    return 0


if __name__ == "__main__":
    if sys.argv[1] == "gencontrols":
        sys.exit(gencontrols(sys.argv[2], sys.argv[3]))
    if sys.argv[1] == "check":
        a = sys.argv[2:]
        sys.exit(check(*a[:6], *(a[6:8] if len(a) >= 8 else [])))
    sys.exit(2)
