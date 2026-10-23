"""Print the conditional diamond profile (3,10;4,8 | Z={1,2,5,6,7,9}) of LP-optimal base vectors (floats)."""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from block_sep import master, NBM
from fractions import Fraction
def m(*vs): return sum(1 << (v - 1) for v in vs)
Z = m(1, 2, 5, 6, 7, 9); U, V, P, Q = m(3), m(10), m(4), m(8)
def prof(h):
    H = lambda *ms: h[Z | sum(ms)] - h[Z]
    I = lambda a, b, c=0: h[Z | a | c] + h[Z | b | c] - h[Z | a | b | c] - h[Z | c]
    return dict(hZ=h[Z], HU=H(U), HV=H(V), HP=H(P), HQ=H(Q), HPQ=H(P, Q), HUV=H(U, V), Hall=H(U, V, P, Q),
                I_UV=I(U, V), I_UV_P=I(U, V, P), I_UV_Q=I(U, V, Q), I_PQ=I(P, Q),
                I_UP=I(U, P), I_UQ=I(U, Q), I_VP=I(V, P), I_VQ=I(V, Q),
                Ing=I(U, V, P) + I(U, V, Q) + I(P, Q) - I(U, V),
                hv=[h[1 << i] for i in range(10)], hV=h[1023])
blocks = {"shannon": [[]], "copyA": [[([9], [0, 1, 2, 4, 5, 6, 7, 8])]]}
out = {}
for k, b in blocks.items():
    st, val, hb, wall, nc, nr = master(b)
    p = prof(hb); p["value"] = val
    out[k] = p
    print(k, json.dumps({a: (round(x, 5) if isinstance(x, float) else [round(y, 4) for y in x]) for a, x in p.items()}))
json.dump(out, open(os.path.join(os.path.dirname(__file__), "..", "evidence", "diamond-profile-float.json"), "w"), indent=1)
