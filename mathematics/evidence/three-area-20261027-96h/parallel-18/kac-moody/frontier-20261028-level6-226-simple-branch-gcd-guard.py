#!/usr/bin/env python3
"""Check the 388-root modular factor by exact gcd/Bezout identities."""
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('helper',ROOT/'frontier-review-f18-ph7-independent-check.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper);S=helper.S


def main():
    C=json.loads((ROOT/'frontier-20261028-level6-226-discriminant-modp-certificate-v1.json').read_text());p=C['prime'];assert p==32749
    x=S.symbols('x')
    def poly(a):return S.Poly(sum(S.Integer(c)*x**i for i,c in enumerate(a)),x,modulus=p)
    D=poly(C['resultant_coefficients_low_to_high']);simple=poly(C['simple_factor_coefficients']);assert D.degree()==420 and simple.degree()==388
    quotient,rem=S.div(D,simple);assert rem.is_zero
    g1=S.gcd(simple,simple.diff());g2=S.gcd(simple,quotient)
    assert g1.degree()==g2.degree()==0
    a,b,c=S.gcdex(simple,simple.diff());assert c==S.Poly(1,x,modulus=p)
    u,v,w=S.gcdex(simple,quotient);assert w==S.Poly(1,x,modulus=p)
    def low(q):return [int(q.nth(i))%p for i in range(q.degree()+1)] if not q.is_zero else []
    result={'prime':p,'D_degree':420,'simple_factor_degree':388,
            'D_quotient_coefficients':low(quotient),
            'squarefree_bezout_a':low(a),'squarefree_bezout_b':low(b),
            'simple_vs_quotient_bezout_a':low(u),'simple_vs_quotient_bezout_b':low(v),
            'status':'PASS_388_DISTINCT_SIMPLE_MODULAR_ROOTS',
            'scope':'finite-field polynomial identities only; Hensel/ramification/geometric-monodromy/genus/Faltings are written theorem inputs'}
    out=ROOT/'frontier-20261028-level6-226-simple-branch-gcd-guard-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact D=S*T, gcd(S,Sprime)=gcd(S,T)=1; deg S=388;',out.name)

if __name__=='__main__':main()
