# Actual Tuscan11 distinct-centre 4+4, class (a)-II, two-row P2 — three-row frame theorem

Actual `/bin/date` before this body: **Mon Oct 26 04:27:44 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting

Class (a)-II, cut counts and the row formula r_P2 = 1+a_v+eps_v = 1+a_w+eps_w are as in v47 §1 (v44 pin `c520658a683cb9acea9e9df9905d46f9a3e7688b3e4887f496dee58c1da6a805`). Take **r_P2 = 2**: |T1|+|T2| = 35, |T3|+|T4| = 20, P6 has nine rows.

Write l = |T1|, W = 35+|T3|, K = W+l. Put H1 = P6[0,35] = T1 b_w T2^- (from b_v(0) to b_v(35)) and H2 = P6[W,W+35] = T1^- b_v T2. Identify b_v = T1[0] = T2[0] and b_w = T1[l] = T2[35-l]. In H1-coordinates (origin 0), T1[s] sits at s and T2[s] at 35-s. In H2-coordinates (origin W), T1[s] sits at l-s and T2[s] at l+s.

Let **beta1** be the least h >= 0 such that h is a P6-boundary, and **beta2** the least h >= 0 such that W+h is one.

Imports: one cut per label; (F2) each unordered label pair is one physical edge; DUP for 2 and 3 labels; and the four-label remark of v21 (T4) (SHA256 `770ed4f5356e2ed1e0084f444c0dda1a33a6c79deaee2c4bb1b981fba02b8589`): vertex-disjoint paths on the same four labels use all six pairs, i.e. they are complementary P4s.

## 2. Statement and scope

**Theorem.** beta1 <= 5 and beta2 <= 5 cannot both hold.

**When the hypothesis holds.** H1's v-run consists of b_v(0), the first visits of the n_v = 3-a_v v-copies on T1 and T2, and b_v(35). These are consecutive v's of P6. They fill n_v+2+X consecutive rows, where X = 1 when the v-cut is one of them. Five rows meet H1 exactly when beta1 <= 5, and four otherwise. Since n_v = 2+eps_v, **beta1 <= 5 iff eps_v + X = 1**: either the v-cut is in P2, or it lies in H1's v-run. The same holds for beta2 with w and H2's w-run.

## 3. The frame

Each of S1 = P6[beta1, beta1+30] and S2 = P6[W+beta2, W+beta2+30] is three whole rows, inside H1 and H2 respectively. Use relative coordinates r in [0,30], so rows are [0,10], [10,20], [20,30] and 0, 10, 20, 30 are boundaries.

Put **Sigma = l - beta1 - beta2**, which lies in [-9,34].
- T1[s] (0 <= s <= l) has r1 = s-beta1 in S1 and r2 = l-beta2-s in S2, so **r1+r2 = Sigma**.
- T2[s] has r1 = 35-beta1-s and r2 = l-beta2+s, so **r1+r2 = 35+Sigma**.
- b_v and b_w fit both formulas.

The vertices met by both windows are:
- **A** = [max(0,Sigma-30), min(30,Sigma)] (T1-side), reflected about Sigma/2;
- **C** = [max(0,Sigma+5), min(30,Sigma+35)] (T2-side), reflected about (Sigma+35)/2.

All other positions are non-common, and they are the same positions in S1 and S2. In the main range they form the 4-position middle [Sigma+1, Sigma+4]. S1's and S2's non-common vertices are physically disjoint.

S2-row i (r2 in [10i-10,10i]) lands at S1-positions [Sigma-10i, Sigma-10i+10] where it lies in A, and at [Sigma+35-10i, Sigma+45-10i] where it lies in C.

## 4. Comparison rule

Let an S1-row Q and an S2-row Q' share one stretch of common vertices, which Q meets at one end and Q' at the other. Both rows are complete, so their remaining ends carry equal label sets, of a common size k.
- **k = 0:** the two rows have the same end vertices, so each end label is cut twice.
- **k = 1:** the lone end vertices carry one label, and both are cuts.
- **k = 2 or 3:** DUP.
- **k = 4:** the ends are complementary P4s.

Two k = 4 comparisons around one 5-path (a,b,c,d,e) give a contradiction. If one compares (b,c,d,e) with an end X and the other compares (a,b,c,d) with an end Y, then X is d-b-e-c and Y is c-a-d-b, so the pair {b,d} occurs on two physical edges. Call this the **bd clash**.

## 5. Every Sigma fails

| Sigma | Pair used | k | Why it fails |
| --- | --- | --- | --- |
| 0, 10, 20 | A[0] = S1[0] | – | A[0] is a cut, and its S2-position Sigma is a boundary |
| 5, 15, 25 | C[30] = S1[30] | – | C[30] is a cut, and its S2-position Sigma+5 is a boundary |
| 1..4 | S1-row 2 against S2-row 3 (C) | 5-Sigma | Sigma=4: C[20] and C[9] (S2-position 30) are both cuts; Sigma=2, 3: DUP; Sigma=1: also S1-row 3 against S2-row 2 (ends C[27,30] and C[16,19]), bd clash on C[16,20] |
| 6..8 | S1-row 2 = M[10,Sigma+4]+C against S2-row 3 | Sigma-5 | Sigma=6: M[10] and C[21] (S2-position 20) are both cuts; DUP otherwise |
| 9 | S1-row 1 = A[0,9]+M[10] against S2-row 1 = A+M'[10] | – | M[10] and M'[10] share a label, and both are cuts |
| 11..14 | S1-row 1 against S2-row 1 (A) | Sigma-10 | Sigma=11: A[0] and A[11] (S2-position 0) are both cuts; Sigma=12, 13: DUP; Sigma=14: S1-row 3 against S2-row 3 gives k=1, with C[30] and C[19] (S2-position 30) both cuts |
| 16 | S1-row 3 = M[20]+C against S2-row 3 = M'[20]+C | – | M[20] and M'[20] share a label, and both are cuts |
| 17..19 | S1-row 2 = A[10,Sigma]+M against S2-row 1 | 20-Sigma | Sigma=19: M[20] and A[9] (S2-position 10) are both cuts; DUP otherwise |
| 21..24 | S1-row 1 against S2-row 2 (A) | Sigma-20 | Sigma=21: A[0] and A[11] (S2-position 10) are both cuts; Sigma=22, 23: DUP; Sigma=24: also S1-row 2 against S2-row 1 (ends A[10,13] and A[21,24]), bd clash on A[10,14] |
| 26..29 | S1-row 3 = A[20,Sigma]+M against S2-row 1 | 30-Sigma | Sigma=29: S1[30] and A[19] (S2-position 10) are both cuts; Sigma=27, 28: DUP; Sigma=26: also S1-row 2 against S2-row 2 (ends A[17,20] and A[6,9]), bd clash on A[16,20] |
| 30 | S1-row 3 against S2-row 1 | 0 | k = 0 |
| 31..34 | S1-row 3 against S2-row 1, whose head S2[0,Sigma-31] lies beyond S1 | Sigma-30 | Sigma=31: S1[20] and S2[0] are both cuts; Sigma=32, 33: DUP; Sigma=34: also S1-row 2 against S2-row 2 (ends A[10,13] and A[21,24]), bd clash on A[20,24] |
| -5 | S1-row 1 against S2-row 3 | 0 | k = 0 |
| -4..-1 | S1-row 1 = M[0,Sigma+4]+C against S2-row 3 | Sigma+5 | Sigma=-4: S1[0] and C[11] (S2-position 20) are both cuts; Sigma=-3, -2: DUP; Sigma=-1: also S1-row 2 against S2-row 2 (ends C[10,13] and C[21,24]), bd clash on C[10,14] |
| -9..-6 | S1-row 1 (inside C = [0,35+Sigma]) against S2-row 3, whose tail S2[36+Sigma,30] lies beyond S1 | -5-Sigma | Sigma=-6: S1[10] and S2[30] are both cuts; Sigma=-7, -8: DUP; Sigma=-9: also S1-row 2 against S2-row 2 (ends C[17,20] and C[6,9]), bd clash on C[6,10] |

In each comparison the common stretch lies entirely in A or entirely in C, and it is met at opposite ends, so the rule of §4 applies. The two ends are distinct vertices (A-, C-, M- or M'-positions differ). This covers every Sigma from -9 to 34. QED

## 6. Result

In class (a)-II with r_P2 = 2, every configuration with beta1 <= 5 and beta2 <= 5 is impossible.
- This re-proves v47 (eps_v = eps_w = 1) and the final step of v48 (SHA256 `aa59b87c9ceb6566a80b883fc70179f0dc6cbd947be28f9ab9c572f2268b1df0`), whose §6 frame is the case beta1 = 1.
- When both cuts lie in P6, the v-cut must avoid H1's v-run or the w-cut must avoid H2's w-run. Exchanging v and w swaps H1 and H2, so assume the former.
- Still open in (a)-II: that case and r_P2 = 3, 4, 5. Also open: class (b), distinct 3+5, and all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
