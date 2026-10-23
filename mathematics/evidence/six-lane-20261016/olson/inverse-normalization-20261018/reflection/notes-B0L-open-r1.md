# B = 0, k >= p + 1 after Theorem B0S++: the open cases (T) and (III), exact reformulation, partial lemmas, evidence

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T06:27:58-0700.  Status: Sec. 2 partial lemmas [W], UNREVIEWED;
Secs. 1, 3 exact statements of what is open; Sec. 4 finite aids (not premises).  Notation of proof-B0SPP-r4.md (669e5d97...24dc).

## 1. What is open

B = 0, all blocks odd, kappa >= 1, k >= p + 1 (so R = 2p - k + 2 kappa <= p - 1 + 2 kappa), not covered by Theorem B0S++:
 (T)  R >= 4 kappa + 1, Delta := k - p - kappa - 1 >= 2, and every two adjacent run pairs of mass >= 2 Delta - 1 share a run;
 (III) R <= 4 kappa (then kappa >= p/4, as R >= p by P0).
In both, B0S Secs. 3-5 would finish the proof given LEMMA SIGMA (sum of singleton representatives = p) and, in (III), a selection
lemma replacing the Case I/II bounds that need R >= 4 kappa - 1 ((L3)) and 4 kappa <= 2p ((U1), (L1)).

## 2. Partial lemmas (regime R >= 4 kappa + 1)

**Lemma P (exact (B') threshold for one light pair sum).**  In a 3-partition (Q1, Q2, Q3) into consecutive intervals with exactly
one pair sum s <= 2 kappa, let r be the mass of the part not in that pair... equivalently write the triple as (A, {j}, C) with s =
m(A) + r_j the light union and the two other unions floor terms.  Then (B') holds iff
   s >= 2 Delta - 1, or s = 2 Delta - 2 and R - r_j is even
(when A u {j} is the light union; symmetric for {j} u C).  Proof: (B') = s - kappa + floor((R - s + r_j)/2) + floor((R - r_j)/2), and
R - kappa - 1 + Delta = p - 2; evaluate the two floors by the parities of R - r_j and s.  []
**Lemma L (jumps are light).**  For any chain Q_j = [s, j] (j = s, ..., s - 2 cyclically), c(Q_j) - c(Q_(j-1)) is 0 or 1, and it can be 1
only at a step where [s, j] or [j, s - 1] is light in the sense of Lemma P (mass <= 2 Delta - 2, and = 2 Delta - 2 only with the
wrong parity).  J equals the number of jumps along every chain.  Proof: Lemma C1(c), C2(a), C2(b) of proof-B0SPP-r4.md and Lemma P;
the third union [k] \ {j} is never light (no run has mass > R - 2 Delta + 1, since otherwise n_E >= p + 2 > 2 kappa).  []
**Corollary L.**  If J >= 1 then some light interval (mass <= 2 Delta - 2) has c >= 1; a shortest such interval B has all proper
sub-intervals at c = 0, W(B) >= p + m_B - kappa + 1, and both end runs t of B satisfy w_t >= m_B - kappa + 2 + floor((R - m_B + r_t)/2)
(near the top of their gaps).  If B extended by at most |B| - 2 runs on one side reaches mass >= 2 Delta - 1, a split of that
extension into two parts shorter than B is (B')-good and gives c <= 0 there, a contradiction; so B lies in a long light stretch.
(Proof: Lemma C1(c) and C2 applied to the split of the shortest jump.)
What is missing in (T): an argument excluding light intervals with c = 1 in long light stretches.  The exact obstruction is
local: e.g. for p = 13, kappa = 3, k = 19 (all runs of mass <= 1) a pair of adjacent empty runs with both singleton representatives
at the top of their gaps (w = 6) has c = 1 locally; any proof must use intervals beyond that pair.

## 3. Regime (III)

There (A') can fail (two light parts and R < 4 kappa - (m1 + m2) roughly), so c is not superadditive and may be negative; Lemma C2
does not apply.  The B0S Case I greedy can violate (L3) (the p = 7, kappa = 3, R = 7 example of proof-B0SP-r1.md Sec. 4) while a pair
of defects kills.  Needed: a substitute for SIGMA and a selection lemma.  Not attempted in writing.

## 4. Finite aids (not premises)

* E11 (plan-E11.md 2ff0da78...28a5, out/e11_sigma_search.json): no interval-feasible datum with sum w != p among 436,534 random
  assignments with sum w in {0, 2p}, p = 7, 11, 13.
* E12 (plan-E12.md b1026438...9e5f, out/e12_thin_dfs.json e8748f2b...6ab0): one thin datum (T-type parameters p = 13, kappa = 3,
  k = 19): 218,273 interval-feasible leaves within 400,000 DFS nodes, all J = 0; first 20 killed by 2-interval patterns.
* E13 (plan-E13.md 3486ab6f...9435, code/e13_regime3_p7.py 2ff1faea...a974, out/e13_regime3_p7.json 759c3a5b...87b0):
  regime (III) family p = 7, kappa = 3, k = 13, R = 7: all 132 run data up to rotation; 1,604,737 interval-feasible assignments
  enumerated (<= 20,000 DFS nodes per datum, so not exhaustive), all with J = 0; 3,960 of them tested against all patterns, every
  one killed by a pattern with 2 intervals (minimal m = 2 throughout); 0 unkilled.
These suggest that SIGMA holds at the interval level in both open regimes and that 2-interval kills suffice, but nothing here is
a proof.
