"""Parent independent check of every FH5 witness in the Sun k6 engine-v3 certificate set.
Written by the parent from CERT-FORMAT-k6-v1/v2 FH5 text and rules-k6-v1 L5/L6 + rules-k6-v2 L9 only (no engine code).
For each FH5 orbit and EACH of the seven E5 placements, exhaustively searches the full assignment space
(a fixed to t=1 and coset {0}; b and alpha_la=1 members of V: all 5 singletons; V members with alpha_la=c>1: all
C(5,c) subsets; every other vertex: t in 1..5 with all t-subsets) and confirms every assignment is rejected by
(i) F3 or (ii) the hereditary fgcd test in some coset.  Pruning only on already-rejected partial assignments
(both rejection conditions are monotone under adding vertices).  V is recomputed and must equal the witness V.
Usage: python3 -B check_sun_k6_parent_fh5_v1.py ENGINE_DIR OUTDIR   (OUTDIR must not exist)
"""
import gzip
import hashlib
import itertools
import json
import os
import sys
import time

BUDGET = 3000.0
T0 = time.monotonic()
EDGES = [(i, j) for j in range(6) for i in range(j)]
EIDX = {e: k for k, e in enumerate(EDGES)}
SAT = 30


def eid(a, b):
    return EIDX[(a, b) if a < b else (b, a)]


def val(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def fh5_check(rep, typ, wit):
    e2, c2, e3 = typ
    al = [[0] * 6 for _ in range(6)]
    for k, (i, j) in enumerate(EDGES):
        al[i][j] = al[j][i] = int(rep[k])
    (a, b), Vw, _counts = wit
    if not (0 <= a < 6 and 0 <= b < 6 and a != b) or al[a][b] != 1:
        return False, 'hypothesis alpha_ab=1 fails'
    V = sorted(v for v in range(6) if v not in (a, b) and al[v][a] == al[v][b])
    if not V or sorted(Vw) != V:
        return False, 'V mismatch or empty: recomputed %s witness %s' % (V, Vw)
    cosets = range(5)
    order = [a, b] + V + [l for l in range(6) if l not in V and l not in (a, b)]
    choices = {}
    choices[a] = [(1, frozenset([0]))]
    choices[b] = [(1, frozenset([c])) for c in cosets]
    for l in order[2:]:
        if l in V:
            c = al[l][a]
            choices[l] = [(c, frozenset(s)) for s in itertools.combinations(cosets, c)]
        else:
            choices[l] = [(t, frozenset(s)) for t in range(1, 6) for s in itertools.combinations(cosets, t)]
    stats = {}
    for e5 in [None, 0, 1, 2, 3, 4, 5]:
        def expo(l, t):
            x2 = val(t, 2) + (0 if l != e2 else (1 if c2 == 1 else SAT))
            x3 = val(t, 3) + (SAT if l == e3 else 0)
            x5 = val(t, 5) + (SAT if l == e5 else 0)
            return (x2, x3, x5)

        def fgcd(ex, ey):
            return 2 ** min(ex[0], ey[0]) * 3 ** min(ex[1], ey[1]) * 5 ** min(ex[2], ey[2])

        survivors = 0
        nodes = 0
        assign = {}

        def rejected_by_new(l):
            t_l, s_l = assign[l]
            # (i) F3 for pairs involving l, both directions
            for x, (t_x, s_x) in assign.items():
                if x == l:
                    continue
                if t_l == 1 and al[l][x] > t_x:
                    return True
                if t_x == 1 and al[x][l] > t_l:
                    return True
            # (ii) hereditary test in each coset l belongs to, subsets containing l
            ex = {x: expo(x, assign[x][0]) for x in assign}
            for c in s_l:
                M = [x for x in assign if c in assign[x][1]]
                others = [x for x in M if x != l]
                for r in range(1, len(others) + 1):
                    for Tm in itertools.combinations(others, r):
                        T = Tm + (l,)
                        sz = len(T)
                        if not any(fgcd(ex[x], ex[y]) >= sz for x, y in itertools.combinations(T, 2)):
                            return True
            return False

        def dfs(i):
            nonlocal survivors, nodes
            if time.monotonic() - T0 > BUDGET:
                raise TimeoutError
            if i == len(order):
                survivors += 1
                return
            l = order[i]
            for ch in choices[l]:
                nodes += 1
                assign[l] = ch
                if not rejected_by_new(l):
                    dfs(i + 1)
                del assign[l]
                if survivors:
                    return

        dfs(0)
        stats[str(e5)] = {'survivors': survivors, 'nodes': nodes}
        if survivors:
            return False, 'surviving assignment at e5=%s' % e5
    return True, stats


def main():
    eng, out = sys.argv[1], sys.argv[2]
    os.mkdir(out)
    raw = gzip.open(os.path.join(eng, 'orbits.jsonl.gz'), 'rb').read()
    lines = [json.loads(l) for l in raw.decode().splitlines() if l.strip()]
    fh = [l for l in lines if l['rule'] == 'FH5']
    res = {'script_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
           'orbits_jsonl_uncompressed_sha256': hashlib.sha256(raw).hexdigest(),
           'fh5_lines': len(fh), 'verified': 0, 'failed': 0, 'failures': [], 'max_nodes': 0, 'incomplete': False}
    try:
        for ln in fh:
            ok, info = fh5_check(ln['rep'], tuple(ln['type']), ln['witness'])
            if ok:
                res['verified'] += 1
                res['max_nodes'] = max(res['max_nodes'], max(v['nodes'] for v in info.values()))
            else:
                res['failed'] += 1
                if len(res['failures']) < 20:
                    res['failures'].append({'rep': ln['rep'], 'type': ln['type'], 'witness': ln['witness'], 'why': info})
    except TimeoutError:
        res['incomplete'] = True
    res['elapsed_s'] = round(time.monotonic() - T0, 1)
    with open(os.path.join(out, 'RESULT-FH5-v1.json'), 'x') as f:
        json.dump(res, f, indent=1)
        f.write('\n')
    print(json.dumps({k: res[k] for k in ('fh5_lines', 'verified', 'failed', 'incomplete', 'max_nodes', 'elapsed_s')}))


if __name__ == '__main__':
    main()
