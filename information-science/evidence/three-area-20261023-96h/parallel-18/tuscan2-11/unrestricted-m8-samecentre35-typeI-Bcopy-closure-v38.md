# Actual Tuscan11 same-centre 3+5, Type I, short copy on B, v-cut in O — impossible; Type I complete

Actual `/bin/date` before this body: **Mon Oct 26 01:31:00 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting

Notation and tools of v37 §§1–2 (SHA256 `73bd714b319456157b198f3fb1f1517432a485b7c9f67452bc2d29eed6130e80`) with Lambda=B, coordinates along B (v5 to v3). O-departure from Lambda[0] follows A^-, O-arrival at Lambda[L] precedes C^-; P-departure from Lambda[L] follows A, P-arrival at Lambda[0] precedes D. Pure-K' segments: D_L>0: TAIL of A^- (O) and TAIL of A (P); D_L<0: HEAD of C^- (O) and HEAD of D (P). P-band: f_0 at B^-|D, f_0+d at D|A, g=f_0+d+a at A|B^-, w=g+q. Remaining cuts: C^-|D^-, D^-|C, C|A^-.

## 2. Cut C^-|D^-

O-band d, d+5, d+5+a, u, 5 with 1<=d<=4; D_L=10-u-w=5-g, so g in {1,9}.

- g=9 (D_L=-4): the O-head C[10,14]=K' minus {k_2} makes E_R empty, and the P-tail of A has 9 vertices, so a>=0. The P-head of D is D[1,1+d+a], covering D[1,d], so O-row 1 (D[1,d]+v+C[1,10-d]) and the window C[1,10] make C[11-d,10] pure K'. O-row 2 says C[10-d,9]+A[5+a+d,9+a] = Q+{k_2}, so C[11-d,9] lies in {k_2}, d<=2, and A[5+a+d,9+a] holds three consecutive Q (d=2, C[9]=k_2, C[8] in Q) or, for d=1, four consecutive Q (C[9]=k_2) or three Q among four places (C[9] in Q): (Q4) fails in every case.
- g=1 (D_L=4, r=4): tails A[1,d+5+a] (O) and A[9+a] (P), |E_R|=4. O-row 5 makes C[10,14]=Q,K',Q,K',Q; the six extras (C[11,14], D[1,d-1], A[d+6+a,8+a]) carry four Q and two K' (C[11], C[13]), so (Q4) forces d=2. Each K' label has exactly two copies outside the overlap and the windows C[1,10], D[2,11]; this forces {C[11],C[13]}={k_1,k_2}, and O-row 2 (C[8,14]+v+A[7+a,9+a]) then forces k_1 in E_R and z=A[9+a] in E_L. The P-rows at B^-|D and D|A give D[1,11+a] = (K' minus E_L)+(Q minus q_1') and D[11+a,11] = O minus labels(A), whose K' part is (E_L+{k_1}) minus z. With D[1] in Q, the window D[2,11] has two Q in D[12+a,11], so D[11+a] is Q, and k_1 lies in both D[2,10+a] and D[12+a,11]: twice in one row. Impossible.

## 3. Cut D^-|C

O-band 5, 5+a, u, 5-d, 10-d with 1<=d<=4; D_L=5-a-f_0.

- D_L<=-4: the pure-K' head of C^- has 10-e_4=5+d>=6 vertices. Impossible.
- D_L>=4: the tail A[1,5+a] and O-row 2 give |E_L|=-a=f_0-1, so r=4, f_0=1-a, g=1+d, |E_R|=4-d, P-tail A[9+a-d,9+a], A-extras A[6+a,8+a-d]. O-row 4 gives C[10-d,14] three Q, and O-row 1 (C[10,14]+v+A[5+a,9+a]) gives C[10,14] four Q minus those of A's extras; hence A's extras hold at least one Q, which excludes d=3, while d=1 would leave a K' among A's two extras and three K' extras in all. So d=2, C[8,9] in K', C[10,14]=Q,K',Q,K',Q, and the copy count gives {C[11],C[13]}={k_1,k_2}. O-row 1 then puts k_1 in E_R; but O-row 4 is C[8,14]+v+({q_2}+E_R), so C[8,14] avoids E_R while containing k_1. Impossible.

## 4. Cut C|A^-

O-band a, u, -d, 5-d, 5 with a>=1, -4<=d<=-1; D_L=10-a-f_0, and f_0+d>=1 gives f_0>=2.

- D_L<=-4: the pure-K' head of C^- has 10+d>=6 vertices. Impossible.
- D_L>=4: windows A[a,9+a] (O-row 0) and C[5,14]; tails A[1,a], A[10+a-g,9+a]; the window's r Q lie in r-1-d positions. r=6 (the Lemma) and r=5 (the Q budget forces d in {-4,-3}, then the Lemma) force f_0=1. Impossible. r=4: d=-4, a=1, f_0=5, g=2; A=K' Q K' Q K' Q K' Q K' K'; D=(Q,K',Q,K',Q) with K' labels K' minus E_L; copy counting gives E_R={C[5],m1,m2}, K' minus E_L={m1,m2}, and the window and tails put both m's at K'-isolated A-positions and D-positions. If q_2=C[6] each m has C-degree 1 and needs degree 2 at both its E_R and overlap copies, but only Lambda[21] has E_R-degree 2; if q_2=C[7] the m at C[8] has degree at most 4. Impossible (DEG).

**Result.** Same-centre 3+5 Type I is impossible in every case (v18 §§4–5 cut in P; v35 short copy on C; v37 short copy on D, A; this packet short copy on B). Remaining m8: same-centre 3+5 Type II; 4+4 F2; distinct 3+5 connected or reverse-pair; all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
