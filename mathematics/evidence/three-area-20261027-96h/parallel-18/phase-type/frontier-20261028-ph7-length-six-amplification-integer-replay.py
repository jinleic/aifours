#!/usr/bin/env python3
"""Independent stdlib reconstruction and integer replay of amplification covers.

Rebuilds all source polynomials with Fraction dictionaries, reconstructs the
four-cone blowup and quadratic compactification, binds each coefficient hash,
and checks every leaf plus complete prefix coverage of the frozen JSON.
"""
from fractions import Fraction as F
from itertools import product
from math import comb,lcm
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
CERT=ROOT/'frontier-20261028-ph7-length-six-amplification-certificate-v1.json'


class P:
    def __init__(self,n,d=None):self.n=n;self.d={k:F(v)for k,v in (d or {}).items()if v}
    @staticmethod
    def c(n,value):return value if isinstance(value,P) else P(n,{(0,)*n:F(value)})
    def __add__(self,other):
        other=P.c(self.n,other);out=dict(self.d)
        for k,v in other.d.items():out[k]=out.get(k,F(0))+v
        return P(self.n,out)
    __radd__=__add__
    def __neg__(self):return P(self.n,{k:-v for k,v in self.d.items()})
    def __sub__(self,other):return self+-P.c(self.n,other)
    def __rsub__(self,other):return P.c(self.n,other)-self
    def __mul__(self,other):
        other=P.c(self.n,other);out={}
        for (a,x),(b,y) in product(self.d.items(),other.d.items()):
            k=tuple(i+j for i,j in zip(a,b));out[k]=out.get(k,F(0))+x*y
        return P(self.n,out)
    __rmul__=__mul__
    def __pow__(self,k):
        out=P.c(self.n,1)
        for _ in range(k):out=out*self
        return out
    def degrees(self):return tuple(max(k[i]for k in self.d) for i in range(self.n))


def var(n,i):return P(n,{tuple(int(j==i)for j in range(n)):1})


def compact(p,which):
    n=p.n;u=[var(n,i)for i in range(n)];deg=p.degrees();out=P.c(n,0)
    for ex,c in p.d.items():
        term=P.c(n,c)
        for i in range(n):
            term=term*u[i]**ex[i]
            if i in which:term=term*(1-u[i])**(deg[i]-ex[i])
        out=out+term
    return out


def substitute(p,exprs):
    n=exprs[0].n;out=P.c(n,0)
    for ex,c in p.d.items():
        term=P.c(n,c)
        for f,k in zip(exprs,ex):term=term*f**k
        out=out+term
    return out


def blowup(p,pivot):
    s=var(4,0);vs=[var(4,i)for i in (1,2,3)];it=iter(vs)
    e=[s if i==pivot else s*next(it) for i in range(4)]
    q=substitute(p,[1-x for x in e]);assert all(k[0]>=2 for k in q.d)
    return P(4,{(k[0]-2,)+k[1:]:c for k,c in q.d.items()})


def triangle(m,bound):
    a,b,c,t=[var(4,i)for i in range(4)];z=F(8,9);x,y,w=a-1,b-1,c-1
    re=x*y*w-z*(x+y+w)-t*a*b*c;im=x*y+x*w+y*w-z
    norm=re**2+z*im**2;rates=[a,b,c];num=(1-t)**2
    for i,r in enumerate(rates):num=num*(r**2 if i<m else (r-1)**2+z)
    return bound*norm-num


def quad():
    h,eta=var(2,0),var(2,1);z=F(8,9);v2=h*h*eta*F(1,3)
    den=((h-1)**2-z+v2)**2+4*z*(h-1)**2
    return compact(F(225,16)*den-(h*h+v2)**2,{0})


def digest(p):
    rows=[[list(k),str(v)]for k,v in sorted(p.d.items())]
    return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()


def grid(p):
    ds=p.degrees();den=lcm(*(c.denominator for c in p.d.values()));scale=den
    for d in ds:scale*=lcm(*(comb(d,j)for j in range(d+1)))
    out={key:0 for key in product(*(range(d+1)for d in ds))}
    for ex,c in p.d.items():
        div=1
        for d,k in zip(ds,ex):div*=comb(d,k)
        assert scale%div==0;v=c*(scale//div);assert v.denominator==1;v=int(v)
        for key in product(*(range(e,d+1)for e,d in zip(ex,ds))):
            t=v
            for j,e in zip(key,ex):t*=comb(j,e)
            out[key]+=t
    return out


def split(A,ds,axis):
    L={};R={};others=[i for i in range(len(ds))if i!=axis];d=ds[axis]
    for xyz in product(*(range(ds[i]+1)for i in others)):
        key=[0]*len(ds)
        for i,v in zip(others,xyz):key[i]=v
        levels=[];row=[]
        for k in range(d+1):key[axis]=k;row.append(A[tuple(key)])
        levels.append(row)
        while len(levels[-1])>1:levels.append([a+b for a,b in zip(levels[-1],levels[-1][1:])])
        for k in range(d+1):
            key[axis]=k;L[tuple(key)]=levels[k][0]*(1<<(d-k));R[tuple(key)]=levels[d-k][-1]*(1<<k)
    return L,R


def replay(p,paths):
    assert len(set(paths))==len(paths);leaves=set(paths);prefixes={p[:i]for p in paths for i in range(len(p)+1)};ds=p.degrees()
    def walk(path,A):
        assert path in prefixes
        if path in leaves:
            assert all(c>=0 for c in A.values()),('negative coefficient',path)
            assert path+'0' not in prefixes and path+'1' not in prefixes
            return 1
        left,right=split(A,ds,len(path)%len(ds))
        return walk(path+'0',left)+walk(path+'1',right)
    count=walk('',grid(p));assert count==len(paths);return count

cert=json.loads(CERT.read_text());assert cert['z']=='8/9' and len(cert['records'])==9
for rec in cert['records']:
    name=rec['name']
    if name=='quadratic':p=quad()
    else:
        assert name in ('full3','partial2') and 0<=rec['pivot']<4
        m,b=(3,F(16)) if name=='full3' else (2,F(45369,10000))
        p=blowup(compact(triangle(m,b),{0,1,2}),rec['pivot'])
    assert list(p.degrees())==rec['degrees'] and digest(p)==rec['sha256'],name
    n=replay(p,rec['leaves']);print(name,'pivot',rec.get('pivot'), 'leaves',n,flush=True)
print('PASS: independently reconstructed exact polynomials, coefficient hashes, complete cover and integer Bernstein signs')
