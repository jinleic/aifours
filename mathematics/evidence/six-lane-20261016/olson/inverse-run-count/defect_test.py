import subprocess, sys
from hw import windows
def run(p,fam,a,b,l,maxsol,cap):
    k=len(a)
    out=subprocess.run(['./hwsingle',str(p),str(fam),str(k)]+[str(x) for x in a+b+l]+[str(maxsol),str(cap)],capture_output=True,text=True).stdout
    return [list(map(int,line.split()[1:])) for line in out.splitlines() if line.startswith('phi:')]
def centered(x,p):
    x%=p
    return x-p if x>p//2 else x
def test(p,a,b,l,sols):
    k=len(a); W=windows(a,b,l,p); inv2=(p+1)//2
    ok=0; bad=[]
    for phi in sols:
        hit=False
        for c in (1,-1):
            # e_t as integer-or-half: work with doubled values
            dev=[centered(phi[t]-((a[t]-b[t]+c)*inv2), p) for t in range(k)]
            for sgn in (-1,1):
                Z=[t for t in range(k) if sgn*dev[t]<0]
                if not Z or len(Z)==k: continue
                P=sum(1<<t for t in Z)
                lo,hi=W[P]
                s=sum(phi[t] for t in Z)%p
                if lo<=hi and (hi-lo+1>=p or (s-lo)%p<=hi-lo):
                    hit=True; break
            if hit: break
        if hit: ok+=1
        else: bad.append(phi)
    return ok,bad
if __name__=='__main__':
    cases=[(7,[1,1,1,1,1,1,1,3],[0]*8,[1,1,1,1,1,1,1,9]),
       (11,[1]*16,[0]*16,[1]*11+[3]*5),
       (7,[1]*10,[0]*10,[1]*9+[7]),
       (7,[1]*11,[0]*11,[1]*10+[5])]
    for (p,a,b,l) in cases:
        sols=run(p,1,a,b,l,20000,20000)
        ok,bad=test(p,a,b,l,sols)
        print(p,a,l,'interval-feasible',len(sols),'killed by defect set',ok,'not',len(bad), bad[:3])
