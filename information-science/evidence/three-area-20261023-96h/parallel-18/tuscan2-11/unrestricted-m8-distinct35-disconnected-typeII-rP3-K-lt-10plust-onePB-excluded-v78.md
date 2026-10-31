# Actual Tuscan11 distinct 3+5, disconnected, Type II with r_P = 3, case (1,1) with K < 10+t and one P-boundary on B — excluded

Actual `/bin/date` before this body: **Mon Oct 26 11:26:56 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

**Imports:**
- v76 (SHA256 `a2218f8fb409011ea8d0279d2b75ec3a8066af584afde61bc0dcfdbb8bf1b9a8`): Lemma W and the Type II, r_P = 3 frame of §4(a);
- v77 (SHA256 `c5dabb9939e0bb6e25221f233e8239a9184d324adca7daea35201e88b58f62d7`): Lemma U.

## 1. The O-rows

Here n_A^w = n_B^w = 1. O's rows are Q_a = (K−10, K), Q_b = (K, K+10), M1 = (K+10, K+20), Q_c = (K+20, K+30), Q_d = (K+30, K+40) and M2 = (K+40, K+50). Assume K < 10+t; the frame gives K ∈ (15, 25) ∩ (5+t, 15+t).

- Since t < K < 10+t, b_v(30+t) lies in Q_c, so Q_c = B[ρ−10..1], v, C[1..c−1], w, D[t−1..τ], with ρ = 20+t−K > 10 and τ = 15+t−K.
- M1 = B[ρ..ρ−10] lies inside B.

**Lemma W fixes the copies.**
- The self-dual v-copy cannot lie on C (its forward visit would be a second v in Q_c). So it lies on D at some u. Its backward visit avoids Q_c, so u < τ, and Q_d's v is this copy.
- Hence b_v(0) is not in Q_d, which forces K < 20 and b_v(0) ∈ M2 = C[20−K..1], v, A[1..K−10].
- M1 holds the B w-copy b_w' and needs a v, so one cross v-copy b_v' lies on B inside M1.
- M2 holds the A w-copy a_w ∈ (0, K−10).

## 2. One P-boundary on B

P's rows are:
- R_P1 = A[10−β_P..1], v, B[1..β_P];
- R_P2 = B[β_P..y−1], w, A[x−1..20−β_P];
- R_P3 = A[20−β_P..10−β_P], which lies inside A.

**Placing the copies by Lemma W.**
- R_P3 needs one v and one w, both from A-copies. So a_w and the second cross v-copy a_v both lie in (10−β_P, 20−β_P), with a_v ∈ (K−10, x) on Q_a's side.
- Hence Q_b's v is the D-copy's forward visit, so σ < u < τ.
- R_P1's w must be b_w', so b_w' < β_P.
- R_P2's v must be b_v', so b_v' > β_P.
- Thus ρ−10 < b_w' < β_P < b_v' < ρ.

**No v–w edge exists.**
- **b_v–b_w:**
  - A has two P-boundaries, so x ≥ 11.
  - y > ρ > 10.
  - C has length at least 2: c = 1 would need t = 14, and then K ∈ (19, 20), which contains no integer.
  - D is a loop.
- **v-copy next to b_w:** a_v < 20−β_P < x; b_v' < ρ < y; and 2 ≤ u ≤ t−2, since σ ≥ 1 and τ ≤ t−1.
- **w-copy next to b_v:** a_w > 10−β_P ≥ 1 and b_w' > ρ−10 ≥ 1.
- **v-copy next to w-copy:**
  - On A, the O-cut A[K−10] separates a_w from a_v.
  - On B, the P-cut B[β_P] separates b_w' from b_v'.
  - D carries no w-copy.

This contradicts Lemma U. **Excluded (WRITTEN).**

## 3. Remaining Type II, r_P = 3 survivors

After v76, v77 and this packet, three Type II, r_P = 3 cases remain open:
- **S1:** (0,2), with 10 < K < 15, two P-boundaries on B and β_P = 6+t−K, together with its (2,0) mirror.
- **S2:** (1,1) with K > 20, one P-boundary on B and K+β_P = 26.
- **S2′:** (1,1) with K < 10+t and two P-boundaries on B.

Type II with r_P = 2 and Type I with r_P = 3, 4 remain open; so do R4 and R6.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
