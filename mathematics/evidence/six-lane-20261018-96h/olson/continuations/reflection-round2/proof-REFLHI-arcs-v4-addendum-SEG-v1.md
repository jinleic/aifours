# Addendum SEG to proof-REFLHI-arcs-v4.md: optional segments, and exclusions inside p + 1 <= k <= 2p

Owner OlsonReflectionSuccessor.  Written after host clock 2026-10-19T05:57:47-0700.  Status: CANDIDATE_UNVERIFIED (written
only).  Base: proof-REFLHI-arcs-v4.md (7683eb17905ab0c9d21046f4e4a0de2fc7e868a9c394e1c874308bf4a2a77f0e) and its addendum
K2P+ (7f5b3dc598fc6e346adc1c129e228074eb4c0ca51a884c559312d50e165a383f), both unchanged.  Notation, imports, Lemmas W, 3.1,
ARC, 4.1, 4.2, BAL and Facts 2.1, 2.2 are those of v4.  New: Lemma ARC+, Lemma SEG, Theorem SEG, Corollaries SEG-p, SEG-num.

## 1. Optional segments

A **segment** is a nonempty set Sigma of consecutive blocks inside one maximal reflection run (so all runs strictly inside
Sigma are empty and consecutive blocks of Sigma have different values).  Given an arc system A (the base) and pairwise
disjoint segments Sigma_1, ..., Sigma_s, each disjoint from every base arc, and integers t_j >= 0, a **configuration**
chooses for each j an even number 2t'_j <= 2t_j of blocks c_1 < ... < c_(2t'_j) of Sigma_j (in the cyclic order of w, read
inside Sigma_j) and adds each chosen block as a single-block arc.
**Lemma ARC+.**  (i) Every configuration is an arc system with 2(m_b + sum_j t'_j) arcs (m_b = half the number of base arcs),
and its IN-gap mass E_in, hence E+, equals that of the base.  (ii) Its u-value is u_base + sum_j eps_j W_j, where u_base
ranges over the base sumset of Lemma ARC, eps_j in {+1, -1} depends only on the base gap containing Sigma_j, and
W_j = (1/2) sum_(s = 1..t'_j) (y_(c_(2s)) - y_(c_(2s-1))).  (iii) Hence, if every m in [m_b, m_b + sum_j t_j] satisfies the two
conditions of Fact 2.1 for E+ and for R - E+, all configurations share the window [-floor(E-/2), floor(E+/2)], and w has an
identity 2p-subword as soon as
   floor(E+/2) + floor(E-/2) + sum over base arcs (nu - 1) + sum_j (|U_j| - 1) >= p - 1,
where U_j := {W_j : 0 <= t'_j <= t_j, c's as above}.
Proof.  (i) Sigma_j lies inside one gap of the base system (it is a set of consecutive blocks disjoint from the base arcs and
contains no nonempty run).  Inserting 2t' arcs inside a gap splits it into 2t' + 1 sub-gaps whose labels alternate and whose
first and last sub-gaps keep the old label; every run whose label changes lies strictly inside Sigma_j and is empty (d = 0).
So E_in is unchanged.  Consecutive inserted arcs are separated by the run before the later block, so every gap still contains
a run.  (ii) Lemma 3.1 for the new system: if the base gap is IN (after X_i, before Y_i), the arcs X_i, c_1, ..., c_(2t'), Y_i
alternate X, Y, X, ..., Y, so the interval from a_i to b_i is replaced by a_i..c_1, c_2..c_3, ..., c_(2t')..b_i and u changes by
(1/2)(-y_(c_1) + y_(c_2) - ... + y_(c_(2t'))) = W; for an OUT gap the new intervals are c_1..c_2, ..., c_(2t'-1)..c_(2t') and u
changes by -W.  (iii) The window is the same for all configurations by Fact 2.1; the set of u-values contains the sumset of
the base sets and the eps_j U_j, which by (CD) has at least min(p, 1 + sum(nu - 1) + sum(|U_j| - 1)) residues; conclude as in
Lemma ARC.  []
**Lemma SEG.**  For a segment of b' blocks and t >= 0, |U| >= min(p, 1 + min(2t, b' - 1)) for U = U^(t) as above.
Proof.  Let v_1, ..., v_(b') be the values and delta_j := v_(j+1) - v_j != 0 (1 <= j <= b' - 1).  For c_1 < ... < c_(2t'),
2W = sum over J of delta_j with J = union of [c_(2s-1), c_(2s) - 1]; these t' intervals are pairwise separated (index c_(2s)
lies between the s-th and (s+1)-st), and conversely every union J of at most t maximal intervals of [1, b' - 1] arises (an
interval [x, y] corresponds to the pair c = x, c' = y + 1).  So 2U^(t) = {sum_(j in J) delta_j : J has at most t maximal
intervals}.  Induction on b'.  If t = 0 or b' = 1, |U| >= 1.  If b' = 2 and t >= 1, U contains 0 and delta_1/2.  If b' >= 3 and
t >= 1: A := {0, delta_1, delta_2, delta_1 + delta_2} (J inside {1, 2}) has >= 3 elements (if delta_1 + delta_2 = 0 it is
{0, delta_1, -delta_1}, p odd; otherwise 0, delta_1, delta_1 + delta_2 are distinct); U' := sums over J' inside [3, b' - 1]
with at most t - 1 maximal intervals has |U'| >= min(p, 1 + min(2t - 2, b' - 3)) by induction (U' = {0} if b' = 3).  For
J inside {1, 2} and such J', J u J' has at most t maximal intervals, so 2U^(t) contains A + U', and (CD) gives
|U^(t)| >= min(p, 3 + min(2t - 2, b' - 3) - 1 + 1 - 1 + ... ) = min(p, |A| + |U'| - 1) >= min(p, 1 + min(2t, b' - 1)).  []
So a segment of b' blocks used with t = ceil((b' - 1)/2) has gain |U| - 1 >= b' - 1 (its number of internal empty runs, if
< p), and every unit of t up to that value adds at least one unit of gain.

## 2. Theorem SEG

Let w be in setting (S) and suppose w avoids; let N_1, ..., N_q be its nonempty runs and M_1, ..., M_q its maximal reflection
runs (v4 Sec. 4), b_i the number of blocks of M_i, e_i = b_i - 1, g_E = sum e_i = k - q the number of empty runs.  Classes:
C = {i : b_i = 1}, AB = {i : b_i = 2}, L = {i : b_i >= 3}; n_CA := |C| + |AB|.  With d := max_j |d(N_j)|, put
   m_lo := max(1, kappa + 1 - ceil((R - d)/4)),   m_hi := p - floor((R + d)/4),   Pi_need := p - ceil(R/2).
**Theorem SEG.**  If (H1) m_hi - m_lo >= Pi_need + 1, (H2) n_CA >= 2 m_lo + 2 and (H3) g_E >= Pi_need + 1, then w does not
avoid (contradiction).  (Any B; runs need not be pure.)
Proof.  N_O := 2 m_lo + 2.  Choose O_0, a set of N_O indices in C u AB (H2).  Base arcs: for i in O_0 the single block of M_i
(i in C) or the two blocks of M_i as one arc ("pair-arc", nu = 2; i in AB).  This is an arc choice (v4 Sec. 4) with c_i = 1
exactly on O_0; let z, T be its labelling.  Lemma BAL with an index i in O_0 gives i' such that changing both parities yields
|T| <= d (no change if already).  Realise a parity change at j by: removing the base arc of M_j if j is in the current base
set; otherwise adding the single block (j in C), the pair-arc (j in AB), or the FIRST block of M_j as a singleton (j in L).
Let O be the final set of indices carrying one base arc; |O| in {N_O - 2, N_O}, so the base has m_b in {m_lo, m_lo + 1}, and
|L n O| <= 1.
Segments: for j in AB \ O, Sigma_j := M_j (b' = 2); for j in L \ O, Sigma_j := M_j (b' = b_j); for j in L n O, Sigma_j := M_j
minus its first block (b' = b_j - 1).  These are disjoint from the base arcs and from each other.  Their potential gains
(Lemma SEG with t_j = ceil((b' - 1)/2)) are 1, e_j and e_j - 1; with the base pair-arcs (gain 1 each for AB n O), the total
potential is |AB| + sum_(L) e_j - |L n O| = g_E - |L n O| >= g_E - 1 >= Pi_need (H3).  Reduce the t_j (each unit of t adds at
least one unit of gain) to the least values reaching total gain >= Pi_need; then sum t_j <= Pi_need.
Windows.  All configurations have m in [m_b, m_b + sum t_j], inside [m_lo, m_lo + 1 + Pi_need], inside [m_lo, m_hi] by (H1).
|T| <= d gives E_min >= (R - d)/2 and E_max <= (R + d)/2, so for these m: ceil(E_min/2) >= ceil((R - d)/4) >= kappa + 1 - m and
floor(E_max/2) <= floor((R + d)/4) <= p - m; Fact 2.1 gives floor-type windows on both sides, and
floor(E+/2) + floor(E-/2) >= ceil(R/2) - 1.  Lemma ARC+ (iii): ceil(R/2) - 1 + Pi_need = p - 1.  So w has an identity
2p-subword.  []

## 3. Corollaries

**Corollary SEG-p (R = p, every B).**  Let p >= 5 be prime and w a word of length 4p - 2 over D_(2p) with rotation letters in
one pair {rho_x, rho_-x}, x != 0, exactly p of them, all maximal constant reflection blocks odd, and
   (p + 1)/4 <= kappa <= (p - 3)/2.
Then w has an identity 2p-subword.
Proof.  If w avoided: v4 Sec. 4.4 gives q = p, every nonempty run one letter, d = 1, g_E = 2 kappa.  Write
r := ceil((p - 1)/4) = floor((p + 1)/4).  Pi_need = (p - 1)/2.  kappa >= (p + 1)/4 gives kappa + 1 - r >= 3/4, so
m_lo = kappa + 1 - r; m_hi = p - r; m_hi - m_lo = p - 1 - kappa >= (p + 1)/2 = Pi_need + 1 (H1) as kappa <= (p - 3)/2.  Each
L-run has >= 2 empty runs, so |L| <= kappa and n_CA >= p - kappa; (H2) needs p - kappa >= 2 kappa + 4 - 2r, which follows from
2r >= (p - 1)/2 and kappa <= (p - 3)/2.  (H3): g_E = 2 kappa >= (p + 1)/2.  Theorem SEG.  []
**Corollary SEG-num (every R).**  Let w be as in Theorem K2P+ (length 4p - 2, rotations in one pair, all blocks odd), put
delta := R - p.  If
   delta >= 0   and   (p + 3 delta + 2)/4 <= kappa <= (p - delta - 4)/2,
then w has an identity 2p-subword.  (If delta < 0, w has one by Fact 2.2.)
Proof.  Suppose w avoids.  Fact 2.2: d <= 2 delta + 1, so floor(d/2) <= delta, and q >= 2p - R = p - delta.
(H1): m_hi - m_lo >= p - 1 - kappa - floor(d/2) >= p - 1 - kappa - delta (also when m_lo = 1 is the max: then m_hi - m_lo
is larger); Pi_need + 1 = p + 1 - ceil(R/2) <= p + 1 - (p + delta)/2; so (H1) follows from kappa <= (p - delta - 4)/2.
(H3): g_E = k - q >= k - R = p - delta + 2 kappa - (p + delta) = 2 kappa - 2 delta + ... ; precisely k = 2p - R + 2 kappa =
p - delta + 2 kappa and q <= R, so g_E >= 2 kappa - 2 delta + (p - delta) - (p + delta) + 2 delta ... = k - R = 2 kappa - 2 delta;
(H3) needs 2 kappa - 2 delta >= p - ceil(R/2) + 1, implied by 2 kappa >= 2 delta + (p - delta)/2 + 1, i.e.
kappa >= (p + 3 delta + 2)/4.
(H2): |L| <= (g_E - |AB|)/2 <= (k - q)/2, so n_CA = q - |L| >= (3q - k)/2 >= (3(p - delta) - k)/2 = (2p - 2 delta - 2 kappa)/2
= p - delta - kappa.  m_lo <= max(1, kappa + 1 - (R - d)/4) <= max(1, kappa + 1 - (p - delta - 1)/4) (as R - d >= p + delta -
2 delta - 1).  (H2) holds if p - delta - kappa >= 2 kappa + 4 - (p - delta - 1)/2 and p - delta - kappa >= 4; the first is
3 kappa <= (3p - 3 delta - 9)/2, i.e. kappa <= (p - delta - 3)/2, implied by the hypothesis; the second follows from
kappa <= (p - delta - 4)/2 and p - delta >= 10 (the range is nonempty only if 5 delta <= p - 10).  Theorem SEG.  []
Arithmetic of the (H3) line, restated cleanly: g_E >= k - R = (2p - R + 2 kappa) - R = 2 kappa - 2 delta, and
p - ceil(R/2) + 1 <= p - (p + delta)/2 + 1 = (p - delta)/2 + 1.

Ranges.  SEG-num is nonempty iff 5 delta <= p - 10.  In (kappa, k): k = p - delta + 2 kappa, so for delta = 0 it gives
(p + 2)/4 <= kappa <= (p - 4)/2, i.e. 3p/2 + 1 <= k <= 2p - 4 (SEG-p is the sharper R = p form); in general the covered k lie
between (3p - delta + 2)/2 + ... and 2p - 2 delta - 4.  All these cells have k >= p + 1 when kappa >= (delta + 1)/2.

## 4. Updated map of RES-HI(p) after v4 + K2P+ + SEG (all CANDIDATE)

Excluded (any B, all-odd words with rotations in one pair):
* k >= max(2p + 1, 3 kappa + 3)  (K2P+);
* R = p: (p + 1)/4 <= kappa <= (p - 3)/2 (SEG-p) and (p + 1)/2 <= kappa <= p - 3 (K2P+); FP-1 under its diversity condition;
* R = p + delta, 0 <= 5 delta <= p - 10: (p + 3 delta + 2)/4 <= kappa <= (p - delta - 4)/2 (SEG-num).
Remaining (besides the accepted B = 0 CJ''''/EDGE/REFL-B0 coverage, which applies only to B = 0):
* R = p: kappa < (p + 1)/4 (where 2 kappa empty runs cannot supply (p - 1)/2 units: an arc-method limit), kappa = (p - 1)/2,
  kappa in {p - 2, p - 1};
* R > p outside SEG-num and K2P+: notably large delta (big runs, d large) and small H.
Arc-method limit (proved inside Theorem SEG's accounting, not an obstruction to REFL): every arc/segment configuration has
gain at most g_E, so the method needs g_E >= Pi_need, i.e. roughly k >= p + R/2; below that, other pattern families are needed.
