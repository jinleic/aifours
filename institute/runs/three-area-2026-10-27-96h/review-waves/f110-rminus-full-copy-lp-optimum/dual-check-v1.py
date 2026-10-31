#!/usr/bin/env python3
"""dual-check-v1.py -- independent reviewer controls for review manifest
f110-rminus-full-copy-lp-optimum (reviewer file prefix: dual-).

Written from scratch for this review. No author checker is imported or executed.
All inputs are pinned by SHA-256 (manifest values / audit-pinned source values).

Sections
  A  publisher text binding: Theorem 5.2 copy protocol, Remark 5.4 / Remark 3.8 text
  B  Appendix C certificate: parse 1920 PDF rows + 1920 TXT rows, bind coefficients
     by position, decode every TXT name into an expression and require equality with
     the PDF expression, classify each row semantically, check branch membership,
     verify the exact dual identity  sum c_r*row_r == H(V)  and  sum c_r*rhs_r == 1847/276
  C  primal: base original profile + three auxiliary branch profiles -> exact integer
     verification of every elemental Shannon inequality per branch, every copy
     marginal/CI equality, FDs, caps, generator symmetries, objective, 1920-row tightness
  D  F_n family: own enumeration of all disjoint substitutions mod A<->B, all n>=1,
     machine check of the written proof's E_k identity, numeric check of the recurrences
  E  numeric semantic control: random laws built by the copy protocol must annihilate
     every copy-equality row and keep every Shannon row nonnegative
"""
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import lcm, log
from pathlib import Path
import json, re, sys, time

import numpy as np

EVID = Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus')
PAPER = Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/public-sources/gurpinar-kybernetika60-2024-553-575.pdf')
HERE = Path(__file__).resolve().parent
OUT = HERE / 'dual-check-v1-result.json'

PINS = {
    'paper_pdf': (PAPER, '373e8a2567fc7de9d40d0e5fabca9655cbb7b689a162005262b4f4d432bb46d8'),
    'paper_layout': (HERE / 'dual-paper-layout.txt', '98d1dba760d383db92948026002bfa7dd95ebbe558cf1917f0c471189b528c88'),
    'annex_txt': (EVID / 'frontier-20261028-gurpinar-annexc-original.txt', 'b0bd3f614397ed11edd475efdc4acb6e8f326c6722ede71d5a08760d84578b22'),
    'annex_pdf': (EVID / 'frontier-20261028-gurpinar-annexc-original.pdf', '8befddb0faba71dbae9221956939d883946649e07a261c036ff7514dfea9ec6b'),
    'annex_layout': (EVID / 'frontier-20261028-gurpinar-annexc-pdf-layout.txt', '6ff906bb54ddf33e46d5bfcddf50ffa0680c0315e118d6530e6f13f36adc2ca5'),
    'base': (EVID / 'frontier-20261028-separator-bound-primal.json', 'aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'),
    'branch1': (EVID / 'frontier-20261028-affine-exact-branch-1.json', '1898339bb4ba63c53dbda6dff9603f82414f29645543631bc21d82d752941e37'),
    'branch2': (EVID / 'frontier-20261028-affine-exact-branch-2.json', '09981982317f1659a9a291dbbc416f77d2ac8a91eac818191048cb0ac9cd7a87'),
    'branch3': (EVID / 'frontier-20261028-affine-exact-branch-3.json', 'fd53af75dfa47e9eb03af60fb9704d89719ba8720ddf6aeb192533bcb44c4cd0'),
}
TARGET = Fraction(1847, 276)
ORIG = tuple('abcdefghij')               # vertex v  <->  ORIG[v-1]
ORIGSET = frozenset(ORIG)
AUX = {1: ("b'0",), 2: ("d'1", "e'1", "g'2"), 3: ("f'3", "g'3", "h'4")}
BRANCHVARS = {b: frozenset(ORIG) | frozenset(AUX[b]) for b in (1, 2, 3)}
ALLNAMES = ORIGSET | frozenset(n for b in AUX for n in AUX[b])

# --- R^- graph: my own transcription (Fig. 2 p570, Appendix B generators, FD rows la/lb/lf)
NBR_V = {1: {2, 3, 4, 5, 6, 7}, 2: {1, 3, 7, 9, 10}, 3: {1, 2, 4, 8, 9}, 4: {1, 3, 5, 8, 10},
         5: {1, 4, 6, 9, 10}, 6: {1, 5, 7, 8, 9}, 7: {1, 2, 6, 8, 10}, 8: {3, 4, 6, 7, 9, 10},
         9: {2, 3, 5, 6, 8}, 10: {2, 4, 5, 7, 8}}
NBR = {ORIG[v - 1]: frozenset(ORIG[u - 1] for u in nb) for v, nb in NBR_V.items()}
SIGMA_V = {1: 8, 8: 1, 2: 10, 10: 5, 5: 9, 9: 2, 3: 7, 7: 4, 4: 6, 6: 3}   # (18)(2 10 5 9)(3746)
TAU_V = {1: 1, 8: 8, 9: 9, 10: 10, 2: 5, 5: 2, 3: 6, 6: 3, 4: 7, 7: 4}      # (25)(36)(47)
SIGMA = {ORIG[v - 1]: ORIG[w - 1] for v, w in SIGMA_V.items()}
TAU = {ORIG[v - 1]: ORIG[w - 1] for v, w in TAU_V.items()}

# --- Theorem 5.2 copy protocol, my own transcription (paper variable X_v -> ORIG[v-1])
#  (a) X2'  is a X3-copy of X2  (over all others: X1,X4..X10)
#  (b) (X4'',X5'') is a X10-copy of (X4,X5) over X1,X2,X3,X6,X7,X8,X9
#      X7''' is a (X4'',X5,X10)-copy of X7 over X1,X2,X3,X4,X5'',X6,X8,X9
#  (c) (X6'''',X7'''') is a copy of (X6,X7) over X1,X2,X3,X4,X5,X8,X9,X10   (Y empty)
#      X8''''' is a (X7,X7'''')-copy of X8 over X1,X2,X3,X4,X5,X6,X6'''',X9,X10
STEPS = [
    dict(branch=1, Z=('b',), Zp=("b'0",), X=frozenset('adefghij'), Y=frozenset('c')),
    dict(branch=2, Z=('d', 'e'), Zp=("d'1", "e'1"), X=frozenset('abcfghi'), Y=frozenset('j')),
    dict(branch=2, Z=('g',), Zp=("g'2",), X=frozenset('abcdfhi') | {"e'1"}, Y=frozenset({"d'1", 'e', 'j'})),
    dict(branch=3, Z=('f', 'g'), Zp=("f'3", "g'3"), X=frozenset('abcdehij'), Y=frozenset()),
    dict(branch=3, Z=('h',), Zp=("h'4",), X=frozenset('abcdefij') | {"f'3"}, Y=frozenset({'g', "g'3"})),
]

# exact substrings that must occur in the pinned pdftotext -layout of the paper
PAPER_ANCHORS = {
    'thm52_a': "(a) X2′ be a X3 -copy of X2 ;",
    'thm52_b1': "(X4′′ , X5′′ ) be a X10 -copy of (X4 , X5 )",
    'thm52_b1_over': "over X1 , X2 , X3 , X6 , X7 , X8 , X9 ,",
    'thm52_b2': "and X7′′′ be a (X4′′ , X5 , X10 )-copy of X7",
    'thm52_b2_over': "over X1 , X2 , X3 , X4 , X5′′ , X6 , X8 , X9 ;",
    'thm52_c1': "(X6′′′′ , X7′′′′ ) be a copy of (X6 , X7 )",
    'thm52_c1_over': "over X1 , X2 , X3 , X4 , X5 , X8 , X9 , X10 ,",
    'thm52_c2': "and X8′′′′′ be a (X7 , X7′′′′ )-copy of X8",
    'thm52_c2_over': "over X1 , X2 , X3 , X4 , X5 , X6 , X6′′′′ , X9 , X10 ;",
    'thm52_set_a': "X1 , X2 , X2′ , X3 , X4 , X5 , X6 , X7 , X8 , X9 , X10 ,",
    'thm52_set_b': "X1 , X2 , X3 , X4 , X4′′ , X5 , X5′′ , X6 , X7 , X7′′′ , X8 , X9 , X10 ,",
    'thm52_set_c': "X1 , X2 , X3 , X4 , X5 , X6 , X6′′′′ , X7 , X7′′′′ , X8 , X8′′′′′ , X9 , X10 ;",
    'thm52_sym': "3. the symmetry constraints.",
    'thm52_value': "The optimal value of this linear program is 1847/276",
    'remark38': "Remark 3.8. In [1] non-Shannon-type inequalities were added to such a linear program",
    'remark38b': "instead of item (ii) (the copy lemma constraints).",
    'remark54': "Remark 5.4. Note that in the linear programs constructed in the proofs above, unlike",
    'remark54b': "type inequality involving both X2′ and X4′′ in the first linear program and none involving",
    'lemma210_copy': "Z ′ is called a Y -copy of Z over X or simply Y -copy of Z when X consist of all the",
    'lemma210_ci': "I(Z ′ : Y, Z|X) = 0.",
    'cor37_caps': "hXi ≤ 1 for every i ∈ J1, nK",
    'appB': "and τ = (25)(36)(47). Aut(R− ) = ⟨σ, τ ⟩.",
    'appB_sigma': "σ = (18)(2 10 5 9)(3746)",
    'appC': "https://archive.org/details/anx-c-rmns-1847ovr-276crtfcte.",
}


def now():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z')


def pin(key):
    path, digest = PINS[key]
    raw = path.read_bytes()
    got = sha256(raw).hexdigest()
    if got != digest:
        raise SystemExit(f'HASH MISMATCH {key}: {got}')
    return raw


def norm(name):
    return name.replace('\u2019', "'").replace('\u2032', "'").strip()


def mask_of(names, order):
    m = 0
    for n in names:
        m |= 1 << order.index(n)
    return m


def names_of(mask, order):
    if mask >> len(order):
        raise SystemExit(f'mask {mask} exceeds order {order}')
    return frozenset(order[i] for i in range(len(order)) if mask >> i & 1)


# ----------------------------------------------------------------------------- A
def section_a(layout):
    rep = {}
    missing = [k for k, s in PAPER_ANCHORS.items() if s not in layout]
    rep['paper_anchor_missing'] = missing
    # graph sanity
    edges = set()
    for v, nb in NBR_V.items():
        for u in nb:
            if v not in NBR_V[u]:
                raise SystemExit(f'graph not symmetric {v},{u}')
            edges.add(frozenset((u, v)))
    rep['edges'] = len(edges)
    rep['edge_3_4_present'] = frozenset((3, 4)) in edges
    rep['edge_9_10_absent'] = frozenset((9, 10)) not in edges
    rep['degrees'] = {v: len(nb) for v, nb in NBR_V.items()}
    for name, p in (('sigma', SIGMA_V), ('tau', TAU_V)):
        for v, nb in NBR_V.items():
            if {p[u] for u in nb} != NBR_V[p[v]]:
                raise SystemExit(f'{name} is not an automorphism at {v}')
    # generate the group
    ident = {v: v for v in range(1, 11)}
    group = {tuple(ident[v] for v in range(1, 11))}
    frontier = [ident]
    while frontier:
        nxt = []
        for g in frontier:
            for p in (SIGMA_V, TAU_V):
                h = {v: p[g[v]] for v in range(1, 11)}
                key = tuple(h[v] for v in range(1, 11))
                if key not in group:
                    group.add(key); nxt.append(h)
        frontier = nxt
    rep['group_order'] = len(group)
    # protocol consistency: X ∪ Y ∪ Z == variables existing in branch before step
    existing = {b: set(ORIG) for b in (1, 2, 3)}
    for k, st in enumerate(STEPS):
        b = st['branch']
        union = st['X'] | st['Y'] | set(st['Z'])
        if union != existing[b]:
            raise SystemExit(f'step {k}: X∪Y∪Z != existing variables: {sorted(union ^ existing[b])}')
        if set(st['Zp']) & existing[b]:
            raise SystemExit(f'step {k}: Zp already exists')
        existing[b] |= set(st['Zp'])
    for b in (1, 2, 3):
        if existing[b] != set(BRANCHVARS[b]):
            raise SystemExit(f'branch {b} variable set mismatch')
    rep['branch_variable_counts'] = {b: len(BRANCHVARS[b]) for b in (1, 2, 3)}
    rep['union_coordinates'] = sum(2 ** len(BRANCHVARS[b]) - 1 for b in (1, 2, 3)) - 2 * 1023
    full17 = 17 + 136 * 2 ** 15
    three = sum(len(BRANCHVARS[b]) + (len(BRANCHVARS[b]) * (len(BRANCHVARS[b]) - 1) // 2) * 2 ** (len(BRANCHVARS[b]) - 2) for b in (1, 2, 3))
    rep['elemental_rows_17_variable_full'] = full17
    rep['elemental_rows_three_branch_union_with_original_repeats'] = three
    rep['elemental_rows_three_branch_distinct'] = three - 2 * (10 + 45 * 256)
    rep['elemental_rows_omitted_cross_branch'] = full17 - (three - 2 * (10 + 45 * 256))
    return rep, group


# ----------------------------------------------------------------------------- B
TERM_RE = re.compile(r'([+-]?)\s*H\{([^}]*)\}')
REL_RE = re.compile(r'(>=|<=|=)\s*(-?\d+(?:/\d+)?)\s*$')


def parse_expr(expr):
    m = REL_RE.search(expr)
    if not m:
        raise SystemExit(f'no relation in row: {expr!r}')
    rel, rhs = m.group(1), Fraction(m.group(2))
    body = expr[:m.start()]
    terms = {}
    pos = 0
    count = 0
    for t in TERM_RE.finditer(body):
        gap = body[pos:t.start()].strip()
        if gap:
            raise SystemExit(f'unparsed text {gap!r} in {expr!r}')
        pos = t.end()
        sign = -1 if t.group(1) == '-' else 1
        names = [norm(x) for x in t.group(2).split('.')]
        if any(n not in ALLNAMES for n in names) or len(set(names)) != len(names) or not names:
            raise SystemExit(f'bad set {names} in {expr!r}')
        key = frozenset(names)
        if key in terms:
            raise SystemExit(f'duplicate set in row {expr!r}')
        terms[key] = sign
        count += 1
    if body[pos:].strip():
        raise SystemExit(f'trailing text in {expr!r}')
    return terms, rel, rhs, count


def parse_pdf_rows(text):
    rows, buf, others = [], [], []
    for raw in text.split('\n'):
        s = raw.strip()
        if not s:
            continue
        if s.startswith('with coefficient'):
            coef = Fraction(s[len('with coefficient'):].strip())
            if not buf:
                raise SystemExit('coefficient without expression')
            terms, rel, rhs, n = parse_expr(' '.join(buf))
            rows.append(dict(terms=terms, rel=rel, rhs=rhs, coef=coef, nterms=n, text=' '.join(buf)))
            buf = []
        elif s.startswith(('H{', '-', '+')):
            buf.append(s)
        else:
            others.append(s)
    if buf:
        raise SystemExit('dangling expression')
    return rows, others


def parse_txt(text):
    lines = [l for l in text.split('\n') if l.strip()]
    if lines[0] != 'Objective Value = 1847/276':
        raise SystemExit('TXT header')
    out = []
    for l in lines[1:]:
        name, sep, val = l.partition(' = ')
        if sep != ' = ':
            raise SystemExit(f'TXT line {l!r}')
        out.append((name, Fraction(val)))
    return out


def cmi_terms(A, B, K):
    t = defaultdict(int)
    t[frozenset(A | K)] += 1
    t[frozenset(B | K)] += 1
    t[frozenset(A | B | K)] -= 1
    if K:
        t[frozenset(K)] -= 1
    return {k: v for k, v in t.items() if v}


def decode_txt_name(name):
    """Independent decoding of a TXT row name into (terms, rel, rhs)."""
    orders = {b: sorted(BRANCHVARS[b]) for b in (1, 2, 3)}
    m = re.fullmatch(r'csti(\d+)set(\d+)/(\d+)/(\d+)', name)
    if m:
        b = int(m.group(1)) + 1; o = orders[b]
        p, q, k = (names_of(int(x), o) for x in m.group(2, 3, 4))
        if len(p) != 1 or len(q) != 1 or p & k or q & k or p == q:
            raise SystemExit(f'bad cmi name {name}')
        return cmi_terms(p, q, k), '>=', Fraction(0), 'cmi'
    m = re.fullmatch(r'csti(\d+)set(\d+)/(\d+)', name)
    if m:
        b = int(m.group(1)) + 1; o = orders[b]
        if m.group(2) != m.group(3):
            raise SystemExit(f'bad ce name {name}')
        p = names_of(int(m.group(2)), o)
        full = frozenset(o)
        return {full: 1, full - p: -1}, '>=', Fraction(0), 'ce'
    m = re.fullmatch(r'sym(\d+)/(\d+)/(\d+)', name)
    if m:
        g = [SIGMA, TAU][int(m.group(1))]
        moved = [v for v in ORIG if g[v] != v]
        fixed = [v for v in ORIG if g[v] == v]
        S = names_of(int(m.group(2)), moved) | names_of(int(m.group(3)), fixed)
        T = frozenset(g[x] for x in S)
        return {S: 1, T: -1} if S != T else {}, '=', Fraction(0), 'sym'
    m = re.fullmatch(r'copy(\d)1at(\d+)n(\d+)', name)
    if m:
        st = STEPS[int(m.group(1))]
        zo = list(st['Z']); xo = sorted(st['X'])
        T = names_of(int(m.group(2)), zo)
        S = names_of(int(m.group(3)), xo)
        Tp = frozenset(st['Zp'][zo.index(z)] for z in T)
        return {S | T: 1, S | Tp: -1}, '=', Fraction(0), 'copy_marg'
    m = re.fullmatch(r'copy(\d)2', name)
    if m:
        st = STEPS[int(m.group(1))]
        X, Y, Z, Zp = st['X'], st['Y'], frozenset(st['Z']), frozenset(st['Zp'])
        return cmi_terms(Zp, Y | Z, X), '=', Fraction(0), 'copy_ci'
    m = re.fullmatch(r'l([abf])(2?)', name)
    if m:
        v = m.group(1)
        if m.group(2):
            return {frozenset([v]): 1}, '<=', Fraction(1), 'cap'
        return {NBR[v]: 1, NBR[v] | {v}: -1}, '>=', Fraction(0), 'fd'
    raise SystemExit(f'unknown TXT name {name}')


def is_cmi(terms):
    pos = [s for s, c in terms.items() if c == 1]
    neg = [s for s, c in terms.items() if c == -1]
    if len(pos) != 2 or len(neg) not in (1, 2) or len(terms) != len(pos) + len(neg):
        return None
    if len(neg) == 2:
        K, U = sorted(neg, key=len)
    else:
        K, U = frozenset(), neg[0]
    P1, P2 = pos
    if not (K < P1 and K < P2 and P1 | P2 == U and P1 & P2 == K):
        return None
    return P1 - K, P2 - K, K


def classify(row, group):
    terms, rel, rhs, coef = row['terms'], row['rel'], row['rhs'], row['coef']
    names = frozenset().union(*terms)
    branches = [b for b in (1, 2, 3) if names <= BRANCHVARS[b]]
    info = dict(branches=branches, kind=None, elemental=None, coef_sign_ok=None)
    if rel == '<=':
        if rhs == 1 and len(terms) == 1 and next(iter(terms.values())) == 1 and len(next(iter(terms))) == 1 and next(iter(terms)) <= ORIGSET:
            info['kind'] = 'cap'; info['coef_sign_ok'] = coef >= 0
        return info
    if rhs != 0:
        return info
    if rel == '>=':
        info['coef_sign_ok'] = coef <= 0
        c = is_cmi(terms)
        if c:
            A, B, K = c
            info['kind'] = 'cmi'; info['elemental'] = len(A) == 1 and len(B) == 1
            return info
        if len(terms) == 2:
            (S, cs), (T, ct) = terms.items()
            if cs == -1:
                S, T = T, S
            if T < S:
                info['kind'] = 'condent'
                info['elemental'] = len(S - T) == 1 and any(S == BRANCHVARS[b] for b in branches)
                return info
            if S < T and len(T - S) == 1:
                v = next(iter(T - S))
                if v in ORIGSET and S == NBR[v]:
                    info['kind'] = 'fd'; info['elemental'] = True
                    return info
        return info
    if rel == '=':
        if len(terms) == 2:
            (S, cs), (T, ct) = terms.items()
            if cs == -1:
                S, T = T, S
            if S <= ORIGSET and T <= ORIGSET:
                hits = [g for g in group if frozenset(ORIG[g[ORIG.index(x)] - 1] for x in S) == T]
                if hits:
                    info['kind'] = 'sym'
                    info['elemental'] = any(g in (SIGMA_KEY, TAU_KEY) for g in hits)
                    return info
            for k, st in enumerate(STEPS):
                Z, Zp, X = frozenset(st['Z']), st['Zp'], st['X']
                for side1, side2 in ((S, T), (T, S)):
                    Tz = side1 & Z
                    if not Tz:
                        continue
                    Sx = side1 - Tz
                    if not Sx <= X:
                        continue
                    Tp = frozenset(Zp[st['Z'].index(z)] for z in Tz)
                    if side2 == Sx | Tp:
                        info['kind'] = 'copy_marg'; info['elemental'] = True; info['step'] = k
                        return info
        for k, st in enumerate(STEPS):
            X, Y, Z, Zp = st['X'], st['Y'], frozenset(st['Z']), frozenset(st['Zp'])
            if terms == cmi_terms(Zp, Y | Z, X):
                info['kind'] = 'copy_ci'; info['elemental'] = True; info['step'] = k
                return info
    return info


SIGMA_KEY = tuple(SIGMA_V[v] for v in range(1, 11))
TAU_KEY = tuple(TAU_V[v] for v in range(1, 11))


def section_b(group):
    rep = {}
    layout = pin('annex_layout').decode('utf-8')
    txt = pin('annex_txt').decode('utf-8')
    rows, others = parse_pdf_rows(layout)
    rep['pdf_rows'] = len(rows)
    rep['pdf_H_tokens_total'] = layout.count('H{')
    rep['pdf_H_tokens_consumed'] = sum(r['nterms'] for r in rows)
    rep['pdf_other_lines'] = len(others)
    rep['pdf_other_lines_nonnumeric'] = [o for o in others if not o.isdigit()]
    txtrows = parse_txt(txt)
    rep['txt_rows'] = len(txtrows)
    if len(rows) != 1920 or len(txtrows) != 1920:
        raise SystemExit('row count')
    # coefficient binding by position
    mism = [(k, n, str(c), str(rows[k]['coef'])) for k, (n, c) in enumerate(txtrows) if c != rows[k]['coef']]
    rep['coefficient_mismatches_by_position'] = len(mism)
    # TXT name decoding vs PDF expression
    decode_mism = []
    decoded_kinds = Counter()
    for k, (n, c) in enumerate(txtrows):
        terms, rel, rhs, kind = decode_txt_name(n)
        decoded_kinds[kind] += 1
        if terms != rows[k]['terms'] or rel != rows[k]['rel'] or rhs != rows[k]['rhs']:
            decode_mism.append((k, n, rows[k]['text']))
    rep['txt_name_decoding_mismatches'] = len(decode_mism)
    rep['txt_name_decoding_examples'] = decode_mism[:5]
    rep['txt_decoded_kinds'] = dict(decoded_kinds)
    # semantic classification of PDF rows (name-independent)
    kinds = Counter(); unrec = []; signbad = []; nobranch = []; nonelem = Counter(); per_branch = Counter(); multi = 0
    for k, r in enumerate(rows):
        info = classify(r, group)
        r['info'] = info
        if info['kind'] is None:
            unrec.append((k, r['text'], str(r['coef'])))
        kinds[info['kind']] += 1
        if info['coef_sign_ok'] is False:
            signbad.append((k, r['text'], str(r['coef'])))
        if not info['branches']:
            nobranch.append((k, r['text']))
        if info['elemental'] is False:
            nonelem[info['kind']] += 1
        for b in info['branches']:
            per_branch[b] += 1
        if len(info['branches']) > 1:
            multi += 1
    rep['row_kinds'] = dict(kinds)
    rep['unrecognized_rows'] = unrec
    rep['coefficient_sign_violations'] = signbad
    rep['rows_outside_every_branch'] = nobranch
    rep['non_elemental_but_valid'] = dict(nonelem)
    rep['rows_inside_branch'] = {b: per_branch[b] for b in (1, 2, 3)}
    rep['rows_original_only'] = multi
    rep['rows_by_branch_signature'] = {str(k): v for k, v in Counter(tuple(r['info']['branches']) for r in rows).items()}
    rep['copy_rows_by_step'] = {f"{k[0]}:step{k[1]}": v for k, v in Counter((r['info']['kind'], r['info'].get('step')) for r in rows if r['info']['kind'] in ('copy_marg', 'copy_ci')).items()}
    # dual identity
    total = defaultdict(Fraction)
    rhs_total = Fraction(0)
    for r in rows:
        for s, c in r['terms'].items():
            total[s] += r['coef'] * c
        rhs_total += r['coef'] * r['rhs']
    total = {s: v for s, v in total.items() if v}
    rep['dual_lhs_identity'] = {'.'.join(sorted(s)): str(v) for s, v in total.items()}
    rep['dual_lhs_is_H_V'] = total == {ORIGSET: Fraction(1)}
    rep['dual_rhs_sum'] = str(rhs_total)
    rep['dual_rhs_is_target'] = rhs_total == TARGET
    rep['cap_multipliers'] = {next(iter(r['terms'])).__iter__().__next__(): str(r['coef']) for r in rows if r['info']['kind'] == 'cap'}
    rep['distinct_coefficient_denominator_lcm'] = lcm(*(r['coef'].denominator for r in rows))
    return rep, rows


# ----------------------------------------------------------------------------- C
def load_profile(key, field):
    doc = json.loads(pin(key))
    out = {}
    for e in doc[field]:
        k = frozenset(norm(x) for x in e['entropy_variables'])
        if k in out:
            raise SystemExit(f'duplicate coordinate {sorted(k)} in {key}')
        out[k] = Fraction(e['value'])
    return doc, out


def section_c(rows):
    rep = {}
    base_doc, base = load_profile('base', 'primal_values')
    originals = {k: v for k, v in base.items() if k <= ORIGSET}
    rep['base_total_coordinates'] = len(base)
    rep['base_original_coordinates'] = len(originals)
    if len(originals) != 1023:
        raise SystemExit('original coordinate count')
    rep['objective'] = str(originals[ORIGSET])
    rep['objective_is_target'] = originals[ORIGSET] == TARGET
    rep['singletons'] = {v: str(originals[frozenset([v])]) for v in ORIG}
    rep['balance_gap_hV_minus_two_thirds_sum'] = str(originals[ORIGSET] - Fraction(2, 3) * sum(originals[frozenset([v])] for v in ORIG))
    branch_reports = {}
    arrays = {}
    for b in (1, 2, 3):
        t0 = time.monotonic()
        doc, aux = load_profile(f'branch{b}', 'auxiliary_values')
        if doc['branch'] != b or frozenset(norm(x) for x in doc['variables']) != BRANCHVARS[b]:
            raise SystemExit(f'branch {b} labels')
        bad = [k for k in aux if not (k <= BRANCHVARS[b]) or not (k & frozenset(AUX[b]))]
        if bad:
            raise SystemExit(f'branch {b} bad aux keys {bad[:3]}')
        merged = dict(originals); merged.update(aux)
        order = sorted(BRANCHVARS[b]); n = len(order)
        if len(merged) != 2 ** n - 1:
            raise SystemExit(f'branch {b} merged count {len(merged)}')
        scale = lcm(*(v.denominator for v in merged.values()))
        h = np.zeros(2 ** n, dtype=np.int64)
        for k, v in merged.items():
            h[mask_of(k, order)] = int(v * scale)
        if int(np.abs(h).max()) * 4 >= 2 ** 62:
            raise SystemExit('int64 range')
        if (h < 0).any():
            raise SystemExit('negative coordinate')
        full = 2 ** n - 1
        allm = np.arange(2 ** n, dtype=np.int64)
        br = dict(aux_coordinates=len(aux), scale=scale, n=n)
        # elemental conditional entropies
        ce = [int(h[full] - h[full ^ (1 << i)]) for i in range(n)]
        if min(ce) < 0:
            raise SystemExit(f'branch {b} conditional entropy violation')
        # elemental CMIs
        cmi_count = 0; cmi_min = None; tight_cmi = 0
        for i, j in combinations(range(n), 2):
            bi, bj = 1 << i, 1 << j
            K = allm[(allm & (bi | bj)) == 0]
            val = h[K | bi] + h[K | bj] - h[K | bi | bj] - h[K]
            if (val < 0).any():
                kk = int(K[np.flatnonzero(val < 0)[0]])
                raise SystemExit(f'branch {b} CMI violation i={order[i]} j={order[j]} K={sorted(names_of(kk, order))}')
            cmi_count += len(val); tight_cmi += int((val == 0).sum())
            m = int(val.min()); cmi_min = m if cmi_min is None else min(cmi_min, m)
        br['elemental_shannon_rows'] = n + cmi_count
        br['elemental_cmi_rows'] = cmi_count
        br['elemental_cmi_tight'] = tight_cmi
        br['elemental_condent_tight'] = sum(1 for x in ce if x == 0)
        # copy equalities
        ceq = 0; ci = 0
        for k, st in enumerate(STEPS):
            if st['branch'] != b:
                continue
            xm = mask_of(st['X'], order); zm = mask_of(st['Z'], order); zpm = mask_of(st['Zp'], order); ym = mask_of(st['Y'], order)
            # all submasks of xm
            S = xm
            subs = []
            while True:
                subs.append(S)
                if S == 0:
                    break
                S = (S - 1) & xm
            subs = np.array(subs, dtype=np.int64)
            for tsel in range(1, 2 ** len(st['Z'])):
                tz = sum(1 << order.index(st['Z'][i]) for i in range(len(st['Z'])) if tsel >> i & 1)
                tp = sum(1 << order.index(st['Zp'][i]) for i in range(len(st['Z'])) if tsel >> i & 1)
                if (h[subs | tz] != h[subs | tp]).any():
                    raise SystemExit(f'branch {b} copy marginal violation step {k}')
                ceq += len(subs)
            v = int(h[xm | zpm] + h[xm | ym | zm] - h[xm | ym | zm | zpm] - h[xm])
            if v != 0:
                raise SystemExit(f'branch {b} copy CI violation step {k}: {v}')
            ci += 1
        br['copy_marginal_equalities'] = ceq
        br['copy_ci_equalities'] = ci
        br['copy_equalities_total'] = ceq + ci
        # FDs, caps, symmetry (originals; identical across branches but checked on each array)
        for v in ORIG:
            nm = mask_of(NBR[v], order)
            if h[nm | (1 << order.index(v))] != h[nm]:
                raise SystemExit(f'FD violation {v}')
            if h[1 << order.index(v)] > scale:
                raise SystemExit(f'cap violation {v}')
        sym = 0
        for g in (SIGMA, TAU):
            for S in range(1, 1024):
                names = names_of(S, list(ORIG))
                if h[mask_of(names, order)] != h[mask_of([g[x] for x in names], order)]:
                    raise SystemExit('symmetry violation')
                sym += 1
        br['fd_checked'] = 10; br['caps_checked'] = 10; br['generator_symmetry_equalities'] = sym
        br['objective_scaled_ok'] = int(h[mask_of(ORIG, order)]) == int(TARGET * scale)
        # aux singleton values (info)
        br['aux_singletons'] = {a: str(merged[frozenset([a])]) for a in AUX[b]}
        br['elapsed_s'] = round(time.monotonic() - t0, 2)
        branch_reports[b] = br
        arrays[b] = (h, order, scale)
    rep['branches'] = branch_reports
    # 1920 rows tight
    tight = 0; slack_rows = []
    per_branch_tight = Counter()
    for k, r in enumerate(rows):
        bs = r['info']['branches']
        if not bs:
            raise SystemExit('row outside branches at tightness check')
        for b in bs:
            h, order, scale = arrays[b]
            val = sum(c * int(h[mask_of(s, order)]) for s, c in r['terms'].items())
            if val != int(r['rhs'] * scale):
                slack_rows.append((k, r['text'], b, str(Fraction(val, scale))))
            else:
                per_branch_tight[b] += 1
        tight += 1
    rep['source_rows_evaluated'] = tight
    rep['source_rows_not_tight'] = slack_rows[:10]
    rep['source_rows_not_tight_count'] = len(slack_rows)
    rep['source_rows_tight_per_branch_incl_original_only'] = {b: per_branch_tight[b] for b in (1, 2, 3)}
    # old partial aux coordinates in base vs new branch values (information only)
    diffs = {}
    for b in (1, 2, 3):
        _, aux = load_profile(f'branch{b}', 'auxiliary_values')
        shared = [k for k in aux if k in base]
        diffs[b] = dict(shared=len(shared), different=sum(1 for k in shared if aux[k] != base[k]))
    rep['old_partial_aux_in_base_vs_branch'] = diffs
    return rep, originals


# ----------------------------------------------------------------------------- D
def ek_identity_check():
    """E_k identity of the written F_n proof, as exact linear algebra over the
    31-dimensional entropy space of atoms A,B,C,D,S modulo the two CI conditions."""
    atoms = 'ABCDS'
    subsets = [frozenset(c) for r in range(1, 6) for c in combinations(atoms, r)]
    idx = {s: i for i, s in enumerate(subsets)}

    def H(s):
        v = [Fraction(0)] * 31
        if s:
            v[idx[frozenset(s)]] = Fraction(1)
        return v

    def add(*vs):
        out = [Fraction(0)] * 31
        for sign, v in vs:
            for i in range(31):
                out[i] += sign * v[i]
        return out

    def I(x, y, w=''):
        x, y, w = set(x), set(y), set(w)
        return add((1, H(x | w)), (1, H(y | w)), (-1, H(x | y | w)), (-1, H(w)))

    lhs = add((1, I('A', 'B', 'S')), (1, I('S', 'AB', 'C')), (-1, I('A', 'B')), (1, I('A', 'B', 'D')), (1, I('C', 'D')))
    rhs = add((1, I('A', 'B', 'SD')), (1, I('S', 'D', 'A')), (1, I('S', 'D', 'B')), (1, I('C', 'D', 'S')), (1, I('S', 'AB', 'CD')))
    diff = add((1, lhs), (-1, rhs))
    c1 = I('S', 'D', 'AB'); c2 = I('S', 'D', 'ABC')
    # solve diff = x*c1 + y*c2 exactly
    best = None
    for x in [Fraction(k, 1) for k in range(-3, 4)]:
        for y in [Fraction(k, 1) for k in range(-3, 4)]:
            if add((1, diff), (-x, c1), (-y, c2)) == [Fraction(0)] * 31:
                best = (str(x), str(y))
    return dict(identity_holds_modulo_CI=best is not None, combination=best,
                diff_nonzero_entries={'.'.join(sorted(subsets[i])): str(diff[i]) for i in range(31) if diff[i]})


def entropy_np(p, axes_keep, nvars):
    axes = tuple(i for i in range(nvars) if i not in axes_keep)
    m = p.sum(axis=axes) if axes else p
    m = m[m > 0]
    return float(-(m * np.log(m)).sum())


def extend_law(p, vars_, X, Z, Zp, rng=None):
    """Attach Z' ~ P(Z|X) independent of everything else given X (copy lemma kernel)."""
    nv = len(vars_)
    keepXZ = tuple(i for i, v in enumerate(vars_) if v in X or v in Z)
    keepX = tuple(i for i, v in enumerate(vars_) if v in X)
    pxz = p.sum(axis=tuple(i for i in range(nv) if i not in keepXZ), keepdims=True)
    px = p.sum(axis=tuple(i for i in range(nv) if i not in keepX), keepdims=True)
    q = pxz / px
    zidx = [vars_.index(z) for z in Z]
    perm = [i for i in range(nv) if i not in zidx] + zidx
    qt = np.transpose(q, perm)
    newshape = [1 if i in zidx else q.shape[i] for i in range(nv)] + [q.shape[i] for i in zidx]
    qn = qt.reshape(newshape)
    pn = p.reshape(list(p.shape) + [1] * len(Z)) * qn
    return pn, list(vars_) + list(Zp)


def fn_numeric_proof_check(rng):
    """Random laws on (A,B,C,D); attach R_1..R_{n+1} i.i.d. ~ P(C|A,B) given (A,B),
    independent of (C,D); verify the proof's recurrences and the decomposition of F_n."""
    worst = 0.0
    for trial in range(6):
        n = 1 + trial % 4
        k_alpha = 2 if trial < 4 else 3
        p = rng.random((k_alpha,) * 4) + 0.05; p /= p.sum()
        vars_ = ['A', 'B', 'C', 'D']
        for j in range(n + 1):
            p, vars_ = extend_law(p, vars_, X={'A', 'B'}, Z=['C'], Zp=[f'R{j + 1}'])
        nv = len(vars_)
        def Hs(*names):
            return entropy_np(p, tuple(vars_.index(x) for x in names), nv)
        def I(x, y, w=()):
            return Hs(*x, *w) + Hs(*y, *w) - Hs(*x, *y, *w) - (Hs(*w) if w else 0.0)
        A, B, C, D = ('A',), ('B',), ('C',), ('D',)
        a = I(A, B, C); Delta = I(A, B) - I(A, B, D) - I(C, D); d = I(A, C, B) + I(B, C, A)
        Fn = (n + 1) * a - n * Delta + n * (n + 1) * d / 2
        S = lambda j: tuple(f'R{i}' for i in range(1, j + 1))
        h = Hs('C', 'A', 'B') - Hs('A', 'B')
        a_ = [I(A, B, S(j)) for j in range(0, n + 2)]
        B_ = [Hs(f'R{j + 1}', *S(j)) - (Hs(*S(j)) if j else 0.0) - h for j in range(0, n + 1)]
        d_ = [(Hs(f'R{j + 1}', 'A', *S(j)) - Hs('A', *S(j))) + (Hs(f'R{j + 1}', 'B', *S(j)) - Hs('B', *S(j))) - 2 * h for j in range(0, n + 1)]
        errs = [abs(a_[1] - a), abs(d_[0] - d)]
        errs += [abs(a_[j + 1] - (a_[j] - B_[j] + d_[j])) for j in range(0, n + 1)]
        errs += [abs(I(S(k), ('A', 'B'), C) - sum(B_[1:k + 1])) for k in range(1, n + 1)]
        E = [a_[k] + I(S(k), ('A', 'B'), C) - Delta for k in range(1, n + 1)]
        for k in range(1, n + 1):
            Sk = S(k)
            rhs = I(A, B, Sk + D) + I(Sk, D, A) + I(Sk, D, B) + I(C, D, Sk) + I(Sk, ('A', 'B'), C + D)
            errs.append(abs(E[k - 1] - rhs))
            errs.append(abs(E[k - 1] - (a_[1] + sum(d_[1:k]) + B_[k] - Delta)))
        decomp = sum(E) + a_[n + 1] + sum((n - j + 1) * (d - d_[j]) for j in range(1, n + 1))
        errs.append(abs(Fn - decomp))
        errs += [max(0.0, -x) for x in B_ + d_ + E + [a_[n + 1]] + [d - x for x in d_]]
        errs.append(max(0.0, -Fn))
        worst = max(worst, max(errs))
    return worst


def fn_scan(originals):
    t0 = time.monotonic()
    order = list(ORIG)
    scale = lcm(*(v.denominator for v in originals.values()))
    h = np.zeros(1024, dtype=np.int64)
    for k, v in originals.items():
        h[mask_of(k, order)] = int(v * scale)
    if int(h.max()) * 64 * 10 ** 4 >= 2 ** 62:
        raise SystemExit('fn range')

    def I(a, b, w):
        return h[a | w] + h[b | w] - h[a | b | w] - h[w]

    pairs = [(A, B) for A in range(1, 1024) for B in range(A + 1, 1024) if not A & B]
    digit_cache = {}
    checked = 0; min_twice = None; argmin = None; max_n = 0; min_n1 = None
    for A, B in pairs:
        rest = [i for i in range(10) if not (A | B) >> i & 1]
        r = len(rest)
        if r not in digit_cache:
            codes = np.arange(4 ** r, dtype=np.int64)
            digit_cache[r] = [(codes >> (2 * k)) & 3 for k in range(r)]
        digs = digit_cache[r]
        C = np.zeros(4 ** r, dtype=np.int64); D = C.copy(); Z = C.copy()
        for k, bit in enumerate(rest):
            C = C | ((digs[k] == 1).astype(np.int64) << bit)
            D = D | ((digs[k] == 2).astype(np.int64) << bit)
            Z = Z | ((digs[k] == 3).astype(np.int64) << bit)
        ok = (C > 0) & (D > 0)
        C, D, Z = C[ok], D[ok], Z[ok]
        if not len(C):
            continue
        checked += len(C)
        a = I(A, B, C | Z)
        Delta = I(A, B, Z) - I(A, B, D | Z) - I(C, D, Z)
        d = I(A, C, B | Z) + I(B, C, A | Z)
        c = a - Delta
        if (a < 0).any() or (d < 0).any():
            raise SystemExit('negative Shannon component on original profile')
        lin = (d == 0) & (c < 0)
        if lin.any():
            j = int(np.flatnonzero(lin)[0])
            raise SystemExit(f'F_n fails for large n at A={A} B={B} C={int(C[j])} D={int(D[j])} Z={int(Z[j])}')
        n1 = np.ones(len(C), dtype=np.int64)
        pos = d > 0
        n1[pos] = np.maximum(1, np.floor_divide(-(2 * c[pos] + d[pos]), 2 * d[pos]))
        n2 = n1 + 1
        max_n = max(max_n, int(n2.max()))
        twoF = lambda n: 2 * a + 2 * n * c + n * (n + 1) * d
        q = np.minimum(np.minimum(twoF(n1), twoF(n2)), twoF(np.ones_like(n1)))
        m = int(q.min())
        f1 = int(twoF(np.ones_like(n1)).min())
        min_n1 = f1 if min_n1 is None else min(min_n1, f1)
        if min_twice is None or m < min_twice:
            min_twice = m; j = int(np.argmin(q))
            argmin = dict(A=A, B=B, C=int(C[j]), D=int(D[j]), Z=int(Z[j]), n=int(n1[j] if twoF(n1)[j] <= twoF(n2)[j] else n2[j]))
        if m < 0:
            raise SystemExit(f'F_n violation {argmin}')
    expected = (6 ** 10 - 4 * 5 ** 10 + 6 * 4 ** 10 - 4 * 3 ** 10 + 2 ** 10) // 2
    rep = dict(scale=scale, substitutions_checked=checked, expected_inclusion_exclusion=expected,
               count_matches=checked == expected, min_twice_F_scaled=min_twice,
               min_twice_F1_scaled=min_n1, argmin={k: (sorted(names_of(v, order)) if k in 'ABCDZ' else v) for k, v in argmin.items()},
               largest_vertex_neighbour_n=max_n, elapsed_s=round(time.monotonic() - t0, 2))
    # the all-order text's example substitution, evaluated on THIS profile for information
    A, B, C, D, Z = (mask_of(names_of(0, order) | frozenset(ORIG[v - 1] for v in vs), order) for vs in ([2], [10], [6], [3, 4], [1, 5, 8, 9]))
    a = int(I(A, B, C | Z)); Delta = int(I(A, B, Z) - I(A, B, D | Z) - I(C, D, Z)); d = int(I(A, C, B | Z) + I(B, C, A | Z))
    rep['example_A2_B10_C6_D34_Z1589'] = dict(a=str(Fraction(a, scale)), Delta=str(Fraction(Delta, scale)), d=str(Fraction(d, scale)),
                                             F12=str(Fraction(13 * a - 12 * Delta + 78 * d, scale)))
    return rep


# ----------------------------------------------------------------------------- E
def section_e(rows, rng):
    rep = {}
    laws = {}
    for b in (1, 2, 3):
        vars_ = list(ORIG)
        p = rng.random((2,) * 10) + 0.02; p /= p.sum()
        for st in STEPS:
            if st['branch'] == b:
                p, vars_ = extend_law(p, vars_, st['X'], list(st['Z']), list(st['Zp']))
        laws[b] = (p, vars_)
    worst_eq = 0.0; worst_ineq = 0.0; n_eq = 0; n_ineq = 0; cache = {}
    for r in rows:
        kind = r['info']['kind']
        if kind not in ('copy_marg', 'copy_ci', 'cmi', 'condent'):
            continue
        b = r['info']['branches'][0]
        p, vars_ = laws[b]
        val = 0.0
        for s, c in r['terms'].items():
            key = (b, s)
            if key not in cache:
                cache[key] = entropy_np(p, tuple(vars_.index(x) for x in s), len(vars_))
            val += c * cache[key]
        if kind.startswith('copy'):
            worst_eq = max(worst_eq, abs(val)); n_eq += 1
        else:
            worst_ineq = max(worst_ineq, -val); n_ineq += 1
    rep['copy_rows_checked'] = n_eq; rep['copy_rows_max_abs_value'] = worst_eq
    rep['shannon_rows_checked'] = n_ineq; rep['shannon_rows_max_negative_part'] = worst_ineq
    # the three FD rows would NOT vanish on a random law (they need the FD structure); sanity: show they are strictly negative
    fdvals = []
    for r in rows:
        if r['info']['kind'] == 'fd':
            p, vars_ = laws[1]
            fdvals.append(sum(c * entropy_np(p, tuple(vars_.index(x) for x in s), len(vars_)) for s, c in r['terms'].items()))
    rep['fd_rows_on_random_law'] = fdvals
    return rep


def main():
    t0 = time.monotonic()
    rep = {'native_clock_start': now(), 'script': 'dual-check-v1.py'}
    for key in PINS:
        pin(key)
    rep['pins_verified'] = {k: v[1] for k, v in PINS.items()}
    layout = pin('paper_layout').decode('utf-8')
    rep['A_paper_and_protocol'], group = section_a(layout)
    rep['B_certificate'], rows = section_b(group)
    rep['C_primal'], originals = section_c(rows)
    rng = np.random.default_rng(20261028)
    rep['D_Fn'] = dict(Ek_identity=ek_identity_check(), numeric_proof_recurrence_worst_error=fn_numeric_proof_check(rng), scan=fn_scan(originals))
    rep['E_random_law_control'] = section_e(rows, rng)
    rep['elapsed_s'] = round(time.monotonic() - t0, 2)
    rep['native_clock_end'] = now()
    OUT.write_text(json.dumps(rep, indent=1, default=str) + '\n', encoding='utf-8')
    print(json.dumps(rep, indent=1, default=str))


if __name__ == '__main__':
    main()
