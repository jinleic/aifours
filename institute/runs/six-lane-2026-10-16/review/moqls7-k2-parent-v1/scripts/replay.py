#!/usr/bin/env python3
"""Parent replay of the phys-2 K2 r4 certificates (review/moqls7-k2-parent-v1).

For each requested (encoder, class): decode the class key (parent code), regenerate the CNF by running the
pinned lane encoder as a subprocess (A: gram_enc.build(2, L, True, False, None); B: gram_encB.py --squares 2
--net-L L --heavy), hash it and compare with the producer receipt, then solve with a native 900 s limit
(A: CaDiCaL 3.0.1, B: kissat 4.0.4) streaming the binary DRAT proof to the parent drat-trim (-i, -t 1800).
Before every launch: fresh free-space check (>= 12.2e9 per the parent's 23:17 rule, else the run stops and the
rest is recorded as deferred) and lane capacity (wait, 60 s polls). CNFs and proofs never touch disk.
SIGTERM to this driver stops it gracefully at the next instance boundary.

Usage: replay.py TAG ENC[,ENC] CLASSSPEC        (CLASSSPEC like 0-146 or 34,36-146)
"""
import json
import os
import signal
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import k2lib as K  # noqa: E402

SOLVER = {"A": "cadical", "B": "kissat"}


def log(msg):
    print("[%s] %s" % (K.now(), msg), flush=True)


def verdict(match, rec):
    if rec is None:
        return "UNKNOWN"
    s = rec["children"].get("solver", {}).get("rc")
    c = rec["children"].get("checker", {}).get("rc")
    lines = rec["checker_status_lines"]
    if rec["safety_stop_reason"]:
        return "UNKNOWN"
    if (match and s == 20 and c == 0 and "s VERIFIED" in lines and "s NOT VERIFIED" not in lines
            and "s TIMEOUT" not in lines):
        return "PASS"
    if not match or s == 10:
        return "FAIL"
    if s == 20 and "s NOT VERIFIED" in lines and "s TIMEOUT" not in lines:
        return "FAIL"
    return "UNKNOWN"


STOP = {"requested": None}


def _on_term(signum, frame):
    # graceful stop: finish the in-flight instance and its receipt, then write the summary
    STOP["requested"] = "SIGTERM received at %s; stopped at the next instance boundary" % K.now()


def parse_spec(spec):
    out = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    if any(c < 0 or c > 146 for c in out) or len(set(out)) != len(out):
        raise ValueError("bad class spec " + spec)
    return out


def main():
    tag, encs, classes = sys.argv[1], sys.argv[2].split(","), parse_spec(sys.argv[3])
    signal.signal(signal.SIGTERM, _on_term)
    rows = K.read_classes()
    start = K.now()
    pins_start = {p: K.sha_file(p) for p in K.PINS}
    pin_mismatch = {p: h for p, h in pins_start.items() if h != K.PINS[p]}
    if pin_mismatch:
        raise SystemExit("pin mismatch at start: %s" % pin_mismatch)
    script_hashes = {n: K.sha_file(os.path.join(K.DESK, "scripts", n)) for n in ("k2lib.py", "replay.py")}
    summary_rows, deferred, ck_n, last_ck = [], [], 0, time.monotonic()
    stopped = None
    try:
        for enc in encs:
            for c in classes:
                label = "%s-k2%s_%d" % (tag, enc, c)
                if not stopped and STOP["requested"]:
                    stopped = STOP["requested"]
                if not stopped:
                    bad = K.check_runtime_pins()
                    if bad:
                        stopped = "runtime pin changed before %s: %s" % (label, bad)
                if stopped:
                    deferred.append({"class": c, "encoder": enc, "verdict": "UNKNOWN", "deferred": stopped})
                    continue
                with open(os.path.join(K.CERT, "k2%s_%d.json" % (enc, c))) as f:
                    receipt = json.load(f)
                key = rows[c][0]
                L = K.decode_key(key)
                cnf, einfo = (K.encode_A if enc == "A" else K.encode_B)(L, True)
                row = {"class": c, "encoder": enc, "label": label, "key": key, "encoder_run": einfo,
                       "receipt_cnf_sha256": receipt["cnf_sha256"]}
                rec = None
                if cnf is None:
                    row["error"] = "encoder failed"
                    row["cnf_sha256"] = None
                    row["cnf_hash_match"] = False
                else:
                    row["cnf_sha256"] = K.sha_bytes(cnf)
                    row["cnf_header"] = K.cnf_header(cnf)
                    row["cnf_hash_match"] = row["cnf_sha256"] == receipt["cnf_sha256"]
                    cap = K.wait_for_capacity(log, mine=2)
                    if cap is None or "deferred" in cap:
                        stopped = "launch deferred before %s: %s" % (
                            label, cap["deferred"] if cap else "lane capacity wait exceeded")
                        deferred.append({"class": c, "encoder": enc, "verdict": "UNKNOWN", "deferred": stopped,
                                         "cnf_hash_match": row["cnf_hash_match"], "capacity": cap})
                        continue
                    row["capacity"] = cap
                    rec = K.pipeline(label, cnf, solver=K.solver_argv(SOLVER[enc], 900), solver_seconds=900,
                                     checker_seconds=1800)
                    del cnf
                row["pipeline"] = rec
                row["verdict"] = verdict(row["cnf_hash_match"], rec)
                if rec is not None:
                    row["solver_log_matches_receipt"] = (rec.get("solver_log_sha256")
                                                         == receipt.get("solver_log_sha256"))
                K.write_json_x(os.path.join(K.DESK, "receipts", label + ".json"), row)
                brief = {"class": c, "encoder": enc, "verdict": row["verdict"],
                         "cnf_hash_match": row["cnf_hash_match"],
                         "solver_rc": rec["children"].get("solver", {}).get("rc") if rec else None,
                         "checker_rc": rec["children"].get("checker", {}).get("rc") if rec else None,
                         "status": rec["checker_status_lines"] if rec else None,
                         "safety_stop": rec["safety_stop_reason"] if rec else None,
                         "seconds": rec["pipeline_seconds"] if rec else None,
                         "encode_seconds": einfo["seconds"],
                         "solver_maxrss": rec["children"].get("solver", {}).get("maxrss_bytes") if rec else None,
                         "checker_maxrss": rec["children"].get("checker", {}).get("maxrss_bytes") if rec else None,
                         "peak_aggregate": rec["peak_sampled_aggregate_rss_bytes"] if rec else None}
                summary_rows.append(brief)
                log(json.dumps(brief))
                if time.monotonic() - last_ck > 20 * 60:
                    ck_n += 1
                    last_ck = time.monotonic()
                    K.write_json_x(os.path.join(K.DESK, "checkpoints", "%s-ckpt-%02d.json" % (tag, ck_n)), {
                        "at": K.now(), "done": len(summary_rows),
                        "verdicts": {v: sum(1 for r in summary_rows if r["verdict"] == v)
                                     for v in ("PASS", "FAIL", "UNKNOWN")},
                        "last": brief, "free_bytes": K.free_bytes()})
    finally:
        pins_end = {p: K.sha_file(p) for p in K.PINS}
        out = {"tag": tag, "started_at": start, "finished_at": K.now(), "encoders": encs, "classes": classes,
               "pins_start": pins_start, "pins_end": pins_end, "pins_unchanged": pins_start == pins_end,
               "script_sha256": script_hashes, "stopped": stopped, "rows": summary_rows, "deferred": deferred,
               "verdicts": {v: sum(1 for r in summary_rows if r["verdict"] == v)
                            for v in ("PASS", "FAIL", "UNKNOWN")}}
        K.write_json_x(os.path.join(K.DESK, "replay-summary-%s.json" % tag), out)
        log("done: %s; deferred %d; stopped=%s" % (json.dumps(out["verdicts"]), len(deferred), stopped))


if __name__ == "__main__":
    main()
