# Theorem B0S-CJ': Theorem B0S-CJ with (H) weakened to R >= 4 kappa - 1

Owner OlsonReflectionRigidity.  Written after host clock 2026-10-18T07:11:53-0700.  Status: written proof [W], UNREVIEWED.  This is a
separate increment; proof-B0SCJ-r1.md (a775321c...40af) and proof-B0SPP-r5.md (d388d391...bd64) stay frozen and unchanged.
Scope: B = 0 only.  It takes two values of R per kappa out of regime (III), namely R = 4 kappa - 1 and R = 4 kappa; regime (III)
with R <= 4 kappa - 2 stays open.

## 0. Statement

**Theorem B0S-CJ'.**  Theorem B0S-CJ (proof-B0SCJ-r1.md Sec. 0), together with Corollaries 1 and 2 and the Containment remark,
holds verbatim when (H) R >= 4 kappa + 1 is replaced by
   (H') R >= 4 kappa - 1.
The parameter claim for p <= 23 in Corollary 2 (B0SCJ-r1 L24-28) is NOT extended here; see Sec. 3.

## 1. Where (H) is used, and the replacement under (H')

The proofs in proof-B0SPP-r5.md Secs. 1-3 and proof-B0SCJ-r1.md use (H) only at the points below.  Each is re-proved under (H').
Throughout, w avoids, so R >= p >= 5, n_E <= 2 kappa, Delta <= kappa - 1 (B0SPP-r5 L53-55, from P0 only); also R <= 2p - 1.
1. **2 kappa <= p - 1 (B0SPP-r5 L55-56).**  From 4 kappa - 1 <= R <= 2p - 1 we get 2 kappa <= p, and p is odd.
2. **Windows nonempty (L59-61).**  The bound min(R - 2 kappa, (R - 1)/2 - kappa) >= min(2 kappa - 1, kappa - 1) >= 0.
3. **Lemma C2(a), (A') for every split (L81-83).**  "Small" means m <= 2 kappa, as there.
   - None small: >= (R - 3)/2 >= 0.
   - One small: >= R/2 - 1 - kappa >= -2, since R >= 2 kappa - 2.
   - Two small: >= (R - 1)/2 - 2 kappa >= -2, since R >= 4 kappa - 3.
   - Three small: = R - 3 kappa >= kappa - 1 >= -2.
4. **Lemma C2(b) (L83-86).**  The pair sums s1, s2, s3 add up to 2R.  Any two add up to R + (mass of the part they share) >= R.
   - None small, or exactly one small: these two cases are proved exactly as in L84-86.  That proof needs only the other two pair
     sums to be floor terms, and they are > 2 kappa.  (B') holds iff the small one is >= 2 Delta - 1.
   - Two small, s1 and s2, sharing a part Q_b of mass m_b: then R + m_b = s1 + s2 <= 4 kappa, so m_b <= 4 kappa - R <= 1.  Also
     s3 = R - m_b >= 4 kappa - 2 >= 2 kappa - 1, so g(s3) = floor(s3/2) (B0SPP-r5 L56-57).  Hence
     (B') = (s1 - kappa) + (s2 - kappa) + floor((R - m_b)/2) >= R + m_b - 2 kappa + (R - m_b - 1)/2.
     The condition (B') >= p - 2 = R - kappa - 1 + Delta follows from (R + m_b + 1)/2 - kappa >= Delta.  The left side is
     >= (4 kappa - 1 + 1)/2 - kappa = kappa > Delta.  So (B') holds; it holds a fortiori when all three pair sums are
     >= 2 Delta - 1, which is the statement of C2(b).
   - Three small: 2R <= 6 kappa contradicts R >= 4 kappa - 1 >= 3 kappa + 1 when kappa >= 2.  When kappa = 1 it contradicts
     R >= p >= 5.
   So C2(b) holds verbatim under (H'), and C2(c) follows from C2(a) as written (L87).
5. **Lemma SIGMA-2P for Delta <= 0 (L89-90).**  It uses only C2(b) and C1(c).
6. **Sec. 3, the kill (L103-114).**  Each inequality listed there, re-checked under (H') together with 2 kappa <= p - 1
   and k >= 2 kappa + 1:
   - Case I (L106-108):
     - (U1), (L1): Phi(P) <= 4 kappa <= 2p.
     - (L2): R >= 3 kappa + 1.  It holds when kappa >= 2 (4 kappa - 1 >= 3 kappa + 1), and when kappa = 1 since R >= 5.
     - (L3): R >= 4 kappa - 1, which is exactly (H').
   - Case II (L109-114):
     - (U3) and the containment |F| >= d/2 are generic.
     - (L3): 2 kappa - 2 <= R - 1.
     - (U1): r_y + 1 <= 2p, and 3 kappa - 7 < 2p.
     - (L1): 4 kappa - 4 < 2p.
     - (L2): R >= 4 kappa - 5 (W = {y}), resp. R >= 3 kappa - 1.
   All of these hold.
7. **proof-B0SCJ-r1.md.**
   - Facts (F1), (F2) (L35-37) use P0 and 2 kappa <= p - 1 only.
   - Lemma CJ, the Theorem and Corollaries 1-2 use only C1, C2, (F1) and (F2).  In particular the condition p >= kappa + 5 Delta - 5
     of Corollary 2 and its proof are unchanged.
   - The Containment remark is regime-free.
So every step holds under (H').  []

## 2. Remark on the boundary

(H') is where Case I's (L3) stops: the greedy P may have Phi(P) = 4 kappa, so delta_P <= 4 kappa - 2 is needed to be <= R - 1.
The other ingredients survive slightly further: C2(a) down to R >= 4 kappa - 3, and C2(b) down to 3R >= 2p + 4 kappa - 3 (worst
case m_b = 0).  Below R = 4 kappa - 1, the Case I selection must be changed.  This is consistent with notes-B0L-open-r1.md Sec. 3:
for p = 7, kappa = 3, R = 7 the greedy violates (L3) while a pair of defects kills.

## 3. Coverage of the two new R-values

Cells (p, kappa, R, Delta, k) with R in {4 kappa - 1, 4 kappa}, k >= p + 1, Delta <= kappa - 1 and p <= R <= 2p - 1, for p <= 61:
248 of them.
* Delta <= 1 is covered by Corollary 2 (for Delta = 1 its condition reads p >= kappa) or by SIGMA-2P.
* For Delta >= 2 it is covered when p >= kappa + 5 Delta - 5.
* For p <= 61 the condition fails in 20 cells.  The first five are (19, 5, 19, 4, 29), (23, 6, 23, 5, 35), (31, 8, 31, 7, 47), (31, 8, 32, 6, 46), (37, 10, 39, 7, 55).
In particular the p <= 23 claim of B0SCJ-r1 (which concerns R >= 4 kappa + 1) does not extend to R = 4 kappa: (19, 5, 19) and
(23, 6, 23) are open.  The cells for p = 7 are (p, kappa, R, Delta, k) = (7,2,7,1,11), (7,2,8,0,10), (7,3,11,-2,9) and (7,3,12,-3,8),
all with Delta <= 1, so all four are covered.
(Enumeration in the eval transcript of this worker, 07:11 PDT.  It is a parameter check only; no word data is involved.)
