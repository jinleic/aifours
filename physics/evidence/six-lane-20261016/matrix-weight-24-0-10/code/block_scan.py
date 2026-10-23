"""Evaluate every AMH block (exact rational data, float eigenvalues) at a given parameter point s.
Usage: block_scan.py <json file with key "s">  -> prints the most negative normalized eigenvalues."""
import json
import pickle
import sys

import numpy as np


def block_eigs(s, blk, normalize=True):
    out = []
    nf = len(s)
    for b in blk["blocks"]:
        Bs = b["B"]
        m = len(b["idx"])
        nz = [r for r in range(m) if any(Bs[0][r]) or any(any(Bf[r]) for Bf in Bs[1:])]
        if not nz:
            continue
        M = np.array([[float(Bs[0][r][c]) + sum(s[f] * float(Bs[f + 1][r][c]) for f in range(nf)) for c in nz]
                      for r in nz])
        if normalize:
            d = np.sqrt(np.abs(np.diag(M)))
            d = np.where(d > 0, d, 1.0)
            M = M / np.outer(d, d)
        ev = np.linalg.eigvalsh((M + M.T) / 2)
        out.append(((b["a"], b["k"]), len(nz), float(ev[0]), float(ev[-1])))
    out.sort(key=lambda r: r[2])
    return out


if __name__ == "__main__":
    s = json.load(open(sys.argv[1]))["s"]
    blk = pickle.load(open("../evidence/amh_blocks24_exact.pkl", "rb"))
    res = block_eigs(s, blk)
    for r in res[:10]:
        print(r)
    print("n blocks with min eig < -1e-9:", sum(1 for r in res if r[2] < -1e-9))
