#!/usr/bin/env python3
"""Controls for the WAS solver (repr-WAS.md Sec. 2).

  dp     : fresh semidirect-product DP (left convention (v,e)(v',e') = (v+ev', ee')),
           written here independently of coverage_all.py.
  word   : (a, b, l, theta) -> explicit RGR word (y_{k-1} = 0, theta_i = y_{i-1} - y_i).
  key    : canonical class key of an RGR word under cyclic rotation and the
           automorphisms v -> u v (+ translation of reflection values).
Subcommands:
  check FILE p          every 'sol'/'all' line: DP must say NO identity 2p-subword
  mutant FILE p         every 'sol' line (mutated solver): DP must say YES (rejected)
  dump DUMP TAB ALLFILE p   compare canonical keys of the exhaustive avoider dump
                        (table convention 'a then b', converted by reversal) with
                        the WAS 'all' solutions; also structural predictions.
"""
import json, sys

def dp_has(word, p):
    n2 = 2 * p
    # reach[(size, e)] = bitmask of values v
    reach = {(0, 1): 1}
    for c, x in word:
        new = dict(reach)
        for (sz, e), m in reach.items():
            if sz >= n2:
                continue
            # multiply every v by (x, sign): v -> v + e*x
            sh = (e * x) % p
            mm = ((m << sh) | (m >> (p - sh))) & ((1 << p) - 1) if sh else m
            key = (sz + 1, e if c == 'R' else -e)
            new[key] = new.get(key, 0) | mm
        reach = new
    return bool(reach.get((n2, 1), 0) & 1)

def word_of(a, b, l, theta, p):
    k = len(a)
    y = [0] * k
    prev = 0  # y_{-1} = y_{k-1} = 0
    for i in range(k):
        y[i] = (prev - theta[i]) % p
        prev = y[i]
    assert y[k - 1] % p == 0
    w = []
    for i in range(k):
        w += [('R', 1)] * a[i] + [('R', p - 1)] * b[i] + [('F', y[i])] * l[i]
    return w

def key_of(word, p):
    n = len(word)
    rv = {x % p for c, x in word if c == 'R'}
    if not rv or not any(c == 'F' for c, _ in word):
        return None
    xs = [x for x in rv]
    if 0 in rv or len(rv) > 2 or (len(rv) == 2 and (xs[0] + xs[1]) % p):
        return None
    x = xs[0]
    starts = [i for i in range(n) if word[i][0] == 'R' and word[i - 1][0] == 'F']
    best = None
    for u in (pow(x, p - 2, p), (-pow(x, p - 2, p)) % p):
        for s in starts:
            w = [(c, (u * v) % p) for c, v in word[s:] + word[:s]]
            a, b, l, y = [], [], [], []
            i = 0
            ok = True
            while i < n:
                ca = cb = 0
                while i < n and w[i][0] == 'R':
                    if w[i][1] == 1: ca += 1
                    else: cb += 1
                    i += 1
                vals = set(); cl = 0
                while i < n and w[i][0] == 'F':
                    vals.add(w[i][1]); cl += 1; i += 1
                if len(vals) != 1:
                    ok = False; break
                a.append(ca); b.append(cb); l.append(cl); y.append(vals.pop())
            if not ok:
                return None
            k = len(a)
            th = tuple((y[i - 1] - y[i]) % p for i in range(k))
            cand = (k, tuple(a), tuple(b), tuple(l), th)
            if best is None or cand < best:
                best = cand
    return best

def load(path):
    return [json.loads(x) for x in open(path) if x.strip() and not x.startswith('{"summary"')]

def main():
    cmd = sys.argv[1]
    if cmd in ('check', 'mutant'):
        path, p = sys.argv[2], int(sys.argv[3])
        rows = [r for r in load(path) if 'theta' in r]
        bad = 0
        for r in rows:
            w = word_of(r['a'], r['b'], r['l'], r['theta'], p)
            has = dp_has(w, p)
            if (cmd == 'check' and has) or (cmd == 'mutant' and not has):
                bad += 1
        print(json.dumps({'cmd': cmd, 'file': path, 'rows': len(rows), 'violations': bad}))
    elif cmd == 'dump':
        dump, tab, allf, p = sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5])
        elems = json.load(open(tab))['elements']
        conv = []
        for g in elems:
            v = g[0] % p; e = (g[1] - g[0]) % p
            conv.append(('R' if e == 1 else 'F', v))
            assert e in (1, p - 1)
        dkeys = set(); nonrgr = 0; ndump = 0
        for line in open(dump):
            if not line.strip():
                continue
            ndump += 1
            idx = list(map(int, line.split()))
            w = [conv[i] for i in reversed(idx)]   # 'a then b' -> left convention
            assert not dp_has(w, p), 'dump word is not an avoider in left convention'
            k = key_of(w, p)
            if k is None:
                nonrgr += 1
            else:
                dkeys.add(k)
        rows = [r for r in load(allf) if r.get('all')]
        wkeys = set()
        struct = {'all_l_odd': 0, 'all_r_odd': 0, 'rot_runs_constant': 0, 'brackets_equal': 0}
        for r in rows:
            a, b, l, th = r['a'], r['b'], r['l'], r['theta']
            w = word_of(a, b, l, th, p)
            wkeys.add(key_of(w, p))
            struct['all_l_odd'] += all(x % 2 for x in l)
            struct['all_r_odd'] += all((x + y) % 2 for x, y in zip(a, b))
            struct['rot_runs_constant'] += all(x == 0 or y == 0 for x, y in zip(a, b))
            struct['brackets_equal'] += len({(th[i] - (a[i] - b[i])) % p for i in range(len(a))}) == 1
        print(json.dumps({'dump_words': ndump, 'dump_nonRGR': nonrgr, 'dump_keys': len(dkeys),
                          'was_all_rows': len(rows), 'was_keys': len(wkeys),
                          'keys_equal': dkeys == wkeys, 'dump_minus_was': len(dkeys - wkeys),
                          'was_minus_dump': len(wkeys - dkeys), 'structure_counts': struct}))

if __name__ == '__main__':
    main()
