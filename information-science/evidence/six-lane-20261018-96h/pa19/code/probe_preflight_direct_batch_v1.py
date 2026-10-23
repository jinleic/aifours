#!/usr/bin/env python3
"""PA19 96h lane probe 13: read-only item-pin / case-coverage preflight for the next ms06 DIRECT batches.

Per the parent (2026-10-19 ~02:45 PDT), each new batch of the unchanged v17 framework needs only its item pins
and case coverage checked, not a framework re-review. The batches are frozen here. v17 holds 3 items at most
under its chunk fit: 2,960 + 3 x 2,450 = 10,310 <= 10,620, while 4 items give 12,760.
  v18 = v17 with ITEMS [b189, b202, b177] (ranking[3:6] of ms06-direct-pins-v1), out dir run-005;
  v19 = v17 with ITEMS [b295] (ranking[6:7]), out dir run-006.

Order:
  (0) exclusive receipt <out>.receipt.json with PID/PGID/PPID/argv/cwd/source SHA BEFORE any work;
  (1) runner and v17 pins; difflib non-equal opcodes exactly the frozen ones (docstring scope lines and
      ITEMS only);
  (2) items: ids are exactly ms06:bNNNNN:direct for the frozen b list; that list equals the frozen ranking
      slice of evidence/probes/ms06-direct-pins-v1.json; the b values are distinct, disjoint from the run-004
      batch (156, 187, 144) and from the other batch;
  (3) each item CNF is regenerated exactly as v17 run_plan builds it (E.build_v2(D["c0"], types, empty, special)
      then cnf_bytes, special = profiles != runner P0); (sha256, bytes, header) must equal the runner pin, the
      pins evidence (whose regenerated CNF equals the old record);
  (4) case coverage: each b is a lane-original M2 case open in frontier-v1 ms06_undecided AND in the parent's
      current frontier v2 ms06_undecided (same s_tag, same skeleton fields as the pinned skeleton file), and is
      not among the parent's new_case_closures. Whole case, direct: no list, interval or denominator;
  (5) lstat type (regular, not a symlink) and SHA-256 of every path the runner hashes, reads or executes;
      out dir absent;
  (6) runner registry_refusals() and stability_refusals(projected) on the live files (expected []);
      reservation and chunk-fit numbers from the runner constants.
Not re-probed: framework runtime (ps parsing, child identity, transport), which is unchanged from v17, was
reviewed by Codex r8 and was exercised by run-004.
No runner launch, no solver/checker, no CNF file, no child process other than /bin/date, and nothing written
under LANE/tmp or evidence/pilot-v1. Admission: fresh statvfs >= 12.2e9 + 16 MiB and no STOP/HALT/sat-candidate
marker. Self budget 280 s.
Usage: probe_preflight_direct_batch_v1.py {v18|v19} OUT_JSON
"""
import difflib
import hashlib
import importlib.util
import json
import os
import re
import stat
import subprocess
import sys
import time

sys.dont_write_bytecode = True
T0 = time.monotonic()
LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h"
V17 = (LANE + "/code/pilot_file_drat_v17.py", "96e179a4c2de5382336e5bdae78eb9eb9adecd789cb49f5bcfe0694fd3447566")
PINS = (LANE + "/evidence/probes/ms06-direct-pins-v1.json", "c1417c2af428349121091fff3dfa192312f0f15dcd3dd19d0bf902176aee7148")
FRONT1 = (LANE + "/evidence/probes/frontier-v1.json", "0e7e4370961ea8713f8549576a3973c661c1b6499f8a345c74be97d0b4216a46")
FRONT2 = (RUN + "/review/pa19-parent-frontier-v2.json", "2c69ead5cfad206d02a3e289d343f2612f59e2dbd0e4f3f1240bdc65f071805a")
PY_REAL = ("/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/bin/python3.14",
           "cbf84109626aa1013bbe408fbb9590bd0f1c1548f038b2221c6b8b87de26ca43")
RUN004_BATCH = (156, 187, 144)
BATCHES = {
    "v18": {"runner": (LANE + "/code/pilot_file_drat_v18.py",
                       "56528983b5ea98940e51abcb1169b28669228b8ee8826583e8e97920d865f0e7"),
            "opcodes": [["replace", 57, 58, 57, 58], ["replace", 110, 116, 110, 116]],
            "b": [189, 202, 177], "ranking_slice": [3, 6], "out_dir": LANE + "/evidence/pilot-v1/run-005"},
    "v19": {"runner": (LANE + "/code/pilot_file_drat_v19.py",
                       "fd6bbb43a35bcf29644dc24c6d24c9f538d6665e92d7ef4cafe0b65ea62f13ef"),
            "opcodes": [["replace", 55, 56, 55, 56], ["replace", 57, 58, 57, 58], ["replace", 110, 116, 110, 112]],
            "b": [295], "ranking_slice": [6, 7], "out_dir": LANE + "/evidence/pilot-v1/run-006"},
}
FLOOR = 12_200_000_000 + 16 * 1024 * 1024
BUDGET = 280.0


def clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True, check=True,
                          stdin=subprocess.DEVNULL).stdout.strip()


def budget(stage):
    if time.monotonic() - T0 > BUDGET:
        raise SystemExit("BUDGET exceeded at " + stage)


def ltype(path):
    try:
        st = os.lstat(path)
    except FileNotFoundError:
        return "absent", None
    m = st.st_mode
    t = ("regular" if stat.S_ISREG(m) else "symlink" if stat.S_ISLNK(m) else "directory" if stat.S_ISDIR(m)
         else "fifo" if stat.S_ISFIFO(m) else "other")
    return t, st.st_ino


def check_file(path, pin):
    t, ino = ltype(path)
    rec = {"path": path, "lstat_type": t, "inode": ino, "pin": pin}
    if t == "regular":
        with open(path, "rb") as f:
            h = hashlib.sha256(f.read()).hexdigest()
        rec["sha256"] = h
        rec["pin_ok"] = None if pin is None else (h == pin)
    rec["ok"] = (t == "regular" and rec.get("pin_ok") is not False)
    return rec


def pinned_json(path, pin):
    with open(path, "rb") as f:
        raw = f.read()
    if hashlib.sha256(raw).hexdigest() != pin:
        raise SystemExit("REFUSED pin mismatch " + path)
    return json.loads(raw)


def main():
    batch = sys.argv[1]
    if batch not in BATCHES:
        raise SystemExit("REFUSED: unknown batch")
    B = BATCHES[batch]
    out_path = os.path.abspath(sys.argv[2])
    if not (out_path.startswith(LANE + "/evidence/probes/") and out_path.endswith(".json")):
        raise SystemExit("REFUSED: output outside probes or not .json")
    receipt_path = out_path[:-len(".json")] + ".receipt.json"
    with open(os.path.abspath(__file__), "rb") as f:
        src_sha = hashlib.sha256(f.read()).hexdigest()
    receipt = {"schema": "PA19-96H-PROBE-RECEIPT-v1", "probe": os.path.abspath(__file__), "probe_sha256": src_sha,
               "pid": os.getpid(), "ppid": os.getppid(), "pgid": os.getpgid(0), "sid": os.getsid(0),
               "argv": sys.argv, "cwd": os.getcwd(), "executable": sys.executable, "python": sys.version,
               "host_clock": clock(), "self_budget_seconds": BUDGET, "output": out_path,
               "scope": "read-only item-pin/case-coverage preflight; children /bin/date only; no CNF file"}
    with open(receipt_path, "xb") as f:
        f.write(json.dumps(receipt, indent=1, sort_keys=True).encode())
    print("RECEIPT", receipt_path, receipt["pid"], flush=True)
    st = os.statvfs(LANE)
    free0 = st.f_bavail * st.f_frsize
    mk = [os.path.join(d, n) for d in (LANE + "/control", RUN + "/control") for n in sorted(os.listdir(d))
          if re.match(r"(?i)^(stop|halt|sat-candidate)", n) or "HALT" in n]
    if free0 < FLOOR or mk:
        raise SystemExit(f"REFUSED free={free0} markers={mk}")
    started = clock()
    # (1) runner pins and diff scope
    rn, base = check_file(*B["runner"]), check_file(*V17)
    if not (rn["ok"] and base["ok"]):
        raise SystemExit("REFUSED: runner pin mismatch")
    with open(V17[0], "rb") as f:
        a = f.read().decode().splitlines(keepends=True)
    with open(B["runner"][0], "rb") as f:
        b = f.read().decode().splitlines(keepends=True)
    ops = [list(op) for op in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes() if op[0] != "equal"]
    diff_ok = ops == B["opcodes"]
    spec = importlib.util.spec_from_file_location("pilot_%s_readonly" % batch, B["runner"][0])
    M = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(M)  # module top level defines constants only; main() is not called
    # (2) item identity
    pins = pinned_json(*PINS)
    lo, hi = B["ranking_slice"]
    ranked = [r["b_index"] for r in pins["ranking"]]
    other = [x for k, v in BATCHES.items() if k != batch for x in v["b"]]
    ids_ok = [it["id"] for it in M.ITEMS] == ["ms06:b%05d:direct" % x for x in B["b"]] \
        and [it["b"] for it in M.ITEMS] == B["b"]
    identity = {"ids_exact": ids_ok, "ranking": ranked, "ranking_slice_equal": ranked[lo:hi] == B["b"],
                "distinct": len(set(B["b"])) == len(B["b"]),
                "disjoint_from_run004_batch": not set(B["b"]) & set(RUN004_BATCH),
                "disjoint_from_other_batch": not set(B["b"]) & set(other)}
    # (3) CNFs exactly as v17 run_plan builds them
    with open(M.ENC[0], "rb") as f:
        if hashlib.sha256(f.read()).hexdigest() != M.ENC[1]:
            raise SystemExit("REFUSED: encoder pin")
    espec = importlib.util.spec_from_file_location("encode_skel_b_lane", M.ENC[0])
    E = importlib.util.module_from_spec(espec)
    espec.loader.exec_module(E)
    D = pinned_json(*M.SKEL)
    special = [p for p in D["profiles"] if list(p) != M.P0]
    f1 = pinned_json(*FRONT1)
    f2 = pinned_json(*FRONT2)
    open1 = {x["b_index"]: x for x in f1["ms06_undecided"]}
    open2 = {x["b_index"]: x for x in f2["ms06_undecided"]}
    closed2 = {c.get("case") for c in f2.get("new_case_closures", [])}
    pin_by_b = {c["b_index"]: c for c in pins["cases"]}
    items = []
    for it in M.ITEMS:
        sk = D["skeletons"][it["b"]]
        nv, cl = E.build_v2(D["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special)
        cnf = E.cnf_bytes(nv, cl)
        del cl
        got = (hashlib.sha256(cnf).hexdigest(), len(cnf), cnf.split(b"\n", 1)[0].decode())
        del cnf
        pc = pin_by_b.get(it["b"])
        x1, x2 = open1.get(it["b"]), open2.get(it["b"])
        case = "ms06_b%05d" % it["b"]
        cov = {"lane_original_case": case, "s_tag_frontier_v1": None if x1 is None else x1["s_tag"],
               "s_tag_parent_frontier_v2": None if x2 is None else x2["s_tag"],
               "open_in_frontier_v1": x1 is not None, "open_in_parent_frontier_v2": x2 is not None,
               "not_in_parent_new_case_closures": case not in closed2,
               "skeleton_fields_equal_v1_v2_file": x1 is not None and x2 is not None
               and x1["skeleton_types"] == x2["skeleton_types"] == sk["types"]
               and x1["skeleton_empty"] == x2["skeleton_empty"] == sk["empty"] and x1["s_tag"] == x2["s_tag"],
               "whole_case_direct": "build_v2 of the full skeleton entry; no list, interval or denominator"}
        items.append({"id": it["id"], "b": it["b"], "regenerated": list(got), "runner_pin": list(it["cnf"]),
                      "equal_runner_pin": got == tuple(it["cnf"]),
                      "equal_pins_evidence": pc is not None and [pc["direct_cnf"]["sha256"], pc["direct_cnf"]["bytes"],
                                                                 pc["direct_cnf"]["header"]] == list(got),
                      "pins_evidence_record_equal": pc is not None and pc["record_cnf_equal"] is True,
                      "old_provenance": None if pc is None else {k: pc["provenance"].get(k) for k in (
                          "route", "record", "record_sha256", "status", "solver_version", "solver_rc", "solve_seconds",
                          "check_seconds", "drat_trim_s_lines", "solver_status_lines", "unknown_reason")},
                      "coverage": cov})
        budget("item %s" % it["id"])
    items_ok = all(i["equal_runner_pin"] and i["equal_pins_evidence"] and i["pins_evidence_record_equal"]
                   and i["coverage"]["open_in_frontier_v1"] and i["coverage"]["open_in_parent_frontier_v2"]
                   and i["coverage"]["not_in_parent_new_case_closures"]
                   and i["coverage"]["skeleton_fields_equal_v1_v2_file"] for i in items)
    # (5) runtime pins
    files = [("runner_" + batch, B["runner"][0], B["runner"][1]), ("runner_v17_base", V17[0], V17[1]),
             ("kissat", M.KISSAT[0], M.KISSAT[1]),
             ("drat_trim_old", M.DRAT_OLD[0], M.DRAT_OLD[1]), ("drat_trim_lane_copy", M.DRAT, M.DRAT_OLD[1]),
             ("encoder", M.ENC[0], M.ENC[1]), ("skeleton_ms06", M.SKEL[0], M.SKEL[1]),
             ("stop_registry", M.REGISTRY[0], M.REGISTRY[1]), ("launch_contract", M.LAUNCH_CONTRACT[0], M.LAUNCH_CONTRACT[1]),
             ("binary_imports", M.BINARY_IMPORTS[0], M.BINARY_IMPORTS[1]),
             ("kissat_source_evidence", M.KISSAT_SOURCE[0], M.KISSAT_SOURCE[1]), ("monitor", M.MONITOR, None),
             ("python_real", PY_REAL[0], PY_REAL[1]), ("direct_pins_evidence", PINS[0], PINS[1]),
             ("frontier_v1", FRONT1[0], FRONT1[1]), ("parent_frontier_v2", FRONT2[0], FRONT2[1]),
             ("bin_date", "/bin/date", None), ("bin_ps", "/bin/ps", None)]
    files += [("inherited_marker_" + n, M.OLD + "/cycle2/" + n, h) for n, h in M.OLD_LIVE_MARKERS.items()]
    checks = [dict(check_file(p, h), role=r) for r, p, h in files]
    drat_inodes_distinct = ltype(M.DRAT)[1] != ltype(M.DRAT_OLD[0])[1]
    out_absent = not os.path.lexists(B["out_dir"])
    budget("file checks")
    # (6) admission functions and constants
    reg = M.registry_refusals()
    projected_max = M.PROOF_CAP + M.LOG_CAP + 3 * M.RECORD_MAX
    projected_ctrl = M.LOG_CAP + M.CONTROL_PROOF_CAP + 3 * M.RECORD_MAX
    stab_at = clock()
    stab_max = M.stability_refusals(projected_max)
    stab_ctrl = M.stability_refusals(projected_ctrl)
    offset = M.CONTROLS_WORST_SECONDS + len(M.ITEMS) * M.ITEM_WORST_SECONDS
    consts = {"items": len(M.ITEMS), "CNF_ITEM_MAX": M.CNF_ITEM_MAX, "ITEM_RESERVE": M.ITEM_RESERVE,
              "retained_output_reservation_bytes": M.RUN_RESERVE + M.CONTROL_RESERVE + len(M.ITEMS) * M.ITEM_RESERVE,
              "absolute_end_offset_seconds": offset,
              "chunk_fit_ok": offset + M.SETTLE + M.MARGIN <= M.MAX_CHUNK,
              "SOLVER_SECONDS": M.SOLVER_SECONDS, "CHECK_SECONDS": M.CHECK_SECONDS, "PROOF_CAP": M.PROOF_CAP}
    ok = (diff_ok and all(identity[k] for k in identity if k != "ranking") and items_ok
          and all(c["ok"] for c in checks if not c["role"].startswith("bin_")) and drat_inodes_distinct
          and out_absent and reg == [] and stab_max == [] and stab_ctrl == [] and consts["chunk_fit_ok"])
    st = os.statvfs(LANE)
    res = {"schema": "PA19-96H-PROBE-PREFLIGHT-DIRECT-BATCH-v1", "batch": batch, "receipt": receipt_path,
           "receipt_pid": receipt["pid"], "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3), "probe_sha256": src_sha,
           "admission": {"free_start": free0, "free_end": st.f_bavail * st.f_frsize, "floor": FLOOR, "markers": mk},
           "runner_diff_check": {"base": V17, "runner": B["runner"], "opcodes": ops, "expected": B["opcodes"],
                                 "ok": diff_ok},
           "identity": identity, "items": items, "items_ok": items_ok, "file_checks": checks,
           "drat_inodes_distinct": drat_inodes_distinct, "out_dir": B["out_dir"], "out_dir_absent": out_absent,
           "registry_refusals": reg,
           "stability_refusals": {"evaluated_after_host_clock": stab_at, "projected_item_max": [projected_max, stab_max],
                                  "projected_control": [projected_ctrl, stab_ctrl]},
           "runner_constants": consts, "all_ok": ok,
           "scope": "item pins and case coverage plus runtime path pins and admission functions; framework runtime "
                    "unchanged from v17 (Codex r8, run-004) and not re-probed; no launch, no solver/checker"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data), "all_ok", ok, flush=True)


if __name__ == "__main__":
    main()
