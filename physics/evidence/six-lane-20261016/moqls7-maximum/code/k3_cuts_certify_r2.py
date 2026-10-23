#!/usr/bin/env python3
"""k3_cuts_certify_r2.py: AMENDMENT-4.r3 appender and certification driver for C311 + transported cuts, r2.

New version of k3_cuts_certify_r1.py (0e978302...0b5a, preserved, never run). It answers the parent source review of
2026-10-18 (message 15aae4593f5e6f0b):
  1. Status lines are parsed from bytes: read the log as bytes, remove only b"\r", split on b"\n", and keep the lines
     that start with b"s ". There is no whitespace stripping. A certificate needs the checker status lines to be
     exactly [b"s VERIFIED"] and the solver status lines exactly [b"s UNSATISFIABLE"]; both are recorded.
  2. Preparation (in-process A build, B encoder child, appending) and the native pipeline each run inside a
     stage_guard_r1.StageGuard covering the driver and all its descendants: aggregate RSS <= 3.5 GiB, the 12e9 floor
     and a stage wall cap from the delta, with a fail-closed sampler. A trip stops the stage by SIGTERM with a
     bounded wait and gives UNKNOWN. There is no subprocess timeout and no SIGKILL. The pipeline also keeps the
     reviewed proof_stream.watch (checkpoints, keepalive writer, its own guards).
  3. SIGTERM handlers are installed for the whole run. External SIGTERM stops the active stage's descendants and gives
     UNKNOWN. Survivors after the 30 s grace are quarantined in evidence/k3cubes/C311cuts.QUARANTINE.json. While that
     record exists, admission is refused; code never removes it.
  4. Each route has one deliberately created directory evidence/k3cubes/C311cuts_<route>_r2 (os.mkdir; an existing
     directory means an attempt exists and nothing runs). All outputs are exclusive-create.
Routes (A+B standard), regeneration, appending, block, headers, B oracle binding and FIFO streaming are as in r1:
  A  lex C311 059be616...8c4f = A base d0d884f9... + C311 cube (7fca33f1...) + k3_lex make method; CaDiCaL 3.0.1.
  B  original B_C311 b3ec0108...c077 = B base 42a5f304... (oracle base) + C311 cube; kissat 4.0.4; B_C311 metadata
     bfa298ee...a056 bound to the oracle's base, wrapper and encoder pins.
The block (238140 clauses, 05f31da4...e6dd) is re-emitted by k3_cuts_r1.emit. Headers 107513/659168 -> 107513/897308
and 461370/1629802 -> 461370/1867942. The input bytes must equal the named file. The strengthened bytes go from
memory into two FIFOs (solver, checker) with per-feed SHA and byte counts. Binary DRAT goes solver -> FIFO ->
drat-trim stdin. No CNF or proof file is written.
Usage: /usr/bin/python3 -I -B k3_cuts_certify_r2.py A|B
"""
import errno
import fcntl
import hashlib
import json
import os
import shutil
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import gram_enc  # noqa: E402
import k3_cubes  # noqa: E402
import k3_cuts_r1  # noqa: E402
import k3_lex  # noqa: E402
import stage_guard_r1 as sg  # noqa: E402
from gram_certify_r4 import CHECKER, now, rss, sha  # noqa: E402
from proof_stream import watch  # noqa: E402

LANE = os.path.dirname(HERE)
K3DIR = os.path.join(LANE, "evidence", "k3cubes")
QUARANTINE = os.path.join(K3DIR, "C311cuts.QUARANTINE.json")
AMENDMENT = os.path.join(LANE, "review", "AMENDMENT-4.r3.md")
DELTA = os.path.join(LANE, "review", "K3-CUTS-CERT-DELTA.r2.json")
GENERATOR_RECEIPT = os.path.join(K3DIR, "cuts_r3_receipt.json")
CONTROLS_RECEIPT = os.path.join(K3DIR, "cuts_cert_controls_r2.json")
ORACLE_RECEIPT = os.path.join(K3DIR, "bmap_oracle_r1.json")
ORACLE_RECEIPT_SHA = "6e2bd95ee38c615ab2a1a6282531da730b2bf0cc45e104e95b850102e0b1952c"
ORACLE_SHA = "13f4a5e6c34b61478fcdbb5fddc1a934901c1b82480553cfee8b0f958f73cd8e"
CODE_PINS = {
    "gram_enc.py": "b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833",
    "gram_encB.py": "c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45",
    "k3_cubes.py": "70c79c624dd4c4ad0929a41790b7674eaa7343f3fcb5802c5e0c1abdbfb30550",
    "k3_lex.py": "2b721e85812cd7b3438771868f63da1e10f3fbeed6551f7888f74a399e159b10",
    "k3_cuts_r1.py": "0ec92c861024a728aa38d238fda2d7f5f056fae12cb0f474a15db0335b6e1b0a",
    "proof_stream.py": "aa0d5a0bf2fa144a9ec2b7be9b4c7f5de15e8c8a07008780e3966552a56d05de",
    "gram_certify_r4.py": "ec540a8700b7933b71605e7b03f86d5ef52ad258a5895d0b558db9819f0fa18a",
    "stage_guard_r1.py": "2d945ed0274445ced50a99f6ed309734073aff92da79e2e3e3fe43ecdeae0fba",
}
BLOCK_SHA = "05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd"
BLOCK_CLAUSES = 238140
NG = 2646
CHECKER_SHA = "111b0405566d55629f5d391b80b3220cc7a3ebc3cd406a35895ff65cc9acd5e4"
CHECKER_SOURCE_SHA = "d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee"
GATE, GROWTH, FLOOR = 12200000000, 10485760, 12000000000
RSS_CAP = 3584 * 1024 * 1024
SOLVER_MAX, CHECKER_MAX, WALL_MAX = 3600, 7200, 10740
STAGE_MARGIN = 180
CHUNK = 1 << 20
ROUTES = {
    "A": {"instance": "lex C311 (AMENDMENT-3) + AMENDMENT-4 cuts, encoder A",
          "input": "explore/k3lex/A_C311.cnf",
          "input_sha256": "059be6164176ee93c94d93bd47fa1d365477b6c94f3aa867df991f677e1a8c4f",
          "input_meta": "explore/k3lex/A_C311.meta.json",
          "input_meta_sha256": "7bef0b78007151d94661181244fa8614c114705522b58fc16cf287014bde190d",
          "source_cube_sha256": "7fca33f1e6324cbe17bc44bbea7f8d9188bcac187252d766fb0fa5e39e1c2001",
          "source_meta": "explore/k3cubes/A_C311.meta.json",
          "source_meta_sha256": "3b2ab04f2b42b799169bdccf3d868f544ba571ff1d72e18d0cf68187a0f4d9ed",
          "base_sha256": "d0d884f9a0f9715b256da68be97408ae4a55c88d76183c02246a570f115a4388",
          "input_header": (107513, 659168), "strengthened_header": (107513, 897308),
          "solver": "cadical", "solver_sha256": "601c9fa8ba5d09fd81bb00c89b3e54832f138bccc3422bd8652e8cda4d74d1fa"},
    "B": {"instance": "original B_C311 + AMENDMENT-4 cuts, encoder B",
          "input": "explore/k3cubes/B_C311.cnf",
          "input_sha256": "b3ec010855ad4abd75ffd6eb57aaa3ff158bc8447625ee2097f5a6057594c077",
          "input_meta": "explore/k3cubes/B_C311.meta.json",
          "input_meta_sha256": "bfa298eea4a6b102a16e15663d42c2cdf86ab7ab093f86bdecb7d8bf8d28a056",
          "base_sha256": "42a5f30453bba3eb423e78b99b1a8fe6039e1c91c32b6ff1dd72f498fa8e0aac",
          "input_header": (461370, 1629802), "strengthened_header": (461370, 1867942),
          "solver": "kissat", "solver_sha256": "05d6f3e9c402a1fe8853b0746e384e1b3d1c4a550e255f11daa2461d279aa848"},
}


def lane_path(rel):
    return os.path.join(LANE, rel)


def dimacs_line(clause):
    return (" ".join(map(str, clause)) + " 0\n").encode()


def dimacs_header(nv, nc):
    return ("p cnf %d %d\n" % (nv, nc)).encode()


def digest(parts):
    h = hashlib.sha256()
    for part in parts:
        h.update(part)
    return h.hexdigest()


def status_lines(data):
    """Bytes in; remove only b"\\r", split on b"\\n", keep lines starting with b"s "; no stripping."""
    return [line for line in data.replace(b"\r", b"").split(b"\n") if line.startswith(b"s ")]


def log_status_lines(path):
    with open(path, "rb") as f:
        return status_lines(f.read())


def shown(lines):
    return [line.decode("ascii", "backslashreplace") for line in lines]


def make_route_dir(path):
    os.mkdir(path)
    return path


def environment():
    modules = {}
    for name in ("gram_enc", "k3_cubes", "k3_cuts_r1", "k3_lex", "gram_certify_r4", "proof_stream", "stage_guard_r1"):
        path = os.path.abspath(sys.modules[name].__file__)
        modules[name] = {"path": path, "sha256": sha(path)}
    return {"executable": sys.executable, "version": sys.version, "isolated": bool(sys.flags.isolated),
            "dont_write_bytecode": bool(sys.dont_write_bytecode), "modules": modules,
            "driver": {"path": os.path.abspath(__file__), "sha256": sha(os.path.abspath(__file__))}}


def check_code_pins():
    bad = [name for name, pin in CODE_PINS.items() if sha(os.path.join(HERE, name)) != pin]
    if bad:
        raise AssertionError("lane code differs from the pins: %s" % bad)


def check_oracle(oracle, receipt_sha):
    ok = (receipt_sha == ORACLE_RECEIPT_SHA and oracle.get("status") == "PASS"
          and oracle.get("oracle_sha256") == ORACLE_SHA and oracle.get("decoded_identity_mismatches") == 0
          and oracle.get("A_map_equals_wrapper_map") is True and oracle.get("failures") == []
          and oracle.get("encoder_A_sha256") == CODE_PINS["gram_enc.py"]
          and oracle.get("encoder_B_sha256") == CODE_PINS["gram_encB.py"]
          and oracle.get("cube_wrapper_sha256") == CODE_PINS["k3_cubes.py"]
          and oracle.get("production_arguments") == ["--squares", "3", "--heavy", "--sym"]
          and oracle.get("B_base", {}).get("sha256") == ROUTES["B"]["base_sha256"])
    if not ok:
        raise AssertionError("B-map oracle receipt is not PASS with the pinned fields")


def check_b_c311_binding(meta, meta_sha, oracle):
    route = ROUTES["B"]
    ok = (meta_sha == route["input_meta_sha256"] and meta.get("encoder") == "B" and meta.get("cube") == "C311"
          and meta.get("cnf_sha256") == route["input_sha256"]
          and meta.get("base_cnf_sha256") == oracle["B_base"]["sha256"]
          and meta.get("wrapper_sha256") == oracle["cube_wrapper_sha256"]
          and meta.get("base_encoder_sha256") == oracle["encoder_B_sha256"])
    if not ok:
        raise AssertionError("B_C311 metadata is not bound to the oracle base, wrapper and encoder pins")


def check_header(parts, expected):
    first = parts[0]
    fields = first.decode().split()
    if len(fields) != 4 or first.count(b"\n") != 1 or not first.endswith(b"\n") \
            or (fields[0], fields[1], int(fields[2]), int(fields[3])) != ("p", "cnf") + tuple(expected):
        raise AssertionError("header %r differs from %r" % (first, expected))


def check_body(body, clauses):
    if body.count(b"\n") != clauses or not body.endswith(b" 0\n") or body.startswith(b"0\n") \
            or b"\n0\n" in body or b"None" in body:
        raise AssertionError("body is not exactly %d nonempty DIMACS clause lines" % clauses)


def check_block(block, clauses):
    if len(clauses) != BLOCK_CLAUSES or hashlib.sha256(block).hexdigest() != BLOCK_SHA:
        raise AssertionError("cut block differs from the frozen block")
    if any(lit >= 0 or lit < -NG for clause in clauses for lit in clause):
        raise AssertionError("cut block literal outside the negative g range")


def check_input(parts, pin):
    if digest(parts) != pin:
        raise AssertionError("regenerated input SHA differs from the pin")


def check_prefix_against_file(path, parts):
    """The regenerated input equals the named input file byte for byte (prefix equality of the strengthened body)."""
    with open(path, "rb") as f:
        for part in parts:
            view, offset = memoryview(part), 0
            while offset < len(view):
                chunk = f.read(min(1 << 22, len(view) - offset))
                if not chunk or view[offset:offset + len(chunk)] != chunk:
                    raise AssertionError("regenerated input differs from %s" % path)
                offset += len(chunk)
        if f.read(1):
            raise AssertionError("named input %s is longer than the regenerated input" % path)


def regenerate_a(route):
    with open(lane_path(route["source_meta"])) as f:
        source_meta = json.load(f)
    with open(lane_path(route["input_meta"])) as f:
        input_meta = json.load(f)
    ok = (sha(lane_path(route["source_meta"])) == route["source_meta_sha256"]
          and sha(lane_path(route["input_meta"])) == route["input_meta_sha256"]
          and source_meta["cnf_sha256"] == route["source_cube_sha256"]
          and source_meta["base_cnf_sha256"] == route["base_sha256"]
          and source_meta["base_encoder_sha256"] == CODE_PINS["gram_enc.py"]
          and source_meta["wrapper_sha256"] == CODE_PINS["k3_cubes.py"]
          and input_meta["source_cube_cnf_sha256"] == route["source_cube_sha256"]
          and input_meta["cnf_sha256"] == route["input_sha256"]
          and input_meta["wrapper_sha256"] == CODE_PINS["k3_lex.py"]
          and input_meta["cube_wrapper_sha256"] == CODE_PINS["k3_cubes.py"]
          and input_meta["finite_controls_status"] == "PASS")
    if not ok:
        raise AssertionError("A lex/source metadata differ from the pins")
    vmap = k3_cubes.variable_map()
    F, actual_map = gram_enc.build(3, None, True, True, None)
    expected_map = {"%d|%d,%d|%d,%d" % (a, p[0], p[1], q[0], q[1]): v for (a, p, q), v in vmap.items()}
    if actual_map != expected_map:
        raise AssertionError("encoder A map differs from the cube wrapper map")
    nv, nbase = F.nv, len(F.cl)
    base_body = b"".join(dimacs_line(cl) for cl in F.cl)
    del F, actual_map
    if digest([dimacs_header(nv, nbase), base_body]) != route["base_sha256"]:
        raise AssertionError("regenerated A base differs from its metadata hash")
    cube, _, _ = k3_cubes.cube_clauses(vmap, "C311")
    cube_body = b"".join(dimacs_line(cl) for cl in cube)
    if digest([dimacs_header(nv, nbase + len(cube)), base_body, cube_body]) != route["source_cube_sha256"]:
        raise AssertionError("regenerated A original C311 differs from its pin")
    lex_nv, lex = nv, []
    for gen in k3_lex.generators("C311"):
        perm = k3_lex.image(vmap, gen)
        lex_nv, clauses = k3_lex.lex_clauses(sorted(perm.items()), lex_nv)
        lex.extend(clauses)
    if len(lex) != input_meta["extra_clauses"] or lex_nv - nv != input_meta["new_auxiliaries"]:
        raise AssertionError("regenerated lex clauses differ from the lex metadata counts")
    body = b"".join([base_body, cube_body, b"".join(dimacs_line(cl) for cl in lex)])
    del base_body, cube_body
    nc = nbase + len(cube) + len(lex)
    return (lex_nv, nc), body, {"base_sha256": route["base_sha256"], "source_cube_sha256": route["source_cube_sha256"],
                                "base_header": [nv, nbase], "cube_clauses": len(cube), "lex_clauses": len(lex),
                                "lex_auxiliaries": lex_nv - nv, "method": "gram_enc.build + k3_cubes C311 + k3_lex make"}


def b_base_output(guard):
    command = ["/usr/bin/python3", "-B", os.path.join(HERE, "gram_encB.py"),
               "--squares", "3", "--heavy", "--sym", "--out", "/dev/stdout"]
    out = guard.run(command)
    first_end = out.index(b"\n") + 1
    fields = out[:first_end].decode().split()
    stats_start = out.rindex(b"\n", 0, len(out) - 1) + 1
    if len(fields) != 4 or fields[:2] != ["p", "cnf"] or not out[stats_start:].startswith(b"vars ") \
            or out.count(b"\n", first_end, stats_start) != int(fields[3]):
        raise AssertionError("encoder B output is not header + exactly nc clause lines + stats line")
    return int(fields[2]), int(fields[3]), out[first_end:stats_start]


def regenerate_b(route, oracle, guard):
    meta_path = lane_path(route["input_meta"])
    with open(meta_path) as f:
        meta = json.load(f)
    check_b_c311_binding(meta, sha(meta_path), oracle)
    nv, nbase, base_body = b_base_output(guard)
    base_sha = digest([dimacs_header(nv, nbase), base_body])
    if base_sha != route["base_sha256"] or base_sha != oracle["B_base"]["sha256"] \
            or [nv, nbase] != [oracle["B_base"]["variables"], oracle["B_base"]["clauses"]]:
        raise AssertionError("regenerated B base differs from the oracle base")
    cube, _, _ = k3_cubes.cube_clauses(k3_cubes.variable_map(), "C311")
    body = base_body + b"".join(dimacs_line(cl) for cl in cube)
    del base_body
    return (nv, nbase + len(cube)), body, {"base_sha256": base_sha, "base_header": [nv, nbase],
                                           "cube_clauses": len(cube), "B_C311_metadata_sha256": sha(meta_path),
                                           "B_C311_bound_to_oracle_base_wrapper_encoder": True,
                                           "method": "gram_encB.py stdout (k3_cube_certify_r3 method) + k3_cubes C311"}


def prepare(route_name, oracle, guard):
    """Regenerate the named input in memory, append the re-emitted block, and assert every pre-solve binding.
    Must run inside `guard` (a StageGuard): the A build is in-process and the B encoder is a guarded child."""
    route = ROUTES[route_name]
    if route_name == "A":
        (nv, nc), body, regen = regenerate_a(route)
    else:
        (nv, nc), body, regen = regenerate_b(route, oracle, guard)
    input_parts = [dimacs_header(nv, nc), body]
    check_header(input_parts, route["input_header"])
    check_body(body, nc)
    check_input(input_parts, route["input_sha256"])
    check_prefix_against_file(lane_path(route["input"]), input_parts)
    clauses = k3_cuts_r1.emit(k3_cubes.variable_map())
    block = b"".join(dimacs_line(c) for c in clauses)
    check_block(block, clauses)
    del clauses
    parts = [dimacs_header(nv, nc + BLOCK_CLAUSES), body, block]
    check_header(parts, route["strengthened_header"])
    check_body(block, BLOCK_CLAUSES)
    strengthened_sha = digest(parts)
    return {"parts": parts, "sha256": strengthened_sha, "bytes": sum(len(p) for p in parts),
            "summary": {"instance": route["instance"], "input": route["input"], "input_sha256": route["input_sha256"],
                        "input_header": list(route["input_header"]), "strengthened_header": [nv, nc + BLOCK_CLAUSES],
                        "block_sha256": BLOCK_SHA, "block_clauses": BLOCK_CLAUSES, "block_bytes": len(block),
                        "input_prefix_equal_to_named_file": True, "strengthened_sha256": strengthened_sha,
                        "strengthened_bytes": sum(len(p) for p in parts), "regeneration": regen,
                        "block_map": "k3_cubes.variable_map(); equal to encoder B's map by the PASS oracle"}}


def feed(path, parts, record, stop):
    """Write parts into a FIFO once a reader has opened it, hashing exactly the bytes written."""
    h, written, fd = hashlib.sha256(), 0, None
    try:
        while fd is None:
            try:
                fd = os.open(path, os.O_WRONLY | os.O_NONBLOCK)
            except OSError as exc:
                if exc.errno != errno.ENXIO:
                    raise
                if stop.is_set():
                    record["error"] = "no reader opened the FIFO"
                    return
                time.sleep(0.05)
        os.set_blocking(fd, True)
        for part in parts:
            view, offset = memoryview(part), 0
            while offset < len(view):
                n = os.write(fd, view[offset:offset + CHUNK])
                h.update(view[offset:offset + n])
                offset += n
                written += n
    except OSError as exc:
        record["error"] = repr(exc)
    finally:
        if fd is not None:
            os.close(fd)
        record.update({"bytes_written": written, "sha256": h.hexdigest()})


def solver_arguments(solver, seconds, cnf, proof):
    if solver == "cadical":
        return ["-q", "-t", str(seconds), cnf, proof]
    if solver == "kissat":
        return ["-q", "-f", "--time=%d" % seconds, cnf, proof]
    raise ValueError(solver)


def stream_pipeline(solver_parts, checker_parts, solver, prefix, solver_seconds, checker_seconds, wall_seconds, guard):
    """Inside `guard`: solver and drat-trim read the CNF from two FIFOs fed from memory; binary DRAT flows solver ->
    FIFO -> drat-trim stdin; proof_stream.watch adds checkpoints, the keepalive writer and its own guards."""
    if not (1 <= solver_seconds <= SOLVER_MAX and 1 <= checker_seconds <= CHECKER_MAX
            and max(solver_seconds, checker_seconds) < wall_seconds <= WALL_MAX):
        raise ValueError("caps outside the declared bounds")
    st = os.statvfs(LANE)
    if st.f_bavail * st.f_frsize < FLOOR or not rss(os.getpid()):
        raise RuntimeError("Free-space floor or native RSS prerequisite failed")
    paths = {key: prefix + suffix for key, suffix in (
        ("solver_log", ".solver.log"), ("checker_log", ".checker.log"), ("checkpoints", ".checkpoints.jsonl"),
        ("proof_fifo", ".drat.fifo"), ("solver_cnf_fifo", ".solver-cnf.fifo"), ("checker_cnf_fifo", ".checker-cnf.fifo"))}
    if any(os.path.exists(path) for path in paths.values()):
        raise FileExistsError(prefix)
    binary = shutil.which(solver)
    if not binary:
        raise FileNotFoundError(solver)
    binary = os.path.realpath(binary)
    solver_sha = sha(binary)
    for key in ("proof_fifo", "solver_cnf_fifo", "checker_cnf_fifo"):
        os.mkfifo(paths[key])
    read_fd = os.open(paths["proof_fifo"], os.O_RDONLY | os.O_NONBLOCK)
    keep_writer = [os.open(paths["proof_fifo"], os.O_WRONLY | os.O_NONBLOCK)]
    os.set_blocking(read_fd, True)
    stop, feeds, started = threading.Event(), {"solver": {}, "checker": {}}, []
    threads = {"checker": threading.Thread(target=feed, args=(paths["checker_cnf_fifo"], checker_parts, feeds["checker"], stop), daemon=True),
               "solver": threading.Thread(target=feed, args=(paths["solver_cnf_fifo"], solver_parts, feeds["solver"], stop), daemon=True)}
    command = [binary] + solver_arguments(solver, solver_seconds, paths["solver_cnf_fifo"], paths["proof_fifo"])
    checker_command = [CHECKER, paths["checker_cnf_fifo"], "-i", "-t", str(checker_seconds)]
    start, t0 = now(), time.monotonic()
    solve = check = None
    peak, reason, survivors = 0, None, []
    try:
        with open(paths["solver_log"], "x") as sl, open(paths["checker_log"], "x") as cl, open(paths["checkpoints"], "x") as cp:
            threads["checker"].start()
            started.append(threads["checker"])
            check = guard.popen(checker_command, stdin=read_fd, stdout=cl, stderr=subprocess.STDOUT)
            threads["solver"].start()
            started.append(threads["solver"])
            solve = guard.popen(command, stdout=sl, stderr=subprocess.STDOUT)
            try:
                peak, reason = watch(solve, check, wall_seconds, cp, keep_writer)
            except sg.StageTrip as exc:
                reason = "stage guard: %s" % (exc,)
            except RuntimeError as exc:
                reason = "proof_stream stop: %s" % (exc,)
    finally:
        for fd in [read_fd] + keep_writer:
            os.close(fd)
        stop.set()
        survivors = guard.stop_all()
        for thread in started:
            thread.join(60)
    checker_status = log_status_lines(paths["checker_log"])
    solver_status = log_status_lines(paths["solver_log"])
    solver_rc = solve.returncode if solve is not None else None
    checker_rc = check.returncode if check is not None else None
    transport_ok = (reason is None and not survivors and solver_rc == 20 and checker_rc == 0
                    and checker_status == [b"s VERIFIED"] and solver_status == [b"s UNSATISFIABLE"])
    return {"started_at": start, "finished_at": now(), "seconds": round(time.monotonic() - t0, 3),
            "solver_command": command, "checker_command": checker_command,
            "solver_rc": solver_rc, "checker_rc": checker_rc,
            "checker_status_lines": shown(checker_status), "solver_status_lines": shown(solver_status),
            "status_parse_rule": "bytes; remove only b'\\r'; split b'\\n'; lines starting b's '; no stripping",
            "transport_verified": transport_ok, "peak_sampled_aggregate_rss_bytes": max(peak, guard.peak),
            "safety_stop_reason": reason, "survivors_after_stop": survivors,
            "feeds": feeds, "feed_threads_alive_after_join": [t.name for t in started if t.is_alive()],
            "solver_binary": binary, "solver_binary_sha256": solver_sha,
            "checker_binary_sha256": sha(CHECKER), "checker_source_sha256": sha(CHECKER + ".c"),
            "solver_log_sha256": sha(paths["solver_log"]), "checker_log_sha256": sha(paths["checker_log"]),
            "checkpoint_log_sha256": sha(paths["checkpoints"]),
            "native_limits_seconds": {"solver": solver_seconds, "checker": checker_seconds},
            "wall_guard_seconds": wall_seconds,
            "transport": "CNF bytes fed from memory into two FIFOs (solver, checker) with per-feed SHA; binary DRAT "
                         "solver -> FIFO -> drat-trim stdin -i; nonblocking FIFO startup; keepalive writer",
            "storage": "no CNF or proof file; logs, checkpoints and one receipt only"}


def gate(prefix, phase):
    st = os.statvfs(LANE)
    available = st.f_bavail * st.f_frsize
    record = {"at": now(), "phase": phase, "available_bytes": available,
              "launch_threshold_bytes": GATE, "projected_retained_growth_bytes": GROWTH}
    record["status"] = "PASS" if available >= GATE + GROWTH else "UNKNOWN / DEFERRED_RESOURCE; no native stage launched"
    return record


def preflight(route_name):
    """Frozen amendment, delta, generator r3 and controls r2 receipts, oracle and binary pins, mutually bound."""
    route = ROUTES[route_name]
    check_code_pins()
    driver_sha, amendment_sha, delta_sha = sha(os.path.abspath(__file__)), sha(AMENDMENT), sha(DELTA)
    with open(DELTA) as f:
        delta = json.load(f)
    with open(GENERATOR_RECEIPT) as f:
        generator = json.load(f)
    with open(CONTROLS_RECEIPT) as f:
        controls = json.load(f)
    with open(ORACLE_RECEIPT) as f:
        oracle = json.load(f)
    check_oracle(oracle, sha(ORACLE_RECEIPT))
    caps = delta["caps"]
    ok = (delta["driver"]["sha256"] == driver_sha and delta["amendment"]["sha256"] == amendment_sha
          and delta["routes"][route_name]["input_sha256"] == route["input_sha256"]
          and generator.get("status") == "PASS" and generator["amendment"]["sha256"] == amendment_sha
          and generator["generator_sha256"] == delta["generator"]["sha256"]
          and generator["block_sha256_A"] == BLOCK_SHA
          and controls.get("status") == "PASS" and controls["driver_sha256"] == driver_sha
          and controls["amendment_sha256"] == amendment_sha and controls["delta_sha256"] == delta_sha
          and controls["controls_sha256"] == delta["controls"]["sha256"]
          and controls["routes"][route_name]["strengthened_sha256"] is not None
          and 1 <= caps["preparation_wall_seconds"] <= WALL_MAX
          and caps["wall_guard_seconds"] + STAGE_MARGIN <= WALL_MAX)
    if not ok:
        raise AssertionError("frozen amendment/delta/generator/controls bindings are inconsistent")
    binary = os.path.realpath(shutil.which(route["solver"]) or "")
    if not (os.path.isfile(binary) and sha(binary) == route["solver_sha256"] and sha(CHECKER) == CHECKER_SHA
            and sha(CHECKER + ".c") == CHECKER_SOURCE_SHA):
        raise AssertionError("solver or checker binary differs from its pin")
    return oracle, caps, {"amendment_sha256": amendment_sha, "delta_sha256": delta_sha,
                          "generator_receipt_sha256": sha(GENERATOR_RECEIPT),
                          "controls_receipt_sha256": sha(CONTROLS_RECEIPT), "oracle_receipt_sha256": ORACLE_RECEIPT_SHA,
                          "expected_strengthened_sha256": controls["routes"][route_name]["strengthened_sha256"]}


def certify(route_name, route_dir, state):
    route = ROUTES[route_name]
    prefix = os.path.join(route_dir, "C311cuts_" + route_name)
    oracle, caps, bindings = preflight(route_name)
    state["bindings"] = bindings
    state["outer_gates"] = [gate(prefix, "before in-memory regeneration and appending")]
    if state["outer_gates"][-1]["status"] != "PASS":
        state["status"] = "UNKNOWN"
        state["stop"] = "gate before preparation"
        return
    guard = sg.StageGuard("preparation", caps["preparation_wall_seconds"], RSS_CAP, FLOOR, LANE, QUARANTINE)
    state["guards"] = [guard]
    with guard:
        prepared = prepare(route_name, oracle, guard)
    state["prepared"] = prepared["summary"]
    if prepared["sha256"] != bindings["expected_strengthened_sha256"]:
        raise AssertionError("strengthened SHA differs from the controls receipt")
    state["outer_gates"].append(gate(prefix, "before the native proof pipeline"))
    if state["outer_gates"][-1]["status"] != "PASS":
        state["status"] = "UNKNOWN"
        state["stop"] = "gate before pipeline"
        return
    pguard = sg.StageGuard("pipeline", caps["wall_guard_seconds"] + STAGE_MARGIN, RSS_CAP, FLOOR, LANE, QUARANTINE)
    state["guards"].append(pguard)
    result = None
    try:
        with pguard:
            result = stream_pipeline(prepared["parts"], prepared["parts"], route["solver"], prefix,
                                     caps["solver_seconds"], caps["checker_seconds"], caps["wall_guard_seconds"], pguard)
    except sg.StageTrip as exc:
        state["stop"] = "pipeline stage: %s" % (exc,)
    if result is None:
        state["status"] = "UNKNOWN"
        return
    feeds_ok = all(result["feeds"][k].get("sha256") == prepared["sha256"]
                   and result["feeds"][k].get("bytes_written") == prepared["bytes"]
                   and "error" not in result["feeds"][k] for k in ("solver", "checker"))
    verified = (result["transport_verified"] and feeds_ok and not result["feed_threads_alive_after_join"]
                and pguard.reason is None and not pguard.survivors
                and result["solver_binary_sha256"] == route["solver_sha256"]
                and result["checker_binary_sha256"] == CHECKER_SHA)
    state["result"] = result
    state["feeds_match_strengthened"] = feeds_ok
    state["verified_unsat"] = verified
    state["status"] = "VERIFIED_UNSAT_CASE" if verified else ("SAT_PATTERN_ONLY" if result["solver_rc"] == 10 else "UNKNOWN")


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ROUTES:
        raise SystemExit("usage: k3_cuts_certify_r2.py A|B")
    route_name = sys.argv[1]
    sg.install_process_handlers()
    lock = open(os.path.abspath(__file__), "rb")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        raise SystemExit("another C311+cuts pipeline holds the lock; not launched")
    if os.path.exists(QUARANTINE):
        raise SystemExit("quarantine record %s exists; admission refused" % QUARANTINE)
    route_dir = make_route_dir(os.path.join(K3DIR, "C311cuts_%s_r2" % route_name))
    receipt = os.path.join(route_dir, "C311cuts_%s.json" % route_name)
    state = {"route": route_name, "status": "UNKNOWN", "verified_unsat": False, "started_at": now()}
    try:
        certify(route_name, route_dir, state)
    except sg.StageTrip as exc:
        state["stop"] = "stage trip: %s" % (exc,)
    except Exception as exc:
        state["stop"] = "exception: %r" % (exc,)
    finally:
        guards = state.pop("guards", [])
        state.update({"finished_at": now(), "guards": [g.record() for g in guards],
                      "quarantined": os.path.exists(QUARANTINE), "planned_new_retained_bytes": GROWTH,
                      "environment": environment(), "driver_sha256": sha(os.path.abspath(__file__)),
                      "authority": "Parent AMENDMENT-4 disposition 3c9373c0...4e44 decisions 1-6; parent source "
                                   "review 15aae4593f5e6f0b; frozen AMENDMENT-4.r3 and K3-CUTS-CERT-DELTA.r2",
                      "scope": "One strengthened C311 input on one route; parent replay and composition review remain separate"})
        if state["status"] != "VERIFIED_UNSAT_CASE":
            state["verified_unsat"] = False
        with open(receipt, "x") as f:
            json.dump(state, f, indent=2)
            f.write("\n")
        print(json.dumps({k: state.get(k) for k in ("route", "status", "verified_unsat", "stop", "quarantined")}), flush=True)
        if state.get("result"):
            r = state["result"]
            print(json.dumps({"solver_rc": r["solver_rc"], "checker_rc": r["checker_rc"],
                              "checker_status_lines": r["checker_status_lines"],
                              "solver_status_lines": r["solver_status_lines"], "seconds": r["seconds"]}), flush=True)


if __name__ == "__main__":
    main()
