#!/usr/bin/env python3
"""Plain-integer replay of all 388-simple-root Bezout identities."""
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('finite',ROOT/'frontier-20261028-level6-226-generic-irreducibility-independent-replay.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)


def main():
    D=json.loads((ROOT/'frontier-20261028-level6-226-discriminant-modp-certificate-v1.json').read_text())
    W=json.loads((ROOT/'frontier-20261028-level6-226-simple-branch-gcd-guard-v1.json').read_text())
    p=D['prime'];assert p==W['prime']==32749;f.p=p
    R=D['resultant_coefficients_low_to_high'];S=D['simple_factor_coefficients'];T=W['D_quotient_coefficients']
    assert len(R)==421 and len(S)==389 and S[-1]==1 and len(T)==33
    assert f.mul(S,T)==R
    derivative=f.trim([i*S[i] for i in range(1,len(S))])
    a,b=W['squarefree_bezout_a'],W['squarefree_bezout_b']
    u,v=W['simple_vs_quotient_bezout_a'],W['simple_vs_quotient_bezout_b']
    assert f.add(f.mul(a,S),f.mul(b,derivative))==[1]
    assert f.add(f.mul(u,S),f.mul(v,T))==[1]
    out=ROOT/'frontier-20261028-level6-226-simple-branch-gcd-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'prime':p,'D_degree':420,'simple_factor_degree':388,
                               'integer_modular_product_and_two_bezout_identities_checked':True,
                               'status':'PASS_FULL_388_SIMPLE_ROOT_FACTOR_IDENTITIES',
                               'scope':'finite-field identities only; Hensel/monodromy/genus/Faltings remain named written theorem inputs'},indent=2)+'\n')
    print('PASS independent integer modular product and two full Bezout identities for degree388 factor;',out.name)

if __name__=='__main__':main()
