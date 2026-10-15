"""Run the (independent) Knuth-Bendix completion on the Artin-Garside
presentation of A(W) and compare its rules with leading words of length <= L
against the Garside-oracle reduced GS basis (and, optionally, an explicit
family spec).

Presentation fed to KB (letters '0' = Delta^-1 < '1' = Delta < 'a' < 'b' < ...):
  braid relations;  Delta = (a positive word for Delta);  Delta Delta^-1 = 1 = Delta^-1 Delta;
  s Delta = Delta phi(s), s Delta^-1 = Delta^-1 phi(s)  (standard consequences, added
  so that the truncated completion does not need overlaps longer than maxlen).

Usage: python3 work/kb_compare.py TYPE n --order 0,2,1 --maxlen 14 --L 12 [--m M] [--spec B3]
"""
from __future__ import annotations

import argparse
import json
import sys
import time

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from coxeter import build  # noqa: E402
from gs_oracle import enumerate_basis  # noqa: E402
from kb import KB  # noqa: E402
from specs import SPECS, alt  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("typ")
    ap.add_argument("n", type=int)
    ap.add_argument("--m", type=int, default=0)
    ap.add_argument("--order", default=None)
    ap.add_argument("--maxlen", type=int, default=14)
    ap.add_argument("--L", type=int, default=12)
    ap.add_argument("--spec", default=None)
    ap.add_argument("--monoid", action="store_true", help="Artin monoid only (no Delta letters)")
    a = ap.parse_args()
    order = [int(x) for x in a.order.split(",")] if a.order else None
    G = build(a.typ, a.n, a.m, order)
    W = G.W
    gens = [chr(97 + i) for i in range(W.n)]
    eqs = []
    for i in range(W.n):
        for j in range(i + 1, W.n):
            eqs.append((alt(gens[i], gens[j], W.M[i][j]), alt(gens[j], gens[i], W.M[i][j])))
    if not a.monoid:
        # any positive word for Delta: a reduced word of w0 built greedily in W (not the lexmin one)
        w, word = W.e, []
        while True:
            asc = [i for i in range(W.n) if i not in W.rdesc(w)]
            if not asc:
                break
            i = asc[-1]
            w = W.rmul(w, i)
            word.append(gens[i])
        eqs.append(("".join(word), "1"))
        eqs += [("10", ""), ("01", "")]
        for i in range(W.n):
            eqs.append((gens[i] + "1", "1" + gens[W.phi[i]]))
            eqs.append((gens[i] + "0", "0" + gens[W.phi[i]]))
    t0 = time.time()
    rws = KB()
    rws.complete(eqs, a.maxlen)
    t1 = time.time()
    kb_rules = {l: r for l, r in rws.rules.items() if len(l) <= a.L}
    rules, _ = enumerate_basis(G, a.L, monoid=a.monoid)
    oracle = dict(rules)
    rep = {"type": a.typ, "n": a.n, "m": a.m, "order": order, "monoid": a.monoid,
           "maxlen": a.maxlen, "L": a.L, "kb_seconds": round(t1 - t0, 1),
           "kb_rules_total": len(rws.rules), "kb_discarded_long_equations": rws.truncated,
           "kb_skipped_long_overlaps": rws.skipped_overlaps,
           "kb_rules_le_L": len(kb_rules), "oracle_rules_le_L": len(oracle),
           "kb_equals_oracle": kb_rules == oracle}
    if kb_rules != oracle:
        rep["only_kb"] = sorted(set(kb_rules) - set(oracle))[:20]
        rep["only_oracle"] = sorted(set(oracle) - set(kb_rules))[:20]
    if a.spec:
        from certify import expand, instances_upto
        spec = SPECS[a.spec]()
        inst = instances_upto([expand(f) for f in spec["families"]], a.L)
        rep["kb_equals_spec"] = kb_rules == inst
    print(json.dumps(rep))


if __name__ == "__main__":
    main()
