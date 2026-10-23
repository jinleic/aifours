# Region (B) of RES-HI(p): kappa in {(p - 3)/2, (p - 1)/2}, R = p + delta > p - a mixed pair/segment exclusion (candidate v1)

Owner OlsonReflectionSuccessor.  Written after host clock 2026-10-19T06:46:06-0700.  Status: CANDIDATE_UNVERIFIED (written
only; no computation, no model call).  Separate from every current review set.  Conditional on the CANDIDATE lemmas of
proof-REFLHI-arcs-v5.md (4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c) as corrected by its errata 1-4
(512e1d9e...3331, b4451461...8820, 380106c9...669a, 32811de5...07f1): Lemma W, Facts 2.1-2.2, Lemma 2.1, Lemmas ARC+, SEG,
3.1, 3.2 and BAL.  Theorem SEG of v5 is NOT used.  Parent-accepted imports enter only through those lemmas ((H0), (P0) of
REFL/proof-K0star-r2.md 6681676e...96e1; Cauchy-Davenport).

## 1. Region and counts

Region (B): p >= 5 prime, eps in {0, 1}, kappa = (p - 1)/2 - eps, R = p + delta with delta >= 1, all maximal constant blocks
odd, rotation letters in one pair (setting (S) of v5).  Then H = (p - 1)/2 + eps, k = 2p - R + 2 kappa = 2p - 1 - 2 eps - delta,
Pi_need = p - ceil(R/2) <= (p - delta)/2 (and Pi_need >= 1 for delta <= p - 3).
**Lemma B.1.**  If w avoids, then with q := number of nonempty runs and x := R - q:
 (i) p - delta <= q <= p + delta, 0 <= x <= 2 delta;  (ii) g_E = k - q = p - 1 - 2 eps - 2 delta + x;  (iii) d <= x + 1;
 (iv) for a := |AB|, c := |C|, l := |L| (v5 Theorem SEG classes): l <= (g_E - a)/2 and a + c >= q - g_E/2.
Proof.  (P0) with e_F = 0: at most 2 kappa runs are even, so q >= k - 2 kappa = p - delta; q <= R.  (ii) definition.  (iii) one
run has at most R - (q - 1) letters.  (iv) every L-run has >= 2 empty runs.  []
Put m_lo := kappa + 1 - ceil((R - d)/4) and m_hi := p - floor((R + d)/4) (v5 Sec. 5).  For delta <= p - 8, m_lo >= 1
(kappa + 1 - (R - d + 3)/4 >= (p - delta - 4)/4 + 1/4 > 1 - ... precisely kappa + 1 - ceil((R - d)/4) >= (p + 1)/2 - 1 -
(p + delta + 2)/4 = (p - delta - 4)/4 >= 1).  Also m_hi - m_lo >= H - floor(d/2) >= (p - 1)/2 + eps - delta (v5 K2P+ (a)),
and N_O := 2 m_lo + 2 satisfies
 (v) N_O >= (p - delta + d + 3 - 4 eps)/2 >= Pi_need,   (vi) N_O <= (p + 7 - 4 eps - delta + x)/2,
by 2 kappa = p - 1 - 2 eps, (R - d)/2 <= 2 ceil((R - d)/4) <= (R - d + 3)/2 and R - d >= q - 1 = R - x - 1.

## 2. The configuration

Let w avoid (region (B)).  Classes C, AB, L as in v5 Theorem SEG; e_j = b_j - 1.
Base.  O_0: all AB-runs if a <= N_O (otherwise N_O of them), then C-runs, then L-runs, |O_0| = N_O (possible since
N_O <= q for delta <= (p - 7)/3, by (vi) and q >= p + delta - x... and (i): N_O <= (p + 7 + x - delta)/2 <= p + delta - x = q
iff 3x <= p + 3 delta - 7, true as x <= 2 delta <= ... for delta <= (p - 7)/3).  lambda := number of L-runs in O_0.
Base arcs: AB-run -> both blocks as one arc (pair-arc, nu = 2); C-run -> its block; L-run -> a pair-arc on its first two
blocks.  Lemma BAL with some i in O_0: a change at j removes the base arc of M_j if it carries one, and otherwise adds the
block (C), the pair-arc (AB), or the pair-arc on the first two blocks (L).  (All arcs are singletons or two-block arcs, as
erratum-2 e5 requires.)  Final base set O, |O| in {N_O - 2, N_O}, m_b in {m_lo, m_lo + 1}, |T| <= d, and
   |L n O| <= lambda + 1,   base gain G_b := |AB n O| + |L n O| >= min(a, N_O) + lambda - 2.
Segments (Lemma ARC+): j in AB \ O: M_j (e' = 1); j in L \ O: M_j (e' = e_j); j in L n O: blocks 3..b_j of M_j (e' = e_j - 2).
A unit of a segment is one more inserted pair (t -> t + 1).  By Lemma SEG the first floor(e'/2) units each add >= 2 to the
guaranteed gain ("rate-2"), and one further unit adds >= 1 when e' is odd ("rate-1").  So the segments offer
   W2 = sum over segments of 2 floor(e'/2) = sum_(j in L) 2 floor(e_j/2) - 2 |L n O|   (rate-2 gain),
   W1 = number of segments with odd e'   (rate-1 gain),
and G_b + W2 + W1 = |AB| + sum_(L) e_j - |L n O| = g_E - |L n O|.
Choice of units: with G_need := max(0, Pi_need - G_b), take rate-2 units until G_need is reached, then rate-1 units.  If
G_b + W2 + W1 >= Pi_need, this reaches total guaranteed gain >= Pi_need with
   sum t <= max(ceil(G_need/2), G_need - W2/2)   (W2 is even).
Kill (Lemma 3.2 via Lemma ARC+): if moreover m_lo + 1 + sum t <= m_hi, every configuration has m in [m_lo, m_hi], hence
floor-type windows on both sides (|T| <= d, Fact 2.1), and w has an identity 2p-subword.

## 3. Theorem B

**Theorem B.**  Let p >= 5 be prime, eps in {0, 1}, and w a word of length 4p - 2 over D_(2p) whose rotation letters lie in
one pair {rho_x, rho_-x}, x != 0, all of whose maximal constant reflection blocks have odd length, with
kappa = (p - 1)/2 - eps and R = p + delta, where
   1 <= delta <= (2p - 29 + 2 eps)/7.
Then w has an identity 2p-subword (in increasing index order).  (Any B; runs need not be pure.)
Proof.  Suppose w avoids; Sec. 2 applies (the range gives delta <= (p - 8)/3, so m_lo >= 1 and N_O <= q).
Case a > N_O.  Then O_0 consists of AB-runs, lambda = 0, and G_b >= N_O - 2 >= Pi_need - 2 by (v).  If BAL removed r <= 2
AB-runs from the base, they are AB-segments, each giving rate-1 gain 1 with one unit, and G_b >= N_O - r; so the gain
Pi_need is reached with sum t <= 2.  m_hi - m_lo - 1 >= (p - 3)/2 + eps - delta >= 2.
Case a <= N_O.  All AB-runs are in O_0.
 Potential: G_b + W2 + W1 = g_E - |L n O| >= g_E - lambda - 1.  By (iv), (vi): lambda <= max(0, N_O - a - c) <=
 max(0, 3 - 3 eps - 5 delta/2 + 2x).  If lambda = 0: g_E - 1 = p - 2 - 2 eps - 2 delta + x >= (p - delta)/2 >= Pi_need as
 delta <= (p - 4 - 4 eps)/3.  If lambda > 0: g_E - lambda - 1 >= p - 5 + eps + delta/2 - x >= (p - delta)/2 as x <= 2 delta and
 delta <= p/2 - 5 + eps.  Both delta bounds follow from the hypothesis.
 Budget: W2 >= sum_L (e_j - [e_j odd]) - 2(lambda + 1) >= (2/3)(g_E - a) - 2 lambda - 2 (an L-run has e_j >= 2, and
 e - [e odd] >= 2e/3 for e >= 2), and G_need <= Pi_need - a - lambda + 2.  Hence
   ceil(G_need/2) <= (Pi_need + 3)/2 <= (p - delta + 3)/4 + 1/2,
   G_need - W2/2 <= Pi_need - (2/3) a - g_E/3 + 3 <= (p - delta)/2 - (p - 1 - 2 eps - 2 delta + x)/3 + 3.
 We need both <= m_hi - m_lo - 1, for which (p - 3)/2 + eps - delta suffices.  The first: (p - delta + 5)/4 <= (p - 3)/2 - delta
 iff 3 delta <= p - 11, implied.  The second, multiplied by 6 and with x >= 0: 3p - 3 delta - 2p + 2 + 4 eps + 4 delta + 18 <=
 3p - 9 + 6 eps - 6 delta, i.e. 7 delta <= 2p - 29 + 2 eps: the hypothesis.
In both cases the kill of Sec. 2 applies: contradiction.  []
Range.  Nonempty iff p >= 19 (eps = 0) or p >= 17 (eps = 1).  Examples: p = 31: delta <= 4 (eps = 0), delta <= 5 (eps = 1);
p = 101: delta <= 24 (eps = 0), delta <= 25 (eps = 1).  In (kappa, k): k = 2p - 1 - 2 eps - delta, so Theorem B excludes the
region-(B) cells with 2p - 1 - 2 eps - (2p - 29 + 2 eps)/7 <= k <= 2p - 2 - 2 eps.
Comparison: v5 SEG-num does not reach kappa >= (p - 3)/2 for delta >= 1, and v5 Theorem SEG (rate-1 accounting) misses
region (B) by about two units of m when d is small (its (H1) needs H - floor(d/2) >= Pi_need + 1); the gain here comes from
(a) base pair-arcs (one unit of gain per half unit of m) and (b) rate-2 segment units.

## 4. What remains in region (B), exactly

For the parameters of region (B) outside Theorem B, the proof above fails only in the inequality G_need - W2/2 <= m_hi - m_lo - 1
(the others hold up to delta <= (p - 8)/3 and delta <= p/2 - 5 + eps).  Retracing it without x >= 0:
**Corollary B.2 (structure of a remaining avoider).**  If w is an avoider in region (B) with delta <= (p - 11)/3, then
   2x < 7 delta - 2p + 29 - 2 eps,   i.e.   g_E < p - 1 - 2 eps - 2 delta + (7 delta - 2p + 29 - 2 eps)/2,
where x = R - q is the number of rotation letters in excess of one per nonempty run.  In words: few multi-letter runs and few
empty runs (the arc limit).  For delta > (p - 11)/3 nothing beyond Lemma B.1 is claimed (also the arc limit regime).
Remaining cells of region (B): (B-small) p <= 17 (eps = 0) or p <= 13 (eps = 1) with delta >= 1; (B-high)
(2p - 29 + 2 eps)/7 < delta <= p - 2 - 2 eps, where avoiders must satisfy Corollary B.2 when delta <= (p - 11)/3.
Region (A) (kappa < (p + 1)/4) remains the larger stated obstruction; no lift argument is claimed.
