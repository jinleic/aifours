# Addendum SEG-k to proof-REFLHI-arcs-v5.md: a parameter-only form of Theorem SEG, every R and every B

Owner OlsonReflectionSuccessor.  Written after host clock 2026-10-19T06:11:49-0700.  Status: CANDIDATE_UNVERIFIED (written
only; no computation).  Base: proof-REFLHI-arcs-v5.md (4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c)
with erratum-1 (512e1d9e...3331) and erratum-2 (b4451461...8820), unchanged.  Notation and Theorem SEG are those of v5 Sec. 5.

**Corollary SEG-k.**  Let p >= 5 be prime and w a word of length 4p - 2 over D_(2p) whose rotation letters lie in one pair
{rho_x, rho_-x}, x != 0, all of whose maximal constant reflection blocks have odd length; k = number of these blocks,
kappa = p - 1 - H, R = 2p - k + 2 kappa.  If
   k >= 4 kappa + 5   and   k >= p + floor(R/2) + 1,
then w has an identity 2p-subword in increasing index order.  No hypothesis on B, on run purity or on R beyond these.

Proof.  If R = 0, (AR).  Normalise x = 1 and A >= B; suppose w avoids (setting (S)).  Let q be the number of nonempty runs.
(i) q >= k - 2 kappa: by (P0) with e_F = 0 at most 2 kappa runs are even, and odd runs are nonempty.
(ii) q <= R (each nonempty run has a letter), and d <= R - q + 1 (one run has at most R - (q - 1) letters).
(H1) As in v5 Corollary SEG-num, m_hi - m_lo >= p - 1 - kappa - floor(d/2) (also when m_lo = 1 is the maximum, since then
m_hi - m_lo is larger).  Pi_need + 1 = p + 1 - ceil(R/2).  So (H1) holds if ceil(R/2) - floor(d/2) >= kappa + 2.  By (ii),
ceil(R/2) - floor(d/2) >= R/2 - (R - q + 1)/2 = (q - 1)/2, and by (i) q - 1 >= k - 2 kappa - 1 >= 2 kappa + 4.
(H2) |L| <= (g_E - |AB|)/2 <= (k - q)/2 (every L-run has >= 2 empty runs), so n_CA = q - |L| >= (3q - k)/2 >=
(3(k - 2 kappa) - k)/2 = k - 3 kappa.  Also 2 m_lo + 2 <= max(4, 2 kappa + 4 - (R - d)/2) <= max(4, 2 kappa + 4 - (q - 1)/2)
by (ii), and <= max(4, 2 kappa + 4 - (k - 2 kappa - 1)/2) by (i).  Now k - 3 kappa >= 2 kappa + 4 - (k - 2 kappa - 1)/2 iff
3k >= 12 kappa + 9, i.e. k >= 4 kappa + 3; and k - 3 kappa >= 4 iff k >= 3 kappa + 4.  Both follow from k >= 4 kappa + 5
(kappa >= -1).
(H3) g_E = k - q >= k - R by (ii), and k - R >= Pi_need + 1 = p - ceil(R/2) + 1 iff k >= p + floor(R/2) + 1.
Theorem SEG gives a contradiction.  []

Range.  R and k have the same parity (R = 2p - k + 2 kappa), and floor(R/2) = p + kappa - ceil(k/2), so the second hypothesis
reads k + ceil(k/2) >= 2p + kappa + 1, i.e. k >= (4p + 2 kappa + 2)/3 for even k and k >= (4p + 2 kappa + 1)/3 for odd k.
An avoider has k <= p + 2 kappa (v5 Fact 2.2), so for RES_<(p) the corollary excludes the cells
   (p + 1)/4 <= kappa <= (p - 5)/2,   max(4 kappa + 5, (4p + 2 kappa + 1)/3) <= k <= p + 2 kappa,
for both B = 0 and 1 <= B < kappa, with no restriction on R (here p <= R <= (2p + 4 kappa - 1)/3).  It contains v5's
Corollary SEG-num, and v5's Corollary SEG-p at R = p except kappa in {(p - 4)/2 ... (p - 3)/2} (i.e. the top one or two values,
which SEG-p and MID keep).

Updated map (CANDIDATE): excluded, any B: k >= max(2p + 1, 3 kappa + 3) (K2P+); k >= max(4 kappa + 5, p + floor(R/2) + 1)
(SEG-k); R = p with kappa >= (p + 1)/4 for p >= 11 (v5 Sec. 6).  Remaining in RES-HI(p): kappa < (p + 1)/4 (the arc-method
limit g_E <= Pi_need; for B = 0 partly covered by the accepted CJ''''/REFL-B0), the band (p - 5)/2 < kappa < (p + 1)/2 with
R > p and k <= 2p, and k >= 2p + 1 with k <= 3 kappa + 2.
