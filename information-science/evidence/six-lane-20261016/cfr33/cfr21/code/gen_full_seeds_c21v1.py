#!/usr/bin/env python3
"""f_1 lists for the full-permutation engine cfr_perm_search_c21v1 (sub-lane cfr21, worker InfoCFR27Lift.C21FullPermPrep).
Pure Python: no native program, no model call, no search.

Usage: gen_full_seeds_c21v1.py OUTDIR
OUTDIR is created with os.mkdir and must not exist; every file in it is created with mode 'x'. Map files hold one map per
line, the values f(1) .. f(N-1) separated by single spaces (f(0) = 0): the f1file format of cfr_perm_search_c21v1.
summary.json (written last) holds source hashes, counts and file hashes; p21-detail.json holds the replay data.

1. P21 inventory, N = 21. calib/xc-v1/runs-v1/P21-zero-count.out is dmorbit_xc_c21v1 on calib/xc-v1/P21.model in mode
   zero count (checked against its runs-v1/records.jsonl line: command, exit code 0, out_sha256), with 96 "sol" lines
   and "s COUNT 96 COMPLETE". P21.model (n 21, k 6) must list exactly the closure of the P21.spec.json generator
   (mu 1, pi = [0,2,3,4,5,1], row 0 fixed), and its SPEC_SHA256 line must be the sha256 of P21.spec.json. Each sol line
   gives the 4 base columns b (b[0] = 0 omitted) of one invariant (Z_21, 6; 1)-DM, expanded as dmorbit_xc_c21v1 emit():
   column 0 = zero column, then per base column (sol order) its distinct images under the model's G lines in file order,
   (g b)_x = mu b[pinv[x]] + t[x] renormalised to entry 0 = 0. All 15 row pairs of every 6 x 21 array are checked
   directly. For every ordered pair of distinct rows (p, q): rows E_i = D_i - D_p, columns indexed by s = E_q (checked
   bijective), every row translated to take 0 at index 0; the other 4 rows are normalised orthomorphisms (checked
   directly, and pairwise orthogonal). The inventory is the set of distinct maps among the 96 * 30 * 4 occurrences.
2. R1 reduction (facts-v4 R1: renormalisations of a normal form and unit conjugation; no oddness used):
   C_u f(x) = u f(u^-1 x) (u a unit), A f(x) = f(-x) + x (renormalisation (p, q) = (id, 0); equals id - f only for odd
   f), I f = f^-1 (renormalisation (p, q) = (0, f)). f is an f-row of some normalised DM iff every member of its R1-orbit
   is. Every inventory orbit is closed explicitly (every image checked directly); the lexicographically smallest member
   of each orbit is written, sorted, with a replay path (seed occurrence and generator word) in p21-detail.json.
   Scope: searching every representative exhaustively would exclude exactly the normalised (Z_21, 7; 1)-DMs that have
   at least one f-row in this finite R1-closed family. No P21 (or other) symmetry of a target DM is assumed or implied.
3. Calibration lists: all normalised orthomorphisms of Z_9 (all 8! orders of 1..8 as f(1..8), kept iff f - id is a
   permutation; expected 225); f(x) = 2x for N = 7 and N = 13; the position map (symbol s -> column c with row[c] = s) of
   the first non-identity row of ../controls/kirtchakov-cfr-5-25.raw (N = 25). Every map is checked directly: f(0) = 0,
   f and f - id permutations of Z_N.
"""
import hashlib
import itertools
import json
import os
import sys
from collections import Counter
from datetime import datetime
from math import gcd
from pathlib import Path
from zoneinfo import ZoneInfo

LANE = Path(__file__).resolve().parent.parent
SOURCES = {
    'P21-zero-count.out': LANE / 'calib' / 'xc-v1' / 'runs-v1' / 'P21-zero-count.out',
    'records.jsonl': LANE / 'calib' / 'xc-v1' / 'runs-v1' / 'records.jsonl',
    'P21.model': LANE / 'calib' / 'xc-v1' / 'P21.model',
    'P21.spec.json': LANE / 'calib' / 'xc-v1' / 'P21.spec.json',
    'kirtchakov-cfr-5-25.raw': LANE.parent / 'controls' / 'kirtchakov-cfr-5-25.raw',
    'program': Path(__file__).resolve(),
}
P21_GENS = [[1, [0, 2, 3, 4, 5, 1]]]
P21_SOLS = 96
Z9_EXPECTED = 225


def clock():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def is_perm(vals, n):
    return len(vals) == n and sorted(vals) == list(range(n))


def check_orthomorphism(f, n, what):
    """Direct check: f is the full array f(0..n-1) of a normalised orthomorphism of Z_n."""
    if not (len(f) == n and all(type(v) is int for v in f) and f[0] == 0 and is_perm(list(f), n)
            and is_perm([(f[x] - x) % n for x in range(n)], n)):
        raise SystemExit('INVALID %s: not a normalised orthomorphism of Z_%d: %s' % (what, n, list(f)))


def orthogonal(f, g, n):
    return is_perm([(f[x] - g[x]) % n for x in range(n)], n)


def apply_gen(name, f, n):
    """R1 generators on full arrays: 'A' f(x) -> f(-x) + x; 'I' f -> f^-1; 'C<u>' f(x) -> u f(u^-1 x)."""
    if name == 'A':
        return tuple((f[(-x) % n] + x) % n for x in range(n))
    if name == 'I':
        r = [None] * n
        for x in range(n):
            r[f[x]] = x
        return tuple(r)
    u = int(name[1:])
    ui = pow(u, -1, n)
    return tuple((u * f[(ui * x) % n]) % n for x in range(n))


def apply_word(f, word, n):
    for name in word:
        f = apply_gen(name, f, n)
    return f


def r1_orbit(seed, n, gen_names):
    """Explicit orbit of seed (breadth first); every new image is checked directly.
    Returns {member: (predecessor, generator) or None for the seed}."""
    parent = {seed: None}
    frontier = [seed]
    while frontier:
        new = []
        for f in frontier:
            for name in gen_names:
                g = apply_gen(name, f, n)
                if g not in parent:
                    check_orthomorphism(g, n, 'R1 image')
                    parent[g] = (f, name)
                    new.append(g)
        frontier = new
    return parent


def word_to(parent, target):
    word = []
    while parent[target] is not None:
        target, name = parent[target]
        word.append(name)
    return word[::-1]


def read_model(text):
    lines = text.split('\n')
    if lines[0] != 'DMORBIT-MODEL v2':
        raise SystemExit('unexpected model header %r' % lines[0])
    n, k = (int(x) for x in lines[1].split())
    tag, ng = lines[2].split()
    if tag != 'G':
        raise SystemExit('unexpected model line %r' % lines[2])
    G = []
    for ln in lines[3:3 + int(ng)]:
        v = [int(x) for x in ln.split()]
        if len(v) != 1 + 2 * k:
            raise SystemExit('bad G line %r' % ln)
        G.append((v[0], tuple(v[1:1 + k]), tuple(v[1 + k:])))
    shas = [ln.split()[1] for ln in lines if ln.startswith('SPEC_SHA256 ')]
    if len(G) != int(ng) or len(shas) != 1:
        raise SystemExit('model incomplete')
    return n, k, G, shas[0]


def spec_closure(spec):
    """Closure of the untwisted spec generators (mu, pi) under composition, as the set of (mu, pi^-1)."""
    n, k = spec['n'], spec['k']
    gens = []
    for g in spec['gens']:
        if len(g) > 2 and any(g[2]):
            raise SystemExit('twisted generator in the P21 spec')
        gens.append((g[0] % n, tuple(g[1])))
    elems = {(1, tuple(range(k)))}
    frontier = list(elems)
    while frontier:
        new = []
        for (m, p) in frontier:
            for (gm, gp) in gens:
                y = ((gm * m) % n, tuple(gp[p[i]] for i in range(k)))
                if y not in elems:
                    elems.add(y)
                    new.append(y)
        frontier = new
    out = set()
    for (m, p) in elems:
        pinv = [0] * k
        for i in range(k):
            pinv[p[i]] = i
        out.add((m, tuple(pinv)))
    return out


def expand(bases, G, n, k):
    """k x n array in dmorbit_xc_c21v1 emit() order: zero column, then each base column's distinct G-images."""
    cols = [[0] * k]
    for b in bases:
        orbit = []
        for (mu, pinv, t) in G:
            base = (mu * b[pinv[0]] + t[0]) % n
            im = [(mu * b[pinv[x]] + t[x] - base) % n for x in range(k)]
            if im not in orbit:
                orbit.append(im)
        cols.extend(orbit)
    if len(cols) != n:
        raise SystemExit('expansion gives %d columns, not %d' % (len(cols), n))
    return [[cols[c][x] for c in range(n)] for x in range(k)]


def check_dm(D, n, what):
    """Direct check of every row pair; returns the number of pairs checked."""
    pairs = 0
    for i in range(len(D)):
        for j in range(i + 1, len(D)):
            if not is_perm([(D[i][c] - D[j][c]) % n for c in range(n)], n):
                raise SystemExit('%s: rows %d,%d differences are not a permutation of Z_%d' % (what, i, j, n))
            pairs += 1
    return pairs


def normal_forms(D, n):
    """For every ordered pair p != q: (p, q, [(i, f_i) for the other rows]), f_i normalised as in the module doc."""
    k = len(D)
    out = []
    for p in range(k):
        for q in range(k):
            if p == q:
                continue
            E = [[(D[i][c] - D[p][c]) % n for c in range(n)] for i in range(k)]
            col = [None] * n
            for c in range(n):
                col[E[q][c]] = c
            if None in col:
                raise SystemExit('D_%d - D_%d is not a bijection' % (q, p))
            maps = []
            for i in range(k):
                if i in (p, q):
                    continue
                g = [E[i][col[s]] for s in range(n)]
                f = tuple((g[s] - g[0]) % n for s in range(n))
                check_orthomorphism(f, n, 'normal-form row (p %d q %d i %d)' % (p, q, i))
                maps.append((i, f))
            for x in range(len(maps)):
                for y in range(x + 1, len(maps)):
                    if not orthogonal(maps[x][1], maps[y][1], n):
                        raise SystemExit('normal form (p %d q %d): rows %d, %d not orthogonal'
                                         % (p, q, maps[x][0], maps[y][0]))
            out.append((p, q, maps))
    return out


def write_maps(outdir, name, maps):
    text = ''.join(' '.join(str(v) for v in f[1:]) + '\n' for f in maps)
    with open(outdir / name, 'x', encoding='ascii', newline='\n') as fh:
        fh.write(text)
    return {'file': name, 'lines': len(maps), 'values_per_line': len(maps[0]) - 1,
            'sha256': sha(text.encode('ascii'))}


def main():
    if len(sys.argv) != 2:
        raise SystemExit('usage: gen_full_seeds_c21v1.py OUTDIR')
    outdir = Path(sys.argv[1])
    try:
        os.mkdir(outdir)
    except FileExistsError:
        raise SystemExit('OUTDIR exists (must be new): %s' % outdir)
    start = clock()
    raw = {key: path.read_bytes() for key, path in SOURCES.items()}

    # ---- P21 model, spec and run record
    spec = json.loads(raw['P21.spec.json'])
    n, k, G, spec_sha_line = read_model(raw['P21.model'].decode('ascii'))
    if (n, k) != (21, 6) or (spec['n'], spec['k']) != (n, k) or spec['gens'] != P21_GENS:
        raise SystemExit('P21 spec/model are not n 21, k 6 with gens %s' % P21_GENS)
    if spec_sha_line != sha(raw['P21.spec.json']):
        raise SystemExit('P21.model SPEC_SHA256 is not the sha256 of P21.spec.json')
    model_elems = {(m % n, p) for (m, p, t) in G}
    if any(any(t) for (m, p, t) in G) or len(model_elems) != len(G) or model_elems != spec_closure(spec):
        raise SystemExit('P21.model G lines are not the closure of the P21.spec.json generator')
    rec = None
    for ln in raw['records.jsonl'].decode('utf-8').split('\n'):
        if ln.strip():
            r = json.loads(ln)
            if r.get('name') == 'P21-zero-count':
                rec = r
                break
    if (rec is None or Path(rec['cmd'][1]).resolve() != SOURCES['P21.model'].resolve()
            or rec['cmd'][3:5] != ['zero', 'count'] or rec.get('exit_code') != 0
            or rec.get('out_sha256') != sha(raw['P21-zero-count.out'])):
        raise SystemExit('records.jsonl does not attest P21-zero-count.out (P21.model, zero count, exit 0, out_sha256)')

    # ---- 96 solutions -> 6 x 21 arrays -> normal forms -> inventory
    lines = raw['P21-zero-count.out'].decode('ascii').split('\n')
    if not any(ln.startswith('c dmorbit_xc_c21v1 n 21 k 6 |G| %d ' % len(G)) and ' mode zero count ' in ln for ln in lines):
        raise SystemExit('P21-zero-count.out is not dmorbit_xc_c21v1 n 21 k 6 mode zero count')
    sols = []
    for ln in lines:
        if ln.startswith('sol'):
            parts = ln.split('|')
            if parts[0] != 'sol ' or len(parts) != 5:
                raise SystemExit('bad sol line %r' % ln)
            bases = [[0] + [int(x) for x in part.split()] for part in parts[1:]]
            if any(len(b) != k for b in bases):
                raise SystemExit('bad sol line %r' % ln)
            sols.append(bases)
    if len(sols) != P21_SOLS or ('s COUNT %d COMPLETE' % P21_SOLS) not in lines:
        raise SystemExit('expected %d sol lines and "s COUNT %d COMPLETE"' % (P21_SOLS, P21_SOLS))
    dms, inventory, inv = [], {}, []
    pairs_checked = n_forms = n_occ = 0
    for si, bases in enumerate(sols, 1):
        D = expand(bases, G, n, k)
        pairs_checked += check_dm(D, n, 'P21 sol %d' % si)
        dms.append({'sol': si, 'bases': [b[1:] for b in bases], 'rows': D})
        for (p, q, maps) in normal_forms(D, n):
            n_forms += 1
            for (i, f) in maps:
                n_occ += 1
                if f not in inventory:
                    inventory[f] = len(inv)
                    inv.append({'f': f, 'occurrences': []})
                inv[inventory[f]]['occurrences'].append([si, p, q, i])

    # ---- explicit R1 closure, one lexicographically smallest representative per orbit
    units = [u for u in range(1, n) if gcd(u, n) == 1]
    gen_names = ['A', 'I'] + ['C%d' % u for u in units if u != 1]
    orbit_of, orbits = {}, []
    for idx, e in enumerate(inv):
        if e['f'] in orbit_of:
            continue
        parent = r1_orbit(e['f'], n, gen_names)
        if len(parent) > 6 * len(units):
            raise SystemExit('INTERNAL: R1-orbit of size %d exceeds 6 * |units|' % len(parent))
        for g in parent:
            if g in orbit_of:
                raise SystemExit('INTERNAL: R1-orbits overlap')
            orbit_of[g] = len(orbits)
        rep = min(parent)
        seed, word = (inventory[rep], []) if rep in inventory else (idx, word_to(parent, rep))
        if apply_word(inv[seed]['f'], word, n) != rep:
            raise SystemExit('INTERNAL: replay word does not reach the representative')
        orbits.append({'rep': rep, 'size': len(parent), 'seed': seed, 'word': word})
    order = sorted(range(len(orbits)), key=lambda o: orbits[o]['rep'])
    line_of = {o: pos + 1 for pos, o in enumerate(order)}
    members = [[] for _ in orbits]
    for idx, e in enumerate(inv):
        members[orbit_of[e['f']]].append(idx)
    reps = [orbits[o]['rep'] for o in order]
    for f in reps:
        check_orthomorphism(f, n, 'representative')

    # ---- calibration lists
    z9, scanned = [], 0
    for perm in itertools.permutations(range(1, 9)):
        scanned += 1
        f = (0,) + perm
        if is_perm([(f[x] - x) % 9 for x in range(9)], 9):
            check_orthomorphism(f, 9, 'Z_9 map')
            z9.append(f)
    if scanned != 40320 or len(z9) != Z9_EXPECTED:
        raise SystemExit('Z_9: %d normalised orthomorphisms among %d permutations, expected %d among 40320'
                         % (len(z9), scanned, Z9_EXPECTED))
    lin = {}
    for m in (7, 13):
        lin[m] = tuple((2 * x) % m for x in range(m))
        check_orthomorphism(lin[m], m, 'f(x) = 2x mod %d' % m)
    ktext = raw['kirtchakov-cfr-5-25.raw'].decode('ascii')
    if not ktext.endswith('\n'):
        raise SystemExit('Kirtchakov raw file: no final LF')
    krows = [[int(x) for x in ln.split(' ')] for ln in ktext[:-1].split('\n')]
    if len(krows) != 5 or not all(is_perm(r, 25) for r in krows):
        raise SystemExit('Kirtchakov raw file: expected 5 rows, each a permutation of 0..24')
    krow = next((i for i, r in enumerate(krows) if r != list(range(25))), None)
    if krow is None:
        raise SystemExit('Kirtchakov raw file: no non-identity row')
    pos = [None] * 25
    for c, s in enumerate(krows[krow]):
        pos[s] = c
    kmap = tuple(pos)
    check_orthomorphism(kmap, 25, 'Kirtchakov position map')

    # ---- outputs (exclusive creates; summary.json last)
    kname = 'calib-kirtchakov-row%d-n25.txt' % krow
    files = {}
    for name, maps in (('p21-r1-reps-n21.txt', reps), ('calib-z9-all-n9.txt', z9), ('calib-linear2-n7.txt', [lin[7]]),
                       ('calib-linear2-n13.txt', [lin[13]]), (kname, [kmap])):
        files[name] = write_maps(outdir, name, maps)
    detail = {
        'map_format': 'f = [f(1), ..., f(n-1)], f(0) = 0',
        'dms': dms,
        'inventory': [{'index': idx, 'f': list(e['f'][1:]), 'rep_line': line_of[orbit_of[e['f']]],
                       'occurrences': e['occurrences']} for idx, e in enumerate(inv)],
        'representatives': [{'line': line_of[o], 'f': list(orbits[o]['rep'][1:]), 'orbit_size': orbits[o]['size'],
                             'rep_in_inventory': orbits[o]['rep'] in inventory,
                             'seed_inventory_index': orbits[o]['seed'],
                             'seed_occurrence': inv[orbits[o]['seed']]['occurrences'][0],
                             'word_from_seed': orbits[o]['word'], 'inventory_members': members[o]} for o in order],
    }
    dtext = json.dumps(detail, separators=(',', ':')) + '\n'
    with open(outdir / 'p21-detail.json', 'x', encoding='ascii', newline='\n') as fh:
        fh.write(dtext)
    files['p21-detail.json'] = {'file': 'p21-detail.json', 'sha256': sha(dtext.encode('ascii'))}
    summary = {
        'program': 'code/gen_full_seeds_c21v1.py',
        'clock_start': start,
        'clock_end': clock(),
        'outdir': str(outdir.resolve()),
        'sources': {key: {'path': str(path), 'sha256': sha(raw[key])} for key, path in SOURCES.items()},
        'map_files_format': 'one map per line: f(1) .. f(N-1), single spaces, LF; f(0) = 0 (f1file of cfr_perm_search_c21v1)',
        'checks': ('every map (inventory, every R1 image, representatives, calibration) checked directly: f(0) = 0 and f, '
                   'f - id permutations of Z_N; every P21 array: all 15 row pairs; every normal form: its 4 f-rows '
                   'pairwise orthogonal; every replay word re-applied'),
        'p21': {
            'n': n, 'k': k, 'spec': spec,
            'model_group_lines_mu_pinv_t': [[m, list(p), list(t)] for (m, p, t) in G],
            'run_record': rec,
            'sol_lines': len(sols),
            'column_order': ('column 0 = zero column; then for each base column in sol order its distinct images under the '
                             'P21.model G lines in file order, (g b)_x = mu b[pinv[x]] + t[x] - (mu b[pinv[0]] + t[0]) '
                             '(dmorbit_xc_c21v1 emit order)'),
            'row_pairs_checked': pairs_checked,
            'normalisation': ('ordered rows p != q: E_i = D_i - D_p; the column with E_q = s gets index s; row i becomes '
                              'f(s) = E_i(col(s)) - E_i(col(0)); p -> 0, q -> id, the other 4 rows -> f'),
            'normal_forms': n_forms,
            'occurrences': n_occ,
            'occurrence_format': '[sol, p, q, i]: sol 1-based sol-line index, rows 0-based in the expanded 6 x 21 array',
            'inventory_distinct': len(inv),
            'r1': {
                'A': 'f(x) -> f(-x) + x (renormalisation (p, q) = (id, 0); id - f only for odd f)',
                'I': 'f -> f^-1 (renormalisation (p, q) = (0, f))',
                'C<u>': 'f(x) -> u f(u^-1 x) for a unit u',
                'units': units,
                'validity': ('facts-v4 R1: these maps send normalised DMs to normalised DMs, so "f is an f-row of a '
                             'normalised DM" is R1-invariant; no oddness is used'),
            },
            'closure_size': len(orbit_of),
            'closure_maps_not_in_inventory': len(orbit_of) - len(inv),
            'representatives': len(orbits),
            'representatives_in_inventory': sum(1 for o in orbits if o['rep'] in inventory),
            'orbit_size_histogram': {str(s): c for s, c in sorted(Counter(o['size'] for o in orbits).items())},
            'representatives_file': files['p21-r1-reps-n21.txt'],
            'replay': ('p21-detail.json: dms[sol-1].rows is the expanded array; inventory[j].occurrences lists every '
                       '[sol, p, q, i] giving map j; representatives[r] (line r+1) is obtained from '
                       'inventory[seed_inventory_index] by applying word_from_seed left to right (A, I, C<u>)'),
            'scope': ('An exhaustive engine run over every representative (f_1 fixed, all 4-cliques of L2) would exclude '
                      'exactly the normalised (Z_21, 7; 1)-DMs having at least one f-row in this finite R1-closed '
                      'family: restricted evidence only. No P21 or other symmetry of a target DM is assumed or implied.'),
        },
        'calibration': {
            'z9_all': {'n': 9, 'permutations_scanned': scanned, 'count': len(z9), 'expected': Z9_EXPECTED,
                       'definition': 'all f with f(0) = 0, f(1..8) one of the 8! orders of 1..8, f - id a permutation',
                       'file': files['calib-z9-all-n9.txt']},
            'n7_linear2': {'n': 7, 'f': 'x -> 2x mod 7', 'file': files['calib-linear2-n7.txt']},
            'n13_linear2': {'n': 13, 'f': 'x -> 2x mod 13', 'file': files['calib-linear2-n13.txt']},
            'n25_kirtchakov': {'n': 25, 'source_row_0based': krow,
                               'definition': 'position map s -> c with row[c] = s of the first non-identity row',
                               'values': list(kmap[1:]), 'file': files[kname]},
        },
        'files_sha256': {name: info['sha256'] for name, info in files.items()},
    }
    with open(outdir / 'summary.json', 'x', encoding='ascii', newline='\n') as fh:
        json.dump(summary, fh, indent=1)
        fh.write('\n')
    print('P21: %d sols, %d occurrences, inventory %d, R1 closure %d, representatives %d; Z_9 %d; files in %s'
          % (len(sols), n_occ, len(inv), len(orbit_of), len(orbits), len(z9), outdir))


if __name__ == '__main__':
    main()
