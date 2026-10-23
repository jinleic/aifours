"""Dump triple lists (format 'v m' + triples) for resolution-engine calibration and search inputs."""
import sys, random, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rdsqs_lib import derived
OUT = 'runs/engine_calib'
def dump(name, v, triples):
    with open(os.path.join(OUT, name + '.tri'), 'w') as f:
        f.write(f"{v} {len(triples)}\n" + "".join(f"{a} {b} {c}\n" for a, b, c in triples))
# known-resolvable KTS(57) constituents, relabelled
CERT='/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/kirkman57/evidence/lkts57-g513/lkts57_g513.txt'
systems=[]
for line in open(CERT):
    line=line.split('#')[0].strip()
    if not line: continue
    t=line.split()
    if t[0]=='LKTS': continue
    if t[0]=='KTS': systems.append(set()); continue
    if t[0]=='CLASS': continue
    systems[-1].add(tuple(sorted(map(int,t))))
for k in (0, 20, 40):
    rng=random.Random(1000+k); perm=list(range(57)); rng.shuffle(perm)
    dump(f'kts57_sys{k}', 57, sorted(tuple(sorted(perm[x] for x in b)) for b in systems[k]))
# Liu–Lei RDSQS(22) derived at 0 (relabel to 0..20 by dropping point 0)
blocks=[]
for line in open('../evidence/controls/liulei_rdsqs22.txt'):
    line=line.split('#')[0].strip()
    if not line: continue
    t=line.split()
    if t[0] in ('RDSQS','BLOCKS'): continue
    if t[0]=='POINT': break
    blocks.append(tuple(map(int,t)))
d=derived(blocks,0); lab={p:i for i,p in enumerate(sorted({x for t in d for x in t}))}
dump('liulei22_d0', 21, [tuple(sorted(lab[x] for x in t)) for t in d])
print('ok')
