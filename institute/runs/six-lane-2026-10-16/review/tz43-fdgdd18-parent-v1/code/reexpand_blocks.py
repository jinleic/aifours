#!/usr/bin/env python3
"""Independent block re-expansion for the FDGDD(3,4,5{18}) candidate (parent desk Tz43FdgddParentCheck).

Usage: python3 -B reexpand_blocks.py MASTER_JSON RDTD_TXT CANDIDATE_TXT --out NEW.json
Uses ONLY the pinned master (blocks, groups, permutations) and the pinned RDTD(3,4,3) (GROUPS and BLOCKS
sections). For every master block with points p0 < p1 < p2 < p3 and every RDTD block, the RDTD point of
group i at position b of its GROUPS line becomes the inflated point 3*p_i + b. The inflated block multiset
is compared with the candidate's BLOCKS section. Frames are NOT reproduced: they were found after
inflation (worker construction note section 3) and are not determined by the master or the RDTD.
Ingredient checks (master GDD, RDTD TD, master permutation group) are informational.
Stdlib only; no lane code imported or executed. Output file created exclusively.
"""
import collections
import hashlib
import itertools
import json
import os
import platform
import resource
import sys
import time


def sha(data):
    return hashlib.sha256(data).hexdigest()


def gdd_triple_check(groups, blocks, block_size):
    """Return dict: is every block a transverse block_size-set and every transverse 3-subset in exactly one block."""
    grp = {}
    for gi, g in enumerate(groups):
        for p in g:
            grp[p] = gi
    pts = sorted(grp)
    res = collections.OrderedDict()
    res['points'] = len(pts)
    res['groups_partition_points'] = (sum(len(g) for g in groups) == len(pts) and pts == list(range(len(pts))))
    res['group_sizes'] = [len(g) for g in groups]
    res['blocks'] = len(blocks)
    res['blocks_distinct'] = len(set(frozenset(b) for b in blocks))
    res['all_blocks_transverse_size'] = all(len(b) == block_size and len(set(grp.get(p, -1) for p in b)) == block_size
                                            and all(p in grp for p in b) for b in blocks)
    cnt = collections.Counter()
    for b in blocks:
        for t in itertools.combinations(sorted(b), 3):
            cnt[t] += 1
    universe = set()
    for ga, gb, gc in itertools.combinations(range(len(groups)), 3):
        for t in itertools.product(groups[ga], groups[gb], groups[gc]):
            universe.add(tuple(sorted(t)))
    res['transverse_triples'] = len(universe)
    res['every_transverse_triple_exactly_once'] = (set(cnt) == universe and all(c == 1 for c in cnt.values()))
    return res


def compose(p, q):
    """(p o q)(i) = p[q[i]]"""
    return tuple(p[i] for i in q)


def perm_order(p):
    ident = tuple(range(len(p)))
    r, n = p, 1
    while r != ident:
        r = compose(p, r)
        n += 1
    return n


def main(argv):
    if len(argv) != 6 or argv[4] != '--out':
        sys.stderr.write('usage: reexpand_blocks.py MASTER_JSON RDTD_TXT CANDIDATE_TXT --out NEW.json\n')
        return 64
    t0 = time.perf_counter()
    c0 = time.process_time()
    master_path, rdtd_path, cand_path, out_path = argv[1], argv[2], argv[3], argv[5]
    raw = {}
    for key, path in (('master', master_path), ('rdtd', rdtd_path), ('candidate', cand_path)):
        with open(path, 'rb') as f:
            raw[key] = f.read()
    rep = collections.OrderedDict()
    rep['inputs'] = collections.OrderedDict((key, {'path': os.path.abspath(p), 'sha256': sha(raw[key]),
                                                  'bytes': len(raw[key])})
                                            for key, p in (('master', master_path), ('rdtd', rdtd_path),
                                                           ('candidate', cand_path)))
    rep['python'] = {'executable': sys.executable, 'version': platform.python_version(),
                     'optimize_flag': sys.flags.optimize}

    master = json.loads(raw['master'].decode('ascii'))
    mgroups = [list(g) for g in master['groups']]
    mblocks = [list(b) for b in master['blocks']]
    perms = [tuple(p) for p in master['permutations']]

    # RDTD: only header, GROUPS and BLOCKS are used.
    rl = raw['rdtd'].decode('ascii').split('\n')
    hdr = rl[0].split(' ')
    if hdr[0] != 'GDD34' or rl[1] != 'GROUPS':
        raise SystemExit('unexpected RDTD header')
    rk, rm = int(hdr[2]), int(hdr[3])
    rgroups = [[int(t) for t in rl[2 + i].split(' ')] for i in range(rk)]
    if rl[2 + rk] != 'BLOCKS':
        raise SystemExit('RDTD BLOCKS expected')
    rblocks = []
    i = 3 + rk
    while i < len(rl) and rl[i] and not rl[i].startswith('POINT'):
        rblocks.append([int(t) for t in rl[i].split(' ')])
        i += 1
    pos = {}
    for gi, g in enumerate(rgroups):
        for b, p in enumerate(g):
            pos[p] = (gi, b)
    rep['rdtd_header'] = rl[0]

    # candidate: GROUPS and BLOCKS sections only
    cl = raw['candidate'].decode('ascii').split('\n')
    chdr = cl[0].split(' ')
    ck, cm = int(chdr[2]), int(chdr[3])
    cgroups = [[int(t) for t in cl[2 + i].split(' ')] for i in range(ck)]
    if cl[2 + ck] != 'BLOCKS':
        raise SystemExit('candidate BLOCKS expected')
    cblocks = []
    i = 3 + ck
    while i < len(cl) and not cl[i].startswith('POINT'):
        cblocks.append(tuple(sorted(int(t) for t in cl[i].split(' '))))
        i += 1

    ing = collections.OrderedDict()
    ing['master_H_5_6_as_GDD_3_4_30_type_6^5'] = gdd_triple_check(mgroups, mblocks, 4)
    ing['rdtd_as_TD_3_4_3'] = gdd_triple_check(rgroups, rblocks, 4)
    zero_sum = set()
    for betas in itertools.product(range(rm), repeat=rk):
        if sum(betas) % rm == 0:
            zero_sum.add(tuple(betas))
    rdtd_betas = set()
    for b in rblocks:
        vec = [None] * rk
        for p in b:
            gi, beta = pos[p]
            vec[gi] = beta
        rdtd_betas.add(tuple(vec))
    ing['rdtd_blocks_equal_zero_sum_set'] = (rdtd_betas == zero_sum and len(rblocks) == len(zero_sum))
    ing['rdtd_position_equals_label_mod_3'] = all(pos[p][1] == p % rm and pos[p][0] == p // rm for p in pos)

    # informational: master permutations
    n = len(perms[0]) if perms else 0
    ident = tuple(range(n))
    pset = set(perms)
    mbset = set(frozenset(b) for b in mblocks)
    mgset = set(frozenset(g) for g in mgroups)
    pg = collections.OrderedDict()
    pg['count'] = len(perms)
    pg['distinct'] = len(pset)
    pg['all_bijections'] = all(sorted(p) == list(ident) for p in perms)
    pg['all_preserve_master_blocks'] = all(set(frozenset(p[x] for x in b) for b in mblocks) == mbset for p in perms)
    pg['all_preserve_group_partition'] = all(set(frozenset(p[x] for x in g) for g in mgroups) == mgset for p in perms)
    pg['contains_identity'] = ident in pset
    pg['closed_under_composition'] = all(compose(a, b) in pset for a in perms for b in perms)
    pg['regular_on_points'] = (sorted(p[0] for p in perms) == list(ident) and len(pset) == n)
    orders = collections.Counter(perm_order(p) for p in perms)
    pg['element_order_histogram'] = dict((str(a), b) for a, b in sorted(orders.items()))
    pg['abelian'] = all(compose(a, b) == compose(b, a) for a in perms for b in perms)
    pg['note'] = ('order-30 groups: C30 has 1 involution, C5xS3 3, C3xD5 5, D15 15; so 15 involutions and '
                  'closure identify D15')
    ing['master_permutations'] = pg
    rep['ingredient_checks_informational'] = ing

    # expansion
    inflated = []
    inflated_rev = []
    for b in mblocks:
        P = sorted(b)
        R = P[::-1]
        for rb in rblocks:
            q = []
            qr = []
            for p in rb:
                gi, beta = pos[p]
                q.append(3 * P[gi] + beta)
                qr.append(3 * R[gi] + beta)
            inflated.append(tuple(sorted(q)))
            inflated_rev.append(tuple(sorted(qr)))
    infl_groups = [sorted(3 * p + beta for p in g for beta in range(rm)) for g in mgroups]
    ci = collections.Counter(inflated)
    cc = collections.Counter(cblocks)
    missing = ci - cc
    extra = cc - ci
    cmp = collections.OrderedDict()
    cmp['inflated_blocks'] = len(inflated)
    cmp['inflated_distinct'] = len(ci)
    cmp['candidate_block_lines'] = len(cblocks)
    cmp['candidate_distinct'] = len(cc)
    cmp['multiset_equal'] = (ci == cc)
    cmp['in_inflation_not_in_candidate'] = sum(missing.values())
    cmp['in_candidate_not_in_inflation'] = sum(extra.values())
    cmp['examples_in_inflation_not_in_candidate'] = [list(t) for t in sorted(missing)[:5]]
    cmp['examples_in_candidate_not_in_inflation'] = [list(t) for t in sorted(extra)[:5]]
    cmp['candidate_line_order_equals_sorted_inflation'] = (cblocks == sorted(inflated))
    cmp['reversed_point_assignment_gives_same_multiset'] = (collections.Counter(inflated_rev) == ci)
    cmp['inflated_groups_equal_candidate_groups'] = ([sorted(g) for g in cgroups] == infl_groups)
    cmp['inflated_multiset_sha256'] = sha(('\n'.join(' '.join(map(str, t)) for t in sorted(inflated)) + '\n').encode())
    cmp['candidate_blocks_sorted_sha256'] = sha(('\n'.join(' '.join(map(str, t)) for t in sorted(cblocks)) + '\n').encode())
    cmp['frames'] = ('not reproduced: frames were found after inflation and are not determined by the master '
                     'blocks or the RDTD; only the block multiset is compared')
    rep['comparison'] = cmp
    rep['timing'] = {'wall_seconds': round(time.perf_counter() - t0, 4),
                     'cpu_seconds': round(time.process_time() - c0, 4)}
    ru = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rep['max_rss_bytes'] = ru if sys.platform == 'darwin' else ru * 1024
    with open(out_path, 'x') as f:
        f.write(json.dumps(rep, indent=1) + '\n')
    sys.stdout.write('multiset_equal=%s inflated=%d candidate=%d missing=%d extra=%d\n' % (
        cmp['multiset_equal'], len(inflated), len(cblocks), cmp['in_inflation_not_in_candidate'],
        cmp['in_candidate_not_in_inflation']))
    return 0 if cmp['multiset_equal'] else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
