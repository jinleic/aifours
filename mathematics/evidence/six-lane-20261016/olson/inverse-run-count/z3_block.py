"""Aid: z3 check of the C0 Step-1 inequality (9.1) at BLOCK level for mixed all-odd words:
blocks have net mass >= 1; k runs grouped into kb blocks (j = k - kb merges); interval chain of
blocks; prefix of nb blocks with net Dj1 >= nb; added block t with net dt >= 1; suffix net >= 1."""
from z3 import Int, And, Or
from z3lib import g, prove
p, kap, B, A, k, kb, Dj1, dt, nb = [Int(x) for x in 'p kap B A k kb Dj1 dt nb'.split()]
R = A + B; kB = kap - B; D = A - B
base = [p >= 5, B >= 1, B <= kap, A >= B, A <= 2 * p - 1, kap <= p - 1, 2 * kap == R + k - 2 * p,
        kb >= 3, kb <= k, nb >= 1, nb <= kb - 2, Dj1 >= nb, dt >= 1, D - Dj1 - dt >= kb - nb - 1,
        D >= kb, dt <= 2 * kB - 2]
S = g(p, 1, B + Dj1 + dt, kap) + g(p, 1, A - Dj1, kap) + g(p, 1, A - dt, kap)
for nm, extra in [('j <= B', [k - kb <= B]), ('j <= 2B', [k - kb <= 2 * B]), ('j free', []),
                  ('j <= B, R<=2p-3', [k - kb <= B, R <= 2 * p - 3])]:
    mdl = prove(base + extra, S >= p - 1, nm)
    if mdl is not None:
        print('   ', {str(v): mdl[v] for v in [p, kap, B, A, k, kb, Dj1, dt, nb]})
