#!/usr/bin/env python3
"""Independent reviewer control (f141) for the t=29 / n=7 residual argument.
Hypotheses taken from the written candidate (verified by hand separately):
  * E is a set of words in A1 x A2 x A3 x A4 (residual alphabets, |Ai| = r_i, every symbol used)
  * every one of the six coordinate-pair projections of E has exactly n=7 cells
  * every occupied cell has 2 or 3 extensions (degree bound from the 2n+3 classification)
  * |E| = 17 (optional in variant B)
  * P: 29 maximal words; for every pair {i,j} the 36 pairs split into 29 distinct P-pairs and the 7 E-cells.
Controls:
  C1 exact arithmetic of the fiber inequality 2r <= 3(7-r) and the active-count table over all
     profiles (r1..r4) with 1<=r_i<=6, r_i*r_j>=7, including which profiles the active count ALONE kills.
  C2 z3 (supplementary, no proof certificate checked): for every sorted profile with max r_i >= 4,
     the E-only constraints are UNSAT; positive controls: (3,3,3,3) and relaxed degree bound (<=4).
Written by the reviewer; no author code read or executed."""
import itertools, json, hashlib, subprocess, sys, time
from math import comb
import z3

def clock(): return subprocess.run(["/bin/date","-u","+%Y-%m-%dT%H:%M:%SZ"],capture_output=True,text=True).stdout.strip()

def C1():
    fiber = {r: (2*r <= 3*(7-r)) for r in range(1,7)}
    rows = []
    for prof in itertools.combinations_with_replacement(range(1,7),4):
        if any(prof[i]*prof[j] < 7 for i,j in itertools.combinations(range(4),2)): continue
        sk  = sum(6*r - 7 for r in prof)                           # sum_P k(x)
        sk2 = sum(prof[i]*prof[j] - 7 for i,j in itertools.combinations(range(4),2))  # sum_P C(k,2)
        S = sk - sk2
        rows.append({"profile": prof, "sum_k": sk, "sum_C(k,2)": sk2, "S=sum(k-C(k,2))": S,
                     "active_count_contradiction_S>29": S > 29, "all_r<=3": max(prof) <= 3})
    kmap = {k: k - comb(k,2) for k in range(5)}
    return {"fiber_inequality_2r<=3(7-r)": fiber, "max_k_minus_C(k,2)": max(kmap.values()), "k_minus_C(k,2)": kmap,
            "profiles": rows}

def E_model(prof, degmax=3, fixE=17, ncells=7):
    r = prof
    words = list(itertools.product(*[range(a) for a in r]))
    x = {w: z3.Bool("x_%d_%d_%d_%d" % w) for w in words}
    s = z3.Solver()
    s.set("timeout", 600_000)
    def tot(ws): return z3.Sum([z3.If(x[w],1,0) for w in ws])
    for i,j in itertools.combinations(range(4),2):
        occ = []
        for a in range(r[i]):
            for b in range(r[j]):
                cell = [w for w in words if w[i]==a and w[j]==b]
                d = tot(cell)
                s.add(z3.Or(d == 0, z3.And(d >= 2, d <= degmax)))
                occ.append(z3.If(d >= 1, 1, 0))
        s.add(z3.Sum(occ) == ncells)
    for i in range(4):
        for a in range(r[i]):
            s.add(tot([w for w in words if w[i]==a]) >= 1)   # every alphabet symbol used
    if fixE is not None:
        s.add(tot(words) == fixE)
    return s, x, words

def solve(prof, **kw):
    t0 = time.time(); s, x, words = E_model(prof, **kw); res = s.check()
    out = {"profile": prof, "params": kw, "result": str(res), "seconds": round(time.time()-t0,2)}
    if res == z3.sat:
        m = s.model(); E = [w for w in words if z3.is_true(m.eval(x[w], model_completion=True))]
        out["witness_E"] = E; out["witness_size"] = len(E)
        # independent re-verification of the witness against the stated constraints
        ok = True
        for i,j in itertools.combinations(range(4),2):
            cnt = {}
            for w in E: cnt[(w[i],w[j])] = cnt.get((w[i],w[j]),0)+1
            ok &= (len(cnt) == kw.get("ncells",7)) and all(2 <= v <= kw.get("degmax",3) for v in cnt.values())
        for i in range(4): ok &= len({w[i] for w in E}) == prof[i]
        out["witness_recheck"] = bool(ok)
    return out

if __name__ == "__main__":
    c0 = clock()
    c1 = C1()
    killed = [p["profile"] for p in c1["profiles"] if p["active_count_contradiction_S>29"]]
    print("C1 profiles killed by active count alone:", killed)
    print("C1 fiber inequality:", c1["fiber_inequality_2r<=3(7-r)"])
    runs = []
    # C2a: all sorted profiles with some r_i >= 4 (E-only constraints, degree <= 3, |E| = 17)
    for prof in itertools.combinations_with_replacement(range(1,7),4):
        if any(prof[i]*prof[j] < 7 for i,j in itertools.combinations(range(4),2)): continue
        if max(prof) < 4: continue
        rr = solve(prof, degmax=3, fixE=17); runs.append(rr); print(rr, flush=True)
    # C2b: same without |E|=17 for the profiles with max r = 4 (closest to the written fiber argument)
    for prof in [(3,3,3,4),(3,3,4,4),(3,4,4,4),(4,4,4,4),(2,4,4,4)]:
        rr = solve(prof, degmax=3, fixE=None); rr["variant"]="B_no_|E|"; runs.append(rr); print(rr, flush=True)
    # C2c: positive/diagnostic controls
    rr = solve((3,3,3,3), degmax=3, fixE=17); rr["variant"]="diag_3333_E_only"; runs.append(rr); print(rr, flush=True)
    for prof in [(3,3,3,4),(4,4,4,4)]:
        rr = solve(prof, degmax=4, fixE=None); rr["variant"]="relaxed_degmax4"; runs.append(rr); print(rr, flush=True)
    c2 = clock()
    src = open(__file__,"rb").read()
    rec = {"script": __file__.split("/")[-1], "script_sha256": hashlib.sha256(src).hexdigest(),
           "clock_start_utc": c0, "clock_end_utc": c2, "z3": z3.get_version_string(), "python": sys.version.split()[0],
           "C1": c1, "C2_runs": runs,
           "nonclaim": "z3 UNSAT results are supplementary (no independently checked proof certificate); C1 is exact integer arithmetic. Neither proves anything about t>=30 or a global bound."}
    out = __file__.replace(".py","-receipt.json")
    json.dump(rec, open(out,"w"), indent=1); print("receipt", out)
