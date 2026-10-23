"""Aid: block-level Step-1 inequality (9.1) when blocks have net mass >= 0 (j <= B merges)."""
from z3 import Int, And, Or
from z3lib import g, prove
p, kap, B, A, k, kb, Dj1, dt, nb, z0 = [Int(x) for x in 'p kap B A k kb Dj1 dt nb z0'.split()]
R = A + B; kB = kap - B; D = A - B
base = [p >= 5, B >= 1, B <= kap, A >= B, A <= 2 * p - 1, kap <= p - 1, 2 * kap == R + k - 2 * p,
        kb >= 3, kb <= k, nb >= 1, nb <= kb - 2, Dj1 >= 0, dt >= 0, D - Dj1 - dt >= 0,
        k - kb <= B, dt <= 2 * kB - 2]
S = g(p, 1, B + Dj1 + dt, kap) + g(p, 1, A - Dj1, kap) + g(p, 1, A - dt, kap)
mdl = prove(base, S >= p - 1, 'net>=0 blocks, j<=B')
if mdl is not None:
    print('   ', {str(v): mdl[v] for v in [p, kap, B, A, k, kb, Dj1, dt, nb]})
# with the number of zero-mass blocks z0 bounded by B - j
base2 = base + [z0 >= 0, z0 <= B - (k - kb), Dj1 >= nb - z0, D - Dj1 - dt >= kb - nb - 1 - z0]
mdl = prove(base2, S >= p - 1, 'net>=0 blocks, j + #zero-blocks <= B')
if mdl is not None:
    print('   ', {str(v): mdl[v] for v in [p, kap, B, A, k, kb, Dj1, dt, nb, z0]})
