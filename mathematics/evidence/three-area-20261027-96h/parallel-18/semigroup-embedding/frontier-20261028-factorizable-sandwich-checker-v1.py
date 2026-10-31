#!/usr/bin/env python3
"""Exhaustively check sandwich-unit characterization for one finite base.

A=(2x2 rectangular band with identity) semidirect C2, with simultaneous
row/column flip. Each of 10^4 sandwich matrices is analyzed exactly; all 16
all-unit sources are fully checked. No external code or packages.
"""
from itertools import product


def require(ok,why):
    if not ok:raise ValueError(why)


def bm(a,b):
    if a is None:return b
    if b is None:return a
    return (a[0],b[1])


def flip(a,g):return a if a is None or g==0 else (1-a[0],1-a[1])


def am(a,b):return (bm(a[0],flip(b[0],a[1])),(a[1]+b[1])%2)


def main():
    band=[None]+list(product(range(2),repeat=2))
    A=list(product(band,range(2)))
    one=(None,0)
    units=[a for a in A if any(am(a,b)==one==am(b,a) for b in A)]
    require(set(units)=={(None,0),(None,1)},'unit group')
    require(all(any(am(am(a,b),a)==a and am(am(b,a),b)==b for b in A) for a in A),'A regular')
    require(all((a[1]==0)==(am(a,a)==a) for a in A),'pure quotient')
    S=list(product(range(2),A,range(2)))
    good=bad=0
    for entries in product(A,repeat=4):
        P=((entries[0],entries[1]),(entries[2],entries[3]))
        def mul(s,t):return (s[0],am(am(s[1],P[s[2]][t[0]]),t[1]),t[2])
        def idem(s):return mul(s,s)==s
        failing=next(((lam,i) for lam,i in product(range(2),repeat=2) if P[lam][i] not in units),None)
        if failing is not None:
            lam,i=failing
            p=P[lam][i]
            v=(None,p[1])
            x=(i,v,lam)
            x2=mul(x,x);x3=mul(x2,x)
            require(x3==x2 and x2!=x and idem(x2),'nonunit witness')
            require(mul(x2,x)==x2==mul(x,x2),'natural-order witness')
            bad+=1
            continue
        good+=1
        E=[s for s in S if idem(s)]
        require(all(any(mul(mul(a,b),a)==a and mul(mul(b,a),b)==b for b in S) for a in S),'S regular')
        for a in S:
            left={mul(e,a) for e in E};right={mul(a,e) for e in E}
            require(not (left&right&set(E)) or idem(a),'S WEU')
        for e in E:
            local={mul(mul(e,a),e) for a in S}
            le=[a for a in local if idem(a)]
            require(all(idem(mul(a,b)) for a,b in product(le,repeat=2)),'local E closed')
            require(all(mul(mul(mul(mul(a,b),a),c),a)==mul(mul(mul(a,b),c),a)
                        for a,b,c in product(le,repeat=3)),'local RB')
        require(all(idem(a)==(a[1][1]==P[a[2]][a[0]][1]) for a in S),'actor purity')
        def beta(s):return s[1][0]
        require(all(beta(mul(s,t))==bm(beta(s),flip(beta(t),(s[1][1]+P[s[2]][t[0]][1])%2))
                    for s,t in product(S,repeat=2)),'host multiplication')
        require(len({(beta(s),s[0],s[1][1],s[2]) for s in S})==len(S),'host injectivity')
    require(good==16 and bad==9984,'matrix census')
    print('base_size=',len(A),' unit_count=',len(units),' matrices=',good+bad,sep='')
    print('all_unit_matrices=',good,' nonunit_matrices=',bad,sep='')
    print('PASS all9984 nonunit matrices have explicit x^3=x^2!=x, violating WEU')
    print('PASS all16 unit matrices: full source regular/local-r/WEU, pure actor and faithful host')
    print('LIMIT: one finite factorizable base; universal theorem is a separate written proof')


if __name__=='__main__':main()
