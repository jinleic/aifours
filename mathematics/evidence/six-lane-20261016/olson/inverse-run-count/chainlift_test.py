import subprocess, sys, json
from hw import windows
def run(p,fam,a,b,l,maxsol,cap):
    k=len(a)
    out=subprocess.run(['./hwsingle',str(p),str(fam),str(k)]+[str(x) for x in a+b+l]+[str(maxsol),str(cap)],capture_output=True,text=True).stdout
    return [list(map(int,line.split()[1:])) for line in out.splitlines() if line.startswith('phi:')]
def in_win(W,P,s,p):
    lo,hi=W[P]
    if lo>hi: return False
    if hi-lo+1>=p: return True
    return (s-lo)%p<=hi-lo
def chain_lifts(p,a,b,l,phi,W,start=0):
    k=len(a)
    order=[(start+i)%k for i in range(k)]
    prev=0; P=0; lifts=[0]*k; amb=0
    for j,t in enumerate(order):
        P|=1<<t
        s=sum(phi[u] for u in range(k) if P>>u&1)
        lo,hi=W[P]
        # base gap (hi, p-lo')? window [lo,hi] = [-g(E-), g(E+)]; gap above: (hi, lo+p)
        if lo>hi:
            # empty window: choose rep closest to prev + centered phi_t
            cand=prev+((phi[t]+p//2)%p - p//2)
            amb+=1
        else:
            # rep of s in (hi, lo+p)
            cand=hi+1+((s-(hi+1))%p)
            assert cand<lo+p
        lifts[t]=cand-prev; prev=cand
    return lifts,prev,amb
def test(p,a,b,l,sols,start=0):
    k=len(a); W=windows(a,b,l,p)
    res={'n':0,'sumlift':{},'Zkill':0,'Zfail':0,'amb':0}
    fails=[]
    for phi in sols:
        lifts,tot,amb=chain_lifts(p,a,b,l,phi,W,start)
        res['n']+=1; res['amb']+=amb>0
        res['sumlift'][tot]=res['sumlift'].get(tot,0)+1
        bh=[2*lifts[t]-(a[t]-b[t]) for t in range(k)]
        Z=[t for t in range(k) if bh[t]<=0]
        killed=False
        for ZZ in (Z,[t for t in range(k) if t not in Z]):
            if 0<len(ZZ)<k:
                P=sum(1<<t for t in ZZ); s=sum(phi[t] for t in ZZ)%p
                if in_win(W,P,s,p): killed=True
        if killed: res['Zkill']+=1
        else:
            res['Zfail']+=1
            if len(fails)<3: fails.append((phi,lifts,bh))
    return res,fails
if __name__=='__main__':
    cases=[(7,[1,1,1,1,1,1,1,3],[0]*8,[1,1,1,1,1,1,1,9]),
       (11,[1]*16,[0]*16,[1]*11+[3]*5),
       (7,[1]*10,[0]*10,[1]*9+[7]),
       (7,[1]*11,[0]*11,[1]*10+[5]),
       (5,[1,0,0,0,0,0,0],[0,1,1,1,1,1,1],[1,1,1,1,1,1,5])]
    for (p,a,b,l) in cases:
        sols=run(p,1,a,b,l,20000,20000)
        res,fails=test(p,a,b,l,sols)
        print(p,a,b,l,res,fails[:2])
