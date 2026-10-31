# Actual Tuscan11 distinct-centre 4+4, class (a)-II, two-row P2 with both cuts in P6 — thread-chain reduction

Actual `/bin/date` before this body: **Mon Oct 26 04:58:00 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting

Class (a)-II with r_P2 = 2 and eps_v = eps_w = 0: both cuts lie in P6, and a_v = a_w = 1. Notation is that of v49 (SHA256 `0b02a602b2d03bbea47fc5db072da4d0cba5395900f31c75301dcccadf67ded9`): l = |T1|, H1 = P6[0,35], H2 = P6[W,W+35], K = W+l. Each run has 2+2 = 4 run vertices.

By v49 the configuration X = X' = 1 is impossible, where X = 1 means the v-cut lies in H1's v-run and X' = 1 means the w-cut lies in H2's w-run. Exchanging v and w swaps H1 and H2, so take **X = 0**.

The four v's b_v(0), c1, c2, b_v(35) then fill four consecutive rows B_0..B_3, with **B_j = H1[10j-o0, 10j+10-o0]**. Here o0 in 1..4 is b_v(0)'s offset (b_v(35) has offset o0+5).

H2's rows are **D_i = H2[e+10(i-1), e+10i]**:
- if X' = 1: i in 0..4 and e = beta2 in 0..5;
- if X' = 0: i in 1..4 and e = -p0, where p0 in 1..4 is b_w(W)'s offset in D_1.

Put **Sigma = l + o0 - e**.

Imports: v49 §4 rule (R) and the bd clash; one cut per label; (F2); DUP.

## 2. Two chain lemmas

On a thread, an H1-row and an H2-row run opposite ways. Call such a pair **clean** if they overlap there and do not both leave the thread through the same end. Leaving through the same end sends them into different threads, which would put exclusive parts on one side. A clean pair satisfies rule (R) with k the difference of their starts.

**bd chain.** Clean pairs (X1,Y1) and (X2,Y2) with starts a, a+4, a+10, a+14 are impossible. Rule (R) with k = 4 applies twice around the 5-path [a+10, a+14].

**Shift-5 lemma.** Clean pairs (W1,W2) and (W3,W4) with starts a, a+5, a+10, a+15 are impossible.

*Proof.* By rule (R) with k = 5, labels[a,a+4] = labels[a+11,a+15] and labels[a+10,a+14] = labels[a+21,a+25]. Let Q be the four labels of [a+11,a+14], a common thread stretch. The 5-paths [a,a+4] and [a+21,a+25] carry Q plus one more label, so each has at least 2 edges inside Q. The path [a+11,a+14] has 3. That is seven vertex-disjoint physical edges on the 6 pairs of Q, contradicting (F2). QED

## 3. Thread coordinates

On T1 (b_v at 0, b_w at l):
- B_j = [10j-o0, 10j+10-o0];
- D_i = [Sigma-o0-10i, Sigma-o0-10i+10].

On T2 (b_v at 0, b_w at 35-l):
- B_j = [o0+25-10j, o0+35-10j];
- D_i = [o0-Sigma+10(i-1), o0-Sigma+10i].

With n = i+j, **k = |Sigma - 10n| on T1** and **k = |Sigma + 35 - 10n| on T2**.

Rows leave the threads as follows:
- **T1:**
  - B_0 always leaves low, into T4.
  - B_j leaves high iff 10j+10-o0 > l.
  - D_i leaves low iff l-e < 10i.
  - The first H2-row leaves high, into T3: D_0 if X' = 1, D_1 if X' = 0. No other D_i does.
- **T2:**
  - B_3 always leaves low, into T3.
  - B_j leaves high iff l > 10j-o0.
  - D_i leaves low iff 10(i-1) < l-e.
  - Only D_4 leaves high, into T4.

## 4. X' = 1 is impossible

Sigma lies in [-3, 38].

| Sigma | Thread | Contradiction |
| --- | --- | --- |
| -3, -2 | T2 | (B_1,D_2), k = 2, 3 |
| -1 | T2 | bd chain D_1,B_2,D_2,B_1 |
| 0 | T2 | shift-5 chain D_1,B_2,D_2,B_1 |
| 1 | T2 | bd chain B_2,D_2,B_1,D_3 |
| 2..8 | T2 | (B_2,D_2), k = \|Sigma-5\| |
| 9 | T2 | bd chain D_2,B_2,D_3,B_1 |
| 10 | T2 | shift-5 chain D_2,B_2,D_3,B_1 |
| 11 | T2 | bd chain B_3,D_2,B_2,D_3 (D_2 does not leave low, since 11-o0 <= 10) |
| 12..18 | T2 | (B_2,D_3) |
| 17..23 | T1 | (B_1,D_1), clean because B_1 never leaves low and D_1 never leaves high |
| 24 | T1 | bd chain B_0,D_2,B_1,D_1 (D_2 does not leave low, since 24-o0 >= 20) |
| 25 | T1 | shift-5 chain D_2,B_1,D_1,B_2 |
| 26 | T1 | bd chain D_2,B_1,D_1,B_2 |
| 27..33 | T1 | (B_1,D_2) |
| 34 | T1 | bd chain B_1,D_2,B_2,D_1 |
| 35 | T1 | shift-5 chain D_3,B_1,D_2,B_2 (D_3 does not leave low) |
| 36 | T1 | bd chain D_3,B_1,D_2,B_2 |
| 37, 38 | T1 | (B_2,D_2) |

Every comparison uses two distinct rows. The formulas for B_j and D_i hold whether or not one physical row is shared by both runs (B_3 = D_0 or B_0 = D_4), so this covers both the no-shared-row and one-shared-row cases.

## 5. X' = 0 leaves two values

Sigma lies in [3, 42].

| Sigma | Thread | Contradiction |
| --- | --- | --- |
| 3..8 | T2 | (B_2,D_2) |
| 9 | T2 | bd chain D_2,B_2,D_3,B_1 |
| 10 | T2 | shift-5 chain D_2,B_2,D_3,B_1 |
| 11 | T2 | bd chain B_3,D_2,B_2,D_3 |
| 12..18 | T2 | (B_2,D_3) |
| 20 | T2 | shift-5 chain B_3,D_3,B_2,D_4: D_3 does not leave low and B_2 does not leave high, since l = 20-o0-p0 |
| 21 | T2 | bd chain B_3,D_3,B_2,D_4 |
| 22, 23 | T1 or T2 | (B_1,D_1) on T1 if p0 <= Sigma-20, else (B_2,D_4) on T2 |
| 24 | T1 | bd chain B_0,D_2,B_1,D_1 |
| 25 | T1 | shift-5 chain B_0,D_2,B_1,D_1 |
| 27..33 | T1 | (B_1,D_2) |
| 34 | T1 | bd chain B_1,D_2,B_2,D_1 (B_2 does not leave high) |
| 35 | T1 | shift-5 chain D_3,B_1,D_2,B_2 |
| 36 | T1 | bd chain D_3,B_1,D_2,B_2 |
| 37..42 | T1 | (B_2,D_2) |

Two values survive, because their small-k pairs leave through a common end:
- **Sigma = 19:** l = 19-o0-p0. (B_1,D_1) on T1 both leave through b_w, (B_0,D_2) on T1 both leave through b_v, and T2's only clean k = 4 pair is (B_2,D_3).
- **Sigma = 26:** l = 26-o0-p0. (B_2,D_4) and (B_3,D_3) on T2 have k = 1 but leave through common ends, and T1's only clean k = 4 pair is (D_2,B_1).

## 6. Result

In class (a)-II with r_P2 = 2 and both cuts in P6, every configuration is impossible except two. In both, X = X' = 0 (neither cut lies in its own run) and l + o0 + p0 is 19 or 26.

With v47, v48 and v49, every other r_P2 = 2 configuration is excluded.

Still open: those two values, (a)-II with r_P2 = 3, 4, 5, class (b), distinct 3+5, and all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
