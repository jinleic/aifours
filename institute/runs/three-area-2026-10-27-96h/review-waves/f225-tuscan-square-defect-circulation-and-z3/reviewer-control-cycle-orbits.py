#!/usr/bin/env python3
"""Construct and inspect a small symmetric D1 Hamiltonian decomposition.
This is a control, not a T2(11) witness and not an exclusion search.
"""
import collections
import hashlib
import itertools
import json
import os
import signal
import subprocess
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))

def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()

def timeout(_signum, _frame):
    raise TimeoutError('60-second cap, search incomplete: UNKNOWN')

def run(q):
    r = 4 if q == 2 else 3
    m = q * r
    def g(v):
        return v // q * q + (v % q + 1) % q
    def canonical(c):
        i = c.index(0)
        return tuple(c[i:] + c[:i])
    def transform(c):
        return canonical([g(v) for v in c])
    def typ(x, y):
        return (x // q, y // q, (y % q - x % q) % q)
    types = [(a, b, d) for a in range(r) for b in range(r) for d in range(q)
             if a != b or d != 0]
    idx = {t: i for i, t in enumerate(types)}
    candidates = []
    seen = set()
    for suffix in itertools.permutations(range(1, m)):
        c = (0,) + suffix
        if c in seen:
            continue
        orbit = []
        cur = c
        while cur not in orbit:
            orbit.append(cur)
            cur = transform(cur)
        assert cur == c and q % len(orbit) == 0
        seen.update(orbit)
        typecounts = collections.Counter(typ(v[j], v[(j + 1) % m])
                                         for v in orbit for j in range(m))
        if any(count != q for count in typecounts.values()):
            continue
        bits = sum(1 << idx[t] for t in typecounts)
        candidates.append((bits, tuple(orbit)))
    bytype = [[] for _ in types]
    for ci, (bits, _orbit) in enumerate(candidates):
        for i in range(len(types)):
            if bits & (1 << i):
                bytype[i].append(ci)
    full = (1 << len(types)) - 1
    nodes = 0
    def cover(used):
        nonlocal nodes
        nodes += 1
        if used == full:
            return []
        best = None
        for i, options in enumerate(bytype):
            if used & (1 << i):
                continue
            eligible = [j for j in options if not (candidates[j][0] & used)]
            if not eligible:
                return None
            if best is None or len(eligible) < len(best):
                best = eligible
        for j in best:
            rest = cover(used | candidates[j][0])
            if rest is not None:
                return [j] + rest
        return None
    chosen = cover(0)
    if chosen is None:
        return {'status': 'NO_WITNESS_FOUND_BY_FINITE_SEARCH', 'nodes': nodes,
                'warning': 'Not used as a no-go claim.'}
    orbits = [candidates[j][1] for j in chosen]
    cycles = [v for orbit in orbits for v in orbit]
    assert len(cycles) == m - 1
    one = collections.Counter((v[j], v[(j + 1) % m]) for v in cycles for j in range(m))
    assert all(one[(x, y)] == 1 for x in range(m) for y in range(m) if x != y)
    two = collections.Counter((v[j], v[(j + 2) % m]) for v in cycles for j in range(m))
    assert all(two[(x, x)] == 0 for x in range(m))
    assert all(sum(two[(x, y)] for y in range(m)) == m - 1 for x in range(m))
    assert all(sum(two[(x, y)] for x in range(m)) == m - 1 for y in range(m))
    mu = {}
    for a, b, d in types:
        vals = [two[(a*q+t, b*q+(t+d)%q)] for t in range(q)]
        assert len(set(vals)) == 1
        mu[(a,b,d)] = vals[0]
    w = {t: mu[t] - 1 for t in types}
    assert all(sum(v for t, v in w.items() if t[0] == a) == 0 for a in range(r))
    assert all(sum(v for t, v in w.items() if t[1] == a) == 0 for a in range(r))
    all_one, all_two = collections.Counter(), collections.Counter()
    stabilizers = collections.Counter()
    for orbit in orbits:
        c = orbit[0]
        s = q // len(orbit)
        L = m // s
        assert any(all(c[(j+L)%m] == (lambda x, t: perm_power(g, x, t))(c[j], k)
                       for j in range(m)) for k in range(q))
        first = collections.Counter(typ(c[j], c[(j+1)%m]) for j in range(L))
        second = collections.Counter(typ(c[j], c[(j+2)%m]) for j in range(L))
        firstfull = collections.Counter(typ(v[j], v[(j+1)%m]) for v in orbit for j in range(m))
        secondfull = collections.Counter(typ(v[j], v[(j+2)%m]) for v in orbit for j in range(m))
        assert all(firstfull[t] == q*first[t] and secondfull[t] == q*second[t] for t in types)
        assert (sum(t[2]*v for t,v in second.items()) - 2*sum(t[2]*v for t,v in first.items())) % q == 0
        all_one.update(first)
        all_two.update(second)
        stabilizers[str(s)] += 1
    assert all(all_one[t] == 1 and all_two[t] == mu[t] for t in types)
    S = sum(t[2] for t in types)
    assert (sum(t[2]*v for t,v in w.items()) - S) % q == 0
    assert S % q == 0
    P = sum(max(v, 0) for v in w.values())
    assert P != 1
    # Intended-reason negative: duplicating an actual cycle destroys D1 uniqueness.
    bad = cycles[:-1] + cycles[:1]
    badone = collections.Counter((v[j], v[(j+1)%m]) for v in bad for j in range(m))
    assert any(v > 1 for v in badone.values())
    # Independent algebraic negative: perturbing the jump total violates (10).
    moment = sum(t[2]*v for t,v in w.items())
    assert (moment + 1 - S) % q != 0
    return {'status': 'PASS', 'q': q, 'vertices': m, 'layers': r,
            'cycles': [list(v) for v in cycles], 'candidate_orbits': len(candidates),
            'exact_cover_nodes': nodes, 'cycle_orbit_stabilizers': dict(stabilizers),
            'type_excess_P': P, 'type_baseline_jump_S_mod_q': S % q,
            'negative_duplicate_cycle': 'rejected: duplicate distance-one arc',
            'negative_perturbed_jump': 'rejected: nonzero conservation residue',
            'scope': 'Actual smaller Hamiltonian decomposition; no T2 cut assumed, not a witness for the target.'}

def perm_power(g, x, k):
    for _ in range(k):
        x = g(x)
    return x

def main():
    q = int(sys.argv[1])
    assert q in (2, 3)
    out = {'started_native': clock(), 'source_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
           'cap_seconds': 60, 'q': q}
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(60)
    rc = 0
    try:
        out['result'] = run(q)
        if out['result']['status'] != 'PASS':
            rc = 2
    except TimeoutError as exc:
        out['result'] = {'status': 'UNKNOWN_TIMEOUT', 'detail': str(exc)}
        rc = 124
    except Exception:
        out['result'] = {'status': 'FAIL', 'detail': traceback.format_exc()}
        rc = 1
    finally:
        signal.alarm(0)
        out['ended_native'] = clock()
        out['program_exit_intended'] = rc
        text = json.dumps(out, indent=2, sort_keys=True) + '\n'
        with open(os.path.join(HERE, f'reviewer-control-cycle-orbits-q{q}-result.json'), 'x', encoding='utf-8') as f:
            f.write(text)
        print(text, end='')
    return rc

if __name__ == '__main__':
    sys.exit(main())
