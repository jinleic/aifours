from itertools import permutations,product
G=list(permutations(range(3)));ix={g:i for i,g in enumerate(G)}
def comp(a,b):return tuple(a[b[i]] for i in range(3))
M=[[ix[comp(a,b)] for b in G] for a in G]
invs=[ix[tuple(g.index(i) for i in range(3))] for g in G]
one=ix[(0,1,2)];swap=ix[(1,0,2)];cycle=ix[(1,2,0)];other=ix[(0,2,1)]
P=((one,swap),(cycle,other));D=list(product(range(2),range(6),range(2)))
def bm(a,b):
 if b==0:return 0
 if a==0:return b+3 if b<=3 else b
 if a<=3:return a if b<=3 else b
 return a if b<=3 else b
def alpha(g,b):return 0 if b==0 else 1+G[g][b-1] if b<=3 else 4+G[g][b-4]
def actor(x,y):
 i,g,l=x;j,h,mu=y;return i,M[M[g][P[l][j]]][h],mu
def mul(x,y):
 a,(i,g,l)=x;b,(j,h,mu)=y
 return bm(a,alpha(M[g][P[l][j]],b)),actor(x[1],y[1])
def oppmap(x):
 a,(i,g,l)=x;return alpha(invs[g],a),(l,g,i)
def mulopp(x,y):
 a,(l,g,i)=x;b,(mu,h,j)=y
 # G^op product g∘P[mu][i] = P[mu][i]g; gamma_k=alpha_(k^-1).
 weight=M[P[mu][i]][g]
 return bm(alpha(invs[weight],b),a),(l,M[M[h][P[mu][i]]][g],j)
H=list(product(range(7),D));images=set(map(oppmap,H))
assert len(H)==len(images)==168
assert all(oppmap(mul(y,x))==mulopp(oppmap(x),oppmap(y)) for x,y in product(H,repeat=2))
assert any(M[g][h]!=M[h][g] for g,h in product(range(6),repeat=2))
print('PASS exact physical opposite isomorphism on168-element S3 host, all28224 products')
print('noncommuting group/sandwich and inverse-action coefficient transform; no abelian shortcut')
