#!/usr/bin/env python3
"""OB1 controls: Lemma GRX (grx.py) versus the fresh raw DP (rawdp.py) and the unchanged read-only
olson/code/was_verify.py dp_has.  Writes one JSON summary line to stdout.

Families (all with a fixed seed):
  P5dump : all 3,730 normalised D10 avoiders of length 18 (olson/evidence/groups, table convention
           'a then b' converted by reversal, element g -> (g[0], g[1]-g[0])), expected NO.
  P7was  : every 'all' row of olson/evidence/was/p7_N26_all.jsonl (RGR avoiders, N = 26), expected NO.
  POSfam : rho_1^(2p-1) sigma_0^(2p-1) (N = 4p-2) and sigma_(v-2) rho_1^(2p-3) sigma_v^(2p-1) (N = 4p-3),
           p in {5,7,11,13}, v in {0,1,p-1}, expected NO.
  NEG    : each positive control above (sampled) mutated so that an explicit random index set of size 2p
           multiplies to the identity (last letter of the set replaced by the inverse of the prefix
           product); expected YES and the index set is re-multiplied directly.
  RAND   : random words (uniform letters; rigid-ish letters; deletions / one-letter substitutions of
           known avoiders), p in {5,7}, lengths 4p-3, 4p-2, 4p-1: GRX must equal raw DP.
"""
import json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OLSON = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
sys.path.insert(1, os.path.join(OLSON, 'code'))
import rawdp, grx  # noqa: E402
import was_verify  # noqa: E402  (read-only import; unchanged file)


def old_dp(word, p):
    return was_verify.dp_has([('R' if k == 'r' else 'F', v) for k, v in word], p)


def d10_dump():
    tab = json.load(open(os.path.join(OLSON, 'evidence/groups/D10.tab.json')))['elements']
    conv = []
    for g in tab:
        v, e = g[0] % 5, (g[1] - g[0]) % 5
        assert e in (1, 4)
        conv.append(('r' if e == 1 else 's', v))
    out = []
    for line in open(os.path.join(OLSON, 'evidence/groups/D10.L18.avoiders.txt')):
        if line.strip():
            out.append([conv[int(t)] for t in reversed(line.split())])
    return out


def word_of(a, b, l, theta, p):
    k = len(a)
    y, prev = [0] * k, 0
    for i in range(k):
        y[i] = (prev - theta[i]) % p
        prev = y[i]
    assert y[k - 1] == 0
    w = []
    for i in range(k):
        w += [('r', 1)] * a[i] + [('r', p - 1)] * b[i] + [('s', y[i])] * l[i]
    return w


def p7_was():
    out = []
    for line in open(os.path.join(OLSON, 'evidence/was/p7_N26_all.jsonl')):
        r = json.loads(line)
        if r.get('all'):
            out.append(word_of(r['a'], r['b'], r['l'], r['theta'], 7))
    return out


def pos_fam():
    out = []
    for p in (5, 7, 11, 13):
        out.append((p, [('r', 1)] * (2 * p - 1) + [('s', 0)] * (2 * p - 1)))
        for v in (0, 1, p - 1):
            out.append((p, [('s', (v - 2) % p)] + [('r', 1)] * (2 * p - 3) + [('s', v)] * (2 * p - 1)))
    return out


def rigid(word, p):
    vals = {v % p for k, v in word if k == 'r'}
    if not vals:
        return True
    if 0 in vals:
        return False
    x = next(iter(vals))
    return vals <= {x, (-x) % p}


def mutate_identity(word, p, rng):
    n = len(word)
    idx = sorted(rng.sample(range(n), 2 * p))
    v, e = rawdp.product(word, idx[:-1], p)
    w = list(word)
    w[idx[-1]] = ('r' if e == 1 else 's', (-e * v) % p)
    assert rawdp.product(w, idx, p) == (0, 1)
    return w, idx


def main():
    rng = random.Random(20261018)
    res = {'family': {}}
    bad = []

    def check(name, p, w, expect=None):
        a = rawdp.has_identity(w, p, 2 * p)
        b = grx.grx_has_identity(w, p)
        c = old_dp(w, p)
        fam = res['family'].setdefault(name, {'n': 0, 'yes': 0, 'no': 0, 'disagree': 0,
                                               'unexpected': 0, 'nonrigid_no': 0})
        fam['n'] += 1
        fam['yes' if a else 'no'] += 1
        if not (a == b == c):
            fam['disagree'] += 1
            bad.append((name, p, rawdp.fmt(w), a, b, c))
        if expect is not None and a != expect:
            fam['unexpected'] += 1
            bad.append((name, p, rawdp.fmt(w), 'expected', expect))
        if not a and not rigid(w, p) and len(w) == 4 * p - 2:
            fam['nonrigid_no'] += 1
            bad.append((name, p, rawdp.fmt(w), 'NONRIGID AVOIDER N=4p-2'))
        return a

    dump = d10_dump()
    for w in dump:
        check('P5dump', 5, w, expect=False)
    was = p7_was()
    for w in was:
        check('P7was', 7, w, expect=False)
    fam = pos_fam()
    for p, w in fam:
        check('POSfam', p, w, expect=False)
    # negative controls
    for w in rng.sample(dump, 300):
        m, idx = mutate_identity(w, 5, rng)
        check('NEG', 5, m, expect=True)
    for w in rng.sample(was, 300):
        m, idx = mutate_identity(w, 7, rng)
        check('NEG', 7, m, expect=True)
    for p, w in fam:
        if p <= 7:
            m, idx = mutate_identity(w, p, rng)
            check('NEG', p, m, expect=True)
    # random families
    for p in (5, 7):
        for N in (4 * p - 3, 4 * p - 2, 4 * p - 1):
            for _ in range(150):
                w = [(rng.choice('rs'), rng.randrange(p)) for _ in range(N)]
                check('RANDuni', p, w)
            for _ in range(150):
                ys = rng.sample(range(p), 2)
                w = [('r', rng.choice((1, p - 1))) if rng.random() < 0.5 else ('s', rng.choice(ys))
                     for _ in range(N)]
                if rng.random() < 0.5:
                    j = rng.randrange(N)
                    w[j] = ('r', rng.randrange(p))
                check('RANDrig', p, w)
        src = dump if p == 5 else was
        for _ in range(300):
            w = list(rng.choice(src))
            if rng.random() < 0.5:
                del w[rng.randrange(len(w))]          # deletion: still an avoider (4p-3)
                check('DEL', p, w, expect=False)
            else:
                j = rng.randrange(len(w))
                w[j] = (rng.choice('rs'), rng.randrange(p))
                check('SUB', p, w)
    res['bad'] = bad[:50]
    res['n_bad'] = len(bad)
    print(json.dumps(res, sort_keys=True))


if __name__ == '__main__':
    main()
