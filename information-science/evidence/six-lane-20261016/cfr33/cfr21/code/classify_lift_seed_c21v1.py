#!/usr/bin/env python3
"""Classify first-row normal forms from an already verified six-row Z21 DM.
Usage: classify_lift_seed_c21v1.py DM6RAW NEW_OUTDIR
No CFR search. Enumerate all ordered base-row pairs and remaining rows, normalize
zero/id by a common column relabelling, and quotient by the proved R1 operations
plus point translations. Omit every class already in the baseline6 or completed
50-trade primary inventories. No completed neighbourhood search is repeated.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
source, out = Path(sys.argv[1]), Path(sys.argv[2])
os.mkdir(out)
begin = time.monotonic()
def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def valid(f):
    return len(f) == 21 and f[0] == 0 and sorted(f) == list(range(21)) and len({(f[x] - x) % 21 for x in range(21)}) == 21

spec = importlib.util.spec_from_file_location('pinned_r1_ops_for_seed_intake', ROOT / 'code/gen_three_trades_c21v1.py')
group = importlib.util.module_from_spec(spec)
spec.loader.exec_module(group)
cache = {}
def extended_canonical(f):
    if f in cache:
        return cache[f]
    _, members, _ = group.orbit(f)
    answer = min(tuple((g[(x + e) % 21] - g[e]) % 21 for x in range(21))
                 for g in members for e in range(21))
    if not valid(answer):
        raise AssertionError('invalid normal form')
    for g in members:
        cache[g] = answer
    return answer

known_paths = [ROOT / 'specs/full-seeds-v1/p21-r1-reps-n21.txt',
               ROOT / 'specs/three-trades-v1/new-trade-R1-reps.txt']
known = set()
for p in known_paths:
    for line in p.read_text().splitlines():
        if line.strip():
            f = tuple([0] + [int(v) for v in line.split()])
            if not valid(f):
                raise ValueError('bad known first row')
            known.add(extended_canonical(f))
D = [[int(v) for v in line.split()] for line in source.read_text().splitlines() if line.strip()]
if len(D) != 6 or any(len(row) != 21 for row in D):
    raise ValueError('expected6x21 DM')
if not all(len({(D[i][c] - D[j][c]) % 21 for c in range(21)}) == 21 for i in range(6) for j in range(i)):
    raise ValueError('input DM definition fails')
new, all_classes = {}, set()
occurrences = 0
for p in range(6):
    for q in range(6):
        if p == q:
            continue
        basis = [(D[q][c] - D[p][c]) % 21 for c in range(21)]
        inverse = [0] * 21
        for c, value in enumerate(basis):
            inverse[value] = c
        for r in range(6):
            if r in (p, q):
                continue
            f = [(D[r][inverse[x]] - D[p][inverse[x]]) % 21 for x in range(21)]
            offset = f[0]
            f = tuple((v - offset) % 21 for v in f)
            if not valid(f):
                raise AssertionError('derived normal form fails')
            occurrences += 1
            canonical = extended_canonical(f)
            all_classes.add(canonical)
            if canonical not in known:
                new.setdefault(canonical, []).append({'zero_row': p, 'identity_row': q, 'other_row': r})
report = {'clock': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
          'source_sha256': sha(source), 'program_sha256': sha(__file__),
          'r1_helper_sha256': sha(ROOT / 'code/gen_three_trades_c21v1.py'),
          'known_inventory_sha256': {str(p.relative_to(ROOT)): sha(p) for p in known_paths},
          'occurrences': occurrences, 'seed_extended_classes': len(all_classes),
          'known_extended_classes': len(known), 'new_extended_classes': len(new),
          'status': 'NEW-FINITE-INPUT-FAMILY' if new else 'NO-NEW-FIRST-ROW-CLASSES',
          'scope': 'seed intake only; no CFR6,21 existence or nonexistence conclusion',
          'provenance': [{'f': list(f), 'sources': new[f]} for f in sorted(new)],
          'wall_s': time.monotonic() - begin}
if new:
    path = out / 'new-f1-reps.txt'
    with open(path, 'x') as f:
        for row in sorted(new):
            f.write(' '.join(map(str, row[1:])) + '\n')
    report['new_input_sha256'] = sha(path)
with open(out / 'record.json', 'x') as f:
    json.dump(report, f, indent=1)
print(json.dumps({k: v for k, v in report.items() if k != 'provenance'}), flush=True)
