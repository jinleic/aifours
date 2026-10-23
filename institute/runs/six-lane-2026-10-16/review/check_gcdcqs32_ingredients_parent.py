#!/usr/bin/env python3
"""Definition-first parent verification of the fixed Construction 2.3 ingredients.
No claimant imports. Tan-Zhou arXiv:2503.11934v1 lines 237-255 define the predicates.
Usage: python3 -B check_gcdcqs32_ingredients_parent.py NEW_OUTPUT_DIRECTORY
Retains copied mutation fixtures; writes exclusively; invokes the existing parent checker for I2.
"""
from collections import Counter
from datetime import datetime
from itertools import combinations
from pathlib import Path
from zoneinfo import ZoneInfo
import hashlib
import json
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
PIN = HERE / 'gcdcqs32-parent-producer-inputs-v1'
LANE = HERE.parents[3] / 'mathematics/evidence/six-lane-20261016/gcdcqs32-four-groups'


class Invalid(Exception):
    pass


def need(condition, reason):
    if not condition:
        raise Invalid(reason)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fg(path):
    d = json.loads(path.read_bytes())
    groups, B, T = d['groups'], d['B'], d['T']
    need(len(groups) == 4 and all(len(g) == 4 for g in groups)
         and sorted(p for g in groups for p in g) == list(range(16)), 'GROUPS')
    for members, size, label in ((groups, 4, 'GROUPS'), (B, 4, 'B'), (T, 5, 'T')):
        need(all(len(m) == size for m in members), label + '-SIZE')
        need(all(all(type(p) is int and 0 <= p < 16 for p in m)
                 and len(set(m)) == size for m in members), label + '-POINTS')
    pairs = Counter(t for m in groups + B for t in combinations(sorted(m), 2))
    need(set(pairs) == set(combinations(range(16), 2)) and set(pairs.values()) == {1}, 'STEINER2')
    triples = Counter(t for m in groups + B + T for t in combinations(sorted(m), 3))
    need(set(triples) == set(combinations(range(16), 3)) and set(triples.values()) == {1}, 'STEINER3')
    return {'points': 16, 'groups': 4, 'B_blocks': len(B), 'T_blocks': len(T),
            'pairs': len(pairs), 'triples': len(triples)}


def fdh(path):
    raw = path.read_bytes().decode('ascii')
    need('\r' not in raw, 'FORMAT')
    lines = [l for l in raw.split('\n') if l and not l.startswith('#')]
    need(lines[:2] == ['FDH 5 8', 'GROUPS'], 'HEADER')
    integer_line = re.compile(r'(?:0|[1-9][0-9]*)(?: (?:0|[1-9][0-9]*))*')

    def points(line, size):
        need(integer_line.fullmatch(line) is not None, 'FORMAT')
        p = tuple(map(int, line.split(' ')))
        need(len(p) == size and len(set(p)) == size and all(0 <= q < 40 for q in p), 'POINTS')
        return tuple(sorted(p))

    groups = [points(l, 8) for l in lines[2:7]]
    need(len(groups) == 5 and sorted(p for g in groups for p in g) == list(range(40)), 'GROUPS')
    group_of = {p: g for g, pts in enumerate(groups) for p in pts}
    need(lines[7] == 'BLOCKS', 'FORMAT')
    i = 8
    blocks = []
    while i < len(lines) and not lines[i].startswith('POINT '):
        blocks.append(points(lines[i], 4))
        i += 1
    need(len(set(blocks)) == len(blocks), 'DUPLICATE-BLOCK')
    need(all(len({group_of[p] for p in b}) == 4 for b in blocks), 'BLOCK-GROUPS')
    covered = Counter(t for b in blocks for t in combinations(b, 3))
    universe = {t for t in combinations(range(40), 3) if len({group_of[p] for p in t}) == 3}
    need(set(covered) == universe and set(covered.values()) == {1}, 'COVERAGE')
    profiles = set()
    for x in range(40):
        need(i < len(lines) and lines[i] == f'POINT {x}', 'POINT-SECTIONS')
        i += 1
        derived = Counter(tuple(p for p in b if p != x) for b in blocks if x in b)
        listed = Counter()
        misses = Counter()
        sizes = []
        for j in range(16):
            need(i < len(lines) and lines[i] == f'CLASS {j}', 'CLASS-SECTIONS')
            i += 1
            cls = []
            while i < len(lines) and not lines[i].startswith(('CLASS ', 'POINT ')):
                cls.append(points(lines[i], 3))
                i += 1
            need(cls, 'EMPTY-CLASS')
            ps = [p for t in cls for p in t]
            need(len(ps) == len(set(ps)), 'FRAME-PPC')
            need(group_of[x] not in {group_of[p] for p in ps}, 'FRAME-OWN-GROUP')
            absent = {g for g in range(5) if g != group_of[x] and not set(groups[g]).intersection(ps)}
            need(len(absent) == 1, 'FRAME-MISSING-GROUP')
            gm = next(iter(absent))
            need(set(ps) == {p for p in range(40) if group_of[p] not in (group_of[x], gm)}, 'FRAME-COVERAGE')
            misses[gm] += 1
            listed.update(cls)
            sizes.append(len(cls))
        need(listed == derived and all(n == 1 for n in listed.values()), 'FRAME-DERIVED-PARTITION')
        need(misses == Counter({g: 4 for g in range(5) if g != group_of[x]}), 'FRAME-MULTIPLICITIES')
        profiles.add(tuple(sorted(Counter(sizes).items())))
    need(i == len(lines), 'FORMAT-TRAILING')
    return {'points': 40, 'groups': 5, 'blocks': len(blocks), 'transverse_triples': len(covered),
            'all_point_frame_class_size_profiles': sorted(profiles), 'classes_missing_each_other_group': 4,
            'noncomment_lines_consumed': i}


def main():
    out = Path(sys.argv[1])
    out.mkdir(exist_ok=False)
    expected = json.loads((PIN / 'pins.json').read_bytes())['files']
    results = {}
    for name, fn in [('ingredient_I1_fg_ag24.json', fg), ('ingredient_I3_fdh_5_8.txt', fdh)]:
        path = PIN / 'ingredients' / name
        need(sha(path) == expected['ingredients/' + name], 'PIN-HASH')
        results[name] = {'sha256': sha(path), 'status': 'PASS', 'structure': fn(path)}
    i2 = PIN / 'ingredients/ingredient_I2_gcdcqs8.txt'
    i2out = out / 'I2-parent-check.json'
    proc = subprocess.run(['/usr/bin/python3', '-B', str(HERE / 'check_gcdcqs_parent.py'),
                           str(i2), '32', '4', '8', expected['ingredients/' + i2.name], str(i2out)],
                          capture_output=True, text=True)
    need(proc.returncode == 0 and json.loads(i2out.read_bytes())['status'] == 'PASS', 'I2-CHECK')
    results[i2.name] = {'sha256': sha(i2), 'status': 'PASS', 'receipt_sha256': sha(i2out)}
    controls = [
        ('fg_T_point_swapped.json', fg, 'STEINER3'),
        ('fg_T_block_dropped.json', fg, 'STEINER3'),
        ('fg_B_line_replaced.json', fg, 'STEINER2'),
        ('fg_T_block_size4.json', fg, 'T-SIZE'),
        ('fg_group_size3.json', fg, 'GROUPS'),
        ('fdh_block_dropped.txt', fdh, 'COVERAGE'),
        ('fdh_block_duplicated.txt', fdh, 'DUPLICATE-BLOCK'),
        ('fdh_block_meets_group_twice.txt', fdh, 'BLOCK-GROUPS'),
        ('fdh_triple_moved_between_classes.txt', fdh, 'FRAME-PPC'),
        ('fdh_point_section_dropped.txt', fdh, 'POINT-SECTIONS'),
    ]
    control_results = []
    for name, fn, intended in controls:
        src = LANE / 'evidence/gcdcqs32-c23/ingredient_controls' / name
        target = out / name
        with target.open('xb') as f:
            f.write(src.read_bytes())
        try:
            fn(target)
            got = 'ACCEPTED'
        except Invalid as exc:
            got = str(exc)
        control_results.append({'fixture': name, 'sha256': sha(target), 'expected': intended,
                                'actual': got, 'intended': got == intended})
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'status': 'PASS' if all(c['intended'] for c in control_results) else 'CONTROL-MISMATCH',
              'checker_sha256': sha(Path(__file__)), 'ingredients': results, 'controls': control_results,
              'scope': 'Independent fixed-ingredient predicates; no symmetry, solver or affine-geometry claims checked.'}
    with (out / 'result.json').open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({'status': result['status'], 'controls': len(control_results),
                      'mismatches': [c for c in control_results if not c['intended']]}, indent=1))
    return 0 if result['status'] == 'PASS' else 1


if __name__ == '__main__':
    sys.exit(main())
