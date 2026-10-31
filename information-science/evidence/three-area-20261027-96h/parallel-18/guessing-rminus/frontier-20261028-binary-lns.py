#!/usr/bin/env python3
"""Bounded large-neighbourhood search for actual binary R-minus winning sets.

A candidate support is valid for arbitrary full-domain decoders iff all pair
conflicts are absent.  Z3 supplies candidates only; every returned support is
independently checked by lookup tables before recording it.  A neighbourhood
failure is not a global bound or an unrestricted impossibility result.
"""
from itertools import combinations
from pathlib import Path
import hashlib
import json
import random
import time

from z3 import Bool, Or, Not, PbGe, Solver, sat

INPUT = Path(__file__).with_name('frontier-20261028-fd-law-search-precise-result.json')
OUTPUT = Path(__file__).with_name('frontier-20261028-binary-lns-result.json')
NEIGHBOURS = {
    1: (2, 3, 4, 5, 6, 7), 2: (1, 3, 7, 9, 10),
    3: (1, 2, 4, 8, 9), 4: (1, 3, 5, 8, 10),
    5: (1, 4, 6, 9, 10), 6: (1, 5, 7, 8, 9),
    7: (1, 2, 6, 8, 10), 8: (3, 4, 6, 7, 9, 10),
    9: (2, 3, 5, 6, 8), 10: (2, 4, 5, 7, 8),
}
SEED = 2026102801
MAX_SECONDS = 55.0
MAX_TRIALS = 25
SOLVER_MILLISECONDS = 2000
MAX_POOL = 220


def check(words):
    if len(set(words)) != len(words):
        return False
    tables = {v: {} for v in range(1, 11)}
    for w in words:
        for v, neighbours in NEIGHBOURS.items():
            key = tuple((w >> (u - 1)) & 1 for u in neighbours)
            value = (w >> (v - 1)) & 1
            if key in tables[v] and tables[v][key] != value:
                return False
            tables[v][key] = value
    return True


def main():
    started = time.monotonic()
    raw = INPUT.read_bytes()
    current = set(json.loads(raw)['support_words_one_based_bitsets'])
    assert len(current) == 88 and check(current)
    original = set(current)
    masks = {v: sum(1 << (u - 1) for u in neighbours)
             for v, neighbours in NEIGHBOURS.items()}
    bad = {d for d in range(1, 1024)
           if any((d & (1 << (v - 1))) and not (d & mask)
                  for v, mask in masks.items())}
    assert len(bad) == 113
    conflict = [sum(1 << (x ^ d) for d in bad) for x in range(1024)]
    universe = (1 << 1024) - 1
    rng = random.Random(SEED)
    best = set(current)
    records = []
    for trial in range(MAX_TRIALS):
        if time.monotonic() - started >= MAX_SECONDS:
            break
        remove_count = (14, 18, 22, 26, 30, 34)[trial % 6]
        removed = set(rng.sample(sorted(current), remove_count))
        keep = current - removed
        blocked = 0
        for w in keep:
            blocked |= conflict[w] | (1 << w)
        available_mask = universe & ~blocked
        pool = [w for w in range(1024) if (available_mask >> w) & 1]
        assert removed <= set(pool)
        if len(pool) > MAX_POOL:
            records.append({'trial': trial, 'removed': remove_count, 'pool': len(pool),
                            'status': 'SKIPPED_POOL_LIMIT'})
            continue
        x = [Bool(f'x_{trial}_{w}') for w in pool]
        solver = Solver()
        solver.set(timeout=SOLVER_MILLISECONDS, random_seed=SEED % 2147483647)
        for i, j in combinations(range(len(pool)), 2):
            if (conflict[pool[i]] >> pool[j]) & 1:
                solver.add(Or(Not(x[i]), Not(x[j])))
        solver.add(PbGe([(y, 1) for y in x], remove_count + 1))
        status = solver.check()
        result = {'trial': trial, 'removed': remove_count, 'pool': len(pool),
                  'status': str(status), 'before': len(current)}
        if status == sat:
            model = solver.model()
            chosen = {w for w, variable in zip(pool, x) if bool(model.eval(variable, model_completion=True))}
            candidate = keep | chosen
            assert len(candidate) >= len(current) + 1 and check(candidate)
            current = candidate
            if len(candidate) > len(best):
                best = set(candidate)
            result['after'] = len(candidate)
            result['strict_original_target_gain'] = len(candidate) ** 3 > 2 ** 20
        else:
            # If a strict improvement was not found, search for a different
            # same-size replacement; its failure also says nothing globally.
            solver = Solver()
            solver.set(timeout=SOLVER_MILLISECONDS, random_seed=(SEED + trial + 1) % 2147483647)
            for i, j in combinations(range(len(pool)), 2):
                if (conflict[pool[i]] >> pool[j]) & 1:
                    solver.add(Or(Not(x[i]), Not(x[j])))
            solver.add(PbGe([(y, 1) for y in x], remove_count))
            solver.add(Or([x[i] for i, w in enumerate(pool) if w not in removed]))
            move = solver.check()
            result['equal_size_move'] = str(move)
            if move == sat:
                model = solver.model()
                chosen = {w for w, variable in zip(pool, x) if bool(model.eval(variable, model_completion=True))}
                candidate = keep | chosen
                assert len(candidate) >= len(current) and check(candidate)
                current = candidate
                if len(candidate) > len(best):
                    best = set(candidate)
                result['after'] = len(candidate)
        records.append(result)
        if len(best) ** 3 > 2 ** 20:
            break
    result = {
        'input_sha256': hashlib.sha256(raw).hexdigest(), 'seed': SEED,
        'time_cap_seconds': MAX_SECONDS, 'solver_per_check_milliseconds': SOLVER_MILLISECONDS,
        'pool_cap': MAX_POOL, 'planned_trials': MAX_TRIALS, 'trials': records,
        'elapsed_seconds': time.monotonic() - started,
        'original_size': len(original), 'best_size': len(best),
        'best_code': sorted(best), 'best_lookup_independently_validated': check(best),
        'strict_original_20_over_3_lower_gain_exact': len(best) ** 3 > 2 ** 20,
        'limits': 'Only a bounded q=2 support search. No global optimality, unrestricted upper bound, or absence of higher-alphabet/nonlinear strategies follows.',
    }
    with OUTPUT.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
