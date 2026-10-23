from itertools import product
import random
import time

def raw_dp(word, p):
    k=2*p
    dp=[set() for _ in range(k+1)]; dp[0].add((0,1))
    for v,e in word:
        for n in range(k,0,-1):
            dp[n].update(((a+s*v)%p,s*e) for a,s in dp[n-1])
    return (0,1) in dp[k]

def blocks(word):
    N=len(word)
    boundaries=[i for i,(v,e) in enumerate(word) if e==-1 and word[(i+1)%N] != (v,-1)]
    if not any(e==-1 for v,e in word):return None
    cut=boundaries[0]+1 if boundaries else 0
    w=word[cut:]+word[:cut]; X=[]; y=[]; length=[]; i=0
    while i<N:
        xx=[]
        while i<N and w[i][1]==1:xx.append(w[i][0]);i+=1
        if i==N:raise AssertionError('cut not at a reflection block end')
        yy=w[i][0];ll=0
        while i<N and w[i]==(yy,-1):ll+=1;i+=1
        X.append(xx);y.append(yy);length.append(ll)
    return X,y,length

def criterion(rep,p,allrot=None):
    if rep is None:
        signed=list(allrot)
        sums=[set() for _ in range(2*p+1)];sums[0]={0}
        for v in signed:
            for n in range(2*p,0,-1):sums[n].update((a+v)%p for a in sums[n-1])
        return 0 in sums[2*p]
    X,y,ls=rep;k=len(X);F=sum(ls);R=sum(map(len,X))
    for suffix in product((1,-1),repeat=k-1):
        z=(1,)+suffix
        flips=[int(z[i]!=z[(i+1)%k]) for i in range(k)]
        low=sum(flips);high=F-sum((ls[i]-flips[i])%2 for i in range(k))
        counts=[2*p-C for C in range(low,high+1,2) if 0<=2*p-C<=R]
        if not counts:continue
        wanted=sum(y[i-1]-y[i] for i in range(k) if z[i]==1)%p
        sums=[set() for _ in range(max(counts)+1)];sums[0]={0}
        for i,xx in enumerate(X):
            for v in xx:
                for n in range(len(sums)-1,0,-1):sums[n].update((a+z[i]*v)%p for a in sums[n-1])
        if any(wanted in sums[n] for n in counts):return True
    return False

def run():
    rng=random.Random(202610180255)
    rows=[];counts={'random':0,'known_family':0,'cyclic_shift':0,'nonmaximal_blocks':0}
    for p in (3,5,7):
        candidates=[]
        for N in (2*p-1,2*p,4*p-2):
            for _ in range(128):candidates.append(('random',[(rng.randrange(p),rng.choice((1,-1))) for _ in range(N)],None))
        candidates.extend([('known_family',[(1,1)]*(2*p-1)+[(0,-1)]*(2*p-1),False),
                           ('known_family',[(0,1)]*(2*p),True),
                           ('known_family',[(1,-1)]*(2*p),True)])
        for kind,w,expected in candidates:
            actual=raw_dp(w,p);rep=blocks(w);pred=criterion(rep,p,[v for v,e in w])
            if actual!=pred or (expected is not None and actual!=expected):raise AssertionError((p,kind,w,actual,pred,expected))
            counts[kind]+=1
            if expected is not None:
                shift=len(w)//3;rotated=w[shift:]+w[:shift]
                if raw_dp(rotated,p)!=actual or criterion(blocks(rotated),p,[v for v,e in rotated])!=actual:raise AssertionError('cyclic')
                counts['cyclic_shift']+=1
                if rep is not None and any(ll>=2 for ll in rep[2]):
                    X,y,ls=rep;j=next(i for i,ll in enumerate(ls) if ll>=2)
                    split=(X[:j]+[X[j],[]]+X[j+1:],y[:j]+[y[j],y[j]]+y[j+1:],ls[:j]+[1,ls[j]-1]+ls[j+1:])
                    if criterion(split,p)!=actual:raise AssertionError('nonmaximal')
                    counts['nonmaximal_blocks']+=1
    return {'status':'PASS','counts':counts,'total_checks':sum(counts.values()),'seed':202610180255,
            'scope':'Independent ordered-product DP versus parent GRX reconstruction, including cyclic cuts, empty rotations and nonmaximal constant blocks. Finite aid only; p3 tests GRX, not the p>=5 ROT theorem.'}
