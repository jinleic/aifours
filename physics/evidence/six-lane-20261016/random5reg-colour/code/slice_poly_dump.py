"""Dump the raw coefficient certificates of the slice-concavity lemma (all dropped indices).

Writes evidence/slice_minors_rainbow.json: for drop in 0..3 and minor in P1,P2,P3 the full list of
(exponent vector over (mu_{-1,-1}, mu_{-1,1}, mu_{1,-1}, mu_{1,1}), integer coefficient).
Matrix: Mpoly = 5 Phi (2 diag(m) - S2) + 3 m m^T with d_s = w_s mu^s, Phi = sum d_s, m = sum d_s s,
S2 = sum d_s s s^T (homogeneous degree 10).  Claim: every coefficient of every minor is > 0, hence
each minor is > 0 on the open orthant mu in (0,inf)^4 (which parametrises the open cone of m).
"""
import json, itertools, hashlib, sys
import flint
sys.path.insert(0, 'code')
from model import spectra, multinomial
S = spectra(5, True)
ctx = flint.fmpz_mpoly_ctx.get(('x', 'y', 'z', 'w'), 'degrevlex')
zero = ctx.from_dict({})
mono = lambda s: ctx.from_dict({tuple(s): 1})
Phi = sum((multinomial(s) * mono(s) for s in S), zero)
m = [sum((multinomial(s) * s[k] * mono(s) for s in S), zero) for k in range(4)]
S2 = [[sum((multinomial(s) * s[k] * s[l] * mono(s) for s in S), zero) for l in range(4)] for k in range(4)]
M = [[5 * Phi * ((2 * m[k] if k == l else 0) - S2[k][l]) + 3 * m[k] * m[l] for l in range(4)] for k in range(4)]
for k in range(4):
    assert sum(M[k], zero) == 0
out = {'variables': ['mu_{-1,-1}', 'mu_{-1,1}', 'mu_{1,-1}', 'mu_{1,1}'], 'matrix': '5 Phi (2 diag m - S2) + 3 m m^T', 'minors': {}}
allpos = True
for drop in range(4):
    keep = [k for k in range(4) if k != drop]
    A = [[M[i][j] for j in keep] for i in keep]
    P1 = A[0][0]
    P2 = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    P3 = (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
          + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
    for name, P in (('P1', P1), ('P2', P2), ('P3', P3)):
        terms = sorted(([list(map(int, e)), int(c)] for e, c in zip(P.monoms(), P.coeffs())))
        allpos &= all(c > 0 for _, c in terms)
        out['minors'][f'drop{drop}_{name}'] = {'n_terms': len(terms), 'all_coefficients_positive': all(c > 0 for _, c in terms), 'terms': terms}
out['all_minors_all_coefficients_positive'] = bool(allpos)
s = json.dumps(out, sort_keys=True)
open('evidence/slice_minors_rainbow.json', 'w').write(s)
print('all positive:', allpos, ' sha256', hashlib.sha256(s.encode()).hexdigest(), ' bytes', len(s))
