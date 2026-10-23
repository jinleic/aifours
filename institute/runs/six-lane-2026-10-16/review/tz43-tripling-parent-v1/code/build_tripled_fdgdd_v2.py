#!/usr/bin/env python3
r"""tz43 tripling desk: constructive Kirkman frames for the zero-sum tripled bare H(5,6,4,3) master.

Stdlib only. Written by the parent desk Tz43TriplingAudit from lemma-v1.md / lemma-v2.md; no lane, producer, SAT
or checker code is imported or read. Only the pinned master JSON fields 'groups' and 'blocks' are used.

v2 (review dispositions of tz43-tripling-claude-v1 findings 4-7; construction and output bytes unchanged):
  * docstring cites the right results; mut_b wording says existence AND uniqueness fail only at C-copies;
  * mut_c analysis also checks that each class covers exactly the 54 points of (X \ G_x) \ G_j;
  * the rendered certificate must have the original header/GROUPS/BLOCKS prefix byte for byte, and it is
    re-parsed and compared with the in-memory sections before anything is written;
  * --verify-existing: regenerate all bytes, require byte equality with the files already on disk (nothing is
    rewritten), then write only a new manifest.

Construction (lemma-v2.md, Lemmas 1-2 and Theorem 3):
  * master: an H(5,6,4,3) = GDD(3,4,30) of type 6^5 (5 groups of 6, 540 blocks).
  * inflation: point (p, b), b in Z3, gets label 3p+b; each master block {p0,p1,p2,p3} gives the 27 blocks
    {(p_i, b_i)} with b0+b1+b2+b3 = 0 (mod 3).  This yields 14580 blocks.
  * the derived design at the inflated point (p, beta) is the zero-sum lift, with constant s = -beta, of the
    master derived design D_p (a 3-GDD of type 6^4 on the other four groups).
  * for each group j other than the group of p, the missing-group family F = {T in D_p : T misses G_j} is
    3-partite with parts (A, B, C) = the three remaining groups in increasing index order, and 3-regular.
  * a proper 3-edge-colouring u of the incidence bipartite graph (vertex nodes vs edge nodes) of F is computed
    as three successive perfect matchings (augmenting paths; existence by Hall for regular bipartite graphs).
  * the lift ((a,x),(b,y),(c,z)) of T = (a,b,c), with x+y+z = s, gets the label P = (x+u(a,T), y+u(b,T)) in
    Z3^2; the 9 label classes are written as the 9 FRAME j classes of POINT 3p+beta.

Every positive output is checked internally (each class is a parallel class of the 54 points outside the two
groups, and the 36 classes partition exactly the derived triples at that point) before anything is written.
Four mutation fixtures are produced on purpose to fail; they are analysed, not checked.

Usage:
  python3 -B build_tripled_fdgdd_v2.py --master M --master-sha S --orig O --orig-sha S \
      --cert-out NEW.txt --fixtures-dir DIR --colourings-out NEW.json --manifest-out NEW.json
  python3 -B build_tripled_fdgdd_v2.py ... same paths ... --verify-existing   (cert/fixtures/colourings must exist)
  python3 -B build_tripled_fdgdd_v2.py --master M --master-sha S --orig O --orig-sha S --hashes-only
All new outputs are created exclusively (open mode 'x'); nothing is written if any internal check fails.
"""
import argparse
import collections
import hashlib
import itertools
import json
import os
import platform
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

Z3 = (0, 1, 2)
LABELS = tuple(itertools.product(Z3, Z3))
K, M_MASTER, COPIES = 5, 6, 3

MUTATIONS = collections.OrderedDict([
    ('mut_a_colour_vertex_swap', collections.OrderedDict([
        ('point', 7), ('family_group', 'first group other than the group of p'), ('edge_index', 0),
        ('change', 'at POINT 7 = (p=2, beta=1), family missing group 1, swap u(a,T) and u(b,T) on the first '
                   'edge T: zero-sum at T is kept, but u(a,.) and u(b,.) stop being bijections'),
        ('expected_parent_failed_checks', ['F05_CLASS_PAIRWISE_DISJOINT',
                                           'F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP']),
        ('expected_claude_invariant', 'frame.parallel')])),
    ('mut_b_colour_shift_A_vertex', collections.OrderedDict([
        ('point', 31), ('family_group', 'first group other than the group of p'), ('vertex', 'first vertex of part A'),
        ('change', 'at POINT 31 = (p=10, beta=1), family missing group 0, add 1 to u(a*,T) for the three edges T '
                   'at the first A-vertex a*: u stays a bijection at every vertex, but the three edges at a* lose '
                   'the zero sum, so only step (iii) at C-vertices can fail (existence and uniqueness); A- and '
                   'B-copies stay exactly covered'),
        ('expected_parent_failed_checks', ['F05_CLASS_PAIRWISE_DISJOINT',
                                           'F06_CLASS_IS_PC_OF_X_MINUS_GX_AND_ONE_GROUP']),
        ('expected_claude_invariant', 'frame.parallel')])),
    ('mut_c_wrong_third_sum_constant', collections.OrderedDict([
        ('point', 56),
        ('change', 'at POINT 56 = (p=18, beta=2), every lift is built with z = s\' - x - y where s\' = s + 1 '
                   '(s = -beta is the correct constant): classes stay parallel classes of the right 54 points, '
                   'but no listed triple is a derived triple of POINT 56'),
        ('expected_parent_failed_checks', ['F04_CLASSES_PARTITION_DERIVED']),
        ('expected_claude_invariant', 'derived.not_block')])),
    ('mut_d_duplicate_frame_class', collections.OrderedDict([
        ('point', 89),
        ('change', 'at POINT 89 = (p=29, beta=2), the second FRAME 0 class (label P=(0,1)) is replaced by a copy '
                   'of the first FRAME 0 class (label P=(0,0)); class and label counts are unchanged'),
        ('expected_parent_failed_checks', ['F04_CLASSES_PARTITION_DERIVED']),
        ('expected_claude_invariant', 'derived.repeat')])),
])


class ConstructionError(Exception):
    pass


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def read_pinned(path, expected):
    with open(path, 'rb') as f:
        data = f.read()
    got = sha256(data)
    if got != expected:
        raise ConstructionError('sha256 of %s is %s, expected %s' % (path, got, expected))
    return data


# ---------------------------------------------------------------- master H(5,6,4,3)

def load_master(data):
    d = json.loads(data.decode('ascii'))
    groups = [list(g) for g in d['groups']]
    v = K * M_MASTER
    if len(groups) != K or any(len(g) != M_MASTER for g in groups):
        raise ConstructionError('master groups are not of type 6^5')
    if any(type(p) is not int for g in groups for p in g) or sorted(p for g in groups for p in g) != list(range(v)):
        raise ConstructionError('master groups do not partition 0..29')
    grp = [None] * v
    for i, g in enumerate(groups):
        for p in g:
            grp[p] = i
    blocks = []
    for b in d['blocks']:
        if len(b) != 4 or any(type(p) is not int or not 0 <= p < v for p in b) or len(set(b)) != 4:
            raise ConstructionError('master block %r is not a 4-subset of 0..29' % (b,))
        if len(set(grp[p] for p in b)) != 4:
            raise ConstructionError('master block %r is not transverse' % (b,))
        blocks.append(tuple(sorted(b)))
    if len(set(blocks)) != len(blocks):
        raise ConstructionError('repeated master block')
    return groups, grp, blocks


def check_master_is_h(groups, blocks):
    """Direct (non-SAT) precondition: every transverse triple of the master lies in exactly one block."""
    cnt = collections.Counter(t for b in blocks for t in itertools.combinations(b, 3))
    universe = set()
    for ga, gb, gc in itertools.combinations(range(K), 3):
        for a in groups[ga]:
            for b in groups[gb]:
                for c in groups[gc]:
                    universe.add(tuple(sorted((a, b, c))))
    if len(universe) != 2160 or set(cnt) != universe or max(cnt.values()) != 1 or len(blocks) != 540:
        raise ConstructionError('master is not an H(5,6,4,3)')
    return len(universe)


def master_derived(groups, grp, blocks):
    der = collections.defaultdict(list)
    for b in blocks:
        for p in b:
            der[p].append(tuple(q for q in b if q != p))
    for p in range(K * M_MASTER):
        D = der[p]
        pairs = collections.Counter()
        for T in D:
            if grp[p] in set(grp[q] for q in T) or len(set(grp[q] for q in T)) != 3:
                raise ConstructionError('derived triple %r at master point %d is not transverse' % (T, p))
            for e in itertools.combinations(sorted(T), 2):
                pairs[e] += 1
        want = set()
        others = [i for i in range(K) if i != grp[p]]
        for ga, gb in itertools.combinations(others, 2):
            for a in groups[ga]:
                for b in groups[gb]:
                    want.add(tuple(sorted((a, b))))
        if len(D) != 72 or set(pairs) != want or max(pairs.values()) != 1:
            raise ConstructionError('master derived design at %d is not a 3-GDD of type 6^4' % p)
    return der


def missing_family(groups, grp, der, p, j):
    """Return (parts, vertices, oriented edges (a,b,c)) of F_{p,j}; check 3-partite and 3-regular."""
    parts = [i for i in range(K) if i not in (grp[p], j)]
    edges = []
    for T in sorted(der[p]):
        if any(grp[q] == j for q in T):
            continue
        by = dict((grp[q], q) for q in T)
        if sorted(by) != parts:
            raise ConstructionError('family (%d,%d): triple %r is not 3-partite on %r' % (p, j, T, parts))
        edges.append((by[parts[0]], by[parts[1]], by[parts[2]]))
    verts = [q for i in parts for q in sorted(groups[i])]
    deg = collections.Counter(q for e in edges for q in e)
    if len(edges) != 18 or set(deg) != set(verts) or any(deg[q] != 3 for q in verts):
        raise ConstructionError('family (%d,%d) is not 3-regular with 18 edges' % (p, j))
    return parts, verts, edges


# ---------------------------------------------------------------- incidence colouring (Hall / Konig)

def incidence_colouring(verts, edges):
    """u[e][pos] in Z3 for the incidence (edges[e][pos], e); three successive perfect matchings."""
    remaining = dict((q, [e for e, E in enumerate(edges) if q in E]) for q in verts)
    colour = {}
    for c in range(3):
        match = {}

        def augment(q, seen):
            for e in remaining[q]:
                if e in seen:
                    continue
                seen.add(e)
                if e not in match or augment(match[e], seen):
                    match[e] = q
                    return True
            return False

        for q in verts:
            if not augment(q, set()):
                raise ConstructionError('round %d: no perfect matching (impossible for a regular bipartite graph)' % c)
        if len(match) != len(edges) or len(set(match.values())) != len(verts):
            raise ConstructionError('round %d: matching is not perfect on both sides' % c)
        for e, q in match.items():
            colour[(q, e)] = c
            remaining[q].remove(e)
    u = [tuple(colour[(q, e)] for q in E) for e, E in enumerate(edges)]
    for e, row in enumerate(u):
        if sorted(row) != [0, 1, 2]:
            raise ConstructionError('colouring not proper at edge node %d' % e)
    for q in verts:
        if sorted(u[e][E.index(q)] for e, E in enumerate(edges) if q in E) != [0, 1, 2]:
            raise ConstructionError('colouring not proper at vertex node %d' % q)
    return u


def lift_classes(edges, u, s):
    """The 9 label classes of the zero-sum lift with constant s (inflated labels 3q+x)."""
    classes = collections.OrderedDict((P, []) for P in LABELS)
    for (a, b, c), (ua, ub, _uc) in zip(edges, u):
        for x in Z3:
            for y in Z3:
                z = (s - x - y) % 3
                classes[((x + ua) % 3, (y + ub) % 3)].append(tuple(sorted((3 * a + x, 3 * b + y, 3 * c + z))))
    return classes


def class_defects(cls, verts, parts, grp):
    """Per-part counts of inflated points covered 0 times or >= 2 times by one class."""
    cov = collections.Counter(t for tri in cls for t in tri)
    out = collections.OrderedDict()
    for name, gi in zip('ABC', parts):
        pts = [3 * q + x for q in verts if grp[q] == gi for x in Z3]
        out[name] = [sum(1 for t in pts if cov[t] == 0), sum(1 for t in pts if cov[t] >= 2)]
    return out


# ---------------------------------------------------------------- inflation and certificate

def inflate(blocks):
    out = []
    for b in blocks:
        for b0, b1, b2 in itertools.product(Z3, Z3, Z3):
            b3 = (-(b0 + b1 + b2)) % 3
            out.append(tuple(sorted((3 * b[0] + b0, 3 * b[1] + b1, 3 * b[2] + b2, 3 * b[3] + b3))))
    if len(out) != 14580 or len(set(out)) != len(out):
        raise ConstructionError('inflated block list is not 14580 distinct blocks')
    return sorted(out)


def orig_prefix_blocks(orig):
    """Strictly read the original certificate's header, GROUPS and BLOCKS records (POINT sections ignored)."""
    text = orig.decode('ascii')
    lines = text.split('\n')
    if lines[-1] != '' or lines[0] != 'GDD34 FDGDD 5 18' or lines[1] != 'GROUPS' or lines[7] != 'BLOCKS':
        raise ConstructionError('original certificate header/GROUPS/BLOCKS layout not as pinned')
    end = lines.index('POINT 0')
    blocks = []
    for ln in lines[8:end]:
        t = ln.split(' ')
        if len(t) != 4:
            raise ConstructionError('original block line %r' % ln)
        blocks.append(tuple(sorted(int(z) for z in t)))
    return lines[:end], blocks


def render(groups_inf, blocks_inf, sections):
    out = ['GDD34 FDGDD 5 18', 'GROUPS']
    out.extend(' '.join(str(p) for p in g) for g in groups_inf)
    out.append('BLOCKS')
    out.extend(' '.join(str(p) for p in b) for b in blocks_inf)
    for X in range(len(sections)):
        out.append('POINT %d' % X)
        for j, cls in sections[X]:
            out.append('FRAME %d' % j)
            out.extend(' '.join(str(p) for p in t) for t in sorted(cls))
    return ('\n'.join(out) + '\n').encode('ascii')


def reparse_sections(cert, v_inf):
    """v2: strict re-read of the rendered POINT/FRAME/triple records; one [(j, [triple, ...]), ...] per POINT."""
    lines = cert.decode('ascii').split('\n')
    if lines[-1] != '':
        raise ConstructionError('rendered certificate does not end with LF')
    lines.pop()
    i = lines.index('POINT 0')
    out = []
    while i < len(lines):
        if lines[i] != 'POINT %d' % len(out):
            raise ConstructionError('rendered POINT header out of order at LF %d' % (i + 1))
        i += 1
        sec = []
        while i < len(lines) and not lines[i].startswith('POINT '):
            t = lines[i].split(' ')
            if len(t) != 2 or t[0] != 'FRAME':
                raise ConstructionError('rendered FRAME header expected at LF %d' % (i + 1))
            j = int(t[1])
            i += 1
            tris = []
            while i < len(lines) and not lines[i].startswith(('POINT ', 'FRAME ')):
                tri = tuple(int(z) for z in lines[i].split(' '))
                if len(tri) != 3:
                    raise ConstructionError('rendered triple record malformed at LF %d' % (i + 1))
                tris.append(tri)
                i += 1
            sec.append((j, tris))
        out.append(sec)
    if len(out) != v_inf:
        raise ConstructionError('rendered certificate has %d POINT sections' % len(out))
    return out


def build(master_data, orig_data):
    groups, grp, blocks = load_master(master_data)
    n_universe = check_master_is_h(groups, blocks)
    der = master_derived(groups, grp, blocks)
    v_inf = K * M_MASTER * COPIES
    groups_inf = [sorted(3 * p + x for p in g for x in Z3) for g in groups]
    grp_inf = [grp[X // 3] for X in range(v_inf)]
    blocks_inf = inflate(blocks)
    orig_head, orig_blocks = orig_prefix_blocks(orig_data)
    same_set = set(orig_blocks) == set(blocks_inf) and len(orig_blocks) == len(blocks_inf)
    if not same_set:
        raise ConstructionError('re-inflated blocks differ from the original certificate blocks as a set')
    der_inf = collections.defaultdict(set)
    for b in blocks_inf:
        for X in b:
            der_inf[X].add(tuple(q for q in b if q != X))

    families, colourings, degree_hist = {}, [], collections.Counter()
    for p in range(K * M_MASTER):
        for j in range(K):
            if j == grp[p]:
                continue
            parts, verts, edges = missing_family(groups, grp, der, p, j)
            u = incidence_colouring(verts, edges)
            families[(p, j)] = (parts, verts, edges, u)
            degree_hist.update(collections.Counter(q for e in edges for q in e).values())
            colourings.append(collections.OrderedDict([('p', p), ('j', j), ('parts', parts),
                                                       ('edges', [list(e) for e in edges]),
                                                       ('u', [list(r) for r in u])]))

    sections, class_count = [], 0
    for X in range(v_inf):
        p, beta = divmod(X, 3)
        s = (-beta) % 3
        sec, listed = [], []
        for j in range(K):
            if j == grp[p]:
                continue
            parts, verts, edges, u = families[(p, j)]
            target = set(Y for Y in range(v_inf) if grp_inf[Y] not in (grp[p], j))
            for P, cls in lift_classes(edges, u, s).items():
                pts = [t for tri in cls for t in tri]
                if len(cls) != 18 or len(set(pts)) != 54 or set(pts) != target:
                    raise ConstructionError('POINT %d FRAME %d label %r is not a parallel class' % (X, j, P))
                sec.append((j, cls))
                listed.extend(cls)
                class_count += 1
        if len(listed) != 648 or set(listed) != der_inf[X] or len(set(listed)) != 648:
            raise ConstructionError('POINT %d: classes do not partition the derived design' % X)
        sections.append(sec)
    cert = render(groups_inf, blocks_inf, sections)
    head_lines = cert.decode('ascii').split('\n')[:len(orig_head)]
    prefix_identical = head_lines == orig_head
    if not prefix_identical:
        raise ConstructionError('rendered header/GROUPS/BLOCKS prefix differs from the original certificate')
    if reparse_sections(cert, v_inf) != [[(j, sorted(cls)) for j, cls in sec] for sec in sections]:
        raise ConstructionError('re-parsed certificate sections differ from the in-memory sections')

    fixtures = collections.OrderedDict()
    analyses = collections.OrderedDict()
    # mutation a: swap u(a,T), u(b,T) on the first edge of the first family at POINT 7
    X = MUTATIONS['mut_a_colour_vertex_swap']['point']
    p, beta = divmod(X, 3)
    sec = list(sections[X])
    j0 = min(j for j in range(K) if j != grp[p])
    parts, verts, edges, u = families[(p, j0)]
    bad = [list(r) for r in u]
    bad[0][0], bad[0][1] = bad[0][1], bad[0][0]
    bad = [tuple(r) for r in bad]
    new = lift_classes(edges, bad, (-beta) % 3)
    idx = [i for i, (j, _) in enumerate(sec) if j == j0]
    for i, (P, cls) in zip(idx, new.items()):
        sec[i] = (j0, cls)
    fixtures['mut_a_colour_vertex_swap'] = render(groups_inf, blocks_inf, sections[:X] + [sec] + sections[X + 1:])
    analyses['mut_a_colour_vertex_swap'] = collections.OrderedDict([
        ('p', p), ('beta', beta), ('family_group', j0), ('edge', list(edges[0])), ('u_before', list(u[0])),
        ('u_after', list(bad[0])), ('edge_sum_after_mod3', sum(bad[0]) % 3),
        ('vertex_colours_after', dict((str(q), sorted(bad[e][E.index(q)] for e, E in enumerate(edges) if q in E))
                                      for q in edges[0][:2])),
        ('class_defects_uncovered_multicovered_by_part', [class_defects(c, verts, parts, grp) for c in new.values()])])

    # mutation b: shift u at the first A-vertex by +1 (vertex-proper, zero sum broken on its 3 edges) at POINT 31
    X = MUTATIONS['mut_b_colour_shift_A_vertex']['point']
    p, beta = divmod(X, 3)
    sec = list(sections[X])
    j0 = min(j for j in range(K) if j != grp[p])
    parts, verts, edges, u = families[(p, j0)]
    a_star = min(q for q in verts if grp[q] == parts[0])
    bad = [((r[0] + 1) % 3, r[1], r[2]) if E[0] == a_star else r for E, r in zip(edges, u)]
    new = lift_classes(edges, bad, (-beta) % 3)
    idx = [i for i, (j, _) in enumerate(sec) if j == j0]
    for i, (P, cls) in zip(idx, new.items()):
        sec[i] = (j0, cls)
    fixtures['mut_b_colour_shift_A_vertex'] = render(groups_inf, blocks_inf, sections[:X] + [sec] + sections[X + 1:])
    vertex_proper = all(sorted(bad[e][E.index(q)] for e, E in enumerate(edges) if q in E) == [0, 1, 2] for q in verts)
    analyses['mut_b_colour_shift_A_vertex'] = collections.OrderedDict([
        ('p', p), ('beta', beta), ('family_group', j0), ('a_star', a_star),
        ('edges_at_a_star', [list(E) for E in edges if E[0] == a_star]),
        ('still_vertex_proper_everywhere', vertex_proper),
        ('edge_sums_mod3_at_a_star', [sum(r) % 3 for E, r in zip(edges, bad) if E[0] == a_star]),
        ('class_defects_uncovered_multicovered_by_part', [class_defects(c, verts, parts, grp) for c in new.values()])])

    # mutation c: wrong sum constant s' = s + 1 for every family at POINT 56
    X = MUTATIONS['mut_c_wrong_third_sum_constant']['point']
    p, beta = divmod(X, 3)
    s_bad = ((-beta) + 1) % 3
    sec = []
    perfect = True
    for j in range(K):
        if j == grp[p]:
            continue
        parts, verts, edges, u = families[(p, j)]
        target = set(Y for Y in range(v_inf) if grp_inf[Y] not in (grp[p], j))
        for P, cls in lift_classes(edges, u, s_bad).items():
            sec.append((j, cls))
            pts = [t for tri in cls for t in tri]
            perfect = perfect and len(pts) == 54 and set(pts) == target
    fixtures['mut_c_wrong_third_sum_constant'] = render(groups_inf, blocks_inf, sections[:X] + [sec] + sections[X + 1:])
    listed = set(t for _, c in sec for t in c)
    analyses['mut_c_wrong_third_sum_constant'] = collections.OrderedDict([
        ('p', p), ('beta', beta), ('correct_s', (-beta) % 3), ('used_s', s_bad),
        ('all_classes_still_parallel_classes', perfect),
        ('listed_triples_that_are_derived_at_point', len(listed & der_inf[X])), ('listed_triples', len(listed))])

    # mutation d: duplicate the first FRAME 0 class over the second one at POINT 89
    X = MUTATIONS['mut_d_duplicate_frame_class']['point']
    sec = list(sections[X])
    idx = [i for i, (j, _) in enumerate(sec) if j == 0]
    sec[idx[1]] = (0, list(sec[idx[0]][1]))
    fixtures['mut_d_duplicate_frame_class'] = render(groups_inf, blocks_inf, sections[:X] + [sec] + sections[X + 1:])
    analyses['mut_d_duplicate_frame_class'] = collections.OrderedDict([
        ('p', X // 3), ('beta', X % 3), ('replaced_class_index_in_section', idx[1]), ('copied_class_index', idx[0])])

    pos_lines = cert.decode('ascii').split('\n')
    for name, data in fixtures.items():
        mut_lines = data.decode('ascii').split('\n')
        diff = [i + 1 for i, (x, y) in enumerate(zip(pos_lines, mut_lines)) if x != y]
        analyses[name]['line_count_equal_to_positive'] = len(mut_lines) == len(pos_lines)
        analyses[name]['first_last_differing_lf'] = [diff[0], diff[-1]] if diff else None
        analyses[name]['differing_lines'] = len(diff)
        X = MUTATIONS[name]['point']
        lo = pos_lines.index('POINT %d' % X) + 1
        hi = pos_lines.index('POINT %d' % (X + 1)) if X + 1 < v_inf else len(pos_lines) - 1
        analyses[name]['positive_section_lf_range'] = [lo, hi]
        analyses[name]['all_differences_inside_that_point_section'] = bool(diff) and all(lo <= d <= hi for d in diff)

    stats = collections.OrderedDict([
        ('master_points', K * M_MASTER), ('master_blocks', len(blocks)), ('master_transverse_triples', n_universe),
        ('master_derived_triples_per_point', 72), ('missing_families', len(families)),
        ('family_vertex_degree_histogram', dict((str(k), v) for k, v in sorted(degree_hist.items()))),
        ('inflated_points', v_inf), ('inflated_blocks', len(blocks_inf)),
        ('re_inflated_blocks_equal_original_as_set', same_set),
        ('header_groups_blocks_prefix_byte_identical_to_original', prefix_identical),
        ('original_prefix_lines', len(orig_head)),
        ('points_with_frames', len(sections)), ('frame_classes_total', class_count),
        ('frame_classes_per_point', class_count // v_inf), ('triples_per_class', 18),
        ('derived_triples_per_point', 648)])
    colour_json = (json.dumps(colourings, separators=(',', ':')) + '\n').encode('ascii')
    return cert, fixtures, analyses, stats, colour_json


def own_sha():
    with open(os.path.abspath(__file__), 'rb') as f:
        return sha256(f.read())


def main(argv):
    ap = argparse.ArgumentParser()
    for name in ('--master', '--master-sha', '--orig', '--orig-sha'):
        ap.add_argument(name, required=True)
    ap.add_argument('--cert-out')
    ap.add_argument('--fixtures-dir')
    ap.add_argument('--colourings-out')
    ap.add_argument('--manifest-out')
    ap.add_argument('--hashes-only', action='store_true')
    ap.add_argument('--verify-existing', action='store_true')
    a = ap.parse_args(argv[1:])
    started = stamp()
    master = read_pinned(a.master, a.master_sha)
    orig = read_pinned(a.orig, a.orig_sha)
    cert, fixtures, analyses, stats, colour_json = build(master, orig)
    files = collections.OrderedDict([('positive', cert)] + list(fixtures.items()) + [('colourings', colour_json)])
    hashes = collections.OrderedDict((k, collections.OrderedDict([('sha256', sha256(v)), ('bytes', len(v)),
                                                                  ('lf_count', v.count(b'\n'))]))
                                     for k, v in files.items())
    base = collections.OrderedDict([
        ('generator', collections.OrderedDict([('path', os.path.abspath(__file__)), ('sha256', own_sha())])),
        ('python', collections.OrderedDict([('executable', sys.executable), ('version', platform.python_version()),
                                            ('optimize_flag', sys.flags.optimize)])),
        ('inputs', collections.OrderedDict([
            ('master', collections.OrderedDict([('path', os.path.abspath(a.master)), ('sha256', a.master_sha)])),
            ('original_certificate', collections.OrderedDict([('path', os.path.abspath(a.orig)),
                                                              ('sha256', a.orig_sha)]))])),
        ('started_at_pt', started), ('stats', stats), ('outputs', hashes)])
    if a.hashes_only:
        base['finished_at_pt'] = stamp()
        sys.stdout.write(json.dumps(base, indent=1) + '\n')
        return 0
    if not (a.cert_out and a.fixtures_dir and a.colourings_out and a.manifest_out):
        raise SystemExit('write mode needs --cert-out --fixtures-dir --colourings-out --manifest-out')
    paths = collections.OrderedDict([('positive', a.cert_out)])
    for name in fixtures:
        paths[name] = os.path.join(a.fixtures_dir, name + '.txt')
    paths['colourings'] = a.colourings_out
    if a.verify_existing:
        if os.path.exists(a.manifest_out):
            raise SystemExit('refusing to overwrite ' + a.manifest_out)
        for k, p in paths.items():
            with open(p, 'rb') as f:
                if f.read() != files[k]:
                    raise ConstructionError('existing file %s differs from the regenerated %s bytes' % (p, k))
    else:
        for p in list(paths.values()) + [a.manifest_out]:
            if os.path.exists(p):
                raise SystemExit('refusing to overwrite ' + p)
        for k, p in paths.items():
            with open(p, 'xb') as f:
                f.write(files[k])
    manifest = base
    manifest['mode'] = 'verify-existing (byte equality, nothing rewritten)' if a.verify_existing else 'write'
    manifest['written' if not a.verify_existing else 'verified_existing'] = collections.OrderedDict(
        (k, os.path.abspath(p)) for k, p in paths.items())
    manifest['mutations'] = collections.OrderedDict(
        (name, collections.OrderedDict(list(MUTATIONS[name].items()) + [('analysis', analyses[name])]))
        for name in fixtures)
    manifest['finished_at_pt'] = stamp()
    with open(a.manifest_out, 'x') as f:
        f.write(json.dumps(manifest, indent=1) + '\n')
    sys.stdout.write(json.dumps(collections.OrderedDict(
        [('stats', stats), ('outputs', hashes)]), indent=1) + '\n')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main(sys.argv))
    except ConstructionError as exc:
        sys.stderr.write('ConstructionError: %s\n' % exc)
        sys.exit(3)
