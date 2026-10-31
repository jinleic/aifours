# Actual Tuscan11 distinct-centre 4+4 — self-dual thread lemma; class (b) with a two-row face is impossible

Actual `/bin/date` before this body: **Mon Oct 26 05:29:21 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Self-dual thread lemma

**Lemma.** Let a thread Y be traversed twice by one face, once in each direction (passes A and B). If pass A contains two consecutive rows lying inside Y's interior, there is a contradiction.

*Proof.* The face's row boundaries are one residue class mod 10 along the face. Pass B therefore meets Y in boundaries forming one residue class mod 10 in Y-coordinates, and its rows tile Y.

The two pass-A rows do not leave Y, so each is clean against every overlapping pass-B row (v50 §2, SHA256 `b7bcd3730661be24c9f1dd218254ff6881821c06ab1402cbbd690f3e7e5ac5bc`). Rule (R) of v49 §4 (SHA256 `0b02a602b2d03bbea47fc5db072da4d0cba5395900f31c75301dcccadf67ded9`) then applies with k the difference of starts. The table and chains of the cross-thread lemma, v53 §1 (SHA256 `73c0724422c1c9be9e63acab22f7c5f55ee7845d58063d7f8dff973610bd7c08`), apply word for word, with one change: for d = 0 the shared vertex is a boundary at both of its two visits, so its label is cut twice. QED

**Length form.** If Y has at least 30 interior vertices, pass A has two consecutive rows inside Y. Its first full window starts at one of the first ten interior positions, and the next window ends at most 20 positions later. So **a doubly traversed thread has at most 30 edges**.

## 2. Class (b)

Class (b) (v44, SHA256 `c520658a683cb9acea9e9df9905d46f9a3e7688b3e4887f496dee58c1da6a805`) has faces F_1 = T1 L_w T1^- L_v and F_2 = T2 L_w^- T2^- L_v^-. Put a = |T1|, b = |T2|, p = |L_v| and q = |L_w|, and let F_1 and F_2 have r_1 and r_2 rows. Then 2a+p+q = 10r_1 and 2b+p+q = 10r_2. Since r_1 + r_2 = 11, we get **b - a = 5d** with d = 11 - 2r_1 in {1, 3, 5, 7}.

F_2 traverses T2 twice and F_1 traverses T1 twice, so a and b are at most 30.

- **d = 7.** Here b = a+35 >= 36. So class (b) with a two-row face is impossible.
- **d = 5.** Here b = a+25 <= 30, hence a <= 5 and p+q = 30-2a >= 20. The pass of F_2 along T2 with first interior boundary beta' has two consecutive inside rows when beta' + 20 <= b-1. So b in 26..30 survives only when neither pass of T2 has that alignment.

## 3. Class (a)-II

P6 traverses T1 and T2 twice, so |T1| and |T2| are at most 30. This adds nothing new to v47-v53 (r_P2 = 2 is already closed).

## 4. Result

The new results are:
- the self-dual thread lemma;
- class (b) with d = 7 (a two-row face F_1) is impossible;
- in class (b) with d = 5, a <= 5, b <= 30 and p+q >= 20.

The cross-thread lemma (v53) applies verbatim to the loops L_v and L_w of class (b), since each loop is traversed once by each face in opposite directions. So neither face has two consecutive rows inside a loop.

Still open: class (b) with d = 1, 3, 5; (a)-II with r_P2 = 3 or 4; distinct 3+5; all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
