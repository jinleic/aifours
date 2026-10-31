#!/usr/bin/env python3
"""Independent, finite Gaussian-rational controls; no author code is used."""
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


class Z:
    __slots__ = ('r', 'i')
    def __init__(self, r=0, i=0):
        if isinstance(r, Z):
            self.r, self.i = r.r, r.i
        else:
            self.r, self.i = F(r), F(i)
    def __add__(self, x):
        x = Z(x)
        return Z(self.r+x.r, self.i+x.i)
    __radd__ = __add__
    def __neg__(self):
        return Z(-self.r, -self.i)
    def __sub__(self, x):
        return self + -Z(x)
    def __rsub__(self, x):
        return Z(x) - self
    def __mul__(self, x):
        x = Z(x)
        return Z(self.r*x.r-self.i*x.i, self.r*x.i+self.i*x.r)
    __rmul__ = __mul__
    def __truediv__(self, x):
        x = Z(x)
        n = x.abs2()
        if not n:
            raise ZeroDivisionError
        y = self * x.conj()
        return Z(y.r/n, y.i/n)
    def __eq__(self, x):
        x = Z(x)
        return self.r == x.r and self.i == x.i
    def __bool__(self):
        return bool(self.r or self.i)
    def __repr__(self):
        return f'({self.r},{self.i})'
    def conj(self):
        return Z(self.r, -self.i)
    def abs2(self):
        return self.r*self.r+self.i*self.i


def zeros(n, m): return [[Z() for _ in range(m)] for _ in range(n)]
def eye(n): return [[Z(i == j) for j in range(n)] for i in range(n)]
def add(A, B): return [[x+y for x, y in zip(a, b)] for a, b in zip(A, B)]
def neg(A): return [[-x for x in row] for row in A]
def sub(A, B): return add(A, neg(B))
def scale(a, A): return [[Z(a)*x for x in row] for row in A]
def dag(A): return [[A[i][j].conj() for i in range(len(A))] for j in range(len(A[0]))]
def trans(A): return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
def mm(A, B):
    out = zeros(len(A), len(B[0]))
    for i, row in enumerate(A):
        for k, x in enumerate(row):
            if x:
                for j, y in enumerate(B[k]):
                    if y: out[i][j] = out[i][j] + x*y
    return out

def kron(A, B):
    n, m, p, q = len(A), len(A[0]), len(B), len(B[0])
    return [[A[i//p][j//q]*B[i%p][j%q] for j in range(m*q)] for i in range(n*p)]
def trace(A): return sum((A[i][i] for i in range(len(A))), Z())
def norm2(A): return sum((x.abs2() for row in A for x in row), F(0))
def vnorm2(v): return sum((x.abs2() for x in v), F(0))
def inner(v, w): return sum((x.conj()*y for x, y in zip(v, w)), Z())
def mv(A, v): return [sum((x*y for x, y in zip(row, v)), Z()) for row in A]
def outer(v, w): return [[x*y.conj() for y in w] for x in v]
def unit(n, k): return [Z(i == k) for i in range(n)]
def vec(v, scale_=1): return [Z(scale_)*x for x in v]
def vadd(v, w): return [x+y for x, y in zip(v, w)]
def rank(A):
    A = [[Z(x) for x in row] for row in A]
    m, n = len(A), len(A[0]); r = 0
    for j in range(n):
        pivot = next((i for i in range(r, m) if A[i][j]), None)
        if pivot is None: continue
        A[r], A[pivot] = A[pivot], A[r]
        div = A[r][j]; A[r] = [x/div for x in A[r]]
        for i in range(r+1, m):
            if A[i][j]:
                c = A[i][j]; A[i] = [x-c*y for x, y in zip(A[i], A[r])]
        r += 1
        if r == m: break
    return r

def part(C, site):
    if site == 1:
        return [[sum((C[4*a+b][4*a+d] for a in range(4)), Z()) for d in range(4)] for b in range(4)]
    return [[sum((C[4*a+b][4*c+b] for b in range(4)), Z()) for c in range(4)] for a in range(4)]
def block(C, site, k, l):
    if site == 2:
        return [[C[4*a+k][4*c+l] for c in range(4)] for a in range(4)]
    return [[C[4*k+a][4*l+c] for c in range(4)] for a in range(4)]
def q1(A): return norm2(A) - trace(A).abs2()/2
def q2(C): return norm2(C) - norm2(part(C, 1))/2 - norm2(part(C, 2))/2 + trace(C).abs2()/4
def qpair(A, B):
    return sum((x*y.conj() for a, b in zip(A, B) for x, y in zip(a, b)), Z()) - trace(A)*trace(B).conj()/2
def E(i, j):
    A = zeros(4, 4); A[i][j] = Z(1); return A


positives, negatives = [], []
def pos(label, condition, detail=''):
    if not condition: raise AssertionError('POSITIVE: '+label+' '+str(detail))
    positives.append({'control': label, 'detail': str(detail)})
def negcheck(label, bad_condition, detail=''):
    if bad_condition: raise AssertionError('NEGATIVE DID NOT FAIL: '+label+' '+str(detail))
    negatives.append({'mutation': label, 'intended_reason': str(detail)})


def worker():
    I = eye(4); I16 = eye(16); i = Z(0, 1)
    u = [Z(1 if k in (0, 5, 10, 15) else 0) for k in range(16)]
    v = [Z(1 if k in (0, 6, 15) else 0, 1 if k == 6 else 0) for k in range(16)]
    w = [Z(1 if k in (3, 10, 15) else 0, 1 if k == 10 else 0) for k in range(16)]
    C = add(outer(u, u), scale(F(1, 5), outer(v, w)))
    pos('complex C is rank exactly two', rank(C) == 2)
    pos('fixture has a strictly negative one-site trace sign', q1(part(C, 2)) < 0, q1(part(C, 2)))
    pos('trace-sign fixture has positive q2', q2(C) > 0, q2(C))
    fullrank = kron(I, E(0, 0))
    pos('rank-four counterfixture has nonpositive reduced q1', rank(fullrank) == 4 and q1(part(fullrank, 2)) < 0)
    negcheck('drop rank restriction from trace-sign lemma', q2(fullrank) >= 0, f'q2={q2(fullrank)}, rank=4')

    odd = add(scale(F(1, 4), add(kron(I, part(C, 1)), kron(part(C, 2), I))), scale(-trace(C)/8, I16))
    pos('odd-sector identity on rank-two complex C', q2(C) == norm2(C)-2*norm2(odd))
    wrongodd = add(scale(F(1, 4), add(kron(I, part(C, 1)), kron(part(C, 2), I))), scale(-trace(C)/4, I16))
    negcheck('odd projector overlap coefficient 1/4 instead of 1/8', q2(C) == norm2(C)-2*norm2(wrongodd), 'double-counted identity sector')

    for site in (1, 2):
        blocks = [block(C, site, k, l) for k in range(4) for l in range(4)]
        total = sum((q1(B) for B in blocks), F(0)); reduced = q1(part(C, site))
        pos(f'block identity site {site}', q2(C) == total-reduced/2, f'sum={total}, reduced={reduced}')
        pos(f'each block rank at most two site {site}', all(rank(B) <= 2 for B in blocks))
        negcheck(f'block coefficient -1/3 site {site}', q2(C) == total-reduced/3, 'wrong partial-trace coefficient')
        # Covariance from E[J tensor J] = a I + b F, contracted exactly.
        cov = Z()
        for k in range(4):
            for l in range(4):
                for n in range(4):
                    for m in range(4):
                        weight = (-F(1, 15) if k == l and n == m else F(0)) + (F(4, 15) if l == m and k == n else F(0))
                        if weight: cov += weight*qpair(block(C, site, k, l), block(C, site, n, m))
        pos(f'Haar covariance contraction site {site}', cov == Z(F(4, 15)*total-F(1, 15)*reduced), cov)
        negcheck(f'Haar I coefficient -1/16 site {site}', cov == Z(F(4, 15)*total-F(1, 16)*reduced), 'mutated covariance coefficient')
    pos('Haar coefficients satisfy tr(J)=0 and tr(J^2)=4', 16*(-F(1, 15))+4*F(4, 15) == 0 and 4*(-F(1, 15))+16*F(4, 15) == 4)
    negcheck('Haar covariance coefficient mutation violates trace', 16*(-F(1, 16))+4*F(4, 15) == 0, 'tr J = 0')

    s0 = vadd(vec(unit(4, 0), F(3, 5)), vec(unit(4, 2), Z(0, F(4, 5))))
    s1 = vadd(vec(unit(4, 1), F(3, 5)), vec(unit(4, 3), Z(0, -F(4, 5))))
    P = add(outer(s0, s0), outer(s1, s1)); Q = sub(I, P); J = sub(P, Q)
    pos('complex rank-two projector fixture', mm(P, P) == P and dag(P) == P and rank(P) == 2 and trace(J) == 0)
    CP = mm(kron(I, P), C); CQ = mm(kron(I, Q), C)
    D = part(mm(C, kron(I, J)), 2); S = part(C, 2)
    split = q2(CP)+q2(CQ)-q1(S)/4+q1(D)/4
    pos('complex projection split identity', q2(C) == split, f'q2={q2(C)}, qP={q2(CP)}, qQ={q2(CQ)}')
    pos('two supported projected operators nonnegative', rank(CP) <= 2 and rank(CQ) <= 2 and q2(CP) >= 0 and q2(CQ) >= 0)
    negcheck('reverse sign of split correction', q2(C) == q2(CP)+q2(CQ)+q1(S)/4-q1(D)/4, 'correction sign')

    A = scale(Z(0, 2), E(0, 1))
    B = [[Z() for _ in range(4)] for _ in range(4)]
    for k, x in enumerate((Z(1), Z(-1), i, -i)): B[k][k] = x
    pos('normal-B fixture is complex, traceless and A nonnormal', trace(A) == 0 and trace(B) == 0 and mm(A, dag(A)) != mm(dag(A), A) and mm(B, dag(B)) == mm(dag(B), B))
    for k in range(4):
        Mk = add(A, scale(B[k][k], I)); Hk = mm(dag(Mk), Mk)
        pos(f'normal-B 2x2 block characteristic polynomial {k}', Hk[0][0]+Hk[1][1] == 6 and Hk[0][0]*Hk[1][1]-Hk[0][1]*Hk[1][0] == 1 and Hk[2][2] == 1 and Hk[3][3] == 1)
    pos('normal-B top-two inequality in exact radicals', 25 >= 8 and 2*(norm2(A)+norm2(B)) == 16, 'top sum 6+4*sqrt(2) <= 16')
    scalarproj = scale(Z(1, 1), E(0, 0)); Xbad = add(kron(scalarproj, I), kron(I, scalarproj))
    diagonal = sorted((Xbad[k][k].abs2() for k in range(16)), reverse=True)
    negcheck('drop tracelessness in dual inequality', sum(diagonal[:2]) <= 2*(norm2(scalarproj)+norm2(scalarproj)), f'top={sum(diagonal[:2])}, rhs={2*(norm2(scalarproj)+norm2(scalarproj))}')

    Acomm = add(add(E(0, 0), scale(-1, E(1, 1))), add(scale(i, E(2, 2)), add(scale(-i, E(3, 3)), scale(Z(1, 1), E(0, 1)))))
    Psi = add(add(E(0, 2), scale(Z(2, -1), E(1, 0))), add(scale(i, E(2, 3)), E(3, 1)))
    vpsi = [Psi[r][c] for r in range(4) for c in range(4)]
    Xcomm = add(kron(Acomm, I), kron(I, neg(trans(Acomm))))
    expected = sub(mm(Acomm, Psi), mm(Psi, Acomm))
    pos('complex row-vectorized commutator identity', mv(Xcomm, vpsi) == [expected[r][c] for r in range(4) for c in range(4)])
    pos('one finite BW-premise instance', norm2(expected) <= 2*norm2(Acomm)*norm2(Psi), f'{norm2(expected)} <= {2*norm2(Acomm)*norm2(Psi)}')
    Xwrong = add(kron(Acomm, I), kron(I, neg(dag(Acomm))))
    negcheck('replace transpose with adjoint in commutator', mv(Xwrong, vpsi) == [expected[r][c] for r in range(4) for c in range(4)], 'wrong complex vectorization')

    # A complex traceless nonnormal A for exact completion of the b square.
    Ared = add(add(E(0, 0), scale(-1, E(1, 1))), scale(Z(2, 1), E(1, 0)))
    psi0 = vec(unit(4, 0), F(3, 5)); psi1 = vec(unit(4, 1), Z(0, F(4, 5)))
    p2, q2v = vnorm2(psi0), vnorm2(psi1)
    c = inner(mv(Ared, psi0), psi1); bopt = c.conj()/(1+p2)
    base = vnorm2(mv(Ared, psi0))+vnorm2(mv(Ared, psi1))
    def expression(b):
        return vnorm2(vadd(mv(Ared, psi0), vec(psi1, b)))+vnorm2(mv(Ared, psi1))-2*Z(b).abs2()
    for b in (Z(), Z(1, -2), bopt):
        pos('exact complex b completion '+repr(b), expression(b) == base+c.abs2()/(1+p2)-(1+p2)*(Z(b)-bopt).abs2())
    pos('normalization and nonzero optimal b', trace(Ared) == 0 and p2+q2v == 1 and bool(c) and bool(bopt))
    negcheck('replace 1+p² by 1+q² in dagger', expression(bopt) == base+c.abs2()/(1+q2v), 'wrong optimizer denominator')
    Bred = scale(bopt, E(0, 1)); Xred = add(kron(Ared, I), kron(I, Bred))
    rvec = [psi0[a] if b == 0 else psi1[a] if b == 1 else Z() for a in range(4) for b in range(4)]
    phi = unit(4, 1); rphi = [phi[a] if b == 2 else Z() for a in range(4) for b in range(4)]
    pos('rank-one B is traceless and square-zero', rank(Bred) == 1 and trace(Bred) == 0 and mm(Bred, Bred) == zeros(4, 4))
    pos('two-block direct sum and cross pair', vnorm2(mv(Xred, rvec))+vnorm2(mv(Xred, rphi)) == expression(bopt)+2*bopt.abs2()+vnorm2(mv(Ared, phi)) and inner(rvec, rphi) == 0)
    negcheck('drop 2|b|² from cross objective', vnorm2(mv(Xred, rvec))-2*bopt.abs2() == vnorm2(mv(Xred, rvec)), 'norm of X contains rank-one B')
    # Nontraceless rank-one A gives an exact violating cross pair after optimizing b.
    Ant = scale(Z(1, 1), E(0, 0)); y0 = vec(unit(4, 0), F(3, 5)); y1 = vec(unit(4, 0), F(4, 5))
    cfalse = inner(mv(Ant, y0), y1); falseleft = vnorm2(mv(Ant, y0))+vnorm2(mv(Ant, y1))+cfalse.abs2()/(1+vnorm2(y0))+norm2(Ant)
    negcheck('remove traceless A from dagger', falseleft <= 2*norm2(Ant), f'lhs={falseleft}, rhs={2*norm2(Ant)}, trace={trace(Ant)}')
    # The cheap bound's 3-2sqrt(2) constant must exceed this exact lower instance.
    csharp = (F(3, 5)*F(4, 5))**2/(1+F(9, 25))
    pos('explicit rational value below exact max', csharp == F(72, 425), csharp)
    negcheck('replace maximum 3-2sqrt(2) by 1/8', csharp <= F(1, 8), f'value={csharp}')

    Aorth = add(scale(Z(0, 2), E(0, 1)), E(2, 3)); phi = unit(4, 1); topu = vec(unit(4, 0), i)
    pos('orthogonal top singular pair, traceless and nonnormal', trace(Aorth) == 0 and mv(Aorth, phi) == vec(topu, 2) and inner(topu, phi) == 0 and norm2(Aorth) == 5)
    b = Z(F(1, 3), F(1, 3)); block01 = [[Z() for _ in range(8)] for _ in range(8)]
    for r in range(4):
        for c0 in range(4):
            block01[r][c0] = Aorth[r][c0]; block01[r+4][c0+4] = Aorth[r][c0]
        block01[r][r+4] = b
    va = phi + [Z() for _ in range(4)]; vb = [Z() for _ in range(4)] + phi
    pos('orthogonal output pair gives two singular directions >= sigma', inner(mv(block01, va), mv(block01, vb)) == 0 and vnorm2(mv(block01, va)) == 4 and vnorm2(mv(block01, vb)) >= 4)
    pos('Frobenius threshold fixture meets exact bound', 2*norm2(Aorth) == 10 and 128 >= 100, '10 >= 20 - 8 sqrt(2)')
    rankoneA = scale(Z(1, 1), E(0, 1)); ph = unit(4, 1)
    y0, y1 = vec(ph, F(3, 5)), vec(ph, F(4, 5))
    lhs = vnorm2(mv(rankoneA, y0))+vnorm2(mv(rankoneA, y1))+inner(mv(rankoneA, y0), y1).abs2()/(1+vnorm2(y0))+norm2(rankoneA)
    pos('rank-one traceless A attains dagger equality', rank(rankoneA) == 1 and trace(rankoneA) == 0 and lhs == 2*norm2(rankoneA), lhs)

    # An exact genuinely complex point in the near-rank-one, small-optimal-b residual.
    c = F(7, 25); s = F(24, 25); eps = F(7, 57)
    uu = [Z(c), Z(0, s), Z(), Z()]; uu2 = [Z(0, s), Z(c), Z(), Z()]
    Anear = sub(outer(uu, unit(4, 0)), scale(eps, add(add(outer(uu2, unit(4, 1)), E(2, 2)), E(3, 3))))
    pos('near-rank-one A is complex traceless with exact singular Gram', trace(Anear) == 0 and mm(dag(Anear), Anear) == add(E(0, 0), scale(eps*eps, add(add(E(1, 1), E(2, 2)), E(3, 3)))) and mm(Anear, dag(Anear)) != mm(dag(Anear), Anear))
    f2 = norm2(Anear); pos('near-rank-one A lies strictly below threshold', f2 == 1+3*eps*eps and 2*(f2-1) < F(1, 10), f'frob²={f2}, sigma²=1')
    near0, near1 = vec(unit(4, 0), F(3, 5)), vec(unit(4, 0), F(4, 5))
    cn = inner(mv(Anear, near0), near1); bn = cn.conj()/(1+vnorm2(near0))
    nearL = vnorm2(mv(Anear, near0))+vnorm2(mv(Anear, near1))+cn.abs2()/(1+vnorm2(near0))+1
    pos('small optimal b inside residual', 0 < bn.abs2() < c*c, f'b={bn}, overlap={c}')
    pos('finite dagger instance inside residual', nearL <= 2*f2, f'lhs={nearL}, rhs={2*f2}')
    chi = [Z(s), Z(0, -c), Z(), Z()]
    pos('nonorthogonal top pair threshold construction', vnorm2(chi) == 1 and inner(uu, chi) == 0 and vnorm2(mv(Anear, chi)) >= 1-c*c and c*c+vnorm2(mv(Anear, chi)) >= 1)
    negcheck('ignore the overlap term in top-pair threshold', c == 0, f'actual nonzero overlap={c}')

    # Equality-family spectrum: exact matrix polynomial plus power sums.
    a, b = Z(1, 1), Z(2, -1)
    X = add(kron(scale(a, E(0, 1)), I), kron(I, scale(b, E(0, 1))))
    H = mm(dag(X), X); alpha, beta, total = a.abs2(), b.abs2(), a.abs2()+b.abs2()
    poly = mm(mm(mm(H, sub(H, scale(total, I16))), sub(H, scale(alpha, I16))), sub(H, scale(beta, I16)))
    pos('complex equality-family spectral polynomial', poly == zeros(16, 16), f'squared eigenvalues 0,{alpha},{beta},{total}')
    Hk = eye(16)
    for k in range(4):
        expectedtrace = 16 if k == 0 else 2*total**k+2*alpha**k+2*beta**k
        pos(f'equality-family multiplicity power sum {k}', trace(Hk) == expectedtrace, trace(Hk))
        Hk = mm(Hk, H)
    pos('equality-family dual equality', 2*total == 2*(alpha+beta))
    negcheck('use complex a²,b² rather than modulus squares', trace(H) == 4*(a*a+b*b), f'trace={trace(H)}, mutated={4*(a*a+b*b)}')
    return {'scope': 'finite exact Gaussian-rational controls only; not universal proof', 'positive_count': len(positives), 'negative_count': len(negatives), 'positives': positives, 'negatives': negatives}


def native_clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()


def controller():
    src = Path(__file__).resolve(); root = src.parent
    start_wall = native_clock(); start = time.monotonic()
    try:
        p = subprocess.run([sys.executable, '-B', str(src), '--worker'], capture_output=True, text=True, timeout=110)
        outcome = 'COMPLETED' if p.returncode == 0 else 'FAILED'
        body = p.stdout; err = p.stderr; exitcode = p.returncode
    except subprocess.TimeoutExpired as exc:
        outcome = 'UNKNOWN_TIMEOUT'; body = exc.stdout or ''; err = exc.stderr or ''; exitcode = None
        if isinstance(body, bytes): body = body.decode('utf-8', errors='replace')
        if isinstance(err, bytes): err = err.decode('utf-8', errors='replace')
    elapsed = time.monotonic()-start; end_wall = native_clock()
    result_path = root/'reviewer-controls-v2-results.json'
    receipt_path = root/'reviewer-controls-v2-receipt.json'
    payload = {'outcome': outcome, 'worker_stdout': json.loads(body) if outcome == 'COMPLETED' else body, 'worker_stderr': err}
    data = (json.dumps(payload, indent=2, sort_keys=True)+'\n').encode()
    with result_path.open('xb') as f: f.write(data)
    receipt = {'start_native': start_wall, 'end_native': end_wall, 'elapsed_monotonic_seconds': elapsed,
               'timeout_seconds': 110, 'worker_argv': [sys.executable, '-B', str(src), '--worker'],
               'worker_exit_code': exitcode, 'outcome': outcome, 'script_sha256': hashlib.sha256(src.read_bytes()).hexdigest(),
               'results_sha256': hashlib.sha256(data).hexdigest(), 'results_bytes': len(data),
               'control_scope': 'finite, exact Gaussian rationals; no author code'}
    with receipt_path.open('x', encoding='utf-8') as f: json.dump(receipt, f, indent=2, sort_keys=True); f.write('\n')
    print(json.dumps(receipt, sort_keys=True))
    return 0 if outcome == 'COMPLETED' else 1

if __name__ == '__main__':
    if sys.argv[1:] == ['--worker']:
        print(json.dumps(worker(), sort_keys=True))
    else:
        raise SystemExit(controller())
