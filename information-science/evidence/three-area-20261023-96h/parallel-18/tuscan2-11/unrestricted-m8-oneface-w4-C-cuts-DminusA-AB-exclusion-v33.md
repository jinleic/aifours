# Actual Tuscan11 one8/ONE face — W4 interior corners Lambda=C, cuts D^-|A and A|B are impossible

Actual `/bin/date` before this body: **Mon Oct 26 00:49:38 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Tools

v31 (SHA256 `b8e9ac80393acbc68c21a3ed96b04f214cec5f1a0e9eb4b56b5c6c7a698bc950`) §2–3; (F1), (F2) of v30 §2; (C5), (L2), (Q4), (DEG) of v32 §1 (SHA256 `802a12b583a506ccaf08e59b485b46d0608f3334e5cb7008bad7812aa3f6a2e1`). r=|D|=|Q|, k=10-r. "Extras" are the ordinary vertices outside the two full windows and the two pure-K' segments; by (C5) they carry exactly the Q copies not in Lambda or the windows. (Q5) if r=5 the Q-paths use 8 of the 10 Q-Q edges, so at most two more Q-Q adjacencies exist; (Q6) if r=6, at most five.

## 2. Cut D^-|A (Lambda=C)

Face: A, B, A^-, C[0,t], C[t,L], D, B^-, C[L,t], C[t,0], D^-; excesses alpha,beta,alpha,p,q,omega,beta,q,p,omega. Using the excess sum, e_1..e_9 = alpha, alpha+beta, 2alpha+beta, 2alpha+beta+p (=u), alpha+5-omega, alpha+5, alpha+beta+5, alpha+beta+5+q (=w), 10-omega. So 1<=alpha<=4, 1<=alpha+beta<=4, omega>=1, and D=omega-2alpha-beta. Full windows: row 0 = A[1,10], row 10 = D[1,10].

- D>0: e_5=5-alpha-beta-D<=0. Impossible.
- D<0, r=2alpha+beta-omega: |E_L|=9-2alpha-beta>=1, |E_R|=4-alpha-beta; pure-K' heads HEAD(5)=D[1,5-alpha+omega] and HEAD(9)=the last omega vertices of D. The v31 Lemma gives c_0=2, c_L=1+[alpha+beta<=3], so r=6 is impossible and r=5 forces alpha+beta=4.
  - r=5: the window D[1,10] holds the K' heads D[1,4] and D[10], i.e. all five K' labels, so D[5,9] are five Q labels with four Q-Q edges, against (Q5).
  - r=4: the window's four Q lie in D[6-alpha+omega,9], pairwise non-adjacent (Q4), so alpha-omega>=3: alpha=4, omega=1, beta=-3, and D=D[1,10] is the window. Row 6 = D[2,10] v B[6] gives label(B[6])=label(D[1]), a K' label (head). But the six K' v-edges are already at C[t-1], C[t+1], C[1], C[L-1], D[1], D[10] (F1), so the v-neighbour B[6] is a Q label. Impossible.

## 3. Cut A|B (Lambda=C)

Face: B, A^-, C[0,t], C[t,L], D, B^-, C[L,t], C[t,0], D^-, A; excesses beta,alpha,p,q,omega,beta,q,p,omega,alpha. e_1..e_9 = beta, alpha+beta, alpha+beta+p, 5-omega, 5, 5+beta, 5+beta+q, 5+beta+p+q, 10-alpha; so 1<=beta<=4 and -4<=omega<=4, hence D=omega-beta<0 (D>=4 would need omega>=5) and r=beta-omega. |E_L|=9-alpha-beta, |E_R|=4-beta; pure-K' heads D[1,5+omega] and the last alpha+omega vertices of D, where alpha+omega>=1 because row 9 fits D[1,10-alpha] into D's 9+omega vertices; middle M=D[6+omega,9-alpha]. Rows used: row 2: A[1,alpha+beta]=O minus (E_L+q_1); row 9: D[1,10-alpha]+A[1,alpha]=O; rows 6, 0: B[6+beta,10]={q_2}+E_R; row 1: labels B[10,9+beta] = labels A[alpha,alpha+beta-1]; row 5: D[5+omega,9+omega]+B[5+beta,9+beta]=O. Full windows B[1,10], A[alpha,9+alpha].

- r=6: the Lemma forces beta=4, alpha=5; row 9 makes D[4] a Q and A[1,5] five Q (four Q-Q edges); by the v31 Corollary the four K' labels are non-adjacent in each window, so each window adds a Q-Q edge: six against (Q6).
- r=5: the Lemma forces alpha+beta=9 or beta=4. If alpha+beta=9, row 9 puts all five Q in A[1,alpha], but row 2 allows four. If beta=4, row 9 makes M all Q and A[1,alpha] all Q: (alpha-1)+(4-alpha)=3 Q-Q edges against (Q5).
- r=4: row 9 and row 2 (three Q in A[1,alpha+beta]) put a Q in M, so alpha+beta<=7; and e_8=14-alpha-beta<=9 gives alpha+beta>=5. The four Q extras lie, non-adjacent, in A[1,alpha-1], B[11,9+beta], M. beta=4 (B[10]=q_2 blocks B[11]): at most 3. beta=3: alpha=3 allows at most 3; alpha=2, 4 attain 4 only with a pattern that row 9 turns into a Q-Q adjacency in A[1,alpha]. beta=1: alpha=5 allows at most 3; for alpha=4, 6, (F1) makes the v-neighbour B[10] a Q, hence q_2, so E_R sits on B[7,9] as well as on C[L-3,L-1]: four edges on three labels. beta=2: alpha=4 attains 4 only with A[1,3]=(Q,K',Q), and row 9 then forces A[4] into Q next to A[3]. alpha=3 attains 4 only with M=D[4,6]=(Q,K',Q), B[11] in Q and A[1,3]=(Q,K',Q); rows 2, 9, 1 and HEAD(8)=D[7]=K' minus (E_L+k_1) give one label d7 at A[4], D[7] and B[10], lying in E_R; B[9] must then be q_2 (the E_R pair is already the edge C[L-2]C[L-1]); the five copies of d7 are A[4], D[7], B[10] (no K' neighbour), its E_R copy (one) and its overlap copy (at most two), so its K'-degree is at most 3<5 (DEG). alpha=5 (p+q=0, D=D[1,7], M=D[4]): row 9 and row 2 make D[4] a Q; row 5 and B[8,10]={q_2}+E_R give E_R = K' minus {D[3],D[5],D[6],D[7]}; then D[1,3]=K' minus (k_2+E_R) forces k_2=D[5] (row 9 distinctness) and {D[1],D[2]}={D[6],D[7]}, so the edges D[1]D[2] and D[6]D[7] repeat one pair. Impossible.

**Result.** Both corners are impossible. Remaining one8/ONE-face interior corners: W3 D^-|A (Lambda=B); W4 C|D, C^-|D^- (Lambda=A); D^-|A, A^-|C, C|D, C^-|D^- (Lambda=B); W1 branch part per unreviewed v19. All Lambda=C corners of W4 are now closed (v30, v32, v33).

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
