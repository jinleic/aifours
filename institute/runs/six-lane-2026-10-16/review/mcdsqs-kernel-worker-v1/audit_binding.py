#!/usr/bin/env python3
"""Bound literal audit: the Lean literals of McdKernel/Data38.lean are the raw mcDSQS(38) certificate.

Usage: python3 -B audit_binding.py NEW_RECEIPT.json      (refuses to overwrite)

Python standard library only; no Lean, and no code shared with gen_lean.py.  Checks:
  1. the raw certificate has its pinned SHA-256 and the strict layout: leading `#` lines,
     `MCDSQS 38`, `COLOURS 19`, `BLOCKS`, 2109 lines of four numbers, then `POINT x` for
     x = 0..37 in order, each with `CLASS 0..18` in order, each followed by >= 1 line of three
     numbers;
  2. the Lean literals equal the raw sections exactly: `blocks38` (the concatenation of the
     chunks `blocks38_k`, in the order the module concatenates them) equals the raw block lines
     in raw order, and `col38_x` equals the raw `POINT x` section (same classes, same triples,
     same order, same numbers) for every x, with `colour38 = [col38_0, ..., col38_37]`;
  3. an independent definition-first check of the raw certificate itself: every block has four
     distinct points below 38; every 3-subset of {0..37} lies in exactly one block; at every point
     x the 19 classes are nonempty, consist of pairwise disjoint 3-subsets avoiding x, every
     listed triple plus x is a block, and every derived triple is listed exactly once.  The
     raw `POINT 37` section, read on {0..36}, is an STS(37) (every pair in exactly one listed
     triple).
Controls: the audit is re-run on in-memory corruptions with the SHA pin lifted; each must be
rejected by the literal check 2, and the definition-first check 3 run on the corrupted
certificate alone must reject the semantic corruptions (one block line changed; two points
swapped between two triples of POINT 7; POINT 7 replaced by POINT 0) and accept the pure
reordering (two triple lines of POINT 0 exchanged), which only the verbatim binding detects.
The SHA pin itself is tested too.
"""
import ast
from datetime import datetime
import hashlib
from itertools import combinations
import json
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
REVIEW = HERE.parent
RAW = 'mcdsqs38-parent-inputs-v1/mcdsqs38_g342_s0.txt'
RAW_SHA256 = '973f93e4646e48df64b70b3a64811afcdc87b10a1767222f54ffe65d3a303f1c'
V, R, NB = 38, 19, 2109
NUM = r'(?:0|[1-9][0-9]*)'


class AuditError(ValueError):
    def __init__(self, check, message):
        super().__init__(f'check {check}: {message}')
        self.check = check


def require(condition, check, message):
    if not condition:
        raise AuditError(check, message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def parse_raw(text):
    require(text.endswith('\n') and '\r' not in text, 1, 'noncanonical line endings')
    lines = text.split('\n')[:-1]
    i = 0
    while i < len(lines) and lines[i].startswith('#'):
        i += 1
    require(lines[i:i + 3] == [f'MCDSQS {V}', f'COLOURS {R}', 'BLOCKS'], 1, 'header')
    i += 3
    blocks = []
    for line in lines[i:i + NB]:
        require(re.fullmatch(' '.join([NUM] * 4), line) is not None, 1, f'bad block line {line!r}')
        blocks.append(tuple(int(x) for x in line.split(' ')))
    require(len(blocks) == NB, 1, 'truncated block list')
    i += NB
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
    return blocks, points


def parse_lean(text):
    chunks = dict(re.findall(r'def (blocks38_\d+) : List RawQuad := (\[.*?\])\n', text, re.S))
    m = re.search(r'def blocks38 : List RawQuad :=\n  ([^\n]*)\n', text)
    require(m is not None and chunks, 2, 'blocks38 literal not found')
    order = [name.strip() for name in m.group(1).split('++')]
    require(sorted(order) == sorted(chunks), 2, 'blocks38 does not concatenate exactly its chunks')
    blocks = [tuple(b) for name in order for b in ast.literal_eval(chunks[name])]
    cols = {}
    for name, body in re.findall(r'def (col38_\d+) : List \(List RawTriple\) := (\[.*?\])\n', text, re.S):
        cols[name] = [[tuple(t) for t in c] for c in ast.literal_eval(re.sub(r'--[^\n]*', '', body))]
    m2 = re.search(r'def colour38 : List \(List \(List RawTriple\)\) :=\n  \[([^\n]*)\]\n', text)
    require(m2 is not None, 2, 'colour38 literal not found')
    names = [n.strip() for n in m2.group(1).split(',')]
    require(names == [f'col38_{x}' for x in range(V)] and sorted(cols) == sorted(names), 2,
            'colour38 is not [col38_0, ..., col38_37]')
    return blocks, [cols[n] for n in names]


def semantic_check(blocks, points):
    """Definition-first check of the raw certificate (check 3)."""
    bsets = [frozenset(b) for b in blocks]
    require(all(len(b) == 4 and max(b) < V for b in bsets), 3, 'block is not a 4-subset of 0..37')
    require(len(set(bsets)) == NB, 3, 'duplicate block')
    count = {}
    for b in bsets:
        for t in combinations(sorted(b), 3):
            count[t] = count.get(t, 0) + 1
    require(len(count) == 8436 and set(count.values()) == {1}, 3,
            'some 3-subset is not in exactly one block')
    bset = set(bsets)
    for x in range(V):
        derived = {b - {x} for b in bsets if x in b}
        classes = points[x]
        require(len(classes) == R, 3, f'POINT {x}: not 19 classes')
        listed = []
        for cls in classes:
            sets = [frozenset(t) for t in cls]
            require(sets and all(len(t) == 3 and max(t) < V and x not in t for t in sets), 3,
                    f'POINT {x}: bad triple')
            union = set()
            for t in sets:
                require(not (union & t), 3, f'POINT {x}: class not pairwise disjoint')
                union |= t
                require(t | {x} in bset, 3, f'POINT {x}: listed triple is not derived')
            listed.extend(sets)
        require(len(listed) == len(set(listed)) and set(listed) == derived, 3,
                f'POINT {x}: classes do not partition the derived design')
    triples = [frozenset(t) for cls in points[37] for t in cls]
    pairs = [p for t in triples for p in combinations(sorted(t), 2)]
    require(all(max(t) < 37 for t in triples) and len(pairs) == len(set(pairs)) == 666, 3,
            'POINT 37 read on 0..36 is not an STS(37)')
    return {'blocks': NB, 'three_subsets_covered_once': len(count), 'points': V,
            'classes_per_point': R,
            'class_size_profiles': sorted({tuple(len(c) for c in p) for p in points})}


def audit(raw_bytes, lean_text, sha_pin=RAW_SHA256):
    require(sha256(raw_bytes) == sha_pin, 1, 'raw SHA-256 mismatch')
    raw_blocks, raw_points = parse_raw(raw_bytes.decode('ascii'))
    lean_blocks, lean_points = parse_lean(lean_text)
    require(lean_blocks == raw_blocks, 2, 'blocks38 differs from the raw block lines')
    for x in range(V):
        require(lean_points[x] == raw_points[x], 2, f'col38_{x} differs from the raw POINT {x} section')
    return semantic_check(raw_blocks, raw_points)


def corrupt(text, kind):
    lines = text.split('\n')
    if kind == 'block_line':
        i = lines.index('BLOCKS') + 1
        a, b, c, d = map(int, lines[i].split(' '))
        lines[i] = f'{a} {b} {c} {d - 1 if d - 1 > c else d + 1}'
        return '\n'.join(lines), 2, True
    if kind == 'point0_triple':
        i = lines.index('POINT 0') + 2
        lines[i], lines[i + 1] = lines[i + 1], lines[i]
        return '\n'.join(lines), 2, False
    if kind == 'point7_swap':
        i = lines.index('POINT 7') + 2
        t1, t2 = lines[i].split(' '), lines[i + 1].split(' ')
        t1[0], t2[0] = t2[0], t1[0]
        lines[i] = ' '.join(map(str, sorted(map(int, t1))))
        lines[i + 1] = ' '.join(map(str, sorted(map(int, t2))))
        return '\n'.join(lines), 2, True
    if kind == 'point7_copy0':
        i0, i1 = lines.index('POINT 0'), lines.index('POINT 1')
        i7, i8 = lines.index('POINT 7'), lines.index('POINT 8')
        lines[i7 + 1:i8] = lines[i0 + 1:i1]
        return '\n'.join(lines), 2, True
    raise ValueError(kind)


def run_controls(raw_bytes, lean_text):
    results = {}
    text = raw_bytes.decode('ascii')
    for kind in ['block_line', 'point0_triple', 'point7_swap', 'point7_copy0']:
        bad_text, intended, semantic_expected = corrupt(text, kind)
        bad = bad_text.encode('ascii')
        try:
            audit(bad, lean_text, sha_pin=sha256(bad))
            outcome = {'rejected': False}
        except AuditError as exc:
            outcome = {'rejected': True, 'check': exc.check, 'reason': str(exc)}
        # the definition-first check must also reject the corrupted certificate on its own
        try:
            semantic_check(*parse_raw(bad_text))
            outcome['semantic_rejected'] = False
        except AuditError as exc:
            outcome['semantic_rejected'] = True
            outcome['semantic_reason'] = str(exc)
        outcome['intended_check'] = intended
        outcome['semantic_rejection_expected'] = semantic_expected
        outcome['as_intended'] = (outcome['rejected'] and outcome.get('check') == intended and
                                  outcome['semantic_rejected'] == semantic_expected)
        outcome['corrupted_sha256'] = sha256(bad)
        results[kind] = outcome
    try:
        audit(raw_bytes + b'\n', lean_text)
        results['sha_pin'] = {'rejected': False, 'as_intended': False}
    except AuditError as exc:
        results['sha_pin'] = {'rejected': True, 'check': exc.check, 'reason': str(exc),
                              'as_intended': exc.check == 1}
    return results


def main(argv):
    if len(argv) != 1:
        raise SystemExit(__doc__)
    out = Path(argv[0])
    if out.exists():
        raise SystemExit('Refusing to overwrite receipt')
    raw_bytes = (REVIEW / RAW).read_bytes()
    lean_path = HERE / 'McdKernel' / 'Data38.lean'
    lean_bytes = lean_path.read_bytes()
    receipt = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
               'auditor_sha256': sha256(Path(__file__).read_bytes()),
               'raw': {'path': f'review/{RAW}', 'sha256': sha256(raw_bytes)},
               'lean_data_module': {'path': 'McdKernel/Data38.lean', 'sha256': sha256(lean_bytes)}}
    manifest = HERE / 'manifest.json'
    if manifest.exists():
        pinned = json.loads(manifest.read_text())['files'].get('McdKernel/Data38.lean')
        receipt['lean_data_module']['manifest_pin_matches'] = pinned == sha256(lean_bytes)
    rc = 0
    try:
        receipt['result'] = audit(raw_bytes, lean_bytes.decode('utf-8'))
        receipt['status'] = 'BINDING_AUDIT_PASS'
    except AuditError as exc:
        receipt['status'] = 'BINDING_AUDIT_FAIL'
        receipt['error'] = str(exc)
        rc = 1
    receipt['controls'] = run_controls(raw_bytes, lean_bytes.decode('utf-8'))
    if not all(c['as_intended'] for c in receipt['controls'].values()):
        receipt['status'] = 'BINDING_AUDIT_CONTROLS_FAIL'
        rc = 1
    if receipt['lean_data_module'].get('manifest_pin_matches') is False:
        receipt['status'] = 'BINDING_AUDIT_PIN_MISMATCH'
        rc = 1
    with out.open('x') as stream:
        json.dump(receipt, stream, indent=1)
        stream.write('\n')
    print(json.dumps({'status': receipt['status'],
                      'controls': {k: c['as_intended'] for k, c in receipt['controls'].items()},
                      'result': receipt.get('result')}))
    return rc


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
