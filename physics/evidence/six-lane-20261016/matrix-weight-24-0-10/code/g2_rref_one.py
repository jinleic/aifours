"""Build the n=24 genus-2 system modulo one prime and save its RREF (for multi-prime reconstruction)."""
import json
import sys

import numpy as np

from g2_exact import rref_mod
from g2_system import build_mod

if __name__ == "__main__":
    p = int(sys.argv[1])
    Mfull, b, okeys, orbits = build_mod(p, log=lambda *a: None)
    piv, R, cons = rref_mod(Mfull, b, p)
    np.savez_compressed(f"../evidence/rref/rref_{p}.npz", piv=np.array(piv), R=R, cons=np.array([cons]),
                        okeys=np.array(json.dumps(okeys)))
    np.savez_compressed(f"../evidence/rref/system_{p}.npz", M=Mfull, b=b)
    print(json.dumps({"prime": p, "rank": len(piv), "consistent": bool(cons)}))
