# Actual Tuscan11 distinct-centre 4+4, class (a)-II — single only-row lemma; r_P2 = 4 is impossible

Actual `/bin/date` before this body: **Mon Oct 26 05:34:33 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Single only-row lemma

Class (a)-II is as in v47 §1 (v44 pin `c520658a683cb9acea9e9df9905d46f9a3e7688b3e4887f496dee58c1da6a805`). Use T3-coordinates t: b_v at 0, b_w at lam3, and P6 runs forward.

Suppose P6 covers T3 with three consecutive rows:
- B, whose T3 part is [0, x], with 1 <= x <= 10; it leaves T3 through b_v when x < 10;
- an only-row O = [x, x+10] inside T3;
- D, whose T3 part is [x+10, lam3] with y := lam3 - x - 10 in 1..10; it leaves through b_w when y < 10.

P2 runs backward on T3 and its rows leave through b_v or b_w. Let c be P2's boundary residue in t, put d = (c-x) mod 10, and let the P2-rows R_- = [x+d-10, x+d] and R_+ = [x+d, x+d+10] meet O.

**Lemma.** d is 4, 5 or 6, subject to:
- d = 4 requires x <= 5;
- d = 6 requires y <= 5;
- d = 5 requires x <= 4 and y <= 4.

*Proof.* O does not leave T3, so (O, R_-) and (O, R_+) are clean (v50 §2, SHA256 `b7bcd3730661be24c9f1dd218254ff6881821c06ab1402cbbd690f3e7e5ac5bc`), with k = 10-d and k = d. Rule (R) of v49 §4 (SHA256 `0b02a602b2d03bbea47fc5db072da4d0cba5395900f31c75301dcccadf67ded9`) excludes k <= 3. For d = 0 the vertex at x is a boundary of both faces.

(B, R_-) is clean exactly when R_- does not leave through b_v, i.e. x+d-10 >= 0. (R_+, D) is clean exactly when R_+ does not leave through b_w, i.e. x+d+10 <= lam3.
- **d = 4:** the bd chain B, R_-, O, R_+ (starts x-10, x-6, x, x+4) works once x >= 6.
- **d = 6:** the bd chain R_-, O, R_+, D (starts x-4, x, x+6, x+10) works once y >= 6.
- **d = 5:** the shift-5 chain B, R_-, O, R_+ works once x >= 5, and R_-, O, R_+, D works once y >= 5.

QED

The mirror statement for an only-row inside T4 follows by row reversal.

## 2. r_P2 = 4 is impossible

By v53 (SHA256 `73c0724422c1c9be9e63acab22f7c5f55ee7845d58063d7f8dff973610bd7c08`), r_P2 = 4 has exactly one only-row O and no shared row, and both runs fill three rows. Take O inside T3 (row reversal).

- H1 = P6[0,15]. Its rows are B_j = H1[10j-o0, 10j+10-o0] for j = 0, 1, 2, with o0 in 5..10.
- B_2 holds b_v(15), so x = 15-o0 lies in 5..10.
- The first H2-row holds b_w(W) and has p0 T3-vertices, so y = p0 lies in 5..10.
- T4 is covered by the last H2-row and B_0 alone, so lam := |T4| = 40 - lam3 = 30 - x - y.

**Applying the lemma.**
- d = 5 needs x <= 4. Excluded.
- d = 4 forces x = 5.
- d = 6 forces y = 5.

**Applying v46.** On T4, P2 runs forward from b_v (P2-position = T4-coordinate). Its boundaries are at the residue -c = -(x+d) mod 10.
- If d = 4 and x = 5, the window [1, 11] lies inside T4, since lam = 25 - y >= 15.
- If d = 6 and y = 5, the window [tau0, tau0+10] with tau0 = (-x-6) mod 10 in 4..9 ends exactly at lam - 1 = 24 - x, for every x in 5..10.

Either way P2 has a full row inside T4 while P6 has the full row O inside T3. This contradicts v46 (SHA256 `d212cc7d2c8b7907187f0e20732206224cfa0cee0dcfedb41d874342e5d9c5ca`). So **r_P2 = 4 is impossible**.

## 3. Result

The new results are the single only-row lemma and **r_P2 = 4 is impossible** in class (a)-II. With v51 and v53, class (a)-II is now open only at r_P2 = 3. The two open shapes are:
- both runs fill four rows (Sigma = 21, v52);
- one run fills three rows, with o = 1 and s = 0.

Also open: class (b) d = 1, 3, 5; distinct 3+5; all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
