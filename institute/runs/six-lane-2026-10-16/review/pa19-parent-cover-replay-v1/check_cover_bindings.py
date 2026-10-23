"""Independent parent R1/R2/R4 check of the frozen PA19 coverage inputs; no solver or proof replay.
R1 enumerates partitions and profile multisets without importing worker code.
R2 regenerates all486 balanced quad graphs with the pinned nauty binary, checks graph properties and every index binding.
R4 binds every one of5577 specifications to its declared profile multiset and skeleton, verifies basic skeleton
incidence invariants, and checks that each M1->M2 map is a permutation. This does not independently establish
isomorphism of the M1/M2 lists; that is a later generation replay.
"""
import hashlib
import itertools
import json
import math
import subprocess
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
INP = HERE / 'inputs'
GENG = Path('/opt/homebrew/Cellar/nauty/2.9.3/bin/geng')
LABELG = Path('/opt/homebrew/Cellar/nauty/2.9.3/bin/labelg')
EXPECTED_COUNTS = [3215, 59, 674, 39, 73, 482, 482, 482, 71]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def now():
    return subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()


def check_profiles():
    D = json.loads((INP / 'data/profiles-19-8-6.json').read_text())
    parts = [tuple(reversed(c)) for c in itertools.combinations_with_replacement(range(20), 6) if sum(c) == 19]
    pair_total = math.comb(19, 2)
    agreeing = lambda p: sum(math.comb(x, 2) for x in p)
    minimum = min(map(agreeing, parts))
    budget = pair_total - 8 * minimum
    profiles = [p for p in parts if agreeing(p) <= minimum + budget]
    if len(parts) != 235 or minimum != 21 or budget != 3 or len(profiles) != 6:
        raise ValueError('independent profile count')
    if set(profiles) != {tuple(x['profile']) for x in D['profiles']}:
        raise ValueError('profile list mismatch')
    if any(x['kappa'] != agreeing(x['profile']) or x['excess'] != agreeing(x['profile']) - minimum for x in D['profiles']):
        raise ValueError('profile attributes mismatch')
    canonical = lambda ps: tuple(sorted(tuple(p) for p in ps))
    all_multisets = set()
    for choice in itertools.combinations_with_replacement(range(6), 8):
        ps = [profiles[j] for j in choice]
        if sum(agreeing(p) - minimum for p in ps) <= budget:
            all_multisets.add(canonical(ps))
    recorded = [canonical(x['profiles']) for x in D['multisets']]
    if len(recorded) != 10 or len(set(recorded)) != 10 or set(recorded) != all_multisets:
        raise ValueError('profile-multiset coverage mismatch')
    for ms in D['multisets']:
        e = sum(agreeing(p) - minimum for p in ms['profiles'])
        if ms['excess'] != e or ms['zero_agreement_pairs'] != budget - e:
            raise ValueError('multiset slack mismatch')
    return D, {'partitions': len(parts), 'profiles': len(profiles), 'multisets': len(recorded), 'minimum': minimum, 'budget': budget}


def graph6_edges(line):
    n = line[0] - 63
    if n != 8:
        raise ValueError('balanced graph order')
    bits = [(v >> b) & 1 for c in line[1:] for v in [c - 63] for b in range(5, -1, -1)]
    edges, at = [], 0
    for j in range(1, n):
        for i in range(j):
            if bits[at]:
                edges.append((i, j))
            at += 1
    if any(bits[at:]):
        raise ValueError('graph6 padding')
    return edges


def check_balanced():
    r = subprocess.run([str(GENG), '-q', '8', '13:16', '-D4'], capture_output=True)
    if r.returncode:
        raise ValueError('geng failed')
    source = (INP / 'data/quadgraphs-8v-13to16e-D4.g6').read_bytes()
    if r.stdout != source:
        raise ValueError('balanced graph regeneration mismatch')
    lines = source.splitlines()
    counts = Counter()
    for line in lines:
        edges = graph6_edges(line)
        deg = Counter(x for edge in edges for x in edge)
        if not 13 <= len(edges) <= 16 or max(deg.values()) > 4:
            raise ValueError('balanced graph constraints')
        counts[len(edges)] += 1
    c = subprocess.run([str(LABELG), '-q'], input=source, capture_output=True)
    if c.returncode or len(set(c.stdout.splitlines())) != 486:
        raise ValueError('balanced graph distinct classes')
    idx = json.loads((INP / 'cases19q0/index.json').read_text())
    if idx['num_cases'] != 486 or len(idx['cases']) != 486:
        raise ValueError('balanced case count')
    if any(row != {'tag': 'g%03d' % i, 'graph6': line.decode()} for i, (row, line) in enumerate(zip(idx['cases'], lines))):
        raise ValueError('balanced index binding')
    if dict(counts) != {13: 309, 14: 136, 15: 35, 16: 6}:
        raise ValueError('balanced graph edge histogram')
    return {'graphs': len(lines), 'distinct_classes': 486, 'edge_counts': dict(counts), 'all_index_bindings': True,
            'geng_sha256': sha(GENG), 'labelg_sha256': sha(LABELG), 'graph6_sha256': hashlib.sha256(source).hexdigest()}


def skeleton_invariants(S, c0, tmax):
    members = [tuple(e) for e in S['edges']] + [tuple(h) for h in S['hyper']]
    if len(members) != len(set(members)):
        raise ValueError('duplicate skeleton membership')
    pair_counts, deg = Counter(), Counter()
    for pos, item in enumerate(members):
        if tuple(sorted(set(item))) != item or not 2 <= len(item) <= tmax or any(v < 0 or v >= c0 for v in item):
            raise ValueError('skeleton membership format')
        if pos < len(S['edges']) and len(item) != 2:
            raise ValueError('skeleton edge length')
        if pos >= len(S['edges']) and len(item) < 3:
            raise ValueError('skeleton hyperedge length')
        pair_counts.update(itertools.combinations(item, 2))
        deg.update(item)
    if any(n > 1 for n in pair_counts.values()) or any(deg[v] > 4 for v in range(c0)):
        raise ValueError('nonlinear skeleton or overfull quad')
    private = sum(4 - deg[v] for v in range(c0))
    if S['empty'] < 0 or len(members) + private + S['empty'] != 19:
        raise ValueError('skeleton row accounting')


def check_specs(D):
    idx = json.loads((INP / 'cases19skel/index.json').read_text())
    if idx['num_cases'] != 5577 or len(idx['cases']) != 5577:
        raise ValueError('A2 index coverage')
    if len({r['tag'] for r in idx['cases']}) != 5577:
        raise ValueError('duplicate A2 tag')
    headers = {}
    for mi, expected in enumerate(EXPECTED_COUNTS, 1):
        H = json.loads((INP / ('skeletons/skeletons-ms%02d.json' % mi)).read_text())
        ps = D['multisets'][mi]['profiles']
        c0 = ps.count([4, 3, 3, 3, 3, 3])
        special = sorted([p for p in ps if p != [4, 3, 3, 3, 3, 3]],
                         key=lambda p: (-sum(math.comb(x, 2) for x in p), [-x for x in p]))
        L = D['multisets'][mi]['zero_agreement_pairs']
        wmin = sum(min(x - 3 for x in p) for p in special)
        tmax = min(c0, 2 - wmin)
        hmax = sum(x for p in special for x in p if x <= 2)
        if H['profiles'] != ps or H['c0'] != c0 or H['special'] != special or H['L'] != L:
            raise ValueError('skeleton profile binding')
        if H['wmin'] != wmin or H['tmax'] != tmax or H['hmax'] != hmax:
            raise ValueError('skeleton generation bounds')
        if H['num_skeletons'] != expected or len(H['skeletons']) != expected:
            raise ValueError('skeleton count')
        for S in H['skeletons']:
            skeleton_invariants(S, c0, tmax)
        headers[mi] = H
        mapping = json.loads((INP / ('cycle2/skel-b/compare-map-ms%02d.json' % mi)).read_text())
        if mapping['count_a'] != expected or mapping['count_b'] != expected or sorted(mapping['a_to_b']) != list(range(expected)):
            raise ValueError('M1/M2 map is not a permutation')
    seen = set()
    for row in idx['cases']:
        mi, si, tag = row['multiset'], row['skel'], row['tag']
        if mi not in headers or tag != 'ms%02d_s%05d' % (mi, si) or (mi, si) in seen:
            raise ValueError('A2 tag binding')
        seen.add((mi, si))
        H = headers[mi]
        spec = json.loads((INP / ('cases19skel/specs/' + tag + '.json')).read_text())
        if spec['kind'] != 'skel' or (spec['N'], spec['k'], spec['q']) != (19, 8, 6):
            raise ValueError('A2 spec parameters')
        if spec['multiset_index'] != mi or spec['skel_index'] != si:
            raise ValueError('A2 spec indices')
        if any(spec[k] != H[k] for k in ('c0', 'special', 'L')) or spec['skeleton'] != H['skeletons'][si]:
            raise ValueError('A2 spec skeleton binding')
    wanted = {(mi, si) for mi, H in headers.items() for si in range(len(H['skeletons']))}
    if seen != wanted:
        raise ValueError('A2 skeleton indices not completely covered')
    return {'cases': len(seen), 'counts': EXPECTED_COUNTS, 'all_specs_bound': True,
            'maps_are_permutations': True, 'limit': 'Map isomorphism and generator exhaustiveness still need independent replay.'}


def main():
    started = now()
    D, r1 = check_profiles()
    r2 = check_balanced()
    r4 = check_specs(D)
    rec = {'started': started, 'ended': now(), 'driver_sha256': sha(Path(__file__)),
           'R1_profiles': r1, 'R2_balanced_graphs': r2, 'R4_A2_bindings': r4,
           'verdict': 'PASS', 'scope': 'Coverage input bindings only. No UNSAT certificate or encoder is accepted by this receipt.'}
    with open(HERE / 'cover-binding-result.json', 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps(rec))


if __name__ == '__main__':
    main()
