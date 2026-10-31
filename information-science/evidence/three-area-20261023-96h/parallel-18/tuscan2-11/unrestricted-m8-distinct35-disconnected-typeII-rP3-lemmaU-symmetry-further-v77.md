# Actual Tuscan11 distinct 3+5, disconnected, Type II with r_P = 3 — the unique v–w edge, a reversal symmetry, a D-lemma and four more excluded sub-cases

Actual `/bin/date` before this body: **Mon Oct 26 11:19:35 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Imports

- v60 (SHA256 `d09ec901a98a25480d12b9c81622c43044f5c2415b196fb9d64bb71ae9ad6259`): the setting and the counts.
- v76 (SHA256 `a2218f8fb409011ea8d0279d2b75ec3a8066af584afde61bc0dcfdbb8bf1b9a8`): Lemmas W, T3 and C5, and the Type II, r_P = 3 frame of §4(a).
- (L1) of v57: no face has two consecutive rows inside a cross path.
- Rule (R), the bd chain and the shift-5 chain (v49 §4, v50 §2).
- The exchange identity and distinct cut labels.

**T3 for walks.** Lemma T3 also holds when a row's side at b_v is an initial segment of a longer walk (for example through b_w). The proof only needs, for each half-edge, the two rows' sides to be nested initial segments of one common walk from b_v.

## 2. Lemma U (exactly one v–w edge in H)

In a Tuscan-1 square every ordered pair occurs exactly once as consecutive entries. Every support edge is traversed once in each direction. So every unordered label pair is the label pair of exactly one support edge.

The reverse-pair component is the path v = x0, ..., x10 = w, and {v, w} is not one of its edges. Hence **exactly one edge of H joins a v-vertex to a w-vertex.**

## 3. Reversal symmetry of Type II

Reverse every row, swap the threads A ↔ B and reverse the loop D. Then P = B A^- and O = A D B^- C D^- C^- go to faces of the same form (after a cyclic rotation). The image is again a Tuscan-1 array with the same component structure.

This swaps the cross-path w-copy counts (n_A^w, n_B^w). So, for r_P = 3, the case (2,0) is the mirror of (0,2) and needs no separate treatment.

## 4. D-lemma (Type II, r_P = 3)

Let Q_c = (C-segment), w, D[t−1..τ] and Q_d = D[τ..1], w, (C-walk), with Q_c's C-segment contained in Q_d's C-walk. Let Q_a ⊇ D[1..σ] and Q_b ⊇ D[σ..t−1] as in v76. Suppose σ > τ.
- The partitions of Q_c and Q_d give {d_1..d_(τ−1)} ⊆ {d_(τ+1)..d_(t−1)}.
- Q_a contains D[1..σ], so these labels avoid d_(τ+1)..d_σ. Hence they lie in {d_(σ+1)..d_(t−1)}.

So σ+τ ≤ t. (The case σ < τ is symmetric and gives σ+τ ≥ t.)

## 5. Case (n_A^w, n_B^w) = (0,2)

O's rows are Q_a = (K−10, K), Q_b = (K, K+10), N1 = (K+10, K+20), N2 = (K+20, K+30), Q_c ∋ b_w(45) and Q_d ∋ b_w(45+t). So K ∈ (5, 15) and K < 5+t. Put ρ = 20+t−K > 15; then N1 = B[ρ..ρ−10] lies inside B.

**K < t.** Then N2 = B[ρ−10..t−K] also lies inside B. O has two consecutive rows inside the cross path B, against (L1). **Excluded.**

**t < K < 10.** Here b_v(0) ∈ Q_a, which contains all of A (since x < K). So A carries no copy, and both cross v-copies lie on B.
- N2 = B[ρ−10..1], v(30+t), C[1..K−t] has v = b_v(30+t). Lemma W then puts the B v-copies in N1 and Q_b, and the self-dual copy on C (with its forward visit in Q_c and its backward visit in Q_d).
- P has two boundaries on B and one on A, because y > 20 and (L1) holds. So R_P1 = A[10−β_P..1], v, B[1..β_P] and R_P* = B[β_P+10..y−1], w, A[x−1..10−β_P].
- T3 at b_v, with Q_a's A-side being the walk A[1..x−1], b_w, D[1..σ] of length K: R_P1's A-segment has length 10−β_P < x < K, so R_P1 is shorter on A. Hence it is not shorter on B against N2's B-side ρ−10, i.e. β_P > ρ−10. Hence K+β_P > 10+t.
- C5: R_P*'s A-segment (x−10+β_P) lies inside Q_a's A-walk, and its B-segment (y−β_P−10) is shorter than Q_b's (y−ρ) because K+β_P > 10+t. C5 gives a contradiction. **Excluded.**

**10 < K < 15, with P having one boundary on B.** Then P's b_w-row R_P2 = B[β_P..y−1], w, A[x−1..20−β_P] contains b_w.
- T3 forces β_P < ρ−10. So R_P2 also contains N1's B w-copy, which lies between ρ−10 and ρ.
- R_P2 then holds two w-visits, against Lemma W. **Excluded.**

## 6. Case (1,1) with K > 20, P having two boundaries on B

Here b_v(0) lies in Q_d = D[τ..1], w, C[c−1..1], v, A[1..K−20], with τ = 15+t−K. M2 = A[K−20..K−10] lies inside A.

**Lemma W fixes the copies.**
- The self-dual copy cannot lie on C, since its backward visit would give Q_d a second v. So it lies on D, at some u > τ, with its backward visit in Q_c. Then b_v(30+t) ∈ M1, so K > 10+t.
- M2's v and w are the A copies a_v1 and a_w.
- P's middle row P_mid = (β_P, β_P+10) lies inside B. So it holds the B w-copy b_w' ∈ (β_P, β_P+10) with b_w' < ρ, and the second cross v-copy b_v' ∈ (ρ, β_P+10), on B.
- Hence the D-copy's forward visit is in Q_a, giving τ < u < σ.
- R_P1 takes a_w < 10−β_P, and R_P* takes a_v1 > 10−β_P.

**No v–w edge exists.**
- **b_v–b_w:** A ⊇ M2 and B is long. C has length at least 2, since M1 and Q_c each meet C in at least one edge. D is a loop at b_w. So no thread joins b_v to b_w in one edge.
- **v-copy next to b_w:** a_v1 ≤ x−2 because K−10 < x. b_v' ≤ y−2 because b_v' < β_P+10 < y. The D-copy has u ∈ [2, t−2].
- **w-copy next to b_v:** a_w > K−20 ≥ 1 and b_w' > β_P ≥ 1.
- **v-copy next to w-copy:**
  - On A, the P-cut A[10−β_P] separates a_w from a_v1.
  - On B, the O-cut B[ρ] separates b_w' from b_v'.
  - D carries no w-copy.

This contradicts Lemma U. **Excluded.**

## 7. Result and exact remaining gap

**WRITTEN, conditional on v76's lemmas.** In Type II with r_P = 3, the following are now excluded:
- (0,2) with K < t;
- (0,2) with t < K < 10;
- (0,2) with 10 < K < 15 and one P-boundary on B;
- (1,1) with K > 20 and two P-boundaries on B.

By §3, the matching (2,0) sub-cases are excluded too. Together with v76 §4(b), what remains in Type II with r_P = 3 is:
- **(0,2), 10 < K < 15, two P-boundaries on B.** Rule (R) on B with the chains forces β_P = 6+t−K, with the B copies of N1 in (ρ−10, ρ−5]. Lemma U does not yet decide this case.
- **(1,1), K > 20, one P-boundary on B.** Rule (R) on A forces K+β_P = 26, and t ∈ (6, 12].
- **(1,1) with K < 10+t.** Not yet analysed.

Type II with r_P = 2 and Type I with r_P = 3, 4 remain open. R4 and R6 are unchanged.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
