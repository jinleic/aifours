#!/usr/bin/env python3
"""Static evidentiary check of the parent K2 replay receipts (read/hash only; reruns nothing).
For every final instance in RESULT.r2.json: bind receipt -> class key (class file line i) -> regenerated CNF SHA
-> producer r4 receipt CNF SHA; re-hash the retained native logs and read their status/parse-dimension lines.
Usage (cwd = desk root): /usr/bin/python3 -B desk/replay_static_check.py
"""
import datetime, hashlib, json, os, re
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = os.path.dirname(HERE)
RP = os.path.join(R, "moqls7-k2-parent-v1")
P = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls7-maximum"
OUT = os.path.join(HERE, "desk", "replay-static-check.json")
PARENT_DRAT = os.path.join(R, "moqls7-parent-proofcheck-v1", "drat-trim")
SOLVERS = {"A": "/opt/homebrew/Cellar/cadical/3.0.1/bin/cadical", "B": "/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat"}
DIMS = re.compile(r"parsing input formula with (\d+) variables and (\d+) clauses")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def main():
    res_path = os.path.join(RP, "RESULT.r2.json")
    res_sha = sha(res_path)
    res = json.load(open(res_path))
    classes = [l.split() for l in open(os.path.join(P, "evidence/ls7_main_classes.txt")) if l.strip()]
    prod = {}
    for e in "AB":
        for row in json.load(open(os.path.join(P, "evidence/gram/k2%s_cert_summary_r4.json" % e)))["rows"]:
            prod[(e, row["class"])] = row["cnf_sha256"]
    rows, seen = [], set()
    labels = {}
    for name in os.listdir(os.path.join(RP, "receipts")):
        r = json.load(open(os.path.join(RP, "receipts", name)))
        labels.setdefault((r["encoder"], r["class"]), []).append((name, r))
    for inst in res["replay"]["instances"]:
        e, c = inst["encoder"], inst["class"]
        cands = [(n, r) for n, r in labels[(e, c)] if r.get("verdict") == "PASS"]
        assert len(cands) == 1, (e, c, [n for n, _ in labels[(e, c)]])
        name, r = cands[0]
        p = r["pipeline"]
        clog, slog = os.path.join(RP, p["checker_log"]), os.path.join(RP, p["solver_log"])
        ctext = open(clog, "rb").read().decode("utf-8", "replace").replace("\r", "\n")
        status = [s.strip() for s in ctext.splitlines() if s.strip().startswith("s ")]
        dims = DIMS.findall(ctext)
        checks = {
            "result_entry_pass": inst["verdict"] == "PASS" and inst["cnf_hash_match"] is True,
            "receipt_key_is_classfile_line": r["key"] == classes[c][0],
            "regenerated_cnf_eq_receipt_field": r["cnf_sha256"] == r["receipt_cnf_sha256"] == p["cnf_sha256"] == p["checker_cnf_sha256"],
            "regenerated_cnf_eq_producer_r4": r["cnf_sha256"] == prod[(e, c)],
            "result_cnf_eq_receipt": inst["cnf_sha256"] == r["cnf_sha256"],
            "checker_log_sha256": sha(clog) == p["checker_log_sha256"],
            "solver_log_sha256": sha(slog) == p["solver_log_sha256"],
            "checker_log_status_exact": status == ["s VERIFIED"] and p["checker_status_lines"] == ["s VERIFIED"],
            "checker_parsed_dims_eq_cnf_header": len(dims) == 1 and [int(dims[0][0]), int(dims[0][1])] == list(r["cnf_header"]),
            "solver_log_unsat": open(slog).read().strip() == "s UNSATISFIABLE",
            "checker_is_parent_drat_trim": p["checker_argv"][0] == PARENT_DRAT,
            "solver_is_pinned_path": p["solver_argv"][0] == SOLVERS[e],
            "no_safety_stop": p["safety_stop_reason"] is None and r["verdict"] == "PASS",
        }
        rows.append({"encoder": e, "class": c, "receipt": name, "run": name.split("-")[0], "receipt_sha256": sha(os.path.join(RP, "receipts", name)),
                     "cnf_sha256": r["cnf_sha256"], "checks_ok": all(checks.values()),
                     "failed": [k for k, v in checks.items() if not v]})
        seen.add((e, c))
    assert len(seen) == 294
    observed = {(x["encoder"], x["class"]) for x in rows if x["run"] in ("v2", "v3")}
    no_hash_observed_classes = sorted(c for c in range(147) if ("A", c) not in observed and ("B", c) not in observed)
    out = {"recorded_at_pt": datetime.datetime.now(ZoneInfo("America/Los_Angeles")).isoformat(),
           "script_sha256": sha(os.path.abspath(__file__)), "parent_result": "moqls7-k2-parent-v1/RESULT.r2.json", "parent_result_sha256": res_sha,
           "provenance_v1_sha256": sha(os.path.join(RP, "provenance-v1.json")),
           "instances": len(rows), "all_static_checks_ok": all(x["checks_ok"] for x in rows),
           "failures": [x for x in rows if not x["checks_ok"]],
           "by_run": {k: sum(1 for x in rows if x["run"] == k) for k in ("v1", "v2", "v3")},
           "classes_with_script_hash_observed_replay": len({c for _, c in observed}),
           "classes_without_any_script_hash_observed_replay": no_hash_observed_classes,
           "rows": rows}
    with open(OUT, "x") as f:
        json.dump(out, f, indent=1)
        f.write("\n")
    print(json.dumps({k: out[k] for k in ("instances", "all_static_checks_ok", "by_run", "classes_with_script_hash_observed_replay")}),
          "no_hash_classes", len(no_hash_observed_classes), no_hash_observed_classes, "failures", len(out["failures"]))


if __name__ == "__main__":
    main()
