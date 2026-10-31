from itertools import product
# NonGLOBALREG rightSN band B_{0,1,2}: x=0,u_i=1+i,v_i=4+i.
def bm(a,b):
 if b==0:return 0
 if a==0:return b+3 if b<=3 else b
 return a if b<=3 else b
B=list(range(7));G=list(product(range(3),range(2)));P=[[0,1],[2,0]]
def gm(x,y):return((x[0]+(-1 if x[1] else 1)*y[0])%3,x[1]^y[1])
def action(x,b):
 if b==0:return 0
 offset=1 if b<=3 else 4;return offset+(x[0]+(-1 if x[1] else 1)*(b-offset))%3
D1=list(product(range(2),range(3),range(2)));D2=list(product(range(2),repeat=3))
def dm1(x,y):
 i,g,l=x;j,h,u=y;return(i,(g+P[l][j]+h)%3,u)
def dm2(x,y):
 i,g,l=x;j,h,u=y;return(i,g^(l&j)^h,u)
def theta(h,d):return(d[0]^h,(-d[1])%3 if h else d[1],d[2]^h)
def inner(x,y):
 b,(i,g,l)=x;c,(j,h,u)=y;w=(g+P[l][j])%3;return(bm(b,action((w,0),c)),dm1(x[1],y[1]))
def outeraction(h,x):return(action((0,h),x[0]),theta(h,x[1]))
V=list(product(B,D1));N=list(product(V,D2))
def nm(x,y):
 j,h,u=x[1];k,t,v=y[1];w=h^(u&k);return(inner(x[0],outeraction(w,y[0])),dm2(x[1],y[1]))
def flatten(x):
 (b,(i,g,l)),(j,h,u)=x;return(b,((i,j),(g,h),(l^h,u)))
def target(x,y):
 b,(r,g,c)=x;d,(s,h,v)=y;lam,mu=c;i,j=s;q=mu&j
 sandwich=(P[lam][i^q],q);weight=gm(g,sandwich)
 return(bm(b,action(weight,d)),(r,gm(weight,h),v))
assert len(N)==672 and len(set(map(flatten,N)))==672
assert all(bm(b,b)==b for b in B)
assert all(bm(bm(a,b),c)==bm(a,bm(b,c)) and bm(bm(a,b),c)==bm(bm(bm(bm(a,c),a),b),c) for a,b,c in product(B,repeat=3))
assert any(bm(bm(bm(bm(a,b),a),c),a)!=bm(bm(bm(a,b),c),a) for a,b,c in product(B,repeat=3))
assert all(gm(gm(g,h),k)==gm(g,gm(h,k)) for g,h,k in product(G,repeat=3))
assert any(gm(g,h)!=gm(h,g) for g,h in product(G,repeat=2))
assert all(action(g,action(h,b))==action(gm(g,h),b) for g,h,b in product(G,G,B))
assert all(action(g,bm(b,c))==bm(action(g,b),action(g,c)) for g,b,c in product(G,B,B))
assert all(theta(h,dm1(x,y))==dm1(theta(h,x),theta(h,y)) for h,x,y in product(range(2),D1,D1))
assert all(outeraction(h,inner(x,y))==inner(outeraction(h,x),outeraction(h,y)) for h,x,y in product(range(2),V,V))
for x,y in product(N,repeat=2):assert flatten(nm(x,y))==target(flatten(x),flatten(y))
print('PASS band7 RIGHTSN nonGLOBALREG; compatible C3/C2 actions and nonabelian semidirect group S3')
print('PASS nontrivialrow/columnpermutations,inversiononC3,andbothnontrivialReessandwichmatrices')
print('PASS whole672element nestedhost to672element singleCSactorhost:bijective and ALL451584products')
print('RESULT targetbandSAME7, finalCSactor96 withgroupS3,rows4,cols4; WRITTENgeneralflatteningrequiredforuniversalclaim')
