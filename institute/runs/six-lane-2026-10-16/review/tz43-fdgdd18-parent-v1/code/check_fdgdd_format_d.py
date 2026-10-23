#!/usr/bin/env python3
r"""tz43-fdgdd18 parent definition-first checker for FDGDD(3,4,k{m}) certificates in lane Format D.

Stdlib only. Authored by the parent verification desk Tz43FdgddParentCheck; no lane code imported or read.

Usage:
  python3 -B check_fdgdd_format_d.py CERT [--out NEW.json] [--k 5] [--m 18]
Exit status: 0 PASS, 1 FAIL, 2 checker exception, 64 usage error.
With --out the full JSON report is written to a NEW file (exclusive create) and a one-line summary is
printed; without --out the JSON report is printed.

Definitions implemented, quoted from Tan-Zhou arXiv:2503.11934v1, pinned local text
mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt
(sha256 df52a8f11a46974eef129fa115bb3305831f7c8edc3e2102e4fd22c64c3c8164), LF line numbers:
  LF 48-59   GDD(t,K,v) (X,G,B): "(1) B is a family of subsets of X (called blocks), each having
             cardinality in K; (2) each block of B intersects any given group in at most one point;
             (3) each t-subset of X from t distinct groups is contained in exactly one block."
  LF 69-70   "A partial parallel class (PPC) of Y is a collection of pairwise disjoint blocks contained
             in Y. A parallel class (PC) of Y is a PPC that partitions Y."
  LF 237-239 "A Kirkman frame ... KF(m^v), is a GDD(2,3,mv) of type m^v (X,G,B) such that the block set
             B can be partitioned into subsets P_r, r in R, each P_r being a PC of X \ G for some group
             G in G."
  LF 241-242 "Let (X,G,A) be a GDD(3,4,mv) of type m^v. For any x in X, let A_x = {A\{x} : x in A,
             A in A}. Then the derived design (X\G, G\{G}, A_x) is a GDD(2,3,m(v-1)) of type m^(v-1)."
             (G = the group containing x.)
  LF 246-247 "FDGDD(3,4,v{m}) to denote a GDD(3,4,mv) of type m^v whose derived design at every point
             is a KF(m^(v-1))."
Format D (lane README section 3, LF 126-131), read with a strict canonical grammar:
  ASCII only; characters [0-9A-Z space LF]; LF line ends; final LF; no blank lines, comments, tabs or CR;
  tokens separated by single spaces; integers 0 or [1-9][0-9]*;
  "GDD34 FDGDD k m" / "GROUPS" / k group lines / "BLOCKS" / block lines of 4 integers /
  for x = 0..km-1 in order: "POINT x", then one or more classes "FRAME j" each followed by >= 1 triple
  lines of 3 integers. j is the index (GROUPS order) of the group missed by the class.
No symmetry, construction route or producer output is assumed.
"""
import collections
import hashlib
import itertools
import json
import math
import os
import platform
import re
import resource
import sys
import time
import traceback

TARGET_KIND = 'FDGDD'
INT_RE = re.compile(r'(?:0|[1-9][0-9]*)\Z')
ALLOWED_CHARS = frozenset('0123456789 \nABCDEFGHIJKLMNOPQRSTUVWXYZ')
MAX_EXAMPLES = 5

# (name, level, description); level 'definition' = part of the FDGDD/KF definition itself,
# 'format' = Format D bookkeeping or a count forced by the definition (consistency check).
CHECK_SPECS = [
    ('FORMAT', 'format', 'file parses under the strict canonical Format D grammar'),
    ('C01_HEADER', 'format', 'header is "GDD34 FDGDD k m" with (k, m) equal to the target'),
    ('C02_GROUPS_SHAPE', 'definition', 'k group lines, each with exactly m labels (type m^k)'),
    ('C03_POINT_LABEL_RANGE', 'format', 'every point label (groups, blocks, POINT headers, triples) lies in 0..km-1'),
    ('C04_GROUPS_PARTITION', 'definition', 'the declared groups partition X = {0,...,km-1}'),
    ('C05_BLOCK_IS_4_SUBSET', 'definition', 'every block line lists 4 distinct points (K = {4}, LF 52)'),
    ('C06_BLOCK_TRANSVERSE', 'definition', 'every block meets each group in at most one point (LF 53)'),
    ('C07_BLOCK_NOT_IN_GROUP_PAIR_UNION', 'definition', 'no block lies inside the union of two groups (redundant with C06; checked separately)'),
    ('C08_BLOCKS_DISTINCT', 'definition', 'no block occurs twice'),
    ('C09_BLOCK_COUNT', 'format', 'number of block lines equals C(k,3) m^3 / 4 (forced by C10)'),
    ('C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE', 'definition', 'multiset of 3-subsets of blocks equals the set of all transverse 3-subsets (exact universe equality, LF 59)'),
    ('D01_DERIVED_COUNT', 'format', 'at every x, |A_x| = C(k-1,2) m^2 / 3 (forced)'),
    ('D02_DERIVED_IS_GDD_2_3', 'definition', 'at every x, (X\\G_x, G\\{G_x}, A_x) is a GDD(2,3,(k-1)m) of type m^(k-1): derived triples are transverse 3-subsets of X\\G_x and every cross pair lies in exactly one (exact universe equality)'),
    ('F01_POINT_SECTIONS', 'format', 'exactly one POINT section for each x, in order 0..km-1'),
    ('F02_FRAME_LABEL_VALID', 'format', 'every FRAME label j is a group index 0..k-1 other than the group of x'),
    ('F03_FRAME_TRIPLE_IS_3_SUBSET', 'definition', 'every listed triple consists of 3 distinct points'),
    ('F04_CLASSES_PARTITION_DERIVED', 'definition', 'at every x the listed triples over all classes equal A_x as multisets (each derived triple exactly once, nothing else)'),
    ('F05_CLASS_PAIRWISE_DISJOINT', 'definition', 'the triples of each class are pairwise disjoint'),
    ('F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP', 'definition', 'each class is a PC of (X\\G_x)\\G for some group G != G_x (KF, LF 237-239)'),
    ('F07_FRAME_LABEL_MATCHES_MISSED_GROUP', 'format', 'the declared FRAME label equals the group the class misses'),
    ('F08_CLASS_COUNT', 'format', 'exactly (k-1)m/2 classes at every x (forced)'),
    ('F09_DECLARED_MISSED_GROUP_COUNTS', 'format', 'at every x each group other than G_x is the declared label of exactly m/2 classes (forced)'),
]


class FormatError(Exception):
    def __init__(self, lineno, msg):
        Exception.__init__(self, msg)
        self.lineno = lineno
        self.msg = msg


class Checks(object):
    def __init__(self):
        self.order = [s[0] for s in CHECK_SPECS]
        self.data = collections.OrderedDict()
        for name, level, desc in CHECK_SPECS:
            self.data[name] = collections.OrderedDict(
                [('level', level), ('description', desc), ('status', 'NOT_RUN'),
                 ('violations', 0), ('examples', [])])

    def violation(self, name, example):
        d = self.data[name]
        d['violations'] += 1
        if len(d['examples']) < MAX_EXAMPLES:
            d['examples'].append(example)

    def close(self, name):
        d = self.data[name]
        d['status'] = 'PASS' if d['violations'] == 0 else 'FAIL'

    def status(self, name):
        return self.data[name]['status']

    def with_status(self, status):
        return [n for n in self.order if self.data[n]['status'] == status]


def parse_format_d(data):
    """Strict parse; returns (kind, k, m, groups, blocks, sections) with 1-based LF line numbers."""
    try:
        text = data.decode('ascii')
    except UnicodeDecodeError as e:
        raise FormatError(None, 'non-ASCII byte at offset %d' % e.start)
    bad = set(text) - ALLOWED_CHARS
    if bad:
        raise FormatError(None, 'disallowed characters %r' % sorted(bad)[:5])
    if not text.endswith('\n'):
        raise FormatError(None, 'file does not end with LF')
    lines = text.split('\n')
    lines.pop()
    n = len(lines)
    if n == 0:
        raise FormatError(1, 'empty file')

    def toks(idx):
        line = lines[idx]
        if line == '':
            raise FormatError(idx + 1, 'blank line')
        t = line.split(' ')
        if '' in t:
            raise FormatError(idx + 1, 'leading, trailing or repeated space')
        return t

    def ints(idx, t):
        out = []
        for s in t:
            if INT_RE.match(s) is None:
                raise FormatError(idx + 1, 'non-canonical integer token %r' % s[:20])
            out.append(int(s))
        return out

    t = toks(0)
    if len(t) != 4 or t[0] != 'GDD34':
        raise FormatError(1, 'header must be "GDD34 KIND k m"')
    kind = t[1]
    k, m = ints(0, t[2:])
    if not (1 <= k <= 64 and 1 <= m <= 4096):
        raise FormatError(1, 'k or m outside parser limits')
    i = 1
    if i >= n or toks(i) != ['GROUPS']:
        raise FormatError(i + 1, 'expected GROUPS')
    i += 1
    groups = []
    for _ in range(k):
        if i >= n:
            raise FormatError(i + 1, 'missing group line')
        groups.append((i + 1, ints(i, toks(i))))
        i += 1
    if i >= n or toks(i) != ['BLOCKS']:
        raise FormatError(i + 1, 'expected BLOCKS')
    i += 1
    blocks = []
    while i < n:
        t = toks(i)
        if t[0] == 'POINT':
            break
        if len(t) != 4:
            raise FormatError(i + 1, 'block line must have 4 tokens')
        blocks.append((i + 1, ints(i, t)))
        i += 1
    sections = []
    while i < n:
        t = toks(i)
        if len(t) != 2 or t[0] != 'POINT':
            raise FormatError(i + 1, 'expected "POINT x"')
        x = ints(i, t[1:])[0]
        sec_line = i + 1
        i += 1
        classes = []
        while i < n:
            t = toks(i)
            if t[0] == 'POINT':
                break
            if len(t) != 2 or t[0] != 'FRAME':
                raise FormatError(i + 1, 'expected "FRAME j"')
            j = ints(i, t[1:])[0]
            cls_line = i + 1
            i += 1
            triples = []
            while i < n:
                t = toks(i)
                if t[0] == 'POINT' or t[0] == 'FRAME':
                    break
                if len(t) != 3:
                    raise FormatError(i + 1, 'triple line must have 3 tokens')
                triples.append((i + 1, ints(i, t)))
                i += 1
            classes.append((cls_line, j, triples))
        sections.append((sec_line, x, classes))
    return kind, k, m, groups, blocks, sections


def classify_class(union, disjoint, invalid, Y, gx, group_sets, grp, k):
    """Return (status, missed_group). status 'OK' iff the class is a PC of Y minus one whole group."""
    if invalid:
        return 'HAS_INVALID_TRIPLE', None
    if not disjoint:
        return 'OVERLAP', None
    if not union <= Y:
        return 'MEETS_GROUP_OF_X', None
    missing = Y - union
    for gj in range(k):
        if gj != gx and missing == group_sets[gj]:
            return 'OK', gj
    for gj in range(k):
        if gj != gx and group_sets[gj] < missing:
            return 'NOT_FULL', gj
    missed = set(grp[p] for p in missing)
    if len(missed) >= 2:
        return 'SPANS_TWO_OR_MORE_MISSING_GROUPS', None
    if len(missed) == 1:
        return 'MISSES_PART_OF_ONE_GROUP', None
    return 'COVERS_ALL_OF_X_MINUS_GX', None


def check_certificate(data, k_t, m_t):
    C = Checks()
    stats = collections.OrderedDict()
    try:
        kind, k, m, groups, blocks, sections = parse_format_d(data)
    except FormatError as e:
        C.violation('FORMAT', {'line': e.lineno, 'reason': e.msg})
        C.close('FORMAT')
        return C, stats
    C.close('FORMAT')
    stats['parsed'] = collections.OrderedDict([
        ('kind', kind), ('k', k), ('m', m), ('group_lines', len(groups)),
        ('block_lines', len(blocks)), ('point_sections', len(sections)),
        ('frame_headers', sum(len(s[2]) for s in sections)),
        ('triple_lines', sum(len(c[2]) for s in sections for c in s[2]))])

    if kind != TARGET_KIND or k != k_t or m != m_t:
        C.violation('C01_HEADER', {'line': 1, 'kind': kind, 'k': k, 'm': m,
                                   'expected': [TARGET_KIND, k_t, m_t]})
        C.close('C01_HEADER')
        return C, stats
    C.close('C01_HEADER')
    v = k * m

    # C03: label range everywhere
    for ln, g in groups:
        for p in g:
            if p >= v:
                C.violation('C03_POINT_LABEL_RANGE', {'line': ln, 'label': p, 'where': 'GROUPS'})
    for ln, b in blocks:
        for p in b:
            if p >= v:
                C.violation('C03_POINT_LABEL_RANGE', {'line': ln, 'label': p, 'where': 'BLOCKS'})
    for ln, x, classes in sections:
        if x >= v:
            C.violation('C03_POINT_LABEL_RANGE', {'line': ln, 'label': x, 'where': 'POINT header'})
        for cl, j, triples in classes:
            for tl, t in triples:
                for p in t:
                    if p >= v:
                        C.violation('C03_POINT_LABEL_RANGE', {'line': tl, 'label': p, 'where': 'triple'})
    C.close('C03_POINT_LABEL_RANGE')

    # C02 / C04: groups as declared
    for ln, g in groups:
        if len(g) != m:
            C.violation('C02_GROUPS_SHAPE', {'line': ln, 'size': len(g), 'expected': m})
    C.close('C02_GROUPS_SHAPE')
    grp = [-1] * v
    for gi, (ln, g) in enumerate(groups):
        for p in g:
            if p >= v:
                C.violation('C04_GROUPS_PARTITION', {'line': ln, 'label': p, 'reason': 'out of range'})
            elif grp[p] != -1:
                C.violation('C04_GROUPS_PARTITION', {'line': ln, 'label': p,
                                                     'reason': 'label declared twice', 'first_group': grp[p]})
            else:
                grp[p] = gi
    for p in range(v):
        if grp[p] == -1:
            C.violation('C04_GROUPS_PARTITION', {'label': p, 'reason': 'point in no group'})
    C.close('C04_GROUPS_PARTITION')
    if C.status('C02_GROUPS_SHAPE') != 'PASS' or C.status('C04_GROUPS_PARTITION') != 'PASS':
        return C, stats
    group_sets = [frozenset(g) for ln, g in groups]
    stats['groups'] = collections.OrderedDict([
        ('v', v), ('sizes', [len(g) for ln, g in groups]),
        ('declared_as_consecutive_runs', all(sorted(g) == list(range(gi * m, gi * m + m))
                                              for gi, (ln, g) in enumerate(groups)))])

    # C05-C08: blocks
    good_blocks = []
    for ln, b in blocks:
        if any(p >= v for p in b):
            continue
        if len(set(b)) != 4:
            C.violation('C05_BLOCK_IS_4_SUBSET', {'line': ln, 'block': b})
            continue
        gs = set(grp[p] for p in b)
        if len(gs) != 4:
            C.violation('C06_BLOCK_TRANSVERSE', {'line': ln, 'block': b, 'groups': [grp[p] for p in b]})
        if len(gs) <= 2:
            C.violation('C07_BLOCK_NOT_IN_GROUP_PAIR_UNION', {'line': ln, 'block': b, 'groups': sorted(gs)})
        good_blocks.append((ln, tuple(sorted(b))))
    for name in ('C05_BLOCK_IS_4_SUBSET', 'C06_BLOCK_TRANSVERSE', 'C07_BLOCK_NOT_IN_GROUP_PAIR_UNION'):
        C.close(name)
    first_line = {}
    for ln, b in good_blocks:
        if b in first_line:
            C.violation('C08_BLOCKS_DISTINCT', {'line': ln, 'block': list(b), 'first_line': first_line[b]})
        else:
            first_line[b] = ln
    C.close('C08_BLOCKS_DISTINCT')

    n_tt = math.comb(k, 3) * m ** 3
    expected_blocks = n_tt // 4
    if len(blocks) != expected_blocks or n_tt % 4 != 0:
        C.violation('C09_BLOCK_COUNT', {'block_lines': len(blocks), 'expected': expected_blocks})
    C.close('C09_BLOCK_COUNT')

    vv = v * v

    def key3(a, b, c):
        return a * vv + b * v + c

    def dec3(key):
        return [key // vv, (key // v) % v, key % v]

    # C10: exact universe equality for transverse triples
    universe = set()
    for ga, gb, gc in itertools.combinations(range(k), 3):
        for a in groups[ga][1]:
            for b in groups[gb][1]:
                for c in groups[gc][1]:
                    s = sorted((a, b, c))
                    universe.add(key3(s[0], s[1], s[2]))
    tri_count = collections.Counter()
    for ln, b in good_blocks:
        for t in itertools.combinations(b, 3):
            tri_count[key3(t[0], t[1], t[2])] += 1
    uncovered = universe.difference(tri_count)
    over = [t for t, c in tri_count.items() if c > 1]
    outside = [t for t in tri_count if t not in universe]
    exact = (len(universe) == n_tt and set(tri_count) == universe
             and (max(tri_count.values()) if tri_count else 0) == 1)
    if uncovered or over or outside or not exact:
        C.violation('C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE', collections.OrderedDict([
            ('uncovered_transverse_triples', len(uncovered)),
            ('multiply_covered_triples', len(over)),
            ('non_transverse_triples_in_blocks', len(outside)),
            ('examples_uncovered', [dec3(t) for t in sorted(uncovered)[:3]]),
            ('examples_multiply_covered', [dec3(t) for t in sorted(over)[:3]]),
            ('examples_non_transverse', [dec3(t) for t in sorted(outside)[:3]])]))
    C.close('C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE')
    stats['blocks'] = collections.OrderedDict([
        ('block_lines', len(blocks)), ('expected', expected_blocks),
        ('distinct_blocks', len(first_line)),
        ('transverse_triple_universe', len(universe)), ('expected_universe', n_tt),
        ('distinct_triples_in_blocks', len(tri_count)),
        ('triple_incidences_in_blocks', sum(tri_count.values())),
        ('max_triple_multiplicity', max(tri_count.values()) if tri_count else 0),
        ('uncovered', len(uncovered)), ('multiply_covered', len(over)),
        ('non_transverse_in_blocks', len(outside)), ('exact_universe_equality', exact)])

    # D01/D02: derived designs
    derived = [collections.Counter() for _ in range(v)]
    for ln, b in good_blocks:
        for x in b:
            r = [p for p in b if p != x]
            derived[x][key3(r[0], r[1], r[2])] += 1
    n_der = math.comb(k - 1, 2) * m * m // 3
    pair_universe = []
    for gx in range(k):
        others = [gi for gi in range(k) if gi != gx]
        s = set()
        for ga, gb in itertools.combinations(others, 2):
            for a in groups[ga][1]:
                for b in groups[gb][1]:
                    s.add(a * v + b if a < b else b * v + a)
        pair_universe.append(s)
    der_sizes = collections.Counter()
    d02_points = 0
    for x in range(v):
        gx = grp[x]
        cnt = derived[x]
        total = sum(cnt.values())
        der_sizes[total] += 1
        if total != n_der:
            C.violation('D01_DERIVED_COUNT', {'x': x, 'derived_triples': total, 'expected': n_der})
        pc = collections.Counter()
        bad = 0
        for key, c in cnt.items():
            a, b, cc = dec3(key)
            gs = (grp[a], grp[b], grp[cc])
            if gx in gs or len(set(gs)) != 3:
                bad += c
            pc[a * v + b] += c
            pc[a * v + cc] += c
            pc[b * v + cc] += c
        pu = pair_universe[gx]
        missing_pairs = pu.difference(pc)
        multi = [pk for pk, c in pc.items() if c > 1]
        extra = [pk for pk in pc if pk not in pu]
        ok = (bad == 0 and not missing_pairs and not multi and not extra
              and len(pu) == math.comb(k - 1, 2) * m * m and set(pc) == pu)
        if not ok:
            d02_points += 1
            C.violation('D02_DERIVED_IS_GDD_2_3', collections.OrderedDict([
                ('x', x), ('non_transverse_or_own_group_derived_triples', bad),
                ('cross_pairs_uncovered', len(missing_pairs)), ('pairs_multiply_covered', len(multi)),
                ('non_cross_pairs', len(extra))]))
    C.close('D01_DERIVED_COUNT')
    C.close('D02_DERIVED_IS_GDD_2_3')
    stats['derived'] = collections.OrderedDict([
        ('expected_triples_per_point', n_der),
        ('triples_per_point_histogram', dict((str(a), b) for a, b in sorted(der_sizes.items()))),
        ('cross_pairs_per_point', math.comb(k - 1, 2) * m * m),
        ('points_failing_D02', d02_points)])

    # F01-F09: frames
    sec_by_x = {}
    order = []
    for ln, x, classes in sections:
        order.append(x)
        if x >= v:
            C.violation('F01_POINT_SECTIONS', {'line': ln, 'reason': 'section for out-of-range point', 'x': x})
            continue
        if x in sec_by_x:
            C.violation('F01_POINT_SECTIONS', {'line': ln, 'reason': 'second section for point', 'x': x,
                                               'first_line': sec_by_x[x][0]})
        else:
            sec_by_x[x] = (ln, classes)
    if order != list(range(v)):
        C.violation('F01_POINT_SECTIONS', collections.OrderedDict([
            ('reason', 'POINT sections are not exactly 0..v-1 in order'),
            ('sections', len(order)),
            ('missing_points', [x for x in range(v) if x not in sec_by_x][:10])]))
    C.close('F01_POINT_SECTIONS')

    n_cls = (k - 1) * m // 2
    pc_triples = (k - 2) * m // 3
    per_group = m // 2
    Y_by_group = [frozenset(p for p in range(v) if grp[p] != gx) for gx in range(k)]
    status_hist = collections.Counter()
    size_hist = collections.Counter()
    classes_per_point = collections.Counter()
    actual_counts = collections.OrderedDict()
    declared_counts = collections.OrderedDict()
    for x in range(v):
        gx = grp[x]
        Y = Y_by_group[gx]
        classes = sec_by_x[x][1] if x in sec_by_x else []
        classes_per_point[len(classes)] += 1
        listed = collections.Counter()
        declared = collections.Counter()
        actual = collections.Counter()
        for cl, j, triples in classes:
            if j >= k or j == gx:
                C.violation('F02_FRAME_LABEL_VALID', {'x': x, 'line': cl, 'label': j, 'group_of_x': gx})
            declared[j] += 1
            valid = []
            invalid = 0
            for tl, t in triples:
                if any(p >= v for p in t):
                    invalid += 1
                    continue
                if len(set(t)) != 3:
                    C.violation('F03_FRAME_TRIPLE_IS_3_SUBSET', {'x': x, 'line': tl, 'triple': t})
                    invalid += 1
                    continue
                s = sorted(t)
                valid.append(s)
                listed[key3(s[0], s[1], s[2])] += 1
            size_hist[len(triples)] += 1
            pts = collections.Counter(p for s in valid for p in s)
            union = frozenset(pts)
            disjoint = all(c == 1 for c in pts.values())
            if not disjoint:
                C.violation('F05_CLASS_PAIRWISE_DISJOINT', collections.OrderedDict([
                    ('x', x), ('line', cl), ('label', j),
                    ('shared_points', sorted(p for p, c in pts.items() if c > 1)[:5])]))
            st, gj = classify_class(union, disjoint, invalid, Y, gx, group_sets, grp, k)
            status_hist[st] += 1
            if st != 'OK':
                C.violation('F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP', collections.OrderedDict([
                    ('x', x), ('line', cl), ('label', j), ('status', st), ('triples', len(triples)),
                    ('covered_points', len(union)),
                    ('missing_by_group', dict((str(g), len((Y - union) & group_sets[g]))
                                              for g in range(k) if g != gx))]))
            else:
                actual[gj] += 1
                if gj != j:
                    C.violation('F07_FRAME_LABEL_MATCHES_MISSED_GROUP',
                                {'x': x, 'line': cl, 'declared': j, 'missed_group': gj})
        der = derived[x]
        if listed != der:
            not_derived = sum(c for t, c in listed.items() if t not in der)
            repeated = sum(c - der[t] for t, c in listed.items() if t in der and c > der[t])
            unlisted = sum(c - listed[t] for t, c in der.items() if listed[t] < c)
            C.violation('F04_CLASSES_PARTITION_DERIVED', collections.OrderedDict([
                ('x', x), ('listed_not_derived', not_derived), ('listed_extra_repeats', repeated),
                ('derived_not_listed', unlisted), ('listed_total', sum(listed.values())),
                ('derived_total', sum(der.values()))]))
        if len(classes) != n_cls:
            C.violation('F08_CLASS_COUNT', {'x': x, 'classes': len(classes), 'expected': n_cls})
        want = collections.Counter(dict((g, per_group) for g in range(k) if g != gx))
        if declared != want:
            C.violation('F09_DECLARED_MISSED_GROUP_COUNTS', {'x': x, 'declared_label_counts':
                                                            dict((str(a), b) for a, b in sorted(declared.items()))})
        actual_counts[str(x)] = [None if g == gx else actual[g] for g in range(k)]
        declared_counts[str(x)] = [None if g == gx else declared[g] for g in range(k)]
    for name in ('F02_FRAME_LABEL_VALID', 'F03_FRAME_TRIPLE_IS_3_SUBSET', 'F04_CLASSES_PARTITION_DERIVED',
                 'F05_CLASS_PAIRWISE_DISJOINT', 'F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP',
                 'F07_FRAME_LABEL_MATCHES_MISSED_GROUP', 'F08_CLASS_COUNT', 'F09_DECLARED_MISSED_GROUP_COUNTS'):
        C.close(name)
    patterns = collections.Counter(tuple(sorted(c for c in vec if c is not None))
                                   for vec in actual_counts.values())
    stats['frames'] = collections.OrderedDict([
        ('expected_classes_per_point', n_cls), ('expected_triples_per_class', pc_triples),
        ('expected_classes_missing_each_other_group', per_group),
        ('classes_per_point_histogram', dict((str(a), b) for a, b in sorted(classes_per_point.items()))),
        ('triples_per_class_histogram', dict((str(a), b) for a, b in sorted(size_hist.items()))),
        ('class_status_histogram', dict(sorted(status_hist.items()))),
        ('actual_missed_group_count_patterns', dict((','.join(map(str, a)), b) for a, b in sorted(patterns.items()))),
        ('actual_missed_group_counts_by_point', actual_counts),
        ('declared_label_counts_by_point', declared_counts)])
    return C, stats


DEFINITION_CORE = ['C02_GROUPS_SHAPE', 'C04_GROUPS_PARTITION', 'C05_BLOCK_IS_4_SUBSET', 'C06_BLOCK_TRANSVERSE',
                   'C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE', 'D02_DERIVED_IS_GDD_2_3',
                   'F03_FRAME_TRIPLE_IS_3_SUBSET', 'F04_CLASSES_PARTITION_DERIVED',
                   'F05_CLASS_PAIRWISE_DISJOINT', 'F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP']


def own_sha256():
    try:
        with open(os.path.abspath(__file__), 'rb') as f:
            return hashlib.sha256(f.read()).hexdigest()
    except (NameError, OSError):
        return None


def main(argv):
    args = list(argv[1:])
    out = None
    k_t, m_t = 5, 18
    cert = None
    while args:
        a = args.pop(0)
        if a == '--out' and args:
            out = args.pop(0)
        elif a == '--k' and args:
            k_t = int(args.pop(0))
        elif a == '--m' and args:
            m_t = int(args.pop(0))
        elif cert is None and not a.startswith('--'):
            cert = a
        else:
            sys.stderr.write('usage: check_fdgdd_format_d.py CERT [--out NEW.json] [--k K] [--m M]\n')
            return 64
    if cert is None:
        sys.stderr.write('usage: check_fdgdd_format_d.py CERT [--out NEW.json] [--k K] [--m M]\n')
        return 64
    t0 = time.perf_counter()
    c0 = time.process_time()
    started = time.strftime('%Y-%m-%d %H:%M:%S %Z')
    with open(cert, 'rb') as f:
        data = f.read()
    report = collections.OrderedDict()
    report['checker'] = collections.OrderedDict([
        ('name', 'tz43-fdgdd18 parent definition-first checker (Format D, FDGDD)'),
        ('path', os.path.abspath(__file__)), ('sha256', own_sha256())])
    report['input'] = collections.OrderedDict([
        ('path', os.path.abspath(cert)), ('sha256', hashlib.sha256(data).hexdigest()),
        ('bytes', len(data)), ('lf_count', data.count(b'\n'))])
    report['target'] = collections.OrderedDict([('kind', TARGET_KIND), ('k', k_t), ('m', m_t)])
    report['python'] = collections.OrderedDict([
        ('executable', sys.executable), ('version', platform.python_version()),
        ('optimize_flag', sys.flags.optimize), ('dont_write_bytecode', sys.flags.dont_write_bytecode),
        ('platform', sys.platform)])
    code = 0
    try:
        C, stats = check_certificate(data, k_t, m_t)
        failed = C.with_status('FAIL')
        not_run = C.with_status('NOT_RUN')
        verdict = 'PASS' if not failed and not not_run else 'FAIL'
        core_ok = all(C.status(n) == 'PASS' for n in DEFINITION_CORE)
        report['verdict'] = verdict
        report['definition_core_checks'] = DEFINITION_CORE
        report['definition_core_verdict'] = 'PASS' if core_ok else 'FAIL'
        report['failed_checks'] = failed
        report['first_failed_check'] = failed[0] if failed else None
        report['not_run_checks'] = not_run
        report['checks'] = C.data
        report['stats'] = stats
        code = 0 if verdict == 'PASS' else 1
    except Exception:
        report['verdict'] = 'FAIL'
        report['failed_checks'] = ['CHECKER_EXCEPTION']
        report['first_failed_check'] = 'CHECKER_EXCEPTION'
        report['exception'] = traceback.format_exc()
        code = 2
    report['timing'] = collections.OrderedDict([
        ('started_at', started), ('finished_at', time.strftime('%Y-%m-%d %H:%M:%S %Z')),
        ('wall_seconds', round(time.perf_counter() - t0, 4)),
        ('cpu_seconds', round(time.process_time() - c0, 4))])
    ru = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report['max_rss_bytes'] = ru if sys.platform == 'darwin' else ru * 1024
    text = json.dumps(report, indent=1) + '\n'
    if out is None:
        sys.stdout.write(text)
    else:
        with open(out, 'x') as f:
            f.write(text)
        sys.stdout.write('%s %s sha256=%s failed=%s wall=%.2fs rss=%d\n' % (
            report['verdict'], os.path.basename(cert), report['input']['sha256'],
            ','.join(report['failed_checks']) or '-', report['timing']['wall_seconds'],
            report['max_rss_bytes']))
    return code


if __name__ == '__main__':
    sys.exit(main(sys.argv))
