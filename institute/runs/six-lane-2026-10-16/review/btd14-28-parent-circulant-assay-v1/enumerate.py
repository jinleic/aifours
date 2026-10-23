"""Definition-first two-circulant BTD assay. See protocol.json (frozen before enumeration).
No solver, no orbit pruning. Every permitted first row is counted exactly once by disjoint combinations.
"""
import hashlib
import itertools
import json
import math
import subprocess
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent


def now():
    return subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sequences(n, ones, twos):
    for t in itertools.combinations(range(n), twos):
        available = [j for j in range(n) if j not in t]
        for o in itertools.combinations(available, ones):
            a = [0] * n
            for j in t:
                a[j] = 2
            for j in o:
                a[j] = 1
            yield a


def acf(a):
    n = len(a)
    return tuple(sum(a[j] * a[(j + d) % n] for j in range(n)) for d in range(1, n // 2 + 1))


def matrix(a, b):
    n = len(a)
    return [[a[(j + i) % n] for j in range(n)] + [b[(j + i) % n] for j in range(n)] for i in range(n)]


def verify(M, n, ones, twos, colsum, lam):
    if len(M) != n or any(len(r) != 2 * n for r in M):
        raise ValueError('shape')
    if any(x not in (0, 1, 2) for r in M for x in r):
        raise ValueError('alphabet')
    if any(r.count(1) != ones or r.count(2) != twos for r in M):
        raise ValueError('row composition')
    if any(sum(M[i][j] for i in range(n)) != colsum for j in range(2 * n)):
        raise ValueError('column sum')
    if any(sum(x * y for x, y in zip(M[i], M[k])) != lam for i in range(n) for k in range(i)):
        raise ValueError('row inner product')


def profile(n, o, t):
    counts = Counter()
    representative = {}
    count = 0
    for a in sequences(n, o, t):
        k = acf(a)
        counts[k] += 1
        representative.setdefault(k, a)
        count += 1
        # Sum over all cyclic shifts equals (row sum)^2; verifies mirror indexing, including n even.
        off = 2 * sum(k) - (k[-1] if n % 2 == 0 else 0)
        if off + o + 4 * t != (o + 2 * t) ** 2:
            raise ValueError('autocorrelation checksum')
    expected = math.comb(n, t) * math.comb(n - t, o)
    if count != expected:
        raise ValueError('profile coverage')
    return counts, representative, count


def assay(n, colsum, ones, twos, lam, save=False):
    profiles = [(colsum - 2 * t, t) for t in range(colsum // 2 + 1)
                if 0 <= colsum - 2 * t <= n - t]
    hist, reps, sizes = {}, {}, {}
    for p in profiles:
        hist[p], reps[p], sizes[p] = profile(n, *p)
        if save:
            path = HERE / ('profile-%d-%d-signatures.json' % p)
            with open(path, 'x') as f:
                json.dump({'profile': p, 'count': sizes[p],
                           'signatures': [{'acf': k, 'multiplicity': v} for k, v in sorted(hist[p].items())]}, f)
                f.write('\n')
    result = {'n': n, 'profiles': [], 'pairs': [], 'witnesses': []}
    for p in profiles:
        result['profiles'].append({'ones': p[0], 'twos': p[1], 'rows': sizes[p], 'acf_signatures': len(hist[p])})
    seen = set()
    for p in profiles:
        q = (ones - p[0], twos - p[1])
        if q not in hist or frozenset((p, q)) in seen:
            continue
        seen.add(frozenset((p, q)))
        total = 0
        signature_matches = 0
        for k, ca in hist[p].items():
            want = tuple(lam - x for x in k)
            cb = hist[q].get(want, 0)
            if cb:
                signature_matches += 1
                total += ca * cb
                a, b = reps[p][k], reps[q][want]
                M = matrix(a, b)
                verify(M, n, ones, twos, colsum, lam)
                if len(result['witnesses']) < 10:
                    result['witnesses'].append({'a': a, 'b': b, 'matrix': M})
        result['pairs'].append({'p': p, 'q': q, 'sequence_pair_matches': total,
                                'signature_pair_matches': signature_matches})
    return result


def main():
    started, t0 = now(), time.monotonic()
    control = assay(3, 2, 2, 1, 1)
    control_ok = sum(x['sequence_pair_matches'] for x in control['pairs']) == 9
    if not control_ok:
        raise ValueError('positive control expected nine profile-pair matches')
    for w in control['witnesses']:
        verify(w['matrix'], 3, 2, 1, 2, 1)
    mutant = [r[:] for r in control['witnesses'][0]['matrix']]
    j = mutant[0].index(0)
    mutant[0][j] = 1
    reason = None
    try:
        verify(mutant, 3, 2, 1, 2, 1)
    except ValueError as e:
        reason = str(e)
    if reason != 'row composition':
        raise ValueError('mutation did not fail for intended reason')
    target = assay(14, 7, 8, 3, 6, save=True)
    matches = sum(x['sequence_pair_matches'] for x in target['pairs'])
    rec = {'started': started, 'ended': now(), 'wall_s': time.monotonic() - t0,
           'script_sha256': sha(Path(__file__)), 'protocol_sha256': sha(HERE / 'protocol.json'),
           'positive_control': control, 'mutation_rejection': reason,
           'target': target, 'target_sequence_pair_matches': matches,
           'verdict': 'WITNESS' if matches else 'RESTRICTED-CLASS-EMPTY',
           'limit': 'Excludes only matrices made of two 14x14 circulants, not unrestricted BTD(14,28).'}
    with open(HERE / 'result.json', 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps({k: rec[k] for k in ('started', 'ended', 'wall_s', 'target_sequence_pair_matches', 'verdict')}))
    print(json.dumps(target['profiles']))
    print(json.dumps(target['pairs']))


if __name__ == '__main__':
    main()
