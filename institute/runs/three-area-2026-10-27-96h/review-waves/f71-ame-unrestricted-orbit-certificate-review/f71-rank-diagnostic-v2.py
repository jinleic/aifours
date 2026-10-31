#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
f71-rank-diagnostic-v2.py  (reviewer-authored; DIAGNOSTIC ONLY, not a proof over C)

v2 versus v1 (bytes preserved): v1 mis-stated the pure-K/pure-K prediction as an
"iff"; the written Section 3.2 only claims the necessary direction (rank 1 implies
u_H = 0 and u_g = 0 for every g in supp t).  v2 tests that implication, biases all
covector kinds toward sparse supports so low-rank cases occur, and makes the
interpretation string depend on the outcome.

Exact arithmetic over Q(sqrt2).  Reads the pinned table with the reviewer's own
parser (imported from f71-independent-checker-v2.py, reviewer code), builds the
unnormalized face-P and face-P' tensors, and tests the written Section 3 rank
statements on random rational covectors, plus actual supports of structured
GL(6,Q)^4 transforms.  Random/structured instances cannot replace the written
complex argument; they can only expose a misreading of the block structure.

Usage: python3 f71-rank-diagnostic-v2.py TABLE CHECKER_V2 --output RECEIPT.json
"""
import sys, os, json, hashlib, itertools, random, datetime, importlib.util
from fractions import Fraction as Fr

H = (1, 2); K = (0, 3, 4, 5)
PARTIES = range(4)


def load_mod(path):
    spec = importlib.util.spec_from_file_location('revchk', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Q(sqrt2) elements as (p, q) Fractions
Z0 = (Fr(0), Fr(0)); Z1 = (Fr(1), Fr(0))


def qa(x, y): return (x[0] + y[0], x[1] + y[1])
def qm(x, y): return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def qneg(x): return (-x[0], -x[1])
def qinv(x):
    d = x[0] * x[0] - 2 * x[1] * x[1]
    if d == 0:
        raise ZeroDivisionError
    return (x[0] / d, -x[1] / d)
def qz(x): return x[0] == 0 and x[1] == 0


def rank(M):
    M = [row[:] for row in M]
    nr, nc = len(M), len(M[0])
    r = 0
    for c in range(nc):
        piv = None
        for i in range(r, nr):
            if not qz(M[i][c]):
                piv = i; break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = qinv(M[r][c])
        M[r] = [qm(v, inv) for v in M[r]]
        for i in range(nr):
            if i != r and not qz(M[i][c]):
                f = M[i][c]
                M[i] = [qa(M[i][j], qneg(qm(f, M[r][j]))) for j in range(nc)]
        r += 1
        if r == nr:
            break
    return r


def contract(T, C, B, lam, u):
    """M[a][d] = sum_{b,c} T[pos] lam[c] u[b] with A,D the remaining parties in order."""
    A, D = [i for i in PARTIES if i not in (C, B)]
    M = [[Z0] * 6 for _ in range(6)]
    for pos, coef in T.items():
        lc = lam[pos[C]]; ub = u[pos[B]]
        if qz(lc) or qz(ub):
            continue
        M[pos[A]][pos[D]] = qa(M[pos[A]][pos[D]], qm(qm(coef, lc), ub))
    return M


def rnd_vec(rng, kind):
    while True:
        v = [Z0] * 6
        keep = set(range(6))
        if rng.random() < 0.6:
            keep = set(rng.sample(range(6), rng.randint(1, 3)))
            if kind == 'mixed':
                keep |= {rng.choice(H), rng.choice(K)}
        for i in range(6):
            if kind == 'pureH' and i not in H: continue
            if kind == 'pureK' and i not in K: continue
            if i not in keep: continue
            v[i] = (Fr(rng.randint(-3, 3)), Fr(rng.randint(-1, 1)))
        hz = all(qz(v[i]) for i in H); kz = all(qz(v[i]) for i in K)
        if kind == 'pureH' and not hz: return v
        if kind == 'pureK' and not kz: return v
        if kind == 'mixed' and not hz and not kz: return v
        if kind == 'any' and not (hz and kz): return v


def necessary_condition_rank_one(lam, u, colour, C, B):
    # written Section 3.2: rank 1 implies F = 0, i.e. t_g u_g = 0 for every colour g
    # (u lies in W_t for every g in supp t); and never both supports the same singleton
    tsup = {colour[C][i] for i in K if not qz(lam[i])}
    usup = {colour[B][i] for i in K if not qz(u[i])}
    F_zero = not (tsup & usup)
    same_singleton = (len(tsup) == 1 and tsup == usup)
    return F_zero and not same_singleton


def main(argv):
    if len(argv) != 5 or argv[3] != '--output':
        sys.stderr.write(__doc__); return 2
    table_path, chk_path, _, out_path = argv[1:]
    if os.path.exists(out_path):
        sys.stderr.write('refusing to overwrite\n'); return 3
    mod = load_mod(chk_path)
    tb = open(table_path, 'rb').read()
    T_int, cells = mod.parse_pinned_table(tb.decode('utf-8'))
    mod.check_table_shape(T_int, cells)
    P, E = mod.classify(T_int)
    colour = mod.COLOUR_BASE
    Pp = [(0,3,5,3),(3,5,3,0),(4,0,4,4),(5,4,0,5),(0,4,3,4),(3,0,5,5),(4,5,0,3),(5,3,4,0),(0,5,4,5),(3,3,0,4),(4,4,5,0),(5,0,3,3)]
    faces = {}
    faces['P'] = {pos: (Fr(c[0]), Fr(c[1])) for pos, c in T_int.items()}
    faces["P'"] = {pos: (Fr(T_int[pos][0]), Fr(0)) for pos in E}
    for pos in Pp:
        faces["P'"][pos] = (Fr(0), Fr(1))
    rng = random.Random(71)
    receipt = {'inputs': {'table': {'path': os.path.abspath(table_path), 'sha256': hashlib.sha256(tb).hexdigest()},
                          'reviewer_checker': {'path': os.path.abspath(chk_path), 'sha256': hashlib.sha256(open(chk_path, 'rb').read()).hexdigest()}},
               'self_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
               'clock_start_local': datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
               'diagnostic_only': True, 'faces': {}}
    ok = True
    N = 60
    for fname, T in faces.items():
        stats = {'pureH_vs_any_min_rank': 9, 'pureK_vs_uH_nonzero_min_rank': 9, 'mixed_vs_any_min_rank': 9,
                 'pureK_pureK_tested': 0, 'pureK_pureK_rank_one_cases': 0,
                 'pureK_pureK_rank_one_violating_necessary_condition': 0,
                 'pureK_pureK_necessary_condition_but_rank_two': 0,
                 'pureK_pureK_min_rank': 9,
                 'zero_contractions': 0, 'trials_per_orientation_per_kind': N}
        for C, B in itertools.permutations(PARTIES, 2):
            for _ in range(N):
                lam = rnd_vec(rng, 'pureH'); u = rnd_vec(rng, 'any')
                r = rank(contract(T, C, B, lam, u)); stats['pureH_vs_any_min_rank'] = min(stats['pureH_vs_any_min_rank'], r)
                if r == 0: stats['zero_contractions'] += 1
                lam = rnd_vec(rng, 'pureK'); u = rnd_vec(rng, 'any')
                while all(qz(u[i]) for i in H):
                    u = rnd_vec(rng, 'any')
                r = rank(contract(T, C, B, lam, u)); stats['pureK_vs_uH_nonzero_min_rank'] = min(stats['pureK_vs_uH_nonzero_min_rank'], r)
                if r == 0: stats['zero_contractions'] += 1
                lam = rnd_vec(rng, 'mixed'); u = rnd_vec(rng, 'any')
                r = rank(contract(T, C, B, lam, u)); stats['mixed_vs_any_min_rank'] = min(stats['mixed_vs_any_min_rank'], r)
                if r == 0: stats['zero_contractions'] += 1
                lam = rnd_vec(rng, 'pureK'); u = rnd_vec(rng, 'pureK')
                # bias toward sparse supports so rank-one cases occur
                if rng.random() < 0.6:
                    keepC = rng.sample(list(K), rng.randint(1, 2)); keepB = rng.sample(list(K), rng.randint(1, 2))
                    lam = [lam[i] if i in keepC else Z0 for i in range(6)]
                    u = [u[i] if i in keepB else Z0 for i in range(6)]
                    if all(qz(x) for x in lam) or all(qz(x) for x in u):
                        continue
                r = rank(contract(T, C, B, lam, u))
                if r == 0: stats['zero_contractions'] += 1
                nec = necessary_condition_rank_one(lam, u, colour, C, B)
                stats['pureK_pureK_tested'] += 1
                stats['pureK_pureK_min_rank'] = min(stats['pureK_pureK_min_rank'], r)
                if r == 1:
                    stats['pureK_pureK_rank_one_cases'] += 1
                    if not nec:
                        stats['pureK_pureK_rank_one_violating_necessary_condition'] += 1
                elif nec:
                    stats['pureK_pureK_necessary_condition_but_rank_two'] += 1
        stats['pureK_pureK_implication_holds'] = stats['pureK_pureK_rank_one_violating_necessary_condition'] == 0
        if stats['pureH_vs_any_min_rank'] < 2 or stats['pureK_vs_uH_nonzero_min_rank'] < 2 or stats['mixed_vs_any_min_rank'] < 2 \
           or stats['zero_contractions'] or not stats['pureK_pureK_implication_holds'] or stats['pureK_pureK_min_rank'] < 1:
            ok = False
        # identity-basis slice ranks must sum to 60
        total = 0
        for C, B in ((2, 1),):
            for c in range(6):
                for b in range(6):
                    lam = [Z1 if i == c else Z0 for i in range(6)]; u = [Z1 if i == b else Z0 for i in range(6)]
                    total += rank(contract(T, C, B, lam, u))
        stats['identity_basis_rank_sum_C2_B1'] = total
        if total != 60: ok = False
        # structured GL(6,Q)^4 transforms: actual support count
        def transform_support(Vs):
            out = {}
            for pos, coef in T.items():
                cols = [[(i, Vs[p][i][pos[p]]) for i in range(6) if not qz(Vs[p][i][pos[p]])] for p in PARTIES]
                for (a, va) in cols[0]:
                    ca = qm(coef, va)
                    for (b, vb) in cols[1]:
                        cb = qm(ca, vb)
                        for (c, vc) in cols[2]:
                            cc = qm(cb, vc)
                            for (d, vd) in cols[3]:
                                key = (a, b, c, d)
                                out[key] = qa(out.get(key, Z0), qm(cc, vd))
            return sum(1 for v in out.values() if not qz(v))
        def ident():
            return [[Z1 if i == j else Z0 for j in range(6)] for i in range(6)]
        def hadamard_H():
            V = ident()
            V[1][1] = Z1; V[1][2] = Z1; V[2][1] = Z1; V[2][2] = qneg(Z1)
            return V
        def swap_levels(i, j):
            V = ident(); V[i][i] = Z0; V[j][j] = Z0; V[i][j] = Z1; V[j][i] = Z1; return V
        def mix_HK():
            V = ident(); V[1][0] = Z1; V[0][3] = Z1; V[4][2] = (Fr(0), Fr(1)); return V
        def random_dense():
            while True:
                V = [[(Fr(rng.randint(-2, 2)), Fr(0)) for _ in range(6)] for _ in range(6)]
                if rank(V) == 6: return V
        def kblock_dense():
            while True:
                V = ident()
                for i in K:
                    for j in K:
                        V[i][j] = (Fr(rng.randint(-2, 2)), Fr(rng.randint(-1, 1)))
                if rank(V) == 6: return V
        attempts = {
            'identity': [ident()] * 4,
            'hadamard_on_H_all_parties': [hadamard_H()] * 4,
            'hadamard_on_H_party0_only': [hadamard_H(), ident(), ident(), ident()],
            'swap_H_K_levels_1_0_party2': [ident(), ident(), swap_levels(1, 0), ident()],
            'mix_HK_party2': [ident(), ident(), mix_HK(), ident()],
            'mix_HK_all_parties': [mix_HK()] * 4,
            'dense_K_block_party1_party2': [ident(), kblock_dense(), kblock_dense(), ident()],
            'dense_K_block_all_parties': [kblock_dense() for _ in range(4)],
            'random_dense_party3': [ident(), ident(), ident(), random_dense()],
            'random_dense_parties_2_3': [ident(), ident(), random_dense(), random_dense()],
        }
        sup = {}
        for name, Vs in attempts.items():
            s = transform_support(Vs)
            sup[name] = s
            if s < 60: ok = False
        stats['structured_transform_supports'] = sup
        stats['all_transform_supports_at_least_60'] = all(v >= 60 for v in sup.values())
        receipt['faces'][fname] = stats
    receipt['clock_end_local'] = datetime.datetime.now().astimezone().isoformat(timespec='seconds')
    receipt['overall'] = 'CONSISTENT' if ok else 'INCONSISTENT'
    receipt['interpretation'] = ('All observations consistent with the written Section 3/7 claims' if ok else 'At least one observation contradicts the reviewer-coded expectation; see stats') + '; this is a diagnostic over finitely many rational instances and is not a proof over C.'
    with open(out_path, 'x', encoding='utf-8') as f:
        json.dump(receipt, f, indent=1); f.write('\n')
    print(json.dumps({k: (v if k != 'faces' else {fk: {kk: vv for kk, vv in fv.items() if kk != 'structured_transform_supports'} for fk, fv in v.items()}) for k, v in receipt.items()}, indent=1))
    for fk, fv in receipt['faces'].items():
        print(fk, fv['structured_transform_supports'])
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
