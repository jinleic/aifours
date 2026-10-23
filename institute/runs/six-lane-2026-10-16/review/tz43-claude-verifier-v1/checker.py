#!/usr/bin/env python3
"""Independent certificate checker for gcDCQS(g^n:s), FDGDD(3,4,k{m}) and mcDSQS(v).

Usage: checker.py KIND EXPECTED_V FILE EXPECTED_SHA   (KIND in gcdcqs, fdgdd, mcdsqs)

The definitions (Tan-Zhou, arXiv:2503.11934, LF 211-247 and 281-288) and the lane README
section 3 formats are checked directly; no symmetry, orbit or construction structure is
assumed. Prints one JSON object; exit 0 valid, 1 invalid certificate or arguments, 2 io or
internal error.
"""
import sys
import hashlib
import json
import itertools
import collections

KINDS = ('gcdcqs', 'fdgdd', 'mcdsqs')
TEXT_BYTES = bytes([10]) + bytes(range(32, 127))


class Fail(Exception):
    """The first failing check: invariant name and precise reason."""

    def __init__(self, invariant, reason):
        Exception.__init__(self, invariant, reason)
        self.invariant = invariant
        self.reason = reason


def chi(w):
    """chi'(w) of Steiner triple systems by (1.1); None where undefined."""
    if w % 6 == 3:
        return (w - 1) // 2
    if w % 6 == 1:
        return {7: 7, 13: 8}.get(w, (w + 1) // 2)
    return None


def canon(tok):
    """ASCII token matching 0|[1-9][0-9]* with at most 6 digits."""
    return tok.isdigit() and len(tok) <= 6 and (tok[0] != '0' or len(tok) == 1)


def key3(a, b, c):
    """Integer code of the 3-subset {a < b < c}; points are < 1024."""
    return (a << 20) | (b << 10) | c


def fmt(pts):
    return '{' + ','.join(str(p) for p in pts) + '}'


def clip(text):
    return repr(text if len(text) <= 80 else text[:80] + '...')


def check(argv, out):
    """Run every check in order; raise Fail at the first failure; fill out['counts']."""
    counts = out['counts']

    # Arguments (the file is not opened unless all are valid).
    if len(argv) != 4:
        raise Fail('args', 'expected 4 arguments KIND EXPECTED_V FILE EXPECTED_SHA, got %d' % len(argv))
    kind, ev_text, path, sha = argv
    if kind not in KINDS:
        raise Fail('args', 'KIND %s is not gcdcqs, fdgdd or mcdsqs' % clip(kind))
    out['kind'] = kind
    if not (1 <= len(ev_text) <= 4 and ev_text[0] in '123456789'
            and all(ch in '0123456789' for ch in ev_text) and 4 <= int(ev_text) <= 1000):
        raise Fail('args', 'EXPECTED_V %s does not match [1-9][0-9]{0,3} with 4 <= EXPECTED_V <= 1000'
                   % clip(ev_text))
    ev = int(ev_text)
    out['expected_v'] = ev
    if len(sha) != 64 or not all(ch in '0123456789abcdef' for ch in sha):
        raise Fail('args', 'EXPECTED_SHA %s is not exactly 64 lowercase hex digits' % clip(sha))

    # Read once; hash the bytes before decoding or parsing anything.
    try:
        with open(path, 'rb') as fh:
            data = fh.read()
    except Exception as exc:
        raise Fail('io', 'cannot open or read FILE: %s' % type(exc).__name__)
    digest = hashlib.sha256(data).hexdigest()
    out['sha256'] = digest
    if digest != sha:
        raise Fail('sha256', 'sha256 of FILE is %s, expected %s' % (digest, sha))

    # Lexical layer.
    if not data:
        raise Fail('format.encoding', 'file is empty')
    if data.translate(None, TEXT_BYTES):
        at = next(j for j, byte in enumerate(data) if byte != 10 and not 32 <= byte <= 126)
        raise Fail('format.encoding', 'LF %d: byte 0x%02x at offset %d is neither LF nor printable ASCII'
                   % (data.count(b'\n', 0, at) + 1, data[at], at))
    if data[-1] != 10:
        raise Fail('format.encoding', 'LF %d: the file does not end with LF' % (data.count(b'\n') + 1))
    recs = [(j + 1, line) for j, line in enumerate(data.decode('ascii').split('\n')[:-1])
            if line and line[0] != '#']

    def keyword(idx, name, nnum, strict):
        """recs[idx] must be the keyword record 'name' with nnum numbers; returns (LF, numbers)."""
        if idx >= len(recs):
            raise Fail('format.header', 'end of file: missing %s record' % name)
        ln, text = recs[idx]
        fields = text.split()
        if fields[:1] != [name] or len(fields) != nnum + 1:
            raise Fail('format.header', 'LF %d: expected a %s record with %d number(s), found %s'
                       % (ln, name, nnum, clip(text)))
        if text != ' '.join(fields) or not all(canon(f) for f in fields[1:]):
            raise Fail('format.header' if strict else 'format.record',
                       'LF %d: malformed %s record %s' % (ln, name, clip(text)))
        return ln, [int(f) for f in fields[1:]]

    def record(idx, what):
        if idx >= len(recs):
            raise Fail('format.record', 'end of file: missing %s record' % what)
        return recs[idx]

    def points(ln, text, q):
        """Point record of size q at LF ln: form, then range, then distinctness."""
        fields = text.split(' ')
        if len(fields) != q or not all(canon(f) for f in fields):
            raise Fail('format.record', 'LF %d: expected %d canonical points separated by single spaces, found %s'
                       % (ln, q, clip(text)))
        pts = [int(f) for f in fields]
        for p in pts:
            if p >= v:
                raise Fail('range.point', 'LF %d: point %d is not in X = {0..%d}' % (ln, p, v - 1))
        if len(set(pts)) != q:
            raise Fail('distinct_points', 'LF %d: record %s repeats a point' % (ln, clip(text)))
        return pts

    # Phase 1: preamble.
    r = t = stem_ln = None
    groups, stem = [], []
    if kind == 'gcdcqs':
        ln, (v, n, g, s) = keyword(0, 'GCDCQS', 4, False)
        counts.update(v=v, n=n, g=g, s=s)
        if v != ev:
            raise Fail('order', 'LF %d: v = %d but EXPECTED_V = %d' % (ln, v, ev))
        w = v - 1
        if (n < 2 or g < 1 or v != g * n + s or w % 6 not in (1, 3) or (v - g - s) % 2
                or chi(w) < (v - g - s) // 2):
            raise Fail('params', 'LF %d: GCDCQS %d %d %d %d needs n >= 2, g >= 1, v = gn + s, v - 1 = 1 or 3 '
                       '(mod 6), v - g - s even and t >= 0' % (ln, v, n, g, s))
        r = chi(w)
        t = r - (v - g - s) // 2
        counts.update(r=r, t=t)
        ln, (x,) = keyword(1, 'COLOURS', 1, False)
        if x != r:
            raise Fail('colours', "LF %d: COLOURS %d but r = chi'(%d) = %d" % (ln, x, w, r))
        ln, (x,) = keyword(2, 'HOLEFREE', 1, False)
        if x != t:
            raise Fail('holefree', 'LF %d: HOLEFREE %d but t = r - (v - g - s)/2 = %d' % (ln, x, t))
        keyword(3, 'GROUPS', 0, False)
        i = 4
        for _ in range(n):
            ln, text = record(i, 'group')
            groups.append((ln, points(ln, text, g)))
            i += 1
        keyword(i, 'STEM', 0, False)
        i += 1
        if s:
            stem_ln, text = record(i, 'stem')
            stem = points(stem_ln, text, s)
            i += 1
        keyword(i, 'BLOCKS', 0, False)
        i += 1
        nlab = n
    elif kind == 'fdgdd':
        if not recs:
            raise Fail('format.header', 'end of file: missing GDD34 FDGDD k m record')
        ln, text = recs[0]
        fields = text.split(' ')
        if len(fields) != 4 or fields[:2] != ['GDD34', 'FDGDD'] or not all(canon(f) for f in fields[2:]):
            raise Fail('format.header', 'LF %d: expected "GDD34 FDGDD k m", found %s' % (ln, clip(text)))
        k, m = int(fields[2]), int(fields[3])
        v = k * m
        counts.update(v=v, k=k, m=m)
        if v != ev:
            raise Fail('order', 'LF %d: v = km = %d but EXPECTED_V = %d' % (ln, v, ev))
        if k < 4 or m < 1:
            raise Fail('params', 'LF %d: GDD34 FDGDD %d %d needs k >= 4 and m >= 1' % (ln, k, m))
        keyword(1, 'GROUPS', 0, False)
        i = 2
        for _ in range(k):
            ln, text = record(i, 'group')
            groups.append((ln, points(ln, text, m)))
            i += 1
        keyword(i, 'BLOCKS', 0, False)
        i += 1
        nlab = k
    else:
        ln, (v,) = keyword(0, 'MCDSQS', 1, True)
        counts['v'] = v
        if v != ev:
            raise Fail('order', 'LF %d: v = %d but EXPECTED_V = %d' % (ln, v, ev))
        if v < 8 or v % 6 not in (2, 4):
            raise Fail('params', 'LF %d: MCDSQS %d needs v >= 8 and v = 2 or 4 (mod 6)' % (ln, v))
        w = v - 1
        r = chi(w)
        counts.update(r=r, counting_lower_bound=-(-(w * (w - 1) // 6) // (w // 3)))
        ln, (x,) = keyword(1, 'COLOURS', 1, True)
        if x != r:
            raise Fail('colours', "LF %d: COLOURS %d but r = chi'(%d) = %d" % (ln, x, w, r))
        keyword(2, 'BLOCKS', 0, True)
        i = 3
        nlab = 0

    # Phase 1: blocks, up to the first section line.
    secwords = ('POINT', 'STEMPOINT') if kind == 'gcdcqs' else ('POINT',)
    blocks = []
    while i < len(recs) and recs[i][1].partition(' ')[0] not in secwords:
        ln, text = recs[i]
        blocks.append((ln, tuple(sorted(points(ln, text, 4)))))
        i += 1
    if not blocks:
        raise Fail('format.record', '%s: BLOCKS must be followed by at least one block record'
                   % ('LF %d' % recs[i][0] if i < len(recs) else 'end of file'))
    counts['blocks'] = len(blocks)

    # Phase 1: sections [tag, point, LF, classes]; class [label, LF, [(LF, triple)]].
    clsword = {'POINT': 'FRAME' if kind == 'fdgdd' else 'CLASS', 'STEMPOINT': 'FRAME'}

    def close(sec, cls, end):
        """Checks due when class cls, and with end also section sec, is complete."""
        if cls is not None and not cls[2]:
            raise Fail('class.empty', 'LF %d: %s %d of section %s %d (LF %d) is not followed by a triple record'
                       % (cls[1], clsword[sec[0]], cls[0], sec[0], sec[1], sec[2]))
        if end and sec is not None:
            if clsword[sec[0]] == 'CLASS' and len(sec[3]) != r:
                raise Fail('class.order', 'section %s %d (LF %d) has %d CLASS line(s); CLASS 0..%d are required'
                           % (sec[0], sec[1], sec[2], len(sec[3]), r - 1))
            if not sec[3]:
                raise Fail('class.empty', 'section %s %d (LF %d) has no FRAME class' % (sec[0], sec[1], sec[2]))

    sections = []
    sec = cls = None
    stem_started = False
    while i < len(recs):
        ln, text = recs[i]
        i += 1
        if text[0].isdigit():
            if cls is None:
                raise Fail('format.record', 'LF %d: triple record %s is not inside a class' % (ln, clip(text)))
            cls[2].append((ln, tuple(points(ln, text, 3))))
            continue
        word, _, arg = text.partition(' ')
        if word in secwords:
            fits = True
        else:
            fits = word in ('CLASS', 'FRAME') and sec is not None and word == clsword[sec[0]]
        if not (fits and canon(arg)):
            raise Fail('format.record', 'LF %d: record %s does not have the form required here' % (ln, clip(text)))
        label = int(arg)
        if word in secwords:
            close(sec, cls, True)
            if word == 'POINT' and stem_started:
                raise Fail('section.order', 'LF %d: POINT %d follows the first STEMPOINT line' % (ln, label))
            if label >= v:
                raise Fail('range.point', 'LF %d: section point %d is not in X = {0..%d}' % (ln, label, v - 1))
            stem_started = stem_started or word == 'STEMPOINT'
            sec, cls = [word, label, ln, []], None
            sections.append(sec)
            continue
        close(sec, cls, False)
        if word == 'CLASS' and (label != len(sec[3]) or label >= r):
            raise Fail('class.order', 'LF %d: CLASS %d in section %s %d (LF %d), expected %s'
                       % (ln, label, sec[0], sec[1], sec[2], 'CLASS %d' % len(sec[3]) if len(sec[3]) < r
                          else 'no class after CLASS %d' % (r - 1)))
        if word == 'FRAME' and label >= nlab:
            raise Fail('class.label', 'LF %d: FRAME %d in section %s %d (LF %d); labels are 0..%d'
                       % (ln, label, sec[0], sec[1], sec[2], nlab - 1))
        cls = [label, ln, []]
        sec[3].append(cls)
    close(sec, cls, True)
    if kind == 'gcdcqs':
        counts['group_point_sections'] = sum(1 for sc in sections if sc[0] == 'POINT')
        counts['stem_point_sections'] = len(sections) - counts['group_point_sections']
    else:
        counts['point_sections'] = len(sections)

    # Phase 2a: the groups (and the stem) partition X.
    members = [grp for _, grp in groups]
    gi = [-1] * v
    if kind != 'mcdsqs':
        where = collections.defaultdict(list)
        for ln, grp in groups:
            for p in grp:
                where[p].append(ln)
        for p in stem:
            where[p].append(stem_ln)
        missing = [p for p in range(v) if p not in where]
        repeated = ['%d at LF %s' % (p, ','.join(str(z) for z in where[p]))
                    for p in sorted(where) if len(where[p]) > 1]
        if missing or repeated:
            raise Fail('partition.groups', 'GROUPS%s do not partition X = {0..%d}: %d missing point(s) %s; '
                       '%d repeated point(s) %s' % (' and STEM' if kind == 'gcdcqs' else '', v - 1, len(missing),
                                                   fmt(missing[:20]), len(repeated), '; '.join(repeated[:20])))
        for idx, grp in enumerate(members):
            for p in grp:
                gi[p] = idx
    stemset = set(stem)

    # Phase 2b: blocks are transverse (fdgdd).
    if kind == 'fdgdd':
        for ln, blk in blocks:
            for p, q in itertools.combinations(blk, 2):
                if gi[p] == gi[q]:
                    raise Fail('block.transverse', 'LF %d: block %s meets group G_%d (LF %d) in points %d and %d'
                               % (ln, fmt(blk), gi[p], groups[gi[p]][0], p, q))

    # Phase 2c: no repeated block.
    first = {}
    for ln, blk in blocks:
        if blk in first:
            raise Fail('block.duplicate', 'LF %d and LF %d: the same block %s' % (first[blk], ln, fmt(blk)))
        first[blk] = ln

    # Phase 2d: no block contains a triple inside some S u G_i (gcdcqs).
    if kind == 'gcdcqs':
        for ln, blk in blocks:
            for tri in itertools.combinations(blk, 3):
                gs = set(gi[p] for p in tri) - {-1}
                if len(gs) <= 1:
                    raise Fail('coverage.forbidden', 'LF %d: block %s contains the triple %s inside %s'
                               % (ln, fmt(blk), fmt(tri), 'S u G_%d' % min(gs) if gs else 'S'))

    # Phase 2e: every triple of the explicitly enumerated universe U lies in exactly one block.
    mult = collections.Counter()
    for _, (a, b, c, d) in blocks:
        for code in (key3(a, b, c), key3(a, b, d), key3(a, c, d), key3(b, c, d)):
            mult[code] += 1
    nu = nf = n_unc = n_over = 0
    ex_unc = ex_over = None
    for a, b, c in itertools.combinations(range(v), 3):
        if kind == 'gcdcqs':
            inside = len({gi[a], gi[b], gi[c]} - {-1}) <= 1
        elif kind == 'fdgdd':
            inside = gi[a] == gi[b] or gi[a] == gi[c] or gi[b] == gi[c]
        else:
            inside = False
        if inside:
            nf += 1
            continue
        nu += 1
        got = mult.get(key3(a, b, c), 0)
        if got == 0:
            n_unc += 1
            ex_unc = ex_unc or (a, b, c)
        elif got > 1:
            n_over += 1
            ex_over = ex_over or ((a, b, c), got)
    counts['universe_triples'] = nu
    if kind == 'gcdcqs':
        counts['forbidden_triples'] = nf
    if n_unc or n_over:
        raise Fail('coverage', '%d of the %d triples of U lie in no block%s; %d lie in more than one block%s'
                   % (n_unc, nu, ' (e.g. %s)' % fmt(ex_unc) if ex_unc else '', n_over,
                      ' (e.g. %s in %d blocks)' % (fmt(ex_over[0]), ex_over[1]) if ex_over else ''))

    # Phase 2f: the derived design at every point, pair by pair.
    der = [[] for _ in range(v)]
    for _, blk in blocks:
        for x in blk:
            der[x].append(tuple(p for p in blk if p != x))
    for x in range(v):
        # A pair {p,q} must lie in exactly one derived triple unless p or q is dead or part[p] == part[q].
        if kind == 'mcdsqs':
            part, dead = list(range(v)), set()
            rule = 'A_%d must be an STS(%d) on X \\ {%d}' % (x, v - 1, x)
        elif kind == 'fdgdd':
            part, dead = gi, set(members[gi[x]]) - {x}
            rule = 'A_%d must be a GDD(2,3,%d) of type %d^%d on X \\ G_%d' % (x, v - m, m, k - 1, gi[x])
        elif gi[x] >= 0:
            hole = (set(members[gi[x]]) | stemset) - {x}
            part, dead = [-1 if p in hole else p for p in range(v)], set()
            rule = 'A_%d must be an STS(%d,%d) with hole (G_%d u S) \\ {%d}' % (x, v - 1, len(hole), gi[x], x)
        else:
            part, dead = gi, stemset - {x}
            rule = 'A_%d must be a GDD(2,3,%d) of type %d^%d on X \\ S' % (x, v - s, g, n)
        pairs = collections.Counter()
        for a, b, c in der[x]:
            pairs[a * v + b] += 1
            pairs[a * v + c] += 1
            pairs[b * v + c] += 1
        for p, q in itertools.combinations([y for y in range(v) if y != x], 2):
            want = 0 if p in dead or q in dead or part[p] == part[q] else 1
            got = pairs.get(p * v + q, 0)
            if got != want:
                tris = [fmt(T) for T in der[x] if p in T and q in T]
                raise Fail('derived.design', 'point %d: pair {%d,%d} lies in %d derived triple(s)%s but %d required; %s'
                           % (x, p, q, got, (' ' + ', '.join(tris[:3])) if tris else '', want, rule))
    dset = [set(key3(*T) for T in der[x]) for x in range(v)]

    # Phase 2g: section labels in the required order.
    if kind == 'gcdcqs':
        required = [('POINT', p) for p in range(v) if gi[p] >= 0] + [('STEMPOINT', a) for a in stem]
    else:
        required = [('POINT', p) for p in range(v)]
    seen = {}
    for idx, (tag, x, ln, _) in enumerate(sections):
        if x in seen:
            raise Fail('section.duplicate', 'LF %d: section %s %d repeats the section of point %d at LF %d'
                       % (ln, tag, x, x, seen[x]))
        if idx >= len(required) or (tag, x) != required[idx]:
            raise Fail('section.order', 'LF %d: section %s %d where %s is required'
                       % (ln, tag, x, '%s %d' % required[idx] if idx < len(required) else 'no further section'))
        seen[x] = ln
    if len(sections) < len(required):
        raise Fail('section.missing', '%d required section(s) absent, the first being %s %d'
                   % ((len(required) - len(sections),) + required[len(sections)]))

    # Phase 2h: classes, triple record by triple record.
    if kind == 'gcdcqs':
        names = ('derived_triples_per_group_point', 'classes_per_group_point',
                 'hole_avoiding_classes_per_group_point', 'derived_triples_per_stem_point',
                 'frame_classes_per_stem_point')
    elif kind == 'fdgdd':
        names = ('derived_triples_per_point', 'frame_classes_per_point', 'frame_classes_per_label')
    else:
        names = ('derived_triples_per_point', 'classes_per_point')
    stats = dict((nm, set()) for nm in names)
    per_label, profiles, targets = {}, collections.Counter(), {}
    total = 0
    for tag, x, sln, classes in sections:
        word = clsword[tag]
        derived = dset[x]
        hole = (set(members[gi[x]]) | stemset) - {x} if kind == 'gcdcqs' and tag == 'POINT' else set()
        listed = {}
        holefree = 0
        per = [0] * nlab
        for lbl, cln, triples in classes:
            cname = '%s %d (LF %d) of section %s %d' % (word, lbl, cln, tag, x)
            if word == 'FRAME':
                if kind == 'fdgdd' and lbl == gi[x]:
                    raise Fail('class.label', 'LF %d: FRAME %d in section POINT %d (LF %d) names the group G_%d '
                               'of the section point' % (cln, lbl, x, sln, lbl))
                if (gi[x], lbl) not in targets:
                    targets[gi[x], lbl] = (set(range(v)) - set(members[lbl])
                                           - (set(members[gi[x]]) if kind == 'fdgdd' else stemset))
                target = targets[gi[x], lbl]
                tname = 'X \\ (G_%d u G_%d)' % (gi[x], lbl) if kind == 'fdgdd' else 'X \\ (S u G_%d)' % lbl
            used = {}
            for tln, tri in triples:
                code = key3(*sorted(tri))
                if code not in derived:
                    raise Fail('derived.not_block', 'LF %d: triple %s in %s: %s'
                               % (tln, fmt(tri), cname, 'it contains the section point' if x in tri
                                  else '%s is not a block' % fmt(sorted(tri + (x,)))))
                if code in listed:
                    raise Fail('derived.repeat', 'LF %d: triple %s in %s is already listed at LF %d'
                               % (tln, fmt(tri), cname, listed[code]))
                listed[code] = tln
                if word == 'FRAME':
                    outside = [p for p in tri if p not in target]
                    if outside:
                        raise Fail('frame.parallel', 'LF %d: triple %s in %s has point %d outside %s'
                                   % (tln, fmt(tri), cname, outside[0], tname))
                clash = [p for p in tri if p in used]
                if clash:
                    raise Fail('frame.parallel' if word == 'FRAME' else 'class.ppc',
                               'LF %d: triple %s in %s meets the triple at LF %d in point %d'
                               % (tln, fmt(tri), cname, used[clash[0]], clash[0]))
                for p in tri:
                    used[p] = tln
            if word == 'FRAME':
                if len(used) != len(target):
                    lack = sorted(target - set(used))
                    raise Fail('frame.parallel', '%s ends at LF %d covering %d of the %d points of %s; missing %s%s'
                               % (cname, triples[-1][0], len(used), len(target), tname, fmt(lack[:12]),
                                  ' ...' if len(lack) > 12 else ''))
                per[lbl] += 1
            elif not hole.intersection(used):
                holefree += 1
        total += sum(len(cl[2]) for cl in classes)
        if len(listed) != len(derived):
            lack = sorted(derived - set(listed))
            c0 = lack[0]
            raise Fail('derived.missing', 'section %s %d (LF %d) lists %d of the %d derived triples; %d missing, '
                       'e.g. %s' % (tag, x, sln, len(listed), len(derived), len(lack),
                                    fmt((c0 >> 20, (c0 >> 10) & 1023, c0 & 1023))))
        if kind == 'gcdcqs' and tag == 'POINT' and holefree != t:
            raise Fail('holefree_count', 'section POINT %d (LF %d): %d classes avoid the hole (G_%d u S) \\ {%d}, '
                       'but exactly t = %d are required' % (x, sln, holefree, gi[x], x, t))
        if kind == 'gcdcqs':
            if tag == 'POINT':
                stats['derived_triples_per_group_point'].add(len(derived))
                stats['classes_per_group_point'].add(len(classes))
                stats['hole_avoiding_classes_per_group_point'].add(holefree)
            else:
                stats['derived_triples_per_stem_point'].add(len(derived))
                stats['frame_classes_per_stem_point'].add(len(classes))
                per_label[str(x)] = per
        elif kind == 'fdgdd':
            stats['derived_triples_per_point'].add(len(derived))
            stats['frame_classes_per_point'].add(len(classes))
            stats['frame_classes_per_label'].update(per[j] for j in range(nlab) if j != gi[x])
        else:
            stats['derived_triples_per_point'].add(len(derived))
            stats['classes_per_point'].add(len(classes))
            profiles[' '.join(str(z) for z in sorted((len(cl[2]) for cl in classes), reverse=True))] += 1

    for nm in names:
        counts[nm] = sorted(stats[nm])
    if kind == 'gcdcqs':
        counts['frame_classes_per_label'] = per_label
    elif kind == 'mcdsqs':
        counts['class_size_profiles'] = dict(profiles)
    counts['total_listed_triples'] = total


def main():
    out = {'valid': False, 'kind': None, 'expected_v': None, 'sha256': None,
           'invariant': None, 'reason': '', 'counts': {}}
    try:
        check(sys.argv[1:], out)
        out['valid'] = True
        out['reason'] = 'all checks passed'
        code = 0
    except Fail as exc:
        out['valid'] = False
        out['invariant'], out['reason'] = exc.invariant, exc.reason
        code = 2 if exc.invariant == 'io' else 1
    except BaseException as exc:
        out['valid'] = False
        out['invariant'] = 'internal'
        try:
            out['reason'] = 'unexpected exception %s: %s' % (type(exc).__name__, str(exc)[:200])
        except BaseException:
            out['reason'] = 'unexpected exception'
        code = 2
    try:
        line = json.dumps(out, sort_keys=True)
    except BaseException:
        line = json.dumps({'valid': False, 'kind': None, 'expected_v': None, 'sha256': None,
                           'invariant': 'internal', 'reason': 'result could not be serialised',
                           'counts': {}}, sort_keys=True)
        code = 2
    sys.stdout.write(line + '\n')
    sys.stdout.flush()
    return code


if __name__ == '__main__':
    sys.exit(main())
