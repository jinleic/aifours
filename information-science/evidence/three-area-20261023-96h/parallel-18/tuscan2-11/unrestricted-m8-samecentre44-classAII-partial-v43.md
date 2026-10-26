# Actual Tuscan11 same-centre 4+4, class (a)-II — two of four short-copy/cut cases closed

Actual `/bin/date` before this body: **Mon Oct 26 01:56:30 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting

v41 (SHA256 `e07d7252b8d15cfca2a7b431f5d29fdd015b1d52a9bbcdd39be4966c07fd0704`) class (a)-II: P2 = T4 T3^-, P6 = T1 T2^- T3 T1^- T2 T4^-, all threads from b1 to b2, excesses x1..x4 (the short-copy path Lambda has p+q). T1, T2 are self-dual (in P6), T3, T4 cross. Cut in P6: x3+x4=0, x1+x2=5; cut in P2: x3+x4=10, x1+x2=-5. Tools of v37 §1, v20 §4, v30, and the cross-path observation of v40 §3.

## 2. Short copy on T3 or T4, cut in P2

Both corners of P2 are ends of T3 and of T4, so every cut is at the short copy or at an end of Lambda's P2-traversal: excluded by v20 §4 and v30.

## 3. Short copy on T1 or T2, cut in P6

v20 §4 and v30 exclude the short copy and every end of a Lambda-traversal (T1 and T1^-, resp. T2^- and T2, are not adjacent in P6). The interior corners:

- Lambda=T1, cut T2^-|T3: e_1..e_7 = x3, w, x3+x1, x3+5, 5, u, 5+x1; D_L=5-(x3+x1) forces x3+x1=1, D_L=4, r=4. The pure-K' tail T4[1,5] of T4^- gives E_L empty, so P6-row 3 is Lambda[1]+v+T2[1,9] with Lambda[1] in Q (three Q in T2[1,9]) and the window T2[1,10] puts a Q at T2[10]. P6-row 4 is T2[9,13+x3]+v+T4[5,9-x3]; the four Q extras lie in T2[11,13+x3] and T4[6,9-x3], so T2[9,10] has none. Impossible.
- Lambda=T1, cut T2|T4^-: e_1..e_7 = x4, u, x4+x1, x4+5, 5, w, 5+x1; again x4+x1=1, D_L=4, r=4, and the pure-K' tail of T3 (its last 5) gives E_R empty, so P6-row 3 (Lambda[L-1]=q_2 + v + T2[5+x4,13+x4]) and the window T2[4+x4,13+x4] put q_2 at T2[4+x4]. P6-row 4 is T2[1,5+x4]+v+T3[1,5-x4]; with the four Q extras in T2[1,3+x4] and T3[1,4-x4], it carries at least five Q. Impossible.
- Lambda=T2, cut T4^-|T1: e_1..e_7 = x1, w, 5, 5+x3, 5+x3+x1, u, 10+x3; D_L=-(x3+x1) forces x3+x1=4, D_L=-4. Heads T3[1,5] (E_L empty) and the last -x3 vertices of T4. P6-rows 1 and 5 with the window T1[1,10] give T1[10..9+x1] three Q including T1[10], so two Q extras in T1[11,9+x1] and two in T3[6,9+x3]; P6-row 4 = T3[5,9+x3]+v+T1[9,9+x1] then has at least five Q. Impossible.
- Lambda=T2, cut T3|T1^-: e_1..e_7 = x1, u, 5, 5+x4, 5+x4+x1, w, 10+x4; x1+x4=4, D_L=-4, heads the last 5 of T4 (E_R empty) and T3[1,-x4]. P6-rows 1 and 5 with the window T1[x1,9+x1] give T1[1,x1] three Q including T1[x1], so two Q extras in T1[1,x1-1] and two in T4[1,4+x4]; P6-row 4 = T4[1,5+x4]+v+T1[1,x1+1] has at least five Q. Impossible.

## 4. Short copy on T3 or T4, cut in P6 (partial)

By the cross-path observation (v40 §3) the other cross path X carries only r-1 Q, so X cannot be the first or last gap of P6: this excludes T2|T4^- and T4^-|T1 for Lambda=T3, and T2^-|T3 and T3|T1^- for Lambda=T4; v20/v30 exclude Lambda's own ends. Open here: corners T1|T2^- and T1^-|T2 for Lambda in {T3,T4}.

**Result.** Same-centre 4+4 (a)-II is impossible with the short copy on a cross path and the cut in P2, and with the short copy on a self-dual path and the cut in P6. Open in (a)-II: short copy on T1/T2 with the cut in P2; short copy on T3/T4 with the cut at T1|T2^- or T1^-|T2. Remaining m8 otherwise: distinct-centre 4+4; distinct 3+5 connected or reverse-pair; all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
