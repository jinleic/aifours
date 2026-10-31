#!/usr/bin/env python3
"""ReviewF179RminusExact: FLOAT semantic self-test of the reviewer's own row decoder.

NOT part of the exact proof.  It builds genuine joint laws: a random full-support law of
binary X1..X10 (fixed seed), then every branch is constructed by the sequential copy
lemma exactly as the decoder assumes (new copy sampled from P(copied | over-set),
conditionally independent of every existing variable).  Each decoded certificate row that
is meaningful for an arbitrary law (mono/cmi/dfz >= 0; copy/independence families = 0) is
evaluated with float entropies.  FD, cap and symmetry rows need the game law / symmetric
law and are NOT tested here.  Negative probes evaluate deliberately invalid rows (U outside
the over-set, independence against a future copy) that the exact verifier rejects, to show
that those rejections correspond to genuinely false equalities on a real law.
"""
import importlib.util
import json
import math
import random
import sys
import time
from fractions import Fraction

DIR = "/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f179-rminus-fresh-exact-certificate/"
spec = importlib.util.spec_from_file_location("rv", DIR + "ReviewF179RminusExact-verify.py")
rv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rv)


def base_law(seed):
    rnd = random.Random(seed)
    law = {}
    for x in range(1 << 10):
        law[tuple((x >> k) & 1 for k in range(10))] = rnd.random() ** 3 + 1e-3
    s = sum(law.values())
    return {k: v / s for k, v in law.items()}


def extend(law, vars_, step):
    pos = {n: i for i, n in enumerate(vars_)}
    O = sorted(step["over"], key=lambda n: pos[n])
    Q = list(step["old"])
    po = [pos[n] for n in O]
    pq = [pos[n] for n in Q]
    joint, marg = {}, {}
    for x, p in law.items():
        o = tuple(x[i] for i in po)
        q = tuple(x[i] for i in pq)
        joint.setdefault(o, {})
        joint[o][q] = joint[o].get(q, 0.0) + p
        marg[o] = marg.get(o, 0.0) + p
    out = {}
    for x, p in law.items():
        o = tuple(x[i] for i in po)
        for q, pqv in joint[o].items():
            nv = (q,) if step["atomic"] else q
            out[x + nv] = out.get(x + nv, 0.0) + p * pqv / marg[o]
    return out, vars_ + list(step["new"])


class Ent:
    def __init__(self, law, vars_):
        self.law, self.pos, self.cache = law, {n: i for i, n in enumerate(vars_)}, {}

    def H(self, names):
        key = frozenset(names)
        if not key:
            return 0.0
        if key not in self.cache:
            idx = sorted(self.pos[n] for n in key)
            m = {}
            for x, p in self.law.items():
                t = tuple(x[i] for i in idx)
                m[t] = m.get(t, 0.0) + p
            self.cache[key] = -sum(p * math.log2(p) for p in m.values() if p > 0)
        return self.cache[key]


def value(ent, expr):
    return sum(float(c) * ent.H(k[1]) for k, c in expr.items())


def main():
    t0 = time.time()
    cap = {}
    status, rep, info = rv.run("none", 0, capture=cap)
    if status != "VALID":
        print(json.dumps({"error": "exact verifier not VALID", "status": status}))
        return 2
    branches = cap["branches"]
    law0 = base_law(20261029)
    ents = {}
    for bid, br in branches.items():
        law, vars_ = law0, list(rv.ORIG)
        for st in br.steps:
            law, vars_ = extend(law, vars_, st)
        assert vars_ == br.vars, bid
        ents[bid] = Ent(law, vars_)
    used = sorted({r[2] for r in cap["rows"]})
    res = {"seed": 20261029, "law": "full-support binary X1..X10, weights u^3+1e-3 normalised",
           "branches_built": {b: len(ents[b].law) for b in ents}, "rows": {}, "worst": {}}
    tol = 1e-9
    fails = []
    tested = 0
    for idx, kind, bid, expr, w in cap["rows"]:
        if kind in ("fd", "cap", "sym"):
            continue
        val = value(ents[bid], expr)
        tested += 1
        cls = "ge0" if kind in rv.GE0 else "eq0"
        ok = val >= -tol if cls == "ge0" else abs(val) <= tol
        r = res["rows"].setdefault(kind, {"n": 0, "min": None, "max": None})
        r["n"] += 1
        r["min"] = val if r["min"] is None else min(r["min"], val)
        r["max"] = val if r["max"] is None else max(r["max"], val)
        if not ok:
            fails.append([idx, kind, bid, val])
    # shared original coordinates are the same in every branch (marginal preservation)
    maxdiff = 0.0
    probe = [frozenset(rv.ORIG), frozenset("abd"), frozenset("bcefhi"), frozenset("adefghij")]
    for s in probe:
        vals = [ents[b].H(s) for b in used]
        maxdiff = max(maxdiff, max(vals) - min(vals))
    res["shared_coordinate_max_spread_across_branches"] = maxdiff
    # negative semantic probes (rows the exact verifier REJECTS)
    neg = {}
    p2 = branches["P2"]
    st = p2.steps[0]
    e = {}
    U = sorted(st["over"]) + ["d"]              # U contains X4 (copied), not in over-set
    rv.h(e, p2, U + ["d'1"], 1)
    rv.h(e, p2, U + ["d"], -1)
    neg["copy_U_outside_overset_P2_step0"] = value(ents["P2"], e)
    m4 = branches["M4"]
    st0 = m4.steps[0]
    e = {}
    E_final = set(m4.vars) - set(st0["new"])
    rv.cmi(e, m4, st0["new"], E_final - st0["over"], st0["over"], 1)
    neg["independence_vs_future_copies_M4_step0"] = value(ents["M4"], e)
    e = {}
    rv.cmi(e, m4, st0["new"], set(st0["existing"]) - st0["over"], st0["over"], 1)
    neg["control_valid_independence_M4_step0"] = value(ents["M4"], e)
    res["negative_probes"] = neg
    res["negative_probes_nonzero"] = {k: abs(v) > 1e-6 for k, v in neg.items()
                                      if not k.startswith("control")}
    res["tested_rows"] = tested
    res["failures"] = fails[:20]
    res["failure_count"] = len(fails)
    res["runtime_s"] = round(time.time() - t0, 2)
    ok = (not fails and maxdiff < 1e-9 and all(res["negative_probes_nonzero"].values())
          and abs(neg["control_valid_independence_M4_step0"]) < 1e-9)
    res["selftest_pass"] = ok
    print(json.dumps(res, sort_keys=True))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
