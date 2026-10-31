#!/usr/bin/env python3
"""Plain-integer replay of both univariate finite-field factor certificates."""
import importlib.util
import json
import math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('finite',ROOT/'frontier-20261028-level6-226-generic-irreducibility-independent-replay.py')
finite=importlib.util.module_from_spec(spec);spec.loader.exec_module(finite)


def main():
    R=json.loads((ROOT/'frontier-20261028-level6-226-generic-irreducibility-certificate-v1.json').read_text())
    C=json.loads((ROOT/'frontier-20261028-level6-226-galois-cycle-certificate-v1.json').read_text())
    assert C['status']=='EXACT_FINITE_FIELD_CYCLE_DATA'
    coefficients={(t['x_power'],t['y_power']):int(t['coefficient']) for t in R['R_coefficients']}
    results=[]
    for record in C['cycles']:
        p=record['prime'];finite.p=p;assert all(p%d for d in range(2,math.isqrt(p)+1))
        lead=2107392%p;assert lead
        full=finite.trim([coefficients.get((0,j),0)*pow(lead,-1,p) for j in range(22)])
        assert full==record['monic_full_polynomial'] and len(full)==22 and full[-1]==1
        factors=[f['factor_low_to_high'] for f in record['factors']]
        assert finite.mul(factors[0],factors[1])==full
        assert [len(f)-1 for f in factors]==record['pattern']
        assert finite.add(finite.mul(record['pairwise_bezout_a'],factors[0]),finite.mul(record['pairwise_bezout_b'],factors[1]))==[1]
        for item,g in zip(record['factors'],factors):
            n=item['degree'];assert len(g)==n+1 and g[-1]==1
            y=[0,1];h=y;powers={}
            for k in range(1,n+1):
                h=finite.powmod(h,p,g);powers[k]=h
            assert powers[n]==finite.rem(y,g) and powers[n]==item['frobenius_n_remainder']
            prime_divisors=[ell for ell in range(2,n+1) if n%ell==0 and all(ell%d for d in range(2,math.isqrt(ell)+1))]
            assert set(item['proper_prime_divisor_checks'])=={str(n//ell) for ell in prime_divisors}
            for ell in prime_divisors:
                k=n//ell;check=item['proper_prime_divisor_checks'][str(k)]
                assert powers[k]==check['h_power']
                identity=finite.add(finite.mul(check['bezout_a'],finite.add(powers[k],finite.neg(y))),finite.mul(check['bezout_b'],g))
                assert identity==[1]
        results.append({'prime':p,'factor_degrees':record['pattern'],'product_irreducibility_and_coprimality_checked':True})
    assert results==[{'prime':59,'factor_degrees':[2,19],'product_irreducibility_and_coprimality_checked':True},
                     {'prime':467,'factor_degrees':[1,20],'product_irreducibility_and_coprimality_checked':True}]
    out=ROOT/'frontier-20261028-level6-226-galois-cycle-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'cycles':results,'status':'PASS_BOTH_EXACT_FACTOR_RABIN_BEZOUT_DATA',
                               'scope':'finite-field data only; Dedekind/Frobenius and specialization group theory are written imports'},indent=2)+'\n')
    print('PASS integer finite-field product/Rabin/Bezout data at p59 and p467;',out.name)

if __name__=='__main__':main()
