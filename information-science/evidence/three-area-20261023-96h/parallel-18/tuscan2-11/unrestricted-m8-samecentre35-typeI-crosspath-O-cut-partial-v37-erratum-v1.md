# Erratum to v37: Lambda=A, cut C^-|D^- had a wrong band value and an unexamined branch

Actual `/bin/date` before this body: **Mon Oct 26 03:01:57 PDT 2026**. InfoRecursiveMDS18-2. Additive erratum; v37 (SHA256 `73bd714b319456157b198f3fb1f1517432a485b7c9f67452bc2d29eed6130e80`) is unchanged. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO.

## 1. What is wrong

v37 §4, clause "C^-|D^-" (Lambda=A), lists the O-band as d, d+5, d+5+p, 5-b, 10-b. From this cut O's gaps are D^-, C, A^- (split), B, C^- with excesses d, 5, a, b, 5 and d+a+b=0, so the fifth value is 5, not 10-b. The claimed b>=1 is therefore unjustified, and with it "|D_L|<=3". For b>=1 the bound still holds (below), but b<=0 admits D_L<=-4 and was never examined. The proof below closes it. The other v37 clauses (Lambda=D: C|A^-, A^-|B, B|C^-; Lambda=A: D^-|C both signs, B|C^-) were re-derived in the same pass and their band lists and conclusions are correct as written.

## 2. Corrected proof

Coordinates along A^- (Lambda[0] = v3, Lambda[L] = v5, L = 20+a). O-band d, d+5, d+5+p (u), 5-b, 5, so 1<=d<=4 and -4<=b<=4. P-band f_0 (B^-|D), f_0+d (D|A), w = f_0+d+q, f_0-b (A|B^-), hence 1+b <= f_0 <= 9-d and D_L = 10-u-w = 5-d+b-f_0 lies in [b-4, 4-d]. So b>=1 gives |D_L|<=3, and b<=0 needs D_L<=-4, r = f_0+d-b-5.

Rows (D_L<0): O-row 0 is the window D[d,9+d]; O-row 1 = D[1,d]+v+C[1,10-d]; O-row 2 = C[10-d,14]+v+Lambda[1,5-d], so C[10-d,14] = O minus (E_L+q_1) with |E_L| = 4-d; O-row 4 = (Lambda's last 5-b)+v+B[1,5+b] with B[1,5+b] pure K' = K' minus (E_R+k_2); O-row 5 = B[5+b,9+b]+v+C[10,14]; O-row 6 is the window C[1,10]. P-rows: B[1,f_0]+v+D[1,10-f_0]; D[10-f_0,9+d]+v+(q_2+E_R) with |E_R| = 9-d-f_0; Lambda[1,f_0-b]+v+B[f_0,9+b] with B[f_0,9+b] pure K' = K' minus (E_L+k_1). Between the two pure segments B has the middle B[6+b,f_0-1] of r-d-1 vertices, and the r Q extras lie in that middle, in C[11,14] and in D[1,d-1].

- r=6: q=6 rigidity gives |E_R| = -2-b in {0,3}, so b=-2 and f_0 = 9-d; f_0-b<=9 gives d>=2, and |E_L| = 4-d in {0,3} gives d=4, f_0=5, B = B[1,3], B[4], B[5,7] with both 3-paths designated, so K4(K') is exhausted. O-row 5 = B[3,7]+v+C[10,14] has its four K' at B[3], B[5,7], so C[10,14] is all Q; O-row 2 = C[6,14] = O minus {q_1} then puts four consecutive K' in C[6,9]. Impossible.
- r=5: O-row 5 gives Q(C[10,14]) >= 5-(4-d), and C[10,14] lies in C[10-d,14] with four Q, so d<=3 and E_L is nonempty. The K' v-neighbours Lambda[t-1], Lambda[t+1], Lambda[1], B[1], B[9+b] and, if E_R is nonempty, Lambda[L-1] number at most k=5, so E_R is empty: b=-1, f_0 = 9-d, B interior 8. The P-row at B^-|D = B[1,9-d]+v+D[1,1+d] contains B[1,4] (four K') and B[9-d] (a K' label outside B[1,4]), i.e. all five K', so B[5,8-d] and D[1,1+d] are all Q: 3-d plus d adjacent Q pairs off the Q-paths, against the two allowed by (Q5). Impossible.
- r=4: the middle has 3-d vertices and C[10,14] holds at most three non-adjacent Q, so the middle carries exactly one Q, d<=2, and C[10], C[12], C[14] are Q; then C[12], C[14] and the middle give three extras, so D[1,d-1] carries one Q and d=2. O-row 2 makes C[8], C[9], C[11], C[13] carry K' minus E_L = {k_1} + labels(B[7+b,9+b]); O-row 5 contains B[7+b,9+b] together with C[11] and C[13], so both would be k_1. Impossible.

So the clause's conclusion holds and the v37 Result is unchanged.

All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged.
