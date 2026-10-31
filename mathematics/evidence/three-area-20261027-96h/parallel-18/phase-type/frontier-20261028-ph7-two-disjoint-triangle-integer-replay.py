#!/usr/bin/env python3
"""Independent stdlib reconstruction/replay of two-triangle Q/H certificates.

Rebuilds all formulas using Fraction monomial dictionaries, binds frozen
coefficient digests, checks complete prefix covers, integer Bernstein signs,
and strictness at every admissible interior box vertex.
"""
import hashlib,itertools,json,math,time
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
HC=json.loads((ROOT/'frontier-20261028-ph7-two-disjoint-triangle-universal-H-certificate-v1.json').read_text())
QC=json.loads((ROOT/'frontier-20261028-ph7-two-disjoint-triangle-universal-Q-certificate-v1.json').read_text())
n=7;zero=(0,)*n

def clean(a):return {k:v for k,v in a.items()if v}
def const(x):return {zero:Q(x)}if x else{}
def add(a,b):
    out=a.copy()
    for k,v in b.items():out[k]=out.get(k,Q(0))+v
    return clean(out)
def scale(a,c):return clean({k:v*Q(c)for k,v in a.items()})
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
    out={}
    for k,x in a.items():
        for l,y in b.items():
            key=tuple(k[i]+l[i]for i in range(n));out[key]=out.get(key,Q(0))+x*y
    return clean(out)
def total(*items):
    out={}
    for item in items:out=add(out,item)
    return out
def prod(items):
    out=const(1)
    for item in items:out=mul(out,item)
    return out
U=[]
for i in range(6):
    key=[0]*n;key[i]=1;U.append({tuple(key):Q(1)})
theta={(0,0,0,0,0,0,1):Q(1)}
f=[]
for k in range(1,5):
    val={}
    for term in itertools.combinations(U,k):val=add(val,prod(term))
    f.append(val)
f1,f2,f3,f4=f;wa=prod(U[:3]);pB=prod(U[3:]);wb=mul(theta,pB);W=add(wa,wb)
A=total(f2,scale(f1,-4),const(Q(74,9)))
B0=total(f3,scale(f2,-4),scale(f1,Q(74,9)),const(Q(-28,3)))
B=sub(B0,W)
H0=total(f4,scale(f2,Q(-70,9)),scale(f1,Q(212,9)),const(Q(-1007,27)),scale(mul(wa,total(*U[3:])),-1),scale(mul(wb,total(*U[:3])),-1))
H1=total(f3,scale(f1,Q(-70,9)),const(Q(212,9)),scale(W,-1))
HH=scale(sub(mul(H0,A),mul(H1,B)),-243)
q11=scale(sub(mul(A,A),mul(sub(f1,const(4)),sub(B0,add(wa,pB)))),81)

def bytheta(p,degree):
    out=[{}for _ in range(degree+1)]
    for key,val in p.items():assert key[-1]<=degree;out[key[-1]][key[:-1]]=val
    return out
def add6(a,b):
    out=a.copy()
    for k,v in b.items():out[k]=out.get(k,Q(0))+v
    return clean(out)
def scale6(a,c):return clean({k:v*Q(c)for k,v in a.items()})
def mul6(a,b):
    out={}
    for k,x in a.items():
        for l,y in b.items():
            key=tuple(k[i]+l[i]for i in range(6));out[key]=out.get(key,Q(0))+x*y
    return clean(out)
h=bytheta(HH,2);H0p=h[0];H1p=add6(scale6(h[0],2),h[1]);H2p=add6(add6(h[0],h[1]),h[2])
Gram=add6(scale6(mul6(H0p,H2p),4),scale6(mul6(H1p,H1p),-1))
Q11=bytheta(q11,0)[0];polys={'H0':H0p,'H2':H2p,'H1_twice':H1p,'Gram4':Gram,'Q11':Q11}

def digest(poly):
    assert all(x.denominator==1 for x in poly.values())
    rows=[[list(k),str(int(c))]for k,c in sorted(poly.items())]
    return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
for rec in HC['records']:
    p=polys[rec['name']];assert len(p)==rec['terms'] and digest(p)==rec['sha256']
assert len(Q11)==QC['terms'] and digest(Q11)==QC['sha256']

def grid(poly,degree):
    n=6;m=degree+1;stride=[m**(n-1-i)for i in range(n)];common=math.lcm(*(math.comb(degree,i)for i in range(m)))**n;arr=[0]*(m**n)
    for key,val in poly.items():
        div=math.prod(math.comb(degree,key[j])for j in range(n));assert common%div==0
        arr[sum(key[j]*stride[j]for j in range(n))]=int(val)*(common//div)
    return arr,m,stride

def split(arr,m,stride,axis):
    L=[0]*len(arr);R=[0]*len(arr);d=m-1;other=[j for j in range(6)if j!=axis]
    for coord in itertools.product(range(m),repeat=5):
        base=sum(coord[k]*stride[other[k]]for k in range(5));idx=[base+j*stride[axis]for j in range(m)];lev=[[arr[i]for i in idx]]
        while len(lev[-1])>1:lev.append([x+y for x,y in zip(lev[-1],lev[-1][1:])])
        for k in range(m):L[idx[k]]=lev[k][0]*(1<<(d-k));R[idx[k]]=lev[d-k][-1]*(1<<k)
    return L,R

def vertex(arr,m,stride,bounds):
    inside=0
    for corner in itertools.product((0,1),repeat=6):
        coord=[bounds[j][corner[j]]for j in range(6)]
        if all(0<x<1 for x in coord):
            inside+=1;idx=sum((0 if corner[j]==0 else m-1)*stride[j]for j in range(6))
            if arr[idx]<=0:return False
    return inside>0

def single(poly,paths):
    assert len(paths)==len(set(paths));leaves=set(paths);prefix={p[:j]for p in leaves for j in range(len(p)+1)};seen=set();arr,m,stride=grid(poly,2)
    def walk(path,A,bounds):
        dep=len(path)
        if path in leaves:seen.add(path);assert dep>=6 and min(A)>=0 and vertex(A,m,stride,bounds);return
        assert path+'0'in prefix and path+'1'in prefix;axis=dep%6;L,R=split(A,m,stride,axis);lo,hi=bounds[axis];mid=(lo+hi)/2
        z=list(bounds);z[axis]=(lo,mid);walk(path+'0',L,tuple(z));z=list(bounds);z[axis]=(mid,hi);walk(path+'1',R,tuple(z))
    walk('',arr,tuple((Q(0),Q(1))for _ in range(6)));assert seen==leaves
    return len(seen)

def dual():
    pos=set(HC['dual_mid_nonnegative_paths']);gram=set(HC['dual_gram_strict_paths']);assert not(pos&gram)
    leaves=pos|gram;prefix={p[:j]for p in leaves for j in range(len(p)+1)};gp={p[:j]for p in gram for j in range(len(p)+1)};seen=set()
    h,mh,sh=grid(H1p,2);g,mg,sg=grid(Gram,4)
    def walk(path,H,G,bounds):
        dep=len(path)
        if path in pos:seen.add(path);assert H is not None and min(H)>=0;return
        if path in gram:seen.add(path);assert dep>=6 and G is not None and min(G)>=0 and vertex(G,mg,sg,bounds);return
        assert path+'0'in prefix and path+'1'in prefix;axis=dep%6;lo,hi=bounds[axis];mid=(lo+hi)/2
        HL,HR=split(H,mh,sh,axis)if H is not None else(None,None)
        if G is not None and (path+'0'in gp or path+'1'in gp):GL,GR=split(G,mg,sg,axis)
        else:GL=GR=None
        for bit,h,g,inter in [('0',HL,GL,(lo,mid)),('1',HR,GR,(mid,hi))]:
            z=list(bounds);z[axis]=inter;walk(path+bit,h,g if path+bit in gp else None,tuple(z))
    walk('',h,g,tuple((Q(0),Q(1))for _ in range(6)));assert seen==leaves
    return len(pos),len(gram)

start=time.monotonic();counts=[]
for rec in HC['records'][:2]:
    count=single(polys[rec['name']],rec['strict_paths']);counts.append(count);print(rec['name'],'strict leaves',count,flush=True)
qcount=single(Q11,QC['strict_paths']);print('Q11 strict leaves',qcount,flush=True)
d=dual();print('dual nonnegative/strict leaves',*d,flush=True)
assert counts==[2443,2141] and qcount==1338 and d==(2693,445)
print('PASS: independent Fraction/stdlib reconstruction, hashes, full covers, Bernstein signs and interior strictness')
print('elapsed_seconds',time.monotonic()-start)
