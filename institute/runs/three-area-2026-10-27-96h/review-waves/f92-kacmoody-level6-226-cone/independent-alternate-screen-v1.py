#!/usr/bin/env python3
"""Independent replay of the first 400 one-row replacement axis screens."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json
HERE=Path(__file__).resolve().parent
SRC=Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody')
alt=SRC/'frontier-20261028-level6-free-22-alternate-v1.json'
assert hashlib.sha256(alt.read_bytes()).hexdigest()=='5c6a7888c784f5408405a1ef386bfc32d69770e46544d0b1bd5b9427f036726b'
source=HERE/'independent-exact-check-v1.py'
text=source.read_text(); marker="\nout={'degree'"
assert text.count(marker)==1
ns={'__file__':str(source)}
exec(compile(text.split(marker,1)[0],str(source),'exec'),ns)
images=[[ns['d3'](v,r,s) for v in ns['vectors']] for r,s in ((6,6),(7,6),(6,7))]
words=sorted(set().union(*(set(v) for sample in images for v in sample)))
selected=ns['rows']; candidates=[w for w in words if w not in set(selected)]
assert len(words)==235 and len(candidates)==201
trials=[(slot,w) for slot in range(34) for w in candidates][:400]

def invdet(A):
    n=len(A); aug=[list(map(F,row))+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]; determinant=F(1)
    for j in range(n):
        ii=next((i for i in range(j,n) if aug[i][j]),None)
        if ii is None: return None,F(0)
        if ii!=j: aug[j],aug[ii]=aug[ii],aug[j];determinant=-determinant
        pivot=aug[j][j];determinant*=pivot;aug[j]=[v/pivot for v in aug[j]]
        for i in range(n):
            if i!=j and aug[i][j]:
                q=aug[i][j];aug[i]=[x-q*y for x,y in zip(aug[i],aug[j])]
    return [row[n:] for row in aug],determinant

def axis_cofactors(axis):
    cof=[]
    other=ns['X'] if axis=='x' else ns['Y']
    for t in range(35):
        mat=[[ns['A'][i][j]+t*(other[i][j]-ns['A'][i][j]) for j in range(34)] for i in range(34)]
        inv,det=invdet(mat);assert det
        cof.append([[det*inv[j][slot] for j in range(34)] for slot in (0,1)])
    return cof

def ordinary_coefficients(values):
    delta=list(values); poly=[F(0)]*len(values); basis=[F(1)]
    for k in range(len(values)):
        for j,b in enumerate(basis): poly[j]+=delta[0]*b
        delta=[delta[i+1]-delta[i] for i in range(len(delta)-1)]
        nxt=[F(0)]*(len(basis)+1)
        for j,b in enumerate(basis): nxt[j]-=F(k,k+1)*b;nxt[j+1]+=b/F(k+1)
        basis=nxt
    return poly

def axis_values(word,slot,axis,cof):
    sample=1 if axis=='x' else 2
    vals=[]
    for t in range(35):
        row=[F(images[0][j].get(word,0))+t*(F(images[sample][j].get(word,0))-F(images[0][j].get(word,0))) for j in range(34)]
        vals.append(sum(row[j]*cof[t][slot][j] for j in range(34)))
    return vals
xcof=axis_cofactors('x'); ycof=axis_cofactors('y')
zero=xreject=yreject=0; survivors=[]
for n,(slot,w) in enumerate(trials):
    xv=axis_values(w,slot,'x',xcof); c0=xv[0]
    if not c0: zero+=1;continue
    if any(c0*c<0 for c in ordinary_coefficients(xv)): xreject+=1;continue
    yv=axis_values(w,slot,'y',ycof);assert yv[0]==c0
    if any(c0*c<0 for c in ordinary_coefficients(yv)): yreject+=1;continue
    survivors.append((n,slot,w))
assert (zero,xreject,yreject,len(survivors))==(174,213,13,0)
claimed=json.loads(alt.read_text());assert claimed['attempts']==400 and claimed['axis_survivors']==0 and not claimed['all_one_row_candidates_exhausted']
result={'full_target_tensor_words':len(words),'candidate_replacement_words':len(candidates),
        'attempts':len(trials),'attempt_order':'selected slot first, then lexical replacement word',
        'first_slot_attempts':201,'second_slot_attempts':199,
        'zero_constant_rejected':zero,'x_axis_mixed_rejected':xreject,'y_axis_mixed_rejected':yreject,
        'axis_survivors':len(survivors),'search_exhaustive':False,
        'own_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'alternate_receipt_sha256':hashlib.sha256(alt.read_bytes()).hexdigest(),
        'method':'own Jacobi target rows, exact cofactor row replacement and Newton interpolation at 35 points per axis'}
with (HERE/'independent-alternate-screen-v1.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result,indent=2),flush=True)
