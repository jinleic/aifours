# Actual Tuscan11 distinct-centre 4+4, class (a)-II, two-row P2 carrying exactly one cut — impossible

Actual `/bin/date` before this body: **Mon Oct 26 04:04:12 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting and symmetries

Class (a)-II and the row count r_P2 = 1+a_v+eps_v = 1+a_w+eps_w are as in v47 §1 (v44 pin `c520658a683cb9acea9e9df9905d46f9a3e7688b3e4887f496dee58c1da6a805`). Here **r_P2 = 2 and exactly one cut lies in P2**. Imports: one cut per label; (F2) each unordered label pair is one physical edge; DUP (vertex-disjoint paths with the same 2- or 3-label set share a pair). For four labels the two paths must be complementary P4s: the complement of a-b-c-d is c-a-d-b.

Row reversal maps (T1,T2,T3,T4) to (T2,T1,T4,T3) and exchanges |T3| and |T4|. Exchanging v and w maps them to (T1^-,T2^-,T4^-,T3^-) and swaps (eps_v,eps_w). Both maps preserve the class. So take eps_v = 1, eps_w = 0: then a_v = 0, the v-cut is b_v's P2-visit, a_w = 1 (one copy w' on T3 or T4) and the w-cut is in P6. Put lam = |T4|, so |T3| = 20-lam. lam = 10 would put b_w on P2's second boundary, so it is excluded, and reversal lets us take lam <= 9.

## 2. P2

The boundaries are at 0 (b_v) and 10. The rows are **R1 = v T4[1,lam-1] w T3[19-lam,10]** and **R2 = T3[10,1] v**. By R2, T3[1,10] lists w and the nine ordinary labels O, and w' = T3[t'] with t' <= 9. z := T3[10] is P2's ordinary cut, so **z is on no P6-boundary**. By R1, T4[1,lam-1] + T3[10,19-lam] = O.

## 3. P6 frame

Write l = |T1|, so |T2| = 35-l. P6 has nine rows and no v-cut, so each P6-row holds one v, at an interior position.

| Item | P6-positions |
| --- | --- |
| b_v | 0, 35, K = W+l |
| b_w | l, W = 55-lam, W+35 = 90-lam |
| T1[s] | s and K-s |
| T2[s] | 35-s and K+s |
| T3[s] | 35+s |
| T4[s] | 90-s |

The v's in [0,35] are b_v(0), the first visits of the three v-copies (all on T1, T2) and b_v(35). These are five consecutive v's, in rows B_0..B_4. Let e0 and e4 be the offsets of b_v(0) and b_v(35), both in 1..9. Then 35 = 40+e4-e0, so e0 = e4+5 with e4 in 1..4, and B_4 = [35-e4,45-e4]. B_5 = [45-e4,55-e4] holds the next v, which lies beyond W because T3 carries no v-copy.

## 4. e4 <= 3 and |T2| <= e4 are impossible

If |T2| > e4, then B_4 = T2[e4,1] v T3[1,10-e4], so T2[1,e4] and T3[11-e4,10] carry the same labels.
- e4 = 1: T2[1] carries z on the boundary 34, a second cut of z.
- e4 = 2 or 3: DUP.

If |T2| <= e4, then b_w(l) lies in B_4, inside it or on its first boundary, so B_4 holds no other w. This forces t' >= 11-e4, which is already impossible for e4 = 1. For e4 >= 2, w' lies inside B_5, so b_w(W) lies strictly beyond B_5. B_5 then sits inside T3's range and holds no v.

## 5. e4 = 4

B_4 = [31,41] = T2[4,1] v T3[1,6] with |T2| >= 5, so **T2[1,4] = T3[7,10]**. T2[4] lies on the boundary 31, so z is in T2[1,3]. Call the other two labels of T2[1,3] s1 and s2, and let s3 = T2[4]; all three lie in T3[7,9].

B_5 = [41,51] needs a v in (W,51), so W <= 49 and **lam >= 6**. Then b_w(W) lies inside B_5, which forces t' <= 5, and B_5 = T3[6,19-lam] w followed by T1^-'s first vertices. Because B_5 is a row, T3[11,19-lam] lies inside T3[1,5]\{w'} as labels. The labels of T3[1,5] left over are disjoint from T3[7,10].

With e0 = 9, B_0 = [81,91]. It holds b_w(90-lam), T4[lam-1,1], b_v(90) and T1[1] on the boundary 91; l = 1 would give B_0 two w's.
- **lam = 9.** b_w(81) is a boundary and B_0 = w T4[8,1] v T1[1], so T1[1] = z by R1. Contradiction.
- **lam = 8.** B_0 = T2[|T2|-1] w T4[7,1] v T1[1] gives {T2[|T2|-1], T1[1]} = {z, T3[11]}. Both sit on boundaries (81 and 91). Contradiction.
- **lam = 7.**
  - B_0 = T2[33-l] T2[34-l] w T4[6,1] v T1[1] gives T2[34-l] = z (position 82), and T2[33-l], T1[1] in T3[11,12] (positions 81 and 91).
  - B_5 = T3[6,12] w T1[l-1] T1[l-2] T1[l-3] with l >= 4: {T1[l-1],T1[l-2]} = {v,y}, and T1[l-3] = y' lies on the boundary 51, where {y,y'} = T3[1,5]\({w'}+T3[11,12]).
  - Smaller l puts b_v on 51, or a T2[1,4]-label among the y's.
- **lam = 6.**
  - B_0 = T2[32-l] T2[33-l] T2[34-l] w T4[5,1] v T1[1]: T2[32-l] and T1[1] (on boundaries) lie in T3[11,13], and {T2[33-l],T2[34-l]} = {z,u} with u in T3[11,13].
  - B_5 = T3[6,13] w T1[l-1] T1[l-2] with l >= 3: T1[l-1] is a v-copy, and T1[l-2], on the boundary 51, carries the leftover label. (l = 2 puts b_v on 51; l = 1 puts T2[1], whose label is in T3[7,10], in the leftover slot.)
- In both cases the T2-vertex on the boundary 81 carries a T3[11,13]-label, so it is not in T2[1,4]. Hence l <= 27 (lam = 6) and l <= 28 (lam = 7).

## 6. Two H-sequences (lam = 6, 7)

Take S1 = P6[1,31] (rows B_1..B_3) and S2 = P6[51,81] (rows B_6..B_8, index q = position-50). Rows are [1,11], [11,21], [21,31] in both. Put m = l-2 (lam = 6) or m = l-3 (lam = 7), so m is between 1 and 25. Then:
- **A = T1[1,m]** fills [1,m] in both, reversed: S2[q] = S1[m+1-q].
- **C = T2[4,..]** fills [m+5,31] in both, reversed: S2[q] = S1[m+36-q].
- **The middle [m+1,m+4]:**
  - S1 holds T1[l-1] b_w T2[34-l] T2[33-l] = {v,w,z,u} for lam = 6, and T1[l-2] T1[l-1] b_w T2[34-l] = {v,y,w,z} for lam = 7.
  - S2 holds b_v T2[1] T2[2] T2[3] = {v,z,s1,s2}.

Put psi = u or y; psi is not one of s1, s2, s3.

A label occurs in S1 three times, minus the number of S1's internal boundaries (11, 21) it occupies; the same holds for S2. Common vertices cancel, so S1 - S2 = {w,psi} - {s1,s2}. Hence **S1's internal boundaries carry s1 and s2, and S2's carry w and psi**. No middle position is 11 or 21, so m is not in 7..10 or 17..20.

S1[1] = A[1] and S1[31] = C[31] are boundaries. Their S2-positions are m and m+5, which must not be boundaries, so m mod 10 is not 1 or 6. This leaves m in {2..5, 12..15, 22..25}.

When an S1-row and an S2-row (read back in S1-positions) overlap, both are complete label sets, so their ends outside the overlap carry equal labels.
- **m in 2..5.** S1-rows [11,21] and [21,31] against S2-rows at [m+5,m+15] and [m+15,m+25] give C[m+5,10] = C[m+16,21] and C[m+15,20] = C[m+26,31].
  - m = 3, 4: DUP.
  - m = 5: C[10] = C[21], where C[21] is S1-boundary 21 and C[10] has S2-position 31. Two cuts.
  - m = 2: with C[17,21] = (a,b,c,d,e), C[7,10] is the path d-b-e-c and C[28,31] is the path c-a-d-b. Both use the pair {b,d}. Contradiction.
- **m in 12..15.** S1-row [1,11] against S2-row 1 = [m-10,m] gives A[1,m-11] = A[12,m]. S1-row [21,31] against S2-row 3 = [m+5,m+15] gives C[m+5,20] = C[m+16,31].
  - m = 13, 14: DUP.
  - m = 12: A[1] = A[12], and A[12] has S2-position 1. Two cuts.
  - m = 15: C[20] = C[31], and C[20] has S2-position 31. Two cuts.
- **m in 22..25.** S1-row [1,11] against S2-row 2 = [m-20,m-10] gives A[1,m-21] = A[12,m-10]. S1-row [11,21] against S2-row 1 = [m-10,m] gives A[11,m-11] = A[22,m].
  - m = 23, 24: DUP.
  - m = 22: A[1] = A[12], and A[12] has S2-position 11. Two cuts.
  - m = 25: with A[11,15] = (a,b,c,d,e), A[1,4] is the path d-b-e-c and A[22,25] is the path c-a-d-b. Both use {b,d}. Contradiction.

## 7. Result

In distinct-centre 4+4 class (a)-II, r_P2 = 2 with exactly one cut in P2 is impossible. Together with v47 (SHA256 `3a60200022a7d702a4589e6e0752fc2e86d7421f11f3d7210499b90a72d6a321`), r_P2 = 2 survives only with both cuts in P6 (a_v = a_w = 1).

Still open in (a)-II: that case and r_P2 = 3, 4, 5. Also open: class (b), distinct 3+5, and all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
