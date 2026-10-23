#!/usr/bin/env python3
"""bmap_oracle_r1.py: runtime oracle that encoder B's g-variable indices equal encoder A's map.

Parent requirement (2026-10-18 00:46 PDT): no B-route K3 certificate may be relied on until a runtime oracle
shows that encoder B's variables 1..2646 coincide with encoder A's vmap. Both encoders are unchanged and are run
with the K3 production arguments (3 squares, heavy, sym).

Method, using only B's own --fix-json branch:
  * base run of gram_encB.py --squares 3 --heavy --sym, read from its stdout pipe;
  * 12 binary designs. In design b, pair (a,p,q) is marked nonzero iff bit b of A's index of (a,p,q) is 1.
    B appends exactly one unit clause per g variable after its base clauses. The sign of the unit on B-variable
    v is therefore bit b of the A-index of the pair that B itself attached to v;
  * two sign controls: every pair marked nonzero (all units must be positive) and none (all negative).
PASS iff every design reproduces the base clause bytes as an exact prefix, appends exactly 2646 unit clauses
covering 1..2646 once each, the sign controls behave, and the decoded code of every B-variable v equals v.
It also checks A's map against the cube wrapper's independently written map, and the B base bytes against the
base hash recorded in both B cube metadata files. Decode-level comparator controls show the check is not vacuous.
No CNF is written: B output is captured from its stdout pipe and each design is passed on stdin.
Usage: bmap_oracle_r1.py OUT.json
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

import gram_enc
import k3_cubes

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
ENC_B = os.path.join(HERE, "gram_encB.py")
NG = 2646
BITS = 12
GROWTH = 1048576
GATE = 12200000000


def sha_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def run_b(fix):
    cmd = ["/usr/bin/python3", "-B", ENC_B, "--squares", "3", "--heavy", "--sym", "--out", "/dev/stdout"]
    if fix is None:
        r = subprocess.run(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        r = subprocess.run(cmd + ["--fix-json", "/dev/stdin"], input=json.dumps(fix).encode(),
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode != 0:
        raise RuntimeError("encoder B failed: rc %d: %s" % (r.returncode, r.stderr[-400:]))
    lines = r.stdout.splitlines(keepends=True)
    tag, form, nv, nc = lines[0].decode().split()
    nv, nc = int(nv), int(nc)
    if (tag, form) != ("p", "cnf") or len(lines) != nc + 2 or not lines[-1].startswith(b"vars "):
        raise RuntimeError("unexpected encoder B output layout")
    return lines[0], lines[1:nc + 1], nv, nc


def main(out):
    if os.path.exists(out):
        raise FileExistsError(out)
    t0 = time.monotonic()
    st = os.statvfs(LANE)
    available = st.f_bavail * st.f_frsize
    gate = {"at": now(), "available_bytes": available, "threshold_bytes": GATE,
            "projected_retained_growth_bytes": GROWTH}
    if available < GATE + GROWTH:
        gate["status"] = "UNKNOWN / DEFERRED_RESOURCE; oracle not run"
        with open(out, "x") as f:
            json.dump({"status": "DEFERRED", "gate": gate}, f, indent=2)
            f.write("\n")
        print(json.dumps(gate))
        return
    gate["status"] = "PASS"
    failures = []
    record = {"started_at": now(), "gate": gate, "oracle_sha256": sha_file(os.path.abspath(__file__)),
              "encoder_A_sha256": sha_file(os.path.join(HERE, "gram_enc.py")),
              "encoder_B_sha256": sha_file(ENC_B),
              "cube_wrapper_sha256": sha_file(os.path.join(HERE, "k3_cubes.py")),
              "production_arguments": ["--squares", "3", "--heavy", "--sym"], "designs": []}

    F, amap_str = gram_enc.build(3, None, True, True, None)
    record["A_header"] = {"variables": F.nv, "clauses": len(F.cl)}
    del F
    amap = {}
    for key, v in amap_str.items():
        a, p, q = key.split("|")
        amap[(int(a), tuple(map(int, p.split(","))), tuple(map(int, q.split(","))))] = v
    if sorted(amap.values()) != list(range(1, NG + 1)):
        failures.append("A map values are not exactly 1..2646")
    if k3_cubes.variable_map() != amap:
        failures.append("A map differs from the cube wrapper's independently written map")
    record["A_map_equals_wrapper_map"] = k3_cubes.variable_map() == amap

    head, body, nv0, nc0 = run_b(None)
    base_hash = hashlib.sha256(head)
    body_hash = hashlib.sha256()
    for line in body:
        base_hash.update(line)
        body_hash.update(line)
    del body
    record["B_base"] = {"variables": nv0, "clauses": nc0, "sha256": base_hash.hexdigest()}
    meta_bindings = {}
    for cube in ("C321", "C411"):
        meta = os.path.join(LANE, "explore", "k3cubes", "B_" + cube + ".meta.json")
        with open(meta) as f:
            recorded = json.load(f)["base_cnf_sha256"]
        meta_bindings[cube] = {"metadata_sha256": sha_file(meta), "recorded_base_sha256": recorded,
                               "equal": recorded == base_hash.hexdigest()}
        if recorded != base_hash.hexdigest():
            failures.append("B base bytes differ from %s metadata" % cube)
    record["B_cube_metadata_bindings"] = meta_bindings

    def fix_for(predicate):
        fix = {"g1": [], "g2": [], "g3": []}
        for (a, p, q), v in sorted(amap.items(), key=lambda item: item[1]):
            if predicate(v):
                fix["g%d" % a].append([list(p), list(q)])
        return fix

    def design(name, predicate):
        fix = fix_for(predicate)
        _, dbody, nv, nc = run_b(fix)
        info = {"design": name, "marked_nonzero": sum(len(x) for x in fix.values()),
                "variables": nv, "clauses": nc}
        if nv != nv0 or nc != nc0 + NG:
            failures.append("%s: header %d/%d, expected %d/%d" % (name, nv, nc, nv0, nc0 + NG))
        prefix = hashlib.sha256()
        for line in dbody[:nc0]:
            prefix.update(line)
        info["base_prefix_identical"] = prefix.hexdigest() == body_hash.hexdigest()
        if not info["base_prefix_identical"]:
            failures.append("%s: base clauses are not an exact prefix" % name)
        units = {}
        for line in dbody[nc0:]:
            toks = line.split()
            if len(toks) != 2 or toks[1] != b"0":
                failures.append("%s: non-unit appended clause" % name)
                continue
            lit = int(toks[0])
            if not 1 <= abs(lit) <= NG or abs(lit) in units:
                failures.append("%s: unit outside 1..2646 or repeated" % name)
                continue
            units[abs(lit)] = lit > 0
        if len(units) != NG:
            failures.append("%s: %d distinct units, expected %d" % (name, len(units), NG))
        info["positive_units"] = sum(units.values())
        record["designs"].append(info)
        return units

    codes = {v: 0 for v in range(1, NG + 1)}
    for b in range(BITS):
        units = design("bit%d" % b, lambda v, b=b: (v >> b) & 1)
        for v, positive in units.items():
            if positive:
                codes[v] |= 1 << b
    if not all(design("all_nonzero", lambda v: True).values()):
        failures.append("all-nonzero sign control produced a negative unit")
    if any(design("all_zero", lambda v: False).values()):
        failures.append("all-zero sign control produced a positive unit")
    mismatches = [v for v in range(1, NG + 1) if codes[v] != v]
    record["decoded_identity_mismatches"] = len(mismatches)
    record["first_mismatches"] = [[v, codes[v]] for v in mismatches[:20]]
    if mismatches:
        failures.append("%d B variables decode to a different A index" % len(mismatches))

    swapped = dict(codes)
    swapped[1], swapped[NG] = swapped[NG], swapped[1]
    flipped = dict(codes)
    flipped[1000] ^= 1 << 5
    record["comparator_controls"] = {
        "swap_1_and_2646_detected_exactly": [v for v in range(1, NG + 1) if swapped[v] != v] == [1, NG],
        "bit5_flip_of_var1000_detected_exactly": [v for v in range(1, NG + 1) if flipped[v] != v] == [1000],
        "scope": "decode-level self-tests of the comparison only; not mutations of encoder B"}
    if not all(v for k, v in record["comparator_controls"].items() if k != "scope"):
        failures.append("comparator self-test failed")

    record.update({"status": "PASS" if not failures else "FAIL", "failures": failures,
                   "finished_at": now(), "seconds": round(time.monotonic() - t0, 3),
                   "no_CNF_written": True, "designs_on_stdin": True,
                   "claim": ("Encoder B (unchanged bytes) attaches to each variable 1..2646 exactly the pair that "
                             "encoder A and the cube wrapper attach to it, under the K3 production arguments")})
    with open(out, "x") as f:
        json.dump(record, f, indent=2)
        f.write("\n")
    print(json.dumps({k: record[k] for k in ("status", "decoded_identity_mismatches", "seconds")}))
    print("receipt_sha256", sha_file(out))


if __name__ == "__main__":
    OUT = sys.argv[1]
    try:
        main(OUT)
    except Exception as exc:
        if not os.path.exists(OUT):
            with open(OUT, "x") as f:
                json.dump({"status": "FAIL", "failures": ["exception: %r" % (exc,)], "finished_at": now(),
                           "oracle_sha256": sha_file(os.path.abspath(__file__))}, f, indent=2)
                f.write("\n")
        raise
