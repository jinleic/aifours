#!/usr/bin/env python3
"""Independent re-implementation control for the frozen GPS-1|C1 (ms09, ms06 b68/b73) and GPS-2|C1 (ms06 b68/b73)
conditions (README amendments, frozen 14:07:37 and 14:10:23). No new condition or representation: a second algorithm
for the SAME conditions, run on every placement of the same authority-bound lists, compared placement by placement with
the frozen implementations (imported unchanged). Metadata-only pure Python; one lane metadata token; fresh statvfs
admission; creation-only receipt cycle2/gps-crosscheck-<stamp>.json.
ms09 (L=0), casework instead of pair-pair enumeration: with s = 2 - t - e1, R2 = {s=-2}, R1 = {s=-1}, Z = {s=0} and
Y = {y in {0,1,2}: 0 <= 8 - #(s=2) - y <= #(s=1)}:
  |R2| >= 2 infeasible; |R2| = 1 (row u): pairs {u,a},{u,b}, a != b in R1+Z, R1 within {a,b}, oriented so that
  [P3's non-u row in Z] is in Y; |R2| = 0: two disjoint compatible pairs on 4 distinct rows of R1+Z covering R1,
  oriented so that #(Z rows of P3) is in Y. Compatible = T-disjoint and not together in A1/B1/P1. Any |s| > 2 infeasible.
ms06 (L=1): for every leave pair, e2 is computed directly; counts and (GPS-2) the column-2 block partition are
checked by a different search (most-constrained-row-first over an explicit compatibility table).
Usage: gps_crosscheck_v1.py
"""
import hashlib
import itertools
import json
import os
import time
from pathlib import Path

import gps1c1_probe_v1 as C
import gps2c1_ms06_probe_v1 as C2
import gps_probe_v1 as G
import m2_supervised_runtime_v6_3 as R

L = Path(__file__).resolve().parents[1]
BIND = ('cycle2/gps-list-binding-20261018T141454.json','6e40783cce4ea392204741d2d26b68b83a724281b62a012ea97659c8525a40a9')
EXPECT = {'gps1c1':('cycle2/gps1c1-probe-20261018T140808.json','d82ddf381c34348b1c4ae8b7a6956f8a6a6f0650c6ee947dd30e24beb0cc961d'),
          'gps2c1':('cycle2/gps2c1-ms06-probe-20261018T141048.json','12b4320e3acdfd119516a505518357c9bd647f1ec5b19755196a0cf752b8bf57')}
SKB = {'ms09':'cycle2/skel-b/skeletons-b-ms09.json','ms06':'cycle2/skel-b/skeletons-b-ms06.json'}


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def roles(N,A,B,P):
    blk = {}
    for name,b in (('A',A),('B',B),('P',P)):
        for r in b: blk[r] = name
    return blk


def ind_ms09(T,t,A,B,P):
    N = len(T); blk = roles(N,A,B,P)
    e1 = {r:(1 if blk.get(r) in ('A','B') else (-1 if blk.get(r) == 'P' else 0)) for r in range(N)}
    s = {r:2-t[r]-e1[r] for r in range(N)}
    if any(abs(v) > 2 for v in s.values()): return False
    R2 = [r for r in range(N) if s[r] == -2]; R1 = [r for r in range(N) if s[r] == -1]; Z = [r for r in range(N) if s[r] == 0]
    n2 = sum(1 for v in s.values() if v == 2); n1 = sum(1 for v in s.values() if v == 1)
    Y = {y for y in (0,1,2) if 0 <= 8-n2-y <= n1}
    if not Y: return False

    def comp(a,b):
        return a != b and not (T[a] & T[b]) and not (a in blk and b in blk and blk[a] == blk[b])
    pool = R1+Z; zset = set(Z)
    if len(R2) >= 2: return False
    if len(R2) == 1:
        u = R2[0]
        if len(R1) > 2: return False
        for a,b in itertools.permutations(pool,2):
            if not (set(R1) <= {a,b}) or not comp(u,a) or not comp(u,b): continue
            if (1 if b in zset else 0) in Y: return True  # P2={u,a}, P3={u,b}; permutations cover the other orientation
        return False
    if len(R1) > 4: return False
    for rest in itertools.combinations(Z,4-len(R1)):  # the 4 distinct endpoints = all of R1 plus rows of Z
        a,b,c,d = tuple(R1)+rest
        for p,q in (((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))):
            if not (comp(*p) and comp(*q)): continue
            if sum(x in zset for x in q) in Y or sum(x in zset for x in p) in Y: return True
    return False


def ind_partition(rows,size,ok):
    """Most-constrained-first exact partition of `rows` into blocks of `size` with pairwise ok(); True/False."""
    rows = set(rows)
    if not rows: return True
    if len(rows) % size: return False
    deg = {r:sum(1 for x in rows if x != r and ok(r,x)) for r in rows}
    r0 = min(rows,key=lambda r:(deg[r],r))
    nb = sorted(x for x in rows if x != r0 and ok(r0,x))
    for rest in itertools.combinations(nb,size-1):
        if all(ok(a,b) for a,b in itertools.combinations(rest,2)):
            if ind_partition(rows-{r0,*rest},size,ok): return True
    return False


def ind_ms06(T,t,A,B,P,level2):
    N = len(T); blk = roles(N,A,B,P)
    e1 = {r:(1 if blk.get(r) in ('A','B') else (-1 if blk.get(r) == 'P' else 0)) for r in range(N)}
    for x,y in itertools.combinations(range(N),2):
        if T[x] & T[y] or (x in blk and y in blk and blk[x] == blk[y]): continue
        e2 = {r:2-(1 if r in (x,y) else 0)-t[r]-e1[r] for r in range(N)}
        if any(v not in (-1,0,1) for v in e2.values()): continue
        neg = [r for r in range(N) if e2[r] == -1]
        if len(neg) != 2 or sum(1 for v in e2.values() if v == 1) != 8: continue

        def ok(a,b,x=x,y=y):
            return not (T[a] & T[b]) and not (a in blk and b in blk and blk[a] == blk[b]) and {a,b} != {x,y}
        if not ok(*neg): continue
        if not level2: return True
        if ind_partition([r for r in range(N) if e2[r] == 1],4,ok) and ind_partition([r for r in range(N) if e2[r] == 0],3,ok): return True
    return False


def main():
    started = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    for p,h in [BIND]+list(EXPECT.values()): assert digest(L/p) == h, ('pinned file changed',p)
    bind = json.loads((L/BIND[0]).read_bytes()); assert bind['all_bound'] is True
    exp1 = json.loads((L/EXPECT['gps1c1'][0]).read_bytes()); exp2 = json.loads((L/EXPECT['gps2c1'][0]).read_bytes())
    lists = {}
    for row in bind['rows']: lists[row['case']] = (row['list'],row['disk_sha256'])
    out,disagree = {},[]
    for case,(path,sha) in sorted(lists.items()):
        assert digest(L/path) == sha
        ms,b = case.split('_b'); b = int(b)
        d = json.loads((L/SKB[ms]).read_bytes()); T = G.rows_of(d['skeletons'][b],d['c0'],19); t = [len(x) for x in T]
        e = json.loads((L/path).read_bytes())
        res = {'n':e['num_placements'],'frozen_c1_excluded':0,'independent_c1_excluded':0}
        if ms == 'ms06': res.update(frozen_c2_excluded=0,independent_c2_excluded=0)
        for i,(A,B,P) in enumerate(e['placements']):
            if ms == 'ms09':
                f = C.c1_L0(T,t,A,B,P) is not None; g = ind_ms09(T,t,A,B,P)
            else:
                f = C.c1_L1(T,t,A,B,P) is not None; g = ind_ms06(T,t,A,B,P,False)
                f2 = C2.gps2_L1(T,t,A,B,P) is not None; g2 = ind_ms06(T,t,A,B,P,True)
                res['frozen_c2_excluded'] += not f2; res['independent_c2_excluded'] += not g2
                if f2 != g2: disagree.append({'case':case,'index':i,'level':2,'frozen_feasible':f2,'independent_feasible':g2})
            res['frozen_c1_excluded'] += not f; res['independent_c1_excluded'] += not g
            if f != g: disagree.append({'case':case,'index':i,'level':1,'frozen_feasible':f,'independent_feasible':g})
        out[case] = res
    # receipt totals must be reproduced by the frozen functions on the same lists
    tot_ok = all(out['ms09_b%05d' % x['b_index']]['frozen_c1_excluded'] == x['excluded'] for x in exp1['cases']['ms09']) and \
             all(out['ms06_b%05d' % x['b_index']]['frozen_c1_excluded'] == x['excluded'] for x in exp1['cases']['ms06']) and \
             all(out['ms06_b%05d' % x['b_index']]['frozen_c2_excluded'] == x['gps2c1_excluded'] for x in exp2['cases'])
    s = os.statvfs(L)
    rec = {'schema':'PA19-GPS-CROSSCHECK-v1','started_host_clock':started,'finished_host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
           'source_sha256':digest(__file__),'imports':{p:digest(L/p) for p in ('src/gps1c1_probe_v1.py','src/gps2c1_ms06_probe_v1.py','src/gps_probe_v1.py')},
           'pinned':{p:h for p,h in [BIND]+list(EXPECT.values())},'cases':out,'placements_compared':sum(v['n'] for v in out.values()),
           'disagreements':disagree[:200],'disagreement_count':len(disagree),'receipt_totals_reproduced':tot_ok,
           'admission':{'free_bytes_at_finish':s.f_bavail*s.f_frsize},
           'scope':'implementation cross-check of frozen candidate conditions only; no acceptance; no solver'}
    dest = L/'cycle2'/('gps-crosscheck-%s.json' % time.strftime('%Y%m%dT%H%M%S'))
    with dest.open('x') as f: json.dump(rec,f,indent=1); f.write('\n')
    print(dest,digest(dest),'compared',rec['placements_compared'],'disagreements',len(disagree),'totals_reproduced',tot_ok,flush=True)


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        s = os.statvfs(L); free = s.f_bavail*s.f_frsize
        assert free >= R.BASE_GATE+16*1024**2, ('fresh admission refused',free)
        print('admission free',free,flush=True)
        main()
