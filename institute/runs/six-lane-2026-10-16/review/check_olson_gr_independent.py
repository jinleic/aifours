"""Finite cross-check of Lemma GR from its written equations against raw ordered-product DP.

No worker code imported. This checks mechanics on retained deterministic examples; it is not
an all-primes proof, an exhaustive theorem, or a solution of ordered Olson.
"""
from datetime import datetime
import hashlib
import itertools
import json
from pathlib import Path
import random
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PROOF = ROOT / 'mathematics/evidence/six-lane-20261016/olson/proof-GR.md'
OUT = HERE / 'olson-gr-parent-check-v1'


def raw_dp(p, word):
    """D_2p=(Z_p) semidirect C2; multiply (a,e)(b,f)=(a+(-1)^e b,e+f)."""
    target = 2 * p
    states = [set() for _ in range(target + 1)]
    states[0].add((0, 0))
    for index, (b, f) in enumerate(word):
        for count in range(min(target, index + 1), 0, -1):
            states[count].update(((a + (b if e == 0 else -b)) % p, (e + f) % 2)
                                 for a, e in states[count - 1])
    return (0, 0) in states[target]


def gr_equations(p, rotation_runs, reflection_runs, values):
    """Equations 19–27 of the pinned written proof; all arithmetic integral."""
    k = len(rotation_runs)
    R = sum(len(run) for run in rotation_runs)
    F = sum(reflection_runs)
    for z in itertools.product((-1, 1), repeat=k):
        flips = [int(z[i] != z[(i + 1) % k]) for i in range(k)]
        Phi = sum(flips)
        Cmax = F - sum((length - f) % 2 for length, f in zip(reflection_runs, flips))
        Eplus = sum(sum(a == sign for a in run) for run, sign in zip(rotation_runs, z))
        Eminus = R - Eplus
        s0, s1 = 2 * p - Cmax, 2 * p - Phi
        low = max(-s1, s0 - 2 * Eminus, -Eminus)
        high = min(s1, 2 * Eplus - s0, Eplus)
        tau = (-pow(2, -1, p) * sum(z[i] * (values[i] - values[i - 1]) for i in range(k))) % p
        if any(t % p == tau for t in range(low + low % 2, high + 1, 2)):
            return True
    return False


def main():
    OUT.mkdir(exist_ok=False)
    proof = PROOF.read_bytes()
    (OUT / 'proof-GR.snapshot.md').write_bytes(proof)
    rng = random.Random(202610162339)
    cases = []
    failures = []
    started = time.monotonic()
    for p in (3, 5, 7, 11, 13):
        for length in (4 * p - 1, 4 * p - 2, 4 * p - 3):
            for _ in range(120):
                k = rng.randint(1, min(8, length // 2))
                cuts = sorted(rng.sample(range(1, length), 2 * k - 1))
                sizes = [b - a for a, b in zip([0] + cuts, cuts + [length])]
                rotations = [[rng.choice((-1, 1)) for _ in range(sizes[2 * i])] for i in range(k)]
                reflections = sizes[1::2]
                values = [rng.randrange(p) for _ in range(k)]
                word = []
                for run, size, y in zip(rotations, reflections, values):
                    word.extend((a % p, 0) for a in run)
                    word.extend([(y, 1)] * size)
                direct = raw_dp(p, word)
                criterion = gr_equations(p, rotations, reflections, values)
                row = {'p': p, 'length': length, 'rotations': rotations, 'reflection_lengths': reflections,
                       'reflection_values': values, 'word': word, 'raw_dp': direct, 'gr': criterion}
                cases.append(row)
                if direct != criterion:
                    failures.append(len(cases) - 1)
    # Boundary and nontrivial no-solution controls: a length-2p word with an odd reflection count
    # has only one full-length selection, which cannot be identity. Rotations remain +/-1.
    for p in (3, 5, 7, 11, 13):
        rotations, reflections, values = [[1] * (2 * p - 1)], [1], [0]
        word = [(1, 0)] * (2 * p - 1) + [(0, 1)]
        direct = raw_dp(p, word)
        criterion = gr_equations(p, rotations, reflections, values)
        cases.append({'p': p, 'length': len(word), 'control': 'single available selection has odd reflection parity',
                      'rotations': rotations, 'reflection_lengths': reflections, 'reflection_values': values,
                      'word': word, 'raw_dp': direct, 'gr': criterion})
        if direct or criterion:
            failures.append(len(cases) - 1)
    fixtures = OUT / 'cases.json'
    with fixtures.open('x') as stream:
        json.dump(cases, stream, separators=(',', ':'))
        stream.write('\n')
    result = {'status': 'FINITE_GR_MECHANICS_PASS' if not failures else 'DISAGREEMENT',
              'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'proof_sha256': hashlib.sha256(proof).hexdigest(),
              'cases_sha256': hashlib.sha256(fixtures.read_bytes()).hexdigest(), 'seed': 202610162339,
              'cases': len(cases), 'raw_dp_no_cases': sum(not row['raw_dp'] for row in cases),
              'nonboundary_no_cases': sum(not row['raw_dp'] and 'control' not in row for row in cases),
              'failure_indices': failures, 'duration_seconds': time.monotonic() - started,
              'scope': 'Independent finite mechanics only. Does not prove Lemma GR for all p or solve its no-window remainder.'}
    with (OUT / 'parent-result.json').open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(result, indent=2))
    return int(bool(failures))


if __name__ == '__main__':
    raise SystemExit(main())
