"""Exact gate definitions and source conventions (no numerics here).

Conventions (survey arXiv:2508.04777v3, layout l.239-241, eqs. (10),(11a)):
  |ij> <-> 3i+j ;  R: <ij|U^R|ab> = <ia|U|jb> ;  Gamma: <ib|U^G|ja> = <ia|U|jb>.
Entries are any ring elements (sympy expressions, python ints/Fractions, numpy scalars).
"""
d = 3
N = d * d


def idx(i, a):
    return d * i + a


def realign(U):
    """U^R[3i+j][3a+b] = U[3i+a][3j+b] (source R)."""
    return [[U[idx(i, a)][idx(j, b)] for a in range(d) for b in range(d)] for i in range(d) for j in range(d)]


def ptrans(U):
    """U^G[3i+b][3j+a] = U[3i+a][3j+b] (source Gamma: transpose of the second-factor indices)."""
    G = [[None] * N for _ in range(N)]
    for i in range(d):
        for a in range(d):
            for j in range(d):
                for b in range(d):
                    G[idx(i, b)][idx(j, a)] = U[idx(i, a)][idx(j, b)]
    return G


def ptrans1(U):
    """Thesis Gamma_1: transpose of the first-factor (block) indices, U^G1[3j+a][3i+b] = U[3i+a][3j+b]."""
    G = [[None] * N for _ in range(N)]
    for i in range(d):
        for a in range(d):
            for j in range(d):
                for b in range(d):
                    G[idx(j, a)][idx(i, b)] = U[idx(i, a)][idx(j, b)]
    return G


def perm_matrix(f, one=1, zero=0):
    """Matrix of |ij> -> |f(i,j)>: P[row][col] = 1 iff P|col> = |row>."""
    P = [[zero] * N for _ in range(N)]
    for i in range(d):
        for j in range(d):
            k, l = f(i, j)
            P[idx(k, l)][idx(i, j)] = one
    return P


def swap(one=1, zero=0):
    return perm_matrix(lambda i, j: (j, i), one, zero)


def identity(one=1, zero=0):
    return perm_matrix(lambda i, j: (i, j), one, zero)


def P9(one=1, zero=0):
    """Source (C7) as pinned by the prior lane: P9|ij> = |2i+j, i+j> mod 3."""
    return perm_matrix(lambda i, j: ((2 * i + j) % 3, (i + j) % 3), one, zero)


# Thesis [62] eq. (3.36), read from the rendered page (07_chapter3.pdf p.16). Each row: list of (col, coeff_name)
# with coeff_name in {'c','-c','s','-s','1'}.
U36_ROWS = [
    [(2, '-c'), (3, 's')],
    [(1, '1')],
    [(0, 'c'), (8, 's')],
    [(0, 's'), (8, '-c')],
    [(5, 's'), (7, 'c')],
    [(4, 's'), (6, 'c')],
    [(5, '-c'), (7, 's')],
    [(4, 'c'), (6, '-s')],
    [(2, 's'), (3, 'c')],
]


def U36(c, s, one=1, zero=0):
    """Thesis T-dual family U(theta), c = cos(theta), s = sin(theta)."""
    val = {'c': c, '-c': -c, 's': s, '-s': -s, '1': one}
    U = [[zero] * N for _ in range(N)]
    for r, row in enumerate(U36_ROWS):
        for col, name in row:
            U[r][col] = val[name]
    return U


def matmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), start=0 * A[0][0]) for j in range(len(B[0]))]
            for i in range(len(A))]
