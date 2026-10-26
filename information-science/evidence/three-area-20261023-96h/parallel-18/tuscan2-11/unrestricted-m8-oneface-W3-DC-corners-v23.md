# Actual Tuscan11 one8/ONE face, word W3 — both cuts inside the D C^- D^- pattern are impossible

Actual `/bin/date` before this body: **Sun Oct 25 22:14:29 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed/adopted/formal/executable/novelty cleared. Written reasoning only; no interpreter, program, enumeration tool, solver, replay or GO.

## 1. Scope

Word `W3 = A B A^- C B^- D C^- D^-`, one8/ONE face, branch cut. Tools and notation: v21 §2 (band identity e_m, full loops, span-2, cut uniqueness, Lambda windows) and v22 §2 (Case S/Case T window complements). Predecessors: v20 SHA256 `0a1249ba2d262010efaaba699e2beccb3e9b4142ade16e53ccf515cdd04c642f`, v21 SHA256 `770ed4f5356e2ed1e0084f444c0dda1a33a6c79deaee2c4bb1b981fba02b8589`, v22 SHA256 `1894d359e0ce0f94b6db42aee0fe678233868863ff1e627381860f7faf612949`. W3's reversal symmetry (A<->D, B<->C) leaves short loop Lambda in{A,B}. This paper closes the cuts C^-|D^- and D|C^- for BOTH choices; together with v22 §3 this finishes W3 apart from the cases listed in §5.

Write c=10+gamma, d=10+omega, b=10+beta, a=10+alpha for ordinary loops; Lambda=[0,L] with short copy at t, forward parts excess p=t-10, q=L-t-10.

## 2. Cut C^-|D^- (gap9=C^-, gap0=D^-, gap8=D)

Rows10 and0 give C[1,10]=O and D[omega,9+omega]=O. Row9 is D-tail D[gamma+omega,9+omega] then v then C^- head C[10,9+gamma]; so

`Z := labels C[10,9+gamma] = labels D[omega,omega+gamma-1]`.

gamma=1 makes the cuts C_10 (face100) and D_omega (face10) share a label; gamma=2,3 put two physical paths on the same2 or3 labels. So gamma>=4. In both choices of Lambda the band value at the fourth corner is e_4=5-gamma>=1, hence **gamma=4** and the paths C[10,13], D[omega,omega+3] exhaust K4(Z).

**Lambda=A.** Gaps: D^-,A[0,t],A[t,L],B,A[L,t],A[t,0],C,B^-,D,C^-. Row7 is C-tail C[9-p-q,13] (e_6=1+p+q>=1, so it contains Z) then B^- head; row8 is B^- tail then D-head D[1,4+omega] (contains Z). Thus B avoids Z. The Lambda windows have start difference 10-u-w=8+beta, so beta in[-4,0], Case S, |Q|=2-beta, |K'|=8+beta. B follows A[t,L]; its head is (K' minus k_F)+(Q minus E1) with E1=Lambda[t-u+11,L-1], |E1|=-beta. As B avoids Z, at most one Z label lies in K' and the remaining at least three lie in E1. Three Z labels among at most four consecutive Lambda vertices repeat a K4(Z) edge.

**Lambda=B.** Gaps: D^-,A,B[0,t],B[t,L],A^-,C,B[L,t],B[t,0],D,C^-. Band values e_5=1+alpha and e_6=5+alpha lie in1..9, so alpha in[0,4]; the windows have 10-u-w=4-alpha, forcing alpha=0. Then A has length10 and e_4=1, so HEAD(4) is all of A's interior A_9..A_1, ending with the cut A_1 (face50); row5 is A_1 then v then C[1,9]. With row10 (C[1,10]=O) this gives label(C_10)=label(A_1): two cuts (faces100 and50) share a label.

## 3. Cut D|C^- (gap9=D, gap0=C^-, gap1=D^-)

Row0 gives C[gamma,9+gamma]=O, row10 gives D[omega,9+omega]=O, row1 is C^- tail C[1,gamma] then v then D^- head D[omega+gamma,9+omega]. So Z:=labels C[1,gamma]=labels D[omega,omega+gamma-1]; gamma=1 makes the cuts C_1 (face10) and D_omega (face100) share a label, gamma=2,3 repeat an edge, hence gamma>=4. Row2 is D^- tail D[1,gamma+omega] then v then HEAD(2), so HEAD(2) avoids Z.

**Lambda=A.** Gaps: C^-,D^-,A[0,t],A[t,L],B,A[L,t],A[t,0],C,B^-,D. Then e_5=5 and 10-u-w=beta, while e_4=5-beta in1..9; so beta=+-4.

- beta4: Case S with |K'|=4, |Q|=6, e_4=1, e_5=5. HEAD(2) contains every K' label, so Z lies in Q. B's head is B[1,9]=O minus k_F (hence E1 empty) and B's tail is B[9,13]=Q minus q_B. If gamma>=5, counting Z edges on Lambda's two overlap paths, on B[9,13] and on the C and D paths exceeds the K5 or K6 total. If gamma=4: e_7=2-omega forces omega=1; q_B must lie in Z (else four Z labels in five consecutive vertices) and B[9,13]=Z W Z W Z. The SAME positions are B^-'s head (e_8=5), so row8 gives C[9,13]=K' plus q_B: four K' labels in five consecutive vertices repeat a K4(K') edge.
- beta-4: then omega=5, gamma=4, p+q=0, L=20, Case T with F=Lambda[1,11], Bw=Lambda[5,15], K'=labels Lambda[1,4]=labels Lambda[12,15]. b=6. Rows4 and5 give labels B[2,5]=labels Lambda[11,14], containing three K' labels of Lambda[12,14] in four consecutive B vertices. Repetition.

**Lambda=B.** Gaps: C^-,D^-,A,B[0,t],B[t,L],A^-,C,B[L,t],B[t,0],D. e_5=5, e_7=5+alpha+gamma<=9 and gamma>=4 give alpha+gamma<=4; the windows give |gamma+alpha|>=4, and gamma+alpha<=-4 would need alpha<=-8, making e_6=5+alpha<1. So gamma+alpha=4 (Case T, |K'|=4). C has length10+gamma with forward band value e_6=9-gamma, so its tail is C[gamma+1,9+gamma] = O minus label(C_gamma) by row0. The Case T complement makes that tail (K' minus k_Btop)+(Q minus E1'), where k_Btop is the top cut of Lambda's backward window. Hence label(C_gamma)=k_Btop: the cuts C_gamma (face10) and k_Btop share a label.

## 4. Conclusion

In W3 the cuts C^-|D^- and D|C^- are impossible for every short-loop position. With v22 §3, W3 is excluded at every branch corner EXCEPT the Lambda-incident delta=4 saturated corners (Lambda=A: cuts D^-|A, A|B, B|A^-; Lambda=B: A|B, B|A^-, B^-|D) and the interior corner D^-|A for Lambda=B.

## 5. Residual and status

Remaining one8/ONE face: the W3 corners just listed; W4 as listed in v22 §5; W1's branch part only in unreviewed v19. All other m8 placements and all m>=9 remain. **First unproved original step:** a literal11x11 table with110 distinct LINEAR adjacencies and99 distinct LINEAR distance-two events, or a contradiction for every remaining full system. Neither is supplied. Needs its own gate; inherits no verdict. All process histories and the checkpoint045 withdrawal remain.
