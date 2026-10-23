#!/usr/bin/env python3
"""PA19 96h lane probe 3: re-derive exact independent-encoder CNF digests for the pilot items.

Items: ms09 b70 [0..24], ms09 b5 [200..299], ms09 b5 [300..350]. Unchanged encoder
encode_skel_b.py (SHA d0002e60...) is vendored into LANE/code/vendor by exclusive creation from
SHA-verified old bytes (no link to the old inode) and imported from there with -B (no bytecode).
Inputs (skeleton list, placement lists, old pins) are regular files verified by SHA-256 before use.
Standard library only; only child processes are /bin/date clock reads; no solver/checker child.
No CNF bytes are written to disk: only digest/length/header/clause counts are recorded.
Admission (fail closed): fresh statvfs >= 12.2e9 + 16 MiB + vendored-copy bytes; no NEW-round
STOP/HALT marker in LANE/control or RUN/control; self wall budget 280 s checked between items.
Output: one exclusive-created JSON (argv[1]).
"""
import hashlib
import importlib.util
import json
import os
import re
import stat
import subprocess
import sys
import time

LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h"
OLD = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
FLOOR = 12_200_000_000 + 16 * 1024 * 1024 + 64 * 1024
BUDGET = 280.0
T0 = time.monotonic()
ENC_OLD = os.path.join(OLD, "src/encode_skel_b.py")
ENC_SHA = "d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5"
ENC_LANE = os.path.join(LANE, "code/vendor/encode_skel_b.py")
SKEL = ("cycle2/skel-b/skeletons-b-ms09.json", "7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0")
P0 = [4, 3, 3, 3, 3, 3]
ITEMS = [
    {"id": "b00070:00000-00024", "b": 70, "lo": 0, "hi": 24,
     "list": ("cycle2/m2part_drat/ms09_b00070/ext.json", "c91d656a6c62426752fc6b9683bd8d491031d75bfdb9d3940055ddd22b536c10"),
     "denominator": 25,
     "old_pin": ("cycle2/m2-kissat-strata-calibration-20261018T030136/calibration_ms09_b00070_00000_00024.cnf-pin.json",
                 "2adc75c090b2a2883be02c47cb5b9b6c909b0a76b1cffaf19f7b605d5cfb8def"),
     "expect": ("565dd02cf532cb6a58fb70935d8e74fa7bca8e15432ad800c5019eaf5c98ff2b", 9448478)},
    {"id": "b00005:00200-00299", "b": 5, "lo": 200, "hi": 299,
     "list": ("cycle2/m2part_drat/ms09_b00005/ext.json", "3f71e620c9efa7b3075f8579e357e5096f91282cf6434120706391bb8909fb00"),
     "denominator": 351,
     "old_pin": ("cycle2/m2part_drat/ms09_b00005/batch_00200_00299_k1_v6.cnf-pin.json",
                 "48efb529b0751e5ee28d11feec341f16192915bbbf7ed6085dfcf9a2dc4e397e"),
     "expect": ("952b8839f7daa66ba499ba0e523696562425cce047b845dbdaef87b8d696a642", 9482840)},
    {"id": "b00005:00300-00350", "b": 5, "lo": 300, "hi": 350,
     "list": ("cycle2/m2part_drat/ms09_b00005/ext.json", "3f71e620c9efa7b3075f8579e357e5096f91282cf6434120706391bb8909fb00"),
     "denominator": 351, "old_pin": None, "expect": None},
]
CONTROL_ITEM = {"id": "b00005:00000-00099 (positive control, v6 VALIDATED record)", "b": 5, "lo": 0, "hi": 99,
                "list": ITEMS[1]["list"], "denominator": 351, "old_pin": None,
                "expect": ("cb72114e3ec2fb4824c384c95c52fe5f8b2f43a69f82404aa7b246b1e7df6d01", 9482814)}


def host_clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True,
                          check=True, stdin=subprocess.DEVNULL).stdout.strip()


def free_bytes(path):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def new_round_markers():
    found = []
    for d in (os.path.join(LANE, "control"), os.path.join(RUN, "control")):
        for name in sorted(os.listdir(d)):
            if re.match(r"(?i)^(stop|halt)", name) or "HALT" in name:
                found.append(os.path.join(d, name))
    return found


def read_regular_pinned(path, expect):
    st = os.lstat(path)
    if not stat.S_ISREG(st.st_mode):
        raise SystemExit(f"REFUSED: not a regular file: {path}")
    with open(path, "rb") as f:
        raw = f.read()
    got = hashlib.sha256(raw).hexdigest()
    if expect is not None and got != expect:
        raise SystemExit(f"REFUSED: pin mismatch {path}: {got} != {expect}")
    return raw, got


def budget_left():
    return BUDGET - (time.monotonic() - T0)


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: probe_cnf_pins_v1.py OUTPUT.json")
    out_path = os.path.abspath(sys.argv[1])
    if not out_path.startswith(os.path.join(LANE, "evidence", "probes") + os.sep):
        raise SystemExit("REFUSED: output outside LANE/evidence/probes")
    started = host_clock()
    free0 = free_bytes(LANE)
    markers = new_round_markers()
    if free0 < FLOOR or markers:
        raise SystemExit(f"REFUSED: free={free0} floor={FLOOR} new_round_markers={markers}")
    with open(os.path.abspath(__file__), "rb") as f:
        self_sha = hashlib.sha256(f.read()).hexdigest()
    enc_raw, _ = read_regular_pinned(ENC_OLD, ENC_SHA)
    vendored = "existing"
    if not os.path.lexists(ENC_LANE):
        os.makedirs(os.path.dirname(ENC_LANE), exist_ok=True)
        with open(ENC_LANE, "xb") as f:
            f.write(enc_raw)
        vendored = "created_exclusive"
    lane_raw, lane_sha = read_regular_pinned(ENC_LANE, ENC_SHA)
    if os.lstat(ENC_LANE).st_ino == os.lstat(ENC_OLD).st_ino:
        raise SystemExit("REFUSED: vendored encoder shares the old inode")
    spec = importlib.util.spec_from_file_location("encode_skel_b_lane", ENC_LANE)
    ENC = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(ENC)
    skel_raw, skel_sha = read_regular_pinned(os.path.join(OLD, SKEL[0]), SKEL[1])
    D = json.loads(skel_raw)
    special = [p for p in D["profiles"] if list(p) != P0]
    if D["c0"] != 5 or len(special) != 3 or D["L"] != 0:
        raise SystemExit("REFUSED: unexpected ms09 skeleton header")
    results = []
    for it in [CONTROL_ITEM] + ITEMS:
        if budget_left() < 60:
            raise SystemExit("REFUSED: self wall budget exhausted before item " + it["id"] + "; no output written")
        lst_raw, lst_sha = read_regular_pinned(os.path.join(OLD, it["list"][0]), it["list"][1])
        E = json.loads(lst_raw)
        if not (E["num_placements"] == len(E["placements"]) == it["denominator"]):
            raise SystemExit("REFUSED: list denominator mismatch for " + it["id"])
        if not (0 <= it["lo"] <= it["hi"] < it["denominator"]):
            raise SystemExit("REFUSED: bad interval " + it["id"])
        old_pin = None
        if it["old_pin"]:
            pin_raw, pin_sha = read_regular_pinned(os.path.join(OLD, it["old_pin"][0]), it["old_pin"][1])
            pj = json.loads(pin_raw)
            old_pin = {"path": it["old_pin"][0], "sha256": pin_sha, "cnf_sha256": pj["cnf_sha256"],
                       "cnf_bytes": pj["cnf_bytes"]}
            if (pj["cnf_sha256"], pj["cnf_bytes"]) != it["expect"]:
                raise SystemExit("REFUSED: old pin content differs from frozen expectation " + it["id"])
        sk = D["skeletons"][it["b"]]
        t1 = time.monotonic()
        nv, cl = ENC.build_partbatch(D["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special,
                                     [E["placements"][i] for i in range(it["lo"], it["hi"] + 1)])
        cnf = ENC.cnf_bytes(nv, cl)
        dt = time.monotonic() - t1
        digest = hashlib.sha256(cnf).hexdigest()
        header = cnf.split(b"\n", 1)[0].decode()
        rec = {"id": it["id"], "b_index": it["b"], "indices": [it["lo"], it["hi"]],
               "placements_in_interval": it["hi"] - it["lo"] + 1, "list_path": it["list"][0],
               "list_sha256": lst_sha, "complete_denominator": E["num_placements"],
               "raw_class_assignments": E.get("raw_class_assignments"), "automorphisms": E.get("automorphisms"),
               "skeleton_types": sk["types"], "skeleton_empty": sk["empty"],
               "cnf_sha256": digest, "cnf_bytes": len(cnf), "header": header, "variables": nv,
               "clauses": len(cl), "empty_clauses_in_formula": sum(1 for c in cl if not c),
               "build_seconds": round(dt, 3), "old_pin": old_pin,
               "matches_frozen_expectation": (None if it["expect"] is None else (digest, len(cnf)) == it["expect"])}
        if it["expect"] is not None and not rec["matches_frozen_expectation"]:
            raise SystemExit("REFUSED: re-derived CNF digest mismatch for " + it["id"] + ": " + json.dumps(rec))
        results.append(rec)
        del cl, cnf
    result = {
        "schema": "PA19-96H-PROBE-CNF-PINS-v1",
        "started_host_clock": started, "finished_host_clock": host_clock(),
        "elapsed_seconds": round(time.monotonic() - T0, 3), "probe_sha256": self_sha,
        "admission": {"free_bytes_start": free0, "floor_bytes": FLOOR, "new_round_markers": markers,
                      "free_bytes_end": free_bytes(LANE)},
        "python": sys.version, "encoder": {"old_path": ENC_OLD, "lane_path": ENC_LANE, "sha256": lane_sha,
                                            "vendoring": vendored},
        "skeleton": {"path": SKEL[0], "sha256": skel_sha, "special_profiles": special},
        "construction": "ENC.build_partbatch(c0, [tuple(t) for t in sk['types']], sk['empty'], special, "
                        "[E['placements'][i] for i in range(lo, hi+1)]) then ENC.cnf_bytes, identical to the "
                        "old calibration/v6 call",
        "items": results,
        "not_done": "no CNF/proof written; no solver/checker child; no old file written",
    }
    data = json.dumps(result, indent=1, sort_keys=True).encode()
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data))


if __name__ == "__main__":
    main()
