# Actual Tuscan11 distinct-centre 4+4, class (a)-II, three-row P2 with four-row runs — reduction to one value

Actual `/bin/date` before this body: **Mon Oct 26 05:18:03 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting

Class (a)-II with **r_P2 = 3**: |T1|+|T2| = 25, |T3|+|T4| = 30, P6 has eight rows and P2 three. Write l = |T1|, H1 = P6[0,25] = T1 b_w T2^- and H2 = P6[W,W+25] = T1^- b_v T2.

H1's v-run consists of b_v(0), the first visits of the n_v = 1+eps_v v-copies on T1 and T2, and b_v(25). It fills 3+eps_v+X consecutive rows, where X = 1 when the v-cut lies in the run. This packet treats the case where **both runs fill four rows**. On the H1 side that happens exactly when eps_v + X = 1; on the H2 side, exactly when eps_w + X' = 1.

The four H1-rows are **B_j = H1[10j-o0, 10j+10-o0]** (j = 0..3), where o0 in 5..10 is b_v(0)'s offset; o0 = 10 or 5 only when b_v(0) or b_v(25) is the v-cut. Likewise **D_i = H2[10i-p0, 10i+10-p0]** (i = 0..3) with p0 in 5..10. Put **Sigma = l + o0 + p0**, which lies in [11, 44].

Imports: v49 §4 rule (R) and the bd clash, both v49 (SHA256 `0b02a602b2d03bbea47fc5db072da4d0cba5395900f31c75301dcccadf67ded9`); clean pairs, bd chains and the shift-5 lemma, all v50 (SHA256 `b7bcd3730661be24c9f1dd218254ff6881821c06ab1402cbbd690f3e7e5ac5bc`).

## 2. Thread coordinates

| Thread | B_j | D_i | k with n = i+j |
| --- | --- | --- | --- |
| T1 (b_v at 0, b_w at l) | [10j-o0, 10j+10-o0] | [Sigma-o0-10-10i, Sigma-o0-10i] | \|10(n+1) - Sigma\| |
| T2 (b_v at 0, b_w at 25-l) | [15+o0-10j, 25+o0-10j] | [10i-Sigma+o0, 10i+10-Sigma+o0] | \|Sigma + 15 - 10n\| |

Rows leave the threads as follows.
- **T1:**
  - B_0 always leaves low, and D_0 always leaves high.
  - B_j leaves high iff Sigma-p0 < 10(j+1).
  - D_i leaves low iff Sigma-o0 < 10(i+1).
- **T2:**
  - B_3 always leaves low, and D_3 always leaves high.
  - B_j leaves high iff Sigma-p0 > 10j.
  - D_i leaves low iff Sigma-o0 > 10i.
  - B_0..B_2 never leave low, and D_0..D_2 never leave high (p0 >= 5).

So **every pair with i, j in {1, 2} is clean on both threads**.

## 3. Every Sigma except 21 and 34 fails

The always-clean pairs (i, j in {1,2}, so n = 2, 3, 4) give:
- k <= 3 on T1 for Sigma in 27..33 and 37..43;
- k <= 3 on T2 for Sigma in 12..18 and 22..28.

The remaining values are:

| Sigma | Thread | Contradiction |
| --- | --- | --- |
| 11 | T2 | bd chain B_2,D_1,B_1,D_2 |
| 19 | T2 | bd chain D_1,B_2,D_2,B_1 |
| 20 | T2 | shift-5 chain D_1,B_2,D_2,B_1 |
| 35 | T1 | shift-5 chain D_2,B_1,D_1,B_2 |
| 36 | T1 | bd chain D_2,B_1,D_1,B_2 |
| 44 | T1 | bd chain B_1,D_2,B_2,D_1 |

The survivors are **Sigma = 21** (l = 21-o0-p0) and **Sigma = 34**.

**Survivor Sigma = 21.**
- On T1 the k = 1 pairs (B_0,D_1) and (B_1,D_0) leave through a common end: through b_v, since D_1 leaves low as 21-o0 < 20; and through b_w, since B_1 leaves high as 21-p0 < 20.
- On T2 the k = 4 pairs (B_1,D_3) and (B_3,D_1) leave through common ends. (B_2,D_2) is the only clean k = 4 pair, so no chain forms.

**Symmetry.** Row reversal maps o0 to 15-o0, p0 to 15-p0 and l to 25-l, hence Sigma to 55-Sigma, and it keeps the class and the four-row shapes. So **Sigma = 34 is the mirror of Sigma = 21**.

## 4. Result

In class (a)-II with r_P2 = 3, if both runs fill four rows then Sigma = l+o0+p0 = 21 up to row reversal.

This shape covers three cut placements:
- both cuts in P2;
- one cut in P2, with the other face's cut in its run;
- both cuts in P6, each in its own run.

In the 21-configuration T1 is short (l = 21-o0-p0 <= 11), and only one clean k = 4 pair occurs, on T2.

Still open:
- that value, which needs the T3/T4 rows and P2;
- r_P2 = 3 with a three-row run;
- r_P2 = 4 and 5;
- class (b), distinct 3+5, and all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
