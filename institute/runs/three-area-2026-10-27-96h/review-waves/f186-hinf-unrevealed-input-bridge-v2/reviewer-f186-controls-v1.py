#!/usr/bin/env python3
"""Independently authored diagnostic controls; never evidence for T1--T8.
Only stdlib, numpy and mpmath are used. No author code is read or imported.
Native clock before composing: 2026-10-29T09:04:05-0700 PDT (not creation time).
"""
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, math, platform, random, time
import mpmath as mp
from mpmath import iv
import numpy as np

mp.mp.dps = 28
iv.dps = 60
START = datetime.now(timezone.utc).isoformat()
T0 = time.monotonic()
RESULTS = []
def add(name, kind, ok, data):
    RESULTS.append({'id': name, 'kind': kind, 'as_expected': bool(ok), 'data': data})
def s(x): return mp.nstr(x, 22)
def M(x):
    x=Q(x); return mp.mpf(x.numerator)/x.denominator
def I(x):
    x=Q(x); return iv.mpf(x.numerator)/iv.mpf(x.denominator)
def low(x): return mp.mp.make_mpf(x._mpi_[0])
def high(x): return mp.mp.make_mpf(x._mpi_[1])
def close(x,y,tol=mp.mpf('1e-20')): return abs(x-y) <= tol*max(1,abs(x),abs(y))

# C1: interval certification of (7.3), exact rational grid and extra cases.
ys=[Q(1,10**6),Q(1,100),Q(1,10),Q(1,2),Q(1),Q(2),Q(100),Q(10**6)]
cs=[Q(1,10**5),Q(1,100),Q(1,5),Q(1,2),Q(1)]
ws=[Q(0),Q(1,10**6),Q(1,10),Q(1),Q(3),Q(100),Q(10**6)]
triples=[(y,c,w) for y in ys for c in cs for w in ws]
triples += [(c,c,w) for c in cs for w in ws]
rng=random.Random(186)
triples += [(Q(rng.randint(1,10000),rng.randint(1,100)),Q(rng.randint(1,100),100),Q(rng.randint(1,10000),rng.randint(1,100))) for _ in range(250)]
strict=equal=bad=0
negative=0
single_sqrt_c=single_c_over_root_y=0
example=None
for y,c,w in triples:
    yy,cc,ww=I(y),I(c),I(w)
    lhs=iv.sqrt(yy+cc*ww)-iv.sqrt(yy)
    root_cost=iv.sqrt(1+ww)-1
    large=iv.sqrt(cc) if y>=c else cc/iv.sqrt(yy)
    small=cc/iv.sqrt(yy) if y>=c else iv.sqrt(cc)
    margin=large*root_cost-lhs
    if w==0 or y==c:
        equal+=1
        bad+=not (low(margin)<=0<=high(margin) and high(margin)-low(margin)<mp.mpf('1e-48'))
    else:
        strict+=1
        bad+=not (low(margin)>0)
        neg=small*root_cost-lhs
        negative += high(neg)<0
        if example is None and high(neg)<0:
            example={'y':str(y),'c':str(c),'w':str(w),'min_bound_minus_lhs_upper':s(high(neg))}
        single_sqrt_c += y<c and high(iv.sqrt(cc)*root_cost-lhs)<0
        single_c_over_root_y += y>c and high(cc/iv.sqrt(yy)*root_cost-lhs)<0
add('C1-positive-7.3','exact-rational-input/interval',bad==0,{'cases':len(triples),'strict':strict,'equality':equal,'bad':bad})
add('C1-negative-max-to-min','intended-reason-negative',negative==strict and single_sqrt_c>0 and single_c_over_root_y>0,{'certified_violations':negative,'expected':strict,'sqrt_c_only_violations':single_sqrt_c,'c_over_sqrt_y_only_violations':single_c_over_root_y,'example':example})

# C2: exact rational stationary point in (7.4), interval comparisons.
matched=below=bad=0
for k in [Q(4,5),Q(9,10),Q(99,100)]:
    for frac in [Q(1,10000),Q(1,10),Q(1,2),Q(9,10)]:
        c=k*k*frac; wstar=c/(k*k-c)
        kk,cc=I(k),I(c)
        target=kk-iv.sqrt(kk*kk-cc)
        for mult in [Q(0),Q(1,100),Q(1,2),Q(1),Q(2),Q(100)]:
            w=I(wstar*mult)
            value=iv.sqrt(cc*w)-kk*(iv.sqrt(1+w)-1)
            gap=target-value
            if mult==1:
                matched+=1
                bad+=not(low(gap)<=0<=high(gap) and high(gap)-low(gap)<mp.mpf('1e-47'))
            else:
                below+=1; bad+=not(low(gap)>0)
add('C2-positive-7.4','exact-rational-input/interval',bad==0,{'stationary_equalities':matched,'strict_below':below,'bad':bad})
k=I(Q(4,5)); c=I(1); w=I(10**8)
value=iv.sqrt(c*w)-k*(iv.sqrt(1+w)-1)
add('C2-negative-remove-c-less-kappa2','intended-reason-negative',low(value)>100,{'kappa':'4/5','c':'1','w':10**8,'objective_lower':s(low(value)),'reason':'sqrt(c)>kappa, so the objective grows without bound'})

# C3: exact rational Gaussian conditioning for Brownian bridge.
bridge_cases=0; bridge_bad=0; wrong_var=0
for a in [Q(1,10),Q(1,4),Q(1,2),Q(4,5),Q(9,10)]:
    for frac in [Q(1,10),Q(1,3),Q(1,2),Q(4,5)]:
        t=a+(1-a)*frac
        det=a*(1-a)
        # k=(Cov(B_t,B_a),Cov(B_t,B_1))=(a,t).
        alpha=(a-a*t)/det
        beta=(-a*a+a*t)/det
        variance=t-(alpha*a+beta*t)
        bridge_bad+=not(alpha==1-frac and beta==frac and variance==frac*(1-frac)*(1-a))
        bridge_bad+=not(a-a*a==a*(1-a))
        wrong_var+=variance!=frac*(1-frac)
        bridge_cases+=1
add('C3-positive-exact-bridge-and-XgivenZ','exact-Fraction',bridge_bad==0,{'cases':bridge_cases,'bad':bridge_bad})
add('C3-negative-drop-bridge-1-minus-a','intended-reason-negative',wrong_var==bridge_cases,{'wrong_variance_mismatches':wrong_var,'cases':bridge_cases})

# C4: T6 conditional Stein identity, direct integration vs derived expression.
def stein(p,a,z):
    mu=a*z; variance=a*(1-a); sd=mp.sqrt(variance)
    def density(x): return mp.exp(-(x-mu)**2/(2*variance))/(mp.sqrt(2*mp.pi)*sd)
    def g(x): return (p*x*x+(1-p)*z*z)**(-mp.mpf('1.5'))
    points=sorted(set([-mp.inf,mu-8*sd,mp.mpf(0),mu,mu+8*sd,mp.inf]))
    Eg=mp.quad(lambda x:g(x)*density(x),points)
    Ek=mp.quad(lambda x:x*(p*x*x+(1-p)*z*z)**(-mp.mpf('2.5'))*density(x),points)
    direct=mp.quad(lambda x:(z-x)*g(x)*density(x),points)
    rhs=(1-a)*z*Eg+3*p*variance*Ek
    return direct,rhs,Ek,Eg
for index,(p,a,z) in enumerate([(Q(3,10),Q(1,2),Q(2,5)),(Q(1434,10000),Q(8566,10000),Q(1)),(Q(7,10),Q(1,5),Q(2)),(Q(1,2),Q(9,10),Q(1,10))]):
    p,a,z=map(M,(p,a,z))
    direct,rhs,Ek,Eg=stein(p,a,z)
    opposite=stein(p,a,-z)[0]
    add('C4-positive-Stein-'+str(index),'high-precision-numerical',close(direct,rhs) and direct>0 and Ek>0 and close(opposite,-direct),{'p':s(p),'a':s(a),'z':s(z),'direct_m':s(direct),'Stein_rhs':s(rhs),'absolute_error':s(abs(direct-rhs)),'oddness_error':s(abs(opposite+direct))})
    wrong=(1-a)*z*Eg+p*a*(1-a)*Ek
    add('C4-negative-missing-factor3-'+str(index),'intended-reason-negative',abs(wrong-direct)>mp.mpf('1e-6'),{'wrong_rhs':s(wrong),'error':s(abs(wrong-direct)),'m_negative_z':s(opposite),'reason':'Stein derivative has coefficient 3; positivity of m is only for z>0'})

# C5: independently derived polar factorization of homogeneous Gaussian integrals.
# X=sqrt(a)U, Delta=sqrt(1-a)V, Z=X+Delta; (U,V)=R(cos,sin).
# E[R]=E[R^-1]=sqrt(pi/2). Smooth periodic integrands sampled at 2 resolutions.
def angular(p,a,N):
    p,a=M(p),M(a); acc=[mp.mpf(0) for _ in range(11)]
    for j in range(N):
        theta=2*mp.pi*(mp.mpf(j)+mp.mpf('0.5'))/N
        x=mp.sqrt(a)*mp.cos(theta); d=mp.sqrt(1-a)*mp.sin(theta); z=x+d
        y=p*x*x+(1-p)*z*z; root=mp.sqrt(y); inv3=1/(y*root)
        vals=[root,x*x/root,z*z/root,x*d/root,x*z*inv3,d*d/root,1/root,d*z*inv3,x*x*inv3,z*d*inv3,x*z/root]
        for k,val in enumerate(vals):acc[k]+=val
    return [v*mp.sqrt(mp.pi/2)/N for v in acc]
for index,(p,a) in enumerate([(Q(3,10),Q(1,2)),(Q(1434,10000),Q(8566,10000)),(Q(7,10),Q(1,5)),(Q(1,2),Q(9,10))]):
    v=angular(p,a,1024); refined=angular(p,a,2048)
    p0,a0=M(p),M(a)
    F,fa,f1,xd,xzinv,dd,inv,dzinv,xxinv,zdinv,xz=v
    Gamma=2*xz+(1-a0)*inv
    residuals=[xd+(1-a0)*(1-p0)*xzinv,dd-(1-a0)*(inv-(1-p0)*dzinv),fa-f1-(1-a0)*((1-p0)*xzinv-p0*xxinv),F-p0*fa-(1-p0)*f1,(Gamma-2*fa-(1-a0)*(1-p0)*zdinv)-(f1-fa)]
    err=max(abs(x) for x in residuals)
    conv=max(abs(x-y) for x,y in zip(v,refined))
    add('C5-positive-IBP-'+str(index),'high-precision-numerical',err<mp.mpf('1e-18') and conv<mp.mpf('1e-18') and zdinv>0,{'p':str(p),'a':str(a),'max_residual':s(err),'1024vs2048':s(conv),'E_ZDelta_Yminus3over2':s(zdinv),'F':s(F),'Gamma':s(Gamma)})
    add('C5-negative-IBP-sign-'+str(index),'intended-reason-negative',abs(xd-(1-a0)*(1-p0)*xzinv)>mp.mpf('1e-6'),{'wrong_sign_residual':s(xd-(1-a0)*(1-p0)*xzinv)})

# C6: KKT equalities are necessary for the reduced Gamma identity.
theta=2*np.pi*(np.arange(16384)+0.5)/16384
ct,st=np.cos(theta),np.sin(theta)
radial=math.sqrt(math.pi/2)
def quantities_float(p,a):
    x=math.sqrt(a)*ct; d=math.sqrt(1-a)*st; z=x+d
    y=p*x*x+(1-p)*z*z; root=np.sqrt(y)
    return {'F':radial*np.mean(root),'fa':radial*np.mean(x*x/root),'f1':radial*np.mean(z*z/root),'Gamma':radial*np.mean((2*x*z+(1-a))/root),'positive_term':radial*np.mean(z*d/(y*root))}
def p_stationary(a):
    left,right=1e-5,1-1e-5
    for _ in range(55):
        p=(left+right)/2; q=quantities_float(p,a)
        if q['fa']>q['f1']:left=p
        else:right=p
    p=(left+right)/2
    return p,quantities_float(p,a)
for a in [0.2,0.5,0.8566,0.95]:
    p,q=p_stationary(a)
    gap=q['Gamma']-2*q['F']; rhs=(1-a)*(1-p)*q['positive_term']
    add('C6-positive-KKT-curve-'+str(a),'float-numerical',abs(q['fa']-q['f1'])<1e-11 and abs(gap-rhs)<1e-11 and gap>0,{'a':a,'p':p,**q,'Gamma_minus_2F':gap,'factored_rhs':rhs,'interior_midpoint':q['F']+gap/4})
    off=quantities_float(p/2,a)
    residual=off['Gamma']-2*off['fa']-(1-a)*(1-p/2)*off['positive_term']
    add('C6-negative-use-KKT-off-curve-'+str(a),'intended-reason-negative',abs(residual)>1e-5 and abs(residual-(off['f1']-off['fa']))<1e-10,{'p_off_curve':p/2,'residual':residual,'f1_minus_fa':off['f1']-off['fa']})
# Recompute the rounded author diagnostic independently, not as a premise.
q=quantities_float(0.1434,0.8566)
add('C6-rounded-two-atom-diagnostic','float-numerical',abs(q['F']-0.802139)<1e-6 and abs(q['Gamma']-1.73851)<1e-4,{'p':0.1434,'a':0.8566,**q,'diagnostic_only':True})

# C7: exact determinant lower bound for separated weighted Brownian averages.
def covariance(xs,ws,ys,vs,q0):
    return sum(w*v*(min(x,y)-q0) for x,w in zip(xs,ws) for y,v in zip(ys,vs))/(sum(ws)*sum(vs))
det_cases=0; det_bad=0; minimum=None
for q0,L1,U1,L2,U2 in [(Q(1,10),Q(3,10),Q(4,10),Q(7,10),Q(9,10)),(Q(1,5),Q(1,2),Q(3,5),Q(4,5),Q(1))]:
    for _ in range(100):
        xs=[L1+(U1-L1)*Q(rng.randint(1,99),100) for _ in range(rng.randint(1,5))]
        ys=[L2+(U2-L2)*Q(rng.randint(1,99),100) for _ in range(rng.randint(1,5))]
        ws=[rng.randint(1,10) for _ in xs]; vs=[rng.randint(1,10) for _ in ys]
        v11=covariance(xs,ws,xs,ws,q0); v22=covariance(ys,vs,ys,vs,q0); v12=covariance(xs,ws,ys,vs,q0)
        det=v11*v22-v12*v12; bound=(L1-q0)*(L2-U1)
        det_bad+=not(v11>=L1-q0 and det/v11>=L2-U1 and det>=bound)
        minimum=min(minimum,det/bound) if minimum is not None else det/bound
        det_cases+=1
add('C7-positive-separated-support-determinant','exact-Fraction',det_bad==0,{'cases':det_cases,'bad':det_bad,'minimum_det_over_bound':str(minimum)})
q0=Q(1,10); t=Q(1,2)
v=covariance([t],[1],[t],[1],q0); determinant=v*v-v*v
add('C7-negative-no-separated-support','intended-reason-negative',determinant==0,{'G1_equals_G2':True,'determinant':str(determinant),'reason':'two coincident Brownian averages do not supply rank two'})

# C8: the two-dimensional density inverse-moment bound, numerical diagnostics.
def inverse_radius(v11,v12,v22):
    v11,v12,v22=map(mp.mpf,(v11,v12,v22)); l11=mp.sqrt(v11); l21=v12/l11; l22=mp.sqrt(v22-l21*l21)
    return mp.sqrt(mp.pi/2)*mp.quad(lambda t: 1/mp.sqrt((l11*mp.cos(t))**2+(l21*mp.cos(t)+l22*mp.sin(t))**2),[0,mp.pi/2,mp.pi,3*mp.pi/2,2*mp.pi])/(2*mp.pi)
for index,vals in enumerate([('1','0','1'),('100','0','100'),('0.01','0','2'),('1','0.99','1'),('0.2','0.1','0.8')]):
    v11,v12,v22=map(mp.mpf,vals); det=v11*v22-v12*v12
    actual=inverse_radius(*vals); bound=1+1/mp.sqrt(det)
    add('C8-positive-rank2-inverse-moment-'+str(index),'high-precision-numerical',actual<bound,{'covariance':vals,'actual':s(actual),'bound':s(bound)})
actual=inverse_radius('100','0','100')
add('C8-negative-drop-tail-plus1','intended-reason-negative',actual>mp.mpf('0.01'),{'actual':s(actual),'false_bound':'0.01','reason':'the unit-disc density bound alone does not bound the tail'})
trunc=2*mp.quad(lambda x:mp.exp(-x*x/2)/(mp.sqrt(2*mp.pi)*x),[mp.mpf('1e-6'),1,mp.inf])
add('C8-negative-rank1-analogue','intended-reason-negative',trunc>2,{'truncated_E_inverse_abs_normal':s(trunc),'cutoff':'1e-6','false_bound':'2','reason':'one-dimensional inverse absolute Gaussian moment diverges'})

# C9: exact constants and independent numerical exit-time check for T5.
N=10
partial=sum((Q(1,math.factorial(j)) for j in range(N+1)),Q(0))
tail=Q(1,math.factorial(N+1))/(1-Q(1,N+2))
e_upper=partial+tail
exact=(e_upper<Q(68,25) and Q(68,25)**25<3**32 and Q(44,7)<9 and 1-Q(1,243)/8==Q(1943,1944))
phi=iv.exp(-I(Q(25,8)))/iv.sqrt(2*iv.pi)
add('C9-positive-T5-constants','exact-Fraction/interval',exact and low(phi)>M(Q(1,243)),{'e_rational_upper':str(e_upper),'phi_2.5_lower':s(low(phi)),'threshold':'1/243','exact_last_fraction':'1943/1944'})
exponential=iv.exp(I(Q(25,8)))
normal_tail=mp.erfc(mp.sqrt(2))
wrong_phi2=mp.exp(-2)/mp.sqrt(2*mp.pi)
add('C9-negative-tightened-constants','intended-reason-negative',low(exponential)>22 and normal_tail<wrong_phi2,{'exp25over8_lower':s(low(exponential)),'false_upper':22,'normal_two_sided_tail_at2':s(normal_tail),'phi_at2':s(wrong_phi2),'reason':'neither replacing 81 by 22 nor replacing phi(2.5) by phi(2) is valid'})
exit_half=4*mp.sqrt(2*mp.pi)*mp.catalan/mp.pi**2
laplace_half=mp.sqrt(2/mp.pi)*mp.quad(lambda t:(1-mp.sech(t))/t**2,[0,1,10,mp.inf])
add('C9-exit-half-moment-diagnostic','high-precision-numerical',abs(exit_half-laplace_half)<mp.mpf('1e-15') and exit_half<M(Q(1943,1944)),{'via_Catalan_survival_series':s(exit_half),'via_Laplace_sech_integral':s(laplace_half),'reciprocal':s(1/exit_half),'diagnostic_classical_exit_transform_not_a_theorem_premise':True})

# C10: exact arithmetic in T2 and T8, and physical/normalized threshold maps.
etas=[Q(i,120) for i in range(120)]
hs=[eta/(1+eta) for eta in etas]
exact=(2-Q(1,2))/(1-Q(1,2))==3 and Q(1,2)/(1+Q(1,2))==Q(1,3)
exact=exact and all(x<y for x,y in zip(hs,hs[1:])) and all(h<Q(1,2) for h in hs)
exact=exact and all((eta<Q(1,2))==(h<Q(1,3)) for eta,h in zip(etas,hs))
add('C10-positive-normalization-arithmetic','exact-Fraction',exact,{'eta_grid':len(etas),'Lenglart_constant':'3','h_at_eta_half':'T/3','upper_open_endpoint':'T/2'})

END=datetime.now(timezone.utc).isoformat()
report={'schema_version':1,'kind':'INDEPENDENT_REVIEWER_DIAGNOSTICS_NOT_THEOREM_EVIDENCE','author_code_read_or_imported':False,'start_utc':START,'end_utc':END,'wall_seconds':time.monotonic()-T0,'python':platform.python_version(),'numpy':np.__version__,'mpmath':mp.__version__,'mpmath_dps':mp.mp.dps,'interval_dps':iv.dps,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'results':RESULTS,'summary':{'expected_outcomes':sum(x['as_expected'] for x in RESULTS),'unexpected_outcomes':sum(not x['as_expected'] for x in RESULTS),'controls':len(RESULTS),'negative_controls':sum(x['kind']=='intended-reason-negative' for x in RESULTS)}}
output=Path(__file__).with_name('reviewer-f186-controls-output-v1.json')
with output.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps(report['summary'],sort_keys=True))
raise SystemExit(0 if report['summary']['unexpected_outcomes']==0 else 1)
