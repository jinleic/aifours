# Second erratum to v40: the clause "Lambda=A, cut D^-|C^-" used a wrong row; corrected proof

Actual `/bin/date` before this body: **Mon Oct 26 02:53:08 PDT 2026**. InfoRecursiveMDS18-2. Additive erratum; v40 (SHA256 `912a3bc25760e6c4b747679b7343a7b314bdbdbbb965ec4daf9a8a4e129cfee5`) and erratum v1 (SHA256 `d25d34f06dd4de28f88ca34c35dd246ce3e4b365a82b0c7a56eca5cef51e3cbb`) are unchanged. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO.

## 1. What is wrong

v40 §3, clause "Lambda=A, cut D^-|C^-", argues from "O-row 6 (B[1,5+x_C]+v+C[1,5-x_C])". From this cut O's gaps are C^-, A (split), D, B^-, C, D^-, with band values x_C, x_C+p, x_C+x_A, 5+x_A, 5, 5+x_C, 10; the row at B^-|C has band 5 and is B[1,5]+v+C[1,5]. So the cited row, and every step built on it (x_C<=2, the E_L+{q_1'} comparison), is invalid. The clause's conclusion is nevertheless true; the proof below replaces it. In the same pass the clauses "Lambda=A, cut C|D^-" and "Lambda=B, cut D^-|C^-" (both values of t') and the cross-path Observation were re-derived and found correct as written; with erratum v1 this covers every clause of v40 §3.

## 2. Corrected proof (Lambda=A, x_A+x_B=0, x_C+x_D=5)

P-band g_0 at A^-|B and g_0+x_B at B|A^-; D_L = 10-x_C-g_0, and D_L<=-4 would need x_C+g_0>=14 with x_C<=4 (band 5+x_C<=9), so D_L = r in {4,5,6}. With Lambda[0] = v3: O-row 1 = C[1,x_C]+v+Lambda[1,10-x_C] with C[1,x_C] pure K' = K' minus (E_L+k_1), |E_L| = g_0-1; the pure P-tail is B's last g_0+x_B vertices = K' minus (E_R+k_2); O-row 3 = (q_2+E_R)+v+D[1,10-x_C-x_A] with |E_R| = x_C+x_A-1; O-row 4 = (D's last 5+x_A)+v+B[5,9-x_A]; O-row 5 = B[1,5]+v+C[1,5]; O-row 6 = C[5,9+x_C]+v+D[10,9+x_D]; windows C[x_C,9+x_C] (O-row 0) and D[1,10] (O-row 7); P-row at A^-|B = (Lambda[1,g_0] = E_L+q_1)+v+B[1,10-g_0].

Q extras: B carries r-1 Q (P-head plus pure P-tail) and C[1,x_C-1] lies in the pure tail, so D[11,9+x_D] carries one Q: x_D>=2, x_C<=3. O-row 6 with the C window gives labels C[x_C,4] = labels D[10,9+x_D]; O-row 3 with the D window gives labels D[11-x_C-x_A,10] = q_2+E_R.

- r=6: q=6 rigidity and x_C+g_0=4 give g_0=1, x_C=3, x_D=2, and |E_R| = 2+x_A in {0,3} with the P-band g_0+x_B = 1-x_A >= 1 leaves x_A=-2 (E_R empty). The designated K' paths exhaust K4(K'), so the window C[3,12] puts a Q at C[4]; C[3,4] = D[10,11] with D[11] the Q extra makes D[10] carry C[3]'s K' label. O-row 3 gives D[1,9] = O minus {q_2}, containing all four K', so D[10] repeats a K' label in the window D[1,10]. Impossible.
- r=5: g_0 = 5-x_C >= 2 gives c_0 = 2, so the Lemma forces E_R empty: x_A = 1-x_C. O-row 3 gives D[1,9] = O minus {q_2}, so D[10] = q_2 and C[x_C+1,4] carries two Q: x_C<=2. x_C=2 (x_A=-1, x_D=3, B[7,10] the pure P-tail): O-row 4 = D[9,12]+v+B[5,10] needs D[9], B[5], B[6] in Q, giving the off-path Q pairs C[3]C[4], D[9]D[10], B[5]B[6], three against the two allowed by (Q5). x_C=1 (x_A=0, x_D=4, B[6,9] pure): O-row 4 = D[9,13]+v+B[5,9] has at most [D[9]]+1+1+[B[5]] <= 4 < 5 Q. Impossible.
- r=4: B[1,4+x_C] = O minus (E_L+q_1) has K' labels K' minus E_L = {k_1} + labels(C[1,x_C]). By O-row 5 the labels of C[1,x_C] avoid B[1,5], so they occupy B[6,4+x_C], which has only x_C-1 places. Impossible.

So "Lambda=A, cut D^-|C^-" is impossible, and the v40 Result stands.

All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged.
