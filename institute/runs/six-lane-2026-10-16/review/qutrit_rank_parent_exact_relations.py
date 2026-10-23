"""Parent symbolic re-derivation of the rank-proof's normal-form relations, with no worker imports.
Sparse polynomials over Q in independent formal entries z_abcd and their conjugates w_abcd;
all arithmetic exact. Every displayed relation must equal an entry (or sign/conjugate) of one of
UU*, U*U, R(U)R(U)*, R(U)*R(U) minus identity. Also verifies an explicit attaining gate over Q(sqrt3).
Usage: python3 -B qutrit_rank_parent_exact_relations.py NEW_RECEIPT.json
This checks algebraic identities, not the remaining mathematical case arguments or imported Fact K.
"""
from collections import Counter
from datetime import datetime
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path
import sys
from zoneinfo import ZoneInfo


def const(n):
    return {(): Fraction(n)} if n else {}


def add(*ps):
    q = {}
    for p in ps:
        for m, c in p.items():
            q[m] = q.get(m, 0) + c
            if not q[m]:
                del q[m]
    return q


def scale(p, c):
    return {m: a * c for m, a in p.items() if a * c}


def mul(a, b):
    q = {}
    for m, x in a.items():
        for n, y in b.items():
            terms = m + n
            r = terms.count('sqrt3')
            key = tuple(sorted(t for t in terms if t != 'sqrt3')) + ('sqrt3',) * (r % 2)
            key = tuple(sorted(key))
            c = x * y * 3 ** (r // 2)
            q[key] = q.get(key, 0) + c
    return {m: c for m, c in q.items() if c}


def conjugate(p):
    def bar(t):
        return ('w' + t[1:]) if t.startswith('z') else ('z' + t[1:]) if t.startswith('w') else t
    return {tuple(sorted(bar(t) for t in m)): c for m, c in p.items()}


def key(p):
    return tuple(sorted((m, c) for m, c in p.items()))


def dagger(A):
    return [[conjugate(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]


def transpose(A):
    return [list(c) for c in zip(*A)]


def mm(A, B):
    return [[add(*(mul(A[i][k], B[k][j]) for k in range(len(B)))) for j in range(len(B[0]))] for i in range(len(A))]


def ma(*As):
    return [[add(*(A[i][j] for A in As)) for j in range(len(As[0][0]))] for i in range(len(As[0]))]


def eye(n, value=1):
    return [[const(value if i == j else 0) for j in range(n)] for i in range(n)]


def residual(A, left):
    return ma(mm(A, dagger(A)) if left else mm(dagger(A), A), eye(len(A), -1))


def phi(a, b, c, d):
    if a == b == c == d == 0:
        return const(1)
    if (a == b == 0) or (c == d == 0) or (a == c == 0) or (b == d == 0):
        return {}
    return {(f'z{a}{b}{c}{d}',): Fraction(1)}


def realign(U):
    return [[U[3*i+a][3*j+b] for a,b in product(range(3), repeat=2)] for i,j in product(range(3), repeat=2)]


def pt(U):
    G = [[{} for _ in range(9)] for _ in range(9)]
    for i,a,j,b in product(range(3), repeat=4):
        G[3*i+b][3*j+a] = U[3*i+a][3*j+b]
    return G


def main():
    path = Path(sys.argv[1])
    if path.exists():
        raise SystemExit('Refusing to overwrite receipt')
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(), 'status': 'FAILED',
              'driver_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    try:
        U = [[phi(a,b,c,d) for a,b in product(range(3), repeat=2)] for c,d in product(range(3), repeat=2)]
        R = realign(U)
        base = {}
        for name, A, left in [('UUdag',U,True),('UdagU',U,False),('RRdag',R,True),('RdagR',R,False)]:
            E = residual(A,left)
            for i,j in product(range(9),repeat=2):
                p = E[i][j]
                for variant, q in [('same',p),('negative',scale(p,-1)),('conjugate',conjugate(p)),('negative-conjugate',scale(conjugate(p),-1))]:
                    base.setdefault(key(q), {'equation':name,'row':i,'column':j,'variant':variant})
        K = (1,2)
        N = {d:[[phi(0,b,c,d) for c in K] for b in K] for d in range(3)}
        Q = {a:[[phi(a,b,c,0) for c in K] for b in K] for a in range(3)}
        Rc = {c:[[phi(a,0,c,d) for d in K] for a in K] for c in range(3)}
        Tb = {b:[[phi(a,b,0,d) for d in K] for a in K] for b in range(3)}
        Om = {(a,d):[[phi(a,b,c,d) for c in K] for b in K] for a,d in product(K,repeat=2)}
        Op = {(b,c):[[phi(a,b,c,d) for d in K] for a in K] for b,c in product(K,repeat=2)}
        checks = []
        def equation(name,p):
            match = base.get(key(p))
            checks.append({'name':name,'matches_original_unitarity_entry':match is not None,'entry':match,'terms':len(p)})
            if match is None:
                raise ValueError('not an original biunitarity relation: '+name)
        def matrix(name,A):
            for i,j in product(range(len(A)),range(len(A[0]))):equation(f'{name}[{i+1},{j+1}]',A[i][j])
        for label,fam in [('N',N),('Q',Q),('R',Rc),('T',Tb)]:
            matrix('U-'+label+'-left',ma(*(mm(A,dagger(A)) for A in fam.values()),eye(2,-1)))
            matrix('U-'+label+'-right',ma(*(mm(dagger(A),A) for A in fam.values()),eye(2,-1)))
        for a in K:
            matrix(f'alpha-{a}',ma(mm(N[0],dagger(Q[a])),*(mm(N[d],dagger(Om[a,d])) for d in K)))
            matrix(f'gamma-{a}',ma(mm(dagger(N[0]),Q[a]),*(mm(dagger(N[d]),Om[a,d]) for d in K)))
        for d in K:
            matrix(f'beta-{d}',ma(mm(N[d],dagger(N[0])),*(mm(Om[a,d],dagger(Q[a])) for a in K)))
            matrix(f'delta-{d}',ma(mm(dagger(N[0]),N[d]),*(mm(dagger(Q[a]),Om[a,d]) for a in K)))
        for b in K:
            matrix(f'mirror-alpha-{b}',ma(mm(Tb[b],dagger(Rc[0])),*(mm(Op[b,c],dagger(Rc[c])) for c in K)))
            matrix(f'mirror-gamma-{b}',ma(mm(dagger(Rc[0]),Tb[b]),*(mm(dagger(Rc[c]),Op[b,c]) for c in K)))
        for a,b in product(K,repeat=2):
            equation(f'O1-{a}-{b}',add(*(mul(N[d][b-1][c-1],conjugate(Rc[c][a-1][d-1])) for c,d in product(K,repeat=2))))
        for c,d in product(K,repeat=2):
            equation(f'O2-{c}-{d}',add(*(mul(Q[a][b-1][c-1],conjugate(Tb[b][a-1][d-1])) for a,b in product(K,repeat=2))))
        for a,c in product(K,repeat=2):
            equation(f'O3-{a}-{c}',add(*(mul(N[d][b-1][c-1],conjugate(Tb[b][a-1][d-1])) for b,d in product(K,repeat=2))))
        for b,d in product(K,repeat=2):
            equation(f'O4-{b}-{d}',add(*(mul(Q[a][b-1][c-1],conjugate(Rc[c][a-1][d-1])) for a,c in product(K,repeat=2))))
        bad_O1=add(*(mul(N[d][0][c-1],Rc[c][0][d-1]) for c,d in product(K,repeat=2)))
        bad_alpha=ma(mm(N[0],transpose(Q[1])),*(mm(N[d],dagger(Om[1,d])) for d in K))[0][0]
        mutations={'omit-conjugate-O1':key(bad_O1) not in base,'transpose-not-dagger-alpha':key(bad_alpha) not in base}
        if not all(mutations.values()):raise ValueError('a wrong-relation control was not distinguished')
        result['relations'] = checks
        result['relation_count'] = len(checks)
        result['negative_controls'] = mutations
        # An independently specified attaining gate: theta=2pi/3 in the published real family, then left SWAP.
        c,s = const(Fraction(-1,2)), {('sqrt3',):Fraction(1,2)}
        rows=[[(2,scale(c,-1)),(3,s)],[(1,const(1))],[(0,c),(8,s)],[(0,s),(8,scale(c,-1))],
              [(5,s),(7,c)],[(4,s),(6,c)],[(5,scale(c,-1)),(7,s)],[(4,c),(6,scale(s,-1))],[(2,s),(3,c)]]
        T=[[{} for _ in range(9)] for _ in range(9)]
        for i,row in enumerate(rows):
            for j,value in row:T[i][j]=value
        star=[T[3*j+i] for i,j in product(range(3),repeat=2)]
        starR=realign(star);G=pt(star);W=mm(G,dagger(G));WW=mm(W,W)
        equalities={'unitary':mm(star,dagger(star))==eye(9),'dual':mm(starR,dagger(starR))==eye(9),
                    'self-realigned':starR==star,'W_squared_equals_three_halves_W':WW==[[scale(p,Fraction(3,2)) for p in row] for row in W],
                    'trace_W_equals9':add(*(W[i][i] for i in range(9)))==const(9),
                    'trace_W2_equals27_over2':add(*(WW[i][i] for i in range(9)))==const(Fraction(27,2)),'not_2unitary':W!=eye(9)}
        if not all(equalities.values()):raise ValueError('attaining gate exact identity failed')
        result['attaining_gate']={'field':'Q(sqrt3), exact Fraction coefficients','identities':equalities,
                                 'rank_from_positive_W_polynomial_and_trace':6,'entangling_power':str(Fraction(9,8)-Fraction(27,2)/72)}
        result['status']='PARENT_EXACT_BIUNITARITY_RELATIONS_AND_ATTAINING_GATE_PASS'
        result['limits']='Symbolic relations and explicit attaining gate only. This does not by itself prove the rank case tree; independent mathematical reviews and the FactK import are separate.'
    except Exception as exc:
        result['error']=type(exc).__name__+': '+str(exc)
    with path.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({k:result.get(k) for k in ['status','error','relation_count','negative_controls','attaining_gate']},indent=2))
    return 0 if result['status'].endswith('PASS') else 1


if __name__=='__main__':raise SystemExit(main())
