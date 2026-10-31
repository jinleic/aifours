from fractions import Fraction as F

# Polynomials are coefficient lists in ascending order, all exact rationals.
def trim(a):
    a = list(map(F, a))
    while len(a)>1 and a[-1] == 0: a.pop()
    return a

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def scale(a,c): return trim([F(c)*x for x in a])
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)

def der(a): return trim([i*a[i] for i in range(1,len(a))] or [0])
def value(a,t): return sum((c*t**i for i,c in enumerate(a)),F(0))
def integ(a,t): return sum((c*t**(i+1)/F(i+1) for i,c in enumerate(a)),F(0))
def mm(a,b): return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]

# Example 1: physical single visible state, nonzero diffusion, two controls.
sigma=F(1,2); B=[F(1),F(0)]; B0=[F(0),sigma]; D1=[F(0),F(1)]; L0=[F(1),F(0)]; H=[F(0),F(-1)]; C=F(-1); O=F(1); Q=sigma
dot=lambda a,b: sum((x*y for x,y in zip(a,b)),F(0))
impulse=dot(B,L0); after=impulse+C
early_output=dot(D1,H)+O*impulse
early_noise=dot(B0,H)+Q*impulse
assert (impulse,after,early_output,early_noise)==(1,0,0,0)
assert dot(B0,H)!=0 and Q!=0
print('scalar/noisy: impulse',impulse,'late endpoint',after,'early output',early_output,'early diffusion',early_noise)

# Example 2: P=[[0,1],[0,0]], Bbar=e2; O=[1,0].
# The observability matrix [O; OP] is I: N=0, with C=e1 and h=0 range=e2.
obs=[[F(1),F(0)],[F(0),F(1)]]
assert obs[0][0]*obs[1][1]-obs[0][1]*obs[1][0]==1
for h in [F(1,2),F(1),F(2),F(3,2)]:
    heavy1=[-F(6)/h**2,F(12)/h**3]
    heavy2=[0,0,F(3)/h**2,-F(2)/h**3]
    m1=scale(heavy2,-1); m2=der(m1)
    assert der(m1)==m2 and der(m2)==trim(heavy1)
    assert add(m1,heavy2)==[0]
    assert (value(m1,h)+1,value(m2,h))==(0,0)
    energy=integ(add(mul(heavy1,heavy1),mul(heavy2,heavy2)),h)
    assert energy==F(12)/h**3+F(13)*h/35
    wh=[[h**3/3,h**2/2],[h**2/2,h]]
    whinv=[[F(12)/h**3,-F(6)/h**2],[-F(6)/h**2,F(4)/h]]
    assert mm(wh,whinv)==[[1,0],[0,1]]
    rho=[[-F(1)],[F(0)]]
    gramcoef=mm(whinv,rho)
    # Bc^T exp(P^T(h-t))=[h-t,1].
    v=add(scale([h,-1],gramcoef[0][0]),[gramcoef[1][0]])
    assert v==trim(heavy1)
    # Alternative atom-heavy law, with L0=-e1/h and Lh=e1/h.
    a_m1=[F(0),-1/h]; a_m2=[-1/h]; a_H1=[F(0)]; a_H2=[0,1/h]
    assert der(a_m1)==trim(a_m2) and der(a_m2)==a_H1
    assert add(a_m1,a_H2)==[0]
    assert (value(a_m1,h)+1,value(a_m2,h)+1/h)==(0,0)
    assert integ(mul(a_H2,a_H2),h)==h/3
    print('double-integrator h=',h,'heavy energy=',energy,'atom-heavy kernel energy=',h/3,'Gramian=',wh,'Gramian control=',v)

# Matrix feedthrough illustration and exact singular-value square.
e0=[[F(3,5),F(0)],[F(0),F(1,5)]]
eh=[[F(4,5),F(0)],[F(0),F(0)]]
et=lambda a:[[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
g0=mm(et(e0),e0); gh=mm(et(eh),eh)
g=[[g0[i][j]+gh[i][j] for j in range(2)] for i in range(2)]
assert g==[[1,0],[0,F(1,25)]]
print('feedthrough stacked Gramian=',g,'norm=1')

# h=0 scope counterexample: full-column-rank Astar=[1;0], combined tap zero
# although the written pair is nonzero (only the sum is physically meaningful).
a_star=[[F(1)],[F(0)]]; l0=F(1); lh=F(-1)
assert a_star[0][0]!=0 and l0+lh==0 and l0!=0 and lh!=0
print('h=0 full-rank scope: L0=',l0,'Lh=',lh,'sum=',l0+lh,'zero law')
