"""Parent check of the pinned point-cyclic 2-(100,4,1) resolution: definition-first checker,
own seed expansion, seed difference property, lane-expander replay and intended-reason mutations."""
from collections import Counter
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
PIN = HERE / 'point-cyclic100-parent-inputs-v1'
OUT = HERE / 'point-cyclic100-parent-check-v2'
CHECKER = HERE / 'check_point_cyclic_resolution_independent.py'
LANE = HERE.parents[3] / 'information-science/evidence/six-lane-20261016/point-cyclic100'
CERT_SHA = '971f722460020f5a572b4f17f1cffe249488b8de079badbfa0184b9a79b4f7c1'
SEED_SHA = 'ac727835e2f15075e0697206d81482b634ed76c5f7ff000adc58bef43b256245'
EXPANDER_SHA = '8fe20ef270defd0924c3c4fc296919fc6ffe8bf9fcaeae6c1ed8cfd687ff25c6'


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run_checker(path, digest, name):
    receipt = OUT / (name + '.json')
    p = subprocess.run([sys.executable, '-B', str(CHECKER), str(path), '100', digest, str(receipt)],
                       capture_output=True, text=True, timeout=600)
    return p.returncode, json.loads(receipt.read_text())


def parse_seed(text):
    lines = text.rstrip('\n').split('\n')
    if lines[0] != 'PC-T2-SEED 100':
        raise ValueError('seed header')
    rows = [(line.split()[0], tuple(map(int, line.split()[1:]))) for line in lines[1:]]
    kinds = [k for k, _ in rows]
    if kinds != ['H'] + ['X'] * 6 + ['Y'] * 2 or any(len(r) != 4 for _, r in rows):
        raise ValueError('seed shape')
    return rows


def expand(rows, v=100):
    q = v // 4
    H = frozenset(rows[0][1])
    X = [frozenset(r) for k, r in rows if k == 'X']
    Y = [frozenset(r) for k, r in rows if k == 'Y']
    shift = lambda blk, t: frozenset((p + t) % v for p in blk)
    base = [H] + [shift(x, q * j) for x in X for j in range(4)]
    classes = [frozenset(shift(blk, t) for blk in base) for t in range(q)]
    for y in Y:
        cls = [shift(y, 4 * m) for m in range(q)]
        classes += [frozenset(shift(blk, t) for blk in cls) for t in range(4)]
    return rows, H, X, Y, classes


def canonical_text(classes, v=100):
    ordered = sorted(sorted(sorted(blk) for blk in cl) for cl in classes)
    lines = [f'POINT-CYCLIC-RESOLUTION {v} 4 {len(ordered)} {len(ordered[0])}']
    for j, cl in enumerate(ordered):
        lines += [f'{j} ' + ' '.join(map(str, blk)) for blk in cl]
    return '\n'.join(lines) + '\n'


def cert_classes(text):
    classes = {}
    for line in text.rstrip('\n').split('\n')[1:]:
        j, *pts = map(int, line.split())
        classes.setdefault(j, set()).add(frozenset(pts))
    return {frozenset(cl) for cl in classes.values()}


def mutations(text):
    lines = text.rstrip('\n').split('\n')
    out = {}
    def put(name, new_lines, intended):
        out[name] = ('\n'.join(new_lines) + '\n', intended)
    # swap the smallest points of two blocks of class 0 (class stays a partition, pairs break)
    a, b = lines[1].split(), lines[2].split()
    m = list(lines)
    pa = list(map(int, a[1:])); pb = list(map(int, b[1:]))
    pa[0], pb[0] = pb[0], pa[0]
    m[1] = a[0] + ' ' + ' '.join(map(str, sorted(pa)))
    m[2] = b[0] + ' ' + ' '.join(map(str, sorted(pb)))
    put('swap-points-within-class', m, 'pair')
    # exchange one block of class 0 with one block of class 1 (counts kept, partitions break)
    m = list(lines)
    first1 = next(i for i, l in enumerate(lines) if i > 0 and l.split()[0] == '1')
    blk0, blk1 = lines[1].split()[1:], lines[first1].split()[1:]
    m[1] = '0 ' + ' '.join(blk1)
    m[first1] = '1 ' + ' '.join(blk0)
    m = [m[0]] + sorted(m[1:], key=lambda s: (int(s.split()[0]), list(map(int, s.split()[1:]))))
    put('exchange-blocks-between-classes', m, 'partition')
    # duplicate a block in place of another in the same class
    m = list(lines); m[3] = lines[2]
    put('duplicate-block', m, 'repeated block')
    # replace one block by its +1 translate, which is another block of the cyclic design
    m = list(lines); parts = list(map(int, lines[5].split()))
    m[5] = str(parts[0]) + ' ' + ' '.join(map(str, sorted((p + 1) % 100 for p in parts[1:])))
    put('translate-one-block', m, 'repeated block')
    # header with wrong class count
    m = list(lines); m[0] = 'POINT-CYCLIC-RESOLUTION 100 4 32 25'
    put('wrong-header-class-count', m, 'forced value')
    # drop last line
    put('missing-block-line', lines[:-1], 'wrong number of block lines')
    # point out of range
    m = list(lines); parts = lines[7].split(); parts[-1] = '100'
    m[7] = ' '.join(parts)
    put('point-out-of-range', m, 'out of range')
    # relabel points 0 <-> 1 everywhere: still a resolved 2-(100,4,1) design, but x+1 is no automorphism
    swap = lambda p: {0: 1, 1: 0}.get(p, p)
    body = []
    for line in lines[1:]:
        j, *pts = map(int, line.split())
        body.append((j, sorted(swap(p) for p in pts)))
    body.sort()
    put('transpose-point-labels-0-1', [lines[0]] + [f'{j} ' + ' '.join(map(str, pts)) for j, pts in body],
        'not invariant under x+1')
    # exchange a common sub-partition between two classes: still a resolution of the same cyclic
    # design, but (checked below) no longer mapped onto itself by x+1
    classes = {}
    for line in lines[1:]:
        j, *pts = map(int, line.split())
        classes.setdefault(j, []).append(frozenset(pts))
    best = None
    for i in classes:
        for j in classes:
            if i >= j:
                continue
            nodes = [('a', blk) for blk in classes[i]] + [('b', blk) for blk in classes[j]]
            parent = list(range(len(nodes)))
            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x
            for x in range(25):
                for y in range(25, 50):
                    if nodes[x][1] & nodes[y][1]:
                        parent[find(x)] = find(y)
            comps = {}
            for x in range(50):
                comps.setdefault(find(x), []).append(x)
            if len(comps) >= 2:
                comp = min(comps.values(), key=len)
                if best is None or len(comp) < len(best[2]):
                    best = (i, j, comp, nodes)
    if best is not None:
        i, j, comp, nodes = best
        S = {nodes[x][1] for x in comp if nodes[x][0] == 'a'}
        T = {nodes[x][1] for x in comp if nodes[x][0] == 'b'}
        new = dict(classes)
        new[i] = [blk for blk in classes[i] if blk not in S] + sorted(T, key=sorted)
        new[j] = [blk for blk in classes[j] if blk not in T] + sorted(S, key=sorted)
        class_set = {frozenset(cl) for cl in new.values()}
        shifted = lambda cl: frozenset(frozenset((p + 1) % 100 for p in blk) for blk in cl)
        invariant = all(shifted(frozenset(cl)) in class_set for cl in new.values())
        body = sorted((c, sorted(blk)) for c, cl in new.items() for blk in cl)
        put('exchange-subpartition-between-classes', [lines[0]] + [f'{c} ' + ' '.join(map(str, blk)) for c, blk in body],
            'VALID_POINT_CYCLIC_RESOLUTION' if invariant else 'not mapped onto a listed class')
        out['_subpartition_info'] = (json.dumps({'classes': [i, j], 'blocks_exchanged_each_side': len(S),
                                                 'mutated_resolution_shift_invariant_by_own_check': invariant}), None)
    else:
        out['_subpartition_info'] = (json.dumps({'available': False}), None)
    return out


def main():
    OUT.mkdir(exist_ok=False)
    result = {'started_at_pt': stamp(), 'status': 'FAILED', 'driver_sha256': sha(__file__),
              'checker_sha256': sha(CHECKER)}
    try:
        cert, seed = PIN / 'pc100_t2.cert', PIN / 'pc100_t2.seed'
        if sha(cert) != CERT_SHA or sha(seed) != SEED_SHA:
            raise ValueError('pinned input SHA mismatch')
        rc, receipt = run_checker(cert, CERT_SHA, 'candidate')
        result['candidate'] = {'returncode': rc, 'receipt': receipt}
        if rc != 0 or receipt['status'] != 'VALID_POINT_CYCLIC_RESOLUTION':
            raise ValueError('candidate rejected by parent checker')
        text = cert.read_text()
        rows, H, X, Y, classes = expand(parse_seed(seed.read_text()))
        diffs = Counter((a - b) % 100 for blk in X + Y for a in blk for b in blk if a != b)
        expected = set(range(1, 100)) - {25, 50, 75}
        seed_ok = set(diffs) == expected and all(n == 1 for n in diffs.values())
        h_ok = H == frozenset({0, 25, 50, 75})
        expanded = canonical_text(classes)
        result['seed'] = {'difference_property_96_once': seed_ok, 'short_block_is_subgroup_of_order_4': h_ok,
                          'own_expansion_class_sets_equal_certificate': cert_classes(expanded) == cert_classes(text),
                          'own_expansion_bytes_equal_certificate': expanded == text,
                          'own_expansion_sha256': hashlib.sha256(expanded.encode()).hexdigest()}
        (OUT / 'own-expansion.cert').write_text(expanded)
        if not (seed_ok and h_ok and result['seed']['own_expansion_class_sets_equal_certificate']):
            raise ValueError('seed check failed')
        if sha(LANE / 'code/pc_expand.py') != EXPANDER_SHA:
            raise ValueError('lane expander changed since pin')
        p = subprocess.run([sys.executable, '-B', str(LANE / 'code/pc_expand.py'), str(seed), str(OUT / 'lane-expander-replay.cert')],
                           capture_output=True, text=True, timeout=600)
        result['lane_expander_replay'] = {'returncode': p.returncode, 'stdout_tail': p.stdout[-600:],
                                          'output_sha256': sha(OUT / 'lane-expander-replay.cert') if (OUT / 'lane-expander-replay.cert').exists() else None}
        result['lane_expander_replay']['bytes_equal_certificate'] = result['lane_expander_replay']['output_sha256'] == CERT_SHA
        if p.returncode != 0 or not result['lane_expander_replay']['bytes_equal_certificate']:
            raise ValueError('lane expander replay did not reproduce the pinned certificate')
        controls = []
        built = mutations(text)
        result['subpartition_exchange'] = json.loads(built.pop('_subpartition_info')[0])
        for name, (mtext, intended) in built.items():
            path = OUT / ('mutation-' + name + '.cert')
            path.write_text(mtext)
            rc, rec = run_checker(path, sha(path), 'mutation-' + name)
            if intended == 'VALID_POINT_CYCLIC_RESOLUTION':
                ok = rc == 0 and rec['status'] == intended
            else:
                ok = rc == 1 and rec['status'] == 'INVALID' and intended in rec['reason']
            controls.append({'name': name, 'returncode': rc, 'reason': rec.get('reason', rec.get('status')),
                             'intended': intended, 'intended_reason': ok})
        result['mutations'] = controls
        if not all(c['intended_reason'] for c in controls):
            raise ValueError('a mutation was not rejected for its intended reason')
        result['status'] = 'PARENT_VALID_SEED_REPLAY_AND_CONTROLS_PASS'
    except Exception as exc:
        result['error'] = type(exc).__name__ + ': ' + str(exc)
    finally:
        result['finished_at_pt'] = stamp()
        with (OUT / 'parent-result.json').open('x') as f:
            json.dump(result, f, indent=2)
            f.write('\n')
        print(json.dumps({k: result.get(k) for k in ['status', 'error', 'seed', 'lane_expander_replay']}, indent=2))
        for c in result.get('mutations', []):
            print(c)
    return 0 if result['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
