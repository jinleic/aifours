#!/usr/bin/env python3
"""GPS-2|C1 probe for ms06 (E2b, L=1, m=2): for each placement of the frozen complete first-column lists of the two
open ms06 cases with lists (b68, b73), the second P1 column is FORCED up to the leave pair: e2 = 2 - l - t - e1. GPS-2|C1
adds to GPS-1|C1 the block partition of column 2 (frozen in README, Amendment GPS-2|C1, before execution):
  the 8 rows with e2=+1 split into two 4-blocks and the 9 rows with e2=0 into three triples, where every block is
  pairwise T-disjoint, contains no two rows already together in a column-1 block (A1, B1, P1), and does not contain
  both leave rows (they agree nowhere); the two rows with e2=-1 form a T-disjoint pair, not together in a column-1
  block and not the leave pair.
Rows in one block of column 2 agree in column 2, hence in no P0 column and in no column-1 block; this is the same
definition-level argument as GPS (1)-(4). A placement for which no leave pair passes admits no array (its orbit is
excluded). Pure Python, one metadata token, no solver. Receipt cycle2/gps2c1-ms06-probe-<stamp>.json.
Usage: gps2c1_ms06_probe_v1.py
"""
import collections
import hashlib
import itertools
import json
import os
import time
from pathlib import Path

import gps1c1_probe_v1 as C
import gps_probe_v1 as G
import m2_supervised_runtime_v6_3 as R

L = Path(__file__).resolve().parents[1]
GPS1 = ('cycle2/gps1-probe-20261018T140007.json','67170e7b6934cf2e5594985922e8385f3c46f646714c862e3d6f94014fe52218')
GPS1C1 = ('cycle2/gps1c1-probe-20261018T140808.json','d82ddf381c34348b1c4ae8b7a6956f8a6a6f0650c6ee947dd30e24beb0cc961d')
SKB = 'cycle2/skel-b/skeletons-b-ms06.json'
CASES = (68,73)


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def compatible(T,bid,leave,rows):
    """Rows may share one block of column 2: pairwise T-disjoint, never together in a column-1 block, not both leave rows."""
    for a,b in itertools.combinations(rows,2):
        if T[a] & T[b] or (bid[a] >= 0 and bid[a] == bid[b]) or {a,b} == set(leave): return False
    return True


def split_blocks(T,bid,leave,rows,size):
    """Partition `rows` into blocks of `size`, each compatible; returns one partition or None (exhaustive)."""
    rows = sorted(rows)
    if not rows: return []
    first,rest = rows[0],rows[1:]
    for others in itertools.combinations(rest,size-1):
        blk = (first,)+others
        if not compatible(T,bid,leave,blk): continue
        tail = split_blocks(T,bid,leave,[r for r in rest if r not in others],size)
        if tail is not None: return [list(blk)]+tail
    return None


def gps2_L1(T,t,A,B,P):
    N = len(T); bid = C.block_ids(N,A,B,P)
    e1 = [1 if bid[r] in (0,1) else (-1 if bid[r] == 2 else 0) for r in range(N)]
    base = [2-t[r]-e1[r] for r in range(N)]
    for x,y in itertools.combinations(range(N),2):
        if T[x] & T[y] or (bid[x] >= 0 and bid[x] == bid[y]): continue
        e2 = [base[r]-(1 if r in (x,y) else 0) for r in range(N)]
        if any(v < -1 or v > 1 for v in e2): continue
        neg = [r for r in range(N) if e2[r] == -1]; pos = [r for r in range(N) if e2[r] == 1]; zero = [r for r in range(N) if e2[r] == 0]
        if len(neg) != 2 or len(pos) != 8: continue
        if not compatible(T,bid,(x,y),neg): continue
        quads = split_blocks(T,bid,(x,y),pos,4)
        if quads is None: continue
        trip = split_blocks(T,bid,(x,y),zero,3)
        if trip is None: continue
        return {'leave':[x,y],'pair':neg,'four_blocks':quads,'triples':trip}
    return None


def verify(T,t,A,B,P,w):
    """Independent re-check of a full column-2 witness."""
    N = len(T); bid = C.block_ids(N,A,B,P); x,y = w['leave']
    blocks = w['four_blocks']+w['triples']+[w['pair']]
    if sorted(r for b in blocks for r in b) != list(range(N)) or [len(b) for b in blocks] != [4,4,3,3,3,2]: return False
    if not all(compatible(T,bid,(x,y),b) for b in blocks): return False
    if T[x] & T[y] or (bid[x] >= 0 and bid[x] == bid[y]): return False
    for r in range(N):
        e1 = 1 if bid[r] in (0,1) else (-1 if bid[r] == 2 else 0)
        e2 = next(len(b)-3 for b in blocks if r in b)
        if t[r]+e1+e2 != 2-(1 if r in (x,y) else 0): return False
    return True


def control_partition13():
    """Unit control of split_blocks/compatible on real data: in the (13,5,4) SAT model, with its first P1 column as column
    1, the true blocks of its second P1 column must be found compatible, and split_blocks must partition them."""
    A = [list(map(int,s.split())) for s in (L/G.CONTROL13['model']).read_text().split('\n') if s.strip()]
    N,k = len(A),len(A[0]); cnt = [collections.Counter(A[r][c] for r in range(N)) for c in range(k)]
    p0 = [c for c in range(k) if sorted(cnt[c].values(),reverse=True) == [4,3,3,3]]
    p1 = [c for c in range(k) if sorted(cnt[c].values(),reverse=True) == [4,4,3,2]]
    quad = {c:next(s for s,n in cnt[c].items() if n == 4) for c in p0}
    T = [frozenset(i for i,c in enumerate(p0) if A[r][c] == quad[c]) for r in range(N)]
    c1,c2 = p1[0],p1[1]
    f1 = [s for s,n in cnt[c1].items() if n == 4]; two1 = next(s for s,n in cnt[c1].items() if n == 2)
    bid = C.block_ids(N,[r for r in range(N) if A[r][c1] == f1[0]],[r for r in range(N) if A[r][c1] == f1[1]],[r for r in range(N) if A[r][c1] == two1])
    true_blocks = [[r for r in range(N) if A[r][c2] == s] for s in cnt[c2]]
    ok_true = all(compatible(T,bid,(),b) for b in true_blocks)
    pos = [r for b in true_blocks if len(b) == 4 for r in b]
    found = split_blocks(T,bid,(),pos,4)
    return {'true_blocks_compatible':ok_true,'four_block_split_found':found is not None,'ok':ok_true and found is not None}


def main():
    stamp = time.strftime('%Y%m%dT%H%M%S'); started = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    assert digest(L/GPS1[0]) == GPS1[1] and digest(L/GPS1C1[0]) == GPS1C1[1]
    c1r = json.loads((L/GPS1C1[0]).read_bytes())
    d = json.loads((L/SKB).read_bytes()); c0 = d['c0']
    inputs = {GPS1[0]:GPS1[1],GPS1C1[0]:GPS1C1[1],SKB:digest(L/SKB)}
    cases,mono = [],True
    for b in CASES:
        p = 'cycle2/m2part_drat/ms06_b%05d/ext.json' % b; inputs[p] = digest(L/p)
        e = json.loads((L/p).read_bytes()); assert e['index'] == b and e['num_placements'] == len(e['placements'])
        prev = next(x for x in c1r['cases']['ms06'] if x['b_index'] == b)
        assert prev['list_sha256'] == inputs[p]
        prev_excl = set(prev['excluded_indices'] or [])
        T = G.rows_of(d['skeletons'][b],c0,19); t = [len(x) for x in T]
        excl,feas = [],0
        for i,(A,B,P) in enumerate(e['placements']):
            C.check_placement(T,A,B,P,c0)
            w = gps2_L1(T,t,A,B,P)
            if w is None: excl.append(i)
            else:
                assert verify(T,t,A,B,P,w), ('witness re-check failed',b,i)
                feas += 1
                if i in prev_excl: mono = False  # GPS-2|C1 is stronger than GPS-1|C1: a GPS-1|C1 exclusion must stay excluded
        ex = set(excl)
        full = [list(iv) for iv in C.intervals(e['num_placements']) if all(j in ex for j in range(iv[0],iv[1]+1))]
        cases.append({'b_index':b,'m1_tag':prev['m1_tag'],'list':p,'list_sha256':inputs[p],'num_placements':e['num_placements'],
                      'gps1c1_excluded':prev['excluded'],'gps2c1_excluded':len(excl),'feasible':feas,'all_excluded':len(excl) == e['num_placements'],
                      'surviving_indices':[i for i in range(e['num_placements']) if i not in ex] if feas <= 3000 else None,
                      'fully_excluded_b100_intervals':full,'b100_intervals':len(C.intervals(e['num_placements']))})
    ctl = control_partition13()
    controls = {'C1_monotone_vs_gps1c1':mono,'C2_partition_unit_control_13row':ctl['ok'],'C4_every_witness_rechecked':True}
    allok = mono and ctl['ok']
    out = {'schema':'PA19-GPS2C1-MS06-PROBE-v1','started_host_clock':started,'finished_host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
           'source_sha256':digest(__file__),'imports':{'src/gps1c1_probe_v1.py':digest(L/'src/gps1c1_probe_v1.py'),'src/gps_probe_v1.py':digest(L/'src/gps_probe_v1.py')},
           'inputs':inputs,'controls':controls,'controls_all_expected':allok,'control_partition13':ctl,'cases':cases,
           'scope':'necessary-condition probe only; candidate structural exclusions pending written-proof review, list-completeness '
                   'acceptance and parent acceptance; no L=1 semantic positive control exists; no solver; no PA19 claim'}
    dest = L/'cycle2'/('gps2c1-ms06-probe-%s.json' % stamp)
    with dest.open('x') as f: json.dump(out,f,indent=1); f.write('\n')
    print(dest,digest(dest),'controls_all_expected',allok,flush=True)
    print(json.dumps({'controls':controls,'cases':[{k:c[k] for k in ('b_index','m1_tag','num_placements','gps1c1_excluded','gps2c1_excluded','feasible','all_excluded','b100_intervals')}
                                                     | {'full_intervals':len(c['fully_excluded_b100_intervals'])} for c in cases]}),flush=True)


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+16*1024**2
        main()
