#!/opt/homebrew/bin/python3
"""Exhaustive odd-half search for one rank-four profile (D,m,S) with small D.

Model (frontier-20261029-rank4-m112-and-profiles-v1.md, section C): after the symmetries
lambda=mu=0 and theta=1, sigma=(-1)^{Q4} on the odd Walsh support Y=block 0, and
    v' = sigma*psi on Y,      v'(c,.) = -lift(Walsh_delta(c,.) mod 3) on blocks c!=0,
where psi=sigma*v' on Y has p entries +1 and z0 entries 0 with S=p-(16-p-z0), and delta has D
signed atoms (r_a,s_a) whose per-fibre signed sums satisfy sum_{a in s} eps_a = F(s) (mod 3),
F = Walsh(sigma*(1-psi)) mod 3.  Atom positions are taken modulo the affine maps
r_a -> r_a + M s_a + w (shear and odd relabelling); up to GL(4) on blocks the position map is a
subspace L of the quotient F_2^D / A of dimension <= 4.  Atoms of one fibre must have distinct
positions.  For every (psi, atom distribution, L) the script builds the full 256-point v', checks
sum_{c!=0} n_c = m - z0 (n_c = zeros of the block-c mod-3 values) and the maximum |Walsh(v')|
by a fast Walsh transform.  A profile is excluded by this model iff no candidate has max<=14.
"""
import argparse, collections, itertools, json, pathlib, time
import numpy as np


def chi(a, b):
    return 1 - 2 * (bin(a & b).count('1') & 1)


def Q4(s):
    s1, s2, s3, s4 = s & 1, (s >> 1) & 1, (s >> 2) & 1, (s >> 3) & 1
    return (s1 * s2 + s3 * s4 + s3 + s4) % 2


SIG = [1 - 2 * Q4(z) for z in range(16)]
CH = np.array([[chi(s, z) for z in range(16)] for s in range(16)], dtype=np.int64)


def fwht(V):
    V = V.copy(); h = 1
    while h < 256:
        V = V.reshape(V.shape[0], -1, 2 * h)
        a = V[:, :, :h].copy(); b = V[:, :, h:].copy()
        V[:, :, :h] = a + b; V[:, :, h:] = a - b
        V = V.reshape(V.shape[0], 256); h *= 2
    return V


def rank_basis(vecs):
    piv = {}
    for v in vecs:
        while v:
            h = v.bit_length() - 1
            if h in piv:
                v ^= piv[h]
            else:
                piv[h] = v; break
    return piv


def subspaces(basis, maxdim=4):
    k = len(basis); out = []
    def vec(cv):
        v = 0
        for i in range(k):
            if (cv >> i) & 1:
                v ^= basis[i]
        return v
    for d in range(0, min(maxdim, k) + 1):
        for piv in itertools.combinations(range(k), d):
            frees = [[x for x in range(piv[i] + 1, k) if x not in piv] for i in range(d)]
            tot = sum(len(f) for f in frees)
            for mask in range(1 << tot):
                gens = []; b = 0
                for i in range(d):
                    cv = 1 << piv[i]
                    for x in frees[i]:
                        if (mask >> b) & 1:
                            cv |= 1 << x
                        b += 1
                    gens.append(vec(cv))
                out.append(gens)
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--D', type=int, required=True); p.add_argument('--m', type=int, required=True)
    p.add_argument('--S', type=int, required=True); p.add_argument('--output', type=pathlib.Path, required=True)
    a = p.parse_args()
    if a.output.exists():
        raise FileExistsError(a.output)
    D, m, S = a.D, a.m, a.S; t0 = time.time(); stats = collections.Counter(); hist = collections.Counter(); best = []
    for pp in range(17):
        for z0 in range(17 - pp):
            if pp - (16 - pp - z0) != S:
                continue
            for P1 in itertools.combinations(range(16), pp):
                rest = [z for z in range(16) if z not in P1]
                for P0 in itertools.combinations(rest, z0):
                    psi = [-1] * 16
                    for z in P1:
                        psi[z] = 1
                    for z in P0:
                        psi[z] = 0
                    f = [SIG[z] * (1 - psi[z]) for z in range(16)]
                    F = [sum(f[z] * chi(s, z) for z in range(16)) % 3 for s in range(16)]
                    if sum(1 for x in F if x) > D:
                        continue
                    stats['psi_configs'] += 1
                    opts = [[(n, npl) for n in range(D + 1) for npl in range(n + 1) if (npl - (n - npl) - F[s]) % 3 == 0] for s in range(16)]
                    dists = []
                    def rec(i, left, cur):
                        if i == 16:
                            if left == 0:
                                dists.append(list(cur))
                            return
                        for o in opts[i]:
                            if o[0] <= left:
                                cur.append(o); rec(i + 1, left - o[0], cur); cur.pop()
                    rec(0, D, [])
                    blk0 = [SIG[z] * psi[z] for z in range(16)]
                    for dist in dists:
                        atoms = []
                        for s, (n, npl) in enumerate(dist):
                            atoms += [(s, 1)] * npl + [(s, -1)] * (n - npl)
                        stats['distributions'] += 1
                        A = [sum((((bin(al & s).count('1') + be) & 1) << i) for i, (s, e) in enumerate(atoms)) for al in range(16) for be in (0, 1)]
                        piv = rank_basis(A)
                        def red(v):
                            for h in sorted(piv, reverse=True):
                                if (v >> h) & 1:
                                    v ^= piv[h]
                            return v
                        comp = sorted(rank_basis([red(1 << i) for i in range(D) if red(1 << i)]).values())
                        same = [(i, j) for i in range(D) for j in range(i + 1, D) if atoms[i][0] == atoms[j][0]]
                        batch = []
                        for gens in subspaces(comp, 4):
                            g = gens + [0] * (4 - len(gens))
                            if any(all(((gi >> i) & 1) == ((gi >> j) & 1) for gi in g) for (i, j) in same):
                                continue
                            stats['position_classes'] += 1
                            V = np.zeros(256, dtype=np.int64); nus = 0
                            for z in range(16):
                                V[16 * z] = blk0[z]
                            for c in range(1, 16):
                                l = 0
                                for i in range(4):
                                    if (c >> i) & 1:
                                        l ^= g[i]
                                Wz = np.zeros(16, dtype=np.int64)
                                for k_, (s, e) in enumerate(atoms):
                                    Wz += (-e if (l >> k_) & 1 else e) * CH[s]
                                r3 = Wz % 3; nus += int((r3 == 0).sum())
                                V[c + 16 * np.arange(16)] = np.where(r3 == 0, 0, np.where(r3 == 1, -1, 1))
                            if nus != m - z0:
                                continue
                            stats['nu_sum_ok'] += 1; batch.append(V)
                        if batch:
                            mx = np.abs(fwht(np.array(batch))).max(1)
                            for v in mx.tolist():
                                hist[v] += 1
                            stats['max_le_14'] += int((mx <= 14).sum())
    out = {'profile': {'D': D, 'm': m, 'S': S}, 'stats': dict(stats), 'max_abs_walsh_histogram': {str(k): v for k, v in sorted(hist.items())},
           'elapsed_seconds': time.time() - t0, 'scope': 'odd-half model exhaustion for one rank-four profile; not a Boolean witness'}
    with a.output.open('x', encoding='utf-8') as fh:
        json.dump(out, fh, indent=2, sort_keys=True); fh.write('\n')
    print(json.dumps(out['stats']), 'max_le_14=', stats['max_le_14'])


if __name__ == '__main__':
    main()
