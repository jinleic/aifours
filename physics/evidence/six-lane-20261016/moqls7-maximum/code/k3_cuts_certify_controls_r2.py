#!/usr/bin/env python3
"""k3_cuts_certify_controls_r2.py: pre-solve, parser, guard and transport controls for the C311+cuts driver r2.

New version of k3_cuts_certify_controls_r1.py (1dc761d1...0025, preserved, never run). Run it after AMENDMENT-4.r3
and K3-CUTS-CERT-DELTA.r2 are frozen and generator r3 has passed, and before any C311+cuts launch. Every check is
designed to fail on a wrong driver.
1. Bindings among the frozen r3 text, the frozen delta, the driver, this script, generator r3 and the stage guard;
   the generator r3 receipt PASS; lane code pins; the oracle receipt PASS with its pins; the B_C311 metadata bound
   to the oracle.
2. Status-line parser (review item 1): synthetic byte logs. Only exactly [b"s VERIFIED"] or [b"s UNSATISFIABLE"]
   counts; leading, trailing or tab whitespace, duplicates, NOT VERIFIED and TIMEOUT do not. Replays of the real
   A/C321 checker and solver logs (accepted) and of the B/C321 r5 timeout log (rejected).
3. Creation-only route directory (review item 4): a second os.mkdir of the same route directory raises.
4. Pre-solve appender checks for both routes, each inside a StageGuard, plus negative controls (as in r1): a mutated
   block clause; a header without the increment; the wrong instance (by SHA and against the file); a one-byte
   change (against the file and by SHA); oracle receipts with status FAIL, another B base or another receipt SHA;
   B_C311 metadata with another base hash or another file SHA.
5. Guard controls (review items 2 and 3), with quarantine records only in this script's own directory:
   GC1 wall-cap trip stops an owned child by SIGTERM; GC2 an RSS trip (injected sampler) stops it; GC3 a sampler
   exception fails closed and stops it; GC4 a child and grandchild that ignore SIGTERM are found, survive the grace
   period and are quarantined, then exit by themselves (no SIGKILL); GC5 external SIGTERM to a separate guarded
   process stops its child and gives a trip; GC6 external SIGTERM to a separate process running stream_pipeline on
   a hard CNF (PHP(12,11)) stops solver and checker and gives UNKNOWN, for cadical and for kissat.
6. Transport controls on tiny CNFs through stream_pipeline inside a StageGuard, for cadical and kissat. The base is
   PHP(5,4) without pigeon 5's clause (SAT) and the block is that clause:
   (i) base + block to both: verified, with matching feeds;
   (ii) base only: solver rc 10, not verified;
   (iii) solver gets base + block, checker gets base only: not verified, checker feed SHA differs.
Usage: /usr/bin/python3 -I -B k3_cuts_certify_controls_r2.py
"""
import copy
import json
import os
import signal
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import k3_cubes  # noqa: E402
import k3_cuts_certify_r2 as drv  # noqa: E402
import k3_cuts_r1 as r1  # noqa: E402
import stage_guard_r1 as sg  # noqa: E402
from gram_certify_r4 import now, rss, sha  # noqa: E402

LANE = os.path.dirname(HERE)
OUT = drv.CONTROLS_RECEIPT
TEST_DIR = os.path.join(LANE, "evidence", "k3cubes", "cuts_cert_controls_r2")
GATE, GROWTH = 12200000000, 4194304
CHILD_PRELUDE = "import json, sys, time\nsys.path.insert(0, %r)\nimport stage_guard_r1 as sg\nsg.install_process_handlers()\n" % HERE


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


def alive(pid):
    return rss(pid) > 0


def guard(name, wall, quarantine, grace=5.0, sampler=sg.tree_rss):
    return sg.StageGuard(name, wall, drv.RSS_CAP, drv.FLOOR, LANE, os.path.join(TEST_DIR, quarantine), grace=grace,
                         sampler=sampler)


def delayed_sampler(kind):
    calls = {"n": 0}

    def sampler(pid):
        calls["n"] += 1
        if calls["n"] > 4:
            if kind == "rss":
                return 1 << 40
            raise RuntimeError("injected sampler failure")
        return sg.tree_rss(pid)
    return sampler


def owned_child_case(name, wall, sampler, command, grace=5.0):
    g = guard(name, wall, name + ".quarantine.json", grace=grace, sampler=sampler)
    t0, out, child = time.monotonic(), {}, None
    try:
        with g:
            child = g.popen(command)
            child.wait()
        out["outcome"] = "completed"
    except sg.StageTrip as exc:
        out["outcome"] = "trip"
        out["reason"] = str(exc)
    out.update({"elapsed_seconds": round(time.monotonic() - t0, 3), "guard": g.record(),
                "child_returncode": child.returncode if child is not None else None,
                "quarantine_exists": os.path.exists(os.path.join(TEST_DIR, name + ".quarantine.json"))})
    return out, g, child


def guard_controls():
    res = {}
    out, g, _ = owned_child_case("gc1_wall", 2, sg.tree_rss, ["/bin/sleep", "30"])
    out["ok"] = (out["outcome"] == "trip" and out["reason"].startswith("stage wall cap") and out["child_returncode"] == -15
                 and not g.survivors and not out["quarantine_exists"] and out["elapsed_seconds"] < 15)
    res["GC1_wall_trip_stops_owned_child"] = out
    out, g, _ = owned_child_case("gc2_rss", 60, delayed_sampler("rss"), ["/bin/sleep", "30"])
    out["ok"] = (out["outcome"] == "trip" and out["reason"].startswith("aggregate RSS above") and out["child_returncode"] == -15
                 and not g.survivors and not out["quarantine_exists"])
    res["GC2_rss_trip_stops_owned_child"] = out
    out, g, _ = owned_child_case("gc3_sampler", 60, delayed_sampler("exception"), ["/bin/sleep", "30"])
    out["ok"] = (out["outcome"] == "trip" and out["reason"].startswith("sampler exception") and out["child_returncode"] == -15
                 and not g.survivors and not out["quarantine_exists"])
    res["GC3_sampler_exception_fails_closed"] = out
    out, g, child = owned_child_case("gc4_survivor", 1, sg.tree_rss,
                                     ["/bin/sh", "-c", "trap '' TERM; /bin/sleep 12; :"], grace=3.0)
    listed = list(g.survivors)
    deadline = time.monotonic() + 40
    while any(alive(p) for p in listed) and time.monotonic() < deadline:
        time.sleep(0.5)
    if child is not None:
        child.poll()
    out.update({"survivors_listed": listed, "grandchild_listed": len(listed) >= 2,
                "survivors_exited_without_sigkill": not any(alive(p) for p in listed)})
    out["ok"] = (out["outcome"] == "trip" and out["quarantine_exists"] and len(listed) >= 2
                 and out["survivors_exited_without_sigkill"])
    res["GC4_survivors_quarantined"] = out

    code5 = CHILD_PRELUDE + (
        "g = sg.StageGuard('gc5_child', 120, %d, %d, %r, %r, grace=5)\n"
        "out = {}\nc = None\n"
        "try:\n"
        "    with g:\n"
        "        c = g.popen(['/bin/sleep', '60'])\n"
        "        print(json.dumps({'ready': True, 'sleep_pid': c.pid}), flush=True)\n"
        "        c.wait()\n"
        "    out['outcome'] = 'completed'\n"
        "except sg.StageTrip as exc:\n"
        "    out['outcome'] = 'trip'\n    out['reason'] = str(exc)\n"
        "out['sleep_returncode'] = c.wait() if c is not None else None\n"
        "out['survivors'] = g.survivors\n"
        "print(json.dumps(out), flush=True)\n") % (drv.RSS_CAP, drv.FLOOR, LANE, os.path.join(TEST_DIR, "gc5.quarantine.json"))
    res["GC5_external_sigterm_guarded_stage"] = external_sigterm_case("gc5_outer", code5, 1.0)
    r5 = res["GC5_external_sigterm_guarded_stage"]
    final = r5.get("final") or {}
    r5["ok"] = (final.get("outcome") == "trip" and final.get("reason") == "external SIGTERM"
                and final.get("sleep_returncode") == -15 and final.get("survivors") == []
                and not alive((r5.get("ready") or {}).get("sleep_pid", 0) or 0))

    for solver in ("cadical", "kissat"):
        code6 = CHILD_PRELUDE + (
            "import k3_cuts_certify_r2 as drv\n"
            "parts = %r\n"
            "g = sg.StageGuard('gc6_child', 300, drv.RSS_CAP, drv.FLOOR, drv.LANE, %r, grace=10)\n"
            "res, out = None, {}\n"
            "try:\n"
            "    with g:\n"
            "        print(json.dumps({'ready': True}), flush=True)\n"
            "        res = drv.stream_pipeline(parts, parts, %r, %r, 60, 60, 120, g)\n"
            "except sg.StageTrip as exc:\n"
            "    out['trip'] = str(exc)\n"
            "out['guard'] = g.record()\n"
            "out['result'] = None if res is None else {k: res[k] for k in ('solver_rc', 'checker_rc', 'checker_status_lines', "
            "'solver_status_lines', 'transport_verified', 'safety_stop_reason', 'survivors_after_stop')}\n"
            "print(json.dumps(out), flush=True)\n") % (
            php_parts(12, 11, True), os.path.join(TEST_DIR, "gc6_%s.quarantine.json" % solver), solver,
            os.path.join(TEST_DIR, "gc6_" + solver))
        case = external_sigterm_case("gc6_outer_" + solver, code6, 3.0)
        final = case.get("final") or {}
        result = final.get("result") or {}
        owned = (final.get("guard") or {}).get("owned_children", [])
        case["ok"] = (str(final.get("trip", "")).startswith("external SIGTERM")
                      and str(result.get("safety_stop_reason", "")).startswith("stage guard: external SIGTERM")
                      and result.get("transport_verified") is False and result.get("survivors_after_stop") == []
                      and len(owned) == 2 and not any(alive(c["pid"]) for c in owned))
        res["GC6_external_sigterm_pipeline_" + solver] = case
    return res


def external_sigterm_case(name, code, delay):
    g = guard(name, 240, name + ".quarantine.json")
    out = {}
    try:
        with g:
            child = g.popen(["/usr/bin/python3", "-I", "-B", "-c", code], stdout=sg.subprocess.PIPE,
                            stderr=sg.subprocess.PIPE)
            first = child.stdout.readline()
            out["ready"] = json.loads(first) if first else None
            time.sleep(delay)
            os.kill(child.pid, signal.SIGTERM)
            rest, err = child.communicate()
            lines = [line for line in rest.splitlines() if line.strip()]
            out["final"] = json.loads(lines[-1]) if lines else None
            out["child_returncode"] = child.returncode
            out["stderr_tail"] = err[-400:].decode("utf-8", "backslashreplace")
    except sg.StageTrip as exc:
        out["outer_trip"] = str(exc)
    out["outer_guard"] = g.record()
    return out


def transport_case(name, solver, solver_parts, checker_parts):
    prefix = os.path.join(TEST_DIR, "%s_%s" % (solver, name))
    g = guard("transport_%s_%s" % (solver, name), 300, "transport_%s_%s.quarantine.json" % (solver, name))
    result = None
    try:
        with g:
            result = drv.stream_pipeline(solver_parts, checker_parts, solver, prefix, 60, 60, 120, g)
    except sg.StageTrip as exc:
        result = dict(result or {}, outer_trip=str(exc))
    result["expected_solver_feed_sha256"] = drv.digest(solver_parts)
    result["expected_checker_feed_sha256"] = drv.digest(checker_parts)
    result["feeds_equal_expected"] = (
        result.get("feeds", {}).get("solver", {}).get("sha256") == result["expected_solver_feed_sha256"]
        and result.get("feeds", {}).get("checker", {}).get("sha256") == result["expected_checker_feed_sha256"]
        and result["feeds"]["solver"].get("bytes_written") == sum(len(p) for p in solver_parts)
        and result["feeds"]["checker"].get("bytes_written") == sum(len(p) for p in checker_parts))
    result["guard"] = g.record()
    return result


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


def main():
    if os.path.exists(OUT):
        raise FileExistsError(OUT)
    if os.path.exists(drv.QUARANTINE):
        raise SystemExit("quarantine record %s exists; not started" % drv.QUARANTINE)
    sg.install_process_handlers()
    t0 = time.monotonic()
    st = os.statvfs(LANE)
    available = st.f_bavail * st.f_frsize
    gate = {"at": now(), "available_bytes": available, "threshold_bytes": GATE, "projected_growth_bytes": GROWTH}
    me, driver_sha = sha(os.path.abspath(__file__)), sha(os.path.abspath(drv.__file__))
    generator_sha = sha(os.path.join(HERE, "k3_cuts_r3.py"))
    guard_sha = sha(os.path.join(HERE, "stage_guard_r1.py"))
    amendment_sha, delta_sha = sha(drv.AMENDMENT), sha(drv.DELTA)
    rec = {"started_at": now(), "gate": gate, "controls_sha256": me, "driver_sha256": driver_sha,
           "generator_sha256": generator_sha, "stage_guard_sha256": guard_sha, "amendment_sha256": amendment_sha,
           "delta_sha256": delta_sha, "environment": drv.environment()}
    failures = []
    if available < GATE + GROWTH:
        gate["status"] = "UNKNOWN / DEFERRED_RESOURCE; controls not run"
        rec["status"] = "DEFERRED"
    else:
        gate["status"] = "PASS"
        try:
            run_controls(rec, failures, me, driver_sha, generator_sha, guard_sha, amendment_sha)
            rec["status"] = "PASS" if not failures else "FAIL"
        except sg.StageTrip as exc:
            rec["status"] = "UNKNOWN"
            failures.append("stage trip: %s" % (exc,))
        except Exception as exc:
            rec["status"] = "FAIL"
            failures.append("exception: %r" % (exc,))
    rec.update({"failures": failures, "finished_at": now(), "seconds": round(time.monotonic() - t0, 3),
                "production_quarantine_exists": os.path.exists(drv.QUARANTINE)})
    with open(OUT, "x") as f:
        json.dump(rec, f, indent=2)
        f.write("\n")
    print(json.dumps({"status": rec["status"], "failures": failures, "seconds": rec["seconds"],
                      "strengthened": {k: v["strengthened_sha256"] for k, v in rec.get("routes", {}).items()}}))
    print("receipt_sha256", sha(OUT))


def run_controls(rec, failures, me, driver_sha, generator_sha, guard_sha, amendment_sha):
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
                "r3_names_generator": generator_sha in text, "r3_names_stage_guard": guard_sha in text,
                "delta_pins_r3": delta["amendment"]["sha256"] == amendment_sha,
                "delta_pins_driver": delta["driver"]["sha256"] == driver_sha,
                "delta_pins_controls": delta["controls"]["sha256"] == me,
                "delta_pins_generator": delta["generator"]["sha256"] == generator_sha,
                "delta_pins_stage_guard": delta["stage_guard"]["sha256"] == guard_sha,
                "generator_receipt_pass_bound_to_r3": generator.get("status") == "PASS"
                and generator["amendment"]["sha256"] == amendment_sha and generator["generator_sha256"] == generator_sha,
                "oracle_pass_with_pins": True, "B_C311_metadata_bound_to_oracle": True}
    rec["bindings"] = bindings
    if not all(bindings.values()):
        failures.append("binding check failed")

    # 2. parser
    rec["parser_controls"] = parser_controls()
    if not all(v["ok"] for v in rec["parser_controls"].values()):
        failures.append("parser control failed")

    # 3. creation-only directory
    drv.make_route_dir(TEST_DIR)
    try:
        drv.make_route_dir(TEST_DIR)
        rec["creation_only_directory"] = {"second_mkdir_raised": False}
    except FileExistsError:
        rec["creation_only_directory"] = {"second_mkdir_raised": True}
    if not rec["creation_only_directory"]["second_mkdir_raised"]:
        failures.append("creation-only directory control failed")

    # 4. pre-solve appender checks and negative controls
    routes, prepared, guards = {}, {}, {}
    for name in ("A", "B"):
        g = guard("prepare_" + name, 900, "prepare_%s.quarantine.json" % name)
        with g:
            prepared[name] = drv.prepare(name, oracle, g)
        routes[name] = prepared[name]["summary"]
        guards[name] = g.record()
    rec["routes"] = routes
    rec["prepare_guards"] = guards
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

    # 5. guard controls
    rec["guard_controls"] = guard_controls()
    if not all(v.get("ok") for v in rec["guard_controls"].values()):
        failures.append("guard control failed")

    # 6. transport controls
    transport = {}
    unsat, sat = php_parts(5, 4, True), php_parts(5, 4, False)
    pins = {"cadical": drv.ROUTES["A"]["solver_sha256"], "kissat": drv.ROUTES["B"]["solver_sha256"]}
    for solver in ("cadical", "kissat"):
        c1 = transport_case("unsat_with_block", solver, unsat, unsat)
        c2 = transport_case("sat_without_block", solver, sat, sat)
        c3 = transport_case("checker_fed_without_block", solver, unsat, sat)
        verdicts = {
            "unsat_with_block_verified": c1.get("transport_verified") is True and c1["feeds_equal_expected"]
            and c1["checker_status_lines"] == ["s VERIFIED"] and c1["solver_status_lines"] == ["s UNSATISFIABLE"],
            "sat_without_block_rejected": c2.get("solver_rc") == 10 and c2.get("transport_verified") is False
            and c2["feeds_equal_expected"],
            "checker_mismatch_rejected": c3.get("transport_verified") is False and c3["feeds_equal_expected"]
            and c3["feeds"]["checker"]["sha256"] != c3["feeds"]["solver"]["sha256"],
            "solver_binary_pinned": c1.get("solver_binary_sha256") == pins[solver],
            "checker_binary_pinned": c1.get("checker_binary_sha256") == drv.CHECKER_SHA,
            "no_survivors": not any(c.get("survivors_after_stop") for c in (c1, c2, c3))}
        transport[solver] = {"cases": {"unsat_with_block": c1, "sat_without_block": c2, "checker_fed_without_block": c3},
                             "verdicts": verdicts}
        if not all(verdicts.values()):
            failures.append("transport control failed for %s" % solver)
    rec["transport_controls"] = transport


if __name__ == "__main__":
    main()
