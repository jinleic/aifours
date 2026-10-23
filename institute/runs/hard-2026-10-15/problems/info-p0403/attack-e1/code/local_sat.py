"""Exact small-radius balancing CNF using binary input indices.

No Python SAT packages are required. Every primary flip index has nine
bits. A lookup table gives its seed value. Shared XOR circuits evaluate
all 512 characters at each selected point; small cardinality clauses
enforce every Walsh bound and at least one zero. Strictly increasing
indices remove permutation duplicates. Only exact even radii 2,4,6 are
used; lower radii are separate exhaustive claims.
"""
import argparse
from itertools import combinations
import hashlib
import json
from pathlib import Path
from seeds import SEEDS,decode,fwht


def neg(v):
    return not v if isinstance(v,bool) else -v


class CNF:
    def __init__(self):
        self.n=0
        self.clauses=[]
        self.blocks=[]
        self.primary={}

    def var(self,role=None):
        self.n+=1
        if role is not None:
            self.primary[role]=self.n
        return self.n

    def block(self,meta,clauses):
        start=len(self.clauses)
        self.clauses.extend(clauses)
        self.blocks.append(dict(meta,start=start,end=len(self.clauses)))

    def gate(self,op,a,b):
        if isinstance(a,bool):
            if op=='xor': return neg(b) if a else b
            if op=='and': return b if a else False
            if op=='or': return True if a else b
        if isinstance(b,bool):
            return self.gate(op,b,a)
        if a==b:
            return False if op=='xor' else a
        if a==-b:
            return False if op=='and' else True
        out=self.var()
        if op=='xor':
            clauses=[[a,b,-out],[-a,-b,-out],[a,-b,out],[-a,b,out]]
        elif op=='and':
            clauses=[[-a,-b,out],[a,-out],[b,-out]]
        elif op=='or':
            clauses=[[a,b,-out],[-a,out],[-b,out]]
        else:
            raise ValueError(op)
        self.block({'kind':'gate','op':op,'out':out,'a':a,'b':b},clauses)
        return out

    def require(self,lits,role):
        if any(v is True for v in lits):
            return
        ls=[v for v in lits if v is not False]
        self.block({'kind':'require','lits':ls,'role':role},[ls])

    def atmost(self,lits,k,role,guard=None):
        assert all(type(v) is int for v in lits)
        if k>=len(lits): return
        clauses=[]
        prefix=[] if guard is None else [-guard]
        if k<0:
            clauses=[prefix]
        else:
            clauses=[prefix+[neg(v) for v in subset] for subset in combinations(lits,k+1)]
        self.block({'kind':'atmost','lits':lits,'k':k,'guard':guard,'role':role},clauses)


def produce(name,r,bound,degree_eight=False,forced=None,zero_origin=None):
    bits=decode(SEEDS[name])
    w=fwht(bits)
    assert set(map(abs,w))=={4,12,20,28}
    assert r in (2,4,6,8,10)
    cnf=CNF()
    xs=[[cnf.var('x%d_%d'%(i,j)) for j in range(9)] for i in range(r)]
    fs=[cnf.var('f%d'%i) for i in range(r)]
    zero_indices=[a for a in range(512) if abs(w[a])<=2*r and (2*r-abs(w[a]))%4==0]
    if zero_origin is not None:
        assert zero_origin in zero_indices
        zero_indices=[zero_origin]
    selectors={a:cnf.var('zero_%d'%a) for a in zero_indices}
    for i in range(r):
        clauses=[]
        for x in range(512):
            clauses.append([(-xs[i][j] if (x>>j)&1 else xs[i][j]) for j in range(9)]+[fs[i] if bits[x] else -fs[i]])
        cnf.block({'kind':'lookup','point':i,'bits':xs[i],'out':fs[i]},clauses)
    less=[]
    for i in range(r-1):
        lt=False
        eq=True
        for j in reversed(range(9)):
            term=cnf.gate('and',eq,cnf.gate('and',neg(xs[i][j]),xs[i+1][j]))
            lt=cnf.gate('or',lt,term)
            eq=cnf.gate('and',eq,neg(cnf.gate('xor',xs[i][j],xs[i+1][j])))
        cnf.require([lt],'strict-order-%d'%i)
        less.append(lt)
    chars=[]
    for i in range(r):
        parity=[False]*512
        for a in range(1,512):
            bit=a&-a
            parity[a]=cnf.gate('xor',parity[a^bit],xs[i][bit.bit_length()-1])
        chars.append([cnf.gate('xor',fs[i],parity[a]) for a in range(512)])
    for a in range(512):
        bad=[chars[i][a] if w[a]>0 else neg(chars[i][a]) for i in range(r)]
        upper=(bound-abs(w[a])+2*r)//4
        lower=-((-2*r+bound+abs(w[a]))//4) # ceil((2r-bound-|W|)/4)
        # For r<=6 and bound>=28, this lower bound is nonpositive.
        assert lower<=0
        cnf.atmost(bad,upper,'walsh-%d'%a)
        if a in selectors:
            target=(2*r-abs(w[a]))//4
            cnf.atmost(bad,target,'zero-upper-%d'%a,selectors[a])
            cnf.atmost([neg(v) for v in bad],r-target,'zero-lower-%d'%a,selectors[a])
    cnf.require(list(selectors.values()),'some-walsh-zero')
    support_xor=[]
    if degree_eight:
        for j in range(9):
            p=False
            for i in range(r): p=cnf.gate('xor',p,xs[i][j])
            support_xor.append(p)
        cnf.require(support_xor,'nonzero-support-xor')
    if forced is not None:
        assert len(forced)==r and forced==sorted(set(forced))
        for i,x in enumerate(forced):
            for j in range(9):
                cnf.require([xs[i][j] if (x>>j)&1 else -xs[i][j]],'forced-point-%d-%d'%(i,j))
    return cnf,{'seed':name,'seed_hex':SEEDS[name],'radius_exact':r,'bound':bound,'degree_eight_necessary_constraint':degree_eight,'required_zero_origin':zero_origin,'xs':xs,'fs':fs,'zero_selectors':{str(a):s for a,s in selectors.items()},'characters':chars,'less_outputs':less,'support_xor':support_xor,'forced_points':forced,'walsh':w}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--seed',choices=SEEDS,default='dsbf40')
    p.add_argument('--radius',type=int,choices=(2,4,6,8,10),default=6)
    p.add_argument('--bound',type=int,choices=(28,32,36),default=28)
    p.add_argument('--degree-eight',action='store_true')
    p.add_argument('--force',help='comma-separated increasing flip indices')
    p.add_argument('--zero-origin',type=int)
    p.add_argument('--prefix',required=True)
    args=p.parse_args()
    forced=list(map(int,args.force.split(','))) if args.force else None
    cnf,meta=produce(args.seed,args.radius,args.bound,args.degree_eight,forced,args.zero_origin)
    dest=Path(args.prefix+'.cnf')
    text='p cnf %d %d\n'%(cnf.n,len(cnf.clauses))+''.join(' '.join(map(str,c))+' 0\n' for c in cnf.clauses)
    dest.write_text(text)
    meta.update({'variables':cnf.n,'clauses':len(cnf.clauses),'cnf_sha256':hashlib.sha256(text.encode()).hexdigest(),'primary':cnf.primary,'blocks':cnf.blocks})
    Path(args.prefix+'.encoding.json').write_text(json.dumps(meta,separators=(',',':'))+'\n')
    print(args.prefix,'vars',cnf.n,'clauses',len(cnf.clauses),'sha256',meta['cnf_sha256'],flush=True)


if __name__=='__main__': main()
