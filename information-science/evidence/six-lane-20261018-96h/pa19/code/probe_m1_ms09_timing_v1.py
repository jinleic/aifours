#!/usr/bin/env python3
"""PA19 96h lane probe 4: per-case M1 ms09 split timing (planning data only, never coverage).

Reads, read-only, every regular JSON record directly under OLD/cycle2/part/ms09_s*/ named
batch_*.json (including _r2/_r3 rerun variants, reported separately) and summary_batched.json, and
the frozen v6 M9 contract (pinned) for the s-tag <-> b-index map and M2 placement counts.  Standard
library only; only child processes are /bin/date reads.  Admission: fresh statvfs >= 12.2e9 + 16 MiB,
no NEW-round STOP/HALT marker; self wall budget 280 s.  Output: one exclusive JSON (argv[1]).
These timings are M1-encoder observations; they are NOT M2 costs and NOT scientific results.
"""
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import time

LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h"
OLD = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
C9 = (OLD + "/cycle2/m2-ms09-k1-v6-contract-20261018T075542.json", "072a6172c9cb71ab8110effb24e26eba66b5239594df4300d58c9797b1ec14a8")
FLOOR = 12_200_000_000 + 16 * 1024 * 1024
BUDGET = 280.0
T0 = time.monotonic()


def clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True, check=True,
                          stdin=subprocess.DEVNULL).stdout.strip()


def markers():
    out = []
    for d in (LANE + "/control", RUN + "/control"):
        out += [os.path.join(d, n) for n in sorted(os.listdir(d))
                if re.match(r"(?i)^(stop|halt|sat-candidate)", n) or "HALT" in n]
    return out


def main():
    out_path = os.path.abspath(sys.argv[1])
    if not out_path.startswith(LANE + "/evidence/probes/"):
        raise SystemExit("REFUSED: output outside LANE/evidence/probes")
    st = os.statvfs(LANE)
    free0 = st.f_bavail * st.f_frsize
    mk = markers()
    if free0 < FLOOR or mk:
        raise SystemExit(f"REFUSED free={free0} markers={mk}")
    started = clock()
    raw = open(C9[0], "rb").read()
    if hashlib.sha256(raw).hexdigest() != C9[1]:
        raise SystemExit("REFUSED: contract pin mismatch")
    c9 = json.loads(raw)
    s2b = {c["mapped_A2_tag"]: (c["b_index"], (c["list"] or {}).get("n")) for c in c9["cases"]}
    base = OLD + "/cycle2/part"
    cases = {}
    for d in sorted(os.listdir(base)):
        if not re.fullmatch(r"ms09_s\d{5}", d):
            continue
        if time.monotonic() - T0 > BUDGET:
            raise SystemExit("REFUSED: self budget exhausted; no output")
        p = os.path.join(base, d)
        if not stat.S_ISDIR(os.lstat(p).st_mode):
            continue
        agg = {"primary": {"records": 0, "placements": 0, "solve": 0.0, "check": 0.0, "drat_bytes": 0,
                           "status": {}}, "reruns": {"records": 0}, "summary": None}
        for n in sorted(os.listdir(p)):
            fp = os.path.join(p, n)
            if not stat.S_ISREG(os.lstat(fp).st_mode):
                continue
            if n == "summary_batched.json":
                agg["summary"] = json.load(open(fp))
                continue
            m = re.fullmatch(r"batch_(\d{5})_(\d{5})(_r\d+|_exact)?\.json", n)
            if not m:
                continue
            if m.group(3):
                agg["reruns"]["records"] += 1
                continue
            r = json.load(open(fp))
            a = agg["primary"]
            a["records"] += 1
            a["placements"] += int(m.group(2)) - int(m.group(1)) + 1
            a["solve"] += float(r.get("solve_seconds") or 0)
            a["check"] += float(r.get("check_seconds") or 0)
            a["drat_bytes"] += int(r.get("drat_bytes") or 0)
            a["status"][str(r.get("status"))] = a["status"].get(str(r.get("status")), 0) + 1
        b, n2 = s2b.get(d, (None, None))
        a = agg["primary"]
        agg.update(b_index=b, m2_list_placements=n2,
                   m1_seconds_per_placement=round((a["solve"] + a["check"]) / a["placements"], 4) if a["placements"] else None,
                   m1_drat_bytes_per_placement=round(a["drat_bytes"] / a["placements"]) if a["placements"] else None)
        cases[d] = agg
    st = os.statvfs(LANE)
    res = {"schema": "PA19-96H-PROBE-M1-MS09-TIMING-v1", "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3),
           "probe_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
           "admission": {"free_start": free0, "free_end": st.f_bavail * st.f_frsize, "floor": FLOOR, "markers": mk},
           "contract": {"path": C9[0], "sha256": C9[1]}, "cases": cases,
           "scope": "M1-encoder planning observations only; not M2 cost, not coverage, not a verdict"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data))


if __name__ == "__main__":
    main()
