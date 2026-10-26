# Actual Tuscan11 same-centre 3+5, Type II, short copy on C or D — impossible

Actual `/bin/date` before this body: **Mon Oct 26 01:35:32 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting

Type II words (v18 §2 (2), SHA256 `66a010b502ca9647d3c1af37745cefd59f94ad71136c4a1243d21d37aeb962bb`): P = B A^-, O = A D B^- C D^- C^-. Closing the words forces A, B, C to run v3 to v5 and D to be the loop at v5. C and D are self-dual (both traversals in O); here the short copy lies on Lambda in {C, D}. Excesses x_A, x_B, x_C, x_D (Lambda's value p+q). Rows: cut in O gives r_P=2, r_O=9, x_A+x_B=0, x_C+x_D=5; cut in P gives r_P=3, r_O=8, x_A+x_B=10, x_C+x_D=-5. Tools as in v35-v38 (all row-local): (T4) |D_L|>=4 with D_L=10-u-w; the v31 bookkeeping and pure-K' segments; (Q4).

## 2. Cut in P: band arithmetic in the cut-free face O

O-band (cyclic, all in [1,9]), starting with f at C^-|A: f, f+x_A, f+x_A+x_D, f+10+x_D, f+5, f+5+x_D.

- Lambda=D: u=f+x_A+p, w=f+5+q, D_L=5-f-(f+x_A+x_D)<=3. D_L<=-4 needs f+(f+x_A+x_D)>=9, but f+10+x_D<=9 and f+x_A<=9 give f+(f+x_A+x_D)<=8.
- Lambda=C: u=f+10+x_D+p, w=f+5+x_D+q, D_L=-2f-x_D in [1-f,4-f] (from f+10+x_D<=9 and f+5+x_D>=1), so |D_L|>=4 needs f>=5, while f+5<=9 needs f<=4.

## 3. Cut in O

In O the traversals of C (and of D) are not adjacent, so v20 §4 and v30 (SHA256 `16159aa53d6db5bf3b08a64a534a81190da9f3680ee325be24e645c45a41bddc`) exclude the short-copy cut and every cut at an end of Lambda (global reversal preserves Type II, the cut face and Lambda). The remaining corners:

- Lambda=D, cut B^-|C: e_1..e_7 = x_C, x_C+q (w), 5, 5+x_C, 5+x_C+x_A, 5+x_C+x_A+p (u), 10+x_A, so 1<=x_C<=4, x_A<=-1, and e_5>=1 gives D_L=-(x_C+x_A)<=4; D_L<=-4 needs x_A>=0. So D_L=4=r, e_5=1, and the pure-K' tail before D's forward departure (A's last vertex) gives |E_L|=4. O-row 3 = Lambda[1,5]+v+C[5+x_C,9+x_C] with Lambda[1,5]=E_L+{q_1}, so C[5+x_C,9+x_C] holds two K' and three Q; it contains the pure-K' tail C[10,9+x_C] before D^-'s departure, so x_C<=2, and the three Q lie non-adjacent in at most four places. Impossible.
- Lambda=D, cut C^-|A: e_1..e_7 = x_A, x_A+p (u), x_A+x_D, x_D, 5, 5+q (w), 5+x_D, so x_A>=1, 1<=x_D<=4, D_L=5-x_A-x_D<=3; D_L<=-4 with e_3<=9 forces x_A+x_D=9, r=4, and the head of B^- has one vertex, so |E_R|=4. O-row 5 = C[10-x_D,14-x_D]+v+({q_2}+E_R) gives that C-segment two K' and three Q; it contains the pure-K' head C[10,14-x_D] of C^- (5-x_D vertices), so x_D>=3, and the three Q lie non-adjacent in C[10-x_D,9], at most four places. Impossible.
- Lambda=C, cut A|D: with s=x_D+x_B, bands give x_B<=-1 and 1<=s<=4, and D_L=x_A-s; D_L<=-4 needs x_A<=0, so D_L>=4 and the pure-K' tail before C^-'s departure is D^-'s last e_5=s+5>=6 vertices, longer than k-1<=5. Impossible.
- Lambda=C, cut D|B^-: e_1..e_7 = x_B, u, x_B+x_C, x_B+5, w, x_B+5+x_C, 5+x_C, so 1<=x_B<=4 and s=x_B+x_C in [1,4], while D_L=5-x_B-s in [-3,3]. Impossible.

**Result.** Same-centre 3+5 Type II with the short copy on C or D is impossible for either cut face. Remaining same-centre 3+5: Type II with the short copy on A or B (cut in O or in P). Remaining m8 otherwise: 4+4 F2; distinct 3+5 connected or reverse-pair; all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
