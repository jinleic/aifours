# Actual Tuscan11 same-centre 3+5, Type II, short copy on A or B — impossible; same-centre 3+5 complete

Actual `/bin/date` before this body: **Mon Oct 26 01:43:18 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting

Type II as in v39 §1 (SHA256 `86ae5e680a05dc315d32007931ed50513f94fc141cfc474fb65d72978b7eb894`), now with the short copy on a cross path Lambda in {A, B} (one traversal in each face). Cut in P: r_P=4, r_O=7, x_A+x_B=10, x_C+x_D=-5. Cut in O: r_P=3, r_O=8, x_A+x_B=0, x_C+x_D=5. Tools as in v37 §1.

## 2. Cut in P

Both corners of P (B|A^-, A^-|B) are ends of A^- and of B. So every cut in P is at the short copy or at an end of Lambda's P-traversal, and v20 §4 and v30 (row-local, as in v37 §2) exclude it.

## 3. Cut in O: a window loop meets a cross Lambda

**Observation.** Let X be the cross path other than Lambda. In P, X is traversed between Lambda's two P-ends, so X is covered by a P-head and a P-tail of the rows at Lambda's P-ends. One of them is a pure-K' segment of v31 §2; the other is O minus ({q}+E) for the corresponding Q-path endpoint q and end set E, hence carries exactly r-1 Q labels. So X carries only r-1 Q-labelled vertices, and X cannot contain a full window (r Q). This kills every cut whose first or last O-gap is X: for Lambda=A the cuts D|B^- and B^-|C; for Lambda=B the cuts A|D and C^-|A.

The remaining cuts (all others are ends of Lambda's O-traversal or the short copy, excluded by v20/v30):

- Lambda=A, cut C|D^-: O-band x_D, 5, 5+p (u), 5+x_A, 5+x_A+x_D, 5+x_D; with g_0 the P-band at A^-|B, D_L=5-g_0, so g_0 in {1,9}. g_0=1: the pure-K' tail C[1,5] of C^- (so E_L is empty and Lambda[1] is a Q), O-row 6 = B[1,5+x_D]+v+C[1,x_C] puts four Q into B[1,5+x_D], while the P-row at A^-|B is Lambda[1]+v+B[1,9] (three Q). g_0=9: the pure-K' head D[1,5-x_A] covers D[1,x_D] (e_5<=9), so O-row 1 and the window C[x_C,9+x_C] make C[x_C,4] pure K'; with C[1,5]=Q,K',Q,K',Q (O-row 2) this forces x_C=4, x_D=1, and then the Q copies number 8+4+4+3+2=21. Impossible.
- Lambda=A, cut D^-|C^-: D_L=10-x_C-g_0>=4; O-row 6 (B[1,5+x_C]+v+C[1,5-x_C]) and the P-head B[1,10-g_0] put a Q into C[1,5-x_C], so the pure-K' tail C[1,x_C] forces x_C<=2; the Lemma excludes r=6. If x_C+g_0<=5, O-row 6 gives C[1,5-x_C]=E_L+{q_1'}, which must contain the tail C[1,x_C] of labels outside E_L+{q_1'}; if x_C+g_0=6 the same holds with one E_L label removed. Impossible.
- Lambda=B, cut C|D^-: D_L=5-x_D-t' (t' the P-band at A^-|B) forces D_L<=-4. r=6: (x_D,t',h_0,x_A)=(2,9,7,2); O-row 1 and the windows give D[1]=C[4] (Q), D[2]=C[3] (K'), and O-row 4 makes D[3,11]=O minus {q_1}, so the window D[2,11] holds five K'. r=5: the Lemma gives E_L empty, x_A=4-x_D, x_D in {3,4}; row counts force three Q-Q adjacencies (A[5]A[6], D[3]D[4], C[3]C[4]) or a shortage (x_D=4), against (Q5). r=4: x_D=4 puts three Q non-adjacent in A[1,4]; x_D=3 forces C[1,2] inside {A[6]}; x_D=2 forces the three labels of C[1,3] into the two labels of A[6,7]. Impossible.
- Lambda=B, cut D^-|C^-: D_L=5-t', so t' in {1,9}. t'=9: O-row 1 puts all four Q into A[1,10-x_C], but the P-row at A^-|B gives A[1,9] three Q. t'=1: the Q-extra count forces x_C=2 and C[1,5]=Q,K',Q,K',Q; O-row 6 with the pure-K' tail D[10,12] puts all four Q into C[5,11], so the Q label at C[3] repeats inside the window C[2,11]. Impossible.

**Result.** Same-centre 3+5 Type II with the short copy on A or B is impossible; with v39, all of Type II; with v18, v35, v37, v38, all of Type I. **The whole same-centre 3+5 placement is excluded (written candidate).** Remaining m8: 4+4 F2; distinct 3+5 connected or reverse-pair; all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
