#!/usr/bin/env python3
"""Exact row-content elimination for a saved hard affine minor.

For an m-square matrix with pivot p, set C_ij=p*B_ij-B_i0*B_0j.
Then det(B)=det(C)/p**(m-2). Extracting each row gcd of C reduces
intermediate growth. Scalar factors are factored and cancelled exactly;
the final polynomial, if produced within the bound, has the usual format.
"""
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
from round2_uniform_producer import expired


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=300)
    parser.add_argument('--term-limit', type=int, default=250000)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    blob = args.input.read_bytes()
    data = json.loads(gzip.decompress(blob))
    spec = {'argv': sys.argv, 'input_sha256': hashlib.sha256(blob).hexdigest(),
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'seconds': args.seconds, 'term_limit': args.term_limit, 'threads': 1}
    with (args.output/'input.json').open('x') as stream:
        json.dump(spec, stream, indent=2)
    flint.ctx.threads = 1
    signal.signal(signal.SIGALRM, expired)
    start = time.monotonic()
    with (args.output/'execution.jsonl').open('x') as log:
        def event(record):
            log.write(json.dumps({'seconds': round(time.monotonic()-start, 3), **record})+'\n')
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
            scalar, factors = Q(1), {}
            def register(poly, exponent):
                nonlocal scalar
                if not exponent:
                    return
                content, decomposition = poly.factor()
                scalar *= Q(int(content))**exponent
                rebuilt = ring.constant(int(content))
                for factor, multiplicity in decomposition:
                    rebuilt *= factor**multiplicity
                    identity = tuple(sorted((tuple(map(int, powers)), int(coefficient)) for powers, coefficient in factor.to_dict().items()))
                    old = factors.get(identity, (factor, 0))
                    factors[identity] = (factor, old[1]+int(multiplicity)*exponent)
                if rebuilt != poly:
                    raise ArithmeticError('factorization identity failed')
            pivot_index = 0
            while len(matrix) > 1:
                m = len(matrix)
                selected = next((r for r in range(m) if matrix[r][0].to_dict().get((0,)*arity, 0)), None)
                if selected is None:
                    raise ArithmeticError('no nonzero baseline pivot')
                if selected:
                    matrix[0], matrix[selected] = matrix[selected], matrix[0]
                    scalar = -scalar
                pivot = matrix[0][0]
                register(pivot, -(m-2))
                next_matrix = []
                maximum = 0
                for i in range(1, m):
                    row = [pivot*matrix[i][j]-matrix[i][0]*matrix[0][j] for j in range(1, m)]
                    content = next(value for value in row if value)
                    for value in row:
                        if value:
                            content = content.gcd(value)
                    register(content, 1)
                    stripped = []
                    for value in row:
                        quotient, remainder = divmod(value, content)
                        if remainder:
                            raise ArithmeticError('row content does not divide an entry')
                        maximum = max(maximum, len(quotient))
                        if maximum > args.term_limit:
                            raise OverflowError('content-stripped entry term bound')
                        stripped.append(quotient)
                    next_matrix.append(stripped)
                matrix = next_matrix
                event({'pivot': pivot_index, 'remaining_dimension': len(matrix), 'largest_entry_terms': maximum})
                pivot_index += 1
            register(matrix[0][0], 1)
            if any(exponent < 0 for factor, exponent in factors.values()):
                raise ArithmeticError('uncancelled nonconstant denominator factor')
            polynomial = ring.constant(scalar.numerator)
            for factor, exponent in factors.values():
                if exponent:
                    polynomial *= factor**exponent
                    if len(polynomial) > args.term_limit:
                        raise OverflowError('expanded final determinant term bound')
            polynomial, remainder = divmod(polynomial, ring.constant(scalar.denominator))
            if remainder:
                raise ArithmeticError('nonintegral final determinant')
            terms = polynomial.to_dict()
            constant = int(terms.get((0,)*arity, 0))
            if not constant:
                raise ArithmeticError('zero final baseline determinant')
            orientation = 1 if constant > 0 else -1
            normalized = sorted((tuple(map(int, powers)), orientation*int(coefficient)) for powers, coefficient in terms.items())
            negative = sum(coefficient < 0 for powers, coefficient in normalized)
            data.update(status='POSITIVE_MINOR_CANDIDATE' if not negative else 'SIGN_TEST_INCONCLUSIVE',
                        orientation=orientation, constant=str(abs(constant)), monomials=len(normalized),
                        negative_coefficients=negative,
                        polynomial_terms=[[list(powers) if variables else [], str(coefficient)] for powers, coefficient in normalized],
                        determinant_algorithm='row-content elimination and checked factorization identities')
        except (TimeoutError, OverflowError, ArithmeticError) as error:
            data.update(status=type(error).__name__.upper(), error=str(error))
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)
        data['elapsed_seconds'] = round(time.monotonic()-start, 3)
        event({'status': data['status']})
    with gzip.open(args.output/'certificate.json.gz', 'xt') as stream:
        json.dump(data, stream, sort_keys=True)
    result = {k: v for k, v in data.items() if k not in ('minor_affine', 'polynomial_terms')}
    result['certificate_sha256'] = hashlib.sha256((args.output/'certificate.json.gz').read_bytes()).hexdigest()
    (args.output/'result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
