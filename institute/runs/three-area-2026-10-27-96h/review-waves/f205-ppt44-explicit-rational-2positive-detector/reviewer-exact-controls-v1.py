#!/usr/bin/env python3
"""Independent, finite rational controls for the frozen 4x5 detector review.

Constructs the matrices from the vector definitions, not from any author code.
The exact Schur congruences certify PSD for these finite matrices; the universal
rank-two and filter statements also require the written arguments in the review.
"""
from fractions import Fraction as F
from itertools import permutations
import json

n = 20
basis = [
    {(0, 0): 1, (1, 1): 1, (2, 2): 1},
    {(0, 1): 1, (1, 2): 1},
    {(1, 0): 1, (2, 1): -1},
    {(0, 2): 1, (3, 4): 1},
    {(2, 0): 1, (3, 3): 1},
    {(2, 3): 1},
    {(3, 0): 1},
    {(3, 2): 1},
    {(0, 4): 1},
]
weights = [1, 1, 1, 3, 3, 3, 3, 3, 3]
vecs = [[F(b.get((x // 5, x % 5), 0)) for x in range(n)] for b in basis]
norms = [sum(x*x for x in v) for v in vecs]
for i, v in enumerate(vecs):
    for j, w in enumerate(vecs):
        assert sum(x*y for x, y in zip(v, w)) == (norms[i] if i == j else 0)

def zeros(k):
    return [[F(0) for _ in range(k)] for _ in range(k)]

def outer(v):
    return [[v[i]*v[j] for j in range(len(v))] for i in range(len(v))]

def quadratic(m, v):
    return sum(v[i]*m[i][j]*v[j] for i in range(len(v)) for j in range(len(v)))

def trprod(m, z):
    return sum(m[i][j]*z[j][i] for i in range(len(m)) for j in range(len(m)))

def components(m):
    seen = set()
    parts = []
    for start in range(len(m)):
        if start in seen:
            continue
        seen.add(start)
        queue = [start]
        for i in queue:
            for j in range(len(m)):
                if j != i and m[i][j] and j not in seen:
                    seen.add(j)
                    queue.append(j)
        parts.append(sorted(queue))
    return parts

def schur_certificate(m):
    """Symmetric elimination, including exact zero-pivot row checks."""
    assert all(m[i][j] == m[j][i] for i in range(len(m)) for j in range(len(m)))
    records = []
    total_rank = 0
    for ids in components(m):
        a = [[F(m[i][j]) for j in ids] for i in ids]
        pivots = []
        nulls = []
        for k, ix in enumerate(ids):
            d = a[k][k]
            if d < 0:
                raise AssertionError(('negative pivot', ix, str(d)))
            if d == 0:
                if any(a[k][j] != 0 for j in range(k + 1, len(ids))):
                    raise AssertionError(('zero pivot nonzero row', ix))
                nulls.append(ix)
                continue
            pivots.append(str(d))
            total_rank += 1
            for i in range(k + 1, len(ids)):
                for j in range(k + 1, len(ids)):
                    a[i][j] -= a[i][k]*a[k][j]/d
        records.append({'indices': ids, 'pivots': pivots, 'zero_pivots': nulls})
    return {'rank': total_rank, 'blocks': records}

R = zeros(n)
PR = zeros(n)
for v, w, norm in zip(vecs, weights, norms):
    o = outer(v)
    for i in range(n):
        for j in range(n):
            R[i][j] += w*o[i][j]
            PR[i][j] += o[i][j]/norm
PK = [[F(i == j) - PR[i][j] for j in range(n)] for i in range(n)]
AA = outer(vecs[0])
PK0 = [[PR[i][j] - AA[i][j]/3 for j in range(n)] for i in range(n)]
Rgamma = zeros(n)
for i in range(4):
    for b in range(5):
        for j in range(4):
            for d in range(5):
                Rgamma[5*i+d][5*j+b] = R[5*i+b][5*j+d]
rcert = schur_certificate(R)
ptcert = schur_certificate(Rgamma)
assert rcert['rank'] == 9 and ptcert['rank'] == 10
assert sum(R[i][i] for i in range(n)) == 31
W = [[18*10**11*PK[i][j] + 18*PK0[i][j] - 58*AA[i][j]
      for j in range(n)] for i in range(n)]
assert all(x.denominator == 1 for row in W for x in row)
pairings = [trprod(PK, R), trprod(PK0, R), trprod(AA, R), trprod(W, R)]
assert pairings == [0, 28, 9, -18]
assert quadratic(W, vecs[0]) == -522

# Polynomial dictionaries use exponent vectors for a,b,c,d,e,f,g,h,i.
names = 'abcdefghi'
zeroexp = (0,)*9

def const(k):
    return {} if not k else {zeroexp: F(k)}

def variable(k):
    t = [0]*9
    t[k] = 1
    return {tuple(t): F(1)}

def add(*ps):
    ans = {}
    for p in ps:
        for mon, val in p.items():
            ans[mon] = ans.get(mon, F(0)) + val
    return {m: v for m, v in ans.items() if v}

def scale(p, c):
    return {m: v*c for m, v in p.items() if v*c}

def mul(p, q):
    result = {}
    for m, v in p.items():
        for k, w in q.items():
            e = tuple(x+y for x, y in zip(m, k))
            result[e] = result.get(e, F(0)) + v*w
    return {m: v for m, v in result.items() if v}

def show(p):
    terms = []
    for exps, coeff in sorted(p.items(), reverse=True):
        mon = ''.join(name + (str(e) if e > 1 else '') for name, e in zip(names, exps) if e) or '1'
        terms.append(str(coeff) + '*' + mon)
    return terms

a, b, c, d, e, f, g, h, iv = [variable(k) for k in range(9)]
y = [[a,b,c,const(0),h], [d,a,b,const(0),const(0)],
     [e,scale(d,-1),a,f,const(0)], [g,const(0),iv,e,c]]

def minor(rows, cols):
    acc = {}
    for p in permutations(range(3)):
        inversions = sum(p[i] > p[j] for i in range(3) for j in range(i+1,3))
        term = const(-1 if inversions % 2 else 1)
        for k in range(3):
            term = mul(term, y[rows[k]][cols[p[k]]])
        acc = add(acc, term)
    return acc

ms = [minor((0,1,2),(0,1,2)), minor((0,1,3),(1,2,3)),
      minor((1,2,3),(0,1,4)), minor((0,1,3),(0,1,3)),
      minor((1,2,3),(1,2,4))]
rhs = add(mul(a,ms[0]), scale(mul(a,ms[1]),-1), scale(mul(a,ms[2]),-1),
          scale(mul(c,ms[3]),F(-1,2)), scale(mul(e,ms[4]),F(-1,2)))
a4 = mul(mul(a,a),mul(a,a))
assert add(rhs,scale(a4,-1)) == {}
# The last sign flipped is not the same polynomial; intended identity failure.
wrong_rhs = add(rhs, mul(e,ms[4]))
wrong_residual = add(wrong_rhs,scale(a4,-1))
assert wrong_residual

alpha = F(1,10**11)
margin = alpha/33
case2_slack = F(1,2)-29*alpha-margin
case3_slack = F(1,144*66**4)-29*alpha-margin
assert case2_slack >= 0 and case3_slack >= 0
assert 18*10**11*margin == F(6,11)

# Build the 25x25 pullback of PK directly from coefficient lists and R's weights.
L6 = zeros(25)
for src, weight in zip(basis, weights):
    byq = {q: [(i, F(value)) for (i, bq), value in src.items() if bq == q]
           for q in range(5)}
    for p in range(5):
        for q in range(5):
            for r in range(5):
                for s in range(5):
                    value = sum(x*y*PK[5*i+p][5*j+r]
                                for i, x in byq[q] for j, y in byq[s])
                    L6[5*p+q][5*r+s] += 6*weight*value
assert all(x.denominator == 1 for row in L6 for x in row)
u = [F(p == q) for p in range(5) for q in range(5)]
assert all(sum(L6[k][j]*u[j] for j in range(25)) == 0 for k in range(25))
Hmat = [[5*L6[i][j] - 15*F(i == j) + 3*u[i]*u[j]
         for j in range(25)] for i in range(25)]
hcert = schur_certificate(Hmat)
assert hcert['rank'] == 24

# Negative controls: alter one source weight, one detector coefficient, or an
# indispensable hypothesis. Each uses a concrete algebraic counterexample.
Rbad = [[R[i][j] - 6*vecs[3][i]*vecs[3][j] for j in range(n)] for i in range(n)]
negative_source = quadratic(Rbad,vecs[3])
assert negative_source == -12
wrong_pair = 18*28-56*9
assert wrong_pair == 0
assert sum(u) == 5 and quadratic(L6,u) == 0  # T=I has rank 5, so no rank-4 lower bound.
overstrong = next((p,q,L6[5*p+q][5*p+q]) for p in range(5) for q in range(5)
                  if p != q and L6[5*p+q][5*p+q] < 60)
# For the unit off-diagonal matrix, 6 Q_K = the diagonal entry: <60 disproves gap 10.

# Concrete rank-two probe and explicit rank-three warning.
probe = [x+y for x,y in zip(vecs[0],[-v for v in vecs[0]])]  # reset to zero
probe[0] = probe[6] = 1  # |00>+|11>, rank two
probe_norm = sum(x*x for x in probe)
probe_q = quadratic(W,probe)
assert probe_q >= F(6,11)*probe_norm

print(json.dumps({
    'source_orthogonal_squared_norms': [str(x) for x in norms],
    'source_eigenvalues': [str(x*y) for x,y in zip(norms,weights)],
    'source_trace': str(sum(R[i][i] for i in range(n))),
    'R_schur_certificate': rcert,
    'R_gamma_schur_certificate': ptcert,
    'integer_W': True,
    'PK_PK0_A_W_pairings': [str(v) for v in pairings],
    'minor_polynomials': [show(p) for p in ms],
    'minor_identity_residual': show(add(rhs,scale(a4,-1))),
    'wrong_minor_sign_residual': show(wrong_residual),
    'case2_slack': str(case2_slack), 'case3_slack': str(case3_slack),
    'scaled_margin': str(18*10**11*margin),
    'L6_integer_and_scalar_identity_null': True,
    'H_schur_certificate': hcert,
    'rank2_probe_norm_and_W': [str(probe_norm),str(probe_q)],
    'rank3_A_W_expectation': str(quadratic(W,vecs[0])),
    'negative_bad_C_weight_expectation': str(negative_source),
    'negative_wrong_A_coefficient_pairing': str(wrong_pair),
    'negative_rank5_identity_L6_quadratic': str(quadratic(L6,u)),
    'negative_overstrong_gap_matrix_p_q_L6': [overstrong[0],overstrong[1],str(overstrong[2])]
}, indent=2))
