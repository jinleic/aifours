#!/usr/bin/env python3
"""Independent rational-interval reconstruction. No candidate code is imported.
All arithmetic endpoints are Fraction; interval rounding is directed to a rational grid.
"""
from fractions import Fraction as Q
from math import isqrt
import json

class CheckFailure(Exception):
    def __init__(self, reason):
        self.reason = reason
        super().__init__(reason)

def need(condition, reason):
    if not condition:
        raise CheckFailure(reason)

def q(v):
    return v if isinstance(v, Q) else Q(v)

def sgn(x):
    return int(x > 0) - int(x < 0)

# Field arithmetic is exact; comparisons never pass through a float.
class Quad:
    def __init__(self, a, b, rad):
        self.a, self.b, self.rad = q(a), q(b), q(rad)
        need(self.rad > 0, 'quadratic-radicand')
    def coerce(self, x):
        if isinstance(x, Quad):
            need(self.rad == x.rad, 'quadratic-field-mismatch')
            return x
        return Quad(x, 0, self.rad)
    def __add__(self, x):
        x = self.coerce(x)
        return Quad(self.a+x.a, self.b+x.b, self.rad)
    __radd__ = __add__
    def __neg__(self):
        return Quad(-self.a, -self.b, self.rad)
    def __sub__(self, x):
        return self + (-self.coerce(x))
    def __rsub__(self, x):
        return self.coerce(x) - self
    def __mul__(self, x):
        x = self.coerce(x)
        return Quad(self.a*x.a+self.b*x.b*self.rad,
                    self.a*x.b+self.b*x.a, self.rad)
    __rmul__ = __mul__
    def __pow__(self, n):
        need(isinstance(n, int) and n >= 0, 'quadratic-exponent')
        z = self.coerce(1)
        for _ in range(n):
            z = z*self
        return z
    def inverse(self):
        norm = self.a*self.a - self.b*self.b*self.rad
        need(norm != 0, 'quadratic-zero-norm')
        return Quad(self.a/norm, -self.b/norm, self.rad)
    def __truediv__(self, x):
        return self*self.coerce(x).inverse()
    def sign(self):
        a, b, r = self.a, self.b, self.rad
        if not b: return sgn(a)
        if not a: return sgn(b)
        if a > 0 and b > 0: return 1
        if a < 0 and b < 0: return -1
        if a > 0: return sgn(a*a-b*b*r)
        return sgn(b*b*r-a*a)
    def enclosure(self):
        low, high = sqrt_bracket(self.rad)
        p, z = self.a+self.b*low, self.a+self.b*high
        return Interval(min(p, z), max(p, z))

# Directed rational-grid intervals; no input or output endpoint is a float.
GRID = 10**75

def floor_grid(x):
    x = q(x)
    return Q((x.numerator*GRID)//x.denominator, GRID)

def ceil_grid(x):
    x = q(x)
    return Q(-((-x.numerator*GRID)//x.denominator), GRID)

class Interval:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = q(lo), q(lo if hi is None else hi)
        need(self.lo <= self.hi, 'interval-order')
    @staticmethod
    def cast(x):
        return x if isinstance(x, Interval) else Interval(x)
    @staticmethod
    def outward(lo, hi):
        return Interval(floor_grid(lo), ceil_grid(hi))
    def __add__(self, x):
        x = self.cast(x)
        return self.outward(self.lo+x.lo, self.hi+x.hi)
    __radd__ = __add__
    def __neg__(self):
        return Interval(-self.hi, -self.lo)
    def __sub__(self, x):
        return self + (-self.cast(x))
    def __rsub__(self, x):
        return self.cast(x) - self
    def __mul__(self, x):
        x = self.cast(x)
        v = (self.lo*x.lo, self.lo*x.hi, self.hi*x.lo, self.hi*x.hi)
        return self.outward(min(v), max(v))
    __rmul__ = __mul__
    def __truediv__(self, x):
        x = self.cast(x)
        need(x.lo > 0, 'denominator-positive')
        return self * Interval(Q(1)/x.hi, Q(1)/x.lo)
    def __pow__(self, n):
        need(isinstance(n, int) and n >= 0, 'interval-exponent')
        z = Interval(1)
        for _ in range(n): z = z*self
        return z

def sqrt_bracket(x):
    x = q(x)
    need(x > 0, 'sqrt-positive-domain')
    k = isqrt((x.numerator*GRID*GRID)//x.denominator)
    lo, hi = Q(k, GRID), Q(k+1, GRID)
    need(lo*lo <= x < hi*hi, 'sqrt-orientation')
    return lo, hi

def atan_interval(z, terms=20):
    z = Interval.cast(z)
    need(0 < z.lo <= z.hi < 1, 'atan-domain')
    need(terms > 0 and terms % 2 == 0, 'atan-truncation-parity')
    # At both endpoints the alternating 20-term sum is below atan; next term above.
    # Interval evaluation encloses those endpoint sums and the omitted term.
    total = Interval(0)
    for k in range(terms):
        term = (z**(2*k+1))/Q(2*k+1)
        total = total + (term if k % 2 == 0 else -term)
    nextterm = (z**(2*terms+1))/Q(2*terms+1)
    return Interval(total.lo, (total+nextterm).hi)

# Sparse rational polynomial arithmetic: variables (t,d,u,m,L).
DIM = 5
class Poly:
    def __init__(self, coeff=None):
        self.c = {k:q(v) for k,v in (coeff or {}).items() if v}
    @staticmethod
    def num(x):
        return x if isinstance(x, Poly) else Poly({(0,)*DIM:q(x)})
    @staticmethod
    def var(i):
        a = [0]*DIM; a[i]=1
        return Poly({tuple(a):Q(1)})
    def __add__(self, other):
        other = self.num(other); v = dict(self.c)
        for k,x in other.c.items(): v[k] = v.get(k,Q(0))+x
        return Poly(v)
    __radd__ = __add__
    def __neg__(self): return Poly({k:-x for k,x in self.c.items()})
    def __sub__(self, o): return self + (-self.num(o))
    def __rsub__(self, o): return self.num(o)-self
    def __mul__(self, o):
        o = self.num(o); z = {}
        for a,x in self.c.items():
            for b,y in o.c.items():
                k=tuple(i+j for i,j in zip(a,b)); z[k]=z.get(k,Q(0))+x*y
        return Poly(z)
    __rmul__ = __mul__
    def __truediv__(self, o):
        need(not isinstance(o, Poly) and q(o) != 0, 'poly-scalar-division')
        return self * (Q(1)/q(o))
    def __pow__(self, n):
        z = Poly.num(1)
        for _ in range(n): z=z*self
        return z
    def diff(self, i):
        z = {}
        for a,x in self.c.items():
            if a[i]:
                b=list(a); b[i]-=1
                z[tuple(b)]=x*a[i]
        return Poly(z)
    def substitute(self, i, expr):
        z=Poly.num(0)
        for a,x in self.c.items():
            b=list(a); k=b[i]; b[i]=0
            z=z+Poly({tuple(b):x})*(Poly.num(expr)**k)
        return z
    def integrate_zero_to(self, i, upper):
        z=Poly.num(0)
        for a,x in self.c.items():
            b=list(a); k=b[i]; b[i]=0
            z=z+Poly({tuple(b):x/Q(k+1)})*(Poly.num(upper)**(k+1))
        return z
    def __eq__(self, o): return self.c == self.num(o).c

def equal_poly(a,b,reason): need(a == b,reason)

m=Q(1,63)
v=m*(1+m)
T2=m+2*m*m
T3=m+6*m*m+6*m**3
T4=m+14*m*m+36*m**3+24*m**4
lo=Q(163006627735070347894185905345794,10**33)
hi=Q(163006627735070347894185905345795,10**33)
ca=Q(9274808134495397323165995922,10**30)
cb=Q(9274808134495397323165995923,10**30)
t40=Q(1882704899884405717532381874371113060926,10**40)
c40=Q(92748081344953973231659959220098184342,10**40)
C0=T3/Q(3)-m*T2/Q(2)

def valid_lambda(l,h):
    need(T2 < Q(1,50) < Q(4,25) < l < h < Q(1,2), 'lambda-domain-order')
    need(h-l == Q(1,10**33), 'lambda-width')

def scalar_field(c, lam):
    rad=lam-v-c*c
    need(rad > 0, 'rounded-radicand-positive')
    S=Quad(0,1,rad)
    t=(S+c-m)/2
    d=(S-c-m)/2
    f=C0+t*v-(Q(4,3)*d**3+2*m*d**2+m*m*d)
    return S,t,d,f

# Evaluate section 6 directly from polynomial strip and tail integrals.
# The arc integrations use I0=integral sqrt(A-y^2) and I1=integral y^2 sqrt(A-y^2).
# The facet is integrated via x=2t-y rather than the author's representation.
def shell_integrals(t,c,S,A):
    t,c,S,A=map(Interval.cast,(t,c,S,A))
    theta=atan_interval(c/S)
    I0=(c*S+A*theta)/2
    I1=(c*(2*c*c-A)*S+A*A*theta)/8
    U=2*t-c
    common=A*c-c**3/3
    arc1=I0-m*c
    arc2=common-2*m*I0+m*m*c
    arc3=A*I0-I1-3*m*common+3*m*m*I0-m**3*c
    arcy2=I1-m*c**3/3
    facet1=(U**2-t**2)/2
    facet2=(U**3-t**3)/3
    facet3=(U**4-t**4)/4
    def primitive_y2x(x): return 2*t*t*x*x-Q(4,3)*t*x**3+x**4/4
    facety2=primitive_y2x(U)-primitive_y2x(t)
    E1=arc1+facet1
    E2=arc2+facet2
    E3=arc3+facet3
    Ey=arcy2+facety2
    Z=8*(E1-t*t/2)+8*t*m+2*T2
    N=Q(2,3)*T4+Q(16,3)*t*T3+4*t*t*T2 + 8*(T2*E1+m*(E2+t**3/3)+E3/3+Ey-t**4/3)
    return N,Z,theta

def upper_shell(t,c):
    need(0 < c < t, 'upper-profile-order')
    Y=2*t-c+m
    need(Y > c, 'upper-profile-slope')
    A=Y*Y+c*c
    N,Z,theta=shell_integrals(t,c,Y,A)
    need(Z.lo > 0, 'upper-mass-positive')
    need(N.lo > 0, 'upper-moment-positive')
    return N,Z,theta

def shell_between(N,Z,l,h):
    need(Z.lo > 0, 'upper-mass-positive')
    need((N-l*Z).lo > 0, 'upper-exceeds-lower')
    need((h*Z-N).lo > 0, 'upper-below-upper')

def rounded_at(c, lam):
    S,t,d,f=scalar_field(c,lam)
    need(c > 0 and d.sign() > 0, 'rounded-interior')
    need((S-c).sign() > 0, 'rounded-slope-domain')
    SI=S.enclosure(); ti=t.enclosure(); di=d.enclosure()
    need(ti.lo > c and di.lo > 0, 'rounded-interval-domain')
    N,Z,theta=shell_integrals(ti,c,SI,lam-v)
    need(Z.lo > 0, 'rounded-mass-positive')
    return N-lam*Z, f, ti, di, SI, theta

def coarse(x, base=10**40):
    x=q(x)
    return [str(Q((x.numerator*base)//x.denominator,base)),
            str(Q(-((-x.numerator*base)//x.denominator),base))]

def check_box(interval, lower, upper, reason):
    need(q(lower) < interval.lo <= interval.hi < q(upper), reason)

def expected_mutation(name, reason, fn, registry):
    try:
        fn()
    except CheckFailure as e:
        need(e.reason == reason, 'mutation-wrong-reason:'+name+':'+e.reason)
        registry[name]={'outcome':'rejected','reason':e.reason}
        return
    raise CheckFailure('mutation-not-rejected:'+name)

# Positive symbolic checks. All are polynomial identities over Q[m,t,d,u,L].
t,d,u,mm,L=[Poly.var(i) for i in range(DIM)]
TT2=mm+2*mm**2
TT3=mm+6*mm**2+6*mm**3
TT4=mm+14*mm**2+36*mm**3+24*mm**4
VV=mm+mm**2
M2=lambda x: x*x+2*mm*x+TT2
M4=lambda x: x**4+4*mm*x**3+6*TT2*x*x+4*TT3*x+TT4
facet=2*t-u
Zfacet=8*(facet-u).integrate_zero_to(2,t)+8*t*mm+2*TT2
Nfacet=Q(2,3)*TT4+Q(16,3)*t*TT3+4*t*t*TT2 + 8*(TT2*facet+mm*(facet**2+u**2)+facet**3/3+u*u*facet-Q(4,3)*u**3).integrate_zero_to(2,t)
equal_poly(Zfacet,2*M2(2*t),'diamond-mass-identity')
equal_poly(Nfacet,Q(2,3)*M4(2*t),'diamond-moment-identity')
P=u**5+5*mm*u**4+(2*mm+12*mm**2)*u**3+(12*mm**3-2*mm)*u**2-mm*(1+2*mm)*(1+6*mm)*u+mm**2*(1+2*mm)
equal_poly(M4(u).diff(2)*M2(u)-M4(u)*M2(u).diff(2),2*P,'diamond-derivative-identity')
tri=((t+d-u)**2+(t+u)**2).integrate_zero_to(2,d/2)
tri_expected=t*t*d+t*d*d+d**3/3
equal_poly(tri,tri_expected,'triangle-boundary-term')
equal_poly(Poly.num(1).integrate_zero_to(2,d/2),d/2,'triangle-mass-slice')
# Upper facet h' has fixed-breakpoint term B and an explicit moving-profile integral.
B=Q(16,3)*TT3+16*t*TT2+16*mm*t*t-8*L*mm
facet_derivative=2*t*t+2*u*u+2*mm*(t+u)+TT2-L
junction=2*t*t+2*d*d+2*mm*(t+d)+TT2
hprime=(B+16*facet_derivative.integrate_zero_to(2,d))/16
poly_p3=Q(4,3)*d**3+2*mm*d*d+mm*mm*d
poly_c0=TT3/3-mm*TT2/2
rc=poly_c0+t*VV-poly_p3
equal_poly(hprime.substitute(4,junction),rc,'rounded-derivative-identity')
equal_poly(poly_p3.diff(1),(2*d+mm)**2,'rounded-second-derivative-identity')
equal_poly(poly_c0,mm/3+Q(3,2)*mm**2+mm**3,'rounded-c0-identity')
# Arc primitive derivatives after multiplying by the positive root r and substituting r^2=A-y^2.
# Here t stands for A and u for y.
equal_poly(((t-u*u)-u*u+t)/2,t-u*u,'arc-I0-derivative')
equal_poly(((6*u*u-t)*(t-u*u)-u*u*(2*u*u-t)+t*t)/8,u*u*(t-u*u),'arc-I1-derivative')

results={}
valid_lambda(lo,hi)
results['domain']={'T2_lt_1_over_50_lt_4_over_25_lt_lo_lt_hi_lt_1_over_2':True,'width':str(hi-lo),'m':str(m),'v':str(v),'T2':str(T2),'T3':str(T3),'T4':str(T4)}
# Field arithmetic positive controls with opposite-sign comparisons and an actual inverse.
q2=Quad(0,1,2)
need((3-2*q2).sign()>0 and (1-q2).sign()<0,'quadratic-sign-control')
qinv=(1+q2)*(1+q2).inverse()
need(qinv.a==1 and qinv.b==0,'quadratic-inverse-control')
results['symbolic']={'diamond_mass_moment':True,'diamond_derivative':True,'triangle_slice_and_mass':True,'rounded_derivative_and_second':True,'c0':True,'arc_I0_I1':True,'quadratic_sign_and_inverse':True}

# Fixed feasible law, with explicit positivity and both sides of its value enclosure.
N,Z,theta=upper_shell(t40,c40)
shell_between(N,Z,lo,hi)
results['upper_law']={'t':str(t40),'c':str(c40),'S':str(2*t40-c40+m),'positive_mass':True,'positive_moment':True,'theta_interval': [str(theta.lo),str(theta.hi)],'N_minus_loZ_lower_coarse':coarse((N-lo*Z).lo),'hiZ_minus_N_lower_coarse':coarse((hi*Z-N).lo)}

# Descartes plus four exact endpoint signs and the interval lower bound.
def M2q(x): return x*x+2*m*x+T2
def M4q(x): return x**4+4*m*x**3+6*T2*x*x+4*T3*x+T4
pc=[m*m*(1+2*m),-m*(1+2*m)*(1+6*m),12*m**3-2*m,2*m+12*m*m,5*m,Q(1)]
def Pq(x): return sum((a*x**i for i,a in enumerate(pc)),Q(0))
a=Q(3761763123,10**10); z=Q(3761763124,10**10)
signs=[sgn(x) for x in reversed(pc)]
need(all(signs) and sum(signs[i]!=signs[i+1] for i in range(5))==2,'diamond-descartes-signs')
need(Pq(0)>0 and Pq(a)<0,'diamond-left-sign')
need(Pq(z)>0 and Pq(1)>0,'diamond-right-sign')
need(M2q(z)>0,'diamond-denominator-positive')
need(M4q(a)>3*hi*M2q(z),'diamond-value-bound')
need(M4q(0)*M2q(1)==M4q(1)*M2q(0),'diamond-periodic-endpoint')
results['diamond']={'coefficient_signs_high_to_low':signs,'a':str(a),'z':str(z),'P0_positive':True,'Pa_negative':True,'Pz_positive':True,'P1_positive':True,'M4a_over_3M2z_minus_hi_lower_coarse':coarse((M4q(a)-3*hi*M2q(z))/(3*M2q(z))),'endpoint_values_equal':True}

# Rounded interval: exact field signs; exact rational outward H and derivative bounds.
Ha,fa,ta,da,Sa,tha=rounded_at(ca,lo)
Hb,fb,tb,db,Sb,thb=rounded_at(cb,lo)
need(fa.sign()<0,'junction-left-sign')
need(fb.sign()>0,'junction-right-sign')
need(ta.hi < tb.lo,'junction-parameter-order')
faI=fa.enclosure()
need(faI.hi<0,'junction-left-interval-sign')
slope=16*max(abs(faI.lo),abs(faI.hi))
width=tb.hi-ta.lo
need(width>0,'junction-width-positive')
tangent=Ha.lo-slope*width
need(tangent>Q(27,10**35),'rounded-tangent-margin')
results['rounded']={'ca':str(ca),'cb':str(cb),'left_derivative_negative_exact_field':True,'right_derivative_positive_exact_field':True,'t_order':True,'left_mass_positive':True,'right_mass_positive':True,'tangent_lower_coarse':coarse(tangent,10**37),'target_margin':str(Q(27,10**35)),'H_at_left_lower_coarse':coarse(Ha.lo,10**37),'slope_abs_upper_coarse':coarse(slope,10**35),'t_interval_width_upper_coarse':coarse(width,10**35)}

# L regime: the derivative lower bound is uniform for all t >= t_U and lambda in bracket.
Lbound=Q(16,3)*T3-8*hi*m
need(Lbound>0,'lowerclip-derivative-positive')
results['lower_clip']={'derivative_lower_bound_exact':str(Lbound),'strictly_positive':True}

# Whole rectangle: S increases with lambda, decreases with c; d and t enclosed by independent corners.
Smin=sqrt_bracket(lo-v-cb*cb)[0]
Smax=sqrt_bracket(hi-v-ca*ca)[1]
need(ca>0 and cb<Smin,'box-slope-domain')
dmin=(Smin-cb-m)/2; dmax=(Smax-ca-m)/2
tmin=(Smin+ca-m)/2; tmax=(Smax+cb-m)/2
need(dmin>0,'box-positive-d')
need((2*dmin+m)**2>v,'box-lambda-monotonicity')
_,_,_,f_cb_hi=scalar_field(cb,hi)
need(f_cb_hi.sign()>0,'box-right-hi-sign')
dbox=Interval(dmin,dmax); tbox=Interval(tmin,tmax)
dL=Q(17899568185394517443007219151,10**29); dH=Q(17899568185394517443007219152,10**29)
tL=Q(18827048998844057175323818743,10**29); tH=Q(18827048998844057175323818744,10**29)
check_box(dbox,dL,dH,'facet-parameter-box')
check_box(tbox,tL,tH,'diagonal-parameter-box')
results['parameter_boxes']={'c':[str(ca),str(cb)],'S_corner_interval':[str(Smin),str(Smax)],'d_enclosure':[str(dmin),str(dmax)],'t_enclosure':[str(tmin),str(tmax)],'c_less_S_and_d_positive':True,'(2d_plus_m)^2_gt_v':True,'f_ca_lo_negative_and_f_cb_hi_positive':True,'d_target':[str(dL),str(dH)],'t_target':[str(tL),str(tH)]}

# Deliberately malformed alternatives, each required to hit its named invariant.
mut={}
expected_mutation('lambda endpoints swapped','lambda-domain-order',lambda:valid_lambda(hi,lo),mut)
expected_mutation('lambda width enlarged','lambda-width',lambda:valid_lambda(lo,lo+Q(2,10**33)),mut)
expected_mutation('diamond right root endpoint moved left','diamond-right-sign',lambda:need(Pq(a)>0,'diamond-right-sign'),mut)
expected_mutation('round tangent derivative sign flipped','rounded-derivative-identity',lambda:equal_poly(hprime.substitute(4,junction),-rc,'rounded-derivative-identity'),mut)
expected_mutation('omitted triangle moment boundary term','triangle-boundary-term',lambda:equal_poly(tri,tri_expected-t*t*d,'triangle-boundary-term'),mut)
expected_mutation('diamond numerator derivative sign flipped','diamond-derivative-identity',lambda:equal_poly(M4(u).diff(2)*M2(u)+M4(u)*M2(u).diff(2),2*P,'diamond-derivative-identity'),mut)
expected_mutation('denominator interval includes zero','denominator-positive',lambda:Interval(1)/Interval(-1,1),mut)
expected_mutation('quadratic division by zero','quadratic-zero-norm',lambda:Quad(1,0,2)/Quad(0,0,2),mut)
expected_mutation('atan odd truncation falsely declared lower','atan-truncation-parity',lambda:atan_interval(Q(1,3),19),mut)
expected_mutation('atan endpoint outside alternating domain','atan-domain',lambda:atan_interval(Q(1),20),mut)
# 21-term partial sum is an upper, not a lower; prove using the 40-term upper.
def wrong_atan_lower():
    x=Q(1,3)
    odd=sum(((-1)**k*x**(2*k+1)/Q(2*k+1) for k in range(21)),Q(0))
    even=sum(((-1)**k*x**(2*k+1)/Q(2*k+1) for k in range(40)),Q(0))
    proven_upper=even+x**81/Q(81)
    need(odd<=proven_upper,'atan-lower-orientation')
expected_mutation('atan upper mislabelled lower','atan-lower-orientation',wrong_atan_lower,mut)
def wrong_sqrt_upper():
    a,b=sqrt_bracket(Q(2))
    need(Q(2)<a*a,'sqrt-orientation')
expected_mutation('sqrt lower mislabelled upper','sqrt-orientation',wrong_sqrt_upper,mut)
expected_mutation('left junction shifted right','junction-left-sign',lambda:need(scalar_field(Q(1,100),lo)[3].sign()<0,'junction-left-sign'),mut)
expected_mutation('right junction shifted left','junction-right-sign',lambda:need(scalar_field(Q(9,1000),lo)[3].sign()>0,'junction-right-sign'),mut)
expected_mutation('diagonal parameter box narrowed by one grid unit','diagonal-parameter-box',lambda:check_box(tbox,tL+Q(1,10**29),tH,'diagonal-parameter-box'),mut)
expected_mutation('facet parameter box narrowed by one grid unit','facet-parameter-box',lambda:check_box(dbox,dL+Q(1,10**29),dH,'facet-parameter-box'),mut)
Nround,Zround,_=upper_shell(Q(1883,10000),Q(93,10000))
expected_mutation('rounded upper-law constants','upper-below-upper',lambda:shell_between(Nround,Zround,lo,hi),mut)
results['negative_controls']=mut
print(json.dumps({'status':'PASS','method':'independent rational intervals, exact quadratic signs and sparse Q polynomial identities','results':results},indent=2,sort_keys=True))
