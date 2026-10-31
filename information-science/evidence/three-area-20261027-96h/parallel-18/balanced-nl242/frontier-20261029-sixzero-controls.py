#!/opt/homebrew/bin/python3
"""Controls for frontier-20261029-sixzero-exclusion-v1.md (independent of the C++ exhaustion).

1. Coset-parity tool (adopted f131 statement) on seeded random balanced Boolean functions:
   for random 5-dim L <= K = T^perp, wt(q|A)/4 + |A cap Z8| is constant mod 2 over the cosets A.
2. Independent construction of the family {5-dim L : rank(B|L) <= 2} for the rank-8 and rank-6 normal
   forms (sizes must be 11475 = #isotropic 3-spaces and 16515 = 1395 + 315*3*16).
3. Non-vacuity: the radical 2-plane R (4 points) passes every rank-6 family constraint; 2000 random
   six-sets with zero XOR are each violated by some family member in both forms.
"""
import argparse, functools, itertools, json, pathlib, random


def par(x):
    return bin(x).count('1') & 1


def span(vecs):
    S = {0}
    for v in vecs:
        S |= {s ^ v for s in S}
    return S


def rank_rows(rows):
    piv = {}
    for v in rows:
        while v:
            h = v.bit_length() - 1
            if h in piv:
                v ^= piv[h]
            else:
                piv[h] = v; break
    return len(piv)


def parity_tool(seed=7, trials=6, Ls=40):
    rng = random.Random(seed); tot = bad = 0
    for _ in range(trials):
        pts = list(range(512)); rng.shuffle(pts); M = pts[:256]
        k = [0] + [sum(par(a & x) for x in M) - 128 for a in range(1, 512)]
        T = 0
        for x in M:
            T ^= x
        if T == 0:
            continue
        K = [a for a in range(512) if par(a & T) == 0]
        q = {a: (k[a] // 2) % 2 for a in K}; Z8 = {a for a in K if k[a] % 8 == 0}
        for _ in range(Ls):
            while True:
                L = span([rng.choice(K) for _ in range(5)])
                if len(L) == 32:
                    break
            cos = {}
            for a in K:
                cos.setdefault(min(a ^ l for l in L), []).append(a)
            vals = {(sum(q[a] for a in A) // 4 + sum(1 for a in A if a in Z8)) % 2 for A in cos.values()}
            tot += 1; bad += (len(vals) != 1)
    return {'pairs_tested': tot, 'violations': bad, 'seed': seed}


def family(pairs):
    B = [[0] * 8 for _ in range(8)]
    for p in range(pairs):
        B[2 * p][2 * p + 1] = B[2 * p + 1][2 * p] = 1
    def Bf(a, b):
        return sum(B[i][j] for i in range(8) if (a >> i) & 1 for j in range(8) if (b >> j) & 1) % 2
    fam = []
    for pv in itertools.combinations(range(8), 5):
        frees = [[x for x in range(pv[a] + 1, 8) if x not in pv] for a in range(5)]
        tb = sum(len(f) for f in frees)
        for mask in range(1 << tb):
            g = []; b = 0
            for a in range(5):
                v = 1 << pv[a]
                for x in frees[a]:
                    if (mask >> b) & 1:
                        v |= 1 << x
                    b += 1
                g.append(v)
            if rank_rows([sum(Bf(g[a], g[c]) << c for c in range(5)) for a in range(5)]) <= 2:
                S = span(g); lab = {}; nc = 0
                for x in range(256):
                    if x not in lab:
                        for l in S:
                            lab[x ^ l] = nc
                        nc += 1
                fam.append(lab)
    return fam


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--output', type=pathlib.Path, required=True); a = ap.parse_args()
    if a.output.exists():
        raise FileExistsError(a.output)
    out = {'parity_tool_control': parity_tool()}
    f6, f8 = family(3), family(4)
    out['family_sizes'] = {'rank6': len(f6), 'rank8': len(f8)}
    pv = lambda lab, Z: functools.reduce(lambda u, z: u ^ (1 << lab[z]), Z, 0)
    R = [0, 64, 128, 192]
    out['radical_plane_violations_rank6'] = sum(1 for lab in f6 if pv(lab, R))
    rng = random.Random(5); unviolated = 0
    for _ in range(2000):
        while True:
            zs = rng.sample(range(1, 256), 4); z5 = zs[0] ^ zs[1] ^ zs[2] ^ zs[3]
            if z5 and z5 not in zs:
                break
        Z = [0] + zs + [z5]
        for fam in (f6, f8):
            if not any(pv(lab, Z) for lab in fam):
                unviolated += 1
    out['random_six_sets_unviolated'] = unviolated
    with a.output.open('x', encoding='utf-8') as fh:
        json.dump(out, fh, indent=2, sort_keys=True); fh.write('\n')
    print(json.dumps(out))


if __name__ == '__main__':
    main()
