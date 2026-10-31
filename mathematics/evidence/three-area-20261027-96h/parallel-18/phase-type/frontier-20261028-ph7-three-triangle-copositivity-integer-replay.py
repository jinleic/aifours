#!/usr/bin/env python3
"""Independent stdlib exact reconstruction/replay of 3-triangle simplex proof.

Reconstructs all polynomials from the advertised moment formulas, checks
frozen coefficient digests, complete selector-prefix covers, integer Bernstein
signs, and all required strictly positive finite interior vertices.
"""
import hashlib,itertools,json,math,time
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent
C=json.loads((ROOT/'frontier-20261028-ph7-three-triangle-copositivity-certificate-v1.json').read_text())
n=8;zero=(0,)*n

def clean(a):return {k:v for k,v in a.items()if v}
def const(x):return {zero:F(x)}if x else{}
def add(a,b):
    o=a.copy()
    for k,v in b.items():o[k]=o.get(k,F(0))+v
    return clean(o)
def scale(a,c):return clean({k:v*F(c)for k,v in a.items()})
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
    out={}
    for k,x in a.items():
        for l,y in b.items():
            z=tuple(k[i]+l[i]for i in range(n));out[z]=out.get(z,F(0))+x*y
    return clean(out)
def total(*seq):
    out={}
    for v in seq:out=add(out,v)
    return out
def prod(seq):
    out=const(1)
    for v in seq:out=mul(out,v)
    return out

def var(i):return {tuple(int(j==i)for j in range(n)):F(1)}
U=[var(i)for i in range(6)];ta,tb=var(6),var(7)
f=[]
for k in range(1,5):
    val={}
    for z in itertools.combinations(U,k):val=add(val,prod(z))
    f.append(val)
f1,f2,f3,f4=f;wa=mul(ta,prod(U[:3]));wb=mul(tb,prod(U[3:]));W=add(wa,wb)
A=total(f2,scale(f1,-4),const(F(74,9)))
B=total(f3,scale(f2,-4),scale(f1,F(74,9)),const(F(-28,3)),scale(W,-1))
h0=total(f4,scale(f2,F(-70,9)),scale(f1,F(212,9)),const(F(-1007,27)),scale(mul(wa,total(*U[3:])),-1),scale(mul(wb,total(*U[:3])),-1))
h1=total(f3,scale(f1,F(-70,9)),const(F(212,9)),scale(W,-1))
T=total(U[1],U[2],U[4],U[5]);krel=prod([sub(const(1),ta),U[0],U[3]])
H=scale(sub(mul(h0,sub(A,krel)),mul(sub(h1,mul(krel,T)),B)),-243)
assert all(key[6]+key[7]<=2 for key in H)

def evaltheta(p,a,b):
    out={}
    for key,val in p.items():
        k=key[:6];out[k]=out.get(k,F(0))+val*F(a)**key[6]*F(b)**key[7]
    return clean(out)
def add6(a,b):
    out=a.copy()
    for k,v in b.items():out[k]=out.get(k,F(0))+v
    return clean(out)
def scale6(a,c):return clean({k:v*F(c)for k,v in a.items()})
def sub6(a,b):return add6(a,scale6(b,-1))
def mul6(a,b):
    out={}
    for k,x in a.items():
        for l,y in b.items():
            z=tuple(k[i]+l[i]for i in range(6));out[z]=out.get(z,F(0))+x*y
    return clean(out)
verts=[(0,0),(1,0),(1,1)];D=[evaltheta(H,*v)for v in verts];pairs=[(0,1),(0,2),(1,2)];O=[]
for i,j in pairs:
    a=F(verts[i][0]+verts[j][0],2);b=F(verts[i][1]+verts[j][1],2)
    O.append(sub6(scale6(evaltheta(H,a,b),4),add6(D[i],D[j])))
G=[sub6(scale6(mul6(D[i],D[j]),4),mul6(O[k],O[k]))for k,(i,j)in enumerate(pairs)]
C12=sub6(scale6(mul6(O[2],D[0]),2),mul6(O[0],O[1]))
C01=sub6(scale6(mul6(O[0],D[2]),2),mul6(O[1],O[2]))
polys={**{f'D{i}':p for i,p in enumerate(D)},**{f'O{i}':p for i,p in enumerate(O)},**{f'G{i}':p for i,p in enumerate(G)},'C12':C12,'C01':C01}

def digest(poly):
    assert all(x.denominator==1 for x in poly.values())
    rows=[[list(k),str(int(c))]for k,c in sorted(poly.items())]
    return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()
for name,rec in C['records'].items():
    p=polys[name];assert len(p)==rec['terms'] and digest(p)==rec['sha256']
    assert rec['degrees']==[2]*6 if name.startswith(('D','O')) else rec['degrees']==[4]*6

def grid(poly,degree):
    m=degree+1;stride=[m**(5-i)for i in range(6)];common=math.lcm(*(math.comb(degree,j)for j in range(m)))**6;arr=[0]*(m**6)
    for key,c in poly.items():
        div=math.prod(math.comb(degree,k)for k in key);assert common%div==0
        arr[sum(key[j]*stride[j]for j in range(6))]=int(c)*(common//div)
    return arr,m,stride

def split(arr,m,stride,axis):
    L=[0]*len(arr);R=[0]*len(arr);d=m-1;other=[j for j in range(6)if j!=axis]
    for coord in itertools.product(range(m),repeat=5):
        base=sum(coord[k]*stride[other[k]]for k in range(5));idx=[base+j*stride[axis]for j in range(m)];lev=[[arr[i]for i in idx]]
        while len(lev[-1])>1:lev.append([x+y for x,y in zip(lev[-1],lev[-1][1:])])
        for k in range(m):L[idx[k]]=lev[k][0]*(1<<(d-k));R[idx[k]]=lev[d-k][-1]*(1<<k)
    return L,R

def vertex(arr,m,stride,bounds):
    found=False
    for corner in itertools.product((0,1),repeat=6):
        xyz=[bounds[j][corner[j]]for j in range(6)]
        if all(0<x<1 for x in xyz):
            found=True;idx=sum((0 if corner[j]==0 else m-1)*stride[j]for j in range(6))
            if arr[idx]<=0:return False
    return found

def cover(rec):
    names=rec['names'];strict=rec['strict'];paths=rec['paths'];assert len(names)==len(strict)==len(paths)
    leaves=[set(p)for p in paths];assert all(len(a)==len(b)for a,b in zip(leaves,paths))
    union=set().union(*leaves);assert len(union)==sum(map(len,leaves))
    prefs=[{p[:j]for p in ls for j in range(len(p)+1)}for ls in leaves];prefix=set().union(*prefs);seen=set()
    initial=[grid(polys[name],2 if name.startswith(('D','O'))else 4)for name in names]
    sizes=[(m,st)for _,m,st in initial];arrays=[a for a,_,_ in initial]
    def walk(path,arr,bounds):
        dep=len(path)
        for i,ls in enumerate(leaves):
            if path in ls:
                seen.add(path);assert arr[i] is not None and min(arr[i])>=0
                if strict[i]:assert dep>=6 and vertex(arr[i],*sizes[i],bounds)
                assert path+'0' not in prefix and path+'1' not in prefix
                return
        assert path+'0'in prefix and path+'1'in prefix;axis=dep%6;lo,hi=bounds[axis];mid=(lo+hi)/2
        splitarrays=[]
        for i,a in enumerate(arr):
            if a is not None and (path+'0'in prefs[i] or path+'1'in prefs[i]):splitarrays.append(split(a,*sizes[i],axis))
            else:splitarrays.append((None,None))
        for bit,index,inter in [('0',0,(lo,mid)),('1',1,(mid,hi))]:
            z=list(bounds);z[axis]=inter;child=path+bit
            walk(child,[parts[index]if child in prefs[i]else None for i,parts in enumerate(splitarrays)],tuple(z))
    walk('',arrays,tuple((F(0),F(1))for _ in range(6)));assert seen==union
    return [len(x)for x in leaves]

expected=[(['D0'],[True]),(['D1'],[True]),(['D2'],[True]),(['O0','G0'],[False,True]),(['O1','G1'],[False,True]),(['O2','G2'],[False,True]),(['O0','O2'],[False,False]),(['O0','O1','C12'],[False,False,False]),(['O1','O2','C01'],[False,False,False])]
assert len(C['covers'])==len(expected)
start=time.monotonic();total_leaves=0
for rec,(names,strict)in zip(C['covers'],expected):
    assert rec['names']==names and rec['strict']==strict
    counts=cover(rec);total_leaves+=sum(counts);print('/'.join(names),'checked',counts,flush=True)
print('PASS: independently reconstructed 11 polynomials, complete 9 selector covers and',total_leaves,'exact leaves')
print('elapsed_seconds',time.monotonic()-start)
