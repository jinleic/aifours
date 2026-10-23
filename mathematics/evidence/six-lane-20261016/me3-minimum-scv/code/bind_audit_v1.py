"""Provenance BINDING audit, version 1 (hostile delta review me3-charts-v2-delta-codex-v1.note.md, finding 3).

This is a layer separate from the geometry checker code/check_cover_v3.py, which is unchanged: that checker evaluates
no predicate and binds only leaf content to a run summary. For every ACTIVE certified chart run this audit binds, by
SHA-256 and identity fields,
    spec file + run summary + leaf file + chart / kind / cells + executed code + interpreter + geometry-audit run
to the lane's launcher receipts, the pre-run spec freeze receipts, the certificate index i02 and the anchored pin v2.
It evaluates no chart predicate and does not re-read leaf lines (the leaf-line SHA-256 is bound through the geometry
audit's cover.json, whose own inputs, checker code and output file are bound here).

Anchor (hard-coded): receipts/me3-candidate-pin-v2.json with SHA-256 c9a1eb6d...796c (the value reported to the parent
at 06:18). Binding table (hard-coded, TABLE below): chart -> run, summary, spec, freeze receipt, driver + library
closure, geometry-audit run.
Checks (a failure is recorded as "<id>: <detail>"; a chart is bound iff it has no failure):
 B1 pin anchor SHA-256; the pin's manifest SHA-256 equals pin["manifest"]; every bound file's current SHA-256 equals
    its pin-v2 manifest entry and, where present, its pin-v2 key_files entry.
 B2 dual charts: the freeze receipt names the active spec path and SHA-256; freeze time < run pre-receipt time; every
    code hash in the freeze receipt equals the run pre-receipt's hash for that file; driver and libraries were frozen.
    P (no pre-run freeze receipt exists): the spec SHA-256 equals every earlier recorded value (index i01 05:18,
    pin v1 05:29, parent primal desk RESULT-v1 (itself pinned by pin v2), index i02, pin v2); mtime order is
    recorded as information only.
 B3 run pre-receipt: run name, stage, argv exactly "<driver> <spec>[ <chart>]", interpreter path and version string
    equal to the runtime identity r01, code hashes of driver + closure equal to the current (pinned) files.
    Post-receipt: run name, stage, exit 0, names the pre-receipt by SHA-256, records the summary and leaf-file SHA-256
    equal to the current files.
 B4 summary identity: summary.spec == spec.name; (dual) summary.chart == chart and summary.kind == spec kind ==
    expected kind; summary.cells == number of initial cells of the spec; no FAIL; certificate_ok true;
    eval_cap_hit false; evaluations == 2*leaves - cells (every initial cell a complete binary tree, no early stop).
 B5 geometry audit: pre-receipt run/stage, argv exactly "code/check_cover_v3.py <spec> <chart> <leaves> <summary>
    <stride>" for this run, checker hash and interpreter as pinned; post-receipt (exit 0, names its pre-receipt)
    records the cover.json SHA-256; cover.json: audit_ok, checker, chart, spec path, leaf-file path and SHA-256,
    leaf-line SHA-256 == summary's, counts / leaves / cells == summary's.
 B6 index i02 row: run, spec path and SHA-256, leaf-file and leaf-line SHA-256, pre/post receipt SHA-256, audit run.
Controls (the same function on substituted inputs; each must be rejected and show its required reasons):
 C1  SWC summary CONTENT replaced by the invalid run d02's summary (same path);
 C1b SWC summary PATH pointed at runs/d02-SWC/dual.json;
 C2  SWC spec content with one INTERIOR s breakpoint changed, 1/16 -> 1/17 (byte-level edit of that token only;
     endpoints, cell count, weights, depth, name unchanged);
 C3  SWC spec content replaced by spec v2 (d02's spec; differs from v3 only in its name);
 C4  G summary content replaced by LD1's summary;
 C5  P spec content with initial_split r and w swapped, 12 <-> 80 (byte-level edit; same cell count);
 C6  pin v2 content with the key-file hash of runs/d03-SWC/dual.json zeroed (byte-level edit).
argv[1] = run directory. Writes binding.json and the mutant inputs (exclusive create).
Limits: the receipts are written by this lane's own launcher (no third-party timestamping); the P spec has no pre-run
freeze receipt; file mtimes are not authenticated; the runtime build was hashed once at 05:58 (r01), and each run's
pre-receipt records only the interpreter path and version string.
"""
import sys
import os
import json
import hashlib
from datetime import datetime
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402

RUN = sys.argv[1]
L = "/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/me3-minimum-scv/"
REVIEW = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/"
PIN = "receipts/me3-candidate-pin-v2.json"
PIN_SHA = "c9a1eb6dffac3e61e4994304ea0ac3f6e882c5456aac39519c42e7ef1bce796c"
INDEX = "runs/i02-index/certificate_index.json"
INDEX1 = "runs/i01-index/certificate_index.json"
PIN1 = "receipts/me3-candidate-pin-v1.json"
CHECKER = "code/check_cover_v3.py"
RUNTIME = "runs/r01-runtime/runtime.json"
PARENT_RESULT = REVIEW + "me3-parent-primal-reductions-v1/RESULT-v1.json"
PARENT_RESULT_KEY = "review/me3-parent-primal-reductions-v1/RESULT-v1.json"
FMT = "%Y-%m-%dT%H:%M:%S%z"
DUAL_LIBS = ["code/me3dual_v7.py", "code/me3dual_v6.py", "code/me3dual_v4.py", "code/me3dual_v3.py", "code/me3jet_v1.py",
             "code/me3jet_v2.py"]
COMMON = ["code/lane_guard.py", "code/run_v1.sh"]


def entry(chart, kind, run, summary, spec, freeze, driver, libs, audit):
    rd = f"runs/{run}/"
    return {"chart": chart, "kind": kind, "run": run, "spec": spec, "freeze": freeze, "driver": driver,
            "closure": [driver] + libs + COMMON, "summary": rd + summary, "leaves": rd + "leaves.txt.gz",
            "pre": f"receipts/{run}-pre.json", "post": f"receipts/{run}-post.json", "audit": audit,
            "cover": f"runs/{audit}/cover.json", "apre": f"receipts/{audit}-pre.json",
            "apost": f"receipts/{audit}-post.json"}


F1 = "receipts/spec-dual-freeze-v1.json"
TABLE = [
    entry("P", None, "c03-primalP", "primal.json", "code/spec_primal_P_v1.json", None, "code/cert_primal_v3.py",
          ["code/me3lib_v1.py", "code/me3jet_v1.py"], "b03-cover-P"),
    entry("G", "G", "d01-G", "dual.json", "code/spec_dual_v1.json", F1, "code/cert_dual_v5.py", DUAL_LIBS, "b03-cover-G"),
    entry("SWB", "B", "d01-SWB", "dual.json", "code/spec_dual_v1.json", F1, "code/cert_dual_v5.py", DUAL_LIBS,
          "b03-cover-SWB"),
    entry("LW", "LW", "d01-LW", "dual.json", "code/spec_dual_v1.json", F1, "code/cert_dual_v5.py", DUAL_LIBS,
          "b03-cover-LW"),
    entry("LD1", "LD1", "d01-LD1", "dual.json", "code/spec_dual_v1.json", F1, "code/cert_dual_v5.py", DUAL_LIBS,
          "b03-cover-LD1"),
    entry("LD2", "LD2", "d01-LD2", "dual.json", "code/spec_dual_v1.json", F1, "code/cert_dual_v5.py", DUAL_LIBS,
          "b03-cover-LD2"),
    entry("SWC", "C", "d03-SWC", "dual.json", "code/spec_dual_v3.json", "receipts/spec-dual-freeze-v3.json",
          "code/cert_dual_v7.py", ["code/me3dual_v9.py"] + DUAL_LIBS, "b03-cover-SWC"),
]
BASE_SHA = {}


class FS:
    """File access with optional content substitutions (controls only)."""

    def __init__(self, overrides=None):
        self.ov = overrides or {}

    def raw(self, rel):
        if rel in self.ov:
            return self.ov[rel]
        with open(rel if rel.startswith("/") else L + rel, "rb") as fh:
            return fh.read()

    def sha(self, rel):
        if rel in self.ov:
            return hashlib.sha256(self.ov[rel]).hexdigest()
        if rel not in BASE_SHA:
            BASE_SHA[rel] = hashlib.sha256(self.raw(rel)).hexdigest()
        return BASE_SHA[rel]

    def json(self, rel):
        return json.loads(self.raw(rel))


def audit_chart(e, fs):
    fails = []

    def need(cond, cid, detail=""):
        if not cond:
            fails.append(f"{cid}: {detail}")
        return bool(cond)

    out = {"chart": e["chart"], "run": e["run"], "spec": e["spec"], "summary": e["summary"], "leaves": e["leaves"]}
    # ---------------------------------------------------------------- B1 pin anchor, manifest, key files
    pin_sha = fs.sha(PIN)
    need(pin_sha == PIN_SHA, "B1-pin-anchor", pin_sha)
    pin = fs.json(PIN)
    man_rel = pin["manifest"]["path"]
    need(fs.sha(man_rel) == pin["manifest"]["sha256"], "B1-manifest", man_rel)
    man = fs.json(man_rel)
    keyf = pin.get("key_files", {})
    bound = [e["spec"], e["summary"], e["leaves"], e["pre"], e["post"], e["cover"], e["apre"], e["apost"], INDEX,
             CHECKER, RUNTIME] + e["closure"] + ([e["freeze"]] if e["freeze"] else [])
    sh = {}
    for rel in bound:
        h = fs.sha(rel)
        sh[rel] = h
        m = man.get(rel)
        need(m is not None and m.get("sha256") == h, "B1-manifest-entry", rel)
        if rel in keyf:
            need(keyf[rel] == h, "B1-key-file", rel)
    out["sha256"] = sh
    spec_sha = sh[e["spec"]]
    # ---------------------------------------------------------------- B2 freeze / spec-hash records
    pre = fs.json(e["pre"])
    tpre = datetime.strptime(pre["written_at_host_clock"], FMT)
    if e["freeze"]:
        fr = fs.json(e["freeze"])
        fspec = fr.get("spec", {})
        need(fspec.get("path") == e["spec"] and fspec.get("sha256") == spec_sha, "B2-freeze-spec",
             f"{fspec} vs {spec_sha}")
        tfr = datetime.strptime(fr["frozen_at_host_clock"], FMT)
        need(tfr < tpre, "B2-freeze-before-run", f"{fr['frozen_at_host_clock']} vs {pre['written_at_host_clock']}")
        codes = fr.get("code") or fr.get("code_transitive_closure_sha256") or {}
        for f, h in sorted(codes.items()):
            need(pre.get("code_sha256", {}).get(f) == h, "B2-freeze-code", f)
        for f in e["closure"]:
            if f not in COMMON:
                need(f in codes, "B2-closure-frozen", f)
        out["freeze"] = {"receipt": e["freeze"], "frozen_at": fr["frozen_at_host_clock"],
                         "run_pre_receipt_at": pre["written_at_host_clock"]}
    else:
        recs = {"index i01 (05:18)": next((r.get("spec_sha256") for r in fs.json(INDEX1)["rows"]
                                           if r.get("chart") == e["chart"]), None),
                "pin v1 (05:29)": fs.json(PIN1).get("key_files", {}).get(e["spec"]),
                "parent primal RESULT-v1": fs.json(PARENT_RESULT).get("inputs_rehashed_after_runs_unchanged",
                                                                     {}).get(e["spec"]),
                "index i02": next((r.get("spec_sha256") for r in fs.json(INDEX)["rows"]
                                   if r.get("chart") == e["chart"]), None),
                "pin v2": keyf.get(e["spec"])}
        for src, h in recs.items():
            need(h == spec_sha, "B2-P-record", f"{src}: {h}")
        need(fs.sha(PARENT_RESULT) == pin.get("external_citations_sha256", {}).get(PARENT_RESULT_KEY),
             "B2-P-parent-result-pinned", "")
        out["spec_hash_records"] = recs
        out["info_spec_mtime_before_run_pre_receipt"] = os.path.getmtime(L + e["spec"]) < tpre.timestamp()
    # ---------------------------------------------------------------- B3 launch receipts
    rt = fs.json(RUNTIME)
    exp_ver = (f"{rt['python_version'].split()[0]} flint {rt['python_flint_version']} sympy {rt['sympy_version']} "
               f"mpmath {rt['mpmath_version']}")
    exp_argv = f"{e['driver']} {e['spec']}" + ("" if e["chart"] == "P" else f" {e['chart']}")
    need(pre.get("run") == e["run"] and pre.get("stage") == "pre-execution", "B3-pre-identity",
         f"{pre.get('run')} {pre.get('stage')}")
    need(pre.get("argv") == exp_argv, "B3-argv", f"{pre.get('argv')!r} vs {exp_argv!r}")
    need(pre.get("interpreter") == rt["sys_executable"] and pre.get("interpreter_version") == exp_ver,
         "B3-interpreter", f"{pre.get('interpreter_version')!r} vs {exp_ver!r}")
    for f in e["closure"]:
        need(pre.get("code_sha256", {}).get(f) == sh[f], "B3-code-at-launch", f)
    post = fs.json(e["post"])
    need(post.get("run") == e["run"] and post.get("stage") == "post-execution" and post.get("exit_code") == 0,
         "B3-post-identity", f"{post.get('run')} {post.get('stage')} {post.get('exit_code')}")
    need(post.get("pre_receipt_sha256") == sh[e["pre"]], "B3-post-names-pre", "")
    outs = post.get("outputs_sha256", {})
    need(outs.get("./" + e["summary"], {}).get("sha256") == sh[e["summary"]], "B3-summary-sha", e["summary"])
    need(outs.get("./" + e["leaves"], {}).get("sha256") == sh[e["leaves"]], "B3-leaves-sha", e["leaves"])
    out["launch"] = {"argv": pre.get("argv"), "pre_receipt_at": pre.get("written_at_host_clock"),
                     "ended_at": post.get("ended_at_host_clock"), "exit_code": post.get("exit_code")}
    # ---------------------------------------------------------------- B4 summary identity
    spec = fs.json(e["spec"])
    summ = fs.json(e["summary"])
    need(summ.get("spec") == spec.get("name"), "B4-spec-name", f"{summ.get('spec')!r} vs {spec.get('name')!r}")
    cells = None
    if e["chart"] == "P":
        ns = [int(spec["initial_split"][k]) for k in ("r", "w", "phi")]
        cells = ns[0] * ns[1] * ns[2]
    else:
        cs = spec.get("charts", {}).get(e["chart"])
        if need(cs is not None, "B4-chart-in-spec", e["chart"]):
            need(summ.get("chart") == e["chart"], "B4-chart", str(summ.get("chart")))
            need(summ.get("kind") == e["kind"] and cs.get("kind") == e["kind"], "B4-kind",
                 f"{summ.get('kind')} / {cs.get('kind')}")
            cells = 1
            for bp in cs["breakpoints"]:
                cells *= len(bp) - 1
    counts = {k: v for k, v in summ.get("counts", {}).items() if v}
    leaves = sum(counts.values())
    need(summ.get("cells") == cells, "B4-cells", f"{summ.get('cells')} vs {cells}")
    need("FAIL" not in counts, "B4-no-FAIL", "")
    need(summ.get("certificate_ok") is True and summ.get("eval_cap_hit") is False, "B4-certificate-flags", "")
    need(cells is not None and summ.get("evaluations") == 2 * leaves - cells, "B4-evaluations-tree-identity",
         f"{summ.get('evaluations')} vs 2*{leaves}-{cells}")
    out["identity"] = {"spec_name": spec.get("name"), "kind": e["kind"], "cells": cells, "leaves": leaves,
                       "evaluations": summ.get("evaluations"), "counts": counts,
                       "leaf_lines_sha256": summ.get("leaf_lines_sha256")}
    # ---------------------------------------------------------------- B5 geometry-audit binding
    apre = fs.json(e["apre"])
    toks = apre.get("argv", "").split()
    need(len(toks) == 6 and toks[:5] == [CHECKER, e["spec"], e["chart"], e["leaves"], e["summary"]], "B5-argv",
         apre.get("argv"))
    need(apre.get("run") == e["audit"] and apre.get("stage") == "pre-execution", "B5-pre-identity", "")
    need(apre.get("code_sha256", {}).get(CHECKER) == sh[CHECKER], "B5-checker-code", "")
    need(apre.get("interpreter") == rt["sys_executable"] and apre.get("interpreter_version") == exp_ver,
         "B5-interpreter", "")
    apost = fs.json(e["apost"])
    need(apost.get("run") == e["audit"] and apost.get("exit_code") == 0
         and apost.get("pre_receipt_sha256") == sh[e["apre"]], "B5-post", "")
    need(apost.get("outputs_sha256", {}).get("./" + e["cover"], {}).get("sha256") == sh[e["cover"]],
         "B5-cover-sha", "")
    cov = fs.json(e["cover"])
    need(cov.get("audit_ok") is True and cov.get("checker") == "check_cover_v3" and cov.get("chart") == e["chart"]
         and cov.get("spec") == e["spec"] and cov.get("leaves_file") == e["leaves"], "B5-cover-identity", "")
    need(cov.get("leaves_gz_sha256") == sh[e["leaves"]], "B5-cover-leaves-file", "")
    need(cov.get("leaf_lines_sha256") == summ.get("leaf_lines_sha256"), "B5-cover-leaf-lines", "")
    need(cov.get("counts") == counts and cov.get("leaves") == leaves, "B5-cover-counts", "")
    need(cov.get("cells_seen") == cells and cov.get("cells_expected") == cells, "B5-cover-cells", "")
    # ---------------------------------------------------------------- B6 index i02 row
    rows = [r for r in fs.json(INDEX).get("rows", []) if r.get("chart") == e["chart"]]
    if need(len(rows) == 1, "B6-index-row-count", str(len(rows))):
        r = rows[0]
        exp = {"run": e["run"], "spec": e["spec"], "spec_sha256": spec_sha, "leaves_gz_sha256": sh[e["leaves"]],
               "leaf_lines_sha256": summ.get("leaf_lines_sha256"), "pre_receipt_sha256": sh[e["pre"]],
               "post_receipt_sha256": sh[e["post"]], "audit_run": e["audit"]}
        for k, v in exp.items():
            need(r.get(k) == v, "B6-index-row", k)
    out["failures"] = fails
    out["ok"] = not fails
    return out


def by(chart):
    return dict(next(x for x in TABLE if x["chart"] == chart))


def byte_edit(rel, old, new, name):
    data = FS().raw(rel)
    assert data.count(old) == 1, (rel, old, data.count(old))
    mut = data.replace(old, new)
    with lane_guard.xopen(RUN + "/" + name, "xb") as fh:
        fh.write(mut)
    return mut


results = {x["chart"]: audit_chart(x, FS()) for x in TABLE}
all_ok = all(r["ok"] for r in results.values())

controls = {}


def control(name, desc, e, overrides, required):
    r = audit_chart(e, FS(overrides))
    ids = sorted({f.split(":")[0] for f in r["failures"]})
    c = {"description": desc, "rejected": not r["ok"], "failure_ids": ids, "required": sorted(required),
         "required_present": set(required) <= set(ids), "failures_first25": r["failures"][:25]}
    c["verdict"] = c["rejected"] and c["required_present"]
    controls[name] = c


swc = by("SWC")
control("C1", "SWC summary content replaced by the invalid d02 summary (same path)", swc,
        {swc["summary"]: FS().raw("runs/d02-SWC/dual.json")}, ["B1-manifest-entry", "B3-summary-sha", "B4-spec-name"])
c1b = by("SWC")
c1b["summary"] = "runs/d02-SWC/dual.json"
control("C1b", "SWC summary path pointed at runs/d02-SWC/dual.json", c1b, {},
        ["B3-summary-sha", "B4-spec-name", "B5-argv"])
m2 = byte_edit("code/spec_dual_v3.json", b'"1/16"', b'"1/17"', "mutant_spec_dual_v3_interior.json")
control("C2", "SWC spec v3 with interior s breakpoint 1/16 -> 1/17 (endpoints, cell count, name unchanged)", by("SWC"),
        {"code/spec_dual_v3.json": m2}, ["B1-manifest-entry", "B1-key-file", "B2-freeze-spec", "B6-index-row"])
control("C3", "SWC spec content replaced by spec v2 (d02's spec)", by("SWC"),
        {"code/spec_dual_v3.json": FS().raw("code/spec_dual_v2.json")}, ["B2-freeze-spec", "B4-spec-name"])
g = by("G")
control("C4", "G summary content replaced by LD1's summary", g, {g["summary"]: FS().raw("runs/d01-LD1/dual.json")},
        ["B3-summary-sha", "B4-chart", "B4-kind", "B4-cells", "B5-cover-leaf-lines"])
m5 = byte_edit("code/spec_primal_P_v1.json", b'"initial_split": {"r": 12, "w": 80, "phi": 64}',
               b'"initial_split": {"r": 80, "w": 12, "phi": 64}', "mutant_spec_primal_P_swapsplit.json")
control("C5", "P spec with initial_split r and w swapped (same cell count)", by("P"),
        {"code/spec_primal_P_v1.json": m5}, ["B1-key-file", "B2-P-record", "B6-index-row"])
d03sum = FS().sha("runs/d03-SWC/dual.json")
m6 = byte_edit(PIN, d03sum.encode(), b"0" * 64, "mutant_pin_v2.json")
control("C6", "pin v2 with the key-file hash of runs/d03-SWC/dual.json zeroed", by("SWC"), {PIN: m6},
        ["B1-pin-anchor", "B1-key-file"])
controls_ok = all(c["verdict"] for c in controls.values())
c2 = controls["C2"]["failure_ids"]
geometry_level = [i for i in c2 if i.startswith("B4") or i.startswith("B5")]
res = {"audit": "bind_audit_v1", "anchor_pin": {"path": PIN, "sha256": PIN_SHA},
       "charts": results, "all_bound": all_ok, "controls": controls, "controls_ok": controls_ok,
       "C2_identity_or_geometry_level_failures": geometry_level,
       "limits": ["receipts are written by this lane's own launcher (no third-party timestamping)",
                  "the P spec has no pre-run freeze receipt; its hash is recorded from 05:18 on; mtime is information",
                  "file mtimes are not authenticated",
                  "runtime build hashed once at 05:58 (r01); run pre-receipts record interpreter path and version",
                  "no chart predicate is evaluated here (predicate replay is separate)"]}
with lane_guard.xopen(RUN + "/binding.json") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({"all_bound": all_ok, "per_chart": {k: (v["ok"], v["failures"][:3]) for k, v in results.items()},
                  "controls_ok": controls_ok,
                  "controls": {k: (v["verdict"], v["failure_ids"]) for k, v in controls.items()},
                  "C2_identity_or_geometry_level_failures": geometry_level}, indent=1))
