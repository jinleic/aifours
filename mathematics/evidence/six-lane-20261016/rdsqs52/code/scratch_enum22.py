import sys, json, time, collections
sys.path.insert(0,'.')
from rdsqs_lib import SQSKM, kissat, derived, resolution_cnf
v=22
M=SQSKM(v,[tuple((x+1)%v for x in range(v))])
cnf,rv=M.cnf()
stats=collections.Counter(); n=0; t0=time.time()
half_counts=collections.Counter()
while n < 400:
    p='runs/e1_enum22/km.cnf'; cnf.write(p)
    st,model,dt=kissat(p,60,seed=n)
    if st!='SAT': print('KM',st,'after',n,'solutions'); break
    sel=[j for j,x in enumerate(rv) if x in model]
    cnf.add([-rv[j] for j in sel])
    blocks=M.blocks_of(sel)
    nhalf=sum(1 for j in sel if M.sizeQ[M.rows[j][0]]==11)
    der=derived(blocks,0)
    rc,tv=resolution_cnf(der,list(range(1,v)),10,anchor=1)
    rp='runs/e1_enum22/res.cnf'; rc.write(rp)
    rs,_,rdt=kissat(rp,60,seed=1)
    stats[rs]+=1; half_counts[(nhalf,rs)]+=1; n+=1
print('n',n,dict(stats),'by #half orbits',dict(half_counts),'s',round(time.time()-t0,1))
