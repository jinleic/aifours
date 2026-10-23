"""Parent derivation of general point-cyclic seed sufficiency, independent of lane expander code.
PC-SEED v / SHORT t / (t-1)/4 X blocks / GROUP k followed by k Y blocks.
Checks the residue partitions and directed differences, expands all classes, and compares canonical
bytes to a separately pinned full certificate. Actual design validity is checked separately.
Usage: SEED EXPECTED_SEED_SHA CERT EXPECTED_CERT_SHA NEW_OUTPUT_DIR
"""
from collections import Counter
from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys
from zoneinfo import ZoneInfo


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def require(ok, reason):
    if not ok:
        raise ValueError(reason)


def expand(seed):
    lines = seed.decode('ascii').splitlines()
    require(lines[0].split()[0] == 'PC-SEED', 'seed header')
    v = int(lines[0].split()[1]); q = v // 4
    require(v % 12 == 4, 'order congruence')
    require(lines[1].split()[0] == 'SHORT', 'short parameter')
    t = int(lines[1].split()[1])
    require(t > 0 and q % t == 0 and t % 4 == 1, 'short orbit divisibility')
    pos = 2
    def block(tag):
        nonlocal pos
        data = lines[pos].split(); pos += 1
        require(data[0] == tag and len(data) == 5, 'block syntax')
        b = tuple(map(int, data[1:]))
        require(len(set(b)) == 4 and all(0 <= x < v for x in b), 'block range or cardinality')
        return b
    X = [block('X') for _ in range((t - 1) // 4)]
    groups = []
    while pos < len(lines):
        d = lines[pos].split(); pos += 1
        require(d[0] == 'GROUP' and len(d) == 2, 'group syntax')
        k = int(d[1]); require(k > 0 and q % k == 0, 'group divisibility')
        groups.append((k, [block('Y') for _ in range(k)]))
    require(sorted(x % t for b in X for x in b) == list(range(1, t)), 'X residue partition')
    for k, group in groups:
        require(sorted(x % (4 * k) for b in group for x in b) == list(range(4 * k)), 'Y residue partition')
    full = X + [b for _, group in groups for b in group]
    H = frozenset(range(0, v, q))
    diffs = Counter((a - b) % v for B in full for a in B for b in B if a != b)
    require(set(diffs) == set(range(v)) - H and all(n == 1 for n in diffs.values()), 'directed differences')
    shift = lambda B, s: tuple(sorted((x + s) % v for x in B))
    short_base = {shift(H, s) for s in range(0, v, t)}
    short_base.update(shift(B, s) for B in X for s in range(0, v, t))
    classes = [{shift(B, s) for B in short_base} for s in range(t)]
    for k, group in groups:
        base = {shift(B, s) for B in group for s in range(0, v, 4 * k)}
        classes.extend({shift(B, s) for B in base} for s in range(4 * k))
    require(len(classes) == (v - 1) // 3 and all(len(C) == q for C in classes), 'class counts')
    ordered = sorted(sorted(C) for C in classes)
    text = f'POINT-CYCLIC-RESOLUTION {v} 4 {len(ordered)} {q}\n'
    text += ''.join(f'{j} ' + ' '.join(map(str, B)) + '\n' for j, C in enumerate(ordered) for B in C)
    return text.encode(), {'v': v, 'short_class_orbit': t, 'group_parameters': [k for k, _ in groups],
                           'directed_differences_once': len(diffs), 'classes': len(classes), 'blocks_per_class': q}


def main():
    seed, seed_sha, cert, cert_sha, output = sys.argv[1:]
    out = Path(output); out.mkdir(exist_ok=False)
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(), 'status': 'FAILED',
              'driver_sha256': sha(__file__)}
    try:
        seed_bytes, cert_bytes = Path(seed).read_bytes(), Path(cert).read_bytes()
        require(hashlib.sha256(seed_bytes).hexdigest() == seed_sha and
                hashlib.sha256(cert_bytes).hexdigest() == cert_sha, 'input SHA mismatch')
        data, counts = expand(seed_bytes)
        (out / 'own-expanded.cert').write_bytes(data)
        require(data == cert_bytes, 'independent expansion bytes differ from pinned certificate')
        result.update(counts)
        result.update(seed_sha256=seed_sha, certificate_sha256=cert_sha, own_expansion_sha256=hashlib.sha256(data).hexdigest(),
                      status='PARENT_RESIDUE_DIFFERENCE_CONDITIONS_AND_BYTE_EXPANSION_PASS')
    except Exception as exc:
        result['error'] = type(exc).__name__ + ': ' + str(exc)
    with (out / 'parent-result.json').open('x') as f:
        json.dump(result, f, indent=2); f.write('\n')
    print(json.dumps(result))
    return 0 if result['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
