"""Calibration of the plain anchored resolution SAT on KNOWN-resolvable STS(57)s:
constituents of the lane-pinned LKTS(57) certificate (read-only input), randomly relabelled."""
import sys, random, json
sys.path.insert(0,'.')
from rdsqs_lib import kissat, resolution_cnf, decode_resolution, verify_resolution
CERT='/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/kirkman57/evidence/lkts57-g513/lkts57_g513.txt'
systems=[]; 
for line in open(CERT):
    line=line.split('#')[0].strip()
    if not line: continue
    t=line.split()
    if t[0]=='LKTS': continue
    if t[0]=='KTS': systems.append(set()); continue
    if t[0]=='CLASS': continue
    systems[-1].add(tuple(sorted(map(int,t))))
which=[int(x) for x in sys.argv[1].split(',')]; tmo=int(sys.argv[2])
out=[]
for k in which:
    rng=random.Random(1000+k); perm=list(range(57)); rng.shuffle(perm)
    bl=sorted(tuple(sorted(perm[x] for x in b)) for b in systems[k])
    c,tv=resolution_cnf(bl,list(range(57)),28,anchor=0)
    p=f'runs/kts51_calib/kts57_sys{k}.cnf'; sha=c.write(p)
    st,model,dt=kissat(p,tmo,seed=1)
    ok=verify_resolution(bl,list(range(57)),decode_resolution(model,bl,tv,28)) if st=='SAT' else None
    out.append({'system':k,'status':st,'seconds':round(dt,2),'verified':ok,'vars':c.nv,'cnf_sha256':sha}); print(out[-1],flush=True)
json.dump(out, open(f'runs/kts51_calib/kts57_{sys.argv[1].replace(",","_")}.json','w'), indent=1)
