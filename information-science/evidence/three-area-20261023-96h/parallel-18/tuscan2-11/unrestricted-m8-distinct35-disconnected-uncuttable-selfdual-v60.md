# Actual Tuscan11 distinct 3+5, disconnected (reverse pair + nine-row component) — counts, an uncuttable self-dual lemma, and Type I with r_P = 2 excluded

Actual `/bin/date` before this body: **Mon Oct 26 06:41:00 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36). This is a necessary-case reduction for any Tuscan-2(11) square, not a construction and not a nonexistence result.

## 1. Setting

By v12 §5.1 (parent-accepted; SHA256 `c2a9283d09b06781e0f1b76a42a0dcb700913dc87bddf69aabae78ff32caf6b2`), a disconnected distinct 3+5 array consists of:
- an actual reverse pair (two rows);
- a nine-row component H.

H contains both branches: b_v of degree 3 (label v) and b_w of degree 5 (label w). Its start set is exactly the other nine labels, so **neither v nor w is a cut label in H**. Hence no row boundary of H ever falls on a visit of b_v or b_w, or on a degree-2 copy of v or w.

The identity d_H(x) = r_H - 1_(x in C_H) gives d_H(v) = d_H(w) = 9. So H has exactly three degree-2 copies of v (3 + 2·3 = 9) and two of w (5 + 2·2 = 9). The core is three threads between b_v and b_w plus a loop D at b_w, with two faces.

**Rotation types.** The classification of v18 §2 (SHA256 `66a010b502ca9647d3c1af37745cefd59f94ad71136c4a1243d21d37aeb962bb`; parent-accepted R2) uses only:
- the degree-3 and degree-5 rotations;
- the end involution alpha;
- the no-one-branch-visit-face theorem.

It does not use the branch labels, so it applies to H. Following phi = sigma alpha in v18's dart words, with threads A, B, C oriented b_v -> b_w and D oriented d -> bar d:
- **Type I:** P = A D C^- (3 branch visits) and O = B D^- B^- C A^- (5 branch visits). A, C and D are cross paths, each traversed once by each face in opposite directions. B is self-dual for O.
- **Type II:** P = B A^- (2 branch visits) and O = A D B^- C D^- C^- (6 branch visits). A and B are cross paths. The thread C and the loop D are each self-dual for O.

## 2. Counts

Every symbol is in every row once, and v and w have no cut in H. Let a_x be the number of x-copies on cross paths and s_x the number on self-dual paths.

**Type I.**
- v: r_P = 1 + a_v and r_O = 2 + a_v + 2s_v, with a_v + s_v = 3.
- w: r_P = 2 + a_w and r_O = 3 + a_w + 2s_w, with a_w + s_w = 2.

Hence a_v = a_w + 1 and **r_P = 2 + a_w is 2, 3 or 4**. The face lengths |A|+|C|+|D| = 10r_P and |A|+|C|+|D|+2|B| = 10r_O = 90 - 10r_P give **|B| = 45 - 10r_P**, i.e. 25, 15 or 5.

**Type II.**
- v: r_P = 1 + a_v and r_O = 2 + a_v + 2s_v.
- w: r_P = 1 + a_w and r_O = 4 + a_w + 2s_w.

Hence a_v = a_w = r_P - 1. Every face has at least two rows (v4, accepted) and a_w <= 2, so **r_P is 2 or 3**. Then |A|+|B| = 10r_P and **|C|+|D| = 45 - 10r_P**, i.e. 25 or 15.

## 3. Uncuttable self-dual lemma

**Lemma.** Let a path Y of length L (a thread or a loop) be traversed twice by one face, in opposite directions, and suppose no boundary of that face ever falls on either end vertex of Y. Then:
- L <= 24;
- if L >= 21, the two passes' least positive boundaries (in Y-coordinates) are beta' and beta'+4 for some beta' with L-19 <= beta' <= 5.

*Proof.* A pass's least positive boundary lies in 1..10. The value 10 would make the end at coordinate 0 a boundary, so both values beta' and gamma' lie in 1..9. They differ by boundary coincidence (L3) of v57 (SHA256 `41ae55f5aeff940eadfcd9c947bd43ea7c323b9ef3cc3bf42eee56646d4eaa89`). The non-leaving self-dual lemma (L2) of v57 gives beta', gamma' >= L-19.

For L >= 21 each pass then has an inside row, I_1 = [beta', beta'+10] and I_2 = [gamma', gamma'+10]. Take beta' < gamma' and put delta = gamma' - beta'. Since I_1 does not leave Y:
- (I_1, I_2) is clean with k = delta;
- I_1 against the pass-2 row [gamma'-10, gamma'] is clean with k = 10-delta.

Rule (R) of v49 §4 (SHA256 `0b02a602b2d03bbea47fc5db072da4d0cba5395900f31c75301dcccadf67ded9`) then gives delta in {4, 5, 6}.
- **delta = 6:** the windows [gamma'-10], I_1, I_2, [beta'+10] (starts beta'-4, beta', beta'+6, beta'+10) form a bd chain. Both k = 4 pairs are clean because I_1 and I_2 do not leave Y, and the bd 5-path [beta'+6, beta'+10] is interior. This is the bd clash of v49.
- **delta = 5:** [gamma'-10], I_1, I_2, [beta'+10] is a shift-5 chain with all three pairs clean (v50 §2, SHA256 `b7bcd3730661be24c9f1dd218254ff6881821c06ab1402cbbd690f3e7e5ac5bc`).

So delta = 4 and gamma' = beta'+4 <= 9, giving beta' <= 5 and L <= beta'+19 <= 24. For L >= 25 the step "L >= 21" already applies and yields L <= 24, a contradiction. QED

## 4. Consequences in H

- **Type I with r_P = 2 is impossible.** There |B| = 25, while B is self-dual for O and its ends b_v and b_w are never boundaries. The lemma forbids L >= 25.
- **Type II with r_P = 2:** |C|+|D| = 25 with both C and D uncuttable and self-dual. The lemma gives |C|, |D| <= 24, and if either has length >= 21 its passes are fixed as in §3.
- **Type I with r_P = 3 or 4** (|B| = 15 or 5) and **Type II with r_P = 3** are not decided here.

## 5. Result

For the disconnected distinct 3+5 placement, the nine-row component has exactly the copy counts and length formulas of §2, and **Type I with r_P = 2 is impossible**. Open there: Type I with r_P = 3, 4 and Type II with r_P = 2, 3. These are necessary-case exclusions only. No distance-two event is used, so none of this constructs or excludes a Tuscan-2(11) square.

Other open lines are unchanged from manifest v12 (SHA256 `1592f9e272a7f4daafc2f6ef67d1c20e63de3800f9625e52f8214f4a51efdda3`):
- the distinct-centre 4+4 survivors R1-R3;
- distinct 3+5 connected (R4);
- all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
