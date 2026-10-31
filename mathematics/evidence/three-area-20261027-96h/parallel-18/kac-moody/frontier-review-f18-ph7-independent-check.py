#!/usr/bin/env python3
"""Independent exact reconstruction of the f18 PH7 two-candidate assertions.

Reads no author checker or certificate.  SymPy is loaded from the owner's
already-existing local dependency directory.  All computations are symbolic
or exact rationals; outputs are review evidence, not formal verification.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEPS = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261028-localdeps')
sys.path.insert(0, str(DEPS))
import sympy as S

z, y, c, u, t, h = S.symbols('z y c u t h', real=True)
R = S.Rational


def zero(expr, label):
    value = S.cancel(S.together(expr))
    if value != 0:
        raise AssertionError(f'{label}: {S.factor(value)}')


def esym(values):
    result = [S.Integer(1)] + [S.Integer(0)] * len(values)
    for v in values:
        for j in range(len(values), 0, -1):
            result[j] += v * result[j - 1]
    return [S.expand(x) for x in result]


def bernstein(poly, var, lo, hi):
    q = S.Poly(S.cancel(poly), var)
    if not q.is_univariate:
        raise AssertionError('non-univariate polynomial')
    degree = q.degree()
    coeff = S.Poly(S.expand(q.as_expr().subs(var, lo + (hi - lo) * t)), t)
    power = [coeff.nth(i) for i in range(degree + 1)]
    out = [S.cancel(sum(power[i] * S.binomial(k, i) / S.binomial(degree, i)
                        for i in range(k + 1))) for k in range(degree + 1)]
    if not all(x.is_Rational and x > 0 for x in out):
        raise AssertionError(f'non-positive Bernstein coefficient: {out}')
    return out


def build_six_rate():
    U = [R(657,500), R(34,25), R(701,500)]
    V = [R(333,250), R(973,1000), R(1083,1000)]
    e = esym(U + V)
    a, b, c3 = e[1:4]
    H0 = b + 4*a - a*a - 6
    L = b - 4*a + 10 - 2*z
    N = 4*H0 + 4 - c3 - b*(4-a) - 4*z
    p = S.cancel(N/L)
    q = S.cancel((a-4)*p + H0 - 2*z)
    w = S.cancel(p + 4 - a)
    B = S.cancel(p - U[0] - U[1])
    C = S.cancel(q - U[0]*U[1] - U[0]*B)
    Qpoly = y*y + p*y + q
    phi = S.cancel(e[4]+c3*w-((6+2*z)*q+(4+4*z)*p+(1+z)**2))
    R2 = S.cancel(e[5]+e[4]*w-(4+4*z)*q-(1+z)**2*p)
    R1 = S.cancel(e[6]+e[5]*w-(1+z)**2*q)
    R0 = S.cancel(e[6]*w)
    D1 = S.cancel(R2-phi*sum(U))
    D2 = S.cancel(R1-phi*(U[0]*U[1]+U[0]*U[2]+U[1]*U[2])-(V[1]+V[2])*D1)
    D3 = S.cancel(R0-phi*U[0]*U[1]*U[2]-V[1]*V[2]*D1-V[2]*D2)
    G = S.Matrix([
        [-U[0],1,0,0,0,0,0], [0,-U[1],1,0,0,0,0],
        [0,0,-U[2],1,0,0,0], [0,0,0,-w,1,0,0],
        [D1,0,0,0,-V[0],1,0], [D2,0,0,0,0,-V[1],1],
        [D3,0,0,phi,0,0,-V[2]],
    ])
    beta = S.Matrix([[C,B,1,0,0,0,0]])
    e7 = S.Matrix([0,0,0,0,0,0,1])
    D = y*((y+1)**2+z)**2
    zero(Qpoly - ((y+U[0])*(y+U[1])+B*(y+U[0])+C), 'numerator Q identity')
    M = y*S.eye(7)-G
    det = S.factor(M.det(method='domain-ge'))
    zero(det-D*Qpoly, 'full 7x7 determinant')
    numerator = S.factor((M+e7*beta).det(method='domain-ge')-det)
    zero(numerator-Qpoly, 'full rank-one-update numerator')
    lo, hi = R(7,9), R(813,1000)
    quantities = {'L': L, 'L p': L*p, 'L q': L*q, 'L w': L*w,
                  'L B': L*B, 'L C': L*C, 'L phi': L*phi,
                  'L D1': L*D1, 'L D2': L*D2, 'L D3': L*D3}
    mins = {}
    coeffs = {}
    for name, value in quantities.items():
        pz = S.cancel(value)
        assert S.denom(pz) == 1 or S.denom(pz).is_Integer, (name, pz)
        vals = bernstein(pz, z, lo, hi)
        mins[name] = str(min(vals))
        coeffs[name] = [str(x) for x in vals]
    expected = {
        'L': '1655827/1000000', 'L p': '197624241/25000000',
        'L q': '821082825464857/81000000000000', 'L w': '387385171/187500000',
        'L B': '15434139089/4500000000', 'L C': '206156361843349/81000000000000',
        'L phi': '1537854116399697/250000000000000000',
        'L D1': '1101567448349339830399/281250000000000000000',
        'L D2': '8070475831016351252607/62500000000000000000000',
        'L D3': '313487595401834859325348379107/136687500000000000000000000000',
    }
    assert mins == expected, (mins, expected)
    K = c*((c+1)**2+z)**2
    Qc = c*c+p*c+q
    h1 = 1/Qc
    h2 = (c+U[0])*h1
    h3 = (c+U[1])*h2
    h4 = (c+U[2])*h3
    h7 = (K+D3*h1+phi*h4)/(c+V[2])
    h6 = (h7+D2*h1)/(c+V[1])
    h5 = (h6+D1*h1)/(c+V[0])
    hv = S.Matrix([h1,h2,h3,h4,h5,h6,h7])
    for j, value in enumerate((c*S.eye(7)-G)*hv-K*e7):
        zero(value, f'normalizer row {j+1}')
    zero((beta*hv)[0]-1, 'initial row normalization')
    return {'determinant_and_actual_numerator': 'PASS',
            'all_seven_rows_and_beta_h': 'PASS',
            'full_bernstein_coefficients': coeffs,
            'bernstein_minima': mins}


def build_equal_rate():
    e = esym([u,u,u,1,1,1])
    a,b,c3 = e[1:4]
    H0=b+4*a-a*a-6
    L=b-4*a+10-2*z
    N=4*H0+4-c3-b*(4-a)-4*z
    zero(L-(3*u*u-3*u+1-2*z),'equal L')
    zero(N-(8*u**3-9*u*u+3*u-4*z),'equal N')
    p=N/L
    q=(a-4)*p+H0-2*z
    w=p+4-a
    C=q-u*p+u*u
    phi=e[4]+c3*w-((6+2*z)*q+(4+4*z)*p+(1+z)**2)
    zero(C*L-((u*u+4*z)*(u-1)**2+2*z*(2*z-1)), 'C identity')
    zero(N.subs(z,(3*u*u-3*u+1)/2)-(u-1)*(8*u*u-7*u+2), 'singular matching')
    P = u**6-3*u**5+3*u**4-u**3+(6*u**4-26*u**3+30*u*u-12*u+2)*z+(15*u*u-27*u+9)*z*z+6*z**3
    zero(-L*phi-P, 'feedback numerator')
    deriv = t*t*(6*t*t-2*t+1)+(30*z-13)*t*t+(6*z-6)*t+(18*z*z-6*z)
    zero(S.diff(P,z).subs(u,1+t)-deriv, 'z derivative decomposition')
    disc=(6*z-6)**2-4*(30*z-13)*(18*z*z-6*z)
    zero((-disc).subs(z,R(1,2)+h)-(2160*h**3+1548*h*h+312*h+3), 'negative discriminant')
    z0=R(389,500)
    intervals=[]
    for k in range(8):
        vals=bernstein(P.subs(z,z0),u,1+R(k,16),1+R(k+1,16))
        intervals.append([str(v) for v in vals])
    expected_minima = [
        '27208441993941/32768000000000','332782156669/512000000000',
        '15478323400941/32768000000000','2439759321/8000000000',
        '5219194922941/32768000000000','26265477669/512000000000',
        '69564559941/32768000000000','467999551/2048000000000']
    assert [str(min(map(S.Rational,v))) for v in intervals] == expected_minima
    tail=S.Poly(S.expand(P.subs({u:R(3,2)+t,z:z0})),t)
    expected_tail=[R(1202491,31250000),R(179139,125000),R(377469,25000),
                   R(1239,50),R(9459,500),S.Integer(6),S.Integer(1)]
    assert [tail.nth(i) for i in range(7)] == expected_tail
    return {'all_equal_rate_algebra_and_monotonicity_identities': 'PASS',
            'full_bernstein_coefficients': intervals,
            'bernstein_minima': expected_minima,
            'tail_coefficients': [str(x) for x in expected_tail]}


def main():
    result={'sympy_version': S.__version__, 'six_rate': build_six_rate(),
            'equal_rate': build_equal_rate(),
            'scope':'exact polynomial identities and full Bernstein certificates; conditional PH proof in review',
            'not_formal_or_external_model_review':True}
    path=ROOT/'frontier-review-f18-ph7-independent-check-v1.json'
    if path.exists(): raise FileExistsError(path)
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: SymPy {S.__version__}; full 7x7 determinant/numerator, 7 normalization rows, 10 Bernstein lists, equal-rate 8 intervals, tail and monotonicity identities')
    print(path.name)


if __name__=='__main__': main()
