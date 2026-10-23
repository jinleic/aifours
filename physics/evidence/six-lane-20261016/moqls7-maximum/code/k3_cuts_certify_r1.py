#!/usr/bin/env python3
"""k3_cuts_certify_r1.py: AMENDMENT-4.r3 appender and certification driver for C311 + transported cuts.

Implements MAJOR-A of the parent AMENDMENT-4 disposition (3c9373c0...4e44). Routes, A+B standard (decision 1):
  A  lex C311 (AMENDMENT-3), 059be616...8c4f: encoder A base (gram_enc.build(3, None, True, True, None), d0d884f9...)
     + C311 cube clauses (k3_cubes; original C311 7fca33f1...2001) + lex clauses (k3_lex make method), regenerated in
     memory; then the cut block. Solver CaDiCaL 3.0.1: cadical -q -t S CNF PROOF.
  B  original B_C311, b3ec0108...c077: encoder B base (gram_encB.py --squares 3 --heavy --sym to stdout,
     42a5f304...0aac) + C311 cube clauses, regenerated in memory (k3_cube_certify_r3 method); then the cut block.
     B_C311 metadata (bfa298ee...a056) is bound to the B-map oracle receipt. Solver kissat 4.0.4: kissat -q -f --time=S.
Appending: the block is re-emitted by the reviewed emission k3_cuts_r1.emit on the wrapper map (equal to encoder B's
map by the oracle) and must have exactly 238140 clauses hashing to 05f31da4...e6dd. The strengthened bytes are
header' + input body + block, with header' = (nv, nc + 238140) asserted equal to A lex (107513, 897308) or B original
(461370, 1867942); the regenerated input must equal the named input file byte for byte (prefix equality).
Streaming: no CNF or proof file. The parent writes the in-memory strengthened bytes into two named FIFOs, one read by
the solver and one by drat-trim, hashing exactly the bytes written to each; the solver writes binary DRAT into a
third FIFO that drat-trim reads on stdin (proof_stream.py design: nonblocking open and a keepalive writer).
Guards: fresh gate >= 12.2e9 + 10 MiB before regeneration and again before the native pipeline; the continuous 12e9
floor, aggregate RSS <= 3.5 GiB (parent + solver + checker), cooperative wall guard, 15-minute checkpoints and
SIGTERM-only stops come from proof_stream.watch/stop_children (aa0d5a0b...05de). Caps and pins come from the frozen
delta. At most one C311+cuts pipeline at a time (advisory lock on this file).
Verified only if: solver rc 20, checker rc 0, checker status lines exactly ["s VERIFIED"], no safety stop, both
measured feeds equal the precomputed strengthened SHA and length, and solver/checker binaries equal their pins.
Usage: /usr/bin/python3 -I -B k3_cuts_certify_r1.py A|B
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
from gram_certify_r4 import CHECKER, now, rss, sha  # noqa: E402
from proof_stream import stop_children, watch  # noqa: E402

LANE = os.path.dirname(HERE)
OUTDIR = os.path.join(LANE, "evidence", "k3cubes", "cuts_cert_r1")
AMENDMENT = os.path.join(LANE, "review", "AMENDMENT-4.r3.md")
DELTA = os.path.join(LANE, "review", "K3-CUTS-CERT-DELTA.r1.json")
GENERATOR_RECEIPT = os.path.join(LANE, "evidence", "k3cubes", "cuts_r2_receipt.json")
CONTROLS_RECEIPT = os.path.join(LANE, "evidence", "k3cubes", "cuts_cert_controls_r1.json")
ORACLE_RECEIPT = os.path.join(LANE, "evidence", "k3cubes", "bmap_oracle_r1.json")
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
}
BLOCK_SHA = "05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd"
BLOCK_CLAUSES = 238140
NG = 2646
CHECKER_SHA = "111b0405566d55629f5d391b80b3220cc7a3ebc3cd406a35895ff65cc9acd5e4"
CHECKER_SOURCE_SHA = "d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee"
GATE, GROWTH, FLOOR = 12200000000, 10485760, 12000000000
SOLVER_MAX, CHECKER_MAX, WALL_MAX = 3600, 7200, 10740
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


def environment():
    modules = {}
    for name in ("gram_enc", "k3_cubes", "k3_cuts_r1", "k3_lex", "gram_certify_r4", "proof_stream"):
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
    tag, form, nv, nc = first.decode().split()
    if first.count(b"\n") != 1 or not first.endswith(b"\n") or (tag, form, int(nv), int(nc)) != ("p", "cnf") + tuple(expected):
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


def regenerate_b(route, oracle):
    meta_path = lane_path(route["input_meta"])
    with open(meta_path) as f:
        meta = json.load(f)
    check_b_c311_binding(meta, sha(meta_path), oracle)
    command = ["/usr/bin/python3", "-B", os.path.join(HERE, "gram_encB.py"),
               "--squares", "3", "--heavy", "--sym", "--out", "/dev/stdout"]
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = result.stdout
    del result
    first_end = out.index(b"\n") + 1
    tag, form, nv, nbase = out[:first_end].decode().split()
    nv, nbase = int(nv), int(nbase)
    stats_start = out.rindex(b"\n", 0, len(out) - 1) + 1
    if (tag, form) != ("p", "cnf") or not out[stats_start:].startswith(b"vars ") \
            or out.count(b"\n", first_end, stats_start) != nbase:
        raise AssertionError("encoder B output is not header + exactly nc clause lines + stats line")
    base_body = out[first_end:stats_start]
    del out
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


def prepare(route_name, oracle):
    """Regenerate the named input in memory, append the re-emitted block, and assert every pre-solve binding."""
    route = ROUTES[route_name]
    if route_name == "A":
        (nv, nc), body, regen = regenerate_a(route)
    else:
        (nv, nc), body, regen = regenerate_b(route, oracle)
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


def stream_pipeline(solver_parts, checker_parts, solver, prefix, solver_seconds, checker_seconds, wall_seconds):
    """Solver and drat-trim read the CNF from two FIFOs fed from memory; binary DRAT flows solver -> FIFO -> stdin."""
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
    stop, feeds, started, children = threading.Event(), {"solver": {}, "checker": {}}, [], []
    threads = {"checker": threading.Thread(target=feed, args=(paths["checker_cnf_fifo"], checker_parts, feeds["checker"], stop), daemon=True),
               "solver": threading.Thread(target=feed, args=(paths["solver_cnf_fifo"], solver_parts, feeds["solver"], stop), daemon=True)}
    command = [binary] + solver_arguments(solver, solver_seconds, paths["solver_cnf_fifo"], paths["proof_fifo"])
    checker_command = [CHECKER, paths["checker_cnf_fifo"], "-i", "-t", str(checker_seconds)]
    start, t0 = now(), time.monotonic()
    try:
        with open(paths["solver_log"], "x") as sl, open(paths["checker_log"], "x") as cl, open(paths["checkpoints"], "x") as cp:
            threads["checker"].start()
            started.append(threads["checker"])
            check = subprocess.Popen(checker_command, stdin=read_fd, stdout=cl, stderr=subprocess.STDOUT)
            children.append(check)
            threads["solver"].start()
            started.append(threads["solver"])
            solve = subprocess.Popen(command, stdout=sl, stderr=subprocess.STDOUT)
            children.append(solve)
            peak, reason = watch(solve, check, wall_seconds, cp, keep_writer)
    finally:
        for fd in [read_fd] + keep_writer:
            os.close(fd)
        stop.set()
        stop_children(children)
        for thread in started:
            thread.join(60)
    with open(paths["checker_log"]) as f:
        lines = [line.strip() for line in f.read().replace("\r", "\n").splitlines()]
    statuses = [line for line in lines if line.startswith("s ")]
    transport_ok = reason is None and solve.returncode == 20 and check.returncode == 0 and statuses == ["s VERIFIED"]
    return {"started_at": start, "finished_at": now(), "seconds": round(time.monotonic() - t0, 3),
            "solver_command": command, "checker_command": checker_command,
            "solver_rc": solve.returncode, "checker_rc": check.returncode, "checker_status_lines": statuses,
            "transport_verified": transport_ok, "peak_sampled_aggregate_rss_bytes": peak, "safety_stop_reason": reason,
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
    if available < GATE + GROWTH:
        record["status"] = "UNKNOWN / DEFERRED_RESOURCE; no solver/checker launched"
        with open(prefix + ".deferred.json", "x") as f:
            json.dump(record, f, indent=2)
            f.write("\n")
        print(json.dumps(record), flush=True)
        raise SystemExit(0)
    record["status"] = "PASS"
    return record


def preflight(route_name):
    """Frozen amendment, delta, generator r2 and controls receipts, oracle and binary pins, all mutually bound."""
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
          and generator["generator_sha256"] == delta["generator_r2"]["sha256"]
          and generator["block_sha256_A"] == BLOCK_SHA
          and controls.get("status") == "PASS" and controls["driver_sha256"] == driver_sha
          and controls["amendment_sha256"] == amendment_sha and controls["delta_sha256"] == delta_sha
          and controls["controls_sha256"] == delta["controls"]["sha256"]
          and controls["routes"][route_name]["strengthened_sha256"] is not None)
    if not ok:
        raise AssertionError("frozen amendment/delta/generator/controls bindings are inconsistent")
    binary = os.path.realpath(shutil.which(route["solver"]) or "")
    if not (os.path.isfile(binary) and sha(binary) == route["solver_sha256"] and sha(CHECKER) == CHECKER_SHA
            and sha(CHECKER + ".c") == CHECKER_SOURCE_SHA):
        raise AssertionError("solver or checker binary differs from its pin")
    return oracle, caps, {"amendment_sha256": amendment_sha, "delta_sha256": delta_sha,
                          "generator_r2_receipt_sha256": sha(GENERATOR_RECEIPT),
                          "controls_receipt_sha256": sha(CONTROLS_RECEIPT), "oracle_receipt_sha256": ORACLE_RECEIPT_SHA,
                          "expected_strengthened_sha256": controls["routes"][route_name]["strengthened_sha256"]}


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ROUTES:
        raise SystemExit("usage: k3_cuts_certify_r1.py A|B")
    route_name = sys.argv[1]
    route = ROUTES[route_name]
    lock = open(os.path.abspath(__file__), "rb")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        raise SystemExit("another C311+cuts pipeline holds the lock; not launched")
    os.makedirs(OUTDIR, exist_ok=True)
    prefix = os.path.join(OUTDIR, route_name + "_C311cuts")
    receipt = prefix + ".json"
    for path in (receipt, prefix + ".deferred.json"):
        if os.path.exists(path):
            raise FileExistsError(path)
    oracle, caps, bindings = preflight(route_name)
    first_gate = gate(prefix, "before in-memory regeneration and appending")
    prepared = prepare(route_name, oracle)
    if prepared["sha256"] != bindings["expected_strengthened_sha256"]:
        raise AssertionError("strengthened SHA differs from the controls receipt")
    second_gate = gate(prefix, "before the native proof pipeline")
    result = stream_pipeline(prepared["parts"], prepared["parts"], route["solver"], prefix,
                             caps["solver_seconds"], caps["checker_seconds"], caps["wall_guard_seconds"])
    feeds_ok = all(result["feeds"][k].get("sha256") == prepared["sha256"]
                   and result["feeds"][k].get("bytes_written") == prepared["bytes"]
                   and "error" not in result["feeds"][k] for k in ("solver", "checker"))
    verified = (result["transport_verified"] and feeds_ok and not result["feed_threads_alive_after_join"]
                and result["solver_binary_sha256"] == route["solver_sha256"]
                and result["checker_binary_sha256"] == CHECKER_SHA)
    status = "VERIFIED_UNSAT_CASE" if verified else ("SAT_PATTERN_ONLY" if result["solver_rc"] == 10 else "UNKNOWN")
    result.update({"route": route_name, "status": status, "verified_unsat": verified, "feeds_match_strengthened": feeds_ok,
                   "prepared": prepared["summary"], "outer_gates": [first_gate, second_gate], "bindings": bindings,
                   "planned_new_retained_bytes": GROWTH, "environment": environment(),
                   "driver_sha256": sha(os.path.abspath(__file__)),
                   "authority": "Parent AMENDMENT-4 disposition 3c9373c0...4e44 decisions 1-6; frozen AMENDMENT-4.r3 and "
                                "K3-CUTS-CERT-DELTA.r1 after parent source review",
                   "scope": "One strengthened C311 input on one route; parent replay and composition review remain separate"})
    with open(receipt, "x") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps({k: result[k] for k in ("route", "status", "verified_unsat", "solver_rc", "checker_rc",
                                             "checker_status_lines", "seconds")}), flush=True)


if __name__ == "__main__":
    main()
