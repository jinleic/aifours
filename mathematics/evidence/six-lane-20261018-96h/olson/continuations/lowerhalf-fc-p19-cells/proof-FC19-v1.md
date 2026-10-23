# FC19: the two p=19 terminal cells (kappa,p) = (7,19) and (8,19), final count at levels 5 and 6, v1

Owner: OlsonThirdCutWindow (same math2 slot). Drafted by hand after /bin/date 2026-10-20T10:24:30-0700.
Status: WRITTEN CANDIDATE, NOT YET REVIEWED OR ACCEPTED. Both proofs complete relative to accepted UMR scope.
Scope freeze: FC19-scope-v1.md, SHA256 889acf673aed2005ee3ab412d5d82050c7026d053e54844574a000619eee3c05, frozen
2026-10-20T10:04:27-0700 before any new derivation. Authority: written-olson-fc-p19-cells-transition-v1.json, SHA256
9c04963a8d484c774812fe549a8552004bdf2a0bce57e584c80b627de708e094, LF1-49 (absolute paths in Sec. 5).
OUTCOME, SEPARATELY FOR EACH CELL: (7,19) is EXCLUDED (Theorem FC19(a), Sec. 3); (8,19) is EXCLUDED (Theorem
FC19(b), Sec. 4); both relative to the accepted UMR scope (verdict CORRECTNESS_ACCEPTED_SCOPED_PARTIAL, read through
parent errata v1 and v2). No failing step remains in either cell. Written by hand; no computation, enumeration,
solver, test or assertion over mathematical objects. No claim about any other cell, prime, kappa or k.

## 0. Exact statement and premises

THEOREM FC19. Let (kappa,p) be (7,19) or (8,19). No word of length 74 over D_38 without an identity 38-subword in
increasing original index order has SOME admissible NF with terminal k = 20 and kappa_hat = kappa. The extra reflection
pairs may lie anywhere in the odd blocks, every empty NF run separates different reflection values, and no o_F,
nonempty-run, rotation-pair or rigidity hypothesis is imposed. Part (a) is the cell (7,19), part (b) the cell (8,19);
each part is proved on its own (Secs. 3 and 4) and neither part uses the other.

Premises (accepted UMR, literal scopes, through errata v1 and v2): the frame definitions, UMR-F, Lemma 2 (windows),
Lemma 5(b)-(d), Lemmas 7-8 (offsets and representatives), Lemma 10 (empty runs), Lemma 13 (U' = Theta) and Lemma 14
(identity). Both cells lie in UMR's range T: floor((19+7)/4) = 6 < kappa <= 8 = (19-3)/2. UB, RES, Lemmas 15-20 and
UMR's unproved Lemma FC are NOT used; no saturation, characterisation or converse of Lemma 20 is used. What is proved
here is, for these two cells only, the inequality that UMR left open: Xi(S_ev)+Xi(S_od) <= -1 in EVERY frame of EVERY
target NF. FC717 (not accepted) supplied method inspiration only; no FC717 lemma or constant is used.

NEW COUNT LEMMAS. WC719 (Sec. 3) and WC819 (Sec. 4): the data (D1)-(D3) of Sec. 1 imply Xi(S_ev)+Xi(S_od) <= -1.
With the identity (D4), Xi(S_ev)+Xi(S_od) = e >= 0, this is a contradiction, so no frame and hence no NF exists.

## 1. Literal inputs from accepted UMR

Common constants: N = 20 runs (indices mod 20), h = 10, p = 19, 2p = 38 (UMR LF18-19).
(7,19): R = 32, g = 6, delta = 8, H = 11, central levels 3..8.  (8,19): R = 34, g = 4, delta = 12, H = 10, central
levels 2..9. (UMR LF18-19 and LF64-66; UMR Sec. 6 LF344-355 lists the same values.) Fix ANY admissible NF of the cell
and ANY frame of it (UMR LF111-112: a frame exists and every frame has the properties below).
(D1) Letters. The R letter OCCURRENCES are partitioned into the sets L_0,...,L_19 of letters of the runs (L_i empty iff
     run i is empty). Each letter l has an odd nonzero integer c_l (UMR LF88-110). A := {l : c_l < 0}, A^c := {c_l > 0},
     a := |A|, a' := R-a, nu := nu0 = sum over A of |c_l|, e := e* = sum over all l of (|c_l|-1). Then
       (1) e >= nu-a >= 0,   (2) nu = a (mod 2),   (3) a' >= 14.
     Proof. e = (nu-a)+(Pi0-a') with Pi0 = sum over A^c of |c_l| (UMR LF107-108), and UMR Lemma 5(d) (LF118) gives
     nu >= a, Pi0 >= a' and a' >= (p+kappa+1)/2, i.e. a' >= 27/2 at (7,19) and a' >= 14 at (8,19); every |c_l| is odd.
(D2) Theta. Each run i has an integer theta_i; if run i is empty, theta_i is a NONZERO EVEN integer (UMR-F LF24-28,
     Lemma 10 LF201-209). Theta(Q) := sum over i in Q of theta_i.
(D3) Windows. S_ev := {0,2,...,18} and S_od := {1,3,...,19}; each has 10 pairwise non-adjacent runs. A subset Q of
     either with |Q| = j, 1 <= j <= 9, is a proper independent set with m(Q) = j (UMR LF55-56, LF252-254). For a run
     set Q put q(Q) := |L(Q) symdiff A| and q'(Q) := R-q(Q) (UMR Lemma 5(b),(c), LF114-118), eps(Q) := q(Q) mod 2, and at
     a central level j, with (ell_j, M_j) := (2kappa+2-2j, 2j-g) (UMR Lemma 2, LF64-66),
       x_j(Q) := max(eps, ell_j-q, M_j-q'),   y_j(Q) := max(eps, M_j-q, ell_j-q')   (UMR Lemma 7, LF137-139).
     UMR Lemma 8 (LF161-165) gives low(Q) <= U'(Q) <= up(Q) with up(Q) = -2-nu+x_j(Q) and
     low(Q) = Pi0+2-y_j(Q)-2p = e-g+2-nu-y_j(Q) (as Pi0 = B*-nu0 = R+e-nu and R-2p = -g), and UMR Lemma 13 (LF238-247)
     gives U'(Q) = Theta(Q). Hence, for every j-subset Q of S_ev or S_od with j central:
       (U_j)  Theta(Q) <= -2-nu+x_j(Q),        (L_j)  Theta(Q) >= e-g+2-nu-y_j(Q).
     Used instances: at (7,19) only (U_5), with (ell_5,M_5) = (6,4). At (8,19) (U_5), (U_6) and (L_5), with
     (ell_5,M_5) = (8,6) and (ell_6,M_6) = (6,8).
(D4) Identity. Xi(S) := Theta(S)+nu+g/2 (UMR LF254, h-kappa = g/2). UMR Lemma 14 (LF256-258):
       Xi(S_ev)+Xi(S_od) = e >= 0.
WC719 and WC819 use only (D1)-(D3); (D4) is used once, at the end of each part.

## 2. Common notation and elementary facts

For a run set Q: L(Q) := union of the L_i (i in Q), l(Q) := |L(Q)|, n(Q) := number of nonempty runs of Q, e(Q) :=
number of empty runs of Q, and
  alpha(Q) := |A \ L(Q)|,  beta(Q) := |L(Q) n A^c|,  alpha'(Q) := |A^c \ L(Q)|,  beta'(Q) := |L(Q) n A|.
Then q(Q) = alpha(Q)+beta(Q), q'(Q) = alpha'(Q)+beta'(Q) (UMR Lemma 5(c)), l(Q) = beta(Q)+beta'(Q),
beta'(Q) = a-alpha(Q) <= a and beta(Q) = a'-alpha'(Q). For a single run v write alpha(v), beta(v), beta'(v) etc.
(F1) n(Q) <= l(Q). Disjoint run sets have disjoint letter sets (letters are occurrences).
(F2) Let Q1, Q2 be disjoint run sets. Then a <= alpha(Q1)+alpha(Q2) and a' <= alpha'(Q1)+alpha'(Q2), and at most
     alpha'(Q1)+alpha(Q2) letters lie outside L(Q1) u L(Q2).
     Proof. A letter of A lies outside L(Q1) or outside L(Q2) (the two sets are disjoint); likewise for A^c. A letter
     outside both lies in A^c \ L(Q1) or in A \ L(Q2). []
(F3) Sorting. For each alternating set S fix one order of its 10 runs by decreasing theta (ties arbitrary); J_j(S) is
     the set of the first j runs, t_j(S) the j-th value and B_j(S) := S \ J_j(S) (10-j runs). Runs of J_j have
     theta >= t_j, runs of B_j have theta <= t_j. By (D2) an empty run with theta >= -1 has theta >= 2, and one with
     theta <= 0 has theta <= -2. Hence:
     (a) t_j >= 0 implies Theta(J_j) >= 2e(J_j) >= 2(j-l(J_j));
     (b) t_j >= -1 implies Theta(J_j) >= 2e(J_j)-n(J_j) = 2j-3n(J_j);
     (c) t_j <= -1 implies Theta(B_j) <= -(10-j)-e(B_j);
     (d) t_j <= -2 implies Theta(B_j) <= -2(10-j);
     (e) t_j <= 0 implies Theta(B_j) <= -2e(B_j);
     (f) Theta(J_j) <= -1 implies t_j <= -1, and Theta(J_j) <= j-1 implies t_j <= 0.
(F4) Offsets. Since eps <= 1: if q <= ell_j-2 then q' = R-q > M_j, so x_j = ell_j-q; if q' <= M_j-2 then x_j = M_j-q';
     x_j <= 1 iff q >= ell_j-1 and q' >= M_j-1. (Here R >= 32 > ell_j+M_j.)

## 3. Part (a): the cell (7,19)

Here R = 32, g/2 = 3, Xi(S) = Theta(S)+nu+3, and only level 5 is used: x_5 = max(eps, 6-q, 4-q'). For an alternating
set S write J := J_5(S), t := t_5(S), B := B_5(S) (five runs). By (F4) the TYPE of J is exactly one of
  G: q(J) >= 5 and q'(J) >= 3, so x_5(J) <= 1;
  Q: k := q(J) <= 4, so x_5(J) = 6-k;
  P: k := q'(J) <= 2, so x_5(J) = 4-k
(Q and P exclude each other since q+q' = 32).
LEMMA 3.1 (one set).
(a) Type G: t <= -1 and Xi(S) <= -3-e(B).
(b) Type Q: t <= -1, Xi(S) <= 2-k-e(B), and if t <= -2 then Xi(S) <= -3-k.
(c) Type P: t <= 0, and if t <= -1 then Xi(S) <= -k-e(B) <= 0.
(d) Type P with t = 0 (case H): nu+k <= 2, at most nu+k <= 2 letters lie outside L(J), and
    Xi(S) <= -5-k+2n(B) <= -1-k.
Proof. (a) (U_5): Theta(J) <= -1-nu <= -1, so t <= -1 (F3f). (F3c): Theta(S) <= -1-nu-5-e(B); add nu+3.
(b) (U_5): Theta(J) <= 4-k-nu. Suppose t >= 0. Then 0 <= Theta(J) gives nu+k <= 4, and l(J) = beta'(J)+beta(J) <= a+k,
so (F3a) gives 10-2a-2k <= Theta(J) <= 4-k-nu, i.e. 6+nu <= 2a+k. As a <= nu: 6 <= a+k <= nu+k <= 4, impossible.
So t <= -1, and (F3c) gives Theta(S) <= 4-k-nu-5-e(B); if t <= -2, (F3d) gives Theta(S) <= 4-k-nu-10. Add nu+3.
(c) (U_5): Theta(J) <= 2-k-nu <= 2 < 5, so t <= 0 (F3f). If t <= -1, (F3c): Theta(S) <= 2-k-nu-5-e(B); add nu+3.
(d) t = 0 gives 0 <= Theta(J) <= 2-k-nu. The letters outside L(J) number alpha(J)+alpha'(J) <= a+q'(J) <= nu+k <= 2.
(F3e): Theta(S) <= 2-k-nu-2e(B) = 2-k-nu-2(5-n(B)); add nu+3. Finally n(B) <= l(B) <= 2 by (F1). []
LEMMA 3.2 (pairs). Let S_1, S_2 be the two alternating sets, with J^i, t_i, B^i, k_i as above.
(a) J^1 and J^2 are not both of type P.
(b) If J^1 is P with t_1 <= -1 and J^2 is Q, then Xi(S_1)+Xi(S_2) <= -8.
(c) If both are Q, then Xi(S_1)+Xi(S_2) <= -1.
(d) If S_1 is in case H, then J^2 is G or Q and Xi(S_1)+Xi(S_2) <= -2.
Proof. (a) (F2) and (D1)(3): 14 <= a' <= alpha'(J^1)+alpha'(J^2) <= q'(J^1)+q'(J^2) <= 4.
(b) By (F2) at most alpha'(J^1)+alpha(J^2) <= k_1+k_2 letters lie outside L(J^1) u L(J^2); the ten runs of B^1 u B^2
have their letters there, so (F1) gives e(B^1)+e(B^2) >= 10-k_1-k_2. Lemma 3.1(c),(b):
Xi(S_1)+Xi(S_2) <= -k_1-e(B^1)+2-k_2-e(B^2) <= -8.
(c) If some t_i <= -2, Lemma 3.1(b) gives Xi(S_i) <= -3-k_i and Xi(S_(3-i)) <= 2-k_(3-i); the sum is <= -1. Otherwise
t_1 = t_2 = -1. Put alpha_i := alpha(J^i), beta_i := beta(J^i), so k_i = alpha_i+beta_i. By (F2) a <= alpha_1+alpha_2,
hence l(J^i) = (a-alpha_i)+beta_i <= alpha_(3-i)+beta_i. (F3b), (F1) and (U_5):
  10-3(alpha_(3-i)+beta_i) <= 10-3n(J^i) <= Theta(J^i) <= 4-alpha_i-beta_i-nu.
Adding the two inequalities: 12+2nu <= 2(alpha_1+alpha_2)+2(beta_1+beta_2) = 2(k_1+k_2). So k_1+k_2 >= 6+nu, and Lemma
3.1(b) gives Xi(S_1)+Xi(S_2) <= 4-k_1-k_2 <= -2-nu <= -2.
(d) Let k := q'(J^1) and lam := l(S_2). By Lemma 3.1(d), lam+l(B^1) <= 2 and Xi(S_1) <= -5-k+2n(B^1), with
n(B^1) <= l(B^1) <= 2-lam. For J^2 (inside S_2), q'(J^2) >= alpha'(J^2) >= a'-lam >= 12 > 2, so J^2 is G or Q. By (F1)
e(B^2) >= 5-lam >= 3+n(B^1). If J^2 is G, Lemma 3.1(a): Xi(S_2) <= -6-n(B^1), and the sum is <= -11-k+n(B^1) <= -9.
If J^2 is Q, Lemma 3.1(b): Xi(S_2) <= 2-k_2-e(B^2) <= -1-k_2-n(B^1), and the sum is <= -6-k-k_2+n(B^1) <= -4. []
PROOF OF WC719 AND THEOREM FC19(a). Fix any frame. If one of J^1, J^2 is of type G, the other set has Xi <= 2 by Lemma
3.1, so the sum is <= -3+2 = -1. Otherwise both types lie in {P, Q}. Two P (including case H) are
excluded by Lemma 3.2(a); P with t <= -1 and Q give <= -8 (Lemma 3.2(b)); H and Q give <= -2 (Lemma 3.2(d)); Q and Q
give <= -1 (Lemma 3.2(c)). Hence Xi(S_ev)+Xi(S_od) <= -1 in every frame (WC719), contradicting (D4). So no admissible
NF of a length-74 avoider over D_38 has terminal k = 20 and kappa_hat = 7. []

## 4. Part (b): the cell (8,19)

Here R = 34, g/2 = 2, Xi(S) = Theta(S)+nu+2, and
  x_5 = max(eps, 8-q, 6-q'),  y_5 = max(eps, 6-q, 8-q'),  x_6 = max(eps, 6-q, 8-q').
For an alternating set S write J5 := J_5(S), J6 := J_6(S) = J5 u {u} (u the sixth run), t5, t6, B5, B6 (five and
four runs). By (F4) the type of J5 is exactly one of G5 (q >= 7, q' >= 5; x_5 <= 1), Q5 (q <= 6; x_5 = 8-q) and P5
(q' <= 4; x_5 = 6-q'), and the type of J6 is exactly one of G6 (q >= 5, q' >= 7; x_6 <= 1), Q6 (q <= 4; x_6 = 6-q)
and P6 (q' <= 6; x_6 = 8-q'). CLASSES of S:
  C1: J5 is G5.   C2: J5 is P5 and t5 <= -1.   C3: J5 is P5 and t5 = 0 (case H5).
  C4: J5 is Q5 and J6 is G6.   C5: J5 is Q5 and J6 is Q6.   C6: J5 is Q5 and J6 is P6 (hybrid).
These are exhaustive once we know that P5 forces t5 <= 0 (Lemma 4.1(b)).
LEMMA 4.1 (one set). Let k denote q'(J5) for P5, q(J6) for Q6.
(a) C1: t5 <= -1 and Xi(S) <= -4-e(B5).
(b) P5: t5 <= 0. C2: Xi(S) <= 1-k-e(B5) <= 1.
(c) C3: nu+k <= 4; l(B5)+l(S') <= alpha(J5)+alpha'(J5) <= nu+k <= 4 (S' the other alternating set); a <= nu <= 4; and
    Xi(S) <= -4-k+2n(B5).
(d) C4: t6 <= -1 and Xi(S) <= -3-e(B6).
(e) If J6 is Q6 (whatever J5 is): t6 <= -1 and Xi(S) <= 2-k-e(B6) <= 2; if t6 <= -2 then Xi(S) <= -2-k; if t6 = -1
    then n(J6) >= 3.
(f) C6: put k5 := q(J5), k6 := q'(J6) (both <= 6). Then beta(u) >= 34-k5-k6 >= 22; a <= k5+k6 <= 12; the number o of
    letters outside L(J6) is at most alpha(J5)+alpha'(J6) <= k5+k6; every run set Q inside S' has q'(Q) >= 16; and if
    t6 <= -1 then Xi(S) <= 4-k6-e(B6).
Proof. (a) (U_5): Theta(J5) <= -1-nu, so t5 <= -1 (F3f); (F3c): Theta(S) <= -1-nu-5-e(B5); add nu+2.
(b) (U_5): Theta(J5) <= 4-k-nu <= 4 < 5, so t5 <= 0. If t5 <= -1, (F3c): Theta(S) <= 4-k-nu-5-e(B5); add nu+2.
(c) t5 = 0 gives 0 <= Theta(J5) <= 4-k-nu. Letters outside L(J5) number alpha(J5)+alpha'(J5) <= a+k <= nu+k <= 4,
and L(B5), L(S') are disjoint sets of such letters. (F3e): Theta(S) <= 4-k-nu-2(5-n(B5)); add nu+2.
(d) (U_6): Theta(J6) <= -1-nu, so t6 <= -1; (F3c): Theta(S) <= -1-nu-4-e(B6); add nu+2.
(e) (U_6): Theta(J6) <= 4-k-nu. Suppose t6 >= 0: then nu+k <= 4, l(J6) <= a+k and (F3a) give
12-2a-2k <= 4-k-nu, so 8+nu <= 2a+k and 8 <= a+k <= nu+k <= 4, impossible. So t6 <= -1, and (F3c), (F3d) give
Theta(S) <= 4-k-nu-4-e(B6), resp. <= 4-k-nu-8 if t6 <= -2; add nu+2. If t6 = -1, (F3b) gives
12-3n(J6) <= 4-k-nu, so 3n(J6) >= 8 and n(J6) >= 3.
(f) k6 = alpha'(J6)+beta'(J6) = (a'-beta(J5)-beta(u)) + (a-alpha(J5)+beta'(u)) >= 34-k5-beta(u), so beta(u) >= 22.
a = beta'(J6)+alpha(J6) <= q'(J6)+alpha(J5) <= k6+k5 <= 12, so a' >= 22. Letters outside L(J6) lie in A \ L(J5) or in
A^c \ L(J6): o <= alpha(J5)+alpha'(J6) <= k5+k6. For Q inside S', L(Q) n A^c lies outside L(J6), so
beta(Q) <= alpha'(J6) <= 6 and q'(Q) >= alpha'(Q) = a'-beta(Q) >= 16. If t6 <= -1: q(J6) >= beta(u) >= 22, so
x_6(J6) = 8-k6 by (F4), (U_6) gives Theta(J6) <= 6-k6-nu, (F3c) gives Theta(S) <= 2-k6-nu-e(B6); add nu+2. []
LEMMA 4.2 (lower window on a negative five-set). Let K be a 5-subset of an alternating set with q'(K) >= 7 and all five
theta_i (i in K) <= -2. If a <= 5, then beta'(K) = |L(K) n A| >= 2.
Proof. Theta(K) <= -10. By (L_5), Theta(K) >= e-2-nu-y_5(K), and y_5(K) <= max(1, 6-q(K)) since 8-q'(K) <= 1. Also
q(K) >= alpha(K) = a-beta'(K), and e-nu >= -a by (D1)(1). Hence
  Theta(K) >= -a-2-max(1, 6-a+beta'(K)) = -2-max(a+1, 6+beta'(K)).
If beta'(K) <= 1 and a <= 5 the right side is >= -9 > -10, a contradiction. []
LEMMA 4.3 (pairs among C1, C2, C4, C5). Let S_1, S_2 be the two alternating sets (data with superscripts 1, 2).
(a) J5^1 and J5^2 are not both P5. In particular C2 and C3 never meet C2 or C3.
(b) If S_1 is C2 and J6^2 is Q6, then Xi(S_1)+Xi(S_2) <= -6.
(c) If J6^1 and J6^2 are both Q6, then Xi(S_1)+Xi(S_2) <= -1.
Proof. (a) (F2): 14 <= a' <= alpha'(J5^1)+alpha'(J5^2) <= q'(J5^1)+q'(J5^2) <= 8.
(b) With k_1 := q'(J5^1), k_2 := q(J6^2): by (F2) at most alpha'(J5^1)+alpha(J6^2) <= k_1+k_2 letters lie outside
L(J5^1) u L(J6^2), and the nine runs of B5^1 u B6^2 have their letters there; so e(B5^1)+e(B6^2) >= 9-k_1-k_2.
Lemma 4.1(b),(e): the sum is <= 1-k_1-e(B5^1)+2-k_2-e(B6^2) <= -6.
(c) Let k_i := q(J6^i) and t^i := t6(S_i), all <= -1 (Lemma 4.1(e)). If t^1, t^2 <= -2: sum <= -4. If t^1 <= -2 and
t^2 = -1 (the symmetric case is the same): sum <= -2-k_1+2-k_2-e(B6^2) = -k_1-k_2-e(B6^2); if this were >= 0, then k_1 = k_2 = 0, i.e. L(J6^1) = A =
L(J6^2); these sets are disjoint, so A is empty and all six runs of J6^2 are empty, whence t^2 is even by (D2), not -1.
If t^1 = t^2 = -1: put alpha_i := alpha(J6^i), beta_i := beta(J6^i); by (F2) l(J6^i) <= alpha_(3-i)+beta_i, and (F3b),
(F1), (U_6) give 12-3(alpha_(3-i)+beta_i) <= 4-alpha_i-beta_i-nu. Adding: 16+2nu <= 2(k_1+k_2), so k_1+k_2 >= 8+nu and
the sum is <= 4-k_1-k_2 <= -4-nu. []
LEMMA 4.4 (case H5). If S_1 is C3, then Xi(S_1)+Xi(S_2) <= -2.
Proof. Let k := q'(J5^1), m := n(B5^1), lam := l(S_2). Lemma 4.1(c): m+lam <= l(B5^1)+lam <= 4, a <= 4 and
Xi(S_1) <= -4-k+2m. For Q inside S_2, q'(Q) >= alpha'(Q) >= a'-lam >= 10; so J5^2 is not P5 and J6^2 not P6, i.e.
S_2 is C1, C4 or C5.
C1: e(B5^2) >= 5-lam, Xi(S_2) <= -9+lam, sum <= -13+2m+lam <= -13+m+4 <= -5.
C4: e(B6^2) >= 4-lam, Xi(S_2) <= -7+lam, sum <= -11+2m+lam <= -3.
C5, t6(S_2) = -1: n(J6^2) >= 3 (Lemma 4.1(e)), so lam >= 3+n(B6^2); then m <= 1 and n(B6^2) <= 1, e(B6^2) >= 3,
  Xi(S_2) <= -1-q(J6^2) <= -1, Xi(S_1) <= -2, sum <= -3.
C5, t6(S_2) <= -2: the five runs of B5(S_2) all have theta <= t6(S_2) <= -2 and q'(B5(S_2)) >= 10; as a <= 4, Lemma
  4.2 gives lam >= beta'(B5(S_2)) >= 2, so m <= 2, Xi(S_1) <= 0 and Xi(S_2) <= -2 (Lemma 4.1(e)); sum <= -2. []
LEMMA 4.5 (hybrid with t6 <= -1). If S is C6 with t6(S) <= -1 and S' is the other set, Xi(S)+Xi(S') <= -1.
Proof. By Lemma 4.1(f) every run set inside S' has q' >= 16, so S' is not C2, C3 or C6: it is C1, C4 or C5. Letters
of B6 u S' lie outside L(J6), and Xi(S) <= 4-k6-e(B6).
C1: the nine runs of B6 u B5(S') give e(B6)+e(B5(S')) >= 9-o >= 9-k5-k6; sum <= 4-k6-e(B6)-4-e(B5(S')) <= k5-9 <= -3.
C4: e(B6)+e(B6(S')) >= 8-k5-k6; sum <= 4-k6-3-(8-k5-k6) = k5-7 <= -1.
C5: with k' := q(J6(S')), (F2) bounds the letters outside L(J6) u L(J6(S')) by alpha'(J6)+alpha(J6(S')) <= k6+k',
  so e(B6)+e(B6(S')) >= 8-k6-k'; sum <= 4-k6+2-k'-(8-k6-k') = -2. []
LEMMA 4.6 (hybrid with t6 >= 0). If S is C6 with t6(S) >= 0 and S' is the other set, Xi(S)+Xi(S') <= -8.
Proof. All six runs of J6 = J5 u {u} have theta >= 0; u is nonempty (Lemma 4.1(f)).
Step 1. As t5 >= 0 and J5 is Q5, (U_5) gives 0 <= Theta(J5) <= 6-k5-nu, and (F3a) with l(J5) = a-alpha(J5)+beta(J5)
gives 10-2a+2alpha(J5)-2beta(J5) <= 6-alpha(J5)-beta(J5)-nu, i.e. 4+nu+3alpha(J5) <= 2a+beta(J5). With
beta(J5) <= 6-nu-alpha(J5): nu+2alpha(J5) <= a+1. As nu >= a, alpha(J5) = 0 and nu <= a+1; by (D1)(2) nu = a. So
A lies inside L(J5), every letter outside L(J6) is in A^c, o = alpha'(J6), beta'(u) = 0, k6 = o+a, and
beta(J5) >= 4-a.
Step 2. For v in J5 let Q_v := (J5 \ {v}) u {u}, a 5-subset of S whose runs all have theta >= 0, so
Theta(Q_v) >= 2e(J5 \ {v}) >= 0. Here q(Q_v) >= beta(u) >= 22 and
q'(Q_v) = alpha'(Q_v)+beta'(Q_v) = (o+beta(v))+(a-beta'(v)). By (U_5), 0 <= Theta(Q_v) <= -2-nu+max(eps, 6-q'(Q_v));
since -2-nu+eps < 0 the maximum is 6-q'(Q_v), and
  (*) o+2a+beta(v)-beta'(v)+2e(J5 \ {v}) <= 4   for every v in J5.
Step 3. Sum (*) over the five runs v of J5. The beta(v) sum to beta(J5) >= 4-a, the beta'(v) to a (A inside L(J5)),
and each empty run of J5 lies in four of the sets J5 \ {v}. So 5o+10a+(4-a)-a+8e(J5) <= 20, i.e.
5o+8a+8e(J5) <= 16. Hence a <= 2 and o+a <= 3 (a = 0: o <= 3; a = 1: o <= 1; a = 2: o = 0).
Step 4. S' has no letter of A, so for Q inside S': alpha(Q) = a, beta'(Q) = 0, q(Q) = a+l(Q), and l(S') <= o.
J6(S') has q(J6(S')) = a+l(J6(S')) <= a+o <= 3, so J6(S') is Q6 and t6(S') <= -1 (Lemma 4.1(e)). If t6(S') <= -2,
the five runs of B5(S') have theta <= -2, q'(B5(S')) >= 16 and beta'(B5(S')) = 0 with a <= 2: impossible by Lemma
4.2. So t6(S') = -1 and n(J6(S')) >= 3 (Lemma 4.1(e)): o >= l(S') >= 3, hence a = 0, o = 3 = l(S'), all letters of
S' lie in J6(S') (so e(B6(S')) = 4 and q(J6(S')) = 3), and L(B6) is empty (so e(B6) = 4).
Step 5. x_6(J6) = 8-k6 = 5 (q(J6) >= 22), so (U_6) gives Theta(J6) <= 3 < 6 and t6 <= 0, i.e. t6 = 0. (F3e):
Theta(S) <= 3-8 = -5 and Xi(S) <= -3. Lemma 4.1(e): Xi(S') <= 2-3-4 = -5. The sum is <= -8. []
PROOF OF WC819 AND THEOREM FC19(b). Fix any frame. If S_1 or S_2 is C3, the sum is <= -2 (Lemma 4.4; two C3 sets are
excluded by Lemma 4.3(a)). Otherwise, if one of them is C6, the sum is <= -1 by Lemmas 4.5 and 4.6. Otherwise both lie
in C1, C2, C4, C5, with Xi <= -4, 1, -3, 2 respectively (Lemma 4.1). If one is C1 or C4, the sum is <= -3+2 = -1.
Otherwise both are C2 or C5: C2 with C2 is excluded (Lemma 4.3(a)), C2 with C5 gives <= -6 (Lemma 4.3(b)) and C5
with C5 gives <= -1 (Lemma 4.3(c)). Hence Xi(S_ev)+Xi(S_od) <= -1 in every frame (WC819), contradicting (D4). So no
admissible NF of a length-74 avoider over D_38 has terminal k = 20 and kappa_hat = 8. []

## 5. Scope, route remark and literal interface table

Claimed: Theorem FC19(a) and FC19(b) as stated in Sec. 0, each for its own cell, relative to the accepted UMR scope.
The new counts WC719 and WC819 are proved by hand from (D1)-(D3); their availability for the NF word, and the identity
(D4), are the accepted UMR premises listed below. NOT claimed: any other cell, kappa, prime or terminal k; the full
p = 19 union beyond these two kappa values; full ordered Olson; INV*, reflection rigidity or o_F assembly; UMR's
Lemma FC outside these two cells; any UB, RES or Lemma 20 statement; priority, novelty, Lean, human-referee or
runtime verification. This worker runs no review; the parent controls review, acceptance and any composed claim.
Route remark. The authority's untrusted parent hint (the real balancing level lies between integer levels) was not
checked before the freeze. From the constants of Sec. 1 the real solution of ell_m = M_m is m = 5.5 at both cells;
level 5 alone suffices at (7,19), and at (8,19) level 5 handles near-A^c top sets and level 6 near-A top sets, with
the hybrid class C6 joining them. The hint is not a premise of any step.

| Input | Absolute path | Whole-file SHA256 | LF lines | Scope and use |
|---|---|---|---|---|
| Authority | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-olson-fc-p19-cells-transition-v1.json | 9c04963a8d484c774812fe549a8552004bdf2a0bce57e584c80b627de708e094 | 1-49 | Both p=19 k=20 cells; separate outcomes; premises; rules |
| Frozen scope | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-p19-cells/FC19-scope-v1.md | 889acf673aed2005ee3ab412d5d82050c7026d053e54844574a000619eee3c05 | 1-78 | Frozen before new derivation; prior-exposure disclosure |
| UMR verdict (accepted scope) | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-verdict-v1.md | a2535971cb214e399433235a4b9fca2de7328d15bec2c2f4eece35c05456c772 | 1-38 | UMR-F, Lemmas 0-13, Lemma 14 identity at literal scope; FC open; frames quantified |
| UMR proof | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-middle-range/proof-UMR-v1.md | c403bfbae9f1c7b75698010cae78515a253154e689336e79006c588ff15023a9 | used 18-28, 55-56, 64-66, 88-118, 137-139, 161-165, 201-209, 238-247, 252-258; check 344-355 | (D1)-(D4) only; no UB, RES, Lemma 15-20 or FC use |
| UMR parent erratum v1 | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-erratum-v1.md | b83313b3fe828ee19a0902e9a5149db42ee55318500f92bac577b4bbd7088c5f | 1-10 | Lemma 13 link restricted to g/2<=m<=kappa (U' = Theta unchanged); saturation gloss withdrawn |
| UMR parent erratum v2 | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-erratum-v2.md | 2a5f142ef136b04c15304137a4ba19946d0fee115ce18e8660817cd25bc902a2 | 1-9 | Residual wording only; no saturation, characterisation or necessary obstruction used |
| FC717 (not accepted) | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-fc-cell-7-17/proof-FC717-v1.md | e2c74806fc5f1986b298d490b121676eff7dce5f90f014311d3d8c099800b945 | read 1-113 | Method inspiration only; no lemma, constant or statement used |
| Frontier context | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FQW-parent-verdict-v1.md | a9388a49e227b3bf418e2250b515860a33f880dba816b5318a834faa5da9e566 | 9 | Context only; not a premise |

Primitive inputs (NF, GRX, SC0, ZSTRUCT/FB, (S1), LOWER and FCW errata) enter only through accepted UMR, at the scopes
of UMR's interface table (UMR LF393-399) as governed by the UMR verdict LF24.
Machine steps for this file: /bin/date, shasum -a 256, wc -c -l, reading files, and one exclusive creation (Python
open(path,'x')) of this text, drafted by hand in memory in four parts; pre-creation wording replacements are disclosed
in the checkpoints; no assertion of any kind and no computation over mathematical objects.
