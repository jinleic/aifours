#!/usr/bin/env python3
"""f140 reviewer: independent exact Q(sqrt2) checks for candidate 1 (explicit H(x)Q/Pi_A source: PPT, core, range
identities, Alice-row support) and candidate 2 (printed arXiv:2402.12966v1 HTML Eq.36 list: Bob-PT principal block,
test vector, exact mismatch count against the explicit source under the paper's stated relabeling).

INDEPENDENCE: nothing here imports, reads, executes or copies the author checkers. The explicit source is rebuilt from
the prose definition in the candidate-1 packet ('explicit_source'); the printed list is the reviewer's own transcription
of the HTML rendering of Eq.36 / Fig.5 caption (https://arxiv.org/html/2402.12966v1, read 2026-10-29T03:36Z).
Arithmetic: elements of Q(sqrt2) as (p, q) = p + q*sqrt(2) with p, q fractions.Fraction. No floating point anywhere.
Positivity: exact symmetric Gaussian elimination (LDL^T without pivoting is valid for PSD testing over an ordered field:
M is PSD iff every pivot is >= 0, every zero pivot has a zero row, and each Schur complement is PSD).
"""
import hashlib, json, os, sys, time
from fractions import Fraction as F

# ---------------------------------------------------------------- Q(sqrt2) --------------------------------------------
def E(p, q=0): return (F(p), F(q))
ZERO, ONE, SQ2 = E(0), E(1), E(0, 1)
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def neg(x): return (-x[0], -x[1])
def mul(x, y): return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def inv(x):
    d = x[0] * x[0] - 2 * x[1] * x[1]
    if d == 0: raise ZeroDivisionError('zero element of Q(sqrt2)')
    return (x[0] / d, -x[1] / d)
def div(x, y): return mul(x, inv(y))
def iszero(x): return x[0] == 0 and x[1] == 0
def sign(x):
    p, q = x
    if p == 0 and q == 0: return 0
    if p >= 0 and q >= 0: return 1
    if p <= 0 and q <= 0: return -1
    if p > 0: return 1 if p * p > 2 * q * q else -1      # q < 0
    return 1 if 2 * q * q > p * p else -1                # p < 0 < q
def fmt(x):
    p, q = x
    if q == 0: return str(p)
    if p == 0: return f'{q}*sqrt2'
    return f'{p}{"+" if q > 0 else ""}{q}*sqrt2'

# ---------------------------------------------------------------- matrices --------------------------------------------
def zeros(n, m=None): return [[ZERO] * (m if m is not None else n) for _ in range(n)]
def outer_add(M, v):
    nz = [i for i in range(len(v)) if not iszero(v[i])]
    for i in nz:
        for j in nz:
            M[i][j] = add(M[i][j], mul(v[i], v[j]))      # all vectors are real, so no conjugation is needed
def gram_sum(vectors, n):
    M = zeros(n)
    for v in vectors: outer_add(M, v)
    return M
def trace(M):
    t = ZERO
    for i in range(len(M)): t = add(t, M[i][i])
    return t
def equal(A, B): return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def count_diff(A, B): return sum(1 for i in range(len(A)) for j in range(len(A[0])) if A[i][j] != B[i][j])
def symmetric(M): return all(M[i][j] == M[j][i] for i in range(len(M)) for j in range(len(M)))
def pt_bob(M, dA, dB):
    """Partial transpose on Bob: <a,b|M^G|a',b'> = <a,b'|M|a',b>."""
    T = zeros(dA * dB)
    for a in range(dA):
        for b in range(dB):
            for a2 in range(dA):
                for b2 in range(dB):
                    T[a * dB + b][a2 * dB + b2] = M[a * dB + b2][a2 * dB + b]
    return T
def psd_ldl(M):
    """Exact PSD test for a symmetric matrix. Returns (is_psd, rank_or_partial, witness)."""
    n = len(M); A = [row[:] for row in M]; rank = 0
    for k in range(n):
        piv = A[k][k]; s = sign(piv)
        if s < 0: return (False, rank, {'kind': 'negative_pivot', 'index': k, 'pivot': fmt(piv)})
        if s == 0:
            for j in range(k + 1, n):
                if not iszero(A[k][j]):
                    return (False, rank, {'kind': 'zero_pivot_nonzero_row', 'index': k, 'col': j, 'entry': fmt(A[k][j])})
            continue
        rank += 1
        for i in range(k + 1, n):
            if iszero(A[i][k]): continue
            f = div(A[i][k], piv)
            for j in range(k + 1, n):
                if not iszero(A[k][j]): A[i][j] = sub(A[i][j], mul(f, A[k][j]))
    return (True, rank, None)
def rank_general(rows):
    """Rank of a list of row vectors over Q(sqrt2) (Gaussian elimination with pivot search)."""
    A = [r[:] for r in rows]; n = len(A)
    if n == 0: return 0
    m = len(A[0]); r = 0
    for c in range(m):
        p = next((i for i in range(r, n) if not iszero(A[i][c])), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        pinv = inv(A[r][c])
        for i in range(n):
            if i != r and not iszero(A[i][c]):
                f = mul(A[i][c], pinv)
                A[i] = [sub(A[i][j], mul(f, A[r][j])) for j in range(m)]
        r += 1
        if r == n: break
    return r
def matvec(M, v):
    out = []
    for i in range(len(M)):
        s = ZERO
        for j in range(len(v)):
            if not iszero(v[j]) and not iszero(M[i][j]): s = add(s, mul(M[i][j], v[j]))
        out.append(s)
    return out
def dot(u, v):
    s = ZERO
    for a, b in zip(u, v): s = add(s, mul(a, b))
    return s
def coeff_matrix(v, dA, dB): return [[v[a * dB + b] for b in range(dB)] for a in range(dA)]
def schmidt_rank(v, dA, dB): return rank_general(coeff_matrix(v, dA, dB))
def vec(n, terms):
    """terms: list of (index, coefficient)."""
    v = [ZERO] * n
    for i, c in terms: v[i] = add(v[i], c)
    return v

# --------------------------------------------------- definitions (from the packet prose) -----------------------------
# Horodecki 2x4 kets, |a b> -> 4a+b. H = [|00>]+[|01>+|10>]+[|03>+|12>]+[|02>+|11>]+[sqrt2|13>+|10>]
H_KETS = [
    [((0, 0), ONE)],
    [((0, 1), ONE), ((1, 0), ONE)],
    [((0, 3), ONE), ((1, 2), ONE)],
    [((0, 2), ONE), ((1, 1), ONE)],
    [((1, 3), SQ2), ((1, 0), ONE)],
]
# crosshatch 3x3 kets, |a b> -> 3a+b. Q = [|10>+|02>]+[|20>+|12>]+[|00>+|21>]+[|01>+|22>]
Q_KETS = [
    [((1, 0), ONE), ((0, 2), ONE)],
    [((2, 0), ONE), ((1, 2), ONE)],
    [((0, 0), ONE), ((2, 1), ONE)],
    [((0, 1), ONE), ((2, 2), ONE)],
]
AUTHOR_ALICE = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 1): 3}        # retained (a_H,a_Q) rows, packet ordering
PAPER_ALICE = {(0, 0): 0, (0, 1): 1, (1, 1): 2, (0, 2): 3}         # paper relabeling {|00>,|01>,|11>,|02>} -> 0..3
def author_bob(bH, bQ): return 3 * bH + bQ                           # packet: Bob index 3*b_H + b_Q
def paper_bob(bH, bQ): return bH + 4 * bQ                            # paper: |ij>_{B1B2} -> |i+4j>

def source_kets(alice_map, bob_map, h_kets=H_KETS, q_kets=Q_KETS):
    """The 20 kets (Pi_A (x) 1)(|h_k> (x) |q_l>) in the regrouped 4x12 coordinates. Order: k major, l minor."""
    out = []
    for h in h_kets:
        for q in q_kets:
            v = [ZERO] * 48
            for (aH, bH), c1 in h:
                for (aQ, bQ), c2 in q:
                    if (aH, aQ) in alice_map:
                        i = 12 * alice_map[(aH, aQ)] + bob_map(bH, bQ)
                        v[i] = add(v[i], mul(c1, c2))
            out.append(v)
    return out

def build_small(kets, dA, dB):
    return [vec(dA * dB, [((a * dB + b), c) for (a, b), c in k]) for k in kets]

# ------------------------------------------------ printed list (reviewer transcription) ------------------------------
def printed_kets():
    """Reviewer transcription of arXiv:2402.12966v1 HTML Eq.36 (= Fig.5 caption list), 4x12, |a,b> -> 12a+b."""
    K = []
    K.append([((2, 0), SQ2), ((2, 3), ONE)])                                   # s~  = sqrt2|2,0>+|2,3>
    K.append([((2, 8), SQ2), ((2, 11), ONE)])                                  # s~' = sqrt2|2,8>+|2,11>
    for i in range(3): K.append([((0, 9 + i), ONE), ((1, i), ONE), ((2, 1 + i), ONE)])   # h_i
    K.append([((0, 1), ONE), ((3, 8), ONE)])                                   # h_3
    for i in range(3): K.append([((1, 9 + i), ONE), ((2, 8 + i), ONE), ((3, 1 + i), ONE)])  # r_i
    K.append([((0, 3), ONE), ((1, 8), ONE)])                                   # r_3
    for i in range(8): K.append([((0, 4 + i), ONE), ((3, i), ONE)])            # q_i
    return K
PRINTED_NAMES = ['s~', "s~'", 'h_0', 'h_1', 'h_2', 'h_3', 'r_0', 'r_1', 'r_2', 'r_3'] + [f'q_{i}' for i in range(8)]

def ket_str(v, dB):
    parts = []
    for i, c in enumerate(v):
        if not iszero(c):
            a, b = divmod(i, dB)
            parts.append(f'{fmt(c) if c != ONE else ""}|{a},{b}>')
    return ' + '.join(parts) if parts else '0'

# ---------------------------------------------------------------- main -------------------------------------------------
def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f: h.update(f.read())
    return h.hexdigest()

def main(out_path):
    R = {'reviewer': 'f140 (same-harness reviewer)', 'script_sha256_self': sha256_file(os.path.abspath(__file__)),
         'utc_start': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'coefficient_field': 'Q(sqrt2) exact',
         'author_code_executed_or_imported': False}
    checks = {}

    # ---------- H (2x4) ----------
    Hv = build_small(H_KETS, 2, 4)
    H = gram_sum(Hv, 8)
    HG = pt_bob(H, 2, 4)
    checks['H_symmetric'] = symmetric(H) and symmetric(HG)
    psdH, rkH, _ = psd_ldl(H); psdHG, rkHG, wHG = psd_ldl(HG)
    checks['H_psd'] = psdH; checks['H_rank'] = rkH
    checks['H_PT_psd'] = psdHG; checks['H_PT_rank'] = rkHG
    checks['H_trace'] = fmt(trace(H))
    checks['H_ket_rank_independent'] = rank_general(Hv)
    # stated kernel vectors of H^Gamma
    k1 = vec(8, [(0, E(-1)), (5, ONE)])                      # -|00> + |11>
    k2 = vec(8, [(1, E(-1)), (6, ONE)])                      # -|01> + |12>
    k3 = vec(8, [(2, E(-1)), (4, (F(0), F(-1, 2))), (7, ONE)])   # -|02> - (1/sqrt2)|10> + |13>   (1/sqrt2 = (1/2)sqrt2)
    kern = [k1, k2, k3]
    checks['H_PT_kernel_vectors_annihilated'] = [all(iszero(x) for x in matvec(HG, k)) for k in kern]
    checks['H_PT_kernel_vectors_rank'] = rank_general(kern)
    checks['H_PT_kernel_dim_is_3'] = (8 - rkHG == 3)
    # range parametrization [[a,b,d,c],[b+e,d,c,sqrt2 e]]: basis kets give the coefficient matrices of a,b,c,d,e
    cm = [coeff_matrix(v, 2, 4) for v in Hv]
    param_ok = (cm[0] == [[ONE, ZERO, ZERO, ZERO], [ZERO] * 4] and
                cm[1] == [[ZERO, ONE, ZERO, ZERO], [ONE, ZERO, ZERO, ZERO]] and
                cm[2] == [[ZERO, ZERO, ZERO, ONE], [ZERO, ZERO, ONE, ZERO]] and
                cm[3] == [[ZERO, ZERO, ONE, ZERO], [ZERO, ONE, ZERO, ZERO]] and
                cm[4] == [[ZERO] * 4, [ONE, ZERO, ZERO, SQ2]])
    checks['H_range_parametrization_matches_[[a,b,d,c],[b+e,d,c,sqrt2e]]'] = param_ok
    # product-vector family (b=1): X(t) = (|0>+t|1>) (x) (a|0>+|1>+t|2>+t^2|3>), a = 1/t + t^2/sqrt2; verify X(t) in ran H
    # (i.e. the five parameters a,b,c,d,e read off X(t) satisfy the range form) for rational sample t; this is the
    # algebraic identity used in the written proof, checked at 12 points (Laurent-polynomial identities of degree <= 6).
    fam_ok = True; fam_pts = []
    for tt in [F(1), F(-1), F(2), F(-2), F(1, 2), F(-1, 3), F(3), F(5, 7), F(-7, 2), F(4), F(-9), F(11, 5)]:
        t = E(tt); a = add(inv(t), mul(mul(t, t), inv(SQ2)))
        row0 = [a, ONE, t, mul(t, t)]
        row1 = [mul(t, x) for x in row0]
        X = [row0, row1]
        # read parameters: a=X00, b=X01, d=X02, c=X03, e = X13/sqrt2; range form requires X10 = b+e, X11 = d, X12 = c
        bb, dd, cc = X[0][1], X[0][2], X[0][3]; ee = div(X[1][3], SQ2)
        ok = (X[1][0] == add(bb, ee) and X[1][1] == dd and X[1][2] == cc)
        # kernel conditions for the Bob-conjugated vector with t real (conj = identity): k2 forces t^2 = 1
        fam_ok &= ok; fam_pts.append(str(tt))
    checks['product_family_in_range_identity_sample_points'] = {'ok': fam_ok, 'points': fam_pts}
    # the two explicit product vectors: |1>(x)(|0>+sqrt2|3>) = h_4 and |00>: their (real) partial conjugates vs ran H^Gamma
    h4 = Hv[4]; e00 = Hv[0]
    checks['h4_is_product_vector_in_ranH'] = (schmidt_rank(h4, 2, 4) == 1)
    checks['h4_partialconj_orthogonal_to_kernel_H_PT'] = [fmt(dot(k, h4)) for k in kern]
    checks['e00_partialconj_orthogonal_to_kernel_H_PT'] = [fmt(dot(k, e00)) for k in kern]

    # ---------- Q (3x3) ----------
    Qv = build_small(Q_KETS, 3, 3)
    Q = gram_sum(Qv, 9); QG = pt_bob(Q, 3, 3)
    psdQ, rkQ, _ = psd_ldl(Q); psdQG, rkQG, _ = psd_ldl(QG)
    checks['Q_psd'] = psdQ; checks['Q_rank'] = rkQ; checks['Q_PT_psd'] = psdQG; checks['Q_PT_rank'] = rkQG
    flipped = [[((1, 2), ONE), ((0, 0), ONE)], [((2, 2), ONE), ((1, 0), ONE)], [((0, 1), ONE), ((2, 0), ONE)], [((0, 2), ONE), ((2, 1), ONE)]]
    checks['Q_PT_equals_sum_of_four_flipped_edge_projectors'] = equal(QG, gram_sum(build_small(flipped, 3, 3), 9))
    checks['Q_trace'] = fmt(trace(Q))

    # ---------- explicit source R (author coordinates) ----------
    S = source_kets(AUTHOR_ALICE, author_bob)
    Rm = gram_sum(S, 48)
    checks['R_trace'] = fmt(trace(Rm))
    checks['R_rank'] = rank_general(S)
    psdR, rkR, _ = psd_ldl(Rm)
    RG = pt_bob(Rm, 4, 12)
    psdRG, rkRG, wRG = psd_ldl(RG)
    checks['R_psd'] = psdR; checks['R_rank_ldl'] = rkR
    checks['R_PT_psd_direct_48x48_exact'] = psdRG; checks['R_PT_rank'] = rkRG; checks['R_PT_witness'] = wRG
    # core: Alice rows 1,3 ; Bob columns J=(0,3,6,9) ; compare to H with row1->a_H=0, row3->a_H=1
    J = (0, 3, 6, 9)
    core_idx = [12 * a + b for a in (1, 3) for b in J]
    core = [[Rm[i][j] for j in core_idx] for i in core_idx]
    checks['core_R_equals_H_64_entries'] = equal(core, H)
    # range identities on all 20 kets
    id1 = all(iszero(v[12 * 1 + j]) and iszero(v[12 * 3 + j]) for v in S for j in (1, 4, 7, 10))
    id2 = all(v[12 * 2 + j] == v[12 * 0 + (j - 1)] for v in S for j in (1, 4, 7, 10))
    id3 = all(v[12 * 1 + j] == v[12 * 0 + (j + 2)] for v in S for j in J)
    checks['range_identity_rows1_3_vanish_at_Jplus1'] = id1
    checks['range_identity_row2_at_Jplus1_equals_row0_at_J'] = id2
    checks['range_identity_row1_at_J_equals_row0_at_Jplus2'] = id3
    # Alice-row support and Schmidt rank of each source ket; consistency with lemma (SR<=2 => core rank<=1)
    supports = []; srs = []; lemma_consistent = True
    for v in S:
        rows = sorted({i for i in range(4) if any(not iszero(v[12 * i + j]) for j in range(12))})
        supports.append(len(rows)); sr = schmidt_rank(v, 4, 12); srs.append(sr)
        core_rk = rank_general([[v[12 * a + b] for b in J] for a in (1, 3)])
        if sr <= 2 and core_rk > 1: lemma_consistent = False
    checks['source_ket_alice_row_counts'] = supports
    checks['all_source_kets_at_most_three_alice_rows'] = max(supports) <= 3
    checks['source_ket_schmidt_ranks'] = srs
    checks['lemma_consistency_on_source_kets'] = lemma_consistent
    checks['R_kets_nonzero'] = all(any(not iszero(x) for x in v) for v in S)

    # ---------- printed list P (paper coordinates) ----------
    Pk = printed_kets()
    Pv = build_small(Pk, 4, 12)
    P = gram_sum(Pv, 48)
    checks['printed_ket_count'] = len(Pv)
    checks['P_trace'] = fmt(trace(P))
    PG = pt_bob(P, 4, 12)
    i00, i19 = 0, 12 * 1 + 9
    block = [[fmt(PG[i00][i00]), fmt(PG[i00][i19])], [fmt(PG[i19][i00]), fmt(PG[i19][i19])]]
    checks['P_PT_principal_block_|0,0>,|1,9>'] = block
    tv = vec(48, [(i00, ONE), (i19, E(-1))])
    checks['P_PT_test_vector_|0,0>-|1,9>_value'] = fmt(dot(tv, matvec(PG, tv)))
    psdP, rkP, _ = psd_ldl(P); psdPG, rkPG, wPG = psd_ldl(PG)
    checks['P_psd'] = psdP; checks['P_rank'] = rkP
    checks['P_PT_psd_direct_48x48_exact'] = psdPG; checks['P_PT_witness'] = wPG
    checks['P_kets_containing_|0,0>'] = [PRINTED_NAMES[n] for n, v in enumerate(Pv) if not iszero(v[i00])]
    checks['P_kets_containing_|0,9>_and_|1,0>'] = [PRINTED_NAMES[n] for n, v in enumerate(Pv) if not iszero(v[9]) and not iszero(v[12])]
    checks['P_kets_containing_|1,9>'] = [PRINTED_NAMES[n] for n, v in enumerate(Pv) if not iszero(v[i19])]

    # ---------- mismatch: R in paper coordinates vs P ----------
    Sp = source_kets(PAPER_ALICE, paper_bob)
    Rp = gram_sum(Sp, 48)
    checks['R_paper_trace'] = fmt(trace(Rp))
    checks['R_paper_vs_P_unequal_entries'] = count_diff(Rp, P)
    checks['R_paper_|0,9>_diagonal'] = fmt(Rp[9][9]); checks['P_|0,9>_diagonal'] = fmt(P[9][9])
    checks['R_paper_PT_psd'] = psd_ldl(pt_bob(Rp, 4, 12))[0]
    checks['R_paper_rank'] = rank_general(Sp)
    diag_diffs = [(divmod(i, 12), fmt(Rp[i][i]), fmt(P[i][i])) for i in range(48) if Rp[i][i] != P[i][i]]
    checks['R_paper_vs_P_diagonal_differences_(a,b),R,P'] = [[list(d[0]), d[1], d[2]] for d in diag_diffs]
    checks['R_paper_kets_(k=H index, l=Q index)'] = [f'h{k}(x)q{l}: ' + ket_str(Sp[4 * k + l], 12) for k in range(5) for l in range(4)]
    checks['P_kets_transcribed'] = [f'{PRINTED_NAMES[n]}: ' + ket_str(v, 12) for n, v in enumerate(Pv)]
    # documentary: Eq.(37)-style compression (Alice {1,2} x Bob {0..3}) of R_paper and of P against H
    comp_idx = [12 * a + b for a in (1, 2) for b in range(4)]
    compR = [[Rp[i][j] for j in comp_idx] for i in comp_idx]
    compP = [[P[i][j] for j in comp_idx] for i in comp_idx]
    checks['documentary_compression_R_paper_equals_H'] = equal(compR, H)
    lam = None
    for i in range(8):
        for j in range(8):
            if not iszero(H[i][j]):
                lam = div(compP[i][j], H[i][j]); break
        if lam is not None: break
    prop = lam is not None and all(compP[i][j] == mul(lam, H[i][j]) for i in range(8) for j in range(8))
    checks['documentary_compression_P_proportional_to_H'] = prop
    checks['documentary_compression_P_trace'] = fmt(trace(compP))

    # ---------- mutation controls ----------
    mut = {}
    # M1: alter one H ket: sqrt2|13>+|10>  ->  sqrt2|13>+|00>
    H_mut = [k[:] for k in H_KETS]; H_mut[4] = [((1, 3), SQ2), ((0, 0), ONE)]
    Hm = gram_sum(build_small(H_mut, 2, 4), 8); HmG = pt_bob(Hm, 2, 4)
    psdHm, rkHm, wHm = psd_ldl(HmG)
    mut['M1_altered_H_ket'] = {'ket': 'sqrt2|1,3>+|0,0> replaces sqrt2|1,3>+|1,0>',
                               'H_PT_psd': psdHm, 'H_PT_rank_or_partial': rkHm, 'H_PT_witness': wHm,
                               'stated_kernel_vectors_still_annihilated': [all(iszero(x) for x in matvec(HmG, k)) for k in kern],
                               'core_of_mutated_source_equals_original_H': None}
    Sm = source_kets(AUTHOR_ALICE, author_bob, h_kets=H_mut)
    Rmm = gram_sum(Sm, 48)
    mut['M1_altered_H_ket']['core_of_mutated_source_equals_original_H'] = equal([[Rmm[i][j] for j in core_idx] for i in core_idx], H)
    mut['M1_altered_H_ket']['mutated_source_PT_psd'] = psd_ldl(pt_bob(Rmm, 4, 12))[0]
    # M2: alter one source ket in place: swap Bob columns 0 and 1 in ket h1(x)q0 (index 4*1+0=4)
    S2 = [v[:] for v in S]
    v = S2[4]
    for a in range(4): v[12 * a + 0], v[12 * a + 1] = v[12 * a + 1], v[12 * a + 0]
    mut['M2_altered_source_ket'] = {'ket_index': 4, 'mutation': 'swap Bob columns 0 and 1 in ket h1(x)q0',
                                    'identity_rows1_3_vanish_at_Jplus1': all(iszero(w[12 * 1 + j]) and iszero(w[12 * 3 + j]) for w in S2 for j in (1, 4, 7, 10)),
                                    'core_equals_H': None}
    R2 = gram_sum(S2, 48)
    mut['M2_altered_source_ket']['core_equals_H'] = equal([[R2[i][j] for j in core_idx] for i in core_idx], H)
    mut['M2_altered_source_ket']['mutated_R_PT_psd'] = psd_ldl(pt_bob(R2, 4, 12))[0]
    # M3: alter one printed ket: delete |0,9> from h_0
    Pk3 = [k[:] for k in Pk]; Pk3[2] = [((1, 0), ONE), ((2, 1), ONE)]
    P3 = gram_sum(build_small(Pk3, 4, 12), 48); P3G = pt_bob(P3, 4, 12)
    mut['M3_altered_printed_ket'] = {'mutation': 'h_0 -> |1,0>+|2,1> (|0,9> deleted)',
                                     'block_|0,0>,|1,9>': [[fmt(P3G[i00][i00]), fmt(P3G[i00][i19])], [fmt(P3G[i19][i00]), fmt(P3G[i19][i19])]],
                                     'test_vector_value': fmt(dot(tv, matvec(P3G, tv))),
                                     'mutated_P_PT_psd': psd_ldl(P3G)[0], 'mutated_P_PT_witness': psd_ldl(P3G)[2],
                                     'mismatch_vs_R_paper': count_diff(P3, Rp)}
    # positive / negative controls for the PSD routine
    bell = vec(4, [(0, ONE), (3, ONE)])
    B = gram_sum([bell], 4); BG = pt_bob(B, 2, 2)
    mut['control_bell_PT_not_psd'] = {'psd': psd_ldl(BG)[0], 'witness': psd_ldl(BG)[2]}
    sep = gram_sum([vec(4, [(0, ONE)]), vec(4, [(3, ONE)]), vec(4, [(1, ONE), (2, ONE)])], 4)
    mut['control_separable_2x2_PT_psd'] = psd_ldl(pt_bob(sep, 2, 2))[0]
    mut['control_PPT_positive_R_PT_psd'] = psdRG
    mut['control_PPT_positive_Q_PT_psd'] = psdQG
    mut['control_PPT_positive_H_PT_psd'] = psdHG
    # sign() self-test on mixed-sign elements
    mut['sign_selftest'] = [sign(E(3, -2)) == 1, sign(E(2, -2)) == -1, sign(E(-1, 1)) == 1, sign(E(-3, 2)) == -1, sign(E(-7, 5)) == 1, sign(E(-10, 7)) == -1]

    R['checks'] = checks; R['mutation_controls'] = mut
    R['utc_end'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with open(out_path, 'w') as f:
        json.dump(R, f, indent=1, default=str); f.write('\n')
    print(json.dumps(R, indent=1, default=str))

if __name__ == '__main__':
    main(sys.argv[1])
