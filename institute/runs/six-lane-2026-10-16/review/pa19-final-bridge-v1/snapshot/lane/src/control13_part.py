#!/usr/bin/env python3
"""(13,5,4) control for the partial split (extend_p1q.py with m = 1 + encode_partq.py).
For every (13,5,4) A2 skeleton whose special columns are all (4,4,3,2) (multisets ms01,
ms05, ms07 of controls/skel13), enumerate the one-column extensions and solve every
subcase with kissat_stream (stream_check4). Expected from the M-class and skeleton
encoders: a SAT subcase (with a valid model) exactly for skeleton ms07_s00001, UNSAT for all
subcases of the other skeletons. Usage (research venv): control13_part.py OUT_JSON
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_partq  # noqa: E402
import stream_check4 as S  # noqa: E402

LANE = os.path.dirname(HERE)
VENV_PY = os.path.expanduser("~/.local/state/research-explorer/venv/bin/python")


def main():
    out = {}
    wd = os.path.join(LANE, "cycle2", "control13-part")
    os.makedirs(wd, exist_ok=True)
    for mi in [1, 5, 7]:
        d = json.load(open(os.path.join(LANE, "controls", "skel13", "skeletons-ms%02d.json" % mi)))
        for si, sk in enumerate(d["skeletons"]):
            tag = "ms%02d_s%05d" % (mi, si)
            spec = {"kind": "skel", "N": 13, "k": 5, "q": 4, "multiset_index": mi, "skel_index": si,
                    "c0": d["c0"], "special": d["special"], "L": d["L"], "skeleton": sk}
            sp = os.path.join(wd, tag + ".spec.json")
            json.dump(spec, open(sp, "w"))
            ext = os.path.join(wd, tag + ".ext.json")
            subprocess.run([VENV_PY, os.path.join(HERE, "extend_p1q.py"), sp, ext, "1"], check=True,
                           capture_output=True)
            E = json.load(open(ext))
            st = {"placements": E["num_full"], "UNSAT_checked": 0, "SAT": 0, "other": 0, "models_valid": []}
            for i, pl in enumerate(E["full"]):
                sub = dict(spec)
                sub["placed"] = pl
                F, X, _ = encode_partq.build(sub)
                r = S.kissat_stream(S.cnf_bytes_of(F), os.path.join(LANE, "scratch", "fifo",
                                    "c13p_%d_%s_%d" % (int(time.time()), tag, i)), 120, check_budget=300)
                if r["status"] == "UNSAT" and r["checked"]:
                    st["UNSAT_checked"] += 1
                elif r["status"] == "SAT":
                    st["SAT"] += 1
                    vals = set()
                    for line in r["solver_out"].splitlines():
                        if line.startswith("v "):
                            vals.update(int(t) for t in line.split()[1:] if t != "0")
                    arr = [[[s for s in range(4) if X[a][c][s] in vals][0] for c in range(5)] for a in range(13)]
                    st["models_valid"].append(all(sum(1 for c in range(5) if arr[a][c] == arr[b][c]) <= 1
                                                  for a in range(13) for b in range(a + 1, 13)))
                else:
                    st["other"] += 1
            out[tag] = st
    ok = all((v["SAT"] >= 1 and all(v["models_valid"])) if k == "ms07_s00001" else
             (v["SAT"] == 0 and v["other"] == 0 and v["UNSAT_checked"] == v["placements"]) for k, v in out.items())
    res = {"cases": out, "ok": ok}
    json.dump(res, open(sys.argv[1], "w"), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
