#!/usr/bin/env python3
"""Exact scalar budgets and physical endpoint for normalized-tube candidate."""
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location('endpoint', ROOT / 'frontier-20261028-66-noise-endpoint-check.py')
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)
m, c, b, e = d.m, d.c, d.b, d.e


def main():
    eta = F(1, 8)
    v = F(23, 1000)
    s = F(3, 250)
    d_norm = F(5)
    w_norm = F(17)
    q_norm = F(17)
    off_bound = F(403, 100)
    gap = F(7, 5)
    comm = 2 * v * s + 2 * d_norm * s * s
    first = d_norm * (2 * s)**3 / 3 + v * (2 * s)**2 + 2 * w_norm * (2 * s)
    assert comm < F(1, 500)
    assert first < F(817, 1000)
    assert 4 + v + comm < off_bound
    perturbation = eta * v + eta**2 * q_norm
    assert perturbation < F(27, 100)
    assert 2 - 2 * F(27, 100) > gap
    loss = 3 * F(817, 1000) * eta + 3 * F(1, 500) * eta**2 + 3 * off_bound**2 * eta**2 / gap
    assert loss < 1
    assert 20 * F(1, 1000) < 2 * eta**2
    assert F(15, 4) - loss > F(11, 4)

    vec = [e.ZERO] * 16
    vec[0], vec[3], vec[7], vec[15] = e.z(1500), e.z(1), e.z(0, 2), e.z(2)
    rho = [[e.scale(e.mul(vec[i], e.conj(vec[j])), F(1, 2250009)) for j in range(16)] for i in range(16)]
    assert rho == e.adjoint(rho) and e.matmul(rho, rho) == rho and e.trace(rho) == e.ONE
    P = e.zero(16)
    for i in (0, 1, 2):
        P[i][i] = e.ONE
    ident = e.zero(16)
    for i in range(16):
        ident[i][i] = e.ONE
    upper1 = F('0.0627503737')
    upper2 = F('0.0626249993')
    rows = []
    for p in (1-F(1, 1000), 1+F(1, 1000)):
        out = e.channel(rho, p)
        assert out == b.direct_pauli(rho, p)
        assert len(c.positive_definite_ldl(out)) == 16
        assert len(c.positive_definite_ldl(e.add_matrix(e.scale_matrix(ident, upper1), e.scale_matrix(out, -1)))) == 16
        inertia = m.hermitian_inertia(e.add_matrix(e.scale_matrix(ident, upper2), e.scale_matrix(out, -1)))
        assert inertia == (15, 1, 0)
        t = abs(1-p)
        a, bb = (1+t)/2, (1-t)/2
        ref = a**4 + 2*a**3*bb
        upper = upper1 + 2*upper2
        assert ref > upper
        actual_p = P if p < 1 else e.global_spinflip(P)
        assert actual_p == e.adjoint(actual_p) and e.matmul(actual_p, actual_p) == actual_p and e.trace(actual_p) == e.z(3)
        tr = e.trace(e.matmul(actual_p, out))
        assert tr[1] == 0 and tr[0] < upper
        arr = np.array([[complex(float(x[0]), float(x[1])) for x in row] for row in out])
        eig = np.linalg.eigvalsh(arr)[::-1]
        rows.append({'p': str(p), 'full_pauli_equals_sequential': True,
                     'output_positive_LDL_pivots': 16, 'lambda1_upper_positive_LDL_pivots': 16,
                     'lambda2_upper_inertia': list(inertia), 'certified_top3_upper': str(upper),
                     'reference_top3': str(ref), 'gap_lower': str(ref-upper),
                     'same_actual_projector_trace': str(tr[0]),
                     'numerical_top3': [float(x) for x in eig[:3]]})
    print(json.dumps({'scope': 'exact finite scalar arithmetic and one physical input at endpoints; not a universal proof',
                      'eta': str(eta), 'commutator_bound': str(comm),
                      'first_conjugation_remainder_constant': str(first),
                      'perturbation_bound': str(perturbation), 'loss_coefficient': str(loss),
                      'far_actual_deficit': str(2*eta**2), 'far_required': str(20*F(1,1000)),
                      'state': '(1500|0000>+|0011>+2i|0111>+2|1111>)/sqrt(2250009)',
                      'rows': rows}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
