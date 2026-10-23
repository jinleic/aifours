#!/usr/bin/env python3
"""(13,5,4) control for the independent encoder encode_skel_b (19 = 3q+1 structure at
q=4): every (13,5,4) A2 skeleton (controls/skel13, multisets with skeletons) is encoded by
encode_skel_b with N=13, K=5, Q=4 and solved by CaDiCaL with streamed LRAT. Expected (from
the M-class encoder and the M1 skeleton encoder): SAT exactly for ms04_s00000 and
ms07_s00001, UNSAT otherwise. SAT models are checked directly (rows agree <= once).
Usage: control13_m2.py OUT_JSON
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_skel_b  # noqa: E402
import stream_check  # noqa: E402

LANE = os.path.dirname(HERE)


def main():
    out = {}
    for mi in [1, 4, 5, 6, 7]:
        d = json.load(open(os.path.join(LANE, "controls", "skel13", "skeletons-ms%02d.json" % mi)))
        for si, sk in enumerate(d["skeletons"]):
            types = [tuple(e) for e in sk["edges"]] + [tuple(h) for h in sk["hyper"]]
            nv, cl = encode_skel_b.build(d["c0"], types, sk["empty"], d["special"], N=13, K=5, Q=4)
            r = stream_check.cadical_stream(encode_skel_b.cnf_bytes(nv, cl),
                                            os.path.join(LANE, "scratch", "fifo", "c13m2_%d_%d" % (mi, si)), 120)
            ent = {"status": r["status"], "lrat_checked": r["checked"], "cnf_sha256": r["cnf_sha256"]}
            if r["status"] == "SAT":
                vals = set()
                for line in r["solver_out"].splitlines():
                    if line.startswith("v "):
                        vals.update(int(t) for t in line.split()[1:] if t != "0")
                arr = [[[s for s in range(4) if (1 + 20 * a + 4 * c + s) in vals][0] for c in range(5)]
                       for a in range(13)]
                ent["model"] = arr
                ent["model_valid"] = all(sum(1 for c in range(5) if arr[a][c] == arr[b][c]) <= 1
                                         for a in range(13) for b in range(a + 1, 13))
            out["ms%02d_s%05d" % (mi, si)] = ent
    expected_sat = {"ms04_s00000", "ms07_s00001"}
    ok = all((v["status"] == "SAT" and v.get("model_valid")) if k in expected_sat else
             (v["status"] == "UNSAT" and v["lrat_checked"]) for k, v in out.items())
    res = {"cases": out, "expected_sat": sorted(expected_sat), "ok": ok}
    json.dump(res, open(sys.argv[1], "w"), indent=1)
    print(json.dumps({"ok": ok, "n": len(out)}))


if __name__ == "__main__":
    main()
