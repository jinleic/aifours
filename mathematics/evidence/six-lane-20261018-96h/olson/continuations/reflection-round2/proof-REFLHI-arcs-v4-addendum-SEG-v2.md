# Addendum SEG (v2) to proof-REFLHI-arcs-v4.md: optional segments and exclusions inside p + 1 <= k <= 2p

Owner OlsonReflectionSuccessor.  Written after host clock 2026-10-19T05:59:22-0700.  Status: CANDIDATE_UNVERIFIED (written
only; no computation).  Supersedes the unsent v1 of this addendum (e43f39ac...98b1, kept unchanged; two of its displayed
computations are garbled; the mathematics is the same).  Base: proof-REFLHI-arcs-v4.md
(7683eb17905ab0c9d21046f4e4a0de2fc7e868a9c394e1c874308bf4a2a77f0e) and addendum K2P+ (7f5b3dc5...383f), unchanged.
Notation, imports, Lemmas W, 3.1, ARC, 4.1, 4.2, BAL and Facts 2.1, 2.2 are those of v4.

## 1. Optional segments

A **segment** is a nonempty set Sigma of consecutive blocks inside one maximal reflection run (runs strictly inside Sigma are
empty; consecutive blocks of Sigma have different values).  Given a base arc system and pairwise disjoint segments
Sigma_1, ..., Sigma_s disjoint from all base arcs, and integers t_j >= 0, a **configuration** chooses for every j some blocks
c_1 < ... < c_(2t'_j) of Sigma_j (in the cyclic order of w, inside Sigma_j), 0 <= t'_j <= t_j, and adds each as a
single-block arc.
**Lemma ARC+.**  (i) Every configuration is an arc system with 2(m_b + sum_j t'_j) arcs (2 m_b = number of base arcs), and its
E+ equals that of the base.  (ii) Its u-value is u_base + sum_j eps_j W_j, where u_base ranges over the base sumset of Lemma
ARC, eps_j in {+1, -1} depends only on the base gap containing Sigma_j, and W_j := (1/2) sum_(s=1..t'_j)
(y_(c_(2s)) - y_(c_(2s-1))).  (iii) If every m in [m_b, m_b + sum_j t_j] satisfies the conditions of Fact 2.1 for E+ and for
E- = R - E+, and
   floor(E+/2) + floor(E-/2) + sum over base arcs of (nu - 1) + sum_j (|U_j| - 1) >= p - 1,
with U_j := the set of all values W_j (all admissible choices in Sigma_j), then w has an identity 2p-subword.
Proof.  (i) Sigma_j contains no nonempty run and meets no base arc, so it lies inside one gap of the base system.  Inserting
2t' single-block arcs into a gap splits it into 2t' + 1 sub-gaps with alternating labels, the first and the last keeping the
old label; every run whose label changes lies strictly inside Sigma_j and is empty (d = 0), so E_in is unchanged.  Each new
gap contains the run just after its arc, so the result is an arc system.  (ii) If the base gap lies after X_i (IN), the arcs
read X_i, c_1, ..., c_(2t'), Y_i with alternating roles X, Y, ..., X, Y; the interval a_i..b_i of Lemma 3.1 becomes
a_i..c_1, c_2..c_3, ..., c_(2t')..b_i, which adds t' intervals and changes u by
(1/2)(-y_(c_1) + y_(c_2) - ... + y_(c_(2t'))) = W.  If the base gap lies after Y_i (OUT), the arcs read Y_i, c_1, ..., c_(2t'),
X_(i+1) and the new intervals are c_1..c_2, ..., c_(2t'-1)..c_(2t'): t' new intervals and the change -W.  (iii) By Fact 2.1 all
configurations have the window [-floor(E-/2), floor(E+/2)].  Their u-values contain the sumset of the base sets (1/2)V(X_i),
-(1/2)V(Y_i) and the sets eps_j U_j, which by (CD) has at least min(p, 1 + sum(nu - 1) + sum(|U_j| - 1)) residues; the window
has min(p, floor(E+/2) + floor(E-/2) + 1).  The sizes add up to at least p + 1; Lemma W.  []
**Lemma SEG.**  If Sigma has b' blocks, then |U| >= min(p, 1 + min(2t, b' - 1)) for U = the set of values W with t' <= t.
Proof.  Let v_1, ..., v_(b') be the values and delta_j := v_(j+1) - v_j != 0.  For c_1 < ... < c_(2t'),
2W = sum over j in J of delta_j with J = union over s of [c_(2s-1), c_(2s) - 1]; these t' intervals are pairwise separated
(c_(2s) lies between the s-th and the (s+1)-st).  Conversely a set J with at most t maximal intervals [x_s, x'_s] arises from
c = (x_1, x'_1 + 1, x_2, x'_2 + 1, ...).  So 2U = {sum_(j in J) delta_j : J in [1, b' - 1] with at most t maximal intervals}.
Induction on b'.  If t = 0 or b' = 1: |U| >= 1.  If b' = 2 and t >= 1: U contains 0 and delta_1/2 != 0.  If b' >= 3 and t >= 1:
A := {0, delta_1, delta_2, delta_1 + delta_2} has at least 3 elements (if delta_1 + delta_2 = 0 it is {0, delta_1, -delta_1};
otherwise 0, delta_1, delta_1 + delta_2 are distinct).  Let U'' be the set of sums over J'' in [3, b' - 1] with at most t - 1
maximal intervals; by induction (applied to the segment of blocks 3..b') |U''| >= min(p, 1 + min(2t - 2, b' - 3)).  For J in
{1, 2} with at most one interval and such J'', J u J'' has at most t maximal intervals, so 2U contains A + U''.  By (CD),
|U| >= min(p, |A| + |U''| - 1) >= min(p, 3 + min(2t - 2, b' - 3) - 1 + 1) - ... ; explicitly |A| + |U''| - 1 >=
3 + (1 + min(2t - 2, b' - 3)) - 1 = 1 + min(2t, b' - 1).  []
Consequences.  With t = ceil((b' - 1)/2) the gain |U| - 1 is at least b' - 1 (the number of empty runs inside Sigma), unless
the cap p is reached; raising t by one (while 2t < b' - 1 + 1) raises the guaranteed gain by at least one.

## 2. Theorem SEG

Let w be in setting (S), suppose w avoids, and use v4 Sec. 4: nonempty runs N_1, ..., N_q, maximal reflection runs
M_1, ..., M_q, b_i blocks in M_i, e_i = b_i - 1, g_E = sum e_i = k - q the number of empty runs, d = max_j |d(N_j)|.
Classes C = {i : b_i = 1}, AB = {i : b_i = 2}, L = {i : b_i >= 3}; n_CA = |C| + |AB|.  Put
   m_lo := max(1, kappa + 1 - ceil((R - d)/4)),   m_hi := p - floor((R + d)/4),   Pi_need := p - ceil(R/2).
**Theorem SEG.**  If (H1) m_hi - m_lo >= Pi_need + 1, (H2) n_CA >= 2 m_lo + 2 and (H3) g_E >= Pi_need + 1, then w has an
identity 2p-subword (contradiction).  Any B; runs need not be pure.
Proof.  N_O := 2 m_lo + 2 (even, >= 4).  By (H2) choose O_0 inside C u AB with |O_0| = N_O.  Base arcs: for i in O_0 the single
block of M_i (i in C) or both blocks of M_i as one arc (a "pair-arc", nu = 2; i in AB).  This arc choice has c_i = 1 exactly
on O_0 (sum even); let z, T be its labelling.  Lemma BAL with some index i in O_0 gives an index i' != i (or nothing, if
|T| <= d already) such that changing the parities at i and i' gives |T| <= d.  A parity change at j removes the base arc of
M_j if M_j carries one; otherwise it adds the single block (j in C), the pair-arc (j in AB) or the first block of M_j as a
single-block arc (j in L).  Let O be the final set of indices carrying a base arc: |O| in {N_O - 2, N_O}, so the base has
m_b in {m_lo, m_lo + 1}, and |L n O| <= 1.
Segments (disjoint from the base and from each other): Sigma_j := M_j for j in (AB u L) \ O, and Sigma_j := M_j minus its
first block for j in L n O.  By Lemma SEG with t_j := ceil((b' - 1)/2) their potential gains are 1 (AB), e_j (L \ O) and
e_j - 1 (L n O); with the base pair-arcs (gain 1 for each j in AB n O) the potential total is
|AB| + sum_(j in L) e_j - |L n O| = g_E - |L n O| >= g_E - 1 >= Pi_need by (H3).  Lower the t_j to the least values for which
the guaranteed total gain is still >= Pi_need; as every unit of t adds at least one unit of guaranteed gain, sum t_j <= Pi_need.
Every configuration has m in [m_b, m_b + sum t_j], inside [m_lo, m_lo + 1 + Pi_need], inside [m_lo, m_hi] by (H1).  From
|T| <= d: E_min >= (R - d)/2 and E_max <= (R + d)/2, so for these m, ceil(E_min/2) >= ceil((R - d)/4) >= kappa + 1 - m and
floor(E_max/2) <= floor((R + d)/4) <= p - m: both windows are floor-type (Fact 2.1), and
floor(E+/2) + floor(E-/2) >= ceil(R/2) - 1 (E+ + E- = R).  Lemma ARC+ (iii) with total gain >= Pi_need = p - ceil(R/2): the
left side is >= p - 1.  So w does not avoid.  []

## 3. Corollaries

**Corollary SEG-p (R = p, every B).**  Let p >= 5 be prime and w a word of length 4p - 2 over D_(2p) with rotation letters in
one pair {rho_x, rho_-x}, x != 0, exactly p of them, all maximal constant reflection blocks odd, and
   (p + 1)/4 <= kappa <= (p - 3)/2.
Then w has an identity 2p-subword.
Proof.  Normalise; suppose w avoids.  v4 Sec. 4.4: q = p, every nonempty run is one letter (d = 1), g_E = 2 kappa.  Put
r := ceil((p - 1)/4) = floor((p + 1)/4).  Then ceil((R - d)/4) = floor((R + d)/4) = r, kappa + 1 - r >= 1 (for p = 4a + 1,
r = a and kappa >= a + 1; for p = 4a + 3, r = a + 1 and kappa >= a + 1), so m_lo = kappa + 1 - r and m_hi = p - r.
Pi_need = (p - 1)/2.  (H1): m_hi - m_lo = p - 1 - kappa >= (p + 1)/2 iff kappa <= (p - 3)/2.  (H2): every L-run has at least
two empty runs, so |L| <= kappa and n_CA >= p - kappa; 2 m_lo + 2 = 2 kappa + 4 - 2r <= 2 kappa + 4 - (p - 1)/2 <= p - kappa
iff 3 kappa <= (3p - 9)/2, i.e. kappa <= (p - 3)/2.  (H3): 2 kappa >= (p + 1)/2.  Theorem SEG.  []
**Corollary SEG-num (every R).**  Let w have length 4p - 2, rotation letters in one pair, all maximal constant reflection
blocks odd, and put delta := R - p.  If
   delta >= 0   and   (p + 3 delta + 2)/4 <= kappa <= (p - delta - 4)/2,
then w has an identity 2p-subword.  (The range is nonempty only if 5 delta <= p - 10.)
Proof.  Normalise; suppose w avoids.  Fact 2.2: d <= 2 delta + 1, so floor(d/2) <= delta, R - d >= p - delta - 1; and
q >= 2p - R = p - delta.  Also k = 2p - R + 2 kappa = p - delta + 2 kappa.
(H1): if m_lo = kappa + 1 - ceil((R - d)/4), then m_hi - m_lo = p - 1 - kappa - (floor((R + d)/4) - ceil((R - d)/4)) >=
p - 1 - kappa - floor(d/2) >= p - 1 - kappa - delta; if m_lo = 1 is larger, m_hi - m_lo is larger still.  Since
ceil(R/2) >= (p + delta)/2, Pi_need + 1 <= (p - delta)/2 + 1, and p - 1 - kappa - delta >= (p - delta)/2 + 1 iff
kappa <= (p - delta - 4)/2.
(H3): g_E = k - q >= k - R = 2 kappa - 2 delta >= (p - delta)/2 + 1 >= Pi_need + 1 iff kappa >= (p + 3 delta + 2)/4.
(H2): |L| <= (g_E - |AB|)/2 <= (k - q)/2, so n_CA = q - |L| >= (3q - k)/2 >= (3(p - delta) - (p - delta + 2 kappa))/2 =
p - delta - kappa.  And 2 m_lo + 2 <= max(4, 2 kappa + 4 - (p - delta - 1)/2).  Now p - delta - kappa >= 2 kappa + 4 -
(p - delta - 1)/2 iff kappa <= (p - delta - 3)/2, and p - delta - kappa >= 4 because kappa <= (p - delta - 4)/2 and
p - delta >= 10.  Theorem SEG.  []
Ranges.  delta = 0: SEG-p.  In general k = p - delta + 2 kappa runs over [(3p - delta + 2 + 6 delta)/2 rounded, 2p - 2 delta - 4],
i.e. roughly 3p/2 + 5 delta/2 <= k <= 2p - 2 delta - 4, all with k >= p + 1.

## 4. Updated map of RES-HI(p) (v4 + K2P+ + SEG; all CANDIDATE)

Excluded for all-odd words with rotations in one pair (any B):
* k >= max(2p + 1, 3 kappa + 3) (K2P+);
* R = p: (p + 1)/4 <= kappa <= (p - 3)/2 (SEG-p), (p + 1)/2 <= kappa <= p - 3 (K2P+), and FP-1 under its diversity condition;
* R = p + delta, 0 <= 5 delta <= p - 10: (p + 3 delta + 2)/4 <= kappa <= (p - delta - 4)/2 (SEG-num).
Remaining in RES-HI(p) (B = 0 additionally keeps the accepted CJ''''/EDGE/REFL-B0 coverage):
* R = p: kappa < (p + 1)/4, kappa = (p - 1)/2, kappa in {p - 2, p - 1};
* R >= p + 1 outside SEG-num and K2P+: large delta (some run with many letters), small H, and the band where
  g_E < Pi_need + 1.
Arc-method limit (a property of the method, not an obstruction to REFL): every configuration of Lemma ARC+ built from arcs
and segments inside reflection runs has total gain at most g_E (each unit of gain needs an empty run), so the method requires
g_E > Pi_need, roughly k > p + R/2.  Below that, other pattern families (intervals crossing nonempty runs with varying D_P)
are needed.
