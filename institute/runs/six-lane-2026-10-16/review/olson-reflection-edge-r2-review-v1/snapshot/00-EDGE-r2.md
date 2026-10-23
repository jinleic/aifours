# Lemma EDGE (r2): the edge cells kappa = (p + 1)/2, R in {2p - 2, 2p - 1} have no B = 0 avoider; hence B0S-CJ''' holds under R >= 4 kappa - 4 alone

Owner OlsonReflectionRigidity.  r2 written after host clock 2026-10-18T12:18:58-0700; r1 (893c04ff...fa35, never sent) is superseded:
(K3) is restated cleanly, and Step 5's bookkeeping is unified (fix map at the end).  r1 was written after host clock 2026-10-18T12:17:40-0700.  Status: written proof [W], UNREVIEWED.
Builds on the following, used verbatim:
- proof-B0SCJx-r4.md (f2779c24...843d; parent-accepted with the overlay R/olson-cj-cjx-parent-verdict-v1.md, 5cfd6a4f...45f6d),
  in particular its Sec. 1 items 2-5 (windows, C2(a), C2(b), SIGMA-2P);
- proof-B0S-r4.md Secs. 3-5 (kill conditions L73-75; Case II L91-113);
- proof-B0SPP-r5.md Secs. 1-3.
Scope: B = 0 only.

## 0. Statement

Setting: B = 0, all blocks odd, an avoider of length 4p - 2, p >= 5, kappa >= 1.
**Lemma EDGE.**  No such word has kappa = (p + 1)/2 and R in {2p - 2, 2p - 1}.
**Theorem B0S-CJ''''.**  Theorem B0S-CJ''' (proof-B0SCJx-r4.md) holds with (H''') replaced by R >= 4 kappa - 4 alone.
Proof of the Theorem from the Lemma.  Let R >= 4 kappa - 4 with 2 kappa > p - 1.  Then R <= 2p - 1 gives 4 kappa <= 2p + 3, so
2 kappa = p + 1, and R >= 4 kappa - 4 = 2p - 2.  These are exactly the edge cells, and Lemma EDGE covers them.  []
(Consequence for proof-REFL-B0-r3.md: its hypothesis "2 kappa <= p - 1" can be dropped.  The terminal word has kappa' <= kappa
and R >= 4 kappa' - 4, and its edge cells are covered by Lemma EDGE.)

## 1. Facts in the edge cells

Let kappa = (p + 1)/2 and R in {2p - 2, 2p - 1}.
- Delta = p + kappa - 1 - R <= (3 - p)/2 <= -1.
- k = 2p - R + 2 kappa = 3p + 1 - R lies in {p + 3, p + 2}.
- 4 kappa = 2p + 2.
(F1) Windows, C2(a), C2(b) and SIGMA-2P hold.  proof-B0SCJx-r4 Sec. 1 items 2-5 use only R >= 4 kappa - 4 and R >= p.  So J = 0,
     i.e. sum x_t = p for x_t := w_t, and sum bh_t = k - 2 kappa = 2p - R, which is 2 or 1.
(F2) Every empty run is a defect.  g(R) = min(R - kappa, floor(R/2)) = p - 1, so gap({t}) = [1 - kappa, 0] for r_t = 0.
     Genuineness gives x_t in [1 - kappa, -1], so bh_t = 2 x_t <= -2.
(F3) Defect data (B0S-r4 (2.1)): for a defect t, c_t := r_t + delta_t is even, 2 <= c_t <= 2 kappa - 2 = p - 1.
     c_t = 2 kappa - 2 iff x_t = r_t - kappa + 1, the bottom of gap({t}).
(F4) Phi(P) = rho_P + 2m(P) + delta_P = sum_(t in P) c_t + 2m(P) for P contained in Z (the defects).  Adding one defect t to a set
     of defects raises Phi by c_t + 2, c_t or c_t - 2: t starts a new interval, extends one, or joins two.  So Phi is
     non-decreasing under adding defects.  It is always even.

## 2. Kill conditions in the edge cells

**(K1)** Every proper P contained in Z with 2 kappa + 2 <= Phi(P) <= 4 kappa - 2 = 2p kills.  Check the six conditions of B0S-r4
L74-75:
- (U2) by assumption, and (U3) since delta_P >= 0.
- (U1) and (L1): both left sides are <= Phi(P) <= 2p.
- (L2): delta + rho - 2m = Phi - 4m <= 2p - 4 <= 2R - 2 kappa - 2 = 2R - p - 3, because R >= 2p - 2.
- (L3): delta_P = Phi - rho_P - 2m <= 2p - 2 - rho_P.
  * If rho_P = 0: this is <= R - [R odd], for both R = 2p - 2 and R = 2p - 1.
  * If rho_P >= 1: it is <= 2p - 3 <= R - 1.
**(K2)** Two non-adjacent defects s, t with Phi({s, t}) = 4 kappa = 2p + 2 kill if delta_P >= 1 and rho_P >= 1.
- With m = 2, (U1) reads Phi - 2 delta <= 2p, i.e. delta >= 1.
- (L1) reads Phi - 2 rho <= 2p, i.e. rho >= 1.
- (L2): Phi - 8 = 2p - 6 <= 2R - p - 3.
- (L3): delta = 2p - 2 - rho, as in (K1).
**(K3)** Let t be an empty defect with x_t = 1 - kappa (so delta_t = p - 1), and y a non-defect not adjacent to t (bh_y >= 1).
P := {t, y} kills if
   (a) x_y <= r_y,   (b) bh_y <= p - 1,   (c) x_y <= (3p - 5)/2.
Here rho = r_y, m = 2, delta = p - 1 - bh_y and Phi = p + 3 + r_y - bh_y, with bh_y = 2 x_y - r_y.
- (U2) iff bh_y <= r_y iff (a).
- (U3) iff (b).
- (U1): r_y + 4 - delta = 2 x_y + 5 - p <= 2p iff (c).
- (L1): p + 3 - 2 x_y <= 2p, true as x_y >= (r_y + 1)/2 > 0.
- (L2): p - 5 + 2(r_y - x_y) <= 2R - p - 3 iff r_y - x_y <= R - p + 1.  This is automatic: otherwise
  r_y >= R - p + 2 + x_y >= p + (r_y + 1)/2, so r_y >= 2p + 1 > R.
- (L3): delta = p - 1 - bh_y <= p - 2 <= R - 1.

## 3. Proof of Lemma EDGE

Suppose an edge-cell avoider exists.  Z := the defects; Z is nonempty and proper (B0S-r4 L78-79).
- Case II, Phi(Z) <= 2 kappa: B0S-r4 Sec. 5 kills.  Its numerical conditions hold here:
  - (L3): delta_P <= 2 kappa - 2 = p - 1 <= R - 1;
  - (U1): r_y + 1 <= 2p, and 3 kappa - 7 < 2p;
  - (L1): 4 kappa - 4 = 2p - 2 < 2p;
  - (L2): r_y <= R <= 2R - 4 kappa + 5 for W = {y}, and otherwise 4 kappa - 4 <= 2R - 2 kappa - 2, as 2R >= 4p - 4 >= 3p + 1;
  - |F| >= d/2 holds because k >= 2 kappa + 1 = p + 2.
- Case I, Phi(Z) >= 2 kappa + 2.
Step 1 (reduction to pairwise non-adjacent extreme defects).
- Let P' be an inclusion-maximal subset of Z with Phi(P') <= 2 kappa.  It is nonempty, since Phi({t}) = c_t + 2 <= 2 kappa, and
  proper in Z.
- For every t in Z \ P', maximality and evenness give Phi(P' u {t}) >= 2 kappa + 2, and (F4) gives Phi(P' u {t}) <= 4 kappa.
  If it is <= 4 kappa - 2, (K1) kills.  So assume Phi(P' u {t}) = 4 kappa for every t in Z \ P'.  Then Phi(P') = 2 kappa,
  c_t = 2 kappa - 2, and t is adjacent to no run of P'.
- Fix such a t and an end defect e of some interval of P'.  Put P'' := (P' \ {e}) u {t}.
  * If e's interval has >= 2 defects, Phi(P'') = 4 kappa - c_e, which lies in [2 kappa + 2, 4 kappa - 2]: (K1) kills.
  * If e is a singleton interval, Phi(P'') = 4 kappa - 2 - c_e.  This is >= 2 kappa + 2 unless c_e = 2 kappa - 2; so (K1) kills
    unless c_e = 2 kappa - 2.
- Hence, with no kill so far, every interval of P' is a singleton with c = 2 kappa - 2, and 2 kappa = Phi(P') = 2 kappa |P'|.
  So P' = {e}.  The same argument applies to {t} for each t in Z \ {e}, since {t} is also inclusion-maximal.
- Conclusion: the defects are pairwise non-adjacent, all with c = 2 kappa - 2 = p - 1, and |Z| >= 2 (as Phi(Z) = 2 kappa |Z|).
Step 2 (the pairs).
- For defects s, t: delta_({s,t}) = 2p - 2 - r_s - r_t and rho = r_s + r_t, with each r <= p - 1.
- By (K2) a pair kills unless r_s + r_t = 0 or r_s + r_t >= 2p - 2; the latter means r_s = r_t = p - 1.
- So either every defect is empty with delta = p - 1 ("EB"), or every defect has r = p - 1 and delta = 0 ("FM").  A defect with
  0 < r < p - 1, or an EB-FM pair, gives a killing pair.
Step 3 (FM is impossible).
- The mass gives |Z| = 2.  Then sum_Z delta = 0, so sum_(Y) bh = sum bh = 2p - R <= 2, with Y := [k] \ Z.
- But |Y| = k - 2 >= p and every non-defect has bh >= 1.
Step 4 (EB with |Z| >= 3).
- Take three defects t1, t2, t3 (pairwise non-adjacent, empty, x = 1 - kappa), so m = 3 and E = 0.
- The window is [-g_3(R), g_3(0)] = [3 - p, 2 - kappa]: g_3(0) = min(p - 3, 2 - kappa, 0) = 2 - kappa as kappa >= 3, and
  g_3(R) = min(p - 3, R + 2 - kappa, p - 1) = p - 3.
- x(P) = 3 - 3 kappa, and x(P) + p = 2 - kappa because 2 kappa = p + 1.  So u_P lies in I(P) (mod p): a kill.
Step 5 (EB with |Z| = 2).
- Z = {t1, t2}.  By (F2) these are the only empty runs, so every run of Y := [k] \ Z is nonempty.
- Counts: N_+ := |Y| = k - 2 = 3p - 1 - R, and sum_Y bh = (2p - R) + 2(p - 1) = 4p - 2 - R.
- Suppose no y in Y satisfies (K3) with t1 or with t2.  Let y0 be a run adjacent to both t1 and t2, if one exists; at most one
  exists, since k >= p + 2 >= 7.
- Every other y in Y is non-adjacent to some t_i, so it violates (a), (b) or (c) for that t_i.
  * Not (a): bh_y >= r_y + 2.
  * Not (b): bh_y >= p.
  * Not (c): bh_y >= 3p - 4 - r_y.
  Hence bh_y >= min(r_y + 2, p, 3p - 4 - r_y).  This is r_y + 2 if r_y <= p - 2, and at least p - 3 if r_y >= p - 1 ("big").
  At most two runs are big, since 3(p - 1) > 2p - 1.
- Let S := {big runs} u {y0}, b := the number of big runs other than y0, and e := [y0 exists], so |S| = b + e.  Write M_S for
  the mass of S.  The runs outside S are nonempty, so M_S <= R - (N_+ - |S|) = 2R - 3p + 1 + |S| <= p - 1 + |S|.
- Summing over Y (bh_(y0) >= 1):
  4p - 2 - R >= (R - M_S) + 2(N_+ - |S|) + b(p - 3) + e,
  which, using N_+ = 3p - 1 - R, says M_S >= 2p - 2|S| + b(p - 3) + e.
- Combining the two bounds on M_S: 3(b + e) >= p + 1 + b(p - 3) + e, i.e. 2e >= p + 1 + b(p - 6).
  * b = 0: p <= 1.
  * b = 1: p <= 7/2.
  * b = 2: p <= 13/3.
  Each contradicts p >= 5.  So some y satisfies (K3) for some t_i, and that P kills.
Every case ends in a kill: a contradiction.  []

## 4. Remarks

(1) The finite aid E15b (out/e15b_4_9.json, out/e15b_4_10.json; not a premise) found 0 avoiders in the two p = 7 edge cells
(4, 9, 13) and (4, 10, 12).  This is consistent with the Lemma.
(2) r1 -> r2: see the fix map.

## Fix map r1 -> r2 (author, before sending)

1. (K3): r1's condition (b) contained a garbled expression.  It is now bh_y <= p - 1, which is what the derivation uses.
2. Step 5: r1 bounded the big-run cases separately and omitted y0 in two of them.  r2 uses one inequality, with the mass bound
   M_S <= R - (N_+ - |S|), and covers every combination of big runs and y0.
The statement, the cases, and the conclusion are unchanged.
