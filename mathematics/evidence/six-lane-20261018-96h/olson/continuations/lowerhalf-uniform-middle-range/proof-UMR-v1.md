# UMR: uniform middle range, terminal k = p+1, kappa_hat = kappa: uniform lift framework, partial final count, v1

Owner OlsonThirdCutWindow (same math2 slot). Drafted by hand after /bin/date 2026-10-20T08:25:54-0700. Status:
CANDIDATE_UNVERIFIED written mathematics for the frozen target (UMR-scope-v1.md SHA256
2d0ef2fc8e7a5a94892a6b50a03ae55840931a36d5273734bce95e027728c4da, frozen 2026-10-20T07:29:56-0700 before any derivation
and before the parent route note was read; authority RUN/control/written-olson-uniform-middle-transition-v1.json SHA256
459233f3ac03cac347540d9c173d54810d9f464aab20e2a909c19d9df4447e59).
OUTCOME: the ENTIRE range is NOT proved. The EXACT FIRST FAILING UNIFORM LEMMA is Lemma FC (the final count, Sec. 5):
it is proved outside an explicitly described residual class (Theorem UMR-P) and is open on that class. Everything
before it (Secs. 1-4: windows, frame, a uniform two-sided realisation lemma, representatives, a lift framework on ALL
central levels with pair-independent theta, complements, an additive triple, connectivity, and the final-count
reductions) is proved uniformly for every target (kappa,p). The cells (7,17), (7,19), (8,19) are OPEN at Lemma FC
(Sec. 6). All case work is by hand; no script, assertion, enumeration or computation over scientific data. No novelty,
priority, Lean or human-review claim; no other k; no full ordered Olson.

## 0. Statements

Target range T: p >= 17 prime and kappa an integer with floor((p+7)/4) < kappa <= (p-3)/2. Throughout,
N := p+1, R := p-1+2kappa, g := 2p-R = p+1-2kappa, delta := 4kappa-p-1 = 2kappa-g, h := N/2 = kappa+g/2.
An "avoider" is a word of length 4p-2 over D_(2p) without an identity 2p-subword in increasing original index order;
"NF" is an admissible normal form (full existential antecedent: SOME admissible NF, the H extra reflection pairs anywhere
in the odd blocks, every empty NF run separating different reflection values; no o_F, nonempty-run, rotation-pair or
rigidity hypothesis).
THEOREM UMR-F (uniform framework; proved). Let (kappa,p) be in T and let u be the NF word (terminal k = p+1,
kappa_hat = kappa) of an avoider, with a frame as in Sec. 1. Call m a central level if g/2 <= m <= kappa+1. Then there
are integers theta_i (one per run) such that U'(P) = Theta(P) := sum_(i in P) theta_i for every set P of runs with
central m(P), where U'(P) is the representative of Sec. 2; every empty run has a nonzero even theta; and
Theta(all runs) = B* - 2nu0 - 2p.
THEOREM UMR-P (partial exclusion; proved). Let (kappa,p) be in T. No avoider has an NF with terminal k = p+1 and
kappa_hat = kappa for which some frame satisfies UB(S_ev) and UB(S_od) (Sec. 4, Definition UB). The frames failing this
form the residual class RES of Sec. 5, described by Lemma 20.
LEMMA FC (first failing uniform lemma; NOT proved). For every frame of every such NF word, Xi(S_ev)+Xi(S_od) <= -1
(notation of Sec. 4). FC would prove the whole target (Lemma 14). FC is proved in Theorem UMR-P outside RES; on RES it
is open, and no uniform argument is given there.
Cells. (7,17), (7,19), (8,19): all of Secs. 1-4 hold with the instantiated constants of Sec. 6; each cell is OPEN at
Lemma FC (its residual class RES is not excluded).
Exposure. Before the freeze I had derived TCW (delta = 4, now parent-accepted), P7L (parent-accepted) and FQW (delta = 6,
not accepted) and read FCW, SCW and their inputs. The parent route note (read after the freeze) proposed the unit
reservoir, two-sided offsets x, y, central levels and coupled additivity; each is re-derived below; Sec. 7 compares.
No TCW, P7L, FQW, FCW, SCW or USK lemma is a premise.

## 1. Setting, windows, frame and label counts

LEMMA 0 (range). For (kappa,p) in T: g and delta are even, g >= 4, delta >= 8, kappa >= 7, delta+2 <= 2kappa-2,
R = 4kappa+g-2, 2p = 4kappa+2g-2, N = 2kappa+g, and kappa+1 <= h-1.
Proof. p is odd, so g = p+1-2kappa and delta = 4kappa-(p+1) are even. kappa <= (p-3)/2 gives g >= 4.
floor((p+7)/4) >= (p+4)/4, so kappa >= (p+8)/4, delta >= 7, hence delta >= 8; and kappa >= 25/4. delta+2 = 2kappa-g+2
<= 2kappa-2. The identities are direct (p = 2kappa+g-1); h-1 = kappa+g/2-1 >= kappa+1. []
Word form [NF lines 28-43; GRX]. The NF word u is an avoider of length 4p-2 with the rotation multiset of w. Read it
cyclically as R_0 S_0 ... R_p S_p: N runs R_i (r_i >= 0 letters) and blocks S_i = sigma_(y_i)^(l_i), l_i odd,
sum (l_i-1)/2 = H = p-1-kappa (NF line 42), an EMPTY run R_i having y_(i-1) != y_i (indices mod N); F = N+2H.
tau_i := y_i - y_(i-1) in Z_p (sum 0). m(P) := half the number of sign transitions of (-1 on P, +1 off P) (LOWER parent
erratum): m(empty) = m(all runs) = 0, a proper nonempty P has m(P) = its number of maximal cyclic intervals, and
m(P^c) = m(P). T(P) := sum_(i in P) tau_i; X^(P) := letter values with every letter of a run of P negated; L(P) := the set
of letters in runs of P; L_i := L({i}). Independent = pairwise non-adjacent mod N; a proper independent set of j >= 1 runs
has m = j.
LEMMA 1 ((SR)) [NF, GRX if-direction; derivation of FCW parent erratum m4]. For every P and every even n with
max(0,2kappa+2-2m(P)) <= n <= min(R,2p-2m(P)), T(P) is not a sum in Z_p of n letters (distinct occurrences) of X^(P).
Write Win_m for this set of n.
Proof. GRX applies to the NF representation with z_i = -1 iff i in P; its theta_i = y_(i-1)-y_i = -tau_i, so
T(z) = sum_(i not in P) theta_i = T(P). Phi = 2m(P); all l_i are odd, so delta_GRX = N-2m(P) and C_max = F-delta_GRX =
2H+2m(P). GRX: an even C with 2m(P) <= C <= 2H+2m(P), 0 <= 2p-C <= R and T(P) in Sigma_(2p-C)(X^(P)) gives an identity
2p-subword. With n := 2p-C this is the displayed range (2p-2H = 2kappa+2). u is an avoider. []
LEMMA 2 (windows). Win_m = [ell_m, R-M_m] (even integers) with ell_m := max(0,2kappa+2-2m) and M_m := max(0,2m-g).
Win_0 = [2kappa+2,R], Win_1 = [2kappa,R]. For a central level m: ell_m = 2kappa+2-2m, M_m = 2m-g, ell_m+M_m = delta+2,
and 0 <= ell_m, M_m <= delta+2 <= 2kappa-2.
Proof. min(R,2p-2m) = R - max(0,R-2p+2m) = R - M_m. For m = 0, 1 use 2kappa+2 <= R and R <= 2p-2 (g >= 2). For
g/2 <= m <= kappa+1 both maxima are attained by the second entries, and their sum is 2kappa+2-g = delta+2. []

LEMMA 3 (frame).
(a) [pigeonhole] The N block values lie in Z_p, so y_c = y_c' for some c != c'. P0 := runs c+1,...,c' is a proper
 nonempty arc with T(P0) = 0; its complementary arc C0 has T(C0) = 0.
(b) [direct] Let Y be the sequence of the R elements (1,x) of C_(2p) = Z_2 x Z_p, one per letter x of X^(P0). A zero-sum
 of Y of length n is a set of n letters with X^(P0)-sum 0 = T(P0) (n even, n <= R); Lemma 1 at P0 (m = 1) excludes
 n in [2kappa,R]. So every zero-sum of Y has length <= 2kappa-2.
(c) [SC0 through Y'z] Let Z be a LONGEST zero-sum of Y, |Z| = 2t, 0 <= t <= kappa-1; Y' := Y - Z is zero-sum free (a
 nonempty zero-sum of Y' with Z would be longer) of length L = R-2t >= R-2kappa+2 = p+1. z := -sigma(Y') != 0 and Y'z is
 a minimal zero-sum sequence (a nonempty proper zero-sum T of Y'z gives the nonempty zero-sum T, if z not in T, or
 Y'z-T, if z in T, inside Y'). Its length is >= p+2 = floor(2p/2)+2 and 2p >= 3, so by SC0 it has a 1-element basis
 {g0}: each term is x*g0 with least positive x, the coefficients summing to ord(g0) >= L+1 >= p+2; so ord(g0) = 2p.
 Hence Y' = (a_1 g0)...(a_L g0), W := sum a_i = 2p - x(z) <= 2p-1. Write g0 = (g_1,gamma), g_1 in Z_2: every term of Y'
 is odd, so a_i g_1 = 1 (mod 2), g_1 = 1 and every a_i is odd; gamma != 0 since g0 generates.
(d) [ZSTRUCT, FB in (S')] If t = 0 put n+ = n- = 0. If t >= 1, Y lies in (S') with (k',kappa') = (p-1,kappa-1): p >= 5
 prime, 1 <= k' <= p-1, kappa' integer with 1 <= kappa' < p, |Y| = 2p+2kappa'-k' = R odd elements, every zero-sum of
 length <= 2kappa' ((b), i.e. (S1) at kappa'), Z longest with t <= kappa', L >= 2p-k' = p+1, g0 an index-<1 generator of
 Y-Z. ZSTRUCT gives Z = g0^(n+)(-s_1 g0)...(-s_(n-) g0), s_j odd, 1 <= s_j <= 2t-1, n+ + n- = 2t, n- >= 1; FB gives
 sum s_j = n+ and W+n+ <= 2p-1. So n- <= n+, n- <= t <= kappa-1, n+ >= t, s_j <= n+-(n- - 1).
(e) [labels] Each letter l gets an odd label b_l with X^(P0)-value b_l*gamma: the a_i for Y', +1 (n+ times) and -s_j for
 Z. E := W-L = sum (a_i-1) >= 0 is even; m1 := #{i : a_i = 1}; u1 := #{l : |b_l| = 1} >= m1+n+; bmax := max |b_l|.
LEMMA 4 (label counts). (i) E <= g-1+n- <= g+kappa-2. (ii) Every a_i <= 1+E <= p-kappa and every s_j <= 2kappa-3, so
bmax <= p-6. (iii) m1+n+ >= R-n- -E/2 >= (5kappa+g)/2. (iv) [reservoir] u1 >= |b_l|+2kappa-1 for every letter l.
Proof. (i) L = R-n+-n- and W <= 2p-1-n+ give E <= 2p-1-R+n- = g-1+n-. (ii) a_i-1 <= E and g+kappa-1 = p-kappa;
s_j <= 2t-1 <= 2kappa-3; p-kappa <= p-7 and 2kappa-3 <= p-6. (iii) Each a_i > 1 is odd, so it adds >= 2 to E: L-m1 <= E/2.
So m1+n+ >= L+n+-E/2 = R-n- -E/2 >= R-(kappa-1)-(g+kappa-2)/2 = (5kappa+g)/2.
(iv) |b_l| = 1: u1 >= (5kappa+g)/2 >= 2kappa. b_l = a_i = b >= 3: the other L-m1-1 labels > 1 add >= 2 each to
E-(b-1), so m1 >= L-1-(E-b+1)/2 and u1-b >= L+n+-1-(E+b+1)/2 >= L+n+-E-2 (b <= E+1) = R-n- -E-2 >= R-g-1-2n-
>= R-g-2kappa+1 = 2kappa-1. b_l = -s_j: u1-s_j >= m1+n+-s_j >= m1+n- -1 >= R-n+-E/2-1; with n+ = 2t-n-,
E <= g-1+n-, t <= kappa-1 and n- >= 1: n+ + E/2 <= 2t - n-/2 + (g-1)/2 <= 2kappa-3+g/2, so u1-s_j >= 2kappa+g/2. []
Normalisation. (v,eps) -> (gamma^(-1)v,eps) is an automorphism of D_(2p); letterwise it preserves identity subwords,
the run/block structure with the empty-run rule and Lemma 1 (tau and values scaled), and carries the frame with the same
labels. Take gamma = 1; put c_l := b_l on C0 and c_l := -b_l on P0. The original value of l is c_l (mod p); its value in
X^(P) is eps_l c_l, eps_l = -1 iff l lies in a run of P.
Light side. o(Q) := #{l in L(Q) : b_l = 1}. If o(C0), o(P0) >= kappa+1, then kappa+1 letters of each (original values +1,
-1) have sum 0 = T(empty) with 2kappa+2 in Win_0: impossible by Lemma 1. Exchanging P0 and C0 keeps Lemmas 3-4 with the
same labels (C0 is a proper arc with T(C0) = 0, X^(C0) = -X^(P0), its sequence is -Y, zero-sums and Z are unchanged, -g0
is an index-<1 generator of -Y' with the same coefficients). Fix P0 with q1 := o(P0) <= kappa and normalise.
Quantities. A := {l : c_l < 0}, A^c := {l : c_l > 0}, a := |A|, a' := |A^c| = R-a. Pi0 := sum over A^c of |c_l|,
nu0 := sum over A of |c_l|, B* := Pi0+nu0 = sum |b_l| = W+2n+ = R+E+n+-n-, e* := B*-R = sum_l (|c_l|-1) >= 0; B* is
even (R odd terms, R even). sigma(P) := sum of c_l over L(P); X_i := sum of the original values of run i;
sigma_i := sigma({i}) = X_i (mod p); hh_i := tau_i+X_i; Hh(P) := sum_(i in P) hh_i = T(P)+sigma(P) (mod p).
Frame quantifier. Lemmas 3-4 and the light side hold for EVERY admissible choice of P0, Z, g0 and light side; the proof
fixes one frame, and one always exists.
LEMMA 5 (density, signed sums, negative letters). (a) Every integer of [0,B*] is a sum of a sub-multiset of {|c_l|}.
(b) For a set P of runs let Pos(P), Neg(P) be the letters with eps_l c_l > 0, < 0; q(P) := |Neg(P)|,
q'(P) := |Pos(P)| = R-q(P), Pi(P) := sum over Pos(P) of |c|, nu(P) := sum over Neg(P) of |c|. The signed sums over sets J
of letters are exactly the integers of [-nu(P),Pi(P)], each of the parity of |J|; Pi(P) = Pi0-sigma(P),
nu(P) = nu0+sigma(P), nu(P) = q(P) (mod 2). (c) Neg(P) = L(P) symdiff A, so q(P) = |A \ L(P)|+|L(P) n A^c|,
q'(P) = |A^c \ L(P)|+|L(P) n A|, and q(P^c) = q'(P). (d) a' >= (3kappa+g)/2 = (p+kappa+1)/2 and nu0 >= a, Pi0 >= a'.
Proof. (a) u1 ones and every element <= u1+1 (Lemma 4(iv)); prefix sums of the elements > 1 in increasing order, each
extended by 0..u1 ones, cover [0,B*]. (b) J -> (J n Pos(P)) u (Neg(P)\J) is a bijection with signed sum = (sum of |c| over
the image) - nu(P); terms are odd. (c) A letter of a run of P has value -c_l. (d) By Lemma 4(iii), at least
(5kappa+g)/2 letters have b = 1; at most q1 <= kappa of them lie in P0; the others have c = +1. []
LEMMA 6 (lift margin). M0 := 2Pi0+nu0-2p satisfies (i) M0 >= 2kappa-1+E/2; (ii) M0 >= 4kappa-2+e*-a;
(iii) M0 >= a'-g+e*.
Proof. (i) A letter with c < 0 is one of the q1 <= kappa letters of P0 with b = 1, a letter of P0 with an a-label B >= 3
(B <= (3/2)(B-1), the B-1 summing to <= E), or a letter of C0 with label -s_j (these sum to <= n+). So
nu0 <= q1+3E/2+n+ and M0 = 2B*-nu0-2p >= (2R-2p)+E/2+n+-2n- -q1 >= 4kappa-2+E/2-n- -kappa >= 2kappa-1+E/2.
(ii), (iii) Write nu0 = a+e_A and Pi0 = a'+e_(A^c) with e_A+e_(A^c) = e*. Then M0 = 2a'+a-2p+2e_(A^c)+e_A
>= 2R-2p-a+e* = 4kappa-2+e*-a, and also >= a'+R-2p+e* = a'-g+e*. []

## 2. Two-sided realisation and representatives at central levels [NEW, uniform]

Fix a central level m, put ell := ell_m, M := M_m, and let P be a set of runs (only m(P) = m is used later). An even v
is REALISED if v = sum_(l in J) eps_l c_l for a set J of letters with ell <= |J| <= R-M; a "representation" of v is any
such J without the size condition. For v even in [-nu(P),Pi(P)] put sigma_v := v+nu(P) in [0,B*] (sigma_v = q (mod 2)).
Units: U+ and U- are the letters of value +1 and -1 in X^(P).
LEMMA 7 (realisation). Let q := q(P), q' := q'(P), eps := q mod 2 and
  x(P) := max(eps, ell-q, M-q'),   y(P) := max(eps, M-q, ell-q').
Every even v in [-nu(P),Pi(P)] with x(P) <= sigma_v <= B*-y(P) is realised. Moreover x(P)+y(P) <= ell+M = delta+2.
Proof. Two numerical facts are used: (C1) u1 >= bmax+max(ell,M)+1 (Lemma 4(iv), max(ell,M) <= 2kappa-2);
(C2) R-M-ell = R-delta-2 = p+g-3 >= bmax+1 (Lemma 4(ii)). Let v be as stated and suppose v is not realised; v has a
representation (Lemma 5(b)) and all representations have even size.
Case U: every representation has size > R-M. Take J of minimum size; its exterior X has <= M-2 letters, so J contains
 >= u1-M+2 >= bmax+3 units. Units of both signs in J would give a removable zero-signed pair. Say J's units are +1 (the
 case -1 is the negative). A letter of J of value -b (b >= 3) together with b units of J is removable. So J lies in
 Pos(P). A letter of Pos(P)\J with |c| = b >= 3 could replace b units of J, lowering the size. So Neg(P) and k' units of
 Pos(P) form X: q+k' <= M-2 and v = Pi(P)-k', i.e. sigma_v = B*-k' > B*-(M-q). In the negative case
 sigma_v = k' < M-q'.
Case L: some representation has size <= R-M, hence < ell. Take J of maximum size among those; |J| <= ell-2, and X has
 >= u1-ell+2 >= bmax+3 units. A move that keeps the signed sum and raises the size by at most bmax+1 gives a
 representation of size <= ell-2+bmax+1 <= R-M by (C2): it would be realised (size >= ell) or contradict maximality
 (size < ell); so no such move exists. First, X's units have one value (else add a pair {+1,-1} of them); say +1 (the
 case -1 is the negative). Then X has no negative letter (a letter of value -b, b >= 3, could be added with b units of
 X), and J n Pos(P) consists of units (a letter of J of value +b, b >= 3, could be replaced by b units of X). So
 J = Neg(P) u {k' units}, v = -nu(P)+k', q+k' <= ell-2, i.e. sigma_v = k' < ell-q. In the negative case
 sigma_v = B*-k' > B*-(ell-q').
In all cases sigma_v < max(ell-q, M-q') <= x(P) or sigma_v > B*-max(M-q, ell-q') >= B*-y(P): a contradiction.
For the last claim: x and y are each one of eps, ell-q, M-q' resp. eps, M-q, ell-q'; the nine sums are bounded by
ell+M (using q, q' >= 0, q+q' = R >= ell+M, and eps <= q, eps <= q' when the other entry is chosen: eps = 0 if q = 0,
eps <= 1 <= q otherwise), and 2 <= delta+2. []
LEMMA 8 (representatives). Let m(P) = m be central and x := x(P), y := y(P). Then B* <= 2p-4+x+y, and there is a
unique integer U(P) with U(P) = Hh(P) (mod p), U(P) = sigma(P) (mod 2) in
  [Pi0+1-lambda(P), 2p-1-nu0+mu(P)],   lambda(P) := y-1, mu(P) := x-1,
an interval of length 2p-4-B*+x+y <= 2kappa-2 < 2p. Put U'(P) := U(P)-2p, low(P) := Pi0+1-lambda(P)-2p,
up(P) := -1-nu0+mu(P) = -2-nu0+x. Also (x,y)(P^c) = (y,x)(P).
Proof. By Lemma 1, T(P) != v (mod p) for every realised v. Hh(P) = T(P)+sigma(P) (mod p), and v+sigma(P) = sigma_v-nu0
(Lemma 5(b)). By Lemma 7 the excluded integers v+sigma(P) include every integer of the parity of sigma(P) in
[-nu0+x, Pi0-y] (an interval with ends of that parity, nonempty since x+y <= delta+2 < R <= B*). The p integers
a0, a0+2, ..., a0+2p-2 (a0 := -nu0+x) are pairwise incongruent mod p, so Hh(P) is congruent to exactly one of them,
a0+2j > Pi0-y; hence Pi0-y <= a0+2p-4, i.e. B* <= 2p-4+x+y, and a0+2j lies in [Pi0-y+2, a0+2p-2], the displayed interval.
Its length is <= 2p-4-R+ell+M = g-4+delta+2 = 2kappa-2. Residues mod p and mod 2 fix the residue mod 2p (p odd).
Finally q(P^c) = q'(P) and m(P^c) = m(P). []
Write D0 := 2p-2-B* <= 2p-2-R = g-2.

## 3. The lift framework on all central levels [NEW, uniform]

Cl := {P : m(P) central}; P in Cl implies P^c in Cl. A PAIR is (P, P u {i}) with i not in P and P, P u {i} in Cl;
its difference is d := U'(P u {i}) - U'(P). Since adding a run changes m by at most 1, every pair lies in a BLOCK
{m, m+1} of two consecutive central levels (both levels of the pair in the block; a pair at (kappa+1,kappa+1) lies in
{kappa, kappa+1}). For a run i put alpha := |L_i n A|, beta := |L_i n A^c|, r := alpha+beta = r_i.
LEMMA 9 (one block). Two pairs pi, rho for the same run i in the same block {m,m+1} have equal differences.
Proof. For pi = (P, P u {i}) put s := q(P) and s~ := q(P u {i}). As L_i and L(P) are disjoint, Lemma 5(c) gives
s~ = s-alpha+beta, s >= alpha, R-s >= beta, s~ >= beta, R-s~ >= alpha. By Lemma 8, d_pi = hh_i (mod p),
d_pi = sigma_i (mod 2) and -(D0+X_pi) <= d_pi <= D0+Y_pi with X_pi := lambda(P u {i})+mu(P) = y(P u {i})+x(P)-2 and
Y_pi := x(P u {i})+y(P)-2. Let l* := ell_m >= every ell in the block, M* := M_(m+1) >= every M in the block;
l*+M* = delta+4 =: D4 and l*, M* <= delta+2. Expanding the two maxima of Lemma 7 (nine sums each) and using the
displayed inequalities and s-s~ = alpha-beta =: w:
  X_pi+2 <= max(x1..x6): x1 = 2, x2 = 1+l*-alpha, x3 = 1+M*-beta, x4 = D4-r, x5 = 2M*-R+w, x6 = 2l*-R-w;
  Y_pi+2 <= max(y1..y6): y1 = 2, y2 = 1+M*-alpha, y3 = 1+l*-beta, y4 = D4-r, y5 = 2l*-R+w, y6 = 2M*-R-w.
Here X_pi+2 = y(P u {i})+x(P) with y(P u {i}) in {eps', M2-s~, l2-R+s~} and x(P) in {eps, l1-s, M1-R+s} (l1, M1 and l2,
M2 the ell, M of the levels of P and P u {i}): eps'+eps <= x1; eps'+(l1-s), (l2-R+s~)+eps <= x2; eps'+(M1-R+s),
(M2-s~)+eps <= x3; (M2-s~)+(l1-s), (l2-R+s~)+(M1-R+s) <= x4; (M2-s~)+(M1-R+s) = M1+M2-R+w <= x5;
(l2-R+s~)+(l1-s) = l1+l2-R-w <= x6. Likewise Y_pi+2 = x(P u {i})+y(P) with x(P u {i}) in {eps', l2-s~, M2-R+s~} and
y(P) in {eps, M1-s, l1-R+s}, giving y1..y6. Every sum x_k+y_l is <= 2D4: x1..x4 and y1..y4 are <= D4;
x5+y5 = 2D4-2R+2w and x6+y6 = 2D4-2R-2w are <= 2D4 (|w| <= R); x5+y6 = 4M*-2R and x6+y5 = 4l*-2R are negative
(4(delta+2) < 2R); x5+y2 = 1+3M*-R-beta, x6+y3 = 1+3l*-R-alpha, y5+x2 = 1+3l*-R-beta, y6+x3 = 1+3M*-R-alpha are
<= 1+3(delta+2)-R < D4; x5+y3, y6+x2 are <= 1+2M*+l* and x6+y2, y5+x3 are <= 1+2l*+M*, all <= 1+D4+(delta+2) = 2D4-1;
x5+y4, x6+y4, y5+x4, y6+x4 are <= D4+2(delta+2)-R <= D4; and x5+2, x6+2, y5+2, y6+2 are <= 2(delta+2)+2. Hence
(X_pi+2)+(Y_rho+2) <= 2D4 = 2delta+8 for any two pairs pi, rho of the block, and
|d_pi-d_rho| <= 2D0+2delta+4 <= 2(g-2)+2delta+4 = 4kappa < 2p. As d_pi = d_rho (mod 2p), d_pi = d_rho. []
LEMMA 10 (theta; empty runs). For every run i there is one integer theta_i such that EVERY pair for i has difference
theta_i (theta only through explicit pairs, LOWER parent erratum). theta_i = hh_i (mod p), theta_i = sigma_i (mod 2),
|theta_i| < 2p. If run e is empty, theta_e is a NONZERO EVEN integer.
Proof. For each central m there is a pair rho_m = (P, P u {i}) at levels (m,m): P := {i+1} u V with V an independent
set of m-1 runs inside the arc i+3, ..., i-3 (N-5 >= 2m-3 runs, as m <= (p-1)/2); i-1 is not in P u {i}. rho_m and
rho_(m+1) lie in the block {m,m+1}, and every pair lies in some block together with some rho_m; Lemma 9 chains all of
them. Define theta_i := d(rho_(g/2)). |theta_i| <= D0+max(X,Y) <= (g-2)+(2delta+2) = 4kappa-g < 2p (each list entry is
<= 2(delta+2)). For e empty, X_e = 0 = sigma_e, so theta_e = tau_e = y_e-y_(e-1) != 0 (mod p) by the empty-run rule;
theta_e is even and |theta_e| < 2p, so theta_e is a nonzero even integer. []
Put Theta(P) := sum_(i in P) theta_i and f(P) := U'(P)-Theta(P) (P in Cl). Lemma 10 gives f(P u {i}) = f(P) for every
pair.
LEMMA 11 (complements). For P in Cl, U'(P)+U'(P^c) = Pi0-nu0-2p = B*-2nu0-2p.
Proof. sum_i hh_i = 0+sum_l c_l = Pi0-nu0 (mod p) and sigma(P)+sigma(P^c) = Pi0-nu0, so U(P)+U(P^c) = Pi0-nu0
(mod 2p). By Lemma 8 with (lambda,mu)(P^c) = (mu,lambda)(P) it lies in [2Pi0+2-(lambda+mu), 4p-2-2nu0+(lambda+mu)], of
length 4p-4-2B*+2(x+y-2) <= 2g-4+2delta = 4kappa-4 < 2p, which contains Pi0-nu0+2p (both end conditions read
B* <= 2p-4+x+y, Lemma 8). []
LEMMA 12 (an additive triple). Let m_T := max(g/2, ceil(kappa/4), ceil((kappa-g-1)/2)). Then m_T is central,
3m_T <= N, and for P1 := {0,3,...,3(m_T-1)}, P2 := P1+1 and P12 := P1 u P2 (all three with m = m_T):
U'(P12) = U'(P1)+U'(P2).
Proof. m_T <= kappa+1 and 3m_T <= N: 3g/2 <= 2kappa+g; 3(kappa+3)/4 <= 2kappa+g; 3(kappa-g)/2 <= 2kappa+g. P1, P2 are
independent (steps 3; wrap gaps of N-3m_T+2 >= 2 runs), disjoint, and P12 has the m_T maximal intervals {3k,3k+1}
separated by single runs and by the N-3m_T+1 >= 1 runs 3m_T-1, ..., N-1. Write ell, M for the level m_T and q1, q2, q12,
q'1, q'2, q'12 for q, q' of P1, P2, P12. By Lemma 5(c), as L(P1), L(P2) are disjoint:
  (I1) q1+q2 = a+q12, q'1+q'2 = a'+q'12, q12+q'12 = R;   (I2) q1+q'12 >= a, q2+q'12 >= a, q'1+q12 >= a', q'2+q12 >= a'.
Delta := U(P1)+U(P2)-U(P12) = 0 (mod 2p) (Hh, sigma additive). By Lemma 8:
  Delta >= M0+6-(y1+y2+x12)  and  Delta <= 4p-6-nu0-B*+(x1+x2+y12).
Lower bound. y_k is eps, M-q_k or ell-q'_k; x12 is eps, ell-q12 or M-q'12. By (I1), (I2) the 27 sums are bounded by
  2M+ell-a, 3M-a-R, 2M+1-a, 2ell+M-a', 3ell-a'-R, 2ell+1-a', delta+4
(e.g. (M-q1)+(M-q2)+(ell-q12) = 2M+ell-a-2q12; (M-q1)+(ell-q'2)+(ell-q12) <= M+2ell-a' by q'2+q12 >= a';
(M-q1)+(ell-q'2)+(M-q'12) <= 2M+ell-a by q1+q'12 >= a; sums with an eps are <= 1+ell+M or of the listed eps forms).
Each is <= M0+5: 2M+ell <= 2delta+4 <= 4kappa+3, 2M+1 <= 4kappa+3 and 3M-R <= 4kappa+3, so Lemma 6(ii) covers the
'a' terms;
2ell+M-a' <= M0+5 follows from Lemma 6(iii) if 2a' >= 2ell+M+g-5 = 2kappa+ell-3, and 2ell+1-a' <= M0+5 if
2a' >= 2ell+g-4; with 2a' >= 3kappa+g (Lemma 5(d)) these hold since ell = 2kappa+2-2m_T <= min(kappa+g+3, (3kappa+4)/2)
(m_T >= (kappa-g-1)/2 and m_T >= kappa/4); 3ell-R <= 2kappa+4 and delta+4 <= 2kappa+4 <= M0+5 by Lemma 6(i). So Delta >= 1.
Upper bound. Symmetrically the 27 sums x1+x2+y12 are <= max(2ell+M, 2M+ell, 3ell-R, 3M-R, 1+2(delta+2), 3) <= 2delta+5,
and 2delta+5 < B*+nu0+6 as 2delta <= R. So Delta < 4p, hence Delta = 2p. []
LEMMA 13 (connectivity, constant, total). f is constant on Cl, the constant is 0, i.e. U'(P) = Theta(P) for every P in
Cl, and Theta(all runs) = B*-2nu0-2p.
Proof. (a) If P in Cl has a maximal interval [x,z] with x != z, then P\{z} has the same m: P is joined to an independent
set of m(P) runs. (b) Independent m-sets (m central) are joined: if V has a gap g_j >= 2 (runs strictly between
consecutive members), V u {v_(j+1)-1} (same m) and (V\{v_(j+1)}) u {v_(j+1)-1} move one unit from gap j to gap j+1;
pushing units forward reaches gaps (1,...,1,G) with G = N-2m+1 >= 3, i.e. {x,x+2,...,x+2m-2}, and moving the members
forward one at a time rotates it. (c) In the form {x,...,x+2m-2} the gap G >= 3 admits a run at distance >= 2 from both
neighbours; adding it is a pair of levels (m,m+1). So Cl is connected by pairs and f is a constant f0. Lemma 12 and
additivity of Theta give f0 = f(P12) = f(P1)+f(P2) = 2f0, so f0 = 0. Q0 := {0,2,...,2(g/2-1)} and Q0^c both have
m = g/2; Lemma 11 gives Theta(all runs) = U'(Q0)+U'(Q0^c) = B*-2nu0-2p. []
This proves Theorem UMR-F.

## 4. Final-count reductions [NEW, uniform]

S_ev := {0,2,...,N-2} and S_od := {1,3,...,N-1} each have h = kappa+g/2 runs, pairwise non-adjacent; a subset Q of one
of them with 1 <= |Q| <= h-1 is a proper independent set with m(Q) = |Q|, and every central size is <= h-1
(Lemma 0). For an alternating set S put Xi(S) := Theta(S)+nu0+h-kappa, N_S := {i in S : theta_i >= 0},
P_S := {i in S : theta_i <= 0}, n_S := |N_S|; e(X) := number of empty runs in X; S' := the other alternating set.
LEMMA 14 (identity). Xi(S_ev)+Xi(S_od) = e* >= 0. Hence Lemma FC (Xi(S_ev)+Xi(S_od) <= -1) excludes the frame, and
FC for every frame of every NF word would prove the whole target.
Proof. Lemma 13: Theta(S_ev)+Theta(S_od) = B*-2nu0-2p, so the sum is B*-2p+2h-2kappa = B*-2p+g = B*-R. []
LEMMA 15 (half-certificates). Let j be central and Q c S with |Q| = j.
 (U) If N_S c Q: Xi(S) <= x_j(Q)+j-kappa-2-e(S\Q).   (L) If P_S c Q: Xi(S) >= kappa+2+e*-j-y_j(Q)+e(S\Q).
Here x_j, y_j are x, y of Lemma 7 at level j.
Proof. (U) Theta(S) = Theta(Q)+sum_(S\Q) theta, Theta(Q) = U'(Q) <= up(Q) = -2-nu0+x_j(Q) (Lemmas 8, 13); every run
of S\Q has theta <= -1, and an empty one theta <= -2 (Lemma 10). So Xi(S) <= -2+x_j(Q)-(h-j)-e(S\Q)+h-kappa.
(L) Theta(Q) >= low(Q) = Pi0+2-y_j(Q)-2p = -g+e*+2-nu0-y_j(Q); every run of S\Q has theta >= 1, an empty one >= 2;
so Xi(S) >= -g+e*+2-y_j(Q)+(h-j)+e(S\Q)+h-kappa, and 2h-g = 2kappa. []
DEFINITION (good). For central j <= kappa put lo_j := kappa+1-j and hi_j := R+g+kappa+1-3j. A set Q with N_S c Q c S,
|Q| = j, is +good if lo_j <= q(Q) <= hi_j; a set Q with P_S c Q c S, |Q| = j, is -good if lo_j <= q'(Q) <= hi_j.
LEMMA 16. If Q is +good, Xi(S) <= -1-e(S\Q). If Q is -good, Xi(S) >= 1+e*+e(S\Q).
Proof. q >= lo_j gives ell_j-q <= kappa+1-j; q <= hi_j gives q' >= 3j-g-kappa-1, i.e. M_j-q' <= kappa+1-j; and
eps <= 1 <= kappa+1-j. So x_j(Q) <= kappa+1-j; use (U). The -good case is the same with q, q' exchanged, giving
y_j(Q) <= kappa+1-j; use (L). []
LEMMA 17 (exact cases). (a) If n_S <= kappa and every Q with N_S c Q c S, |Q| = kappa, has q(Q) = 0, then n_S < kappa
and Xi(S) <= -g/2. (b) If |P_S| < kappa and every Q with P_S c Q c S, |Q| = kappa, has q'(Q) = 0, then
Xi(S) >= g/2+e*. If |P_S| = kappa, q'(P_S) = 0 and S\P_S contains an empty run, then Xi(S) >= 1+e*.
Proof. (a) q(Q) = 0 means L(Q) = A. If n_S = kappa, then L(N_S) = A, x_kappa(N_S) = ell_kappa = 2 and
0 <= Theta(N_S) <= up(N_S) = -nu0; so nu0 = 0, A is empty, every run of N_S is empty and has theta >= 2: impossible.
So n_S < kappa. For distinct u, v in S\N_S choose T0 c S\(N_S u {u,v}) with |T0| = kappa-n_S-1 (possible as
h >= kappa+1): L(N_S u T0 u {u}) = A = L(N_S u T0 u {v}) forces L_u = L_v, and L_u, L_v are disjoint, so both are empty.
As |S\N_S| >= 2, every run of S\N_S is empty and L(N_S) = A. With j := max(g/2,n_S) <= kappa and
Q := N_S u (any j-n_S runs of S\N_S): q(Q) = 0, x_j(Q) = ell_j and e(S\Q) = h-j, so (U) gives
Xi(S) <= ell_j+j-kappa-2-(h-j) = kappa-h = -g/2. (b) Same swapping with L(Q) = A^c: every run of S\P_S is empty and
L(P_S) = A^c; with j := max(g/2,|P_S|) and Q := P_S u (empty runs), y_j(Q) = ell_j and (L) gives
Xi(S) >= kappa+2+e*-j-ell_j+(h-j) = g/2+e*. If |P_S| = kappa and q'(P_S) = 0, y_kappa(P_S) = ell_kappa = 2 and (L) gives
Xi(S) >= e*+e(S\P_S). []
LEMMA 18 (no jump). Suppose no two runs of S together hold >= p+3 letters.
 (+) If n_S <= kappa and no Q is +good, then either every kappa-superset Q of N_S in S has q(Q) = 0, or n_S > g/2 and
     every kappa-superset Q of N_S in S has q'(Q) <= delta-2.
 (-) If |P_S| <= kappa and no Q is -good, then either every kappa-superset Q of P_S in S has q'(Q) = 0, or |P_S| > g/2
     and every kappa-superset Q of P_S in S has q(Q) <= delta-2.
Proof. (+) Let j0 := max(g/2,n_S) and, for j0 <= j <= kappa, Q_j := {Q : N_S c Q c S, |Q| = j} (nonempty, h >= kappa).
For a run u not in Q, q(Q u {u}) = q(Q)+d_u with d_u := |L_u n A^c|-|L_u n A| (Lemma 5(c)), |d_u| <= r_u. Each
q(Q), Q in Q_j, is < lo_j ('below') or > hi_j ('above'). Within Q_j: hi_j-lo_j = R+g-2j >= 2p-2kappa >= p+3; two members
of Q_j are joined by single exchanges (one run of Q\N_S replaced by one run of S\Q), and an exchange from below to
above changes q by d_u-d_v >= hi_j-lo_j+2, forcing r_u+r_v >= p+5: excluded. So each Q_j is wholly below or wholly
above. Between consecutive levels: if Q_j is below and Q_(j+1) above, take Q in Q_(j+1) and u in Q\N_S; then
d_u = q(Q)-q(Q\{u}) >= hi_(j+1)-lo_j+2 = R+g-2j-1 >= p+4: excluded. If Q_j is above and Q_(j+1) below, -d_u >=
hi_j-lo_(j+1)+2 = R+g+3-2j >= p+6: excluded. So all levels are below, or all above. All below: at j = kappa,
q(Q) < lo_kappa = 1. All above: at j0 = g/2 this is impossible (hi_(g/2) > R >= q), so j0 = n_S > g/2, and at j = kappa
q(Q) > hi_kappa = R+g+1-2kappa, i.e. q'(Q) <= delta-2. (-) Identical with q' and -d_u. []
DEFINITION UB. For an alternating set S (other set S'), UB(S) holds if one of: (UB1) some Q is +good for S; (UB2) the
hypothesis of Lemma 17(a) holds for S; (UB3) some Q is -good for S'; (UB4) one of the hypotheses of Lemma 17(b) holds for
S'.
LEMMA 19. UB(S) implies Xi(S) <= -1.
Proof. UB1: Lemma 16. UB2: Lemma 17(a). UB3, UB4: Lemmas 16, 17(b) give Xi(S') >= 1+e*, so Xi(S) = e*-Xi(S') <= -1
(Lemma 14). []
Proof of Theorem UMR-P. If UB(S_ev) and UB(S_od) hold for some frame, Lemma 19 gives Xi(S_ev)+Xi(S_od) <= -2 < 0 <= e*,
contradicting Lemma 14. So no such avoider exists. []

## 5. Lemma FC: the exact first failing uniform lemma

LEMMA FC (needed, NOT proved). For every (kappa,p) in T, every NF word u as in Sec. 0 and every frame of u,
Xi(S_ev)+Xi(S_od) <= -1.
Proved part. FC holds for every frame satisfying UB(S_ev) and UB(S_od) (Theorem UMR-P). Lemmas 1-19 are uniform on T.
Residual class RES := frames in which UB(S) fails for some alternating set S (with S' the other one).
LEMMA 20 (structure of RES). If UB(S) fails, then
 (i) S contains two runs holding together >= p+3 letters; or n_S >= kappa+1; or g/2 < n_S <= kappa and every
     kappa-superset Q of N_S in S has q'(Q) <= delta-2;
and
 (ii) S' contains two runs holding together >= p+3 letters; or |P_(S')| >= kappa+1; or g/2 < |P_(S')| <= kappa and every
     kappa-superset Q of P_(S') in S' has q(Q) <= delta-2; or |P_(S')| = kappa, L(P_(S')) = A^c and no run of
     S'\P_(S') is empty.
Moreover, in the second and third alternatives of (i), S' holds at most delta letters of A^c (if n_S >= kappa+1, every
(kappa+1)-subset Q' of N_S has 0 <= Theta(Q') <= up(Q') = -2-nu0+max(eps, delta+2-q'(Q')), so q'(Q') <= delta-nu0; and
|A^c \ L(S)| <= q'(Q)).
Proof. (i): if S has no such pair of runs and n_S <= kappa, Lemma 18(+) applies (UB1 fails); its first alternative is
UB2 (n_S < kappa) or impossible (n_S = kappa) by Lemma 17(a). (ii): the same with Lemma 18(-) for S' (UB3 fails); its
first alternative is UB4 unless |P_(S')| = kappa and S'\P_(S') has no empty run. []
Where the method stops. In RES every set available to (U) for S contains N_S (or, through Lemma 14, every set
available to (L) for S' contains P_(S')); by Lemma 20 these sets are 'A^c-saturated' (resp. 'A-saturated') at every
central level <= kappa, so their offsets exceed kappa+1-j and Lemma 15 bounds Xi(S) only by a nonnegative number.
Additional constraints that hold in RES and are not exploited here: the lower windows of all central subsets of S and
S', the windows of non-independent central sets, empty-run evenness inside N_S and P_(S'), and the freedom to choose
another frame. No proof that RES is nonempty is claimed; FC may hold on RES, but it is not proved here.

## 6. The three named cells (instantiated; status OPEN at Lemma FC)

(kappa,p) = (7,17): N = 18, R = 30, g = 4, delta = 10, h = 9, H = 9, F = 36, 2p = 34. Central levels 2..8 with
(ell,M) = (12,0), (10,2), (8,4), (6,6), (4,8), (2,10), (0,12). Frame: t <= 6, L >= 18, (S') at (k',kappa') = (16,6) with
34+12-16 = 30 = R; E <= 3+n- <= 9, so E <= 8; a_i <= 9, s_j <= 11, bmax <= 11; u1 >= |b_l|+13; a' >= 13;
M0 >= 13+E/2, M0 >= 26+e*-a, M0 >= a'-4+e*. Lemma 7: x+y <= 12; Lemma 8 windows of length <= 12; Lemma 9:
|d-d'| <= 28 < 34. Lemma 12: m_T = 2, P1 = {0,3}, P2 = {1,4}, P12 = {0,1},{3,4}; ell = 12 <= min(14, 12.5). Lemma 13:
Q0 = {0,2}, Q0^c = {1},{3,...,17}. Sec. 4: alternating sets of 9 runs; lo_j = 8-j, hi_j = 42-3j; the giant threshold is
20 letters in two runs. STATUS: OPEN at Lemma FC (RES at these constants is not excluded).
(kappa,p) = (7,19): N = 20, R = 32, g = 6, delta = 8, h = 10, H = 11, F = 42, 2p = 38. Central levels 3..8 with
(ell,M) = (10,0), (8,2), (6,4), (4,6), (2,8), (0,10). Frame: t <= 6, L >= 20, (S') at (18,6) with 38+12-18 = 32 = R;
E <= 5+n- <= 11, so E <= 10; a_i <= 11, s_j <= 11; u1 >= |b_l|+13; a' >= 14; M0 >= 13+E/2, M0 >= 26+e*-a,
M0 >= a'-6+e*. Lemma 9: |d-d'| <= 28 < 38. Lemma 12: m_T = 3, P1 = {0,3,6}, P2 = {1,4,7}; ell = 10 <= min(16, 12.5).
Lemma 13: Q0 = {0,2,4}, Q0^c = {1},{3},{5,...,19}. Sec. 4: 10 runs per alternating set; lo_j = 8-j, hi_j = 46-3j; giant
threshold 22. STATUS: OPEN at Lemma FC.
(kappa,p) = (8,19): N = 20, R = 34, g = 4, delta = 12, h = 10, H = 10, F = 40, 2p = 38. Central levels 2..9 with
(ell,M) = (14,0), (12,2), (10,4), (8,6), (6,8), (4,10), (2,12), (0,14). Frame: t <= 7, L >= 20, (S') at (18,7) with
38+14-18 = 34 = R; E <= 3+n- <= 10; a_i <= 11, s_j <= 13; u1 >= |b_l|+15; a' >= 14; M0 >= 15+E/2, M0 >= 30+e*-a,
M0 >= a'-4+e*. Lemma 9: |d-d'| <= 32 < 38. Lemma 12: m_T = 2, P1 = {0,3}, P2 = {1,4}; ell = 14 <= min(15, 14).
Lemma 13: Q0 = {0,2}. Sec. 4: 10 runs per alternating set; lo_j = 9-j, hi_j = 47-3j; giant threshold 22.
STATUS: OPEN at Lemma FC.
For each cell, Theorem UMR-P excludes every NF word with a frame outside RES; no cell is claimed excluded.

## 7. Route remarks and the parent route note (no claims beyond Secs. 0-6)

(M1) Parent note, re-derived. The unit reservoir u1 >= |b|+2kappa-1 holds (Lemma 4(iv); for -s_j the coupling
 n+ + E/2 <= 2kappa-3+g/2 through t is needed). The original positive-unit count >= (p+kappa+1)/2 holds (Lemma 5(d)).
 The margin M0 >= 4kappa-2+(B*-R)-|A| holds (Lemma 6(ii)); also M0 >= |A^c|-g+(B*-R) (Lemma 6(iii)). The offsets
 x = max(eps, ell-q, M-q'), y = max(eps, M-q, ell-q') are valid for every pattern at every central level, with the
 'bridge' argument written as Cases U and L of Lemma 7. Coupled additivity is used for one interleaved triple at the
 level m_T (Lemma 12, couplings (I1), (I2)).
(M2) All central levels at once. Theta is pair-independent on the whole central range [g/2, kappa+1], not only near the
 balanced level: inside a block of two consecutive levels the exact identity q(P u {i})-q(P) = beta_i-alpha_i keeps the
 offset sums <= 2delta+8 < 4kappa+6, and blocks chain through (m,m)-pairs (Lemmas 9, 10).
(M3) Final count. Sorting the top j runs of each alternating set is the special case Q = top-j of (U). With N_S and
 P_S both certificates (U), (L) and the identity of Lemma 14 combine in four compatible ways; Lemmas 16-19 turn this
 into the explicit sufficient condition UB. The obstruction is the residual class RES of Lemma 20.
Failed or unused routes (kept; not premises).
(R1) Top-j sorting at a single level: fails when both sorted sets are near A (letter-poor sorted runs).
(R2) Partitioning an alternating set into central sets: each block contributes only about -2-nu0, too little.
(R3) Averaging over all j-subsets: the slack is far too small at the levels where typical subsets are generic.
(R4) PL Secs. 7-9, Theorem P, CJ''', K3-11 and all USK, FCW, SCW, TCW, P7L and FQW lemmas are not used.

## 8. Scope and interface table

Claimed: Theorem UMR-F and Theorem UMR-P for every (kappa,p) in T, and Lemmas 0-20, all proved only on T in the frame of
Sec. 1. NOT claimed: the exclusion of the target cells (Lemma FC is open on RES); the exclusion of (7,17), (7,19) or
(8,19); any statement for kappa or p outside T; kappa_hat != kappa; nonterminal k; reflection rigidity; INV*; o_F
assembly; full ordered Olson; any multiset-only statement outside the antecedent; that RES is nonempty; novelty,
priority, "first", Lean, human review or runtime authority. No USK, FCW, SCW, TCW, P7L or FQW statement is extended or
used as a premise.
Aroot=/Users/jinleic/repos/aifours; R16=Aroot/institute/runs/six-lane-2026-10-16/review;
R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review;
ROT=Aroot/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation;
FBP=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/evidence;
CONT=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations.
| Input | Path; whole-file SHA256 | LF lines | Scope; use here |
|---|---|---|---|
| NF | ROT/proof-ROT-few-E-v4.md; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | 28-43 | some admissible NF; odd blocks; empty-run rule; H = (F-k)/2, kappa = p-1-H, R = 2p+2kappa-k (line 42) |
| GRX | ROT/notes-GRX-v1.md; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | 7-20 | if-direction; Lemma 1 |
| SC0 | R16/olson-index-one-primary-statement-parent-v1.md; e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6 | 1-11 | 1-element basis of a minimal zero-sum sequence of length >= floor(n/2)+2 over C_n, n >= 3; applied to Y'z (Lemma 3(c)) |
| ZSTRUCT, FB in (S') | R18/olson-FB-parent-verdict-v1.md 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a (1-16); FBP/proof-FB-v1.md 339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b (9-24); FBP/proof-FB-v1-erratum-1.md 33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202 (1-7, no statement change); (S') extension R18/olson-balfull-rotzb-parent-verdict-v1.md 56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0 (26-34) | as listed | Lemma 3(d), t >= 1 only, at (k',kappa') = (p-1,kappa-1): Z-shape, n- >= 1, 1 <= s_j <= 2t-1, balance, W+n+ <= 2p-1. FB-E NOT used |
| (S1) definition | R16/olson-zx-s1c-parent-verdict-v1.md; 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af | 19 | the definition "(S1) bounds every zero-sum length by 2kappa" only; S1(a) NOT used (Lemma 3(b) is direct) |
| LOWER parent erratum | R18/olson-LOWER-parent-erratum-v1.md; 087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377 | 1-10 | m(P) = half the sign transitions (LF7); theta only through explicit pairs (LF6) |
| FCW parent erratum | R18/olson-FCW-parent-erratum-v1.md; e56bf0f337d7d670be99075829217431cf605437320dd3414cde75c3d1ae2413 | 1-14 | derivation patterns only: (SR) from NF+GRX (m4, LF8), redone in Lemma 1; SC0 through Y'z (m3, LF7), redone in Lemma 3(c) |
| context only | R18/olson-USK-parent-verdict-v1.md 6d3358ce3f1e9e95a366f2b32f10adbc73df607bc62723f561567dce1a53de18; R18/olson-FCW-parent-verdict-v1.md b28837c9c8a9549b99a6c2205e8bbe40d65ab1aad265595c511395d4c1738f71; R18/olson-SCW-parent-verdict-v1.md d51b5d8e6c6a7c38047434b3740d477bccd2ab7e0e53ce68ea34aa83486bdfe0; R18/olson-TCW-parent-verdict-v1.md 17f6d80d664c4e3b60bb7be5aba560502f5597350b025b3d058d7d989fef0c29; R18/olson-P7L-parent-verdict-v1.md 57664b53b35aa0de0729d7ec7b2c2ff4d9b7e738155612c5ffcb43ec169a8569; R18/olson-K0T-parent-verdict-v1.md 4a2a2ffd8d8624c33c0f7cc1265cf679c18ac3a9c63565bc093b2e8afc8bf8ba; R18/olson-LOWER-K1-parent-verdict-v1.md 93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83 | whole | exact scopes only; not premises |
| untrusted | R18/olson-UMR-parent-untrusted-route-note-v1.md 738567ca9367edf739444af614bc923a40773d28926d42411b52bdb3cbbb142a (read after the freeze); CONT/lowerhalf-fourth-cut-window/proof-FQW-v1.md 9b4561780b37874c47a188fc788ae34fc223f1252f7e4bf9a1be9a6dffd09dc5; CONT/lowerhalf-third-cut-window/proof-TCW-v1.md 62c747911239c32998d2ec2b3bd9ec538eee5e523f68b92233aa06e890f85713; CONT/p7-lower-terminal/proof-P7L-v1.md 7e8bee08dacb10a9b4dd373dc9e57e526a21bd4bc77e91a41091b8e88cacb7e8 | whole | methods only, re-derived; never premises |
Not used: PL (proof-LOWER-v1.md) in its entirety (every step written out); S1(a); the Setting fact; FB-E; Theorem P;
B0S-CJ'''; every USK, K3, FCW, SCW, TCW, P7L and FQW lemma; P11R and every other unreviewed candidate.
Machine steps for this file: /bin/date, shasum -a 256, wc -c -l, reading files, and one exclusive creation (Python
open(path,'x')) of this text, drafted by hand in memory in six parts; in-memory rewording replacements before creation
are disclosed in the checkpoints; no assertion of any kind and no check over mathematical objects.
