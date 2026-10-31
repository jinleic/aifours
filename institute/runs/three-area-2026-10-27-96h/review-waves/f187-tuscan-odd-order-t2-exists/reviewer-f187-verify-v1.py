#!/usr/bin/env python3
"""Reviewer f187 independent verification (ReviewF187TuscanOdd21).

Independently authored reviewer code. It reads the listed wave inputs as DATA
only (bytes/JSON/Markdown); it never imports or executes author code (the
author checker is only hashed). Public-source data (Ollis, arXiv:1603.01496v1,
Section 1 presentation of G_{21,1}, Section 3 terrace) are transcribed below by
the reviewer from the rendered PDF page 8.

Usage: reviewer-f187-verify-v1.py RECEIPT_OUT.json   (exclusive create)
Exit 0: every check and every control behaved as recorded in `expectations`.
Exit 1: at least one mismatch (listed in the receipt and on stdout).
"""
import hashlib
import json
import re
import sys
import time
from collections import Counter

WAVE = ('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/'
        'review-waves/f187-tuscan-odd-order-t2-exists/')
BASE = ('/Users/jinleic/repos/aifours/information-science/evidence/'
        'three-area-20261027-96h/parallel-18/tuscan2-11/')
MANIFEST = ('manifest-v1.json',
            '10b7739be62eee9ec59c183a077eef80b7217cfd33607e7a4b77df0d9d5983d5')
INPUTS = [
    ('frontier-20261029-odd-order-t2-exists-and-refuted-boundary-shortcuts-v1.md',
     '4f0f07c01c9024da4bdd99eabbdd6ff2d7f17d8e3b4c6c8186deb4fc08ded29b', 5393, 71),
    ('frontier-20261029-ollis-g21-t2-square-v1.json',
     '4f20ab9ae5c125bf13cdcc9b847d2ee040dac6e29ac9e14a32c5bfd158fb7c3c', 4055, 516),
    ('frontier-20261028-general-t2-check-v1.py',
     'a534f304686eeae097c824ee4ff90c202b6260b02d4c8caf5a55f558acb760e0', 2166, 47),
    ('frontier-20261029-ollis-g21-t2-check-v1.json',
     '419cfbab18c6126dbccc6f0ed5a87af8ecbf1441a2bd717ed85f1358de1ee218', 831, 67),
    ('frontier-20261029-small-and-odd-t2-profiles-v1.json',
     '2d78d16d047f415fe4c50902a7a6e1c1e1fe9df7460203eced192082be011316', 3028, 200),
]

# Reviewer transcription of Ollis arXiv:1603.01496v1 p.8 (Section 3), read from
# the rendered page, as (u-exponent, v-exponent) pairs of words u^i v^j.
PAPER_TERRACE_WORDS = ['e', 'v', 'u', 'v^2', 'u^4', 'u^2v', 'u^4v^2', 'u^6v^2', 'uv',
                       'u^3', 'u^3v^2', 'u^2', 'u^6', 'u^5v', 'u^2v^2', 'uv^2',
                       'u^5v^2', 'u^4v', 'u^3v', 'u^6v', 'u^5']
# pdftotext -layout rendering of the same printed line (superscripts flattened).
PAPER_TERRACE_PDFTOTEXT = ('(e, v, u, v 2, u4 , u2 v, u4v 2 , u6 v 2 , uv, u3, u3v 2 , u2 , u6 , '
                           'u5v, u2 v 2 , uv 2, u5 v 2 , u4 v, u3v, u6 v, u5).')
PAPER_LAW_EXPONENT = 4  # Section 1: G21,1 = <u, v : u^7 = e = v^3, vu = u^4 v>

mismatches = []
facts = {}


def expect(label, observed, expected):
    ok = observed == expected
    facts[label] = {'observed': observed, 'expected': expected, 'ok': ok}
    if not ok:
        mismatches.append(label)
    return ok


def no_dup_hook(pairs):
    keys = [k for k, _ in pairs]
    dups = sorted(k for k, c in Counter(keys).items() if c > 1)
    if dups:
        raise ValueError('duplicate JSON keys: %r' % dups)
    return dict(pairs)


def load(path, sha, size, lf):
    raw = open(path, 'rb').read()
    got = (hashlib.sha256(raw).hexdigest(), len(raw), raw.count(b'\n'))
    expect('integrity:' + path.rsplit('/', 1)[1], list(got), [sha, size, lf])
    return raw


# ---------------------------------------------------------------- checker
def check_tuscan(rows, k):
    """Reviewer's own linear Tuscan-k / Latin checker on an explicit array."""
    n = len(rows)
    shape = n >= 2 and all(isinstance(r, list) and len(r) == n and
                           all(type(x) is int for x in r) for r in rows)
    rows_perm = shape and all(sorted(r) == list(range(n)) for r in rows)
    cols_perm = shape and all(sorted(rows[i][j] for i in range(n)) == list(range(n))
                              for j in range(n))
    dist = {}
    for m in range(1, k + 1):
        ev = [(r[i], r[i + m]) for r in rows for i in range(n - m)] if shape else []
        cnt = Counter(ev)
        rep = sorted(p for p, c in cnt.items() if c > 1)
        dist[m] = {'events': len(ev), 'distinct': len(cnt), 'repeated_pairs': len(rep),
                   'loops': sum(1 for a, b in ev if a == b),
                   'max_multiplicity': max(cnt.values()) if cnt else 0}
    d1_complete = rows_perm and dist[1]['events'] == n * (n - 1) == dist[1]['distinct']
    tuscan = rows_perm and all(dist[m]['repeated_pairs'] == 0 for m in dist)
    reasons = []
    if not rows_perm:
        reasons.append('row_not_permutation')
    reasons += ['repeat_at_distance_%d' % m for m in dist if dist[m]['repeated_pairs']]
    return {'n': n, 'k': k, 'shape_ok': shape, 'rows_perm': rows_perm, 'cols_perm': cols_perm,
            'latin': rows_perm and cols_perm, 'dist': dist, 'd1_complete': d1_complete,
            'tuscan_k': tuscan, 'fail_reasons': reasons}


def perm_sign(p):
    n, seen, s = len(p), [False] * len(p), 1
    for i in range(n):
        if not seen[i]:
            j, length = i, 0
            while not seen[j]:
                seen[j], j, length = True, p[j], length + 1
            if length % 2 == 0:
                s = -s
    return s


def cycle_type(mapping):
    seen, out = set(), []
    for a in sorted(mapping):
        if a in seen:
            continue
        length, b = 0, a
        while b not in seen:
            seen.add(b)
            b = mapping[b]
            length += 1
        out.append(length)
    return sorted(out, reverse=True)


def profile(rows):
    """Boundary-coincidence profile of an explicit T2 array (reviewer definitions)."""
    n = len(rows)
    first, last = [r[0] for r in rows], [r[-1] for r in rows]
    second, penult = [r[1] for r in rows], [r[-2] for r in rows]
    isperm = lambda col: sorted(col) == list(range(n))
    out = {'first_col_perm': isperm(first), 'last_col_perm': isperm(last),
           'second_col_perm': isperm(second), 'penult_col_perm': isperm(penult)}
    E = dict(zip(first, last))
    out['E'] = [E[a] for a in range(n)]
    out['E_cycle_type'] = cycle_type(E)
    out['E_fixed_points'] = sum(1 for a in range(n) if E[a] == a)
    out['E_squared_is_id'] = all(E[E[a]] == a for a in range(n))
    d2 = set((r[i], r[i + 2]) for r in rows for i in range(n - 2))
    M = set((a, b) for a in range(n) for b in range(n) if a != b) - d2
    C = set(zip(last, first))
    R = set(zip(penult, second))
    out.update({'M_size': len(M), 'closing_pairs_eq_M': C == M, 'M_eq_R': M == R,
                'M_is_permutation_graph': sorted(a for a, _ in M) == list(range(n)) and
                sorted(b for _, b in M) == list(range(n))})
    signs = [perm_sign(r) for r in rows]
    out['row_signs_plus_minus'] = [signs.count(1), signs.count(-1)]
    out['row_sign_classes'] = sorted((c for c in Counter(signs).values()), reverse=True)
    # Two reviewer hypotheses for the undefined JSON field "e_dist" (informational):
    pos = {}
    for r in rows:
        for i in range(n - 1):
            pos[(r[i], r[i + 1])] = i
    h1 = Counter(str(pos[(a, E[a])] + 1) for a in range(n))  # 1-based column of (a,E(a))
    start = {r[0]: r for r in rows}
    h2 = Counter(str(start[E[a]].index(a)) for a in range(n))  # 0-based col of a in row E(a)...
    out['e_dist_hypothesis_H1'] = dict(h1)
    out['e_dist_hypothesis_H2'] = dict(h2)
    return out


# ---------------------------------------------------------------- group G21
def make_group(r):
    els = [(i, j) for i in range(7) for j in range(3)]

    def mul(x, y):  # v^j u^k = u^(k r^j) v^j
        return ((x[0] + y[0] * pow(r, x[1], 7)) % 7, (x[1] + y[1]) % 3)
    e = (0, 0)
    inv = {}
    for x in els:
        cands = [y for y in els if mul(x, y) == e]
        assert len(cands) == 1
        inv[x] = cands[0]
    assoc = all(mul(mul(x, y), z) == mul(x, mul(y, z)) for x in els for y in els for z in els)
    ident = all(mul(e, x) == x == mul(x, e) for x in els)
    left_inv = all(mul(inv[x], x) == e for x in els)
    abelian = all(mul(x, y) == mul(y, x) for x in els for y in els)
    u, v = (1, 0), (0, 1)
    conj = mul(mul(v, u), inv[v])

    def power(x, k):
        y = e
        for _ in range(k):
            y = mul(y, x)
        return y
    rel = power(u, 7) == e and power(v, 3) == e and mul(v, u) == mul(power(u, r), v)
    return {'els': els, 'mul': mul, 'inv': inv, 'e': e, 'axioms': assoc and ident and left_inv,
            'abelian': abelian, 'v_u_vinv': conj, 'relations_hold': rel, 'power': power}


WORD = re.compile(r'^(?:u(?:\^(\d+))?)?(?:v(?:\^(\d+))?)?$')


def parse_word(w, mode):
    w = w.strip()
    if w == 'e':
        return (0, 0)
    if mode == 'flat':  # pdftotext flattening: 'u4v2' -> u^4 v^2 (single-digit exponents)
        m = re.match(r'^(?:u(\d)?)?(?:v(\d)?)?$', w)
        if not m or not w:
            raise ValueError('bad flat word %r' % w)
        i = (int(m.group(1)) if m.group(1) else 1) if w.startswith('u') else 0
        j = (int(m.group(2)) if m.group(2) else 1) if 'v' in w else 0
        return (i, j)
    m = WORD.match(w)
    if not m or not w:
        raise ValueError('bad word %r' % w)
    i = (int(m.group(1)) if m.group(1) else 1) if w.startswith('u') else 0
    j = (int(m.group(2)) if m.group(2) else 1) if 'v' in w else 0
    return (i, j)


def terrace_profile(G, seq, kmax):
    mul, inv, e = G['mul'], G['inv'], G['e']
    n = len(seq)
    out = {'arrangement': len(set(seq)) == n == len(G['els'])}
    for m in range(1, kmax + 1):
        q = [mul(inv[seq[i]], seq[i + m]) for i in range(n - m)]
        c = Counter(q)
        out['m%d' % m] = {'length': len(q), 'distinct': len(c),
                          'repeats': sum(1 for x in c.values() if x > 1),
                          'contains_identity': e in c}
    q1 = [mul(inv[seq[i]], seq[i + 1]) for i in range(n - 1)]
    # Bailey (undirected) terrace test for odd order: each {g, g^-1}, g != e, twice in total
    pair_counts = Counter(frozenset((g, inv[g])) for g in q1)
    out['bailey_terrace_odd_order'] = (e not in q1 and
                                       all(c == 2 for c in pair_counts.values()) and
                                       len(pair_counts) == (n - 1) // 2)
    return out


def square_from(G, seq):
    mul, inv = G['mul'], G['inv']
    lab = lambda g: 3 * g[0] + g[1]
    return [[lab(mul(inv[a], b)) for b in seq] for a in seq]


def main(argv):
    if len(argv) != 2:
        raise SystemExit('usage: reviewer-f187-verify-v1.py RECEIPT_OUT.json')
    t0 = time.time()
    out_path = argv[1]
    me = open(__file__, 'rb').read()
    facts['reviewer_script_sha256'] = hashlib.sha256(me).hexdigest()

    # -------- A. integrity + full JSON parses (data only)
    mraw = load(WAVE + MANIFEST[0], MANIFEST[1], 4503, 51)
    man = json.loads(mraw, object_pairs_hook=no_dup_hook)
    expect('manifest_inputs_match_reviewer_table',
           [[x['path'], x['sha256'], x['bytes'], x['LF']] for x in man['inputs_in_read_order']],
           [[BASE + a, b, c, d] for a, b, c, d in INPUTS])
    raws = {name: load(BASE + name, sha, size, lf) for name, sha, size, lf in INPUTS}
    md = raws[INPUTS[0][0]].decode('utf-8')
    sq = json.loads(raws[INPUTS[1][0]], object_pairs_hook=no_dup_hook)
    rec = json.loads(raws[INPUTS[3][0]], object_pairs_hook=no_dup_hook)
    prof = json.loads(raws[INPUTS[4][0]], object_pairs_hook=no_dup_hook)
    expect('rows_json_keys', sorted(sq), sorted(['construction', 'element_labels', 'group_law_used',
                                                 'kind', 'n', 'rows', 'source',
                                                 'terrace_text_as_transcribed']))
    expect('rows_json_n', sq['n'], 21)
    expect('element_labels_are_3i_plus_j',
           sq['element_labels'], {'%d,%d' % (i, j): 3 * i + j for i in range(7) for j in range(3)})
    rows = sq['rows']

    # -------- B. own checker on the 21x21 array
    chk = check_tuscan(rows, 3)
    expect('n21_shape_ok', chk['shape_ok'], True)
    expect('n21_rows_permutations', chk['rows_perm'], True)
    expect('n21_columns_permutations(Latin)', chk['cols_perm'], True)
    expect('n21_d1_events_distinct_repeats', [chk['dist'][1]['events'], chk['dist'][1]['distinct'],
                                              chk['dist'][1]['repeated_pairs']], [420, 420, 0])
    expect('n21_d1_complete_all_420_ordered_pairs', chk['d1_complete'], True)
    expect('n21_d2_events_distinct_repeats', [chk['dist'][2]['events'], chk['dist'][2]['distinct'],
                                              chk['dist'][2]['repeated_pairs']], [399, 399, 0])
    facts['n21_d3_informational'] = chk['dist'][3]
    chk2 = check_tuscan(rows, 2)
    expect('n21_is_linear_tuscan2', chk2['tuscan_k'], True)
    tr = [[rows[i][j] for i in range(21)] for j in range(21)]
    expect('n21_transpose_is_tuscan2(2-complete,informational)', check_tuscan(tr, 2)['tuscan_k'], True)

    # -------- C. E and boundary profile of the 21x21 array; compare with profiles JSON
    p21 = profile(rows)
    facts['n21_profile'] = p21
    expect('n21_E_cycle_type', p21['E_cycle_type'], [7, 7, 7])
    expect('n21_E_fixed_points', p21['E_fixed_points'], 0)
    expect('n21_E_squared_is_id', p21['E_squared_is_id'], False)
    j21 = prof['profiles']['n21_G21']
    expect('n21_profile_keys', sorted(j21), sorted(['B_eq_M', 'E_cycle_type', 'M_eq_R',
                                                     'closing_pairs_eq_M', 'e_dist', 'n',
                                                     'penult_col_perm', 'row_sign_classes',
                                                     'second_col_perm']))
    for key in ['E_cycle_type', 'M_eq_R', 'closing_pairs_eq_M', 'penult_col_perm',
                'second_col_perm', 'row_sign_classes']:
        expect('n21_json_vs_reviewer:' + key, p21[key], j21[key])
    facts['n21_json_e_dist_vs_hypotheses'] = {'json': j21['e_dist'], 'H1': p21['e_dist_hypothesis_H1'],
                                              'H2': p21['e_dist_hypothesis_H2']}
    facts['n21_json_B_eq_M_not_recomputable(B undefined in listed inputs)'] = j21['B_eq_M']

    # -------- D. author receipt (data only) vs reviewer computation
    expect('receipt_keys', sorted(rec), sorted(['all_rows_permutations', 'distance_one_complete',
                                                'first_column', 'input', 'input_sha256',
                                                'is_tuscan_k_square', 'k', 'last_column', 'n',
                                                'per_distance']))
    expect('receipt_values_vs_reviewer',
           [rec['input_sha256'], rec['n'], rec['k'], rec['all_rows_permutations'],
            rec['distance_one_complete'], rec['is_tuscan_k_square'], rec['first_column'],
            rec['last_column'],
            {m: [rec['per_distance'][m]['events'], rec['per_distance'][m]['distinct'],
                 rec['per_distance'][m]['repeated_pairs']] for m in sorted(rec['per_distance'])}],
           [INPUTS[1][1], 21, 2, True, True, True, [r[0] for r in rows], [r[-1] for r in rows],
            {'1': [420, 420, []], '2': [399, 399, []]}])

    # -------- E. group reconstruction against the public source
    G4, G2 = make_group(4), make_group(2)
    expect('G(law u^4)_group_axioms_nonabelian_relation',
           [G4['axioms'], G4['abelian'], G4['v_u_vinv'], G4['relations_hold']],
           [True, False, (4, 0), True])
    expect('G(law u^2)_group_axioms_nonabelian_relation',
           [G2['axioms'], G2['abelian'], G2['v_u_vinv'], G2['relations_hold']],
           [True, False, (2, 0), True])
    paper_seq = [parse_word(w, 'caret') for w in PAPER_TERRACE_WORDS]
    flat_tokens = PAPER_TERRACE_PDFTOTEXT.strip('().').split(',')
    flat_seq = [parse_word(t.replace(' ', ''), 'flat') for t in flat_tokens]
    json_seq = [parse_word(w, 'caret') for w in sq['terrace_text_as_transcribed'].split(',')]
    expect('terrace_paper_visual_eq_pdftotext', paper_seq, flat_seq)
    expect('terrace_json_transcription_eq_paper', json_seq, paper_seq)
    expect('paper_law_exponent', PAPER_LAW_EXPONENT, 4)
    tp4 = terrace_profile(G4, paper_seq, 3)
    tp2 = terrace_profile(G2, paper_seq, 2)
    facts['terrace_profile_law_u4'] = tp4
    facts['terrace_profile_law_u2'] = tp2
    expect('law_u4_is_directed_T2_terrace',
           [tp4['arrangement'], tp4['m1']['distinct'], tp4['m1']['contains_identity'],
            tp4['m2']['distinct'], tp4['m2']['contains_identity']], [True, 20, False, 19, False])
    sq4 = square_from(G4, paper_seq)
    expect('square_rebuilt_from_paper_terrace_law_u4_eq_json_rows', sq4 == rows, True)
    sq2 = square_from(G2, paper_seq)
    c2 = check_tuscan(sq2, 2)
    facts['law_u2_square_check'] = c2
    expect('law_u2_square_negative_intended_reason',
           [c2['rows_perm'], c2['cols_perm'], c2['tuscan_k'],
            c2['dist'][1]['repeated_pairs'] > 0, c2['dist'][2]['repeated_pairs'] > 0],
           [True, True, False, True, True])
    # group-level boundary facts (left-translate structure)
    mul, inv = G4['mul'], G4['inv']
    lab = lambda g: 3 * g[0] + g[1]
    a = paper_seq
    an = a[-1]
    expect('E_equals_right_multiplication_by_a_n',
           all(p21['E'][lab(x)] == lab(mul(x, an)) for x in G4['els']), True)
    order_an = next(k for k in range(1, 22) if G4['power'](an, k) == G4['e'])
    expect('order_of_a_n(u^5)', [an, order_an], [(5, 0), 7])
    q2 = set(mul(inv[a[i]], a[i + 2]) for i in range(19))
    qstar = sorted(set(G4['els']) - {G4['e']} - q2)
    expect('unique_missing_2_quotient', len(qstar), 1)
    expect('qstar_eq_inv(a_n)[C=M]', qstar[0] == inv[an], True)
    expect('qstar_eq_inv(a_{n-1})a_2[M=R]', qstar[0] == mul(inv[a[-2]], a[1]), True)
    facts['qstar'] = qstar[0]

    # -------- F. mutation controls (must break T2 for the intended reason)
    swaps = broke = intended = also_d2 = 0
    for r in range(21):
        for p in range(21):
            for q in range(p + 1, 21):
                mut = [row[:] for row in rows]
                mut[r][p], mut[r][q] = mut[r][q], mut[r][p]
                c = check_tuscan(mut, 2)
                swaps += 1
                broke += (not c['tuscan_k'])
                intended += (c['rows_perm'] and c['dist'][1]['repeated_pairs'] > 0)
                also_d2 += (c['dist'][2]['repeated_pairs'] > 0)
    expect('mutation_within_row_swaps_all_break_T2', [swaps, broke, intended], [4410, 4410, 4410])
    facts['mutation_swaps_that_also_create_D2_repeat'] = also_d2
    mut = [row[:] for row in rows]
    mut[0][4], mut[0][5] = mut[0][5], mut[0][4]  # the single designated swap (row 0, cols 4,5)
    c = check_tuscan(mut, 2)
    facts['designated_swap_row0_cols4_5'] = {'tuscan_k': c['tuscan_k'], 'fail_reasons': c['fail_reasons'],
                                              'd1': c['dist'][1], 'd2': c['dist'][2]}
    expect('designated_swap_breaks_T2_by_D1_repeat',
           [c['tuscan_k'], c['rows_perm'], c['dist'][1]['repeated_pairs'] > 0], [False, True, True])
    mut = [row[:] for row in rows]
    mut[0][0] = mut[0][1]
    c = check_tuscan(mut, 2)
    expect('overwrite_one_entry_fails_as_non_permutation',
           [c['tuscan_k'], 'row_not_permutation' in c['fail_reasons']], [False, True])

    # -------- G. checker calibration on independent known objects
    for p in (5, 7, 11, 13):
        vat = [[(i * j) % p - 1 for j in range(1, p)] for i in range(1, p)]
        cv = check_tuscan(vat, p - 2)
        expect('positive_control_multiplicative_vatican_order_%d' % (p - 1),
               [cv['tuscan_k'], cv['d1_complete'], cv['latin']], [True, True, True])
    for m in (5, 21):
        cyc = [[(i + j) % m for j in range(m)] for i in range(m)]
        cc = check_tuscan(cyc, 2)
        expect('negative_control_cyclic_latin_order_%d' % m,
               [cc['latin'], cc['tuscan_k'], cc['fail_reasons'][:1]],
               [True, False, ['repeat_at_distance_1']])

    # -------- H. candidate table vs profiles JSON (internal consistency only)
    table = [ln for ln in md.split('\n') if ln.startswith('| ') and not ln.startswith('| property')]
    parsed = [[c.strip().strip('*') for c in ln.strip('|').split('|')] for ln in table]
    facts['md_table_rows'] = parsed
    P = prof['profiles']
    expect('profiles_json_keys', [sorted(prof), sorted(P)],
           [['inputs', 'kind', 'profiles', 'scope'],
            ['n21_G21', 'n4', 'n6', 'n8_0', 'n8_1', 'n8_2', 'n8_3', 'n8_4', 'n8_5']])
    for key, ent in P.items():
        expect('profiles_json_entry_schema:' + key, sorted(ent), sorted(j21))
    groups = {'n=4': ['n4'], 'n=6': ['n6'], 'n=8': ['n8_%d' % i for i in range(6)], 'n=21': ['n21_G21']}
    expect('profiles_json_n_values', {k: [P[x]['n'] for x in v] for k, v in groups.items()},
           {'n=4': [4], 'n=6': [6], 'n=8': [8] * 6, 'n=21': [21]})

    def summarise(keys, pred):
        hits = sum(1 for x in keys if pred(P[x]))
        if len(keys) == 1:
            return 'yes' if hits else 'no'
        return 'yes' if hits == len(keys) else ('no' if hits == 0 else '%d of %d' % (hits, len(keys)))
    preds = [lambda d: all(c == 2 for c in d['E_cycle_type']),
             lambda d: d['second_col_perm'] and d['penult_col_perm'],
             lambda d: d['closing_pairs_eq_M'],
             lambda d: d['M_eq_R'],
             lambda d: d['B_eq_M']]
    derived = [[summarise(groups[g], pr) for g in ['n=4', 'n=6', 'n=8', 'n=21']] for pr in preds]
    expect('md_table_cells_eq_profiles_json_summary', [row[1:] for row in parsed], derived)

    facts['elapsed_seconds'] = round(time.time() - t0, 3)
    facts['mismatches'] = mismatches
    with open(out_path, 'x', encoding='utf-8') as fh:
        json.dump(facts, fh, indent=1, sort_keys=True, default=list)
        fh.write('\n')
    print(json.dumps({'mismatches': mismatches, 'n_checks': sum(1 for v in facts.values()
                                                             if isinstance(v, dict) and 'ok' in v),
                      'elapsed_seconds': facts['elapsed_seconds'],
                      'n21_E_cycle_type': p21['E_cycle_type'],
                      'reviewer_script_sha256': facts['reviewer_script_sha256']}))
    return 1 if mismatches else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
