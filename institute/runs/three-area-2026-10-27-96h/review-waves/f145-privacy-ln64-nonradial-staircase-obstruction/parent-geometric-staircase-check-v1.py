#!/usr/bin/env python3
"""Independent parent exact controls; universal privacy/geometry inference remains written.
No author/reviewer code imported. All outputs are exclusive, additive evidence.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
from itertools import product
import hashlib,json,subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
REPO=ROOT.parents[2]
OUT=HERE/'parent-geometric-staircase-result-v1.json'

def clock():
    return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()

def require(ok,label):
    if not ok:raise ValueError(label)

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def val(a,x):
    y=F(0)
    for v in reversed(a):y=y*x+v
    return y

def derivative(a):return [i*a[i] for i in range(1,len(a))]

def ceil(x):return -((-x.numerator)//x.denominator)

def distance_and_point(x,y,a,eta):
    p,q=abs(x),abs(y);c=a-eta
    u,v=min(p,c),min(q,c)
    excess=max(F(0),u+v-a)
    take=min(u,excess);u-=take;v-=excess-take
    distance=p+q-u-v
    require(0<=u<=c and 0<=v<=c and u+v<=a,'CONSTRUCTED_POINT_OUTSIDE_CORE')
    require(distance==max(F(0),p+q-a,max(F(0),p-c)+max(F(0),q-c)),'EXACT_DISTANCE_FORMULA')
    return distance,(u if x>=0 else -u,v if y>=0 else -v)

def main():
    require(not OUT.exists(),'OUTPUT_EXISTS')
    start=clock()
    paths=[(HERE/'parent-required-numeric-correction-v1.json','3b29787c171857d35099fded30bc7d1c2bd9b957537d64b54891209a8a1197bb'),(REPO/'information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-ln64-rational-nonradial-obstruction-v1.md','028397b5e5c5cae583f9fc69ed1efadbaeda169c729d3cb878b74b1e2cc14e01')]
    bindings=[]
    for p,want in paths:
        data=p.read_bytes();digest=hashlib.sha256(data).hexdigest()
        require(digest==want,'INPUT_SHA')
        bindings.append({'path':str(p),'sha256':digest,'bytes':len(data),'LF':data.count(b'\n')})
    correction=json.loads(paths[0][0].read_text())
    b=F(1,64);m=b/(1-b);a=F(3761763123,10**10);z=F(3761763124,10**10);eta=F(1,100)
    raw=[F(1)]
    for j in range(1,5):raw.append(m*sum(comb(j,i)*raw[i] for i in range(j)))
    def moments(j):return [comb(j,i)*raw[j-i] for i in range(j+1)]
    M1,M2,M4=moments(1),moments(2),moments(4)
    P=[m*m*(1+2*m),-m*(1+2*m)*(1+6*m),12*m**3-2*m,2*m+12*m*m,5*m,F(1)]
    left=mul(derivative(M4),M2);right=mul(M4,derivative(M2))
    require([x-y for x,y in zip(left,right)]==[2*x for x in P],'DERIVATIVE_POLYNOMIAL')
    require(val(P,0)>0 and val(P,a)<0 and val(P,z)>0 and val(P,1)>0,'ROOT_BRACKET_SIGNS')
    require([1 if c>0 else -1 for c in reversed(P)]==[1,1,1,-1,-1,1],'DESCARTES_TWO_CHANGES')
    require(val(M4,0)*val(M2,1)==val(M4,1)*val(M2,0),'ENDPOINT_LAWS_COST')
    Z=2*val(M2,a)-4*eta**2
    moment=F(2,3)*val(M4,a)-4*val(M2,a)*eta**2+F(16,3)*val(M1,a)*eta**3-F(8,3)*eta**4
    require(Z>0,'POSITIVE_NORMALIZER');cost=moment/Z
    bound=val(M4,a)/(3*val(M2,z))-cost
    expected=F(int(correction['correct_gap_numerator']),int(correction['correct_gap_denominator']))
    require(bound==expected and bound>F(1,10**6),'CORRECTED_GAP')
    require(bound*10**6!=bound,'ORIGINAL_DENOMINATOR_MUTATION')
    geometry_cases=0;privacy_cases=0
    for k in (F(0),F(1,3),F(1),F(2),F(5)):
        R=a+k;coordinates={F(0),eta,R-eta,R,R+F(1,1000),-(R-eta),-R,-R-F(1,1000)}
        for x,y in product(coordinates,repeat=2):
            d,p=distance_and_point(x,y,a,eta)
            require((d<=k)==(abs(x)+abs(y)<=R and max(abs(x),abs(y))<=R-eta),'MINKOWSKI_BOUNDARY')
            require(abs(x-p[0])+abs(y-p[1])==d,'ATTAINED_DISTANCE')
            geometry_cases+=1
            for h in ((F(1),F(0)),(F(0),F(-1)),(F(1,3),F(2,3)),(F(-1,2),F(1,2))):
                dh,_=distance_and_point(x+h[0],y+h[1],a,eta)
                require(abs(ceil(d)-ceil(dh))<=1,'CLOSED_DIAMOND_SHIFT')
                privacy_cases+=1
    r=a-eta/2
    require(ceil(distance_and_point(r,0,a,eta)[0])==1 and ceil(distance_and_point(r/2,r/2,a,eta)[0])==0,'NONRADIAL_EQUAL_RADIUS')
    ap,ep,kp=F(3,10),F(1,5),F(1);x,y=F(11,10),F(1,5)
    require(abs(x)+abs(y)<=ap+kp and max(abs(x),abs(y))<=ap+kp-ep and distance_and_point(x,y,ap,ep)[0]>kp,'ETA_HYPOTHESIS_COUNTERCONTROL')
    origin=(a-eta,F(0))
    require(ceil(distance_and_point(origin[0]+2,0,a,eta)[0])-ceil(distance_and_point(*origin,a,eta)[0])==2,'OUTSIDE_SHIFT_DOMAIN_COUNTERCONTROL')
    coarse=val(M4,F(37617,100000))/(3*val(M2,F(37618,100000)))-cost
    require(coarse<0,'COARSE_ENCLOSURE_COUNTERCONTROL')
    result={'kind':'PARENT_INDEPENDENT_EXACT_PRIVACY_COMPETITOR_CONTROLS','inputs':bindings,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'started_native_clock':start,'finished_native_clock_before_receipt':clock(),'cost':str(cost),'gap_lower_bound':str(bound),'gap_exceeds_1e_6':True,'derivative_polynomial_identity':True,'root_endpoint_signs':[1,-1,1,1],'geometry_cases':geometry_cases,'closed_D_shift_cases':privacy_cases,'controls':['equal_radius_nonradiality','eta_constraint_counterexample','outside_shift_domain','coarse_enclosure_not_a_gap_certificate','original_denominator_mutation'],'limits':'Bounded exact geometry/arithmetic diagnostics, not all-law optimality, an all-radial theorem, formal/kernel verification or novelty. Universal privacy and all-gamma inference are written mathematics.'}
    with OUT.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print(json.dumps({'result':'PASS','path':str(OUT),'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'geometry_cases':geometry_cases,'closed_D_shift_cases':privacy_cases,'clock':result['finished_native_clock_before_receipt']}))

if __name__=='__main__':main()
