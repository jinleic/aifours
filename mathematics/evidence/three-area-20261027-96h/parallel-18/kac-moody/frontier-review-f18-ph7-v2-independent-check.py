#!/usr/bin/env python3
"""Exact independent reconstruction of f18's stronger 41/50 PH7 band.

Uses the reviewer's own already-written elementary Bernstein helpers and
SymPy installation, NOT any author checker or certificate.
"""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('own_f18', ROOT / 'frontier-review-f18-ph7-independent-check.py')
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)
S, R, z, y, c = a.S, a.R, a.z, a.y, a.c


def main():
    U = [R(1331,1000), R(341,250), R(1339,1000)]
    V = [R(33,25), R(257,250), R(132,125)]
    e = a.esym(U + V)
    A, B2, C3 = e[1:4]
    H0 = B2 + 4*A - A*A - 6
    L = B2 - 4*A + 10 - 2*z
    N = 4*H0 + 4 - C3 - B2*(4-A) - 4*z
    p = S.cancel(N/L)
    q = S.cancel((A-4)*p + H0 - 2*z)
    w = S.cancel(p + 4 - A)
    B = S.cancel(p-U[0]-U[1])
    C = S.cancel(q-U[0]*U[1]-U[0]*B)
    Q = y*y+p*y+q
    phi = S.cancel(e[4]+C3*w-((6+2*z)*q+(4+4*z)*p+(1+z)**2))
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
    a.zero(Q-((y+U[0])*(y+U[1])+B*(y+U[0])+C),'v2 Q identity')
    M = y*S.eye(7)-G
    det = S.factor(M.det(method='domain-ge'))
    a.zero(det-D*Q,'v2 full determinant')
    numerator = S.factor((M+e7*beta).det(method='domain-ge')-det)
    a.zero(numerator-Q,'v2 actual numerator')
    low, high = R(7,9), R(41,50)
    expressions = {'L': L,'L p':L*p,'L q':L*q,'L w':L*w,'L B':L*B,
                   'L C':L*C,'L phi':L*phi,'L D1':L*D1,'L D2':L*D2,'L D3':L*D3}
    coefficients = {key: a.bernstein(S.cancel(value),z,low,high) for key,value in expressions.items()}
    minima = {key: str(min(values)) for key, values in coefficients.items()}
    expected = {
        'L':'1600273/1000000','L p':'152908751/20000000',
        'L q':'793057212755377/81000000000000','L w':'568762837/281250000',
        'L B':'5893223267/1800000000','L C':'2404222780259/1012500000000',
        'L phi':'65787988944437/62500000000000000',
        'L D1':'9385943652095983401971/2531250000000000000000',
        'L D2':'24745026011159738267/62500000000000000000000',
        'L D3':'14989313308981887372658595357/6834375000000000000000000000',
    }
    assert minima == expected, (minima, expected)
    K = c*((c+1)**2+z)**2
    Qc = c*c+p*c+q
    h1=1/Qc
    h2=(c+U[0])*h1
    h3=(c+U[1])*h2
    h4=(c+U[2])*h3
    h7=(K+D3*h1+phi*h4)/(c+V[2])
    h6=(h7+D2*h1)/(c+V[1])
    h5=(h6+D1*h1)/(c+V[0])
    hv=S.Matrix([h1,h2,h3,h4,h5,h6,h7])
    for j,value in enumerate((c*S.eye(7)-G)*hv-K*e7):
        a.zero(value,f'v2 normalizer row {j+1}')
    a.zero((beta*hv)[0]-1,'v2 alpha normalization')
    out=ROOT/'frontier-review-f18-ph7-v2-independent-check-v1.json'
    if out.exists(): raise FileExistsError(out)
    out.write_text(json.dumps({
        'sympy_version':S.__version__, 'all_7x7_determinant_numerator_rows':'PASS',
        'bernstein_minima':minima,
        'full_bernstein_coefficients':{k:[str(x) for x in v] for k,v in coefficients.items()},
        'not_formal_or_external_model_review':True,
    },indent=2)+'\n',encoding='utf-8')
    print(f'PASS: SymPy {S.__version__}; v2 full determinant/numerator, 7 normalizer rows, beta*h and all 10 exact Bernstein lists; {out.name}')


if __name__=='__main__': main()
