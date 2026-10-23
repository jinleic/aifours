#!/usr/bin/env python3
"""Assemble RESULT.json for the parent K2 replay desk from bind, replay receipts and control receipts.

Usage: assemble.py BIND.json REPLAY_TAG CONTROL_TAG OUT.json [DEVIATIONS.json]
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import k2lib as K  # noqa: E402


def load(p):
    with open(p) as f:
        return json.load(f)


def checker_facts(path):
    with open(path, "rb") as f:
        b = f.read()
    m = re.search(rb"c parsing input formula with (\d+) variables and (\d+) clauses", b)
    m2 = re.search(rb"c finished parsing, read (\d+) bytes from proof file", b)
    return ([int(m.group(1)), int(m.group(2))] if m else None), (int(m2.group(1)) if m2 else None)


def checker_verdict(lines):
    for v in ("s VERIFIED", "s NOT VERIFIED", "s TIMEOUT", "s DERIVATION", "s MEMORY ALLOCATION ERROR"):
        if v in lines:
            return v[2:]
    return "NONE"


def row_from_receipt(p, enc, c, pr):
    r = load(p)
    pl = r.get("pipeline") or {}
    ch = pl.get("children", {})
    dims, pbytes = (checker_facts(os.path.join(K.DESK, pl["checker_log"])) if pl else (None, None))
    return {
        "class": c, "encoder": enc, "solver": "cadical 3.0.1" if enc == "A" else "kissat 4.0.4",
        "cnf_sha256": r["cnf_sha256"], "receipt_cnf_sha256": r["receipt_cnf_sha256"],
        "cnf_hash_match": r["cnf_hash_match"], "cnf_header": r.get("cnf_header"),
        "checker_parsed_dims": dims, "producer_checker_parsed_dims": pr["checker_parsed_dims"],
        "solver_rc": ch.get("solver", {}).get("rc"), "checker_rc": ch.get("checker", {}).get("rc"),
        "checker_status_lines": pl.get("checker_status_lines"),
        "checker_verdict": checker_verdict(pl.get("checker_status_lines", [])),
        "verdict": r["verdict"],
        "pipeline_seconds": pl.get("pipeline_seconds"),
        "solver_wall_seconds": ch.get("solver", {}).get("wall_seconds"),
        "checker_wall_seconds": ch.get("checker", {}).get("wall_seconds"),
        "solver_cpu_seconds": round(ch.get("solver", {}).get("user_seconds", 0)
                                    + ch.get("solver", {}).get("sys_seconds", 0), 3),
        "checker_cpu_seconds": round(ch.get("checker", {}).get("user_seconds", 0)
                                     + ch.get("checker", {}).get("sys_seconds", 0), 3),
        "encode_seconds": r["encoder_run"]["seconds"],
        "solver_maxrss_bytes": ch.get("solver", {}).get("maxrss_bytes"),
        "checker_maxrss_bytes": ch.get("checker", {}).get("maxrss_bytes"),
        "peak_sampled_aggregate_rss_bytes": pl.get("peak_sampled_aggregate_rss_bytes"),
        "safety_stop_reason": pl.get("safety_stop_reason"),
        "proof_bytes_read_by_checker": pbytes, "producer_proof_bytes_read": pr["checker_read_proof_bytes"],
        "producer_seconds": pr["seconds"],
        "lane_other_busy_at_launch": (r.get("capacity") or {}).get("lane_other_busy"),
        "free_bytes_at_launch": (r.get("capacity") or {}).get("free_bytes"),
        "solver_log_sha256": pl.get("solver_log_sha256"), "checker_log_sha256": pl.get("checker_log_sha256"),
        "started_at": pl.get("started_at"), "finished_at": pl.get("finished_at"),
        "receipt": os.path.relpath(p, K.DESK), "receipt_sha256": K.sha_file(p)}


def main(bind_path, rtags, ctag, out, extra_dev=None, provenance=None, prev_result=None):
    bind = load(bind_path)
    tags = rtags.split(",")
    prod = {e: {r["class"]: r for r in bind["inventories"][e]["rows"]} for e in ("A", "B")}
    rows, totals, superseded = [], {}, []
    deferred = {}
    for t in tags:
        sp = os.path.join(K.DESK, "replay-summary-%s.json" % t)
        if os.path.exists(sp):
            for d in load(sp).get("deferred", []):
                deferred[(d["encoder"], d["class"])] = dict(d, tag=t)
    for enc in ("A", "B"):
        for c in range(147):
            attempts = []
            for t in tags:
                p = os.path.join(K.DESK, "receipts", "%s-k2%s_%d.json" % (t, enc, c))
                if os.path.exists(p):
                    attempts.append(row_from_receipt(p, enc, c, prod[enc][c]))
            if not attempts:
                d = deferred.get((enc, c), {})
                rows.append({"class": c, "encoder": enc, "verdict": "UNKNOWN",
                             "receipt_cnf_sha256": prod[enc][c]["receipt_cnf_sha256"],
                             "cnf_hash_match": d.get("cnf_hash_match"),
                             "deferred": d.get("deferred", "not run"), "deferred_in_run": d.get("tag"),
                             "deferred_at": (d.get("capacity") or {}).get("at"),
                             "note": ("solve+check held deferred per parent instruction; exact remaining "
                                      "class/CNF hash/commands in checkpoints/remaining-index-v1.json")})
                continue
            final = dict(attempts[-1])
            final["attempts"] = [{k: a[k] for k in ("receipt", "verdict", "solver_rc", "checker_rc",
                                                     "checker_verdict", "safety_stop_reason", "pipeline_seconds")}
                                 for a in attempts]
            superseded += [a for a in attempts[:-1]]
            if (enc, c) in deferred:
                d = deferred[(enc, c)]
                final["prior_deferral"] = {"run": d["tag"], "reason": d["deferred"],
                                           "at": (d.get("capacity") or {}).get("at"),
                                           "cnf_hash_match_at_deferral": d.get("cnf_hash_match")}
            rows.append(final)
    for enc in ("A", "B"):
        rr = [x for x in rows if x["encoder"] == enc]
        ran = [x for x in rr if x.get("pipeline_seconds") is not None]
        totals[enc] = {
            "instances": len(rr), "PASS": sum(x["verdict"] == "PASS" for x in rr),
            "FAIL": sum(x["verdict"] == "FAIL" for x in rr), "UNKNOWN": sum(x["verdict"] == "UNKNOWN" for x in rr),
            "cnf_hash_matches": sum(bool(x.get("cnf_hash_match")) for x in rr),
            "pipeline_seconds_total": round(sum(x["pipeline_seconds"] for x in ran), 3),
            "encode_seconds_total": round(sum(x["encode_seconds"] for x in ran), 3),
            "max_pipeline_seconds": max((x["pipeline_seconds"] for x in ran), default=None),
            "max_solver_maxrss_bytes": max((x["solver_maxrss_bytes"] for x in ran), default=None),
            "max_checker_maxrss_bytes": max((x["checker_maxrss_bytes"] for x in ran), default=None),
            "max_peak_sampled_aggregate_rss_bytes": max((x["peak_sampled_aggregate_rss_bytes"] for x in ran),
                                                       default=None),
            "proof_length_equal_to_producer": sum(x.get("proof_bytes_read_by_checker") is not None and
                                                  x["proof_bytes_read_by_checker"] == x["producer_proof_bytes_read"]
                                                  for x in rr),
            "checker_dims_equal_to_producer": sum(x.get("checker_parsed_dims") is not None and
                                                  x["checker_parsed_dims"] == x["producer_checker_parsed_dims"]
                                                  for x in rr)}
    totals["all"] = {k: sum(totals[e][k] for e in ("A", "B")) for k in ("instances", "PASS", "FAIL", "UNKNOWN",
                                                                      "cnf_hash_matches")}
    controls = {}
    for p in sorted(glob.glob(os.path.join(K.DESK, "controls", ctag + "-*.json"))):
        c = load(p)
        name = os.path.basename(p)[len(ctag) + 1:-5]
        keep = {k: c.get(k) for k in ("outcome", "expectation", "matches_expectation", "cnf_sha256",
                                      "checker_cnf_sha256", "checker_status_lines", "checker_verified",
                                      "safety_stop_reason", "pipeline_seconds", "cnf_text", "proof_hex",
                                      "structure", "numbering", "mutation", "note") if k in c}
        keep["children"] = c.get("children")
        if "model" in c:
            m = dict(c["model"])
            m.pop("bitmask_hex_var1_lsb", None)
            sem = m.get("semantic_parent_numbering", {})
            m["semantic_parent_numbering"] = {k: ({kk: vv for kk, vv in v.items() if kk != "edges"}
                                                  if isinstance(v, dict) else v) for k, v in sem.items()}
            keep["model_summary"] = m
            keep["model_full_record"] = os.path.relpath(p, K.DESK) + " :: model.bitmask_hex_var1_lsb"
        keep["receipt"] = os.path.relpath(p, K.DESK)
        keep["receipt_sha256"] = K.sha_file(p)
        controls[name] = keep
    runs = {}
    for t in tags:
        sp = os.path.join(K.DESK, "replay-summary-%s.json" % t)
        stp = os.path.join(K.DESK, "replay-stop-%s.json" % t)
        bsp = os.path.join(K.DESK, "boundary-stop-%s.json" % t)
        rec = {}
        if os.path.exists(sp):
            s = load(sp)
            rec["summary"] = {k: s[k] for k in ("started_at", "finished_at", "classes", "encoders", "stopped",
                                                "verdicts", "pins_unchanged", "script_sha256", "deferred")}
            rec["pins_start"], rec["pins_end"] = s["pins_start"], s["pins_end"]
            rec["summary_file"], rec["summary_sha256"] = os.path.relpath(sp, K.DESK), K.sha_file(sp)
        for key, path in (("stop_note", stp), ("boundary_stop", bsp)):
            if os.path.exists(path):
                rec[key] = load(path)
                rec[key + "_sha256"] = K.sha_file(path)
        runs[t] = rec
    pins_now = {p: K.sha_file(p) for p in K.PINS}
    deviations = list(bind["deviations"])
    if extra_dev:
        deviations += load(extra_dev)
    for x in rows:
        if x["verdict"] != "PASS":
            deviations.append("instance k2%s_%d final verdict %s" % (x["encoder"], x["class"], x["verdict"]))
    for a in superseded:
        deviations.append("superseded attempt %s: %s (%s)" % (a["receipt"], a["verdict"], a["safety_stop_reason"]))
    if pins_now != K.PINS:
        deviations.append("pins at assembly differ: %s" % {p: h for p, h in pins_now.items() if h != K.PINS[p]})
    scripts = {os.path.basename(p): K.sha_file(p) for p in sorted(glob.glob(os.path.join(K.DESK, "scripts", "*.py")))}
    written = 0
    for root, dirs, files in os.walk(K.DESK):
        for fn in files:
            st = os.lstat(os.path.join(root, fn))
            written += st.st_size
    res = {
        "desk": "review/moqls7-k2-parent-v1", "recorded_at": K.now(),
        "status": ("%d/%d instances PASS, %d FAIL, %d UNKNOWN (%s). Instance scope only; no whole-K2 or theorem "
                   "verdict." % (totals["all"]["PASS"], totals["all"]["instances"], totals["all"]["FAIL"],
                                 totals["all"]["UNKNOWN"],
                                 ", ".join("k2%s_%d: %s" % (x["encoder"], x["class"], x.get("deferred") or
                                                             x.get("safety_stop_reason") or x["verdict"])
                                           for x in rows if x["verdict"] != "PASS") or "none")),
        "scope": ("Parent replay of the phys-2 K2 r4 certificates: 147 classes x 2 encoders. Each CNF regenerated by "
                  "the pinned lane encoder (run as a subprocess, replay only), hashed and compared with the producer "
                  "receipt, solved with a native 900 s limit, binary DRAT streamed through a FIFO to the parent-built "
                  "drat-trim (-i, native -t 1800). Per-instance PASS/FAIL/UNKNOWN only. No theorem verdict: the "
                  "heavy/G4 bridge, G1-G5 encoder faithfulness and class coverage are reviewed separately."),
        "verdict_rule": ("PASS iff cnf_hash_match and solver rc 20 and checker rc 0 and an exact 's VERIFIED' line "
                         "(CR stripped) and no 's NOT VERIFIED'/'s TIMEOUT' and no safety stop; FAIL on hash mismatch, "
                         "solver rc 10, or rc 20 with a definitive 's NOT VERIFIED'; otherwise UNKNOWN (timeouts are "
                         "UNKNOWN)."),
        "pins": {"brief": bind["brief_pins"], "runtime_expected": {p: K.PINS[p] for p in K.PINS},
                 "at_assembly": pins_now, "at_assembly_all_match": pins_now == K.PINS,
                 "lane_current": bind["current_lane_pins"], "referenced_unhashed": bind["referenced_or_related_unhashed"]},
        "claim_binding": bind["claim"], "classfile": bind["classfile"],
        "receipt_audit": {e: {k: v for k, v in bind["inventories"][e].items() if k != "rows"} for e in ("A", "B")},
        "cert_r4_listing": bind["cert_r4_listing"], "producer_chronology": bind["chronology"],
        "unbound_claim_statements": bind["unbound_claim_statements"],
        "replay": {"tags": tags, "runs": runs, "instances": rows, "totals": totals,
                   "superseded_attempts": superseded},
        "controls": controls, "deviations": deviations,
        "unknowns": [{"instance": "k2%s_%d" % (x["encoder"], x["class"]), "reason": x.get("deferred") or
                      x.get("safety_stop_reason") or "see row", "note": x.get("note")}
                     for x in rows if x["verdict"] == "UNKNOWN"],
        "remaining_index": ({"path": "checkpoints/remaining-index-v1.json",
                             "sha256": K.sha_file(os.path.join(K.DESK, "checkpoints", "remaining-index-v1.json")),
                             "state": ("open" if any(x["verdict"] == "UNKNOWN" for x in rows) else
                                       "resolved: every instance it listed now has a final receipt")}
                            if os.path.exists(os.path.join(K.DESK, "checkpoints", "remaining-index-v1.json"))
                            else None),
        "scripts_sha256": scripts, "desk_bytes_on_disk_before_result": written}
    if provenance:
        res["script_provenance"] = load(provenance)
        res["script_provenance_file"] = {"path": os.path.relpath(os.path.abspath(provenance), K.DESK),
                                         "sha256": K.sha_file(provenance)}
    if prev_result:
        prev = load(prev_result)
        prev_pass = {(x["encoder"], x["class"]): x for x in prev["replay"]["instances"] if x["verdict"] == "PASS"}
        now_rows = {(x["encoder"], x["class"]): x for x in rows}
        changed = [("k2%s_%d" % k) for k, x in prev_pass.items()
                   if now_rows[k].get("receipt") != x["receipt"] or now_rows[k].get("receipt_sha256") != x["receipt_sha256"]
                   or now_rows[k]["verdict"] != "PASS"]
        newly = [("k2%s_%d" % k, x["verdict"], x.get("receipt")) for k, x in now_rows.items() if k not in prev_pass]
        res["supersedes"] = {"path": os.path.relpath(os.path.abspath(prev_result), K.DESK),
                             "sha256": K.sha_file(prev_result), "prior_pass_instances": len(prev_pass),
                             "prior_pass_receipts_rebound_unchanged": len(prev_pass) - len(changed),
                             "prior_pass_receipts_changed": changed, "instances_not_pass_in_prior": newly,
                             "note": "prior file preserved unchanged; this result rebinds its PASS receipts by "
                                     "path and SHA-256 and adds only the instances listed as not PASS there"}
    K.write_json_x(out, res)
    print(json.dumps({"totals": totals, "controls": {k: (v.get("outcome"), v.get("matches_expectation"))
                                                     for k, v in controls.items()},
                      "deviations": deviations}, indent=1))


if __name__ == "__main__":
    main(*sys.argv[1:])
