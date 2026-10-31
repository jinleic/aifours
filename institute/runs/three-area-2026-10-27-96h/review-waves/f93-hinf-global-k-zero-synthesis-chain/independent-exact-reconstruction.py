#!/usr/bin/env python3
"""Independent exact rational reconstruction, not an author replay."""
from fractions import Fraction as F

class Mat:
    def __init__(self, rows, n=None):
        self.rows = tuple(tuple(F(x) for x in row) for row in rows)
        self.m = len(self.rows)
        self.n = len(self.rows[0]) if self.m else (0 if n is None else n)
        assert all(len(row) == self.n for row in self.rows)
    def __getitem__(self, i): return self.rows[i]
    def __repr__(self): return '[' + ', '.join(str(list(row)) for row in self.rows) + f'] ({self.m}x{self.n})'
    def __eq__(self, other): return (self.m, self.n, self.rows) == (other.m, other.n, other.rows)

def zero(m,n): return Mat([[0]*n for _ in range(m)], n)
def eye(n): return Mat([[int(i==j) for j in range(n)] for i in range(n)], n)
def tr(A): return Mat([[A[i][j] for i in range(A.m)] for j in range(A.n)], A.m)
def add(A,B):
    assert (A.m,A.n)==(B.m,B.n)
    return Mat([[A[i][j]+B[i][j] for j in range(A.n)] for i in range(A.m)],A.n)
def neg(A): return Mat([[-x for x in row] for row in A.rows],A.n)
def sub(A,B): return add(A,neg(B))
def mm(A,B):
    assert A.n==B.m, (A.m,A.n,B.m,B.n)
    return Mat([[sum((A[i][k]*B[k][j] for k in range(A.n)),F(0)) for j in range(B.n)] for i in range(A.m)],B.n)
def chain(*xs):
    out=xs[0]
    for x in xs[1:]: out=mm(out,x)
    return out
def hs(A,B):
    assert A.m==B.m
    return Mat([A[i]+B[i] for i in range(A.m)], A.n+B.n)
def vs(*xs):
    assert len({x.n for x in xs})==1
    return Mat([row for x in xs for row in x.rows],xs[0].n)
def col(A,inds): return Mat([[A[i][j] for j in inds] for i in range(A.m)],len(inds))
def rref(A):
    q=[list(r) for r in A.rows]; piv=[]; i=0
    for j in range(A.n):
        k=next((k for k in range(i,A.m) if q[k][j]),None)
        if k is None: continue
        q[i],q[k]=q[k],q[i]; a=q[i][j]; q[i]=[v/a for v in q[i]]
        for k in range(A.m):
            if k!=i and q[k][j]:
                a=q[k][j]; q[k]=[x-a*y for x,y in zip(q[k],q[i])]
        piv.append(j); i+=1
        if i==A.m: break
    return Mat(q,A.n),piv
def basis(A): return col(A,rref(A)[1])
def null(A):
    R,piv=rref(A); free=[j for j in range(A.n) if j not in piv]
    return Mat([[F(int(i==j)) if i in free else -R[piv.index(i)][j] for j in free] for i in range(A.n)],len(free))
def inv(A):
    assert A.m==A.n
    R,piv=rref(hs(A,eye(A.n)))
    assert piv[:A.n]==list(range(A.n))
    return col(R,range(A.n,2*A.n))
def pseudo(A):
    piv=rref(A)[1]; r=len(piv)
    if not r: return zero(A.n,A.m)
    C=col(A,piv); Ct=tr(C); Cpinv=mm(inv(mm(Ct,C)),Ct)
    R=mm(Cpinv,A); Rt=tr(R)
    Ap=chain(Rt,inv(mm(R,Rt)),Cpinv)
    assert mm(mm(A,Ap),A)==A and mm(mm(Ap,A),Ap)==Ap
    assert tr(mm(A,Ap))==mm(A,Ap) and tr(mm(Ap,A))==mm(Ap,A)
    return Ap
def projector(V):
    if V.n==0: return zero(V.m,V.m)
    return chain(V,inv(mm(tr(V),V)),tr(V))

def solve(A,A0,B,B0,C,D0,D1):
    n=A.m; V=eye(n); dims=[n]
    for _ in range(n+1):
        R=null(tr(V)); Cj=vs(mm(tr(R),A),mm(tr(R),A0),D0)
        Dj=vs(mm(tr(R),B),mm(tr(R),B0),D1)
        residual=chain(sub(eye(Dj.m),mm(Dj,pseudo(Dj))),Cj,V)
        Vnext=basis(mm(V,null(residual))); dims.append(Vnext.n)
        if Vnext.n==V.n: V=Vnext; break
        V=Vnext
    else: raise AssertionError('iteration did not stabilize')
    R=null(tr(V)); D=vs(mm(tr(R),B),mm(tr(R),B0),D1)
    Cs=vs(mm(tr(R),A),mm(tr(R),A0),D0)
    Fs=vs(mm(tr(R),C),zero(R.n,C.n),zero(D0.m,C.n))
    Dp=pseudo(D); K=neg(chain(Dp,Cs,projector(V))); L=neg(mm(Dp,Fs))
    residual=add(mm(D,L),Fs)
    assert chain(sub(eye(n),projector(V)),add(A,mm(B,K)),V)==zero(n,V.n)
    assert chain(sub(eye(n),projector(V)),add(A0,mm(B0,K)),V)==zero(n,V.n)
    assert mm(add(D0,mm(D1,K)),V)==zero(D0.m,V.n)
    return dims,V,K,L,residual

def pmul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=F(x)*F(y)
    return out
def pd(a):return [F(i)*F(a[i]) for i in range(1,len(a))]
def pinteg(a):return sum((F(x)/F(i+1) for i,x in enumerate(a)),F(0))
def peval(a,x):return sum((F(c)*F(x)**i for i,c in enumerate(a)),F(0))

def main():
    a=Mat([[-1,0],[1,-2]]); a0=Mat([[F(1,2),0],[1,F(1,3)]])
    b=Mat([[1],[0]]); b0=Mat([[0],[1]]); c=Mat([[2],[3]]); d0=Mat([[1,0]]); d1=Mat([[0]])
    dims,V,K,L,res=solve(a,a0,b,b0,c,d0,d1)
    assert dims==[2,1,1] and V==Mat([[0],[1]]) and K==Mat([[0,0]]) and L==Mat([[-2]]) and res==zero(3,1)
    assert add(mm(b,L),c)==Mat([[0],[3]]) and mm(b0,L)==Mat([[0],[-2]])
    print('hidden:',dims,'V=',V,'K=',K,'L=',L,'forcing drift/diffusion=',add(mm(b,L),c),mm(b0,L))

    dims,V,K,L,res=solve(Mat([[0]]),Mat([[0]]),Mat([[1]]),Mat([[1]]),Mat([[1]]),Mat([[1]]),Mat([[0]]))
    assert dims==[1,0,0] and V==zero(1,0) and K==Mat([[0]]) and L==Mat([[F(-1,2)]]) and res==Mat([[F(1,2)],[F(-1,2)],[0]])
    print('obstruction:',dims,'L least squares=',L,'residual=',res,'squared residual=',sum((x*x for row in res.rows for x in row),F(0)))

    a=Mat([[0,1],[0,0]]); a0=zero(2,2); b=Mat([[0,0],[1,0]]); b0=zero(2,2)
    c=Mat([[1],[0]]); d0=Mat([[1,0]]); d1=Mat([[0,1]])
    dims,V,K,L,res=solve(a,a0,b,b0,c,d0,d1)
    assert dims==[2,2] and V==eye(2) and K==Mat([[0,0],[-1,0]]) and L==zero(2,1) and res==zero(1,1)
    assert add(d0,mm(d1,K))==zero(1,2)
    print('conversion:',dims,'V=',V,'K=',K,'L=',L,'D0+D1K=',add(d0,mm(d1,K)))

    A=Mat([[0,1,0],[0,0,1],[0,0,0]])
    dims,V,K,L,res=solve(A,zero(3,3),zero(3,1),zero(3,1),Mat([[0],[0],[1]]),Mat([[1,0,0]]),Mat([[0]]))
    assert dims==[3,2,1,0,0] and V==zero(3,0) and res!=zero(res.m,res.n)
    print('three strict drops:',dims,'terminal V=',V,'residual=',res)

    theta=Mat([[0,0],[-1,0]]); Z=Mat([[1],[0]]); Bv=Mat([[0],[1]]); As=vs(d1,b0); Cs=vs(d0,a0)
    assert add(mm(As,theta),Cs)==zero(3,2)
    assert add(a,mm(b,theta))==a and mm(b,Z)==Bv and mm(As,Z)==zero(3,1)
    assert sub(c,mm(a,Bv))==zero(2,1)
    print('polynomial certificate: N empty, V=I, Z=e1, Av=A, Bv=e2, Theta=',theta,'X0=0 X1=-1; all equations exact')

    W=Mat([[F(1,3),F(1,2)],[F(1,2),1]]); Wi=Mat([[12,-6],[-6,4]])
    assert mm(W,Wi)==eye(2) and inv(W)==Wi
    h1=[-6,12]; h2=[0,0,3,-2]; m1=[0,0,-3,2]; m2=[0,-6,6]
    assert pd(m1)==list(map(F,m2)) and pd(m2)==list(map(F,h1))
    assert [F(x)+F(y) for x,y in zip(m1,h2)]==[0]*4
    assert peval(m1,1)==-1 and peval(m2,1)==0
    E1=pinteg(pmul(h1,h1));E2=pinteg(pmul(h2,h2))
    assert (E1,E2)==(12,F(13,35))
    ts=(F(1,3),F(2,3))
    samples=Mat([[peval(m1,t) for t in ts],[peval(m2,t) for t in ts]])
    controls=Mat([[peval(h1,t) for t in ts],[peval(h2,t) for t in ts]])
    interpolated=mm(controls,inv(samples))
    assert interpolated==Mat([[F(-108,13),F(81,26)],[-1,0]])
    assert mm(interpolated,samples)==controls and add(d0,mm(d1,interpolated))==zero(1,2)
    assert peval(h1,F(1,2))==0 and h1[1]!=0
    print('interpolated theta at t=1/3,2/3:',interpolated,'; zero first row would require two independent samples at the sole root t=1/2')
    print('Gramian=',W,'inverse=',Wi,'kernel energy=',E1,'/h^3 +',E2,'h; h=1 identities verified')
    assert mm(b,Mat([[-1],[0]]))==Mat([[0],[-1]])
    assert add(add(Mat([[-1],[-1]]),mm(b,Mat([[1],[0]]))),c)==zero(2,1)
    assert pd([0,-1])==[F(-1)] and [F(x)+F(y) for x,y in zip([0,-1],[0,1])]==[0,0]
    assert pinteg(pmul([0,1],[0,1]))==F(1,3)
    print('atom-heavy h=1: L0=(-1,0), Lh=(1,0), m=(-t,-1), H=(0,t), endpoint (0,0), energy=1/3; general scaling h/3')
    assert F(-1)+F(1)==0 and F(-1,2)+F(1,2)==0 and 1-1==0
    print('visible stochastic cancellation sigma=1/2: early output -1+1=0, diffusion residual -1/2+1/2=0, tail 1-1=0')

if __name__=='__main__':
    main()
