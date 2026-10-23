"""Independently recheck the lower46 CNFs using an addition-only ASCII DRAT/RUP proof.
No LRAT checker is trusted: discard hint/deletion syntax, then require the parent's drat-trim -I -U to verify
the resulting addition sequence against the original pinned CNF. A successful check proves that CNF UNSAT.
Neither a converted proof nor uncompressed copies are written. Native checker limit300s per pair; sequential.
"""
import hashlib
import json
import subprocess
import sys
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
DT = HERE.parent / 'moqls7-parent-proofcheck-v1/drat-trim'
EXPECTED_DT = 'a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37'
CONVERTER = HERE / 'lrat_additions_to_drat.py'


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def now():
    return subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()


def nvars(cnf):
    with open(cnf) as f:
        for line in f:
            if line.startswith('p cnf '):
                return int(line.split()[2])
    raise ValueError('DIMACS header missing')


def check(cnf, lrat, outdir, label):
    if sha(DT) != EXPECTED_DT:
        raise ValueError('Parent checker binary changed')
    stderr_path = outdir / (label + '.converter.stderr')
    with open(stderr_path, 'xb') as err:
        producer = subprocess.Popen(['/usr/bin/python3', '-B', str(CONVERTER), str(lrat), str(nvars(cnf))],
                                    stdout=subprocess.PIPE, stderr=err)
        checker = subprocess.Popen([str(DT), str(cnf), '-I', '-U', '-t', '300'], stdin=producer.stdout,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        producer.stdout.close()
        h, statuses, tail, count = hashlib.sha256(), [], deque(maxlen=6), 0
        for raw in checker.stdout:
            h.update(raw)
            count += 1
            s = raw.decode('utf-8', 'replace').strip()
            tail.append(s)
            if s.startswith('s '):
                statuses.append(s)
        drc, prc = checker.wait(), producer.wait()
    stats = None
    if prc == 0:
        stats = json.loads(stderr_path.read_text())
    return {'checker_rc': drc, 'converter_rc': prc, 'statuses': statuses, 'converter': stats,
            'checker_output_sha256': h.hexdigest(), 'checker_output_lines': count, 'tail': list(tail),
            'verified': drc == 0 and prc == 0 and statuses == ['s VERIFIED']}


def smoke():
    out = HERE / 'conversion-smoke-v1'
    out.mkdir(exist_ok=False)
    cases = [
        ('sat-empty-nohint', 'p cnf 1 1\n1 0\n', '2 0 0\n', False),
        ('sat-empty-onehint', 'p cnf 1 1\n1 0\n', '2 0 1 0\n', False),
        ('sat-valid-lemma-bogus-empty', 'p cnf 1 1\n1 0\n', '2 1 0 1 0\n3 0 0\n', False),
        ('unsat-unit-conflict', 'p cnf 1 2\n1 0\n-1 0\n', '3 0 1 2 0\n', True),
        ('unsat-satisfied-hint', 'p cnf 2 3\n1 2 0\n-1 0\n-2 0\n', '4 0 2 2 3 1 0\n', True),
        ('unsat-deletion-record', 'p cnf 2 3\n1 2 0\n-1 0\n-2 0\n',
         '4 2 0 2 1 0\n5 d 2 0\n6 0 3 4 0\n', True),
    ]
    rows = []
    for label, cnf, lrat, expected in cases:
        cp, lp = out / (label + '.cnf'), out / (label + '.lrat')
        with open(cp, 'x') as f:
            f.write(cnf)
        with open(lp, 'x') as f:
            f.write(lrat)
        row = check(cp, lp, out, label)
        row.update({'label': label, 'expected_verified': expected})
        row['ok'] = row['verified'] == expected and row['converter_rc'] == 0
        if not expected:
            row['ok'] = row['ok'] and row['checker_rc'] != 0 and row['statuses'] == ['s NOT VERIFIED']
        rows.append(row)
    rec = {'recorded': now(), 'checker_sha256': EXPECTED_DT, 'converter_sha256': sha(CONVERTER),
           'rows': rows, 'verdict': 'PASS' if all(r['ok'] for r in rows) else 'FAIL'}
    with open(HERE / 'conversion-smoke-result.json', 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps({'verdict': rec['verdict'], 'rows': [(r['label'], r['statuses'], r['ok']) for r in rows]}))


def replay():
    if json.loads((HERE / 'conversion-smoke-result.json').read_text())['verdict'] != 'PASS':
        raise ValueError('Pipeline smoke failed')
    pin = json.loads((HERE / 'parent-pin-receipt.json').read_text())
    out = HERE / 'addition-replay-v1'
    out.mkdir(exist_ok=False)
    started = now()
    results = []
    for i, pair in enumerate(pin['pairs']):
        cnf, lrat = HERE / pair['cnf'], HERE / pair['lrat']
        if sha(cnf) != pair['cnf_sha256'] or sha(lrat) != pair['lrat_sha256']:
            raise ValueError('Pinned pair changed')
        row = check(cnf, lrat, out, 'p%02d' % i)
        row.update({'index': i, 't': pair['t'], 'e': pair['e'], 'profile': pair['profile'], 'what': pair['what'],
                    'cnf': pair['cnf'], 'cnf_sha256': pair['cnf_sha256'], 'lrat_sha256': pair['lrat_sha256']})
        row['source_bound'] = row['converter'] is not None and row['converter']['source_sha256'] == pair['lrat_sha256']
        row['verdict'] = 'VERIFIED' if row['verified'] and row['source_bound'] else 'UNKNOWN'
        with open(out / ('p%02d.json' % i), 'x') as f:
            json.dump(row, f, indent=1)
            f.write('\n')
        results.append(row)
    rec = {'started': started, 'ended': now(), 'checker_sha256': EXPECTED_DT, 'converter_sha256': sha(CONVERTER),
           'driver_sha256': sha(Path(__file__)), 'pairs': len(results),
           'verified': sum(r['verdict'] == 'VERIFIED' for r in results),
           'bad': [r['index'] for r in results if r['verdict'] != 'VERIFIED'],
           'verdict': 'PASS' if len(results) == 18 and all(r['verdict'] == 'VERIFIED' for r in results) else 'UNKNOWN',
           'limit': 'Proves each pinned CNF UNSAT, independently of LRAT hints/checkers. CNF-to-mathematics binding is separate.'}
    with open(HERE / 'addition-replay-result.json', 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps(rec))


if __name__ == '__main__':
    {'smoke': smoke, 'replay': replay}[sys.argv[1]]()
