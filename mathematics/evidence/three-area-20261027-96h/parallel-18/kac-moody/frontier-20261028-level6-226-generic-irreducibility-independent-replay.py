#!/usr/bin/env python3
"""Plain-integer replay of bivariate factor and F_61 Rabin certificate."""
import hashlib
import json
import math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
p=61


def trim(a):
    a=[x%p for x in a]
    while a and not a[-1]:a.pop()
    return a


def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def neg(a):return trim([-x for x in a])
def mul(a,b):
    if not a or not b:return []
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%p
    return trim(out)


def rem(a,b):
    a=trim(a);b=trim(b);assert b
    inv=pow(b[-1],-1,p)
    while len(a)>=len(b):
        k=len(a)-len(b);scale=a[-1]*inv%p
        for j,x in enumerate(b):a[j+k]=(a[j+k]-scale*x)%p
        a=trim(a)
    return a


def powmod(a,e,f):
    z=[1]
    while e:
        if e&1:z=rem(mul(z,a),f)
        e//=2
        if e:a=rem(mul(a,a),f)
    return z


def main():
    raw=(ROOT/'frontier-20261028-level6-226-modular-row-certificate-v1.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='738977afb213e2ddec6426c852e27bdab0edbaa8611d127f6048ee84db40a217'
    Qdata=json.loads(raw);C=json.loads((ROOT/'frontier-20261028-level6-226-generic-irreducibility-certificate-v1.json').read_text())
    assert C['status']=='RABIN_IRREDUCIBLE_DEGREE21_SPECIALIZATION' and C['prime']==p
    assert all(p%d for d in range(2,math.isqrt(p)+1))
    q={(t['x_power'],t['y_power']):int(t['coefficient']) for t in Qdata['Q_coefficients']}
    r={(t['x_power'],t['y_power']):int(t['coefficient']) for t in C['R_coefficients']}
    assert len(q)==341 and len(r)==253 and max(j for i,j in r)==21
    assert [(i,c) for (i,j),c in r.items() if j==21]==[(0,2107392)]
    # Independent exact convolution Q=(x+5)^4 R.
    out={}
    for (i,j),c in r.items():
        for u in range(5):out[i+u,j]=out.get((i+u,j),0)+c*math.comb(4,u)*5**(4-u)
    assert {z:c for z,c in out.items() if c}==q
    lc=2107392%p;assert lc and p==61
    f=trim([r.get((0,j),0)*pow(lc,-1,p) for j in range(22)])
    assert len(f)==22 and f[-1]==1 and f==C['monic_f61_coefficients_low_to_high']
    y=[0,1];h=y;powers={}
    for k in range(1,22):
        h=powmod(h,p,f)
        if k in (3,7,21):powers[k]=h
    assert powers[21]==y and C['frobenius_21_remainder']==y
    for k in (3,7):
        b=C['bezout_certificates'][str(k)]
        assert powers[k]==b['h_power']
        relation=add(mul(b['bezout_a'],add(powers[k],neg(y))),mul(b['bezout_b'],f))
        assert relation==[1]
    out=ROOT/'frontier-20261028-level6-226-generic-irreducibility-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    result={'degree':[2,2,6],'R_y_degree':21,'R_y_leading_constant':2107392,
            'integer_Q_factor_identity_verified':True,'prime':p,
            'frobenius_3_7_21_and_both_bezout_identities_verified':True,
            'status':'PASS_INTEGER_FACTOR_AND_F61_RABIN_DATA',
            'scope':'Rabin finite-field criterion is a named standard mathematical theorem; generic/Hilbert application is not program output'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS integer Q factor, degree21 constant leading, F61 Frobenius3/7/21 and both Bezout identities;',out.name)

if __name__=='__main__':main()
