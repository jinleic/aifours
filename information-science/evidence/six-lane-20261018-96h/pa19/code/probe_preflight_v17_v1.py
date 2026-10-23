#!/usr/bin/env python3
"""PA19 96h lane probe 12: read-only runtime preflight of runner v17 (ms06 direct whole-case items) before
GO request v5.

v17 = v16 with only the item family changed: docstring scope lines, SKEL -> skeletons-b-ms06.json, ITEMS ->
three direct whole-case items (ms06 b156, b187, b144; cheapest three by evidence/probes/ms06-direct-pins-v1.json),
the item CNF generation (encode_skel_b.build_v2 instead of a placement list + build_partbatch) and the record
key list_pin -> case_b. Transport, controls, admission and terminal code are unchanged.

Order:
  (0) exclusive receipt <out>.receipt.json with PID/PGID/PPID/argv/cwd/source SHA BEFORE any work;
  (1) v16/v17 pins, plus a difflib check that the non-equal opcodes are exactly the six frozen ones;
  (2) lstat type (regular, not a symlink) and SHA-256 pin of every path v17 hashes, reads or executes;
      directories; run-004 absent;
  (3) each v17 ITEMS CNF regenerated in process exactly as v17 run_plan does
      (build_v2(c0, types, empty, special) then cnf_bytes); (sha256, bytes, header) must equal it["cnf"];
  (4) v17 registry_refusals() and stability_refusals(projected) on the live files (expected []);
  (5) v17 ps_table() and identity_checked() on one harmless owned child (/bin/sleep 1, own session, reaped by
      Popen.wait(); no signal is ever sent);
  (6) v17 reservation and chunk-fit constants, recorded for the GO request.
No runner launch, no solver/checker, no CNF file. Standard library plus the in-process encoder; children
/bin/date, /bin/ps, /bin/sleep. Admission: fresh statvfs >= 12.2e9 + 16 MiB and no STOP/HALT/sat-candidate
marker. Self budget 280 s.
Usage: probe_preflight_v17_v1.py OUT_JSON
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
V16 = (LANE + "/code/pilot_file_drat_v16.py", "0ef4cfdcf7f0220bdde78829198bea7a8acf603e2678e88eedafe0c04bd3170e")
V17 = (LANE + "/code/pilot_file_drat_v17.py", "96e179a4c2de5382336e5bdae78eb9eb9adecd789cb49f5bcfe0694fd3447566")
PY_REAL = ("/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/bin/python3.14",
           "cbf84109626aa1013bbe408fbb9590bd0f1c1548f038b2221c6b8b87de26ca43")
PINS = (LANE + "/evidence/probes/ms06-direct-pins-v1.json", "c1417c2af428349121091fff3dfa192312f0f15dcd3dd19d0bf902176aee7148")
EXPECTED_OPCODES = [["replace", 55, 58, 55, 58], ["replace", 88, 89, 88, 89], ["replace", 110, 119, 110, 116],
                    ["delete", 1259, 1262, 1256, 1256], ["replace", 1263, 1265, 1257, 1258],
                    ["replace", 1275, 1276, 1268, 1269]]
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


def main():
    out_path = os.path.abspath(sys.argv[1])
    if not (out_path.startswith(LANE + "/evidence/probes/") and out_path.endswith(".json")):
        raise SystemExit("REFUSED: output outside probes or not .json")
    receipt_path = out_path[:-len(".json")] + ".receipt.json"
    with open(os.path.abspath(__file__), "rb") as f:
        src_sha = hashlib.sha256(f.read()).hexdigest()
    receipt = {"schema": "PA19-96H-PROBE-RECEIPT-v1", "probe": os.path.abspath(__file__), "probe_sha256": src_sha,
               "pid": os.getpid(), "ppid": os.getppid(), "pgid": os.getpgid(0), "sid": os.getsid(0),
               "argv": sys.argv, "cwd": os.getcwd(), "executable": sys.executable, "python": sys.version,
               "host_clock": clock(), "self_budget_seconds": BUDGET, "output": out_path,
               "scope": "read-only preflight; children /bin/date, /bin/ps, one /bin/sleep 1 reaped by wait()"}
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
    v17, v16 = check_file(*V17), check_file(*V16)
    if not (v17["ok"] and v16["ok"]):
        raise SystemExit("REFUSED: runner pin mismatch")
    with open(V16[0], "rb") as f:
        a = f.read().decode().splitlines(keepends=True)
    with open(V17[0], "rb") as f:
        b = f.read().decode().splitlines(keepends=True)
    ops = [list(op) for op in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes() if op[0] != "equal"]
    diff_ok = ops == EXPECTED_OPCODES
    spec = importlib.util.spec_from_file_location("pilot_v17_readonly", V17[0])
    M = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(M)  # module top level defines constants only; main() is not called
    files = [("runner_v17", V17[0], V17[1]), ("runner_v16_diff_base", V16[0], V16[1]),
             ("kissat", M.KISSAT[0], M.KISSAT[1]),
             ("drat_trim_old", M.DRAT_OLD[0], M.DRAT_OLD[1]), ("drat_trim_lane_copy", M.DRAT, M.DRAT_OLD[1]),
             ("encoder", M.ENC[0], M.ENC[1]), ("skeleton_ms06", M.SKEL[0], M.SKEL[1]),
             ("stop_registry", M.REGISTRY[0], M.REGISTRY[1]), ("launch_contract", M.LAUNCH_CONTRACT[0], M.LAUNCH_CONTRACT[1]),
             ("binary_imports", M.BINARY_IMPORTS[0], M.BINARY_IMPORTS[1]),
             ("kissat_source_evidence", M.KISSAT_SOURCE[0], M.KISSAT_SOURCE[1]), ("monitor", M.MONITOR, None),
             ("python_real", PY_REAL[0], PY_REAL[1]), ("direct_pins_evidence", PINS[0], PINS[1]),
             ("bin_date", "/bin/date", None), ("bin_ps", "/bin/ps", None), ("bin_sleep", "/bin/sleep", None)]
    files += [("inherited_marker_" + n, M.OLD + "/cycle2/" + n, h) for n, h in M.OLD_LIVE_MARKERS.items()]
    checks = [dict(check_file(p, h), role=r) for r, p, h in files]
    budget("file checks")
    drat_inodes_distinct = ltype(M.DRAT)[1] != ltype(M.DRAT_OLD[0])[1]
    dirs = {p: ltype(p)[0] for p in (LANE + "/control", RUN + "/control", M.OLD + "/cycle2", LANE + "/tmp",
                                     LANE + "/evidence/pilot-v1")}
    run004 = LANE + "/evidence/pilot-v1/run-004"
    # (3) item CNFs exactly as v17 run_plan builds them
    with open(M.ENC[0], "rb") as f:
        if hashlib.sha256(f.read()).hexdigest() != M.ENC[1]:
            raise SystemExit("REFUSED: encoder pin")
    espec = importlib.util.spec_from_file_location("encode_skel_b_lane", M.ENC[0])
    E = importlib.util.module_from_spec(espec)
    espec.loader.exec_module(E)
    with open(M.SKEL[0], "rb") as f:
        D = json.loads(f.read())
    with open(PINS[0], "rb") as f:
        pins = json.loads(f.read())
    pin_by_b = {c["b_index"]: c for c in pins["cases"]}
    special = [p for p in D["profiles"] if list(p) != M.P0]
    items = []
    for it in M.ITEMS:
        sk = D["skeletons"][it["b"]]
        nv, cl = E.build_v2(D["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special)
        cnf = E.cnf_bytes(nv, cl)
        del cl
        got = (hashlib.sha256(cnf).hexdigest(), len(cnf), cnf.split(b"\n", 1)[0].decode())
        del cnf
        pc = pin_by_b.get(it["b"])
        items.append({"id": it["id"], "b": it["b"], "regenerated": list(got), "item_cnf": list(it["cnf"]),
                      "equal": got == tuple(it["cnf"]),
                      "equals_direct_pins_evidence": pc is not None and pc["direct_cnf"]["sha256"] == got[0]
                      and pc["direct_cnf"]["bytes"] == got[1] and pc["record_cnf_equal"] is True,
                      "lane_original_m2_case": None if pc is None else pc["lane_original_m2_case"],
                      "id_matches_case": it["id"] == "ms06:b%05d:direct" % it["b"]})
        budget("item %s" % it["id"])
    items_ok = (len(items) == 3 and [i["b"] for i in items] == pins["pilot_pick_three_cheapest"]
                and all(i["equal"] and i["equals_direct_pins_evidence"] and i["id_matches_case"]
                        and i["lane_original_m2_case"]["in_frontier_ms06_undecided"] for i in items))
    reg = M.registry_refusals()
    projected_max = M.PROOF_CAP + M.LOG_CAP + 3 * M.RECORD_MAX
    projected_ctrl = M.LOG_CAP + M.CONTROL_PROOF_CAP + 3 * M.RECORD_MAX
    stab_at = clock()
    stab_max = M.stability_refusals(projected_max)
    stab_ctrl = M.stability_refusals(projected_ctrl)
    budget("admission functions")
    rows = M.ps_table()
    child = subprocess.Popen(["/bin/sleep", "1"], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL, start_new_session=True, close_fds=True, cwd=LANE + "/tmp")
    try:
        ident = M.identity_checked(child.pid, os.getpid())
        ident_err = None
    except Exception as exc:
        ident, ident_err = None, repr(exc)
    rows2 = M.ps_table()
    in_table = [r for r in rows2 if r[0] == child.pid]
    rc = child.wait()
    budget("ps")
    consts = {"ITEM_RESERVE": M.ITEM_RESERVE, "CNF_ITEM_MAX": M.CNF_ITEM_MAX, "RUN_RESERVE": M.RUN_RESERVE,
              "CONTROL_RESERVE": M.CONTROL_RESERVE,
              "retained_output_reservation_bytes": M.RUN_RESERVE + M.CONTROL_RESERVE + len(M.ITEMS) * M.ITEM_RESERVE,
              "PROOF_CAP": M.PROOF_CAP, "LOG_CAP": M.LOG_CAP, "RECORD_MAX": M.RECORD_MAX,
              "SOLVER_SECONDS": M.SOLVER_SECONDS, "CHECK_SECONDS": M.CHECK_SECONDS,
              "absolute_end_offset_seconds": M.CONTROLS_WORST_SECONDS + len(M.ITEMS) * M.ITEM_WORST_SECONDS,
              "MAX_CHUNK": M.MAX_CHUNK, "SETTLE": M.SETTLE, "MARGIN": M.MARGIN}
    ok = (diff_ok and items_ok and all(c["ok"] for c in checks if not c["role"].startswith("bin_"))
          and drat_inodes_distinct and all(dirs[p] == "directory" for p in dirs) and not os.path.lexists(run004)
          and reg == [] and stab_max == [] and stab_ctrl == [] and ident_err is None
          and len(in_table) == 1 and in_table[0][2] == child.pid)
    st = os.statvfs(LANE)
    res = {"schema": "PA19-96H-PROBE-PREFLIGHT-V17-v1", "receipt": receipt_path, "receipt_pid": receipt["pid"],
           "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3), "probe_sha256": src_sha,
           "admission": {"free_start": free0, "free_end": st.f_bavail * st.f_frsize, "floor": FLOOR, "markers": mk},
           "runner_diff_check": {"opcodes": ops, "expected": EXPECTED_OPCODES, "ok": diff_ok,
                                 "line_counts": [len(a), len(b)]},
           "items": items, "items_ok": items_ok, "file_checks": checks,
           "drat_inodes_distinct": drat_inodes_distinct, "dirs": dirs, "run004_absent": not os.path.lexists(run004),
           "registry_refusals": reg,
           "stability_refusals": {"evaluated_after_host_clock": stab_at,
                                  "projected_item_max": [projected_max, stab_max],
                                  "projected_control": [projected_ctrl, stab_ctrl]},
           "ps_table_rows": len(rows), "identity_checked_on_sleep_child": {"pid": child.pid, "identity": ident,
                                                                           "error": ident_err, "ps_table_row": in_table,
                                                                           "returncode": rc},
           "v17_constants": consts, "all_ok": ok,
           "scope": "read-only runtime preflight; no runner launch, no solver/checker, no CNF file; one /bin/sleep 1 "
                    "child reaped by wait()"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data), "all_ok", ok, flush=True)


if __name__ == "__main__":
    main()
