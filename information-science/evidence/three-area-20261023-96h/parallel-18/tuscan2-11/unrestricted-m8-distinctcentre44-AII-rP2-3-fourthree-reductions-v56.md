# Actual Tuscan11 distinct-centre 4+4, class (a)-II, r_P2 = 3 four/three shape — d = 6, 7 <= x <= 9, and Sigma = 19, 20, 25 excluded

Actual `/bin/date` before this body: **Mon Oct 26 05:54:00 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36).

## 1. Setting

Class (a)-II is as in v47 §1 (v44 pin `c520658a683cb9acea9e9df9905d46f9a3e7688b3e4887f496dee58c1da6a805`), with r_P2 = 3, so |T1|+|T2| = 25 and |T3|+|T4| = 30. The open shape left by v55 (SHA256 `8fef03786d56dad775d69968c14a07ff4af586f39b735b36ed27b93febbda190`) has one run of four rows and one run of three rows, one only-row O and no shared row. The v<->w exchange swaps H1 and H2, so let H1 carry the four-row run.

Notation:
- l = |T1|, and H1 = T1 b_w T2^- = P6[0,25].
- The H1 rows are B_j = H1[10j-o0, 10j+10-o0] for j = 0..3, with o0 in 5..10.
- The H2 rows are D_i = H2[10i-p0, 10i+10-p0] for i = 0..2, with p0 in 1..4. p0 = 0 or 5 would make b_w(W) or b_w(W+25) a boundary.
- Sigma = l + o0 + p0.
- **Exchange identity (E):** for two rows A and C, each containing every symbol once, L(A\C) = L(C\A).
- Cut labels are pairwise distinct: each of the 11 symbols is the label of exactly one cut.

**Counts.**
- D_0 holds b_w(W) and D_2 holds b_w(W+25). So every T1/T2 w-copy has its H2 visit inside D_1, and no w-cut lies in the H2-run. With n_w = 1 + eps_w (P6 contains w eight times), this gives eps_w = X' = 0.
- On the v side, B_0 holds b_v(0) and B_3 holds b_v(25). So B_1 and B_2 take their V from copies or from the H1-run v-cut, which gives eps_v + X = 1. There is exactly one v-cut, in P2 or in the H1-run.

**Row reversal.** Row reversal maps T1<->T2 and T3<->T4, and reverses H1 and H2. Under it o0 -> 15-o0, p0 -> 5-p0, l -> 25-l, hence Sigma -> 45-Sigma. The previously surviving set {19, 20, 21 (p0>=2), 24 (p0<=3), 25, 26} is invariant, so take O inside T3.

Put x = 15-o0 (B_3's T3 part is T3[0..x]) and y = p0 (D_0's T3 part is T3[x+10..lam3]). Then lam3 = x+10+y, lam = |T4| = 20-x-y, and the D_2|B_0 boundary is T4[15-x].

## 2. Boundary coincidence: Sigma = 20 and 25 are impossible

On T1, H1 has boundaries at T1[s] with s ≡ -o0 and H2 at s ≡ l+p0 (mod 10); the residues agree iff Sigma ≡ 0. On T2, H1 has boundaries at T2[s] with s ≡ o0+5 and H2 at s ≡ -l-p0; they agree iff Sigma ≡ 5. A vertex that is a boundary at both of its P6 visits doubles a cut.
- **Sigma = 20, o0 <= 9** (o0 = 10 was already excluded): use T1[10-o0], with 1 <= 10-o0 <= 5 < l = 20-o0-p0.
- **Sigma = 25, o0 >= 6:** use T2[o0-5], interior because o0-5 <= 5 <= 24-l = o0+p0-1.
- **Sigma = 25, o0 = 5:** b_v(25) is the B_2|B_3 boundary and b_v(K) (H2-position l = 20-p0) is the D_1|D_2 boundary.

So Sigma lies in {19, 21 (y>=2), 24 (y<=3), 26}.

## 3. P2 shift: d = 6 and 7 <= x <= 9

Let c ≡ x+d be P2's boundary residue in T3-coordinates. The v55 lemma with B = B_3 and D = D_0 gives:
- d = 5 needs x <= 4, which is impossible;
- d = 4 forces x = 5;
- d = 6 is unrestricted, since y <= 4.

**d = 4, x = 5.** Then c ≡ 9 and lam3 = 15+y.
- If y = 4, the boundary t = 19 is b_w. That makes b_w a P2 cut, against eps_w = 0.
- If y <= 3, the boundaries t = 19 and t = 29 lie at T4-coordinates 11 and 1 (T4-coordinate = 30-t). Since lam = 15-y >= 12, T4[1..11] is a full P2 row inside T4 while O is a full P6 row inside T3. This contradicts v46 (SHA256 `d212cc7d2c8b7907187f0e20732206224cfa0cee0dcfedb41d874342e5d9c5ca`).

So d = 6. P2's boundaries are T3[x-4], T3[x+6] and T4[14-x], which gives three P2 rows:
- R_3 = T3[x-4..1] b_v T4[1..14-x];
- R_- = T3[x-4..x+6], a full row inside T3;
- R_+ = T3[x+6..lam3-1] b_w T4[lam-1..14-x].

(C) R_- and O are full rows overlapping in T3[x..x+6], so L(T3[x-4..x-1]) = L(T3[x+7..x+10]).

**x <= 9.** If x = 10, then B_3 = T3[0..10] starts at b_v(25). The windows R_3, B_3, R_-, O start at -4, 0, 6, 10. (R_3, B_3) and (R_-, O) are clean pairs with k = 4. R_3, R_- are consecutive P2 rows, and B_3, O are consecutive P6 rows. This is the bd clash of v49 (SHA256 `0b02a602b2d03bbea47fc5db072da4d0cba5395900f31c75301dcccadf67ded9`); its bd 5-path is T3[6..10].

**x >= 7.** (E) for R_3 and B_0, which share b_v and T4[1..14-x], gives:

(S) L(T3[1..x-4]) = L(T1[1..x-5]) ∪ {L(T4[15-x])}.

T3[x-4] is a P2 cut, and T1[x-5] and T4[15-x] are P6 cuts (the ends of B_0). So L(T3[x-4]) lies in L(T1[1..x-6]), which forces x >= 7. (For x = 5 the set T1[1..0] is empty and b_v(0) ends B_0.)

## 4. Sigma = 19 is impossible

Here l = 4+x-y. The vertex b_w(l) is interior to B_1, whose T1 arm is T1[x-5..l-1] and whose T2 arm is T2[20-x..24-l]. Also D_0 = T3[x+10..lam3-1] b_w T1[l-1..x-6], and D_2's T2 arm is T2[16-x..24-l].
- (E) for (D_0, B_1): {L(T1[x-6])} ∪ L(T3[x+10..lam3-1]) = L(T2[20-x..24-l]).
- (E) for (D_2, R_+): L(T2[16-x..24-l]) = {L(T4[14-x])} ∪ L(T3[x+6..lam3-1]).

So L(T1[x-6]) lies in {L(T4[14-x])} ∪ L(T3[x+6..x+9]), because it is not in D_0's own T3 part. T1[x-6] is a P6 cut (D_0|D_1), while T4[14-x] and T3[x+6] are P2 cuts. Hence L(T1[x-6]) lies in L(T3[x+7..x+9]), and by (C) in L(T3[x-4..x-1]). By (S) it also lies in L(T3[1..x-4]). B_3 contains T3[1..x] with distinct labels, so L(T1[x-6]) = L(T3[x-4]). That is a P6 cut and a P2 cut with one label, a contradiction.

## 5. Restrictions in the surviving Sigma

- **Sigma = 21** (l = 6+x-y). b_w(l) is interior to B_1, whose T2 arm T2[20-x..24-l] has y-1 vertices. (E) for (D_0, B_1) gives L(T3[x+10..lam3-1]) = {L(T1[x-5])} ∪ L(T2[20-x..24-l]). T3[x+10], T1[x-5] and T2[20-x] are P6 cuts, so L(T3[x+10]) lies in L(T2[21-x..24-l]), which needs **y >= 3**.
- **Sigma = 24** (l = 9+x-y). b_w(l) is interior to B_2 = T1[x+5..l-1] b_w T2[24-l..10-x], and D_2's T2 arm is T2[11-x..24-l]. (E) for (B_2, D_2) gives L(T4[15-x..lam-1]) = {L(T2[10-x])} ∪ L(T1[x+5..l-1]). Its three named vertices are P6 cuts, so L(T4[15-x]) lies in L(T1[x+6..l-1]), which needs **y <= 2**.
- **Sigma = 26** (l = 11+x-y). D_1's T2 arm at b_v(K) is T2[1..9-x]. For x = 9 it is empty and b_v(K) becomes a v-cut inside the H2-run, which is impossible; so **x <= 8**. b_w(l) is interior to B_2, with T2 arm T2[10-x..24-l], and D_2's T2 arm is T2[9-x..24-l]. (E) gives L(T1[x+5..l-1]) = {L(T2[9-x])} ∪ L(T4[15-x..lam-1]). All three ends are P6 cuts, so L(T1[x+5]) lies in L(T4[16-x..lam-1]), which needs **y <= 3**.

## 6. Result

In the four/three shape of class (a)-II with r_P2 = 3, and O inside T3 after row reversal:
- P2's shift is d = 6;
- 7 <= x <= 9;
- Sigma = 19, 20, 25 are impossible.

The survivors are:
- Sigma = 21 with y in {3, 4};
- Sigma = 24 with y in {1, 2};
- Sigma = 26 with x in {7, 8} and y in {1, 2, 3}.

No contradiction is claimed for these survivors. In the trial case Sigma = 21, x = 7, y = 3, the pairwise exchange identities I wrote out did not conflict as label-set equations (this is a written observation, not an existence claim). So I expect the next step there to need the edge-distinctness (DUP) of individual adjacencies. Class (a)-II is open only in these survivors and in the four/four shape at Sigma = 21 (v52).

Also open: class (b) d = 1, 3, 5; distinct 3+5; all m>=9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories and the checkpoint045 withdrawal remain unchanged. This candidate needs its own complete source-bound gate.
