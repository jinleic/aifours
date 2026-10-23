#!/usr/bin/env python3
"""snapshot_inputs.py (moqls7-ls147-parent-v1): pin read-only inputs by SHA-256 before and after copying.

Every output is created exclusively (open(...,'x'), os.mkdir without exist_ok). Sources are never modified.
Expected hashes: the assignment (class file, amendment), GRAM-ENCODING.r1 pins (lane drivers, ls_classes.c),
RESULT.json -> receipt-route1.json -> route1 code/output/time/EW-text records (parent K1 check).
Usage: snapshot_inputs.py OUTDIR
"""
import hashlib
import json
import os
import sys
import time

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum"
PAR = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls7-k1-parent-check-v1"


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def read(path):
    with open(path, "rb") as f:
        return f.read()


def main():
    out = sys.argv[1]
    os.mkdir(os.path.join(out, "inputs"))
    os.mkdir(os.path.join(out, "inputs", "lane"))
    os.mkdir(os.path.join(out, "inputs", "parent-k1-route1"))
    result_json = read(os.path.join(PAR, "RESULT.json"))
    res = json.loads(result_json)
    receipt_expect = [r["sha256"] for r in res["receipts"] if r["path"] == "route1/receipt-route1.json"][0]
    receipt = json.loads(read(os.path.join(PAR, "route1", "receipt-route1.json")))
    rec_hash = {}
    for sect in ("code", "outputs"):
        for r in receipt[sect]:
            rec_hash[r["path"]] = r["sha256"]
    for run in receipt["runs"]:
        if "time_file" in run:
            rec_hash[run["time_file"]["path"]] = run["time_file"]["sha256"]
    rec_hash[receipt["EW_source"]["text"]["path"]] = receipt["EW_source"]["text"]["sha256"]

    # (source, dest-relative-to-inputs, expectation kind, expected value, expectation source)
    items = [
        (LANE + "/evidence/ls7_main_classes.txt", "lane/ls7_main_classes.txt", "full",
         "898065c8a592a5a3ed1103a2657e3cff25f9588514ad3d286d441dedc95a8158", "assignment"),
        (LANE + "/code/ls_classes.c", "lane/ls_classes.c", "full",
         "968ad4e574ed02800ac9f391aeb67e7709d328563112c0fe4febe30596058794", "GRAM-ENCODING.r1 pin"),
        (LANE + "/review/AMENDMENT-1.r1.md", "lane/AMENDMENT-1.r1.md", "full",
         "1e6a26ee0239c2fd9c303ffafcafc40b1543513342237aa9e0d7612f1c00297f", "assignment"),
        (LANE + "/review/GRAM-ENCODING.r1.md", "lane/GRAM-ENCODING.r1.md", "observed", None,
         "frozen 19:01:26 per lane LOG; no external pin"),
        (LANE + "/code/k2_classes.py", "lane/k2_classes.py", "prefix_suffix", ("b49099e4", "b891"),
         "GRAM-ENCODING.r1 pin"),
        (LANE + "/code/k2_classesB.py", "lane/k2_classesB.py", "prefix_suffix", ("1637c17f", "37bc"),
         "GRAM-ENCODING.r1 pin"),
        (LANE + "/code/gram_certify.py", "lane/gram_certify.py", "full",
         "8eba2bd38a62e43a4cd4eb28373883d4efcfd9f11cfef165ce5293e322c59778", "GRAM-ENCODING.r1 pin"),
        (LANE + "/README.md", "lane/README.md", "observed", None, "lane README (mutable status section)"),
        (LANE + "/evidence/LOG.md", "lane/LOG.md", "observed", None, "lane LOG (append-only by lane)"),
        (PAR + "/RESULT.json", "parent-k1-route1/RESULT.json", "observed", None, "parent K1 check summary"),
        (PAR + "/route1/receipt-route1.json", "parent-k1-route1/receipt-route1.json", "full", receipt_expect,
         "RESULT.json receipts[route1]"),
        (PAR + "/route1/full_run.out", "parent-k1-route1/full_run.out", "full", rec_hash["route1/full_run.out"],
         "receipt-route1.json outputs"),
        (PAR + "/route1/full_run.time.txt", "parent-k1-route1/full_run.time.txt", "full",
         rec_hash["route1/full_run.time.txt"], "receipt-route1.json runs[full classification].time_file"),
        (PAR + "/route1/c/k1par_nets_v2.c", "parent-k1-route1/k1par_nets_v2.c", "full",
         rec_hash["route1/c/k1par_nets_v2.c"], "receipt-route1.json code"),
        (PAR + "/route1/ew/1406.3681v2.parent.layout.txt", "parent-k1-route1/1406.3681v2.parent.layout.txt", "full",
         rec_hash["route1/ew/1406.3681v2.parent.layout.txt"], "receipt-route1.json EW_source.text"),
    ]
    hash_only = [
        (PAR + "/route1/c/k1par_nets_v2", "full", rec_hash["route1/c/k1par_nets_v2"], "receipt-route1.json code"),
        (PAR + "/route1/c/nets7.txt", "full", rec_hash["route1/c/nets7.txt"], "receipt-route1.json code"),
    ]
    manifest = {"created": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "copies": [], "hash_only": [], "all_ok": True,
                "result_json_sha256_observed": sha_bytes(result_json)}
    for src, dst, kind, exp, why in items:
        before = read(src)
        h0 = sha_bytes(before)
        if kind == "full":
            ok = h0 == exp
        elif kind == "prefix_suffix":
            ok = h0.startswith(exp[0]) and h0.endswith(exp[1])
        else:
            ok = True
        dpath = os.path.join(out, "inputs", dst)
        with open(dpath, "xb") as f:
            f.write(before)
        h_copy = sha_bytes(read(dpath))
        h_after = sha_bytes(read(src))
        ent = {"source": src, "copy": "inputs/" + dst, "bytes": len(before), "sha256_source_before": h0,
               "sha256_copy": h_copy, "sha256_source_after": h_after, "expect_kind": kind,
               "expected": exp if not isinstance(exp, tuple) else "%s...%s" % exp, "expected_from": why,
               "match_expected": ok, "copy_identical": h_copy == h0 == h_after}
        manifest["copies"].append(ent)
        manifest["all_ok"] &= ok and ent["copy_identical"]
    for src, kind, exp, why in hash_only:
        h = sha_bytes(read(src))
        ent = {"source": src, "sha256": h, "expected": exp, "expected_from": why, "match_expected": h == exp}
        manifest["hash_only"].append(ent)
        manifest["all_ok"] &= ent["match_expected"]
    with open(os.path.join(out, "inputs", "MANIFEST.json"), "x") as f:
        json.dump(manifest, f, indent=1)
        f.write("\n")
    print(json.dumps({"all_ok": manifest["all_ok"], "copies": len(items), "hash_only": len(hash_only)}))
    return 0 if manifest["all_ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
