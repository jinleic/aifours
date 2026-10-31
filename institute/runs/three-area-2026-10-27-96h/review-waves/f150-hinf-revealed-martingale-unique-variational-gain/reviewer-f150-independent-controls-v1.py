#!/usr/bin/env python3
"""Independent controls for f150. No author module is imported or executed.
Exact controls use rational or integer arithmetic. mpmath is diagnostic only.
The optional certificate uses a FIXED projective grid, not the author's adaptive
heap or algorithm. Each interval contribution is rounded DOWN before summing.
"""
from fractions import Fraction as Q
from math import isqrt
import random
import mpmath as mp

checks = []
def check(name, condition, detail=''):
    checks.append((name, bool(condition)))
    print(('PASS ' if condition else 'FAIL ') + name + (': ' + str(detail) if detail else ''), flush=True)

# 1. Exact discrete signed-measure variance identity and meaningful negatives.
def variance(points, weights, power=2):
    return 2 * sum((min(s,t)**power * x*y for s,x in zip(points,weights)
                    for t,y in zip(points,weights)), Q(0))
def tails(points, weights):
    value = Q(0); prev = Q(0)
    for p in sorted(set(points)):
        tail = sum((w for s,w in zip(points,weights) if s >= p), Q(0))
        value += 2*(p*p-prev*prev)*tail*tail
        prev = p
    return value
r = random.Random(150)
positive = zero = 0
for i in range(300):
    n = r.randrange(2,7)
    ts = [Q(r.randrange(61),60) for _ in range(n)]
    ws = [Q(r.randrange(-9,10),r.randrange(1,8)) for _ in range(n-1)]
    ws.append(-sum(ws,Q(0)))
    agg = {}
    for t,w in zip(ts,ws): agg[t] = agg.get(t,Q(0)) + w
    nonzero = any(agg.values())
    v = variance(ts,ws)
    assert v == tails(ts,ws)
    assert (v > 0) if nonzero else (v == 0)
    positive += nonzero; zero += not nonzero
check('V1 variance identity and strict positivity for 300 mass-zero cases', True,
      {'positive':positive,'zero':zero})
ts = [Q(1,4), Q(1,2), Q(1)]; ws = [Q(1,2), Q(-1), Q(1,2)]
check('V2 exact hand case', variance(ts,ws)==tails(ts,ws)>0, str(variance(ts,ws)))
check('NV1 negative: wrong min(s,t) kernel is rejected', variance(ts,ws,1)!=tails(ts,ws))
check('NV2 negative: d_0 has zero variance despite being nonzero; mass-zero condition essential',
      variance([Q(0)],[Q(1)])==tails([Q(0)],[Q(1)])==0)
check('V3 d_0-d_(1/3) restores strict positivity under mass zero',
      variance([Q(0),Q(1,3)],[Q(1),Q(-1)])==Q(2,9))

# 2. Exact physical-clock / second-moment bookkeeping on rational examples.
for i,(S,edges,values) in enumerate([
    (Q(3,2),[Q(0),Q(3,2)],[Q(2)]),
    (Q(3,2),[Q(0),Q(1,1000),Q(3,2)],[Q(5),Q(0)]),
    (Q(3,2),[Q(0),Q(1,2),Q(1),Q(3,2)],[Q(1),Q(-3),Q(2)])]):
    norm2 = sum((v*v*(b-a) for a,b,v in zip(edges,edges[1:],values)),Q(0))
    first = sum((v*v*(b*b-a*a)/2 for a,b,v in zip(edges,edges[1:],values)),Q(0))
    out2 = sum((v*v*(S*(b-a)-(b*b-a*a)/2) for a,b,v in zip(edges,edges[1:],values)),Q(0))
    m = first/(S*norm2)
    A_integral=Q(0); acc=Q(0)
    for a,b,v in zip(edges,edges[1:],values):
        A_integral += (acc*(b-a)+v*v*(b-a)**2/2)/(norm2*S)
        acc += v*v*(b-a)
    check('C%d exact Ito identities and mean of clock'%i,
          out2==S*norm2*(1-m) and first==S*norm2*m and A_integral==1-m and out2<=S*norm2,
          'm='+str(m))

# 3. Rational covariance determinant, rank-two requirement, inverse-moment threshold.
for e in [Q(1,2),Q(1,10),Q(1,100),Q(1,10**6)]:
    a,b,c=Q(1,2),Q(1,2),Q(1)
    trace=e*a+(1-e)*c
    det=e*(1-e)*(a*c-b*b)
    check('G eigenvalue invariants e='+str(e), trace==1-e/2 and det==e*(1-e)/4 and det>0)
# Gaussians Z1=B_(1/4), Z2=B_(3/4): a concrete separated-interval special case.
check('I1 separated positive times give rank two', Q(1,4)*Q(3,4)-Q(1,4)**2==Q(1,8)>0)
check('NI1 negative: same time twice gives rank one', Q(1,4)*Q(1,4)-Q(1,4)**2==0)
# In d dimensions the small-radius integral of (r^2)^(-p) is int r^(d-1-2p) dr;
# finite exactly when exponent > -1.
p=Q(3,4)
check('I2 inverse-3/4 is locally integrable for nondegenerate rank two', 2-1-2*p > -1)
check('NI2 negative: inverse-3/4 fails at rank one', not (1-1-2*p > -1))
check('NI3 negative: inverse-half also fails at rank one', not (1-1-2*Q(1,2) > -1))
check('I3 Holder exponents use E[Y^-3/4], not E[|B|^-1/2]', Q(1,3)+Q(2,3)==1 and Q(1,2)*Q(3,2)==Q(3,4))

# 4. Independent exact OPTIONAL quadrature control.
# u_i=i/(N-i), i=0,...,N-1. This is a fixed grid on [0,N-1]. Since g decreases,
# sum_i (u_i-u_(i-1))*g(u_i) is a lower bound. For k=N-i,
# D = (10000 k^4+19900 i^2 k^2+99 i^4)/(10000 k^4).
# r=floor(QROOT sqrt(D)); then r/QROOT<=sqrt(D)<(r+1)/QROOT.
# Thus g(u_i)>= (r-QROOT)/r * k^2/i^2 and the interval contribution is >=
#    N*k*(r-QROOT)/((k+1)*r*i^2).
# Every contribution is additionally rounded down to a multiple of 10^-18.
QROOT=10**30; ISCALE=10**18

def independent_integral_lower(N):
    acc=0
    for i in range(1,N):
        k=N-i
        dn=10000*k**4+19900*i*i*k*k+99*i**4
        dd=10000*k**4
        r=isqrt((dn*QROOT*QROOT)//dd)
        assert r*r*dd <= dn*QROOT*QROOT < (r+1)*(r+1)*dd
        assert r >= QROOT
        term_num=N*k*(r-QROOT)
        term_den=(k+1)*r*i*i
        acc += (ISCALE*term_num)//term_den
    return Q(acc,ISCALE)

coarse=independent_integral_lower(32)
check('NQ negative: coarse fixed grid does not certify 283/200', coarse<Q(283,200), str(coarse))
L=independent_integral_lower(32768)
check('Q1 optional independent exact projective-grid integral lower >= 283/200', L>=Q(283,200), str(L))
margin=Q(283,200)**2*Q(7,22)-Q(7981,10000)**2
check('Q2 exact integral threshold + pi<22/7 implies F>7981/10000', margin>0, str(margin))
# Independent Machin alternating bounds on pi; atan(x)>x-x^3/3 and atan(x)<x.
x=Q(1,5); y=Q(1,239)
pi_lo=16*(x-x**3/3)-4*y
pi_hi=16*(x-x**3/3+x**5/5)-4*(y-y**3/3)
check('Q3 independent Machin pi lower and upper', Q(157,50)<pi_lo<pi_hi<Q(22,7),
      {'pi_lo':str(pi_lo),'pi_hi':str(pi_hi)})
comp=Q(7981,10000)**2*Q(157,50)-2
check('Q4 optional strict lower exceeds c=sqrt(2/pi)', comp==Q(328677,5000000000)>0, str(comp))
check('NQ2 negative: replacing lower threshold by 79/100 cannot certify >c using pi_lo',
      Q(79,100)**2*pi_lo<2)
# The explicit physical pulse step-clock coupling uses total changed time 2delta.
d=Q(1,10**10)
check('Q5 pulse error sqrt(2delta)<1/50000', 2*d<Q(1,50000)**2)
check('Q6 pulse threshold arithmetic', Q(7981,10000)-Q(1,50000)==Q(2494,3125))

# 5. High-precision numerical sanity checks of ORIGINAL proof, diagnostic only.
mp.mp.dps=50
c=mp.sqrt(2/mp.pi); U=(c+mp.sqrt(2-c*c))/2
C=2*mp.exp(-mp.mpf(5)/2)/(mp.pi*(mp.sqrt(5)+1))
a=(mp.sqrt(2-c*c)-c)/2
check('D1 diagnostic crossing', abs(mp.sqrt(1-a*a)-(c+a))<mp.mpf('1e-45') and c<U<1)
print('DIAGNOSTIC upper-bracket constant (not optimal kappa)='+mp.nstr(U,18),flush=True)

def norm_quadratic(l1,l2):
    return mp.sqrt(2/mp.pi)*mp.quad(lambda t:mp.sqrt(l1*mp.cos(t)**2+l2*mp.sin(t)**2),[0,mp.pi/2])
def two_point(e):
    tr=1-e/2; det=e*(1-e)/4
    l1=(tr+mp.sqrt(tr*tr-4*det))/2; l2=det/l1
    return norm_quadratic(l1,l2),l1,l2

for text in ['0.1','0.01','0.001','0.000001']:
    e=mp.mpf(text); f,l1,l2=two_point(e); s=mp.sqrt(e)/2
    increment=norm_quadratic(1,s*s)-c
    low1=mp.sqrt(1-e)*norm_quadratic(1,s*s)
    check('D2 original epsilon-log chain e='+text,
          l1>=1-e and l2>=e*(1-e)/4 and f>=low1 and increment>=C*s*s*mp.log(1/s) and f>c,
          'F-c='+mp.nstr(f-c,12))
# Use logs directly, not subtracting near-equal F and c at astronomically small e.
# e=4 exp(-16c/C-2) gives log(2/sqrt(e))=8c/C+1 and e<1/2.
log_e=mp.log(4)-16*c/C-2
small_e=mp.exp(log_e)
Llog=mp.log(2)-log_e/2
bracket=-c+(1-small_e)*C/4*Llog
check('D3 original sufficient small-e condition gives positive factored deficit', small_e<mp.mpf('0.5') and Llog>8*c/C and bracket>0,
      'log(e)='+mp.nstr(log_e,12)+'; deficit/e lower='+mp.nstr(bracket,12))
normal_e=mp.mpf('1e-6')
check('ND1 negative: crude log lower bound alone does not certify at e=1e-6',
      -c+(1-normal_e)*C/4*mp.log(2/mp.sqrt(normal_e))<0)
check('ND2 negative: moving 0.01 mass from 1 to 0 lowers F', mp.sqrt(mp.mpf('.99'))*c<c)
# Neither inverse-half nor inverse-3/4 exists for Y=B_1^2. The rank-two radial formula
# E R^-3/2 = 2^-3/4 Gamma(1/4) is finite; do not confuse powers of Y with powers of |B|.
rad=mp.mpf(2)**(-mp.mpf(3)/4)*mp.gamma(mp.mpf(1)/4)
check('D4 rank-two radial inverse moment finite', mp.isfinite(rad) and rad>0, mp.nstr(rad,18))
# Brownian scaling with any two-point covariance: eigenvalues scale linearly in time.
f0,aa,bb=two_point(mp.mpf('.1'))
check('D5 support-endpoint scaling', abs(norm_quadratic(aa/2,bb/2)*mp.sqrt(2)-f0)<mp.mpf('1e-45'))

fail=[name for name,ok in checks if not ok]
print('SUMMARY '+str(len(checks)-len(fail))+' PASS / '+str(len(fail))+' FAIL; no Monte Carlo or optimizer used.',flush=True)
if fail:
    raise SystemExit('Failed controls: '+repr(fail))
