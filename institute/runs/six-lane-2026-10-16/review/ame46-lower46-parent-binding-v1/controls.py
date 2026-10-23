#!/usr/bin/env python3
"""controls.py -- intended-reason controls for binding_check.py (parent binding check of LOWER46).

Each negative control changes exactly one thing -- an in-memory copy of a pinned JSON report or profile entry, a
CNF fixture derived from a pinned CNF by one targeted edit (written under controls/fixtures/ with mode "x" and kept
with its SHA-256), or one predicate input -- and requires the checker to reject it for the intended reason
(intended reasons must be contained in the reported failure list; "exact" controls require equality). Positive
baselines on the unmodified inputs must pass. Enumerator controls live in run_enum.py (enum-runs.json); the natural
orth-only negatives used here are read from its no_orth output.
Writes controls-result.json (mode "x").
"""
import sys

sys.dont_write_bytecode = True

import copy  # noqa: E402
import json  # noqa: E402
import platform  # noqa: E402

import binding_check as bc  # noqa: E402

HERE = bc.HERE
FIX = HERE / "controls" / "fixtures"
F332 = "explore/large_t_gen/t28_e0_3-3-2_3-3-2_3-3-2_3-3-2.cnf"
F30 = "explore/large_t_gen/t30_e0_3-3_2-2-2_2-2-2_2-2-2.cnf"
C332 = "explore/large_t_gen/t28_e0_3-3-2_3-3-2_3-3-2_3-3-2_rep0_completion.cnf"
PROF332 = [[3, 3, 2]] * 4
PROF30 = [[3, 3], [2, 2, 2], [2, 2, 2], [2, 2, 2]]
PROF422 = [[4, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
PROF44 = [[4, 4], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]

results = []


def record(name, kind, intended, got, exact=False, **extra):
    ok = set(got) == set(intended) if exact else set(intended) <= set(got)
    results.append(dict(name=name, kind=kind, intended=intended, got=sorted(set(got)), exact=exact, rejected=bool(got),
                        intended_reason_matched=ok, **extra))


def load_report(t, e):
    return json.loads((bc.SNAP / "evidence" / ("large_t_gen_t%d_e%d.json" % (t, e))).read_text())


def entry_of(report, prof):
    (entry,) = [p for p in report["profiles"] if p["profile"] == prof]
    return entry


def fixture(name, src_rel, mutate):
    lines = (bc.SNAP / src_rel).read_bytes().splitlines(keepends=True)
    new = mutate(list(lines))
    if new == lines:
        raise AssertionError("mutation did not change " + name)
    path = FIX / name
    with open(path, "xb") as fh:
        fh.write(b"".join(new))
    return path, bc.sha256_file(path)


def block_layout(lines, sizes):
    nblocks = sum(sizes)
    nbase = len(lines) - 1 - nblocks
    return 1 + nbase, nbase  # index of the first block line, number of base lines


def vars_of(line):
    return [-int(tok) for tok in line.split()[:-1]]


def as_block(vs):
    return (" ".join("-%d" % v for v in vs) + " 0\n").encode()


def cnf_controls():
    r28, r30 = load_report(28, 0), load_report(30, 0)
    e332, e30 = entry_of(r28, PROF332), entry_of(r30, PROF30)
    s332 = [r["orbit_size"] for r in e332["reps"]]
    s30 = [r["orbit_size"] for r in e30["reps"]]
    npts332 = 81

    base = bc.check_profile(28, 0, e332)
    record("POS_cnf_t28_332x4", "positive", [], base["fails"], exact=True)
    base30 = bc.check_profile(30, 0, e30)
    record("POS_cnf_t30_e0_33", "positive", [], base30["fails"], exact=True)

    def run(name, src, entry, t, e, sizes, mutate, intended, exact=False):
        path, sha = fixture(name, src, mutate)
        out = bc.check_profile(t, e, entry, cnf_path=path)
        record(name, "cnf_fixture", intended, out["fails"], exact=exact, fixture=str(path.relative_to(HERE)),
               fixture_sha256=sha, source=src)

    def m_header(L):
        _, _, nv, nc = L[0].split()
        L[0] = b"p cnf %s %d\n" % (nv, int(nc) + 1)
        return L

    run("B01_header_count_plus_one.cnf", F332, e332, 28, 0, s332, m_header, ["header_mismatch"])

    def m_base_flip(L):
        toks = L[1].split()
        toks[0] = str(-int(toks[0])).encode()
        L[1] = b" ".join(toks) + b"\n"
        return L

    run("B02_base_literal_sign_flip.cnf", F332, e332, 28, 0, s332, m_base_flip, ["base_line_mismatch"])

    def m_base_swap(L):
        L[1], L[2] = L[2], L[1]
        return L

    run("B03_base_lines_swapped.cnf", F332, e332, 28, 0, s332, m_base_swap, ["base_line_mismatch"])

    def m_base_crlf(L):
        L[5] = L[5].rstrip(b"\n") + b"\r\n"
        return L

    run("B04_base_line_crlf.cnf", F332, e332, 28, 0, s332, m_base_crlf, ["base_line_mismatch"])

    def m_point_swap(L):
        i, _ = block_layout(L, s332)
        vs = vars_of(L[i])
        new = min(v for v in range(1, npts332 + 1) if v not in vs)
        vs = sorted(vs[:-1] + [new])
        L[i] = as_block(vs)
        return L

    run("B05_block_point_replaced.cnf", F332, e332, 28, 0, s332, m_point_swap, ["segment_orbit_mismatch"])

    def m_positive(L):
        i, _ = block_layout(L, s332)
        toks = L[i].split()
        toks[0] = toks[0].lstrip(b"-")
        L[i] = b" ".join(toks) + b"\n"
        return L

    run("B06_block_positive_literal.cnf", F332, e332, 28, 0, s332, m_positive, ["block_literal_positive"])

    def m_aux(L):
        i, _ = block_layout(L, s332)
        vs = vars_of(L[i])
        L[i] = as_block(vs[:-1] + [npts332 + 1])
        return L

    run("B07_block_aux_variable.cnf", F332, e332, 28, 0, s332, m_aux, ["block_var_out_of_range"])

    def m_short(L):
        i, _ = block_layout(L, s332)
        L[i] = as_block(vars_of(L[i])[:-1])
        return L

    run("B08_block_literal_dropped.cnf", F332, e332, 28, 0, s332, m_short, ["block_length"])

    def m_dup_clause(L):
        i, _ = block_layout(L, s332)
        L[i + 1] = L[i]
        return L

    run("B09_block_clause_duplicated.cnf", F332, e332, 28, 0, s332, m_dup_clause,
        ["segment_duplicate_or_malformed", "segment_orbit_mismatch"])

    def m_unsorted(L):
        i, _ = block_layout(L, s332)
        vs = vars_of(L[i])
        vs[0], vs[1] = vs[1], vs[0]
        L[i] = as_block(vs)
        return L

    run("B10_block_unsorted.cnf", F332, e332, 28, 0, s332, m_unsorted, ["block_unsorted"])

    def m_dup_lit(L):
        i, _ = block_layout(L, s332)
        vs = vars_of(L[i])
        vs[1] = vs[0]
        L[i] = as_block(vs)
        return L

    run("B11_block_duplicate_literal.cnf", F332, e332, 28, 0, s332, m_dup_lit, ["block_duplicate_literal"])

    def m_trailing(L):
        return L + [L[-1]]

    run("B12_trailing_extra_block.cnf", F332, e332, 28, 0, s332, m_trailing, ["trailing_data"])

    def m_drop_last(L):
        return L[:-1]

    run("B13_last_block_deleted.cnf", F332, e332, 28, 0, s332, m_drop_last, ["premature_eof"])

    def m_cross_segment(L):
        i, _ = block_layout(L, s30)
        L[i], L[i + s30[0]] = L[i + s30[0]], L[i]
        return L

    run("B14_blocks_swapped_across_segments.cnf", F30, e30, 30, 0, s30, m_cross_segment, ["segment_orbit_mismatch"])
    out = results[-1]
    path = HERE / out["fixture"]
    detail = bc.check_profile(30, 0, e30, cnf_path=path)
    out["per_rep_verdicts"] = [r["verdict"] for r in detail["reps"]]
    out["intended_reason_matched"] = out["intended_reason_matched"] and out["per_rep_verdicts"] == ["FAIL", "FAIL"]


def json_controls():
    r28, r30 = load_report(28, 0), load_report(30, 0)
    record("POS_profiles_all_cases", "positive", [],
           [f for t, e in bc.CASES for f in bc.check_profiles(t, e, load_report(t, e))["fails"]], exact=True)
    m = copy.deepcopy(r28)
    m["profiles"] = [p for p in m["profiles"] if p["profile"] != PROF422]
    record("A01_profile_dropped", "profiles", ["profile_missing"], bc.check_profiles(28, 0, m)["fails"], exact=True)
    m = copy.deepcopy(r28)
    m["profiles"].append({"profile": [[6, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]], "orbits": 0,
                          "group_order": 1, "reps": []})
    record("A02_lemma12_violating_profile_added", "profiles", ["profile_extra"], bc.check_profiles(28, 0, m)["fails"],
           exact=True)
    m = copy.deepcopy(r28)
    m["profiles"].append(copy.deepcopy(m["profiles"][0]))
    record("A03_profile_duplicated", "profiles", ["profile_duplicate"], bc.check_profiles(28, 0, m)["fails"],
           exact=True)
    m = copy.deepcopy(r28)
    m["t"] = 27
    record("A04_report_case_field_changed", "profiles", ["report_case_mismatch"], bc.check_profiles(28, 0, m)["fails"],
           exact=True)
    m = copy.deepcopy(r28)
    entry_of(m, PROF422)["profile"] = [[2, 2, 4], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
    record("A05_partition_not_non_increasing", "profiles", ["profile_malformed"], bc.check_profiles(28, 0, m)["fails"])

    e = copy.deepcopy(entry_of(r28, PROF332))
    pts = e["reps"][0]["N"]
    pts[0] = "3355" if "3355" not in pts else "3333"
    record("C01_rep_point_changed", "entry", ["rep_predicate_fail", "segment_orbit_mismatch"],
           bc.check_profile(28, 0, e)["fails"])
    e = copy.deepcopy(entry_of(r30, PROF30))
    a, b = e["reps"][0]["orbit_size"], e["reps"][1]["orbit_size"]
    e["reps"][0]["orbit_size"], e["reps"][1]["orbit_size"] = b, a
    record("C02_orbit_sizes_swapped", "entry", ["segment_orbit_mismatch", "orbit_size_mismatch", "proof_table_mismatch"],
           bc.check_profile(30, 0, e)["fails"])
    e = copy.deepcopy(entry_of(r28, PROF332))
    e["group_order"] += 1
    record("C03_group_order_changed", "entry", ["group_order_mismatch"], bc.check_profile(28, 0, e)["fails"],
           exact=True)
    e = copy.deepcopy(entry_of(r28, PROF332))
    e["orbits"] += 1
    record("C04_orbit_count_changed", "entry", ["orbit_count_mismatch"], bc.check_profile(28, 0, e)["fails"],
           exact=True)
    e = copy.deepcopy(entry_of(r30, PROF30))
    e["reps"][0]["N"], e["reps"][1]["N"] = e["reps"][1]["N"], e["reps"][0]["N"]
    record("C05_rep_point_sets_swapped", "entry", ["segment_orbit_mismatch", "orbit_size_mismatch"],
           bc.check_profile(30, 0, e)["fails"])


def predicate_controls():
    r28 = load_report(28, 0)
    V, d = bc.normal_form(PROF332)
    N = [bc.parse_point(s) for s in entry_of(r28, PROF332)["reps"][0]["N"]]
    record("POS_predicate_rep_332", "positive", [], bc.failures(N, V, d, 0), exact=True)
    record("D01_size_e_plus_one", "predicate", ["size"], bc.failures(N, V, d, 1), exact=True)
    record("D02_point_removed", "predicate", ["line"], bc.failures(N[1:], V, d, 0))
    bad = [(0,) + N[0][1:]] + N[1:]
    record("D03_point_outside_V", "predicate", ["domain"], bc.failures(bad, V, d, 0))
    V4, d4 = bc.normal_form(PROF422)
    N4 = [bc.parse_point(s) for s in entry_of(r28, PROF422)["reps"][0]["N"]]
    record("POS_predicate_rep_422", "positive", [], bc.failures(N4, V4, d4, 0), exact=True)
    d4p = [dict(x) for x in d4]
    d4p[0][3], d4p[0][4] = d4[0][4], d4[0][3]
    record("D04_deficits_permuted_across_classes", "predicate", ["deficit"], bc.failures(N4, V4, d4p, 0), exact=True)
    runs = json.loads((HERE / "enum-runs.json").read_text())
    (no_orth,) = [x for x in runs["no_orth"] if x["parts"] == ["3-3-2"] * 4]
    final = set()
    with open(HERE / runs["final"]["t28_e0_3-3-2_3-3-2_3-3-2_3-3-2"]["output"]) as fh:
        for line in fh:
            final.add(frozenset(bc.parse_point(s) for s in line.split()))
    with open(HERE / no_orth["output"]) as fh:
        extra = [frozenset(bc.parse_point(s) for s in line.split()) for line in fh]
    extra = sorted((S for S in extra if S not in final), key=sorted)
    record("D05_natural_orth_only_instance", "predicate", ["orth"], bc.failures(extra[0], V, d, 0), exact=True,
           instance=["".join(map(str, x)) for x in sorted(extra[0])])

    orb = bc.orbit_bfs(N4, bc.generators(tuple(map(tuple, PROF422))))
    img = frozenset(bc.apply_gen(("value", 0, 3, 4), x) for x in N4)
    got = bc.failures(img, V4, d4, 0) + (["image_outside_H_orbit"] if img not in orb else [])
    record("E01_non_H_value_swap_3_4_on_422_rep0", "group", ["deficit", "image_outside_H_orbit"], got,
           note="values 3 (deficit 4) and 4 (deficit 2) of coordinate 0; image must fail and lie outside the orbit")
    V44, d44 = bc.normal_form(PROF44)
    N44 = [bc.parse_point(s) for s in entry_of(r28, PROF44)["reps"][0]["N"]]
    orb44 = bc.orbit_bfs(N44, bc.generators(tuple(map(tuple, PROF44))))
    img = frozenset(bc.apply_gen(("coord", 0), x) for x in N44)
    got = bc.failures(img, V44, d44, 0) + (["image_outside_H_orbit"] if img not in orb44 else [])
    record("E02_non_H_coordinate_swap_0_1_on_44_rep0", "group", ["domain", "image_outside_H_orbit"], got,
           note="coordinates with partitions (4,4) and (2,2,2,2); image must fail and lie outside the orbit")
    gens = bc.generators(tuple(map(tuple, PROF422))) + [("value", 0, 3, 4)]
    big = bc.orbit_bfs(N4, gens)
    failing = sum(1 for S in big if bc.failures(S, V4, d4, 0))
    record("E03_orbit_with_extra_non_H_generator", "group", ["orbit_grew", "orbit_contains_predicate_failures"],
           (["orbit_grew"] if len(big) > len(orb) else []) + (["orbit_contains_predicate_failures"] if failing else []),
           exact=True, h_orbit=len(orb), enlarged_orbit=len(big), enlarged_failing=failing)


def completion_controls():
    r28 = load_report(28, 0)
    rep = entry_of(r28, PROF332)["reps"][0]
    N = [bc.parse_point(s) for s in rep["N"]]
    info, f = bc.check_completion_cnf(bc.SNAP / C332, N, rep["completion_allowed_points"])
    record("POS_completion_332_rep0", "positive", [], f, exact=True)

    def m_no_zero(L):
        L[3] = L[3].rsplit(b" 0", 1)[0] + b"\n"
        return L

    path, sha = fixture("F01_completion_clause_without_terminator.cnf", C332, m_no_zero)
    _, f = bc.check_completion_cnf(path, N, rep["completion_allowed_points"])
    record("F01_completion_clause_without_terminator.cnf", "completion_fixture", ["clause_malformed"], f,
           fixture=str(path.relative_to(HERE)), fixture_sha256=sha)

    def m_count(L):
        _, _, nv, nc = L[0].split()
        L[0] = b"p cnf %s %d\n" % (nv, int(nc) + 1)
        return L

    path, sha = fixture("F02_completion_header_count_plus_one.cnf", C332, m_count)
    _, f = bc.check_completion_cnf(path, N, rep["completion_allowed_points"])
    record("F02_completion_header_count_plus_one.cnf", "completion_fixture", ["clause_count_mismatch"], f, exact=True,
           fixture=str(path.relative_to(HERE)), fixture_sha256=sha)
    _, f = bc.check_completion_cnf(bc.SNAP / C332, N, rep["completion_allowed_points"] + 1)
    record("F03_completion_allowed_count_off_by_one", "completion", ["allowed_points_mismatch"], f, exact=True)


def main():
    started = bc.now()
    json_controls()
    predicate_controls()
    cnf_controls()
    completion_controls()
    bad = [r["name"] for r in results if not r["intended_reason_matched"]]
    out = {"started": started, "ended": bc.now(), "python": platform.python_version(),
           "controls_sha256": bc.sha256_file(HERE / "controls.py"),
           "binding_check_sha256": bc.sha256_file(HERE / "binding_check.py"),
           "controls": results, "negatives": sum(1 for r in results if r["kind"] != "positive"),
           "positives": sum(1 for r in results if r["kind"] == "positive"), "not_matched": bad,
           "verdict": "FAIL" if bad else "PASS", "peak_rss_bytes": bc.peak_rss()}
    with open(HERE / "controls-result.json", "x") as fh:
        json.dump(out, fh, indent=1)
        fh.write("\n")
    print(json.dumps({"verdict": out["verdict"], "not_matched": bad, "n": len(results)}))


if __name__ == "__main__":
    main()
