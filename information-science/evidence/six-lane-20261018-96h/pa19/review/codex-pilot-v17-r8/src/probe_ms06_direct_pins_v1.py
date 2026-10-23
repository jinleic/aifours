#!/usr/bin/env python3
"""PA19 96h lane probe 11: read-only direct-CNF pins and old-status provenance for seven open ms06 cases
(b144, b156, b177, b187, b189, b202, b295), plus the frozen choice of the three cheapest for the first ms06
direct native pilot (parent instruction, 2026-10-19 ~02:13 PDT).

For each case it:
  * checks lane-original M2 identity: the case is in frontier-v1 ms06_undecided (b_index and s_tag), and the
    frontier skeleton fields equal the pinned skeleton file entry. This is the lane-original M2 frontier, not
    an M2H view;
  * regenerates the whole-case direct CNF in process with the vendored encoder (d0002e60...), using exactly
    the call of the old direct attempts: build_v2(c0, types, empty, special) then cnf_bytes. It records
    sha256, bytes and header, and compares them with the old record's cnf_sha256/cnf_bytes;
  * copies the old status provenance from the pinned record: rev-15 records via the v6 ms06 contract rows
    (original_record, original_sha256); b295 via the frontier v6 attempt pin. Fields: solver, rc, solve
    seconds, check seconds, drat-trim status lines, transport revision and the reason the record does not
    count.
Ranking: by observed old solve_seconds + check_seconds; a case without an observed check (b295) ranks after
every fully observed case. The three cheapest become the pilot items.
Standard library plus the in-process encoder; the only child process is /bin/date. Admission: fresh statvfs
>= 12.2e9 + 16 MiB and no STOP/HALT/sat-candidate marker. Self budget 280 s; no output if it is exceeded. The
exclusive receipt with the PID is written before any work, and the output is created exclusively under
LANE/evidence/probes/. No CNF file is written; nothing in the old lane is written.
Usage: probe_ms06_direct_pins_v1.py OUT_JSON
"""
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import time

sys.dont_write_bytecode = True
T0 = time.monotonic()
LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h"
OLD = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
SK6 = (OLD + "/cycle2/skel-b/skeletons-b-ms06.json", "9ec0fd1dd036cbddf197f495684c2d6a54bc36feff35cb6466799a13493e0488")
FRONT = (LANE + "/evidence/probes/frontier-v1.json", "0e7e4370961ea8713f8549576a3973c661c1b6499f8a345c74be97d0b4216a46")
M6C = (OLD + "/cycle2/m2-ms06-initial-v6-contract-20261018T075542.json",
       "dc343809b7597804dde1c71802edd142fe87472d5e20f6220c21e7f234fc2413")
ENC = (LANE + "/code/vendor/encode_skel_b.py", "d0002e60d11ef5cba568309fde5b15e29280ca127bc0e6bb1f4d22929a5628e5")
CASES = (144, 156, 177, 187, 189, 202, 295)
P0 = [4, 3, 3, 3, 3, 3]
FLOOR = 12_200_000_000 + 16 * 1024 * 1024
BUDGET = 280.0


def clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True, check=True,
                          stdin=subprocess.DEVNULL).stdout.strip()


def budget(stage):
    if time.monotonic() - T0 > BUDGET:
        raise SystemExit("REFUSED: self budget exhausted at %s; no output" % stage)


def pinned(path, h):
    with open(path, "rb") as f:
        raw = f.read()
    if hashlib.sha256(raw).hexdigest() != h:
        raise SystemExit("REFUSED pin mismatch " + path)
    return raw


def provenance(b, front, m6rows):
    row = m6rows.get(b)
    if row is not None and row["original_status"] is not None:
        rec = json.loads(pinned(OLD + "/" + row["original_record"], row["original_sha256"]))
        dt = rec.get("drat_trim") or {}
        return {"route": "rev-15 staged direct (run_m2_15.py)", "record": row["original_record"],
                "record_sha256": row["original_sha256"], "record_pinned_by": "v6 ms06 contract rows (dc343809...)",
                "status": rec["status"], "encoder": rec.get("encoder"), "solver": rec.get("solver"),
                "solver_version": (rec.get("solver_info") or {}).get("version"), "solver_rc": rec.get("solver_rc"),
                "solver_stop": rec.get("solver_stop"), "solve_seconds": rec.get("solve_seconds"),
                "check_seconds": rec.get("check_seconds"), "drat_trim_s_lines": dt.get("s_lines"),
                "drat_trim_verified": rec.get("drat_trim_verified"), "drat_bytes": rec.get("drat_bytes"),
                "drat_sha256": rec.get("drat_sha256"), "stream_check_revision": rec.get("stream_check_revision"),
                "staged": rec.get("staged"), "cnf_sha256": rec["cnf_sha256"], "cnf_bytes": rec["cnf_bytes"],
                "why_not_counted": "case is open in the frozen lane-original frontier (STATUS17 M2 open list); this "
                                   "rev-15 staged-transport record is not part of any accepted M2 coverage and its "
                                   "proof was not retained"}
    v6 = front["ms06_v6_attempt_records"].get(str(b))
    if v6 is not None:
        rec = json.loads(pinned(OLD + "/" + v6["record"], v6["sha256"]))
        nr = rec["native_result"]
        return {"route": "v6 supervised direct (m2_native_staged_v6.py)", "record": v6["record"],
                "record_sha256": v6["sha256"], "record_pinned_by": "frontier-v1 ms06_v6_attempt_records",
                "status": rec["status"], "encoder": rec.get("encoder"), "solver": nr.get("solver_command"),
                "solver_rc": nr.get("solver_rc"), "solver_stop": nr.get("solver_stop"),
                "solve_seconds": nr.get("solve_seconds"), "check_seconds": None,
                "solver_status_lines": nr["solver_collector"].get("status_lines"),
                "proof_raw_bytes": (nr.get("proof_stream") or {}).get("raw_bytes"),
                "checker_collector": nr.get("checker_collector"), "resource_refusal": nr.get("resource_refusal"),
                "unknown_reason": nr.get("unknown_reason"), "chunk_stop": nr.get("chunk_stop"),
                "cnf_sha256": rec["cnf_sha256"], "cnf_bytes": rec["cnf_bytes"],
                "why_not_counted": "solver rc 20 is not a certificate; the checker was refused at its gate "
                                   "(STOP-K1 pause), so the attempt is UNKNOWN"}
    return None


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
               "scope": "read-only pins/provenance; children /bin/date only; no solver/checker; no CNF file"}
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
    D = json.loads(pinned(*SK6))
    front = json.loads(pinned(*FRONT))
    m6rows = {r["b_index"]: r for r in json.loads(pinned(*M6C))["rows"]}
    if not (D["c0"] == 6 and D["L"] == 1 and sorted(map(list, D["profiles"])) == [P0] * 6 + [[4, 4, 3, 3, 3, 2]] * 2):
        raise SystemExit("REFUSED: unexpected ms06 header")
    special = [p for p in D["profiles"] if list(p) != P0]
    openmap = {x["b_index"]: x for x in front["ms06_undecided"]}
    pinned(*ENC)
    spec = importlib.util.spec_from_file_location("encode_skel_b_lane", ENC[0])
    E = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(E)
    cases = []
    for b in CASES:
        x = openmap.get(b)
        sk = D["skeletons"][b]
        t1 = time.monotonic()
        nv, cl = E.build_v2(D["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special)
        cnf = E.cnf_bytes(nv, cl)
        del cl
        got = {"sha256": hashlib.sha256(cnf).hexdigest(), "bytes": len(cnf),
               "header": cnf.split(b"\n", 1)[0].decode(), "build_seconds": round(time.monotonic() - t1, 3)}
        del cnf
        prov = provenance(b, front, m6rows)
        cases.append({"b_index": b, "item_id": "ms06:b%05d:direct" % b,
                      "lane_original_m2_case": {"multiset": "ms06", "b_index": b,
                                                "s_tag": None if x is None else x["s_tag"],
                                                "in_frontier_ms06_undecided": x is not None,
                                                "frontier_fields_equal": x is not None and x["skeleton_types"] == sk["types"]
                                                and x["skeleton_empty"] == sk["empty"]},
                      "skeleton": {"types": sk["types"], "empty": sk["empty"]},
                      "direct_cnf": got,
                      "record_cnf_equal": prov is not None and (prov["cnf_sha256"], prov["cnf_bytes"]) == (got["sha256"], got["bytes"]),
                      "provenance": prov})
        budget("case %d" % b)

    def cost(c):
        p = c["provenance"] or {}
        s, k = p.get("solve_seconds"), p.get("check_seconds")
        full = s is not None and k is not None
        return (0 if full else 1, (s or 0) + (k or 0), c["b_index"])

    ranked = sorted(cases, key=cost)
    pick = [c["b_index"] for c in ranked[:3]]
    checks = {"all_in_lane_original_frontier": all(c["lane_original_m2_case"]["in_frontier_ms06_undecided"] for c in cases),
              "frontier_fields_equal": all(c["lane_original_m2_case"]["frontier_fields_equal"] for c in cases),
              "all_regenerated_cnf_equal_records": all(c["record_cnf_equal"] for c in cases),
              "all_have_provenance": all(c["provenance"] is not None for c in cases),
              "picked_three_fully_observed": all(cost(c)[0] == 0 for c in ranked[:3])}
    st = os.statvfs(LANE)
    res = {"schema": "PA19-96H-PROBE-MS06-DIRECT-PINS-v1", "receipt": receipt_path, "receipt_pid": receipt["pid"],
           "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3), "probe_sha256": src_sha,
           "admission": {"free_start": free0, "free_end": st.f_bavail * st.f_frsize, "floor": FLOOR, "markers": mk},
           "pins": {"skeletons": SK6, "frontier": FRONT, "m6_contract": M6C, "encoder": ENC},
           "construction": "encode_skel_b.build_v2(6, types, empty, [[4,4,3,3,3,2]]*2) then cnf_bytes (whole case, "
                           "no placement list), identical to the old direct attempts",
           "cases": cases,
           "ranking": [{"b_index": c["b_index"], "observed_solve_plus_check_seconds": cost(c)[1],
                        "fully_observed": cost(c)[0] == 0} for c in ranked],
           "pilot_pick_three_cheapest": pick, "checks": checks, "all_ok": all(checks.values()),
           "scope": "pins and provenance only; old solver/check observations are not certificates; no case is "
                    "counted or closed by this probe; no PA(19,8,6) claim"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    budget("before output")
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data), "all_ok", res["all_ok"], "pick", pick, flush=True)


if __name__ == "__main__":
    main()
