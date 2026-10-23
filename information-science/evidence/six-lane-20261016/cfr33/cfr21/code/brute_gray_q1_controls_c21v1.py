#!/usr/bin/env python3
"""Direct all-entry brute force for Q1 Gray-checker controls; no RREF/lift imports.
Usage: brute_gray_q1_controls_c21v1.py NEW_OUTPUT.json
For Q1 the projected matrix is all0 and CRT lifts are simply every Kx3 matrix
over Z3. Test the full row-pair difference definition, then count the row0/
column0-zero gauge subset separately. All files exclusive; no native children.
"""
import hashlib
import itertools
import json
from pathlib import Path
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

begin = time.monotonic()
rows = []
for k in (2, 3, 4):
    total = gauged = visited = 0
    for flat in itertools.product(range(3), repeat=3 * k):
        visited += 1
        if not all(len({(flat[3 * j + c] - flat[3 * i + c]) % 3 for c in range(3)}) == 3
                   for i in range(k) for j in range(i + 1, k)):
            continue
        total += 1
        if flat[:3] == (0, 0, 0) and all(flat[3 * i] == 0 for i in range(1, k)):
            gauged += 1
    rows.append({'K': k, 'Q': 1, 'all_matrices_visited': visited,
                 'all_lifts': total, 'gauged_lifts': gauged})
assert [r['all_matrices_visited'] for r in rows] == [3 ** 6, 3 ** 9, 3 ** 12]
assert [r['all_lifts'] for r in rows] == [162, 486, 0]
assert [r['gauged_lifts'] for r in rows] == [2, 2, 0]
record = {'clock': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
          'status': 'DIRECT-TINY-DEFINITION-COUNTS-PASS', 'controls': rows,
          'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'wall_s': time.monotonic() - begin,
          'scope': 'only Q1 small controls, not another checker mutation suite or CFR6,21 result'}
with open(sys.argv[1], 'x') as f:
    json.dump(record, f, indent=1)
print(json.dumps(record), flush=True)
