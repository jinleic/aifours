#!/usr/bin/env python3
"""Certify an existing K3 cube after exact in-memory regeneration, without copying CNFs.

Parent disk steering: no proof files or duplicate CNF copies. Regenerate the
frozen encoder's bytes in memory, append the frozen cube schema, compare SHA to
the single search input, then stream proof against that input. New output is
logs/checkpoints/one receipt only. Native solver/checker caps each3600 seconds.
Usage: k3_cube_certify_r3.py A|B C311|C321|C411 OUTDIR SCREEN_RECEIPT
       k3_cube_certify_r3.py A|B C311|C321|C411 --regenerate-only
"""
import argparse
import hashlib
import json
import os
import subprocess

import gram_enc
import k3_cubes
from gram_certify_r4 import sha
from proof_stream import run_pair

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)



def regeneration(encoder, cube):
    directory = os.path.join(LANE, "explore", "k3cubes")
    cnf = os.path.join(directory, encoder + "_" + cube + ".cnf")
    meta_path = cnf[:-4] + ".meta.json"
    with open(meta_path) as f:
        binding = json.load(f)
    source = "gram_enc.py" if encoder == "A" else "gram_encB.py"
    assert sha(os.path.join(HERE, source)) == binding["base_encoder_sha256"]
    assert sha(os.path.join(HERE, "k3_cubes.py")) == binding["wrapper_sha256"]
    vmap = k3_cubes.variable_map()
    extra, _, _ = k3_cubes.cube_clauses(vmap, cube)
    base_hash, cube_hash = hashlib.sha256(), hashlib.sha256()
    if encoder == "A":
        F, actual_map = gram_enc.build(3, None, True, True, None)
        expected_map = {"%d|%d,%d|%d,%d" % (a, p[0], p[1], q[0], q[1]): v
                        for (a, p, q), v in vmap.items()}
        assert actual_map == expected_map
        base_hash.update(("p cnf %d %d\n" % (F.nv, len(F.cl))).encode())
        cube_hash.update(("p cnf %d %d\n" % (F.nv, len(F.cl) + len(extra))).encode())
        for cl in F.cl:
            line = (" ".join(map(str, cl)) + " 0\n").encode()
            base_hash.update(line)
            cube_hash.update(line)
    else:
        # Python's output file is the existing stdout pipe, not a retained file.
        # The final stats line is separate from exactly nc DIMACS clause lines.
        command = ["/usr/bin/python3", "-B", os.path.join(HERE, "gram_encB.py"),
                   "--squares", "3", "--heavy", "--sym", "--out", "/dev/stdout"]
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        lines = result.stdout.splitlines(keepends=True)
        tag, form, nv, nc = lines[0].decode().split()
        assert (tag, form) == ("p", "cnf")
        nc = int(nc)
        assert len(lines) == nc + 2 and lines[-1].startswith(b"vars ")
        base_hash.update(lines[0])
        cube_hash.update(("p cnf %s %d\n" % (nv, nc + len(extra))).encode())
        for line in lines[1:nc + 1]:
            base_hash.update(line)
            cube_hash.update(line)
    for cl in extra:
        cube_hash.update((" ".join(map(str, cl)) + " 0\n").encode())
    assert base_hash.hexdigest() == binding["base_cnf_sha256"]
    expected = binding["cnf_sha256"]
    assert cube_hash.hexdigest() == expected == sha(cnf)
    return cnf, {"regenerated_cnf_sha256": expected, "base_cnf_sha256": base_hash.hexdigest(),
                 "existing_metadata_sha256": sha(meta_path), "source_encoder_sha256": binding["base_encoder_sha256"],
                 "regeneration_code_sha256": sha(__file__), "no_duplicate_CNF_written": True}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("encoder", choices=("A", "B"))
    ap.add_argument("cube", choices=tuple(k3_cubes.CUBES))
    ap.add_argument("outdir", nargs="?")
    ap.add_argument("screen", nargs="?")
    ap.add_argument("--regenerate-only", action="store_true")
    a = ap.parse_args()
    st = os.statvfs(LANE)
    if st.f_bavail * st.f_frsize - 10485760 < 12000000000:
        raise RuntimeError("Floor plus projected10MiB retained-growth reserve unavailable; do not launch")
    cnf, regen = regeneration(a.encoder, a.cube)
    if a.regenerate_only:
        print(json.dumps({"encoder": a.encoder, "cube": a.cube, "status": "PASS", **regen}))
        return
    if not a.outdir or not a.screen:
        raise ValueError("OUTDIR and SCREEN_RECEIPT required for certification")
    with open(a.screen) as f:
        screen = json.load(f)
    assert screen["encoder"] == a.encoder and screen["cube"] == a.cube
    assert screen["status"] == "UNSAT exploratory" and screen["solver_rc"] == 20
    assert screen["safety_stop_reason"] is None and screen["cnf_sha256"] == regen["regenerated_cnf_sha256"]
    controls = {}
    for label, rel in (("component_controls", "evidence/gram/review_controls_r1/summary.json"),
                       ("transport_controls", "evidence/gram/transport_controls_r2/summary.json")):
        path = os.path.join(LANE, rel)
        with open(path) as f:
            assert json.load(f)["status"] == "PASS"
        controls[label] = sha(path)
    os.makedirs(a.outdir, exist_ok=True)
    prefix = os.path.join(a.outdir, a.encoder + "_" + a.cube)
    receipt = prefix + ".json"
    if os.path.exists(receipt):
        raise FileExistsError(receipt)
    command = (["cadical", "-q", "-t", "3600", cnf] if a.encoder == "A"
               else ["kissat", "-q", "-f", "--time=3600", cnf])
    result = run_pair(cnf, command, prefix, 3600, 3600)
    result.update({"encoder": a.encoder, "cube": a.cube, "regeneration": regen, "controls": controls,
                   "screen_sha256": sha(a.screen), "planned_new_retained_bytes": 10485760})
    result["verified_unsat"] = result["verified_unsat"] and result["cnf_sha256"] == regen["regenerated_cnf_sha256"]
    with open(receipt, "x") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps({k: result[k] for k in ("encoder", "cube", "verified_unsat", "seconds")}))
    if not result["verified_unsat"]:
        raise SystemExit("Cube not certified; no exclusion claimed")


if __name__ == "__main__":
    main()
