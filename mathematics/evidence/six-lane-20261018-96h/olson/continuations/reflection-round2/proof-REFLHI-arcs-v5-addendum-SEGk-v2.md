# Addendum SEG-k (v2) to proof-REFLHI-arcs-v5.md: a parameter-only form of Theorem SEG, every R and every B

Owner OlsonReflectionSuccessor.  Written after host clock 2026-10-19T06:12:32-0700.  Status: CANDIDATE_UNVERIFIED (written
only; no computation).  Separate addendum, NOT part of the v5 delta-review set (parent instruction).  Supersedes the unsent
v1 of this addendum (789d1ed6...a08083, kept unchanged), whose Range paragraph overstated the comparison with SEG-num/SEG-p.
Base: proof-REFLHI-arcs-v5.md (4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c) with erratum-1
(512e1d9e...3331) and erratum-2 (b4451461...8820), unchanged.  Notation and Theorem SEG are those of v5 Sec. 5.

**Corollary SEG-k.**  Let p >= 5 be prime and w a word of length 4p - 2 over D_(2p) whose rotation letters lie in one pair
{rho_x, rho_-x}, x != 0, all of whose maximal constant reflection blocks have odd length; k = number of these blocks,
kappa = p - 1 - H, R = 2p - k + 2 kappa.  If
   k >= 4 kappa + 5   and   k >= p + floor(R/2) + 1,
then w has an identity 2p-subword in increasing index order.  No hypothesis on B, run purity or values.

Proof.  If R = 0, (AR).  Normalise x = 1 and A >= B; suppose w avoids (setting (S)).  Let q be the number of nonempty runs.
(i) q >= k - 2 kappa: by (P0) with e_F = 0 at most 2 kappa runs are even (empty runs included), and odd runs are nonempty.
(ii) q <= R, and d <= R - q + 1 (one run has at most R - (q - 1) letters).
(H1) m_hi - m_lo >= p - 1 - kappa - floor(d/2) (v5 SEG-num proof; larger still if m_lo = 1 is the maximum), and
Pi_need + 1 = p + 1 - ceil(R/2); so (H1) holds if ceil(R/2) - floor(d/2) >= kappa + 2.  By (ii),
ceil(R/2) - floor(d/2) >= R/2 - (R - q + 1)/2 = (q - 1)/2, and by (i) (q - 1)/2 >= (k - 2 kappa - 1)/2 >= kappa + 2.
(H2) Each L-run has >= 2 empty runs, so |L| <= (k - q)/2 and n_CA = q - |L| >= (3q - k)/2 >= k - 3 kappa by (i).  Also
2 m_lo + 2 = max(4, 2 kappa + 4 - 2 ceil((R - d)/4)) <= max(4, 2 kappa + 4 - (R - d)/2), and R - d >= q - 1 >= k - 2 kappa - 1.
Now k - 3 kappa >= 2 kappa + 4 - (k - 2 kappa - 1)/2 iff 3k >= 12 kappa + 9, and k - 3 kappa >= 4 iff k >= 3 kappa + 4; both
follow from k >= 4 kappa + 5 (kappa >= 0 by (P0)-free counting: kappa = p - 1 - H and H <= ... is not needed: if kappa < 0
then H >= p and p disjoint equal-letter pairs give an identity 2p-subword).
(H3) g_E = k - q >= k - R by (ii), and k - R >= p - ceil(R/2) + 1 = Pi_need + 1 iff k >= p + floor(R/2) + 1.
Theorem SEG gives a contradiction.  []

Range.  R = k (mod 2) and floor(R/2) = p + kappa - ceil(k/2), so the second hypothesis is k + ceil(k/2) >= 2p + kappa + 1:
k >= (4p + 2 kappa + 2)/3 for even k, k >= (4p + 2 kappa + 1)/3 for odd k.  An avoider has k <= p + 2 kappa (v5 Fact 2.2), so
inside RES_<(p) the corollary excludes, for B = 0 and for 1 <= B < kappa alike,
   (p + 1)/4 <= kappa <= (p - 5)/2,   max(4 kappa + 5, (4p + 2 kappa + 1)/3) <= k <= p + 2 kappa,
with R = 2p - k + 2 kappa in [p, (2p + 4 kappa - 1)/3].
Comparison (both are v5 results, unchanged): v5 SEG-num covers some cells with kappa = (p - delta - 4)/2 (delta = R - p) that
SEG-k misses (SEG-k needs kappa <= (p - delta - 5)/2 there), and v5 SEG-p covers kappa = (p - 3)/2 at R = p, which SEG-k misses;
otherwise SEG-num's cells satisfy SEG-k (same lower condition kappa >= (p + 3 delta + 2)/4).

Updated map (CANDIDATE): excluded, any B: K2P+ (k >= max(2p + 1, 3 kappa + 3)), SEG-k, SEG-num, and R = p with
kappa >= (p + 1)/4 for p >= 11 (v5 Secs. 5-6).  Remaining in RES-HI(p): kappa < (p + 1)/4 (arc-method limit; B = 0 partly
covered by accepted CJ''''/REFL-B0), the band (p - 5)/2 < kappa < (p + 1)/2 with R > p and k <= 2p, and k >= 2p + 1 with
k <= 3 kappa + 2.
