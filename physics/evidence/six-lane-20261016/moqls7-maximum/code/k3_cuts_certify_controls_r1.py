#!/usr/bin/env python3
"""k3_cuts_certify_controls_r1.py: pre-solve and transport controls for the C311+cuts appender/driver (MAJOR-A).

Run after AMENDMENT-4.r3 and K3-CUTS-CERT-DELTA.r1 are frozen and generator r2 has passed, before any C311+cuts
launch. Each check is designed to fail on a wrong appender or transport.
1. Bindings: the frozen r3 text names the driver, this script and generator r2; the frozen delta pins r3, the
   driver, this script and generator r2; the generator r2 receipt is PASS and bound to r3; lane code pins hold; the
   oracle receipt is PASS with its pins; the B_C311 metadata is bound to the oracle base, wrapper and encoder.
2. For each route, the driver's prepare() regenerates the named input in memory and asserts the input SHA, both
   headers, byte equality with the named file, the block SHA and count. The strengthened SHA is recorded here and
   later asserted again by the driver.
3. Negative controls, each of which must raise in the intended check: a mutated block clause; a header without the
   increment; the wrong instance (A original C311 offered as the lex input); a one-byte change against the named
   file; oracle receipts with status FAIL, a different B base or a different receipt SHA; B_C311 metadata with a
   different base hash or a different file SHA.
4. Transport controls on tiny CNFs through the driver's stream_pipeline, for cadical and for kissat. The base is
   PHP(5,4) without pigeon 5's clause (SAT) and the block is that clause, so only base + block is UNSAT:
   (i) base + block to both: verified, both feeds equal the expected bytes and SHA;
   (ii) base only (SAT): solver rc 10, not verified;
   (iii) solver gets base + block, checker gets base only: not verified, checker feed SHA differs.
Usage: /usr/bin/python3 -I -B k3_cuts_certify_controls_r1.py
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
import k3_cuts_certify_r1 as drv  # noqa: E402
import k3_cuts_r1 as r1  # noqa: E402
from gram_certify_r4 import now, sha  # noqa: E402

LANE = os.path.dirname(HERE)
OUT = drv.CONTROLS_RECEIPT
TRANSPORT_DIR = os.path.join(LANE, "evidence", "k3cubes", "cuts_cert_controls_r1")
GATE, GROWTH = 12200000000, 2097152


def expect_raise(fn, *args):
    try:
        fn(*args)
    except AssertionError as exc:
        return {"raised": True, "message": str(exc)}
    return {"raised": False}


def php_parts(with_block):
    var = lambda i, j: (i - 1) * 4 + j
    base = [[var(i, j) for j in range(1, 5)] for i in range(1, 5)]
    for j in range(1, 5):
        for i in range(1, 6):
            for k in range(i + 1, 6):
                base.append([-var(i, j), -var(k, j)])
    block = [[var(5, j) for j in range(1, 5)]]
    body = b"".join(drv.dimacs_line(c) for c in base)
    if with_block:
        return [drv.dimacs_header(20, len(base) + 1), body, b"".join(drv.dimacs_line(c) for c in block)]
    return [drv.dimacs_header(20, len(base)), body]


def transport_case(name, solver, solver_parts, checker_parts):
    prefix = os.path.join(TRANSPORT_DIR, "%s_%s" % (solver, name))
    result = drv.stream_pipeline(solver_parts, checker_parts, solver, prefix, 60, 60, 120)
    expected_solver = drv.digest(solver_parts)
    expected_checker = drv.digest(checker_parts)
    result["expected_solver_feed_sha256"] = expected_solver
    result["expected_checker_feed_sha256"] = expected_checker
    result["feeds_equal_expected"] = (
        result["feeds"]["solver"].get("sha256") == expected_solver
        and result["feeds"]["checker"].get("sha256") == expected_checker
        and result["feeds"]["solver"].get("bytes_written") == sum(len(p) for p in solver_parts)
        and result["feeds"]["checker"].get("bytes_written") == sum(len(p) for p in checker_parts))
    return result


def main():
    if os.path.exists(OUT):
        raise FileExistsError(OUT)
    t0 = time.monotonic()
    st = os.statvfs(LANE)
    available = st.f_bavail * st.f_frsize
    gate = {"at": now(), "available_bytes": available, "threshold_bytes": GATE, "projected_growth_bytes": GROWTH}
    if available < GATE + GROWTH:
        gate["status"] = "UNKNOWN / DEFERRED_RESOURCE; controls not run"
        with open(OUT, "x") as f:
            json.dump({"status": "DEFERRED", "gate": gate}, f, indent=2)
            f.write("\n")
        print(json.dumps(gate))
        return
    gate["status"] = "PASS"
    failures = []
    me, driver_sha = sha(os.path.abspath(__file__)), sha(os.path.abspath(drv.__file__))
    generator_sha = sha(os.path.join(HERE, "k3_cuts_r2.py"))
    amendment_sha, delta_sha = sha(drv.AMENDMENT), sha(drv.DELTA)
    rec = {"started_at": now(), "gate": gate, "controls_sha256": me, "driver_sha256": driver_sha,
           "generator_r2_sha256": generator_sha, "amendment_sha256": amendment_sha, "delta_sha256": delta_sha,
           "environment": drv.environment()}

    # 1. bindings
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
    bindings = {"r3_names_driver": driver_sha in text, "r3_names_controls": me in text,
                "r3_names_generator_r2": generator_sha in text,
                "delta_pins_r3": delta["amendment"]["sha256"] == amendment_sha,
                "delta_pins_driver": delta["driver"]["sha256"] == driver_sha,
                "delta_pins_controls": delta["controls"]["sha256"] == me,
                "delta_pins_generator_r2": delta["generator_r2"]["sha256"] == generator_sha,
                "generator_r2_receipt_pass_bound_to_r3": generator.get("status") == "PASS"
                and generator["amendment"]["sha256"] == amendment_sha and generator["generator_sha256"] == generator_sha,
                "oracle_pass_with_pins": True, "B_C311_metadata_bound_to_oracle": True}
    rec["bindings"] = bindings
    if not all(bindings.values()):
        failures.append("binding check failed")

    # 2. pre-solve appender checks on both routes
    routes, prepared = {}, {}
    for name in ("A", "B"):
        prepared[name] = drv.prepare(name, oracle)
        routes[name] = prepared[name]["summary"]
    rec["routes"] = routes

    # 3. negative controls
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
    del prepared

    # 4. transport controls
    os.makedirs(TRANSPORT_DIR, exist_ok=True)
    transport = {}
    unsat, sat = php_parts(True), php_parts(False)
    for solver in ("cadical", "kissat"):
        pins = {"cadical": drv.ROUTES["A"]["solver_sha256"], "kissat": drv.ROUTES["B"]["solver_sha256"]}
        c1 = transport_case("unsat_with_block", solver, unsat, unsat)
        c2 = transport_case("sat_without_block", solver, sat, sat)
        c3 = transport_case("checker_fed_without_block", solver, unsat, sat)
        verdicts = {
            "unsat_with_block_verified": c1["transport_verified"] and c1["feeds_equal_expected"]
            and c1["feeds"]["solver"]["sha256"] == drv.digest(unsat) == c1["feeds"]["checker"]["sha256"],
            "sat_without_block_rejected": c2["solver_rc"] == 10 and not c2["transport_verified"] and c2["feeds_equal_expected"],
            "checker_mismatch_rejected": not c3["transport_verified"] and c3["feeds_equal_expected"]
            and c3["feeds"]["checker"]["sha256"] != c3["feeds"]["solver"]["sha256"],
            "solver_binary_pinned": c1["solver_binary_sha256"] == pins[solver],
            "checker_binary_pinned": c1["checker_binary_sha256"] == drv.CHECKER_SHA}
        transport[solver] = {"cases": {"unsat_with_block": c1, "sat_without_block": c2, "checker_fed_without_block": c3},
                             "verdicts": verdicts}
        if not all(verdicts.values()):
            failures.append("transport control failed for %s" % solver)
    rec["transport_controls"] = transport

    rec.update({"status": "PASS" if not failures else "FAIL", "failures": failures, "finished_at": now(),
                "seconds": round(time.monotonic() - t0, 3)})
    with open(OUT, "x") as f:
        json.dump(rec, f, indent=2)
        f.write("\n")
    print(json.dumps({"status": rec["status"], "failures": failures, "seconds": rec["seconds"],
                      "strengthened": {k: v["strengthened_sha256"] for k, v in routes.items()}}))
    print("receipt_sha256", sha(OUT))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        if not os.path.exists(OUT):
            with open(OUT, "x") as f:
                json.dump({"status": "FAIL", "failures": ["exception: %r" % (exc,)], "finished_at": now(),
                           "controls_sha256": sha(os.path.abspath(__file__))}, f, indent=2)
                f.write("\n")
        raise
