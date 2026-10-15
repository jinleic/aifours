#!/usr/bin/env python3
"""Try exact falling-factorial positivity on previously failed sign tests.

For nonnegative integer x, (x)_k=x(x-1)...(x-k+1) is nonnegative, including
zero when x<k. A positive constant and nonnegative coefficients in the
multivariate falling-factorial basis therefore certify strict positivity.
This sufficient criterion is not asserted on nonintegral parameters.
No determinant is recomputed, and no existing certificate is overwritten.
"""
import argparse
import gzip
import hashlib
import json
import signal
import time
from pathlib import Path


def timeout(signum, frame):
    raise TimeoutError('falling-factorial transform deadline')


def transform(terms, variables, term_limit):
    maximum = max(max(powers, default=0) for powers in terms)
    stirling = [[1]]
    for n in range(1, maximum+1):
        previous = stirling[-1]
        stirling.append([0]+[(previous[k-1] if k-1 < len(previous) else 0)
                            + k*(previous[k] if k < len(previous) else 0) for k in range(1, n+1)])
    for variable in range(variables):
        changed = {}
        for powers, coefficient in terms.items():
            for k, multiplier in enumerate(stirling[powers[variable]]):
                if multiplier:
                    index = powers[:variable]+(k,)+powers[variable+1:]
                    changed[index] = changed.get(index, 0)+coefficient*multiplier
            if len(changed) > term_limit:
                raise OverflowError(f'falling-factorial support exceeds {term_limit} terms')
        terms = {powers: coefficient for powers, coefficient in changed.items() if coefficient}
    return terms


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds-per-polynomial', type=float, default=15)
    parser.add_argument('--term-limit', type=int, default=250000)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    if (args.output/'manifest.json').exists():
        raise FileExistsError(args.output/'manifest.json')
    signal.signal(signal.SIGALRM, timeout)
    started = time.monotonic()
    records, recovered = [], []
    with (args.output/'execution.jsonl').open('x') as log:
        for degree in ('322', '422', '332'):
            summary = json.loads((args.directory/f'degree-{degree}'/'summary.json').read_text())
            for cell in summary['results']:
                if cell['status'] != 'NO_POSITIVE_MINOR_FOUND':
                    continue
                for attempt in cell['attempts']:
                    if attempt['status'] != 'SIGN_TEST_INCONCLUSIVE':
                        continue
                    path = args.directory/f'degree-{degree}'/attempt['path']
                    data = json.loads(gzip.decompress(path.read_bytes()))
                    record = {'degree': degree, 'cell': cell['cell_key'],
                              'determinant_certificate': str(path.relative_to(args.directory)),
                              'determinant_sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
                    begin = time.monotonic()
                    try:
                        signal.setitimer(signal.ITIMER_REAL, args.seconds_per_polynomial)
                        terms = {tuple(powers): int(coefficient) for powers, coefficient in data['polynomial_terms']}
                        changed = transform(terms, len(data['variable_edges']), args.term_limit)
                        negative = sum(coefficient < 0 for coefficient in changed.values())
                        record.update(status='NEWTON_POSITIVITY_CANDIDATE' if not negative else 'NEWTON_SIGN_INCONCLUSIVE',
                                      monomials=len(changed), negative_coefficients=negative)
                        if not negative:
                            constant = changed.get((0,)*len(data['variable_edges']), 0)
                            if constant <= 0:
                                raise ArithmeticError('nonpositive Newton constant')
                            name = f'degree-{degree}-cell-{cell["cell_key"]}-newton.json.gz'
                            proof = {**record, 'constant': str(constant),
                                     'falling_factorial_terms': [[list(powers), str(coefficient)] for powers, coefficient in sorted(changed.items())],
                                     'domain': 'all free parameters are nonnegative integers'}
                            with gzip.open(args.output/name, 'xt') as stream:
                                json.dump(proof, stream, sort_keys=True)
                            record['newton_certificate'] = name
                            recovered.append(dict(record))
                    except (TimeoutError, OverflowError) as error:
                        record.update(status=type(error).__name__.upper(), error=str(error))
                    finally:
                        signal.setitimer(signal.ITIMER_REAL, 0)
                    record['elapsed_seconds'] = round(time.monotonic()-begin, 3)
                    records.append(record)
                    log.write(json.dumps(record)+'\n')
                    log.flush()
                    print(json.dumps(record), flush=True)
                    if record['status'] == 'NEWTON_POSITIVITY_CANDIDATE':
                        break
    manifest = {'records': records, 'recovered': recovered,
                'elapsed_seconds': round(time.monotonic()-started, 3), 'compute_processes': 1,
                'seconds_per_polynomial': args.seconds_per_polynomial, 'term_limit': args.term_limit,
                'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'scope': 'Producer candidates only; no independent checker run.'}
    (args.output/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')


if __name__ == '__main__':
    main()
