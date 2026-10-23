#!/usr/bin/env python3
"""Freeze receipt for the order-12 finite-exact computations (D12, Dic3, A4; L = 23).

Records (no recomputation of the long runs):
  * sha256 of sources, binaries, group tables, orbit files, automorphism files;
  * group-table validation (closure, identity, inverses, associativity) and an
    isomorphism-type fingerprint (element-order histogram, centre size,
    number of involutions, exponent);
  * chunk coverage for the chunked direct runs: the set of (orbit, second)
    chunks equals {(o, a) : orbit(a) >= o} exactly once each, all counts 0;
  * identity-letter-reduction records e = 11..0 (count per e) and the live
    status of any unfinished e (from the progress log; no completion claimed);
  * an independent brute-force cross-check of the olson_dfs counting machinery on
    small (L, K) for each group (normalised words, same normalisation);
  * a mutation control (corrupted table rejected by the binary's validator).
Usage: python3 code/receipt_order12.py OUT.json
"""
import hashlib, itertools, json, os, subprocess, sys, time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
GDIR = os.path.join(LANE, 'evidence', 'groups')
RDIR = os.path.join(LANE, 'evidence', 'runs')
GROUPS = ['D12', 'Dic3', 'A4']

def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()

def load(g):
    rows = open(os.path.join(GDIR, g + '.tab')).read().split('\n')
    n = int(rows[0])
    T = [list(map(int, r.split())) for r in rows[1:1 + n]]
    orows = open(os.path.join(GDIR, g + '.orbits')).read().split('\n')
    orbit = list(map(int, orows[1].split()))
    inv = list(map(int, orows[2].split()))
    return n, T, orbit, inv

def validate(n, T, inv):
    ok = all(0 <= T[a][b] < n for a in range(n) for b in range(n))
    e = [x for x in range(n) if all(T[x][a] == a and T[a][x] == a for a in range(n))]
    ok &= e == [0]
    ok &= all(T[a][inv[a]] == 0 and T[inv[a]][a] == 0 for a in range(n))
    ok &= all(T[T[a][b]][c] == T[a][T[b][c]] for a in range(n) for b in range(n) for c in range(n))
    def order(a):
        k, x = 1, a
        while x != 0:
            x = T[x][a]; k += 1
        return k
    orders = Counter(order(a) for a in range(n))
    centre = sum(1 for a in range(n) if all(T[a][b] == T[b][a] for b in range(n)))
    return ok, {'order_hist': dict(sorted(orders.items())), 'centre_size': centre,
                'involutions': orders.get(2, 0), 'abelian': centre == n}

def brute_count(n, T, orbit, L, K):
    """Normalised words: w[0] = rep(o) (least element of orbit o), all letters orbit >= o;
    count those with no identity K-subword (ordered product, increasing indices)."""
    total = 0
    norb = max(orbit) + 1
    for o in range(norb):
        rep = min(a for a in range(n) if orbit[a] == o)
        allowed = [a for a in range(n) if orbit[a] >= o]
        for tail in itertools.product(allowed, repeat=L - 1):
            w = (rep,) + tail
            reach = [set() for _ in range(K + 1)]
            reach[0].add(0)
            bad = False
            for x in w:
                for k in range(K, 0, -1):
                    if reach[k - 1]:
                        reach[k] |= {T[g][x] for g in reach[k - 1]}
                if 0 in reach[K]:
                    bad = True
                    break
            if not bad:
                total += 1
    return total

def main():
    out = sys.argv[1]
    binp = os.path.join(HERE, 'olson_dfs')
    rec = {'created_host': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
           'sources': {f: sha(os.path.join(HERE, f)) for f in
                       ['olson_dfs.cpp', 'olson_dfs_id.cpp', 'chunk_driver.py', 'groups.py',
                        'autorbits.py', 'prep_group.py', 'receipt_order12.py']},
           'binaries': {b: sha(os.path.join(HERE, b)) for b in ['olson_dfs', 'olson_dfs_id']},
           'groups': {}}
    for g in GROUPS:
        n, T, orbit, inv = load(g)
        ok, fp = validate(n, T, inv)
        G = {'table_sha256': sha(os.path.join(GDIR, g + '.tab')),
             'orbits_sha256': sha(os.path.join(GDIR, g + '.orbits')),
             'aut_sha256': sha(os.path.join(GDIR, g + '.aut.json')) if os.path.exists(os.path.join(GDIR, g + '.aut.json')) else None,
             'table_valid_group': ok, 'fingerprint': fp, 'orbit_index': orbit}
        # chunked direct runs
        cpath = os.path.join(RDIR, f'{g}.L23.chunks.jsonl')
        chunks = [json.loads(l) for l in open(cpath) if l.strip()] if os.path.exists(cpath) else []
        expected = {(o, a) for o in range(max(orbit) + 1) for a in range(n) if orbit[a] >= o}
        got = Counter((c['orbit'], c['second']) for c in chunks)
        G['direct_L23'] = {'chunks_file_sha256': sha(cpath) if chunks else None,
                           'expected_chunks': len(expected), 'distinct_chunks': len(got),
                           'duplicates': sum(v - 1 for v in got.values() if v > 1),
                           'coverage_exact': set(got) == expected,
                           'all_counts_zero': all(c['count'] == 0 for c in chunks),
                           'status': 'complete' if chunks and set(got) == expected else
                                     ('not run / incomplete' if not chunks else 'incomplete')}
        # identity reduction
        ipath = os.path.join(RDIR, f'{g}.idred.jsonl')
        idred = [json.loads(l) for l in open(ipath) if l.strip()]
        es = {d['e']: d['count'] for d in idred}
        prog = [json.loads(l) for l in open(os.path.join(RDIR, f'{g}.idred.progress.jsonl')) if l.strip()]
        G['identity_reduction_L23'] = {'file_sha256': sha(ipath), 'counts_by_e': es,
                                       'complete_e_11_to_0': sorted(es) == list(range(12)),
                                       'all_zero': all(v == 0 for v in es.values()),
                                       'last_progress_line': prog[-1] if prog else None}
        # brute-force cross-check of the counting binary
        cross = []
        for (L, K) in [(5, 3), (6, 4)]:
            t0 = time.time()
            bf = brute_count(n, T, orbit, L, K)
            t_bf = time.time() - t0
            r = subprocess.run([binp, os.path.join(GDIR, g + '.tab'), os.path.join(GDIR, g + '.orbits'),
                                str(L), str(K), 'count', '20'], capture_output=True, text=True)
            res = json.loads(r.stdout)
            cross.append({'L': L, 'K': K, 'brute_force': bf, 'olson_dfs_total': res.get('total'),
                          'match': bf == res.get('total'), 'bf_secs': round(t_bf, 1)})
            print(g, L, K, bf, res.get('total'), flush=True)
        G['crosscheck_small'] = cross
        rec['groups'][g] = G
    # mutation control on D12
    n, T, orbit, inv = load('D12')
    T2 = [row[:] for row in T]
    T2[1][2], T2[1][3] = T2[1][3], T2[1][2]
    bad = os.path.join(GDIR, 'D12.corrupt.tab')
    with open(bad, 'w') as f:
        f.write(f"{n}\n" + '\n'.join(' '.join(map(str, r)) for r in T2) + '\n')
    r = subprocess.run([binp, bad, os.path.join(GDIR, 'D12.orbits'), '13', '12', 'count', '20'],
                       capture_output=True, text=True)
    rec['mutation_control'] = {'what': 'D12 table, two entries of row 1 swapped', 'exit': r.returncode,
                               'stderr': r.stderr.strip()[:200], 'expected': 'nonzero exit (validator rejects)'}
    json.dump(rec, open(out, 'w'), indent=1)
    print(json.dumps({g: {'valid': rec['groups'][g]['table_valid_group'],
                          'direct': rec['groups'][g]['direct_L23']['status'],
                          'idred': rec['groups'][g]['identity_reduction_L23']['counts_by_e'],
                          'cross': [c['match'] for c in rec['groups'][g]['crosscheck_small']]} for g in GROUPS}))
    print('mutation exit', r.returncode)

if __name__ == '__main__':
    main()
