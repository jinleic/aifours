#!/usr/bin/env python3
"""make_receipts.py (parent moqls7-k1-parent-check-v1): assemble one receipt JSON per route plus RESULT.json from the
saved outputs. Run records of bash-launched commands are taken from the saved /usr/bin/time files where they exist;
exit codes of bash-launched commands are transcribed from the tool transcript (marked source=transcript)."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mynet, runlib

D = os.path.dirname(HERE)
rel = lambda p: os.path.relpath(p, D)
def h(p):
    p = os.path.join(D, p)
    return {"path": rel(p), "sha256": runlib.sha_file(p), "bytes": os.path.getsize(p)} if os.path.exists(p) else {"path": rel(p), "missing": True}
def timefile(p):
    t = open(os.path.join(D, p)).read()
    out = {"time_file": h(p)}
    m = re.search(r"([\d.]+) real\s+([\d.]+) user\s+([\d.]+) sys", t)
    if m:
        out.update({"real_s": float(m.group(1)), "user_s": float(m.group(2)), "sys_s": float(m.group(3))})
    m = re.search(r"(\d+)\s+maximum resident set size", t)
    if m:
        out["max_rss_bytes"] = int(m.group(1))
    return out
def J(p):
    return json.load(open(os.path.join(D, p)))
RT = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review"
MYDIR = "moqls7-k1-parent-check-v1"
common_scripts = [h("scripts/runlib.py"), h("scripts/mynet.py"), h("scripts/snapshot_inputs.py"), h("scripts/make_receipts.py")]
manifest = J("inputs/lane-manifest.json")
snapshot = {"script": h("scripts/snapshot_inputs.py"), "manifest": h("inputs/lane-manifest.json"),
            "files": len(manifest["files"]), "all_stable_during_copy": manifest["all_stable"],
            "argv": ["/usr/bin/python3", "-B", "scripts/snapshot_inputs.py"], "exit": 0, "exit_source": "transcript",
            "rss": "not instrumented", "started": manifest["started"], "finished": manifest["finished"]}
claim_pins = {r["rel"]: r["sha256_copy"] for r in manifest["files"]}

# ---------------- route 1 ----------------
r1 = J("route1/route1-report.json")
fs, ff = open(os.path.join(D, "route1/ew/fetch_started_utc.txt")).read().strip(), open(os.path.join(D, "route1/ew/fetch_finished_utc.txt")).read().strip()
hdr = open(os.path.join(D, "route1/ew/1406.3681v2.headers.txt")).read()
rec1 = {
    "route": 1, "title": "Net-class completeness (claim section 3)",
    "verdicts": {
        "1a_each_listed_net_is_a_valid_4net": "PASS" if all(v[0] for v in r1["valid_4nets"]) else "FAIL",
        "1b_par_recomputed_explicit_automorphisms_match_claim": "PASS" if all(r["par_matches"] for r in r1["per_class"]) else "FAIL",
        "1c_orbit_sizes_and_orbit_stabiliser": "PASS" if all(r["orbit_matches"] and r["orbit_stabiliser"] for r in r1["per_class"]) else "FAIL",
        "1d_pairwise_non_isomorphic(disjoint reduced-list orbits; canonical forms; invariants)": "PASS" if (r1["cross_class_duplicates"] == 0 and r1["invariants_pairwise_distinct"]) else "FAIL",
        "1e_sum_846720/|par| = 342480 (maximal 341880)": "PASS" if (r1["sum_orbits"] == 342480 and r1["sum_orbits_maximal_per_claim_flags"] == 341880) else "FAIL",
        "1f_maximality_flags_match_own_5net_extension_count": "PASS" if r1["maximality_matches_claim"] else "FAIL",
        "1g_EW_fetched_pinned_quoted": "PASS",
        "1h_identity_matches_EW_reduced_definition": "PASS (with wording note: EW Thm 3.2/Tables 5-6 count reduced SETS; RS=RL for k=2 by Thm 3.1)",
        "1i_independent_full_classification_of_4nets_of_order_7": "PASS" if r1["full_enumeration_ok"] else "FAIL"},
    "results": {
        "per_class": [{k: r[k] for k in ("class", "claim_par", "aut_explicit", "key_equal_frames", "distinct", "claim_orbit",
                                         "canon_equals_lane_key", "invalid")} for r in r1["per_class"]],
        "union_size": r1["union_size"], "cross_class_duplicates": r1["cross_class_duplicates"],
        "sum_orbits": r1["sum_orbits"], "sum_orbits_maximal": r1["sum_orbits_maximal_per_claim_flags"],
        "invariants": r1["invariants"], "full_enumeration": r1["full_enumeration"],
        "meaning_of_846720": "24 orderings of the 4 parallel classes x 49 origins x 720 orderings of the other 6 points on the origin's row line; each normalisation yields one EW-reduced list (rows/cols/L1/L2; first rows of L1,L2 in order, first column of L1 in order). |par| = stabiliser of the 49x4 orthogonal array in S_7 wr S_4 = net automorphism group including class permutations; #distinct reduced lists = 846720/|par| = n!n(k+2)(k+1)k/|par| (EW Thm 3.2, n=7, k=2).",
        "desarguesian_consistency_[INFERENCE]": "|par| 2352 = 49*6*8 and 3528 = 49*6*12 equal translations x scalars x the PGL(2,7) setwise stabilisers (D8 for a harmonic, A4 for an equianharmonic quadruple); class 5 net literally (x,y,y-x,y-2x), class 6 literally (x,y,y-x,y-3x).",
        "EW_quotes": r1["EW_quotes"]},
    "EW_source": {"url": "https://arxiv.org/pdf/1406.3681v2", "fetched_utc": [fs, ff], "pdf": h("route1/ew/1406.3681v2.pdf"),
                  "equals_lane_pin": runlib.sha_file(os.path.join(D, "route1/ew/1406.3681v2.pdf")) == claim_pins["sources/1406.3681v2.pdf"],
                  "http_headers": h("route1/ew/1406.3681v2.headers.txt"), "http_status_line": hdr.split("\n")[0].strip(),
                  "last_modified": [l.split(": ", 1)[1].strip() for l in hdr.split("\n") if l.lower().startswith("last-modified")],
                  "text": h("route1/ew/1406.3681v2.parent.layout.txt"),
                  "text_equals_lane_layout": runlib.sha_file(os.path.join(D, "route1/ew/1406.3681v2.parent.layout.txt")) == claim_pins["sources/1406.3681v2.layout.txt"],
                  "pdftotext": "pdftotext 26.04.0 -layout"},
    "runs": [
        {"what": "fetch EW", "argv": ["curl", "-sS", "-L", "-A", "Mozilla/5.0 (parent-verification read-only)", "-D", "ew/1406.3681v2.headers.txt", "-o", "ew/1406.3681v2.pdf", "https://arxiv.org/pdf/1406.3681v2"], "cwd": "route1", "exit": 0, "exit_source": "transcript"},
        {"what": "extract EW text", "argv": ["pdftotext", "-layout", "1406.3681v2.pdf", "1406.3681v2.parent.layout.txt"], "cwd": "route1/ew", "exit": 0, "exit_source": "transcript"},
        {"what": "compile", "argv": ["clang", "-O2", "-Wall", "-o", "k1par_nets", "k1par_nets.c"], "cwd": "route1/c", "exit": 0, "warnings": 0, "compiler": "Apple clang 17.0.0 (clang-1700.3.19.1)", "exit_source": "transcript"},
        {"what": "part 1: frames, |Aut|, canonical forms", "argv": ["./c/k1par_nets"], "stdin": "c/nets7.txt", "stdout": h("route1/part1.out"), "limit": "ulimit -t 900", "exit": 0, "exit_source": "transcript", **timefile("route1/part1.time.txt")},
        {"what": "compile v2 (progress lines)", "argv": ["clang", "-O2", "-Wall", "-o", "c/k1par_nets_v2", "c/k1par_nets_v2.c"], "cwd": "route1", "exit": 0, "exit_source": "transcript"},
        {"what": "bounded measurement of the full classification", "argv": ["./c/k1par_nets_v2", "full"], "stdin": "c/nets7.txt", "stdout": h("route1/full_measure60.out"), "limit": "ulimit -t 60", "exit": 152, "exit_meaning": "SIGXCPU from the intended 60 s CPU bound; partial output not used as evidence; 5242880 squares by 59.7 s CPU => ~190 s CPU projected", "exit_source": "transcript", **timefile("route1/full_measure60.time.txt")},
        {"what": "full classification", "argv": ["./c/k1par_nets_v2", "full"], "stdin": "c/nets7.txt", "stdout": h("route1/full_run.out"), "limit": "ulimit -t 900", "exit": 0, "exit_source": "transcript", **timefile("route1/full_run.time.txt")},
        {"what": "report", "argv": ["/usr/bin/python3", "-B", "scripts/route1_report.py"], "cwd": ".", "exit": 0, "exit_source": "transcript", **timefile("route1/route1_report.time.txt")}],
    "code": [h("route1/c/k1par_nets.c"), h("route1/c/k1par_nets"), h("route1/c/k1par_nets_v2.c"), h("route1/c/k1par_nets_v2"), h("route1/c/nets7.txt"), h("scripts/route1_report.py")] + common_scripts,
    "outputs": [h("route1/route1-report.json"), h("route1/part1.out"), h("route1/full_run.out"), h("route1/full_measure60.out")],
    "inputs": [h("inputs/lane/evidence/nets7_classes.json"), h("inputs/lane/code/net_canon.c")],
    "independence": "No lane code imported or executed in route 1. net_canon.c was read to learn the normalisation; the parent C code re-derives reduced lists from EW's definition, adds an explicit line-preservation automorphism test, and a full enumeration of reduced Latin squares, transversals and transversal partitions.",
    "notes": ["Full classification: all 16942080 reduced LS(7) (first row and column in order) enumerated; all transversals; all partitions into 7 disjoint transversals give all 342480 reduced 2-MOLS(7) lists; every one lies in exactly one of the 7 listed orbits, each orbit element hit exactly once. This does not rely on EW's published totals (it reproduces them)."]}
# ---------------- route 2 ----------------
rv = J("route2/verify/route2-verify.json")
rr = J("route2/replay-runs.json")
rec2 = {
    "route": 2, "title": "SAT replay (claim section 4)",
    "verdicts": {"2a_pinned_encoders_regenerate_byte_identical_CNFs_and_proofs": "PASS" if all(ok for k, ok in rv["checks"]["H_hash_bindings"]["items"] if "replay" in k) else "FAIL",
                 "2b_hashes_bound_to_lane_summary_JSONs": "PASS" if rv["checks"]["H_hash_bindings"]["pass"] else "FAIL",
                 "2c_parent_drat_trim_all_14_proofs_s_VERIFIED": "PASS" if rv["checks"]["D_parent_drat_trim"]["pass"] else "FAIL",
                 "2d_model_sets_identical_between_encoders": "PASS" if rv["checks"]["M_model_sets_identical"]["pass"] else "FAIL",
                 "2e_final_CNF_equals_base_plus_one_block_per_model": "PASS" if rv["checks"]["F_final_equals_base_plus_blocks"]["pass"] else "FAIL",
                 "2f_models_satisfy_base_CNF_and_F1F4": "PASS" if rv["checks"]["S_models_satisfy_base_and_F1F4"]["pass"] else "FAIL",
                 "2g_drat_trim_controls": "PASS" if rv["checks"]["C_drat_controls"]["pass"] else "FAIL"},
    "results": {"models_per_class": [(c["class"], c["nA"], c["nB"], c["sets_identical"]) for c in rv["per_class_models"]],
                "parent_drat_trim": {"path": rv["parent_drat_trim"], "sha256": rv["parent_drat_trim_sha256"]},
                "drat_runs": [{k: r[k] for k in ("tag", "verified", "s_lines", "exit", "wall_s", "child_maxrss_bytes", "cnf_sha256", "proof_sha256")} for r in rv["drat_runs"]],
                "controls": rv["checks"]["C_drat_controls"]["items"],
                "final_eq_base_plus_blocks": rv["checks"]["F_final_equals_base_plus_blocks"]["items"]},
    "runs": [{"what": "replay driver", "argv": ["/usr/bin/python3", "-B", "scripts/route2_replay.py"], "cwd": ".", "exit": 0, "exit_source": "transcript", "wall_s_tool": 18.32, "rss": "per subprocess below"},
             {"what": "replay subprocesses (pinned lane code)", "records": [{k: r[k] for k in ("argv", "exit", "wall_s", "child_maxrss_bytes", "all_waited_descendants_maxrss_bytes", "started", "finished")} for r in rr["runs"]], "pinned": rr["pinned"]},
             {"what": "verification", "argv": ["/usr/bin/time", "-l", "/usr/bin/python3", "-B", "scripts/route2_verify.py"], "cwd": ".", "exit": 0, "exit_source": "transcript", "real_s": 18.00, "max_rss_bytes": 61358080, "time_source": "tool transcript (not saved to a file)"}],
    "code": [h("scripts/route2_replay.py"), h("scripts/route2_verify.py")] + common_scripts,
    "outputs": [h("route2/replay-runs.json"), h("route2/verify/route2-verify.json"), h("route2/replayA/summary.json"), h("route2/replayB/summaryB.json")],
    "inputs": [h("inputs/lane/code/k1_sat.py"), h("inputs/lane/code/k1_certify.py"), h("inputs/lane/code/k1_encB.py"), h("inputs/lane/evidence/k1A/summary.json"), h("inputs/lane/evidence/k1B/summaryB.json"), h("inputs/lane/env/drat-trim/drat-trim"), h("inputs/lane/env/drat-trim/drat-trim.c")],
    "solvers": {"cadical": "3.0.1 /opt/homebrew/Cellar/cadical/3.0.1/bin/cadical sha256 " + rr["pinned"]["/opt/homebrew/bin/cadical"], "kissat": "4.0.4 sha256 " + rr["pinned"]["/opt/homebrew/bin/kissat"]}}
# ---------------- route 3 ----------------
r3 = J("route3/route3-compare.json")
nets, data = mynet.load_nets(os.path.join(D, "inputs/lane/evidence/nets7_classes.json"))
dirs = {}
for i in (5, 6):
    ss = []
    for c in J("route2/verify/route2-verify.json")["per_class_models"][i]["patterns"]:
        if all(len(s) == 1 for s in c):
            hit = [s for s in range(7) if all(c[7 * x + y] == [(y - s * x) % 7] for x in range(7) for y in range(7))]
            ss.append(hit)
    dirs[str(i)] = ss
rec3 = {
    "route": 3, "title": "Independent non-SAT enumerator for frame lemma + F1-F4 on all 7 nets",
    "verdicts": {"3a_counts_0,0,0,0,0,4,5": "PASS" if r3["counts_fc"] == [0, 0, 0, 0, 0, 4, 5] else "FAIL",
                 "3b_patterns_identical_to_lane_A_and_B": "PASS" if all(c["fc_eq_A"] and c["fc_eq_B"] for c in r3["classes"]) else "FAIL",
                 "3c_two_independent_search_modes_agree": "PASS" if all(c["fc_eq_plain"] for c in r3["classes"]) else "FAIL",
                 "3d_frame_lemma_emerges_from_F2_with_full_127_subset_domains": "PASS" if all(c["frame_lemma_emerges_from_F2"] for c in r3["classes"]) else "FAIL",
                 "3e_class6_nonclassical_pattern_equals_A(p)": "PASS" if r3["classes"][6]["nonclassical_equals_A(p)_everywhere"] == [True] else "FAIL"},
    "results": {"classes": r3["classes"], "classical_patterns_as_directions_y-sx (class: list of s per pattern)": dirs},
    "runs": [{"what": "compile", "argv": ["clang", "-O2", "-Wall", "-o", "c/k1par_enum", "c/k1par_enum.c"], "cwd": "route3", "exit": 0, "warnings": 0, "exit_source": "transcript"},
             {"what": "fc mode", "argv": ["./c/k1par_enum", "fc"], "stdin": "../route1/c/nets7.txt", "limit": "ulimit -t 600", "exit": 0, "exit_source": "transcript", "stdout": h("route3/enum_fc.out"), **timefile("route3/enum_fc.time.txt")},
             {"what": "plain mode", "argv": ["./c/k1par_enum", "plain"], "stdin": "../route1/c/nets7.txt", "limit": "ulimit -t 1500", "exit": 0, "exit_source": "transcript", "stdout": h("route3/enum_plain.out"), **timefile("route3/enum_plain.time.txt")},
             {"what": "compare", "argv": ["/usr/bin/python3", "-B", "scripts/route3_compare.py"], "exit": 0, "exit_source": "transcript", "rss": "not instrumented", "wall": "<1 s"}],
    "code": [h("route3/c/k1par_enum.c"), h("route3/c/k1par_enum"), h("scripts/route3_compare.py")] + common_scripts,
    "outputs": [h("route3/route3-compare.json"), h("route3/enum_fc.out"), h("route3/enum_plain.out")],
    "measurements": "fc: 82-395 search nodes per net, 0.16 s total; plain: 67018-181546 nodes per net, 0.31 s total; RSS 2.1 MB."}
# ---------------- route 4 ----------------
r4 = J("route4/route4-phase-v2.json")
c4 = r4["checks"]
rec4 = {
    "route": 4, "title": "Phase cycle (claim section 5), exact",
    "verdicts": {"4a_class6_net_is_(x,y,y-x,y-3x)_with_index_7x+y": "PASS" if c4["1_net6_equals_(x,y,y-x,y-3x)"] else "FAIL",
                 "4b_A(x,y)=y-x{2,4,5,6}": "PASS" if c4["2_A(x,y)=y-x{2,4,5,6}"] else "FAIL",
                 "4c_seven_relations(points, common line class, shared coordinates)": "PASS" if c4["3_all_rows_ok"] else "FAIL",
                 "4d_signed_sum_cancels_every_phase_variable": "PASS" if c4["4_signed_sum_is_zero_vector"] else "FAIL",
                 "4e_rhs_odd_multiple_of_pi": "PASS" if c4["4_rhs_odd"] else "FAIL",
                 "4f_enumerated_nonclassical_model_equals_weight4_pattern(A,B,parent)": "PASS" if (c4["5_lane_A_equals_weight4"] and c4["5_lane_B_equals_weight4"] and c4["5_parent_enumerator_equals_weight4"]) else "FAIL"},
    "results": {k: v for k, v in c4.items()},
    "runs": [{"what": "phase check", "argv": ["/usr/bin/python3", "-B", "scripts/route4_phase_v2.py"], "exit": 0, "exit_source": "transcript", "rss": "not instrumented", "wall": "<1 s"},
             {"what": "route4_phase.py (v1)", "status": "written, never executed; superseded by v2 because its non-load-bearing numeric sanity test used a fragile float mod-2 comparison"}],
    "code": [h("scripts/route4_phase_v2.py"), h("scripts/route4_phase.py")] + common_scripts,
    "outputs": [h("route4/route4-phase-v2.json")],
    "not_checked": ["claim section 5 exploration statements '97 independent contradictions' and 'minimum-size, found by MILP' (not load-bearing)"]}
# ---------------- route 5 ----------------
r5 = J("route5/route5-controls.json")
rec5 = {
    "route": 5, "title": "Controls C1-C4 (claim section 7)",
    "verdicts": {"5a_pinned_pattern_check_replay_byte_identical": "PASS" if r5["replay_ok"] else "FAIL",
                 "5b_C1_own_exact": "PASS" if r5["own_ok"]["C1"] else "FAIL", "5c_C2_own_exact": "PASS" if r5["own_ok"]["C2"] else "FAIL",
                 "5d_C3_own": "PASS" if r5["own_ok"]["C3"] else "FAIL", "5e_C4_own": "PASS" if r5["own_ok"]["C4"] else "FAIL"},
    "results": {"replay_summary": r5["a_replay"]["replay_summary"], "C1_own": r5["C1_own"], "C2_own": r5["C2_own"],
                "C3_own": {k: r5["C3_own"][k] for k in ("n_models", "all_pass")}, "C4_own": r5["C4_own"]},
    "runs": [{"what": "controls driver", "argv": ["/usr/bin/python3", "-B", "scripts/route5_controls.py"], "exit": 0, "exit_source": "transcript", "rss": "not instrumented (driver)", "wall": "<10 s"},
             {"what": "pinned lane pattern_check.py replay (subprocess)", **{k: r5["a_replay"][k] for k in ("argv", "exit", "wall_s", "child_maxrss_bytes", "started", "finished", "pinned_checker_sha256", "replay_output_sha256", "lane_output_sha256", "byte_identical")}}],
    "code": [h("scripts/route5_controls.py")] + common_scripts,
    "outputs": [h("route5/route5-controls.json"), h("route5/pattern_controls.replay.json")]}
recs = [rec1, rec2, rec3, rec4, rec5]
for r in recs:
    r["snapshot_of_lane_inputs"] = snapshot
    r["created"] = runlib.now()
    vals = list(r["verdicts"].values())
    r["route_verdict"] = "PASS" if all(str(v).startswith("PASS") for v in vals) else ("FAIL" if any(str(v).startswith("FAIL") for v in vals) else "UNKNOWN")
paths = []
for r in recs:
    p = os.path.join(D, "route%d" % r["route"], "receipt-route%d.json" % r["route"])
    with open(p, "x") as f:
        json.dump(r, f, indent=1)
    paths.append(h(rel(p)))
discrepancies = [
    {"id": "X1", "severity": "minor", "where": "K1-THEOREM.r1.md section 4 (line 64)", "what": "k1_certify.py cited as e61ab812...3c7e; actual sha256 e61ab8126463c12fd177e96e7123fd2462747584548949a44dff3f5c33c7e113 (tail e113; '3c7e' sits at hex positions 57-60). The lane summary.json does not record the driver hash (only k1_sat_sha256). The on-disk driver reproduced every CNF and proof byte-for-byte."},
    {"id": "X2", "severity": "minor (wording)", "where": "K1-THEOREM.r1.md section 3 (lines 56-58)", "what": "'Egan-Wanless totals of reduced 2-MOLS(7) lists (Theorem 3.2 with Tables 5-6)': EW Theorem 3.2 and Tables 5-6 count reduced SETS; reduced LISTS are Tables 7-8. For k=2 Theorem 3.1 gives RS = RL and Tables 7-8 rows (7,2) show the same 341880/342480, so the numbers and the identity are unaffected."},
    {"id": "X3", "severity": "observation", "where": "section 4 (lines 69-70)", "what": "Lane drat-trim binary sha256 111b0405...d5e4 differs from the parent binary a46c0c71...8e37; only the SOURCE identity (d834b649...c2ee) is claimed, and it holds. All 14 proofs were re-checked with the parent binary."},
    {"id": "X4", "severity": "observation", "where": "section 3 trust base (lines 58-60)", "what": "The lane ran no independent full enumeration; the parent route-1 full enumeration now supplies one and agrees with EW's totals."}]
deviations = [
    "Three clang compilations ran with the inherited TMPDIR=/var/folders/1p/mqmj96zd5xx2n2l9996zrlbm0000gn/T/ (macOS per-user temp; not /tmp) instead of the own tmp/ subdir; all Python, solver and drat-trim runs had TMPDIR=<dir>/tmp (which stayed empty).",
    "External tools and pinned lane code created files non-exclusively at fresh paths: curl -o/-D, pdftotext, clang -o, and k1_certify.py / k1_encB.py / pattern_check.py (open(...,'w') into new paths and new dirs). No existing file was overwritten. Shell redirections used noclobber; parent scripts used open(...,'x').",
    "RSS not instrumented for snapshot_inputs.py, route3_compare.py, route4_phase_v2.py and route5_controls.py (small stdlib drivers; their subprocesses have records). The route2_verify /usr/bin/time output (18.00 s, 61358080 B) exists only in the tool transcript.",
    "route4_phase.py v1 was written but never executed (superseded by v2 before running).",
    "The bounded 60 s measurement run ended by its own ulimit -t 60 (exit 152, SIGXCPU) as intended; its partial output is not used as evidence."]
result = {"created": runlib.now(), "dir": os.path.join(RT, MYDIR), "claim": h("inputs/lane/review/K1-THEOREM.r1.md"),
          "claim_sha256_prefix_b702b021": claim_pins["review/K1-THEOREM.r1.md"].startswith("b702b021"),
          "route_verdicts": {"route%d" % r["route"]: r["route_verdict"] for r in recs}, "receipts": paths,
          "discrepancies": discrepancies, "deviations": deviations,
          "unknown_or_not_checked": ["claim section 8 (K2/K3 reduction) - outside this assignment",
                                     "claim section 5 exploration statements (97 contradictions; MILP minimality) - not load-bearing, not checked"],
          "resources": {"max_concurrent_busy_processes": 2, "peak_rss_bytes": 193019904, "new_data_bytes_approx": "47 MB"},
          "scope_note": "Per-route PASS/FAIL/UNKNOWN only; no verdict on Theorem K1 (parent decides after hostile reviews)."}
with open(os.path.join(D, "RESULT.json"), "x") as f:
    json.dump(result, f, indent=1)
print(json.dumps(result["route_verdicts"]), [p["sha256"][:12] for p in paths])
for r in recs:
    print(r["route"], r["route_verdict"], r["verdicts"])
print("classical directions", dirs)
