#!/usr/bin/env python3
"""PA19 96h lane probe 15: read-only item-pin / case-coverage / runtime preflight of the six Wave 1 runners
of notes/production-plan-v1.md (review/production-plan-v1.json).

Each runner is an item-only delta. The ms09 PLACEMENT runners v20, v22, v24 derive from v16 (0ef4cfdc...,
build_partbatch). The ms06 DIRECT runners v21, v23, v25 derive from v17 (96e179a4..., build_v2). Only the
docstring scope line and the ITEMS list change.

Per runner:
  (1) runner and base pins; difflib non-equal opcodes exactly the frozen ones;
  (2) ITEMS ids exactly the frozen Wave 1 ids, equal to the pins evidence evidence/probes/production-wave1-pins-v1.json;
  (3) each item CNF regenerated through the runner module's own constants and generation path, exactly as its
      run_plan does: ms09 E.build_partbatch(c0, types, empty, special, [list[i] for lo..hi]) after the
      runner's own list checks (read_pinned list, num_placements == len(placements) == denominator); ms06
      E.build_v2(c0, types, empty, special). (sha256, bytes, header) must equal the runner pin and the pins
      evidence;
  (4) case coverage: the case is open in parent frontier v4 (5bc07039...) with equal skeleton fields, and is
      not among the frontier's new_case_closures*; ms09 list path/SHA-256/n equal the frontier entry;
  (5) lstat type (regular, not a symlink) and SHA-256 of every path the runner hashes, reads or executes;
      planned out dir absent;
  (6) registry_refusals() and stability_refusals(projected) on the live files (expected []); reservation and
      chunk fit from the runner constants.
Across runners: all 18 item ids distinct, and no case appears in two runs except none (Wave 1 has disjoint
cases).
No runner launch, no solver/checker, no CNF file. The only child process is /bin/date. Nothing is written under
LANE/tmp or evidence/pilot-v1. Admission: fresh statvfs >= 12.2e9 + 16 MiB and no STOP/HALT/sat-candidate
marker. Self budget 280 s. The exclusive receipt with the PID is written before any work.
Usage: probe_preflight_wave1_v1.py OUT_JSON
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
PINS = (LANE + "/evidence/probes/production-wave1-pins-v1.json", "b8822c2c454c6db8c9a6a11485be7f763d5383db7a212cf86d7d08438639e930")
FRONT4 = (RUN + "/review/pa19-parent-frontier-v4.json", "5bc070391d61c6e65fb49c9851d776b5468bcd4fa60bf9bdb04a6c079c52adc4")
PY_REAL = ("/opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/bin/python3.14",
           "cbf84109626aa1013bbe408fbb9590bd0f1c1548f038b2221c6b8b87de26ca43")
OPS16 = [["replace", 57, 58, 57, 58], ["replace", 110, 119, 110, 119]]
OPS17 = [["replace", 57, 58, 57, 58], ["replace", 110, 116, 110, 116]]
RUNNERS = [
    ("v20", "4ad50904ebe74c2360abe60fbf7e3a39a20a8b005a52636762b9369fcd99983a", V16, OPS16, "ms09", "run-007",
     ["b00009:00000-00814", "b00025:00000-00099", "b00069:00000-00099"]),
    ("v21", "70de3718a3430f956706f532183eedac729921cef26142c552d7faf0d44f40c7", V17, OPS17, "ms06", "run-008",
     ["ms06:b00088:direct", "ms06:b00089:direct", "ms06:b00186:direct"]),
    ("v22", "ff87f60cfa282c2e4fb7419efe63c0dc5ceb2417e0f24eb01268a0c32effe26a", V16, OPS16, "ms09", "run-009",
     ["b00010:00000-00099", "b00067:00000-00099", "b00011:00000-00099"]),
    ("v23", "983928f6134e328b8b537a0db26c346ccd1c5a3bd49be204fbd36412e61f7e3a", V17, OPS17, "ms06", "run-010",
     ["ms06:b00154:direct", "ms06:b00168:direct", "ms06:b00169:direct"]),
    ("v24", "ef905ede09081555429e779e07963d4b09867ca49aca449550c28f3de8243d75", V16, OPS16, "ms09", "run-011",
     ["b00008:00000-00099", "b00049:00000-00099", "b00061:00000-00099"]),
    ("v25", "4cd01559a21fc92243e13c273a29c5f9ab69a38ad7ac222f5dc1a538bbd06288", V17, OPS17, "ms06", "run-012",
     ["ms06:b00282:direct", "ms06:b00299:direct", "ms06:b00269:direct"]),
]
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
               "scope": "read-only Wave 1 preflight; children /bin/date only; no CNF file"}
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
    pins = pinned_json(*PINS)
    pin_by_id = {i["id"]: i for i in pins["items"]}
    f4 = pinned_json(*FRONT4)
    open6 = {x["b_index"]: x for x in f4["ms06_undecided"]}
    open9 = {x["b_index"]: x for x in f4["ms09_undecided"]}
    closed = set()
    for k, v in f4.items():
        if k.startswith("new_case_closures"):
            for c in v:
                closed.add(c.get("case"))
    results, all_ids, all_cases = [], [], []
    for v, sha, base, ops_exp, fam, run_dir, ids in RUNNERS:
        path = LANE + "/code/pilot_file_drat_%s.py" % v
        rn, bs = check_file(path, sha), check_file(*base)
        if not (rn["ok"] and bs["ok"]):
            raise SystemExit("REFUSED: runner/base pin mismatch " + v)
        with open(base[0], "rb") as f:
            a = f.read().decode().splitlines(keepends=True)
        with open(path, "rb") as f:
            b = f.read().decode().splitlines(keepends=True)
        ops = [list(op) for op in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes() if op[0] != "equal"]
        spec = importlib.util.spec_from_file_location("pilot_%s_readonly" % v, path)
        M = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(M)  # constants only; main() is not called
        with open(M.ENC[0], "rb") as f:
            if hashlib.sha256(f.read()).hexdigest() != M.ENC[1]:
                raise SystemExit("REFUSED: encoder pin")
        espec = importlib.util.spec_from_file_location("encode_skel_b_lane_%s" % v, M.ENC[0])
        E = importlib.util.module_from_spec(espec)
        espec.loader.exec_module(E)
        D = pinned_json(*M.SKEL)
        special = [p for p in D["profiles"] if list(p) != M.P0]
        items = []
        for it in M.ITEMS:
            sk = D["skeletons"][it["b"]]
            rec = {"id": it["id"], "b": it["b"]}
            if fam == "ms09":
                Ej = pinned_json(*it["list"])
                rec["list_checks_like_runner"] = Ej["num_placements"] == len(Ej["placements"]) == it["denominator"]
                nv, cl = E.build_partbatch(D["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special,
                                           [Ej["placements"][i] for i in range(it["lo"], it["hi"] + 1)])
                x = open9.get(it["b"])
                case = "ms09_b%05d" % it["b"]
                rec["coverage"] = {"case": case, "interval": [it["lo"], it["hi"]], "denominator": it["denominator"],
                                   "open_in_frontier_v4": x is not None and case not in closed,
                                   "list_equals_frontier": x is not None and it["list"][0] == M.OLD + "/" + x["list"]["path"]
                                   and it["list"][1] == x["list"]["sha256"] and it["denominator"] == x["list"]["n"],
                                   "skeleton_fields_equal": x is not None and x["skeleton_types"] == sk["types"]
                                   and x["skeleton_empty"] == sk["empty"], "s_tag": None if x is None else x["s_tag"]}
            else:
                nv, cl = E.build_v2(D["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special)
                x = open6.get(it["b"])
                case = "ms06_b%05d" % it["b"]
                rec["coverage"] = {"case": case, "whole_case_direct": True,
                                   "open_in_frontier_v4": x is not None and case not in closed
                                   and ("ms06:b%05d:direct" % it["b"]) not in closed,
                                   "skeleton_fields_equal": x is not None and x["skeleton_types"] == sk["types"]
                                   and x["skeleton_empty"] == sk["empty"], "s_tag": None if x is None else x["s_tag"]}
            cnf = E.cnf_bytes(nv, cl)
            del cl
            got = [hashlib.sha256(cnf).hexdigest(), len(cnf), cnf.split(b"\n", 1)[0].decode()]
            del cnf
            pe = pin_by_id.get(it["id"])
            rec.update(regenerated=got, runner_pin=list(it["cnf"]), equal_runner_pin=got == list(it["cnf"]),
                       equal_pins_evidence=pe is not None and [pe["cnf"]["sha256"], pe["cnf"]["bytes"], pe["cnf"]["header"]] == got)
            items.append(rec)
            all_ids.append(it["id"])
            all_cases.append(case)
            budget("item %s" % it["id"])
        files = [("runner", path, sha), ("base", base[0], base[1]), ("kissat", M.KISSAT[0], M.KISSAT[1]),
                 ("drat_trim_old", M.DRAT_OLD[0], M.DRAT_OLD[1]), ("drat_trim_lane_copy", M.DRAT, M.DRAT_OLD[1]),
                 ("encoder", M.ENC[0], M.ENC[1]), ("skeleton", M.SKEL[0], M.SKEL[1]),
                 ("stop_registry", M.REGISTRY[0], M.REGISTRY[1]),
                 ("launch_contract", M.LAUNCH_CONTRACT[0], M.LAUNCH_CONTRACT[1]),
                 ("binary_imports", M.BINARY_IMPORTS[0], M.BINARY_IMPORTS[1]),
                 ("kissat_source_evidence", M.KISSAT_SOURCE[0], M.KISSAT_SOURCE[1]), ("monitor", M.MONITOR, None),
                 ("python_real", PY_REAL[0], PY_REAL[1]), ("bin_date", "/bin/date", None), ("bin_ps", "/bin/ps", None)]
        if fam == "ms09":
            files += [("item_list_" + it["id"], it["list"][0], it["list"][1]) for it in M.ITEMS]
        files += [("inherited_marker_" + n, M.OLD + "/cycle2/" + n, h) for n, h in M.OLD_LIVE_MARKERS.items()]
        checks = [dict(check_file(p, h), role=r) for r, p, h in files]
        drat_distinct = ltype(M.DRAT)[1] != ltype(M.DRAT_OLD[0])[1]
        out_dir = LANE + "/evidence/pilot-v1/" + run_dir
        reg = M.registry_refusals()
        projected_max = M.PROOF_CAP + M.LOG_CAP + 3 * M.RECORD_MAX
        projected_ctrl = M.LOG_CAP + M.CONTROL_PROOF_CAP + 3 * M.RECORD_MAX
        stab_at = clock()
        stab = [M.stability_refusals(projected_max), M.stability_refusals(projected_ctrl)]
        offset = M.CONTROLS_WORST_SECONDS + len(M.ITEMS) * M.ITEM_WORST_SECONDS
        consts = {"items": len(M.ITEMS), "CNF_ITEM_MAX": M.CNF_ITEM_MAX, "ITEM_RESERVE": M.ITEM_RESERVE,
                  "retained_output_reservation_bytes": M.RUN_RESERVE + M.CONTROL_RESERVE + len(M.ITEMS) * M.ITEM_RESERVE,
                  "absolute_end_offset_seconds": offset, "chunk_fit_ok": offset + M.SETTLE + M.MARGIN <= M.MAX_CHUNK}
        ok = (ops == ops_exp and [it["id"] for it in M.ITEMS] == ids
              and all(i["equal_runner_pin"] and i["equal_pins_evidence"] and i["coverage"]["open_in_frontier_v4"]
                      and i["coverage"]["skeleton_fields_equal"] and i.get("list_checks_like_runner", True)
                      and i["coverage"].get("list_equals_frontier", True) for i in items)
              and all(c["ok"] for c in checks if not c["role"].startswith("bin_")) and drat_distinct
              and not os.path.lexists(out_dir) and reg == [] and stab == [[], []] and consts["chunk_fit_ok"])
        results.append({"runner": v, "runner_sha256": sha, "base": base, "family": fam, "planned_out_dir": out_dir,
                        "out_dir_absent": not os.path.lexists(out_dir), "diff_opcodes": ops, "diff_expected": ops_exp,
                        "items": items, "file_checks": checks, "drat_inodes_distinct": drat_distinct,
                        "registry_refusals": reg, "stability_refusals": {"evaluated_after_host_clock": stab_at,
                                                                         "item_max_and_control": stab},
                        "constants": consts, "ok": ok})
        budget("runner %s" % v)
    cross = {"ids_distinct": len(set(all_ids)) == len(all_ids) == 18, "cases_distinct": len(set(all_cases)) == len(all_cases),
             "ids_equal_pins_evidence": sorted(all_ids) == sorted(pin_by_id)}
    ok_all = all(r["ok"] for r in results) and all(cross.values())
    st = os.statvfs(LANE)
    res = {"schema": "PA19-96H-PROBE-PREFLIGHT-WAVE1-v1", "receipt": receipt_path, "receipt_pid": receipt["pid"],
           "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3), "probe_sha256": src_sha,
           "admission": {"free_start": free0, "free_end": st.f_bavail * st.f_frsize, "floor": FLOOR, "markers": mk},
           "runners": results, "cross_checks": cross, "all_ok": ok_all,
           "scope": "item pins, case coverage, runtime path pins and admission functions; framework unchanged from the "
                    "reviewed bases (v16: Codex r7 + constant diffs, run-003; v17: Codex r8, runs 004-006) and not "
                    "re-probed; no launch, no solver/checker"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data), "all_ok", ok_all, flush=True)


if __name__ == "__main__":
    main()
