#!/usr/bin/env python3
"""Continue one saved exact minor with a larger, explicit research bound."""
import argparse
import gzip
import hashlib
import json
import signal
import sys
import time
from fractions import Fraction as Q
from pathlib import Path

import flint
from flint import fmpz_mpoly_ctx
from round2_uniform_producer import determinant, expired


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=600)
    parser.add_argument('--term-limit', type=int, default=250000)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    output_path = args.output/'certificate.json.gz'
    if output_path.exists():
        raise FileExistsError(output_path)
    encoded = args.input.read_bytes()
    data = json.loads(gzip.decompress(encoded))
    spec = {'argv': sys.argv, 'input_sha256': hashlib.sha256(encoded).hexdigest(),
            'seconds': args.seconds, 'term_limit': args.term_limit, 'threads': 1,
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'determinant_source_sha256': hashlib.sha256(Path('work/round2_uniform_producer.py').read_bytes()).hexdigest()}
    with (args.output/'input.json').open('x') as stream:
        json.dump(spec, stream, indent=2)
    flint.ctx.threads = 1
    signal.signal(signal.SIGALRM, expired)
    started = time.monotonic()
    with (args.output/'execution.jsonl').open('x') as log:
        def event(detail):
            log.write(json.dumps({'elapsed_seconds': round(time.monotonic()-started, 3), **detail})+'\n')
            log.flush()
        try:
            signal.setitimer(signal.ITIMER_REAL, args.seconds)
            variables = len(data['variable_edges'])
            arity = max(1, variables)
            ring = fmpz_mpoly_ctx.get(tuple('x'+str(i) for i in range(arity)))
            gens = ring.gens()
            denominator = data['denominator']
            matrix = [[ring.constant(int(Q(entry[0])*denominator)) +
                       sum((gens[k]*int(Q(entry[k+1])*denominator) for k in range(variables)), ring.constant(0))
                       for entry in row] for row in data['minor_affine']]
            value = determinant(matrix, ring, args.term_limit, event)
            terms = value.to_dict()
            constant = int(terms.get((0,)*arity, 0))
            if not constant:
                raise ArithmeticError('zero baseline determinant')
            orientation = 1 if constant > 0 else -1
            normalized = sorted((tuple(map(int, powers)), orientation*int(coefficient)) for powers, coefficient in terms.items())
            negative = sum(coefficient < 0 for powers, coefficient in normalized)
            data.update(status='POSITIVE_MINOR_CANDIDATE' if not negative else 'SIGN_TEST_INCONCLUSIVE',
                        orientation=orientation, constant=str(abs(constant)), monomials=len(normalized),
                        negative_coefficients=negative,
                        polynomial_terms=[[list(powers) if variables else [], str(coefficient)] for powers, coefficient in normalized])
        except (TimeoutError, OverflowError, ArithmeticError) as error:
            data.update(status=type(error).__name__.upper(), error=str(error))
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)
        data['elapsed_seconds'] = round(time.monotonic()-started, 3)
        event({'status': data['status']})
    with gzip.open(output_path, 'xt') as stream:
        json.dump(data, stream, sort_keys=True)
    result = {k: v for k, v in data.items() if k not in ('minor_affine', 'polynomial_terms')}
    result['certificate_sha256'] = hashlib.sha256(output_path.read_bytes()).hexdigest()
    (args.output/'result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
