"""Structure of the 41 general AMH blocks on the family: exact common kernel of all affine components
(sympy rational nullspace), then float eigenvalues of the compressed block (on the orthogonal complement of the
common kernel) at a given parameter point."""
import json
import pickle
import sys

import numpy as np
import sympy

if __name__ == "__main__":
    point = json.load(open(sys.argv[1]))["s"] if len(sys.argv) > 1 else None
    blk = pickle.load(open("../evidence/amh_blocks24_exact.pkl", "rb"))
    st = json.load(open("../evidence/block_structure.json"))
    general = {tuple(g["block"]) for g in st["general"]}
    nf = len(blk["free"])
    out = {}
    for b in blk["blocks"]:
        if (b["a"], b["k"]) not in general:
            continue
        Bs = b["B"]
        m = len(b["idx"])
        nz = [r for r in range(m) if any(Bs[0][r]) or any(any(Bf[r]) for Bf in Bs[1:])]
        comps = [sympy.Matrix([[sympy.Rational(M[r][c].numerator, M[r][c].denominator) for c in nz] for r in nz])
                 for M in Bs]
        stacked = sympy.Matrix.vstack(*comps)
        ker = stacked.nullspace()
        rnk = len(nz) - len(ker)
        rec = {"rows": [b["idx"][r] for r in nz], "dim": len(nz), "common_kernel_dim": len(ker),
               "effective_rank_bound": rnk}
        if point is not None:
            M = sum((comps[0] if f < 0 else point[f] * comps[f + 1] for f in range(-1, nf)), sympy.zeros(len(nz)))
            Mf = np.array(M.evalf(30).tolist(), dtype=float)
            # orthonormal complement of common kernel
            if ker:
                K = np.array(sympy.Matrix.hstack(*ker).evalf(30).tolist(), dtype=float)
                Q, _ = np.linalg.qr(K, mode="complete")
                Qc = Q[:, len(ker):]
            else:
                Qc = np.eye(len(nz))
            Mc = Qc.T @ Mf @ Qc
            d = np.sqrt(np.abs(np.diag(Mc)))
            d = np.where(d > 0, d, 1.0)
            ev = np.linalg.eigvalsh((Mc + Mc.T) / 2 / np.outer(d, d))
            rec["compressed_min_eig"] = float(ev[0]) if len(ev) else None
            rec["compressed_eigs"] = [float(v) for v in ev]
        out[str((b["a"], b["k"]))] = rec
        print((b["a"], b["k"]), {k: v for k, v in rec.items() if k != "compressed_eigs"})
    json.dump(out, open("../evidence/general_blocks.json", "w"), indent=1)
