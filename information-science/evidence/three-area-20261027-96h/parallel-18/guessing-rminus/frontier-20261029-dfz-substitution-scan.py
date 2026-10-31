#!/usr/bin/env python3
"""Exact scan of published four-variable non-Shannon inequalities at the base h*.

Usage: python3 script.py OUT.json
Every published inequality of Dougherty-Freiling-Zeger (arXiv:1104.3602,
source pinned below) of the form
  a I(A;B) <= b I(A;B|C)+c I(A;C|B)+d I(B;C|A)+e I(A;B|D)+f I(A;D|B)+g I(B;D|A)
            +h I(C;D)+i I(C;D|A)
is evaluated at the fixed 1847/276 base profile h* for EVERY assignment of the
ten original variables to roles A,B,C,D (nonempty), Z (conditioning, possibly
empty) or unused. Conditioning on Z and substituting disjoint unions are valid
for entropic vectors. All values are exact integers after scaling h* by 25944
(float64 matrix products are exact at these magnitudes; integrality and range
are asserted). A negative value is a violated valid inequality instance, i.e.
an exact separator of h*.
"""
from hashlib import sha256
from fractions import Fraction
from pathlib import Path
import json,re,sys,time
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
TEX=('frontier-20261029-dfz-source/src/nonShannon.tex',None)
SCALE=25944

def load():
    raw=(ROOT/BASE[0]).read_bytes()
    if sha256(raw).hexdigest()!=BASE[1]:raise ValueError('BASE_HASH')
    pt=json.loads(raw);H=np.zeros(1024,dtype=np.int64);seen=0
    for x in pt['primal_values']:
        if set(x['entropy_variables'])<=set('abcdefghij'):
            m=sum(1<<'abcdefghij'.index(v) for v in x['entropy_variables']);q=Fraction(x['value'])*SCALE
            if q.denominator!=1:raise ValueError('SCALE')
            H[m]=int(q);seen+=1
    if seen!=1023:raise ValueError('BASE_COUNT')
    return H

def coefficients(texraw):
    lines=texraw.decode('utf-8').split('\n')
    s=next(i for i,l in enumerate(lines) if 'label{FourCopies}' in l);e=next(i for i,l in enumerate(lines) if 'label{infinite}' in l)
    out={}
    for l in lines[s:e]:
        m=re.match(r'\s*\\item\s+((?:\d+\s+){9})',l)
        if m:out.setdefault(tuple(int(x) for x in m.group(1).split()),'four-copy list')
    for l in lines:
        m=re.match(r'\s*&&\((\d+)&,&(\d+)&,&(\d+)&,&(\d+)&,&(\d+)&,&(\d+)&,&(\d+)&,&(\d+)&,&(\d+)\)&&&&&?\s*(?:\\hspace\{-10pt\})?\\label\{([^}]*)\}',l)
        if m:out.setdefault(tuple(int(x) for x in m.groups()[:9]),m.group(10))
    out.setdefault((1,2,1,1,1,0,0,1,0),'Zhang-Yeung (DFZ form)')
    return out

def main():
    t0=time.monotonic();H=load();texraw=(ROOT/TEX[0]).read_bytes();texsha=sha256(texraw).hexdigest()
    coeff=coefficients(texraw);keys=sorted(coeff);W=np.array([[-k[0]]+list(k[1:]) for k in keys],dtype=np.float64).T
    ingleton=np.array([-1,1,0,0,1,0,0,1,0],dtype=np.float64)
    # trailing 8 vertices (v=2..9 zero-based) role masks
    n=8;idx=np.arange(6**n,dtype=np.int64);digs=np.stack([(idx//6**k)%6 for k in range(n)],axis=1)
    tail=[sum(((digs[:,k]==r).astype(np.int64)<<(k+2)) for k in range(n)) for r in range(6)]
    best=np.full(len(keys),np.inf);arg=[None]*len(keys);ing_best=np.inf;ing_arg=None;count=0
    for d0 in range(6):
        for d1 in range(6):
            m=[tail[r]+((1 if d0==r else 0)<<0)+((1 if d1==r else 0)<<1) for r in range(6)]
            A,B,C,D,Z=m[1],m[2],m[3],m[4],m[5]
            ok=(A>0)&(B>0)&(C>0)&(D>0);A,B,C,D,Z=A[ok],B[ok],C[ok],D[ok],Z[ok];count+=int(ok.sum())
            h=lambda x:H[x]
            hZ=h(Z);hAZ=h(A|Z);hBZ=h(B|Z);hCZ=h(C|Z);hDZ=h(D|Z);hABZ=h(A|B|Z);hACZ=h(A|C|Z);hBCZ=h(B|C|Z)
            hADZ=h(A|D|Z);hBDZ=h(B|D|Z);hCDZ=h(C|D|Z);hABCZ=h(A|B|C|Z);hABDZ=h(A|B|D|Z);hACDZ=h(A|C|D|Z)
            MI=np.stack([hAZ+hBZ-hABZ-hZ,hACZ+hBCZ-hABCZ-hCZ,hABZ+hBCZ-hABCZ-hBZ,hABZ+hACZ-hABCZ-hAZ,
                         hADZ+hBDZ-hABDZ-hDZ,hABZ+hBDZ-hABDZ-hBZ,hABZ+hADZ-hABDZ-hAZ,hCZ+hDZ-hCDZ-hZ,hACZ+hADZ-hACDZ-hAZ],axis=1)
            if MI.min()<0 or MI.max()>10*SCALE:raise ValueError('MI_RANGE')
            MF=MI.astype(np.float64)
            vi=MF@ingleton;j=int(np.argmin(vi))
            if vi[j]<ing_best:ing_best=float(vi[j]);ing_arg=(int(A[j]),int(B[j]),int(C[j]),int(D[j]),int(Z[j]))
            for s in range(0,len(MF),400000):
                V=MF[s:s+400000]@W;mins=V.min(axis=0);am=V.argmin(axis=0)
                for k in np.nonzero(mins<best)[0]:
                    best[k]=mins[k];r=s+int(am[k]);arg[k]=(int(A[r]),int(B[r]),int(C[r]),int(D[r]),int(Z[r]))
    def roles(t):return {n:[v+1 for v in range(10) if t[i]>>v&1] for i,n in enumerate('ABCDZ')}
    viol=[{'coefficients':list(k),'source':coeff[k],'min_scaled':int(best[i]),'min_value':str(Fraction(int(best[i]),SCALE)),'argmin':roles(arg[i])}
          for i,k in enumerate(keys) if best[i]<0]
    out={'base_sha256':BASE[1],'tex_sha256':texsha,'inequalities':len(keys),'assignments_checked':count,
         'violations':sorted(viol,key=lambda x:x['min_scaled']),
         'least_slack':sorted([{'coefficients':list(k),'source':coeff[k],'min_scaled':int(best[i]),'argmin':roles(arg[i])} for i,k in enumerate(keys)],key=lambda x:x['min_scaled'])[:15],
         'ingleton_min_scaled':int(ing_best),'ingleton_argmin':roles(ing_arg),'elapsed_s':time.monotonic()-t0,
         'limits':'Validity of each listed inequality is imported from the published DFZ theorems; conditional/union substitution is standard. A violation separates only this base point; it is not by itself an improved guessing-number bound.'}
    with open(ROOT/sys.argv[1],'x',encoding='utf-8') as f:json.dump(out,f,indent=1);f.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='least_slack'},indent=1)[:4000])

if __name__=='__main__':main()
