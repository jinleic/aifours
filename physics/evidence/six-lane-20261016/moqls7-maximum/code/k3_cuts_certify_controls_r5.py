#!/usr/bin/env python3
"""k3_cuts_certify_controls_r5.py: pre-solve, parser and transport controls for the C311+cuts driver r5.

New version of controls r4 (646798ef...07e5). Controls r1 to r4 are preserved and were never run. The only changes
from r4: it uses driver r5 (frozen AMENDMENT-4.r4, delta r5) and generator r6, and it takes the supervisor and
supervisor-controls file names from the frozen delta (supervise_r3.py, supervise_controls_r3.py). It must run as the
session/group leader under that pinned supervisor, so the in-process preparation, the B encoder child and the tiny
solver/checker runs are all inside the supervised group. Supervisor behaviour is tested separately by the
supervisor controls, because those tests create their own process groups. Every check is designed to fail on a
wrong driver.
1. Bindings among the frozen amendment r4, the frozen delta r5, the driver r5, this script, generator r6, the
   supervisor and the supervisor controls; the generator r6 receipt PASS; lane code pins; the oracle receipt PASS
   with its pins;
   the B_C311 metadata bound to the oracle.
2. Status-line parser: synthetic byte logs. Only exactly [b"s VERIFIED"] or [b"s UNSATISFIABLE"] counts; leading,
   trailing or tab whitespace, duplicate lines, NOT VERIFIED and TIMEOUT do not. Real-log replays: the A/C321
   checker and solver logs are accepted; the B/C321 r5 timeout log is rejected.
3. Creation-only directories: this script's own directory is made by os.mkdir, and a second mkdir must raise.
4. Pre-solve appender checks on both routes, plus negative controls that must each raise in the intended check: a
   mutated block clause; a header without the increment; the wrong instance (by SHA and against the file); a
   one-byte change (against the file and by SHA); oracle receipts with status FAIL, another B base or another
   receipt SHA; B_C311 metadata with another base hash or another file SHA.
5. Transport controls on tiny CNFs through the driver's stream_pipeline, for cadical and kissat. The base is PHP(5,4)
   without pigeon 5's clause (SAT), and the block is that clause:
   (i) base + block to both: verified, with matching feeds and exact status lines;
   (ii) base only: solver rc 10, not verified;
   (iii) solver gets base + block, checker gets base only: not verified, and the checker feed SHA differs.
Usage (only under the supervisor, see the delta): /usr/bin/python3 -I -B k3_cuts_certify_controls_r5.py
"""
import copy
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import k3_cubes  # noqa: E402
import k3_cuts_certify_r5 as drv  # noqa: E402
import k3_cuts_r1 as r1  # noqa: E402
from gram_certify_r4 import now, sha  # noqa: E402

LANE = os.path.dirname(HERE)
OUT = drv.CONTROLS_RECEIPT
TEST_DIR = os.path.join(LANE, "evidence", "k3cubes", "cuts_cert_controls_r5")
GATE, GROWTH = 12200000000, 2097152


def expect_raise(fn, *args):
    try:
        fn(*args)
    except AssertionError as exc:
        return {"raised": True, "message": str(exc)}
    return {"raised": False}


def php_parts(pigeons, holes, with_block):
    var = lambda i, j: (i - 1) * holes + j
    base = [[var(i, j) for j in range(1, holes + 1)] for i in range(1, pigeons)]
    for j in range(1, holes + 1):
        for i in range(1, pigeons + 1):
            for k in range(i + 1, pigeons + 1):
                base.append([-var(i, j), -var(k, j)])
    body = b"".join(drv.dimacs_line(c) for c in base)
    if with_block:
        block = drv.dimacs_line([var(pigeons, j) for j in range(1, holes + 1)])
        return [drv.dimacs_header(pigeons * holes, len(base) + 1), body, block]
    return [drv.dimacs_header(pigeons * holes, len(base)), body]


def parser_controls():
    cases = {
        "drat_trim_cr_prefixed": (b"c parsing\n\rs VERIFIED\n\rc verification time: 1.0 seconds\n", b"s VERIFIED", True),
        "crlf_line_end": (b"s VERIFIED\r\n", b"s VERIFIED", True),
        "trailing_space": (b"\rs VERIFIED \n", b"s VERIFIED", False),
        "leading_space": (b" s VERIFIED\n", b"s VERIFIED", False),
        "tab_suffix": (b"s VERIFIED\t\n", b"s VERIFIED", False),
        "duplicate": (b"s VERIFIED\ns VERIFIED\n", b"s VERIFIED", False),
        "not_verified": (b"\rs NOT VERIFIED\n", b"s VERIFIED", False),
        "timeout": (b"\rs TIMEOUT\n", b"s VERIFIED", False),
        "solver_unsat": (b"s UNSATISFIABLE\n", b"s UNSATISFIABLE", True),
        "solver_trailing_space": (b"s UNSATISFIABLE \n", b"s UNSATISFIABLE", False),
        "solver_sat": (b"s SATISFIABLE\nv 1 -2 0\n", b"s UNSATISFIABLE", False),
    }
    out = {}
    for name, (data, wanted, expected) in cases.items():
        got = drv.status_lines(data)
        out[name] = {"status_lines": drv.shown(got), "accepted": got == [wanted], "expected": expected,
                     "ok": (got == [wanted]) == expected}
    real = {"A_C321_checker": ("evidence/k3cubes/cert_r2/A_C321.checker.log", b"s VERIFIED", True),
            "A_C321_solver": ("evidence/k3cubes/cert_r2/A_C321.solver.log", b"s UNSATISFIABLE", True),
            "B_C321_r5_checker_timeout": ("evidence/k3cubes/cert_B_r5/B_C321.checker.log", b"s VERIFIED", False)}
    for name, (rel, wanted, expected) in real.items():
        got = drv.log_status_lines(drv.lane_path(rel))
        out["real_" + name] = {"path": rel, "sha256": sha(drv.lane_path(rel)), "status_lines": drv.shown(got),
                               "accepted": got == [wanted], "expected": expected, "ok": (got == [wanted]) == expected}
    return out


def transport_case(name, solver, solver_parts, checker_parts):
    prefix = os.path.join(TEST_DIR, "%s_%s" % (solver, name))
    result = drv.stream_pipeline(solver_parts, checker_parts, solver, prefix, 60, 60, 120)
    result["expected_solver_feed_sha256"] = drv.digest(solver_parts)
    result["expected_checker_feed_sha256"] = drv.digest(checker_parts)
    result["feeds_equal_expected"] = (
        result["feeds"]["solver"].get("sha256") == result["expected_solver_feed_sha256"]
        and result["feeds"]["checker"].get("sha256") == result["expected_checker_feed_sha256"]
        and result["feeds"]["solver"].get("bytes_written") == sum(len(p) for p in solver_parts)
        and result["feeds"]["checker"].get("bytes_written") == sum(len(p) for p in checker_parts))
    return result


def run_controls(rec, failures, me, driver_sha, generator_sha, supervisor_sha, supervisor_controls_sha, amendment_sha):
    with open(drv.AMENDMENT) as f:
        text = f.read()
    with open(drv.DELTA) as f:
        delta = json.load(f)
    with open(drv.GENERATOR_RECEIPT) as f:
        generator = json.load(f)
    with open(drv.ORACLE_RECEIPT) as f:
        oracle = json.load(f)
    drv.check_code_pins()
    drv.check_oracle(oracle, sha(drv.ORACLE_RECEIPT))
    meta_path = drv.lane_path(drv.ROUTES["B"]["input_meta"])
    with open(meta_path) as f:
        meta = json.load(f)
    drv.check_b_c311_binding(meta, sha(meta_path), oracle)
    bindings = {"amendment_names_driver": driver_sha in text, "amendment_names_controls": me in text,
                "amendment_names_generator": generator_sha in text, "amendment_names_supervisor": supervisor_sha in text,
                "amendment_names_supervisor_controls": supervisor_controls_sha in text,
                "delta_pins_amendment": delta["amendment"]["sha256"] == amendment_sha,
                "delta_pins_driver": delta["driver"]["sha256"] == driver_sha,
                "delta_pins_controls": delta["controls"]["sha256"] == me,
                "delta_pins_generator": delta["generator"]["sha256"] == generator_sha,
                "delta_pins_supervisor": delta["supervisor"]["sha256"] == supervisor_sha,
                "delta_pins_supervisor_controls": delta["supervisor_controls"]["sha256"] == supervisor_controls_sha,
                "generator_receipt_pass_bound_to_amendment": generator.get("status") == "PASS"
                and generator["amendment"]["sha256"] == amendment_sha and generator["generator_sha256"] == generator_sha,
                "oracle_pass_with_pins": True, "B_C311_metadata_bound_to_oracle": True}
    rec["bindings"] = bindings
    if not all(bindings.values()):
        failures.append("binding check failed")

    rec["parser_controls"] = parser_controls()
    if not all(v["ok"] for v in rec["parser_controls"].values()):
        failures.append("parser control failed")

    drv.make_route_dir(TEST_DIR)
    try:
        drv.make_route_dir(TEST_DIR)
        rec["creation_only_directory"] = {"second_mkdir_raised": False}
    except FileExistsError:
        rec["creation_only_directory"] = {"second_mkdir_raised": True}
    if not rec["creation_only_directory"]["second_mkdir_raised"]:
        failures.append("creation-only directory control failed")

    routes, prepared = {}, {}
    for name in ("A", "B"):
        prepared[name] = drv.prepare(name, oracle)
        routes[name] = prepared[name]["summary"]
    rec["routes"] = routes
    neg = {}
    clauses = r1.emit(k3_cubes.variable_map())
    bad = list(clauses)
    bad[0] = (-1 if bad[0][0] != -1 else -2,) + tuple(bad[0][1:])
    neg["mutated_block_clause"] = expect_raise(drv.check_block, b"".join(drv.dimacs_line(c) for c in bad), bad)
    del clauses, bad
    a_parts = prepared["A"]["parts"]
    nv, nc = drv.ROUTES["A"]["input_header"]
    neg["header_without_increment"] = expect_raise(drv.check_header, [drv.dimacs_header(nv, nc)] + a_parts[1:],
                                                   drv.ROUTES["A"]["strengthened_header"])
    with open(drv.lane_path("explore/k3cubes/A_C311.cnf"), "rb") as f:
        original = f.read()
    neg["wrong_instance_sha"] = expect_raise(drv.check_input, [original], drv.ROUTES["A"]["input_sha256"])
    neg["wrong_instance_against_named_file"] = expect_raise(drv.check_prefix_against_file,
                                                            drv.lane_path(drv.ROUTES["A"]["input"]), [original])
    del original
    changed = bytearray(a_parts[1])
    changed[len(changed) // 2] ^= 1
    input_header = drv.dimacs_header(*drv.ROUTES["A"]["input_header"])
    neg["one_byte_change_against_named_file"] = expect_raise(drv.check_prefix_against_file,
                                                             drv.lane_path(drv.ROUTES["A"]["input"]),
                                                             [input_header, bytes(changed)])
    neg["one_byte_change_input_sha"] = expect_raise(drv.check_input, [input_header, bytes(changed)],
                                                    drv.ROUTES["A"]["input_sha256"])
    del changed
    for label, field, value in (("oracle_status_fail", "status", "FAIL"),
                                ("oracle_other_B_base", "B_base", dict(oracle["B_base"], sha256="0" * 64))):
        tampered = copy.deepcopy(oracle)
        tampered[field] = value
        neg[label] = expect_raise(drv.check_oracle, tampered, sha(drv.ORACLE_RECEIPT))
    neg["oracle_other_receipt_sha"] = expect_raise(drv.check_oracle, oracle, "0" * 64)
    neg["B_C311_other_base_hash"] = expect_raise(drv.check_b_c311_binding, dict(meta, base_cnf_sha256="0" * 64),
                                                 sha(meta_path), oracle)
    neg["B_C311_other_metadata_sha"] = expect_raise(drv.check_b_c311_binding, meta, "0" * 64, oracle)
    rec["negative_controls"] = neg
    if not all(v["raised"] for v in neg.values()):
        failures.append("a negative control did not raise")
    del prepared, a_parts

    transport = {}
    unsat, sat = php_parts(5, 4, True), php_parts(5, 4, False)
    pins = {"cadical": drv.ROUTES["A"]["solver_sha256"], "kissat": drv.ROUTES["B"]["solver_sha256"]}
    for solver in ("cadical", "kissat"):
        c1 = transport_case("unsat_with_block", solver, unsat, unsat)
        c2 = transport_case("sat_without_block", solver, sat, sat)
        c3 = transport_case("checker_fed_without_block", solver, unsat, sat)
        verdicts = {
            "unsat_with_block_verified": c1["transport_verified"] is True and c1["feeds_equal_expected"]
            and c1["checker_status_lines"] == ["s VERIFIED"] and c1["solver_status_lines"] == ["s UNSATISFIABLE"],
            "sat_without_block_rejected": c2["solver_rc"] == 10 and c2["transport_verified"] is False
            and c2["feeds_equal_expected"],
            "checker_mismatch_rejected": c3["transport_verified"] is False and c3["feeds_equal_expected"]
            and c3["feeds"]["checker"]["sha256"] != c3["feeds"]["solver"]["sha256"],
            "solver_binary_pinned": c1["solver_binary_sha256"] == pins[solver],
            "checker_binary_pinned": c1["checker_binary_sha256"] == drv.CHECKER_SHA,
            "no_children_alive_after_stop": not any(c["children_alive_after_stop"] for c in (c1, c2, c3))}
        transport[solver] = {"cases": {"unsat_with_block": c1, "sat_without_block": c2, "checker_fed_without_block": c3},
                             "verdicts": verdicts}
        if not all(verdicts.values()):
            failures.append("transport control failed for %s" % solver)
    rec["transport_controls"] = transport


def main():
    if os.path.exists(OUT):
        raise FileExistsError(OUT)
    supervisor = drv.require_supervisor()
    if os.path.exists(drv.QUARANTINE):
        raise SystemExit("quarantine record %s exists; not started" % drv.QUARANTINE)
    t0 = time.monotonic()
    st = os.statvfs(LANE)
    available = st.f_bavail * st.f_frsize
    gate = {"at": now(), "available_bytes": available, "threshold_bytes": GATE, "projected_growth_bytes": GROWTH}
    me, driver_sha = sha(os.path.abspath(__file__)), sha(os.path.abspath(drv.__file__))
    with open(drv.DELTA) as f:
        pinned = json.load(f)
    generator_sha = sha(os.path.join(LANE, pinned["generator"]["path"]))
    supervisor_sha = sha(os.path.join(LANE, pinned["supervisor"]["path"]))
    supervisor_controls_sha = sha(os.path.join(LANE, pinned["supervisor_controls"]["path"]))
    amendment_sha, delta_sha = sha(drv.AMENDMENT), sha(drv.DELTA)
    rec = {"started_at": now(), "gate": gate, "controls_sha256": me, "driver_sha256": driver_sha,
           "generator_sha256": generator_sha, "supervisor_sha256": supervisor_sha,
           "supervisor_controls_sha256": supervisor_controls_sha, "amendment_sha256": amendment_sha,
           "delta_sha256": delta_sha, "supervisor": supervisor, "environment": drv.environment()}
    failures = []
    if available < GATE + GROWTH:
        gate["status"] = "UNKNOWN / DEFERRED_RESOURCE; controls not run"
        rec["status"] = "DEFERRED"
    else:
        gate["status"] = "PASS"
        try:
            run_controls(rec, failures, me, driver_sha, generator_sha, supervisor_sha, supervisor_controls_sha,
                         amendment_sha)
            rec["status"] = "PASS" if not failures else "FAIL"
        except Exception as exc:
            rec["status"] = "FAIL"
            failures.append("exception: %r" % (exc,))
    rec.update({"failures": failures, "finished_at": now(), "seconds": round(time.monotonic() - t0, 3),
                "quarantine_present": os.path.exists(drv.QUARANTINE)})
    with open(OUT, "x") as f:
        json.dump(rec, f, indent=2)
        f.write("\n")
    print(json.dumps({"status": rec["status"], "failures": failures, "seconds": rec["seconds"],
                      "strengthened": {k: v["strengthened_sha256"] for k, v in rec.get("routes", {}).items()}}))
    print("receipt_sha256", sha(OUT))
    raise SystemExit(0 if rec["status"] == "PASS" else 3)


if __name__ == "__main__":
    main()
