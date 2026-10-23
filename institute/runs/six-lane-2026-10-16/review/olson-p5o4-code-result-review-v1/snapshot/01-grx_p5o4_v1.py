#!/usr/bin/env python3
"""Stage G of PLAN-v1.md (p = 5, o_F = 4): exhaustive GRX classification of the domain D.

Domain D: cyclic representations R_1 S_1 R_2 S_2 R_3 S_3 R_4 S_4 of length 18 over D_10, S_i = sigma_(y_i)^(l_i) with
l_i odd, y_i in Z_5, R_i any multiset of rotation values in Z_5 (empty allowed).  A GRX class is (H, dist, y):
H = sum (l_i - 1)/2 in 0..4, dist = the 4 run multisets (counts n[i][x]), y in Z_5^4.  By GRX (accepted,
notes-GRX-v1.md) the verdict depends only on the class.  Written independently of every earlier lane code.
Usage: grx_p5o4_v1.py OUTDIR   (writes OUTDIR/grx_summary.json, grx_avoiders.txt, grx_survivors.txt, grx_mutations.txt)
"""
import sys, os, json, hashlib, itertools
from math import comb
import numpy as np

P, K, NLEN, TP = 5, 4, 18, 10
FULL5 = (1 << P) - 1
ZS = list(itertools.product((1, -1), repeat=K))          # 16 sign patterns, fixed order


def rotmask(m, s):
    s %= P
    return ((m << s) | (m >> (P - s))) & FULL5 if s else m


def multisets(R):
    out = []
    def rec(i, rem, cur):
        if i == P - 1:
            out.append(tuple(cur + [rem])); return
        for c in range(rem, -1, -1):
            rec(i + 1, rem - c, cur + [c])
    rec(0, R, [])
    return out


def compositions(n, parts):
    if parts == 1:
        return [(n,)]
    res = []
    for a in range(n, -1, -1):
        for rest in compositions(n - a, parts - 1):
            res.append((a,) + rest)
    return res


def sizesum(cnt, maxm):
    """cnt[v] copies of value v; S[m] = 5-bit mask of sums (mod 5) of size-m sub-multisets, m <= maxm."""
    S = [0] * (maxm + 1); S[0] = 1
    for v in range(P):
        c = cnt[v]
        if c == 0:
            continue
        N = [0] * (maxm + 1)
        for m in range(maxm + 1):
            if not S[m]:
                continue
            for t in range(c + 1):
                if m + t > maxm:
                    break
                N[m + t] |= rotmask(S[m], t * v)
        S = N
    return S


def pattern_data(z, H, ls_parity_odd=True, cmax_mode='true'):
    """Phi and the allowed rotation counts m for pattern z when all 4 blocks are odd and sum (l_i-1)/2 = H."""
    f = [1 if z[i] != z[(i + 1) % K] else 0 for i in range(K)]
    Phi = sum(f)
    F = 2 * H + K
    delta = sum(1 for i in range(K) if f[i] == 0)        # l_i odd: l_i != f_i mod 2 iff f_i = 0
    Cmax = F - delta if cmax_mode == 'true' else F
    R = NLEN - F
    ms = [TP - C for C in range(Phi, Cmax + 1) if C % 2 == 0 and 0 <= TP - C <= R]
    return Phi, ms


def theta_T_table():
    """T[yidx, zidx] = sum over i with z_i = +1 of theta_i, theta_i = y_(i-1) - y_i (y_(-1) = y_(K-1)), mod 5."""
    ys = list(itertools.product(range(P), repeat=K))
    T = np.zeros((len(ys), len(ZS)), dtype=np.int64)
    for a, y in enumerate(ys):
        th = [(y[i - 1] - y[i]) % P for i in range(K)]
        for b, z in enumerate(ZS):
            T[a, b] = sum(th[i] for i in range(K) if z[i] == 1) % P
    return ys, T


def masks_for_dist(dist, H, cmax_mode='true', zsel=None):
    """A[zidx] = 5-bit mask of effective sums achievable with an allowed count, for the class rotation data."""
    R = NLEN - (2 * H + K)
    A = np.zeros(len(ZS), dtype=np.int64)
    for b, z in enumerate(ZS):
        if zsel is not None and b not in zsel:
            continue
        cnt = [0] * P
        for i in range(K):
            for x in range(P):
                cnt[(z[i] * x) % P] += dist[i][x]
        S = sizesum(cnt, R)
        Phi, ms = pattern_data(z, H, cmax_mode=cmax_mode)
        mk = 0
        for m in ms:
            mk |= S[m]
        A[b] = mk
    return A


def rigid(counts):
    supp = [x for x in range(P) if counts[x] > 0]
    if not supp:
        return True
    if 0 in supp:
        return False
    if len(supp) == 1:
        return True
    return len(supp) == 2 and (supp[0] + supp[1]) % P == 0


def dist_str(dist):
    return '/'.join(','.join(str(dist[i][x]) for x in range(P)) for i in range(K))


def grx_general(runs, ys, ls):
    """Literal GRX (notes-GRX-v1.md Sec. 1) for any k and block lengths; True iff an identity 2p-subword exists."""
    k = len(ys); F = sum(ls); R = sum(len(r) for r in runs)
    theta = [(ys[i - 1] - ys[i]) % P for i in range(k)]
    for z in itertools.product((1, -1), repeat=k):
        f = [1 if z[i] != z[(i + 1) % k] else 0 for i in range(k)]
        Phi = sum(f)
        delta = sum(1 for i in range(k) if ls[i] % 2 != f[i])
        Cmax = F - delta
        T = sum(theta[i] for i in range(k) if z[i] == 1) % P
        cnt = [0] * P
        for i in range(k):
            for x in runs[i]:
                cnt[(z[i] * x) % P] += 1
        S = sizesum(cnt, R)
        for C in range(Phi, Cmax + 1):
            if C % 2:
                continue
            m = TP - C
            if 0 <= m <= R and (S[m] >> T) & 1:
                return True
    return False


def main():
    outdir = sys.argv[1]
    ys, T = theta_T_table()
    yidx = {y: a for a, y in enumerate(ys)}
    summary = {'p': P, 'k': K, 'N': NLEN, 'per_H': {}, 'controls': {}}
    avoider_lines, survivor_lines = [], []
    avoider_classes = []
    tc1_nonrigid = 0; tc1_total = 0; tc2_total = 0; tc2_flipped = 0
    plusminus = [ZS.index((1, 1, 1, 1)), ZS.index((-1, -1, -1, -1))]
    for H in range(0, 5):
        R = NLEN - (2 * H + K)
        ms_all = multisets(R)
        n_classes_formula = comb(R + 19, 19) * P ** K
        allplus_solved_classes = 0; enumerated_classes = 0; n_surv = 0
        n_avoid = 0; n_avoid_nonrigid = 0
        for c in ms_all:
            S = sizesum(list(c), R)
            Phi0, ms0 = pattern_data((1, 1, 1, 1), H)
            ndist = 1
            for x in range(P):
                ndist *= comb(c[x] + 3, 3)
            if any((S[m] >> 0) & 1 for m in ms0):
                allplus_solved_classes += ndist * P ** K
                continue
            n_surv += 1
            survivor_lines.append('H=%d|Y=%s|rigid=%d|ndist=%d' % (H, ','.join(map(str, c)), rigid(c), ndist))
            per_value = [compositions(c[x], K) for x in range(P)]
            cnt_d = 0
            for choice in itertools.product(*per_value):
                dist = [[choice[x][i] for x in range(P)] for i in range(K)]
                cnt_d += 1
                A = masks_for_dist(dist, H)
                bits = (A[None, :] >> T) & 1
                solv = bits.any(axis=1)
                enumerated_classes += len(ys)
                for a in np.nonzero(~solv)[0]:
                    y = ys[a]
                    n_avoid += 1
                    if not rigid(c):
                        n_avoid_nonrigid += 1
                    line = 'H=%d|dist=%s|y=%s' % (H, dist_str(dist), ''.join(map(str, y)))
                    avoider_lines.append(line)
                    avoider_classes.append((H, [row[:] for row in dist], y))
                # TC1: only the all-plus and all-minus patterns
                A1 = masks_for_dist(dist, H, zsel=set(plusminus))
                b1 = ((A1[None, plusminus] >> T[:, plusminus]) & 1).any(axis=1)
                k1 = int((~b1).sum()); tc1_total += k1
                if not rigid(c):
                    tc1_nonrigid += k1
                # TC2: C_max := F (delta ignored)
                A2 = masks_for_dist(dist, H, cmax_mode='F')
                b2 = ((A2[None, :] >> T) & 1).any(axis=1)
                tc2_total += int((~b2).sum())
                tc2_flipped += int(((~solv) & b2).sum())
            assert cnt_d == ndist
        assert allplus_solved_classes + enumerated_classes == n_classes_formula
        summary['per_H'][str(H)] = dict(R=R, multisets=len(ms_all), survivor_multisets=n_surv,
                                        classes_formula=n_classes_formula,
                                        classes_allplus_solved=allplus_solved_classes,
                                        classes_enumerated=enumerated_classes,
                                        avoider_classes=n_avoid, nonrigid_avoider_classes=n_avoid_nonrigid)
    # translation invariance of the avoider set (y -> y + b)
    aset = set(avoider_lines)
    trans_ok = True
    for (H, dist, y) in avoider_classes:
        for bsh in range(P):
            y2 = tuple((yy + bsh) % P for yy in y)
            if 'H=%d|dist=%s|y=%s' % (H, dist_str(dist), ''.join(map(str, y2))) not in aset:
                trans_ok = False
    # positive control: Claude's accepted k = 2 example rho_1^9 sigma_0^7 rho_-1 sigma_0 (p = 5)
    pc_k2 = grx_general([[1] * 9, [4]], [0, 0], [7, 1])
    # type census of avoiders
    types = {}
    for (H, dist, y) in avoider_classes:
        tot = [sum(dist[i][x] for i in range(K)) for x in range(P)]
        key = 'H=%d|Y=%s' % (H, ','.join(map(str, tot)))
        types[key] = types.get(key, 0) + 1
    # TC5 mutation agreement list: first 3000 avoider classes in canonical order, canonical block lengths (2H+1,1,1,1)
    mut_lines = []
    canon = sorted(avoider_classes, key=lambda t: 'H=%d|dist=%s|y=%s' % (t[0], dist_str(t[1]), ''.join(map(str, t[2]))))
    for (H, dist, y) in canon[:3000]:
        ls = [2 * H + 1, 1, 1, 1]
        base = 'H=%d|dist=%s|y=%s' % (H, dist_str(dist), ''.join(map(str, y)))
        for i in range(K):
            for x in range(P):
                if dist[i][x] == 0:
                    continue
                for x2 in range(P):
                    if x2 == x:
                        continue
                    d2 = [row[:] for row in dist]; d2[i][x] -= 1; d2[i][x2] += 1
                    runs = [[v for v in range(P) for _ in range(d2[j][v])] for j in range(K)]
                    mut_lines.append('%s|rot:%d:%d>%d|%d' % (base, i, x, x2, int(grx_general(runs, list(y), ls))))
        for i in range(K):
            for y2 in range(P):
                if y2 == y[i]:
                    continue
                yy = list(y); yy[i] = y2
                runs = [[v for v in range(P) for _ in range(dist[j][v])] for j in range(K)]
                mut_lines.append('%s|blk:%d>%d|%d' % (base, i, y2, int(grx_general(runs, yy, ls))))
    def wr(name, lines):
        txt = ''.join(l + '\n' for l in sorted(lines))
        with open(os.path.join(outdir, name), 'x') as f:
            f.write(txt)
        return hashlib.sha256(txt.encode()).hexdigest(), len(lines)
    summary['files'] = {}
    for name, lines in (('grx_avoiders.txt', avoider_lines), ('grx_survivors.txt', survivor_lines),
                        ('grx_mutations.txt', mut_lines)):
        h, n = wr(name, lines)
        summary['files'][name] = dict(sha256=h, lines=n)
    summary['controls'] = dict(translation_invariant=trans_ok, positive_k2_example_avoider=(not pc_k2),
                               TC1_plusminus_only_avoiders=tc1_total, TC1_nonrigid=tc1_nonrigid,
                               TC2_cmax_F_avoiders=tc2_total, TC2_true_avoiders_flipped=tc2_flipped,
                               mutation_lines=len(mut_lines),
                               mutation_solvable=sum(1 for l in mut_lines if l.endswith('|1')))
    summary['avoider_types'] = types
    summary['total_nonrigid_avoider_classes'] = sum(v['nonrigid_avoider_classes'] for v in summary['per_H'].values())
    with open(os.path.join(outdir, 'grx_summary.json'), 'x') as f:
        json.dump(summary, f, indent=1, sort_keys=True)
    print(json.dumps(summary['controls']), summary['total_nonrigid_avoider_classes'])


if __name__ == '__main__':
    main()
