#!/usr/bin/env python3
"""Independent exact free-associative/Lie and cone review; no owner code imported."""
import itertools, json, math, hashlib
from fractions import Fraction as Q
from pathlib import Path

HERE=Path(__file__).resolve().parent
SRC=Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody')
pin={'frontier-20261028-level6-free-22-pencil-v1.json':'b3779b89c8a5e67bb0478ac31dae9c96cd2c32f912f8f8c63baa4e8227c6e5bc',
     'frontier-20261028-level6-free-22-leading-cone-v1.json':'83e62aba742dca5899ef6f1e086b41c054cc16ed03bc839900596d690deb0323'}
for f,h in pin.items():
    assert hashlib.sha256((SRC/f).read_bytes()).hexdigest()==h
P=json.loads((SRC/next(iter(pin))).read_text())
C=json.loads((SRC/list(pin)[1]).read_text())
assert P['degree']==[2,2,6]
W=((0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2))

def put(dst,key,value):
    if value:
        dst[key]=dst.get(key,0)+value
        if not dst[key]: del dst[key]

def bracket(a,b):
    out={}
    for x,c in a.items():
        for y,d in b.items():
            put(out,x+y,c*d); put(out,y+x,-c*d)
    return out

def lyndon(w):
    return all(w<w[i:] for i in range(1,len(w)))

cache={}
def word_bracket(w):
    if w in cache: return cache[w]
    if len(w)==1: ans={w:1}
    else:
        k=next(i for i in range(1,len(w)) if lyndon(w[i:]))
        ans=bracket(word_bracket(w[:k]),word_bracket(w[k:]))
    assert ans and min(ans)==w and ans[w]==1
    cache[w]=ans
    return ans

class Span:
    def __init__(self): self.p={}
    def rem(self, vec):
        v={k:Q(x) for k,x in vec.items() if x}
        while v:
            k=min(v)
            if k not in self.p: break
            c=v[k]
            for x,y in self.p[k].items(): put(v,x,-c*y)
        return v
    def add(self,vec):
        v=self.rem(vec)
        if not v: return False
        k=min(v); c=v[k]
        self.p[k]={x:y/c for x,y in v.items()}
        return True

# Enumerate all multidegrees needed for the (2,2,6) component.  Then certify,
# by bracket closure and induction, not just by assuming a Lyndon basis theorem.
groups={}
for n in range(1,7):
    for letters in itertools.product(range(8),repeat=n):
        a=sum(W[i][0] for i in letters); b=sum(W[i][1] for i in letters)
        if a>2 or b>2: continue
        w=''.join(map(str,letters))
        if lyndon(w): groups.setdefault((n,a,b),[]).append(w)
spans={}
for deg,words in groups.items():
    s=Span()
    for w in words: assert s.add(word_bracket(w))
    spans[deg]=s
closure_checks=0
for d1,ws1 in groups.items():
    for d2,ws2 in groups.items():
        if d1>d2: continue
        deg=tuple(x+y for x,y in zip(d1,d2))
        if deg[0]>6 or deg[1]>2 or deg[2]>2: continue
        for w in ws1:
            for u in ws2:
                if d1==d2 and w>=u: continue
                v=bracket(word_bracket(w),word_bracket(u)); closure_checks+=1
                assert (not v) or (deg in spans and not spans[deg].rem(v)),(d1,w,d2,u)
source=groups[(6,2,2)]
assert len(source)==74 and source==P['source_words']
print('Lie word enumeration, independence and closure:',len(source),closure_checks,flush=True)

# Reconstruct actual adjoint-module action directly from 3x3 matrices.
def mat(vals):
    out=[[0]*3 for _ in range(3)]
    for i,j,v in vals: out[i][j]+=v
    return tuple(tuple(row) for row in out)
def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def comm(a,b):
    x,y=mul(a,b),mul(b,a)
    return tuple(tuple(x[i][j]-y[i][j] for j in range(3)) for i in range(3))
M=[mat([(2,0,1)]),mat([(2,1,-1)]),mat([(1,0,1)]),
   mat([(0,0,1),(2,2,-1)]),mat([(0,0,1),(1,1,-1)]),
   mat([(0,1,-1)]),mat([(1,2,-1)]),mat([(0,2,-2)])]
E1=mat([(0,1,1)]); E2=mat([(1,2,1)]); E12=comm(E1,E2)
F1=mat([(1,0,1)]); F2=mat([(2,1,1)])
def coords(a):
    assert sum(a[i][i] for i in range(3))==0
    v={0:Q(a[2][0]),1:Q(-a[2][1]),2:Q(a[1][0]),3:Q(-a[2][2]),
       4:Q(-a[1][1]),5:Q(-a[0][1]),6:Q(-a[1][2]),7:Q(-a[0][2],2)}
    v={k:q for k,q in v.items() if q}
    assert all(sum(q*M[k][i][j] for k,q in v.items())==a[i][j] for i in range(3) for j in range(3))
    return v
actions=[[coords(comm(g,m)) for m in M] for g in (F1,F2,E1,E2,E12)]
def apply(v,action):
    out={}
    for w,c in v.items():
        for j,ch in enumerate(w):
            for k,q in action[int(ch)].items(): put(out,w[:j]+str(k)+w[j+1:],c*q)
    return out

basis=[word_bracket(w) for w in source]
hcols=[]
for v in basis:
    col={}
    for i in (0,1):
        for w,q in apply(v,actions[i]).items(): col[str(i)+':'+w]=q
    hcols.append(col)
hspan=Span()
for col in hcols: hspan.add(col)
assert len(hspan.p)==40
coeffs=[{int(i):Q(x) for i,x in v.items()} for v in P['horizontal_kernel_coefficients']]
assert len(coeffs)==34
cs=Span()
for co in coeffs:
    assert all(0<=j<74 for j in co) and cs.add({str(i).zfill(2):v for i,v in co.items()})
    h={}
    for i,c in co.items():
        for w,q in hcols[i].items(): put(h,w,c*q)
    assert not h
vectors=[]
for co in coeffs:
    v={}
    for i,c in co.items():
        for w,q in basis[i].items(): put(v,w,c*q)
    vectors.append(v)
print('Horizontal rank and complete lowest-space basis:',len(hspan.p),len(vectors),flush=True)

# f3(m_i) = -h3, -r e1, -s e2, -(r+s)e12, -s e12, 0,0,0.
# For each associative word, move this degree-zero output to the right.
# Its commutators with each later letter give the level-five tensor; all right
# degree-zero coefficients must cancel, providing a separate Jacobi check.
def d3(v,r,s):
    zero={}; out={}
    emit=[('h',-1),('e1',-r),('e2',-s),('e12',-r-s),('e12',-s),None,None,None]
    gmap={'e1':actions[2],'e2':actions[3],'e12':actions[4]}
    for w,c in v.items():
        for j,ch in enumerate(w):
            e=emit[int(ch)]
            if not e or not e[1]: continue
            g,mulc=e; mult=c*mulc
            put(zero,(w[:j]+w[j+1:],g),mult)
            for k in range(j+1,len(w)):
                letter=int(w[k])
                action=({letter:2-r*W[letter][0]-s*W[letter][1]} if g=='h' else gmap[g][letter])
                for q,x in action.items(): put(out,w[:j]+w[j+1:k]+str(q)+w[k+1:],mult*x)
    assert not zero,(r,s,list(zero.items())[:4])
    return out
rows=P['selected_target_words']; assert len(rows)==len(set(rows))==34
samples=[]
for r,s in ((6,6),(7,6),(6,7)):
    imgs=[d3(v,r,s) for v in vectors]
    samples.append([[Q(v.get(w,0)) for v in imgs] for w in rows])
A,X,Y=samples
L=[[X[i][j]+Y[i][j]-2*A[i][j] for j in range(34)] for i in range(34)]
K=[[X[i][j]-Y[i][j] for j in range(34)] for i in range(34)]
E=[[A[i][j]-6*L[i][j] for j in range(34)] for i in range(34)]
for i in range(34):
    for j in range(34):
        assert [A[i][j],X[i][j]-A[i][j],Y[i][j]-A[i][j]]==list(map(Q,P['matrix'][i][j]))
        assert [L[i][j],K[i][j],E[i][j]]==list(map(Q,C['matrix_entries'][i][j]))
print('All 1156 independently rebuilt affine pencil entries match',flush=True)

def determinant(a):
    m=[row[:] for row in a]; n=len(m); sign=1; d=Q(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if m[i][j]),None)
        if pivot is None: return Q(0)
        if pivot!=j: m[j],m[pivot]=m[pivot],m[j]; sign=-sign
        v=m[j][j]; d*=v
        for i in range(j+1,n):
            if m[i][j]:
                f=m[i][j]/v
                for k in range(j+1,n): m[i][k]-=f*m[j][k]
                m[i][j]=0
    return sign*d
D=determinant(L); assert D==Q(-1454389021504438272000)
R=[sum(map(abs,row),Q(0)) for row in L]
assert all(R) and [str(x) for x in R]==C['L_row_sums']
H=34*math.prod(R)/(abs(D)*min(R))
B=max(sum(map(abs,row),Q(0)) for row in K)
G=max(sum(map(abs,row),Q(0)) for row in E)
assert str(H)==C['inverse_bound_H'] and str(B)==C['K_max_row_sum_B'] and str(G)==C['E_max_row_sum_G']
# Confirm cofactor orientation bound independently: inverse row j uses cofactors
# deleting each possible source row, all <= product(R)/min(R).
out={'degree':[2,2,6],'source_count':len(source),'closure_checks':closure_checks,
     'horizontal_rank':len(hspan.p),'lowest_count':len(vectors),'selected_rows':len(rows),
     'reconstructed_pencil_entries':34*34,'det_L':str(D),'row_sums':[str(q) for q in R],
     'row_sum_min':str(min(R)),'product_row_sums':str(math.prod(R)),
     'H':str(H),'B':str(B),'G':str(G),
     'max_K_rows':[i+1 for i,row in enumerate(K) if sum(map(abs,row),Q(0))==B],
     'max_E_rows':[i+1 for i,row in enumerate(E) if sum(map(abs,row),Q(0))==G],
     'input_sha256':pin,'method':'own tensor Lie closure, 3x3 commutators, Jacobi, Fraction Gaussian elimination and cofactor norm'}
with (HERE/'independent-exact-check-v1.json').open('x') as f: json.dump(out,f,indent=2); f.write('\n')
print(json.dumps(out,indent=2),flush=True)
