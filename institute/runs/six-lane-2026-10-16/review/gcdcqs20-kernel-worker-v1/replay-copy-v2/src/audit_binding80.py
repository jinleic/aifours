#!/usr/bin/env python3
"""Bound literal audit: the Lean literals of Gc80/Data*.lean are the two raw certificates.

Usage: python3 -B audit_binding80.py LEAN_DIR NEW_RECEIPT.json      (refuses to overwrite)
  LEAN_DIR contains Gc80/Data*.lean (the pinned modules, or a regenerated copy).  The raw
  certificates are read from the review directory: $GC80_REVIEW if set, else the parent
  directory of this script.

Python standard library only; no Lean, and no code shared with gen_lean80.py.  For each of the
gcDCQS(20^4 : 0) certificate A and the mcDSQS(80) certificate:
  1. the raw certificate has its pinned SHA-256 and the strict layout (leading `#` lines; gc:
     `GCDCQS 80 4 20`, `COLOURS 40`, `HOLEFREE 10`, `GROUPS`, 4 lines of 20 numbers; mc:
     `MCDSQS 80`, `COLOURS 40`; then `BLOCKS` and exactly 19400 / 20540 lines of four numbers;
     then `POINT x` for x = 0..79 in order, each with `CLASS 0..39` in order, each followed by
     >= 1 line of three numbers; nothing else);
  2. the Lean literals equal the raw sections exactly: the block list (the chunks
     `blocks{Gc,Mc}80_k` in the order `List.flatten` lists them) equals the raw block lines in
     raw order, `col{Gc,Mc}80_x` equals the raw `POINT x` section (same classes, same triples,
     same order, same numbers) for every x, `colour{Gc,Mc}80 = [col_0, ..., col_79]`, and
     `groupsGc80` equals the raw GROUPS lines;
  3. an independent definition-first check of the raw certificates themselves.  gc: the groups
     are {20i, ..., 20i+19}; 19400 distinct 4-subsets of {0..79}; every 3-subset meeting two
     groups lies in exactly one block and no 3-subset of a group lies in any block; at every
     point x the 40 classes are nonempty, consist of pairwise disjoint 3-subsets avoiding x,
     list every derived triple exactly once (970 triples) and nothing else, and exactly 10 of
     them avoid G(x) \\ {x}.  mc: 20540 distinct 4-subsets, every 3-subset in exactly one
     block, at every point the 40 classes partition the 1027 derived triples into pairwise
     disjoint classes, and POINT 79 read on {0..78} is an STS(79).
Controls: the audit is re-run on in-memory corruptions with the SHA pin lifted; each must be
rejected by the literal check 2, and the definition-first check 3 run on the corrupted
certificate alone must reject the semantic corruptions and accept the pure reordering (which
only the verbatim binding detects).  The SHA pin itself is tested too.
"""
import ast
from collections import Counter
from datetime import datetime
import hashlib
from itertools import combinations
import json
import os
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
REVIEW = Path(os.environ.get('GC80_REVIEW', HERE.parent)).resolve()
V, R = 80, 40
NUM = r'(?:0|[1-9][0-9]*)'
SPECS = {
    'Gc': {'raw': 'gcdcqs20-parent-inputs-v1/gcdcqs20-e1s1_p10.txt',
           'sha256': '58b51b50b5281df613c5fae0a3b0178a374554a2f062e55bd8fc25250922a0ca',
           'head': ['GCDCQS 80 4 20', 'COLOURS 40', 'HOLEFREE 10', 'GROUPS'], 'ngroups': 4,
           'nblocks': 19400},
    'Mc': {'raw': 'mcdsqs80-parent-inputs-v1/mcdsqs80_c21_A.txt',
           'sha256': '49f500c5eedd9a79553e1228d0232e203a749bbda04e3a891c52778dbe9d44a3',
           'head': ['MCDSQS 80', 'COLOURS 40'], 'ngroups': 0, 'nblocks': 20540},
}


class AuditError(ValueError):
    def __init__(self, check, message):
        super().__init__(f'check {check}: {message}')
        self.check = check


def require(condition, check, message):
    if not condition:
        raise AuditError(check, message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def parse_raw(text, spec):
    require(text.endswith('\n') and '\r' not in text, 1, 'noncanonical line endings')
    lines = text.split('\n')[:-1]
    i = 0
    while i < len(lines) and lines[i].startswith('#'):
        i += 1
    require(lines[i:i + len(spec['head'])] == spec['head'], 1, 'header')
    i += len(spec['head'])
    groups = []
    for _ in range(spec['ngroups']):
        require(re.fullmatch(' '.join([NUM] * 20), lines[i]) is not None, 1, f'bad GROUPS line {lines[i]!r}')
        groups.append([int(t) for t in lines[i].split(' ')])
        i += 1
    require(lines[i] == 'BLOCKS', 1, 'BLOCKS header')
    i += 1
    blocks = []
    for line in lines[i:i + spec['nblocks']]:
        require(re.fullmatch(' '.join([NUM] * 4), line) is not None, 1, f'bad block line {line!r}')
        blocks.append(tuple(int(t) for t in line.split(' ')))
    require(len(blocks) == spec['nblocks'], 1, 'truncated block list')
    i += spec['nblocks']
    points = []
    for x in range(V):
        require(i < len(lines) and lines[i] == f'POINT {x}', 1, f'POINT {x} header')
        i += 1
        classes = []
        for j in range(R):
            require(i < len(lines) and lines[i] == f'CLASS {j}', 1, f'CLASS {j} header at {x}')
            i += 1
            cls = []
            while i < len(lines) and re.fullmatch(' '.join([NUM] * 3), lines[i]):
                cls.append(tuple(int(t) for t in lines[i].split(' ')))
                i += 1
            require(cls, 1, f'empty class {j} at {x}')
            classes.append(cls)
        points.append(classes)
    require(i == len(lines), 1, 'trailing lines')
    return groups, blocks, points


def parse_lean(lean_dir, key):
    gdir = Path(lean_dir) / 'Gc80'
    btext = (gdir / f'Data{key}B.lean').read_text()
    chunks = dict(re.findall(rf'def (blocks{key}80_\d+) : List RawQuad := (\[.*?\])\n', btext, re.S))
    m = re.search(rf'def blocks{key}80 : List RawQuad :=\n  List\.flatten \[\n(.*?)\]\n', btext, re.S)
    require(m is not None and chunks, 2, f'blocks{key}80 literal not found')
    order = [n for n in re.split(r'[\s,]+', m.group(1)) if n]
    require(sorted(order) == sorted(chunks) and len(order) == len(set(order)), 2,
            f'blocks{key}80 does not flatten exactly its chunks')
    blocks = [tuple(b) for name in order for b in ast.literal_eval(chunks[name])]
    groups = []
    if key == 'Gc':
        mg = re.search(r'def groupsGc80 : List \(List ℕ\) := (\[.*?\])\n', btext, re.S)
        require(mg is not None, 2, 'groupsGc80 literal not found')
        groups = [list(g) for g in ast.literal_eval(mg.group(1))]
    cols = {}
    for m in range(V // 10):
        ptext = (gdir / f'Data{key}P{m}.lean').read_text()
        for name, body in re.findall(rf'def (col{key}80_\d+) : List \(List RawTriple\) := (\[.*?\])\n',
                                     ptext, re.S):
            require(name not in cols, 2, f'{name} defined twice')
            cols[name] = [[tuple(t) for t in c] for c in ast.literal_eval(re.sub(r'--[^\n]*', '', body))]
    ctext = (gdir / f'Data{key}.lean').read_text()
    m2 = re.search(rf'def colour{key}80 : List \(List \(List RawTriple\)\) := \[\n(.*?)\]\n', ctext, re.S)
    require(m2 is not None, 2, f'colour{key}80 literal not found')
    names = [n for n in re.split(r'[\s,]+', m2.group(1)) if n]
    require(names == [f'col{key}80_{x}' for x in range(V)] and sorted(cols) == sorted(names), 2,
            f'colour{key}80 is not [col{key}80_0, ..., col{key}80_79]')
    return groups, blocks, [cols[n] for n in names]


def check_classes(x, classes, derived, check):
    require(len(classes) == R, check, f'POINT {x}: not 40 classes')
    listed = []
    for cls in classes:
        sets = [frozenset(t) for t in cls]
        require(sets and all(len(t) == 3 and max(t) < V and x not in t for t in sets), check,
                f'POINT {x}: bad triple')
        union = set()
        for t in sets:
            require(not (union & t), check, f'POINT {x}: class not pairwise disjoint')
            union |= t
        listed.extend(sets)
    require(len(listed) == len(set(listed)) and set(listed) == derived, check,
            f'POINT {x}: classes do not partition the derived design')
    return len(listed)


def semantic_check(key, groups, blocks, points):
    """Definition-first check of the raw certificate (check 3)."""
    spec = SPECS[key]
    bsets = [frozenset(b) for b in blocks]
    require(all(len(b) == 4 and max(b) < V for b in bsets), 3, 'block is not a 4-subset of 0..79')
    require(len(set(bsets)) == spec['nblocks'], 3, 'duplicate block')
    count = Counter(t for b in bsets for t in combinations(sorted(b), 3))
    out = {'blocks': len(bsets), 'points': V, 'classes_per_point': R}
    if key == 'Gc':
        require([sorted(g) for g in groups] == [list(range(20 * i, 20 * i + 20)) for i in range(4)], 3,
                'GROUPS are not {20i, ..., 20i+19}')
        grp = {p: i for i, g in enumerate(groups) for p in g}
        inside = outside = 0
        for t in combinations(range(V), 3):
            if len({grp[p] for p in t}) == 1:
                require(count.get(t, 0) == 0, 3, f'group 3-subset {t} lies in a block')
                inside += 1
            else:
                require(count.get(t, 0) == 1, 3, f'3-subset {t} is not in exactly one block')
                outside += 1
        require(sum(count.values()) == outside, 3, 'block 3-subset count')
        holefree, triples = [], set()
        for x in range(V):
            derived = {b - {x} for b in bsets if x in b}
            triples.add(check_classes(x, points[x], derived, 3))
            hole = set(groups[grp[x]]) - {x}
            holefree.append(sum(1 for cls in points[x] if all(not (set(t) & hole) for t in cls)))
        require(set(holefree) == {10}, 3, f'hole-free class counts {sorted(set(holefree))}')
        out.update({'non_group_3_subsets_covered_once': outside, 'group_3_subsets_uncovered': inside,
                    'derived_triples_per_point': sorted(triples), 'hole_free_classes_per_point': 10})
    else:
        require(len(count) == 82160 and set(count.values()) == {1}, 3,
                'some 3-subset is not in exactly one block')
        triples = set()
        for x in range(V):
            derived = {b - {x} for b in bsets if x in b}
            triples.add(check_classes(x, points[x], derived, 3))
        sts = [frozenset(t) for cls in points[79] for t in cls]
        pairs = [p for t in sts for p in combinations(sorted(t), 2)]
        require(all(max(t) < 79 for t in sts) and len(pairs) == len(set(pairs)) == 3081, 3,
                'POINT 79 read on 0..78 is not an STS(79)')
        out.update({'three_subsets_covered_once': len(count), 'derived_triples_per_point': sorted(triples),
                    'point79_sts79_pairs_covered_once': 3081})
    out['class_size_profiles'] = sorted({tuple(sorted(len(c) for c in p)) for p in points})
    return out


def audit(key, raw_bytes, lean_dir, sha_pin=None):
    spec = SPECS[key]
    require(sha256(raw_bytes) == (sha_pin or spec['sha256']), 1, 'raw SHA-256 mismatch')
    raw = parse_raw(raw_bytes.decode('ascii'), spec)
    lean = parse_lean(lean_dir, key)
    require(lean[0] == raw[0], 2, 'groups literal differs from the raw GROUPS lines')
    require(lean[1] == raw[1], 2, 'block literal differs from the raw block lines')
    for x in range(V):
        require(lean[2][x] == raw[2][x], 2, f'col{key}80_{x} differs from the raw POINT {x} section')
    return semantic_check(key, *raw)


def corrupt(text, kind):
    lines = text.split('\n')
    if kind == 'block_line':
        i = lines.index('BLOCKS') + 1
        a, b, c, d = map(int, lines[i].split(' '))
        lines[i] = f'{a} {b} {c} {d - 1 if d - 1 > c else d + 1}'
        return '\n'.join(lines), True
    if kind == 'point0_reorder':
        i = lines.index('POINT 0') + 2
        lines[i], lines[i + 1] = lines[i + 1], lines[i]
        return '\n'.join(lines), False
    if kind == 'point7_swap':
        i = lines.index('POINT 7') + 2
        t1, t2 = lines[i].split(' '), lines[i + 1].split(' ')
        t1[0], t2[0] = t2[0], t1[0]
        lines[i] = ' '.join(map(str, sorted(map(int, t1))))
        lines[i + 1] = ' '.join(map(str, sorted(map(int, t2))))
        return '\n'.join(lines), True
    if kind == 'point7_copy0':
        i0, i1 = lines.index('POINT 0'), lines.index('POINT 1')
        i7, i8 = lines.index('POINT 7'), lines.index('POINT 8')
        lines[i7 + 1:i8] = lines[i0 + 1:i1]
        return '\n'.join(lines), True
    if kind == 'groups_swap':
        i = lines.index('GROUPS') + 1
        g1, g2 = lines[i].split(' '), lines[i + 1].split(' ')
        g1[-1], g2[0] = g2[0], g1[-1]
        lines[i], lines[i + 1] = ' '.join(g1), ' '.join(g2)
        return '\n'.join(lines), True
    raise ValueError(kind)


def run_controls(key, raw_bytes, lean_dir):
    results = {}
    text = raw_bytes.decode('ascii')
    kinds = ['block_line', 'point0_reorder', 'point7_swap', 'point7_copy0']
    if key == 'Gc':
        kinds.append('groups_swap')
    for kind in kinds:
        bad_text, semantic_expected = corrupt(text, kind)
        bad = bad_text.encode('ascii')
        try:
            audit(key, bad, lean_dir, sha_pin=sha256(bad))
            outcome = {'rejected': False}
        except AuditError as exc:
            outcome = {'rejected': True, 'check': exc.check, 'reason': str(exc)}
        try:
            semantic_check(key, *parse_raw(bad_text, SPECS[key]))
            outcome['semantic_rejected'] = False
        except AuditError as exc:
            outcome['semantic_rejected'] = True
            outcome['semantic_reason'] = str(exc)
        outcome['intended_check'] = 2
        outcome['semantic_rejection_expected'] = semantic_expected
        outcome['as_intended'] = (outcome['rejected'] and outcome.get('check') == 2 and
                                  outcome['semantic_rejected'] == semantic_expected)
        outcome['corrupted_sha256'] = sha256(bad)
        results[kind] = outcome
    try:
        audit(key, raw_bytes + b'\n', lean_dir)
        results['sha_pin'] = {'rejected': False, 'as_intended': False}
    except AuditError as exc:
        results['sha_pin'] = {'rejected': True, 'check': exc.check, 'reason': str(exc),
                              'as_intended': exc.check == 1}
    return results


def main(argv):
    if len(argv) != 2:
        raise SystemExit(__doc__)
    lean_dir, out = Path(argv[0]), Path(argv[1])
    if out.exists():
        raise SystemExit('Refusing to overwrite receipt')
    receipt = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
               'auditor_sha256': sha256(Path(__file__).read_bytes()),
               'review_dir': str(REVIEW), 'lean_dir': str(lean_dir.resolve()), 'designs': {}}
    rc = 0
    for key, spec in SPECS.items():
        raw_bytes = (REVIEW / spec['raw']).read_bytes()
        mods = [f'Gc80/Data{key}B.lean'] + [f'Gc80/Data{key}P{m}.lean' for m in range(8)] + [f'Gc80/Data{key}.lean']
        entry = {'raw': {'path': f'review/{spec["raw"]}', 'sha256': sha256(raw_bytes)},
                 'lean_data_modules': {m: sha256((lean_dir / m).read_bytes()) for m in mods}}
        try:
            entry['result'] = audit(key, raw_bytes, lean_dir)
            entry['status'] = 'PASS'
        except AuditError as exc:
            entry['status'] = 'FAIL'
            entry['error'] = str(exc)
            rc = 1
        entry['controls'] = run_controls(key, raw_bytes, lean_dir)
        if not all(c['as_intended'] for c in entry['controls'].values()):
            entry['status'] = 'CONTROLS_FAIL'
            rc = 1
        receipt['designs'][key] = entry
    receipt['status'] = 'BINDING_AUDIT_PASS' if rc == 0 else 'BINDING_AUDIT_FAIL'
    with out.open('x') as stream:
        json.dump(receipt, stream, indent=1)
        stream.write('\n')
    print(json.dumps({'status': receipt['status'],
                      'designs': {k: {'status': e['status'],
                                      'controls': {c: o['as_intended'] for c, o in e['controls'].items()}}
                                  for k, e in receipt['designs'].items()}}))
    return rc


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
