"""K4 cover ledger (README §9): the ledger/validator logic of code/k5_cover.py, UNCHANGED, run with the K4 constants
(base evidence/k4_w1_v1/GA3_K4w1.cnf, ledger directory evidence/k4_split_v1/ledger, schema k4-cover-ledger/1).
The declared lists V1..V8 are the same DIMACS ids as for K5 (squares 1 and 2 occupy identical primary variables in
GA3_K4w1.map.json; checked by `check-chain`, receipt evidence/k4_split_v1/CHAIN_CHECK.json).
python -B k4_cover.py init|ingest|refine|validate --base ../evidence/k4_w1_v1/GA3_K4w1.cnf [...]   (as k5_cover.py)
python -B k4_cover.py check-chain --map ../evidence/k4_w1_v1/GA3_K4w1.map.json
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
K4_SPLIT = os.path.normpath(os.path.join(HERE, "..", "evidence", "k4_split_v1"))
K4 = {"BASE_SHA": "7bb806fc8f7793fa5088cc78caf3ebf5b49a72cad82c527f47cf6faced4301f7", "SPLIT_DIR": K4_SPLIT,
      "LEDGER_DIR": os.path.join(K4_SPLIT, "ledger"), "SCHEMA": "k4-cover-ledger/1"}
# intended meaning of each declared list (square, row of the column-0 cell), coordinates k = 1..7
MEANING = {1: (1, 2), 2: (1, 3), 3: (1, 4), 4: (1, 5), 5: (1, 6), 6: (1, 7), 7: (2, 2), 8: (2, 3)}


def load_cover():
    spec = importlib.util.spec_from_file_location("k5_cover", os.path.join(HERE, "k5_cover.py"))
    C = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(C)
    return C


def configure(C):
    for k, v in K4.items():
        setattr(C, k, v)
    return C


def check_chain(C, map_path):
    names = json.load(open(map_path))["vars"]
    ids = {}
    for k, v in names.items():
        kk = json.loads(k)
        if kk[0] == "g":
            ids[(kk[1], tuple(kk[2]), tuple(kk[3]))] = v
    rows = []
    ok = True
    for d, (s, r) in MEANING.items():
        want = [ids.get((s, (0, k), (r, 0))) for k in range(1, 8)]
        rows.append({"depth": d, "square": s, "cell": [r, 0], "map_ids": want, "chain": C.CHAIN[d],
                     "equal": want == C.CHAIN[d]})
        ok &= want == C.CHAIN[d]
    rec = {"argv": sys.argv, "map": map_path, "map_sha256": hashlib.sha256(open(map_path, "rb").read()).hexdigest(),
           "rows": rows, "all_equal": ok}
    os.makedirs(K4_SPLIT, exist_ok=True)
    with open(os.path.join(K4_SPLIT, "CHAIN_CHECK.json"), "x") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({"all_equal": ok}))
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    C = configure(load_cover())
    if len(sys.argv) > 1 and sys.argv[1] == "check-chain":
        check_chain(C, sys.argv[sys.argv.index("--map") + 1])
    else:
        C.main()
