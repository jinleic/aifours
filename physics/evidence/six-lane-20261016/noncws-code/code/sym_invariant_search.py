"""Ansatz B: V = 3-dim subspace of the PSL(2,7)-invariant vectors (Fano-plane qubit permutations).
PSL(2,7) has no 3-dim irreducible constituent in (C^2)^{x7} (multiplicity 0, see psl27_multiplicities.json),
so every PSL(2,7)-invariant 3-dim code space lies in the 10-dim trivial isotypic component.
Controls: K=2 in the same space must reach ~0 (Steane code is PSL(2,7)-invariant).
Exploratory numerics only.
"""
import json
import sys

import numpy as np

from kl_search import KLLoss, search
from sym_ansatz import fano_group, isotypic_projector_basis, perm_matrix_action

if __name__ == "__main__":
    restarts = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    G = fano_group()
    idxs = {g: perm_matrix_action(g) for g in G}
    B, _ = isotypic_projector_basis(G, idxs, {g: 1.0 for g in G}, 1)
    print("invariant subspace dim", B.shape[1])
    res = {}
    for K in (2, 3):
        loss = KLLoss(7, K, 3, basis=B)
        rng = np.random.default_rng(100 + K)
        Ls = []
        for r in range(restarts):
            C0 = rng.normal(size=(B.shape[1], K)) + 1j * rng.normal(size=(B.shape[1], K))
            C, L, it = search(loss, C0, iters=3000)
            Ls.append(L)
        Ls.sort()
        res[K] = {"restarts": restarts, "best": Ls[0], "q10": Ls[len(Ls) // 10], "median": Ls[len(Ls) // 2]}
        print(K, res[K])
    json.dump(res, open("../evidence/psl27_invariant_search.json", "w"), indent=1)
