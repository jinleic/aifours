#!/usr/bin/env python3
"""Universal coefficient verification of the independently derived Green integrals.
All variables formal. Standard-library Fraction sparse polynomial operations.
No author code imports; does not rerun the numerical control.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,subprocess,sys

class P:
    def __init__(self,v=0):
        self.a=dict(v.a) if isinstance(v,P) else ({e:F(c) for e,c in v.items() if c} if isinstance(v,dict) else ({(0,0,0,0):F(v)} if v else {}))
    def __add__(self,b):
        a=dict(self.a)
        for e,c in P(b).a.items(): a[e]=a.get(e,F(0))+c
        return P(a)
    __radd__=__add__
    def __neg__(self): return P({e:-c for e,c in self.a.items()})
    def __sub__(self,b): return self+-P(b)
    def __rsub__(self,b): return P(b)+-self
    def __mul__(self,b):
        a={}
        for e,c in self.a.items():
            for f,d in P(b).a.items():
                h=tuple(x+y for x,y in zip(e,f)); a[h]=a.get(h,F(0))+c*d
        return P(a)
    __rmul__=__mul__
    def __truediv__(self,b): return self*F(1,F(b))
    def __pow__(self,n):
        r=P(1)
        for _ in range(n): r=r*self
        return r
    def __eq__(self,b): return self.a==P(b).a

def var(i):
    e=[0]*4;e[i]=1
    return P({tuple(e):1})

def clock(): return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()
start=clock()
m,t,d,k=[var(i) for i in range(4)]
v=m*(1+m)
mu=[P(1),m,m+2*m*m,m+6*m*m+6*m**3,m+14*m*m+36*m**3+24*m**4]

def mean(poly):
    r=P(0)
    for e,c in poly.a.items():
        f=list(e);f[3]=0
        r+=P({tuple(f):c})*mu[e[3]]
    return r

lam=2*t*t+2*d*d+2*m*(t+d)+mu[2]
A=lam-v;c=t-d;y=t+d+m;w=2*t
checks=[]
def check(name,condition): checks.append({'name':name,'passed':bool(condition)})
check('circle_intersection_identity',A-c*c==y*y)
# Derive the area and second moment of S+kD by Green's theorem on one octant.
e=k-m; a=t+d+k;s=t+k/2;cross=(a-c)*s
Zr=mean(4*(e*c+cross));Ztheta=4*A
Nr=mean(2*(e*(e*e+3*A)*c+e*e*c*y+cross*(a*a+c*c+(a+c)*s+2*s*s)/3))
Ntheta=mean(2*A*(2*e*e+A))
# Independently expand displayed primitive (5).
M2=mean((w+k)**2); M4=mean((w+k)**4)
j3r=c*y*(5*A-2*c*c)/8;j3theta=3*A*A/8
rr=-F(2,3)*j3r+(m*A-m**3/3)*c-c**4/3+lam*c*c/2
rt=-F(2,3)*j3theta
U=(w**3/3+m*w*w+(mu[2]-lam)*w)*c+(-w*w-2*m*w+2*lam-mu[2])*c*c/2+F(2,3)*(w+m)*c**3-F(2,3)*c**4
Hr=F(2,3)*M4-2*lam*M2+8*(rr-U);Htheta=8*rt
check('universal_normalizer_formula',Zr==8*t*d+4*m*(t+d)+2*mu[2] and Ztheta==4*A)
check('universal_H_rational_part',Nr-lam*Zr==Hr)
check('universal_H_atan_coefficient',Ntheta-lam*Ztheta==Htheta==-2*A*A)
check('negative_flipped_atan_coefficient_detected',Ntheta-lam*Ztheta!=2*A*A)
check('positive_core_geometry',A-((t+m)**2+t*t)==2*d*(d+m))
here=Path(__file__).resolve().parent
candidate=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-original-target-consolidated-review-v1.md')
data=candidate.read_bytes()
assert hashlib.sha256(data).hexdigest()=='37d1a560990b44e23da0a7f3c94399b8d88737b9f8276f9f667aa8a80352fa34'
failed=[x['name'] for x in checks if not x['passed']]
result={'kind':'INDEPENDENT_UNIVERSAL_FRACTION_POLYNOMIAL_IDENTITY_CHECK','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'candidate_sha256':hashlib.sha256(data).hexdigest(),'observed_native_clock_before_controls':start,'formal_variables':['m','t','d','k'],'assumed_algebraic_definition':'lambda=2t^2+2d^2+2m(t+d)+m+2m^2; no t(d) cubic is needed for these identities','checks':checks,'check_count':len(checks),'failure_count':len(failed),'failures':failed,'status':'PASS' if not failed else 'FAIL','author_code_imported_or_executed':False,'observed_native_clock_before_receipt_write':clock()}
with (here/'reviewer-geometry-identity-v1-receipt.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result,indent=2))
sys.exit(bool(failed))
