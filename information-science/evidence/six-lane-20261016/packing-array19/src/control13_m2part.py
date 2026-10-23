#!/usr/bin/env python3
"""(13,5,4) control for the M2 partial pipeline (extend_b.py + encode_skel_b.build_part +
CaDiCaL with streamed LRAT, stream_check4). Skeletons: the all-(4,4,3,2) (13,5,4) A2
skeletons (controls/skel13 ms01, ms05, ms07) converted to the M2 format (row types + #empty).
Expected: a SAT subcase with a valid model exactly for skeleton ms07_s00001; every subcase of
the other skeletons UNSAT with a checked proof. Usage: control13_m2part.py OUT_JSON
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_skel_b  # noqa: E402
import stream_check4 as S  # noqa: E402

LANE = os.path.dirname(HERE)


def main():
    wd = os.path.join(LANE, "cycle2", "control13-m2part")
    os.makedirs(wd, exist_ok=True)
    out = {}
    for mi in [1, 5, 7]:
        d = json.load(open(os.path.join(LANE, "controls", "skel13", "skeletons-ms%02d.json" % mi)))
        conv = {"c0": d["c0"], "L": d["L"], "profiles": d["profiles"],
                "skeletons": [{"types": sorted([tuple(e) for e in s["edges"]] + [tuple(h) for h in s["hyper"]]),
                               "empty": s["empty"]} for s in d["skeletons"]]}
        cp = os.path.join(wd, "skel-b-format-ms%02d.json" % mi)
        json.dump(conv, open(cp, "w"))
        special = [p for p in d["profiles"] if list(p) != [4, 3, 3, 3]]
        for si in range(len(conv["skeletons"])):
            tag = "ms%02d_s%05d" % (mi, si)
            ep = os.path.join(wd, tag + ".extb.json")
            subprocess.run([sys.executable, os.path.join(HERE, "extend_b.py"), cp, str(si), ep], check=True,
                           capture_output=True)
            E = json.load(open(ep))
            sk = conv["skeletons"][si]
            st = {"placements": E["num_placements"], "UNSAT_checked": 0, "SAT": 0, "other": 0, "models_valid": []}
            for i, pl in enumerate(E["placements"]):
                nv, cl = encode_skel_b.build_part(d["c0"], [tuple(t) for t in sk["types"]], sk["empty"], special,
                                                  [pl], N=13, K=5, Q=4)
                r = S.cadical_stream(encode_skel_b.cnf_bytes(nv, cl),
                                     os.path.join(LANE, "scratch", "fifo", "c13m2p_%d_%s_%d" % (int(time.time()), tag, i)),
                                     120, check_budget=300)
                if r["status"] == "UNSAT" and r["checked"]:
                    st["UNSAT_checked"] += 1
                elif r["status"] == "SAT":
                    st["SAT"] += 1
                    vals = set()
                    for line in r["solver_out"].splitlines():
                        if line.startswith("v "):
                            vals.update(int(t) for t in line.split()[1:] if t != "0")
                    arr = [[[s for s in range(4) if (1 + 20 * a + 4 * c + s) in vals][0] for c in range(5)]
                           for a in range(13)]
                    st["models_valid"].append(all(sum(1 for c in range(5) if arr[a][c] == arr[b][c]) <= 1
                                                  for a in range(13) for b in range(a + 1, 13)))
                else:
                    st["other"] += 1
            out[tag] = st
    ok = all((v["SAT"] >= 1 and all(v["models_valid"])) if k == "ms07_s00001" else
             (v["SAT"] == 0 and v["other"] == 0 and v["UNSAT_checked"] == v["placements"]) for k, v in out.items())
    json.dump({"cases": out, "ok": ok}, open(sys.argv[1], "w"), indent=1)
    print(json.dumps({"ok": ok, "cases": {k: (v["placements"], v["UNSAT_checked"], v["SAT"]) for k, v in out.items()}}))


if __name__ == "__main__":
    main()
