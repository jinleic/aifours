#!/usr/bin/env python3
"""GPS-1 probe: the global pair-structure necessary condition for the all-P1 multisets ms06 (E2b, L=1) and ms09
(E3c, L=0), frozen in README (Amendment GPS-1) before execution. Pure Python over the frozen skeleton lists; no
solver, checker, CNF or native child. One lane metadata token. Creation-only receipt cycle2/gps1-probe-<stamp>.json.

Setting (any skeleton case of a multiset with c0 P0 columns (4,3,...,3) and m P1 columns (4,4,3,...,3,2), N rows,
k = c0+m columns, L = N(N-1)/2 - sum_c kappa_c): every row r has P0-quad set T(r) (t = |T(r)|) and, in P1 column j,
e_j(r) = block size - 3 in {+1, 0, -1}. Validity gives  t(r) + sum_j e_j(r) = (N-1-2k) - l(r)  with l(r) the number of
rows r agrees with nowhere (exactly L row pairs agree nowhere). With n2(r) = #{j: e_j(r) = -1} (pair blocks) and
n4(r) = #{j: e_j(r) = +1}:  n4 - n2 = D - l - t (D = N-1-2k)  and  0 <= n4 <= m - n2, so
    max(0, t + l - D) <= n2(r) <= floor((m - D + t + l) / 2)      (also n2 <= m).
GPS-1: a valid array of the case yields (i) a set E of m DISTINCT row pairs (the pair block of each P1 column),
(ii) when L = 1 the unique leave pair {x, y}, such that
    P1  every {u, v} in E has T(u) and T(v) disjoint (u, v agree in their P1 column, so in no P0 column);
    P2  every row satisfies the n2 bounds above with l(r) = 1 iff r in {x, y};
    P3  (L = 1) T(x) and T(y) are disjoint and {x, y} is not in E (x, y agree nowhere).
A skeleton with no (E, leave) satisfying P1-P3 admits no packing array (necessary condition only; feasibility of
GPS-1 says nothing about existence).
Usage: gps_probe_v1.py
"""
import collections
import hashlib
import itertools
import json
import os
import time
from pathlib import Path

import m2_supervised_runtime_v6_3 as R

L = Path(__file__).resolve().parents[1]
LISTS = {'ms06':{'m1':'skeletons/skeletons-ms06.json','b':'cycle2/skel-b/skeletons-b-ms06.json','map':'cycle2/skel-b/compare-map-ms06.json'},
         'ms09':{'m1':'skeletons/skeletons-ms09.json','b':'cycle2/skel-b/skeletons-b-ms09.json','map':'cycle2/skel-b/compare-map-ms09.json'}}
STATUS = ('STATUS17.json',None)  # pinned by SHA in the receipt; read-only
POST_STATUS_RESOLVED = {  # M2 b-index cases resolved after STATUS17 (README V6-PRODUCTION; parent b30/b44 verdict)
    'ms06':{182:'v6 M6 UNSAT checked (cycle2/m2skel_drat/ms06_b00182_v6.json)',201:'v6 M6 UNSAT checked (cycle2/m2skel_drat/ms06_b00201_v6.json)'},
    'ms09':{30:'parent structural verdict b30/b44 v1',44:'parent structural verdict b30/b44 v1'}}
CONTROL13 = {'skeletons':'controls/skel13/skeletons-ms07.json','model':'controls/c13skel/models/ms07_s00001.txt','skel_index':1}


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def rows_of(sk,c0,N):
    """T-sets of all N rows: one row per edge/hyperedge ('edges'/'hyper' or 'types'), 4-deg private rows per quad, 'empty' rows."""
    multi = [frozenset(t) for t in sk['types']] if 'types' in sk else [frozenset(e) for e in sk['edges']]+[frozenset(h) for h in sk['hyper']]
    assert all(len(t) >= 2 and t <= set(range(c0)) for t in multi)
    deg = [sum(i in t for t in multi) for i in range(c0)]
    assert all(d <= 4 for d in deg), 'quad degree > 4'
    rows = multi+[frozenset([i]) for i in range(c0) for _ in range(4-deg[i])]+[frozenset()]*sk['empty']
    assert len(rows) == N, ('row count',len(rows),N)
    assert all(len(rows[a] & rows[b]) <= 1 for a,b in itertools.combinations(range(N),2)), 'two rows share two quads'
    return rows


def bounds(t,l,m,D):
    return max(0,t+l-D),min(m,(m-D+t+l)//2)


def verify_structure(rows,E,leave,m,Lval,D):
    """Independent re-check of P1-P3 for one candidate structure (used for every reported witness and the control)."""
    N = len(rows)
    if len(E) != m or len(set(map(frozenset,E))) != m or any(a == b for a,b in E): return False
    if any(rows[a] & rows[b] for a,b in E): return False
    lv = set(leave) if leave else set()
    if Lval == 1:
        if not leave or len(lv) != 2 or rows[leave[0]] & rows[leave[1]] or frozenset(leave) in set(map(frozenset,E)): return False
    elif leave: return False
    n2 = collections.Counter(x for e in E for x in e)
    for r in range(N):
        lo,hi = bounds(len(rows[r]),1 if r in lv else 0,m,D)
        if not lo <= n2[r] <= hi: return False
    return True


def search(rows,m,Lval,D):
    """Exhaustive search for (E, leave) satisfying P1-P3. Returns (witness or None, explored E-sets, reason)."""
    N = len(rows); t = [len(r) for r in rows]
    b0 = [bounds(t[i],0,m,D) for i in range(N)]; b1 = [bounds(t[i],1,m,D) for i in range(N)]
    if Lval == 0 and any(lo > hi for lo,hi in b0): return None,0,'row degree bounds infeasible'
    if sum(lo for lo,_ in b0) > 2*m: return None,0,'required pair memberships exceed 2m'
    can_pair = [b0[i][1] >= 1 or (Lval == 1 and b1[i][1] >= 1) for i in range(N)]
    for i in range(N):
        need = b0[i][0]
        if need >= 1 and sum(1 for j in range(N) if j != i and can_pair[j] and not rows[i] & rows[j]) < need:
            return None,0,'insufficient eligible pair partners for a row needing %d pair blocks' % need
    cand = [(a,b) for a,b in itertools.combinations(range(N),2) if can_pair[a] and can_pair[b] and not rows[a] & rows[b]]
    disj = [sum(1 << j for j in range(N) if j != i and not rows[i] & rows[j]) for i in range(N)]
    explored = 0
    for E in itertools.combinations(cand,m):
        explored += 1
        n2 = [0]*N
        for a,b in E: n2[a] += 1; n2[b] += 1
        if Lval == 0:
            if all(b0[i][0] <= n2[i] <= b0[i][1] for i in range(N)): return (list(E),None),explored,None
            continue
        bad = [i for i in range(N) if not b0[i][0] <= n2[i] <= b0[i][1]]
        if len(bad) > 2 or any(not b1[i][0] <= n2[i] <= b1[i][1] for i in bad): continue
        part = [0]*N
        for a,b in E: part[a] |= 1 << b; part[b] |= 1 << a
        s1 = sum(1 << i for i in range(N) if b1[i][0] <= n2[i] <= b1[i][1])
        xs = [bad[0]] if bad else [i for i in range(N) if s1 >> i & 1]
        for x in xs:
            ys = disj[x] & s1 & ~part[x]
            if len(bad) == 2: ys &= 1 << bad[1]
            if ys:
                y = (ys & -ys).bit_length()-1
                return (list(E),(x,y)),explored,None
    return None,explored,'exhaustive: no pair structure satisfies P1-P3'


def run_list(path,N,k):
    d = json.loads((L/path).read_bytes()); c0,m = d['c0'],len(d['profiles'])-d['c0']
    profs = collections.Counter(tuple(p) for p in d['profiles'])
    assert profs == collections.Counter({(4,3,3,3,3,3):c0,(4,4,3,3,3,2):m}), ('not an all-P1 multiset',path,profs)
    D = N-1-2*k; Lval = d['L']
    out = []
    for idx,sk in enumerate(d['skeletons']):
        rows = rows_of(sk,c0,N)
        w,explored,reason = search(rows,m,Lval,D)
        if w is not None: assert verify_structure(rows,w[0],w[1],m,Lval,D), ('witness failed independent re-check',path,idx)
        hist = collections.Counter(len(r) for r in rows)
        out.append({'index':idx,'t_hist':{str(t):hist[t] for t in sorted(hist)},'feasible':w is not None,'explored_E_sets':explored,'reason':reason,
                    'witness':None if w is None else {'pairs':[[a,b] for a,b in w[0]],'leave':list(w[1]) if w[1] else None,
                                                      'pair_T':[[sorted(rows[a]),sorted(rows[b])] for a,b in w[0]]}})
    return d,c0,m,Lval,D,out


def control13():
    """Positive semantic control: the known (13,5,4) L=0 analog SAT model (profiles (4,4,3,2)^3 + (4,3,3,3)^2)."""
    A = [list(map(int,s.split())) for s in (L/CONTROL13['model']).read_text().split('\n') if s.strip()]
    N,k = len(A),len(A[0])
    agree = [sum(A[a][c] == A[b][c] for c in range(k)) for a,b in itertools.combinations(range(N),2)]
    assert max(agree) <= 1, 'control model invalid'
    prof = []
    for c in range(k):
        cnt = collections.Counter(A[r][c] for r in range(N)); prof.append(tuple(sorted(cnt.values(),reverse=True)))
    p0 = [c for c in range(k) if prof[c] == (4,3,3,3)]; p1 = [c for c in range(k) if prof[c] == (4,4,3,2)]
    assert len(p0) == 2 and len(p1) == 3
    quad = {c:next(s for s,n in collections.Counter(A[r][c] for r in range(N)).items() if n == 4) for c in p0}
    rows = [frozenset(i for i,c in enumerate(p0) if A[r][c] == quad[c]) for r in range(N)]
    E = []
    for c in p1:
        s2 = next(s for s,n in collections.Counter(A[r][c] for r in range(N)).items() if n == 2)
        E.append(tuple(r for r in range(N) if A[r][c] == s2))
    Lval = N*(N-1)//2-sum(sum(n*(n-1)//2 for n in collections.Counter(A[r][c] for r in range(N)).values()) for c in range(k))
    D = N-1-2*k
    true_ok = verify_structure(rows,E,None,len(p1),Lval,D)
    w,explored,reason = search(rows,len(p1),Lval,D)
    sk = json.loads((L/CONTROL13['skeletons']).read_bytes())
    ref = rows_of(sk['skeletons'][CONTROL13['skel_index']],sk['c0'],sk['N'])
    same_t = sorted(len(r) for r in ref) == sorted(len(r) for r in rows)
    return {'model':CONTROL13['model'],'model_sha256':digest(L/CONTROL13['model']),'N':N,'k':k,'L':Lval,'D':D,'max_pair_agreement':max(agree),
            'p0_columns':p0,'p1_columns':p1,'true_pairs':[list(e) for e in E],'true_structure_satisfies_P1_P3':true_ok,
            'search_feasible':w is not None,'reference_skeleton_t_multiset_matches':same_t,
            'ok':Lval == 0 and true_ok and w is not None and same_t}


def main():
    stamp = time.strftime('%Y%m%dT%H%M%S'); started = time.strftime('%Y-%m-%dT%H:%M:%S%z')
    status = json.loads((L/STATUS[0]).read_bytes())
    open_tags = set(status['M2_open_tags'])
    res,checks = {},{}
    for ms,paths in LISTS.items():
        db,c0,m,Lval,D,outb = run_list(paths['b'],19,8)
        d1,_,_,_,_,out1 = run_list(paths['m1'],19,8)
        a_to_b = json.loads((L/paths['map']).read_bytes())['a_to_b']
        b_to_a = {b:a for a,b in enumerate(a_to_b)}
        same = all(out1[a]['feasible'] == outb[b]['feasible'] for a,b in enumerate(a_to_b))
        resolved_after = POST_STATUS_RESOLVED[ms]
        cases = []
        for o in outb:
            tag = '%s_s%05d' % (ms,b_to_a[o['index']])
            m2_open_status17 = tag in open_tags
            open_now = m2_open_status17 and o['index'] not in resolved_after
            cases.append(dict(o,b_index=o['index'],m1_tag=tag,m2_open_status17=m2_open_status17,
                              resolved_after_status17=resolved_after.get(o['index']),m2_open_now=open_now))
        excl = [x for x in cases if not x['feasible']]
        res[ms] = {'c0':c0,'m':m,'L':Lval,'D':D,'skeletons':len(cases),'gps_excluded':len(excl),'gps_feasible':len(cases)-len(excl),
                   'm2_open_status17':sum(x['m2_open_status17'] for x in cases),'m2_open_now':sum(x['m2_open_now'] for x in cases),
                   'm2_open_now_gps_excluded':sorted(x['b_index'] for x in cases if x['m2_open_now'] and not x['feasible']),
                   'm2_open_now_gps_feasible':sorted(x['b_index'] for x in cases if x['m2_open_now'] and x['feasible']),
                   'excluded_reason_counts':dict(collections.Counter(x['reason'] for x in excl)),
                   'm1_list_vs_independent_list_same_verdicts':same,'cases':cases}
        checks['C3_'+ms+'_lists_agree_under_bijection'] = same
    known = {3:'b3 parent structural',30:'b30 parent verdict',44:'b44 parent verdict'}
    checks['C1_known_ms09_exclusions'] = {str(b):not res['ms09']['cases'][b]['feasible'] for b in known}
    c13 = control13(); checks['C2_13row_sat_model_positive_control'] = c13['ok']
    checks['C4_every_witness_rechecked'] = True  # enforced by assert in run_list
    allok = all(v if isinstance(v,bool) else all(v.values()) for v in checks.values())
    out = {'schema':'PA19-GPS1-PROBE-v1','started_host_clock':started,'finished_host_clock':time.strftime('%Y-%m-%dT%H:%M:%S%z'),
           'source_sha256':digest(__file__),
           'inputs':{**{p:digest(L/p) for v in LISTS.values() for p in v.values()},STATUS[0]:digest(L/STATUS[0]),
                     CONTROL13['skeletons']:digest(L/CONTROL13['skeletons']),CONTROL13['model']:digest(L/CONTROL13['model'])},
           'post_status17_resolved':{ms:{str(b):why for b,why in v.items()} for ms,v in POST_STATUS_RESOLVED.items()},
           'controls':checks,'controls_all_expected':allok,'control_13row':c13,'results':res,
           'scope':'necessary-condition probe only; an excluded skeleton is a CANDIDATE structural exclusion pending written-proof review and '
                   'parent acceptance; a feasible skeleton is not evidence of existence; no solver/checker; no PA19 claim'}
    dest = L/'cycle2'/('gps1-probe-%s.json' % stamp)
    with dest.open('x') as f: json.dump(out,f,indent=1); f.write('\n')
    print(dest,digest(dest),'controls_all_expected',allok,flush=True)
    for ms,v in res.items():
        print(ms,{k:v[k] for k in ('skeletons','gps_excluded','gps_feasible','m2_open_status17','m2_open_now','excluded_reason_counts')},flush=True)
        print(ms,'open-now excluded',v['m2_open_now_gps_excluded'],flush=True)
    print('checks',json.dumps(checks),flush=True)


if __name__ == '__main__':
    R.install_handlers()
    with R.Capacity(time.monotonic()+3600,metadata=True,wait_allowance=60):
        s = os.statvfs(L); assert s.f_bavail*s.f_frsize >= R.BASE_GATE+16*1024**2
        main()
