from itertools import permutations,product
G=list(permutations(range(3)));one=(0,1,2);swap=(1,0,2);cycle=(1,2,0)
def comp(a,b):return tuple(a[b[i]] for i in range(3))
def inv(a):return tuple(a.index(i) for i in range(3))
def phi(bit):return swap if bit else one
I=(0,2);L=(0,2);ag=(one,cycle);bg=(swap,one)
P1=((0,0),(0,1))
P0=[[one]*3 for _ in range(3)]
for l,i in product(range(2),repeat=2):P0[L[l]][I[i]]=comp(comp(inv(bg[l]),phi(P1[l][i])),inv(ag[i]))
D1=list(product(range(2),repeat=3))
def m1(x,y):
 i,g,l=x;j,h,mu=y;return i,g^P1[l][j]^h,mu
def m0(x,y):
 i,g,l=x;j,h,mu=y;return i,comp(comp(g,P0[l][j]),h),mu
def mapactor(x):
 i,g,l=x;return I[i],comp(comp(ag[i],phi(g)),bg[l]),L[l]
def cprime(x):return one if x[0]==0 else swap
def c(x):return comp(ag[x[0]],cprime(x))
def action(g,b):return comp(g,b)
for x,y in product(D1,repeat=2):
 assert mapactor(m1(x,y))==m0(mapactor(x),mapactor(y))
 i,g,l=mapactor(x);j,h,mu=mapactor(y);w0=comp(g,P0[l][j])
 assert c(m1(x,y))==c(x)  # left-zero band multiplication
 lifted=action(inv(ag[x[0]]),c(x));lifted_y=action(inv(ag[y[0]]),c(y))
 assert lifted==cprime(x) and lifted_y==cprime(y)
 assert action(inv(ag[m1(x,y)[0]]),c(m1(x,y)))==lifted
 assert action(comp(comp(inv(ag[x[0]]),w0),ag[y[0]]),one)==action(phi(x[1]^P1[x[2]][y[0]]),one)
assert len(set(mapactor(x) for x in D1))==8
assert any(c(x)!=cprime(x) for x in D1)
assert len(D1)==8 and len(G)*3*3==54
print('PASS 64 Rees-hom and gauge equations, nontrivial row transforms, pure nononto actor 8→54')
print('source C2 maps into nonnormal order-2 subgroup of S3; same left-zero band size=6')
