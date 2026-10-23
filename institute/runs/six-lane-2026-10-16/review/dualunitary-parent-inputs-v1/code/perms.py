"""Permutation-matrix inputs (shared INPUT data only; no linear algebra here).

Convention: |ij> <-> d*i + j; a permutation is given by its ones (row, col): P[row][col] = 1 iff P|col> = |row>.
"""


def from_map(d, f):
    """ones of the permutation |ij> -> |f(i,j)>."""
    ones = []
    for i in range(d):
        for j in range(d):
            k, l = f(i, j)
            ones.append((d * k + l, d * i + j))
    return sorted(ones)


# (C7), arXiv:2508.04777v3 Appendix C, PDF p.27, extracted from word coordinates (sources/c7page.bbox.html)
C7 = [(0, 0), (1, 8), (2, 4), (3, 5), (4, 1), (5, 6), (6, 7), (7, 3), (8, 2)]
# [44] = arXiv:2212.06737v2, eq. (A14) (rows read from the layout text lines 899-913)
REF44_A14 = [(0, 0), (1, 4), (2, 8), (3, 5), (4, 6), (5, 1), (6, 7), (7, 2), (8, 3)]


def gf4_add(a, b):
    return a ^ b


_GF4_MUL = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]   # 2 = w, 3 = w^2 = w + 1


def gf4_mul(a, b):
    return _GF4_MUL[a][b]


PERMS = {
    "C7": (3, sorted(C7)),
    "closed_form_C7": (3, from_map(3, lambda i, j: ((2 * i + j) % 3, (i + j) % 3))),
    "eq14": (3, from_map(3, lambda i, j: ((i + j) % 3, (2 * i + j) % 3))),
    "verbal_secIIIA": (3, from_map(3, lambda i, j: ((2 * i + j) % 3, (2 * i + 2 * j) % 3))),
    "ref44_A14": (3, sorted(REF44_A14)),
    # control: dual but not T-dual (M = [[0,1],[1,1]] has m11 = 0)
    "dual_not_tdual": (3, from_map(3, lambda i, j: (j % 3, (i + j) % 3))),
    # d = 4 control: (k,l) = (i + j, i + w j) over GF(4) -> MDS [4,2,3]_4 code -> 2-unitary
    "P16_gf4": (4, from_map(4, lambda i, j: (gf4_add(i, j), gf4_add(i, gf4_mul(2, j))))),
}
