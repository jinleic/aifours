"""K4 strict leaf runner (README §9): code/k5_leafrun.py UNCHANGED (ledger validation, exact-identity resume, certify()
of code/k5_resplit.py with the strict conjunction, guards), with its ledger module configured by code/k4_cover.py's K4
constants. Writes WRAPPER_META.<time>.json (this file's SHA-256 and the constants) into --outdir first.
python -B k4_leafrun.py --ledger ../evidence/k4_split_v1/ledger/LEDGER.v001.json --base ../evidence/k4_w1_v1/GA3_K4w1.cnf \\
       --outdir ../evidence/k4_split_v1/pilot --select ids=c001,c016
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


if __name__ == "__main__":
    K = load("k4_cover")
    LR = load("k5_leafrun")
    K.configure(LR.C)
    if "--bind-root-proofs" in sys.argv:
        raise SystemExit("--bind-root-proofs is K5-only")
    out = sys.argv[sys.argv.index("--outdir") + 1]
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "WRAPPER_META.%d.json" % int(time.time())), "x") as fh:
        json.dump({"argv": sys.argv, "wrapper_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
                   "k4_cover_sha256": hashlib.sha256(open(os.path.join(HERE, "k4_cover.py"), "rb").read()).hexdigest(),
                   "constants": K.K4}, fh, indent=1)
    LR.main()
