#!/usr/bin/env python3
"""make_controls_v1.py -- builds intended-reason corruption fixtures for check_k7_stageB_v2.py.

Reads only the pinned inputs under ../inputs/.  Every fixture directory, file and manifest is created
exclusively (no overwrite).  Unchanged files are byte-identical copies.  Mutated gzip members are
recompressed with mtime=0.  Expected outcomes are written into each manifest BEFORE any control run.
Stdlib only; does not import the checker or any producer code.
"""
import gzip
import hashlib
import json
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
INP = os.path.join(HERE, '..', 'inputs')
NAMES = ['leaves.jsonl.gz', 'lp_duals.json.gz', 'vfc_killed.json.gz', 'survivors.json', 'run.json']


def sha(b):
    return hashlib.sha256(b).hexdigest()


def load(U):
    return {n: open(os.path.join(INP, 'stageB-' + U, n), 'rb').read() for n in NAMES}


def gz(text):
    return gzip.compress(text.encode('utf-8'), mtime=0)


def leaves_lines(raw):
    t = gzip.decompress(raw).decode('utf-8')
    assert t.endswith('\n')
    return t[:-1].split('\n')


def dump_line(obj):
    return json.dumps(obj, separators=(',', ':'))


def write_fixture(cid, U, files, mutated, desc, expected):
    d = os.path.join(HERE, cid, 'stageB-' + U)
    os.makedirs(d)                         # fails if it exists
    rec = {}
    for n in NAMES:
        with open(os.path.join(d, n), 'xb') as fh:
            fh.write(files[n])
        os.chmod(os.path.join(d, n), 0o444)
        rec[n] = sha(files[n])
    man = {'control': cid, 'universe': U, 'description': desc, 'mutated_file': mutated,
           'original_sha256_of_mutated_file': sha(load(U)[mutated]),
           'expected_outcome_preregistered': expected,
           'universes': {U: {'dir': cid + '/stageB-' + U, 'files': rec}}}
    mp = os.path.join(HERE, 'manifest-' + cid + '.json')
    with open(mp, 'x') as fh:
        fh.write(json.dumps(man, indent=1, sort_keys=True) + '\n')
    os.chmod(mp, 0o444)
    return mp, sha(open(mp, 'rb').read())


def first_P(lines):
    for li, s in enumerate(lines):
        o = json.loads(s)
        for ci, c in enumerate(o['witness'][1]):
            if c[0] == 'P':
                return li, ci, o
    raise SystemExit('no P cert')


def main():
    out = []
    kii = load('KII')
    k52 = load('K52')
    L = leaves_lines(kii['leaves.jsonl.gz'])

    # C1 missing coverage: drop leaf line 1 (index 0)
    f = dict(kii)
    f['leaves.jsonl.gz'] = gz('\n'.join(L[1:]) + '\n')
    out.append(write_fixture('C1-KII-drop-leaf-line', 'KII', f, 'leaves.jsonl.gz',
                             'leaf line 1 removed (orbit canon %s)' % json.loads(L[0])['canon'],
                             {'status': 'INVALID', 'must_include': ['LEAF_LINE_MISSING']}))

    # C2 wrong sign: first P cert with a nonzero u/l entry, negate that entry
    done = False
    for li, s in enumerate(L):
        o = json.loads(s)
        for ci, c in enumerate(o['witness'][1]):
            if c[0] == 'P':
                for k in range(12, 42):
                    if Fraction(c[1][k]) != 0:
                        old = c[1][k]
                        c[1][k] = str(-Fraction(old))
                        L2 = list(L)
                        L2[li] = dump_line(o)
                        f = dict(kii)
                        f['leaves.jsonl.gz'] = gz('\n'.join(L2) + '\n')
                        out.append(write_fixture(
                            'C2-KII-P-negate-ul', 'KII', f, 'leaves.jsonl.gz',
                            'line %d cert %d vec[%d] %s -> %s (u/l block)' % (li + 1, ci, k, old, c[1][k]),
                            {'status': 'INVALID', 'must_include': ['LEAF_RPLP_P_NEGATIVE_UL']}))
                        done = True
                        break
            if done:
                break
        if done:
            break

    # C3 missing q: first line with >= 2 certs, drop its last cert
    for li, s in enumerate(L):
        o = json.loads(s)
        if len(o['witness'][1]) >= 2:
            n0 = len(o['witness'][1])
            o['witness'][1] = o['witness'][1][:-1]
            L2 = list(L)
            L2[li] = dump_line(o)
            f = dict(kii)
            f['leaves.jsonl.gz'] = gz('\n'.join(L2) + '\n')
            out.append(write_fixture('C3-KII-drop-last-q', 'KII', f, 'leaves.jsonl.gz',
                                     'line %d: last of %d certs removed' % (li + 1, n0),
                                     {'status': 'INVALID', 'must_include': ['LEAF_RPLP_CERT_COUNT']}))
            break

    # C4 altered alpha: line 1, first edge position with g >= 3, alpha a -> a % (g-1) + 1
    o = json.loads(L[0])
    prof = o['prof']

    def gpp(a, b):
        return 2 ** min(a[0], b[0]) * 3 ** min(a[1], b[1]) * 5 ** min(a[2], b[2])
    edges = [(i, j) for i in range(7) for j in range(i + 1, 7)]
    rep = list(o['rep'])
    for t, (i, j) in enumerate(edges):
        g = gpp(prof[i], prof[j])
        if g >= 3:
            a = int(rep[t])
            rep[t] = str(a % (g - 1) + 1)
            break
    o['rep'] = ''.join(rep)
    L2 = list(L)
    L2[0] = dump_line(o)
    f = dict(kii)
    f['leaves.jsonl.gz'] = gz('\n'.join(L2) + '\n')
    out.append(write_fixture('C4-KII-alter-rep-alpha', 'KII', f, 'leaves.jsonl.gz',
                             'line 1 rep edge %d alpha %d -> %s (canon unchanged)' % (t, a, rep[t]),
                             {'status': 'INVALID', 'must_include': ['LEAF_REP_CANON_MISMATCH', 'LEAF_LINE_MISSING']}))

    # C5 altered profile: line 1, Y-vertex profile -> [1,1,1] (outside the Y domain)
    o = json.loads(L[0])
    old = o['prof'][1]
    o['prof'][1] = [1, 1, 1]
    L2 = list(L)
    L2[0] = dump_line(o)
    f = dict(kii)
    f['leaves.jsonl.gz'] = gz('\n'.join(L2) + '\n')
    out.append(write_fixture('C5-KII-alter-profile', 'KII', f, 'leaves.jsonl.gz',
                             'line 1 prof[1] %r -> [1,1,1]' % (old,),
                             {'status': 'INVALID', 'must_include': ['LEAF_PROF_NOT_A_REPRESENTATIVE', 'LEAF_LINE_MISSING']}))

    # C6 wrong P coefficient: first P cert, b_0 += 2 - LHS(A = N, S = empty)
    li, ci, o = first_P(L)
    vec = [Fraction(x) for x in o['witness'][1][ci][1]]
    lhs_full = sum(vec[6:12]) + sum(vec[27:42]) - sum(vec[12:27])
    delta = 2 - lhs_full
    vec[6] += delta
    o['witness'][1][ci][1] = [str(x) for x in vec]
    L2 = list(L)
    L2[li] = dump_line(o)
    f = dict(kii)
    f['leaves.jsonl.gz'] = gz('\n'.join(L2) + '\n')
    out.append(write_fixture('C6-KII-P-coefficient', 'KII', f, 'leaves.jsonl.gz',
                             'line %d cert %d: b_0 += %s so the column (A=N, S=empty) has LHS 2' % (li + 1, ci, delta),
                             {'status': 'INVALID', 'must_include': ['LEAF_RPLP_P_STAR']}))

    # C7 wrong scaling: first P cert scaled by 2^-k, k minimal with 2^-k * (sum|a|+sum|b|+2sum|u|+2sum|l|) < 1
    li, ci, o = first_P(L)
    vec = [Fraction(x) for x in o['witness'][1][ci][1]]
    bnd = sum(abs(x) for x in vec[0:12]) + 2 * sum(abs(x) for x in vec[12:42])
    k = 1
    while Fraction(bnd, 2 ** k) >= 1:
        k += 1
    o['witness'][1][ci][1] = [str(x / 2 ** k) for x in vec]
    L2 = list(L)
    L2[li] = dump_line(o)
    f = dict(kii)
    f['leaves.jsonl.gz'] = gz('\n'.join(L2) + '\n')
    out.append(write_fixture('C7-KII-P-scaled', 'KII', f, 'leaves.jsonl.gz',
                             'line %d cert %d: whole P vector scaled by 1/2^%d (|obj| bound %s); (*) and u,l>=0 stay valid'
                             % (li + 1, ci, k, bnd),
                             {'status': 'INVALID', 'must_include': ['LEAF_RPLP_P_OBJECTIVE']}))

    # C8 R/VFC dual scaled by 1/2 (KII): key of the first R cert in line order
    d = json.loads(gzip.decompress(kii['lp_duals.json.gz']).decode('utf-8'))
    rkey = None
    for s in L:
        for c in json.loads(s)['witness'][1]:
            if c[0] == 'R':
                rkey = c[1]
                break
        if rkey:
            break
    items = [p.split(',') for p in rkey.split(';')]
    y = [Fraction(t) for t in d[rkey]['y']]
    obj0 = sum(Fraction(it[0]) * yy for it, yy in zip(items, y))
    y2 = [yy / 2 for yy in y]
    obj1 = sum(Fraction(it[0]) * yy for it, yy in zip(items, y2))
    assert obj0 >= 1 > obj1
    d[rkey]['y'] = [str(t) for t in y2]
    f = dict(kii)
    f['lp_duals.json.gz'] = gz(json.dumps(d, separators=(',', ':')))
    out.append(write_fixture('C8-KII-dual-scaled-half', 'KII', f, 'lp_duals.json.gz',
                             'dual of key %s (first R cert) scaled by 1/2: objective %s -> %s' % (rkey, obj0, obj1),
                             {'status': 'INVALID', 'must_include': ['LP_DUAL_ENTRY_DUAL_OBJECTIVE', 'LEAF_RPLP_R_DUAL_OBJECTIVE']}))

    # C9 dual wrong sign (KII): first key in file order with a positive y, negate its first positive entry
    d = json.loads(gzip.decompress(kii['lp_duals.json.gz']).decode('utf-8'))
    for key, ent in d.items():
        ys = [Fraction(t) for t in ent['y']]
        pos = [x for x, t in enumerate(ys) if t > 0]
        if pos:
            ent['y'][pos[0]] = str(-ys[pos[0]])
            break
    f = dict(kii)
    f['lp_duals.json.gz'] = gz(json.dumps(d, separators=(',', ':')))
    out.append(write_fixture('C9-KII-dual-negative', 'KII', f, 'lp_duals.json.gz',
                             'dual of key %s: y[%d] negated' % (key, pos[0]),
                             {'status': 'INVALID', 'must_include': ['LP_DUAL_ENTRY_DUAL_NEGATIVE']}))

    # C10 dual wrong coefficient (KII): same first key, its first positive y entry += 1 (singleton packing > 1)
    d = json.loads(gzip.decompress(kii['lp_duals.json.gz']).decode('utf-8'))
    for key, ent in d.items():
        ys = [Fraction(t) for t in ent['y']]
        pos = [x for x, t in enumerate(ys) if t > 0]
        if pos:
            ent['y'][pos[0]] = str(ys[pos[0]] + 1)
            break
    f = dict(kii)
    f['lp_duals.json.gz'] = gz(json.dumps(d, separators=(',', ':')))
    out.append(write_fixture('C10-KII-dual-packing', 'KII', f, 'lp_duals.json.gz',
                             'dual of key %s: y[%d] += 1' % (key, pos[0]),
                             {'status': 'INVALID', 'must_include': ['LP_DUAL_ENTRY_DUAL_PACKING']}))

    # C11 K52 VFC dual scaled by 1/2: first key in file order
    d = json.loads(gzip.decompress(k52['lp_duals.json.gz']).decode('utf-8'))
    key = next(iter(d))
    items = [p.split(',') for p in key.split(';')]
    y = [Fraction(t) for t in d[key]['y']]
    obj0 = sum(Fraction(it[0]) * yy for it, yy in zip(items, y))
    obj1 = obj0 / 2
    assert obj0 >= 1 > obj1
    d[key]['y'] = [str(t / 2) for t in y]
    f = dict(k52)
    f['lp_duals.json.gz'] = gz(json.dumps(d, separators=(',', ':')))
    out.append(write_fixture('C11-K52-dual-scaled-half', 'K52', f, 'lp_duals.json.gz',
                             'dual of key %s scaled by 1/2: objective %s -> %s' % (key, obj0, obj1),
                             {'status': 'INVALID', 'must_include': ['LP_DUAL_ENTRY_DUAL_OBJECTIVE', 'VFC_SIGNATURE_SIG_Q_DUAL_OBJECTIVE']}))

    # I1 informative (not counted): K52 first vfc_killed signature removed (coverage consequence unknown a priori)
    v = json.loads(gzip.decompress(k52['vfc_killed.json.gz']).decode('utf-8'))
    s0 = v[0]
    f = dict(k52)
    f['vfc_killed.json.gz'] = gz(json.dumps(v[1:], separators=(',', ':')))
    out.append(write_fixture('I1-K52-drop-first-signature', 'K52', f, 'vfc_killed.json.gz',
                             'first listed signature removed: %s' % json.dumps(s0),
                             {'status': 'not COMPLETE_VALID unless the expanded nodes close by other verified rules',
                              'informative_only': True}))

    for mp, h in out:
        print(h, os.path.relpath(mp, HERE))


if __name__ == '__main__':
    sys.exit(main())
