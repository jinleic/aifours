#!/usr/bin/env python3
"""Route-A C311 + AMENDMENT-4 cuts CNF regeneration (encoder A, lex C311), for the parent desk
review/moqls7-k3-B-cube-parent-replay-v1.

Usage: compose_Acuts_v1.py C311

This is the desk's own composition driver. The producer's driver (k3_cuts_certify_r9.py, 2f0ced45...77ed3) is not
imported or run. The pinned lane sources gram_enc.py, k3_cubes.py, k3_lex.py and k3_cuts_r1.py are read as bytes and
SHA-256 checked against the pins below. Exactly those bytes are then compiled and executed as modules named after
their files: never as __main__, with no import-system lookup and no bytecode. The modules are registered in
sys.modules in dependency order, so the imports inside k3_cubes, k3_lex and k3_cuts_r1 bind the verified modules.

Pinned functions run unchanged:
  * gram_enc.build(3, None, True, True, None), the encoder-A base (F.nv, F.cl) and its literal map. The map must equal
    the cube wrapper's k3_cubes.variable_map();
  * k3_cubes.variable_map(), k3_cubes.cube_clauses(vmap, 'C311');
  * k3_lex.generators('C311'), k3_lex.image(vmap, gen), k3_lex.lex_clauses(sorted(perm.items()), nv), in generator order;
  * k3_cuts_r1.emit(k3_cubes.variable_map()), the AMENDMENT-4 cut block.
Only route A's composition is restated (as k3_cuts_certify_r9.regenerate_a and prepare do):
  base   = 'p cnf nv nbase' + lines(F.cl)                           pinned d0d884f9...4388;
  source = 'p cnf nv (nbase + cube)' + base body + lines(cube)       pinned 7fca33f1...2001 (explore/k3cubes/A_C311.cnf);
  input  = 'p cnf lex_nv (nbase + cube + lex)' + base body + cube lines + lex lines
                                                                    pinned 059be616...8c4f (explore/k3lex/A_C311.cnf);
  output = 'p cnf lex_nv (nc_input + block)' + input body + block lines
                                                                    pinned 18583aab...2e5e (r9 receipt 88c154b7...f37f).
Each clause line is ' '.join(map(str, lits)) + ' 0'. The output CNF goes to stdout and one JSON line to stderr. Nothing
is written to any file.
"""
import hashlib
import json
import resource
import sys
import time
import types

LANE_CODE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum/code"
PINS = {"gram_enc": ("gram_enc.py", "b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833"),
        "k3_cubes": ("k3_cubes.py", "70c79c624dd4c4ad0929a41790b7674eaa7343f3fcb5802c5e0c1abdbfb30550"),
        "k3_lex": ("k3_lex.py", "2b721e85812cd7b3438771868f63da1e10f3fbeed6551f7888f74a399e159b10"),
        "k3_cuts_r1": ("k3_cuts_r1.py", "0ec92c861024a728aa38d238fda2d7f5f056fae12cb0f474a15db0335b6e1b0a")}
BASE_SHA256 = "d0d884f9a0f9715b256da68be97408ae4a55c88d76183c02246a570f115a4388"
SOURCE_CUBE_SHA256 = "7fca33f1e6324cbe17bc44bbea7f8d9188bcac187252d766fb0fa5e39e1c2001"
INPUT_SHA256 = "059be6164176ee93c94d93bd47fa1d365477b6c94f3aa867df991f677e1a8c4f"
BLOCK_SHA256 = "05f31da497315877347f7d780e0e6f4c9c4799c8becee3bdb192a8420ff6e6dd"
BLOCK_CLAUSES = 238140
OUTPUT_SHA256 = "18583aabb486b2d7fdf2159ed2172c9dfc9b29bbd2e50c63a5d7d94d44ba2e5e"
BASE_HEADER, INPUT_HEADER, OUTPUT_HEADER = (96978, 627398), (107513, 659168), (107513, 897308)


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


def lines(clauses):
    return "".join(" ".join(map(str, cl)) + " 0\n" for cl in clauses).encode("ascii")


def header(nv, nc):
    return b"p cnf %d %d\n" % (nv, nc)


def main():
    t0 = time.monotonic()
    if len(sys.argv) != 2 or sys.argv[1] != "C311":
        raise SystemExit(__doc__)
    mods = {}
    for name in ("gram_enc", "k3_cubes", "k3_lex", "k3_cuts_r1"):
        mods[name] = load(name)
    enc, k3, lex, cuts = (mods[n][0] for n in ("gram_enc", "k3_cubes", "k3_lex", "k3_cuts_r1"))
    if not (k3.gram_enc is enc and lex.k3_cubes is k3 and cuts.k3_cubes is k3 and cuts.k3_lex is lex
            and cuts.gram_enc is enc):
        raise SystemExit("a lane module bound an unverified dependency")
    cov = k3.coverage()
    vmap = k3.variable_map()
    t_enc = time.monotonic()
    F, amap = enc.build(3, None, True, True, None)
    enc_seconds = round(time.monotonic() - t_enc, 3)
    expected_map = {"%d|%d,%d|%d,%d" % (a, p[0], p[1], q[0], q[1]): v for (a, p, q), v in vmap.items()}
    if amap != expected_map:
        raise SystemExit("encoder A map differs from the cube wrapper map")
    nv, nbase = F.nv, len(F.cl)
    base_body = lines(F.cl)
    del F, amap
    if (nv, nbase) != BASE_HEADER or hashlib.sha256(header(nv, nbase) + base_body).hexdigest() != BASE_SHA256:
        raise SystemExit("regenerated encoder-A base differs from the pin")
    empty_clause_lines = sum(1 for ln in base_body.split(b"\n")[:-1] if ln.split() == [b"0"])
    cube, units, twins = k3.cube_clauses(vmap, "C311")
    cube_body = lines(cube)
    source_sha = hashlib.sha256(header(nv, nbase + len(cube)) + base_body + cube_body).hexdigest()
    if source_sha != SOURCE_CUBE_SHA256:
        raise SystemExit("regenerated A original C311 %s differs from the pin" % source_sha)
    lex_nv, lex_cl, per_gen = nv, [], []
    for gen in lex.generators("C311"):
        perm = lex.image(vmap, gen)
        lex_nv, clauses = lex.lex_clauses(sorted(perm.items()), lex_nv)
        lex_cl.extend(clauses)
        per_gen.append({"generator": gen, "clauses": len(clauses)})
    body = base_body + cube_body + lines(lex_cl)
    del base_body, cube_body
    nc_in = nbase + len(cube) + len(lex_cl)
    input_sha = hashlib.sha256(header(lex_nv, nc_in) + body).hexdigest()
    if input_sha != INPUT_SHA256 or (lex_nv, nc_in) != INPUT_HEADER:
        raise SystemExit("regenerated lex input %s %r differs from the pin" % (input_sha, (lex_nv, nc_in)))
    block_clauses = cuts.emit(k3.variable_map())
    block = lines(block_clauses)
    block_sha = hashlib.sha256(block).hexdigest()
    if block_sha != BLOCK_SHA256 or len(block_clauses) != BLOCK_CLAUSES:
        raise SystemExit("cut block %s (%d clauses) differs from the pin" % (block_sha, len(block_clauses)))
    out = header(lex_nv, nc_in + len(block_clauses)) + body + block
    out_sha = hashlib.sha256(out).hexdigest()
    if out_sha != OUTPUT_SHA256 or (lex_nv, nc_in + len(block_clauses)) != OUTPUT_HEADER:
        raise SystemExit("strengthened output %s differs from the pin" % out_sha)
    info = {"cube": "C311", "encoder": "A", "kind": "lex C311 + AMENDMENT-4 cuts (route A)",
            "modules": {n: {"path": LANE_CODE + "/" + PINS[n][0], "sha256": m[1], "bytes": m[2]}
                        for n, m in mods.items()},
            "gram_enc_build": {"call": "build(3, None, True, True, None)", "seconds": enc_seconds,
                               "map_equals_wrapper_map": True},
            "coverage": {"status": cov["status"], "n_valid": cov["n_valid"],
                         "complete_disjoint_cover": cov["complete_disjoint_cover"]},
            "vmap_entries": len(vmap),
            "base_cnf_sha256": BASE_SHA256, "base_header": [nv, nbase], "base_empty_clause_lines": empty_clause_lines,
            "support_sets": [sorted(S) for S in k3.CUBES["C311"]], "cube_unit_clauses": units,
            "same_ray_identities": json.loads(json.dumps(twins)), "extra_clauses": len(cube),
            "source_cube_sha256": source_sha,
            "lex_generators": json.loads(json.dumps(per_gen)), "lex_clauses": len(lex_cl),
            "lex_auxiliaries": lex_nv - nv,
            "input_sha256": input_sha, "input_header": [lex_nv, nc_in],
            "block_sha256": block_sha, "block_clauses": len(block_clauses), "block_bytes": len(block),
            "out_header": [lex_nv, nc_in + len(block_clauses)], "out_bytes": len(out), "out_sha256": out_sha,
            "python": sys.version.split()[0], "python_executable": sys.executable,
            "ru_maxrss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "seconds": round(time.monotonic() - t0, 3)}
    sys.stdout.buffer.write(out)
    sys.stdout.buffer.flush()
    sys.stderr.write(json.dumps(info, sort_keys=True) + "\n")
    sys.stderr.flush()


if __name__ == "__main__":
    main()
