# Actual Tuscan11 distinct-centre 4+4 — a residue lemma for the two cross paths

Actual `/bin/date` before this body: **Mon Oct 26 03:33:55 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting

Distinct-centre 4+4 (v44, SHA256 `c520658a683cb9acea9e9df9905d46f9a3e7688b3e4887f496dee58c1da6a805`): branch b_v (label v) and b_w (label w) of degree 4, three deg-2 copies of each of v and w, beta=0, two faces, class (a)-II (P2 = T4 T3^-, P6 = T1 T2^- T3 T1^- T2 T4^-, threads b_v->b_w) or class (b) (F_1 = T1 L_w T1^- L_v, F_2 = T2 L_w^- T2^- L_v^-, loop L_v at b_v, L_w at b_w). The cross paths X, Y are T3, T4 in (a)-II and L_v, L_w in (b). "Special copy" means a deg-2 copy of v or of w; its band value in a row is its position there (1..9 unless it is that label's cut). Tools: (T4) opposed whole windows whose physically common overlap starts 0,1,2 or 3 apart are impossible (v21 §2; the proof uses only the common overlap, the equal label sets of the two exclusive parts, DUP for sizes 2, 3, a repeated row start or end for size 1, and beta=0 for size 0).

## 2. The residues

Every row has exactly ten edges, so in a face the row boundaries are the positions congruent to one offset mod 10. A cross path is traversed once in each face, in opposite directions; a copy at coordinate s on it has positions A+s and A'-s, so its two band values satisfy **e+e' = c (mod 10) with c depending only on the path**. If the copy is the cut of its label in one face, its band value in the other face is congruent to c.

The two residues differ by 5. In (a)-II, put position 0 of P6 at T4^-|T1 and of P2 at T3^-|T4: T3-coordinate t sits at |T1|+|T2|+t and 10r_P2-t, T4-coordinate s at 10r_P6-s and s, so c_T3-c_T4 = |T1|+|T2| = 5(11-2r_P2) = 5 (mod 10). In (b), put 0 at L_v|T1 and L_v^-|T2: L_w-coordinate s sits at |T1|+s and |T2|+|L_w|-s, L_v-coordinate s at 2|T1|+|L_w|+s and 2|T2|+|L_w|+|L_v|-s, so c_Lv-c_Lw = |T1|+|T2|+|L_v|+|L_w| = 55 = 5 (mod 10).

## 3. Lemma

**Lemma.** X and Y do not both contain a full row (a row of either face all of whose eleven vertices are interior vertices of that path).

*Proof.* A full row on a path contains its row's v and w, both special copies on that path at interior positions e. Take one, with residue c.
- If it is not a cut, the overlap of its two windows lies inside the full row, hence on the path, so (T4) gives |D| >= 4 for D = 10-e-e'. With e' in 1..9 and e+e' = c or c+10 this leaves e <= c-1 when c <= 6 (D = 10-c) and e >= c+1 when c >= 4 (D = -c).
- If it is its label's cut in the other face, then e = c, and the two rows of that face meeting at the cut overlap the full row on the path; (T4) against both gives e and 10-e >= 4, so e in {4,5,6}.

So the available positions are: c=0, 1, 9: none; c=2: {1}; c=3: {1,2}; c=4, 5, 6: all of 1..9; c=7: {8,9}; c=8: {9}. A full row needs two distinct positions (at most one cut copy can sit in it, as both cuts would occupy position c), so c lies in {3,4,5,6,7}. X and Y would need both c and c+5 (mod 10) in {3,...,7}, which never happens. QED

**Consequences.** In (a)-II at most one of T3, T4 has length 21 or more (a path of length at least 21 contains a whole block of each face traversing it); in (b) at most one of L_v, L_w does. In (a)-II with r_P2 = 5 (both cuts in P2, all six copies on T3 and T4, |T1|+|T2| = 5, |T3|+|T4| = 50), the P6-row pattern in which full P6-rows lie on both T3 and T4 is excluded. No class is closed by this packet.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
