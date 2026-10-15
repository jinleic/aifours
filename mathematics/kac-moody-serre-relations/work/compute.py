#!/usr/bin/env python3
"""One-process exact/modular graded computation; see proof.md for semantics."""
import argparse
import gzip
import hashlib
import json
import time
from pathlib import Path

from graded_lie import Field, FreeLie, compute_matrix


def control_dimension(name, alpha):
    if name == 'A3_control':
        return int(alpha in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 1, 1)))
    if name == 'affine_A2_control':
        if len(set(alpha)) == 1:
            return 2
        return int(max(alpha) - min(alpha) == 1)
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--height', type=int, required=True)
    parser.add_argument('--prime', type=int)
    parser.add_argument('--matrices', nargs='+')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    spec = json.loads(Path('work/matrices.json').read_text())['matrices']
    names = args.matrices or list(spec)
    assert args.height >= 1
    started = time.monotonic()
    free = FreeLie(3, args.height)
    certificate = {'height': args.height, 'field': 'Q' if args.prime is None else f'F_{args.prime}',
                   'prime': args.prime, 'matrices': {}, 'conventions': '[f_i,e_j]=-delta_ij*h_i; [h_i,e_j]=a_ij*e_j'}
    summaries = {}
    for name in names:
        matrix = spec[name]
        before = time.monotonic()
        records = compute_matrix(matrix, free, Field(args.prime))
        for record in records:
            expected = control_dimension(name, tuple(record['alpha']))
            if expected is not None:
                assert record['serre_dim'] == expected, (name, record, expected)
                assert record['contragredient_dim'] == expected, (name, record, expected)
        totals = {}
        for record in records:
            degree = sum(record['alpha'])
            row = totals.setdefault(str(degree), {'free': 0, 'serre': 0, 'contragredient': 0})
            row['free'] += record['free_dim']
            row['serre'] += record['serre_dim']
            row['contragredient'] += record['contragredient_dim']
        extras = [{'alpha': r['alpha'], 'dimension': r['extra_relations']} for r in records if r['extra_relations']]
        summaries[name] = {'matrix': matrix, 'graded_dimensions': totals, 'extra_relations': extras,
                           'root_degrees': len(records), 'elapsed_seconds': round(time.monotonic() - before, 3)}
        certificate['matrices'][name] = {'matrix': matrix, 'records': records}
        print(json.dumps({'completed': name, 'field': certificate['field'], 'height': args.height,
                          'extra_relations': extras, 'seconds': summaries[name]['elapsed_seconds']}), flush=True)
    args.output.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(certificate, sort_keys=True, separators=(',', ':')).encode()
    certpath = args.output / 'certificate.json.gz'
    with certpath.open('wb') as stream:
        with gzip.GzipFile(filename='', fileobj=stream, mode='wb', mtime=0) as archive:
            archive.write(encoded)
    source_sha = {f: hashlib.sha256(Path(f).read_bytes()).hexdigest()
                  for f in ('work/graded_lie.py', 'work/compute.py', 'work/matrices.json')}
    result = {'date': '2026-10-14', 'height': args.height, 'field': certificate['field'],
              'prime': args.prime, 'matrices': summaries, 'processes': 1,
              'elapsed_seconds': round(time.monotonic() - started, 3), 'source_sha256': source_sha,
              'certificate': str(certpath), 'certificate_sha256': hashlib.sha256(certpath.read_bytes()).hexdigest(),
              'claim_limit': 'Finite multigraded computation only; prime-field ranks do not alone prove a characteristic-zero statement.'}
    (args.output / 'results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'result': str(args.output / 'results.json'), 'seconds': result['elapsed_seconds']}), flush=True)


if __name__ == '__main__':
    main()
