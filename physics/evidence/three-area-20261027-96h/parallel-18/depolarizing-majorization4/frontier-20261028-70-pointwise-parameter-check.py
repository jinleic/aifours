#!/usr/bin/env python3
"""Exact polynomial-channel checks for the two-parameter lambda2 obstruction."""

import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location("bloch",ROOT/"frontier-20261028-12-bloch-gap-check.py")
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
e=b.e


def outer(u,v):return [[e.mul(u[i],e.conj(v[j])) for j in range(16)] for i in range(16)]


def main():
    u=[e.ZERO]*16;u[0]=e.ONE
    v=[e.ZERO]*16
    for i in (3,5,15):v[i]=e.ONE
    inputs=[outer(u,u),e.add_matrix(outer(u,v),outer(v,u)),outer(v,v)]
    qs=(F(0),F(1,4),F(1,2),F(3,4),F(1))
    count=0
    for q in qs:
        p=1-q;a=(1+q)/2;c=(1-q)/2;L=a**3*c
        matrices=[]
        for inp in inputs:
            actual=e.channel(inp,p);assert actual==b.direct_pauli(inp,p)
            matrices.append(actual);count+=1
        expected={
          (0,0):(a**4,F(0),2*a*a*c*c+c**4),
          (2,2):(L,F(0),L+2*a*c**3),
          (4,4):(L,F(0),L+2*a*c**3),
          (2,4):(F(0),F(0),q*q*a*c),
          (4,2):(F(0),F(0),q*q*a*c),
          (2,7):(F(0),q*q*a*c,F(0)),
          (7,2):(F(0),q*q*a*c,F(0)),
          (4,7):(F(0),q*q*a*c,F(0)),
          (7,4):(F(0),q*q*a*c,F(0)),
          (7,7):(a*c**3,F(0),3*L),
        }
        for (i,j),coeff in expected.items():assert tuple(M[i][j] for M in matrices)==tuple(e.z(x) for x in coeff)
        for i,j in ((0,2),(0,4),(0,7),(2,0),(4,0),(7,0)):
            assert all(M[i][j]==e.ZERO for M in matrices)
        beta=2*q
        poly=[F(0)]*5
        vpoly={2:(F(1),F(0)),4:(F(1),F(0)),7:(F(0),beta)}
        for i in vpoly:
            for j in vpoly:
                for d,vi in enumerate(vpoly[i]):
                    for k,M in enumerate(matrices):
                        assert M[i][j][1]==0
                        for dd,vj in enumerate(vpoly[j]):poly[d+k+dd]+=vi*M[i][j][0]*vj
        ref=[2*L,F(0),(6+beta**2)*L,F(0),3*beta**2*L]
        difference=[poly[k]-ref[k] for k in range(5)]
        assert difference==[F(0),F(0),2*a*c*q*(2*q*q+q-2),F(0),F(0)]
        assert matrices[0][0][0][0]-L==q*a**3
        assert matrices[2][0][0][0]-3*L==-q*c*(3*a*a+a*c+c*c)
    print(json.dumps({"scope":"exact polynomial coefficient checks, not universal k3 proof", "distinct_q_values":[str(q) for q in qs],"degree_at_most_4_channel_entry_identities_checked_at_each_q":10,"original_Pauli_vs_sequential_coefficient_matrices":count,"zero_cross_entry_identities_per_q":6,"optimized_w_numerator_z2":"2ab q (2q^2+q-2)","u_gap_numerator":"q (a^3-b(3a^2+ab+b^2)z^2)"},indent=2,sort_keys=True))


if __name__=="__main__":main()
