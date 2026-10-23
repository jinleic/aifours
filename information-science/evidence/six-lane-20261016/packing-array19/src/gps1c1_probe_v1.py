#!/usr/bin/env python3
"""GPS-1|C1 probe: the GPS-1 pair-structure condition CONDITIONED on a fixed first P1 column, applied to every
placement of the frozen complete first-column lists (cycle2/m2part_drat/<case>/ext.json, extend_b row order) of the
ms09 cases and of the two ms06 cases with lists (b68, b73). Frozen in README (Amendment GPS-1|C1) before execution.
Pure Python, one lane metadata token; no solver, checker, CNF or native child. Receipt cycle2/gps1c1-probe-<stamp>.json.

Given the first P1 column's blocks (A1, B1: size 4; P1: size 2) every row has e1 in {+1, 0, -1}; the row identity
t + e1 + sum_{j>=2} e_j = 2 - l gives s(r) = 2 - l - t - e1 = sum over the m' = m-1 remaining P1 columns. Then
    n2'(r) := #{remaining pair blocks containing r} in [max(0,-s), floor((m'-s)/2)]   and |s| <= m'.
The m' remaining pair blocks are distinct, T-disjoint, and never two rows already together in A1, B1 or P1.
Column counts: every remaining P1 column has exactly 8 rows with e = +1.
  ms09 (L=0, m'=2): rows with s=2 are +1 in both columns, s=1 rows +1 in exactly one (free), rows with s=0 in exactly
  one pair block are +1 in the OTHER column; feasible iff some x in [0, #(s=1)] gives #(s=2) + y3 + x = 8 where y3 =
  #(s=0 rows in P3 only) (column 3 then has 8 automatically).
  ms06 (L=1, m'=1): for a leave pair {x,y} (T-disjoint, not together in a column-1 block) e2 = s is determined; need
  all e2 in {-1,0,1}, exactly two rows with e2=-1 forming a T-disjoint pair not together in a column-1 block and not
  equal to {x,y}, and exactly 8 rows with e2=+1.
A placement failing this admits no packing array (the whole orbit it represents is excluded, the condition being
invariant under the skeleton automorphisms and the A/B swap). Feasible placements say nothing about existence.
Usage: gps1c1_probe_v1.py
"""
import collections
import hashlib
import itertools
import json
import os
import time
from pathlib import Path

import m2_supervised_runtime_v6_3 as R
import gps_probe_v1 as G

L = Path(__file__).resolve().parents[1]
GPS1 = ('cycle2/gps1-probe-20261018T140007.json','67170e7b6934cf2e5594985922e8385f3c46f646714c862e3d6f94014fe52218')
SKB = {'ms09':'cycle2/skel-b/skeletons-b-ms09.json','ms06':'cycle2/skel-b/skeletons-b-ms06.json'}
MS06_CASES = (68,73)


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def block_ids(N,A,B,P):
    bid = [-1]*N
    for k,blk in enumerate((A,B,P)):
        for r in blk: bid[r] = k
    return bid


def check_placement(T,A,B,P,c0):
    """Sanity: a valid first-column placement (sizes 4,4,2; disjoint; blocks pairwise T-disjoint)."""
    assert len(A) == 4 and len(B) == 4 and len(P) == 2 and len(set(A)|set(B)|set(P)) == 10
    for blk in (A,B,P):
        assert all(not T[a] & T[b] for a,b in itertools.combinations(blk,2))


def c1_L0(T,t,A,B,P):
    """ms09: exists (P2,P3) satisfying the conditioned conditions? Returns witness or None."""
    N = len(T); bid = block_ids(N,A,B,P)
    e1 = [1 if bid[r] in (0,1) else (-1 if bid[r] == 2 else 0) for r in range(N)]
    s = [2-t[r]-e1[r] for r in range(N)]
    if any(x < -2 or x > 2 for x in s): return None
    lo = [max(0,-x) for x in s]; hi = [(2-x)//2 for x in s]
    if sum(lo) > 4: return None
    req2 = sum(1 << r for r in range(N) if lo[r] == 2); req1 = sum(1 << r for r in range(N) if lo[r] == 1)
    s0 = sum(1 << r for r in range(N) if s[r] == 0)
    n_s2 = sum(1 for x in s if x == 2); n_s1 = sum(1 for x in s if x == 1)
    cand = [(a,b) for a,b in itertools.combinations(range(N),2)
            if hi[a] >= 1 and hi[b] >= 1 and not T[a] & T[b] and not (bid[a] >= 0 and bid[a] == bid[b])]
    if not cand: return None
    req = req1 | req2
    if req:
        r0 = (req & -req).bit_length()-1
        first = [p for p in cand if r0 in p]
    else:
        first = cand
    for p2 in first:
        m2 = (1 << p2[0]) | (1 << p2[1])
        for p3 in cand:
            if p3 == p2: continue
            m3 = (1 << p3[0]) | (1 << p3[1])
            if (m2 & m3) != req2 or (req1 & ~(m2 | m3)) or (req1 & m2 & m3): continue
            y3 = bin(m3 & ~m2 & s0).count('1')
            if 0 <= 8-n_s2-y3 <= n_s1: return (p2,p3)
    return None


def c1_L1(T,t,A,B,P):
    """ms06: exists a leave pair {x,y} making column 2 consistent? Returns witness or None."""
    N = len(T); bid = block_ids(N,A,B,P)
    e1 = [1 if bid[r] in (0,1) else (-1 if bid[r] == 2 else 0) for r in range(N)]
    base = [2-t[r]-e1[r] for r in range(N)]
    for x,y in itertools.combinations(range(N),2):
        if T[x] & T[y] or (bid[x] >= 0 and bid[x] == bid[y]): continue
        e2 = [base[r]-(1 if r in (x,y) else 0) for r in range(N)]
        if any(v < -1 or v > 1 for v in e2): continue
        neg = [r for r in range(N) if e2[r] == -1]
        if len(neg) != 2 or sum(1 for v in e2 if v == 1) != 8: continue
        a,b = neg
        if T[a] & T[b] or (bid[a] >= 0 and bid[a] == bid[b]) or {a,b} == {x,y}: continue
        return ((a,b),(x,y))
    return None


def verify_L0(T,t,A,B,P,w):
    """Independent re-check of an ms09 witness by explicit e-vector construction."""
    N = len(T); bid = block_ids(N,A,B,P); p2,p3 = w
    if set(p2) == set(p3) or any(T[a] & T[b] or (bid[a] >= 0 and bid[a] == bid[b]) for a,b in (p2,p3)): return False
    e = {}
    for r in range(N):
        e1 = 1 if bid[r] in (0,1) else (-1 if bid[r] == 2 else 0)
        s = 2-t[r]-e1; in2, in3 = r in p2, r in p3
        e2 = -1 if in2 else None; e3 = -1 if in3 else None
        if in2 and in3: ok = s == -2
        elif in2: e3 = s+1; ok = e3 in (0,1)
        elif in3: e2 = s+1; ok = e2 in (0,1)
        else: ok = s in (0,1,2)
        if not ok: return False
        e[r] = (e2,e3,s)
    fixed2 = sum(1 for r,(a,b,s) in e.items() if a == 1); fixed3 = sum(1 for r,(a,b,s) in e.items() if b == 1)
    both = sum(1 for r,(a,b,s) in e.items() if a is None and b is None and s == 2)
    free = sum(1 for r,(a,b,s) in e.items() if a is None and b is None and s == 1)
    return any(fixed2+both+x == 8 and fixed3+both+(free-x) == 8 for x in range(free+1))


def control13():
    """The (13,5,4) L=0 SAT model: its own first P1 column placement must pass c1_L0."""
    A = [list(map(int,s.split())) for s in (L/G.CONTROL13['model']).read_text().split('\n') if s.strip()]
    N,k = len(A),len(A[0])
    cnt = [collections.Counter(A[r][c] for r in range(N)) for c in range(k)]
    p0 = [c for c in range(k) if sorted(cnt[c].values(),reverse=True) == [4,3,3,3]]
    p1 = [c for c in range(k) if sorted(cnt[c].values(),reverse=True) == [4,4,3,2]]
    quad = {c:next(s for s,n in cnt[c].items() if n == 4) for c in p0}
    T = [frozenset(i for i,c in enumerate(p0) if A[r][c] == quad[c]) for r in range(N)]
    t = [len(x) for x in T]
    res = []
    for c in p1:  # each P1 column in turn as "first"
        fours = [s for s,n in cnt[c].items() if n == 4]; two = next(s for s,n in cnt[c].items() if n == 2)
        Ab = [r for r in range(N) if A[r][c] == fours[0]]; Bb = [r for r in range(N) if A[r][c] == fours[1]]
        Pb = [r for r in range(N) if A[r][c] == two]
        w = c1_L0(T,t,Ab,Bb,Pb)  # (13,5,4): D = 12-10 = 2 and two 4-blocks (8 rows) per P1 column, as in c1_L0
        res.append(w is not None)
    return {'p1_columns':p1,'each_as_first_column_feasible':res,'ok':all(res)}



def intervals(n):
    return [(lo,min(n,lo+100)-1) for lo in range(0,n,100)]


def main():
    stamp = time.strftime('%Y%m%dT%H%M%S'); started = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    assert digest(L/GPS1[0]) == GPS1[1]
    gps = json.loads((L/GPS1[0]).read_bytes())
    out_cases,inputs = {'ms09':[],'ms06':[]},{GPS1[0]:GPS1[1]}
    for ms in ('ms09','ms06'):
        d = json.loads((L/SKB[ms]).read_bytes()); inputs[SKB[ms]] = digest(L/SKB[ms]); c0 = d['c0']
        cases = gps['results'][ms]['cases']
        targets = [c for c in cases if os.path.exists(L/('cycle2/m2part_drat/%s_b%05d/ext.json' % (ms,c['b_index'])))]
        if ms == 'ms06': targets = [c for c in targets if c['b_index'] in MS06_CASES]
        for c in targets:
            p = 'cycle2/m2part_drat/%s_b%05d/ext.json' % (ms,c['b_index']); inputs[p] = digest(L/p)
            e = json.loads((L/p).read_bytes())
            assert e['index'] == c['b_index'] and e['num_placements'] == len(e['placements'])
            T = G.rows_of(d['skeletons'][c['b_index']],c0,19); t = [len(x) for x in T]
            feas,excl,wits = 0,[],[]
            for i,(A,B,P) in enumerate(e['placements']):
                check_placement(T,A,B,P,c0)
                if ms == 'ms09':
                    w = c1_L0(T,t,A,B,P)
                    if w is not None: assert verify_L0(T,t,A,B,P,w), ('witness re-check failed',ms,c['b_index'],i)
                else:
                    w = c1_L1(T,t,A,B,P)
                if w is None: excl.append(i)
                else: feas += 1
            ex = set(excl)
            full = [list(iv) for iv in intervals(e['num_placements']) if all(j in ex for j in range(iv[0],iv[1]+1))]
            out_cases[ms].append({'b_index':c['b_index'],'m1_tag':c['m1_tag'],'m2_open_now':c['m2_open_now'],'gps1_skeleton_feasible':c['feasible'],
                                  'list':p,'list_sha256':inputs[p],'num_placements':e['num_placements'],'feasible':feas,'excluded':len(excl),
                                  'excluded_indices':excl if len(excl) <= 2000 else None,'all_excluded':len(excl) == e['num_placements'],
                                  'fully_excluded_b100_intervals':full,'b100_intervals':len(intervals(e['num_placements']))})
    c13 = control13()
    b30b44 = {str(x['b_index']):x['all_excluded'] for x in out_cases['ms09'] if x['b_index'] in (30,44)}
    controls = {'C1_b30_b44_all_placements_excluded':b30b44,'C2_13row_model_each_P1_column_passes':c13['ok'],'C4_ms09_witnesses_rechecked':True,
                'C6_all_placements_valid_first_columns':True}
    allok = c13['ok'] and len(b30b44) == 2 and all(b30b44.values())
    summary = {}
    for ms,cs in out_cases.items():
        op = [x for x in cs if x['m2_open_now']]
        summary[ms] = {'cases_with_lists':len(cs),'open_now_with_lists':len(op),'open_placements':sum(x['num_placements'] for x in op),
                       'open_placements_excluded':sum(x['excluded'] for x in op),'open_cases_all_excluded':[x['b_index'] for x in op if x['all_excluded']],
                       'open_b100_intervals':sum(x['b100_intervals'] for x in op),
                       'open_b100_intervals_fully_excluded':sum(len(x['fully_excluded_b100_intervals']) for x in op)}
    out = {'schema':'PA19-GPS1C1-PROBE-v1','started_host_clock':started,'finished_host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
           'source_sha256':digest(__file__),'gps_probe_v1_sha256':digest(L/'src/gps_probe_v1.py'),'inputs':inputs,'controls':controls,
           'controls_all_expected':allok,'control_13row':c13,'summary':summary,'cases':out_cases,
           'scope':'necessary-condition probe only; excluded placements/intervals/cases are CANDIDATE structural exclusions pending '
                   'written-proof review and parent acceptance, and rest on the completeness of the frozen first-column lists; no solver; no PA19 claim'}
    dest = L/'cycle2'/('gps1c1-probe-%s.json' % stamp)
    with dest.open('x') as f: json.dump(out,f,indent=1); f.write('\n')
    print(dest,digest(dest),'controls_all_expected',allok,flush=True)
    print(json.dumps({'summary':summary,'controls':controls}),flush=True)


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+16*1024**2
        main()
