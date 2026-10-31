#!/usr/bin/env python3
"""Parent finite-boundary extension, REUSING the pinned parent f129 engine.
Not a new third polynomial implementation; author and reviewer code are unused.
"""
import hashlib,itertools,json,math,subprocess
from pathlib import Path
from fractions import Fraction as F
SOURCE=Path("/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f129-ph7-girth-four-two-or-three-cycle/parent-f129-certificate-check-v1.py")
SOURCE_SHA="1ef15ce57a142c8cfcaf55caf1e89c195e34f13372813946dd2bf08aa486e5cd"
OUT=Path(__file__).with_name('parent-finite-zero-face-result-v1.json')
def clock():return subprocess.check_output(['/bin/date','+%Y-%m-%dT%H:%M:%S%z %Z'],text=True).strip()
def require(ok,reason):
    if not ok:raise ValueError(reason)
raw=SOURCE.read_bytes()
require(hashlib.sha256(raw).hexdigest()==SOURCE_SHA,'ENGINE_HASH')
base={'__name__':'parent_f129_bound_engine','__file__':str(SOURCE)}
exec(compile(raw,str(SOURCE),'exec'),base)
require(not OUT.exists(),'OUTPUT_EXISTS')
start=clock()
data=base['CERT'].read_bytes()
require(hashlib.sha256(data).hexdigest()==base['CERT_SHA'],'CERT_HASH')
cert=json.loads(data);verts=list(itertools.product((0,2),repeat=6));strides=base['STRIDES']
def finite_corners(arr,zero_lo,one_hi):
    by_zeros=[0]*7
    for v in verts:
        if any(bit==2 and one_hi[i] for i,bit in enumerate(v)):continue
        index=sum(bit*s for bit,s in zip(v,strides))
        require(arr[index]>0,'NONPOSITIVE_FINITE_CORNER')
        by_zeros[sum(bit==0 and zero_lo[i] for i,bit in enumerate(v))]+=1
    return by_zeros

def audit(poly,paths):
    leaves,prefixes=base['partition'](paths)
    stack=[('',base['root_coefficients'](poly),(True,)*6,(True,)*6)]
    seen=set();coeffs=0;totals=[0]*7;control=None
    while stack:
        path,arr,zero_lo,one_hi=stack.pop()
        if path in leaves:
            require(path not in seen and len(path)>=6,'LEAF_COVERAGE')
            require(min(arr)>=0,'NEGATIVE_COEFFICIENT')
            seen.add(path);coeffs+=len(arr)
            row=finite_corners(arr,zero_lo,one_hi)
            totals=[a+b for a,b in zip(totals,row)]
            if all(zero_lo) and control is None:
                altered=list(arr);altered[0]=0
                require(min(altered)>=0,'BOUNDARY_MUTATION_NONNEGATIVE')
                try:finite_corners(altered,zero_lo,one_hi)
                except ValueError as err:
                    require(str(err)=='NONPOSITIVE_FINITE_CORNER','WRONG_MUTATION_REASON');control=str(err)
                else:raise ValueError('BOUNDARY_MUTATION_ACCEPTED')
            continue
        require(path in prefixes,'UNKNOWN_PREFIX')
        axis=len(path)%6;left,right=base['split'](arr,axis)
        lhi=list(one_hi);lhi[axis]=False
        rlo=list(zero_lo);rlo[axis]=False
        stack.append((path+'0',left,zero_lo,tuple(lhi)))
        stack.append((path+'1',right,tuple(rlo),one_hi))
    require(seen==leaves and control is not None,'INCOMPLETE_AUDIT')
    return {'leaves':len(seen),'coefficients':coeffs,'finite_corners':sum(totals),'corners_by_zero_count':totals,'zero_face_mutation_rejected':control}
q,h=base['polynomials']()
require(base['digest_poly'](q)==cert['Q_coefficients_sha256'] and base['digest_poly'](h)==cert['H_coefficients_sha256'],'POLYNOMIAL_DIGEST')
qr=audit(q,cert['Q_positive_compactified_binary_leaf_paths'])
hr=audit(h,cert['H_positive_compactified_binary_leaf_paths'])
require(qr['leaves']==5332 and hr['leaves']==5334,'EXPECTED_LEAVES')
require(qr['finite_corners']==289883 and hr['finite_corners']==236463,'EXPECTED_FINITE_CORNERS')
def value(poly,u):return sum(c*math.prod(F(x)**a for x,a in zip(u,e)) for e,c in poly.items())
positive=[]
for u in ((0,)*6,(0,1,0,2,0,3)):
    vals=[value(p,u) for p in (q,h)];require(all(v>0 for v in vals),'BOUNDARY_POSITIVE_CONTROL')
    positive.append({'rates':u,'Q':str(vals[0]),'H':str(vals[1])})
result={'kind':'PARENT_REUSED_F129_ENGINE_FINITE_ZERO_FACE_EXTENSION','engine':str(SOURCE),'engine_sha256':SOURCE_SHA,'wrapper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'certificate_sha256':base['CERT_SHA'],'started_native_clock':start,'finished_native_clock_before_receipt':clock(),'Q':qr,'H':hr,'positive_boundary_controls':positive,'limits':'Exact complete nonnegative-coefficient and finite-corner audit; reuses the previously independent parent polynomial/split engine, not a new third implementation. Universal corner-weight inference, spectral symmetrization, PH caller and novelty are separate written obligations.'}
with OUT.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'result':'PASS','path':str(OUT),'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'clock':result['finished_native_clock_before_receipt'],'leaves':qr['leaves']+hr['leaves'],'coefficients':qr['coefficients']+hr['coefficients'],'finite_corners':qr['finite_corners']+hr['finite_corners']}))
