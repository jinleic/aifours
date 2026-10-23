# Parent independent exact rational boundary/interior checks; no worker imports.
from fractions import Fraction as F
import json

def trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def add(a,b):
    return trim([(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))])

def mul(a,b):
    q=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): q[i+j]+=x*y
    return trim(q)

def div(a,b):
    a=a[:];q=[F(0)]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        i=len(a)-len(b);v=a[-1]/b[-1];q[i]=v
        for j,t in enumerate(b): a[i+j]-=v*t
        trim(a)
    return trim(q),a

def solve(A,b):
    n=len(b);A=[row[:]+[b[i]] for i,row in enumerate(A)]
    for j in range(n):
        k=next(k for k in range(j,n) if A[k][j]);A[j],A[k]=A[k],A[j]
        z=A[j][j];A[j]=[x/z for x in A[j]]
        for i in range(n):
            if i!=j:
                z=A[i][j];A[i]=[x-z*y for x,y in zip(A[i],A[j])]
    return [A[i][-1] for i in range(n)]

def check(n,r,m,t):
    W=F(1);Q=[F(1)]
    for mi in m: W*=1-mi;Q=mul(Q,[-mi,F(1)])
    Q[0]-=W
    D=[-r,r,F(-1),F(1)]
    P,rem=div(Q,D);assert rem==[F(0)]
    N=[F(0)]
    for j in range(n):
        z=[t[j]]
        for k in range(j+1,n): z=mul(z,[-m[k],F(1)])
        N=add(N,z)
    assert N==[F(4+r)*x for x in P]
    T0=[[F(0)]*n for _ in range(n)]
    for i in range(n): T0[i][i]=m[i]-2;T0[i][(i+1)%n]=F(1) if i<n-1 else W
    v=solve([[-x for x in row] for row in T0],t)
    assert min(v)>0 and v[0]==1
    T=[[T0[i][j]*v[j]/v[i] for j in range(n)] for i in range(n)]
    exits=[-sum(row) for row in T]
    assert min(exits)>=0 and all(T[i][j]>=0 for i in range(n) for j in range(n) if i!=j)
    values=[]
    for s in [F(0),F(1,7),F(3),F(11,2)]:
        X=[[s*(i==j)-T[i][j] for j in range(n)] for i in range(n)]
        got=solve(X,exits)[0];want=(4+r)/((s+1)*((s+2)**2+r))
        assert got==want
        values.append({'s':str(s),'transform':str(got)})
    wrong_initial=solve([[F(1)*(i==j)-T[i][j] for j in range(n)] for i in range(n)],exits)[1]
    assert wrong_initial!=(4+r)/(2*(9+r))
    return {'n':n,'beta_squared':str(r),'m':list(map(str,m)),'W':str(W),'t':list(map(str,t)),
        'Q_minus_W':list(map(str,Q)),'D':list(map(str,D)),'P':list(map(str,P)),
        'v':list(map(str,v)),'T':[[str(x) for x in row] for row in T],'exits':list(map(str,exits)),
        'transfer_checks':values,'wrong_initial_e2_rejected':True,'all_exact':True}

def main():
    cases=[check(3,F(1,4),[F(2,3),F(1,6),F(1,6)],[F(0),F(0),F(17,4)]),
           check(4,F(1),[F(0)]*4,[F(0),F(0),F(5),F(5)]),
           check(6,F(3),[F(-1)]*6,[F(0),F(0),F(7),F(28),F(56),F(56)])]
    return {'scope':'Finite exact rational examples only, not universal proof; a=2,c=1,b=sqrt(beta_squared).',
      'cases':cases,'positive_cases_pass':3,'exact_transfer_checks_pass':12,'wrong_initial_controls_rejected':3}
