#!/usr/bin/env python3
"""Find nearby integer weights balancing the 88-word FD candidate's marginals.

The solver supplies candidate weights only; a separate exact integer checker
must verify every mathematical claim. No solver status implies an original bound.
"""
from hashlib import sha256
from pathlib import Path
import json
import math

from z3 import If, Int, Solver, Sum, sat

INPUT = Path(__file__).with_name('frontier-20261028-fd-law-search-result.json')
OUTPUT = Path(__file__).with_name('frontier-20261028-law-balance-result.json')


def binary_entropy(a, total):
    return sum(-(n / total) * math.log(n / total)
               for n in (a, total - a) if n)


def main():
    raw = INPUT.read_bytes()
    data = json.loads(raw)
    words = data['support_words_one_based_bitsets']
    original = data['rounded_probability_numerators']
    total = data['rounded_probability_denominator']
    assert len(words) == len(original) == 88 and total == sum(original) == 600
    variables = [Int(f'w_{i}') for i in range(len(words))]
    solver = Solver()
    solver.set(timeout=10000)
    solver.add(Sum(variables) == total)
    for old, new in zip(original, variables):
        solver.add(new >= max(1, old - 3), new <= old + 3)
    ones = [Sum([variables[j] for j, word in enumerate(words) if (word >> i) & 1])
            for i in range(10)]
    signs = data['best_search_float']['marginal_one_probs']
    for entry, sign in zip(ones, signs):
        if sign < 0.5:
            solver.add(entry >= 240, entry <= 246)
        else:
            solver.add(entry >= 354, entry <= 360)
    distance = Sum([If(new >= old, new - old, old - new)
                    for old, new in zip(original, variables)])
    attempts = []
    values = None
    for limit in (12, 20, 30, 40, 60, 100, 150, 264):
        solver.push()
        solver.add(distance <= limit)
        status = solver.check()
        attempts.append({'l1_limit': limit, 'status': str(status)})
        if status == sat:
            model = solver.model()
            values = [model.eval(v).as_long() for v in variables]
            solver.pop()
            break
        solver.pop()
    if values is None:
        result = {'candidate_sha256': sha256(raw).hexdigest(),
                  'solver_attempts': attempts, 'weights_found': False,
                  'limits': 'Failure/timeout does not rule out a better law.'}
    else:
        marginal = [sum(values[j] for j, word in enumerate(words) if (word >> i) & 1)
                    for i in range(10)]
        assert sum(values) == total
        assert all(abs(a-b) <= 3 and a > 0 for a, b in zip(values, original))
        assert all((240 <= c <= 246) if s < 0.5 else (354 <= c <= 360)
                   for c, s in zip(marginal, signs))
        h = -sum((w / total) * math.log(w / total) for w in values)
        cap = max(binary_entropy(c, total) for c in marginal)
        result = {'candidate_sha256': sha256(raw).hexdigest(),
                  'solver_attempts': attempts, 'weights_found': True,
                  'support_words_one_based_bitsets': words,
                  'rounded_probability_numerators': values,
                  'rounded_probability_denominator': total,
                  'weighted_marginal_one_counts': marginal,
                  'l1_change': sum(abs(a-b) for a, b in zip(values, original)),
                  'numerical_ratio_unverified': h / cap,
                  'limits': 'Solver output and float are candidates only; all FD and strict entropy claims need independent exact verification.'}
    with OUTPUT.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ('support_words_one_based_bitsets', 'rounded_probability_numerators')}, indent=2))


if __name__ == '__main__':
    main()
