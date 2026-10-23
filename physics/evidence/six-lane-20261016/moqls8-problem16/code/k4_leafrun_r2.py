"""K4 strict leaf runner r2 (README §9 + §9.1 GO(b) 17:4x): code/k5_leafrun.py UNCHANGED, its ledger module configured
with the K4 constants of code/k4_cover.py AND wrapped by the pinned orbit-aware validator code/k4_orbit_r3.py
(5a324a1d…), so ledgers containing orbit-certified leaves validate before any run. Only F4 (7bb806fc…01f7) is accepted
as base (the wrapped validator checks the base SHA; one base per process). Writes WRAPPER_META.<time>.json first.
python -B k4_leafrun_r2.py --ledger L.json --base ../evidence/k4_w1_v1/GA3_K4w1.cnf --outdir DIR --select ids=...
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
F4_SHA = "7bb806fc8f7793fa5088cc78caf3ebf5b49a72cad82c527f47cf6faced4301f7"


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


if __name__ == "__main__":
    if "--bind-root-proofs" in sys.argv:
        raise SystemExit("--bind-root-proofs is K5-only")
    K = load("k4_cover")
    O = load("k4_orbit_r3")
    LR = load("k5_leafrun")
    K.configure(LR.C)
    O.install(LR.C)
    if LR.C.BASE_SHA != F4_SHA:
        raise SystemExit("K4 constants not applied")
    out = sys.argv[sys.argv.index("--outdir") + 1]
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "WRAPPER_META.%d.json" % int(time.time())), "x") as fh:
        json.dump({"argv": sys.argv, "wrapper_sha256": sha(__file__),
                   "k4_cover_sha256": sha(os.path.join(HERE, "k4_cover.py")),
                   "k4_orbit_r3_sha256": sha(os.path.join(HERE, "k4_orbit_r3.py")),
                   "k5_leafrun_sha256": sha(os.path.join(HERE, "k5_leafrun.py")),
                   "constants": K.K4}, fh, indent=1)
    LR.main()
