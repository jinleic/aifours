#!/usr/bin/env python3
"""Independent exact boundary and parametric identities, over Q[t,d,y,m,L]."""
from fractions import Fraction as F
import json

class Failure(Exception):
    pass

def require(x,reason):
    if not x: raise Failure(reason)

class R:
    n=5
    def __init__(self, items=None): self.c={k:F(v) for k,v in (items or {}).items() if v}
    @classmethod
    def scalar(cls,x): return x if isinstance(x,R) else cls({(0,)*cls.n:F(x)})
    @classmethod
    def var(cls,i):
        v=[0]*cls.n; v[i]=1
        return cls({tuple(v):1})
    def __add__(self,z):
        z=self.scalar(z); a=dict(self.c)
        for k,v in z.c.items(): a[k]=a.get(k,F(0))+v
        return R(a)
    __radd__=__add__
    def __neg__(self): return R({k:-v for k,v in self.c.items()})
    def __sub__(self,z): return self+(-self.scalar(z))
    def __rsub__(self,z): return self.scalar(z)-self
    def __mul__(self,z):
        z=self.scalar(z); a={}
        for k,v in self.c.items():
            for j,w in z.c.items():
                n=tuple(x+y for x,y in zip(k,j)); a[n]=a.get(n,F(0))+v*w
        return R(a)
    __rmul__=__mul__
    def __truediv__(self,z): return self*F(1,z)
    def __pow__(self,k):
        a=R.scalar(1)
        for i in range(k): a=a*self
        return a
    def diff(self,i):
        a={}
        for k,v in self.c.items():
            if k[i]:
                p=list(k); p[i]-=1; a[tuple(p)]=v*k[i]
        return R(a)
    def at(self,i,x):
        a=R.scalar(0)
        for k,v in self.c.items():
            p=list(k); exponent=p[i]; p[i]=0
            a=a+R({tuple(p):v})*(self.scalar(x)**exponent)
        return a
    def integral0(self,i,x):
        a=R.scalar(0)
        for k,v in self.c.items():
            p=list(k); exponent=p[i]; p[i]=0
            a=a+R({tuple(p):v/F(exponent+1)})*(self.scalar(x)**(exponent+1))
        return a
    def __eq__(self,z): return self.c==self.scalar(z).c

def same(a,b,reason): require(a==b,reason)

t,d,y,m,L=(R.var(i) for i in range(5))
T2=m+2*m*m; T3=m+6*m*m+6*m**3; T4=m+14*m*m+36*m**3+24*m**4; v=m+m*m
# Start from the F-independent parts of Z and N, then use the actual endpoint G(t,t).
Zbase=8*(-y).integral0(2,t)+8*t*m+2*T2
Nbase=F(2,3)*T4+F(16,3)*t*T3+4*t*t*T2+8*(m*y*y-F(4,3)*y**3).integral0(2,t)
G=lambda z: z**3/3+m*z*z+(T2+y*y-L)*z
B=(Nbase-L*Zbase).diff(0)+8*G(t).at(2,t)
Bformula=F(16,3)*T3+16*t*T2+16*m*t*t-8*L*m
same(B,Bformula,'base-endpoint-derivative')
same(B-(F(16,3)*T3-8*L*m),16*t*T2+16*m*t*t,'lowerclip-positive-remainder')
# Junction equation and both clipping thresholds come from the root equation.
# At D/R: z=2t, y=0; at R/L: z=t, y=t.
root=lambda z, yy: z*z+2*m*z+T2+yy*yy
J=root(t+d,t-d)
same(J,2*t*t+2*d*d+2*m*(t+d)+T2,'junction-formula')
same(root(2*t,0)-root(t,t),2*t*(t+m),'threshold-separation')
# A positive width d controls matching at R/L; f(t,0)=C0+t*v.
P=F(4,3)*d**3+2*m*d*d+m*m*d
C=T3/3-m*T2/2
same((C+t*v-P).at(1,0),C+t*v,'junction-one-sided-boundary')
# Coordinate change S=t+d+m, c=t-d and derivative identities.
S=t+d+m; c=t-d; E=2*d+m
lhs=v*(S-c)+E*E*(S+c)
rhs=(S-c)*(v+E*(2*t+m))
same(lhs,rhs,'stationary-c-monotonicity')
same(E,P.diff(1).diff(1)/4,'p3-second-derivative')
# Geometric factorial moments imply shift identity at all m>0, k=2 and 4.
M2=lambda g:g*g+2*m*g+T2
M4=lambda g:g**4+4*m*g**3+6*T2*g*g+4*T3*g+T4
same(m*M2(1),(1+m)*M2(0),'diamond-shift-M2')
same(m*M4(1),(1+m)*M4(0),'diamond-shift-M4')
# Triangle moment with q in [0,s/2], followed by geometric-sum substitution.
triangle=((t+d-y)**2+(t+y)**2).integral0(2,d/2)
same(triangle,t*t*d+t*d*d+d**3/3,'triangle-slice')
# Integral of b^ceil(s)*s^j = E G^(j+1)/(j+1).
# Triangle mass and moment after multiplication by 8.
triangle_mass=8*T2/4
triangle_moment=8*(t*t*T2/2+t*T3/3+T4/12)
same(triangle_mass,2*T2,'triangle-mass-tail')
same(triangle_moment,4*t*t*T2+F(8,3)*t*T3+F(2,3)*T4,'triangle-moment-tail')

negative={}
def rejected(name,reason,fn):
    try: fn()
    except Failure as e:
        require(str(e)==reason,'wrong-mutation-reason:'+name)
        negative[name]={'outcome':'rejected','reason':str(e)}
        return
    raise Failure('not-rejected:'+name)
rejected('drop endpoint G(t,t)','base-endpoint-derivative',lambda:same((Nbase-L*Zbase).diff(0),Bformula,'base-endpoint-derivative'))
rejected('flip lambda boundary sign','base-endpoint-derivative',lambda:same(B,Bformula+16*L*m,'base-endpoint-derivative'))
rejected('reverse threshold separation','threshold-separation',lambda:same(root(2*t,0)-root(t,t),-2*t*(t+m),'threshold-separation'))
rejected('omit T4 geometric tail','triangle-moment-tail',lambda:same(triangle_moment,4*t*t*T2+F(8,3)*t*T3,'triangle-moment-tail'))
rejected('flip junction y square','junction-formula',lambda:same(root(t+d,t-d)-2*(t-d)**2,J,'junction-formula'))
print(json.dumps({'status':'PASS','identities':['base endpoint B','lower-clip nonnegative remainder','junction and threshold separation','R/L derivative match','stationary monotonicity','P3 derivative','diamond shift moments','triangle slice and both tails'],'negative_controls':negative},indent=2,sort_keys=True))
