"""Experiment CANON2 (exploratory): Codex-proposed canonical candidate for fully-closed boxes:
the contact kernel intersected with {E_b in span(E_-, E_+)} (two extra linear conditions).
Computed independently by linear algebra (not from the delegate's closed formulas), then
tested for closed feasibility on fine grids.  Also tests the mirror candidate
{O_b in span(O_-, O_+)}.
"""
from __future__ import annotations

import numpy as np
from numpy.polynomial import polynomial as NP

from fclosed import contact_matrix
from canon import check


def coeff_rows_E_in_span(n, Em, Ep):
    """Rows (in b's s-coefficients) expressing that E_b lies in span(E_-, E_+): E_b's coefficient
    vector (in t) is orthogonal to the orthogonal complement of span(E_-, E_+)."""
    DE = n // 2
    M = np.zeros((DE + 1, 2))
    M[:len(Em), 0] = Em; M[:len(Ep), 1] = Ep
    u, s, vt = np.linalg.svd(M)
    comp = u[:, 2:]          # basis of orthogonal complement in R^{DE+1}
    rows = []
    for v in comp.T:
        r = np.zeros(n + 1)
        for l in range(DE + 1):
            r[2 * l] = (-1) ** l * v[l]
        rows.append(r)
    return rows


def coeff_rows_O_in_span(n, Om, Op):
    DO = (n - 1) // 2
    M = np.zeros((DO + 1, 2))
    M[:len(Om), 0] = Om; M[:len(Op), 1] = Op
    u, s, vt = np.linalg.svd(M)
    comp = u[:, 2:]
    rows = []
    for v in comp.T:
        r = np.zeros(n + 1)
        for l in range(DO + 1):
            r[2 * l + 1] = (-1) ** l * v[l]
        rows.append(r)
    return rows


def candidate(x, n, Em, Ep, Om, Op, which='E'):
    A = list(contact_matrix(x, n, Em, Ep, Om, Op))
    extra = coeff_rows_E_in_span(n, Em, Ep) if which == 'E' else coeff_rows_O_in_span(n, Om, Op)
    S = np.sqrt(x[0] * x[-1]); tau = np.sqrt(S)
    D = np.diag(tau ** (-np.arange(n + 1.0)))
    rows = [r / np.abs(r).max() for r in A] + [r / (np.abs(r).max() + 1e-300) for r in extra]
    M = np.array(rows) @ D
    u, s, vt = np.linalg.svd(M)
    b = D @ vt[-1]
    # choose sign: leading coefficient positive (or next)
    lead = b[-1] if abs(b[-1]) > 1e-12 * np.abs(b).max() else b[-2]
    if lead < 0:
        b = -b
    return b, s[-1] / s[0], s[-2] / s[0]
