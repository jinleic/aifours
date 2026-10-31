#!/usr/bin/env python3
"""Exact polynomial identities for an original-channel pointwise obstruction."""

import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("bloch",ROOT/"frontier-20261028-12-bloch-gap-check.py")
b=importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
e=b.e


def outer(u,v):
    return [[e.mul(u[i],e.conj(v[j])) for j in range(16)] for i in range(16)]


def main():
    v0=[e.ZERO]*16;v0[0]=e.ONE
    v1=[e.ZERO]*16
    for i in (3,5,15):v1[i]=e.ONE
    inputs=[outer(v0,v0),e.add_matrix(outer(v0,v1),outer(v1,v0)),outer(v1,v1)]
    matrices=[]
    for matrix in inputs:
        direct=b.direct_pauli(matrix,F(1,5))
        sequential=e.channel(matrix,F(1,5))
        assert direct==sequential
        matrices.append(direct)
    expected={
        (0,0):(F(6561,10000),F(0),F(163,10000)),
        (2,2):(F(729,10000),F(0),F(747,10000)),
        (4,4):(F(729,10000),F(0),F(747,10000)),
        (2,4):(F(0),F(0),F(36,625)),
        (4,2):(F(0),F(0),F(36,625)),
        (2,7):(F(0),F(36,625),F(0)),
        (7,2):(F(0),F(36,625),F(0)),
        (4,7):(F(0),F(36,625),F(0)),
        (7,4):(F(0),F(36,625),F(0)),
        (7,7):(F(9,10000),F(0),F(2187,10000)),
    }
    for (i,j),coeff in expected.items():
        assert tuple(matrix[i][j] for matrix in matrices)==tuple(e.z(x) for x in coeff)
    for i,j in ((0,2),(0,4),(0,7),(2,0),(4,0),(7,0)):
        assert all(matrix[i][j]==e.ZERO for matrix in matrices)
    # N(z)*<w(z)|sigma(z)|w(z)>; w_2=w_4=1,w_7=3z/2.
    pol=[F(0)]*5
    components={2:(F(1),F(0)),4:(F(1),F(0)),7:(F(0),F(3,2))}
    for i in components:
        for j in components:
            for u,wu in enumerate(components[i]):
                for k,matrix in enumerate(matrices):
                    assert matrix[i][j][1]==0
                    for v,wv in enumerate(components[j]):
                        pol[u+k+v]+=wu*matrix[i][j][0]*wv
    reference=F(729,10000)
    ref_pol=[2*reference,F(0),F(33,4)*reference,F(0),F(27,4)*reference]
    difference=[pol[i]-ref_pol[i] for i in range(5)]
    assert difference==[F(0),F(0),F(27,2500),F(0),F(0)]
    d0=[matrices[0][0][0][0]-reference,matrices[1][0][0][0],matrices[2][0][0][0]-3*reference]
    assert d0==[F(729,1250),F(0),-F(253,1250)]
    print(json.dumps({"scope":"exact coefficient-matrix identities for one analytic original-channel family; no all-state k3 claim", "input_polynomial_matrices":3, "independent_full_Pauli_vs_sequential_checks":3,"listed_channel_entry_polynomials":len(expected),"parity_cross_polynomials_zero":6,"w_rayleigh_gap_numerator_coefficients_z0_to_z4":[str(x) for x in difference],"u_rayleigh_gap_numerator_coefficients_z0_to_z2":[str(x) for x in d0],"exact_physical_p":"1/5"},indent=2,sort_keys=True))


if __name__=="__main__":main()
