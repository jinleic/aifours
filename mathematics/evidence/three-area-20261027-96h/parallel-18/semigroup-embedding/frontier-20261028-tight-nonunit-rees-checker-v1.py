#!/usr/bin/env python3
"""Exhaustive finite nonunit-sandwich Rees source and canonical-host check.

A is a local submonoid of (R^1 x P({0,1})) semidirect C2.  The 2x2
sandwich matrix has a nonunit entry but a unit in each row and column.
Exact all-context checks; no external libraries, file writes or randomness.
"""
from itertools import product


def require(ok,why):
    if not ok:raise ValueError(why)


def rm(a,b):
    if a is None:return b
    if b is None:return a
    return (a[0],b[1])


def flip_r(a,h):
    return a if a is None or h==0 else (1-a[0],1-a[1])


def flip_mask(mask,h):
    if not h:return mask
    return ((mask&1)<<1)|((mask&2)>>1)


def alpha(b,h):return (flip_r(b[0],h),flip_mask(b[1],h))

def bm(a,b):return (rm(a[0],b[0]),a[1]&b[1])

def am(a,b):
    z=bm((a[0],a[1]),alpha((b[0],b[1]),a[2]))
    return (z[0],z[1],(a[2]+b[2])%2)


def main():
    R=[None]+list(product(range(2),repeat=2))
    A=[(r,mask,h) for r in R for h in range(2) for mask in ((0,1) if h==0 else (0,))]
    one=(None,1,0);p=(None,0,1);e=(None,1)
    require(len(A)==15,'A size')
    require(all(am(one,a)==a==am(a,one) for a in A),'A unit')
    require(all(am(am(a,b),c)==am(a,am(b,c)) for a,b,c in product(A,repeat=3)),'A associativity')
    require(all(any(am(am(a,b),a)==a and am(am(b,a),b)==b for b in A) for a in A),'A regular')
    require(not any(am(p,a)==one==am(a,p) for a in A),'p should be nonunit')
    beta=lambda a:(a[0],a[1])
    require(beta(p)==bm(e,alpha(e,p[2])),'tight sandwich')
    P=((one,one),(one,p))
    S=list(product(range(2),A,range(2)))
    def mul(a,b):return (a[0],am(am(a[1],P[a[2]][b[0]]),b[1]),b[2])
    def idem(a):return mul(a,a)==a
    def actor(a):return (a[0],a[1][2],a[2])
    def coeff(a):return beta(a[1])
    require(all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a,b,c in product(S,repeat=3)),'S associativity')
    require(all(any(mul(mul(a,b),a)==a and mul(mul(b,a),b)==b for b in S) for a in S),'S regular')
    E=[a for a in S if idem(a)]
    for f in E:
        local={mul(mul(f,a),f) for a in S}
        le=[a for a in local if idem(a)]
        require(all(idem(mul(a,b)) for a,b in product(le,repeat=2)),'local E closure')
        require(all(mul(mul(mul(mul(a,b),a),c),a)==mul(mul(mul(a,b),c),a)
                    for a,b,c in product(le,repeat=3)),'local regular identity')
    for a in S:
        left={mul(f,a) for f in E};right={mul(a,f) for f in E}
        require(not (left&right&set(E)) or idem(a),'WEU')
    require(any(not idem(mul(a,b)) for a,b in product(E,repeat=2)),'expected global nonorthodoxy')
    def aid(d):return d[1]==int(d[0]==1 and d[2]==1)
    require(all(idem(s)==aid(actor(s)) for s in S),'actor purity')
    ctx=[None]+S
    def test(x,a,y):
        v=a if x is None else mul(x,a)
        return idem(v if y is None else mul(v,y))
    signatures={a:bytes(test(x,a,y) for x,y in product(ctx,repeat=2)) for a in S}
    require(all((signatures[a]==signatures[b])==(actor(a)==actor(b)) for a,b in product(S,repeat=2)),
            'actual syntactic quotient')
    require(all(coeff(mul(a,b))==bm(coeff(a),alpha(coeff(b),
                (a[1][2]+P[a[2]][b[0]][2])%2)) for a,b in product(S,repeat=2)),'host multiplication')
    require(len({(coeff(a),actor(a)) for a in S})==len(S),'host injectivity')
    same=[(a,b) for a,b in product(E,repeat=2) if a!=b and actor(a)==actor(b)]
    rp=[(a,b) for a,b in same if mul(a,b)==b and mul(b,a)==a]
    lp=[(a,b) for a,b in same if mul(a,b)==a and mul(b,a)==b]
    require(rp and lp and all(coeff(a)!=coeff(b) for a,b in rp+lp),'same-q R/L')
    bad=(next(r for r in R if r is not None),1,0)
    require(beta(bad)!=bm(e,alpha(e,bad[2])),'nontight control')
    require(beta(bad)!=bm(beta(one),alpha(beta(one),bad[2])),'nontight 1-p-1 failure')
    print('A_size=',len(A),' S_size=',len(S),' idempotents=',len(E),' actor=',len(set(map(actor,S))),sep='')
    print('nonunit_p=',p,' identity=',one,' p_squared=',am(p,p),sep='')
    print('same_q_idempotent_pairs=',len(same),' R_pairs=',len(rp),' L_pairs=',len(lp),sep='')
    print('PASS tight nonunit, row/column units, regularity, local-r, WEU, nonorthodox')
    print('PASS all3721 contexts/source, actual actor, full host law/injection, R/L')
    print('CONTROL nontight sandwich fails 1-p-1 coefficient equation')
    print('LIMIT: one finite60-element source, not a universal proof or novelty result')


if __name__=='__main__':main()
