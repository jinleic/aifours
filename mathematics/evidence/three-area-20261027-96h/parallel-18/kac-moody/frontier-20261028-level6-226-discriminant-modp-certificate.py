#!/usr/bin/env python3
"""Compute one exact modular discriminant and its simple-root factor.

The coefficient-degree bound 840 is an elementary resultant bound.  Euclid
resultants are crosschecked with a distinct exact Sylvester determinant on
three values. No genus, geometric irreducibility or Faltings claim is made.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('mod',ROOT/'frontier-20261028-level6-446-modular-determinant-replay.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
p=32749


def trim(a):
    a=[x%p for x in a]
    while a and not a[-1]:a.pop()
    return a


def divmodp(a,b):
    a=trim(a);b=trim(b);assert b
    if len(a)<len(b):return [],a
    q=[0]*(len(a)-len(b)+1);inv=pow(b[-1],-1,p)
    while len(a)>=len(b):
        d=len(a)-len(b);v=a[-1]*inv%p;q[d]=v
        for j,c in enumerate(b):a[j+d]=(a[j+d]-v*c)%p
        a=trim(a)
    return trim(q),a


def gcdp(a,b):
    a=trim(a);b=trim(b)
    while b:_,r=divmodp(a,b);a,b=b,r
    if not a:return []
    inv=pow(a[-1],-1,p);return trim([z*inv for z in a])


def resultant(a,b):
    a=trim(a);b=trim(b);assert a and b
    value=1
    while len(b)>1:
        ma,mb=len(a)-1,len(b)-1
        _,r=divmodp(a,b)
        if not r:return 0
        if (ma*mb)&1:value=-value
        value=value*pow(b[-1],ma-(len(r)-1),p)%p
        a,b=b,r
    return value*pow(b[0],len(a)-1,p)%p


def polyval(a,x):
    z=0
    for c in reversed(a):z=(z*x+c)%p
    return z


def sylvester(a,b):
    m=len(a)-1;n=len(b)-1;ad=list(reversed(a));bd=list(reversed(b));size=m+n
    return [[0]*i+ad+[0]*(size-i-len(ad)) for i in range(n)]+[[0]*i+bd+[0]*(size-i-len(bd)) for i in range(m)]


def main():
    assert mod.prime(p) and p>840
    raw=(ROOT/'frontier-20261028-level6-226-generic-irreducibility-certificate-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='5aa67436e478db33b12bdfe3f6ba00b321ca81ebe9a8fa1fca4a6c9efd7d4297'
    R=json.loads(raw);assert R['R_degree_y']==21 and R['R_y_leading_constant']==2107392 and 2107392%p
    terms=[(e['x_power'],e['y_power'],int(e['coefficient'])%p) for e in R['R_coefficients']]
    assert all(i>=0 and j>=0 and i+j<=21 for i,j,c in terms)
    def evaluate(x):
        powers=[pow(x,i,p) for i in range(22)];f=[0]*22
        for i,j,c in terms:f[j]=(f[j]+c*powers[i])%p
        assert f[-1] and len(f)==22
        der=[j*f[j]%p for j in range(1,22)];assert der[-1]
        return f,der,resultant(f,der)
    values=[]
    for x in range(841):
        f,g,v=evaluate(x)
        if x<3:assert v==mod.modular_det(sylvester(f,g),p),('resultant convention',x)
        values.append(v)
    work=values[:];diff=[]
    while work:diff.append(work[0]);work=[(b-a)%p for a,b in zip(work,work[1:])]
    # Interpolate in binomial basis, then expand to ordinary coefficients.
    poly=[0]*841;basis=[1]
    for k,q in enumerate(diff):
        for j,c in enumerate(basis):poly[j]=(poly[j]+q*c)%p
        if k<840:
            inv=pow(k+1,-1,p);nxt=[0]*(len(basis)+1)
            for j,c in enumerate(basis):
                nxt[j]=(nxt[j]-k*c*inv)%p;nxt[j+1]=(nxt[j+1]+c*inv)%p
            basis=trim(nxt)
    poly=trim(poly);assert poly
    assert all(polyval(poly,x)==v for x,v in enumerate(values))
    assert all(polyval(poly,x)==evaluate(x)[2] for x in range(841,846))
    derivative=trim([i*poly[i]%p for i in range(1,len(poly))]);g=gcdp(poly,derivative)
    distinct,rem=divmodp(poly,g);assert not rem
    repeated=gcdp(distinct,g);simple,rem=divmodp(distinct,repeated);assert not rem
    # Normalize simple factor so degree and coefficients are independent of units.
    if simple:
        inv=pow(simple[-1],-1,p);simple=trim([x*inv for x in simple])
    out=ROOT/'frontier-20261028-level6-226-discriminant-modp-certificate-v1.json'
    if out.exists():raise FileExistsError(out)
    result={'R_sha256':digest,'prime':p,'resultant_degree_bound':840,'evaluations':841,
            'euclid_vs_sylvester_checks':3,'extra_grid_checks':5,'modular_resultant_degree':len(poly)-1,
            'resultant_coefficients_low_to_high':poly,'gcd_derivative_coefficients':g,
            'distinct_factor_coefficients':distinct,'repeated_distinct_gcd':repeated,
            'simple_factor_coefficients':simple,'simple_root_count_over_algebraic_closure':len(simple)-1,
            'status':'EXACT_MODP_SIMPLE_DISCRIMINANT_FACTOR',
            'limits':'no independently reviewed interpolation, characteristic-zero lifting, geometric monodromy, genus, Faltings or original-map conclusion'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact modular discriminant degree',len(poly)-1,'simple-root factor degree',len(simple)-1,out.name,flush=True)

if __name__=='__main__':main()
