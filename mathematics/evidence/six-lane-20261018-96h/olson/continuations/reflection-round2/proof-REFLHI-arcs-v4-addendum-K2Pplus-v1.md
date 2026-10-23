# Addendum K2P+ to proof-REFLHI-arcs-v4.md: the threshold k >= 2p + 3 lowered to k >= 2p + 1

Owner OlsonReflectionSuccessor.  Written after host clock 2026-10-19T05:44:24-0700.  Status: CANDIDATE_UNVERIFIED (written
only).  Base: proof-REFLHI-arcs-v4.md, sha256 7683eb17905ab0c9d21046f4e4a0de2fc7e868a9c394e1c874308bf4a2a77f0e (unchanged).
All notation, Lemmas W, ARC, 3.1, 4.1, 4.2, BAL, Facts 2.1, 2.2 and the imports are those of v4.  Theorem K2P of v4 stays
valid and is implied by Theorem K2P+ below.

**Theorem K2P+.**  Let p >= 5 be prime and w a word of length 4p - 2 over D_(2p) whose rotation letters lie in one pair
{rho_x, rho_-x}, x != 0, all of whose maximal constant reflection blocks have odd length.  If
   k >= 2p + 1   and   k >= 3 kappa + 3,
then w has an identity 2p-subword in increasing index order.  (No hypothesis on B, run purity, values or o_F = k.)

Proof.  k >= 1, so F >= 1; if R = 0 use (AR).  Normalise x = 1, A >= B; w is in setting (S).  Suppose w avoids.  Let
delta := R - p >= 0 and d := max_j |d_(N_j)| <= 2 delta + 1 (Fact 2.2).  As R = 2p - k + 2 kappa: k >= 3 kappa + 3 is
H - delta >= 2, and k >= 2p + 1 is 2 kappa >= R + 1; also R = k (mod 2).  Put
   m_lo := kappa + 1 - ceil((R - d)/4),  m_hi := p - floor((R + d)/4),  Pi_need := p - ceil(R/2),  Pi* := Pi_need + 1.
(a) m_hi - m_lo >= H - floor(d/2) >= H - delta >= 2 (as in v4).
(b) m_lo >= 1: m_lo >= kappa + 1 - (R + 3)/4 >= (R + 1)/2 + 1 - (R + 3)/4 = (R + 3)/4 > 0.
(c) Pair supply: at least (k - R)/2 disjoint pairs (v4 (c)); (k - R)/2 >= Pi* iff k >= 2p + 2 - [R odd], which follows from
    k >= 2p + 1 and k = R (mod 2) (k odd: k >= 2p + 1; k even: k >= 2p + 2).
(d) Bounds.  2 kappa >= R + 1 >= p + 1 gives H = p - 1 - kappa <= (p - 3)/2, so d <= 2 delta + 1 <= 2(H - 2) + 1 <= p - 6.
    N0 := 2 m_lo + 2 satisfies N0 >= 2 kappa + 4 - (R - d + 3)/2 >= R + 1 + 4 - (R + 3)/2 = R/2 + 3.5 >= p - R/2 + 1 + ... ;
    precisely Pi* <= p - R/2 + 1 <= R/2 + 3.5 <= N0 because R >= p.  And N0 + Pi* <= 2 kappa + 4 - (R - d)/2 + p - R/2 + 1
    = k - p + 5 + d/2 <= k - 1 because d <= p - 6 <= 2p - 12 (p >= 7; for p = 5 the hypotheses are inconsistent, see below).
(e) Initial choice: Pi* disjoint pairs and N0 - Pi* singleton arcs on unused blocks (possible since N0 + Pi* <= k - 1 < k, i.e.
    2 Pi* + (N0 - Pi*) < k).  At least one block is then unused, or at least one singleton exists; let i be the index of a
    reflection run M_i containing an unused block or a singleton.
(f) Balance.  Apply Lemma BAL with this i.  The parity change at i costs no pair (delete its singleton, or put a singleton
    on its unused block); the parity change at i' costs at most one pair.  Afterwards |T| <= d, the number of pairs is
    >= Pi* - 1 = Pi_need, and the arc count lies in [N0 - 2, N0 + 2] = [2 m_lo, 2 m_lo + 4], inside [2 m_lo, 2 m_hi] by (a).
(g) Kill.  As in v4 (f): with m_lo <= m <= m_hi and |T| <= d, Fact 2.1 gives floor-type windows on both sides, and
    sum(nu - 1) >= Pi_need = p - ceil(R/2); Lemma 4.2 gives a contradiction.  []
Range.  For an avoider of RES_<(p), k <= p + 2 kappa (Fact 2.2), so the hypotheses describe the cells
   (p + 1)/2 <= kappa <= p - 3,   max(2p + 1, 3 kappa + 3) <= k <= p + 2 kappa,   any B (B = 0 and 1 <= B < kappa).
Nonempty iff p >= 7.  For p = 5 they are empty (kappa >= 3 and kappa <= 2).
**Corollary IIIb-X (the extreme IIIb family).**  For every prime p >= 7, no word of length 4p - 2 with all rotation letters
equal (B = 0), R = p, kappa = (p + 1)/2 and all maximal constant blocks odd (hence k = 2p + 1) avoids.
Proof.  k = 2p + 1 and 3 kappa + 3 = (3p + 9)/2 <= 2p + 1 iff p >= 7.  []
This is the family of REFL/notes-IIIb-extreme-r1.md (gap (d) of REFL/results-r4.md); at p = 7 it is the cell
(kappa, k) = (4, 15), where the previous desk's census found 54,927 two-interval survivors, all killed by 3-interval patterns
(finite aid there, not a premise here).  For B = 0, R = p the kill uses the alternating-type labellings of Theorem FP.

Worked check of the inequalities at p = 7, kappa = 4, R = 7, k = 15 (arithmetic only): H = 2, delta = 0, d = 1, Pi_need = 3,
Pi* = 4, (k - R)/2 = 4, m_lo = 3, m_hi = 5, N0 = 8, N0 + Pi* = 12 <= 14; windows for E in {3, 4}, m in [3, 5]: gamma = 1, 2;
G + G' = 3; pairs >= 3; 3 + 3 = 6 = p - 1.

Remaining after K2P+ (replaces the first two bullets of v4 Sec. 7):
* p + 1 <= k <= 2p (every B), except FP-1 words at R = p and the accepted B = 0 CJ''''/REFL-B0 ranges;
* k >= 2p + 1 with k <= 3 kappa + 2 (H - delta <= 1).
