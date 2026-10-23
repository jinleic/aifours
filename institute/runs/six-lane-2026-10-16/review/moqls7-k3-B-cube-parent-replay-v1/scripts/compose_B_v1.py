#!/usr/bin/env python3
"""K3 cube CNF regeneration, encoder B, for the parent desk review/moqls7-k3-B-cube-parent-replay-v1.

Usage: compose_B_v1.py CUBE            (CUBE: a key of k3_cubes.CUBES, i.e. C311, C321 or C411)

This is the desk's own composition driver; the producer's regeneration code (k3_cube_certify_r3.py) and drivers are
not imported or run. The pinned lane sources gram_enc.py, k3_cubes.py and gram_encB.py are read as bytes, SHA-256
checked against the pins below, then compiled and executed from exactly those bytes as modules named after their
files (never as __main__; no import-system lookup; no bytecode written). gram_enc is registered in sys.modules
first, so k3_cubes' 'import gram_enc' binds the verified module.

Pinned functions, run unchanged:
  * k3_cubes.coverage(), k3_cubes.variable_map(), k3_cubes.cube_clauses(vmap, CUBE);
  * gram_encB.main() with argv '--squares 3 --heavy --sym --out /dev/fd/W', the production arguments that
    k3_cubes.make(encoder="B") passes (k3_cubes.py make()). W is the write end of an anonymous pipe owned by this
    process; a reader thread collects the bytes that the encoder's own Builder.dump() writes, in memory. The
    encoder's closing 'vars N clauses M' print goes to sys.stdout, which is redirected to an in-memory buffer
    for the duration of main() and checked against the header.
Only make's encoder-B composition is restated, in make's order: header 'p cnf <nv> <nc + len(extra)>' (nv kept as
the base header's text), the base body after its header line, then each extra clause as
' '.join(map(str, lits)) + ' 0'.

Output: the CNF bytes on stdout and one JSON line on stderr. Nothing is written to any file.
"""
import contextlib
import hashlib
import io
import json
import os
import resource
import sys
import threading
import time
import types

LANE_CODE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code"
PINS = {"gram_enc": ("gram_enc.py", "b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833"),
        "k3_cubes": ("k3_cubes.py", "70c79c624dd4c4ad0929a41790b7674eaa7343f3fcb5802c5e0c1abdbfb30550"),
        "gram_encB": ("gram_encB.py", "c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45")}
ENC_B_ARGS = ["--squares", "3", "--heavy", "--sym"]


def load(name):
    fname, pin = PINS[name]
    path = LANE_CODE + "/" + fname
    with open(path, "rb") as f:
        src = f.read()
    got = hashlib.sha256(src).hexdigest()
    if got != pin:
        raise SystemExit("pin mismatch for %s: %s != %s" % (path, got, pin))
    mod = types.ModuleType(name)
    mod.__file__ = path
    code = compile(src, path, "exec", dont_inherit=True)
    sys.modules[name] = mod
    exec(code, mod.__dict__)
    return mod, got, len(src)


def run_encoder_b(enc_b):
    """Run the verified gram_encB.main() with the production arguments; return (dumped bytes, captured stdout)."""
    rfd, wfd = os.pipe()
    chunks, err = [], {}

    def reader():
        try:
            while True:
                b = os.read(rfd, 1 << 20)
                if not b:
                    break
                chunks.append(b)
        except OSError as e:
            err["reader"] = repr(e)

    t = threading.Thread(target=reader, daemon=True)
    t.start()
    saved = sys.argv
    sys.argv = [enc_b.__file__] + ENC_B_ARGS + ["--out", "/dev/fd/%d" % wfd]
    captured = io.StringIO()
    try:
        with contextlib.redirect_stdout(captured):
            enc_b.main()
    finally:
        sys.argv = saved
        os.close(wfd)
    t.join()
    os.close(rfd)
    if err:
        raise SystemExit("encoder B pipe reader failed: %r" % err)
    return b"".join(chunks), captured.getvalue()


def main():
    t0 = time.monotonic()
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    cube = sys.argv[1]
    gram_enc, h_enc, n_enc = load("gram_enc")
    k3, h_k3, n_k3 = load("k3_cubes")
    if k3.gram_enc is not gram_enc:
        raise SystemExit("k3_cubes bound a different gram_enc module")
    enc_b, h_b, n_b = load("gram_encB")
    if cube not in k3.CUBES:
        raise SystemExit("unknown cube " + cube)
    cov = k3.coverage()
    vmap = k3.variable_map()
    t_enc = time.monotonic()
    base, stats = run_encoder_b(enc_b)
    enc_seconds = round(time.monotonic() - t_enc, 3)
    header, body = base.split(b"\n", 1)
    tag, form, nv, nc = header.split()
    if not ((tag, form) == (b"p", b"cnf") and int(nv) >= len(vmap)):
        raise SystemExit("unexpected base header %r" % header)
    if stats != "vars %d clauses %d\n" % (int(nv), int(nc)):
        raise SystemExit("encoder B stats line %r does not match its header %r" % (stats, header))
    if not body.endswith(b"\n") or body.count(b"\n") != int(nc):
        raise SystemExit("encoder B body is not exactly nc newline-terminated clause lines")
    empty_clause_lines = sum(1 for ln in body.split(b"\n")[:-1] if ln.split() == [b"0"])
    clauses, units, twins = k3.cube_clauses(vmap, cube)
    head = b"p cnf %s %d\n" % (nv, int(nc) + len(clauses))
    extra = "".join(" ".join(map(str, cl)) + " 0\n" for cl in clauses).encode("ascii")
    out = head + body + extra
    info = {"cube": cube, "encoder": "B",
            "gram_enc": {"path": LANE_CODE + "/gram_enc.py", "sha256": h_enc, "bytes": n_enc},
            "k3_cubes": {"path": LANE_CODE + "/k3_cubes.py", "sha256": h_k3, "bytes": n_k3},
            "gram_encB": {"path": LANE_CODE + "/gram_encB.py", "sha256": h_b, "bytes": n_b,
                          "argv": ENC_B_ARGS + ["--out", "/dev/fd/<in-process pipe>"],
                          "seconds": enc_seconds, "stats_line": stats.strip()},
            "coverage": {"status": cov["status"], "n_valid": cov["n_valid"],
                         "complete_disjoint_cover": cov["complete_disjoint_cover"]},
            "vmap_entries": len(vmap),
            "base_cnf_sha256": hashlib.sha256(base).hexdigest(), "base_bytes": len(base),
            "base_header": [int(nv), int(nc)], "base_empty_clause_lines": empty_clause_lines,
            "support_sets": [sorted(S) for S in k3.CUBES[cube]], "cube_unit_clauses": units,
            "same_ray_identities": json.loads(json.dumps(twins)), "extra_clauses": len(clauses),
            "extra_text_sha256": hashlib.sha256(extra).hexdigest(),
            "out_header": [int(nv), int(nc) + len(clauses)], "out_bytes": len(out),
            "out_sha256": hashlib.sha256(out).hexdigest(),
            "python": sys.version.split()[0], "python_executable": sys.executable,
            "ru_maxrss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "seconds": round(time.monotonic() - t0, 3)}
    sys.stdout.buffer.write(out)
    sys.stdout.buffer.flush()
    sys.stderr.write(json.dumps(info, sort_keys=True) + "\n")
    sys.stderr.flush()


if __name__ == "__main__":
    main()
