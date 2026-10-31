#!/usr/bin/env python3
"""Check the pinned 60-support tensor exactly, without author code.

Arithmetic is in Z[sqrt(2)]; the source/table correspondence is a separate
review obligation. Outputs are exclusive-create research evidence.
"""
import hashlib
import itertools
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
TABLE = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-pandya-table-v1.txt')
EXPECTED = 'cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38'
OUT = HERE / 'parent-pandya-witness-result-v1.json'
TOKEN = re.compile(r'([+\-s])([0-5])([0-5])\Z')


def clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'],
                          check=True, capture_output=True, text=True).stdout.strip()


def read_tensor(data):
    entries, cells = {}, set()
    counts = {'single_sqrt2_cells': 0, 'two_signed_cells': 0}
    for lineno, line in enumerate(data.decode('utf-8').splitlines(), 1):
        if not line or line.startswith('#'):
            continue
        fields = line.split()
        if len(fields) not in (3, 4) or not all(x in '012345' and len(x) == 1 for x in fields[:2]):
            raise ValueError(f'BAD_CELL_LINE:{lineno}')
        a, b = map(int, fields[:2])
        if (a, b) in cells:
            raise ValueError(f'DUPLICATE_CELL:{lineno}')
        cells.add((a, b))
        parsed = [TOKEN.fullmatch(x) for x in fields[2:]]
        if not all(parsed):
            raise ValueError(f'BAD_KET:{lineno}')
        tags = [m.group(1) for m in parsed]
        if tags == ['s']:
            counts['single_sqrt2_cells'] += 1
        elif len(tags) == 2 and all(t in '+-' for t in tags):
            counts['two_signed_cells'] += 1
        else:
            raise ValueError(f'BAD_CELL_SHAPE:{lineno}')
        for m in parsed:
            t, c, d = m.groups()
            position = (a, b, int(c), int(d))
            if position in entries:
                raise ValueError(f'DUPLICATE_POSITION:{lineno}')
            entries[position] = (0, 1) if t == 's' else (1 if t == '+' else -1, 0)
    if cells != set(itertools.product(range(6), repeat=2)):
        raise ValueError('CELL_UNIVERSE')
    if counts != {'single_sqrt2_cells': 12, 'two_signed_cells': 24} or len(entries) != 60:
        raise ValueError('SUPPORT_COUNTS')
    return entries, counts


def product(x, y):
    a, b = x
    c, d = y
    return (a * c + 2 * b * d, a * d + b * c)


def gram_failure(entries, selected, columns=False):
    remaining = tuple(i for i in range(4) if i not in selected)
    matrix = [[(0, 0) for _ in range(36)] for _ in range(36)]
    for x, value in entries.items():
        row = 6 * x[selected[0]] + x[selected[1]]
        col = 6 * x[remaining[0]] + x[remaining[1]]
        matrix[row][col] = value
    for i in range(36):
        for j in range(36):
            s0 = s1 = 0
            for k in range(36):
                a = matrix[k][i] if columns else matrix[i][k]
                b = matrix[k][j] if columns else matrix[j][k]
                x, y = product(a, b)
                s0 += x
                s1 += y
            expected = (2, 0) if i == j else (0, 0)
            if (s0, s1) != expected:
                return {'i': i, 'j': j, 'observed': [s0, s1],
                        'expected': list(expected), 'kind': 'diagonal' if i == j else 'off_diagonal'}
    return None


def main():
    start = clock()
    data = TABLE.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED:
        raise ValueError('TABLE_HASH_MISMATCH')
    if OUT.exists():
        raise FileExistsError(OUT)
    entries, counts = read_tensor(data)
    cuts = ((0, 1), (0, 2), (0, 3))
    for cut in cuts:
        for columns in (False, True):
            error = gram_failure(entries, cut, columns)
            if error:
                raise AssertionError(f'GRAM_FAILURE:{cut}:{columns}:{error}')
    mutated = dict(entries)
    del mutated[next(iter(mutated))]
    failure = gram_failure(mutated, cuts[0])
    if not failure or failure['kind'] != 'diagonal':
        raise AssertionError('REMOVED_TERM_CONTROL_DID_NOT_FAIL_DIAGONAL')
    result = {
        'kind': 'PARENT_EXACT_PANDYA_TRANSCRIPTION_WITNESS_CHECK',
        'started_native_clock': start,
        'finished_native_clock': clock(),
        'table_sha256': digest,
        'table_cells': 36,
        'support': len(entries),
        'cell_counts': counts,
        'cuts': [list(x) for x in cuts],
        'row_and_column_gram': '2I over Z[sqrt(2)] on all three cuts',
        'normalization': 'coefficients divided by sqrt(72); each cut is unitary after multiplying tensor by 6',
        'control': {'removed_first_nonzero': 'rejected', 'failure': failure},
        'limits': 'Verifies this exact transcription, not its correspondence to public HTML, novelty, '
                  'the global minimum, a human review, or a formal proof.',
    }
    with OUT.open('x', encoding='utf-8') as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
