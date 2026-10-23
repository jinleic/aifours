"""Calibration: how fast does the plain anchored resolution SAT resolve a KNOWN-resolvable STS(51)?
Build a cyclic STS(51) on Z51 whose 8 full base blocks are transversal mod 3 (plus the short orbit
{0,17,34}); it is resolvable (fixed class = short orbit, other classes = <3>-orbits of base blocks).
Relabel points randomly (seeded) and run the plain anchored resolution SAT with a cap."""
import sys, random, json, itertools, collections
sys.path.insert(0,'.')
from rdsqs_lib import CNF, kissat, resolution_cnf, decode_resolution, verify_resolution
n=51
# cyclic STS(51): difference triples. Base block {0,a,b} with a<b covers differences ±a, ±b, ±(b-a).
diffs=list(range(1,26))  # need 24 differences (excluding 17) covered by 8 base blocks
cand=[]
for a in range(1,51):
    for b in range(a+1,51):
        T=(0,a,b)
        if len({x%3 for x in T})!=3: continue
        ds={min(d,51-d) for d in (a,b,b-a)}
        if len(ds)!=3 or 17 in ds: continue
        cand.append((T,frozenset(ds)))
cnf=CNF(); var={}
for T,ds in cand: var[T]=cnf.var()
by=collections.defaultdict(list)
for T,ds in cand:
    for d in ds: by[d].append(var[T])
for d in diffs:
    if d==17: continue
    cnf.exactly_one(by[d])
cnf.write('runs/kts51_calib/diff.cnf'); st,model,_=kissat('runs/kts51_calib/diff.cnf',60,seed=0)
base=[T for T,ds in cand if var[T] in model]
blocks=set()
for T in base+[(0,17,34)]:
    for s in range(51): blocks.add(tuple(sorted((x+s)%51 for x in T)))
assert len(blocks)==425, len(blocks)
res=[]
for seed in range(int(sys.argv[1]) if len(sys.argv)>1 else 4):
    rng=random.Random(seed); perm=list(range(51)); rng.shuffle(perm)
    bl=sorted(tuple(sorted(perm[x] for x in b)) for b in blocks)
    c,tv=resolution_cnf(bl,list(range(51)),25,anchor=0)
    p=f'runs/kts51_calib/res_{seed}.cnf'; sha=c.write(p)
    st,model,dt=kissat(p,int(sys.argv[2]) if len(sys.argv)>2 else 300,seed=1)
    ok=None
    if st=='SAT':
        ok=verify_resolution(bl,list(range(51)),decode_resolution(model,bl,tv,25))
    res.append({'seed':seed,'status':st,'seconds':round(dt,2),'verified':ok,'cnf_sha256':sha})
    print(res[-1], flush=True)
json.dump({'base_blocks':base,'runs':res}, open('runs/kts51_calib/summary.json','w'), indent=1)
