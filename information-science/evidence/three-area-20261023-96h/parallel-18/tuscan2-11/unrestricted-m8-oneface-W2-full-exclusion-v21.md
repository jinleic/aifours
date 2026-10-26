# Actual Tuscan11 one8/ONE face — the whole W2 class is impossible

Actual `/bin/date` before this body: **Sun Oct 25 21:56:20 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed/adopted/formal/executable/novelty cleared. All case splits and integer facts are written by hand; no interpreter, program, enumeration tool, solver or replay. No scientific GO.

## 1. Scope

Builds on the unreviewed v20 (`unrestricted-m8-oneface-classification-and-internal-cut-v20.md`, SHA256 `0a1249ba2d262010efaaba699e2beccb3e9b4142ade16e53ccf515cdd04c642f`): a one8/ONE-face system has one of four words W1–W4, and its unique v-cut lies at a branch corner. This paper excludes every branch corner for

`W2 = A B A^- B^- C D C^- D^-`.

Setting and imports are those of v20 §1 (eleven arbitrary rows, all original K_x/fpGF/simpleM/layers/Hamilton conditions; only Tuscan1 consequences used). Parent-accepted scope remains m>=8 only.

## 2. Tools

Put the v-cut at face0. By v20 §3 the other v-visits are P_m=10m+e_m, e_m in1..9, row m is `TAIL(m-1) v HEAD(m)` with `TAIL(m-1) disjoint-union HEAD(m) = O`, HEAD(m) has10-e_m symbols, TAIL(m-1) has e_m. Gap m has length10+e_(m+1)-e_m. Writing each gap length as10+(excess), the e_m are partial sums of excesses and must lie in1..9.

**(T1) Full loop.** If gap9 is a traversal of an ordinary loop Z ending at the cut, row10 shows the ten interior vertices of Z nearest the cut carry all of O; likewise gap0 and row0. Such Z is called full: every ordinary label occurs on Z.

**(T2) Span-2 exclusion (new).** Let gaps m-1,m,m+1 be X,Y,X^- with1<=m<=8, so X ends and X^- starts at the same branch corner of X's physical end. Write x for the vertex of X next to v there. Row m contains x (last symbol of TAIL(m-1)) and Y's head; row m+1 contains Y's tail and x (first symbol of HEAD(m+1)). Both rows are Hamilton, so the label of x occurs nowhere in Y's interior. If Y is an ordinary loop, the label of x is absent from all of physical Y.

**(T3) Cut uniqueness.** The cuts are the vertices at faces0,10,...,100; every symbol labels exactly one of them.

**(T4) Windows on the short loop.** On the physical path Lambda, opposed whole windows whose starts differ by0,1,2,3 are impossible (actual reverse pair needs two fixed boundaries, beta=0 here; difference1 duplicates an actual row start; differences2/3 repeat an edge of K2/K3 at distinct physical positions). Two physical paths on the same four labels at disjoint positions use all six K4 edges; on five labels, eight of ten K5 edges.

## 3. Reduction to short loop A and the base gap list

The rotation of W2 by four letters (renaming A<->C,B<->D) and global reversal of ALL rows (renaming A<->D,B<->C) generate a group of order four acting simply transitively on the loops. So the short copy may be taken on A. Put the short copy at physical t on A (length L). Base gap list, starting at the corner D^-|A:

|base|0|1|2|3|4|5|6|7|8|9|
|---|---|---|---|---|---|---|---|---|---|---|
|traversal|A[0,t]|A[t,L]|B|A[L,t]|A[t,0]|B^-|C|D|C^-|D^-|
|excess|p|q|beta|q|p|beta|gamma|omega|gamma|omega|

with p+q+beta+gamma+omega=5. Base corners1 and4 are the short-copy visits (excluded by v20 §4). The branch corners are bases0,2,3,5,6,7,8,9; "k" below denotes the base index of the gap starting at the cut.

## 4. Five corners closed directly by (T1)+(T2)

- k0: gap9 is D^- ending at the cut, so D is full. The pattern C D C^- sits at relative gaps6,7,8 and (T2) removes label(C_(c-1)) from D. Contradiction.
- k5: gap0 is B^- starting at the cut, so B is full. The pattern A[t,L],B,A[L,t] sits at relative gaps6,7,8; (T2) removes label(Lambda_(L-1)) from B. Contradiction.
- k6: gap9 is B^-, so B is full; the same A–B–A^- pattern sits at relative5,6,7. Contradiction.
- k7: gap0 is D and gap9 is C, so C and D are full; D C^- D^- sits at relative0,1,2 with middle index1, so label(D_(d-1)) is absent from C. Contradiction.
- k9: gap0 is D^- and gap9 is C^-, so both are full; C D C^- sits at relative7,8,9 with middle index8, so label(C_(c-1)) is absent from D. Contradiction.

## 5. Corner k8 (D|C^-)

Relative gaps: C^-,D^-,A[0,t],A[t,L],B,A[L,t],A[t,0],B^-,C,D, so c,d>=11 and sigma:=gamma+omega>=2. Partial sums give e_4=gamma+omega+p+q=5-beta. The two Lambda windows (rows3 and6) have start difference10-e_3-e_6=beta, so (T4) forces |beta|>=4; with e_4 in1..9, beta=4 or-4.

- beta4 (b=14, L=21-sigma): the windows are F=Lambda[10-sigma,20-sigma] and Bw=Lambda[6-sigma,16-sigma]; K:=labels Lambda[6-sigma,9-sigma]=labels Lambda[L-4,L-1], an exhausted K4. Row5 gives B[9,13]=O minus Lambda[L-5,L-1], so B[9,13] has no K label. Row7 gives B[10-sigma,13]=O minus Lambda[1,6-sigma]; since Lambda[1,10-sigma] is part of row2, Lambda[1,6-sigma] contains exactly one K label, so three K labels lie in B[10-sigma,8]. That segment has sigma-1<=4 vertices (e_7=6-sigma>=1), forcing two adjacent K labels: a repeated K4 edge.
- beta-4 (b=6, L=29-sigma): F=Lambda[L-19,L-9], Bw=Lambda[L-15,L-5], K=labels Lambda[L-19,L-16]=labels Lambda[L-8,L-5], exhausted K4. Rows4 and5 read `Lambda[L-9,L-1] + B_1` and `B[1,5] + Lambda[L-5,L-1]`, so labels B[2,5]=labels Lambda[L-9,L-6], which contains the three K labels of Lambda[L-8,L-6]. Two of them are adjacent on B. Repetition.

## 6. Corner k2 (A[t,L]|B)

Relative gaps: B,A[L,t],A[t,0],B^-,C,D,C^-,D^-,A[0,t],A[t,L]. Use y=L-x on Lambda. Rows10 and9 are the forward windows y[0,10],y[10,20]; row2 is the backward window y[10-beta,20-beta] (e_2=beta+q). (T4) gives beta in{4,5,6}. Subtraction yields H'=labels y[1,9-beta], K=labels y[10-beta,9]=labels y[21-beta,20] (|K|=beta), c10=label y_10, O=H' plus K plus c10. Row1 gives

`labels B[10,9+beta] = (K minus k*) plus c10`, k*=y_(10-beta).

beta4: three K labels among four consecutive B vertices with K4 exhausted. beta5: at least two new K edges, exactly two only with c10 in the middle; then K5 would be complete although k* has degree<=3 (endpoint of one path, absent from B). beta6: row3 gives B^- head = O minus y[14,L-1], disjoint from K; its first vertex B_15 (next to v) also lies in B[10,15], so B_15=c10 and B[10,14]=K minus k*. That is14 K edges with at most three at k*, while at most10 exist among the other five labels. Repetition in all cases.

## 7. Corner k3 (B|A[L,t])

Relative gaps: A[L,t],A[t,0],B^-,C,D,C^-,D^-,A[0,t],A[t,L],B. With y=L-x, rows0 and1 are the backward windows y[0,10],y[10,20]; row8 is the forward window y[10-beta,20-beta] (e_9=10-beta). (T4) gives beta in{4,5,6}. The same subtraction gives H',K,c10, and row9 yields labels B[1,beta]=(K minus k*) plus c10. beta4,5 close as in §6.

beta6: e_2=p+q in1..3 and L=20+e_2. Row7 shows E'':=labels y[21,L-1] avoids K. Row2 reads y[20,L-1]+v+B[6+e_2,15]; with row10 (B[6,15]=O) this gives labels B[6,5+e_2]=y_20 plus E''. Since B_6 lies in B[1,6], its label is in (K minus k*) plus c10; hence B_6 is y_20 or c10. Both are cut labels (faces20 and10), while B_6 is the cut at face100. (T3) is violated.

## 8. Conclusion and residual

Every branch corner of W2 is impossible, and v20 excludes its two short-copy corners. **No actual one8/ONE-face Tuscan1(11) system has face word W2.** This is a NEW written candidate requiring its own complete gate; it inherits no earlier verdict.

Remaining one8/ONE face: W3 and W4 with a branch cut (W1's branch part is only in unreviewed v19). All other m8 placements and all m>=9 remain. **First unproved original step:** a literal11x11 table with110 distinct LINEAR adjacencies and99 distinct LINEAR distance-two events, or a contradiction for every remaining full system. Neither is supplied.

All cadence/private-written-exactness/admission/clock/source histories and the checkpoint045 withdrawal remain unchanged.
