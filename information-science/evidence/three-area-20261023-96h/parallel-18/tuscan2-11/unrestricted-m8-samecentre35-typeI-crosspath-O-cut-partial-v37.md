# Actual Tuscan11 same-centre 3+5, Type I, short copy on a cross path, v-cut in O — Lambda=D and Lambda=A closed

Actual `/bin/date` before this body: **Mon Oct 26 01:24:33 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting

As v35 §1 (SHA256 `574ce16f45303f1978f1b57645933e685745e33d44e80adeea7518abf1ed91f6`), now with the short copy on Lambda in {A,B,D}: Lambda has one traversal in each face, r_P=4, r_O=7, C has 14 interior vertices and its two traversals in O are gaps of excess 5 (v18 §6). Excesses d, a, b of D, A, B (Lambda's entry is x=p+q, split p,q in O's order and q,p in P's); P has no v-cut, so d+a+b=0. O's cyclic excess word is d,5,a,b,5 (D^-,C,A^-,B,C^-). P-band: f_0 at B^-|D, f_0+d at D|A, f_0+d+a at A|B^-, all in [1,9]. Lambda's windows lie in different faces but are rows, so (T4) |D_L|>=4 holds for D_L=10-u-w (u, w the O- and P-band values at the short copy), and the bookkeeping, Lemma and pure-K' segments of v31 §§2-3 hold verbatim (they are row-local); (F1), (F2), (C5), (Q4), (Q5) as in v32/v33.

## 2. Transfers and interior corners

v20 §4 (cut at the short copy) and v30 (cut at an end of Lambda's O-traversal) use only rows, band values in [1,9], (F1), (F2), and the fact that Lambda's neighbours in each face are other loops; all hold, and global reversal preserves the class. The remaining cuts are O-corners avoiding Lambda: Lambda=D: C|A^-, A^-|B, B|C^-; Lambda=A: C^-|D^-, D^-|C, B|C^-; Lambda=B: C^-|D^-, D^-|C, C|A^-.

## 3. Lambda=D (coordinates along D^-)

- C|A^-: O-band a, a+b, a+b+5, u=a+b+5+p, 5, so a>=1, 1<=a+b<=4, d<=-1. D_L=5-f_0, and f_0+d>=1 forces f_0=9, D_L=-4, r=4. Pure-K' heads are C[1,5] (so E_R is empty and Lambda[L-1] is a Q label) and A[1,1-d] in P. The P-row at B^-|D is B[1,9]+v+Lambda[L-1], so B[1,9] has three Q; O-row 1 is A[1,a]+v+B[1,10-a] with A[1,a] pure K' (b>=0 from f_0+d+a<=9), so B[1,10-a] has four Q. Impossible.
- A^-|B: O-band b, b+5, ... gives 1<=b<=4, 1<=a<=4; D_L=5+a-f_0<=-4 would need f_0>=9+a>=10, so D_L>=4 and the pure-K' tail before Lambda's O-departure is the last b+5>=6 vertices of C^-, longer than k-1<=5.
- B|C^-: O-band 5, 5+p, 5+d, 10+d, 10-b gives d<=-1, b>=1; D_L=5-d-f_0 with f_0>=1-d gives D_L<=4, and D_L<=-4 would need f_0>=9-d>=10, so D_L=4, f_0=1-d, E_L empty (tail C[1,5]) and B^-'s P-tail B[1,1-d] is pure K'. The P-row at D|A (f=1) is Lambda[1]+v+A[1,9] with Lambda[1] in Q, so A[1,9] has three Q; O-row 5 is A[1,10-b]+v+B[1,b] with B[1,b] pure K' (a>=0), so A[1,10-b] has four Q, but 10-b<=9. Impossible.

## 4. Lambda=A (coordinates along A^-)

- C^-|D^-: O-band d, d+5, d+5+p, 5-b, 10-b gives 1<=d,b<=4; D_L=5-d+b-f_0 with 1+b<=f_0<=9-d gives |D_L|<=3.
- D^-|C: O-band 5, 5+p, 5+x, 5-d, 10-d gives 1<=d<=4; D_L=5+b-f_0 with 1<=f_0-b<=9, so f_0=1+b (D_L=4) or f_0=9+b (D_L=-4); r=4.
  - D_L=4: tails C[10,14] (E_L empty) and D[9-b,9+d] (P). The P-row at B^-|D gives labels B[1,1+b] = labels D[10-b,10] (window D[1,10]), pure K'; the P-row at A|B^- (f=1) gives B[1+b,9+b] three Q. C and D have no vertex outside their windows and pure-K' tails, so B holds all four extra Q: b=0 leaves 19 Q copies; b>=1 needs a Q in B[1,b], inside the pure-K' B[1,1+b]. Impossible.
  - D_L=-4 (b<=0): heads B[1,5-x] (O) and B[9+b] (P), |E_L|=4, |E_R|=x. O-row 1 = C[10,14]+v+Lambda[1,5] makes C[10,14] = Q,K',Q,K',Q. The extras C[11,14], D[11,9+d], B[6-x,8+b] carry four Q and two K' (C[11], C[13]); (Q4) forces d=2. The P-rows at B^-|D and D|A give D[2-b,10] = labels of B and D[1-b,11] = O minus (E_R+q_2), hence D[1-b] in Q and B[9+b]=k_2. Each K' label has exactly two copies outside the overlap and the windows; K' = E_L+{k_1,k_2} then forces {C[11],C[13]}={k_1,k_2}. O-row 4 = B[7+b,9+b]+v+C[14..8] contains k_2 twice. Impossible.
- B|C^-: O-band 5, 5+d, 10+d, u, 10-b gives -4<=d<=-1, b>=1; D_L=b-d-f_0<=-4; the window B[b,9+b] keeps its r Q strictly between the pure-K' heads B[1,b] and B[f_0,9+b], i.e. in r-d-1 positions. r=6 needs f_0=10; r=5 puts five consecutive Q (Q5); r=4 needs d=-4, b=1, f_0=9. Then D has five vertices, O-row 1 and the P-row at D|A give C[1,5] one Q, and O-row 2 = D[1]+v+C[1,9] with D[1]=B[10] (pure K') puts three Q in C[6,9]. Impossible.

**Result.** With the short copy on D or A and the cut in O, same-centre 3+5 Type I is impossible. Remaining same-centre 3+5: Type I with the short copy on B and the cut at C^-|D^-, D^-|C or C|A^-; all of Type II. Other m8 placements as in v36.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
