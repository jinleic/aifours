#!/usr/bin/env python3
"""reviewer-f131-controls-v1.py  (review wave f131-walsh-four-zero-rank6-only)

Independently written reviewer controls.  No author code is imported or executed;
every routine below is the reviewer's own reconstruction of the packet setting.

Setting (as in the two packets): f : F2^9 -> {0,1} balanced, k = W_f/4,
T = XOR of the one-support (assumed nonzero), K = T^perp (8-dim), q = k/2 mod 2 on K,
B = polar form of q, R = rad(B), Z8 = {a in K : k(a) = 0 mod 8}.

Control A (real Boolean functions, every rank 0..8 of B):
  A1 q is quadratic on K;  A1' bit2(k mod 8)|K is quartic and 1_Z8 = (1+q)(1+bit2)  [reviewer's
      independent route to deg<=6 via Lucas' theorem];
  A2 mixed-6-flat identity (1): E(A)+E(B0) = 0 mod 32 for EVERY 5-dim L<=K, every even coset A,
      with a fixed odd coset B0;  A2' all affine 6-flats of F2^9 (exhaustive or sampled);
  A3 every coset weight n_q(A) = 0 mod 4; coset lemma (3) for all 97155 five-dim L<=K;
  A4 parity constancy H2 for all L;  A5 deg 1_Z8 <= 6, <= 5 when rank(B) <= 4;  A6 |Z8| bounds.
Control B (abstract model = packet hypotheses only): for 13 GL(8)-classes of quadratic q,
  compute the full H2 solution space, then EXHAUSTIVELY enumerate all 4-sets containing 0 and
  report which satisfy H2 (and which lie in {q=0}); verify rank-8 L-construction on every totally
  singular plane; planted counter-controls N1..N5.
"""
import sys, os, json, time, random, hashlib, subprocess, itertools
from collections import defaultdict
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261028
rng = random.Random(SEED)

def clock():
    return subprocess.run(["/bin/date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True).stdout.strip()

T0 = time.time()
RESULT = {"schema": 1, "id": "reviewer-f131-controls-v1", "seed": SEED, "clock_start": clock()}
RESULT["script_sha256"] = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()

# ----------------------------------------------------------------------------- basics
def parity_table(nbits):
    size = 1 << nbits
    idx = np.arange(size, dtype=np.int64)
    pc = np.array([bin(i).count("1") & 1 for i in range(size)], dtype=np.uint8)
    return pc[idx[:, None] & idx[None, :]]          # [u, a] = parity(u & a)

PAR9 = parity_table(9)
PAR8 = parity_table(8)
SIGN9 = 1 - 2 * PAR9.astype(np.int64)

def mobius(vals, nbits):
    a = np.array(vals, dtype=np.uint8).copy()
    n = 1 << nbits
    idx = np.arange(n)
    for i in range(nbits):
        step = 1 << i
        hi = idx[(idx & step) != 0]
        a[hi] ^= a[hi ^ step]
    return a

def degree(vals, nbits):
    anf = mobius(vals, nbits)
    nz = np.nonzero(anf)[0]
    return -1 if len(nz) == 0 else max(bin(int(m)).count("1") for m in nz)

def gf2_rank(rows):
    M = [int(x) for x in rows]
    r = 0
    for bit in range(64):
        piv = None
        for i in range(r, len(M)):
            if (M[i] >> bit) & 1:
                piv = i; break
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and (M[i] >> bit) & 1: M[i] ^= M[r]
        r += 1
    return r

def rref_subspaces(r, n):
    """All r-dim subspaces of F2^n as tuples of r RREF basis ints (bit j <-> coordinate j)."""
    out = []
    for pivots in itertools.combinations(range(n), r):
        free = [(i, j) for i in range(r) for j in range(pivots[i] + 1, n) if j not in pivots]
        for bits in itertools.product((0, 1), repeat=len(free)):
            rows = [1 << pivots[i] for i in range(r)]
            for (i, j), b in zip(free, bits):
                if b: rows[i] |= 1 << j
            out.append(tuple(rows))
    return out

def span(vecs):
    s = {0}
    for v in vecs:
        s |= {x ^ v for x in s}
    return s

# ----------------------------------------------------------------------------- 5-dim L structures on F2^8
def build_L_structures():
    U = rref_subspaces(3, 8)
    assert len(U) == 97155, len(U)
    U = np.array(U, dtype=np.int64)
    CID = (PAR8[U[:, 0]] | (PAR8[U[:, 1]] << 1) | (PAR8[U[:, 2]] << 2)).astype(np.uint8)
    NL = len(U)
    Uel = np.zeros((NL, 8), dtype=np.int64)
    for m in range(8):
        v = np.zeros(NL, dtype=np.int64)
        for i in range(3):
            if (m >> i) & 1: v ^= U[:, i]
        Uel[:, m] = v
    Umask = np.zeros((NL, 256), dtype=bool)
    Umask[np.arange(NL)[:, None], Uel] = True
    return dict(U=U, CID=CID, Umask=Umask, isinL=(CID == 0), NL=NL)

def coset_sums(CID, vec):
    v = vec.astype(np.float32)
    out = np.zeros((CID.shape[0], 8), dtype=np.int64)
    for j in range(8):
        out[:, j] = np.rint((CID == j).astype(np.float32) @ v).astype(np.int64)
    return out

def polar_data(q):
    """Polar matrix, Mvec[r] = B(.,r) as a dot-mask, rank, radical, and an all-pairs quadraticity check."""
    assert int(q[0]) == 0
    Bm = np.zeros((8, 8), dtype=np.uint8)
    for i in range(8):
        for j in range(8):
            Bm[i, j] = q[(1 << i) ^ (1 << j)] ^ q[1 << i] ^ q[1 << j]
    rowmask = [sum(int(Bm[i, j]) << j for j in range(8)) for i in range(8)]
    c = np.arange(256)
    Mvec = np.zeros(256, dtype=np.int64)
    for i in range(8):
        Mvec |= PAR8[rowmask[i], c].astype(np.int64) << i
    lhs = q[c[:, None] ^ c[None, :]] ^ q[:, None] ^ q[None, :]
    rhs = PAR8[:, Mvec]
    quadratic_consistent = bool(np.array_equal(lhs, rhs))
    rank = gf2_rank(rowmask)
    R = [int(r) for r in range(256) if Mvec[r] == 0]
    return Bm, Mvec, rank, R, quadratic_consistent

def restricted_rank_info(LS, Mvec):
    inrad = LS["isinL"] & LS["Umask"][:, Mvec]      # x in L and B(x,.) kills L  <=> x in rad(B|L)
    radsize = inrad.sum(axis=1)
    assert set(np.unique(radsize).tolist()) <= {2, 8, 32}
    rankL = 5 - np.log2(radsize).astype(np.int64)
    inrad[:, 0] = False
    rL = np.argmax(inrad, axis=1)                    # unique nonzero radical element when rank 4
    return rankL, rL

def analyze_profile(LS, q, z, Mvec, rankL, rL):
    """Checks on an even-half profile (q quadratic, z = 1_Z): weights mod 4, lemma (3), H2."""
    CID = LS["CID"]
    nq = coset_sums(CID, q)
    nz = coset_sums(CID, z)
    wt_mod4_ok = bool(np.all(nq % 4 == 0))
    phi = ((nq // 4) & 1).astype(np.uint8)
    rows4 = np.nonzero(rankL == 4)[0]
    rows_le2 = np.nonzero(rankL <= 2)[0]
    ok_le2 = bool(np.all(phi[rows_le2] == 0))
    if len(rows4):
        r = rL[rows4]
        expected = (1 ^ q[r][:, None] ^ PAR8[:, Mvec[r]].T).astype(np.uint8)
        actual = phi[rows4][np.arange(len(rows4))[:, None], CID[rows4]]
        ok4 = bool(np.all(expected == actual))
    else:
        ok4 = True
    phi_const = np.all(phi == phi[:, :1], axis=1)
    par = ((nz + nq // 4) & 1)
    h2_ok_rows = np.all(par == par[:, :1], axis=1)
    return dict(weights_mod4_ok=wt_mod4_ok, lemma3_rank_le2_phi_zero=ok_le2, lemma3_rank4_affine_formula=ok4,
                n_L_rank4=int(len(rows4)), n_L_rank_le2=int(len(rows_le2)),
                n_L_phi_nonconstant=int((~phi_const).sum()),
                h2_violating_L=int((~h2_ok_rows).sum()), n_L=int(LS["NL"]))

# ----------------------------------------------------------------------------- real functions
def walsh(f):
    s = 1 - 2 * f.astype(np.int64)
    return SIGN9 @ s

def even_half(f):
    """Returns (dict with T, K-basis map, k on K, q, z, e4) or (None, W) if outside the setting."""
    W = walsh(f)
    if not np.all(W % 4 == 0):
        return None, W
    k = W // 4
    supp = np.nonzero(f)[0]
    T = 0
    for x in supp: T ^= int(x)
    if T == 0:
        return None, W
    t = (T & -T).bit_length() - 1
    basis = []
    for i in range(9):
        if i == t: continue
        v = 1 << i
        if (T >> i) & 1: v |= 1 << t
        basis.append(v)
    amap = np.zeros(256, dtype=np.int64)
    for c in range(256):
        a = 0
        for i in range(8):
            if (c >> i) & 1: a ^= basis[i]
        amap[c] = a
    assert np.all(PAR9[T, amap] == 0) and len(set(amap.tolist())) == 256
    kK = k[amap]
    assert np.all(kK % 2 == 0)
    q = ((kK % 4) == 2).astype(np.uint8)
    z = ((kK % 8) == 0).astype(np.uint8)
    e4 = (((kK % 8) // 4) & 1).astype(np.uint8)
    return dict(W=W, k=k, T=T, t=t, amap=amap, kK=kK, q=q, z=z, e4=e4), W

def six_flat_check(k, U9, sample=None):
    k2 = k.astype(np.float32) ** 2
    rows = U9 if sample is None else U9[sample]
    viol = 0; total = 0
    for start in range(0, len(rows), 16384):
        Uc = rows[start:start + 16384]
        cid = (PAR9[Uc[:, 0]] | (PAR9[Uc[:, 1]] << 1) | (PAR9[Uc[:, 2]] << 2))
        for j in range(8):
            E = np.rint((cid == j).astype(np.float32) @ k2).astype(np.int64)
            viol += int(np.sum(E % 32 != 0)); total += int(len(E))
    return viol, total

def control_A_one(LS, U9, f, label, full_flats):
    eh, W = even_half(f)
    res = {"label": label, "weight": int(f.sum()), "peak": int(np.abs(W).max()), "W_mod4_zero": bool(np.all(W % 4 == 0))}
    if eh is None:
        res["note"] = "outside setting (k non-integral or T = 0)"
        return res
    res["T"] = eh["T"]
    res["k_parity_equals_a_dot_T"] = bool(np.all((eh["k"] % 2) == PAR9[eh["T"]]))
    q, z, e4, kK = eh["q"], eh["z"], eh["e4"], eh["kK"]
    Bm, Mvec, rank, R, quad_ok = polar_data(q)
    res.update(deg_q=degree(q, 8), q_quadratic_allpairs=quad_ok, rank_B=rank, dim_R=int(np.log2(len(R))), deg_e4=degree(e4, 8))
    res["z_equals_1pq_1pe4"] = bool(np.array_equal(z, (1 ^ q) & (1 ^ e4)))
    res["Z8_size"] = int(z.sum()); res["zero_in_Z8"] = bool(z[0] == 1)
    res["Z8_subset_qzero"] = bool(np.all(q[z == 1] == 0))
    res["deg_1Z8"] = degree(z, 8)
    res["deg_bound_ok"] = (res["deg_1Z8"] <= 6) and (rank > 4 or res["deg_1Z8"] <= 5)
    res["size_bound_ok"] = (res["Z8_size"] >= 4) and (rank > 4 or res["Z8_size"] >= 8)
    rankL, rL = restricted_rank_info(LS, Mvec)
    res["rankL_histogram"] = {int(v): int(c) for v, c in zip(*np.unique(rankL, return_counts=True))}
    res.update(analyze_profile(LS, q, z, Mvec, rankL, rL))
    res["phi_constant_when_rank_le4"] = (rank > 4) or (res["n_L_phi_nonconstant"] == 0)
    # (1): E(A)+E(B0) = 0 mod 32 for every 5-dim L<=K, every even coset A, fixed odd coset B0 = a0+L
    a0 = 1 << eh["t"]                       # a0.T = T_t = 1, so a0 lies in the odd half
    kodd2 = (eh["k"][a0 ^ eh["amap"]].astype(np.float32)) ** 2
    E_even = coset_sums(LS["CID"], kK.astype(np.float32) ** 2)
    E_odd = np.rint(LS["isinL"].astype(np.float32) @ kodd2).astype(np.int64)
    res["mixed_identity_1_violations"] = int(np.sum((E_even + E_odd[:, None]) % 32 != 0))
    res["E_even_mod32_constant_per_L"] = bool(np.all((E_even % 32) == (E_even[:, :1] % 32)))
    if full_flats:
        v, tot = six_flat_check(eh["k"], U9)
        res["six_flat_check"] = {"mode": "exhaustive", "flats": tot, "violations": v}
    else:
        samp = np.array(rng.sample(range(len(U9)), 20000))
        v, tot = six_flat_check(eh["k"], U9, samp)
        res["six_flat_check"] = {"mode": "sampled", "flats": tot, "violations": v}
    return res, eh, Mvec, rankL, rL

def random_balanced():
    perm = list(range(512)); rng.shuffle(perm)
    f = np.zeros(512, np.uint8); f[perm[:256]] = 1
    return f

def structured(m, V=None):
    """S0 = {x : bit8 = 0}; remove m points of S0 and add m points outside; optionally inside subspace V."""
    f = np.zeros(512, np.uint8); f[:256] = 1
    if V is None:
        out = rng.sample(range(256), m); inn = rng.sample(range(256, 512), m)
    else:
        Vin = [x for x in V if x < 256]; Vout = [x for x in V if x >= 256]
        out = rng.sample(Vin, m); inn = rng.sample(Vout, m)
    f[out] = 0; f[inn] = 1
    return f

def random_subspace(dim, n=9):
    while True:
        vecs = [rng.randrange(1, 1 << n) for _ in range(dim)]
        S = span(vecs)
        if len(S) == 1 << dim and any(x >= 256 for x in S) and any(0 < x < 256 for x in S):
            return sorted(S)

# ----------------------------------------------------------------------------- abstract model
def canonical_q(rank, variant):
    h = rank // 2
    q = np.zeros(256, dtype=np.uint8)
    for c in range(256):
        val = 0
        for i in range(h):
            val ^= ((c >> (2 * i)) & 1) & ((c >> (2 * i + 1)) & 1)
        if variant == "arf1" and h >= 1:
            val ^= (c & 1) ^ ((c >> 1) & 1)
        if variant == "lin":
            val ^= (c >> (2 * h)) & 1
        q[c] = val
    return q

def rm2_columns():
    monos = [()] + [(i,) for i in range(8)] + [(i, j) for i in range(8) for j in range(i + 1, 8)]
    assert len(monos) == 37
    col = np.zeros(256, dtype=np.int64)
    for idx, S in enumerate(monos):
        for c in range(256):
            if all((c >> j) & 1 for j in S): col[c] |= 1 << idx
    return col

def solve_gf2(A, b):
    M = np.concatenate([A.astype(np.uint8), b.astype(np.uint8)[:, None]], axis=1)
    nrows, ncols = M.shape; nvar = ncols - 1
    piv = []; r = 0
    for c in range(nvar):
        rows = np.nonzero(M[r:, c])[0]
        if len(rows) == 0: continue
        p = r + int(rows[0])
        if p != r: M[[r, p]] = M[[p, r]]
        others = np.nonzero(M[:, c])[0]; others = others[others != r]
        M[others] ^= M[r]
        piv.append(c); r += 1
        if r == nrows: break
    inconsistent = bool(np.any((M[:, :nvar].sum(axis=1) == 0) & (M[:, nvar] == 1)))
    sol = np.zeros(nvar, dtype=np.uint8)
    for i, c in enumerate(piv): sol[c] = M[i, nvar]
    return sol, len(piv), inconsistent

def h2_system(q, Mvec):
    """Equations <g, 1_{a+M}> = [rank(B|M) = 6] over all 6-dim M <= F2^8 and all cosets a+M."""
    U2 = np.array(rref_subspaces(2, 8), dtype=np.int64); assert len(U2) == 10795
    cid2 = (PAR8[U2[:, 0]] | (PAR8[U2[:, 1]] << 1)).astype(np.uint8)
    isinM = (cid2 == 0)
    Uel = np.stack([np.zeros(len(U2), np.int64), U2[:, 0], U2[:, 1], U2[:, 0] ^ U2[:, 1]], axis=1)
    Umask = np.zeros((len(U2), 256), dtype=bool); Umask[np.arange(len(U2))[:, None], Uel] = True
    radsize = (isinM & Umask[:, Mvec]).sum(axis=1)
    assert set(np.unique(radsize).tolist()) <= {1, 4, 16, 64}
    rankM = 6 - np.log2(radsize).astype(np.int64)
    psi = (rankM == 6).astype(np.uint8)
    rows = []; rhs = []
    for j in range(4):
        rows.append((cid2 == j).astype(np.uint8)); rhs.append(psi)
    A = np.concatenate(rows, axis=0); b = np.concatenate(rhs)
    return A, b, {int(v): int(c) for v, c in zip(*np.unique(rankM, return_counts=True))}

def four_set_search(col, t):
    byval = defaultdict(list)
    for c in range(1, 256): byval[int(col[c])].append(c)
    found = []; base = t ^ int(col[0])
    for z1 in range(1, 256):
        c1 = base ^ int(col[z1])
        for z2 in range(z1 + 1, 256):
            need = c1 ^ int(col[z2])
            for z3 in byval.get(need, ()):
                if z3 > z2: found.append((0, z1, z2, z3))
    return found

def random_rm(maxdeg, force_monomial=None):
    anf = np.zeros(256, dtype=np.uint8)
    for m in range(256):
        if bin(m).count("1") <= maxdeg and rng.random() < 0.5: anf[m] = 1
    if force_monomial is not None: anf[force_monomial] = 1
    return mobius(anf, 8)        # Moebius transform is an involution: ANF -> truth table

def totally_singular_planes(q, Mvec):
    planes = set()
    zeros = [c for c in range(1, 256) if q[c] == 0]
    for i, z1 in enumerate(zeros):
        for z2 in zeros[i + 1:]:
            if PAR8[z1, Mvec[z2]] == 0:
                planes.add(frozenset({0, z1, z2, z1 ^ z2}))
    return planes

def rank8_L_construction(e1, e2, Mvec, q):
    Bf = lambda a, b: int(PAR8[a, Mvec[b]])
    f1 = next(x for x in range(256) if Bf(e1, x) == 1 and Bf(e2, x) == 0)
    f2 = next(x for x in range(256) if Bf(e1, x) == 0 and Bf(e2, x) == 1)
    if Bf(f1, f2): f2 ^= e1
    assert Bf(f1, f2) == 0 and Bf(e1, f1) == 1 and Bf(e2, f1) == 0 and Bf(e1, f2) == 0 and Bf(e2, f2) == 1
    Wc = [x for x in range(256) if Bf(x, e1) == 0 and Bf(x, e2) == 0 and Bf(x, f1) == 0 and Bf(x, f2) == 0]
    assert len(Wc) == 16
    e3 = next(x for x in Wc if x != 0)
    D = span([f1, f2, e3]); assert len(D) == 8
    L = [x for x in range(256) if Bf(x, f1) == 0 and Bf(x, f2) == 0 and Bf(x, e3) == 0]
    rad = [x for x in L if all(Bf(x, l) == 0 for l in L)]
    cid = lambda x: Bf(x, f1) | (Bf(x, f2) << 1) | (Bf(x, e3) << 2)
    Z = [0, e1, e2, e1 ^ e2]
    wts = [sum(int(q[x]) for x in range(256) if cid(x) == j) for j in range(8)]
    zc = [cid(zz) for zz in Z]
    return dict(dimL5=(len(L) == 32), D_in_L=(D <= set(L)), radical_is_D=(set(rad) == D), rankL=5 - int(np.log2(len(rad))),
                L_meets_Z_only_at_0=(set(L) & set(Z) == {0}), Z_in_four_distinct_cosets=(len(set(zc)) == 4),
                coset_weights=wts, weights_div8=all(w % 8 == 0 for w in wts))

def complement_L_containing(r, Zset):
    """5-dim L containing r with L ∩ Z = {0} (Z a 2-plane, r not in Z)."""
    basis = [r]
    while len(basis) < 5:
        v = rng.randrange(1, 256)
        S = span(basis + [v])
        if len(S) == 1 << (len(basis) + 1) and (S & Zset) == {0}:
            basis.append(v)
    return sorted(span(basis))

def coset_table(Lset):
    rep = {a: min(a ^ l for l in Lset) for a in range(256)}
    ids = {r: i for i, r in enumerate(sorted(set(rep.values())))}
    return np.array([ids[rep[a]] for a in range(256)], dtype=np.int64)

# ============================================================================= RUN
LS = build_L_structures()
U9 = np.array(rref_subspaces(3, 9), dtype=np.int64); assert len(U9) == 788035
RESULT["enumerations"] = {"five_dim_subspaces_of_F2^8": int(LS["NL"]), "six_dim_subspaces_of_F2^9": int(len(U9))}
print("structures built", round(time.time() - T0, 1), flush=True)

# ---------------- Control A
A = []
keep = {}
specs = [("random_balanced_1", lambda: random_balanced(), True, None),
         ("random_balanced_2", lambda: random_balanced(), False, None),
         ("random_balanced_3", lambda: random_balanced(), False, None),
         ("hyperplane_swap_m1_rank0", lambda: structured(1), False, 0),
         ("hyperplane_swap_m2_rank2", lambda: structured(2), False, 2),
         ("hyperplane_swap_m3_rank4", lambda: structured(3), False, 4),
         ("hyperplane_swap_m4_rank6", lambda: structured(4), True, 6),
         ("hyperplane_swap_m5_rank8", lambda: structured(5), False, 8),
         ("hyperplane_swap_m40_in_V7_rank6", lambda: structured(40, random_subspace(7)), False, 6),
         ("hyperplane_swap_m12_in_V5_rank4", lambda: structured(12, random_subspace(5)), False, 4)]
for label, gen, full, expect in specs:
    for attempt in range(30):
        f = gen()
        eh, W = even_half(f)
        if eh is None:
            continue
        if expect is not None:
            _, _, rk, _, _ = polar_data(eh["q"])
            if rk != expect:
                continue
        out = control_A_one(LS, U9, f, label, full)
        res, eh, Mvec, rankL, rL = out
        res["attempts"] = attempt + 1
        A.append(res); keep[label] = (f, eh, Mvec, rankL, rL)
        print(label, "rank", res["rank_B"], "|Z8|", res["Z8_size"], "deg", res["deg_1Z8"], "H2viol", res["h2_violating_L"],
              "lemma3", res["lemma3_rank4_affine_formula"], res["lemma3_rank_le2_phi_zero"], "id1viol", res["mixed_identity_1_violations"],
              "6flat", res["six_flat_check"], round(time.time() - T0, 1), flush=True)
        break
    else:
        A.append({"label": label, "note": "no instance with expected rank in 30 attempts"})
RESULT["control_A"] = A
RESULT["control_A_ranks_covered"] = sorted({r["rank_B"] for r in A if "rank_B" in r})

# N4 planted: add one extra point to Z8 of a real function (violates H2 structurally)
f, eh, Mvec, rankL, rL = keep["random_balanced_1"]
z2 = eh["z"].copy(); extra = next(c for c in range(1, 256) if z2[c] == 0 and eh["q"][c] == 0); z2[extra] = 1
prof = analyze_profile(LS, eh["q"], z2, Mvec, rankL, rL)
RESULT["N4_planted_extra_Z8_point"] = {"base": "random_balanced_1", "extra_point": int(extra), "h2_violating_L": prof["h2_violating_L"], "deg": degree(z2, 8)}
print("N4", RESULT["N4_planted_extra_Z8_point"], flush=True)

# N5 planted: odd weight (unbalanced) f -> k non-integral
f = random_balanced(); f[np.nonzero(f == 0)[0][0]] = 1
Wodd = walsh(f)
RESULT["N5_planted_odd_weight"] = {"weight": int(f.sum()), "all_W_mod4_zero": bool(np.all(Wodd % 4 == 0)), "count_W_mod4_nonzero": int(np.sum(Wodd % 4 != 0))}
print("N5", RESULT["N5_planted_odd_weight"], flush=True)

# ---------------- Control B
col = rm2_columns()
classes = [(0, "zero"), (0, "lin"), (2, "arf0"), (2, "arf1"), (2, "lin"), (4, "arf0"), (4, "arf1"), (4, "lin"),
           (6, "arf0"), (6, "arf1"), (6, "lin"), (8, "arf0"), (8, "arf1")]
B_res = []
G0 = {}
for rank, variant in classes:
    q = canonical_q(rank, variant)
    Bm, Mvec, rk, R, quad_ok = polar_data(q)
    assert rk == rank and quad_ok
    rankL, rL = restricted_rank_info(LS, Mvec)
    Aeq, beq, rankM_hist = h2_system(q, Mvec)
    g0, sysrank, inconsistent = solve_gf2(Aeq, beq)
    entry = {"rank": rank, "variant": variant, "dim_R": int(np.log2(len(R))), "q_zero_on_R": bool(all(q[r] == 0 for r in R)),
             "zero_set_size": int(np.sum(q == 0)), "rankM_histogram": rankM_hist, "system_rank": sysrank, "system_inconsistent": inconsistent}
    if inconsistent:
        B_res.append(entry); print(entry, flush=True); continue
    G0[(rank, variant)] = g0
    entry["g0_satisfies_all_equations"] = bool(np.all((np.rint(Aeq.astype(np.float32) @ g0.astype(np.float32)).astype(np.int64) % 2) == beq))
    prof0 = analyze_profile(LS, q, g0, Mvec, rankL, rL)
    entry["g0_H2_violating_L_exhaustive"] = prof0["h2_violating_L"]; entry["g0_deg"] = degree(g0, 8); entry["g0_weight"] = int(g0.sum())
    entry["lemma3_ok"] = prof0["lemma3_rank_le2_phi_zero"] and prof0["lemma3_rank4_affine_formula"] and prof0["weights_mod4_ok"]
    entry["n_L_phi_nonconstant"] = prof0["n_L_phi_nonconstant"]
    t = 0
    for c in range(256):
        if g0[c]: t ^= int(col[c])
    found = four_set_search(col, t)
    sols = []
    for Z in found:
        zz = np.zeros(256, np.uint8); zz[list(Z)] = 1
        pr = analyze_profile(LS, q, zz, Mvec, rankL, rL)
        sols.append({"Z": list(Z), "in_qzero": bool(all(q[c] == 0 for c in Z)), "linear_plane": bool(Z[3] == Z[1] ^ Z[2]),
                     "equals_R": bool(set(Z) == set(R)), "H2_violating_L_exhaustive": pr["h2_violating_L"], "deg": degree(zz, 8)})
    entry["four_sets_containing_0_in_solution_space"] = len(found)
    entry["four_sets_in_qzero"] = sum(1 for s in sols if s["in_qzero"])
    entry["solutions"] = sols
    # positive sample: random degree<=5 part added (random cubic/quartic/quintic parts)
    h = random_rm(5); g = g0 ^ h
    pr = analyze_profile(LS, q, g, Mvec, rankL, rL)
    entry["random_deg5_perturbation"] = {"deg": degree(g, 8), "H2_violating_L": pr["h2_violating_L"]}
    # negative sample: degree-7 monomial added
    h7 = random_rm(5, force_monomial=0x7F); g7 = g0 ^ h7
    pr7 = analyze_profile(LS, q, g7, Mvec, rankL, rL)
    entry["planted_deg7_perturbation"] = {"deg": degree(g7, 8), "H2_violating_L": pr7["h2_violating_L"]}
    B_res.append(entry)
    print({k: v for k, v in entry.items() if k != "solutions"}, "sols:", [(s["Z"], s["in_qzero"], s["equals_R"], s["H2_violating_L_exhaustive"]) for s in sols], round(time.time() - T0, 1), flush=True)
RESULT["control_B"] = B_res

# N2: rank-8 L-construction of packet 2 on EVERY totally singular plane
N2 = []
for variant in ("arf0", "arf1"):
    q = canonical_q(8, variant); Bm, Mvec, rk, R, _ = polar_data(q)
    planes = totally_singular_planes(q, Mvec)
    bad = 0; checked = 0
    for P in planes:
        nz = sorted(x for x in P if x)
        info = rank8_L_construction(nz[0], nz[1], Mvec, q)
        checked += 1
        if not (info["dimL5"] and info["D_in_L"] and info["radical_is_D"] and info["rankL"] == 2 and info["L_meets_Z_only_at_0"]
                and info["Z_in_four_distinct_cosets"] and info["weights_div8"]):
            bad += 1
    N2.append({"variant": variant, "totally_singular_planes": len(planes), "checked": checked, "construction_failures": bad})
    print("N2", N2[-1], round(time.time() - T0, 1), flush=True)
RESULT["N2_rank8_construction_all_planes"] = N2

# N1: rank-6 (q|R = 0): every totally singular plane Z' != R admits the packet's radical-containment witness L
N1 = []
for variant in ("arf0", "arf1"):
    q = canonical_q(6, variant); Bm, Mvec, rk, R, _ = polar_data(q)
    Rset = set(R)
    planes = [P for P in totally_singular_planes(q, Mvec) if set(P) != Rset]
    g0 = G0[(6, variant)]
    t = 0
    for c in range(256):
        if g0[c]: t ^= int(col[c])
    tR = 0
    for c in R: tR ^= int(col[c])
    sample = planes if len(planes) <= 400 else rng.sample(planes, 400)
    n_witness = 0; n_syndrome_excluded = 0
    for P in sample:
        Zset = set(P)
        s = 0
        for c in P: s ^= int(col[c])
        if s != t: n_syndrome_excluded += 1
        r = next(x for x in R if x and x not in Zset)
        L = complement_L_containing(r, Zset); Lset = set(L)
        cid = coset_table(Lset)
        nq = np.bincount(cid, weights=q.astype(np.float64), minlength=8).astype(np.int64)
        nzc = np.bincount(cid, weights=np.array([1.0 if a in Zset else 0.0 for a in range(256)]), minlength=8).astype(np.int64)
        phi = (nq // 4) & 1
        rad = [x for x in L if all(PAR8[x, Mvec[l]] == 0 for l in L)]
        ok = (len(L) == 32 and r in rad and bool(np.all(nq % 4 == 0)) and bool(np.all(phi == phi[0]))
              and sorted((nzc % 2).tolist()) == [0, 0, 0, 0, 1, 1, 1, 1])
        if ok: n_witness += 1
    N1.append({"variant": variant, "planes_other_than_R": len(planes), "sampled": len(sample), "witness_L_found": n_witness,
               "syndrome_excluded": n_syndrome_excluded, "R_in_solution_space": bool(tR == t)})
    print("N1", N1[-1], round(time.time() - T0, 1), flush=True)
RESULT["N1_rank6_other_planes_excluded"] = N1

# N3: planted cubic "q": premise n_q(A) = 0 mod 4 fails
q3 = canonical_q(8, "arf0").copy()
for c in range(256):
    if (c & 7) == 7: q3[c] ^= 1          # add x0 x1 x2
Bm3, Mvec3, rk3, R3, quad3 = polar_data(q3)
nq3 = coset_sums(LS["CID"], q3)
RESULT["N3_planted_cubic_q"] = {"deg_q": degree(q3, 8), "quadratic_allpairs": quad3,
                                "n_L_with_coset_weight_not_0_mod4": int(np.sum(np.any(nq3 % 4 != 0, axis=1))), "n_L": int(LS["NL"])}
print("N3", RESULT["N3_planted_cubic_q"], flush=True)

# 108/140 arithmetic for the rank-6, q|R=0 classes
RESULT["rank6_counts"] = [{"variant": e["variant"], "zero_set_size": e["zero_set_size"], "magnitude16_count_if_Z8_eq_R": e["zero_set_size"] - 4}
                          for e in B_res if e["rank"] == 6 and e["q_zero_on_R"]]

RESULT["elapsed_s"] = round(time.time() - T0, 1)
RESULT["clock_end"] = clock()
out = os.path.join(HERE, "reviewer-f131-controls-v1-result.json")
with open(out, "w") as fh:
    json.dump(RESULT, fh, indent=1, default=lambda o: o.tolist() if hasattr(o, "tolist") else o)
print("WROTE", out, RESULT["clock_end"])
