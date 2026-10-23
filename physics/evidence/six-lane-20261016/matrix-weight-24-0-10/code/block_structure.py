"""Exact structure of each AMH block on the 8-parameter genus-2 family.
For each block: restrict to rows that are not identically zero; test whether all affine components
B_0, B_1..B_8 are rational multiples of ONE fixed rank-1 matrix R = v v^T (then PSD <=> linear functional >= 0).
Outputs the exact linear functionals for rank-1 families and lists the remaining (general) blocks."""
import json
import pickle
from fractions import Fraction


def nonzero_rows(Bs, m):
    return [r for r in range(m) if any(Bs[0][r]) or any(any(Bf[r]) for Bf in Bs[1:])]


def rank1(S):
    n = len(S)
    piv = next(((i, j) for i in range(n) for j in range(n) if S[i][j] != 0), None)
    if piv is None:
        return True
    i0, j0 = piv
    return all(S[i][j] * S[i0][j0] == S[i][j0] * S[i0][j] for i in range(n) for j in range(n))


if __name__ == "__main__":
    blk = pickle.load(open("../evidence/amh_blocks24_exact.pkl", "rb"))
    nf = len(blk["free"])
    rank1_funcs = []
    general = []
    for b in blk["blocks"]:
        m = len(b["idx"])
        Bs = b["B"]
        nz = nonzero_rows(Bs, m)
        if not nz:
            continue
        comps = [[[M[r][c] for c in nz] for r in nz] for M in Bs]
        # reference: first component with nonzero diagonal entry
        ref = None
        for S in comps:
            if any(S[i][i] != 0 for i in range(len(nz))):
                ref = S
                break
        ok = ref is not None and rank1(ref)
        coefs = []
        if ok:
            i0 = next(i for i in range(len(nz)) if ref[i][i] != 0)
            for S in comps:
                q = S[i0][i0] / ref[i0][i0]
                if any(S[i][j] != q * ref[i][j] for i in range(len(nz)) for j in range(len(nz))):
                    ok = False
                    break
                coefs.append(q)
        if ok:
            sign = 1 if ref[i0][i0] > 0 else -1   # R = sign * v v^T
            # PSD of block <=> sign * (coefs[0] + sum coefs[f+1] s_f) >= 0
            rank1_funcs.append({"block": [b["a"], b["k"]], "rows": [b["idx"][r] for r in nz],
                                "const": str(sign * coefs[0]), "coef": [str(sign * q) for q in coefs[1:]]})
        else:
            general.append({"block": [b["a"], b["k"]], "rows": [b["idx"][r] for r in nz]})
    print("rank-1 family blocks:", len(rank1_funcs), " general blocks:", len(general))
    print("general:", [g["block"] for g in general])
    json.dump({"rank1": rank1_funcs, "general": general}, open("../evidence/block_structure.json", "w"), indent=1)
