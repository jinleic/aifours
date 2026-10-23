#!/usr/bin/env python3
"""Mutation controls for checker A (outer/code/cert_cells.py) on a finished certificate.

Usage: mutation_controls.py CERT.json RESULT.json [--only a,b,c,d,e,f,g] [--tmpdir DIR]
Mutations (each applied to a fresh copy of the certificate, then checked by cert_cells.main):
  g  unmodified control (must PASS)
  a  one y entry (largest |y_e|) of a chosen leaf multiplied by 1.1      [leaf near a secondary max; leaf nearest n*]
  b  mu0 of one class of a chosen leaf replaced by a far point (mu0 * (1,1,1,2^10))   [same two leaves]
  c  L* lowered by 0.02 (checker constant patched in-process); failing leaves located
  d  one subtree dropped (second child of a split at depth ~8); replay must fail
  e  r0 replaced by 1/5000 and checked with --require-r0 1/10000
  f  a dual leaf whose cell is not inside the box relabelled 'C'
Leaf choice uses float margins recomputed here (outer/code/fastdual.py); this script is not trusted.
"""
import argparse
import copy
import hashlib
import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fastdual as fd  # noqa: E402
import bnb_produce as bp  # noqa: E402
import cert_cells as cc  # noqa: E402
from flint import arb  # noqa: E402


def replay(cert):
    """Preorder replay with exact integer vertices: returns list of (pos, kind, cell, depth)."""
    out = []
    nodes = cert['tree']
    fi, fj = cert['facet']
    stack = [(bp.root_cell(fi, fj), 0)]
    pos = 0
    while stack:
        cell, d = stack.pop()
        node = nodes[pos]
        out.append((pos, node[0], cell, d))
        pos += 1
        if node[0] == 'S':
            c1, c2 = bp.split_cell(cell, node[1], node[2])
            stack.append((c2, d + 1))
            stack.append((c1, d + 1))
    assert pos == len(nodes)
    return out


def float_margin(node, cell):
    y = np.array([float.fromhex(x) for x in node[1]])
    mu = np.array([[float.fromhex(x) for x in m] for m in node[2]])
    a = fd.a_from_mu(fd.zmat(y), mu)
    V9 = bp.cell_v9(cell)
    U = V9 @ a + fd.ent(V9)
    return float(fd.LSTAR - U.max()), V9, int(np.argmax(U))


def loc(V9):
    c = V9.mean(axis=0)
    return {'r_centroid': float(np.linalg.norm(c - 1 / 9)), 'min_n_centroid': float(c.min()),
            'centroid9': [round(float(x), 6) for x in c]}


def run_check(cert, tmpdir, name, require_r0=None, lstar_shift=None):
    path = os.path.join(tmpdir, f'mut_{name}.json')
    raw = json.dumps(cert, separators=(',', ':')).encode()
    with open(path, 'wb') as f:
        f.write(raw)
    saved = cc.LSTAR
    if lstar_shift is not None:
        cc.LSTAR = saved - arb(lstar_shift)
    try:
        res = cc.main(path, require_r0, progress_every=0)
    finally:
        cc.LSTAR = saved
    return path, hashlib.sha256(raw).hexdigest(), res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('cert')
    ap.add_argument('result')
    ap.add_argument('--only', default='g,a,b,c,d,e,f')
    ap.add_argument('--tmpdir', default='/tmp/outer_mutations')
    args = ap.parse_args()
    os.makedirs(args.tmpdir, exist_ok=True)
    np.seterr(all='ignore')
    which = set(args.only.split(','))
    base = json.load(open(args.cert))
    base_sha = hashlib.sha256(open(args.cert, 'rb').read()).hexdigest()
    rep = replay(base)
    leaves = []
    for pos, kind, cell, d in rep:
        if kind == 'D':
            mg, V9, iv = float_margin(base['tree'][pos], cell)
            leaves.append((mg, pos, cell, d, V9, iv))
    leaves.sort(key=lambda t: t[0])
    sec = [t for t in leaves if loc(t[4])['r_centroid'] > 0.35]
    choice = {'nstar': leaves[0], 'secmax': sec[0] if sec else leaves[-1]}
    out = {'cert': args.cert, 'cert_sha256': base_sha, 'started': bp.now(), 'mutations': []}
    out['chosen_leaves'] = {k: {'pos': v[1], 'float_margin': v[0], 'depth': v[3], **loc(v[4])}
                            for k, v in choice.items()}

    def record(tag, desc, expect, path, sha, res, extra=None):
        ent = {'id': tag, 'description': desc, 'expected': expect, 'verdict': res['verdict'],
               'failed_leaves': res['failed'], 'reason': res['reason'], 'mutated_file': path,
               'mutated_sha256': sha, 'checker_runtime_s': res['runtime_s'],
               'min_margin': res['min_margin'], 'rejected': res['verdict'] == 'FAIL'}
        if extra:
            ent.update(extra)
        out['mutations'].append(ent)
        print(json.dumps({k: ent[k] for k in ('id', 'verdict', 'failed_leaves', 'reason')}), flush=True)
        return ent

    if 'g' in which:
        p, s, r = run_check(base, args.tmpdir, 'g_control')
        record('g', 'unmodified certificate', 'PASS', p, s, r)
    for key, (mg, pos, cell, d, V9, iv) in choice.items():
        node = base['tree'][pos]
        if 'a' in which:
            m = copy.deepcopy(base)
            y = [float.fromhex(x) for x in node[1]]
            e = int(np.argmax(np.abs(y)))
            m['tree'][pos][1][e] = (y[e] * 1.1).hex()
            p, s, r = run_check(m, args.tmpdir, f'a_{key}')
            record(f'a_{key}', f'leaf {pos} ({key}): y[{e}] = {y[e]:.6g} multiplied by 1.1',
                   'FAIL (expected for a tight leaf; not guaranteed)', p, s, r,
                   {'leaf_float_margin': mg, 'failed_at': r['failed_at'][:5]})
        if 'b' in which:
            m = copy.deepcopy(base)
            u = int(np.argmax(V9[iv]))
            mu = [float.fromhex(x) for x in node[2][u]]
            far = [mu[0], mu[1], mu[2], mu[3] * 1024.0]
            m['tree'][pos][2][u] = [x.hex() for x in far]
            p, s, r = run_check(m, args.tmpdir, f'b_{key}')
            record(f'b_{key}', f'leaf {pos} ({key}): mu0 of class {u} replaced by mu0*(1,1,1,2^10)',
                   'FAIL', p, s, r, {'leaf_float_margin': mg, 'failed_at': r['failed_at'][:5]})
    if 'c' in which:
        p, s, r = run_check(base, args.tmpdir, 'c_lstar', lstar_shift=0.02)
        pred = [t for t in leaves if t[0] < 0.02]
        predpos = {t[1] for t in pred}
        locs = [loc(t[4]) for t in pred]
        near_star = sum(1 for L in locs if L['r_centroid'] < 0.15)
        far = [L for L in locs if L['r_centroid'] > 0.35]
        listed_ok = all(fa[0] in predpos for fa in r['failed_at'])
        record('c', 'L* lowered by 0.02 (checker constant patched in-process)',
               'FAIL; rejects leaves near n* (margin ~1.16 r^2) and near the secondary maxima (0.0106)',
               p, s, r, {'float_predicted_failures': len(pred),
                         'checker_failed_positions_subset_of_predicted': listed_ok,
                         'predicted_r_lt_0.15': near_star, 'predicted_r_gt_0.35': len(far),
                         'predicted_r_gt_0.35_min_n_range': [min((L['min_n_centroid'] for L in far), default=None),
                                                             max((L['min_n_centroid'] for L in far), default=None)],
                         'predicted_examples_far': far[:5],
                         'leaves_total': len(leaves),
                         'leaves_r_gt_0.35_total': sum(1 for t in leaves if loc(t[4])['r_centroid'] > 0.35)})
    if 'd' in which:
        m = copy.deepcopy(base)
        target = next(t for t in rep if t[1] == 'S' and t[3] >= 8)
        pos = target[0]
        # find the extent of the second child's subtree: skip first child subtree, then second
        def subtree_end(i):
            need = 1
            while need:
                need += 2 if m['tree'][i][0] == 'S' else 0
                need -= 1
                i += 1
            return i
        first_end = subtree_end(pos + 1)
        second_end = subtree_end(first_end)
        dropped = second_end - first_end
        del m['tree'][first_end:second_end]
        p, s, r = run_check(m, args.tmpdir, 'd_drop')
        record('d', f'second child subtree of split node {pos} (depth {target[3]}) dropped ({dropped} nodes)',
               'FAIL (replay misaligned/truncated)', p, s, r)
    if 'e' in which:
        m = copy.deepcopy(base)
        m['r0'] = '1/5000'
        p, s, r = run_check(m, args.tmpdir, 'e_r0', require_r0='1/10000')
        record('e', "cert['r0'] replaced by 1/5000, checked with --require-r0 1/10000", 'FAIL', p, s, r)
    if 'f' in which:
        m = copy.deepcopy(base)
        cands = [t for t in leaves if loc(t[4])['r_centroid'] < 0.01] or leaves
        pos = cands[0][1]
        m['tree'][pos] = ['C']
        p, s, r = run_check(m, args.tmpdir, 'f_fakeC')
        record('f', f'dual leaf {pos} (r_centroid {loc(cands[0][4])["r_centroid"]:.3g}) relabelled C', 'FAIL',
               p, s, r)
    out['finished'] = bp.now()
    with open(args.result, 'w') as f:
        json.dump(out, f, indent=1)


if __name__ == '__main__':
    main()
