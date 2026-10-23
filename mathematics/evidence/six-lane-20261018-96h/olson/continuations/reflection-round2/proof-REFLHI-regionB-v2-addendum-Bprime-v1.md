# Addendum B' to proof-REFLHI-regionB-v2.md: the region-(B) range extended to delta <= (p - 12 + 4 eps)/3

Owner OlsonReflectionSuccessor.  Written after host clock 2026-10-19T06:50:00-0700.  Status: CANDIDATE_UNVERIFIED (written only).
Base: proof-REFLHI-regionB-v2.md (35948d69955ab44faa6464741a2190c97d528218334101b8fc02674422640af3) with erratum-1
(94a018c5...43e3), unchanged; same explicit conditions (v5 candidate lemmas with errata 1-4).  Theorem B of v2 stays valid
and is implied by Theorem B' below.  The only new point: the budget of v2 used floor(d/2) <= delta for every x; here the
x-dependent bound floor(d/2) <= floor((x + 1)/2) (Lemma B.1 (iii)) is kept.

**Theorem B'.**  Let p >= 5 be prime, eps in {0, 1}, and w a word of length 4p - 2 over D_(2p) whose rotation letters lie in one
pair {rho_x, rho_-x}, x != 0, all of whose maximal constant reflection blocks have odd length, with kappa = (p - 1)/2 - eps and
R = p + delta, where
   1 <= delta <= min( (p - 12 + 4 eps)/3 , (2p - 32 + 2 eps)/3 ).
Then w has an identity 2p-subword in increasing index order.  (Any B; runs need not be pure.)

Proof.  Suppose w avoids; notation of v2 (q, x = R - q, a, c, l, N_O, lambda, O, G_b, W2, W1, G_need).
Validity of the construction of v2 Sec. 2 (the items of v2 Lemma B.2 with their actual requirements):
* m_lo >= 1 needs delta <= p - 4 - 4 eps (v2 (v)); N_O <= q needs 3x <= p + 3 delta - 7 + 4 eps, which for x <= 2 delta follows
  from 3 delta <= p - 7 + 4 eps (v2 (viii)); (vi), (vii), (ix) need nothing.  All hold since 3 delta <= p - 12 + 4 eps.
* By v2 (vi) in its exact form m_hi - m_lo >= H - floor(d/2), and d <= x + 1:
     m_hi - m_lo - 1 >= (p - 3)/2 + eps - floor((x + 1)/2).                                                    (*)
Case a > N_O (v2): sum t <= 2 and m_hi - m_lo >= 3 because floor((x + 1)/2) <= delta <= (p - 7)/2 + eps.  Kill (v2 Lemma B.3).
Case a <= N_O.  Potential (v2): lambda = 0 needs 3 delta <= p - 4 - 4 eps; lambda > 0 needs delta <= p/2 - 5 + eps.  Both follow
from 3 delta <= p - 12 + 4 eps (the second as p >= 6 + 2 eps).
Budget.  As in v2, sum t <= max(ceil(G_need/2), G_need - W2/2) with
   ceil(G_need/2) <= (p - delta + 6)/4,   G_need - W2/2 <= (p - delta)/2 - (p - 1 - 2 eps - 2 delta + x)/3 + 3.
(F1) (p - delta + 6)/4 <= (p - 3)/2 + eps - floor((x + 1)/2) iff 4 floor((x + 1)/2) <= p - 12 + 4 eps + delta; the left side is at
     most 4 delta (x <= 2 delta), so 3 delta <= p - 12 + 4 eps suffices.
(F2) Using floor((x + 1)/2) <= (x + 1)/2 and multiplying by 6:
     3p - 3 delta - 2p + 2 + 4 eps + 4 delta - 2x + 18 <= 3p - 9 + 6 eps - 3x - 3,   i.e.   delta + x + 32 - 2 eps <= 2p;
     for x <= 2 delta it suffices that 3 delta <= 2p - 32 + 2 eps.
By (*), (F1) and (F2), m_lo + 1 + sum t <= m_hi, and v2 Lemma B.3 gives a contradiction.  []

Range.  For p >= 20 + 2 eps the bound is delta <= (p - 12 + 4 eps)/3.  Examples: p = 19: delta <= 2 (eps = 0), delta <= 2
(eps = 1); p = 31: delta <= 6 (eps = 0), delta <= 7 (eps = 1); p = 101: delta <= 29 (eps = 0), delta <= 31 (eps = 1).  Theorem B
of v2 gave 1, 2; 4, 5; 24, 25.  Nonempty iff p >= 19 (eps = 0) or p >= 17 (eps = 1).
Consequence for v2 Corollary B.4: for p >= 20 + 2 eps it becomes vacuous inside the range of Theorem B' (every such cell is
excluded).  Remaining cells of region (B): p <= 17 (eps = 0) or p <= 13 (eps = 1); and delta > min((p - 12 + 4 eps)/3,
(2p - 32 + 2 eps)/3) up to delta <= p - 2 - 2 eps.  There only v2 Lemma B.1 is claimed; for large delta the empty-run supply
g_E = p - 1 - 2 eps - 2 delta + x is the binding quantity (the arc limit).
