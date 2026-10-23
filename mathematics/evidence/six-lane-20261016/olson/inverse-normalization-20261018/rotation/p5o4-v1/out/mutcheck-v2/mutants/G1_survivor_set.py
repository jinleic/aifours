#!/usr/bin/env python3
"""Stage C, version 2, of p5o4-v1/PLAN-v1.md (p = 5, o_F = 4): fail-closed comparison of the Stage G (GRX) and
Stage D (direct ordered DP) outputs of one run directory.

Supersedes code/compare_p5o4_v1.py after the Codex review R/olson-p5o4-code-result-codex-v1.note.md:
  M1  v1 checked only the strata present in each per_H (a missing or empty stratum passed vacuously), never validated
      p, k, N, and trusted the formula fields;
  m1  v1 exited 0 on FAIL.
Stage G and Stage D are NOT rerun: this script only reads their outputs.

Usage: compare_p5o4_v2.py RUNDIR OUTFILE
  Reads exactly the nine files in INPUTS from RUNDIR (a fixed list; nothing is discovered from the filesystem), writes
  OUTFILE with open(..., 'x'), and exits 0 iff the verdict is PASS, 1 otherwise (2 on a usage error).
  The verdict is PASS iff every check named in REQUIRED was evaluated and is True and no other check was recorded; an
  exception while checking is recorded as the failed check 'no_exception'.
Independent recomputations (no input field is trusted for them): per stratum H = 0..4 (R = 14 - 2H) the number
M_H = 625 C(R+19,19) of GRX classes and L_H M_H of labelled block-length representations (L_H = C(H+3,3)); the set
of rotation multisets failing the pairs filter P1' (a third, brute-force implementation); the examined counts
625 sum_c n(c), n(c) = prod_x C(c_x+3,3); the rigidity of every avoider multiset; the TC5 mutation specification.
Internal self-checks (independent of the inputs; a failure raises and gives FAIL): the multiset and distribution
counts match their binomial formulas, and the recomputed totals equal the numbers frozen in PLAN-v1 Sec. 3.
Stage D's fields words_formula, words_p1prime_solved and words_enumerated count LABELLED BLOCK-LENGTH
REPRESENTATIONS (H, block-length tuple, run multisets, y-tuple); several can spell the same literal word, so they are
not counts of distinct raw words.
Every input protection is marked '# PROT-<id>' for the single-protection mutation check
(code/mutcheck_compare_p5o4_v2.py).
"""
import sys, os, json, hashlib, re, traceback
from math import comb

P, K, NLEN = 5, 4, 18
HS = (0, 1, 2, 3, 4)
HSTR = ['0', '1', '2', '3', '4']
NCHECK = 3000          # PLAN-v1 Sec. 7: controls on the first 3000 avoider classes in canonical order
P1S = 20000            # PLAN-v1 Sec. 7: size of the P1' validation sample
PLAN = {'classes': 613973068750, 'classes_examined': 25267500,
        'representations': 1021369625000, 'representations_examined': 255650000}   # PLAN-v1 Sec. 3
INPUTS = ['grx_summary.json', 'grx_survivors.txt', 'grx_avoiders.txt', 'grx_mutations.txt',
          'dp_summary.json', 'dp_survivors.txt', 'dp_avoiders.txt', 'dp_mutations.txt', 'dp_mixed.txt']
LISTS = ('survivors', 'avoiders', 'mutations')
G_TOP = {'p', 'k', 'N', 'per_H', 'controls', 'files', 'avoider_types', 'total_nonrigid_avoider_classes'}
D_TOP = {'p', 'k', 'N', 'per_H', 'controls', 'total_nonrigid_avoider_classes', 'mixed_classes', 'avoider_classes'}
G_PERH = {'R', 'multisets', 'survivor_multisets', 'classes_formula', 'classes_allplus_solved', 'classes_enumerated',
          'avoider_classes', 'nonrigid_avoider_classes'}
D_PERH = {'R', 'multisets', 'survivor_multisets', 'words_formula', 'words_p1prime_solved', 'words_enumerated',
          'avoider_classes', 'nonrigid_avoider_classes'}
G_CTL = {'translation_invariant', 'positive_k2_example_avoider', 'TC1_plusminus_only_avoiders', 'TC1_nonrigid',
         'TC2_cmax_F_avoiders', 'TC2_true_avoiders_flipped', 'mutation_lines', 'mutation_solvable'}
D_CTL = {'positive_k2_example_avoider', 'p1prime_sample_tested', 'p1prime_sample_failures',
         'shift_reversal_checked_classes', 'shift_reversal_failures', 'TC4_target8_solvable', 'TC3_words',
         'TC3_verdict_differences', 'mutation_lines', 'mutation_solvable'}
G_FILES = {'grx_survivors.txt', 'grx_avoiders.txt', 'grx_mutations.txt'}
FIELDS = {'G': ('classes_formula', 'classes_allplus_solved', 'classes_enumerated'),
          'D': ('words_formula', 'words_p1prime_solved', 'words_enumerated')}
REQUIRED = (['no_exception', 'inputs_regular_files', 'header_G', 'header_D', 'strata_G', 'strata_D', 'keysets',
             'lists_identical', 'lists_wellformed', 'mixed_empty', 'survivor_lines', 'survivor_set', 'avoider_lines',
             'rigid_avoiders', 'mutation_structure', 'mutation_counts']
            + ['%s_H%d_%s' % (t, H, x) for H in HS for t in ('G', 'D')
               for x in ('shape', 'formula', 'examined', 'cover', 'counts')]
            + ['counts_files', 'controls', 'types'])
REQUIRED_SET = set(REQUIRED)
SURV_RE = re.compile(r'H=([0-4])\|Y=(\d+),(\d+),(\d+),(\d+),(\d+)\|rigid=([01])\|ndist=(\d+)')
AV_RE = re.compile(r'H=([0-4])\|dist=(\d+(?:,\d+){4}(?:/\d+(?:,\d+){4}){3})\|y=([0-4]{4})')
MUT_RE = re.compile(r'(H=[0-4]\|dist=[0-9,/]+\|y=[0-4]{4})\|(rot:[0-3]:[0-4]>[0-4]|blk:[0-3]>[0-4])\|([01])')


def isint(x):
    return type(x) is int


def ieq(d, k, v):
    x = d.get(k)
    return type(x) is int and x == v


def irange(d, k, lo, hi):
    x = d.get(k)
    return type(x) is int and (lo is None or x >= lo) and (hi is None or x <= hi)


def rigid(c):
    """All values in one set {v, -v}, v != 0 (PLAN-v1 Sec. 3); value 0 is never rigid."""
    supp = [x for x in range(P) if c[x] > 0]
    if 0 in supp:
        return False
    return len(supp) <= 1 or (len(supp) == 2 and (supp[0] + supp[1]) % P == 0)


def ndist(c):
    r = 1
    for x in range(P):
        r *= comb(c[x] + 3, 3)
    return r


def multisets(R):
    for c1 in range(R + 1):
        for c2 in range(R + 1 - c1):
            for c3 in range(R + 1 - c1 - c2):
                for c4 in range(R + 1 - c1 - c2 - c3):
                    yield (R - c1 - c2 - c3 - c4, c1, c2, c3, c4)


def p1prime(c, H):
    """Brute force: some sub-multiset of size 10 - 2j (0 <= j <= H) has value sum 0 (mod 5)."""
    sizes = [10 - 2 * j for j in range(H + 1)]
    for t1 in range(c[1] + 1):
        for t2 in range(c[2] + 1):
            for t3 in range(c[3] + 1):
                for t4 in range(c[4] + 1):
                    if (t1 + 2 * t2 + 3 * t3 + 4 * t4) % P == 0:
                        s = t1 + t2 + t3 + t4
                        if any(s <= m <= s + c[0] for m in sizes):
                            return True
    return False


def recompute():
    expected, table = {}, {}
    tot = dict.fromkeys(PLAN, 0)
    for H in HS:
        R = 14 - 2 * H
        allc = list(multisets(R))
        surv = sorted(c for c in allc if not p1prime(c, H))
        if len(allc) != comb(R + 4, 4) or len(set(allc)) != len(allc) or sum(ndist(c) for c in allc) != comb(R + 19, 19):
            raise RuntimeError('internal self-check failed at H=%d' % H)
        M, L = 625 * comb(R + 19, 19), comb(H + 3, 3)
        ex = 625 * sum(ndist(c) for c in surv)
        expected[H] = surv
        table[str(H)] = {'R': R, 'multisets': len(allc), 'survivor_multisets': len(surv), 'L_H': L, 'M_H_classes': M,
                         'classes_examined': ex, 'classes_filtered': M - ex, 'representations': L * M,
                         'representations_examined': L * ex, 'representations_filtered': L * (M - ex)}
        tot['classes'] += M
        tot['classes_examined'] += ex
        tot['representations'] += L * M
        tot['representations_examined'] += L * ex
    if tot != PLAN:
        raise RuntimeError('internal self-check failed: recomputed totals %r differ from PLAN-v1 Sec. 3' % tot)
    return expected, table, tot


def strict_json(b):
    def pairs(ps):
        ks = [k for k, _ in ps]
        if len(ks) != len(set(ks)):
            raise ValueError('duplicate JSON key')
        return dict(ps)

    def bad_constant(s):
        raise ValueError('non-finite JSON constant ' + s)
    return json.loads(b.decode('ascii'), object_pairs_hook=pairs, parse_constant=bad_constant)


def split_lines(b):
    """(well-formed, lines): ASCII, every line non-empty and terminated by a single newline, no carriage returns."""
    try:
        t = b.decode('ascii')
    except UnicodeDecodeError:
        return False, []
    if t == '':
        return True, []
    ls = t.split('\n')
    ok = ls[-1] == '' and '\r' not in t
    ls = ls[:-1] if ls[-1] == '' else ls
    return ok and all(l != '' for l in ls), ls


def mutation_specs(a):
    _, H, d, y, c = a
    s = ['rot:%d:%d>%d' % (i, x, x2) for i in range(K) for x in range(P) if d[i][x] > 0 for x2 in range(P) if x2 != x]
    s += ['blk:%d>%d' % (i, y2) for i in range(K) for y2 in range(P) if y2 != y[i]]
    return sorted(s)


def body(rundir, check, derived):
    expected, table, tot = recompute()
    derived['table'], derived['totals'] = table, tot
    paths = {n: os.path.join(rundir, n) for n in INPUTS}
    check('inputs_regular_files', all(os.path.isfile(q) and not os.path.islink(q) for q in paths.values()))  # PROT-IRF
    raw = {}
    for n in INPUTS:
        with open(paths[n], 'rb') as f:
            raw[n] = f.read()
    derived['inputs'] = {n: {'sha256': hashlib.sha256(raw[n]).hexdigest(), 'bytes': len(raw[n])} for n in INPUTS}
    G = strict_json(raw['grx_summary.json'])
    D = strict_json(raw['dp_summary.json'])
    for tag, S in (('G', G), ('D', D)):
        check('header_' + tag, isinstance(S, dict) and all(isint(S.get(x)) for x in ('p', 'k', 'N')) and (S['p'], S['k'], S['N']) == (P, K, NLEN))  # PROT-A
    for tag, S in (('G', G), ('D', D)):
        check('strata_' + tag, isinstance(S.get('per_H'), dict) and sorted(S['per_H']) == HSTR)  # PROT-B
    gH = G['per_H'] if isinstance(G.get('per_H'), dict) else {}
    dH = D['per_H'] if isinstance(D.get('per_H'), dict) else {}
    keys_ok = (set(G) == G_TOP and set(D) == D_TOP
               and isinstance(G['controls'], dict) and set(G['controls']) == G_CTL
               and isinstance(D['controls'], dict) and set(D['controls']) == D_CTL
               and isinstance(G['files'], dict) and set(G['files']) == G_FILES
               and all(isinstance(G['files'][f], dict) and set(G['files'][f]) == {'lines', 'sha256'} for f in G_FILES)
               and isinstance(G['avoider_types'], dict)
               and all(isinstance(e, dict) and set(e) == G_PERH for e in gH.values())
               and all(isinstance(e, dict) and set(e) == D_PERH for e in dH.values()))
    check('keysets', keys_ok)  # PROT-C
    lines, wf = {}, True
    for n in INPUTS:
        if n.endswith('.txt'):
            ok, ls = split_lines(raw[n])
            lines[n], wf = ls, wf and ok
    check('lists_identical', all(raw['grx_%s.txt' % L] == raw['dp_%s.txt' % L] for L in LISTS))  # PROT-H1
    check('lists_wellformed', wf and all(ls == sorted(ls) and len(set(ls)) == len(ls) for ls in lines.values()))  # PROT-H2
    check('mixed_empty', raw['dp_mixed.txt'] == b'' and ieq(D, 'mixed_classes', 0))  # PROT-K
    # survivors of the pairs filter
    surv, sl_ok = {H: [] for H in HS}, True
    for l in lines['grx_survivors.txt']:
        m = SURV_RE.fullmatch(l)
        if m is None:
            sl_ok = False
            continue
        H, c = int(m.group(1)), tuple(int(m.group(i)) for i in range(2, 7))
        if l != 'H=%d|Y=%s|rigid=%d|ndist=%d' % (H, ','.join(map(str, c)), int(rigid(c)), ndist(c)) or sum(c) != 14 - 2 * H:
            sl_ok = False
        surv[H].append(c)
    check('survivor_lines', sl_ok)  # PROT-G2
    check('survivor_set', True or all(sorted(surv[H]) == expected[H] for H in HS))  # PROT-G1
    # avoider classes
    av, al_ok = [], True
    for l in lines['grx_avoiders.txt']:
        m = AV_RE.fullmatch(l)
        if m is None:
            al_ok = False
            continue
        H = int(m.group(1))
        d = tuple(tuple(int(v) for v in r.split(',')) for r in m.group(2).split('/'))
        y = tuple(int(ch) for ch in m.group(3))
        c = tuple(sum(d[i][x] for i in range(K)) for x in range(P))
        if l != 'H=%d|dist=%s|y=%s' % (H, '/'.join(','.join(map(str, r)) for r in d), ''.join(map(str, y))) or sum(c) != 14 - 2 * H:
            al_ok = False
        av.append((l, H, d, y, c))
    check('avoider_lines', al_ok)  # PROT-AL
    exp_set = {H: set(expected[H]) for H in HS}
    check('rigid_avoiders', all(c in exp_set[H] and rigid(c) for (_, H, _, _, c) in av))  # PROT-J
    # TC5 mutation list
    mut, ml_ok = {}, True
    for l in lines['grx_mutations.txt']:
        m = MUT_RE.fullmatch(l)
        if m is None:
            ml_ok = False
            continue
        mut.setdefault(m.group(1), []).append(m.group(2))
    avd = {a[0]: a for a in av}
    first = [a[0] for a in av][:min(NCHECK, len(av))]
    check('mutation_structure', ml_ok and sorted(mut) == sorted(first) and all(sorted(mut[b]) == mutation_specs(avd[b]) for b in first))  # PROT-L1
    mlines = lines['grx_mutations.txt']
    nsolv = sum(1 for l in mlines if l.endswith('|1'))
    gc, dc = G['controls'], D['controls']
    check('mutation_counts', ieq(gc, 'mutation_lines', len(mlines)) and ieq(dc, 'mutation_lines', len(mlines)) and ieq(gc, 'mutation_solvable', nsolv) and ieq(dc, 'mutation_solvable', nsolv) and nsolv > 0)  # PROT-L2
    # per-stratum accounting against the recomputed formulas and the lists
    nav, nnr = {H: 0 for H in HS}, {H: 0 for H in HS}
    for a in av:
        nav[a[1]] += 1
        nnr[a[1]] += 0 if rigid(a[4]) else 1
    for H in HS:
        R = 14 - 2 * H
        M, L, ex = table[str(H)]['M_H_classes'], table[str(H)]['L_H'], table[str(H)]['classes_examined']
        for tag, SH in (('G', gH), ('D', dH)):
            ff, sf, ef = FIELDS[tag]
            mult = 1 if tag == 'G' else L
            e = SH.get(str(H)) if isinstance(SH.get(str(H)), dict) else {}
            check('%s_H%d_shape' % (tag, H), ieq(e, 'R', R) and ieq(e, 'multisets', comb(R + 4, 4)))  # PROT-S
            check('%s_H%d_formula' % (tag, H), ieq(e, ff, mult * M))  # PROT-D
            check('%s_H%d_examined' % (tag, H), ieq(e, ef, mult * ex))  # PROT-E
            check('%s_H%d_cover' % (tag, H), isint(e.get(sf)) and isint(e.get(ef)) and e.get(sf) + e.get(ef) == mult * M)  # PROT-F
            check('%s_H%d_counts' % (tag, H), ieq(e, 'survivor_multisets', len(surv[H])) and ieq(e, 'avoider_classes', nav[H]) and ieq(e, 'nonrigid_avoider_classes', nnr[H]))  # PROT-I1
    ntot = sum(nnr.values())
    check('counts_files', ieq(G, 'total_nonrigid_avoider_classes', ntot) and ieq(D, 'total_nonrigid_avoider_classes', ntot) and ieq(D, 'avoider_classes', len(av)) and all(G['files'][f].get('sha256') == hashlib.sha256(raw[f]).hexdigest() and ieq(G['files'][f], 'lines', len(lines[f])) for f in sorted(G_FILES)))  # PROT-I2
    # controls (PLAN-v1 Sec. 7)
    n = len(av)
    nchk, ex4 = min(NCHECK, n), table['4']['classes_examined']
    ctl_ok = (gc.get('translation_invariant') is True and gc.get('positive_k2_example_avoider') is True
              and dc.get('positive_k2_example_avoider') is True
              and irange(gc, 'TC1_nonrigid', 1, None) and irange(gc, 'TC1_plusminus_only_avoiders', gc.get('TC1_nonrigid'), None)
              and irange(gc, 'TC2_true_avoiders_flipped', 1, n) and irange(gc, 'TC2_cmax_F_avoiders', 0, None)
              and ieq(dc, 'p1prime_sample_tested', P1S) and ieq(dc, 'p1prime_sample_failures', 0)
              and ieq(dc, 'shift_reversal_checked_classes', nchk) and ieq(dc, 'shift_reversal_failures', 0)
              and irange(dc, 'TC4_target8_solvable', 1, nchk)
              and ieq(dc, 'TC3_words', ex4) and irange(dc, 'TC3_verdict_differences', 1, ex4))
    check('controls', ctl_ok)  # PROT-M
    tc = {}
    for a in av:
        key = 'H=%d|Y=%s' % (a[1], ','.join(map(str, a[4])))
        tc[key] = tc.get(key, 0) + 1
    at = G['avoider_types']
    t1 = any(a[1] == 4 and a[4][0] == 0 and sum(1 for v in a[4] if v) == 1 for a in av)
    t2 = any(a[1] == 1 and sorted(v for v in a[4] if v) == [3, 9] and rigid(a[4]) for a in av)
    check('types', isinstance(at, dict) and all(type(v) is int for v in at.values()) and at == tc and t1 and t2)  # PROT-N


def run(rundir):
    checks, reasons, derived = {}, [], {}

    def check(name, cond):
        if name in checks:
            raise RuntimeError('check evaluated twice: ' + name)
        checks[name] = cond is True
        if cond is not True:
            reasons.append(name)
    try:
        body(rundir, check, derived)
    except Exception:
        checks['no_exception'] = False
        reasons.append('no_exception: ' + traceback.format_exc().strip().splitlines()[-1])
    else:
        checks['no_exception'] = True
    missing = [r for r in REQUIRED if r not in checks]
    unexpected = sorted(c for c in checks if c not in REQUIRED_SET)
    passed = not missing and not unexpected and all(checks[r] is True for r in REQUIRED)  # PROT-P
    return ('PASS' if passed else 'FAIL'), checks, reasons, missing, unexpected, derived


def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    if len(argv) != 2:
        sys.stderr.write('usage: compare_p5o4_v2.py RUNDIR OUTFILE\n')
        sys.exit(2)
    rundir, outfile = argv
    verdict, checks, reasons, missing, unexpected, derived = run(rundir)
    with open(os.path.abspath(__file__), 'rb') as f:
        own = hashlib.sha256(f.read()).hexdigest()
    out = {'comparator': os.path.basename(__file__), 'comparator_sha256': own, 'rundir': rundir, 'verdict': verdict,
           'exit_status': 0 if verdict == 'PASS' else 1, 'n_required': len(REQUIRED), 'checks': checks,
           'failed': sorted(c for c, v in checks.items() if v is not True), 'missing_required': missing,
           'unexpected_checks': unexpected, 'reasons': reasons, 'inputs': derived.get('inputs'),
           'recomputed_per_H': derived.get('table'), 'recomputed_totals': derived.get('totals'),
           'note': ('Stage D words_* fields and the representations counts are labelled block-length representations '
                    '(H, block-length tuple, run multisets, y-tuple), not distinct raw words')}
    with open(outfile, 'x') as f:
        json.dump(out, f, indent=1, sort_keys=True)
        f.write('\n')
    print(verdict, 'failed=%d' % len(out['failed']), 'missing_required=%d' % len(missing))
    sys.exit(0 if verdict == 'PASS' else 1)  # PROT-Q


if __name__ == '__main__':
    main()
