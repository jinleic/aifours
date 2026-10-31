#!/opt/homebrew/bin/python3
"""Finite facts for frontier-20261029-rank4-m112-and-profiles-v1.md (no solver verdict is used).

(1) Quadric-row geometry: among all y=Walsh(w)/4 (w ternary on F_2^4, all values divisible by 4,
    |y| in {0,1,2,4}), the +-1 support is an affine 2-flat whenever it has 4 points, and an affine
    3-flat whenever the shape is (8 ones, 2 twos).
(2) Row-count feasibility of every E=0 configuration (beta,N6,N8): over all type-10 coverings,
    type-12 triple choices and type-8 pairs, count those whose six quadric rows all have an allowed
    shape (#|y|=1,#|y|=2,#|y|=4).
(3) The block-Y bound: for sigma=(-1)^{Q4} and every exceptional set with p points psi=+1 and z0
    points psi=0 (psi=sigma*v'), the number N of s with Walsh(sigma(1-psi))(s) not 0 mod 3.
"""
import argparse, collections, itertools, json, pathlib
import numpy as np


def chi(a, b):
    return 1 - 2 * (bin(a & b).count('1') & 1)


def Q4(s):
    s1, s2, s3, s4 = s & 1, (s >> 1) & 1, (s >> 2) & 1, (s >> 3) & 1
    return (s1 * s2 + s3 * s4 + s3 + s4) % 2


def aff_span(pts):
    if not pts:
        return set()
    o = pts[0]; piv = {}
    for q in pts[1:]:
        v = q ^ o
        while v:
            h = v.bit_length() - 1
            if h in piv:
                v ^= piv[h]
            else:
                piv[h] = v; break
    span = {0}
    for b in piv.values():
        span |= {x ^ b for x in span}
    return {o ^ x for x in span}


def main():
    p = argparse.ArgumentParser(); p.add_argument('--output', type=pathlib.Path, required=True); a = p.parse_args()
    if a.output.exists():
        raise FileExistsError(a.output)
    Z0 = [s for s in range(16) if Q4(s) == 0]
    H = np.array([[chi(s, z) for z in range(16)] for s in range(16)], dtype=np.int16)
    lo = ((np.arange(3 ** 12)[:, None] // (3 ** np.arange(12))) % 3).astype(np.int16) - 1
    rows = set()
    for hi in range(3 ** 4):
        top = np.array([(hi // 3 ** i) % 3 - 1 for i in range(4)], dtype=np.int16)
        W = np.concatenate([lo, np.broadcast_to(top, (lo.shape[0], 4))], axis=1) @ H.T
        Y = W[(W % 4 == 0).all(1)] // 4
        ab = np.abs(Y)
        rows.update(map(tuple, Y[((ab == 0) | (ab == 1) | (ab == 2) | (ab == 4)).all(1)].tolist()))
    geo = collections.Counter(); allowed = set()
    for r in rows:
        ones = [c for c in range(16) if abs(r[c]) == 1]; twos = [c for c in range(16) if abs(r[c]) == 2]
        fours = [c for c in range(16) if abs(r[c]) == 4]
        allowed.add((len(ones), len(twos), len(fours)))
        span = aff_span(ones); flat = len(span) == len(ones)
        geo[(len(ones), len(twos), len(fours), flat)] += 1
    assert all(flat for (o, t, f, flat) in geo if o == 4)
    assert all(flat for (o, t, f, flat) in geo if (o, t) == (8, 2))
    assert all(t == 0 and o == 0 for (o, t, f, flat) in geo if f > 0) and all(f <= 1 for (o, t, f, flat) in geo)
    # (2) configurations
    words = set()
    for coef in itertools.product(range(3), repeat=6):
        words.add(tuple(sum(cf * chi(s, z) for cf, s in zip(coef, Z0)) % 3 for z in range(16)))
    lift = lambda w: [0 if t == 0 else (1 if t == 1 else -1) for t in w]
    V5 = [1, 2, 7, 11, 15]; EDGES = [(i, j) for i in range(5) for j in range(i + 1, 5)]; NZOF = [V5[i] ^ V5[j] for i, j in EDGES]
    pair10 = collections.Counter(); tri12 = collections.defaultdict(set)
    for w in words:
        x = lift(w); U = [sum(x[z] * chi(s, z) for z in range(16)) for s in range(16)]; n = sum(map(abs, x))
        if n == 10:
            pair10[(frozenset(k for k in range(10) if U[NZOF[k]]), frozenset(t for t in Z0 if U[t] == 0))] += 1
        if n == 12:
            A = frozenset(t for t in Z0 if U[t]); s = 0
            for t in A:
                s ^= t
            tri12[NZOF.index(s)].add(A)
    esets = {es: pr for (es, pr) in pair10}
    esl = sorted(esets, key=lambda e: sorted(e))
    feas = {}
    for cfg in [(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0), (4, 0, 0), (1, 1, 0), (0, 0, 1), (2, 1, 0), (1, 0, 1), (5, 0, 0),
                (6, 0, 0), (3, 1, 0), (0, 2, 0), (2, 0, 1)]:
        beta, N6, N8 = cfg; alpha = 10 - beta; tot = ok = 0
        for E12 in itertools.combinations(range(10), beta):
            E12s = set(E12); avail = [e for e in esl if not (e & E12s)]; covs = []
            def rec(i, left, cov, ch):
                if left == 0:
                    if all(cov[k] == (0 if k in E12s else 4) for k in range(10)):
                        covs.append(tuple(ch))
                    return
                if i == len(avail):
                    return
                es = avail[i]; mx = min([left] + [4 - cov[k] for k in es])
                for mult in range(mx, -1, -1):
                    for k in es:
                        cov[k] += mult
                    rec(i + 1, left - mult, cov, ch + [es] * mult)
                    for k in es:
                        cov[k] -= mult
            rec(0, alpha, [0] * 10, [])
            for ch in covs:
                for tris in itertools.product(*[sorted(tri12[e], key=sorted) for e in E12]):
                    for prs in (itertools.combinations(itertools.combinations(Z0, 2), N8) if N8 else [()]):
                        tot += 1; good = True
                        for t in Z0:
                            o = sum(1 for es in ch if t not in esets[es])
                            two = sum(1 for A in tris if t in A) + N6
                            four = sum(1 for P in prs if t in P)
                            if (o, two, four) not in allowed:
                                good = False; break
                        ok += good
        feas[str(cfg)] = {'cases': tot, 'row_shape_feasible': ok}
    # (3) block-Y bound
    sig = [1 - 2 * Q4(z) for z in range(16)]
    ybound = {}
    for (pp, z0) in [(0, 0), (0, 3), (1, 1), (0, 6), (1, 4), (2, 2), (3, 0)]:
        cnt = collections.Counter()
        for P in itertools.combinations(range(16), pp):
            rest = [z for z in range(16) if z not in P]
            for Zp in itertools.combinations(rest, z0):
                f = [0 if z in P else (sig[z] if z in Zp else -sig[z]) for z in range(16)]
                # f = sigma*(1-psi) mod 3 written with psi=-1 -> -sigma(=2sigma), psi=0 -> sigma, psi=1 -> 0
                N = sum(1 for s in range(16) if sum(f[z] * chi(s, z) for z in range(16)) % 3)
                cnt[N] += 1
        ybound[f'p={pp},z0={z0}'] = {'min_N': min(cnt), 'distribution': {str(k): v for k, v in sorted(cnt.items())}}
    out = {'row_geometry': [{'ones': o, 'twos': t, 'fours': f, 'ones_flat': fl, 'count': c} for (o, t, f, fl), c in sorted(geo.items())],
           'config_row_feasibility': feas, 'block_Y_bound': ybound,
           'scope': 'finite lemma inputs; no witness, no solver verdict'}
    with a.output.open('x', encoding='utf-8') as fh:
        json.dump(out, fh, indent=2, sort_keys=True); fh.write('\n')
    print(json.dumps(feas)); print({k: v['min_N'] for k, v in ybound.items()})


if __name__ == '__main__':
    main()
