#!/usr/bin/env python3
"""Independent small-case fixtures and log checks for cycle3_pair_c21v3 (CFR21 lane, worker C21CycleDlxPrep).

Written from the model definition only: no DLX, no option masks, no port of the C canonical test or of
cycle3_affine_checks_c21v2.py. Pure Python standard library, no subprocesses, no network. Its author did
NOT execute it (preparation-worker rule); the integration owner runs it after building the C program.

Model. n, mu with mu^3 = 1 (mod n). For a permutation h of Z_n with h(h(h(t))) = t and g: Z_n -> Z_n,
    R0 = 0, R1 = t, R2 = mu*h(h(t)), R3 = mu^2*h(t), R4 = g(t), R5 = mu*g(h(h(t))), R6 = mu^2*g(h(t)).
H(n, mu, mode): such h with h(0) = 0 (fixed) or with no fixed point (free) for which R0..R3 is a
    difference matrix (each of the 6 row pairs has n distinct differences mod n).
Classes: the conjugates x -> u*(h(u^-1*x + a) - a) (u a unit, a any shift) of h that lie in H, i.e.
    AGL(1,n) conjugacy orbits intersected with H. Canonical h: the least array h(0..n-1) of its class.
G(h): every g with g(0) = 0 for which R0..R6 is a difference matrix (all 21 pairs checked directly).
fnv(h): sum over G(h) of FNV-1a-64 over the bytes g(0), ..., g(n-1), modulo 2^64.
A complete gcount run of the C program prints one line 'c hg INDEX count C fnv F h h(0) .. h(n-1)' per
canonical h, which must give C = |G(h)| and F = fnv(h). Equal counts and equal order-free FNV sums identify
the two g sets up to 64-bit collisions; the C program also re-checks every counted g on all 21 pairs.

Two methods per level where feasible; they must agree:
  H: n <= 9 brute force over itertools.permutations of Z_n; every n: orbit-by-orbit recursion pruned only
     by a repeated R1-R2 difference t - mu*h(h(t)), every leaf fully checked. Also at n <= 9: for every
     order-3 h with the mode condition, 'R0..R3 is a DM' must equal 't - mu*h(h(t)) is bijective'.
  Classes: complete conjugation orbits. Every conjugate with h(a) = a (fixed mode) or any a (free) must
     stay in H, and in fixed mode every conjugate with h(a) != a must leave H (the C test assumes both).
  G: n <= 9 every permutation g with g(0) = 0 (g = R4 - R0 must be bijective); every n: pointwise
     backtracking pruned only by a repeated difference in a row pair whose two entries are known, every
     leaf fully checked. At n <= 9 both must agree, and for every such permutation g the five-map
     criterion (g, g - t, g - mu*h^2, g - mu^2*h, g - mu*g(h^2) bijective) must equal the 21-pair test.

Cases: n7 mu1,2,4 and n9 mu1,4,7, modes fixed and free; --n13 adds n13 mu1,3,9 (runtime unmeasured).
Logs of other cases with n <= 13 are computed on demand. From the definitions alone: free mode needs
3 | n, and Z_9 has no 4-row DM, so every free case here and every n9 case is empty. Fixed-point-free h
first exist at n21, so these fixtures exercise the C G matrix in fixed mode only; free mode is covered
here only by emptiness and, at n21, by comparing v2/v3 outcomes per canonical index.

Log checks (--log FILE, repeatable; stdout of cycle3_pair_c21v3, case read from its first line
'c cycle3_pair_c21v3 n N mu MU MODE RUN limit L skip S'). Every log must have completed (no s UNKNOWN,
no INTERNAL or G capacity line), and its final key/value line must satisfy range_start = S,
range_end = resume = S + hcompleted, last_completed = range_end - 1 (or -1), skipped = min(S, hcanonical).
  hcount: s HCOUNT, hcount = |H|, hcanonical = number of classes, no g search.
  gcount: s GCOUNT, hg indices exactly S, S+1, ..., hcanonical - 1 in order, each h canonical with the
     independent count and fnv (S = 0: all canonical h), gtotal = sum of counts.
  first:  S = 0: s SATISFIABLE iff some canonical h has g, else s EXHAUSTED-RESTRICTED. A solution needs a
     canonical v h, a v g with g(0) = 0 passing the 21-pair test, solution_index = range_end = current,
     and OUTPREFIX.dmraw (path from 'c wrote') equal to the rebuilt rows. S > 0: s SATISFIABLE, or
     s EXHAUSTED-RESTRICTED-SUFFIX with hcompleted = hcanonical - S.
  Across logs of one case: equal canonical index => equal hg line (SKIP determinism); a first-mode
     solution at index I must match gcount line I (count > 0) and every gcount index in [S, I) must have
     count 0; an exhausted first run with SKIP S needs count 0 at every gcount index >= S.

Usage: cycle3_dlx_checks_c21v3.py [--n13] [--log FILE ...] [--out-json NEW.json]
Prints the fixtures, then 'CYCLE3 DLX CHECKS PASS' (exit 0) only if every check passes, otherwise the
failures and 'CYCLE3 DLX CHECKS FAIL' (exit 1). --out-json is created exclusively (mode 'x').

Suggested calibration (integration owner; BIN = built cycle3_pair_c21v3, OUT = a new calib directory):
  for (N, MU) in (7,1) (7,2) (7,4) (9,1) (9,4) (9,7) (13,1) (13,3) (13,9), MODE in fixed free:
      BIN N MU MODE 240 hcount OUT/hcount-N-MU-MODE
      BIN N MU MODE 240 gcount OUT/gcount-N-MU-MODE
      BIN N MU MODE 240 first  OUT/first-N-MU-MODE
  SKIP controls: BIN 13 3 fixed 240 gcount OUT/gcount-skip2-13-3 2   (lines from index 2, identical)
                 BIN 13 3 fixed 240 first  OUT/first-skip1-13-3 1    (a solution at index >= 1, or exit21)
                 BIN 13 3 fixed 240 first  OUT/first-skip99-13-3 99  (exit21 and 'c note SKIP ...')
  cycle3_dlx_checks_c21v3.py --n13 --log OUT/<job>.out ... --out-json OUT/dlx-checks-v3.json
"""
import argparse
import hashlib
import itertools
import json
import re
import sys
from math import gcd
from pathlib import Path

FNV_OFFSET = 0xCBF29CE484222325
FNV_PRIME = 0x100000001B3
MASK64 = (1 << 64) - 1
DEFAULT_CASES = [(7, 1), (7, 2), (7, 4), (9, 1), (9, 4), (9, 7)]
N13_CASES = [(13, 1), (13, 3), (13, 9)]
MODES = ('fixed', 'free')
BRUTE_MAX_N = 9  # itertools brute force for H and G up to this n
MAX_N = 13       # largest n for which expectations are computed
HEADER_RE = re.compile(r'c cycle3_pair_c21v3 n (\d+) mu (\d+) (fixed|free) (first|hcount|gcount) limit \S+ skip (\d+)$')
HG_RE = re.compile(r'c hg (\d+) count (\d+) fnv ([0-9a-f]{16}) h((?: \d+)+)$')
VEC_RE = re.compile(r'v ([hg])((?: \d+)+)$')
SOLUTION_RE = re.compile(r'c solution canonical_index (\d+)$')
WROTE_RE = re.compile(r'c wrote (.+)$')
FINAL_KEYS = ('hcount', 'hcanonical', 'skip', 'skipped', 'hcompleted', 'range_start', 'range_end',
              'last_completed', 'resume', 'current', 'solution_index', 'gtotal', 'timed_out', 'overflow')
COMPLETE = ('HCOUNT', 'GCOUNT', 'EXHAUSTED-RESTRICTED', 'EXHAUSTED-RESTRICTED-SUFFIX')


def fnv1a64(values):
    """FNV-1a, 64 bit, over a sequence of byte values."""
    x = FNV_OFFSET
    for v in values:
        x ^= v
        x = (x * FNV_PRIME) & MASK64
    return x


def rows_of(n, mu, h, g=None):
    """R0..R3, plus R4..R6 when g is given, as lists indexed by the column t."""
    mu2 = mu * mu % n
    rows = [[0] * n, list(range(n)), [mu * h[h[t]] % n for t in range(n)], [mu2 * h[t] % n for t in range(n)]]
    if g is not None:
        rows += [[g[t] % n for t in range(n)], [mu * g[h[h[t]]] % n for t in range(n)],
                 [mu2 * g[h[t]] % n for t in range(n)]]
    return rows


def is_dm(rows, n):
    """Difference matrix: every pair of rows has n distinct differences mod n."""
    return all(len({(x - y) % n for x, y in zip(rows[i], rows[j])}) == n
               for i in range(len(rows)) for j in range(i))


def mode_ok(h, mode):
    if mode == 'fixed':
        return h[0] == 0
    return all(h[t] != t for t in range(len(h)))


def five_maps_ok(n, mu, h, g):
    """The C program's reduction: g, g - t, g - mu*h^2, g - mu^2*h, g - mu*g(h^2) all bijective."""
    mu2 = mu * mu % n
    maps = ([g[t] % n for t in range(n)],
            [(g[t] - t) % n for t in range(n)],
            [(g[t] - mu * h[h[t]]) % n for t in range(n)],
            [(g[t] - mu2 * h[t]) % n for t in range(n)],
            [(g[t] - mu * g[h[h[t]]]) % n for t in range(n)])
    return all(len(set(m)) == n for m in maps)


def order3_perms(n):
    return [p for p in itertools.permutations(range(n)) if all(p[p[p[t]]] == t for t in range(n))]


def h_brute(n, mu, mode, order3, fails):
    out = []
    for h in order3:
        if not mode_ok(h, mode):
            continue
        dm = is_dm(rows_of(n, mu, h), n)
        if dm != (len({(t - mu * h[h[t]]) % n for t in range(n)}) == n):
            fails.append(f'n{n} mu{mu} {mode}: 4-row DM test and d-criterion disagree for h={h}')
        if dm:
            out.append(h)
    return sorted(out)


def h_recursive(n, mu, mode):
    """Orbit by orbit from the least unassigned point; prunes only on a repeated R1-R2 difference."""
    if mode == 'free' and n % 3:
        return []  # a fixed-point-free permutation of order 3 needs 3 | n
    h = [-1] * n
    used = set()
    out = []

    def rec():
        todo = [t for t in range(n) if h[t] < 0]
        if not todo:
            if mode_ok(h, mode) and is_dm(rows_of(n, mu, h), n):
                out.append(tuple(h))
            return
        p, rest = todo[0], todo[1:]
        if mode == 'fixed':
            d = (p - mu * p) % n
            if d not in used:
                h[p] = p
                used.add(d)
                rec()
                used.discard(d)
                h[p] = -1
            if p == 0:
                return  # fixed mode: h(0) = 0
        for q in rest:
            for r in rest:
                if q == r:
                    continue
                # h: p -> q -> r -> p, so h(h(p)) = r, h(h(q)) = p, h(h(r)) = q
                ds = {(p - mu * r) % n, (q - mu * p) % n, (r - mu * q) % n}
                if len(ds) < 3 or ds & used:
                    continue
                h[p], h[q], h[r] = q, r, p
                used.update(ds)
                rec()
                used.difference_update(ds)
                h[p] = h[q] = h[r] = -1

    rec()
    return sorted(out)


def units(n):
    return [u for u in range(1, n) if gcd(u, n) == 1]


def conjugate(h, u, a, n):
    """x -> u*(h(u^-1*x + a) - a): h after relabelling every column t as u*(t - a)."""
    ui = pow(u, -1, n)
    return tuple(u * (h[(ui * x + a) % n] - a) % n for x in range(n))


def class_reps(n, hs, mode, fails, tag):
    """Least member of each class (AGL(1,n) conjugates inside H), plus the closure facts the C test uses."""
    hset = set(hs)
    us = units(n)
    done = set()
    reps = []
    for h in hs:  # ascending: the first unseen member of a class is its least member
        cls = set()
        for u in us:
            for a in range(n):
                c = conjugate(h, u, a, n)
                inside = c in hset
                if mode == 'free' or h[a] == a:
                    if not inside:
                        fails.append(f'{tag}: eligible conjugate leaves H: h={h} u={u} a={a}')
                elif inside:
                    fails.append(f'{tag}: ineligible conjugate stays in H: h={h} u={u} a={a}')
                if inside:
                    cls.add(c)
        if h in done:
            continue
        if min(cls) != h:
            fails.append(f'{tag}: class of h={h} has an earlier least member {min(cls)}')
        done |= cls
        reps.append(h)
    return reps


def g_brute(n, mu, h, fails, tag):
    """Every permutation g with g(0) = 0 (g = R4 - R0 must be bijective), tested on all 21 pairs."""
    out = []
    for p in itertools.permutations(range(1, n)):
        g = (0,) + p
        dm = is_dm(rows_of(n, mu, h, g), n)
        if dm != five_maps_ok(n, mu, h, g):
            fails.append(f'{tag}: five-map criterion and 21-pair test disagree for h={h} g={g}')
        if dm:
            out.append(g)
    return out


def g_backtrack(n, mu, h, fails, tag):
    """Every g with g(0) = 0, assigned point by point, orbit after orbit; prunes only on a repeated difference
    of a row pair (i, j), i >= 4, whose two entries are known; every leaf is fully re-checked."""
    mu2 = mu * mu % n
    top = rows_of(n, mu, h)
    orbits, seen = [], set()
    for t in range(n):
        if t not in seen:
            orbit = [t] if h[t] == t else [t, h[t], h[h[t]]]
            seen.update(orbit)
            orbits.append(orbit)
    points = [s for orbit in orbits for s in orbit]
    closing = {orbit[-1]: orbit for orbit in orbits}
    g = [-1] * n
    used = {(i, j): set() for i in range(4, 7) for j in range(i)}
    out = []

    def column(s):
        return (top[0][s], top[1][s], top[2][s], top[3][s], g[s], mu * g[h[h[s]]] % n, mu2 * g[h[s]] % n)

    def rec(k):
        if k == len(points):
            if is_dm(rows_of(n, mu, h, g), n):
                out.append(tuple(g))
            else:
                fails.append(f'{tag}: backtracking leaf fails the 21-pair test, h={h} g={g}')
            return
        s = points[k]
        for v in ([0] if s == 0 else range(n)):
            added = []
            ok = True
            for j in range(4):  # R4(s) = v is known now
                d = (v - top[j][s]) % n
                if d in used[(4, j)]:
                    ok = False
                    break
                used[(4, j)].add(d)
                added.append((4, j, d))
            if ok:
                g[s] = v
                if s in closing:  # the whole orbit of s is assigned, so R5 and R6 are known on it
                    for c in closing[s]:
                        col = column(c)
                        for i in (5, 6):
                            for j in range(i):
                                d = (col[i] - col[j]) % n
                                if d in used[(i, j)]:
                                    ok = False
                                    break
                                used[(i, j)].add(d)
                                added.append((i, j, d))
                            if not ok:
                                break
                        if not ok:
                            break
                if ok:
                    rec(k + 1)
                g[s] = -1
            for i, j, d in added:
                used[(i, j)].discard(d)

    rec(0)
    return out


def expectations(n, mu, mode, cache, order3_cache, fails):
    key = (n, mu, mode)
    if key in cache:
        return cache[key]
    tag = f'n{n} mu{mu} {mode}'
    if not (3 <= n <= MAX_N and 1 <= mu < n and pow(mu, 3, n) == 1):
        raise ValueError(f'unsupported case {tag}: need 3 <= n <= {MAX_N}, 1 <= mu < n, mu^3 = 1 mod n')
    hs = h_recursive(n, mu, mode)
    if n <= BRUTE_MAX_N:
        if n not in order3_cache:
            order3_cache[n] = order3_perms(n)
        hb = h_brute(n, mu, mode, order3_cache[n], fails)
        if hb != hs:
            fails.append(f'{tag}: brute-force H ({len(hb)}) != recursive H ({len(hs)})')
    canonical = []
    for h in class_reps(n, hs, mode, fails, tag):
        gs = sorted(g_backtrack(n, mu, h, fails, tag))
        if n <= BRUTE_MAX_N and g_brute(n, mu, h, fails, tag) != gs:
            fails.append(f'{tag}: brute-force G != backtracking G for h={h}')
        canonical.append({'h': list(h), 'gcount': len(gs),
                          'fnv': '%016x' % (sum(fnv1a64(g) for g in gs) & MASK64),
                          'least_g': list(gs[0]) if gs else None})
    result = {'n': n, 'mu': mu, 'mode': mode, 'hcount': len(hs), 'hcanonical': len(canonical),
              'gtotal': sum(c['gcount'] for c in canonical), 'canonical': canonical}
    cache[key] = result
    return result


def parse_final(line):
    tok = line.split()[3:]  # after 'c final <seconds>'
    if len(tok) % 2:
        raise ValueError('odd number of key/value tokens')
    return {k: int(v) for k, v in zip(tok[0::2], tok[1::2])}


def check_solution(lines, n, mu, fin, canon, expect, rec):
    vec = {}
    for line in lines:
        mm = VEC_RE.match(line)
        if mm:
            vec[mm[1]] = tuple(int(x) for x in mm[2].split())
    h, g = vec.get('h'), vec.get('g')
    if h is None or g is None or len(h) != n or len(g) != n:
        expect(False, 'missing or malformed v h / v g lines')
        return
    if h not in canon:
        expect(False, f'solution h={h} is not an independent canonical h')
        return
    good = g[0] == 0 and all(0 <= x < n for x in g) and is_dm(rows_of(n, mu, h, g), n)
    expect(good, f'solution g={g} fails g(0) = 0 or the independent 21-pair test')
    sol = [int(mm[1]) for mm in map(SOLUTION_RE.match, lines) if mm]
    expect(sol == [fin['solution_index']] and fin['solution_index'] == fin['range_end'] == fin['current'],
           'solution canonical_index / solution_index / range_end / current disagree')
    wrote = [mm[1] for mm in map(WROTE_RE.match, lines) if mm]
    expect(len(wrote) == 1, 'expected exactly one c wrote line')
    if len(wrote) == 1 and good:
        try:
            raw = [[int(x) for x in line.split()] for line in Path(wrote[0]).read_text().splitlines() if line.strip()]
        except (OSError, ValueError) as e:
            expect(False, f'cannot read {wrote[0]}: {e}')
        else:
            expect(raw == rows_of(n, mu, h, g), f'{wrote[0]} differs from the rows rebuilt from v h / v g')
    rec['solution'] = {'index': fin['solution_index'], 'h': list(h), 'g': list(g)}


def check_log(path, cache, order3_cache, fails):
    path = Path(path)
    data = path.read_bytes()
    rec = {'log': str(path), 'sha256': hashlib.sha256(data).hexdigest(), 'ok': False}
    lines = data.decode('utf-8', 'replace').splitlines()
    m = HEADER_RE.match(lines[0]) if lines else None
    if not m:
        fails.append(f'{path}: first line is not a cycle3_pair_c21v3 header')
        return rec
    n, mu, mode, run, skip = int(m[1]), int(m[2]), m[3], m[4], int(m[5])
    rec.update(n=n, mu=mu, mode=mode, run=run, skip=skip)
    tag = f'{path} [n{n} mu{mu} {mode} {run} skip {skip}]'
    before = len(fails)

    def expect(cond, what):
        if not cond:
            fails.append(f'{tag}: {what}')

    try:
        exp = expectations(n, mu, mode, cache, order3_cache, fails)
    except ValueError as e:
        fails.append(f'{tag}: {e}')
        return rec
    for line in lines:
        expect(not line.startswith(('c INTERNAL', 'c G capacity')), line)
    status = [line for line in lines if line.startswith('s ')]
    finals = [line for line in lines if line.startswith('c final ')]
    if len(status) != 1 or len(finals) != 1:
        fails.append(f'{tag}: need one status and one final line, got {len(status)} and {len(finals)}')
        return rec
    words = status[0].split()
    word = words[1] if len(words) > 1 else ''
    try:
        fin = parse_final(finals[0])
    except ValueError as e:
        fails.append(f'{tag}: unparsable final line ({e})')
        return rec
    missing = [k for k in FINAL_KEYS if k not in fin]
    if missing:
        fails.append(f'{tag}: final line lacks {missing}')
        return rec
    rec.update(status=status[0], final=fin)
    canon = {tuple(c['h']): c for c in exp['canonical']}
    positives = [h for h, c in canon.items() if c['gcount'] > 0]
    searched = max(0, exp['hcanonical'] - skip)

    expect(word != 'UNKNOWN', 's UNKNOWN: calibration logs must run to completion')
    expect(fin['skip'] == skip == fin['range_start'], 'final skip/range_start differ from the header SKIP')
    expect(fin['range_end'] == skip + fin['hcompleted'] == fin['resume'], 'range_end/resume != SKIP + hcompleted')
    expect(fin['last_completed'] == (fin['range_end'] - 1 if fin['hcompleted'] else -1), 'last_completed inconsistent')
    expect(fin['skipped'] == min(skip, fin['hcanonical']), 'skipped != min(SKIP, hcanonical)')
    if word in COMPLETE:
        expect(fin['hcount'] == exp['hcount'], f'hcount {fin["hcount"]} != independent {exp["hcount"]}')
        expect(fin['hcanonical'] == exp['hcanonical'],
               f'hcanonical {fin["hcanonical"]} != independent {exp["hcanonical"]}')
        expect(fin['timed_out'] == 0 and fin['overflow'] == 0, 'complete status with timed_out/overflow set')
        expect(fin['current'] == (fin['range_end'] - 1 if fin['hcompleted'] else -1),
               'current inconsistent with a complete run')
    hg, order = {}, []
    for line in lines:
        mm = HG_RE.match(line)
        if not mm:
            continue
        idx, cnt, fnv = int(mm[1]), int(mm[2]), mm[3]
        h = tuple(int(x) for x in mm[4].split())
        order.append(idx)
        hg[idx] = (h, cnt, fnv)
        c = canon.get(h)
        if c is None:
            fails.append(f'{tag}: hg {idx} h={h} is not an independent canonical h')
        else:
            expect(cnt == c['gcount'] and fnv == c['fnv'],
                   f'hg {idx} h={h}: count/fnv {cnt}/{fnv} != independent {c["gcount"]}/{c["fnv"]}')
    rec['hg'] = {str(i): [list(v[0]), v[1], v[2]] for i, v in sorted(hg.items())}
    if run == 'hcount':
        expect(word == 'HCOUNT', f'status {word} for an hcount run')
        expect(not order and fin['hcompleted'] == 0 and fin['gtotal'] == 0, 'hcount run searched g')
    elif run == 'gcount':
        expect(word == 'GCOUNT', f'status {word} for a gcount run')
        expect(order == list(range(skip, skip + len(order))), 'hg indices are not SKIP, SKIP+1, ... in order')
        expect(len(order) == fin['hcompleted'] == searched,
               f'hg lines {len(order)}, hcompleted {fin["hcompleted"]}, independent hcanonical-SKIP {searched}')
        expect(len({v[0] for v in hg.values()}) == len(hg), 'an h occurs in two hg lines')
        expect(fin['gtotal'] == sum(v[1] for v in hg.values()), 'gtotal != sum of hg counts')
        if skip == 0:
            expect({v[0] for v in hg.values()} == set(canon), 'hg h set != independent canonical set')
    else:
        expect(not order, 'first mode printed hg lines')
        if word == 'SATISFIABLE':
            check_solution(lines, n, mu, fin, canon, expect, rec)
            if skip == 0:
                expect(bool(positives), 'SATISFIABLE, but no independent canonical h has any g')
        elif word == 'EXHAUSTED-RESTRICTED':
            expect(skip == 0, 'EXHAUSTED-RESTRICTED with SKIP > 0')
            expect(not positives, f'exhausted, but {len(positives)} independent canonical h have g')
            expect(fin['hcompleted'] == exp['hcanonical'], 'hcompleted != hcanonical')
        elif word == 'EXHAUSTED-RESTRICTED-SUFFIX':
            expect(skip > 0, 'suffix status with SKIP = 0')
            expect(fin['hcompleted'] == searched, 'hcompleted != hcanonical - SKIP')
            expect(len(positives) <= exp['hcanonical'] - searched, 'more canonical h with g than skipped indices')
        else:
            expect(False, f'unexpected status {word} for a first run')
    rec['ok'] = len(fails) == before
    return rec


def cross_check(records, fails):
    """SKIP determinism and first/gcount consistency between logs of the same case."""
    cases = {}
    for r in records:
        if 'final' in r:
            cases.setdefault((r['n'], r['mu'], r['mode']), []).append(r)
    for (n, mu, mode), rs in sorted(cases.items()):
        tag = f'cross n{n} mu{mu} {mode}'
        union = {}
        for r in rs:
            if r['run'] != 'gcount':
                continue
            for k, v in r.get('hg', {}).items():
                i, line = int(k), (tuple(v[0]), v[1], v[2])
                if union.setdefault(i, line) != line:
                    fails.append(f'{tag}: canonical index {i} differs between gcount logs ({r["log"]})')
        for r in rs:
            if r['run'] != 'first':
                continue
            word, skip = (r['status'].split() + [''])[1], r['skip']
            if word == 'SATISFIABLE' and 'solution' in r:
                i = r['solution']['index']
                if i in union and (union[i][0] != tuple(r['solution']['h']) or union[i][1] == 0):
                    fails.append(f'{tag}: {r["log"]} solution at index {i} disagrees with gcount line {i}')
                bad = sorted(j for j, v in union.items() if skip <= j < i and v[1])
                if bad:
                    fails.append(f'{tag}: {r["log"]} found index {i} from SKIP {skip}, but gcount has g at {bad}')
            elif word.startswith('EXHAUSTED'):
                bad = sorted(j for j, v in union.items() if j >= skip and v[1])
                if bad:
                    fails.append(f'{tag}: {r["log"]} exhausted from SKIP {skip}, but gcount has g at {bad}')


def main():
    ap = argparse.ArgumentParser(description='Independent fixtures and log checks for cycle3_pair_c21v3.')
    ap.add_argument('--n13', action='store_true', help='also compute n13 mu1,3,9 (runtime unmeasured)')
    ap.add_argument('--log', action='append', default=[], help='cycle3_pair_c21v3 stdout file (repeatable)')
    ap.add_argument('--out-json', help='new JSON report, created exclusively')
    args = ap.parse_args()
    fails, cache, order3_cache = [], {}, {}
    for n, mu in DEFAULT_CASES + (N13_CASES if args.n13 else []):
        for mode in MODES:
            e = expectations(n, mu, mode, cache, order3_cache, fails)
            print(f'case n{n} mu{mu} {mode}: hcount {e["hcount"]} hcanonical {e["hcanonical"]} gtotal {e["gtotal"]}')
            for c in e['canonical']:
                print(f'  canonical h {" ".join(map(str, c["h"]))} gcount {c["gcount"]} fnv {c["fnv"]}')
    records = [check_log(p, cache, order3_cache, fails) for p in args.log]
    cross_check(records, fails)
    ok = not fails
    if args.out_json:
        report = {'script': str(Path(__file__).resolve()),
                  'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'python': sys.version, 'cases': [cache[k] for k in sorted(cache)], 'logs': records,
                  'failure_count': len(fails), 'failures': fails[:200], 'pass': ok}
        with open(args.out_json, 'x') as f:
            json.dump(report, f, indent=1)
    for x in fails[:200]:
        print('FAIL', x)
    print('CYCLE3 DLX CHECKS PASS' if ok else 'CYCLE3 DLX CHECKS FAIL')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
