#!/usr/bin/env python3
"""Intended-reason control fixtures for the pinned FDGDD(3,4,5{18}) candidate (parent desk Tz43FdgddParentCheck).

Usage: python3 -B make_controls.py PINNED_CERT OUTDIR
Each fixture is a full copy of the pinned certificate with ONE deliberate defect. Fixtures and
OUTDIR/manifest.json are created exclusively (mode 'x'); nothing is overwritten. Stdlib only, no lane code.
LF line numbers in the manifest refer to the pinned (unmutated) certificate.
"""
import collections
import hashlib
import json
import os
import sys


def ints(line):
    return [int(t) for t in line.split(' ')]


def fmt(pts):
    return ' '.join(str(p) for p in pts)


class GenError(Exception):
    pass


def index(lines):
    hdr = lines[0].split(' ')
    if hdr[0] != 'GDD34' or lines[1] != 'GROUPS':
        raise GenError('unexpected header')
    k, m = int(hdr[2]), int(hdr[3])
    groups = [ints(lines[2 + i]) for i in range(k)]
    if lines[2 + k] != 'BLOCKS':
        raise GenError('BLOCKS expected')
    i = 3 + k
    block_idx = []
    while not lines[i].startswith('POINT '):
        block_idx.append(i)
        i += 1
    sections = []
    while i < len(lines):
        sec = {'x': int(lines[i].split(' ')[1]), 'idx': i, 'classes': []}
        i += 1
        while i < len(lines) and not lines[i].startswith('POINT '):
            cls = {'idx': i, 'j': int(lines[i].split(' ')[1]), 'triples': []}
            i += 1
            while i < len(lines) and not (lines[i].startswith('POINT ') or lines[i].startswith('FRAME ')):
                cls['triples'].append(i)
                i += 1
            sec['classes'].append(cls)
        sec['end'] = i
        sections.append(sec)
    grp = {}
    for gi, g in enumerate(groups):
        for p in g:
            grp[p] = gi
    derived = collections.defaultdict(set)
    blockset = set()
    for bi in block_idx:
        b = ints(lines[bi])
        blockset.add(frozenset(b))
        for x in b:
            derived[x].add(frozenset(p for p in b if p != x))
    return {'k': k, 'm': m, 'groups': groups, 'grp': grp, 'block_idx': block_idx, 'sections': sections,
            'derived': derived, 'blockset': blockset}


def lf(i):
    return i + 1


def c01_point_swap(lines, ctx):
    grp = ctx['grp']
    i1 = ctx['block_idx'][0]
    b1 = ints(lines[i1])
    p = b1[0]
    for i2 in ctx['block_idx']:
        b2 = ints(lines[i2])
        for q in b2:
            if q != p and grp[q] == grp[p] and q not in b1 and p not in b2:
                n1 = sorted([q if t == p else t for t in b1])
                n2 = sorted([p if t == q else t for t in b2])
                if frozenset(n1) in ctx['blockset'] or frozenset(n2) in ctx['blockset']:
                    continue
                new = list(lines)
                new[i1] = fmt(n1)
                new[i2] = fmt(n2)
                return new, {'lf_lines': [lf(i1), lf(i2)], 'old': [lines[i1], lines[i2]],
                             'new': [new[i1], new[i2]], 'swapped_points': [p, q],
                             'same_group': grp[p], 'new_blocks_already_present': False}
    raise GenError('no swap found')


def c02_deleted_block(lines, ctx):
    i = ctx['block_idx'][len(ctx['block_idx']) // 2]
    new = lines[:i] + lines[i + 1:]
    return new, {'lf_line_deleted': lf(i), 'old': lines[i]}


def c03_duplicated_block(lines, ctx):
    i = ctx['block_idx'][3000]
    new = lines[:i + 1] + [lines[i]] + lines[i + 1:]
    return new, {'lf_line_duplicated': lf(i), 'block': lines[i], 'inserted_after_lf_line': lf(i)}


def c04_block_inside_two_groups(lines, ctx):
    grp, groups = ctx['grp'], ctx['groups']
    i = ctx['block_idx'][5000]
    b = sorted(ints(lines[i]))
    a, c = b[0], b[1]
    a2 = [p for p in groups[grp[a]] if p != a][0]
    c2 = [p for p in groups[grp[c]] if p != c][0]
    nb = sorted([a, a2, c, c2])
    if len(set(grp[p] for p in nb)) != 2:
        raise GenError('c04 construction')
    new = list(lines)
    new[i] = fmt(nb)
    return new, {'lf_line': lf(i), 'old': lines[i], 'new': new[i], 'groups_met': sorted(set(grp[p] for p in nb))}


def c05_class_two_triples_share_point(lines, ctx):
    sec = ctx['sections'][0]
    c1 = sec['classes'][0]
    c2 = [c for c in sec['classes'][1:] if c['j'] == c1['j']][0]
    t1, t2 = c1['triples'][0], c2['triples'][0]
    new = list(lines)
    new[t1], new[t2] = lines[t2], lines[t1]
    pts = collections.Counter(p for t in c1['triples'] for p in ints(new[t]))
    shared = sorted(p for p, n in pts.items() if n > 1)
    if not shared:
        raise GenError('c05 no shared point')
    return new, {'x': sec['x'], 'class_lf_lines': [lf(c1['idx']), lf(c2['idx'])], 'label': c1['j'],
                 'swapped_triple_lf_lines': [lf(t1), lf(t2)], 'old': [lines[t1], lines[t2]],
                 'shared_points_in_first_class_after_swap': shared,
                 'note': 'the swap keeps the union of all classes at x equal to A_x'}


def c06_class_not_full_pc(lines, ctx):
    sec = [s for s in ctx['sections'] if s['x'] == 45][0]
    c = sec['classes'][0]
    t = c['triples'][-1]
    end = sec['end']
    new = lines[:t] + lines[t + 1:end] + ['FRAME %d' % c['j'], lines[t]] + lines[end:]
    return new, {'x': sec['x'], 'class_lf_line': lf(c['idx']), 'label': c['j'], 'moved_triple_lf_line': lf(t),
                 'moved_triple': lines[t], 'new_class': 'FRAME %d with that single triple appended at the end of POINT %d'
                 % (c['j'], sec['x']),
                 'note': 'class keeps 17 pairwise disjoint triples (51 of 54 points); all derived triples still listed once'}


def find_kempe(lines, ctx):
    grp, k = ctx['grp'], ctx['k']
    for sec in ctx['sections']:
        gx = grp[sec['x']]
        cls = [(c, [ints(lines[t]) for t in c['triples']]) for c in sec['classes']]
        for a in range(len(cls)):
            for b in range(a + 1, len(cls)):
                (c1, T1), (c2, T2) = cls[a], cls[b]
                if c1['j'] == c2['j']:
                    continue
                common = set(range(k)) - {gx, c1['j'], c2['j']}
                pos1 = {}
                pos2 = {}
                for idx, t in enumerate(T1):
                    for p in t:
                        if grp[p] in common:
                            pos1[p] = idx
                for idx, t in enumerate(T2):
                    for p in t:
                        if grp[p] in common:
                            pos2[p] = idx
                if set(pos1) != set(pos2):
                    continue
                parent = {}

                def find(u):
                    while parent.setdefault(u, u) != u:
                        parent[u] = parent[parent[u]]
                        u = parent[u]
                    return u
                for p in pos1:
                    ra, rb = find((1, pos1[p])), find((2, pos2[p]))
                    if ra != rb:
                        parent[ra] = rb
                comps = collections.defaultdict(lambda: ([], []))
                for idx in range(len(T1)):
                    comps[find((1, idx))][0].append(idx)
                for idx in range(len(T2)):
                    comps[find((2, idx))][1].append(idx)
                for root, (k1, k2) in sorted(comps.items(), key=lambda kv: len(kv[1][0])):
                    if 0 < len(k1) < len(T1) and len(k1) == len(k2):
                        return sec, c1, c2, sorted(k1), sorted(k2), len(comps)
    raise GenError('no proper Kempe component found')


def c07_class_spans_two_missing_groups(lines, ctx):
    grp, groups = ctx['grp'], ctx['groups']
    sec, c1, c2, k1, k2, ncomp = find_kempe(lines, ctx)
    new = list(lines)
    for i1, i2 in zip(k1, k2):
        a, b = c1['triples'][i1], c2['triples'][i2]
        new[a], new[b] = lines[b], lines[a]
    gx = grp[sec['x']]
    Y = set(p for p in grp if grp[p] != gx)
    info = []
    for c in (c1, c2):
        tri = [ints(new[t]) for t in c['triples']]
        pts = [p for t in tri for p in t]
        if len(pts) != len(set(pts)):
            raise GenError('c07 swap broke disjointness')
        miss = Y - set(pts)
        info.append({'class_lf_line': lf(c['idx']), 'label': c['j'], 'triples': len(tri),
                     'missing_points_by_group': dict((str(g), len(miss & set(groups[g]))) for g in range(ctx['k']) if g != gx)})
    return new, {'x': sec['x'], 'labels': [c1['j'], c2['j']], 'component_size_triples_per_class': len(k1),
                 'components_in_exchange_graph': ncomp,
                 'swapped_lf_line_pairs': [[lf(c1['triples'][i1]), lf(c2['triples'][i2])] for i1, i2 in zip(k1, k2)],
                 'classes_after_swap': info,
                 'note': 'Kempe-type exchange of one component: both classes stay pairwise disjoint with 18 triples '
                         'and 54 points, and the union of all classes at x is unchanged'}


def c08_out_of_range_point_label(lines, ctx):
    i = ctx['block_idx'][100]
    b = lines[i].split(' ')
    b[-1] = str(ctx['k'] * ctx['m'])
    new = list(lines)
    new[i] = ' '.join(b)
    return new, {'lf_line': lf(i), 'old': lines[i], 'new': new[i]}


def c08b_out_of_range_frame_label(lines, ctx):
    sec = [s for s in ctx['sections'] if s['x'] == 30][0]
    c = sec['classes'][0]
    new = list(lines)
    new[c['idx']] = 'FRAME %d' % ctx['k']
    return new, {'x': 30, 'lf_line': lf(c['idx']), 'old': lines[c['idx']], 'new': new[c['idx']]}


def c09_groups_duplicate_label(lines, ctx):
    g0 = lines[2].split(' ')
    old = g0[-1]
    g0[-1] = lines[3].split(' ')[0]
    new = list(lines)
    new[2] = ' '.join(g0)
    return new, {'lf_line': 3, 'replaced_label': int(old), 'by_label': int(g0[-1]),
                 'note': 'label also declared in the next group; the replaced label is in no group'}


def c09b_groups_swapped_labels(lines, ctx):
    g0 = lines[2].split(' ')
    g1 = lines[3].split(' ')
    a, b = g0[-1], g1[0]
    g0[-1], g1[0] = b, a
    new = list(lines)
    new[2] = ' '.join(g0)
    new[3] = ' '.join(g1)
    return new, {'lf_lines': [3, 4], 'swapped_labels': [int(a), int(b)],
                 'note': 'declared groups still partition X with sizes 18, but no longer match the blocks'}


def x10_frame_label_mismatch(lines, ctx):
    sec = [s for s in ctx['sections'] if s['x'] == 60][0]
    gx = ctx['grp'][60]
    c = sec['classes'][0]
    jj = min(set(range(ctx['k'])) - {c['j'], gx})
    new = list(lines)
    new[c['idx']] = 'FRAME %d' % jj
    return new, {'x': 60, 'lf_line': lf(c['idx']), 'old': lines[c['idx']], 'new': new[c['idx']]}


def x11_missing_point_section(lines, ctx):
    sec = ctx['sections'][-1]
    new = lines[:sec['idx']] + lines[sec['end']:]
    return new, {'x': sec['x'], 'deleted_lf_lines': [lf(sec['idx']), sec['end']]}


def x12_non_derived_triples_in_intact_class(lines, ctx):
    grp = ctx['grp']
    sec = [s for s in ctx['sections'] if s['x'] == 7][0]
    der = ctx['derived'][7]
    c = sec['classes'][0]
    for ia in range(len(c['triples'])):
        for ib in range(ia + 1, len(c['triples'])):
            t1, t2 = ints(lines[c['triples'][ia]]), ints(lines[c['triples'][ib]])
            for p in t1:
                q = [u for u in t2 if grp[u] == grp[p]]
                if len(q) != 1:
                    continue
                q = q[0]
                n1 = sorted([q if u == p else u for u in t1])
                n2 = sorted([p if u == q else u for u in t2])
                if frozenset(n1) in der or frozenset(n2) in der:
                    continue
                new = list(lines)
                a, b = c['triples'][ia], c['triples'][ib]
                new[a], new[b] = fmt(n1), fmt(n2)
                return new, {'x': 7, 'class_lf_line': lf(c['idx']), 'label': c['j'], 'lf_lines': [lf(a), lf(b)],
                             'old': [lines[a], lines[b]], 'new': [new[a], new[b]],
                             'note': 'class remains a PC of the same 54 points; the two new triples T do not have '
                                     'T + {x} a block'}
    raise GenError('x12 not found')


def x13_frame_label_own_group(lines, ctx):
    sec = [s for s in ctx['sections'] if s['x'] == 20][0]
    gx = ctx['grp'][20]
    c = sec['classes'][0]
    new = list(lines)
    new[c['idx']] = 'FRAME %d' % gx
    return new, {'x': 20, 'group_of_x': gx, 'lf_line': lf(c['idx']), 'old': lines[c['idx']], 'new': new[c['idx']]}


CONTROLS = [
    ('c01_point_swap_between_blocks', 'point swap between blocks', c01_point_swap,
     ['C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE'], None),
    ('c02_deleted_block', 'deleted block', c02_deleted_block,
     ['C09_BLOCK_COUNT', 'C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE'], None),
    ('c03_duplicated_block', 'duplicated block', c03_duplicated_block,
     ['C08_BLOCKS_DISTINCT', 'C10_TRANSVERSE_TRIPLES_EXACTLY_ONCE'], None),
    ('c04_block_inside_two_groups', 'a block inside two groups (non-transverse)', c04_block_inside_two_groups,
     ['C06_BLOCK_TRANSVERSE', 'C07_BLOCK_NOT_IN_GROUP_PAIR_UNION'], None),
    ('c05_frame_class_two_triples_share_point', 'a frame class with two triples sharing a point',
     c05_class_two_triples_share_point,
     ['F05_CLASS_PAIRWISE_DISJOINT'], ['F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP', 'OVERLAP']),
    ('c06_frame_class_not_full_parallel_class', 'a frame class that is not a full parallel class of its 72-18 points',
     c06_class_not_full_pc,
     ['F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP'], ['F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP', 'NOT_FULL']),
    ('c07_frame_class_spans_two_missing_groups', 'a frame class spanning two missing groups',
     c07_class_spans_two_missing_groups,
     ['F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP'],
     ['F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP', 'SPANS_TWO_OR_MORE_MISSING_GROUPS']),
    ('c08_out_of_range_point_label', 'out-of-range label (point label 90 in a block)', c08_out_of_range_point_label,
     ['C03_POINT_LABEL_RANGE'], None),
    ('c08b_out_of_range_frame_label', 'out-of-range label (FRAME label 5)', c08b_out_of_range_frame_label,
     ['F02_FRAME_LABEL_VALID'], None),
    ('c09_group_declaration_duplicate_label', 'corrupted group declaration (label declared twice, one missing)',
     c09_groups_duplicate_label, ['C04_GROUPS_PARTITION'], None),
    ('c09b_group_declaration_swapped_labels', 'corrupted group declaration (two labels swapped between groups)',
     c09b_groups_swapped_labels, ['C06_BLOCK_TRANSVERSE'], None),
    ('x10_frame_label_mismatch', 'extra: declared FRAME label differs from the missed group', x10_frame_label_mismatch,
     ['F07_FRAME_LABEL_MATCHES_MISSED_GROUP'], None),
    ('x11_missing_point_section', 'extra: POINT 89 section removed', x11_missing_point_section,
     ['F01_POINT_SECTIONS'], None),
    ('x12_non_derived_triples_in_intact_class', 'extra: class still a PC but two triples are not derived',
     x12_non_derived_triples_in_intact_class, ['F04_CLASSES_PARTITION_DERIVED'], None),
    ('x13_frame_label_own_group', 'extra: FRAME label equal to the group of x', x13_frame_label_own_group,
     ['F02_FRAME_LABEL_VALID'], None),
]


def build(lines):
    ctx = index(lines)
    out = []
    for name, category, fn, intended, detail in CONTROLS:
        new, info = fn(lines, ctx)
        out.append((name, category, intended, detail, new, info))
    return out


def main(argv):
    if len(argv) != 3:
        sys.stderr.write('usage: make_controls.py PINNED_CERT OUTDIR\n')
        return 64
    src, outdir = argv[1], argv[2]
    with open(src, 'rb') as f:
        data = f.read()
    lines = data.decode('ascii').split('\n')
    if lines[-1] != '':
        raise GenError('no final LF')
    lines.pop()
    manifest = {'source': os.path.abspath(src), 'source_sha256': hashlib.sha256(data).hexdigest(),
                'generator_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
                'controls': []}
    for name, category, intended, detail, new, info in build(lines):
        body = ('\n'.join(new) + '\n').encode('ascii')
        path = os.path.join(outdir, name + '.txt')
        with open(path, 'xb') as f:
            f.write(body)
        manifest['controls'].append({'name': name, 'category': category, 'fixture': path,
                                     'sha256': hashlib.sha256(body).hexdigest(), 'bytes': len(body),
                                     'intended_failed_checks': intended,
                                     'intended_detail': detail, 'mutation': info})
    with open(os.path.join(outdir, 'manifest.json'), 'x') as f:
        f.write(json.dumps(manifest, indent=1) + '\n')
    sys.stdout.write('wrote %d fixtures\n' % len(manifest['controls']))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
