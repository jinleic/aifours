"""Exact polynomial form of slice concavity of psi.

psi strictly concave on the slice through m(mu)  <=>  M(mu) := 5*Phi*(2 diag(m) - S2) + 3 m m^T is PSD
with kernel exactly span(1)  <=>  the leading 3x3 principal block M_123 is positive definite
(because M 1 = 0).  Entries are integer homogeneous polynomials of degree 10 in mu.
This script builds the Sylvester minors P1 (deg 10), P2 (deg 20), P3 (deg 30) with python-flint
and reports coefficient-sign statistics, for every choice of the dropped index.
"""
import sys, json, itertools, time
import flint
sys.path.insert(0, 'code')
from model import spectra, multinomial

rainbow = not (len(sys.argv) > 1 and sys.argv[1] == 'plain')
S = spectra(5, rainbow)
ctx = flint.fmpz_mpoly_ctx.get(('x', 'y', 'z', 'w'), 'degrevlex')
X = ctx.gens()

def mono(s):
    r = ctx.from_dict({tuple(s): 1})
    return r

Phi = sum((multinomial(s) * mono(s) for s in S), ctx.from_dict({}))
m = [sum((multinomial(s) * s[k] * mono(s) for s in S), ctx.from_dict({})) for k in range(4)]
S2 = [[sum((multinomial(s) * s[k] * s[l] * mono(s) for s in S), ctx.from_dict({})) for l in range(4)] for k in range(4)]
M = [[5 * Phi * ((2 * m[k] if k == l else 0) - S2[k][l]) + 3 * m[k] * m[l] for l in range(4)] for k in range(4)]
# sanity: M 1 = 0
for k in range(4):
    assert sum(M[k], ctx.from_dict({})) == 0

def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
            - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))

def stats(p):
    coeffs = [int(c) for c in p.coeffs()]
    neg = [c for c in coeffs if c < 0]
    return {'terms': len(coeffs), 'neg_terms': len(neg), 'min_coeff': min(coeffs), 'max_coeff': max(coeffs)}

out = {}
t0 = time.time()
for drop in range(4):
    keep = [k for k in range(4) if k != drop]
    A = [[M[i][j] for j in keep] for i in keep]
    P1 = A[0][0]
    P2 = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    P3 = det3(A)
    out[drop] = {'P1': stats(P1), 'P2': stats(P2), 'P3': stats(P3)}
    print(drop, out[drop], f'{time.time()-t0:.1f}s', flush=True)
    if drop == 3:
        with open(f'evidence/slice_P3_drop3_{"rainbow" if rainbow else "plain"}.txt', 'w') as f:
            f.write(str(P3))
print(json.dumps(out))
