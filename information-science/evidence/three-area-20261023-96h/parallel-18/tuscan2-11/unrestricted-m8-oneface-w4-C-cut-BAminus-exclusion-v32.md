# Actual Tuscan11 one8/ONE face — W4 interior corner Lambda=C, cut B|A^- is impossible

Actual `/bin/date` before this body: **Mon Oct 26 00:42:40 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Tools

v31 (SHA256 `b8e9ac80393acbc68c21a3ed96b04f214cec5f1a0e9eb4b56b5c6c7a698bc950`) §2 window bookkeeping and Lemma; (F1), (F2) of v30 §2. Write r=|D|=|Q| and K'=O minus Q. Further:

- (C5) every label has five copies; a full window (rows 0, 10 at an interior cut) holds exactly one copy of every label.
- (L2) every ordinary loop has at least two interior vertices (a loop v-x-v would repeat the edge {v,x}).
- (Q4) if r=4 the two Q-paths of Lambda carry 3+3=6 Q-Q edges, all of K4(Q) by (F2); hence no two Q labels are adjacent off those paths.
- (DEG) by (F2) each K' label is adjacent to the other k-1 labels of K' exactly once, so its copies have K'-neighbour counts summing to k-1.

## 2. The corner

Face from the cut: A^-, C[0,t], C[t,L], D, B^-, C[L,t], C[t,0], D^-, A, B with excesses alpha,p,q,omega,beta,q,p,omega,alpha,beta, alpha+beta+omega+p+q=5. Band values e_1..e_9: alpha, alpha+p (=u), alpha+p+q, 5-beta, 5, 5+q (=w), 5+p+q, 10-alpha-beta, 10-beta; so 1<=beta<=4. Here i=1, j=5, t=10+p, L=20+p+q, s_F=10-alpha, s_B=5+p+q, D=beta+omega. Full windows: row 0 = A[alpha,9+alpha], row 10 = B[beta,9+beta].

## 3. D>0

e_3=alpha+p+q=5-D>=1 forces D=4=r, alpha+p+q=1, E_R empty, |E_L|=5-alpha. The pure-K' tails are TAIL(0)=A[1,alpha] and TAIL(4)=B[1,5]. So A and B consist of their windows and parts of these tails; by (C5) the four remaining Q copies all lie in D. Row 3 = C[L-1] v D[1,9], and C[L-1] is the last vertex of the second Q-path (E_R empty), so D[1,9] holds three Q and six K'. Counting K' copies (overlap 6, E_L 5-alpha, A 5+alpha, B 5+beta) leaves 9-beta K' copies for D.

- beta=4: D=D[1,9] would need six K' copies but has 5. Impossible.
- beta<=3: B[beta,5] is K', so the window's four Q lie in B[6,9+beta], pairwise non-adjacent by (Q4); hence beta=3 and Q sits exactly at B[6],B[8],B[10],B[12]. Then D has ten vertices, D[10] is its fourth Q, and row 4 = D[9,10] v B[12..5] carries five Q-labelled vertices. Impossible.

## 4. D<0

e_3=alpha+p+q=5+r<=9 forces r=4, omega=-4-beta, so D has 5-beta interior vertices and, by (L2), beta<=3. Also |E_L|=9-alpha, |E_R|=4, e_7=5+p+q<=9 and e_8=1+p+q-beta>=1, so alpha=9-(p+q)>=5. The pure-K' heads are HEAD(3)=D[1] and HEAD(7)=the last alpha-4>=1 vertices of D. Row 1 gives A[1,alpha]=O minus (E_L+q_1), which holds three Q labels; row 5 gives B[1,5]=O minus (E_R+q_2): three Q and two K', so by (Q4) Q sits at B[1],B[3],B[5]. Row 4 = all of D v B[9+beta..5]; subtracting the window's Q in B[5,9+beta] gives D exactly 2, 1, 1 Q labels for beta=1, 2, 3; by (Q4) they are non-adjacent and avoid both heads.

- beta=1: two non-adjacent Q inside D[2,8-alpha] with alpha>=5. Impossible.
- beta=3: D=D[1],D[2] lies in the two heads. Impossible.
- beta=2: forces alpha=5, D=(K',Q,K'), A[1,5]=Q K' Q K' Q, K' minus E_L = {A[2],A[4]}, and D[3]=HEAD(7)=K' minus (E_L+k_1) is one of them, say a. The five copies of a are then A[2] or A[4], D[3], the overlap, the A-window and the B-window B[2,11]; so a is not in E_R, hence a is a K' label of B[1,5], and its B-window copy is B[2] or B[4]. The copies at A[2]/A[4], D[3], B[2]/B[4] have no K' neighbour, so by (DEG) a has at most 2+2=4<5 K' neighbours. Impossible.

**Result.** The one8/ONE-face cut B|A^- with Lambda=C is impossible. Remaining interior corners: W3 D^-|A (Lambda=B); W4 C|D, C^-|D^- (Lambda=A); D^-|A, A^-|C, C|D, C^-|D^- (Lambda=B); D^-|A, A|B (Lambda=C); W1 branch part per unreviewed v19.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
