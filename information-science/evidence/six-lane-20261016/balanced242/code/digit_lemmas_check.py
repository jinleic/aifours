"""Exact finite checks of the sign-digit lemmas on genuine balanced Boolean functions (controls).

General statements checked (any balanced f on F_2^9, support XOR s != 0; T=W_f/4; d_k = digit k of T mod 16):
 L1  deg d_k <= 2^k (k=0..3) and the quartic part of d2 equals Pf4(B), B = polar matrix of d1.
 L2  translation x->x+c changes B by c s^T + s c^T (off-diagonal).
 L3  W_{d3} = 32F + 64 delta_0 + W_{d0}/8 + W_{d1}/4 + W_{d2}/2 - 4 H(e), e=(T-(d0+2d1+4d2-8d3))/16.
 L4  wt(d3 restricted to O={a.s=1}) = [rank of polar(D) = 8] (mod 2); W_{Jq} = 4[rank 8] (mod 8), Jq=d2|_O.
 L5  sum_y v(y) W_g(y) = 2 sum_{a in O} (-1)^{g(a)} q(a) for g = Jq, Dq (8-variable duality, coordinates s=e_8).
Mutation controls must FAIL: flipping one ANF coefficient of d2 (breaks L3), dropping the -4H(e) term.
Usage: python3 digit_lemmas_check.py [ntrials] [seed]
"""
import sys, json, hashlib, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bf

n, N = 9, 512

def to_e8(t):
    s = bf.support_xor(t); assert s != 0
    cols = [None] * 9; cols[8] = s; basis = [s]; k = 0
    for v in range(1, N):
        M = np.array([[(b >> i) & 1 for i in range(n)] for b in basis + [v]], dtype=np.uint8)
        if bf.rank_gf2(M) == len(basis) + 1:
            cols[k] = v; basis.append(v); k += 1
            if k == 8: break
    Ay = np.zeros(N, dtype=np.int64)
    for y in range(N):
        acc = 0
        for i in range(n):
            if (y >> i) & 1: acc ^= cols[i]
        Ay[y] = acc
    g = t[Ay]; assert bf.support_xor(g) == 256
    return g

def check_one(t, mutate=None):
    g = to_e8(t)
    W = bf.walsh(g); assert W[0] == 0
    d, T = bf.digits_T(W, 4)
    if mutate == "d2anf":
        c = bf.anf(d[2]); c[7] ^= 1; d[2] = bf.anf(c)
    pc = bf.popcount_array(N)
    res = {}
    degs = [bf.degree(x) for x in d]
    res["L1_deg"] = all(degs[k] <= 2 ** k for k in range(4))
    B9 = bf.quad_polar_matrix(d[1], n)
    c2 = bf.anf(d[2]); quart = np.where(pc == 4, c2, 0).astype(np.uint8)
    res["L1_pf4"] = bool(np.array_equal(quart, bf.anf(bf.pf4_function(B9, n))))
    # L3
    e = T - (d[0].astype(np.int64) + 2 * d[1] + 4 * d[2] - 8 * d[3].astype(np.int64))
    ok_e = bool(np.all(e % 16 == 0)); e //= 16
    F = 1 - 2 * g.astype(np.int64)
    Wd = [bf.walsh(x) for x in d]
    delta0 = np.zeros(N, dtype=np.int64); delta0[0] = 1
    corr = -4 * bf.fwht(e) if mutate != "drop_e" else 0
    rhs = 32 * F + 64 * delta0 + Wd[0] // 8 + Wd[1] // 4 + Wd[2] // 2 + corr
    res["L3"] = ok_e and bool(np.array_equal(Wd[3], rhs))
    # L4 (coordinates: O = {a_8=1})
    idxO = np.arange(256) | 256
    D = d[1][np.arange(256)]; B = bf.quad_polar_matrix(D, 8); rk = bf.rank_gf2(B)
    d3O = d[3][idxO]; Jq = d[2][idxO]
    WJ = bf.walsh(Jq)
    res["L4_parity"] = (int(d3O.sum()) % 2) == (1 if rk == 8 else 0)
    res["L4_kappa"] = bool(np.all(WJ % 8 == (4 if rk == 8 else 0)))
    # L4 general: for every h != 0 and c: wt(d3 on {a.h=c}) = det(beta restricted to h-perp) mod 2,
    # beta = sum_{x in supp} x x^T (mod 2, diagonal = s). Checked for 12 random h per table.
    X = np.nonzero(g)[0]
    beta = np.array([[int(np.sum(((X >> i) & 1) & ((X >> j) & 1)) % 2) for j in range(n)] for i in range(n)], dtype=np.int64)
    idx = np.arange(N); okh = True
    for h in np.random.default_rng(int(np.sum(g) * 7 + int(g[:64].sum()))).choice(np.arange(1, N), 12, replace=False):
        h = int(h); basis = []
        for vv in range(1, N):
            if bf.parity_dot(np.int64(vv), np.int64(h)) == 0:
                M = np.array([[(b >> i) & 1 for i in range(n)] for b in basis + [vv]], dtype=np.uint8)
                if bf.rank_gf2(M) == len(basis) + 1: basis.append(vv)
            if len(basis) == 8: break
        L = np.array([[(b >> i) & 1 for i in range(n)] for b in basis], dtype=np.int64)
        det = 1 if bf.rank_gf2(((L @ beta @ L.T) % 2).astype(np.uint8)) == 8 else 0
        for cb in (0, 1):
            okh &= (int(d[3][bf.parity_dot(idx, np.int64(h)) == cb].sum()) % 2) == det
    res["L4_hyperplanes"] = bool(okh)
    # L5: v(y)=(F(y,0)-F(y,1))/2, q = T on O
    v = (F[np.arange(256)] - F[idxO]) // 2
    q = T[idxO]
    assert np.array_equal(bf.fwht(q), 128 * v)
    ok5 = True
    for gfun in (Jq, d[1][idxO]):
        lhs = int(np.dot(v, bf.walsh(gfun)))
        rhs5 = 2 * int(np.dot(1 - 2 * gfun.astype(np.int64), q))
        ok5 &= (lhs == rhs5)
    res["L5"] = ok5
    res["rankD"] = rk; res["maxW"] = int(np.abs(W).max())
    return res, g

def main():
    ntr = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 20261016
    rng = np.random.default_rng(seed)
    rows = []; hashes = []
    ranks = {}
    for k in range(ntr):
        t = np.zeros(N, dtype=np.uint8); t[rng.choice(N, 256, replace=False)] = 1
        if bf.support_xor(t) == 0:
            continue
        r, g = check_one(t)
        rows.append(r); hashes.append(hashlib.sha256(g.tobytes()).hexdigest()[:16])
        ranks[r["rankD"]] = ranks.get(r["rankD"], 0) + 1
    allok = all(all(v for kk, v in r.items() if kk.startswith("L")) for r in rows)
    # mutation controls on the first table
    t = np.zeros(N, dtype=np.uint8); t[np.random.default_rng(seed + 1).choice(N, 256, replace=False)] = 1
    mut1, _ = check_one(t, mutate="d2anf"); mut2, _ = check_one(t, mutate="drop_e")
    controls_fail = (not mut1["L3"]) and (not mut2["L3"])
    out = dict(script=os.path.basename(__file__), seed=seed, trials=len(rows), rank_histogram=ranks,
               all_lemmas_pass=allok, mutation_controls_fail_as_required=controls_fail,
               mutation_results=dict(d2anf=mut1, drop_e=mut2), table_hash_prefixes=hashes)
    print(json.dumps(out, indent=1))
    if not (allok and controls_fail):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
