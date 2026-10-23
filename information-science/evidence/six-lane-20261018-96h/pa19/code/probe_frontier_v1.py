#!/usr/bin/env python3
"""PA19 96h lane probe 2: freeze the exact lane-original M2 frontier (151 = ms06 86 + ms09 65).

Read-only, standard library only; only child processes are /bin/date clock reads.
Admission (fail closed): fresh statvfs free >= 12.2e9 + 16 MiB and no NEW-round STOP/HALT marker in
LANE/control or RUN/control. Every input is SHA-256 pinned against the value named in the closeout
records; any mismatch refuses. Output: one exclusive-created JSON (argv[1]).
The measured M2H views (v6_3 3/5424, v6_4 1/5424) are recorded separately and never merged.
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
OLD_RUN = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16"
FLOOR = 12_200_000_000 + 16 * 1024 * 1024
T0 = time.monotonic()

PINS = {
    "STATUS17.json": "b7bb242bb0304ba5d0a10b8d0b113f34813244f9be74134ec91b067d0acfc223",
    "cycle2/skel-b/compare-map-ms09.json": "d06bb6fce38a2fbf96cf7d84d18331ec8233b54ccdccfc4b4ec759f281aa5282",
    "cycle2/skel-b/compare-map-ms06.json": "c0bffb9be9f97a4a10f79ab64df4903b2fb41fecafe817933c2bbef35393e2f7",
    "cycle2/skel-b/skeletons-b-ms09.json": "7c46ebbad3389476407e99807593287a8b3bb6c6a80f34574f0e9c00134293d0",
    "cycle2/skel-b/skeletons-b-ms06.json": "9ec0fd1dd036cbddf197f495684c2d6a54bc36feff35cb6466799a13493e0488",
    "cycle2/m2-ms09-k1-v6-contract-20261018T075542.json": "072a6172c9cb71ab8110effb24e26eba66b5239594df4300d58c9797b1ec14a8",
    "cycle2/structural-skip-overlay-b30-b44-20261018T082510.json": "b718bd1268eda6565dd4988ed0b9ad51cb0c77cb9837bbe8b07fdd869c02e5b9",
    "cycle2/m2h-inventory-20261018T120437-1792350277375607000.json": "49972a359fbaa64cc3b43acb8f2e2e912d9305d540682568284c1cedd1eb5118",
    "cycle2/m2h-inventory-20261018T133100-1792355460018218000.json": "e5242b5aad81f9974147e7a79f9e65a918bd324b8487df7f59075a86ba3237d5",
    "cycle2/pa19-lane-final-summary-20261018T1641.md": "f5f6cfb817a67657f68d1a67dd936794d2bd81c79685d144ed256c58c72584df",
    "cycle2/pa19-lane-final-summary-20261018T1641-addendum1.md": "57904866786f4d785b7d361bc8c8e30906d26e21e36f3444e1895d66feeb9c54",
}
OLD_RUN_PINS = {
    "review/pa19-b30-b44-parent-verdict-v1.md": "0e56374c3967ef5c1e3425804ce7eb5c89bd0233d36d1240d8e417db8c8d5d1e",
    "review/pa19-ms09-b3-structural-parent-v1.md": "f311d68df95232293f855c5ffe15e08e6a90fba4ed799f0f1c8e559d91716466",
    "review/pa19-final-monitor-ownership-and-corrections-v1.json": None,
    "review/pa19-gps-written-parent-verdict-v1.md": "ff0954eefe72d237eb190ed0fa50a1eeb194c3b5ef1f6eeff041076b2436546e",
}
MS06_V6 = [74, 151, 182, 201, 295]
MS09_B5_V6 = ["00000_00099", "00100_00199", "00200_00299"]


def host_clock():
    return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True,
                          check=True, stdin=subprocess.DEVNULL).stdout.strip()


def free_bytes(path):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


def new_round_markers():
    found = []
    for d in (os.path.join(LANE, "control"), os.path.join(RUN, "control")):
        for name in sorted(os.listdir(d)):
            if re.match(r"(?i)^(stop|halt)", name) or "HALT" in name:
                found.append(os.path.join(d, name))
    return found


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def load_pinned(root, rel, expect, pins_out):
    p = os.path.join(root, rel)
    got = sha(p)
    if expect is not None and got != expect:
        raise SystemExit(f"REFUSED: pin mismatch {p}: {got} != {expect}")
    pins_out[p] = got
    with open(p, "rb") as f:
        raw = f.read()
    return raw


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: probe_frontier_v1.py OUTPUT.json")
    out_path = os.path.abspath(sys.argv[1])
    if not out_path.startswith(os.path.join(LANE, "evidence", "probes") + os.sep):
        raise SystemExit("REFUSED: output outside LANE/evidence/probes")
    started = host_clock()
    free0 = free_bytes(LANE)
    markers = new_round_markers()
    if free0 < FLOOR or markers:
        raise SystemExit(f"REFUSED: free={free0} floor={FLOOR} new_round_markers={markers}")
    with open(os.path.abspath(__file__), "rb") as f:
        self_sha = hashlib.sha256(f.read()).hexdigest()
    pins = {}
    J = {rel: json.loads(load_pinned(OLD, rel, h, pins)) for rel, h in PINS.items() if rel.endswith(".json")}
    for rel, h in PINS.items():
        if not rel.endswith(".json"):
            load_pinned(OLD, rel, h, pins)
    for rel, h in OLD_RUN_PINS.items():
        load_pinned(OLD_RUN, rel, h, pins)

    status = J["STATUS17.json"]
    open_tags = status["M2_open_tags"]
    if status["M2_open"] != 155 or len(open_tags) != 155 or len(set(open_tags)) != 155:
        raise SystemExit("REFUSED: STATUS17 M2 open list is not 155 unique tags")
    a2b = {6: J["cycle2/skel-b/compare-map-ms06.json"], 9: J["cycle2/skel-b/compare-map-ms09.json"]}
    for ms, m in a2b.items():
        if not (m["bijection"] and m["a_each_matched_once"] and m["b_each_matched_once"]):
            raise SystemExit(f"REFUSED: map ms0{ms} not a recorded bijection")
        if sorted(m["a_to_b"]) != list(range(len(m["a_to_b"]))):
            raise SystemExit(f"REFUSED: map ms0{ms} a_to_b not a permutation")
    status17_open = {6: [], 9: []}
    for tag in open_tags:
        mo = re.fullmatch(r"ms0([69])_s(\d{5})", tag)
        if not mo:
            raise SystemExit(f"REFUSED: unexpected open tag {tag}")
        ms, s = int(mo.group(1)), int(mo.group(2))
        status17_open[ms].append({"s_tag": tag, "s_index": s, "b_index": a2b[ms]["a_to_b"][s]})

    # Later lane-original resolutions named by the closeout: ms06 b182/b201 (v6 UNSAT checked),
    # ms09 b30/b44 (parent structural verdict, recorded overlay).
    v6_ms06 = {}
    for b in MS06_V6:
        rel = f"cycle2/m2skel_drat/ms06_b{b:05d}_v6.json"
        p = os.path.join(OLD, rel)
        rec = json.loads(open(p, "rb").read())
        pins[p] = sha(p)
        v6_ms06[b] = {"record": rel, "sha256": pins[p], "status": rec.get("status"),
                      "checked": rec.get("checked"), "integrity_status": rec.get("integrity_status"),
                      "count_for_scientific_coverage": rec.get("count_for_scientific_coverage")}
    for b in (182, 201):
        r = v6_ms06[b]
        if not (r["status"] == "UNSAT" and r["checked"] is True and r["integrity_status"] == "VALIDATED"
                and r["count_for_scientific_coverage"] is True):
            raise SystemExit(f"REFUSED: ms06 b{b} v6 record not a validated UNSAT")
    overlay = J["cycle2/structural-skip-overlay-b30-b44-20261018T082510.json"]
    if overlay["cases"] != [30, 44] or overlay["parent_verdict"]["sha256"] != OLD_RUN_PINS["review/pa19-b30-b44-parent-verdict-v1.md"]:
        raise SystemExit("REFUSED: structural overlay binding mismatch")
    resolved_later = {6: {182, 201}, 9: {30, 44}}
    frontier = {}
    for ms in (6, 9):
        bs = sorted(x["b_index"] for x in status17_open[ms])
        if not resolved_later[ms] <= set(bs):
            raise SystemExit(f"REFUSED: later-resolved ms0{ms} cases not in STATUS17 open list")
        frontier[ms] = [x for x in sorted(status17_open[ms], key=lambda y: y["b_index"])
                        if x["b_index"] not in resolved_later[ms]]
    if len(frontier[6]) != 86 or len(frontier[9]) != 65:
        raise SystemExit(f"REFUSED: frontier counts {len(frontier[6])}/{len(frontier[9])} != 86/65")

    # ms09 per-case data from the frozen v6 M9 contract (pending + reserved interval accounting).
    c9 = J["cycle2/m2-ms09-k1-v6-contract-20261018T075542.json"]
    pending = {}
    for iid in c9["pending_order"]:
        pending.setdefault(int(iid.split(":")[0][1:]), []).append(iid)
    reserved = {}
    for iid in c9["reserved_ids"]:
        reserved.setdefault(int(iid.split(":")[0][1:]), []).append(iid)
    case9 = {c["b_index"]: c for c in c9["cases"]}
    skel9 = J["cycle2/skel-b/skeletons-b-ms09.json"]["skeletons"]
    b5_v6 = {}
    for iv in MS09_B5_V6:
        rel = f"cycle2/m2part_drat/ms09_b00005/batch_{iv}_k1_v6.json"
        p = os.path.join(OLD, rel)
        rec = json.loads(open(p, "rb").read())
        pins[p] = sha(p)
        nr = rec.get("native_result") or {}
        b5_v6[iv] = {"record": rel, "sha256": pins[p], "status": rec.get("status"),
                     "checked": rec.get("checked"), "integrity_status": rec.get("integrity_status"),
                     "count_for_scientific_coverage": rec.get("count_for_scientific_coverage"),
                     "solve_seconds": nr.get("solve_seconds"), "check_seconds": nr.get("check_seconds"),
                     "cnf_sha256": rec.get("cnf_sha256"), "cnf_bytes": rec.get("cnf_bytes"),
                     "proof_raw_bytes": (nr.get("proof_stream") or {}).get("raw_bytes")}
    ms09_rows = []
    for x in frontier[9]:
        b = x["b_index"]
        c = case9[b]
        sk = skel9[b]
        ms09_rows.append({
            "b_index": b, "s_tag": x["s_tag"], "contract_mapped_tag": c["mapped_A2_tag"],
            "skeleton_types": sk["types"], "skeleton_empty": sk["empty"],
            "list": c["list"], "intervals_total": len(c["intervals"]),
            "pending_intervals": len(pending.get(b, [])), "reserved_intervals": reserved.get(b, []),
        })
        if c["mapped_A2_tag"] != x["s_tag"]:
            raise SystemExit(f"REFUSED: ms09 b{b} contract tag {c['mapped_A2_tag']} != map tag {x['s_tag']}")
    skel6 = J["cycle2/skel-b/skeletons-b-ms06.json"]["skeletons"]
    ms06_rows = []
    for x in frontier[6]:
        b = x["b_index"]
        lst = os.path.join(OLD, f"cycle2/m2part_drat/ms06_b{b:05d}/ext.json")
        ms06_rows.append({"b_index": b, "s_tag": x["s_tag"], "skeleton_types": skel6[b]["types"],
                          "skeleton_empty": skel6[b]["empty"], "m2_split_list_exists": os.path.exists(lst),
                          "v6_attempt": v6_ms06.get(b)})
    m2h = {}
    for rel in ("cycle2/m2h-inventory-20261018T120437-1792350277375607000.json",
                "cycle2/m2h-inventory-20261018T133100-1792355460018218000.json"):
        r = J[rel]
        m2h[rel] = {"schema": r["schema"], "contract_sha256": r["contract_sha256"], "cases": r["cases"],
                    "covered_cases": r["covered_cases"], "open_cases": r["open_cases"],
                    "excluded_cases_from_contract": r["excluded_cases_from_contract"]}
    result = {
        "schema": "PA19-96H-FRONTIER-v1",
        "started_host_clock": started, "finished_host_clock": host_clock(),
        "elapsed_seconds": round(time.monotonic() - T0, 3), "probe_sha256": self_sha,
        "admission": {"free_bytes_start": free0, "floor_bytes": FLOOR, "new_round_markers": markers},
        "input_sha256": pins,
        "layer": "LANE-ORIGINAL M2 (independent gen_skel_b/extend_b/encode_skel_b; old-round predicates); "
                 "not measured M2H, not M1, not a PA19 verdict",
        "status17_open_counts": {"ms06": len(status17_open[6]), "ms09": len(status17_open[9])},
        "resolved_after_status17": {"ms06_v6_unsat": [182, 201], "ms09_parent_structural": [30, 44]},
        "frontier_counts": {"ms06": len(frontier[6]), "ms09": len(frontier[9]), "total": 151},
        "ms06_undecided": ms06_rows, "ms09_undecided": ms09_rows,
        "ms06_v6_attempt_records": v6_ms06, "ms09_b5_v6_records": b5_v6,
        "ms09_contract_reserved_ids": c9["reserved_ids"],
        "measured_m2h_views_separate_never_merged": m2h,
    }
    data = json.dumps(result, indent=1, sort_keys=True).encode()
    if len(data) > 16 * 1024 * 1024:
        raise SystemExit("REFUSED: output exceeds 16 MiB")
    with open(out_path, "xb") as f:
        f.write(data)
    print(out_path, hashlib.sha256(data).hexdigest(), len(data))


if __name__ == "__main__":
    main()
