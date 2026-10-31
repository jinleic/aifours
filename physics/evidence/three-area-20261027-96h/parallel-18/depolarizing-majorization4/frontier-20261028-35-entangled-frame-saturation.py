#!/usr/bin/env python3
"""Exact entangled saturation of auxiliary Pauli-frame k3=8, not a global proof."""

import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("simple_frame", ROOT / "frontier-20261028-33-simple-frame-witness.py")
sc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sc)
c, d, b, e = sc.c, sc.d, sc.b, sc.e


def hermitian_inertia(M):
    assert M == e.adjoint(M)
    work = [row[:] for row in M]
    positive = negative = zeros = 0
    for k in range(16):
        pivot_idx = next((i for i in range(k, 16) if work[i][i] != e.ZERO), None)
        if pivot_idx is None:
            assert all(work[i][j] == e.ZERO for i in range(k, 16) for j in range(k, 16))
            zeros += 16 - k
            break
        if pivot_idx != k:
            work[k], work[pivot_idx] = work[pivot_idx], work[k]
            for row in work:
                row[k], row[pivot_idx] = row[pivot_idx], row[k]
        pivot = work[k][k]
        assert pivot[1] == 0 and pivot[0] != 0
        positive += pivot[0] > 0
        negative += pivot[0] < 0
        for i in range(k + 1, 16):
            for j in range(k + 1, 16):
                work[i][j] = c.sub(work[i][j], e.scale(e.mul(work[i][k], work[k][j]), 1 / pivot[0]))
    return positive, negative, zeros


def main():
    v = [F(0)] * 16
    for i, value in ((0,4),(5,1),(6,1),(9,1),(10,1),(15,1)):
        v[i] = F(value)
    rho = [[e.z(v[i]*v[j]/21) for j in range(16)] for i in range(16)]
    assert rho == e.adjoint(rho) and e.matmul(rho, rho) == rho and e.trace(rho) == e.ONE
    cuts = []
    for size in (1,2):
        for active in itertools.combinations(range(4), size):
            if size == 2 and 0 not in active:
                continue
            rest = tuple(i for i in range(4) if i not in active)
            matrix = [[F(0) for _ in range(2**len(rest))] for _ in range(2**len(active))]
            for index in range(16):
                bits = [(index >> (3-i)) & 1 for i in range(4)]
                row = sum(bits[i]*2**(len(active)-1-j) for j,i in enumerate(active))
                col = sum(bits[i]*2**(len(rest)-1-j) for j,i in enumerate(rest))
                matrix[row][col] = v[index]
            rank = sc.rectangular_rank(matrix)
            assert rank >= 2
            cuts.append({"parties_zero_based":list(active),"rank":rank})
    for site in range(4):
        assert e.local_marginal(rho, site) == [[e.z(F(6,7)),e.ZERO],[e.ZERO,e.z(F(1,7))]]
    frame = d.local_pauli_frame(rho)
    expected = {F(68,21):1,F(50,21):2,F(32,21):2,F(8,21):2,F(2,21):2,F(0):7}
    eig = d.verify_spectrum(frame, expected)
    assert sum(eig[:3]) == 8 and eig[1] == eig[2] == F(50,21)
    vectors = [[F(0)]*16 for _ in range(3)]
    vectors[0][0],vectors[0][15] = -4,1
    for i in (1,2): vectors[1][i] = 2
    for i in (7,11): vectors[1][i] = 1
    for i in (4,8): vectors[2][i] = 2
    for i in (13,14): vectors[2][i] = 1
    P = e.zero(16)
    for vector,norm in zip(vectors,(17,10,10)):
        assert sum(x*x for x in vector) == norm
        for i in range(16):
            for j in range(16):
                P[i][j] = e.add(P[i][j],e.z(F(vector[i]*vector[j],norm)))
    assert P == e.adjoint(P) and e.matmul(P,P)==P and e.trace(P)==e.z(3)
    assert e.trace(e.matmul(P,frame))==e.z(8)
    ident=e.zero(16)
    for i in range(16): ident[i][i]=e.ONE
    rows=[]
    for p in (F(2,3),F(4,3)):
        out=e.channel(rho,p)
        assert out==b.direct_pauli(rho,p)
        assert len(c.positive_definite_ldl(out))==16
        upper1=e.add_matrix(e.scale_matrix(ident,F(1,6)),e.scale_matrix(out,-1))
        assert len(c.positive_definite_ldl(upper1))==16
        upper2=e.add_matrix(e.scale_matrix(ident,F(1,10)),e.scale_matrix(out,-1))
        inertia=hermitian_inertia(upper2)
        assert inertia==(15,1,0)
        ref=F(32,81)
        assert F(11,30)<ref
        sameP=e.trace(e.matmul(P,out))
        assert sameP[1]==0 and sameP[0]<F(11,30)
        arr=np.array([[complex(float(z[0]),float(z[1])) for z in row] for row in out])
        ev=np.linalg.eigvalsh(arr)[::-1]
        rows.append({"p":str(p),"original_output_positive_ldl_pivots":16,"lambda1_upper_1_over_6_ldl_pivots":16,"one_tenth_minus_output_inertia":[15,1,0],"certified_top3_upper":"11/30","reference_top3":"32/81","certified_margin_lower":"23/810","same_P_original_trace":str(sameP[0]),"numerical_top3":[float(x) for x in ev[:3]],"numerical_top3_sum":float(sum(ev[:3]))})
    print(json.dumps({"scope":"one exact physical entangled saturation of auxiliary frame top3=8; not a global inequality proof or original-channel counterexample", "state":"(4|0000>+|0101>+|0110>+|1001>+|1010>+|1111>)/sqrt(21)", "schmidt_cut_ranks":cuts, "all_local_bloch_radii":"5/7", "frame_spectrum":[[str(k),v] for k,v in expected.items()], "frame_top3":"8", "same_actual_P_frame_trace":"8", "original_channel_checks":rows}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
