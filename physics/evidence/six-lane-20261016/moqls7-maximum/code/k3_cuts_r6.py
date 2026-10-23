#!/usr/bin/env python3
"""k3_cuts_r6.py: AMENDMENT-4.r4 cut-family controls C1-C4, re-bound to the frozen r4 text (supervised r6).

New version of k3_cuts_r5.py (2b9b1189...8e87). r2 to r5 are preserved, and none of them produced a receipt. The
content is r2's (5c1c1d67...bdd9), with these changes:
  - it imports the current driver k3_cuts_certify_r5 for paths (frozen AMENDMENT-4.r4, delta r5), pins, the oracle
    check and the B_C311 binding;
  - it refuses to run unless it is the session/group leader started by the supervisor that the frozen delta pins
    (supervise_r3.py).
The supervisor therefore guards this whole process and every encoder B child in its group: strict RSS probes, the
12e9 floor, a stage wall cap, killpg stops with a bounded wait, and quarantine on survivors or uncertainty. Admission
is refused while evidence/k3cubes/C311cuts.QUARANTINE.json exists (parent source reviews 15aae4593f5e6f0b and the
stage_guard review).
The clause family and emission come from the reviewed k3_cuts_r1.py (0ec92c86...1b0a), also used by the appender.
Content carried from r2 (desk m9-m12, parent decisions 2 and 4):
  binding  refuses to run unless the frozen amendment (drv.AMENDMENT, review/AMENDMENT-4.r4.md) exists and names this
           script's SHA; binds its SHA, so C1 (2100 local assignments, exactly 450 rejected) and C2-C4 are re-bound to it;
  m9       the runtime B decode first asserts the oracle receipt (PASS and pins) and the B_C311 metadata binding,
           checks the B base output against the oracle base, and checks every --fix-json run: header (base vars,
           base clauses + 2646), byte-identical base clause prefix, exactly 2646 distinct appended units on 1..2646,
           and a positive-unit count equal to the design population;
  m10      control (e): the runtime decode is the only datum; block-SHA and set equality are recorded as its
           consequences, and the swapped map as SHA sensitivity;
  m11      each mutation stores its full shape report, set distinctness and count separately, and the failing checks;
  m12      the receipt records sys.executable, sys.version, flags and the path and SHA of every imported lane module.
The clause block is hashed in memory and not written. No solver is run.
Usage (only under the supervisor, see the delta): /usr/bin/python3 -I -B k3_cuts_r6.py
"""
import hashlib
import itertools
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import gram_enc  # noqa: E402
import k3_cubes  # noqa: E402
import k3_cuts_certify_r5 as drv  # noqa: E402
import k3_cuts_r1 as r1  # noqa: E402
import k3_lex  # noqa: E402
from gram_certify_r4 import now, sha  # noqa: E402

LANE = os.path.dirname(HERE)
ENC_B = os.path.join(HERE, "gram_encB.py")
NG = 2646
B_BASE = (461370, 1629644)
GATE, GROWTH = 12200000000, 1048576


def environment():
    modules = {}
    for name in ("gram_enc", "k3_cubes", "k3_lex", "k3_cuts_r1", "k3_cuts_certify_r5", "gram_certify_r4", "proof_stream"):
        path = os.path.abspath(sys.modules[name].__file__)
        modules[name] = {"path": path, "sha256": sha(path)}
    return {"executable": sys.executable, "version": sys.version, "isolated": bool(sys.flags.isolated),
            "dont_write_bytecode": bool(sys.dont_write_bytecode), "modules": modules}


def b_output(fix):
    cmd = ["/usr/bin/python3", "-B", ENC_B, "--squares", "3", "--heavy", "--sym", "--out", "/dev/stdout"]
    if fix is None:
        r = subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        r = subprocess.run(cmd + ["--fix-json", "/dev/stdin"], input=json.dumps(fix).encode(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode != 0:
        raise RuntimeError("encoder B failed: rc %d" % r.returncode)
    out = r.stdout
    first_end = out.index(b"\n") + 1
    tag, form, nv, nc = out[:first_end].decode().split()
    stats_start = out.rindex(b"\n", 0, len(out) - 1) + 1
    if (tag, form) != ("p", "cnf") or not out[stats_start:].startswith(b"vars ") \
            or out.count(b"\n", first_end, stats_start) != int(nc):
        raise RuntimeError("encoder B output is not header + nc clause lines + stats line")
    return int(nv), int(nc), out[first_end:stats_start]


def decode_b_map(amap, base_body):
    by_index = {v: key for key, v in amap.items()}
    codes = {v: 0 for v in range(1, NG + 1)}
    checks = []
    for b in range(12):
        fix = {"g1": [], "g2": [], "g3": []}
        for (a, p, q), v in sorted(amap.items(), key=lambda item: item[1]):
            if (v >> b) & 1:
                fix["g%d" % a].append([list(p), list(q)])
        nv, nc, body = b_output(fix)
        header_ok = (nv, nc) == (B_BASE[0], B_BASE[1] + NG)
        prefix_ok = body.startswith(base_body)
        units, units_ok = {}, True
        tail = body[len(base_body):].splitlines() if prefix_ok else []
        if len(tail) != NG:
            units_ok = False
        for line in tail:
            toks = line.split()
            if len(toks) != 2 or toks[1] != b"0":
                units_ok = False
                break
            lit = int(toks[0])
            if not 1 <= abs(lit) <= NG or abs(lit) in units:
                units_ok = False
                break
            units[abs(lit)] = lit > 0
        units_ok = units_ok and len(units) == NG
        positives = sum(1 for positive in units.values() if positive)
        population = sum(1 for v in range(1, NG + 1) if (v >> b) & 1)
        checks.append({"design": "bit%d" % b, "header_ok": header_ok, "base_prefix_identical": prefix_ok,
                       "units_ok": units_ok, "positive_units": positives, "design_population": population})
        if not (header_ok and prefix_ok and units_ok and positives == population):
            raise RuntimeError("encoder B --fix-json design bit%d failed a structural check" % b)
        for v, positive in units.items():
            if positive:
                codes[v] |= 1 << b
    if sorted(codes.values()) != list(range(1, NG + 1)):
        raise RuntimeError("decoded B codes are not a permutation of 1..2646")
    return {by_index[code]: v for v, code in codes.items()}, checks


def battery(fam, inv):
    rep = r1.shape_report(fam, inv)
    distinct = len({frozenset(c) for c in fam}) == len(fam)
    count_ok = len(fam) == r1.EXPECTED["total"]
    failed = [name for name, ok in (("shape_report", rep["ok"]), ("distinct_as_set", distinct), ("count", count_ok)) if not ok]
    return {"shape_report": rep, "distinct_as_set": distinct, "count": len(fam), "count_ok": count_ok,
            "failed_checks": failed, "detected": bool(failed)}


def main():
    out = drv.GENERATOR_RECEIPT
    if os.path.exists(out):
        raise FileExistsError(out)
    supervisor = drv.require_supervisor()
    if os.path.exists(drv.QUARANTINE):
        raise SystemExit("quarantine record %s exists; not started" % drv.QUARANTINE)
    t0 = time.monotonic()
    st = os.statvfs(LANE)
    available = st.f_bavail * st.f_frsize
    gate = {"at": now(), "available_bytes": available, "threshold_bytes": GATE, "projected_growth_bytes": GROWTH}
    if available < GATE + GROWTH:
        gate["status"] = "UNKNOWN / DEFERRED_RESOURCE; controls not run"
        with open(out, "x") as f:
            json.dump({"status": "DEFERRED", "gate": gate}, f, indent=2)
            f.write("\n")
        print(json.dumps(gate))
        return
    gate["status"] = "PASS"
    me = sha(os.path.abspath(__file__))
    with open(drv.AMENDMENT) as f:
        amendment_text = f.read()
    failures = []
    if me not in amendment_text:
        failures.append("frozen amendment %s does not name this generator's SHA" % os.path.relpath(drv.AMENDMENT, LANE))
    rec = {"started_at": now(), "gate": gate, "generator_sha256": me, "environment": environment(),
           "supervisor": supervisor, "pid": os.getpid(),
           "amendment": {"path": os.path.relpath(drv.AMENDMENT, LANE), "sha256": sha(drv.AMENDMENT)},
           "family_source": {"path": "code/k3_cuts_r1.py", "sha256": sha(os.path.join(HERE, "k3_cuts_r1.py"))},
           "status_note": "Controls C1-C4 for the frozen amendment text; no solve; clause block not written"}
    drv.check_code_pins()

    F, amap_str = gram_enc.build(3, None, True, True, None)
    del F
    amap = {}
    for key, v in amap_str.items():
        a, p, q = key.split("|")
        amap[(int(a), tuple(map(int, p.split(","))), tuple(map(int, q.split(","))))] = v
    if amap != k3_cubes.variable_map():
        failures.append("A map differs from the cube wrapper map")
    inv = {v: key for key, v in amap.items()}
    clauses = r1.emit(amap)
    counts = {"at_most_three": sum(1 for c in clauses if len(c) == 4),
              "mixed": sum(1 for c in clauses if len(c) == 5), "total": len(clauses)}
    rec["counts"] = counts
    rec["block_sha256_A"] = r1.serialise_sha(clauses)
    if counts != r1.EXPECTED or rec["block_sha256_A"] != drv.BLOCK_SHA:
        failures.append("counts or block SHA differ from the frozen block")

    # C2 = control (a)
    shape = r1.shape_report(clauses, inv)
    rec["C2_control_a"] = {"shape_report": shape, "distinct_as_set": len({frozenset(c) for c in clauses}) == len(clauses),
                           "count": len(clauses)}
    if not (shape["ok"] and rec["C2_control_a"]["distinct_as_set"] and len(clauses) == r1.EXPECTED["total"]):
        failures.append("C2 failed")

    # C1 and README:91 component checks = control (b)
    spec = r1.spec_family()
    tpl = {frozenset((x, i) for x, idxs in cl for i in idxs) for cl in r1.template()}
    c1 = r1.local_coverage(spec)
    classical = {}
    for slopes in ((1, 2, 3), (1, 2, 4), (2, 3, 5), (4, 5, 6), (1, 3, 6)):
        grams = {s: r1.classical_gram(m) for s, m in zip(r1.SQUARES, slopes)}
        classical["slopes_%d%d%d" % slopes] = r1.violations(clauses, inv, grams)
    genuine = {}
    for x in r1.SQUARES:
        others = [s for s in r1.SQUARES if s != x]
        grams = {x: r1.psi_gram(), others[0]: r1.classical_gram(4), others[1]: r1.classical_gram(2)}
        genuine["psi_as_square_%d" % x] = r1.violations(clauses, inv, grams)
    rec["C1_control_b"] = {
        "spec_size": len(spec), "template_equals_spec": tpl == spec, "C1_local_coverage": c1,
        "classical_AG27_triples_violations": classical, "psi_f_weight5_violations": genuine,
        "readme91_ruling": "Parent disposition 3c9373c0...4e44 decision 2: component-level application; the cut "
                           "clauses must be satisfied by all five classical AG(2,7) triples (shown here for the cut "
                           "clauses alone; the classical triples violate base G4); no genuine K3 positive exists",
        "psi_f_label": "non-vacuity only: Psi(f) beside two classical squares is not a K3 triple"}
    if not (len(spec) == 405 and tpl == spec and c1["ok"] and c1["rejected"] == 450
            and all(v == (0, 0) for v in classical.values()) and all(v == (2940, 0) for v in genuine.values())):
        failures.append("C1 or classical-triple check failed")

    # mutations = control (c)
    mutations = {}
    first_amt = next(i for i, c in enumerate(clauses) if len(c) == 4)
    s, a, b = inv[-clauses[first_amt][-1]]
    p = next(iter({a, b} & set(inv[-clauses[first_amt][0]][1:])))
    r = b if a == p else a
    moved = (next(k for k in range(r1.N) if k not in (r[0], p[0])), r[1])
    m1 = list(clauses)
    m1[first_amt] = clauses[first_amt][:-1] + (-amap[(s, min(p, moved), max(p, moved))],)
    mutations["cross_frame_literal"] = battery(m1, inv)
    first_mixed = next(i for i, c in enumerate(clauses) if len(c) == 5)
    sx = inv[-clauses[first_mixed][0]][0]
    m2 = list(clauses)
    m2[first_mixed] = tuple(-amap[(sx,) + inv[-lit][1:]] for lit in clauses[first_mixed])
    mutations["mixed_square_merge"] = battery(m2, inv)

    def frame_kind(c):
        cell = next(iter(set(inv[-c[0]][1:]) & set(inv[-c[1]][1:])))
        others = [y if x == cell else x for _, x, y in (inv[-lit] for lit in c)]
        return "row" if len({o[0] for o in others}) == 1 else "col"
    rows_only = [c for c in clauses if frame_kind(c) == "row"]
    mutations["column_frames_replaced_by_row_frames"] = battery(rows_only + rows_only, inv)
    m4 = [c for c in clauses if len(c) == 5]
    for frame in r1.FRAMES:
        for pp in r1.off_points(frame):
            pos = r1.positions(frame, pp)
            for x in r1.SQUARES:
                for R in itertools.combinations(range(6), 5):
                    m4.append(tuple(-amap[(x, min(pp, pos[i]), max(pp, pos[i]))] for i in R))
    mutations["at_most_four_instead_of_three"] = battery(m4, inv)
    mutations["one_clause_dropped"] = battery(clauses[1:], inv)

    def wrong_positions(frame, pp):
        kind, k = frame
        if kind == "row":
            return [(k, c) for c in range(r1.N) if c != pp[1]]
        return [(rr, k) for rr in range(r1.N) if rr != pp[1]]
    try:
        r1.emit(amap, wrong_positions)
        mutations["column_frame_exclusion_mistransported"] = {"emitted": True, "detected": False}
    except KeyError as exc:
        mutations["column_frame_exclusion_mistransported"] = {
            "emitted": False, "detected": True, "failed_checks": ["literal validity at emission"],
            "reason": "collinear pair has no variable: %r" % (exc.args[0],)}
    rec["control_c_mutations"] = mutations
    if not all(m["detected"] for m in mutations.values()):
        failures.append("control (c): an undetected mutation")

    # C4 = control (d)
    fam = {frozenset(c) for c in clauses}
    per_generator = {}
    for cube in ("C311", "C321", "C411"):
        for gen in k3_lex.generators(cube):
            perm = k3_lex.image(amap, gen)
            per_generator["%s %s" % (cube, json.dumps(gen, sort_keys=True))] = \
                {frozenset(-perm[-lit] for lit in c) for c in fam} == fam
    tperm = {}
    for (sq, pa, pb), v in amap.items():
        ta, tb = (pa[1], pa[0]), (pb[1], pb[0])
        tperm[v] = amap[(sq, min(ta, tb), max(ta, tb))]
    transposition = {frozenset(-tperm[-lit] for lit in c) for c in fam} == fam
    reduced = fam - {frozenset(clauses[0])}
    nonvacuous = False
    for cube in ("C311", "C321", "C411"):
        for gen in k3_lex.generators(cube):
            perm = k3_lex.image(amap, gen)
            if {frozenset(-perm[-lit] for lit in c) for c in reduced} != reduced:
                nonvacuous = True
                break
        if nonvacuous:
            break
    rec["C4_control_d"] = {"generators": len(per_generator), "all_invariant": all(per_generator.values()),
                           "transposition_of_all_three_squares_invariant": transposition,
                           "family_minus_one_clause_fails_for_some_generator": nonvacuous,
                           "per_generator": per_generator}
    if not (len(per_generator) == 22 and all(per_generator.values()) and transposition and nonvacuous):
        failures.append("C4 failed")

    # C3 = control (e)
    with open(drv.ORACLE_RECEIPT) as f:
        oracle = json.load(f)
    drv.check_oracle(oracle, sha(drv.ORACLE_RECEIPT))
    meta_path = os.path.join(LANE, drv.ROUTES["B"]["input_meta"])
    with open(meta_path) as f:
        drv.check_b_c311_binding(json.load(f), sha(meta_path), oracle)
    nv0, nc0, base_body = b_output(None)
    base_sha = hashlib.sha256(("p cnf %d %d\n" % (nv0, nc0)).encode() + base_body).hexdigest()
    base_ok = (nv0, nc0) == B_BASE and base_sha == oracle["B_base"]["sha256"]
    if not base_ok:
        failures.append("encoder B base output differs from the oracle base")
    bmap, design_checks = decode_b_map(amap, base_body)
    del base_body
    clauses_b = r1.emit(bmap)
    swapped = dict(amap)
    k_first = next(k for k, v in amap.items() if v == 1)
    k_last = next(k for k, v in amap.items() if v == NG)
    swapped[k_first], swapped[k_last] = swapped[k_last], swapped[k_first]
    rec["C3_control_e"] = {
        "oracle_receipt_asserted": {"sha256": sha(drv.ORACLE_RECEIPT), "status": oracle["status"]},
        "B_C311_metadata_bound_to_oracle": {"metadata_sha256": sha(meta_path), "ok": True},
        "B_base_output": {"variables": nv0, "clauses": nc0, "sha256": base_sha, "equals_oracle_base": base_ok},
        "fix_json_design_checks": design_checks,
        "datum_B_map_equals_A_map": bmap == amap,
        "consequences_of_the_datum": {"block_sha256_B": r1.serialise_sha(clauses_b),
                                      "block_sha_equal": r1.serialise_sha(clauses_b) == rec["block_sha256_A"],
                                      "sets_equal": {frozenset(c) for c in clauses_b} == fam},
        "sha_sensitivity_swapped_map_changes_block_sha": r1.serialise_sha(r1.emit(swapped)) != rec["block_sha256_A"]}
    if not (base_ok and bmap == amap and rec["C3_control_e"]["consequences_of_the_datum"]["block_sha_equal"]
            and rec["C3_control_e"]["sha_sensitivity_swapped_map_changes_block_sha"]):
        failures.append("C3 failed")

    rec.update({"status": "PASS" if not failures else "FAIL", "failures": failures, "finished_at": now(),
                "seconds": round(time.monotonic() - t0, 3), "block_written": False})
    with open(out, "x") as f:
        json.dump(rec, f, indent=2)
        f.write("\n")
    print(json.dumps({"status": rec["status"], "block_sha256_A": rec["block_sha256_A"], "seconds": rec["seconds"],
                      "failures": failures}))
    print("receipt_sha256", sha(out))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        if not os.path.exists(drv.GENERATOR_RECEIPT):
            with open(drv.GENERATOR_RECEIPT, "x") as f:
                json.dump({"status": "FAIL", "failures": ["exception: %r" % (exc,)], "finished_at": now(),
                           "generator_sha256": sha(os.path.abspath(__file__))}, f, indent=2)
                f.write("\n")
        raise
