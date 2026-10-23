"""Pad a saved mod-k code to a larger cutoff K, seeding the new range with small random amplitudes.

python pad_code.py IN.pt --K 450 --noise 1e-4 --seed 1 --out OUT.pt
"""
import argparse

import torch

ap = argparse.ArgumentParser()
ap.add_argument("inp")
ap.add_argument("--K", type=int, required=True)
ap.add_argument("--noise", type=float, default=1e-4)
ap.add_argument("--seed", type=int, default=1)
ap.add_argument("--out", required=True)
a = ap.parse_args()
st = torch.load(a.inp)
g = torch.Generator().manual_seed(a.seed)
K0 = st["K"]
vs = []
for v in st["vs"]:
    w = torch.zeros(a.K + 1, dtype=torch.float64)
    w[: K0 + 1] = v[: K0 + 1]
    w[K0 + 1:] = a.noise * torch.randn(a.K - K0, generator=g, dtype=torch.float64)
    vs.append(w)
st2 = dict(st)
st2.update({"vs": vs, "K": a.K, "padded_from": a.inp, "pad_noise": a.noise, "pad_seed": a.seed})
torch.save(st2, a.out)
print("saved", a.out)
