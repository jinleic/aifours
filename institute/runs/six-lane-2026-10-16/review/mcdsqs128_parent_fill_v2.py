#!/usr/bin/env python3
"""Parent Construction2.1 replay for32/128, independently extracting AppendixB's text.
Imports only existing parent parser/render helpers; no claimant imports or solvers.
Usage: python3 -B mcdsqs128_parent_fill_v2.py NEW_OUTPUT_DIRECTORY
V2 fixes PDF form-feed splitting; failed v1 output directory is retained.
"""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from zoneinfo import ZoneInfo

import check_gcdcqs_parent as gc
from mcdsqs80_parent_fill import render

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
GC = HERE / 'gcdcqs32-parent-inputs-v1/gcdcqs32_c23.txt'
GC_SHA = 'e38945b1204e78937527f17db3d87f147e47885dc160c04b6a4de49377da0f46'
PIN = HERE / 'mcdsqs128-parent-inputs-v1'
CERT_SHA = 'a97b1ae50fa8f0dc7f3bb6908e6c714fdd233eeede2607c2d16c2101380fd326'
SOURCE = ROOT / 'mathematics/kirkman-large-sets-57-87/sources/tan-zhou-2503.11934.txt'
SOURCE_SHA = 'df52a8f11a46974eef129fa115bb3305831f7c8edc3e2102e4fd22c64c3c8164'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def canonical(path):
    return '\n'.join(l for l in path.read_text().splitlines() if l and not l.startswith('#')) + '\n'


def main():
    out = Path(sys.argv[1])
    out.mkdir(exist_ok=False)
    require(digest(SOURCE) == SOURCE_SHA and digest(GC) == GC_SHA, 'source/gcDCQS pin mismatch')
    require(digest(PIN / 'mcdsqs128_c21.txt') == CERT_SHA, '128 input pin mismatch')
    lines = SOURCE.read_text().split('\n')
    require('cyclic SQS(32)' in lines[1320] and 'derived design' in lines[1333], 'source line anchors changed')

    def sets(text, size):
        members = [tuple(map(int, item.split(','))) for item in re.findall(r'\{([0-9, ]+)\}', text)]
        require(all(len(m) == size for m in members), 'source member has wrong size')
        return members

    bases = sets('\n'.join(lines[1325:1332]), 4)
    parts = [sets('\n'.join(lines[i:i + 2]), 3) for i in range(1340, 1372, 2)]
    require(len(bases) == 40 and len(parts) == 16 and sum(map(len, parts)) == 155, 'source extraction counts')
    worker = json.loads((PIN / 'tz_appb_mcdsqs32.json').read_bytes())
    require(bases == [tuple(b) for b in worker['base_blocks']]
            and parts == [[tuple(t) for t in p] for p in worker['parts']], 'independent transcription differs')
    blocks32 = {tuple(sorted((q + x) % 32 for q in b)) for b in bases for x in range(32)}
    colours32 = {x: [[tuple(sorted((q + x) % 32 for q in t)) for t in cls] for cls in parts] for x in range(32)}
    v, n, g, r, s, groups, blocks, sections = gc.parse(GC.read_text())
    require((v, n, g, r, s) == (128, 4, 32, 64, 16)
            and groups == [list(range(32 * i, 32 * i + 32)) for i in range(4)], 'unexpected gcDCQS parameters')
    blocks128 = {tuple(sorted(b)) for b in blocks}
    for gi in range(4):
        blocks128.update(tuple(32 * gi + p for p in b) for b in blocks32)
    colours128 = {}
    for x, classes in sections:
        gi, local = divmod(x, 32)
        hole = set(groups[gi]) - {x}
        free = [j for j, cls in enumerate(classes) if all(not hole.intersection(t) for t in cls)]
        require(len(free) == 16, 'hole-free count')
        enlarged = [[tuple(sorted(t)) for t in cls] for cls in classes]
        for j, class_index in enumerate(free):
            enlarged[class_index] += [tuple(32 * gi + q for q in t) for t in colours32[local][j]]
        colours128[x] = enlarged
    results = []
    for size, bl, col in [(32, blocks32, colours32), (128, blocks128, colours128)]:
        cert = out / f'mcdsqs{size}-parent.txt'
        with cert.open('x') as f:
            f.write(render(size, bl, col))
        receipt = out / f'mcdsqs{size}-parent-check.json'
        p = subprocess.run(['/usr/bin/python3', '-B', str(HERE / 'check_mcdsqs_independent.py'),
                            str(cert), str(size), digest(cert), str(receipt)], capture_output=True, text=True)
        require(p.returncode == 0 and json.loads(receipt.read_bytes())['status'] == 'VALID_MCDSQS',
                'regenerated certificate failed: ' + p.stdout)
        results.append({'v': size, 'blocks': len(bl), 'sha256': digest(cert), 'receipt_sha256': digest(receipt)})
    same = canonical(out / 'mcdsqs128-parent.txt') == canonical(PIN / 'mcdsqs128_c21.txt')
    require(same, '128 noncomment data differs')
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(), 'status': 'PASS',
              'script_sha256': digest(__file__), 'source_sha256': SOURCE_SHA, 'gcDCQS_sha256': GC_SHA,
              'candidate128_sha256': CERT_SHA, 'transcription_sha256': digest(PIN / 'tz_appb_mcdsqs32.json'),
              'independent_primary_text_transcription_equal': True, 'all_noncomment_lines_equal': same,
              'canonical128_sha256': hashlib.sha256(canonical(out / 'mcdsqs128-parent.txt').encode()).hexdigest(),
              'results': results, 'scope': 'Explicit finite32/128 expansion and direct checks; no formalized recursion.'}
    with (out / 'parent-result.json').open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result, indent=1))


if __name__ == '__main__':
    main()
