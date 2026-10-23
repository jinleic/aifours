#!/usr/bin/env python3
"""PA19 96h lane probe 5: planning cost model for the remaining ms09 M2 cover (NOT a result).

Inputs (pinned): frontier-v1.json, m1-ms09-timing-v1.json, the frozen v6 M9 contract, and the eight
old M2 kissat timing receipts (v6 b5 [0..99]/[100..199]; calibration b4[100..199], b9/b13/b20/b31/b55
[0..99], b70[0..24]).  Model per open ms09 case, in order: (a) measured M2 rate if a receipt exists;
(b) the M2-hard class {b4,b5,b6,b7} (16/15 private rows, few multi-quad rows) at the worst measured M2
rate; (c) otherwise max(M1 rate, 0.12 s/placement); (d) no data: 0.15 s/placement.  Output gives
per-case remaining placements (lane-original layer: pending + reserved intervals of the v6 contract),
estimated seconds, and cumulative closure order (cheapest case first).  Planning figures only.
Standard library; only child processes are /bin/date.  Admission as the other probes.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h"
OLD = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
PINS = {
    LANE + "/evidence/probes/frontier-v1.json": "0e7e4370961ea8713f8549576a3973c661c1b6499f8a345c74be97d0b4216a46",
    LANE + "/evidence/probes/m1-ms09-timing-v1.json": "46d96ef0a028bde842ebe9436626ebc7099f7e9683b54418d5de9d21bdef147a",
    OLD + "/cycle2/m2-ms09-k1-v6-contract-20261018T075542.json": "072a6172c9cb71ab8110effb24e26eba66b5239594df4300d58c9797b1ec14a8",
}
M2_RECEIPTS = {  # b_index: (path, placements in the interval)
    5: [(OLD + "/cycle2/m2part_drat/ms09_b00005/batch_00000_00099_k1_v6.json", 100),
        (OLD + "/cycle2/m2part_drat/ms09_b00005/batch_00100_00199_k1_v6.json", 100)],
    4: [(OLD + "/cycle2/m2-kissat-calibration-20261018T022704/calibration_ms09_b00004_00100_00199.json", 100)],
    9: [(OLD + "/cycle2/m2-kissat-calibration-20261018T022704/calibration_ms09_b00009_00000_00099.json", 100)],
    13: [(OLD + "/cycle2/m2-kissat-strata-calibration-20261018T030136/calibration_ms09_b00013_00000_00099.json", 100)],
    20: [(OLD + "/cycle2/m2-kissat-strata-calibration-20261018T030136/calibration_ms09_b00020_00000_00099.json", 100)],
    31: [(OLD + "/cycle2/m2-kissat-strata-calibration-20261018T030136/calibration_ms09_b00031_00000_00099.json", 100)],
    55: [(OLD + "/cycle2/m2-kissat-strata-calibration-20261018T030136/calibration_ms09_b00055_00000_00099.json", 100)],
    70: [(OLD + "/cycle2/m2-kissat-strata-calibration-20261018T030136/calibration_ms09_b00070_00000_00024.json", 25)],
}
HARD_CLASS = {4, 5, 6, 7}
PILOT = {5: "b5 [200..350] in pilot", 70: "b70 [0..24] in pilot"}
FLOOR = 12_200_000_000 + 16 * 1024 * 1024
T0 = time.monotonic()


def clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True, check=True,
                          stdin=subprocess.DEVNULL).stdout.strip()


def main():
    out_path = os.path.abspath(sys.argv[1])
    if not out_path.startswith(LANE + "/evidence/probes/"):
        raise SystemExit("REFUSED: output outside probes")
    st = os.statvfs(LANE)
    free0 = st.f_bavail * st.f_frsize
    mk = [os.path.join(d, n) for d in (LANE + "/control", RUN + "/control") for n in sorted(os.listdir(d))
          if re.match(r"(?i)^(stop|halt|sat-candidate)", n) or "HALT" in n]
    if free0 < FLOOR or mk:
        raise SystemExit(f"REFUSED free={free0} markers={mk}")
    started = clock()
    J = {}
    for p, h in PINS.items():
        raw = open(p, "rb").read()
        if hashlib.sha256(raw).hexdigest() != h:
            raise SystemExit("REFUSED pin mismatch " + p)
        J[p] = json.loads(raw)
    fr = J[LANE + "/evidence/probes/frontier-v1.json"]
    m1 = J[LANE + "/evidence/probes/m1-ms09-timing-v1.json"]["cases"]
    c9 = J[OLD + "/cycle2/m2-ms09-k1-v6-contract-20261018T075542.json"]
    m1_rate = {v["b_index"]: v["m1_seconds_per_placement"] for v in m1.values() if v["b_index"] is not None}
    m2 = {}
    receipts = {}
    worst = 0.0
    for b, lst in M2_RECEIPTS.items():
        secs = pl = 0
        for p, n in lst:
            r = json.load(open(p))
            nr = r.get("native_result") or {}
            s = float(r.get("solve_seconds") or nr.get("solve_seconds") or 0)
            c = float(r.get("check_seconds") or nr.get("check_seconds") or 0)
            secs += s + c
            pl += n
            receipts[p] = {"sha256": hashlib.sha256(open(p, "rb").read()).hexdigest(), "solve": s, "check": c,
                           "placements": n}
        m2[b] = secs / pl
        worst = max(worst, m2[b])
    interval_size = {}
    for c in c9["cases"]:
        for iv in c["intervals"]:
            interval_size[iv["id"]] = iv["indices"][1] - iv["indices"][0] + 1
    remaining_ids = {}
    for iid in list(c9["pending_order"]) + list(c9["reserved_ids"]):
        remaining_ids.setdefault(int(iid.split(":")[0][1:]), []).append(iid)
    rows = []
    for x in fr["ms09_undecided"]:
        b = x["b_index"]
        ids = remaining_ids.get(b, [])
        if b == 5:
            ids = ["b00005:00200-00299", "b00005:00300-00350"]
        pl = sum(interval_size[i] for i in ids)
        if b in m2:
            rate, basis = (worst, "M2-hard class worst measured M2") if b in HARD_CLASS and m2[b] < worst else (m2[b], "measured M2")
        elif b in HARD_CLASS:
            rate, basis = worst, "M2-hard class (assumed) at worst measured M2 rate"
        elif b in m1_rate and m1_rate[b] is not None:
            rate, basis = max(m1_rate[b], 0.12), "max(M1 rate, 0.12)"
        else:
            rate, basis = 0.15, "default 0.15 (no M1/M2 data)"
        rows.append({"b_index": b, "s_tag": x["s_tag"], "remaining_intervals": len(ids), "remaining_placements": pl,
                     "rate_s_per_placement": round(rate, 4), "basis": basis, "est_seconds": round(rate * pl),
                     "pilot": PILOT.get(b)})
    rows.sort(key=lambda r: (r["est_seconds"], r["b_index"]))
    cum = 0
    for r in rows:
        cum += r["est_seconds"]
        r["cumulative_est_seconds"] = cum
    res = {"schema": "PA19-96H-PROBE-MS09-COST-MODEL-v1", "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3),
           "probe_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
           "admission": {"free": free0, "floor": FLOOR, "markers": mk}, "pins": PINS, "m2_receipts": receipts,
           "m2_rates": m2, "worst_measured_m2_rate": worst, "rows": rows,
           "totals": {"cases": len(rows), "remaining_placements": sum(r["remaining_placements"] for r in rows),
                      "est_seconds_single_process": cum},
           "scope": "planning estimate only; not accepted, not coverage; rates are solve+check seconds per placement"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data))


if __name__ == "__main__":
    main()
