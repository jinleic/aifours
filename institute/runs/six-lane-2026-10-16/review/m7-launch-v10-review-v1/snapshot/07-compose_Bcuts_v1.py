#!/usr/bin/env python3
"""B/C311 + AMENDMENT-4 cuts CNF regeneration (encoder B), for the parent desk review/moqls7-k3-B-cube-parent-replay-v1.

Usage: compose_Bcuts_v1.py C311

This is the desk's own composition driver; the producer's driver (k3_cuts_certify_r6.py) and generator receipts are
not imported or run. Like compose_B_v1.py, it reads the pinned lane sources gram_enc.py, k3_cubes.py, k3_lex.py,
k3_cuts_r1.py and gram_encB.py as bytes, SHA-256 checks them against the pins below, then compiles and executes
exactly those bytes as modules named after their files (never as __main__; no import-system lookup; no bytecode).
The modules are registered in sys.modules in dependency order, so k3_lex's and k3_cuts_r1's imports bind the
verified modules.

Pinned functions run unchanged:
  * gram_encB.main() with argv '--squares 3 --heavy --sym --out /dev/fd/W'. As in compose_B_v1.py, W is an in-process
    pipe read into memory, and the closing stats print is captured and checked against the header;
  * k3_cubes.coverage(), k3_cubes.variable_map(), k3_cubes.cube_clauses(vmap, 'C311');
  * k3_cuts_r1.emit(k3_cubes.variable_map()), the AMENDMENT-4 cut block.
Only the composition is restated:
  input  = 'p cnf <nv> <nc + len(cube)>' + base body + cube clauses. This is k3_cubes.make's encoder-B composition,
           and its SHA-256 must equal the pinned explore/k3cubes/B_C311.cnf;
  output = 'p cnf <nv> <nc_input + len(block)>' + input body + block. This is k3_cuts_certify_r6.prepare's route-B
           composition (header, body, block; each clause written as ' '.join(map(str, lits)) + ' 0').
The pins for the input, the block and the output are asserted. Output: the CNF bytes on stdout and one JSON line on
stderr. Nothing is written to any file.
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
        "k3_lex": ("k3_lex.py", "2b721e85812cd7b3438771868f63da1e10f3fbeed6551f7888f74a399e159b10"),
        "k3_cuts_r1": ("k3_cuts_r1.py", "0ec92c861024a728aa38d238fda2d7f5f056fae12cb0f474a15db0335b6e1b0a"),
        "gram_encB": ("gram_encB.py", "c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45")}
ENC_B_ARGS = ["--squares", "3", "--heavy", "--sym"]
INPUT_SHA256 = "b3ec010855ad4abd75ffd6eb57aaa3ff158bc8447625ee2097f5a6057594c077"      # explore/k3cubes/B_C311.cnf
BLOCK_SHA256 = "05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd"
BLOCK_CLAUSES = 238140
OUTPUT_SHA256 = "ae3b8309601d115e2258782ae3cb793f4dc4b5950064b9536b1eca61521f783a"
INPUT_HEADER, OUTPUT_HEADER = (461370, 1629802), (461370, 1867942)


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


def lines(clauses):
    return "".join(" ".join(map(str, cl)) + " 0\n" for cl in clauses).encode("ascii")


def main():
    t0 = time.monotonic()
    if len(sys.argv) != 2 or sys.argv[1] != "C311":
        raise SystemExit(__doc__)
    mods = {}
    for name in ("gram_enc", "k3_cubes", "k3_lex", "k3_cuts_r1", "gram_encB"):
        mods[name] = load(name)
    k3, lex, cuts = mods["k3_cubes"][0], mods["k3_lex"][0], mods["k3_cuts_r1"][0]
    if not (k3.gram_enc is mods["gram_enc"][0] and lex.k3_cubes is k3 and cuts.k3_cubes is k3
            and cuts.k3_lex is lex and cuts.gram_enc is mods["gram_enc"][0]):
        raise SystemExit("a lane module bound an unverified dependency")
    cov = k3.coverage()
    vmap = k3.variable_map()
    t_enc = time.monotonic()
    base, stats = run_encoder_b(mods["gram_encB"][0])
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
    cube, units, twins = k3.cube_clauses(vmap, "C311")
    extra = lines(cube)
    nc_in = int(nc) + len(cube)
    input_bytes = b"p cnf %s %d\n" % (nv, nc_in) + body + extra
    input_sha = hashlib.sha256(input_bytes).hexdigest()
    if input_sha != INPUT_SHA256 or (int(nv), nc_in) != INPUT_HEADER:
        raise SystemExit("regenerated B_C311 input %s %r differs from the pin" % (input_sha, (int(nv), nc_in)))
    del input_bytes
    block_clauses = cuts.emit(k3.variable_map())
    block = lines(block_clauses)
    block_sha = hashlib.sha256(block).hexdigest()
    if block_sha != BLOCK_SHA256 or len(block_clauses) != BLOCK_CLAUSES:
        raise SystemExit("cut block %s (%d clauses) differs from the pin" % (block_sha, len(block_clauses)))
    out = b"p cnf %d %d\n" % (int(nv), nc_in + len(block_clauses)) + body + extra + block
    out_sha = hashlib.sha256(out).hexdigest()
    if out_sha != OUTPUT_SHA256 or (int(nv), nc_in + len(block_clauses)) != OUTPUT_HEADER:
        raise SystemExit("strengthened output %s differs from the pin" % out_sha)
    info = {"cube": "C311", "encoder": "B", "kind": "C311 + AMENDMENT-4 cuts",
            "modules": {n: {"path": LANE_CODE + "/" + PINS[n][0], "sha256": m[1], "bytes": m[2]}
                        for n, m in mods.items()},
            "gram_encB": {"argv": ENC_B_ARGS + ["--out", "/dev/fd/<in-process pipe>"], "seconds": enc_seconds,
                          "stats_line": stats.strip()},
            "coverage": {"status": cov["status"], "n_valid": cov["n_valid"],
                         "complete_disjoint_cover": cov["complete_disjoint_cover"]},
            "vmap_entries": len(vmap),
            "base_cnf_sha256": hashlib.sha256(base).hexdigest(), "base_bytes": len(base),
            "base_header": [int(nv), int(nc)], "base_empty_clause_lines": empty_clause_lines,
            "support_sets": [sorted(S) for S in k3.CUBES["C311"]], "cube_unit_clauses": units,
            "same_ray_identities": json.loads(json.dumps(twins)), "extra_clauses": len(cube),
            "input_sha256": input_sha, "input_header": [int(nv), nc_in],
            "block_sha256": block_sha, "block_clauses": len(block_clauses), "block_bytes": len(block),
            "out_header": [int(nv), nc_in + len(block_clauses)], "out_bytes": len(out), "out_sha256": out_sha,
            "python": sys.version.split()[0], "python_executable": sys.executable,
            "ru_maxrss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "seconds": round(time.monotonic() - t0, 3)}
    sys.stdout.buffer.write(out)
    sys.stdout.buffer.flush()
    sys.stderr.write(json.dumps(info, sort_keys=True) + "\n")
    sys.stderr.flush()


if __name__ == "__main__":
    main()
