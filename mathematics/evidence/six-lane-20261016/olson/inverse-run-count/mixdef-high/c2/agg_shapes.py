# agg_shapes.py -- aggregate Lemma BC chain shapes printed by bcgstats (c2/README.md Sec. 8). Aid only.
import json, sys, collections
def blocks(mask, k):
    s = [(mask >> t) & 1 for t in range(k)]
    if all(s) or not any(s): return 0
    return sum(1 for t in range(k) if s[t] and not s[t - 1])
def which(P, k, p, kB, B, D_P, m):
    a = p - m + 1; b = D_P + m - kB; c = (D_P + B) // 2 + 1
    v = min(a, b, c)
    return v, ('cap' if v == a else '') + ('mid' if v == b else '') + ('flo' if v == c else '')
for fn in sys.argv[1:]:
    C = collections.Counter(); S = collections.Counter(); F = collections.Counter(); U = collections.Counter()
    E = collections.Counter(); T = collections.Counter(); n = 0; nb = 0
    exs = []
    for line in open(fn):
        if not line.startswith('{"chain"'): continue
        o = json.loads(line); n += 1
        k, p, kB, B = o['k'], o['p'], o['kB'], o['B']; parts = o['parts']; s = len(parts)
        tag = 'bc3' if o['bc3'] else 'bcg'
        S[(tag, s)] += 1
        if o['bc3']: continue
        nb += 1
        last = parts[-1]; full = (1 << k) - 1
        F[('last_m', last['m'])] += 1
        F[('last_size_minus_k/2', last['size'] - k // 2)] += 1
        early = full ^ last['mask']
        U[('union_early_m', blocks(early, k))] += 1
        for i, P in enumerate(parts[:-1]):
            v, w = which(P['mask'], k, p, kB, B, P['D'], P['m'])
            assert v == P['lam'], (v, P)
            E[('early_m_minus_kB', P['m'] - kB)] += 1
            E[('early_size_minus_m', P['size'] - P['m'])] += 1
            E[('early_binding', w)] += 1
            E[('early_lam_minus_D', P['lam'] - P['D'])] += 1
            E[('early_anti', P['anti'])] += 1
        v, w = which(last['mask'], k, p, kB, B, last['D'], last['m'])
        T[('last_binding', w)] += 1
        T[('last_anti', last['anti'])] += 1
        T[('kB', kB)] += 1; T[('B', B)] += 1; T[('k-p', k - p)] += 1; T[('R-2p', o['R'] - 2 * p)] += 1
        if len(exs) < 6 and s >= 5: exs.append(o)
    print('==', fn, 'chains', n, 'BCG-only', nb)
    for c in (S, F, U, E, T):
        for key in sorted(c): print('  ', key, c[key])
    for o in exs:
        k = o['k']
        print('  EX p=%d k=%d R=%d B=%d kB=%d d=%s' % (o['p'], k, o['R'], o['B'], o['kB'], o['d']))
        for P in o['parts']:
            print('     ', ''.join('1' if (P['mask'] >> t) & 1 else '.' for t in range(k)), 'm=%d D=%d lam=%d lamc=%d' % (P['m'], P['D'], P['lam'], P['lamc']))
