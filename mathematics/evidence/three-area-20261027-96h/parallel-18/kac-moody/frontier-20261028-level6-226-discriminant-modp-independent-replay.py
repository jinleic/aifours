#!/usr/bin/env python3
"""Independent full Sylvester-grid and modular squarefree-factor replay.

Uses a direct 41x41 modular determinant at ALL 841 interpolation points,
then SymPy finite-field gcd/quotient identities. No genus or Faltings proof.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
mod=load('mod','frontier-20261028-level6-446-modular-determinant-replay.py')
helper=load('helper','frontier-review-f18-ph7-independent-check.py');S=helper.S
p=32749


def polyval(a,x):
    z=0
    for c in reversed(a):z=(z*x+c)%p
    return z


def sylvester(a,b):
    m=len(a)-1;n=len(b)-1;ad=list(reversed(a));bd=list(reversed(b));N=m+n
    return [[0]*i+ad+[0]*(N-i-len(ad)) for i in range(n)]+[[0]*i+bd+[0]*(N-i-len(bd)) for i in range(m)]


def main():
    raw=(ROOT/'frontier-20261028-level6-226-generic-irreducibility-certificate-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='5aa67436e478db33b12bdfe3f6ba00b321ca81ebe9a8fa1fca4a6c9efd7d4297'
    R=json.loads(raw);C=json.loads((ROOT/'frontier-20261028-level6-226-discriminant-modp-certificate-v1.json').read_text())
    assert C['status']=='EXACT_MODP_SIMPLE_DISCRIMINANT_FACTOR' and C['prime']==p and mod.prime(p)
    terms=[(e['x_power'],e['y_power'],int(e['coefficient'])%p) for e in R['R_coefficients']]
    assert R['R_degree_y']==21 and R['R_y_leading_constant']==2107392 and 2107392%p
    assert all(type(i)==type(j)==int and i>=0 and j>=0 and i+j<=21 for i,j,c in terms)
    polys=C['resultant_coefficients_low_to_high'];assert len(polys)<=841
    for x in range(841):
        powx=[pow(x,i,p) for i in range(22)];f=[0]*22
        for i,j,c in terms:f[j]=(f[j]+c*powx[i])%p
        assert f[-1];g=[j*f[j]%p for j in range(1,22)];assert g[-1]
        assert mod.modular_det(sylvester(f,g),p)==polyval(polys,x),('resultant mismatch',x)
    x=S.symbols('x');P=S.Poly(sum(S.Integer(c)*x**i for i,c in enumerate(polys)),x,modulus=p)
    derivative=P.diff();g=S.gcd(P,derivative).monic();distinct=S.exquo(P,g)
    repeated=S.gcd(distinct,g).monic();simple=S.exquo(distinct,repeated).monic()
    def low(q):return [int(q.nth(i))%p for i in range(q.degree()+1)] if not q.is_zero else []
    assert low(g)==C['gcd_derivative_coefficients']
    assert low(simple)==C['simple_factor_coefficients'] and simple.degree()==C['simple_root_count_over_algebraic_closure']
    out=ROOT/'frontier-20261028-level6-226-discriminant-modp-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'prime':p,'R_sha256':digest,'grid_resultants_checked':841,'Sylvester_matrix_size':41,
                               'coefficient_degree_bound':840,'actual_modular_resultant_degree':P.degree(),
                               'simple_root_factor_degree':simple.degree(),
                               'status':'PASS_ALL_GRID_RESULTANTS_AND_SIMPLE_ROOT_FACTOR',
                               'scope':'finite-field discriminant data only; lifting, geometric monodromy, Riemann-Hurwitz and Faltings require separate proof'},indent=2)+'\n')
    print('PASS 841 full Sylvester resultants and exact modular simple-factor degree',simple.degree(),out.name,flush=True)

if __name__=='__main__':main()
