#!/opt/homebrew/bin/python3
"""Finite facts behind frontier-20261029-rank4-E0-structure-v1.md.

Recomputes, without solver use:
  (1) the 729-word ternary code C0 spanned mod 3 by the six characters chi_s,
      s in the elliptic zero set Z0, and the |U| profile of each lifted word;
  (2) the NZ-row dichotomy: integer 16-vectors with entries in {0,+-6,+-12}
      whose 16-point Walsh transform is identically +-12;
  (3) all 'Z0 rows' y=Walsh(w)/4 with w ternary on F_2^4, Walsh(w)=0 mod 4,
      entries of y in {0,+-1,+-2,+-4}, classified by (#|y|=1,#|y|=2,#|y|=4);
  (4) the multisets of type-10 edge sets covering the complement of E12
      exactly four times, by beta=|E12|.
Nothing here is a Boolean witness or an exclusion by itself.
"""
import argparse, collections, itertools, json, pathlib


def chi(a, b):
    return 1 - 2 * (bin(a & b).count('1') & 1)


def Q4(s):
    s1, s2, s3, s4 = s & 1, (s >> 1) & 1, (s >> 2) & 1, (s >> 3) & 1
    return (s1 * s2 + s3 * s4 + s3 + s4) % 2


def walsh16(x):
    return [sum(x[z] * chi(s, z) for z in range(16)) for s in range(16)]


def main():
    p = argparse.ArgumentParser(); p.add_argument('--output', type=pathlib.Path, required=True); a = p.parse_args()
    if a.output.exists():
        raise FileExistsError(a.output)
    Z0 = [s for s in range(16) if Q4(s) == 0]
    NZ = [s for s in range(16) if Q4(s) == 1]
    assert Z0 == [0, 1, 2, 7, 11, 15]
    # (1) the code C0
    words = set()
    for coef in itertools.product(range(3), repeat=6):
        w = tuple(sum(cf * chi(s, z) for cf, s in zip(coef, Z0)) % 3 for z in range(16))
        words.add(w)
    assert len(words) == 729
    lift = lambda w: [0 if t == 0 else (1 if t == 1 else -1) for t in w]
    types = collections.Counter(); c0 = []
    for w in words:
        x = lift(w); U = walsh16(x); n = sum(abs(t) for t in x)
        key = (n, tuple(sorted(abs(U[s]) for s in Z0)), tuple(sorted(abs(U[s]) for s in NZ)))
        types[key] += 1; c0.append((x, U, n))
        assert all(U[s] % 3 == 0 for s in NZ)
    # every word with all NZ transform values 0 mod 3 is in C0: check the converse on the lifted space by counting
    # (16 ≡ 1 mod 3 makes x ≡ sum_s U_s chi_s; NZ residues vanish iff x mod 3 lies in span(chi_s, s in Z0)).
    # (2) NZ rows
    nzrows = 0; flats = set()
    for base in range(16):
        for u in range(1, 16):
            for v in range(1, 16):
                F = frozenset([base, base ^ u, base ^ v, base ^ u ^ v])
                if len(F) == 4:
                    flats.add(F)
    assert len(flats) == 140
    good = 0
    for c0_ in range(16):
        for g in (12, -12):
            y = [0] * 16; y[c0_] = g
            assert all(abs(w) == 12 for w in walsh16(y)); good += 1
    prod_ok = collections.Counter()
    for F in flats:
        F = sorted(F)
        for sg in itertools.product((1, -1), repeat=4):
            y = [0] * 16
            for c, e in zip(F, sg):
                y[c] = 6 * e
            ok = all(abs(w) == 12 for w in walsh16(y))
            prod_ok[(sg[0] * sg[1] * sg[2] * sg[3], ok)] += 1
    assert prod_ok[(-1, True)] == 140 * 8 and prod_ok[(1, True)] == 0
    # four +-6 entries not on a 2-flat never give a flat +-12 spectrum
    nonflat_bad = 0
    for S in itertools.combinations(range(16), 4):
        if frozenset(S) in flats:
            continue
        for sg in itertools.product((1, -1), repeat=3):
            y = [0] * 16
            for c, e in zip(S, (1,) + sg):
                y[c] = 6 * e
            if all(abs(w) == 12 for w in walsh16(y)):
                nonflat_bad += 1
    assert nonflat_bad == 0
    # (3) Z0 rows, by butterfly Walsh transforms over all 3^16 ternary w (numpy, chunked)
    import numpy as np
    shapes = collections.Counter()
    lo = ((np.arange(3 ** 12)[:, None] // (3 ** np.arange(12))) % 3).astype(np.int16) - 1
    for hi in range(3 ** 4):
        top = np.array([(hi // 3 ** i) % 3 - 1 for i in range(4)], dtype=np.int16)
        W = np.concatenate([lo, np.broadcast_to(top, (lo.shape[0], 4))], axis=1).copy()
        h = 1
        while h < 16:
            for i in range(0, 16, 2 * h):
                for j in range(i, i + h):
                    x, y_ = W[:, j].copy(), W[:, j + h].copy()
                    W[:, j], W[:, j + h] = x + y_, x - y_
            h *= 2
        keep = (W % 4 == 0).all(1)
        Y = np.abs(W[keep] // 4)
        keep2 = ((Y == 0) | (Y == 1) | (Y == 2) | (Y == 4)).all(1)
        Y = Y[keep2]
        for key, cnt in zip(*np.unique(np.stack([(Y == 1).sum(1), (Y == 2).sum(1), (Y == 4).sum(1)], 1), axis=0, return_counts=True)):
            shapes[tuple(int(t) for t in key)] += int(cnt)
    # (4) coverings
    V5 = [1, 2, 7, 11, 15]
    edges = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    nz_of = [V5[i] ^ V5[j] for (i, j) in edges]
    assert sorted(nz_of) == NZ
    esets = collections.Counter()
    for x, U, n in c0:
        if n == 10:
            esets[frozenset(k for k in range(10) if U[nz_of[k]] != 0)] += 1
    assert len(esets) == 15 and set(esets.values()) == {16}
    esl = sorted(esets, key=lambda e: sorted(e))
    cover = collections.Counter()
    for beta in range(11):
        alpha = 10 - beta
        for E12 in itertools.combinations(range(10), beta):
            E12s = set(E12); avail = [e for e in esl if not (e & E12s)]
            def rec(i, left, cov):
                if left == 0:
                    if all(cov[k] == (0 if k in E12s else 4) for k in range(10)):
                        cover[beta] += 1
                    return
                if i == len(avail):
                    return
                es = avail[i]; mx = min([left] + [4 - cov[k] for k in es])
                for mult in range(mx, -1, -1):
                    for k in es:
                        cov[k] += mult
                    rec(i + 1, left - mult, cov)
                    for k in es:
                        cov[k] -= mult
            rec(0, alpha, [0] * 10)
    out = {'Z0': Z0, 'NZ': NZ,
           'C0_types': [{'n': k[0], 'abs_U_Z0': list(k[1]), 'abs_U_NZ': list(k[2]), 'count': v} for k, v in sorted(types.items())],
           'affine_2flats': len(flats), 'nz_rows': {'single_12': good, 'flat_6_product_minus1': 140 * 8, 'product_plus1_flat': 0, 'nonflat_supports': 0},
           'z0_row_shapes': [{'ones': k[0], 'twos': k[1], 'fours': k[2], 'count': v} for k, v in sorted(shapes.items())],
           'type10_edge_sets': [sorted(e) for e in esl], 'coverings_by_beta': {str(b): cover[b] for b in sorted(cover)},
           'scope': 'finite lemma inputs for the E=0 rank-four even half; no witness or exclusion'}
    with a.output.open('x', encoding='utf-8') as fh:
        json.dump(out, fh, indent=2, sort_keys=True); fh.write('\n')
    print('C0 types', len(types), 'coverings', dict(cover), 'z0 shapes', len(shapes))


if __name__ == '__main__':
    main()
