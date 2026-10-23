#!/usr/bin/env python3
"""K3 cube CNF regeneration (encoder A) for the parent replay desk review/moqls7-k3-cube-parent-replay-v1.

Usage: compose_v1.py CUBE            (CUBE: a key of k3_cubes.CUBES, i.e. C311, C321 or C411)

The pinned lane modules gram_enc.py and k3_cubes.py are read as bytes, SHA-256 checked against the pins below, and
compiled and executed from exactly those bytes (no import-system lookup, no bytecode written; gram_enc is registered
in sys.modules first, so k3_cubes' 'import gram_enc' binds the verified module). The pinned functions then run
unchanged: k3_cubes.coverage(), k3_cubes.variable_map(), gram_enc.build(3, None, True, True, None) with the
variable-map identity check, and k3_cubes.cube_clauses(vmap, CUBE).

Deviation (recorded by the desk): k3_cubes.make() is not executed. It calls os.makedirs(<lane>/explore/scratch,
exist_ok=True) (k3_cubes.py:108-110), refuses existing output paths, writes OUT.cnf and OUT.json as files and
re-reads OUT.cnf to hash it (k3_cubes.py:103-105, 128-140). It therefore cannot run without a lane-path call and a
retained CNF file. Only make's deterministic encoder-A composition (k3_cubes.py:106-107, 111-116, 124-132) is
restated below, in make's order: header 'p cnf <nv> <nc + len(extra)>' (nv kept as the base header's text), the
base body after the base header line, then each extra clause as ' '.join(map(str, lits)) + ' 0'.

Output: the CNF bytes on stdout and one JSON line on stderr. Nothing is written to any file.
"""
import hashlib
import json
import sys
import time
import types

LANE_CODE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code"
PINS = {"gram_enc": ("gram_enc.py", "b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833"),
        "k3_cubes": ("k3_cubes.py", "70c79c624dd4c4ad0929a41790b7674eaa7343f3fcb5802c5e0c1abdbfb30550")}


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


def main():
    t0 = time.monotonic()
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    cube = sys.argv[1]
    gram_enc, h_enc, n_enc = load("gram_enc")
    k3, h_k3, n_k3 = load("k3_cubes")
    if k3.gram_enc is not gram_enc:
        raise SystemExit("k3_cubes bound a different gram_enc module")
    if cube not in k3.CUBES:
        raise SystemExit("unknown cube " + cube)
    # k3_cubes.make(encoder="A"), lines 106-107, 111-116, 124-132, in that order
    cov = k3.coverage()
    vmap = k3.variable_map()
    F, actual = gram_enc.build(3, None, True, True, None)
    expected = {"%d|%d,%d|%d,%d" % (a, p[0], p[1], q[0], q[1]): v
                for (a, p, q), v in vmap.items()}
    if actual != expected:
        raise SystemExit("encoder A variable map differs from k3_cubes.variable_map()")
    base = F.text()
    header, body = base.split("\n", 1)
    tag, form, nv, nc = header.split()
    if not ((tag, form) == ("p", "cnf") and int(nv) >= len(vmap)):
        raise SystemExit("unexpected base header " + header)
    clauses, units, twins = k3.cube_clauses(vmap, cube)
    head = "p cnf %s %d\n" % (nv, int(nc) + len(clauses))
    extra = "".join(" ".join(map(str, cl)) + " 0\n" for cl in clauses)
    out = (head + body + extra).encode("ascii")
    info = {"cube": cube, "encoder": "A",
            "gram_enc": {"path": LANE_CODE + "/gram_enc.py", "sha256": h_enc, "bytes": n_enc},
            "k3_cubes": {"path": LANE_CODE + "/k3_cubes.py", "sha256": h_k3, "bytes": n_k3},
            "coverage": {"status": cov["status"], "n_valid": cov["n_valid"],
                         "complete_disjoint_cover": cov["complete_disjoint_cover"]},
            "vmap_entries": len(vmap), "vmap_equals_encoder_A_map": True,
            "base_cnf_sha256": hashlib.sha256(base.encode()).hexdigest(), "base_bytes": len(base),
            "base_header": [int(nv), int(nc)],
            "support_sets": [sorted(S) for S in k3.CUBES[cube]], "cube_unit_clauses": units,
            "same_ray_identities": json.loads(json.dumps(twins)), "extra_clauses": len(clauses),
            "extra_text_sha256": hashlib.sha256(extra.encode("ascii")).hexdigest(),
            "out_header": [int(nv), int(nc) + len(clauses)], "out_bytes": len(out),
            "out_sha256": hashlib.sha256(out).hexdigest(),
            "python": sys.version.split()[0], "python_executable": sys.executable,
            "seconds": round(time.monotonic() - t0, 3)}
    sys.stdout.buffer.write(out)
    sys.stdout.buffer.flush()
    sys.stderr.write(json.dumps(info, sort_keys=True) + "\n")
    sys.stderr.flush()


if __name__ == "__main__":
    main()
