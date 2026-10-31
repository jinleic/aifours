#!/usr/bin/env python3
"""Independent small-array and finite signed-type controls; not author code."""
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
RESULT = os.path.join(HERE, 'reviewer-control-f225-result.json')

def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()

def timed_out(_signum, _frame):
    raise TimeoutError('90-second control cap; incomplete means UNKNOWN')

def pairs(seq, step):
    return [(seq[i], seq[i + step]) for i in range(len(seq) - step)]

def mask(pairs_):
    v = 0
    for a, b in pairs_:
        v |= 1 << (a * 12 + b)
    return v

def matrix_checks(rows):
    n = len(rows)
    inf = n
    m = n + 1
    adjacent = [e for row in rows for e in pairs(row, 1)]
    linear2 = [e for row in rows for e in pairs(row, 2)]
    assert len(set(adjacent)) == n * (n - 1), 'duplicate distance-one event'
    assert len(set(linear2)) == n * (n - 2), 'duplicate distance-two event'
    assert len({row[0] for row in rows}) == n and len({row[-1] for row in rows}) == n
    cycles = tuple((inf,) + tuple(row) for row in rows)
    b = [[0] * m for _ in range(m)]
    for cycle in cycles:
        for j, x in enumerate(cycle):
            b[x][cycle[(j + 2) % m]] += 1
    w = [[b[x][y] - (x != y) for y in range(m)] for x in range(m)]
    assert all(w[x][x] == 0 for x in range(m))
    assert all(sum(w[x]) == 0 for x in range(m))
    assert all(sum(w[x][y] for x in range(m)) == 0 for y in range(m))
    missing = {(x, y) for x in range(n) for y in range(n) if x != y} - set(linear2)
    closing = {(row[-1], row[0]) for row in rows}
    p = collections.Counter(row[-2] for row in rows)
    s = collections.Counter(row[1] for row in rows)
    assert len(missing) == len(closing) == n
    for x in range(n):
        for y in range(n):
            if x != y:
                assert w[x][y] == ((x, y) in closing) - ((x, y) in missing)
        assert w[x][inf] == p[x] - 1 and w[inf][x] == s[x] - 1
    delta = len(closing - missing)
    zp = sum(p[x] == 0 for x in range(n))
    zs = sum(s[x] == 0 for x in range(n))
    f = sum(max(0, w[x][y]) for x in range(m) for y in range(m))
    assert f == delta + zp + zs and zp <= delta and zs <= delta
    assert sum(w[x][y] == -1 for x in range(m) for y in range(m)) == f
    assert (delta == 0) == (f == 0)
    assert f != 1
    if f == 2:
        positive = [(x, y) for x in range(m) for y in range(m) if w[x][y] > 0]
        negative = [(x, y) for x in range(m) for y in range(m) if w[x][y] < 0]
        assert len(positive) == len(negative) == 2
        assert len({x for x, _ in positive}) == len({y for _, y in positive}) == 2
        assert {x for x, _ in positive} == {x for x, _ in negative}
        assert {y for _, y in positive} == {y for _, y in negative}
    if delta == 1:
        a, b0 = next(iter(closing - missing))
        c, d = next(iter(missing - closing))
        assert zp == (a != c) and zs == (b0 != d) and f in (2, 3)
    return cycles, b, w, f, delta

def canonical(cycle, inf):
    j = cycle.index(inf)
    return tuple(cycle[j:] + cycle[:j])

def perm_power(g, x, k):
    for _ in range(k):
        x = g[x]
    return x

def semiregular_perms(m, q):
    return [g for g in itertools.permutations(range(m))
            if all(g[x] != x and perm_power(g, x, q) == x for x in range(m))]

def symmetry_checks(cycles, b, w, f, delta, g, q, counts):
    m = len(cycles[0])
    n = m - 1
    r = m // q
    inf = n
    assert m % q == 0
    remaining = set(range(m))
    starts = [inf]
    layers = []
    while remaining:
        start = starts.pop() if starts else min(remaining)
        if start not in remaining:
            continue
        orbit = [perm_power(g, start, j) for j in range(q)]
        assert len(set(orbit)) == q and set(orbit) <= remaining
        remaining -= set(orbit)
        layers.append(orbit)
    coord = {x: (a, t) for a, orbit in enumerate(layers) for t, x in enumerate(orbit)}
    assert layers[0][0] == inf and len(layers) == r
    types = [(a, z, d) for a in range(r) for z in range(r) for d in range(q)
             if not (a == z and d == 0)]
    def typ(x, y):
        a, t = coord[x]
        z, u = coord[y]
        return (a, z, (u - t) % q)
    mu = {lam: b[layers[lam[0]][0]][layers[lam[1]][lam[2]]] for lam in types}
    for a, z, d in types:
        assert all(b[layers[a][t]][layers[z][(t + d) % q]] == mu[(a, z, d)]
                   for t in range(q))
    tw = {lam: mu[lam] - 1 for lam in types}
    assert all(sum(v for (a, _, _), v in tw.items() if a == z) == 0 for z in range(r))
    assert all(sum(v for (_, b0, _), v in tw.items() if b0 == z) == 0 for z in range(r))
    S = sum(d for _, _, d in types)
    assert (sum(d * v for (_, _, d), v in tw.items()) - S) % q == 0
    P = sum(max(v, 0) for v in tw.values())
    assert f == q * P
    # Verify each actual cycle orbit contributes one type occurrence per period position.
    unseen = set(cycles)
    first_all = collections.Counter()
    second_all = collections.Counter()
    while unseen:
        c = next(iter(unseen))
        orbit = set()
        curr = c
        while curr not in orbit:
            orbit.add(curr)
            curr = canonical([g[x] for x in curr], inf)
        assert orbit <= set(cycles)
        unseen -= orbit
        stabilizer = q // len(orbit)
        L = m // stabilizer
        assert len(orbit) * stabilizer == q
        assert any(all(c[(j + L) % m] == perm_power(g, c[j], t)
                       for j in range(m)) for t in range(q))
        jumps = [typ(c[j], c[(j + 1) % m])[2] for j in range(m)]
        assert all(jumps[j] == jumps[(j + L) % m] for j in range(m))
        one_period = collections.Counter(typ(c[j], c[(j + 1) % m]) for j in range(L))
        two_period = collections.Counter(typ(c[j], c[(j + 2) % m]) for j in range(L))
        one_full = collections.Counter(typ(v[j], v[(j + 1) % m]) for v in orbit for j in range(m))
        two_full = collections.Counter(typ(v[j], v[(j + 2) % m]) for v in orbit for j in range(m))
        assert all(one_full[t] == q * one_period[t] and two_full[t] == q * two_period[t]
                   for t in types)
        assert (sum(t[2] * count for t, count in two_period.items()) -
                2 * sum(t[2] * count for t, count in one_period.items())) % q == 0
        first_all.update(one_period)
        second_all.update(two_period)
        counts['cycle_orbits_by_q_stabilizer'][f'{q}/{stabilizer}'] += 1
    assert all(first_all[t] == 1 and second_all[t] == mu[t] for t in types)
    if S % q == 0:
        assert P != 1
    if q == 3:
        assert P in (0, 2)
        O = set(layers[0])
        for c in cycles:
            assert all(not {c[j], c[(j + 1) % m], c[(j + 2) % m]} <= O for j in range(m))
        pos = [t for t in types if tw[t] > 0]
        assert all(tw[t] == 1 and ((t[0] == 0) != (t[1] == 0)) for t in pos)
        assert sum(t[0] == 0 for t in pos) <= 1
        assert sum(t[1] == 0 for t in pos) <= 1
        if P == 2:
            assert f == 6 and delta == 4
            assert sum(w[x][inf] == -1 for x in range(n)) == 1
            assert sum(w[inf][x] == -1 for x in range(n)) == 1
    counts[f'q{q}_valid_actions'] += 1
    counts[f'q{q}_P{P}'] += 1

def enumerate_small_arrays():
    report = collections.Counter()
    report['cycle_orbits_by_q_stabilizer'] = collections.Counter()
    first_example = None
    for n in (3, 4, 5):
        rows = list(itertools.permutations(range(n)))
        records = [(r, mask(pairs(r, 1)), mask(pairs(r, 2))) for r in rows]
        groups = {q: semiregular_perms(n + 1, q) for q in (2, 3) if (n + 1) % q == 0}
        def visit(start, selected, used1, used2):
            nonlocal first_example
            if len(selected) == n:
                cycles, b, w, f, delta = matrix_checks(selected)
                report[f'n{n}_arrays'] += 1
                report[f'n{n}_F{f}'] += 1
                if first_example is None:
                    first_example = tuple(selected)
                for q, perms in groups.items():
                    cset = set(cycles)
                    for g in perms:
                        if {canonical([g[x] for x in c], n) for c in cycles} == cset:
                            symmetry_checks(cycles, b, w, f, delta, g, q, report)
                return
            for j in range(start, len(records)):
                row, a, b = records[j]
                if not (a & used1 or b & used2):
                    visit(j + 1, selected + [row], used1 | a, used2 | b)
        visit(0, [], 0, 0)
    assert first_example is not None, 'no genuine small-array positives found'
    bad = list(first_example)
    bad[-1] = bad[0]
    try:
        matrix_checks(bad)
    except AssertionError as exc:
        assert str(exc) == 'duplicate distance-one event'
        report['negative_duplicate_row'] = 'rejected: duplicate distance-one event'
    else:
        raise AssertionError('duplicate-row negative accepted')
    return report

def synthetic_defect_controls():
    report = {}
    cells = [(x, y) for x in range(12) for y in range(12) if x != y]
    zero_margin_one = 0
    for p in cells:
        for d in cells:
            if p != d and p[0] == d[0] and p[1] == d[1]:
                zero_margin_one += 1
    assert zero_margin_one == 0
    report['single_surplus_deficit_ordered_pairs'] = len(cells) * (len(cells) - 1)
    report['single_surplus_deficit_balanced'] = zero_margin_one
    w = [[0] * 12 for _ in range(12)]
    for x, y, v in ((0, 2, 1), (1, 3, 1), (0, 3, -1), (1, 2, -1)):
        w[x][y] = v
    assert all(sum(row) == 0 for row in w)
    assert all(sum(w[x][y] for x in range(12)) == 0 for y in range(12))
    assert sum(max(v, 0) for row in w for v in row) == 2
    w[0][2] += 1
    assert sum(w[0]) == 1 and sum(w[x][2] for x in range(12)) == 1
    report['negative_broken_rectangle'] = 'rejected: nonzero source and target margins'
    C = {(x, (x + 1) % 11) for x in range(11)}
    dist = collections.Counter()
    for old in C:
        for new in cells:
            if 11 in new or new in C:
                continue
            M = C - {old} | {new}
            out = collections.Counter(x for x, _ in M)
            inc = collections.Counter(y for _, y in M)
            zp = sum(out[x] == 0 for x in range(11))
            zs = sum(inc[x] == 0 for x in range(11))
            assert zp == (old[0] != new[0]) and zs == (old[1] != new[1])
            dist[1 + zp + zs] += 1
    assert set(dist) == {2, 3}
    report['delta_one_pure_set_controls_F'] = dict(dist)
    return report

def layer_controls():
    report = {}
    for q, r in ((2, 6), (3, 4)):
        types = [(a, b, d) for a in range(r) for b in range(r) for d in range(q)
                 if a != b or d != 0]
        layer_balanced = residue_balanced = 0
        for plus in types:
            for minus in types:
                if plus == minus:
                    continue
                if plus[:2] == minus[:2]:
                    layer_balanced += 1
                    if (plus[2] - minus[2]) % q == 0:
                        residue_balanced += 1
        assert layer_balanced > 0 and residue_balanced == 0
        report[f'q{q}_P1_layer_balanced'] = layer_balanced
        report[f'q{q}_P1_with_jump_also'] = residue_balanced
    types = [(a, b, d) for a in range(4) for b in range(4) for d in range(3)
             if a != b or d != 0]
    cases = collections.Counter()
    for A, B, dplus, eplus in itertools.product(range(1, 4), range(1, 4), range(3), range(3)):
        positive = ((0, A, dplus), (B, 0, eplus))
        for neg in itertools.combinations((t for t in types if t not in positive), 2):
            if sorted(t[0] for t in neg) != sorted(t[0] for t in positive):
                continue
            if sorted(t[1] for t in neg) != sorted(t[1] for t in positive):
                continue
            if (sum(t[2] for t in positive) - sum(t[2] for t in neg)) % 3:
                continue
            pairset = {(t[0], t[1]) for t in neg}
            if pairset == {(0, A), (B, 0)}:
                kind = 'crossing'
            else:
                assert pairset == {(0, 0), (B, A)}
                kind = 'switched'
            # Vertices (layer,phase), with (0,0) representing infinity.
            mat = [[0] * 12 for _ in range(12)]
            for value, entries in ((1, positive), (-1, neg)):
                for a, b, d in entries:
                    for t in range(3):
                        x, y = 3 * a + t, 3 * b + (t + d) % 3
                        assert x != y and mat[x][y] == 0
                        mat[x][y] = value
            assert all(sum(row) == 0 for row in mat)
            assert all(sum(mat[x][y] for x in range(12)) == 0 for y in range(12))
            assert sum(max(v, 0) for row in mat for v in row) == 6
            assert sum(mat[x][y] == 1 for x in range(1, 12) for y in range(1, 12)) == 4
            zp = [x for x in range(1, 12) if mat[x][0] == -1]
            zs = [x for x in range(1, 12) if mat[0][x] == -1]
            dp = [x for x in range(1, 12) if mat[x][0] == 1]
            ds = [x for x in range(1, 12) if mat[0][x] == 1]
            assert len(zp) == len(zs) == len(dp) == len(ds) == 1
            assert dp[0] // 3 != 0 and ds[0] // 3 != 0
            if kind == 'crossing':
                assert zp[0] // 3 == dp[0] // 3 and zs[0] // 3 == ds[0] // 3
                assert zp[0] // 3 != 0 and zs[0] // 3 != 0
            else:
                assert zp[0] in (1, 2) and zs[0] in (1, 2) and zp[0] != zs[0]
            cases[kind] += 1
    assert set(cases) == {'crossing', 'switched'}
    report['six_defect_type_patterns'] = dict(cases)
    # Direct negatives: balance alone is not enough; residue alone is not enough.
    plus = (0, 1, 0)
    bad_jump = (0, 1, 1)
    assert plus[:2] == bad_jump[:2] and (plus[2] - bad_jump[2]) % 3 != 0
    bad_source = (2, 1, 0)
    assert plus[2] == bad_source[2] and plus[0] != bad_source[0] and plus[1] == bad_source[1]
    report['negative_same_layer_P1'] = 'rejected: nonzero jump residue'
    report['negative_equal_jump_P1'] = 'rejected: nonzero source-layer balance'
    return report

def main():
    start = clock()
    source_sha = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()
    signal.signal(signal.SIGALRM, timed_out)
    signal.alarm(90)
    out = {'started_native': start, 'source_sha256': source_sha, 'cap_seconds': 90,
           'scope': 'independent exact controls only; no claimed 12-vertex Hamiltonian witness'}
    rc = 0
    try:
        out['small_actual_arrays'] = enumerate_small_arrays()
        out['synthetic_cell_margins'] = synthetic_defect_controls()
        out['synthetic_type_layers'] = layer_controls()
        out['status'] = 'PASS'
    except TimeoutError as exc:
        out['status'] = 'UNKNOWN_TIMEOUT'
        out['error'] = str(exc)
        rc = 124
    except Exception:
        out['status'] = 'FAIL'
        out['error'] = traceback.format_exc()
        rc = 1
    finally:
        signal.alarm(0)
        out['ended_native'] = clock()
        out['program_exit_intended'] = rc
        text = json.dumps(out, indent=2, sort_keys=True) + '\n'
        with open(RESULT, 'x', encoding='utf-8') as f:
            f.write(text)
        print(text, end='')
    return rc

if __name__ == '__main__':
    sys.exit(main())
