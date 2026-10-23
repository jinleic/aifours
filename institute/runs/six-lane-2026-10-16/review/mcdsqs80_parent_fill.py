"""Parent-independent Construction2.1 expansion from the pinned gcDCQS certificate and published SXK data.
Imports only the parent's parser (no worker code), writes fresh ordinary mcDSQS20 and mcDSQS80 certificates,
checks both with the parent's definition-first mcDSQS checker, and compares every non-comment data line
of the regenerated80 certificate with the pinned worker certificate. No symmetry/SAT assumption is used.
Usage: python3 -B mcdsqs80_parent_fill.py
"""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
from zoneinfo import ZoneInfo

import check_gcdcqs_parent as gc

HERE = Path(__file__).resolve().parent
A = HERE / 'gcdcqs20-parent-inputs-v1/gcdcqs20-e1s1_p10.txt'
A_SHA = '58b51b50b5281df613c5fae0a3b0178a374554a2f062e55bd8fc25250922a0ca'
PIN80 = HERE / 'mcdsqs80-parent-inputs-v1'
OUT = HERE / 'mcdsqs80-parent-fill-v1'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def render(v, blocks, colouring):
    lines = ['# Parent expansion from pinned finite data, Construction2.1 with empty stem.', 'MCDSQS ' + str(v), 'COLOURS ' + str(v // 2), 'BLOCKS']
    lines += [' '.join(map(str, b)) for b in sorted(blocks)]
    for x in range(v):
        lines.append('POINT ' + str(x))
        for j, cls in enumerate(colouring[x]):
            lines.append('CLASS ' + str(j))
            lines += [' '.join(map(str, t)) for t in sorted(cls)]
    return '\n'.join(lines) + '\n'


def main():
    OUT.mkdir(exist_ok=False)
    if digest(A) != A_SHA:
        raise ValueError('gcDCQS pin mismatch')
    spec = json.loads((PIN80 / 'sxk_prop3_transcription.json').read_text())
    blocks20 = {tuple(sorted((p + t) % 20 for p in b)) for b in spec['base_blocks'] for t in range(20)}
    colouring20 = {x: [[tuple(sorted((p + x) % 20 for p in t)) for t in cls] for cls in spec['cells']] for x in range(20)}
    v, n, g, r, s, groups, blocks, sections = gc.parse(A.read_text())
    if (v, n, g, r, s) != (80, 4, 20, 40, 10) or groups != [list(range(20 * i, 20 * i + 20)) for i in range(4)]:
        raise ValueError('unexpected gcDCQS parameters/groups')
    blocks80 = {tuple(sorted(b)) for b in blocks}
    for group_index in range(4):
        blocks80.update(tuple(20 * group_index + p for p in b) for b in blocks20)
    colouring80 = {}
    for x, classes in sections:
        group_index, local = divmod(x, 20)
        hole = set(groups[group_index]) - {x}
        free = [j for j, cls in enumerate(classes) if all(not hole.intersection(t) for t in cls)]
        if len(free) != 10:
            raise ValueError('incorrect number of hole-free classes')
        enlarged = [[tuple(sorted(t)) for t in cls] for cls in classes]
        for local_class, class_index in enumerate(free):
            enlarged[class_index] += [tuple(20 * group_index + p for p in t) for t in colouring20[local][local_class]]
        colouring80[x] = enlarged
    certs = [(20, blocks20, colouring20), (80, blocks80, colouring80)]
    results = []
    for size, bl, col in certs:
        dest = OUT / ('mcdsqs' + str(size) + '-parent.txt')
        with dest.open('x') as f:
            f.write(render(size, bl, col))
        receipt = OUT / ('mcdsqs' + str(size) + '-parent-check.json')
        proc = subprocess.run(['/usr/bin/python3', '-B', str(HERE / 'check_mcdsqs_independent.py'), str(dest), str(size), digest(dest), str(receipt)], capture_output=True, text=True)
        if proc.returncode:
            raise ValueError('parent-generated certificate failed direct checker: ' + proc.stdout)
        results.append({'v': size, 'blocks': len(bl), 'certificate_sha256': digest(dest), 'checker_exit': proc.returncode, 'receipt_sha256': digest(receipt)})
    original = PIN80 / 'mcdsqs80_c21_A.txt'
    generated = OUT / 'mcdsqs80-parent.txt'
    canonical = lambda p: '\n'.join(l for l in p.read_text().split('\n') if l and not l.startswith('#')) + '\n'
    same = canonical(original) == canonical(generated)
    if not same:
        raise ValueError('regenerated80 differs beyond comments')
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(timespec='seconds'), 'status': 'PASS',
              'script_sha256': digest(__file__), 'gcDCQS_sha256': A_SHA, 'source_transcription_sha256': digest(PIN80 / 'sxk_prop3_transcription.json'),
              'worker80_sha256': digest(original), 'all_noncomment_lines_equal': same,
              'canonical_data_sha256': hashlib.sha256(canonical(original).encode('ascii')).hexdigest(), 'results': results,
              'scope': 'Independent finite expansion and direct verification of20 and80, not a formal proof of the imported infinite-family recursion.'}
    with (OUT / 'parent-result.json').open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result, indent=1))


if __name__ == '__main__':
    main()
