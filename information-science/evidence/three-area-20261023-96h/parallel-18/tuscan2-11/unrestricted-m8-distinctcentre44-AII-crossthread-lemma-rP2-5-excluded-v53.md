# Actual Tuscan11 distinct-centre 4+4, class (a)-II — cross-thread lemma; r_P2 = 5 is impossible

Actual `/bin/date` before this body: **Mon Oct 26 05:27:00 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Cross-thread lemma

Class (a)-II is as in v47 §1 (v44 pin `c520658a683cb9acea9e9df9905d46f9a3e7688b3e4887f496dee58c1da6a805`). The cross threads T3 and T4 are each traversed once by P2 and once by P6, in opposite directions.

**Lemma.** Neither face has two consecutive rows lying entirely on the interior of one cross thread.

*Proof.* Let Q1 = [x, x+10] and Q2 = [x+10, x+20] be such rows of one face on the thread X. The other face's rows tile its cycle, which contains X, with boundaries at the positions congruent to some c mod 10. Put d = (c-x) mod 10.

Q1 and Q2 do not leave X, so each is clean against every overlapping row R of the other face. This is the clean-pair notion of v50 §2 (SHA256 `b7bcd3730661be24c9f1dd218254ff6881821c06ab1402cbbd690f3e7e5ac5bc`), and rule (R) of v49 §4 (SHA256 `0b02a602b2d03bbea47fc5db072da4d0cba5395900f31c75301dcccadf67ded9`) then applies with k equal to the difference of starts. R itself may leave X.

| d | Rows compared | Contradiction |
| --- | --- | --- |
| 0 | the vertex at x | it is a boundary of both faces, so its label is cut twice |
| 1, 2, 3 | Q1 against R = [x+d, x+d+10] | k = d <= 3 |
| 7, 8, 9 | Q1 against R = [x+d-10, x+d] | k = 10-d <= 3 |
| 4 | Q1, [x+4], Q2, [x+14] | bd chain (v50 §2) around [x+10, x+14] inside Q2 |
| 6 | [x-4], Q1, [x+6], Q2 | bd chain around [x+6, x+10] inside Q1 |
| 5 | Q1, [x+5], Q2, [x+15] | shift-5 lemma (v50 §2), with Q the labels of [x+11, x+14] inside Q2 |

QED

**Corollary.** Combine the lemma with v46 (SHA256 `d212cc7d2c8b7907187f0e20732206224cfa0cee0dcfedb41d874342e5d9c5ca`), by which T3 and T4 do not both carry a full row. Then P6 has **at most one row lying inside T3 or T4**, and so does P2.

Call a P6-row an **only-row** when its v is not one of H1's run v's and its w is not one of H2's run w's.
- An only-row meets neither H1 nor H2.
- So it lies inside T3 or T4.
- Hence **o <= 1**, where o counts only-rows.

## 2. r_P2 = 5 is impossible

With r_P2 = 5 we have a_v = 4 - eps_v <= 3, so eps_v = eps_w = 1. All six copies lie on T3 and T4, |T1|+|T2| = 5, and P6 has six rows with no v- or w-cut.

The consecutive v's b_v(0) and b_v(5) lie in consecutive rows R_0 and R_1, where R_k = [10k-o, 10k+10-o] and o is 6..9. The consecutive w's b_w(W) and b_w(W+5) lie in rows R_kW and R_kW+1.
- **kW = 0** leaves no row for b_w(l).
- **kW = 3** puts the only-rows R_2 on T3 and R_5 on T4 (v46).
- **kW = 1, 2** make R_3..R_5, respectively R_4 and R_5, consecutive rows inside T4.
- **kW = 4, 5** make R_2 and R_3, respectively R_2..R_4, consecutive rows inside T3.

The last two cases are excluded by the lemma. So **r_P2 = 5 is impossible**.

## 3. Consequences for r_P2 = 3 and 4

The row count of P6 is |R_V| + |R_W| - s + o, where s counts rows shared by the two runs.

**r_P2 = 3.** If both runs fill three rows (both cuts in P6, each off its own run), then o = s+2 >= 2. This is excluded. If exactly one run fills three rows, then o = 1 and s = 0. If both fill four rows, then o = s, which is 0 or 1, and v52 (SHA256 `c7d0b41044cda03fb4879c2c2b89594665e2c13dccd52d8cf3aff6868443fc45`) leaves Sigma = 21 up to reversal.

**r_P2 = 4.** Here o - s = 3 - eps_v - eps_w - X - X', and o <= 1. In every cut placement this gives **o = 1 and s = 0**: there is exactly one only-row, lying inside T3 or T4, and no shared row. When both cuts lie in P6, each must lie in its own run. When one cut lies in P6, it must lie in its run.

## 4. Result

The new results in class (a)-II are:
- the cross-thread lemma;
- r_P2 = 5 is impossible;
- r_P2 = 3 with two three-row runs is impossible;
- r_P2 = 4 has exactly one only-row and no shared row.

With v51, r_P2 = 2 is also impossible.

Still open in (a)-II:
- r_P2 = 3 with four-row runs (Sigma = 21) or with one three-row run;
- r_P2 = 4.

Also still open: class (b), distinct 3+5, and all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
