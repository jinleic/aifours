# Actual Tuscan11 one8/ONE face — the last seven interior corners are impossible

Actual `/bin/date` before this body: **Mon Oct 26 01:04:15 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Tools

As v33 §1 (SHA256 `9d07c7aa6d4e13f120e5c438941f89239a18243ffbd3da0d0e8a3d044e44c362`): v31 bookkeeping, Lemma and q=6 Corollary; (F1), (F2), (C5), (L2), (Q4), (Q5), (Q6), (DEG); (T4) |D|>=4; band values e_1..e_9 lie in [1,9]. P=p+q. "TAIL(i-1), TAIL(j-1)" (D>0) and "HEAD(i+2), HEAD(j+2)" (D<0) are the pure-K' segments of v31 §2.

## 2. W4, Lambda=B: band arithmetic alone

Each face is read from the cut; the excess sum is alpha+gamma+omega+P=5.

- Cut D^-|A: D=gamma+omega-alpha, e_3=5-gamma-omega, e_6=alpha+5, e_8=10-gamma-omega. D>=4 gives e_3<=1-alpha<=0; D<=-4 gives e_8>=14-alpha>=10.
- Cut A^-|C: D=alpha-gamma-omega, e_4=5-alpha, e_6=5+gamma+omega-alpha, e_7=5+gamma+omega. D>=4 and e_6>=1 force alpha=gamma+omega+4, so e_4=1-gamma-omega<=0; D<=-4 gives e_7>=9+alpha>=10.
- Cut C|D: D=alpha+gamma-omega, e_3=5-alpha-gamma, e_8=10-alpha-gamma. D>=4 gives e_3<=1-omega<=0; D<=-4 gives e_8>=14-omega>=10.
- Cut C^-|D^-: D=gamma-alpha-omega, e_2=alpha+omega, e_4=5-gamma, e_7=5+alpha+omega. D>=4 gives e_4<=1-e_2<=0; D<=-4 gives e_7>=9+gamma>=10.

All four are impossible.

## 3. W4, Lambda=A, cut C|D

Face D, B^-, C^-, D^-, A[0,t], A[t,L], B, A[L,t], A[t,0], C; e_1..e_9 = omega, omega+beta, omega+beta+gamma, 2omega+beta+gamma, (u), 5+omega, 5+omega+beta, (w), 10-gamma; D=-(2omega+beta)<0, r=2omega+beta; |E_L|=9-2omega-beta-gamma, |E_R|=4-omega-beta; pure-K' heads B[1,5-omega], C[1,gamma]; windows D[1,10], C[gamma,9+gamma]. Row 1 = D[10,9+omega] v B[9+beta..beta+omega] and row 7 = B[5-omega,9+beta] v ({q_2}+E_R).

- r=4: beta=4-2omega and e_2=4-omega>=1 give omega<=3. Rows 1 and 7 give labels D[10,9+omega] plus label B[4-omega] = {q_2}+E_R, but B[4-omega] lies in the head B[1,5-omega]=K' minus (k_2+E_R). Impossible.
- r=5: the Lemma leaves (omega,beta)=(1,3) with E_R empty, or E_L empty (gamma=4) with (omega,beta) in {(2,1),(3,-1),(4,-3)}. (1,3): row 2 makes C[4+gamma,9+gamma] = Q+{k_2}, three Q-Q edges against (Q5). (2,1): row 2 gives C[7,13]=Q+{k_2}+E_R, so the window C[4,13] needs C[5],C[6] in K', and row 3 then puts six distinct K' labels in C[1,7]. (3,-1): row 2 gives C[6,13] with three K', so C[5] is K', C[1,5] is all of K', and row 3 makes D[9,12] four Q (three Q-Q edges). (4,-3): rows 1, 7 give D[10,13]={q_2}+E_R (one Q), but row 3 gives D[9,13] at least four Q.
- r=6: the Lemma forces (omega,beta,gamma)=(2,2,3), E_L=E_R empty; K4(K') is exhausted by the overlap, C[1,3], B[1,3], so C[4] (next to C[3]) is not K'; row 2 gives C[7,12] at most one K', so the window C[3,12] holds at most C[3], one of C[5],C[6], one of C[7,12]: three K' <4.

## 4. W4, Lambda=A, cut C^-|D^-

Face D^-, A[0,t], A[t,L], B, A[L,t], A[t,0], C, D, B^-, C^-; e_1..e_9 = omega, (u), omega+P, 5-gamma, (w), s_B, 5+P, 5+P+omega, 10-gamma; D=beta+2gamma. D<=-4 contradicts e_3=5-beta-gamma<=9. So D=r>0, |E_R|=4-beta-gamma, pure-K' tails D[1,omega] and the last 5-gamma vertices of B; windows D[omega,9+omega], C[1,10]; row 3: HEAD(3)=B[1,10-e_3]=O minus ({q_2}+E_R); row 9: B[1,10-gamma] v the last gamma of C.

- r=4: e_8=6+gamma<=9 gives gamma<=3; rows 3, 9 put B[10-gamma] in {q_2}+E_R, yet it lies in the K' tail avoiding E_R. Impossible.
- r=5: E_R empty gives (beta,gamma)=(3,1) and row 8 puts five Q and one K' on six consecutive D vertices (three Q-Q edges). E_L empty gives omega=4, P=gamma-4, gamma in {2,3,4}: rows 6, 10, 9, 3 give C[10]=q_1=q_2 and the last gamma-1 C-vertices = E_R; row 7 then forces E_R into K' minus D[1,4], a single label, so gamma=2, and D[5,7] are three Q while D[7,13] adds two more Q-Q edges: four against (Q5).
- r=6: (beta,gamma,omega)=(2,2,3), E_L=E_R empty; row 8 gives D[7,12] at least five Q; D[4] (next to the tail end D[3]) is not K'; the window D[3,12] then holds at most three of the four K'.

## 5. W3, Lambda=B, cut D^-|A

Face A, B[0,t], B[t,L], A^-, C, B[L,t], B[t,0], D, C^-, D^-; e_1..e_9 = alpha, (u), 5-gamma-omega, 5+alpha-gamma-omega, 5+alpha-omega, (w), 10-gamma-2omega, 10-gamma-omega, 10-omega; D=gamma+2omega-alpha. D<=-4 with e_5<=9 gives gamma+omega<=0, contradicting e_8<=9. So D=r>0, |E_L|=9-gamma-2omega, |E_R|=4-gamma-omega, pure-K' tails A[10,9+alpha] and the last 5+alpha-omega vertices of C; windows A[1,10], D[1,10].

- r=6: (gamma,omega,alpha)=(-1,5,3). Rows 3, 0 give A[1,3]={q_2}+A[11,12]; K4(K') is exhausted, so A[2]=q_2 and A[4] is Q; row 4 leaves C[1,5] one K'; row 9 gives D[10,14] two Q; C[5] cannot be K' (next to the tail C[6,8]), so row 8 gives D[9,14] five Q. Impossible.
- r=5: E_R empty: row 8 puts five Q and one K' on six consecutive D vertices. E_L empty (alpha=4, gamma=9-2omega, omega in {6,7,8}): rows 3, 0 give A[1,omega-1]=A[11,13]+{q_2}+E_R with one Q (omega=8 needs six K'); rows 4, 9 give labels D[10,9+omega] = labels A[1,omega] (at most two Q), while row 8 puts at least four Q there.
- r=4: rows 3, 0 give A[1,omega] = A[11,9+alpha]+{q_2}+E_R (one Q), so the window forces omega<=4; rows 7, 10 give D[alpha+5,10]=E_L+{q_1}; row 8 puts all four Q, non-adjacent, in D[alpha+4,9+omega], so D[11,9+omega] holds at least two, forcing omega=4, D[11], D[13], D[alpha+4] in Q and D[10], D[12] in K'; q_1 then sits in D[alpha+6,9], so alpha=gamma+4<=3; rows 4, 9 give D[10,13]=A[1,5] minus C[6], hence A[5] in Q and C[6] (a tail label outside E_R) in A[11,9+alpha]. alpha=1: that set is empty. alpha=2: write x=A[10], y=A[11]=C[6]; the edge xy is the tail A[10]A[11], so the tail C[5]C[6]C[7]=K' minus (E_R+B[14]) avoids x, i.e. B[14]=x; x then has only four copies (A[10], B[14], one in D[1,6], one in C[1,4]) against (C5). alpha=3: with E_L={e_R,e'}, E_R={e_R}=D[10], m=B[7], x=A[10], {y_c,y'}=A[11,12], y_c=C[6]: copy counting forces C[7,8]={m,x}, C[5]=e', B[13]=y'; e_R's copies B[1..2] (one K' neighbour), B[18], D[10] (none) force its A-window copy A[3] between two K' (A[1]=q_2) and its overlap copy B[8] between m=B[7] and x=B[9]; avoiding the edges e'y_c (C[5]C[6]) and y_cy' (A[11]A[12]) forces t=B[11], B[10]=y_c, B[12]=e'. Then e' has copies in B[1..2] (one K' neighbour), A[6] or A[8] (none), D[8] (none), B[12] (one: t, y'), C[5] (at most two): at most 4<5 (DEG).

**Result.** All ten interior corners of v30 §4 are closed (v32, v33, this packet). With v20 (no cut at the short copy), v30 (no cut at a short-loop end), v21 (W2) and the earlier W3/W4 corners (v22, v23), every one8/ONE-face case of W2-W4 is excluded; W1 rests on unreviewed v19 with v20 §4. The m8 residual of manifest v5 now reduces to: same-centre 3+5 Type I cut in O and all Type II; 4+4 F2; distinct 3+5 connected or reverse-pair; and m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
