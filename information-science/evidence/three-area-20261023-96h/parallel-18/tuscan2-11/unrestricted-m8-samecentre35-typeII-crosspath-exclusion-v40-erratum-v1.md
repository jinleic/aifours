# Erratum to v40 (same-centre 3+5 Type II, short copy on a cross path): the r=5 step of Lambda=B, cut C|D^-

Actual `/bin/date` before this body: **Mon Oct 26 02:49:17 PDT 2026**. InfoRecursiveMDS18-2. Additive erratum; v40 (SHA256 `912a3bc25760e6c4b747679b7343a7b314bdbdbbb965ec4daf9a8a4e129cfee5`, 26 LF) is unchanged. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO.

## 1. What is wrong

In v40 §3, bullet "Lambda=B, cut C|D^-", the r=5 clause says "the Lemma gives E_L empty, x_A=4-x_D, x_D in {3,4}". In v31's convention (Lambda[0] = v3, the start of B) the Lemma gives **E_R** empty, not E_L; with E_L empty x_D would be 1, contradicting the stated x_D in {3,4}. The clause also omits why x_D=1, x_D=2 and the empty-P-head branch cannot occur. The conclusion of the clause is correct; the full derivation follows. Re-derived in the same pass and found correct as written: the r=6 and r=4 clauses of this bullet and the t'=9 clause of "Lambda=B, cut D^-|C^-". Not re-derived here: the other v40 clauses.

## 2. Corrected r=5 derivation (k=5)

O-band from the cut: x_D, 5, 5+x_A, 5+x_A+x_D, w, 5+x_D, 10 (gaps D^-, C^-, A, D, B^- split, C); P-band t' at A^-|B and h = t'+x_B at B|A^-; D_L = 5-x_D-t' = -5, so t' = 10-x_D. Rows: O-row 0 window D[x_D,9+x_D]; O-row 1 = D[1,x_D]+v+C[5,14-x_D]; O-row 3 = A[5,9+x_A]+v+D[1,5-x_A]; O-row 4 = D[5-x_A,9+x_D]+v+(Lambda's last 5-x_A-x_D = q_2+E_R); O-row 6 = Lambda[1,5+x_D]+v+C[1,5-x_D] (pure K', so |E_L| = x_D-1); O-row 7 window C[5-x_D,14-x_D]; P-rows A[1,t']+v+(Lambda[1,x_D] = E_L+q_1) and (Lambda's last h)+v+(pure-K' P-head A[t',9+x_A] of x_D+x_A vertices).

- (a) Q copies: 25 = 10 on Lambda + 10 in the two windows + 5 extras. A carries four Q (A[1,t'] = O minus (E_L+q_1), the rest of A is the pure P-head) and C's extras lie in its pure head, so D[1,x_D-1] carries one Q: x_D >= 2.
- (b) Then E_L and C[1,5-x_D] are both nonempty, c_0 = 2, and the Lemma (2+c_0+c_L <= 5) leaves c_L <= 1: either E_R is empty or the P-head is empty. An empty P-head means h = 10, impossible in the cut-free face P. So E_R is empty and x_A = 4-x_D.
- (c) O-row 4 is D[1+x_D,9+x_D]+v+q_2, so the window gives D[x_D] = q_2. O-row 1 with the window C[5-x_D,14-x_D] gives labels C[5-x_D,4] = labels D[1,x_D], which carry two Q (q_2 and the extra of (a)); C[5-x_D] ends the pure head, so both Q lie in C[6-x_D,4]. For x_D = 2 that is one place. Impossible.
- (d) x_D = 3 (x_A = 1, t' = 7): C[3], C[4] are Q; A[7,10] is the pure P-head, so O-row 3 = A[5,10]+v+D[1,4] needs Q(A[5,6]) + 1 (D[1,2]) + 1 (D[3] = q_2) + [D[4] in Q] = 5, forcing A[5], A[6], D[4] in Q. The adjacencies C[3]C[4], D[3]D[4], A[5]A[6] are three Q-Q pairs off the two Q-paths, which leave only two of the ten Q pairs (Q5). Impossible.
- (e) x_D = 4 (x_A = 0, t' = 6): O-row 3 = A[5,9]+v+D[1,5] with A[6,9] pure K' carries at most [A[5]] + 1 + 1 + [D[5]] <= 4 < 5 Q. Impossible.

So r=5 is impossible, as v40 states. The v40 Result is unchanged.

All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged.
