#!/usr/bin/env python3
"""Pin and bind the K2 r1 claim, the r4 inventories and all 294 producer receipts (parent code; no lane code run).

Usage: bind.py OUT.json
"""
import json
import os
import re
import stat
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import k2lib as K  # noqa: E402

LANE = K.LANE
CLAIM = os.path.join(LANE, "review", "K2-THEOREM.r1.md")
INV = {"A": os.path.join(LANE, "evidence", "gram", "k2A_cert_summary_r4.json"),
       "B": os.path.join(LANE, "evidence", "gram", "k2B_cert_summary_r4.json")}
# Each SHA printed in the claim, mapped to the file its sentence names.
CLAIM_HASH_TARGETS = {
    "898065c8a592a5a3ed1103a2657e3cff25f9588514ad3d286d441dedc95a8158": "evidence/ls7_main_classes.txt",
    "968ad4e574ed02800ac9f391aeb67e7709d328563112c0fe4febe30596058794": "code/ls_classes.c",
    "b2c206d8bf4896868fb4e45cd87c633a6cfbb0d62c8fdb62b146ac84a7d38833": "code/gram_enc.py",
    "c7583efe838816d39fe33456af09897cc2a1f5633d1e57e1ee63b3e5238e2b45": "code/gram_encB.py",
    "31aa7eb25bfb760c3b71af21698612ffc6ee8c877f0507d2dd7d3cfa462ddc29": "evidence/gram/k2A_cert_summary_r4.json",
    "ed29e3a199a650f11a10f98d0c262c5ebe4c905e68ce6de18adeee030fa20f4b": "evidence/gram/k2B_cert_summary_r4.json",
    "ec540a8700b7933b71605e7b03f86d5ef52ad258a5895d0b558db9819f0fa18a": "code/gram_certify_r4.py",
    "d834b649f437e091597f5347f259b9f681087f89ca0844d0cee250a1a1a0c2ee": "env/drat-trim/drat-trim.c",
    "a876bea8928d2ea6c62cd61b94d51dbd4c67670f8b779a17c49bb825c0049173": "evidence/gram/gram_controlsA_frozen.json",
    "6c15ef284c96e2a3b1cb880d1fa4b9ca2aae7d4e76999784616641eb1531a669": "evidence/gram/gram_controlsB_frozen.json",
}
# Worker-printed / task-brief pins (prefix...suffix where only that was given).
BRIEF = {
    "review/K2-THEOREM.r1.md": "e846e1d9e345db0630b4aeeee9722d47357daa07daa089b9ae5325c5e58ef05b",
    "evidence/gram/k2A_cert_summary_r4.json": "31aa7eb25bfb760c3b71af21698612ffc6ee8c877f0507d2dd7d3cfa462ddc29",
    "evidence/gram/k2B_cert_summary_r4.json": "ed29e3a199a650f11a10f98d0c262c5ebe4c905e68ce6de18adeee030fa20f4b",
    "code/gram_enc.py": ("b2c206d8", "8833"),
    "code/gram_encB.py": ("c7583efe", "2b45"),
    "evidence/ls7_main_classes.txt": ("898065c8", "8158"),
}
REFERENCED_UNHASHED = ["review/K1-THEOREM.r2.md", "review/GRAM-ENCODING.r1.md", "review/AMENDMENT-2.r1.md",
                       "code/gram_cert_summary.py", "code/k2_classes.py", "code/gram_certify_r2.py",
                       "code/gram_certify_r3.py", "code/gram_certify.py", "env/drat-trim/drat-trim",
                       "review/CERTIFY-DRIVER-DELTA.r2.json", "review/CERTIFY-DRIVER-DELTA.r3.json",
                       "review/CERTIFY-DRIVER-DELTA.r4.json", "review/K2-THEOREM.r2.md",
                       "review/K2-REVIEW-DELTA.r2.json", "evidence/LOG.md"]
EXPECTED_RECEIPT_KEYS = {"instance", "started_at", "finished_at", "seconds", "pins", "cnf_sha256", "solver_command",
                         "solver_rc", "checker_rc", "solver_log_sha256", "checker_log_sha256",
                         "checker_status_lines", "verified_unsat", "proof_storage",
                         "peak_sampled_aggregate_rss_bytes", "rss_sample_period_seconds",
                         "rss_abort_threshold_bytes", "safety_stop_reason", "solver_seconds", "checker_seconds"}


def lane(p):
    return os.path.join(LANE, p)


def main(out):
    res = {"recorded_at": K.now(), "lane": LANE, "deviations": []}
    dev = res["deviations"]
    # 1. brief pins
    pins = {}
    for rel, exp in BRIEF.items():
        h = K.sha_file(lane(rel))
        ok = (h == exp) if isinstance(exp, str) else (h.startswith(exp[0]) and h.endswith(exp[1]))
        pins[rel] = {"sha256": h, "expected": exp if isinstance(exp, str) else "%s...%s" % exp, "match": ok}
        if not ok:
            dev.append("brief pin mismatch: %s" % rel)
    res["brief_pins"] = pins
    # 2. claim document hashes
    with open(CLAIM, "rb") as f:
        claim = f.read()
    lines = claim.decode().split("\n")
    found = []
    for i, ln in enumerate(lines, 1):
        for m in re.finditer(r"[0-9a-f]{64}", ln):
            h = m.group(0)
            tgt = CLAIM_HASH_TARGETS.get(h)
            on_disk = K.sha_file(lane(tgt)) if tgt else None
            found.append({"lf_line": i, "sha256": h, "target": tgt, "on_disk_sha256": on_disk,
                          "match": on_disk == h})
            if on_disk != h:
                dev.append("claim hash at LF%d does not bind: %s" % (i, h))
    res["claim"] = {"path": "review/K2-THEOREM.r1.md", "sha256": K.sha_bytes(claim), "lf_lines": len(lines),
                    "hashes": found, "all_hashes_bind": all(x["match"] for x in found)}
    res["referenced_or_related_unhashed"] = {r: K.sha_file(lane(r)) for r in REFERENCED_UNHASHED}
    # 3. class file arithmetic (file-internal only; coverage is reviewed elsewhere)
    rows = K.read_classes()
    keys = [r[0] for r in rows]
    sizes = [int(r[1]) for r in rows]
    pars = [int(r[2]) for r in rows]
    for k in keys:
        K.decode_key(k)
    res["classfile"] = {"rows": len(rows), "distinct_keys": len(set(keys)), "all_keys_reduced_latin": True,
                        "size_equals_211680_over_par": all(s * p == 211680 for s, p in zip(sizes, pars)),
                        "sum_sizes": sum(sizes), "claim_sum": 16942080, "sum_matches_claim": sum(sizes) == 16942080}
    # 4. inventories + receipts
    cur = {"gram_enc.py": K.sha_file(lane("code/gram_enc.py")), "gram_encB.py": K.sha_file(lane("code/gram_encB.py")),
           "gram_certify_r4.py": K.sha_file(lane("code/gram_certify_r4.py")),
           "k2_classes.py": K.sha_file(lane("code/k2_classes.py")), "classfile": K.sha_file(K.CLASSFILE),
           "drat-trim": K.sha_file(lane("env/drat-trim/drat-trim")),
           "drat-trim.c": K.sha_file(lane("env/drat-trim/drat-trim.c"))}
    res["current_lane_pins"] = cur
    inv_out = {}
    intervals = []
    for enc, path in INV.items():
        with open(path) as f:
            inv = json.load(f)
        problems = []
        if inv["pins"] != cur:
            problems.append("inventory pins differ from current files")
        if inv["certificates"] != 147 or inv["expected_class_indices"] != [0, 146]:
            problems.append("inventory count/index header")
        classes = [r["class"] for r in inv["rows"]]
        if sorted(classes) != list(range(147)) or len(classes) != 147:
            problems.append("inventory rows do not cover 0..146 exactly once")
        tot, peak, per = 0.0, 0, []
        for r in inv["rows"]:
            c = r["class"]
            rp = os.path.join(K.CERT, "k2%s_%d.json" % (enc, c))
            with open(rp, "rb") as f:
                rb = f.read()
            rec = json.loads(rb)
            p = []
            if K.sha_bytes(rb) != r["receipt_sha256"] or r["receipt"] != "k2%s_%d.json" % (enc, c):
                p.append("receipt sha/name")
            if set(rec) != EXPECTED_RECEIPT_KEYS:
                p.append("receipt keys")
            if rec["instance"] != "k2%s:%d" % (enc, c):
                p.append("instance")
            if rec["pins"] != cur:
                p.append("pins")
            if rec["cnf_sha256"] != r["cnf_sha256"]:
                p.append("cnf sha vs inventory")
            if (rec["solver_rc"], rec["checker_rc"], rec["checker_status_lines"], rec["verified_unsat"],
                    rec["safety_stop_reason"]) != (20, 0, ["s VERIFIED"], True, None):
                p.append("result fields")
            if rec["solver_seconds"] != 1800 or rec["checker_seconds"] != 3600:
                p.append("caps")
            exp_cmd = (["cadical", "-q", "-t", "1800"] if enc == "A" else ["kissat", "-q", "-f", "--time=1800"])
            if (rec["solver_command"][:4] != exp_cmd
                    or rec["solver_command"][4] != lane("explore/scratch/cert_r4_current.cnf")
                    or rec["solver_command"][5] != "../evidence/gram/cert_r4/k2%s_%d.drat.fifo" % (enc, c)):
                p.append("solver command")
            for kind in ("solver", "checker"):
                lp = os.path.join(K.CERT, "k2%s_%d.%s.log" % (enc, c, kind))
                with open(lp, "rb") as f:
                    lb = f.read()
                if K.sha_bytes(lb) != rec["%s_log_sha256" % kind]:
                    p.append("%s log sha" % kind)
                if kind == "checker":
                    st = K.status_lines(lb)
                    if st != ["s VERIFIED"]:
                        p.append("checker log status %s" % st)
                    m = re.search(rb"c parsing input formula with (\d+) variables and (\d+) clauses", lb)
                    dims = [int(m.group(1)), int(m.group(2))] if m else None
                    m2 = re.search(rb"c finished parsing, read (\d+) bytes from proof file", lb)
                    proof_bytes = int(m2.group(1)) if m2 else None
                    core = re.findall(rb"c (\d+) of (\d+) (clauses|lemmas) in core", lb)
                else:
                    if lb != b"s UNSATISFIABLE\n":
                        p.append("solver log content %r" % lb[:60])
            if r["checker_log_sha256"] != rec["checker_log_sha256"]:
                p.append("inventory checker log sha")
            for k in ("seconds", "peak_sampled_aggregate_rss_bytes", "started_at", "finished_at"):
                if r[k] != rec[k]:
                    p.append("inventory %s" % k)
            fifo = os.path.join(K.CERT, "k2%s_%d.drat.fifo" % (enc, c))
            st = os.lstat(fifo)
            if not stat.S_ISFIFO(st.st_mode):
                p.append("fifo node is not a FIFO")
            tot += rec["seconds"]
            peak = max(peak, rec["peak_sampled_aggregate_rss_bytes"])
            intervals.append((rec["started_at"], rec["finished_at"], "k2%s_%d" % (enc, c)))
            per.append({"class": c, "receipt_cnf_sha256": rec["cnf_sha256"], "checker_parsed_dims": dims,
                        "checker_read_proof_bytes": proof_bytes,
                        "checker_core": [[int(a), int(b), t.decode()] for a, b, t in core],
                        "seconds": rec["seconds"], "problems": p})
            if p:
                problems.append("k2%s_%d: %s" % (enc, c, p))
        if round(tot, 3) != inv["total_native_pipeline_seconds"]:
            problems.append("total seconds %s vs %s" % (round(tot, 3), inv["total_native_pipeline_seconds"]))
        if peak != inv["max_sampled_aggregate_rss_bytes"]:
            problems.append("max rss")
        inv_out[enc] = {"inventory_sha256": K.sha_file(path), "status": inv["status"], "recorded_at": inv["recorded_at"],
                        "total_native_pipeline_seconds": inv["total_native_pipeline_seconds"],
                        "recomputed_total": round(tot, 3), "max_rss": inv["max_sampled_aggregate_rss_bytes"],
                        "summary_code_sha256": inv["summary_code_sha256"], "problems": problems, "rows": per}
        dev.extend("inventory %s: %s" % (enc, q) for q in problems)
    # proof files must not exist in cert_r4 (FIFO-only claim)
    names = os.listdir(K.CERT)
    extra = sorted(n for n in names if not re.fullmatch(r"k2[AB]_\d+\.(json|solver\.log|checker\.log|drat\.fifo)", n))
    res["cert_r4_listing"] = {"entries": len(names), "unexpected_entries": extra,
                              "regular_file_bytes_total": sum(os.lstat(os.path.join(K.CERT, n)).st_size
                                                              for n in names)}
    # chronology: the producer reused one scratch CNF path, so instance intervals must not overlap
    iv = sorted(intervals)
    overlaps = [(a[2], b[2]) for a, b in zip(iv, iv[1:]) if b[0] < a[1]]
    res["chronology"] = {"first_start": iv[0][0], "last_finish": iv[-1][1], "overlapping_neighbours": overlaps,
                         "note": "second-resolution ISO stamps; equal stamps are not counted as overlap"}
    if overlaps:
        dev.append("receipt intervals overlap: %s" % overlaps[:5])
    res["inventories"] = inv_out
    table = {}
    for enc, route in (("A", "A / CaDiCaL / drat-trim"), ("B", "B / kissat / drat-trim")):
        want = "| %s | 147 | %.3f s | %d bytes |" % (route, inv_out[enc]["total_native_pipeline_seconds"],
                                                    inv_out[enc]["max_rss"])
        hit = [i for i, ln in enumerate(lines, 1) if ln == want]
        table[enc] = {"expected_row": want, "lf_lines": hit, "match": len(hit) == 1}
        if len(hit) != 1:
            dev.append("claim table row for %s does not equal inventory values" % enc)
    res["claim"]["table_rows_bind_inventories"] = table
    res["unbound_claim_statements"] = [
        "LF63/LF67 name CaDiCaL 3.0.1 and kissat 4.0.4; the r4 receipts record only the bare commands "
        "'cadical'/'kissat' (no executable path, version or binary SHA).",
        "LF99-100 checker controls (contradictory unit accepted, satisfiable unit rejected) have no retained "
        "receipt in the inventories or cert_r4.",
        "LF70 'with no safety stop' and RSS figures are producer-sampled values; binding here is to the receipts only."]
    K.write_json_x(out, res)
    print(json.dumps({"deviations": dev, "claim_hashes_bind": res["claim"]["all_hashes_bind"],
                      "classfile": res["classfile"], "cert_r4": res["cert_r4_listing"],
                      "chronology": res["chronology"]}, indent=1))


if __name__ == "__main__":
    main(sys.argv[1])
