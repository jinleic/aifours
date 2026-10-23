"""Build an exact witness JSON (dyadic amplitudes as float.hex) from a saved code (.pt).

python make_witness.py CODE.pt --M 4000 --p 1/5 --D 440 --q 1/2,1/2 --out witness.json [--zero_below 1e-100]
The witness defines the state exactly: phi_i = sum_k amps_i[k] |D^M_k> / ||amps_i||, rho = sum_i q_i |phi_i><phi_i|.
"""
from __future__ import annotations

import argparse
import hashlib
import json

import numpy as np
import torch

ap = argparse.ArgumentParser()
ap.add_argument("code")
ap.add_argument("--M", type=int, required=True)
ap.add_argument("--p", required=True)
ap.add_argument("--D", type=int, required=True)
ap.add_argument("--q", default="1/2,1/2")
ap.add_argument("--zero_below", type=float, default=1e-100)
ap.add_argument("--out", required=True)
a = ap.parse_args()
st = torch.load(a.code)
K, k, res = st["K"], st["k"], st["res"]
n = np.arange(K + 1)
rows = []
for v, r in zip(st["vs"], res):
    w = v.numpy().astype(np.float64) * ((n % k) == r)
    w = w / np.linalg.norm(w)          # rounding here only changes WHICH dyadic state is certified
    w[np.abs(w) < a.zero_below] = 0.0
    last = int(np.nonzero(w)[0].max())
    rows.append([float(x).hex() for x in w[: last + 1]])
wit = {"M": a.M, "p": a.p, "q": a.q.split(","), "amps": rows, "k": k, "residues": res, "D": a.D,
       "source_code_file": a.code, "source_code_sha256": hashlib.sha256(open(a.code, "rb").read()).hexdigest()}
json.dump(wit, open(a.out, "w"))
print(json.dumps({"out": a.out, "K": [len(r) - 1 for r in rows],
                  "sha256": hashlib.sha256(json.dumps(wit, sort_keys=True).encode()).hexdigest()}))
