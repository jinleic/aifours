#!/usr/bin/env python3
"""Search a richer 5+1+1 PH7 graph with the original four-edge delay.

Five-state upstream block has all allowed internal feedback/shortcuts except
initial-support-to-output shortcuts, and full nonnegative center/tail return
rows. Numeric optimization is proposal only; any point is rationalized and
verified by exact actual 7x7 determinants, row ties, and stability.
"""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from itertools import combinations
from pathlib import Path
import json,sys,time,numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import least_squares
base=SourceFileLoader('ex',str(ROOT/'frontier-20261028-ph7-chain-search.py')).load_module()
bal=SourceFileLoader('ba',str(ROOT/'frontier-20261028-ph7-balanced-search.py')).load_module()
nu=SourceFileLoader('nu',str(ROOT/'frontier-20261028-ph7-nonuniform-search.py')).load_module()
C=F(1);RNG=np.random.default_rng(20261108);MAX_STARTS=5;MAX_NFEV=1800;WALL=100
RATIOS=[F(33,40),F(83,100),F(17,20),F(8,9)]
ARCS=[(0,2),(0,3),(1,0),(1,3),(2,0),(2,1),(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(4,3)]


def numeric_outer(x,z):
    rates=x[:6];arcs=x[6:19];bi=x[19:21]
    A=np.zeros((5,5));np.fill_diagonal(A,-rates[:5])
    for i in range(4):A[i,i+1]=1.
    for (i,j),v in zip(ARCS,arcs):A[i,j]=v
    coeff=np.poly(A).real # monic descending characteristic
    Bmat=np.eye(5); U=np.zeros((5,5))
    for k in range(5):
        U[:,4-k]=Bmat[:,4]
        Bmat=A@Bmat+coeff[k+1]*np.eye(5)
    beta=np.array([bi[0],bi[1],1.,0.,0.]);NR=beta@U
    lead=NR[2];q=NR[0]/lead;p=NR[1]/lead
    w=p+4.-sum(rates);v=rates[5]
    a0=coeff[::-1]
    target=np.convolve(np.convolve([0.,1.],np.convolve([1+z,2.,1.],[1+z,2.,1.])),[q,p,1.])
    residual=np.convolve(np.convolve([w,1.],[v,1.]),a0)-target
    gens=[np.convolve([v,1.],U[j]) for j in range(5)]+[U[j] for j in range(5)]+[a0]
    def six(a):return (list(a)+[0.]*6)[:6]
    return np.array([six(a)for a in gens]).T,np.array(six(residual)),w,p,q,lead


def fun(x,z):
    with np.errstate(over='ignore',invalid='ignore',divide='ignore'):
        M,b,w,p,q,lead=numeric_outer(x,float(z));fb=x[21:]
        vals=np.r_[(M@fb-b)/(1+np.abs(b)+np.abs(M)@fb),min(w,0.),min(q,0.),min(lead,0.)]
    return vals if np.isfinite(vals).all() else np.full(9,1e8)


def rational_outer(rates,arcs,bi,z):
    A=[[F(0)for _ in range(5)]for _ in range(5)]
    for i in range(5):A[i][i]=-rates[i]
    for i in range(4):A[i][i+1]=F(1)
    for (i,j),v in zip(ARCS,arcs):A[i][j]=v
    pencil=[[([-A[i][j],F(1)]if i==j else[-A[i][j]])for j in range(5)]for i in range(5)]
    a0=base.det_poly(pencil);U=[]
    for row in range(5):
        minor=[[pencil[i][j]for j in range(5)if j!=row]for i in range(4)]
        col=base.det_poly(minor)
        if (row+4)%2:col=[-v for v in col]
        U.append(col)
    beta=[bi[0],bi[1],F(1),F(0),F(0)]
    N=[F(0)]
    for j in range(5):N=base.pol_add(N,[beta[j]*v for v in U[j]])
    if any(N[i]!=0 for i in range(3,len(N))) or N[2]<=0:return None
    lead=N[2];q=N[0]/lead;p=N[1]/lead;w=p+4-sum(rates);tail=rates[5]
    dz=base.pol_mul([F(0),F(1)],base.pol_mul([1+z,F(2),F(1)],[1+z,F(2),F(1)]))
    residual=base.pol_add(base.pol_mul(base.pol_mul([w,F(1)],[tail,F(1)]),a0),[-v for v in base.pol_mul(dz,[q,p,F(1)])])
    gens=[base.pol_mul([tail,F(1)],v)for v in U]+U+[a0]
    def six(a):return (a+[F(0)]*6)[:6]
    return A,[six(g)for g in gens],six(residual),w,p,q,lead


def verify(rates,arcs,bi,fb,w,p,q,lead,z):
    A,*_=rational_outer(rates,arcs,bi,z);G=[[F(0)for _ in range(7)]for _ in range(7)]
    for i in range(5):
        for j in range(5):G[i][j]=A[i][j]
    G[4][5]=G[5][6]=F(1);G[5][5]=-w;G[6][6]=-rates[5]
    for i in range(5):G[5][i]=fb[i];G[6][i]=fb[5+i]
    G[6][5]=fb[10]
    def pencil():return [[([-G[i][j],F(1)]if i==j else[-G[i][j]])for j in range(7)]for i in range(7)]
    char=base.det_poly(pencil());dz=base.pol_mul([F(0),F(1)],base.pol_mul([1+z,F(2),F(1)],[1+z,F(2),F(1)]))
    Q=[q,p,F(1)]
    if char!=base.pol_mul(dz,Q):raise AssertionError('characteristic')
    K=C*((C+1)**2+z)**2;beta=[bi[0],bi[1],F(1),F(0),F(0),F(0),F(0)];gamma=[F(0)]*6+[K/lead]
    bump=[[v[:]for v in row]for row in pencil()]
    for i in range(7):
        for j in range(7):bump[i][j]=base.pol_add(bump[i][j],[gamma[i]*beta[j]])
    num=base.pol_add(base.det_poly(bump),[-v for v in char])
    while len(num)>3 and num[-1]==0:num.pop()
    if num!=[K*v for v in Q]:raise AssertionError('numerator')
    lhs=[[(C if i==j else F(0))-G[i][j]for j in range(7)]for i in range(7)]
    h=bal.solve_square(lhs,gamma)
    if h is None or not all(v>0 for v in h):raise AssertionError('normalizer')
    T=[[(G[i][j]-(C if i==j else 0))*h[j]/h[i]for j in range(7)]for i in range(7)]
    alpha=[beta[i]*h[i]for i in range(7)];omega=[gamma[i]/h[i]for i in range(7)]
    if sum(alpha)!=1 or not all(v>=0 for v in alpha+omega):raise AssertionError('probability')
    for i in range(7):
        if any(T[i][j]<0 for j in range(7)if i!=j)or sum(T[i])+omega[i]!=0:raise AssertionError('row')
    if p<=0 or q<=0:raise AssertionError('Hurwitz')
    return {'z':str(z),'rates':[str(v)for v in rates],'arcs':[str(v)for v in arcs],
      'initial':[str(v)for v in bi],'feedback':[str(v)for v in fb],'w':str(w),'p':str(p),'q':str(q),'lead':str(lead),
      'G':[[str(v)for v in row]for row in G],'h':[str(v)for v in h],
      'alpha':[str(v)for v in alpha],'T':[[str(v)for v in row]for row in T],'omega':[str(v)for v in omega],
      'checks':['full7x7 exact determinant','full actual numerator','positive h/alpha/exit/Metzler/rows','Hurwitz']}


def exact_project(x,z):
    for den in (100,1000,10000,100000):
        rates=[F(round(float(v)*den),den)for v in x[:6]]
        arcs=[F(round(float(v)*den),den)for v in x[6:19]]
        bi=[F(round(float(v)*den),den)for v in x[19:21]]
        if not all(v>0 for v in rates)or not all(v>=0 for v in arcs+bi):continue
        result=rational_outer(rates,arcs,bi,z)
        if result is None:continue
        A,M,b,w,p,q,lead=result
        if min(w,p,q,lead)<=0:continue
        free=[F(round(float(v)*den),den)for v in x[21:]]
        for choice in combinations(range(11),6):
            others=[i for i in range(11)if i not in choice]
            rhs=[b[j]-sum(M[i][j]*free[i]for i in others)for j in range(6)]
            sol=bal.solve_square([[M[i][j]for i in choice]for j in range(6)],rhs)
            if sol is None:continue
            fb=free[:]
            for i,v in zip(choice,sol):fb[i]=v
            if all(v>=0 for v in fb):
                try:return verify(rates,arcs,bi,fb,w,p,q,lead,z)
                except AssertionError:continue
    return None


def main():
    seed_rates=list(map(F,['669/500','1339/1000','671/500','669/500','1043/1000','1041/1000']))
    nu.Z=F(820409,1000000);v=nu.rational_family(seed_rates)
    # Embed the already verified 3+1+3 construction exactly as 5+1+1.
    rates=[seed_rates[0],seed_rates[1],seed_rates[2],v['w'],seed_rates[3],seed_rates[5]]
    arcs=[F(0)]*13;arcs[9]=v['D1'];bi=[v['C0'],v['B']]
    feedback=[v['D2'],0,0,0,0,v['D3'],0,0,v['phi'],0,0]
    seed=np.array([float(x)for x in rates+arcs+bi+feedback])
    lower=np.array([.05]*6+[0.]*26);upper=np.array([8.]*6+[12.]*13+[15.]*2+[40.]*11)
    start=time.monotonic();rows=[]
    for z in RATIOS:
        best=None;exact=None;attempts=[]
        for j in range(MAX_STARTS):
            if time.monotonic()-start>WALL:break
            x0=seed.copy() if j==0 else seed+RNG.normal(0,.08,len(seed))*np.maximum(.03,np.abs(seed))
            x0=np.maximum(lower+1e-10,np.minimum(upper-1e-10,x0))
            try:fit=least_squares(lambda x:fun(x,z),x0,bounds=(lower,upper),max_nfev=MAX_NFEV,
                                  ftol=1e-12,xtol=1e-12,gtol=1e-12)
            except (np.linalg.LinAlgError,ValueError)as exc:
                attempts.append({'start':j,'error':str(exc)});continue
            err=float(np.linalg.norm(fun(fit.x,z),ord=np.inf));attempts.append({'start':j,'residual_inf':err,'nfev':int(fit.nfev)})
            if best is None or err<best[0]:best=(err,fit.x.copy())
            if err<1e-8:
                exact=exact_project(fit.x,z)
                if exact:seed=fit.x.copy();break
        rows.append({'z':str(z),'attempts':attempts,'best_residual_inf':best[0]if best else None,
                     'best_parameters':best[1].tolist()if best else None,'exact_witness':exact})
        print('z',z,'attempts',len(attempts),'best',rows[-1]['best_residual_inf'],'exact',bool(exact),flush=True)
        if time.monotonic()-start>WALL:break
    out=ROOT/'frontier-20261028-ph7-five-upstream-search-result.json'
    out.write_text(json.dumps({'seed':20261108,'elapsed_seconds':time.monotonic()-start,'rows':rows,
      'scope':'specified 5+1+1 graph; numerical miss is not a global exclusion'},indent=2)+'\n');print('saved:',out)

if __name__=='__main__':main()
