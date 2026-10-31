#!/usr/bin/env python3
"""Exact six-term real state disproving a third-frame-eigenvalue shortcut."""

import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
spec = importlib.util.spec_from_file_location("complex_frame", ROOT / "frontier-20261028-31-complex-frame-counterexample.py")
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
d, b, e = c.d, c.b, c.e


def rectangular_rank(matrix):
    rows, cols = len(matrix), len(matrix[0])
    data = [row[:] for row in matrix]
    rank = 0
    for col in range(cols):
        pivot = next((i for i in range(rank, rows) if data[i][col]), None)
        if pivot is None:
            continue
        data[rank], data[pivot] = data[pivot], data[rank]
        p = data[rank][col]
        data[rank] = [x / p for x in data[rank]]
        for i in range(rank + 1, rows):
            p = data[i][col]
            if p:
                data[i] = [data[i][j] - p * data[rank][j] for j in range(cols)]
        rank += 1
        if rank == rows:
            break
    return rank


def main():
    v = [F(0)] * 16
    for i, value in ((0, 2), (5, 1), (6, 1), (9, 1), (10, 1), (15, 1)):
        v[i] = F(value, 3)
    rho = [[e.z(v[i] * v[j]) for j in range(16)] for i in range(16)]
    assert rho == e.adjoint(rho) and e.matmul(rho, rho) == rho and e.trace(rho) == e.ONE
    cut_ranks = []
    for n in (1, 2):
        for active in itertools.combinations(range(4), n):
            if n == 2 and 0 not in active:
                continue
            other = tuple(i for i in range(4) if i not in active)
            matrix = [[F(0) for _ in range(2**len(other))] for _ in range(2**len(active))]
            for index in range(16):
                bits = [(index >> (3 - i)) & 1 for i in range(4)]
                row = sum(bits[i] * 2**(len(active) - 1 - j) for j, i in enumerate(active))
                col = sum(bits[i] * 2**(len(other) - 1 - j) for j, i in enumerate(other))
                matrix[row][col] = v[index]
            rank = rectangular_rank(matrix)
            assert rank >= 2
            cut_ranks.append({"party_indices_zero_based": list(active), "schmidt_rank": rank})
    frame = d.local_pauli_frame(rho)
    even = [0, 3, 5, 6, 9, 10, 12, 15]
    odd = [1, 2, 4, 7, 8, 11, 13, 14]
    E = [[16,0,0,0,0,0,0,-8],[0,0,0,0,0,0,0,0],[0,0,4,0,0,-4,0,0],[0,0,0,4,-4,0,0,0],[0,0,0,-4,4,0,0,0],[0,0,-4,0,0,4,0,0],[0,0,0,0,0,0,0,0],[-8,0,0,0,0,0,0,4]]
    O = [[12,4,0,6,0,6,0,0],[4,12,0,6,0,6,0,0],[0,0,12,0,4,0,6,6],[6,6,0,6,0,4,0,0],[0,0,4,0,12,0,6,6],[6,6,0,4,0,6,0,0],[0,0,6,0,6,0,6,4],[0,0,6,0,6,0,4,6]]
    for ii, i in enumerate(even):
        for jj, j in enumerate(even):
            assert frame[i][j] == e.z(F(E[ii][jj], 9))
    for ii, i in enumerate(odd):
        for jj, j in enumerate(odd):
            assert frame[i][j] == e.z(F(O[ii][jj], 9))
    assert all(frame[i][j] == e.ZERO for i in even for j in odd)
    W = [[e.ZERO for _ in range(3)] for _ in range(16)]
    for index, value in ((0, -2), (15, 1)):
        W[index][0] = e.z(value)
    for index, value in ((1, 3), (2, 3), (7, 2), (11, 2)):
        W[index][1] = e.z(value)
    for index, value in ((4, 3), (8, 3), (13, 2), (14, 2)):
        W[index][2] = e.z(value)
    ident = e.zero(16)
    for i in range(16):
        ident[i][i] = e.ONE
    H = c.gram(W, e.add_matrix(frame, e.scale_matrix(ident, -2)))
    expected = [[e.z(F(10,9)),e.ZERO,e.ZERO],[e.ZERO,e.z(F(188,9)),e.ZERO],[e.ZERO,e.ZERO,e.z(F(188,9))]]
    assert H == expected
    P = e.zero(16)
    for col, norm in enumerate((5, 26, 26)):
        for i in range(16):
            for j in range(16):
                P[i][j] = e.add(P[i][j], e.scale(e.mul(W[i][col], e.conj(W[j][col])), F(1,norm)))
    assert P == e.adjoint(P) and e.matmul(P, P) == P and e.trace(P) == e.z(3)
    frame_trace = e.trace(e.matmul(P, frame))
    assert frame_trace == e.z(F(916,117))
    originals = []
    for p in (F(2, 3), F(4, 3)):
        out = e.channel(rho, p)
        assert out == b.direct_pauli(rho, p)
        assert len(c.positive_definite_ldl(out)) == 16
        upper = e.add_matrix(e.scale_matrix(ident, F(13,100)), e.scale_matrix(out, -1))
        assert len(c.positive_definite_ldl(upper)) == 16
        ref = F(32,81)
        assert F(39,100) < ref
        tr = e.trace(e.matmul(P, out))
        assert tr[1] == 0 and tr[0] < F(39,100)
        arr = np.array([[complex(float(z[0]),float(z[1])) for z in row] for row in out])
        eig = np.linalg.eigvalsh(arr)[::-1]
        originals.append({"p":str(p),"exact_original_positive_ldl_pivots":16,"exact_upper_13_over_100_ldl_pivots":16,"exact_original_top3_upper":"39/100","reference_top3":"32/81","certified_margin_lower":"41/8100","same_P_trace":str(tr[0]),"numeric_top3":[float(t) for t in eig[:3]],"numeric_top3_sum":float(sum(eig[:3]))})
    print(json.dumps({"scope":"exact physical counterexample to auxiliary lambda3<=2, not an original-channel violation", "input":"(2|0000>+|0101>+|0110>+|1001>+|1010>+|1111>)/3", "schmidt_cut_ranks":cut_ranks, "frame_parity_blocks":"verified exactly", "frame_lambda3_exact":"20/9", "frame_kyfan3_exact":"(46+6 sqrt(17))/9", "same_P_frame_trace":str(frame_trace[0]), "gram_F_minus_2I_diagonal":["10/9","188/9","188/9"], "original_channel_checks":originals}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
