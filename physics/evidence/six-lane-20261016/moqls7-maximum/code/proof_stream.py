#!/usr/bin/env python3
"""Bounded binary-DRAT pipe transport, shared by new transport controls and K3.

Nonblocking parent FIFO endpoints eliminate the startup handshake: native solvers
write a normal FIFO pathname; checker reads blocking stdin -i. A parent keepalive
writer is closed when the solver exits. Full logs go directly to exclusive files.
Old K2 driver and receipts are preserved; this module makes no claim about them.
"""
import json
import os
import shutil
import subprocess
import time

from gram_certify_r4 import CHECKER, LANE, now, rss, sha



def stop_children(children):
    for child in children:
        if child.poll() is None:
            child.terminate()
    end = time.monotonic() + 30
    while any(c.poll() is None for c in children):
        if time.monotonic() > end:
            raise RuntimeError("SIGTERM grace exceeded; no SIGKILL sent")
        time.sleep(0.1)


def watch(solve, check, wall_seconds, checkpoint_file, keep_writer):
    peak, reason, last_checkpoint = 0, None, -900
    t0 = time.monotonic()
    while True:
        if solve.poll() is not None and keep_writer:
            os.close(keep_writer.pop())
        alive = solve.poll() is None or check.poll() is None
        elapsed = time.monotonic() - t0
        current = rss(os.getpid()) + rss(solve.pid) + rss(check.pid)
        peak = max(peak, current)
        if elapsed - last_checkpoint >= 900 or not alive:
            checkpoint = {"at": now(), "elapsed_seconds": round(elapsed, 3),
                          "aggregate_rss_bytes": current, "peak_sampled_rss_bytes": peak,
                          "solver_rc": solve.poll(), "checker_rc": check.poll()}
            checkpoint_file.write(json.dumps(checkpoint) + "\n")
            checkpoint_file.flush()
            print(json.dumps({"proof_pipeline_checkpoint": checkpoint}), flush=True)
            last_checkpoint = elapsed
        if not alive:
            break
        st = os.statvfs(LANE)
        if current > 3584 * 1024 * 1024:
            reason = "aggregate RSS safety threshold 3.5 GiB"
        elif st.f_bavail * st.f_frsize < 12000000000:
            reason = "global free-space floor"
        elif elapsed > wall_seconds:
            reason = "combined native-child wall-clock cap"
        elif check.poll() is not None and solve.poll() is None:
            reason = "checker exited before proof writer"
        if reason:
            stop_children((solve, check))
            break
        time.sleep(0.25)
    return peak, reason


def run_pair(cnf, solver_prefix, log_prefix, solver_seconds, checker_seconds):
    if not 1 <= solver_seconds <= 3600 or not 1 <= checker_seconds <= 3600:
        raise ValueError("Each native limit must be between 1 and 3600 seconds")
    st = os.statvfs(LANE)
    if st.f_bavail * st.f_frsize < 12000000000 or not rss(os.getpid()):
        raise RuntimeError("Free-space floor or native RSS prerequisite failed")
    solver_log, checker_log = log_prefix + ".solver.log", log_prefix + ".checker.log"
    checkpoints, fifo = log_prefix + ".checkpoints.jsonl", log_prefix + ".drat.fifo"
    if any(os.path.exists(path) for path in (solver_log, checker_log, checkpoints, fifo)):
        raise FileExistsError(log_prefix)
    binary = shutil.which(solver_prefix[0])
    if not binary:
        raise FileNotFoundError(solver_prefix[0])
    binary = os.path.realpath(binary)
    prefix = [binary] + list(solver_prefix[1:])
    solver_sha, cnf_sha = sha(binary), sha(cnf)
    os.mkfifo(fifo)
    read_fd = os.open(fifo, os.O_RDONLY | os.O_NONBLOCK)
    keep_writer = [os.open(fifo, os.O_WRONLY | os.O_NONBLOCK)]
    os.set_blocking(read_fd, True)
    children = []
    start, t0 = now(), time.monotonic()
    command = prefix + [fifo]
    checker_command = [CHECKER, cnf, "-i", "-t", str(checker_seconds)]
    try:
        with open(solver_log, "x") as sl, open(checker_log, "x") as cl, open(checkpoints, "x") as cp:
            check = subprocess.Popen(checker_command, stdin=read_fd, stdout=cl, stderr=subprocess.STDOUT)
            children.append(check)
            solve = subprocess.Popen(command, stdout=sl, stderr=subprocess.STDOUT)
            children.append(solve)
            peak, reason = watch(solve, check, solver_seconds + checker_seconds + 120, cp, keep_writer)
    finally:
        for fd in [read_fd] + keep_writer:
            os.close(fd)
        stop_children(children)
    with open(checker_log) as f:
        lines = [line.strip() for line in f.read().replace("\r", "\n").splitlines()]
    statuses = [line for line in lines if line.startswith("s ")]
    ok = reason is None and solve.returncode == 20 and check.returncode == 0 and statuses == ["s VERIFIED"]
    return {"started_at": start, "finished_at": now(), "seconds": round(time.monotonic() - t0, 3),
            "solver_command": command, "checker_command": checker_command,
            "solver_rc": solve.returncode, "checker_rc": check.returncode,
            "checker_status_lines": statuses, "verified_unsat": ok,
            "peak_sampled_aggregate_rss_bytes": peak, "safety_stop_reason": reason,
            "cnf_sha256": cnf_sha, "solver_binary_sha256": solver_sha,
            "checker_binary_sha256": sha(CHECKER), "checker_source_sha256": sha(CHECKER + ".c"),
            "solver_log_sha256": sha(solver_log), "checker_log_sha256": sha(checker_log),
            "checkpoint_log_sha256": sha(checkpoints),
            "transport_code_sha256": sha(__file__),
            "rss_sampler_code_sha256": sha(os.path.join(os.path.dirname(__file__), "gram_certify_r4.py")),
            "transport": "nonblocking FIFO startup; parent keepalive until writer exit; binary stdin -i reader",
            "proof_storage": "streamed only; CNF and full logs retained by caller"}
