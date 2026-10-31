#!/usr/bin/env python3
"""Exact finite counterexample to simultaneous tightness for all valid entries.

A is supplied by its five-element multiplication table; all source hypotheses,
actual syntactic contexts and R/L counts are checked directly. No author code,
randomness, external packages or writes are used.
"""
from itertools import product


def require(ok,why):
    if not ok:raise ValueError(why)


def main():
    table=((0,1,2,3,0),
           (3,2,1,0,1),
           (0,1,2,3,2),
           (3,2,1,0,3),
           (0,1,2,3,4))
    A=tuple(range(5));one=4;p=1;x=3
    theta=(0,1,0,1,0)
    def am(a,b):return table[a][b]
    require(all(am(am(a,b),c)==am(a,am(b,c)) for a,b,c in product(A,repeat=3)),'A associativity')
    require(all(am(one,a)==a==am(a,one) for a in A),'A identity')
    E=[a for a in A if am(a,a)==a]
    require(E==[0,2,4],'A idempotents')
    require(all(any(am(am(a,b),a)==a and am(am(b,a),b)==b for b in A) for a in A),'A regular')
    require(all(am(a,b) in E for a,b in product(E,repeat=2)),'A orthodox')
    require(all(am(am(am(am(a,b),a),c),a)==am(am(am(a,b),c),a)
                for a,b,c in product(E,repeat=3)),'A regular band')
    require(all(theta[am(a,b)]==(theta[a]+theta[b])%2 for a,b in product(A,repeat=2)),'theta homomorphism')
    require(all((theta[a]==0)==(a in E) for a in A),'theta purity')
    def rf(q):return all(am(am(a,q),a)==a for a in A if theta[a]==theta[q])
    require(p!=x and theta[p]==theta[x]==1 and rf(p) and rf(x),'distinct RF entries')
    require(not any(am(e,p)==x==am(p,f) for e,f in product(E,repeat=2)), 'x below p unexpectedly')
    require(not any(am(e,x)==p==am(x,f) for e,f in product(E,repeat=2)), 'p below x unexpectedly')

    P=((one,one,one),(one,p,one),(one,one,x))
    S=list(product(range(3),A,range(3)))
    def sm(a,b):return (a[0],am(am(a[1],P[a[2]][b[0]]),b[1]),b[2])
    def idem(a):return sm(a,a)==a
    def actor(a):return (a[0],theta[a[1]],a[2])
    require(all(sm(sm(a,b),c)==sm(a,sm(b,c)) for a,b,c in product(S,repeat=3)),'S associativity')
    require(all(any(sm(sm(a,b),a)==a and sm(sm(b,a),b)==b for b in S) for a in S),'S regular')
    ES=[a for a in S if idem(a)]
    for a in S:
        left={sm(e,a) for e in ES};right={sm(a,e) for e in ES}
        require(not(left&right&set(ES)) or idem(a),'S weak E-unitarity')
    for e in ES:
        local={sm(sm(e,a),e) for a in S}
        le=[a for a in local if idem(a)]
        require(all(idem(sm(a,b)) for a,b in product(le,repeat=2)),'local orthodox')
        require(all(sm(sm(sm(sm(a,b),a),c),a)==sm(sm(sm(a,b),c),a)
                    for a,b,c in product(le,repeat=3)),'local regular band')
    require(any(not idem(sm(a,b)) for a,b in product(ES,repeat=2)),'expected global nonorthodoxy')
    e0=(0,one,0);local={sm(sm(e0,a),e0) for a in S}
    le=[a for a in local if idem(a)]
    require(any(sm(a,b)!=sm(b,a) for a,b in product(le,repeat=2)),'expected noninverse local corner')
    require(all(idem(s)==(theta[s[1]]==theta[P[s[2]][s[0]]]) for s in S),'Rees actor pure')
    contexts=[None]+S
    def ctx(a,s,b):
        y=s if a is None else sm(a,s)
        return y if b is None else sm(y,b)
    sig={s:bytes(idem(ctx(a,s,b)) for a,b in product(contexts,repeat=2)) for s in S}
    require(all((sig[a]==sig[b])==(actor(a)==actor(b)) for a,b in product(S,repeat=2)), 'actual tau')
    same=[(a,b) for a,b in product(ES,repeat=2) if a!=b and actor(a)==actor(b)]
    rp=[(a,b) for a,b in same if sm(a,b)==b and sm(b,a)==a]
    lp=[(a,b) for a,b in same if sm(a,b)==a and sm(b,a)==b]
    require(rp and not lp,'expected R but no L pairs')
    left={a:frozenset([a]+[sm(y,a) for y in S]) for a in S}
    right={a:frozenset([a]+[sm(a,y) for y in S]) for a in S}
    def H(a,b):return left[a]==left[b] and right[a]==right[b]
    hbad=next(((a,b,y) for a,b,y in product(S,repeat=3)
               if H(a,b) and (not H(sm(a,y),sm(b,y)) or not H(sm(y,a),sm(y,b)))),None)
    require(hbad is None,'unexpected H noncongruence')
    no_group=next((a for a in S if not any(
        sm(sm(a,b),a)==a and sm(sm(b,a),b)==b and sm(a,b)==sm(b,a)
        for b in S)),None)
    require(no_group is not None,'expected a non-completely-regular element')
    # Mutate one source sandwich to idempotent 0, which is not RF-good.
    badP=((one,one,one),(one,0,one),(one,one,x))
    def badmul(a,b):return (a[0],am(am(a[1],badP[a[2]][b[0]]),b[1]),b[2])
    bad=(1,one,1);d=badmul(bad,bad)
    require(d!=bad and badmul(d,bad)==d==badmul(bad,d) and badmul(d,d)==d,'mutant WEU witness')
    print('A_size=5 idempotents=',E,' RF_good_same_fibre=',(p,x),' incomparable=True',sep='')
    print('S_size=',len(S),' idempotents=',len(ES),' actual_actor=',len(set(map(actor,S))),sep='')
    print('same_q_idempotent_pairs=',len(same),' R_pairs=',len(rp),' L_pairs=',len(lp),sep='')
    print('PASS A regular/RB/pure-theta; S regular/WEU/local-r/nonorth/non-locally-inverse; complete tau')
    print('H_congruence=True non_completely_regular_element=',no_group,sep='')
    print('PASS source outside cryptogroup class; no conclusion about any faithful host')
    print('CONTROL nontight idempotent sandwich yields actual WEU failure:',bad,d)
    print('LIMIT: finite exact source; no all-host nonembedding established')


if __name__=='__main__':main()
