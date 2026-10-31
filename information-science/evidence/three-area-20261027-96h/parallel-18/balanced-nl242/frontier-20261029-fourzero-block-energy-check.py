#!/opt/homebrew/bin/python3
"""Exact checker for frontier-20261029-fourzero-block-energy-exclusion-v1.md.

Part A: the exact derivative identity D_r k(x) = |M^r| - 2 N^r(x) and its mod-8 form
        D_r k(x) = |M^r| - 2 x.tau^r - 4 Q^r(x) (mod 8), Q^r = second bit of N^r, deg Q^r <= 2,
        on seeded random balanced Boolean functions of nine variables (positive control).
Part B: from first principles (lambda-hat = (1,0)), all admissible even-fibre value vectors and
        odd-fibre value vectors, their block contributions U(c)^2, V(c)^2, the odd split classes,
        all split-direction distributions N for both nondegenerate six-dimensional normal forms,
        and a weighted block-energy capacity certificate for every (form, h, N).
Part C: controls: (i) the same weights do not certify when the odd mod-8 law is dropped;
        (ii) an explicit type-count assignment satisfying all four block-energy equations when the
        split-direction geometry is ignored, whose class distribution is not realizable.
"""
import argparse, collections, hashlib, itertools, json, pathlib, random


def par(x):
    return bin(x).count('1') & 1


def chi2(r, c):
    return 1 - 2 * par(r & c)


LAM = 1  # lambda-hat = (1,0); r and c are 2-bit integers, r.c = parity(r & c)


def part_a(seed=20261029, trials=12):
    rng = random.Random(seed); checks = 0; bad = 0; deg_bad = 0
    for _ in range(trials):
        pts = list(range(512)); rng.shuffle(pts); M = sorted(pts[:256])
        N = [sum(par(a & x) for x in M) for a in range(512)]
        k = [N[a] - 128 for a in range(512)]; k[0] = 0
        for _ in range(4):
            r = rng.randrange(1, 512)
            Mr = [x for x in M if par(r & x)]
            tau = 0
            for x in Mr:
                tau ^= x
            Q = []
            for a in range(512):
                Nr = sum(par(a & x) for x in Mr)
                if k[a ^ r] - k[a] != len(Mr) - 2 * Nr and a not in (0, r):
                    bad += 1
                q = (Nr >> 1) & 1; Q.append(q)
                if (k[a ^ r] - k[a]) % 8 != (len(Mr) - 2 * par(a & tau) - 4 * q) % 8:
                    bad += 1
                checks += 1
            anf = Q[:]
            for i in range(9):
                for a in range(512):
                    if (a >> i) & 1:
                        anf[a] ^= anf[a ^ (1 << i)]
            if any(anf[a] and bin(a).count('1') > 2 for a in range(512)):
                deg_bad += 1
    return {'checks': checks, 'failures': bad, 'degree_failures': deg_bad, 'seed': seed}


def even_types():
    Z, NZ = set(), set()
    for kv in itertools.product([4, -4], repeat=4):
        Z.add(tuple((sum(kv[r] * chi2(r, c) for r in range(4)) // 2) ** 2 for c in range(4)))
    for kv in itertools.product([2, -2, 6, -6], repeat=4):
        vt = [(kv[r] // 2) * (1 - 2 * par(LAM & r)) for r in range(4)]
        if len({x % 4 for x in vt}) != 1:
            continue
        NZ.add(tuple((sum(kv[r] * chi2(r, c) for r in range(4)) // 2) ** 2 for c in range(4)))
    return sorted(Z), sorted(NZ)


def odd_patterns():
    out = []
    for kv in itertools.product([1, -1, 3, -3, 5, -5, 7, -7], repeat=4):
        if len({x % 4 for x in kv}) != 1:
            continue
        g = 1 if kv[0] % 4 == 1 else -1
        om = tuple(((kv[r] - g) // 4) % 2 for r in range(4))
        v = tuple((sum(kv[r] * chi2(r, c) for r in range(4)) // 2) ** 2 for c in range(4))
        out.append((kv, om, v))
    return out


def in_class(om, x, h):
    target = [par(x & r) ^ (1 if (h == 1 and r == 3) else 0) for r in range(4)]
    return len({om[r] ^ target[r] for r in range(4)}) == 1


def Q6(s, kind):
    b = [(s >> i) & 1 for i in range(6)]
    v = b[0] * b[1] + b[2] * b[3] + b[4] * b[5]
    if kind == 'elliptic':
        v += b[4] + b[5]
    return v & 1


def n_vectors(kind):
    res = collections.Counter()
    for t1 in range(64):
        for t2 in range(64):
            for nu in range(4):
                N = [0] * 4
                for s in range(64):
                    l = (LAM if Q6(s, kind) else 0) ^ (par(t1 & s) | (par(t2 & s) << 1)) ^ nu
                    N[l] += 1
                res[tuple(N)] += 1
    return res


CANDIDATE_WEIGHTS = [[2, 3, 6, 6], [0, 1, 2, 2], [1, 2, 4, 4], [3, 4, 8, 8], [2, 2, 5, 5], [4, 2, 5, 5], [12, 5, 12, 9], [20, 11, 20, 15]]


def capacity(w, kind, h, N, Ztypes, NZtypes, OP, use_law=True):
    nZ0 = sum(1 for s in range(64) if Q6(s, kind) == 0) - 1; nNZ = 64 - nZ0 - 1
    capZ = max(sum(w[c] * t[c] for c in range(4)) for t in Ztypes)
    capN = max(sum(w[c] * t[c] for c in range(4)) for t in NZtypes)
    capx = []
    for x in range(4):
        capx.append(max(sum(w[c] * v[c] for c in range(4)) for (kv, om, v) in OP if (not use_law) or in_class(om, x, h)))
    total = capZ * nZ0 + capN * nNZ + sum(capx[x] * N[x] for x in range(4))
    return {'weights': w, 'capZ0': capZ, 'capNZ': capN, 'capOddByClass': capx, 'capacity': total, 'required': 4096 * sum(w), 'certifies': total < 4096 * sum(w)}


RELAXED = {'even': {'Z_affine_at_block_1': ([0, 64, 0, 0], 3), 'Z_affine_at_block_2': ([0, 0, 64, 0], 24), 'NZ_e0': ([0, 144, 0, 0], 20), 'NZ_e1': ([16, 64, 16, 16], 16)},
           'odd': [((5, 1, 1, 5), 1), ((5, -7, -7, 5), 12), ((-3, -7, -7, -3), 5), ((-7, 5, 5, -7), 14), ((-7, -7, 5, 5), 16), ((-7, -7, -7, -7), 16)]}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--output', type=pathlib.Path, required=True); a = ap.parse_args()
    if a.output.exists():
        raise FileExistsError(a.output)
    out = {'partA_identity_control': part_a()}
    Ztypes, NZtypes = even_types(); OP = odd_patterns()
    out['even_types'] = {'Z0_nonzero_fibre_contributions': Ztypes, 'NZ_fibre_contributions': NZtypes}
    out['odd_pattern_count'] = len(OP)
    cases = []; all_ok = True; control_fail_all = True
    for kind in ('elliptic', 'hyperbolic'):
        NV = n_vectors(kind)
        for h in (0, 1):
            for N in sorted(NV):
                cert = None
                for w in CANDIDATE_WEIGHTS:
                    c = capacity(w, kind, h, N, Ztypes, NZtypes, OP)
                    if c['certifies']:
                        cert = c; break
                ctrl = [capacity(w, kind, h, N, Ztypes, NZtypes, OP, use_law=False)['certifies'] for w in CANDIDATE_WEIGHTS]
                if any(ctrl):
                    control_fail_all = False
                if cert is None:
                    all_ok = False
                cases.append({'form': kind, 'h': h, 'N': list(N), 'multiplicity_of_(T,nu)': NV[N], 'certificate': cert, 'without_odd_law_any_candidate_certifies': any(ctrl)})
    out['cases'] = cases; out['all_cases_certified'] = all_ok; out['control_no_candidate_certifies_without_odd_law'] = control_fail_all
    blocks = [0, 0, 0, 0]; cls = collections.Counter()
    for name, (u, cnt) in RELAXED['even'].items():
        for c in range(4):
            blocks[c] += u[c] * cnt
    nZ = RELAXED['even']['Z_affine_at_block_1'][1] + RELAXED['even']['Z_affine_at_block_2'][1]
    nN = RELAXED['even']['NZ_e0'][1] + RELAXED['even']['NZ_e1'][1]
    for kv, cnt in RELAXED['odd']:
        v = [(sum(kv[r] * chi2(r, c) for r in range(4)) // 2) ** 2 for c in range(4)]
        for c in range(4):
            blocks[c] += v[c] * cnt
        g = 1 if kv[0] % 4 == 1 else -1; om = tuple(((kv[r] - g) // 4) % 2 for r in range(4))
        xs = [x for x in range(4) if in_class(om, x, 0)]
        cls[xs[0] if xs else 'nonaffine'] += cnt
    realizable = set(tuple(N) for kind in ('elliptic',) for N in n_vectors(kind))
    Nrel = tuple(cls.get(x, 0) for x in range(4))
    out['control_relaxed_point'] = {'block_energies': blocks, 'all_equal_4096': blocks == [4096] * 4, 'Z0_count': nZ, 'NZ_count': nN, 'odd_count': sum(c for _, c in RELAXED['odd']),
                                    'affine_class_distribution': list(Nrel), 'distribution_realizable_elliptic': Nrel in realizable}
    out['scope'] = 'four-zero branch block-energy capacity certificates; conditional on the adopted f131/f152 structure and the written lemmas; not a witness'
    with a.output.open('x', encoding='utf-8') as fh:
        json.dump(out, fh, indent=2, sort_keys=True); fh.write('\n')
    print('identity', out['partA_identity_control'], 'all_certified', all_ok, 'control_without_law_certifies_none', control_fail_all, 'relaxed', out['control_relaxed_point'])


if __name__ == '__main__':
    main()
