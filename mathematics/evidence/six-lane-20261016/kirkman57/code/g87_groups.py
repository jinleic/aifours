"""Groups for the LKTS(87) attempt: points {inf} ∪ Z43 x {0,1}; (x,j) -> 43j+x, inf -> 86.
G903 = Z43 ⋊ Z21 acting identically on both copies: tau:(x,j)->(x+1,j), m:(x,j)->(9x,j)
(9 has order 21 mod 43; omega = 9^7 = 36 has order 3, lambda = 9^3 = 41 has order 7)."""
N = 87
INF = 86
Q = 43

def P(f):
    out = [0] * N
    for j in range(2):
        for x in range(Q):
            x2, j2 = f(x, j)
            out[Q * j + x] = Q * j2 + (x2 % Q)
    out[INF] = INF
    return tuple(out)

tau = P(lambda x, j: (x + 1, j))
m21 = P(lambda x, j: (9 * x, j))
omega = P(lambda x, j: (36 * x, j))
lam = P(lambda x, j: (41 * x, j))
G_GENS = [tau, m21]
Z21 = [m21]
Z43 = [tau]
