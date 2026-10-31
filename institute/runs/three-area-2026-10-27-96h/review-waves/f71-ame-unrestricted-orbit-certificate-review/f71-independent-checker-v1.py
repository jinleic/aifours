#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
f71-independent-checker-v1.py
Reviewer-authored, Python 3 standard library only, for review wave
  f71-ame-unrestricted-orbit-certificate-review  (aifours three-area-2026-10-27-96h).

No author code is imported or consulted.  Inputs:
  TABLE   pinned transcription  frontier-20261028-pandya-table-v1.txt
  HTML    public arXiv source   https://arxiv.org/html/2610.16673v1  (saved bytes)
  TWOFACE pinned candidate      frontier-20261028-two-face-unrestricted-orbit-60-v1.md
          (only its backticked 12-entry P' list is read, to compare with Eq. (6))

Usage:
  python3 f71-independent-checker-v1.py TABLE HTML TWOFACE --output RECEIPT.json
Refuses to overwrite RECEIPT.json.  Exit status 0 iff every check and every
control behaved as intended.

Checks (codes used in the receipt):
  T1  strict parse of pinned table: 36 cells, 12 sqrt2 singletons, 24 two-term
      cells with +-1, 60 distinct positions
  T2  independent parse of arXiv HTML Table 1 (LaTeX alttext) == pinned table
  T3  independent parse of arXiv Eq. (6): P1|P2|P3 == all-K support of table;
      P1'|P2'|P3' == two-face candidate's P' list
  C1  K colour relabelling: colour tuples of P == even class A4 exactly;
      colour tuples of P' == odd class exactly
  C2  sharp two-transitivity of the even class and of the odd class;
      S4-conjugation preserves parity and is transitive on ordered pairs (i,c), i!=c
  E1  E: 48 terms, exactly two H indices, equal spectator colours, 8 per pair,
      every (pair,colour) 2x2 block is a signed Pauli, and across the four
      colours each pair carries exactly one each of I, X, Z, J up to sign
  E2  no term with 1, 3 or 4 H indices; all-K support == P exactly
  Z1  structural zeros used by the proof (both faces): all-K positions with a
      repeated colour vanish; two-H positions with unequal spectators vanish;
      matched (g,g) K outputs are fed only by E_{ij,g}; distinct-colour K outputs
      are fed only by the all-K face set
  I1  F F^T = 2 I_36 for all three 2|2 cuts, exactly in Z[sqrt2], for the
      zero-phase face P tensor and for the zero-phase face P' tensor
  B1  for S in {P, P'} and all three cuts: the 12 S terms occupy 12 distinct
      rows and 12 distinct columns, disjoint from the 24 E rows and 24 E columns,
      and the 24x24 E block has exact integer Gram matrix 2 I_24.  Hence
      F F^dagger = 2 I_36 for arbitrary independent unit phases on S.
  B2  floating-point spot check of B1's conclusion with random phases (diagnostic)
  M1  exhaustive 15^4 = 50625 nonempty colour-mask 4-tuples against the rule
      "no permutation of the class meets exactly two or three masks": survivors
      are exactly 4 same-singleton + 12 class-permutation + 1 all-full = 17, for
      the even class and for the odd class; zero-pattern lemma for the three
      pair-product equalities; the written 7-permutation chain forces full support
  P1  Pauli algebra over Z / Z[i]: anticommutation of X,Z,J; linear independence;
      Hilbert-Schmidt orthogonality with squared norm 2; orthogonality (unitarity);
      transpose closure; conjugation signs Q sigma_a Q^-1 = eps sigma_a giving sign
      rows (+++),(+--),(--+),(-+-); Hs^T Hs = 4 I_3; and the Bloch identity
        2 |eta_i^T Q eta_j|^2 - |eta_i|^2 |eta_j|^2
          = eps_x r'_ix r_jx + eps_y r'_iy r_jy + eps_z r'_iz r_jz,  r' = (r_x,-r_y,r_z),
      verified exactly on the grid {0,1,2}^8 of the eight real spinor coordinates.
      Both sides have degree <= 2 in every single variable, so agreement on a
      3-point grid per variable proves the polynomial identity.
  K   controls: each mutation must trip the intended check code(s).
"""
import sys, os, re, json, hashlib, itertools, cmath, random, datetime, platform

H = (1, 2)
K = (0, 3, 4, 5)
COLOUR_BASE = {0: {0: 3, 3: 2, 4: 0, 5: 1},
               1: {0: 3, 3: 0, 4: 2, 5: 1},
               2: {0: 3, 3: 0, 4: 2, 5: 1},
               3: {0: 3, 3: 2, 4: 1, 5: 0}}
PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
CUTS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
CHAIN_BASE = [(1, 3, 2, 0), (1, 2, 0, 3), (3, 2, 1, 0), (3, 1, 0, 2),
              (2, 3, 0, 1), (2, 0, 1, 3), (2, 1, 3, 0)]
SIGN_ROWS_BASE = {'I': (1, 1, 1), 'X': (1, -1, -1), 'Z': (-1, -1, 1), 'J': (-1, 1, -1)}

# ---------- exact arithmetic ----------
ZERO = (0, 0); ONE = (1, 0); MONE = (-1, 0); SQ2 = (0, 1)   # p + q*sqrt2


def zadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def zmul(x, y):
    return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def zfloat(x):
    return x[0] + x[1] * 2 ** 0.5


def gi_add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gi_mul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gi_conj(x):
    return (x[0], -x[1])


def gi_abs2(x):
    return x[0] * x[0] + x[1] * x[1]


class CheckError(Exception):
    def __init__(self, code, msg):
        super().__init__('%s: %s' % (code, msg))
        self.code = code
        self.msg = msg


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def perm_parity(p):
    if sorted(p) != [0, 1, 2, 3]:
        raise ValueError('not a permutation of 0..3: %r' % (p,))
    inv = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                inv += 1
    return inv % 2


ALL_PERMS = list(itertools.permutations(range(4)))
EVEN = [p for p in ALL_PERMS if perm_parity(p) == 0]
ODD = [p for p in ALL_PERMS if perm_parity(p) == 1]

# integer 2x2 Paulis (real), J = Z X
PAULI_INT = {
    'I': ((1, 0), (0, 1)),
    'X': ((0, 1), (1, 0)),
    'Z': ((1, 0), (0, -1)),
    'J': ((0, 1), (-1, 0)),
}

# ---------- parsing: pinned table ----------
RE_TWO = re.compile(r'^([+-])([0-5])([0-5])$')
RE_ONE = re.compile(r'^s([0-5])([0-5])$')


def parse_pinned_table(text):
    T = {}
    cells = {}
    lines = text.split('\n')
    if lines and lines[-1] == '':
        lines = lines[:-1]
    for ln, raw in enumerate(lines, 1):
        if raw.startswith('#'):
            continue
        if raw.strip() == '':
            raise CheckError('T1_SYNTAX', 'blank line %d' % ln)
        toks = raw.split()
        if len(toks) not in (3, 4):
            raise CheckError('T1_SYNTAX', 'line %d token count %d' % (ln, len(toks)))
        for t in toks[:2]:
            if not (len(t) == 1 and t in '012345'):
                raise CheckError('T1_SYNTAX', 'line %d bad cell index %r' % (ln, t))
        a, b = int(toks[0]), int(toks[1])
        if (a, b) in cells:
            raise CheckError('T1_DUPLICATE_CELL', 'cell (%d,%d) repeated at line %d' % (a, b, ln))
        rest = toks[2:]
        terms = []
        if len(rest) == 1:
            m = RE_ONE.match(rest[0])
            if not m:
                raise CheckError('T1_SYNTAX', 'line %d bad singleton token %r' % (ln, rest[0]))
            terms.append(((a, b, int(m.group(1)), int(m.group(2))), SQ2))
        else:
            for tok in rest:
                m = RE_TWO.match(tok)
                if not m:
                    raise CheckError('T1_SYNTAX', 'line %d bad signed token %r' % (ln, tok))
                s = ONE if m.group(1) == '+' else MONE
                terms.append(((a, b, int(m.group(2)), int(m.group(3))), s))
        cells[(a, b)] = terms
        for pos, coef in terms:
            if pos in T:
                raise CheckError('T1_DUPLICATE_POSITION', 'position %r repeated' % (pos,))
            T[pos] = coef
    return T, cells


def check_table_shape(T, cells):
    if len(cells) != 36:
        raise CheckError('T1_CELL_COUNT', 'expected 36 cells, found %d' % len(cells))
    n1 = n2 = 0
    for ab, terms in cells.items():
        if len(terms) == 1:
            if terms[0][1] != SQ2:
                raise CheckError('T1_CELL_TERM_COUNT', 'singleton cell %r without sqrt2' % (ab,))
            n1 += 1
        elif len(terms) == 2:
            for pos, coef in terms:
                if coef not in (ONE, MONE):
                    raise CheckError('T1_CELL_TERM_COUNT', 'two-term cell %r with non +-1' % (ab,))
            n2 += 1
        else:
            raise CheckError('T1_CELL_TERM_COUNT', 'cell %r has %d terms' % (ab, len(terms)))
    if (n1, n2) != (12, 24):
        raise CheckError('T1_CELL_TYPE_COUNT', 'singleton/two-term cells = (%d,%d), expected (12,24)' % (n1, n2))
    if len(T) != 60:
        raise CheckError('T1_SUPPORT_SIZE', 'support %d != 60' % len(T))
    return {'cells': 36, 'singleton_cells': n1, 'two_term_cells': n2, 'support': len(T)}


# ---------- parsing: public arXiv HTML ----------
RE_ALT = re.compile(r'alttext="([^"]*)"')
RE_L2 = re.compile(r'^(-?)\\ket\{([0-5])([0-5])\}([+-])\\ket\{([0-5])([0-5])\}$')
RE_L1 = re.compile(r'^\\sqrt\{2\}\\,\\ket\{([0-5])([0-5])\}$')


def parse_html_table1(html):
    i = html.find('id="S2.T1"')
    if i < 0:
        raise CheckError('T2_HTML_TABLE_NOT_FOUND', 'no element id S2.T1')
    j = html.find('<table', i)
    k = html.find('</table>', j)
    if j < 0 or k < 0:
        raise CheckError('T2_HTML_TABLE_NOT_FOUND', 'table tags missing')
    alts = RE_ALT.findall(html[j:k])
    if len(alts) != 49:
        raise CheckError('T2_HTML_TABLE_SHAPE', '%d alttext cells, expected 49' % len(alts))
    header = alts[:7]
    if header != ['\\ket{\\phi_{ab}}'] + ['b=%d' % b for b in range(6)]:
        raise CheckError('T2_HTML_TABLE_SHAPE', 'unexpected header %r' % (header,))
    T = {}
    for r in range(6):
        row = alts[7 + 7 * r: 14 + 7 * r]
        if row[0] != 'a=%d' % r:
            raise CheckError('T2_HTML_TABLE_SHAPE', 'row label %r' % (row[0],))
        for b in range(6):
            cell = row[1 + b]
            m2 = RE_L2.match(cell)
            m1 = RE_L1.match(cell)
            if m2:
                s1 = MONE if m2.group(1) == '-' else ONE
                s2 = ONE if m2.group(4) == '+' else MONE
                terms = [((r, b, int(m2.group(2)), int(m2.group(3))), s1),
                         ((r, b, int(m2.group(5)), int(m2.group(6))), s2)]
            elif m1:
                terms = [((r, b, int(m1.group(1)), int(m1.group(2))), SQ2)]
            else:
                raise CheckError('T2_HTML_CELL_SYNTAX', 'cell (%d,%d) latex %r' % (r, b, cell))
            for pos, coef in terms:
                if pos in T:
                    raise CheckError('T2_HTML_DUPLICATE_POSITION', '%r' % (pos,))
                T[pos] = coef
    return T


RE_EQ6_VAL = re.compile(r'^\\displaystyle=\\\{(\d{4}(?:,\d{4}){3})\\\}[,.]$')
EQ6_NAMES = ['P_{1}', 'P_{2}', 'P_{3}', 'P^{\\prime}_{1}', 'P^{\\prime}_{2}', 'P^{\\prime}_{3}']


def parse_html_eq6(html):
    i = html.find('id="S4.E6"')
    if i < 0:
        raise CheckError('T3_HTML_EQ6_NOT_FOUND', 'no element id S4.E6')
    alts = RE_ALT.findall(html[i:i + 20000])
    if len(alts) < 12:
        raise CheckError('T3_HTML_EQ6_SHAPE', 'only %d alttexts after S4.E6' % len(alts))
    sets = {}
    for n in range(6):
        name, val = alts[2 * n], alts[2 * n + 1]
        if name != '\\displaystyle ' + EQ6_NAMES[n]:
            raise CheckError('T3_HTML_EQ6_SHAPE', 'name %r' % (name,))
        m = RE_EQ6_VAL.match(val)
        if not m:
            raise CheckError('T3_HTML_EQ6_SHAPE', 'value %r' % (val,))
        words = m.group(1).split(',')
        tuples = [tuple(int(ch) for ch in w) for w in words]
        for t in tuples:
            if any(x > 5 for x in t):
                raise CheckError('T3_HTML_EQ6_SHAPE', 'index out of range in %r' % (t,))
        sets[EQ6_NAMES[n]] = tuples
    return sets


RE_PPRIME_LIST = re.compile(r'`((?:\d{4}, ){11}\d{4})`')


def parse_two_face_pprime(md):
    m = RE_PPRIME_LIST.search(md)
    if not m:
        raise CheckError('T3_TWO_FACE_LIST_NOT_FOUND', 'no backticked 12-entry list')
    return [tuple(int(ch) for ch in w) for w in m.group(1).split(', ')]


def check_transcription(T, Thtml):
    if T != Thtml:
        only_t = sorted(set(T) - set(Thtml))
        only_h = sorted(set(Thtml) - set(T))
        diff = sorted(p for p in set(T) & set(Thtml) if T[p] != Thtml[p])
        raise CheckError('T2_TRANSCRIPTION_MISMATCH',
                         'only in pinned %r, only in html %r, coef differs %r' % (only_t, only_h, diff))
    return {'positions_compared': len(T), 'equal': True}


def check_eq6(eq6, P, pprime_list):
    P_html = eq6['P_{1}'] + eq6['P_{2}'] + eq6['P_{3}']
    Pp_html = eq6['P^{\\prime}_{1}'] + eq6['P^{\\prime}_{2}'] + eq6['P^{\\prime}_{3}']
    if len(set(P_html)) != 12 or len(set(Pp_html)) != 12:
        raise CheckError('T3_EQ6_SHAPE', 'quartets not 12 distinct')
    if set(P_html) != set(P):
        raise CheckError('T3_P_MISMATCH', 'Eq.(6) P1|P2|P3 %r != table all-K support %r' % (sorted(P_html), sorted(P)))
    if list(Pp_html) != list(pprime_list):
        raise CheckError('T3_PPRIME_LIST_MISMATCH', 'Eq.(6) %r != two-face list %r' % (Pp_html, pprime_list))
    if set(P_html) & set(Pp_html):
        raise CheckError('T3_EQ6_SHAPE', 'P and P\' intersect')
    # paper's side statement: all indices in {0,3,4,5} and exactly one 0
    for x in P_html + Pp_html:
        if any(v not in K for v in x) or x.count(0) != 1:
            raise CheckError('T3_EQ6_SHAPE', 'tuple %r not all-K with exactly one 0' % (x,))
    return {'P_from_eq6': ['%d%d%d%d' % x for x in P_html],
            'Pprime_from_eq6': ['%d%d%d%d' % x for x in Pp_html]}


# ---------- classification ----------
def n_H(pos):
    return sum(1 for v in pos if v in H)


def colour_tuple(pos, colour):
    return tuple(colour[i][pos[i]] for i in range(4))


def classify(T):
    P, E = [], []
    for pos in T:
        n = n_H(pos)
        if n == 0:
            P.append(pos)
        elif n == 2:
            E.append(pos)
        else:
            raise CheckError('E2_BAD_H_COUNT', 'position %r has %d H indices' % (pos, n))
    if len(P) != 12:
        raise CheckError('E2_P_COUNT', '%d all-K terms, expected 12' % len(P))
    if len(E) != 48:
        raise CheckError('E2_E_COUNT', '%d two-H terms, expected 48' % len(E))
    for pos in P:
        if T[pos] != SQ2:
            raise CheckError('E2_P_COEF', 'P term %r coefficient %r' % (pos, T[pos]))
    for pos in E:
        if T[pos] not in (ONE, MONE):
            raise CheckError('E2_E_COEF', 'E term %r coefficient %r' % (pos, T[pos]))
    return sorted(P), sorted(E)


def check_parity_class(S, colour, want_parity, code):
    tuples = []
    for pos in S:
        if any(v not in K for v in pos):
            raise CheckError(code, 'position %r not all-K' % (pos,))
        tuples.append(colour_tuple(pos, colour))
    try:
        pars = [perm_parity(t) for t in tuples]
    except ValueError as e:
        raise CheckError(code, str(e))
    want = set(EVEN if want_parity == 0 else ODD)
    if set(tuples) != want or len(set(tuples)) != 12:
        raise CheckError(code, 'colour tuples %r are not exactly the %s class' % (sorted(tuples), 'even' if want_parity == 0 else 'odd'))
    return {'colour_tuples': {'%d%d%d%d' % pos: '%d%d%d%d' % colour_tuple(pos, colour) for pos in S},
            'parities': pars}


def check_two_transitive(perm_class, label):
    for i, j in itertools.combinations(range(4), 2):
        for a, b in itertools.permutations(range(4), 2):
            n = sum(1 for p in perm_class if p[i] == a and p[j] == b)
            if n != 1:
                raise CheckError('C2_NOT_TWO_TRANSITIVE', '%s: positions (%d,%d) colours (%d,%d) extended by %d perms' % (label, i, j, a, b, n))
    return {'class': label, 'size': len(perm_class), 'sharply_two_transitive': True}


def check_conjugation_symmetry():
    # pi sigma pi^-1 preserves parity; S4 transitive on ordered pairs (i,c), i != c
    for pi in ALL_PERMS:
        inv = [0] * 4
        for i in range(4):
            inv[pi[i]] = i
        for sigma in ALL_PERMS:
            conj = tuple(pi[sigma[inv[i]]] for i in range(4))
            if perm_parity(conj) != perm_parity(sigma):
                raise CheckError('C2_CONJUGATION_PARITY', '%r %r' % (pi, sigma))
    for i, c in itertools.permutations(range(4), 2):
        if not any(pi[0] == i and pi[1] == c for pi in ALL_PERMS):
            raise CheckError('C2_CONJUGATION_TRANSITIVITY', '(%d,%d)' % (i, c))
    return {'conjugation_preserves_parity': True, 'transitive_on_ordered_pairs': True}


def signed_pauli_type(M):
    for name, Q in PAULI_INT.items():
        if M == Q:
            return name, +1
        if M == tuple(tuple(-v for v in row) for row in Q):
            return name, -1
    return None


def check_E_structure(E, T, colour):
    per_pair = {pr: {} for pr in PAIRS}
    counts = {pr: 0 for pr in PAIRS}
    for pos in E:
        hidx = tuple(i for i in range(4) if pos[i] in H)
        spec = tuple(i for i in range(4) if pos[i] not in H)
        if len(hidx) != 2:
            raise CheckError('E1_H_COUNT', '%r' % (pos,))
        g1, g2 = colour[spec[0]][pos[spec[0]]], colour[spec[1]][pos[spec[1]]]
        if g1 != g2:
            raise CheckError('E1_SPECTATOR_MISMATCH', 'position %r spectator colours %d,%d' % (pos, g1, g2))
        counts[hidx] += 1
        blk = per_pair[hidx].setdefault(g1, {})
        key = (pos[hidx[0]] - 1, pos[hidx[1]] - 1)
        if key in blk:
            raise CheckError('E1_DUPLICATE_ENTRY', '%r' % (pos,))
        blk[key] = T[pos][0]
    for pr in PAIRS:
        if counts[pr] != 8:
            raise CheckError('E1_PAIR_COUNT', 'pair %r has %d terms, expected 8' % (pr, counts[pr]))
    table = {}
    for pr in PAIRS:
        types = []
        for g in range(4):
            blk = per_pair[pr].get(g, {})
            M = tuple(tuple(blk.get((r, c), 0) for c in range(2)) for r in range(2))
            t = signed_pauli_type(M)
            if t is None:
                raise CheckError('E1_NOT_SIGNED_PAULI', 'pair %r colour %d block %r' % (pr, g, M))
            types.append(t[0])
            table[(pr, g)] = t
        if sorted(types) != ['I', 'J', 'X', 'Z']:
            raise CheckError('E1_PAULI_TYPES_NOT_ONE_EACH', 'pair %r types %r' % (pr, types))
    out = {}
    for (pr, g), (name, sgn) in table.items():
        out['%d%d/g%d' % (pr[0], pr[1], g)] = ('+' if sgn > 0 else '-') + name
    return out


def check_structural_zeros(NZ, S, colour, perm_class, face_label):
    """NZ: set of nonzero positions of the face tensor (E union S)."""
    allK_repeat_zero = 0
    twoH_unequal_zero = 0
    class_set = set(perm_class)
    for pos in itertools.product(range(6), repeat=4):
        n = n_H(pos)
        if n == 0:
            ct = colour_tuple(pos, colour)
            if len(set(ct)) < 4:
                if pos in NZ:
                    raise CheckError('Z1_ALLK_REPEAT_NONZERO', '%s: %r' % (face_label, pos))
                allK_repeat_zero += 1
            else:
                if (pos in NZ) != (ct in class_set):
                    raise CheckError('Z1_ALLK_CLASS_MISMATCH', '%s: %r colour %r' % (face_label, pos, ct))
        elif n == 2:
            spec = [i for i in range(4) if pos[i] not in H]
            if colour[spec[0]][pos[spec[0]]] != colour[spec[1]][pos[spec[1]]]:
                if pos in NZ:
                    raise CheckError('Z1_E_UNEQUAL_SPECTATOR_NONZERO', '%r' % (pos,))
                twoH_unequal_zero += 1
        else:
            if pos in NZ:
                raise CheckError('Z1_BAD_H_COUNT_NONZERO', '%r' % (pos,))
    # matched (g,g) K output on parties k<l is fed only by terms with H on both other parties
    matched_checked = 0
    for k, l in PAIRS:
        others = [i for i in range(4) if i not in (k, l)]
        for xk in K:
            for xl in K:
                if colour[k][xk] != colour[l][xl]:
                    continue
                for pos in NZ:
                    if pos[k] == xk and pos[l] == xl:
                        if not (pos[others[0]] in H and pos[others[1]] in H):
                            raise CheckError('Z1_MATCHED_OUTPUT_FED_BY_NON_E', '%s: output (%d,%d)=(%d,%d) fed by %r' % (face_label, k, l, xk, xl, pos))
                        matched_checked += 1
    # distinct-colour K output on parties i<j is fed only by all-K terms, exactly one of them
    distinct_checked = 0
    for i, j in PAIRS:
        for xi in K:
            for xj in K:
                if colour[i][xi] == colour[j][xj]:
                    continue
                feeders = [pos for pos in NZ if pos[i] == xi and pos[j] == xj]
                if any(n_H(pos) != 0 for pos in feeders):
                    raise CheckError('Z1_DISTINCT_K_OUTPUT_FED_BY_E', '%s: (%d,%d)=(%d,%d) %r' % (face_label, i, j, xi, xj, feeders))
                if len(feeders) != 1:
                    raise CheckError('Z1_DISTINCT_K_OUTPUT_COUNT', '%s: (%d,%d)=(%d,%d) has %d all-K feeders' % (face_label, i, j, xi, xj, len(feeders)))
                distinct_checked += 1
    return {'face': face_label, 'allK_repeated_colour_positions_zero': allK_repeat_zero,
            'twoH_unequal_spectator_positions_zero': twoH_unequal_zero,
            'matched_output_feeders_checked': matched_checked,
            'distinct_colour_output_pairs_checked': distinct_checked}


# ---------- flattenings ----------
def flatten(Tz, cut):
    (i, j), (k, l) = cut
    F = [[ZERO] * 36 for _ in range(36)]
    for pos, c in Tz.items():
        F[6 * pos[i] + pos[j]][6 * pos[k] + pos[l]] = c
    return F


def check_isometry_exact(Tz, label):
    checked = 0
    for cut in CUTS:
        F = flatten(Tz, cut)
        for r in range(36):
            for s in range(36):
                acc = ZERO
                for t in range(36):
                    if F[r][t] != ZERO and F[s][t] != ZERO:
                        acc = zadd(acc, zmul(F[r][t], F[s][t]))
                want = (2, 0) if r == s else ZERO
                if acc != want:
                    raise CheckError('I1_NOT_ISOMETRY', '%s cut %r entry (%d,%d) = %r' % (label, cut, r, s, acc))
                checked += 1
    return {'tensor': label, 'entries_checked': checked, 'FFt_equals_2I': True}


def check_block_structure(E, Ecoef, S, cut, face_label):
    (i, j), (k, l) = cut
    row = lambda pos: 6 * pos[i] + pos[j]
    col = lambda pos: 6 * pos[k] + pos[l]
    S_rows = [row(p) for p in S]
    S_cols = [col(p) for p in S]
    if len(S) != 12:
        raise CheckError('B1_S_COUNT', '%s cut %r: %d S terms' % (face_label, cut, len(S)))
    if len(set(S_rows)) != 12:
        raise CheckError('B1_S_ROW_COLLISION', '%s cut %r rows %r' % (face_label, cut, sorted(S_rows)))
    if len(set(S_cols)) != 12:
        raise CheckError('B1_S_COL_COLLISION', '%s cut %r cols %r' % (face_label, cut, sorted(S_cols)))
    E_rows = sorted(set(row(p) for p in E))
    E_cols = sorted(set(col(p) for p in E))
    if len(E_rows) != 24 or len(E_cols) != 24:
        raise CheckError('B1_E_COUNT', '%s cut %r: E rows %d cols %d' % (face_label, cut, len(E_rows), len(E_cols)))
    if set(E_rows) & set(S_rows) or set(E_cols) & set(S_cols):
        raise CheckError('B1_E_S_OVERLAP', '%s cut %r' % (face_label, cut))
    if sorted(set(E_rows) | set(S_rows)) != list(range(36)) or sorted(set(E_cols) | set(S_cols)) != list(range(36)):
        raise CheckError('B1_COVER', '%s cut %r rows/cols do not cover 36' % (face_label, cut))
    ri = {r: n for n, r in enumerate(E_rows)}
    ci = {c: n for n, c in enumerate(E_cols)}
    B = [[0] * 24 for _ in range(24)]
    for p in E:
        B[ri[row(p)]][ci[col(p)]] = Ecoef[p][0]
    for r in range(24):
        for s in range(24):
            g = sum(B[r][t] * B[s][t] for t in range(24))
            if g != (2 if r == s else 0):
                raise CheckError('B1_E_GRAM', '%s cut %r Gram (%d,%d) = %d' % (face_label, cut, r, s, g))
    return {'face': face_label, 'cut': '%d%d|%d%d' % (i, j, k, l), 'S_rows': 12, 'S_cols': 12,
            'E_rows': 24, 'E_cols': 24, 'disjoint': True, 'E_gram_2I24_entries': 576}


def float_phase_check(E, Ecoef, S, rng, face_label):
    worst = 0.0
    thetas = {p: rng.uniform(0, 2 * 3.141592653589793) for p in S}
    for cut in CUTS:
        (i, j), (k, l) = cut
        F = [[0j] * 36 for _ in range(36)]
        for p in E:
            F[6 * p[i] + p[j]][6 * p[k] + p[l]] = complex(Ecoef[p][0])
        for p in S:
            F[6 * p[i] + p[j]][6 * p[k] + p[l]] = (2 ** 0.5) * cmath.exp(1j * thetas[p])
        for r in range(36):
            for s in range(36):
                acc = sum(F[r][t] * F[s][t].conjugate() for t in range(36))
                want = 2.0 if r == s else 0.0
                worst = max(worst, abs(acc - want))
    return {'face': face_label, 'max_abs_deviation_from_2I': worst, 'diagnostic_only': True}


# ---------- masks ----------
def expected_mask_patterns(perm_class):
    out = set()
    for g in range(4):
        out.add((1 << g,) * 4)
    for p in perm_class:
        out.add(tuple(1 << p[i] for i in range(4)))
    out.add((15, 15, 15, 15))
    return out


def check_masks(perm_class, label):
    survivors = set()
    tested = 0
    for masks in itertools.product(range(1, 16), repeat=4):
        tested += 1
        ok = True
        for p in perm_class:
            hits = sum(1 for i in range(4) if (masks[i] >> p[i]) & 1)
            if hits == 2 or hits == 3:
                ok = False
                break
        if ok:
            survivors.add(masks)
    want = expected_mask_patterns(perm_class)
    if survivors != want:
        raise CheckError('M1_MASK_CLASSIFICATION', '%s: %d survivors, expected %d; extra %r missing %r' % (
            label, len(survivors), len(want), sorted(survivors - want)[:10], sorted(want - survivors)[:10]))
    return {'class': label, 'tuples_tested': tested, 'survivors': len(survivors),
            'same_singleton': 4, 'class_permutations': len(perm_class), 'all_full': 1}


def check_zero_pattern_lemma():
    consistent = set()
    for z in itertools.product((0, 1), repeat=4):
        ok = True
        for (i, j), (k, l) in CUTS:
            if (z[i] & z[j]) != (z[k] & z[l]):
                ok = False
        if ok:
            consistent.add(z)
    want = set(z for z in itertools.product((0, 1), repeat=4) if sum(z) <= 1) | {(1, 1, 1, 1)}
    if consistent != want:
        raise CheckError('M1_ZERO_PATTERN', '%r' % (sorted(consistent),))
    return {'consistent_positivity_patterns': sorted(''.join(map(str, z)) for z in consistent)}


def check_chain(chain):
    S = [{0, 1}, {1}, {2}, {3}]
    steps = []
    for p in chain:
        if perm_parity(p) != 0:
            raise CheckError('M1_CHAIN_PARITY', '%r is odd' % (p,))
        hits = sum(1 for i in range(4) if p[i] in S[i])
        if hits < 2:
            raise CheckError('M1_CHAIN_RULE_NOT_APPLICABLE', '%r hits only %d' % (p, hits))
        for i in range(4):
            S[i].add(p[i])
        steps.append({'perm': '%d%d%d%d' % p, 'hits_before': hits, 'supports_after': [sorted(s) for s in S]})
    if any(s != {0, 1, 2, 3} for s in S):
        raise CheckError('M1_CHAIN_INCOMPLETE', 'final supports %r' % ([sorted(s) for s in S],))
    return {'steps': steps, 'all_full': True}


# ---------- Pauli algebra and Bloch identity ----------
def gi_mat(M):
    return tuple(tuple((v, 0) for v in row) for row in M)


def gmul(A, B):
    return tuple(tuple(gi_add(gi_mul(A[r][0], B[0][c]), gi_mul(A[r][1], B[1][c])) for c in range(2)) for r in range(2))


def gneg(A):
    return tuple(tuple((-v[0], -v[1]) for v in row) for row in A)


def gtrans(A):
    return tuple(tuple(A[c][r] for c in range(2)) for r in range(2))


GI_I = gi_mat(PAULI_INT['I']); GI_X = gi_mat(PAULI_INT['X']); GI_Z = gi_mat(PAULI_INT['Z']); GI_J = gi_mat(PAULI_INT['J'])
GI_Y = (((0, 0), (0, -1)), ((0, 1), (0, 0)))   # sigma_y
GI_PAULI = {'I': GI_I, 'X': GI_X, 'Z': GI_Z, 'J': GI_J}
GI_SIGMA = {'x': GI_X, 'y': GI_Y, 'z': GI_Z}
GI_INV = {'I': GI_I, 'X': GI_X, 'Z': GI_Z, 'J': gneg(GI_J)}   # J^2 = -I


def det4(rows):
    # integer 4x4 determinant by Laplace expansion
    def det(m):
        if len(m) == 1:
            return m[0][0]
        return sum(((-1) ** c) * m[0][c] * det([r[:c] + r[c + 1:] for r in m[1:]]) for c in range(len(m)))
    return det(rows)


def check_pauli_algebra(sign_rows):
    res = {}
    if gmul(GI_Z, GI_X) != GI_J:
        raise CheckError('P1_J_DEFINITION', 'J != Z X')
    for a, b in itertools.combinations(['X', 'Z', 'J'], 2):
        AB = gmul(GI_PAULI[a], GI_PAULI[b]); BA = gmul(GI_PAULI[b], GI_PAULI[a])
        if AB != gneg(BA):
            raise CheckError('P1_ANTICOMMUTE', '%s %s' % (a, b))
    res['anticommute_XZ_XJ_ZJ'] = True
    vecs = [[v for row in PAULI_INT[n] for v in row] for n in ['I', 'X', 'Z', 'J']]
    d = det4(vecs)
    if d == 0:
        raise CheckError('P1_LINEAR_DEPENDENCE', 'det 0')
    res['span_det'] = d
    for a in ['I', 'X', 'Z', 'J']:
        for b in ['I', 'X', 'Z', 'J']:
            tr = sum(PAULI_INT[a][r][c] * PAULI_INT[b][r][c] for r in range(2) for c in range(2))
            if tr != (2 if a == b else 0):
                raise CheckError('P1_HS_ORTHOGONALITY', '%s %s tr %d' % (a, b, tr))
    res['hilbert_schmidt_orthogonal_norm2'] = True
    for a in ['I', 'X', 'Z', 'J']:
        if gmul(GI_PAULI[a], gtrans(GI_PAULI[a])) != GI_I:
            raise CheckError('P1_ORTHOGONAL', a)
        tt = gtrans(GI_PAULI[a])
        if tt not in (GI_PAULI[a], gneg(GI_PAULI[a])):
            raise CheckError('P1_TRANSPOSE_CLOSURE', a)
    res['orthogonal_and_transpose_closed'] = True
    for inv_name, M in GI_INV.items():
        if gmul(GI_PAULI[inv_name], M) != GI_I:
            raise CheckError('P1_INVERSE', inv_name)
    signs = {}
    for q in ['I', 'X', 'Z', 'J']:
        row = []
        for a in ['x', 'y', 'z']:
            C = gmul(gmul(GI_PAULI[q], GI_SIGMA[a]), GI_INV[q])
            if C == GI_SIGMA[a]:
                row.append(1)
            elif C == gneg(GI_SIGMA[a]):
                row.append(-1)
            else:
                raise CheckError('P1_CONJUGATION_SIGN', '%s %s' % (q, a))
        signs[q] = tuple(row)
    if signs != dict(sign_rows):
        raise CheckError('P1_SIGN_ROWS', 'computed %r vs stated %r' % (signs, sign_rows))
    res['sign_rows'] = {q: list(v) for q, v in signs.items()}
    Hs = [sign_rows[q] for q in ['I', 'X', 'Z', 'J']]
    for a in range(3):
        for b in range(3):
            v = sum(Hs[r][a] * Hs[r][b] for r in range(4))
            if v != (4 if a == b else 0):
                raise CheckError('P1_HTH', '(%d,%d)=%d' % (a, b, v))
    res['HsT_Hs_equals_4I3'] = True
    # Bloch identity on the grid {0,1,2}^8
    count = 0
    for a1, a2, b1, b2, c1, c2, d1, d2 in itertools.product((0, 1, 2), repeat=8):
        ei = ((a1, a2), (b1, b2)); ej = ((c1, c2), (d1, d2))
        ni = gi_abs2(ei[0]) + gi_abs2(ei[1]); nj = gi_abs2(ej[0]) + gi_abs2(ej[1])

        def bloch(e):
            r = []
            for a in ['x', 'y', 'z']:
                acc = (0, 0)
                for p in range(2):
                    for q in range(2):
                        acc = gi_add(acc, gi_mul(gi_mul(gi_conj(e[p]), GI_SIGMA[a][p][q]), e[q]))
                if acc[1] != 0:
                    raise CheckError('P1_BLOCH_REAL', '%r' % (acc,))
                r.append(acc[0])
            return r
        ri = bloch(ei); rj = bloch(ej)
        ri_conj = (ri[0], -ri[1], ri[2])
        for q in ['I', 'X', 'Z', 'J']:
            bil = (0, 0)
            for p in range(2):
                for s in range(2):
                    bil = gi_add(bil, gi_mul(gi_mul(ei[p], GI_PAULI[q][p][s]), ej[s]))
            lhs = 2 * gi_abs2(bil) - ni * nj
            rhs = sum(sign_rows[q][a] * ri_conj[a] * rj[a] for a in range(3))
            if lhs != rhs:
                raise CheckError('P1_BLOCH_IDENTITY', 'Q=%s eta_i=%r eta_j=%r lhs %d rhs %d' % (q, ei, ej, lhs, rhs))
            count += 1
    res['bloch_identity_grid_points'] = 3 ** 8
    res['bloch_identity_evaluations'] = count
    res['degree_argument'] = 'both sides have degree <= 2 in each of the 8 real variables; vanishing on {0,1,2}^8 proves the identity'
    return res


# ---------- pipeline ----------
def structural_checks(T, cells, pprime_list, colour, chain, sign_rows, even_class, odd_class, rng, do_float=True):
    """Runs every structural check independently; returns (results, failures)."""
    results = {}
    failures = {}

    def run(name, fn):
        try:
            results[name] = fn()
        except CheckError as e:
            failures[name] = {'code': e.code, 'msg': e.msg[:400]}
        except Exception as e:  # noqa
            failures[name] = {'code': 'CRASH', 'msg': repr(e)[:400]}

    run('T1_shape', lambda: check_table_shape(T, cells))
    try:
        P, E = classify(T)
        results['E2_classes'] = {'P': ['%d%d%d%d' % p for p in P], 'E_count': len(E)}
    except CheckError as e:
        failures['E2_classes'] = {'code': e.code, 'msg': e.msg[:400]}
        P = sorted(p for p in T if n_H(p) == 0)
        E = sorted(p for p in T if n_H(p) == 2)
    Ecoef = {p: T[p] for p in E}
    Pp = list(pprime_list)
    run('C1_P_even', lambda: check_parity_class(P, colour, 0, 'C1_P_NOT_EVEN_CLASS'))
    run('C1_Pprime_odd', lambda: check_parity_class(Pp, colour, 1, 'C1_PPRIME_NOT_ODD_CLASS'))
    run('C2_even_two_transitive', lambda: check_two_transitive(even_class, 'even'))
    run('C2_odd_two_transitive', lambda: check_two_transitive(odd_class, 'odd'))
    run('C2_conjugation', check_conjugation_symmetry)
    run('E1_pauli_families', lambda: check_E_structure(E, T, colour))
    run('Z1_face_P', lambda: check_structural_zeros(set(E) | set(P), P, colour, even_class, 'face P'))
    run('Z1_face_Pprime', lambda: check_structural_zeros(set(E) | set(Pp), Pp, colour, odd_class, "face P'"))
    run('I1_face_P_zero_phase', lambda: check_isometry_exact(T, 'E+P'))
    TPp = dict(Ecoef)
    for p in Pp:
        TPp[p] = SQ2
    run('I1_face_Pprime_zero_phase', lambda: check_isometry_exact(TPp, "E+P'"))
    for face_label, S in (('P', P), ("P'", Pp)):
        for cut in CUTS:
            name = 'B1_%s_%d%d|%d%d' % (face_label, cut[0][0], cut[0][1], cut[1][0], cut[1][1])
            run(name, lambda S=S, cut=cut, face_label=face_label: check_block_structure(E, Ecoef, S, cut, face_label))
        if do_float:
            run('B2_float_%s' % face_label, lambda S=S, face_label=face_label: float_phase_check(E, Ecoef, S, rng, face_label))
    run('M1_masks_even', lambda: check_masks(even_class, 'even'))
    run('M1_masks_odd', lambda: check_masks(odd_class, 'odd'))
    run('M1_zero_pattern', check_zero_pattern_lemma)
    run('M1_chain', lambda: check_chain(chain))
    run('P1_pauli_bloch', lambda: check_pauli_algebra(sign_rows))
    return results, failures


def main(argv):
    if len(argv) != 6 or argv[4] != '--output':
        sys.stderr.write(__doc__)
        return 2
    table_path, html_path, twoface_path, _, out_path = argv[1:]
    if os.path.exists(out_path):
        sys.stderr.write('refusing to overwrite %s\n' % out_path)
        return 3
    t_start = datetime.datetime.now().astimezone().isoformat(timespec='seconds')
    inputs = {}
    blobs = {}
    for role, p in (('table', table_path), ('html', html_path), ('twoface', twoface_path)):
        b = open(p, 'rb').read()
        blobs[role] = b
        inputs[role] = {'path': os.path.abspath(p), 'sha256': sha256_bytes(b), 'bytes': len(b)}
    self_bytes = open(os.path.abspath(__file__), 'rb').read()
    receipt = {
        'schema_version': 1,
        'checker': {'path': os.path.abspath(__file__), 'sha256': sha256_bytes(self_bytes), 'bytes': len(self_bytes)},
        'inputs': inputs,
        'environment': {'python': sys.version.split()[0], 'platform': platform.platform(), 'stdlib_only': True, 'author_code_imported': False},
        'clock_start_local': t_start,
    }
    rng = random.Random(20261028)
    overall = True
    try:
        table_text = blobs['table'].decode('utf-8')
        html = blobs['html'].decode('utf-8')
        twoface = blobs['twoface'].decode('utf-8')
        T, cells = parse_pinned_table(table_text)
        Thtml = parse_html_table1(html)
        eq6 = parse_html_eq6(html)
        pprime_list = parse_two_face_pprime(twoface)
        receipt['T2_transcription'] = check_transcription(T, Thtml)
        P_table = sorted(p for p in T if n_H(p) == 0)
        receipt['T3_eq6'] = check_eq6(eq6, P_table, pprime_list)
    except CheckError as e:
        receipt['source_failure'] = {'code': e.code, 'msg': e.msg}
        overall = False
        T = cells = Thtml = eq6 = pprime_list = None
    if T is not None:
        results, failures = structural_checks(T, cells, pprime_list, COLOUR_BASE, CHAIN_BASE, SIGN_ROWS_BASE, EVEN, ODD, rng)
        receipt['structural_results'] = results
        receipt['structural_failures'] = failures
        if failures:
            overall = False

        # ---------- controls ----------
        controls = []

        def control(name, expected_codes, mutate):
            nonlocal overall
            try:
                args = mutate()
                _, fails = structural_checks(*args, rng=random.Random(1), do_float=False)
                observed = sorted(set(f['code'] for f in fails.values()))
                crashed = any(f['code'] == 'CRASH' for f in fails.values())
                ok = all(c in observed for c in expected_codes) and not crashed
            except CheckError as e:
                observed = [e.code]
                ok = all(c in observed for c in expected_codes)
            controls.append({'control': name, 'expected_codes': expected_codes, 'observed_codes': observed, 'intended_rejection': ok})
            if not ok:
                overall = False

        def base_args(T2=None, cells2=None, pp=None, colour=None, chain=None, signs=None, even=None, odd=None):
            return (T2 if T2 is not None else dict(T), cells2 if cells2 is not None else dict(cells),
                    pp if pp is not None else list(pprime_list), colour if colour is not None else COLOUR_BASE,
                    chain if chain is not None else CHAIN_BASE, signs if signs is not None else SIGN_ROWS_BASE,
                    even if even is not None else EVEN, odd if odd is not None else ODD)

        def mut_text(old, new):
            txt = table_text
            if txt.count(old) != 1:
                raise CheckError('CONTROL_SETUP', 'anchor %r count %d' % (old, txt.count(old)))
            T2, c2 = parse_pinned_table(txt.replace(old, new))
            return T2, c2

        # K1 inserted P' term (odd permutation 0353) added to face P
        def k1():
            T2, c2 = mut_text('0 3 s44\n', '0 3 s44\n0 3 s53\n')  # duplicate cell -> parse error expected
            return base_args(T2, c2)
        control('K1_insert_Pprime_term_duplicate_cell', ['T1_DUPLICATE_CELL'], k1)

        def k1b():
            T2 = dict(T); T2[(0, 3, 5, 3)] = SQ2
            c2 = dict(cells); c2[(0, 3)] = cells[(0, 3)] + [((0, 3, 5, 3), SQ2)]
            return base_args(T2, c2)
        control('K1b_insert_Pprime_term_0353', ['T1_CELL_TERM_COUNT', 'E2_P_COUNT', 'I1_NOT_ISOMETRY', 'B1_S_COUNT'], k1b)

        # K2 swap one P term for a P' term (keeps count 12): parity and isometry must fail
        def k2():
            T2 = dict(T); del T2[(4, 5, 4, 0)]; T2[(4, 5, 0, 3)] = SQ2
            c2 = dict(cells); c2[(4, 5)] = [((4, 5, 0, 3), SQ2)]
            return base_args(T2, c2)
        control('K2_replace_P_term_4540_by_Pprime_4503', ['C1_P_NOT_EVEN_CLASS', 'I1_NOT_ISOMETRY', 'Z1_ALLK_CLASS_MISMATCH', 'B1_S_ROW_COLLISION'], k2)

        # K3 delete a P term
        def k3():
            T2, c2 = mut_text('4 5 s40\n', '')
            return base_args(T2, c2)
        control('K3_delete_P_term_4540', ['T1_CELL_COUNT', 'E2_P_COUNT', 'I1_NOT_ISOMETRY', 'B1_S_COUNT'], k3)

        # K4 sign flip of one E term: Pauli type coverage, isometry and E Gram must fail
        def k4():
            T2, c2 = mut_text('0 0 -12 +21\n', '0 0 +12 +21\n')
            return base_args(T2, c2)
        control('K4_sign_flip_0012', ['E1_PAULI_TYPES_NOT_ONE_EACH', 'I1_NOT_ISOMETRY', 'B1_E_GRAM'], k4)

        # K5 ket change making a non-Pauli block
        def k5():
            T2, c2 = mut_text('0 0 -12 +21\n', '0 0 -12 +22\n')
            return base_args(T2, c2)
        control('K5_ket_change_0021_to_0022', ['E1_NOT_SIGNED_PAULI', 'I1_NOT_ISOMETRY', 'B1_E_GRAM'], k5)

        # K6 missing E term
        def k6():
            T2, c2 = mut_text('0 0 -12 +21\n', '0 0 -12\n')
            return base_args(T2, c2)
        control('K6_missing_E_term_0021', ['T1_SYNTAX'], k6)

        def k6b():
            T2 = dict(T); del T2[(0, 0, 2, 1)]
            c2 = dict(cells); c2[(0, 0)] = [((0, 0, 1, 2), MONE)]
            return base_args(T2, c2)
        control('K6b_missing_E_term_0021_direct', ['T1_CELL_TERM_COUNT', 'E2_E_COUNT', 'E1_PAIR_COUNT', 'E1_NOT_SIGNED_PAULI', 'I1_NOT_ISOMETRY', 'B1_E_GRAM'], k6b)

        # K7 wrong colour relabelling on party 3
        def k7():
            colour = {k: dict(v) for k, v in COLOUR_BASE.items()}
            colour[3][4], colour[3][5] = colour[3][5], colour[3][4]
            return base_args(colour=colour)
        control('K7_relabel_party3_swap_4_5', ['C1_P_NOT_EVEN_CLASS', 'C1_PPRIME_NOT_ODD_CLASS'], k7)

        # K8 mask coverage with wrong classes
        control('K8_mask_rule_with_S4', ['M1_MASK_CLASSIFICATION'], lambda: base_args(even=ALL_PERMS))
        non2t = [p for p in ALL_PERMS if p[0] in (0, 1, 2)][:12]
        control('K8b_mask_rule_non_two_transitive_12_set', ['C2_NOT_TWO_TRANSITIVE', 'M1_MASK_CLASSIFICATION'], lambda: base_args(even=non2t))

        # K9 chain with last permutation removed
        control('K9_chain_drop_last', ['M1_CHAIN_INCOMPLETE'], lambda: base_args(chain=CHAIN_BASE[:-1]))
        control('K9b_chain_odd_perm', ['M1_CHAIN_PARITY'], lambda: base_args(chain=CHAIN_BASE[:-1] + [(2, 1, 0, 3)]))

        # K10 wrong Bloch sign row
        def k10():
            s = dict(SIGN_ROWS_BASE); s['J'] = (-1, -1, -1)
            return base_args(signs=s)
        control('K10_wrong_sign_row_J', ['P1_SIGN_ROWS', 'P1_HTH', 'P1_BLOCH_IDENTITY'], k10)

        def k10b():
            s = dict(SIGN_ROWS_BASE); s['X'] = (1, 1, -1); s['Z'] = (-1, 1, 1)
            return base_args(signs=s)
        control('K10b_wrong_sign_rows_XZ_keep_orthogonality', ['P1_SIGN_ROWS', 'P1_BLOCH_IDENTITY'], k10b)

        # K11 P' list mutated: one entry changed to a non-odd tuple
        def k11():
            pp = list(pprime_list); pp[0] = (0, 3, 3, 5)
            return base_args(pp=pp)
        control('K11_Pprime_list_mutated_0353_to_0335', ['C1_PPRIME_NOT_ODD_CLASS', 'B1_S_ROW_COLLISION'], k11)

        # K12 transcription controls (source comparison level)
        trans_controls = []
        try:
            Tm = dict(Thtml); Tm[(0, 0, 1, 2)] = ONE
            check_transcription(T, Tm)
            trans_controls.append({'control': 'K12_html_sign_flip', 'observed_codes': [], 'intended_rejection': False}); overall = False
        except CheckError as e:
            trans_controls.append({'control': 'K12_html_sign_flip', 'expected_codes': ['T2_TRANSCRIPTION_MISMATCH'], 'observed_codes': [e.code], 'intended_rejection': e.code == 'T2_TRANSCRIPTION_MISMATCH'})
            overall = overall and e.code == 'T2_TRANSCRIPTION_MISMATCH'
        try:
            Tm = dict(Thtml); del Tm[(5, 4, 3, 0)]
            check_transcription(T, Tm)
            trans_controls.append({'control': 'K12b_html_missing_P_term', 'observed_codes': [], 'intended_rejection': False}); overall = False
        except CheckError as e:
            trans_controls.append({'control': 'K12b_html_missing_P_term', 'expected_codes': ['T2_TRANSCRIPTION_MISMATCH'], 'observed_codes': [e.code], 'intended_rejection': e.code == 'T2_TRANSCRIPTION_MISMATCH'})
            overall = overall and e.code == 'T2_TRANSCRIPTION_MISMATCH'
        try:
            pp = list(pprime_list); pp[3], pp[4] = pp[4], pp[3]
            check_eq6(eq6, P_table, pp)
            trans_controls.append({'control': 'K12c_two_face_list_reordered', 'observed_codes': [], 'intended_rejection': False}); overall = False
        except CheckError as e:
            trans_controls.append({'control': 'K12c_two_face_list_reordered', 'expected_codes': ['T3_PPRIME_LIST_MISMATCH'], 'observed_codes': [e.code], 'intended_rejection': e.code == 'T3_PPRIME_LIST_MISMATCH'})
            overall = overall and e.code == 'T3_PPRIME_LIST_MISMATCH'
        try:
            eq6m = {k: list(v) for k, v in eq6.items()}; eq6m['P_{1}'][0] = (0, 3, 5, 3)
            check_eq6(eq6m, P_table, pprime_list)
            trans_controls.append({'control': 'K12d_eq6_P1_mutated', 'observed_codes': [], 'intended_rejection': False}); overall = False
        except CheckError as e:
            trans_controls.append({'control': 'K12d_eq6_P1_mutated', 'expected_codes': ['T3_P_MISMATCH'], 'observed_codes': [e.code], 'intended_rejection': e.code == 'T3_P_MISMATCH'})
            overall = overall and e.code == 'T3_P_MISMATCH'
        receipt['controls'] = controls + trans_controls
    receipt['clock_end_local'] = datetime.datetime.now().astimezone().isoformat(timespec='seconds')
    receipt['overall'] = 'PASS' if overall else 'FAIL'
    receipt['what_this_checker_does_not_prove'] = [
        'the written complex-analytic argument (rank bounds for arbitrary covectors, product saturation via Cauchy-Schwarz, probability identities (6)-(8), Bloch contradiction, rank-sum (11)) is assessed separately by the reviewer in review-v1.md; the finite checks here only certify its finite hypotheses',
        'no statement about AME(4,6) states outside the two explicit phase families, no global support bound, no novelty or priority assessment',
        'B2 random-phase floats are diagnostics; the arbitrary-phase isometry claim rests on B1 exact block structure',
    ]
    with open(out_path, 'x', encoding='utf-8') as f:
        json.dump(receipt, f, indent=1, sort_keys=False, ensure_ascii=False)
        f.write('\n')
    print('OVERALL', receipt['overall'])
    if 'structural_failures' in receipt:
        for k, v in receipt['structural_failures'].items():
            print('FAIL', k, v)
    for c in receipt.get('controls', []):
        print('CONTROL', 'OK ' if c['intended_rejection'] else 'BAD', c['control'], c.get('observed_codes'))
    if 'source_failure' in receipt:
        print('SOURCE FAILURE', receipt['source_failure'])
    return 0 if overall else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
