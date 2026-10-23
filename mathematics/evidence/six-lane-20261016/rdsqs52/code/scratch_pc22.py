"""Enumerate all parallel classes of D0 for cyclic SQS(22) samples; find triples in no parallel class."""
import sys, collections
sys.path.insert(0,'.')
from rdsqs_lib import SQSKM, kissat, derived
v=22
M=SQSKM(v,[tuple((x+1)%v for x in range(v))])
cnf,rv=M.cnf()
def parallel_classes(der, pts):
    by=collections.defaultdict(list)
    for t in der:
        for p in t: by[p].append(t)
    out=[]
    def rec(cov, cur):
        if len(cov)==len(pts): out.append(list(cur)); return
        p=min(q for q in pts if q not in cov)
        for t in by[p]:
            if any(q in cov for q in t): continue
            cur.append(t); rec(cov|set(t), cur); cur.pop()
    rec(frozenset(), [])
    return out
for s in range(6):
    cnf.write('runs/mus22/km2.cnf'); st,model,_=kissat('runs/mus22/km2.cnf',60,seed=s)
    sel=[j for j,x in enumerate(rv) if x in model]; cnf.add([-rv[j] for j in sel])
    blocks=M.blocks_of(sel); der=derived(blocks,0); pts=list(range(1,v))
    pcs=parallel_classes(der,pts)
    inpc=collections.Counter(t for pc in pcs for t in pc)
    none=[t for t in der if inpc[t]==0]
    def kind(t):
        vert=any((a+11)%22==b or (b+11)%22==a for a in t for b in t if a<b)
        return ('has11' if 11 in t else 'no11')+('+vert' if vert else '')
    print('sample',s,'#PC',len(pcs),'triples in no PC',len(none), dict(collections.Counter(kind(t) for t in none)), 'all kinds', dict(collections.Counter(kind(t) for t in der)))
