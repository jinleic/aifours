# Actual Tuscan11 distinct-centre 4+4, class (a)-II, r_P2 = 3 four/four shape (Sigma = 21) — reduction by cross-thread boundary tests

Actual `/bin/date` before this body: **Mon Oct 26 08:30:49 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. This is a successor to the separate, ungated v50-v65 line, not part of the v19-v49 freeze.

## 1. Setting

This is v52 (SHA256 `c7d0b41044cda03fb4879c2c2b89594665e2c13dccd52d8cf3aff6868443fc45`) with both runs of four rows and **Sigma = l+o0+p0 = 21**. Write A = o0 and P = p0, both in 5..10. Then:
- l = 21-A-P >= 1 and |T2| = 4+A+P;
- B_j = P6[10j-A, 10j+10-A] and D_i = P6[W+10i-P, W+10i+10-P].

By v53 §3 (SHA256 `73c0724422c1c9be9e63acab22f7c5f55ee7845d58063d7f8dff973610bd7c08`), o = s is 0 or 1.
- **(S0) s = o = 0.** The two runs tile P6, so W = 40+P-A, lam3 = |T3| = 15+P-A and lam = |T4| = 15+A-P.
- **s = o = 1.** The runs share one row. Either B_3 = D_0, with W = 30+P-A and the only-row P6[70-A, 80-A] inside T4 (**(S1)**), or B_0 = D_3, with the only-row inside T3. Exchanging v and w (v48 §1, SHA256 `aa59b87c9ceb6566a80b883fc70179f0dc6cbd947be28f9ab9c572f2268b1df0`) swaps the two runs and maps the second layout to the first, so take (S1).

Labels a_i, b_i, c_i, e_i are those of T1..T4 as in v61 (SHA256 `5dd3c58a33e185a94c8025cfb8213f8e68802e392bad379bf95ff283109cfa43`), with a_0 = b_0 = c_0 = e_0 = v and a_l = b_|T2| = c_lam3 = e_lam = w.

**Imports:**
- v49 §4 rule (R) and bd clash (SHA256 `0b02a602b2d03bbea47fc5db072da4d0cba5395900f31c75301dcccadf67ded9`): for opposed rows sharing one stretch met from opposite ends, with exclusive ends of size k, k = 0 or 1 doubles a cut label, k = 2 or 3 breaks DUP, and k = 4 gives complementary P4s;
- v50 §2 clean pairs, bd chain and shift-5 lemma (SHA256 `b7bcd3730661be24c9f1dd218254ff6881821c06ab1402cbbd690f3e7e5ac5bc`);
- distinct cut labels and (F2).

A pair is **clean** when its two rows do not both leave the thread through the same end.

## 2. (S0): rows and the cross threads

The rows are:
- B_0 = e_A..e1, v, a1..a_(10-A)
- B_1 = a_(10-A)..a_(l-1), w, b_(3+A+P)..b_(5+A)
- B_2 = b_(5+A)..b_(A-5)
- B_3 = b_(A-5)..b1, v, c1..c_(15-A)
- D_0 = c_(15-A)..c_(lam3-1), w, a_(l-1)..a_(11-A)
- D_1 = a_(11-A)..a1, v, b1..b_(A-1)
- D_2 = b_(A-1)..b_(A+9)
- D_3 = b_(A+9)..b_(3+A+P), w, e_(lam-1)..e_A

The P6 cuts are e_A, a_(10-A), b_(5+A), b_(A-5), c_(15-A), a_(11-A), b_(A-1) and b_(A+9).

In T3-coordinates, P6 runs T3 upward:
- B_3 = [5-A, 15-A], extended below 0 through b_v into T2;
- D_0 = [15-A, 25-A], extended above lam3 through b_w into T1.

In T4-coordinates, P6 runs T4 downward:
- B_0 = [A-10, A], extended below 0 into T1;
- D_3 = [A, A+10], extended above lam into T2.

P2 = T4 T3^- runs both threads the opposite way. Let r0 in 0..9 be b_v's offset in its P2 row. The P2 cuts are T4[u] with u ≡ -r0 and T3[t] with t ≡ r0 (mod 10). Put:
- **kappa = (15-A-r0) mod 10**, the distance from the P6 cut T3[15-A] down to the next P2 cut;
- **kappa' = (A+r0) mod 10**, the distance from T4[A] down to the next P2 cut;
- t1 = 15-A-kappa and u1 = A-kappa'.

Then **kappa + kappa' ≡ 5 (mod 10)**.

## 3. (S0): the boundary tests

**(a)** kappa, kappa' ≠ 0. Otherwise T3[15-A] or T4[A] is a cut of both faces.

**(b) r0 ≠ 0.** If r0 = 0, b_v is a P2 cut.
- The P2 row T3[10..1] b_v (lam3 >= 10) is clean against B_3 with k = A-5.
- The P2 row b_v T4[1..10] (lam >= 10) is clean against B_0 with k = 10-A.

Rule (R) needs both to be at least 4 (k = 0 is a doubled cut), which is impossible.

**(c)** Let r0 ≠ 0.
- If t1 >= 1, the P2 row Q' = [t1, t1+10] on T3 is clean against B_3 with k = 10-kappa, so kappa <= 6. It is clean against D_0 with k = kappa unless both leave T3 through b_w, which happens iff P < 10 and P < 10-kappa.
- If t1 < 0, the P2 row through b_v contains B_3's whole T3 part and leaves through b_v as B_3 does, so it gives nothing.
- Likewise on T4: if u1 >= 1, the row Q'' = [u1, u1+10] is clean against B_0 with k = 10-kappa', so kappa' <= 6. It is clean against D_3 with k = kappa' unless P > 5 and P > 5+kappa'.

**Consequences.**
- **kappa + kappa' = 15.** kappa >= 7 forces t1 < 0, i.e. kappa >= 16-A; kappa' >= 7 forces kappa' >= A+1. So (7,8) and (8,7) are impossible. This leaves **(6,9)** and **(9,6)**.
- **kappa + kappa' = 5.** kappa <= 3 gives t1 >= 2, so (D_0, Q') must be unclean: P < 10-kappa. kappa' <= 3 gives u1 >= 2, so P > 5+kappa'. Hence (2,3) and (3,2) are impossible, **(1,4)** needs P <= 8, and **(4,1)** needs P >= 7.

**Symmetry.** Exchanging v and w swaps (A, P) and turns T3 into the reversed T4. In this exchange B_3 becomes the old D_3, D_0 the old B_0, and the old Q'' becomes the new Q'. Matching their k-values gives (kappa, kappa') -> (10-kappa', 10-kappa). So (1,4) is the mirror of (6,9), and (4,1) is the mirror of (9,6). It suffices to treat (6,9) and (9,6).

## 4. (S0), type (6,9)

Here r0 = 9-A, so A <= 8. The P2 cuts are T4[A+1], T3[9-A] and T3[19-A]. The rows are:
- R_0 = c_(9-A)..c1, v, e1..e_(A+1)
- R_1 = e_(A+1)..e_(lam-1), w, c_(lam3-1)..c_(19-A)
- R_2 = c_(19-A)..c_(9-A), inside T3

The tests:
- **R_1 vs D_3** on T4 has k = 1, so it must be unclean. That needs D_3 to leave T4 high, i.e. **P >= 6**.
- **R_2 vs B_3** has k = 4. If P = 10, D_0 ends at b_w, so R_1 vs D_0 is clean with k = 4. The starts 5-A, 9-A, 15-A, 19-A then form a bd chain. So **P <= 9**.
- **R_0 vs B_0:** {c1..c_(9-A), e_(A+1)} = {a1..a_(10-A)}. The P2 cut labels c_(9-A) and e_(A+1) must lie in {a1..a_(9-A)}, which has at least two elements only if **A <= 7**.
- **R_1 vs D_3:** {c_(19-A)..c_(lam3-1)} = {e_A, b_(A+9)..b_(3+A+P)}. The P2 cut label c_(19-A) must lie in {b_(A+10)..b_(3+A+P)}, so **P >= 7**.

Survivors: **A in {5, 6, 7} and P in {7, 8, 9}.**

## 5. (S0), type (9,6)

Here r0 ≡ 6-A. A = 6 gives r0 = 0, and A = 5 gives t1 = 1 with k = 1 against B_3. So **A >= 7** and r0 = 16-A. The P2 cuts are T4[A-6], T4[A+4] and T3[16-A]. The rows are:
- R_0 = c_(16-A)..c1, v, e1..e_(A-6)
- R_1 = e_(A-6)..e_(A+4), inside T4
- R_2 = e_(A+4)..e_(lam-1), w, c_(lam3-1)..c_(16-A)

The tests:
- **R_1 vs B_0** has k = 4. If P = 5, D_3 ends at b_w, so R_2 vs D_3 is clean with k = 4. The starts A-10, A-6, A, A+4 then form a bd chain. So **P >= 6**.
- If P = 10, D_0 ends at b_w, so R_2 vs D_0 is clean with **k = 1**. So **P <= 9**.
- **R_0 vs B_3:** {c_(16-A), e1..e_(A-6)} = {b1..b_(A-5)}. The P2 cut labels c_(16-A) and e_(A-6) must lie in {b1..b_(A-6)}, so **A >= 8**.
- **R_2 vs D_0:** {e_(A+4)..e_(lam-1)} = {c_(15-A), a_(11-A)..a_(l-1)}. The P2 cut label e_(A+4) must lie in {a_(12-A)..a_(l-1)}, which is nonempty only if **P <= 8**.

Survivors: **A in {8, 9, 10} and P in {6, 7, 8}.**

## 6. (S1)

The rows are:
- B_0 = e_A..e1, v, a1..a_(10-A)
- B_1 = a_(10-A)..a_(l-1), w, b_(3+A+P)..b_(5+A)
- B_2 = b_(5+A)..b_(A-5)
- S = B_3 = D_0 = b_(A-5)..b1, v, c1..c_(lam3-1), w, a_(l-1)..a_(11-A)
- D_1 = a_(11-A)..a1, v, b1..b_(A-1)
- D_2 = b_(A-1)..b_(A+9)
- D_3 = b_(A+9)..b_(3+A+P), w, e_(lam-1)..e_(A+10)
- O = e_(A+10)..e_A

Here lam3 = 5+P-A >= 1 and lam = 25+A-P. O lies inside T4 and never leaves it. Its ends T4[A] and T4[A+10] are P6 cuts. A P2 cut there would double a cut, and the P2 cuts on T4 are 10 apart, so exactly one P2 cut T4[A+kappa''] has 1 <= kappa'' <= 9. The two P2 rows at that cut meet O cleanly, with k = kappa'' and 10-kappa''. So kappa'' is 4, 5 or 6.
- **kappa'' = 5.** (B_0, P2 row at A-5) is clean with k = 5, and (O, P2 row at A+5) also has k = 5. The starts A-10, A-5, A, A+5 contradict the shift-5 lemma.
- **kappa'' = 4.** (O, row at A+4) has k = 4.
  - If A >= 6, (B_0, row at A-6) is clean with k = 4, giving a bd chain A-10, A-6, A, A+4.
  - If P = 5, D_3 ends at b_w, and (D_3, row at A+14) is clean with k = 4, giving a bd chain A, A+4, A+10, A+14.
  - So A = 5 and P >= 6. The rows are R_0 = c1, v, e1..e9; R_1 = e9..e19; R_2 = e19..e_(lam-1), w, c_(P-1)..c1.
  - R_2 vs S gives {e19..e_(lam-1)} = {v, a6..a_(l-1)}. Here v is the label of the v-cut b_v(25) and a6 is a P6 cut, so the P2 cut label e19 lies in {a7..a_(l-1)}. Hence **P <= 8**.
- **kappa'' = 6.** (O, row at A-4) has k = 4. (D_3, row at A+6) is clean with k = 4 unless both leave T4 high, i.e. unless P = 10. So P = 10, because otherwise A-4, A, A+6, A+10 is a bd chain.
  - Then S ends at the w-cut b_w(W), and R_0 = c_(14-A)..c1, v, e1..e_(A-4).
  - S vs R_0 gives {b1..b_(A-5), w} = {e1..e_(A-4)}. The P2 cut label e_(A-4) lies in {b1..b_(A-6)}, so **A >= 7**.

Survivors: **(A = 5, P in {6, 7, 8}, kappa'' = 4)** and **(P = 10, A in {7, 8, 9, 10}, kappa'' = 6)**.

## 7. Result

In the four/four shape of distinct-centre 4+4, class (a)-II with r_P2 = 3 (residual R2 of manifest v12, SHA256 `1592f9e272a7f4daafc2f6ef67d1c20e63de3800f9625e52f8214f4a51efdda3`), every case is impossible except:
- **(S0) type (6,9)** with A in {5, 6, 7} and P in {7, 8, 9}, and its v<->w mirror, type (1,4) with (A, P) swapped;
- **(S0) type (9,6)** with A in {8, 9, 10} and P in {6, 7, 8}, and its mirror, type (4,1);
- **(S1)** with A = 5, P in {6, 7, 8} (kappa'' = 4), or P = 10, A in {7, 8, 9, 10} (kappa'' = 6), together with the mirror layout B_0 = D_3.

All these survivors have every cut position fixed. No survivor is claimed impossible here, and the label exchanges listed above are only part of each case. Other open lines are as in manifest v12 and v60.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
