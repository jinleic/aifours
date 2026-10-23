#!/usr/bin/env python3
"""Consolidated (13,5,4) controls with drat-trim-only acceptance (stream_check5), written as a
receipt cycle2/control13-v5.json. (13,5,4) has the same 3q+1 structure as (19,8,6) (q = 4,
5 columns, base profile (4,3,3,3)); PA(13,5,4) exists, and earlier runs found SAT exactly for
the A2 skeletons ms04_s00000 and ms07_s00001.
Pipelines (each must give SAT with a valid model only inside the expected skeletons and UNSAT
verified by drat-trim everywhere else):
  M1-A2    encode_skel (all skeletons of ms01, ms04, ms05, ms06, ms07), kissat_drat
  M1-A3    extend_p1q m = ns + encode_fullq, all-(4,4,3,2) skeletons (ms01, ms05, ms07)
  M1-A3x   same full skeletons with encode_full2q (exact leave counts)
  M1-A3'   extend_p1q m = 1 + encode_partq
  M1-A3''  extend_p1q m = 1 + encode_partbatch (all placements of a skeleton in one batch)
  M2-A2    encode_skel_b.build and build_v2 (all skeletons), cadical_drat
  M2-A3''  extend_b + build_part (single) and build_partbatch (one batch), cadical_drat
Usage (research venv for networkx): control13_v5.py
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import encode_full2q  # noqa: E402
import encode_fullq  # noqa: E402
import encode_partbatch  # noqa: E402
import encode_partq  # noqa: E402
import encode_skel  # noqa: E402
import encode_skel_b  # noqa: E402
import stream_check5 as S  # noqa: E402

LANE = os.path.dirname(HERE)
WD = os.path.join(LANE, "cycle2", "control13-v5")
FD = os.path.join(LANE, "scratch", "fifo", "c13v5")
EXPECTED_SAT = {"ms04_s00000", "ms07_s00001"}


def model_ok(solver_out, var):
    vals = set()
    for line in solver_out.splitlines():
        if line.startswith("v "):
            vals.update(int(t) for t in line.split()[1:] if t != "0")
    arr = [[([s for s in range(4) if var(a, c, s) in vals] + [-1])[0] for c in range(5)] for a in range(13)]
    return all(-1 not in row for row in arr) and all(
        sum(1 for c in range(5) if arr[a][c] == arr[b][c]) <= 1 for a in range(13) for b in range(a + 1, 13))


def verdict(r, var):
    if r["status"] == "SAT":
        return "SAT_valid" if model_ok(r["solver_out"], var) else "SAT_INVALID_MODEL"
    if r["status"] == "UNSAT":
        return "UNSAT_verified" if r["checked"] else "UNSAT_unverified"
    return r["status"]


def main():
    os.makedirs(WD, exist_ok=True)
    out = {}
    skels = {}
    for mi in [1, 4, 5, 6, 7]:
        d = json.load(open(os.path.join(LANE, "controls", "skel13", "skeletons-ms%02d.json" % mi)))
        for si, sk in enumerate(d["skeletons"]):
            skels["ms%02d_s%05d" % (mi, si)] = (d, sk)
    for tag, (d, sk) in skels.items():
        sp = os.path.join(LANE, "controls", "c13skel", "specs", tag + ".json")
        spec = json.load(open(sp))
        assert spec["skeleton"] == sk and spec["special"] == d["special"] and spec["N"] == 13
        F, X, _ = encode_skel.build(spec)
        v1 = lambda a, c, s, X=X: X[a][c][s]  # noqa: E731
        out.setdefault("M1-A2", {})[tag] = verdict(S.kissat_drat(S.cnf_bytes_of(F), FD + "_a2", 120, 300), v1)
        types = sorted([tuple(e) for e in sk["edges"]] + [tuple(h) for h in sk["hyper"]])
        vb = lambda a, c, s: 1 + 20 * a + 4 * c + s  # noqa: E731
        for name, fn in (("M2-A2-build", encode_skel_b.build), ("M2-A2-build_v2", encode_skel_b.build_v2)):
            nv, cl = fn(d["c0"], types, sk["empty"], d["special"], N=13, K=5, Q=4)
            out.setdefault(name, {})[tag] = verdict(S.cadical_drat(encode_skel_b.cnf_bytes(nv, cl), FD + "_m2", 120, 300), vb)
        if not all(sorted(p, reverse=True) == [4, 4, 3, 2] for p in d["special"]):
            continue
        ns = len(d["special"])
        for m, key in ((ns, "full"), (1, "one")):
            ep = os.path.join(WD, "%s.ext_m%d.json" % (tag, m))
            subprocess.run([sys.executable, os.path.join(HERE, "extend_p1q.py"), sp, ep, str(m)], check=True,
                           capture_output=True)
        Efull = json.load(open(os.path.join(WD, "%s.ext_m%d.json" % (tag, ns))))
        Eone = json.load(open(os.path.join(WD, "%s.ext_m1.json" % tag)))
        res = {"M1-A3": [], "M1-A3x": [], "M1-A3p": [], "M1-A3pp": None}
        for pl in Efull["full"]:
            sub = dict(spec)
            sub["placed"] = pl
            for name, enc in (("M1-A3", encode_fullq), ("M1-A3x", encode_full2q)):
                F, X, _ = enc.build(sub)
                res[name].append(verdict(S.kissat_drat(S.cnf_bytes_of(F), FD + "_a3", 120, 300),
                                         lambda a, c, s, X=X: X[a][c][s]))
        for pl in Eone["full"]:
            sub = dict(spec)
            sub["placed"] = pl
            F, X, _ = encode_partq.build(sub)
            res["M1-A3p"].append(verdict(S.kissat_drat(S.cnf_bytes_of(F), FD + "_a3p", 120, 300),
                                         lambda a, c, s, X=X: X[a][c][s]))
        if Eone["full"]:
            F, X, _ = encode_partbatch.build(spec, Eone["full"])
            res["M1-A3pp"] = verdict(S.kissat_drat(S.cnf_bytes_of(F), FD + "_a3pp", 120, 300),
                                     lambda a, c, s, X=X: X[a][c][s])
        conv = {"c0": d["c0"], "L": d["L"], "profiles": d["profiles"], "skeletons": [{"types": list(map(list, types)), "empty": sk["empty"]}]}
        cp = os.path.join(WD, tag + ".skel-b-format.json")
        json.dump(conv, open(cp, "w"))
        ebp = os.path.join(WD, tag + ".extb.json")
        subprocess.run([sys.executable, os.path.join(HERE, "extend_b.py"), cp, "0", ebp], check=True, capture_output=True)
        Eb = json.load(open(ebp))
        res["M2-A3p_count"] = Eb["num_placements"]
        res["M1-A3p_count"] = Eone["num_full"]
        res["M2-A3p"] = []
        vb = lambda a, c, s: 1 + 20 * a + 4 * c + s  # noqa: E731
        for pl in Eb["placements"]:
            nv, cl = encode_skel_b.build_part(d["c0"], types, sk["empty"], d["special"], [pl], N=13, K=5, Q=4)
            res["M2-A3p"].append(verdict(S.cadical_drat(encode_skel_b.cnf_bytes(nv, cl), FD + "_m2p", 120, 300), vb))
        res["M2-A3pp"] = None
        if Eb["placements"]:
            nv, cl = encode_skel_b.build_partbatch(d["c0"], types, sk["empty"], d["special"], Eb["placements"], N=13, K=5, Q=4)
            res["M2-A3pp"] = verdict(S.cadical_drat(encode_skel_b.cnf_bytes(nv, cl), FD + "_m2pp", 120, 300), vb)
        out.setdefault("splits", {})[tag] = res
    # expectations
    problems = []
    for pipe in ("M1-A2", "M2-A2-build", "M2-A2-build_v2"):
        for tag, v in out[pipe].items():
            want = "SAT_valid" if tag in EXPECTED_SAT else "UNSAT_verified"
            if v != want:
                problems.append((pipe, tag, v))
    for tag, res in out["splits"].items():
        sat_expected = tag in EXPECTED_SAT
        for pipe in ("M1-A3", "M1-A3x", "M1-A3p", "M2-A3p"):
            vs = res[pipe]
            if sat_expected:
                if not (any(v == "SAT_valid" for v in vs) and all(v in ("SAT_valid", "UNSAT_verified") for v in vs)):
                    problems.append((pipe, tag, vs))
            elif not all(v == "UNSAT_verified" for v in vs):
                problems.append((pipe, tag, vs))
        for pipe in ("M1-A3pp", "M2-A3pp"):
            v = res[pipe]
            if v is None:
                continue
            want = "SAT_valid" if sat_expected else "UNSAT_verified"
            if v != want:
                problems.append((pipe, tag, v))
        if res["M1-A3p_count"] != res["M2-A3p_count"]:
            problems.append(("count", tag, res["M1-A3p_count"], res["M2-A3p_count"]))
    out["problems"] = problems
    out["ok"] = not problems
    out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    json.dump(out, open(os.path.join(LANE, "cycle2", "control13-v5.json"), "w"), indent=1)
    print(json.dumps({"ok": out["ok"], "problems": problems[:10]}))


if __name__ == "__main__":
    main()
