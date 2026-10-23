#!/usr/bin/env python3
"""PA19 96h lane probe 6: planning-only upper bounds on the independent-M2 first-P1 placement lists
for the 86 open ms06 skeletons (no list is materialized).

Replicates the per-class option rule of the frozen extend_b.py (row classes by P0 membership; a
nonempty class puts at most one row in each block; ok_row(t,e) budget with ns-1 free special
columns and L) and counts assignments with block totals (4,4,2) by dynamic programming, IGNORING
the pairwise class-disjointness test (so the count upper-bounds extend_b's raw assignments), and
counts skeleton automorphisms (P0 column permutations preserving the type multiset, as extend_b).
raw/(2*aut) is reported only as a heuristic orbit scale, never as a list size.  Standard library;
only child processes are /bin/date.  Admission as the other probes; self budget 280 s.
"""
import hashlib
import itertools
import json
import os
import re
import subprocess
import sys
import time

LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19"
RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h"
OLD = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
SK6 = (OLD + "/cycle2/skel-b/skeletons-b-ms06.json", "9ec0fd1dd036cbddf197f495684c2d6a54bc36feff35cb6466799a13493e0488")
EXTB = (OLD + "/src/extend_b.py", "31924ed66099baf6f03436e6d51793549cd45e96416200aeea8c23af651a26d7")
FRONT = (LANE + "/evidence/probes/frontier-v1.json", "0e7e4370961ea8713f8549576a3973c661c1b6499f8a345c74be97d0b4216a46")
FLOOR = 12_200_000_000 + 16 * 1024 * 1024
T0 = time.monotonic()


def clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True, check=True,
                          stdin=subprocess.DEVNULL).stdout.strip()


def pinned(path, h):
    raw = open(path, "rb").read()
    if hashlib.sha256(raw).hexdigest() != h:
        raise SystemExit("REFUSED pin mismatch " + path)
    return raw


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
    D = json.loads(pinned(*SK6))
    pinned(*EXTB)
    fr = json.loads(pinned(*FRONT))
    c0, L = D["c0"], D["L"]
    q = len(D["profiles"][0])
    P0 = [4] + [3] * (q - 1)
    special = [p for p in D["profiles"] if list(p) != P0]
    ns = len(special)

    def ok_row(t, e):
        return t + e - (ns - 1) <= 2 and t + e + (ns - 1) >= 2 - L

    rows = []
    for x in fr["ms06_undecided"]:
        if time.monotonic() - T0 > 280:
            raise SystemExit("REFUSED: self budget exhausted; no output")
        b = x["b_index"]
        sk = D["skeletons"][b]
        types = [tuple(t) for t in sk["types"]]
        deg = [0] * c0
        for t in types:
            for v in t:
                deg[v] += 1
        member = [frozenset(t) for t in types]
        for v in range(c0):
            member += [frozenset([v])] * (4 - deg[v])
        member += [frozenset()] * sk["empty"]
        classes = []
        for ms in member:
            for cl in classes:
                if cl[0] == ms:
                    cl[1] += 1
                    break
            else:
                classes.append([ms, 1])
        opts = []
        for ms, cap in classes:
            t = len(ms)
            per_block = 1 if ms else cap
            o = []
            for a in range(min(per_block, cap) + 1):
                for bb in range(min(per_block, cap - a) + 1):
                    for p in range(min(per_block, cap - a - bb) + 1):
                        rest = cap - a - bb - p
                        good = not ((a + bb and not ok_row(t, 1)) or (p and not ok_row(t, -1)) or (rest and not ok_row(t, 0)))
                        if good:
                            o.append((a, bb, p))
            opts.append(o)
        dp = {(0, 0, 0): 1}
        for o in opts:
            nd = {}
            for (sa, sb, sp), cnt in dp.items():
                for a, bb, p in o:
                    k = (sa + a, sb + bb, sp + p)
                    if k[0] <= 4 and k[1] <= 4 and k[2] <= 2:
                        nd[k] = nd.get(k, 0) + cnt
            dp = nd
        raw_ub = dp.get((4, 4, 2), 0)
        tset = sorted(tuple(sorted(t)) for t in types)
        aut = sum(1 for perm in itertools.permutations(range(c0))
                  if sorted(tuple(sorted(perm[v] for v in t)) for t in types) == tset)
        rows.append({"b_index": b, "s_tag": x["s_tag"], "types": sk["types"], "empty": sk["empty"],
                     "classes": len(classes), "raw_upper_bound": raw_ub, "aut": aut,
                     "orbit_scale_heuristic": raw_ub / (2 * aut) if aut else None})
    rows.sort(key=lambda r: r["raw_upper_bound"])
    res = {"schema": "PA19-96H-PROBE-MS06-DP-v1", "started_host_clock": started, "finished_host_clock": clock(),
           "elapsed_seconds": round(time.monotonic() - T0, 3),
           "probe_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
           "admission": {"free": free0, "floor": FLOOR, "markers": mk},
           "pins": {"skeletons": SK6, "extend_b": EXTB, "frontier": FRONT},
           "rows": rows, "totals": {"cases": len(rows), "raw_upper_bound_sum": sum(r["raw_upper_bound"] for r in rows)},
           "scope": "planning upper bounds only; not list sizes, not coverage"}
    data = json.dumps(res, indent=1, sort_keys=True).encode()
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data))


if __name__ == "__main__":
    main()
