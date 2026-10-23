# Region (B) of RES-HI(p): kappa in {(p - 3)/2, (p - 1)/2}, R = p + delta > p - a mixed pair/segment exclusion (candidate v2)

Owner OlsonReflectionSuccessor.  Written after host clock 2026-10-19T06:47:32-0700.  Status: CANDIDATE_UNVERIFIED (written
only; no computation, no model call).  Separate from every current review set.  Supersedes the unsent v1 (1bf4dd3d...a339, kept
unchanged; two constants in its budget check and in Corollary B.2 were off by one, and two displayed lines were garbled).
CONDITIONS (not parent-accepted): the CANDIDATE lemmas of proof-REFLHI-arcs-v5.md
(4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c) read with errata 1-4 (512e1d9e...3331, b4451461...8820,
380106c9...669a, 32811de5...07f1): Lemma W, Facts 2.1-2.2, Lemma 2.1, Lemmas ARC+, SEG, 3.1, 3.2, BAL.  Theorem SEG of v5 is
NOT used.  Parent-accepted imports enter only through those lemmas: (H0), (P0) of REFL/proof-K0star-r2.md (6681676e...96e1);
Cauchy-Davenport (classical).

## 1. Region and counts

Region (B): p >= 5 prime; eps in {0, 1}; kappa = (p - 1)/2 - eps; R = p + delta with delta >= 1; all maximal constant reflection
blocks odd; rotation letters in one pair (setting (S) of v5).  Then H = (p - 1)/2 + eps, k = 2p - R + 2 kappa =
2p - 1 - 2 eps - delta, and Pi_need := p - ceil(R/2) satisfies 1 <= Pi_need <= (p - delta)/2 for delta <= p - 3.
**Lemma B.1.**  Let w avoid; q := number of nonempty runs, x := R - q, a := |AB|, c := |C|, l := |L| (classes of v5 Theorem
SEG).  Then
 (i) p - delta <= q <= p + delta and 0 <= x <= 2 delta;  (ii) g_E = k - q = p - 1 - 2 eps - 2 delta + x;  (iii) d <= x + 1;
 (iv) l <= (g_E - a)/2, hence a + c = q - l >= q - g_E/2 = (p + 4 delta - 3x + 1 + 2 eps)/2.
Proof.  (P0) with e_F = 0: at most 2 kappa runs are even, so q >= k - 2 kappa = p - delta; q <= R.  (ii) is the definition.
(iii) one run carries at most R - (q - 1) letters.  (iv) every L-run contains >= 2 empty runs.  []
**Lemma B.2.**  Let w avoid and 1 <= delta <= (p - 12)/3.  Put m_lo := kappa + 1 - ceil((R - d)/4), m_hi := p - floor((R + d)/4),
N_O := 2 m_lo + 2.  Then
 (v) m_lo >= 1;  (vi) m_hi - m_lo >= (p - 1)/2 + eps - delta;  (vii) Pi_need <= (p - delta + d + 3 - 4 eps)/2 <= N_O;
 (viii) N_O <= (p + 7 - 4 eps - delta + x)/2 <= q;  (ix) N_O - a - c <= max(0, 3 - 3 eps - 5 delta/2 + 2x).
Proof.  (v) kappa + 1 - ceil((R - d)/4) >= kappa + 1 - (R + 2)/4 = (p - delta - 4 eps)/4 >= 1 as delta <= p - 8.
(vi) v5 K2P+ (a): m_hi - m_lo >= H - floor(d/2), and floor(d/2) <= delta by (iii) and x <= 2 delta.
(vii), (viii): 2 kappa = p - 1 - 2 eps and (R - d)/2 <= 2 ceil((R - d)/4) <= (R - d + 3)/2 give
(p - delta + d + 3 - 4 eps)/2 <= N_O <= p + 3 - 2 eps - (R - d)/2; then use d >= 1, eps <= 1, Pi_need <= (p - delta)/2, and
R - d >= q - 1 = R - x - 1.  N_O <= q iff 3x <= p + 3 delta - 7 + 4 eps, true as x <= 2 delta and delta <= (p - 7)/3.
(ix) subtract (iv) from (viii).  []

## 2. The configuration

Let w avoid, region (B), 1 <= delta <= (p - 12)/3.
Base.  O_0 of size N_O: all AB-runs if a <= N_O (otherwise N_O of them), then C-runs, then L-runs (possible by (viii));
lambda := number of L-runs in O_0, so lambda <= max(0, N_O - a - c).  Base arcs: AB-run -> its two blocks as one arc
(pair-arc, nu = 2); C-run -> its block; L-run -> a pair-arc on its first two blocks.  Lemma BAL with some index i in O_0; a
change at j removes the base arc of M_j if it carries one, and otherwise adds the block (C), the pair-arc (AB), or the pair-arc
on the first two blocks (L).  Every arc is a singleton or a two-block arc (erratum-2 e5).  Let O be the final base set:
|O| in {N_O - 2, N_O}, the base has m_b in {m_lo, m_lo + 1}, |T| <= d, |L n O| <= lambda + 1, and the base gain
G_b := |AB n O| + |L n O| (pair-arcs) satisfies G_b >= min(a, N_O) + lambda - 2 (BAL removes at most two base arcs).
Segments (Lemma ARC+): M_j for j in AB \ O (e' = 1) and for j in L \ O (e' = e_j); blocks 3..b_j of M_j for j in L n O
(e' = e_j - 2).  A unit is one more inserted pair in a segment.  By Lemma SEG the first floor(e'/2) units of a segment each add
>= 2 to the guaranteed gain (rate 2), and one further unit adds >= 1 if e' is odd (rate 1).  Write
   W2 := sum over segments of 2 floor(e'/2) = sum_(j in L) 2 floor(e_j/2) - 2 |L n O|,   W1 := number of segments with odd e',
so G_b + W2 + W1 = |AB| + sum_(j in L) e_j - |L n O| = g_E - |L n O|.
Units.  G_need := max(0, Pi_need - G_b).  Use rate-2 units until G_need is reached, then rate-1 units.  If G_b + W2 + W1 >= Pi_need
this gives guaranteed total gain >= Pi_need with
   sum t <= max(ceil(G_need/2), G_need - W2/2).
**Lemma B.3 (kill).**  If G_b + W2 + W1 >= Pi_need and m_lo + 1 + sum t <= m_hi, then w has an identity 2p-subword.
Proof.  All configurations have m in [m_b, m_b + sum t], inside [m_lo, m_hi]; with |T| <= d, Fact 2.1 gives floor-type windows
on both sides for every such m (as in v5 Theorem K2P+ (g)); Lemma 3.2 (through Lemma ARC+) applies.  []

## 3. Theorem B

**Theorem B.**  Let p >= 5 be prime, eps in {0, 1}, and w a word of length 4p - 2 over D_(2p) whose rotation letters lie in one
pair {rho_x, rho_-x}, x != 0, and all of whose maximal constant reflection blocks have odd length, with kappa = (p - 1)/2 - eps
and R = p + delta, where
   1 <= delta <= (2p - 29 + 2 eps)/7.
Then w has an identity 2p-subword in increasing index order.  (Any B; runs need not be pure.)
Proof.  Suppose w avoids.  (2p - 29 + 2 eps)/7 <= (p - 12)/3 for every p (equivalent to p >= -3 - 6 eps), so Sec. 2 applies.
Case a > N_O.  O_0 consists of AB-runs and lambda = 0.  If BAL removed r <= 2 AB-runs from the base, G_b >= N_O - r >= Pi_need - r
by (vii), and the r removed AB-runs are segments with one rate-1 unit each; so Pi_need is reached with sum t <= 2, and
m_lo + 3 <= m_hi by (vi) (delta <= (p - 7)/2).  Lemma B.3.
Case a <= N_O.  All AB-runs are in O_0, so G_b >= a + lambda - 2 and G_need <= Pi_need - a - lambda + 2.
 Potential.  G_b + W2 + W1 = g_E - |L n O| >= g_E - lambda - 1.  If lambda = 0: g_E - 1 >= p - 2 - 2 eps - 2 delta >= (p - delta)/2
 because 3 delta <= p - 4 - 4 eps.  If lambda > 0: by (ix), g_E - lambda - 1 >= p - 5 + eps + delta/2 - x >= (p - delta)/2 because
 x <= 2 delta and delta <= p/2 - 5 + eps.  Both delta bounds follow from delta <= (p - 12)/3.
 Budget.  An L-run has e_j >= 2, and e - [e odd] >= 2e/3 for e >= 2, so W2 >= (2/3)(g_E - a) - 2(lambda + 1).  Hence
   ceil(G_need/2) <= (G_need + 1)/2 <= (Pi_need + 3)/2 <= (p - delta + 6)/4,
   G_need - W2/2 <= Pi_need - (2/3) a - g_E/3 + 3 <= (p - delta)/2 - (p - 1 - 2 eps - 2 delta + x)/3 + 3.
 By (vi), m_hi - m_lo - 1 >= (p - 3)/2 + eps - delta.  The first bound is <= (p - 3)/2 - delta iff 3 delta <= p - 12.  For the
 second, multiplying by 6: 3p - 3 delta - 2p + 2 + 4 eps + 4 delta - 2x + 18 <= 3p - 9 + 6 eps - 6 delta iff
 7 delta + 29 - 2 eps - 2x <= 2p, which holds for every x >= 0 by the hypothesis 7 delta <= 2p - 29 + 2 eps.  Lemma B.3.
Both cases contradict the avoidance of w.  []
Range.  Nonempty iff p >= 19 (eps = 0) or p >= 17 (eps = 1).  Examples: p = 31: delta <= 4 (eps = 0), delta <= 5 (eps = 1);
p = 101: delta <= 24 (eps = 0), delta <= 25 (eps = 1).  In terms of k = 2p - 1 - 2 eps - delta, Theorem B excludes the region-(B)
cells with 2p - 1 - 2 eps - floor((2p - 29 + 2 eps)/7) <= k <= 2p - 2 - 2 eps.
Comparison: v5 SEG-num never reaches kappa >= (p - 3)/2 when delta >= 1, and v5 Theorem SEG's rate-1 accounting misses this region
by about two units of m when d is small (its (H1) needs H - floor(d/2) >= Pi_need + 1).  Here base pair-arcs (one unit of gain
per half unit of m) and rate-2 segment units supply the missing room.

## 4. What remains in region (B), exactly

**Corollary B.4 (structure of a remaining avoider).**  Let w be an avoider in region (B) with 1 <= delta <= (p - 12)/3.  Then
a <= N_O and
   2x < 7 delta - 2p + 29 - 2 eps,
where x = R - q is the number of rotation letters in excess of one per nonempty run; equivalently
g_E < p - 1 - 2 eps - 2 delta + (7 delta - 2p + 29 - 2 eps)/2.
Proof.  In the proof of Theorem B every step except the last inequality uses only delta <= (p - 12)/3; Case a > N_O always kills;
in Case a <= N_O the kill fails only if 7 delta + 29 - 2 eps - 2x > 2p.  []
Remaining cells of region (B):
* (B-small) p <= 17 (eps = 0) or p <= 13 (eps = 1), every delta >= 1;
* (B-high) (2p - 29 + 2 eps)/7 < delta <= p - 2 - 2 eps (k >= p + 1).  For delta <= (p - 12)/3 an avoider there must satisfy
  Corollary B.4 (few multi-letter runs and few empty runs: the arc limit); for delta > (p - 12)/3 only Lemma B.1 is claimed.
Region (A) (kappa < (p + 1)/4) remains the larger stated obstruction; no lift argument is claimed.
