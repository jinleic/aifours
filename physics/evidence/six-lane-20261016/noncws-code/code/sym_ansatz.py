"""Symmetry-adapted (non-CWS) ansatz searches for ((7,3,3))_2 -- exploratory numerics.

Groups act on 7 qubits by permuting tensor factors (optionally composed with local unitaries).
Ansatz A (irreducible): V = an irreducible 3-dim G-submodule of (C^2)^{x7}, parametrized by its
  multiplicity vector c in C^m (V(c) = 3 (x) c inside the isotypic component 3 (x) C^m).
Ansatz B (invariant): V = any 3-dim subspace of the G-invariant vectors (or of a chosen isotypic
  component), optimized with the Stiefel search restricted to that subspace.
A zero of the KL loss found here would only be a CANDIDATE; exact verification is separate.
"""
import itertools
import json
import sys

import numpy as np

from kl_search import KLLoss, retract, search

FANO = [(0, 1, 3), (1, 2, 4), (2, 3, 5), (3, 4, 6), (4, 5, 0), (5, 6, 1), (6, 0, 2)]


def fano_group():
    lines = {frozenset(l) for l in FANO}
    G = []
    for p in itertools.permutations(range(7)):
        if all(frozenset(p[i] for i in l) in lines for l in lines):
            G.append(p)
    return G


def perm_matrix_action(p, n=7):
    """Index map for permuting qubits: qubit q -> p[q]. Returns idx with (U psi)[s'] = psi[s] where
    s' has bit p[q] = bit q of s."""
    N = 2 ** n
    out = np.zeros(N, dtype=np.int64)
    for s in range(N):
        t = 0
        for q in range(n):
            if (s >> q) & 1:
                t |= 1 << p[q]
        out[s] = t
    return out  # (U psi)[out[s]] = psi[s]


def apply_perm(idx, psi):
    out = np.empty_like(psi)
    out[idx] = psi
    return out


def compose(p, q):
    """(p o q)(i) = p[q[i]]"""
    return tuple(p[q[i]] for i in range(len(q)))


def order(p):
    e = tuple(range(len(p)))
    k, r = 1, p
    while r != e:
        r = compose(p, r)
        k += 1
    return k


def conj_classes(G):
    Gs = set(G)
    inv = {g: tuple(np.argsort(g)) for g in G}
    seen, classes = set(), []
    for g in G:
        if g in seen:
            continue
        cl = {compose(compose(h, g), inv[h]) for h in G}
        seen |= cl
        classes.append(sorted(cl))
    return classes


def psl27_characters(G):
    """Character table of PSL(2,7) evaluated on each element (dict name -> dict g -> value)."""
    classes = conj_classes(G)
    a = (-1 + 1j * np.sqrt(7)) / 2
    cls_of = {}
    info = []
    seven = []
    for ci, cl in enumerate(classes):
        o = order(cl[0])
        for g in cl:
            cls_of[g] = ci
        info.append((o, len(cl)))
        if o == 7:
            seven.append(ci)
    # label 7A = class containing g with g^2 in same class (always true); pick seven[0] as 7A
    tab = {}
    for g in G:
        o, _ = info[cls_of[g]]
        is7A = cls_of[g] == seven[0]
        v1 = 1
        v3 = {1: 3, 2: -1, 3: 0, 4: 1}.get(o, a if is7A else np.conj(a))
        v3b = np.conj(v3)
        v6 = {1: 6, 2: 2, 3: 0, 4: 0, 7: -1}[o]
        v7 = {1: 7, 2: -1, 3: 1, 4: -1, 7: 0}[o]
        v8 = {1: 8, 2: 0, 3: -1, 4: 0, 7: 1}[o]
        tab[g] = {"1": v1, "3": v3, "3b": v3b, "6": v6, "7": v7, "8": v8}
    return tab, info


def isotypic_projector_basis(G, idxs, chi, dim, N=128, tol=1e-8):
    P = np.zeros((N, N), dtype=complex)
    for g in G:
        U = np.zeros((N, N))
        U[idxs[g], np.arange(N)] = 1.0
        P += np.conj(chi[g]) * U
    P *= dim / len(G)
    P = (P + P.conj().T) / 2
    w, v = np.linalg.eigh(P)
    return v[:, w > 0.5], P


def kl_loss_of_basis(loss, W):
    Q, _ = np.linalg.qr(W)
    return loss.value_grad(Q)[0]


if __name__ == "__main__":
    G = fano_group()
    print("Fano automorphism group order", len(G))
    idxs = {g: perm_matrix_action(g) for g in G}
    tab, info = psl27_characters(G)
    print("classes (order,size):", info)
    # character orthogonality sanity
    for nm in ["1", "3", "3b", "6", "7", "8"]:
        nrm = sum(abs(tab[g][nm]) ** 2 for g in G) / len(G)
        assert abs(nrm - 1) < 1e-9, (nm, nrm)
    mult = {}
    for nm, dm in [("1", 1), ("3", 3), ("3b", 3), ("6", 6), ("7", 7), ("8", 8)]:
        B, P = isotypic_projector_basis(G, idxs, {g: tab[g][nm] for g in G}, dm)
        mult[nm] = B.shape[1] // dm
        print(f"irrep {nm}: isotypic dim {B.shape[1]}, multiplicity {B.shape[1] / dm}")
    json.dump({"group_order": len(G), "multiplicities": mult}, open("../evidence/psl27_multiplicities.json", "w"))
