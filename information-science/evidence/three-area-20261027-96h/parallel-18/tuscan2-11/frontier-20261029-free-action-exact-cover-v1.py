#!/usr/bin/env python3
"""Exact search: 2-perfect Hamiltonian decompositions of K_m* invariant under a FREE group action.

A Hamiltonian decomposition D of K_m* is a set of m-1 directed Hamiltonian cycles using every
ordered pair of distinct vertices once as an arc ("D1").  D is 2-perfect if every ordered pair of
distinct vertices also occurs exactly once at cyclic distance 2 ("D2").  Cutting a 2-perfect
decomposition of K_12* at any vertex gives a linear Tuscan-2 square of order 11.

Model.  G (order g) acts freely on V = G x {0..r-1} by left multiplication, m = g*r.  An arc or a
distance-2 pair (x, y), x=(g1,a), y=(g2,b), has TYPE (a, b, g1^-1 g2); each type is a G-orbit of
exactly g pairs.  Every cycle of a G-invariant D has a cyclic stabilizer K=<k> acting as a rotation
by L = m/|K| positions, so the cycle is x_0..x_{L-1}, x_{j+L} = k x_j, with x_0..x_{L-1} a transversal
of the K-orbits; its G-orbit covers exactly the types of its first L arcs (resp. distance-2 pairs),
each type completely.  Hence G-invariant 2-perfect decompositions <-> exact covers of all D1 types and
all D2 types by such base cycles.  A cycle with trivial stabilizer ("free") covers m types.

The search is exhaustive: all stabilized base cycles are enumerated; free base cycles are enumerated
by depth-first search with the first vertex normalized to (e,0) (rotate the cycle to a layer-0 vertex
and translate).  The script also runs controls (known positive cases at m = 5, 7 and known negative
cases with written reasons) and an orbit-reconstruction self-check of every stabilized signature.
Usage: SCRIPT OUTPUT.json
"""
import hashlib
import json
import sys
import time
from collections import Counter
from pathlib import Path


def semidirect(m, k, u):
    els = [(i, j) for j in range(k) for i in range(m)]
    idx = {e: t for t, e in enumerate(els)}
    upow = [pow(u, j, m) for j in range(k)]
    return [[idx[((a[0] + upow[a[1]] * b[0]) % m, (a[1] + b[1]) % k)] for b in els] for a in els]


def perm_group(gens, npts):
    ident = tuple(range(npts))
    els, seen, frontier = [ident], {ident}, [ident]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                p = tuple(g[h[x]] for x in range(npts))
                if p not in seen:
                    seen.add(p); els.append(p); nxt.append(p)
        frontier = nxt
    idx = {e: t for t, e in enumerate(els)}
    return [[idx[tuple(a[b[x]] for x in range(npts))] for b in els] for a in els]


def check_group(mul):
    n = len(mul)
    e = [i for i in range(n) if all(mul[i][j] == j and mul[j][i] == j for j in range(n))]
    assert len(e) == 1, 'no unique identity'
    e = e[0]
    assert all(sorted(row) == list(range(n)) for row in mul), 'rows not permutations'
    assert all(sorted(mul[i][j] for i in range(n)) == list(range(n)) for j in range(n)), 'columns'
    assert all(mul[mul[a][b]][c] == mul[a][mul[b][c]] for a in range(n) for b in range(n) for c in range(n))
    inv = [next(j for j in range(n) if mul[i][j] == e) for i in range(n)]
    return e, inv


def model(mul, r):
    g = len(mul); e, inv = check_group(mul)
    V = [(x, a) for a in range(r) for x in range(g)]
    vid = {v: i for i, v in enumerate(V)}
    act = [[vid[(mul[k][x], a)] for (x, a) in V] for k in range(g)]
    types = {}
    for a in range(r):
        for b in range(r):
            for d in range(g):
                if not (a == b and d == e):
                    types[(a, b, d)] = len(types)
    T = [[None if x == y else types[(V[x][1], V[y][1], mul[inv[V[x][0]]][V[y][0]])]
          for y in range(len(V))] for x in range(len(V))]
    order = {}
    for k in range(g):
        o, cur = 1, k
        while cur != e:
            cur = mul[cur][k]; o += 1
        order[k] = o
    return {'g': g, 'e': e, 'm': len(V), 'act': act, 'T': T, 'nt': len(types), 'order': order}


def stabilized_signatures(M, use_d2=True):
    g, e, act, T, m = M['g'], M['e'], M['act'], M['T'], M['m']
    sigs = {}
    for k in range(g):
        if k == e or m % M['order'][k]:
            continue
        s = M['order'][k]; L = m // s
        orb = {}
        for x in range(m):
            cur, o = x, []
            for _ in range(s):
                o.append(cur); cur = act[k][cur]
            orb[x] = frozenset(o)

        def rec(seq, used):
            if len(seq) == L:
                xs = seq + [act[k][seq[0]]] + ([act[k][seq[1]]] if L >= 2 else [act[k][act[k][seq[0]]]])
                d1 = [T[xs[j]][xs[j + 1]] for j in range(L)]
                if None in d1 or len(set(d1)) != L:
                    return
                m1 = sum(1 << t for t in d1); m2 = 0
                if use_d2:
                    d2 = [T[xs[j]][xs[j + 2]] for j in range(L)]
                    if None in d2 or len(set(d2)) != L:
                        return
                    m2 = sum(1 << t for t in d2)
                sigs.setdefault((m1, m2), (k, list(seq)))
                return
            for x in range(m):
                if orb[x] in used:
                    continue
                seq.append(x); used.add(orb[x]); rec(seq, used); seq.pop(); used.discard(orb[x])
        rec([], set())
    return sigs


def make_cover(sigs, nt, use_d2=True):
    by_bit = {}
    for (m1, m2), wit in sigs.items():
        mask = m1 | (m2 << nt)
        mm = mask
        while mm:
            low = mm & -mm; by_bit.setdefault(low.bit_length() - 1, []).append((mask, wit)); mm ^= low

    def cover(target):
        out = []

        def rec(cov, chosen):
            if cov == target:
                out.append(list(chosen)); return True
            rem = target & ~cov; low = rem & -rem
            for mask, wit in by_bit.get(low.bit_length() - 1, []):
                if mask & cov or mask & ~target:
                    continue
                chosen.append(wit)
                if rec(cov | mask, chosen):
                    return True
                chosen.pop()
            return False
        rec(0, [])
        return out
    return cover


def search(M, use_d2=True, time_cap=600.0):
    """Exhaustive search for G-invariant Hamiltonian decompositions (2-perfect if use_d2)."""
    nt, m, T = M['nt'], M['m'], M['T']
    sigs = stabilized_signatures(M, use_d2)
    cover = make_cover(sigs, nt, use_d2)
    full = (1 << (2 * nt if use_d2 else nt)) - 1
    t0 = time.time(); stats = {'free_nodes': 0, 'free_leaves': 0}
    found = []

    def free_rec(covered, depth, free_list):
        res = cover(full & ~covered)
        if res:
            found.append({'free_base_cycles': [list(f) for f in free_list], 'stabilized': res[0]}); return True
        rem1 = bin((full & ~covered) & ((1 << nt) - 1)).count('1')
        if rem1 < m:
            return False
        seq = [0]; used = [1]

        def rec(m1, m2):
            stats['free_nodes'] += 1
            if (stats['free_nodes'] & 0x3FFF) == 0 and time.time() - t0 > time_cap:
                raise TimeoutError
            if len(seq) == m:
                a = T[seq[-1]][seq[0]]
                if (covered | m1) >> a & 1:
                    return False
                nm1 = m1 | (1 << a); nm2 = m2
                if use_d2:
                    b1 = T[seq[-2]][seq[0]]; b2 = T[seq[-1]][seq[1]]
                    c2 = covered >> nt
                    if b1 == b2 or (c2 | m2) >> b1 & 1 or (c2 | m2) >> b2 & 1:
                        return False
                    nm2 = m2 | (1 << b1) | (1 << b2)
                stats['free_leaves'] += 1
                return free_rec(covered | nm1 | (nm2 << nt if use_d2 else 0), depth + 1, free_list + [list(seq)])
            last = seq[-1]; prev = seq[-2] if len(seq) >= 2 else None
            c1 = covered & ((1 << nt) - 1); c2 = covered >> nt if use_d2 else 0
            for x in range(m):
                if used[0] >> x & 1:
                    continue
                t1 = T[last][x]
                if (c1 | m1) >> t1 & 1:
                    continue
                nm2 = m2
                if use_d2 and prev is not None:
                    t2 = T[prev][x]
                    if (c2 | m2) >> t2 & 1:
                        continue
                    nm2 = m2 | (1 << t2)
                seq.append(x); used[0] |= 1 << x
                ok = rec(m1 | (1 << t1), nm2)
                used[0] &= ~(1 << x); seq.pop()
                if ok:
                    return True
            return False
        return rec(0, 0)
    try:
        free_rec(0, 0, [])
        status = 'found' if found else 'exhausted'
    except TimeoutError:
        status = 'time_cap'
    return {'status': status, 'signatures': len(sigs), 'types': nt, 'seconds': round(time.time() - t0, 2),
            **stats, 'witness': found[0] if found else None}


def verify_witness(M, w):
    """Rebuild the full decomposition from a witness and check D1 (and D2) exactness directly."""
    act, m, g = M['act'], M['m'], M['g']

    def canon(c):
        i = c.index(min(c)); return c[i:] + c[:i]
    cycles = set()
    for f in w['free_base_cycles']:
        cycles |= {canon(tuple(act[h][x] for x in f)) for h in range(g)}
    for k, seq in w['stabilized']:
        s = M['order'][k]; L = m // s; full = list(seq)
        while len(full) < m:
            full.append(act[k][full[len(full) - L]])
        cycles |= {canon(tuple(act[h][x] for x in full)) for h in range(g)}
    arcs = Counter((c[j], c[(j + 1) % m]) for c in cycles for j in range(m))
    steps = Counter((c[j], c[(j + 2) % m]) for c in cycles for j in range(m))
    return {'cycles': len(cycles), 'd1_exact': len(arcs) == m * (m - 1) and max(arcs.values()) == 1,
            'd2_exact': len(steps) == m * (m - 1) and max(steps.values()) == 1}


def signature_selfcheck(M, sigs):
    act, m, g, T = M['act'], M['m'], M['g'], M['T']
    bad = 0
    for (m1, m2), (k, seq) in sigs.items():
        s = M['order'][k]; L = m // s; full = list(seq)
        while len(full) < m:
            full.append(act[k][full[len(full) - L]])
        orbit = {tuple(act[h][x] for x in full) for h in range(g)}
        arcs = Counter(); steps = Counter()
        for c in orbit:
            for j in range(m):
                arcs[(c[j], c[(j + 1) % m])] += 1; steps[(c[j], c[(j + 2) % m])] += 1
        t1 = Counter(T[x][y] for (x, y) in arcs); t2 = Counter(T[x][y] for (x, y) in steps)
        ok = (len(set(full)) == m and set(t1) == {t for t in range(M['nt']) if m1 >> t & 1}
              and set(t2) == {t for t in range(M['nt']) if m2 >> t & 1}
              and all(v == g for v in t1.values()) and all(v == g for v in t2.values()))
        bad += not ok
    return {'checked': len(sigs), 'failures': bad}


def main(argv):
    if len(argv) != 2:
        raise SystemExit('usage: SCRIPT OUTPUT.json')
    out = Path(argv[1])
    groups = {
        'Z6': semidirect(6, 1, 1), 'S3': semidirect(3, 2, 2),
        'Z12': semidirect(12, 1, 1), 'Z6xZ2': semidirect(6, 2, 1), 'D12': semidirect(6, 2, 5),
        'Dic3': semidirect(3, 4, 2), 'A4': perm_group([(1, 2, 0, 3), (1, 0, 3, 2)], 4),
        'Z5': semidirect(5, 1, 1), 'Z7': semidirect(7, 1, 1), 'Z8': semidirect(8, 1, 1),
        'D8': semidirect(4, 2, 3), 'Z3': semidirect(3, 1, 1),
    }
    runs = []
    plan = [
        ('target', 'Z6', 2, True), ('target', 'S3', 2, True),
        ('target', 'Z12', 1, True), ('target', 'Z6xZ2', 1, True), ('target', 'D12', 1, True),
        ('target', 'Dic3', 1, True), ('target', 'A4', 1, True),
        ('positive_control', 'Z5', 1, True), ('positive_control', 'Z7', 1, True),
        ('positive_control_d1_only', 'Z3', 3, False),
        ('negative_control_written_reason', 'Z5', 2, False), ('negative_control_written_reason', 'Z8', 1, False),
        ('negative_control_written_reason', 'D8', 1, False),
    ]
    for role, gname, r, use_d2 in plan:
        M = model(groups[gname], r)
        res = search(M, use_d2=use_d2, time_cap=900.0)
        rec = {'role': role, 'group': gname, 'orbits': r, 'vertices': M['m'], 'two_perfect_required': use_d2, **res}
        if res['witness'] is not None:
            rec['witness_check'] = verify_witness(M, res['witness'])
        if role == 'target' and r == 2:
            rec['signature_selfcheck'] = signature_selfcheck(M, stabilized_signatures(M, True))
        runs.append(rec)
        print(json.dumps({k: rec[k] for k in ('role', 'group', 'orbits', 'vertices', 'two_perfect_required',
                                                'status', 'seconds')} | ({'witness_check': rec['witness_check']}
                                                                       if 'witness_check' in rec else {})))
    result = {'kind': 'free_action_exact_cover_search', 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'runs': runs,
              'scope': 'Exhaustive within the stated free-action model; a found witness is rechecked from the rebuilt cycles.'}
    with out.open('x', encoding='utf-8') as fh:
        json.dump(result, fh, indent=1, sort_keys=True); fh.write('\n')


if __name__ == '__main__':
    main(sys.argv)
