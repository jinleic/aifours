"""Copy-lemma blocks + Aut(R^-) symmetry + Z-conditional Zhang-Yeung cutting planes on the base.
Exploratory float LPs.  Usage: python copy_zy.py <blockset-name>"""
import sys, os, json, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_MINUS_EDGES, nbmasks
from copy_lp import Model
from copy_explore import SIG, TAU
from nonshannon_cg import scan as zy_scan, zy_row

BLOCKSETS = {
    "A": [[([9], [0, 1, 2, 4, 5, 6, 7, 8])]],
    "AB": [[([9], [0, 1, 2, 4, 5, 6, 7, 8])], [([2], [0, 1, 4, 5, 6, 7, 8, 9])]],
}

def run(blocks, rounds=30, per_round=200, log=None):
    extra = []; seen = set(); hist = []
    for rnd in range(rounds):
        m = Model(nbmasks(R_MINUS_EDGES))
        for cp in blocks: m.add_block(cp)
        t0 = time.time()
        st, val, nc, nr = m.solve(sym_perms=[SIG, TAU], extra_ge=[tuple((None, k, c) for k, c in r.items()) for r in extra])
        viol = zy_scan(m.last_hbase, 1e-9, per_round)
        added = 0
        for v, a, b, c, d in viol:
            key = (a, b, c, d)
            if key in seen: continue
            seen.add(key); extra.append(zy_row(*key)); added += 1
        hist.append(dict(round=rnd, value=val, status=st, added=added, total_zy=len(extra), wall=round(time.time() - t0, 1)))
        if log: print(json.dumps(hist[-1]), file=log, flush=True)
        if added == 0: break
    return hist, sorted(seen)

if __name__ == "__main__":
    name = sys.argv[1]
    hist, keys = run(BLOCKSETS[name], log=sys.stdout)
    json.dump(dict(blocks=BLOCKSETS[name], history=hist, zy_instances=keys),
              open(os.path.join(os.path.dirname(__file__), "..", "evidence", f"copy-zy-{name}.json"), "w"))
