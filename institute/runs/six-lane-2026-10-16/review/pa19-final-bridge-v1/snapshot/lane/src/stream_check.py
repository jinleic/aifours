#!/usr/bin/env python3
"""Online proof checking without storing CNFs or proofs (cycle-2 disk rule).

kissat_stream: kissat 4.0.4 (--seed=1) reads the CNF from a FIFO and writes a binary DRAT
proof into a FIFO; the stream is hashed (SHA-256) and piped into drat-trim (-i, proof on
stdin), whose LRAT output goes through another FIFO, is hashed, and is piped into lrat-check.
cadical_stream: CaDiCaL 3.0.1 writes ASCII LRAT into a FIFO; hashed and piped into
lrat-check. CNF bytes are produced in memory and hashed; nothing is written to disk except
the FIFOs (zero-size). Both are deterministic, so recorded hashes can be reproduced.
"""
import hashlib
import os
import subprocess
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
KISSAT = "/opt/homebrew/bin/kissat"
CADICAL = "/opt/homebrew/bin/cadical"
DT = os.path.join(LANE, "tools", "drat-trim", "drat-trim")
LC = os.path.join(LANE, "tools", "drat-trim", "lrat-check")


def fifos(wdir, names):
    os.makedirs(wdir, exist_ok=True)
    out = {}
    for n in names:
        p = os.path.join(wdir, n)
        if not os.path.exists(p):
            os.mkfifo(p)
        out[n] = p
    return out


def _writer(path, data):
    try:
        with open(path, "wb") as f:
            f.write(data)
    except OSError:
        pass


def _forward(src_path, dst_file, h, counter):
    try:
        with open(src_path, "rb") as f:
            while True:
                b = f.read(1 << 16)
                if not b:
                    break
                h.update(b)
                counter[0] += len(b)
                try:
                    dst_file.write(b)
                except (OSError, ValueError):
                    pass
    finally:
        try:
            dst_file.close()
        except (OSError, ValueError):
            pass


def _collect(stream, sink):
    for line in iter(stream.readline, b""):
        sink.append(line)
    stream.close()


def _start(cmd, stdin=False):
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE if stdin else subprocess.DEVNULL,
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    sink = []
    t = threading.Thread(target=_collect, args=(p.stdout, sink), daemon=True)
    t.start()
    return p, sink, t


def _unblock(path):
    # release a thread blocked opening this FIFO for reading (no writer ever came);
    # callers use a fresh FIFO directory per case, so no stream can leak into another case
    try:
        fd = os.open(path, os.O_WRONLY | os.O_NONBLOCK)
        os.close(fd)
    except OSError:
        pass


def kissat_stream(cnf_bytes, wdir, timeout, dt_timeout=20000):
    F = fifos(wdir, ["cnf_k", "cnf_d", "cnf_l", "prf", "lrat"])
    res = {"cnf_sha256": hashlib.sha256(cnf_bytes).hexdigest(), "cnf_bytes": len(cnf_bytes),
           "solver": "kissat 4.0.4 -q -f --seed=1 (binary DRAT streamed to drat-trim -i)"}
    lc, lc_out, lc_t = _start([LC, F["cnf_l"], "/dev/stdin"], stdin=True)
    dt, dt_out, dt_t = _start([DT, F["cnf_d"], "-i", "-L", F["lrat"], "-t", str(dt_timeout)], stdin=True)
    hl, nl = hashlib.sha256(), [0]
    hp, npf = hashlib.sha256(), [0]
    fw = [threading.Thread(target=_forward, args=(F["lrat"], lc.stdin, hl, nl), daemon=True),
          threading.Thread(target=_forward, args=(F["prf"], dt.stdin, hp, npf), daemon=True)]
    wr = [threading.Thread(target=_writer, args=(F[n], cnf_bytes), daemon=True) for n in ("cnf_d", "cnf_l", "cnf_k")]
    for t in fw + wr:
        t.start()
    t0 = time.time()
    ks, ks_out, ks_t = _start([KISSAT, "-q", "-f", "--seed=1", F["cnf_k"], F["prf"]])
    try:
        ks.wait(timeout=timeout)
        rc = ks.returncode
    except subprocess.TimeoutExpired:
        ks.kill()
        ks.wait()
        rc = -1
    ks_t.join()
    res["solve_seconds"] = round(time.time() - t0, 2)
    res["solver_rc"] = rc
    res["status"] = {10: "SAT", 20: "UNSAT"}.get(rc, "UNKNOWN")
    res["solver_out"] = b"".join(ks_out).decode(errors="replace") if rc == 10 else ""
    t1 = time.time()
    if rc != 20:
        dt.kill()
        lc.kill()
    fw[1].join()
    dt.wait()
    dt_t.join()
    if dt.returncode != 0 or rc != 20:
        _unblock(F["lrat"])
    fw[0].join()
    lc.wait()
    lc_t.join()
    for t in wr:
        t.join(timeout=2)
    res["check_seconds"] = round(time.time() - t1, 2)
    res["drat_sha256"] = hp.hexdigest()
    res["drat_bytes"] = npf[0]
    res["lrat_sha256"] = hl.hexdigest()
    res["lrat_bytes"] = nl[0]
    dto = b"".join(dt_out).decode(errors="replace")
    lco = b"".join(lc_out).decode(errors="replace")
    res["drat_trim_verified"] = "s VERIFIED" in dto
    res["lrat_verified"] = lc.returncode == 0 and "c VERIFIED" in lco.splitlines()
    res["checked"] = res["status"] == "UNSAT" and res["drat_trim_verified"] and res["lrat_verified"]
    return res


def cadical_stream(cnf_bytes, wdir, timeout):
    F = fifos(wdir, ["cnf_c", "cnf_l2", "lrat2"])
    res = {"cnf_sha256": hashlib.sha256(cnf_bytes).hexdigest(), "cnf_bytes": len(cnf_bytes),
           "solver": "cadical 3.0.1 -q --lrat=true --binary=false (LRAT streamed to lrat-check)"}
    lc, lc_out, lc_t = _start([LC, F["cnf_l2"], "/dev/stdin"], stdin=True)
    hl, nl = hashlib.sha256(), [0]
    fw = threading.Thread(target=_forward, args=(F["lrat2"], lc.stdin, hl, nl), daemon=True)
    wr = [threading.Thread(target=_writer, args=(F[n], cnf_bytes), daemon=True) for n in ("cnf_l2", "cnf_c")]
    for t in [fw] + wr:
        t.start()
    t0 = time.time()
    cs, cs_out, cs_t = _start([CADICAL, "-q", "--lrat=true", "--binary=false", F["cnf_c"], F["lrat2"]])
    try:
        cs.wait(timeout=timeout)
        rc = cs.returncode
    except subprocess.TimeoutExpired:
        cs.kill()
        cs.wait()
        rc = -1
    cs_t.join()
    res["solve_seconds"] = round(time.time() - t0, 2)
    res["solver_rc"] = rc
    res["status"] = {10: "SAT", 20: "UNSAT"}.get(rc, "UNKNOWN")
    res["solver_out"] = b"".join(cs_out).decode(errors="replace") if rc == 10 else ""
    t1 = time.time()
    if rc != 20:
        lc.kill()
        _unblock(F["lrat2"])
    fw.join()
    lc.wait()
    lc_t.join()
    for t in wr:
        t.join(timeout=2)
    res["check_seconds"] = round(time.time() - t1, 2)
    res["lrat_sha256"] = hl.hexdigest()
    res["lrat_bytes"] = nl[0]
    lco = b"".join(lc_out).decode(errors="replace")
    res["lrat_verified"] = lc.returncode == 0 and "c VERIFIED" in lco.splitlines()
    res["checked"] = res["status"] == "UNSAT" and res["lrat_verified"]
    return res


def cnf_bytes_of(F):
    parts = ["p cnf %d %d\n" % (F.nv, len(F.clauses))]
    parts.extend(" ".join(map(str, cl)) + " 0\n" for cl in F.clauses)
    return "".join(parts).encode()
