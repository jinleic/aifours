#!/usr/bin/env python3
"""reviewer-f146-controls-supp-v1.py

Supplementary bounded hunt for an actual orthogonal transversal in the
Fourier-product QLS when Phi_p is REDUCIBLE over F (negative-hypothesis
control, "if available"). Reuses only the reviewer's own module
reviewer-f146-controls-v1.py (no author code).

Order 10 (p=5, F=Q(zeta_5)): K in {F_10, F_2(x)F_5 lex, F_5(x)F_2 lex}, each
under identity + SEED-fixed random row permutations; exhaustive node-capped
backtracking per permutation. Order 6 (p=3): all 720 row permutations of
Tao BH(6,3), F_6, F_2(x)F_3, F_3(x)F_2 were already exhausted in the main run.
Writes reviewer-f146-controls-supp-v1.json next to this script.
"""
import datetime
import hashlib
import importlib.util
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.join(HERE, "reviewer-f146-controls-v1.py")
spec = importlib.util.spec_from_file_location("f146main", MAIN)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

N_PERMS = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
NODE_CAP = 3_000_000
SEED = 20261029


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def main():
    t0 = time.time()
    rep = {
        "script": os.path.basename(__file__), "script_sha256": sha(os.path.abspath(__file__)),
        "main_module": os.path.basename(MAIN), "main_module_sha256": sha(MAIN),
        "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "started_local": datetime.datetime.now().astimezone().isoformat(),
        "python": sys.version, "n_random_perms_per_matrix": N_PERMS, "node_cap": NODE_CAP, "seed": SEED,
    }
    rng = random.Random(SEED)
    perms = [tuple(range(10))] + [tuple(rng.sample(range(10), 10)) for _ in range(N_PERMS)]
    mats = {
        "F10": m.fourier(10),
        "F2xF5_lex": m.tensor_lex(*m.fourier(2), *m.fourier(5)),
        "F5xF2_lex": m.tensor_lex(*m.fourier(5), *m.fourier(2)),
    }
    res = {}
    for nm, (k, q) in mats.items():
        assert m.is_butson_hadamard(k, q)
        r = m.sweep_row_permutations(nm + " identity+%d seeded row perms" % N_PERMS, k, q, 5, perms, node_cap=NODE_CAP)
        res[nm] = r
        print(nm, {kk: r[kk] for kk in ("row_permutations_tested", "perms_with_same_parity_triples",
                                        "perms_with_transversal", "searches_capped", "seconds")})
        if r["first_transversal"]:
            print("  FIRST TRANSVERSAL:", r["first_transversal"])
    rep["results"] = res
    rep["reducible_transversal_found"] = any(r["perms_with_transversal"] > 0 for r in res.values())
    rep["any_search_capped"] = any(r["searches_capped"] > 0 for r in res.values())
    rep["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    rep["finished_local"] = datetime.datetime.now().astimezone().isoformat()
    rep["elapsed_seconds"] = round(time.time() - t0, 3)
    out = os.path.join(HERE, "reviewer-f146-controls-supp-v1.json")
    with open(out, "w") as fh:
        json.dump(rep, fh, indent=1)
    print("reducible transversal found:", rep["reducible_transversal_found"], "capped:", rep["any_search_capped"],
          "elapsed", rep["elapsed_seconds"], "wrote", out)


if __name__ == "__main__":
    main()
