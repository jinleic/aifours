#!/usr/bin/env python3
# Independent exact checks; no author code is imported.
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json, hashlib

class Q:
    __slots__=('r','i')
    def __init__(self,r=0,i=0):
        if isinstance(r,Q): self.r,self.i=r.r,r.i
        else: self.r,self.i=F(r),F(i)
    def __add__(self,v):
        v=Q(v); return Q(self.r+v.r,self.i+v.i)
    __radd__=__add__
    def __neg__(self): return Q(-self.r,-self.i)
    def __sub__(self,v): return self+-Q(v)
    def __rsub__(self,v): return Q(v)+-self
    def __mul__(self,v):
        v=Q(v); return Q(self.r*v.r-self.i*v.i,self.r*v.i+self.i*v.r)
    __rmul__=__mul__
    def __truediv__(self,v):
        v=Q(v); d=v.r*v.r+v.i*v.i
        if not d: raise ZeroDivisionError
        t=self*v.conj(); return Q(t.r/d,t.i/d)
    def __eq__(self,v):
        v=Q(v); return self.r==v.r and self.i==v.i
    def conj(self): return Q(self.r,-self.i)
    def abs2(self): return self.r*self.r+self.i*self.i
    def __str__(self): return str(self.r) if self.i==0 else f'({self.r},{self.i})'

def vec(n,terms):
    out=[Q() for _ in range(n)]
    for index,value in terms: out[index]=out[index]+value
    return out

def vcomb(*terms):
    n=len(terms[0][1]); out=[Q() for _ in range(n)]
    for coefficient,v in terms:
        for j,x in enumerate(v): out[j]=out[j]+Q(coefficient)*x
    return out

def zero(n): return [[Q() for _ in range(n)] for _ in range(n)]
def addcross(M,v,w,coefficient=1):
    coefficient=Q(coefficient)
    for i,a in enumerate(v):
        if a==0: continue
        for j,b in enumerate(w):
            if b!=0: M[i][j]=M[i][j]+coefficient*a*b.conj()
def outer(M,v,coefficient=1): addcross(M,v,v,coefficient)
def state(vectors,weights):
    M=zero(len(vectors[0]))
    for v,w in zip(vectors,weights): outer(M,v,w)
    return M

def pt(M,m,n):
    return [[M[(i//n)*n+j%n][(j//n)*n+i%n] for j in range(m*n)] for i in range(m*n)]
def psd(M):
    n=len(M); a=[r[:] for r in M]
    assert all(a[i][j]==a[j][i].conj() for i in range(n) for j in range(n))
    remaining=list(range(n)); piv=[]
    while remaining:
        if any(a[i][i].i!=0 for i in remaining): raise ValueError('non-real diagonal')
        if any(a[i][i].r<0 for i in remaining): return False,piv,'negative diagonal after Schur'
        good=[i for i in remaining if a[i][i].r>0]
        if not good:
            if any(a[i][j]!=0 for i in remaining for j in remaining): return False,piv,'nonzero zero-diagonal block'
            return True,piv,'zero residual'
        k=good[0]; pivot=a[k][k].r; piv.append(pivot); remaining.remove(k)
        for i in remaining:
            for j in remaining: a[i][j]=a[i][j]-a[i][k]*a[k][j]/pivot
    return True,piv,'positive definite'

def det3(M,rs,cs):
    a,b,c=rs; x,y,z=cs
    return M[a][x]*(M[b][y]*M[c][z]-M[b][z]*M[c][y])-M[a][y]*(M[b][x]*M[c][z]-M[b][z]*M[c][x])+M[a][z]*(M[b][x]*M[c][y]-M[b][y]*M[c][x])
def rank2(v,m,n):
    M=[v[n*i:n*(i+1)] for i in range(m)]
    return all(det3(M,rs,cs)==0 for rs in combinations(range(m),3) for cs in combinations(range(n),3))
def trace(M): return sum((M[i][i].r for i in range(len(M))),F())
def gram(w,updates):
    H=zero(len(w))
    for i,x in enumerate(w): H[i][i]=Q(x)
    for coefficient,t in updates: addcross(H,t,t,-coefficient)
    return H
def addgram(M,gens,H):
    for i,v in enumerate(gens):
        for j,w in enumerate(gens): addcross(M,v,w,H[i][j])
def pivstr(p): return [str(x) for x in p]
roots=[Q(1),Q(0,1),Q(-1),Q(0,-1)]

# Four-by-five generators, independently written from the definition.
grid45=[[(0,0,1),(1,1,1),(2,2,1)],[(0,1,1),(1,2,1)],[(1,0,1),(2,1,-1)],[(0,2,1),(3,4,1)],[(2,0,1),(3,3,1)],[(2,3,1)],[(3,0,1)],[(3,2,1)],[(0,4,1)]]
def full45(g): return vec(20,[(5*a+b,c) for a,b,c in g])
def project45(g,v0,v2):
    terms=[]
    for a,b,c in g:
        if b<3: terms.append((4*a+b,c))
        elif b==3: terms += [(4*a,c*v0),(4*a+2,c*v2)]
        else: terms.append((4*a+3,c))
    return vec(16,terms)
def exact45(name,w,v0,v2,ra,rb,p=None,s_given=None):
    w=list(map(F,w)); alpha,beta,delta,gamma,epsilon,phi,eta,iota,kappa=w
    v0=Q(v0);v2=Q(v2); U=v0.abs2();V=v2.abs2(); k=F(ra**3,rb**2)
    assert alpha==ra*ra and beta==rb*rb and delta>=alpha*alpha/beta
    source=state([full45(g) for g in grid45],w)
    vs=[project45(g,v0,v2) for g in grid45]
    A,B,D,C,E,T,G,I,H=vs; X=vcomb((1,E),(-v0,G),(-v2,I))
    assert X==vec(16,[(8,1)])
    target=state(vs,w); ptres=psd(pt(target,4,4)); srcpt=psd(pt(source,4,5))
    Cw=1/epsilon+U/eta+V/iota
    s=Q(-Cw*phi*k)*v0.conj()/(1+Cw*phi*U) if s_given is None else Q(s_given)
    W=vcomb((-k,X),(s,T),(-s*v0,X))
    t1=[-(Q(k)+s*v0),(Q(k)+s*v0)*v0,(Q(k)+s*v0)*v2,s]
    assert W==vcomb(*list(zip(t1,[E,G,I,T])))
    H1=gram([epsilon,eta,iota,phi],[(1,t1)])
    first=[]
    for z in roots:
        q=vcomb((Q(ra)*z,A),(rb,B),(Q(alpha/rb)*z*z,D),(z*z*z,W))
        assert rank2(q,4,4); first.append(q)
    m1=zero(16)
    for q in first: outer(m1,q,F(1,4))
    for coefficient,v in [(delta-alpha*alpha/beta,D),(gamma,C),(kappa,H)]: outer(m1,v,coefficient)
    addgram(m1,[E,G,I,T],H1); assert m1==target
    cost1=sum((t.abs2()/d for t,d in zip(t1,[epsilon,eta,iota,phi])),F())
    chk={'name':name,'source_trace':str(trace(source)),'source_pt':srcpt[0],'source_pt_pivots':pivstr(srcpt[1]),'output_trace':str(trace(target)),'output_pt':ptres[0],'output_pt_pivots':pivstr(ptres[1]),'U':str(U),'V':str(V),'s':str(s),'cost1':str(cost1),'gram1_psd':psd(H1)[0],'gram1_pivots':pivstr(psd(H1)[1]),'first_phase_minors_and_256_entries':'exact'}
    if V:
        Z=vec(16,[(10,1)])
        t2=[-v0/v2,v0*v0/v2,v0,Q(1)/v2]
        assert Z==vcomb(*list(zip(t2,[E,G,I,T])))
        H2=gram([epsilon,eta,iota,phi],[(alpha,t2)])
        q0=vcomb((ra,A),(-ra,Z)); assert rank2(q0,4,4)
        second=[]
        for z in roots:
            q=vcomb((Q(ra)*z,A),(Q(ra)*z,Z),(Q(1,1)*rb*z*z,B),(Q(1,-1)*(alpha/rb),D))
            assert rank2(q,4,4);second.append(q)
        m2=zero(16);outer(m2,q0,F(1,2))
        for q in second:outer(m2,q,F(1,8))
        for coefficient,v in [(delta-alpha*alpha/beta,D),(gamma,C),(kappa,H)]:outer(m2,v,coefficient)
        addgram(m2,[E,G,I,T],H2);assert m2==target
        cost2=alpha*sum((t.abs2()/d for t,d in zip(t2,[epsilon,eta,iota,phi])),F())
        chk.update({'cost2':str(cost2),'gram2_psd':psd(H2)[0],'gram2_pivots':pivstr(psd(H2)[1]),'second_phase_minors_and_256_entries':'exact'})
        if p is not None:
            p=F(p); assert 0<=p<=1
            HM=gram([epsilon,eta,iota,phi],[(p,t1),((1-p)*alpha,t2)])
            mix=zero(16)
            for q in first:outer(mix,q,p/4)
            outer(mix,q0,(1-p)/2)
            for q in second:outer(mix,q,(1-p)/8)
            for coefficient,v in [(delta-alpha*alpha/beta,D),(gamma,C),(kappa,H)]:outer(mix,v,coefficient)
            addgram(mix,[E,G,I,T],HM); assert mix==target
            inner=sum((t1[j].conj()*t2[j]/d for j,d in enumerate([epsilon,eta,iota,phi])),Q())
            xi=alpha*inner.abs2(); a1=1-p*cost1; a2=1-(1-p)*cost2; determinant=a1*a2-p*(1-p)*xi
            by2=a1>=0 and a2>=0 and determinant>=0
            assert by2==psd(HM)[0]
            chk.update({'mix_p':str(p),'mixed_psd':by2,'mixed_pivots':pivstr(psd(HM)[1]),'2x2_principals':[str(a1),str(a2),str(determinant)],'mixed_256_entries':'exact'})
    return chk

W1=(1,1,2,3,9,9,9,6,7)
W2=(1,1,2,3,9,9,9,F(1,10),100)
walt=(4,4,4,3,8,16,4,8,2)
r45=[exact45('author entire plane',W1,F(1,2),4,1,1,F(1,2)),
     exact45('own complex',W1,Q(F(1,2),F(1,3)),Q(4,F(1,2)),1,1,F(1,3)),
     exact45('own V=0 boundary',W1,Q(F(1,2),F(1,3)),0,1,1),
     exact45('own nonunit alpha beta',walt,Q(F(1,2),F(1,4)),Q(4,F(1,3)),2,2,F(2,5)),
     exact45('author mixture',W2,0,F(8,25),1,1,F(1,2),0),
     exact45('own complex mixture',W2,0,Q(F(1,4),F(1,4)),1,1,F(1,3),0)]
assert r45[0]['source_trace']=='64' and r45[0]['source_pt'] and r45[0]['output_pt']
assert r45[0]['cost1']=='404/1053' and r45[0]['cost2']=='13/256'
assert r45[4]['source_trace']=='1511/10' and r45[4]['source_pt'] and r45[4]['output_pt']
assert r45[4]['cost1']=='1277/1125' and r45[4]['cost2']=='625/576'
assert not r45[4]['gram1_psd'] and not r45[4]['gram2_psd'] and r45[4]['mixed_psd']
assert r45[4]['mixed_pivots']==['17/2','9','973/21250','527/128']
assert all(x['gram1_psd'] for x in r45[:4]) and all(x['mixed_psd'] for x in (r45[0],r45[1],r45[3],r45[5]))

# Five-by-five grid; edge weights order A,V,W,B,C,Q,00,14,23,32,41.
grid55=[[(0,2),(1,1),(2,0)],[(0,1)],[(1,0)],[(1,2),(3,4)],[(2,1),(4,3)],[(2,2),(3,3)],[(0,0)],[(1,4)],[(2,3)],[(3,2)],[(4,1)]]
def cut55(g,rows,cols):
    return vec(len(rows)*len(cols),[(len(cols)*rows.index(a)+cols.index(b),1) for a,b in g if a in rows and b in cols])
def decomposition55(vs,w,side,ra,rb,ra0,rb0,rd0):
    m=5-(ra is not None); n=5-(rb is not None)
    alpha,beta,delta,b,c=w[:5]; chosen=None
    if alpha and (ra is None or ra>=3) and (rb is None or rb>=3):
        # one-side or two-side hard cut
        useB=(ra==3 and rb!=3) or (rb==4 and ra!=4)
        if useB: chosen=(1,3,rb0,beta,b)
        else: chosen=(2,4,rd0,delta,c)
    out=[]; excluded=set()
    if chosen:
        loop,edge,root_loop,loopweight,edgeweight=chosen
        if not loopweight or edgeweight*loopweight<alpha*alpha: return None
        assert root_loop*root_loop==loopweight and ra0*ra0==alpha
        for z in roots:
            q=vcomb((ra0,vs[0]),(Q(root_loop)*z,vs[loop]),(Q(alpha/root_loop)*z.conj(),vs[edge]))
            assert rank2(q,m,n);out.append((F(1,4),q))
        out.append((edgeweight-alpha*alpha/loopweight,vs[edge]));excluded={0,loop,edge}
    for i,v in enumerate(vs):
        if i not in excluded and w[i]!=0: assert rank2(v,m,n);out.append((w[i],v))
    return out

def apply_opposite(v,m,n,side):
    # 4x5 -> 4x4 on Bob or 5x4 -> 4x4 on Alice. Map e4 to a genuinely complex vector.
    h=[Q(F(1,2),1),Q(F(1,3)),Q(0,F(1,4)),Q(F(-1,2))]
    out=[Q() for _ in range(16)]
    for a in range(m):
        for b in range(n):
            val=v[a*n+b]
            if side=='alice':
                if b<4: out[4*a+b]=out[4*a+b]+val
                else:
                    for j in range(4):out[4*a+j]=out[4*a+j]+val*h[j]
            else:
                if a<4: out[4*a+b]=out[4*a+b]+val
                else:
                    for j in range(4):out[4*j+b]=out[4*j+b]+val*h[j]
    return out

def check55(name,w,roots3,need_opposite=False):
    w=list(map(F,w)); ra0,rb0,rd0=roots3
    source=state([cut55(g,list(range(5)),list(range(5))) for g in grid55],w)
    sp=psd(pt(source,5,5)); count={'name':name,'source_trace':str(trace(source)),'source_pt':sp[0],'source_pt_pivots':pivstr(sp[1]),'ppt_cuts':0,'hard_ppt_cuts':0,'cut_decompositions':0,'one_side_ppt':0,'one_side_decompositions':0,'complex_opposite_checks':0,'zero_cuts':0}
    for ra,rb in product(range(5),repeat=2):
        rows=[x for x in range(5) if x!=ra];cols=[x for x in range(5) if x!=rb]
        vs=[cut55(g,rows,cols) for g in grid55];target=state(vs,w);ppt=psd(pt(target,4,4))[0]
        count['ppt_cuts']+=int(ppt);count['zero_cuts']+=int(trace(target)==0)
        if ra>=3 and rb>=3 and ppt:count['hard_ppt_cuts']+=1
        dec=decomposition55(vs,w,'both',ra,rb,ra0,rb0,rd0)
        if ppt: assert dec is not None
        if dec is not None:
            result=zero(16)
            for coefficient,q in dec:
                assert coefficient>=0 and rank2(q,4,4);outer(result,q,coefficient)
            assert result==target;count['cut_decompositions']+=1
    for side,k in product(('alice','bob'),range(5)):
        ra=k if side=='alice' else None;rb=k if side=='bob' else None
        rows=[x for x in range(5) if x!=ra];cols=[x for x in range(5) if x!=rb]
        m,n=len(rows),len(cols); vs=[cut55(g,rows,cols) for g in grid55];target=state(vs,w);ppt=psd(pt(target,m,n))[0]
        count['one_side_ppt']+=int(ppt)
        dec=decomposition55(vs,w,side,ra,rb,ra0,rb0,rd0)
        if sp[0]: assert dec is not None and ppt
        if dec is not None:
            result=zero(20)
            for coefficient,q in dec:
                assert coefficient>=0 and rank2(q,m,n);outer(result,q,coefficient)
            assert result==target; count['one_side_decompositions']+=1
            if need_opposite and k in (3,4):
                tv=[apply_opposite(v,m,n,side) for v in vs];newtarget=state(tv,w); out=zero(16)
                for coefficient,q in dec:
                    pq=apply_opposite(q,m,n,side);assert rank2(pq,4,4);outer(out,pq,coefficient)
                assert out==newtarget
                if ppt: assert psd(pt(newtarget,4,4))[0]
                count['complex_opposite_checks']+=1
    return count

orig=(1,1,1,1,1,1,1,1,2,2,1)
weighted=(1,4,4,1,1,1,1,1,2,2,1)
custom=(4,9,16,4,4,4,4,4,8,8,4)
nonppt=(1,1,1,100,1,1,1,1,2,2,1)
zero_case=(0,0,0,0,0,0,1,0,0,0,0)
r55=[check55('paper trace18',orig,(1,1,1)),check55('author trace24',weighted,(1,2,2),True),check55('own rational weight profile',custom,(2,3,4),True),check55('own NPT source, PPT cuts',nonppt,(1,1,1)),check55('own zero-output boundary',zero_case,(0,0,0))]
assert [x['source_trace'] for x in r55]==['18','24','89','216','1']
assert all(x['source_pt'] and x['ppt_cuts']==25 and x['one_side_ppt']==10 for x in r55[:3])
assert not r55[3]['source_pt'] and r55[3]['ppt_cuts']>0 and r55[3]['hard_ppt_cuts']>0
assert r55[4]['zero_cuts']>0

# Sparse polynomial algebra verifies both source-range implications without reading author code.
N=11
Zp={}
def atom(i):
    e=[0]*N;e[i]=1;return {tuple(e):1}
def addp(a,b):
    c=a.copy()
    for k,v in b.items():
        c[k]=c.get(k,0)+v
        if not c[k]: del c[k]
    return c
def negp(a):return {k:-v for k,v in a.items()}
def subp(a,b):return addp(a,negp(b))
def mulp(a,b):
    c={}
    for x,p in a.items():
        for y,q in b.items():
            z=tuple(i+j for i,j in zip(x,y));c[z]=c.get(z,0)+p*q
    return {k:v for k,v in c.items() if v}
def scale(a,v):return {k:v*x for k,x in a.items() if v*x}
def power(a,n):
    out={(0,)*N:1}
    for _ in range(n):out=mulp(out,a)
    return out
def dp(M,r,c):
    i,j,k=r;x,y,z=c
    return addp(subp(mulp(M[i][x],subp(mulp(M[j][y],M[k][z]),mulp(M[j][z],M[k][y]))),mulp(M[i][y],subp(mulp(M[j][x],M[k][z]),mulp(M[j][z],M[k][x])))),mulp(M[i][z],subp(mulp(M[j][x],M[k][y]),mulp(M[j][y],M[k][x]))))
def minors(M):return [dp(M,r,c) for r in combinations(range(len(M)),3) for c in combinations(range(len(M[0])),3)]
def isminor(p,ms):return p in ms or negp(p) in ms
def setzero(p,*inds):return {k:v for k,v in p.items() if all(k[i]==0 for i in inds)}
a,b,c,d,e,f,g,i,h=map(atom,range(9))
M45=[[a,b,c,Zp,h],[d,a,b,Zp,Zp],[e,negp(d),a,f,Zp],[g,Zp,i,e,c]]
g1=mulp(e,subp(power(a,2),mulp(b,d)));g2=mulp(c,addp(power(a,2),mulp(b,d)))
g3=mulp(e,subp(power(b,2),mulp(a,c)));g4=negp(mulp(c,addp(power(d,2),mulp(a,e))))
g5=subp(subp(addp(power(a,3),mulp(power(b,2),e)),mulp(power(d,2),c)),mulp(mulp(a,c),e))
assert all(isminor(x,minors(M45)) for x in [g1,g2,g3,g4,g5])
identity=subp(subp(scale(mulp(a,subp(subp(g5,g3),g4)),2),mulp(c,g1)),mulp(e,g2))
assert identity==scale(power(a,4),2)
# 2024 source range, rename variables a=rank3, b/c=two edges.
u,v,a,w,b,x,c,q,y,z,t=map(atom,range(11))
M55=[[u,v,a,Zp,Zp],[w,a,b,Zp,x],[a,c,q,y,Zp],[Zp,Zp,z,q,b],[Zp,t,Zp,c,Zp]]
ms=minors(M55);assert isminor(mulp(mulp(a,b),c),ms)
ms_b0=[setzero(s,4) for s in ms]
assert isminor(mulp(power(a,2),q),ms_b0) and isminor(mulp(power(a,2),c),ms_b0)
ms_bcq0=[setzero(s,4,6,7) for s in ms]
assert isminor(power(a,3),ms_bcq0)
# Source's stated identity after Eq.12 differs; check a concrete discrepancy independently.
vals={0:1,1:0,2:1,3:0,4:1}
def evaluate(poly,vals):return sum(coef*__import__('functools').reduce(lambda s,item:s*vals.get(item[0],0)**item[1],enumerate(exps),1) for exps,coef in poly.items())
a4,c4=atom(0),atom(2)
source_wrong=subp(subp(mulp(a4,subp(subp(g5,g3),g4)),mulp(c4,g1)),negp(mulp(e,g2)))
assert evaluate(source_wrong,vals)==2 and evaluate(power(a4,4),vals)==1

receipt={'implementation':'independent standard-library Fraction Gaussian-rational arithmetic; no author imports', 'four_by_five':r45,'five_by_five':r55,
'polynomial_range_checks':{'4x5':'all 5 claimed polynomials are actual 3x3 minors up to sign; 2a(g5-g3-g4)-c*g1-e*g2=2a^4 exactly','2025_primary_identity_counterexample':'a,b,c,d,e=(1,0,1,0,1): displayed LHS 2, RHS 1','5x5':'minor abc; b=0 => minors a^2q, a^2c; b=c=q=0 => a^3; a<>0 impossible; b/c cases by transpose symmetry'},
'scope':'point checks are not universal proof; projector decompositions plus independent algebra cover the listed charts only'}
path=Path(__file__).with_name('independent-exact-receipt-v1.json')
with path.open('x') as out:json.dump(receipt,out,indent=2);out.write('\n')
print(json.dumps({'receipt':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'four_by_five':r45,'five_by_five':r55},indent=2))
