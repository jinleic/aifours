#!/usr/bin/env python3
"""Exact budgets and physical endpoint certificates for extended noise window."""
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
    t = F(1, 200)
    eta = F(9, 40)
    vn, sn = F(23, 200), F(23, 400)
    dn, wn, cn = F(5), F(163, 20), F(47, 1000)
    qn, on, gap, ex = F(41, 5), F(21, 5), F(11, 10), F(103, 100)
    assert 4 + 6*t + 4*t*t + t**3 < dn
    assert 1-t-t*t > 0
    assert 8 + vn < wn
    comm = 2*vn*sn + 2*dn*sn*sn
    assert comm < cn and wn+cn < qn and 4+vn+cn < on
    assert (1-2*eta*sn)*ex > 1
    first = ex*(dn*(2*sn)**3/6 + vn*(2*sn)**2/2 + wn*(2*sn))
    assert first < 1
    perturb = eta*vn + eta**2*qn
    assert perturb == F(441, 1000) and 2-2*perturb > gap
    loss = 3*eta + 3*cn*eta**2 + 3*on**2*eta**2/gap
    assert loss < F(13, 4)
    assert 2*eta**2 > 20*t
    assert (1-t*t)/4 > F(15, 64)
    assert (1-t)*F(15, 32) > F(15, 64)
    assert 1-2*t**6 > F(15, 64)

    vec = [e.ZERO]*16
    vec[0],vec[3],vec[7],vec[15] = e.z(1500),e.z(1),e.z(0,2),e.z(2)
    rho = [[e.scale(e.mul(vec[i],e.conj(vec[j])),F(1,2250009)) for j in range(16)] for i in range(16)]
    assert rho == e.adjoint(rho) and e.matmul(rho,rho)==rho and e.trace(rho)==e.ONE
    P=e.zero(16)
    for i in (0,1,2): P[i][i]=e.ONE
    ident=e.zero(16)
    for i in range(16): ident[i][i]=e.ONE
    upper1,upper2=F('0.0637593981'),F('0.0631249811')
    rows=[]
    for p in (1-t,1+t):
        out=e.channel(rho,p)
        assert out==b.direct_pauli(rho,p)
        assert len(c.positive_definite_ldl(out))==16
        assert len(c.positive_definite_ldl(e.add_matrix(e.scale_matrix(ident,upper1),e.scale_matrix(out,-1))))==16
        inertia=m.hermitian_inertia(e.add_matrix(e.scale_matrix(ident,upper2),e.scale_matrix(out,-1)))
        assert inertia==(15,1,0)
        a,bb=(1+t)/2,(1-t)/2
        ref=a**4+2*a**3*bb
        upper=upper1+2*upper2
        assert ref>upper
        actual=P if p<1 else e.global_spinflip(P)
        assert actual==e.adjoint(actual) and e.matmul(actual,actual)==actual and e.trace(actual)==e.z(3)
        tr=e.trace(e.matmul(actual,out))
        assert tr[1]==0 and tr[0]<upper
        arr=np.array([[complex(float(x[0]),float(x[1])) for x in row] for row in out])
        eig=np.linalg.eigvalsh(arr)[::-1]
        rows.append({'p':str(p),'full_pauli_equals_sequential':True,'output_positive_LDL_pivots':16,
                     'lambda1_upper_positive_LDL_pivots':16,'lambda2_upper_inertia':list(inertia),
                     'certified_top3_upper':str(upper),'reference_top3':str(ref),
                     'gap_lower':str(ref-upper),'same_actual_projector_trace':str(tr[0]),
                     'numerical_top3':[float(x) for x in eig[:3]]})
    print(json.dumps({'scope':'exact finite scalar budgets and one state at two endpoints, not a universal proof',
                      't':str(t),'eta':str(eta),'commutator':str(comm),'first_remainder':str(first),
                      'perturbation':str(perturb),'loss':str(loss),'far_actual_deficit':str(2*eta**2),
                      'far_required':str(20*t),'rows':rows},indent=2,sort_keys=True))


if __name__=='__main__': main()
