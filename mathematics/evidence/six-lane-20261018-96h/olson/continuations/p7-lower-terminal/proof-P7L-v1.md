# P7L: p = 7, terminal k = 8, kappa_hat in {1, 2}: both lower-half terminal cells are excluded, v1

Owner OlsonThirdCutWindow (reassigned math2 slot). Drafted by hand after /bin/date 2026-10-20T06:09:40-0700. Status:
CANDIDATE_UNVERIFIED written proof of the FULL frozen target (P7L-scope-v1.md SHA256
a1f2f6835c71b2a96a2062f830032144a2d5e590adf65864c1307e87db1113f3, frozen 2026-10-20T05:53:51-0700 before any derivation;
authority RUN/control/written-olson-p7-lower-transition-v1.json SHA256
618eff97592b75aab0a382ed57c25a072c5cb076ee3af07084855d35eda3578f). Outcome: cell (kappa_hat,p) = (2,7) PROVED (Sec. 2);
cell (1,7) PROVED (Sec. 3); no failing lemma. LABELLED PARTIAL of ordered Olson: two terminal lower-half cells at p = 7.
All case work is by hand; no script, assertion, enumeration or computation over scientific data. No novelty, priority,
Lean or human-review claim; no other cell; not the whole of p = 7; no full ordered Olson.

## 0. Statements

THEOREM P7L-2 (cell (2,7)). No word w of length 26 over D_14 without an identity 14-subword in increasing original index
order has an admissible normal form (NF) with terminal k = 8 and kappa_hat = 2.
THEOREM P7L-1 (cell (1,7)). The same with kappa_hat = 1.
Full antecedent in both: SOME admissible NF of w; the H = 6-kappa_hat extra reflection pairs lie anywhere in the odd
blocks; every empty NF run separates different reflection values; no o_F, nonempty-run, rotation-pair or
reflection-rigidity hypothesis on w.
Routes. Sec. 1 (both cells, re-derived at p = 7): (SR) from NF and GRX (Lemma 1), windows (Lemma 2), frame with SC0 and
ZSTRUCT/FB (Lemma 3), light side (Lemma 4), density and signed sums (Lemma 5), lift margin (Lemma 6), zero-signed sets
(Lemma 7), representatives (Lemma 8) and the lift principles: additivity, complements, pair-independent theta, empty runs
(Lemma 9). Sec. 2 (kappa_hat = 2): FCW-type realisation at m in {2,3}, theta, connectivity of m = 3, an additive pair
whose union has m = 2, sorting the top two runs of each alternating set: B* <= 9 < 10 = R. Sec. 3 (kappa_hat = 1): the
m = 1 window [2,8] behaves like a full window for two-signed singletons; the lift framework on all sets with m in
{1,2,3}; every theta_i equals the representative of the singleton {i}; summing gives the contradiction directly.
Exposure. Before the freeze I had derived the unaccepted TCW candidate (p = 4kappa-5) and read FCW, SCW and their inputs;
the transition disclosed the parent's untrusted route notes. No FCW, SCW, USK, K1, K2, R7 or TCW lemma is a premise; every
step is re-derived at p = 7 from the literal NF, GRX, SC0 and ZSTRUCT/FB interfaces (Sec. 6). PL (proof-LOWER-v1.md) is
accepted only for p >= 11 and is not imported.

## 1. Common setting at p = 7, k = 8

Throughout kappa := kappa_hat in {1,2}, p = 7, 2p = 14. The NF word u of w is an avoider of length 26 with the rotation
multiset of w [NF, lines 37-38]. Read it cyclically as R_0 S_0 R_1 S_1 ... R_7 S_7: there are N = k = 8 blocks
S_i = sigma_(y_i)^(l_i) with l_i odd, and 8 runs R_i of r_i >= 0 rotation letters; an EMPTY run R_i has y_(i-1) != y_i
(indices mod 8). By NF line 42, H := (F-8)/2 = sum_i (l_i-1)/2, kappa = 6-H and R = 14+2kappa-8 = 6+2kappa, so F = 26-R:
kappa = 1: R = 8, F = 18, H = 5; kappa = 2: R = 10, F = 16, H = 4.
Put tau_i := y_i - y_(i-1) in Z_7 (so sum_i tau_i = 0). For a set P of runs, m(P) is half the number of sign transitions
of the cyclic pattern (-1 on P, +1 off P) (LOWER parent erratum): m(empty) = m(all runs) = 0, a proper nonempty P has
m(P) equal to its number of maximal cyclic intervals, and m(P^c) = m(P); as N = 8, m(P) <= 4, and m(P) = 4 only for the
two alternating sets S_ev := {0,2,4,6} and S_od := {1,3,5,7}. T(P) := sum_(i in P) tau_i. X^(P) is the list of letter
values (rho_x contributes x in Z_7) with every letter of a run of P negated; letters(P) is the set of letters lying in
runs of P. A set of runs is independent if its members are pairwise non-adjacent (mod 8); a proper independent set of
j >= 1 runs has m = j.

LEMMA 1 ((SR) at p = 7). For every set P of runs and every even n with max(0,2kappa+2-2m(P)) <= n <= min(R,14-2m(P)),
T(P) is not a sum (in Z_7) of n letters (distinct occurrences) of X^(P).
Proof [NF, GRX if-direction; the derivation of the FCW parent erratum m4, redone at p = 7]. The NF representation is a
cyclic alternation of runs and constant blocks, so GRX applies to u (with GRX's z_i the sign of run R_i and its
theta_i = y_(i-1) - y_i = -tau_i). Take z_i = -1 iff i is in P. Then X^z = X^(P) and, as sum_i tau_i = 0,
T(z) = sum_(i not in P) theta_i = -sum_(i not in P) tau_i = T(P). Phi = sum_i [z_i != z_(i+1)] = 2m(P). Every l_i is
odd, so l_i != f_i (mod 2) iff f_i = 0, delta = 8-2m(P), and C_max = F-delta = 2H+2m(P) (F = 8+2H). GRX: if some even C
with 2m(P) <= C <= 2H+2m(P) and 0 <= 14-C <= R has T(P) in Sigma_(14-C)(X^(P)), then u has an identity 14-subword.
With n := 14-C these conditions read: n even, 14-2H-2m(P) = 2kappa+2-2m(P) <= n <= 14-2m(P) (2H = 12-2kappa), 0 <= n <= R.
u is an avoider, so no such n exists. [] Write Win_m for this set of n when m(P) = m.

LEMMA 2 (windows; sets of even integers).
 kappa = 1 (R = 8): Win_0 = [4,8], Win_1 = [2,8], Win_2 = Win_3 = [0,8], Win_4 = [0,6].
 kappa = 2 (R = 10): Win_0 = [6,10], Win_1 = [4,10], Win_2 = [2,10], Win_3 = [0,8], Win_4 = [0,6].
Proof. Substitute m = 0, ..., 4 into Lemma 1. []

LEMMA 3 (frame).
(a) [pigeonhole] The 8 block values lie in Z_7, so y_c = y_c' for some c != c'. The arc P0 := runs c+1,...,c' (mod 8) is
 proper and nonempty with T(P0) = y_c' - y_c = 0; its complementary arc C0 has T(C0) = 0; m(P0) = m(C0) = 1.
(b) [direct] Let Y be the sequence of the R elements (1,x) of Z_2 x Z_7 = C_14, one for each letter x of X^(P0). A
 zero-sum subsequence of Y of length n is a set of n letters whose X^(P0)-values sum to 0 = T(P0); n is even (first
 coordinates) and n <= R. Lemma 1 at P0 (m = 1) excludes every even n in Win_1 = [2kappa,R]. Hence: for kappa = 1, Y is
 zero-sum free; for kappa = 2, every zero-sum of Y has length 0 or 2.
(c) [SC0, through the minimal-zero-sum step] Let Z be a LONGEST zero-sum of Y, |Z| = 2t: t = 0 if kappa = 1, t in {0,1}
 if kappa = 2. Y' := Y - Z is zero-sum free (a nonempty zero-sum of Y' together with Z would be longer) and has length
 L = R-2t = 8 = p+1 (kappa = 1) or L = 10-2t >= 8 (kappa = 2). Put z := -sigma(Y'); z != 0 because Y' is nonempty and
 zero-sum free. Y'z is a minimal zero-sum sequence: a nonempty proper zero-sum subsequence T of Y'z would give the
 nonempty zero-sum T inside Y' (if z is not in T) or Y'z - T inside Y' (if z is in T). Its length is L+1 >= 9 =
 floor(14/2)+2, and 14 >= 3, so by SC0 it has a 1-element basis {g}: every term is x*g with least positive coefficient
 x, and the coefficients sum to ord(g). There are L+1 >= 9 coefficients, each >= 1, so ord(g) >= 9; as ord(g) divides
 14, ord(g) = 14 and g generates C_14. So Y' = (a_1 g)...(a_L g) with least positive coefficients a_i, and
 W := sum_i a_i = 14 - x(z) <= 13. Write g = (g_1,gamma). Every term of Y' has first coordinate 1, so a_i g_1 = 1 (mod 2):
 g_1 = 1 and every a_i is odd; gamma != 0, since (1,0) has order 2.
(d) [ZSTRUCT, FB in (S')] If t = 0, put n+ = n- = 0. If t = 1 (only for kappa = 2), Y lies in setting (S') with
 (k',kappa') = (6,1): p = 7 >= 5 is prime; 1 <= k' = 6 <= p-1; kappa' = 1 is an integer with 1 <= kappa' < p; Y consists
 of 2p+2kappa'-k' = 10 = R odd elements of C_14; every zero-sum of Y has length <= 2kappa' = 2 ((b), i.e. (S1) at
 kappa'); Z is a longest zero-sum with t = 1 <= kappa'; L = 8 >= 2p-k' = 8 = p+1; and g is an index-<1 generator of
 Y - Z (W <= 13). ZSTRUCT (accepted in (S') through its proof) gives Z = g^(n+) (-s_1 g)...(-s_(n-) g) with odd s_j >= 1,
 n+ + n- = 2 and n- >= 1; Lemma FB gives sum_j s_j = n+ and W + n+ <= 13. As each s_j >= 1, n- <= n+; so n+ = n- = 1,
 s_1 = 1 and W <= 12. Thus Z consists of two letters whose Y-terms are g and -g.
(e) [labels] Each letter l gets an odd integer label b_l, and its value in X^(P0) is b_l*gamma: the a-labels for the
 letters of Y', and the labels +1 and -1 for the two letters of Z (when t = 1). W = L (mod 2), so W is even, and
 E := W-L = sum_i (a_i-1) is even and >= 0; an a-label > 1 is odd, hence >= 3, and adds at least 2 to E. Therefore:
  kappa = 1: L = 8, W <= 12, E in {0,2,4}; the a-labels are {1^8}, {1^7,3}, {1^7,5} or {1^6,3,3}.
  kappa = 2, t = 0: L = 10, W <= 12, E in {0,2}; the a-labels are {1^10} or {1^9,3}.
  kappa = 2, t = 1: L = 8, W <= 12, E in {0,2,4}; the a-labels are {1^8}, {1^7,3}, {1^7,5} or {1^6,3,3}; in addition
  there are the labels +1 and -1.
 Write u1 := #{l : |b_l| = 1}. In every case at most two letters have |b_l| > 1, each such |b_l| is 3 or 5, and
 u1 >= 6 (kappa = 1), u1 >= 9 (kappa = 2, t = 0), u1 >= 8 (kappa = 2, t = 1). In particular u1 >= 5 >= |b_l| for every
 letter with |b_l| > 1. []
Normalisation. (v,eps) -> (gamma^(-1)v,eps) (v in Z_7) is an automorphism of D_14, since multiplication by a unit of Z_7
commutes with v -> -v and the group law is linear in v. Applied letterwise it preserves identity subwords in increasing
index order, the run/block structure with the empty-run rule and the exponents l_i, and Lemma 1, with tau_i and all
letter values scaled by gamma^(-1); the frame (a)-(e) is carried along with the same labels. So take gamma = 1. Put
c_l := b_l for letters l of C0 and c_l := -b_l for letters of P0. The original value of l (its value in X^(empty)) is
c_l (mod 7), and its value in X^(P) is eps_l c_l, where eps_l = -1 iff l lies in a run of P.

LEMMA 4 (light side). Let o(Q) := #{l in letters(Q) : b_l = 1}. Then min(o(P0),o(C0)) <= kappa, and the frame can be
chosen with q1 := o(P0) <= kappa.
Proof. Letters of C0 with b = 1 have c = 1; letters of P0 with b = 1 have c = -1. If o(C0) >= kappa+1 and
o(P0) >= kappa+1, then kappa+1 of each are 2kappa+2 letters whose original values sum to 0 = T(empty), and
2kappa+2 lies in Win_0 = [2kappa+2,R] (4 <= 8, 6 <= 10); Lemma 1 at P = empty forbids this. Exchanging P0 and C0 keeps
Lemma 3 with the same labels: C0 is a proper arc with T(C0) = 0, X^(C0) = -X^(P0), its sequence is -Y because
(1,-x) = -(1,x), the zero-sums of -Y are those of Y, Z stays longest, and -g is an index-<1 generator of -Y' with the same
coefficients (gamma -> -gamma). So exchange the two arcs if necessary, and then normalise. []
Quantities. A := {l : c_l < 0} and A^c := {l : c_l > 0} (every c_l is odd). Pi0 := sum_(l in A^c) |c_l|,
nu0 := sum_(l in A) |c_l|, B* := Pi0+nu0 = sum_l |b_l| = W+2t = R+E. B* is even, B* >= R, and B* = R iff every |b_l| = 1.
A priori B* is 8, 10 or 12 for kappa = 1 and 10, 12 or 14 for kappa = 2. sigma(P) := sum of c_l over letters(P) (an
integer), sigma_i := sigma({i}); X_i := sum of the original values of run i, so X_i = sigma_i (mod 7); hh_i := tau_i+X_i
and Hh(P) := sum_(i in P) hh_i = T(P)+sigma(P) (mod 7). For kappa = 1 every b_l > 0, so A = letters(P0).
Frame quantifier. Lemmas 3-4 hold for EVERY admissible choice of P0, Z, g and light side; the proof fixes one such
frame, and one always exists.

LEMMA 5 (density, signed sums, negative letters).
(a) Every integer of [0,B*] is a sum of a sub-multiset of {|c_l|} = {|b_l|}.
(b) Fix a set P of runs. Let Pos(P), Neg(P) be the letters with eps_l c_l > 0 and < 0, q(P) := |Neg(P)|,
 q'(P) := |Pos(P)| = R-q(P), Pi(P) := sum over Pos(P) of |c_l|, nu(P) := sum over Neg(P) of |c_l|. The signed sums
 sum_(l in J) eps_l c_l over sets J of letters are exactly the integers of [-nu(P),Pi(P)], each with the parity of |J|.
 Moreover Pi(P) = Pi0-sigma(P) and nu(P) = nu0+sigma(P).
(c) Neg(P) = letters(P) symdiff A. Hence X^(P) is all positive (q(P) = 0) iff letters(P) = A, and all negative
 (q'(P) = 0) iff letters(P) = A^c, i.e. letters(P^c) = A. "Two-signed" means q(P) >= 1 and q'(P) >= 1.
Proof. (a) The multiset consists of u1 ones and at most two further elements y, y' in {3,5}, each <= u1+1
(Lemma 3(e)). The sums of ones give [0,u1]; adding y gives [0,u1+y]; adding y' gives [0,B*]. (b) J -> (J n Pos(P)) u
(Neg(P) \ J) is a bijection on sets of letters with sum_(l in J) eps_l c_l = sum_(l in image) |c_l| - nu(P); apply (a) and
Pi(P)+nu(P) = B*. Each eps_l c_l is odd. Also Pi(P)-nu(P) = sum_l eps_l c_l = (Pi0-nu0)-2sigma(P). (c) A letter of a run
of P has value -c_l, negative iff l is in A^c; any other letter has value c_l, negative iff l is in A. []

LEMMA 6 (lift margin). M0 := 2Pi0+nu0-14 >= 1+E/2 if kappa = 1 and >= 3+E/2 if kappa = 2. In particular M0 >= 1.
Proof. A letter with c < 0 is (i) one of the q1 <= kappa letters of P0 with b = 1 (c = -1), or (ii) a letter of P0 with an
a-label B >= 3 (c = -B), or (iii) (t = 1) the letter with b = -1 if it lies in C0 (c = -1). Each B >= 3 satisfies
B <= (3/2)(B-1), and the numbers B-1 sum to at most E; so nu0 <= q1 + 3E/2 + t. With B* = R+E:
M0 = 2B*-nu0-14 >= 2R-14 + E/2 - q1 - t. For kappa = 1: 2R-14 = 2, q1 <= 1, t = 0. For kappa = 2: 2R-14 = 6, q1 <= 2,
t <= 1. []

LEMMA 7 (zero-signed sets). If X^(P) is two-signed, some set Z0 of letters with 2 <= |Z0| <= 6 has
sum_(l in Z0) eps_l c_l = 0.
Proof. If the letters with |c| = 1 take both values +1 and -1 in X^(P), a pair of them is Z0. Otherwise they all take one
value, say +1 (the case -1 is the negative); a letter of negative value then has value -y with y in {3,5}, and it
together with y of the u1 >= y letters of value +1 (Lemma 3(e)) is Z0, of size y+1 <= 6. []

LEMMA 8 (representatives). Fix a proper nonempty set P of runs. Call an even integer v REALISED at P if
v = sum_(l in J) eps_l c_l for some set J of letters with |J| in Win_(m(P)). Suppose that for some integers x, y >= 0,
with -nu0+x and Pi0-y of the parity of sigma(P), every integer of the parity of sigma(P) in [-nu0+x, Pi0-y] has the form
v+sigma(P) with v realised at P. Then B* <= 10+x+y, and there is an integer U(P) with U(P) = Hh(P) (mod 7),
U(P) = sigma(P) (mod 2) and
   Pi0+lo(P) <= U(P) <= 14-nu0+hi(P),   where lo(P) := 2-y and hi(P) := x-2.
An interval of length < 14 contains at most one integer with these two congruences. Put U'(P) := U(P)-14.
Proof. By Lemma 1, T(P) != v (mod 7) for every realised v, because the X^(P)-values are eps_l c_l (mod 7). As
Hh(P) = T(P)+sigma(P) (mod 7), Hh(P) is congruent to no integer of the parity of sigma(P) in [a,b], a := -nu0+x,
b := Pi0-y. The 7 integers a, a+2, ..., a+12 are pairwise incongruent mod 7 and have the parity of sigma(P), so Hh(P) is
congruent to exactly one of them, a+2j, and a+2j > b. If b >= a+12 this is impossible; so B*-x-y = b-a <= 10, and
a+2j lies in [b+2, a+12] = [Pi0+lo(P), 14-nu0+hi(P)]; put U(P) := a+2j. Since 7 is odd, the residues mod 7 and mod 2 fix
the residue mod 14, which an interval of length < 14 holds at most once. []

LEMMA 9 (lift principles). Let G be a family of proper nonempty sets of runs such that every P in G satisfies the
hypothesis of Lemma 8 for some x(P), y(P) in {0,1,2} with x(P)+y(P) <= 2; fix U(P) as in Lemma 8 (so lo(P) >= 0 >= hi(P)
and Pi0+lo(P)-14 <= U'(P) <= -nu0+hi(P)). Assume G is nonempty. Then:
(a) B* <= 12; in particular B* <= 2p-2 = 12 < 14.
(b) [additivity] If P1, P2 are disjoint and P1, P2, P1 u P2 are in G, then U'(P1 u P2) = U'(P1)+U'(P2).
(c) [complements] If P and P^c are in G, then U'(P)+U'(P^c) = Pi0-nu0-14 = B*-2nu0-14.
(d) [differences] If P and P u {i} (i not in P) are in G, then d := U'(P u {i})-U'(P) satisfies d = hh_i (mod 7),
 d = sigma_i (mod 2) and |d| <= 14-B* <= 14-R. Any two such differences for the same run i are equal.
(e) [empty runs] If run e is empty and P, P u {e} are in G, the common value d =: theta_e of (d) is a NONZERO EVEN
 integer with |theta_e| <= 14-R.
Proof. (a) Lemma 8 with x+y <= 2. (b) Delta := U(P1)+U(P2)-U(P1 u P2) is 0 (mod 7), since Hh is additive, and 0
(mod 2), since sigma is additive; so Delta = 0 (mod 14). Delta >= 2Pi0 + lo(P1)+lo(P2) - (14-nu0+hi(P1 u P2)) >= M0 >= 1
(Lemma 6), and Delta <= 2(14-nu0) + hi(P1)+hi(P2) - (Pi0+lo(P1 u P2)) <= 28-nu0-B* < 28. So Delta = 14.
(c) sum_(all i) hh_i = sum_i tau_i + sum_i X_i = 0 + sum_l c_l = Pi0-nu0 (mod 7), and sigma(P)+sigma(P^c) = Pi0-nu0. So
U(P)+U(P^c) = Pi0-nu0 (mod 14). It lies in [2Pi0, 28-2nu0], an interval of length 28-2B* <= 12 < 14 (B* >= R >= 8),
which contains Pi0-nu0+14 because B* <= 14. So U(P)+U(P^c) = Pi0-nu0+14.
(d) The congruences follow from those of U(P u {i}) and U(P). From the windows, d >= (Pi0+lo(P u {i})-14) -
(-nu0+hi(P)) >= B*-14 and d <= (-nu0+hi(P u {i})) - (Pi0+lo(P)-14) <= 14-B*. Two such values are congruent mod 14 and
differ by at most 2(14-R) <= 12 < 14 (R >= 8), so they are equal.
(e) X_e = 0 and sigma_e = 0, so theta_e = hh_e = tau_e = y_e - y_(e-1) (mod 7), which is nonzero by the empty-run rule;
theta_e is even, and |theta_e| <= 6 < 7, so theta_e != 0. []
Lift framework. For such a G, fix for each run i one explicit pair (P_i, P_i u {i}) in G (when it exists) and define
theta_i := U'(P_i u {i}) - U'(P_i); by Lemma 9(d) every pair (P, P u {i}) in G has difference theta_i (theta only
through explicit pairs, LOWER parent erratum). For P in G put Theta(P) := sum_(i in P) theta_i and f(P) := U'(P)-Theta(P).
Then f(P u {i}) = f(P) for every pair in G; so f is constant along any chain in G whose consecutive members differ in one
run.

## 2. Cell (2,7): proof of Theorem P7L-2

Here kappa = 2: R = 10, Win_2 = [2,10] = [2,R], Win_3 = [0,8] = [0,R-2], 14-R = 4, M0 >= 3. Let
Cl := {P : m(P) in {2,3}} and Fp := {P : m(P) = 3}; every P in Cl is proper and nonempty, and P^c is in Cl.

LEMMA 2.1 (realisation at m in {2,3}). Let P be in Cl and v an even integer in [-nu(P),Pi(P)].
 (i) If X^(P) is two-signed, v is realised at P.
 (ii) If letters(P) = A (all values positive; nu(P) = 0, Pi(P) = B*): for m(P) = 2 every even v in [2,B*] is realised;
      for m(P) = 3 every even v in [0,B*-2] is realised.
 (iii) If letters(P^c) = A (all values negative; Pi(P) = 0, nu(P) = B*): for m(P) = 2 every even v in [-B*,-2] is
      realised; for m(P) = 3 every even v in [-B*+2,0] is realised.
Proof. (i) By Lemma 5(b) choose J with signed sum v and |J| minimal. |J| is even, and no nonempty subset of J has
signed sum 0 (removing it would give a smaller J). So J is not the set of all letters, which contains the Z0 of Lemma 7;
hence |J| <= 9, i.e. |J| <= 8. If v != 0, then |J| >= 2 and |J| lies in [2,8], inside Win_2 and Win_3. If v = 0: for
m(P) = 2 take Z0 (|Z0| in [2,6]); for m(P) = 3 take J = empty (0 in Win_3).
(ii) For v != 0 any J with signed sum v (Lemma 5(b)) is nonempty with |J| even, so |J| >= 2; this proves the case m(P) = 2. For
m(P) = 3: v = 0 is realised by J = empty; for 2 <= v <= B*-2, J is not the set of all letters (whose sum is B*), so
|J| <= 8. (iii) is (ii) with all values negated. []
LEMMA 2.2 (windows on Cl). Every P in Cl satisfies Lemma 8 with (x,y) as follows, so Lemma 9 applies to G = Cl:
 two-signed: x = y = (nu(P) mod 2); letters(P) = A: (x,y) = (2,0) if m(P) = 2 and (0,2) if m(P) = 3;
 letters(P^c) = A: (x,y) = (0,2) if m(P) = 2 and (2,0) if m(P) = 3.
Hence (lo,hi) = (2-y, x-2) is (2,-2) or (1,-1) for two-signed P, and (2,0), (0,-2), (0,-2), (2,0) in the four
single-signed cases. In particular: B* <= 12 (so the a priori value 14 does not occur); U'(P) <= -nu0 for every P in Cl;
U'(P) <= -1-nu0 if X^(P) is two-signed; U'(P) <= -2-nu0 if letters(P^c) = A and m(P) = 2.
Proof. By Lemma 5(b), -nu(P)+sigma(P) = -nu0 and Pi(P)+sigma(P) = Pi0, and nu(P), Pi(P) have the same parity (B* is
even). Two-signed: by 2.1(i) the realised values are all even v in [-nu(P),Pi(P)], whose extreme values are
-nu(P)+x and Pi(P)-x with x = nu(P) mod 2. letters(P) = A: sigma(P) = -nu0, and 2.1(ii) gives the shifted ranges
[2-nu0,Pi0] (m = 2) and [-nu0,Pi0-2] (m = 3). letters(P^c) = A: sigma(P) = Pi0, and 2.1(iii) gives [-nu0,Pi0-2] (m = 2)
and [2-nu0,Pi0] (m = 3). In each case x+y <= 2. []

(F1) Theta. For a run i let Q_i := {i+1,i+3,i+5}: consecutive members differ by 2 and i+5, i+9 = i+1 differ by 4, so Q_i
 is independent and m(Q_i) = 3. Q_i u {i} has the maximal intervals {i,i+1}, {i+3}, {i+5} (the runs i+2, i+4, i+6, i+7
 are missing), so m = 3. Both lie in Fp. Define theta_i := U'(Q_i u {i}) - U'(Q_i). By Lemma 9(d) every pair
 (P, P u {i}) in Cl has difference theta_i; theta_i = hh_i (mod 7), theta_i = sigma_i (mod 2), |theta_i| <= 4; and by
 Lemma 9(e) theta_e is a nonzero even integer for every empty run e.
(F2) Connectivity of Fp. Call P, P' in Fp neighbours if they differ in exactly one run.
 (a) If P in Fp has a maximal interval [x,y] with x != y, then P\{y} is in Fp. Repeating, every P in Fp is joined to an
     independent set of 3 runs.
 (b) For an independent V = {v_1,v_2,v_3} in cyclic order let g_j >= 1 be the number of runs strictly between v_j and
     v_(j+1) (v_4 := v_1); g_1+g_2+g_3 = 5. If g_j >= 2, then V u {v_(j+1)-1} is in Fp (intervals {v_(j+1)-1, v_(j+1)}
     and two singletons; v_(j+1)-1 is not adjacent to v_j), and so is the independent set (V\{v_(j+1)}) u {v_(j+1)-1},
     whose gaps are those of V with g_j lowered and g_(j+1) raised by one. Symmetrically, through V u {v_j+1}, one unit
     moves from g_j to g_(j-1).
 (c) While g_1 >= 2, move one unit from gap 1 to gap 2 and then from gap 2 to gap 3; then, while g_2 >= 2, move one unit
     from gap 2 to gap 3. Every donor is >= 2. This ends with gaps (1,1,3), i.e. V = {x,x+2,x+4}.
 (d) From {x,x+2,x+4}: move x+4 to x+5 (gap ahead 3), then x+2 to x+3 (gap ahead 2), then x to x+1 (gap ahead 2). The
     result is {x+1,x+3,x+5}. So all members of Fp are joined.
(F3) f0 = 0. By the lift framework and (F2), f is a constant f0 on Fp. Let P1 := {0,3,6} and P2 := {1,4,7}. Both are
 independent (steps of 3; the wrap gaps hold run 7, respectively run 0), so they lie in Fp; they are disjoint. Their
 union {6,7,0,1} u {3,4} has the two maximal intervals {6,7,0,1} and {3,4} (runs 2 and 5 are missing), so
 m(P1 u P2) = 2 and P1 u P2 is in Cl (it is not in Fp). The set P3 := (P1 u P2)\{7} = {0,1,3,4,6} has the maximal
 intervals {0,1}, {3,4}, {6}, so P3 is in Fp, and (P3, P3 u {7}) is a pair in Cl; hence f(P1 u P2) = f(P3) = f0.
 Lemma 9(b) gives U'(P1 u P2) = U'(P1)+U'(P2); Theta is additive, so f(P1 u P2) = f(P1)+f(P2), i.e. f0 = 2f0, and
 f0 = 0: U'(P) = Theta(P) for every P in Fp.
(F4) Independent pairs. Let J = {j,j'} be independent. Its complement has 6 runs in two gaps, so some gap holds g >= 3
 runs; if it follows j, then x := j+2 has distance 2 from j and distance g-1 >= 2 from j', so J u {x} is an independent
 set of 3 runs, in Fp. (J, J u {x}) is a pair in Cl, so f(J) = f(J u {x}) = 0:
   U'(J) = Theta(J) for every independent pair J.                                                        (F4)
(F5) Total. Q0 := {0,2,4} is independent (runs 5, 6, 7 separate 4 from 0), and Q0^c = {1,3,5,6,7} has the maximal
 intervals {1}, {3}, {5,6,7}. Both lie in Fp, so f = 0 on both, and Lemma 9(c) gives
   Theta(all runs) = U'(Q0) + U'(Q0^c) = B* - 2nu0 - 14.                                                 (F5)

Proof of Theorem P7L-2. Assume an avoider w as in Sec. 0 and fix a frame for its NF word u (Sec. 1). For
S in {S_ev,S_od} (four pairwise non-adjacent runs each) order the theta-values on S as theta_(1) >= ... >= theta_(4)
(ties broken arbitrarily) and let J_S be the two runs carrying theta_(1), theta_(2). J_S is an independent pair, so
m(J_S) = 2 and Theta(J_S) = U'(J_S) by (F4); the two runs of S \ J_S have theta <= theta_(2).
CLAIM. Theta(S) <= -3-nu0, except when nu0 >= 1 and letters(J_S) = A; in that case Theta(S) <= -2-nu0.
Proof. If letters(J_S) != A, then X^(J_S) is two-signed or all negative (Lemma 5(c)), and Lemma 2.2 gives
 Theta(J_S) = U'(J_S) <= -1-nu0 <= -1. Then theta_(2) <= -1 (otherwise theta_(1), theta_(2) >= 0), and
 Theta(S) <= (-1-nu0) + 2theta_(2) <= -3-nu0.
 If letters(J_S) = A and nu0 >= 1, Lemma 2.2 gives Theta(J_S) <= -nu0 <= -1; as before theta_(2) <= -1 and
 Theta(S) <= -nu0-2.
 If letters(J_S) = A and nu0 = 0, then A is empty, so both runs of J_S are empty and their theta-values are nonzero even
 integers ((F1)). Theta(J_S) <= -nu0 = 0. If theta_(2) > 0, then theta_(1), theta_(2) >= 2 and Theta(J_S) >= 4 > 0,
 which is impossible; so theta_(2) <= 0, hence theta_(2) <= -2, and Theta(S) <= 0 + 2(-2) = -4 <= -3-nu0. []
The exception cannot hold for both sets: letters(J_(S_ev)) = A = letters(J_(S_od)) with disjoint J's forces A to be
empty, i.e. nu0 = 0. Adding the CLAIM over S_ev and S_od, which partition the runs, and using (F5):
   B* - 2nu0 - 14 = Theta(all runs) <= (-3-nu0) + (-2-nu0) = -5-2nu0,
so B* <= 9 < 10 = R. This contradicts B* >= R (Sec. 1, Quantities). Every step used only NF, the frame inputs and
Lemma 1 for the avoider u. So no such u exists, and hence no avoider w as in Sec. 0 exists. []
Which inputs carry the weight in Sec. 2. The empty-run rule enters only through (F1)/Lemma 9(e) in the case nu0 = 0; the
placement of the extra reflection pairs enters only through Lemma 1 (C_max = 2H+2m); nonempty runs, o_F and rotation
pairs are never assumed; the all-rotations-equal sub-case needs no separate treatment.

## 3. Cell (1,7): proof of Theorem P7L-1

Here kappa = 1: R = 8, t = 0, every label is an a-label (b_l > 0), A = letters(P0), 14-R = 6, M0 >= 1. Windows (Lemma 2):
Win_1 = [2,8] = [2,R] and Win_2 = Win_3 = [0,8] = [0,R]. Let G := {P : m(P) in {1,2,3}}; since m(P) = 4 only for S_ev
and S_od, G consists of all proper nonempty sets of runs other than S_ev and S_od, and P^c is in G whenever P is.

LEMMA 3.1 (realisation at m in {1,2,3}). Let P be in G and v an even integer in [-nu(P),Pi(P)].
 (i) If m(P) in {2,3}, v is realised at P.
 (ii) If m(P) = 1 and X^(P) is two-signed, v is realised at P.
 (iii) If m(P) = 1 and letters(P) = A, every even v in [2,B*] is realised; if m(P) = 1 and letters(P^c) = A, every even v
      in [-B*,-2] is realised.
Proof. By Lemma 5(b) some J has signed sum v, and |J| is even. (i) |J| lies in [0,8] = Win_(m(P)). (ii) If v != 0, J is
nonempty, so |J| lies in [2,8] = Win_1. If v = 0, the set Z0 of Lemma 7 has signed sum 0 and |Z0| in [2,6]. (iii) For
v != 0, J is nonempty and |J| lies in [2,8]. []
LEMMA 3.2 (windows on G). Every P in G satisfies Lemma 8 with: x = y = (nu(P) mod 2) in cases (i) and (ii) of Lemma 3.1;
(x,y) = (2,0) if m(P) = 1 and letters(P) = A; (x,y) = (0,2) if m(P) = 1 and letters(P^c) = A. So Lemma 9 applies to G;
B* <= 12; and U'(P) <= -1-nu0 for every P in G, except U'(P) <= -nu0 when m(P) = 1 and letters(P) = A.
Proof. As for Lemma 2.2: in cases (i), (ii) the realised values are all even v in [-nu(P),Pi(P)], with extreme values
-nu(P)+x and Pi(P)-x, x = nu(P) mod 2; if letters(P) = A, sigma(P) = -nu0 and the shifted range is [2-nu0,Pi0]; if
letters(P^c) = A, sigma(P) = Pi0 and the shifted range is [-nu0,Pi0-2]. Then hi(P) = x-2 is -2 or -1 in cases (i), (ii),
0 if letters(P) = A, and -2 if letters(P^c) = A. []

(G1) Theta. For a run i, {i+2} (m = 1) and {i,i+2} (independent, m = 2) lie in G; define
 theta_i := U'({i,i+2}) - U'({i+2}). By Lemma 9(d) every pair (P, P u {i}) in G has difference theta_i;
 theta_i = hh_i (mod 7), theta_i = sigma_i (mod 2), |theta_i| <= 6; and theta_e is a nonzero even integer for every
 empty run e (Lemma 9(e)).
(G2) Connectivity of G. If P in G has a maximal interval [x,y] with x != y, then P\{y} is proper, nonempty and has the
 same number of maximal intervals, so it lies in G. Repeating joins P to an independent set V in G with |V| = m(P) in
 {1,2,3}; removing members of V one at a time (each intermediate set is independent with at least one run) joins V to a
 singleton. Two singletons {a}, {a+1} are joined through {a,a+1} (m = 1). So G is connected.
(G3) f0 = 0. By the lift framework and (G2), f is a constant f0 on G. The sets {0}, {2} and {0,2} lie in G, and Lemma
 9(b) gives U'({0,2}) = U'({0})+U'({2}), i.e. f0 = 2f0. So f0 = 0:
   U'(P) = Theta(P) for every P in G; in particular theta_i = U'({i}) for every run i.                     (G3)
(G4) Total. {0} and its complement {1,...,7} (an arc, m = 1) lie in G, so Lemma 9(c) and (G3) give
   Theta(all runs) = U'({0}) + U'({1,...,7}) = B* - 2nu0 - 14 >= R - 2nu0 - 14 = -6 - 2nu0.               (G4)

Proof of Theorem P7L-1. Assume an avoider w as in Sec. 0 and fix a frame for its NF word u (Sec. 1). By (G3) and Lemma 3.2,
theta_i = U'({i}) <= -1-nu0 for every run i, except theta_i <= -nu0 when letters({i}) = A.
 Case nu0 >= 1. A is nonempty, and distinct runs have disjoint letter sets, so letters({i}) = A for at most one run i.
 Hence Theta(all runs) <= 7(-1-nu0) + (-nu0) = -7-8nu0. With (G4): -6-2nu0 <= -7-8nu0, i.e. 6nu0 <= -1, impossible.
 Case nu0 = 0. A is empty. If run i is empty, then letters({i}) = A, so theta_i <= 0, and theta_i is a nonzero even
 integer by (G1); hence theta_i <= -2. If run i is nonempty, letters({i}) != A and theta_i <= -1. Hence
 Theta(all runs) <= -8 < -6 <= Theta(all runs) by (G4), impossible.
Every step used only NF, the frame inputs and Lemma 1 for the avoider u. So no such u exists, and hence no avoider w as in
Sec. 0 exists. []
Which inputs carry the weight in Sec. 3. The light side enters through M0 >= 1 (Lemma 9(b)); the empty-run rule only in
the case nu0 = 0; the placement of the extra reflection pairs only through Lemma 1; nonempty runs, o_F and rotation pairs
are never assumed; the all-rotations-equal sub-case needs no separate treatment.

## 4. Route remarks, the parent exposure, failed or unused routes (no claims beyond Theorems P7L-1 and P7L-2)

(M1) kappa = 2. Since 7 = 4*2-1, the windows Win_2 = [2,R] and Win_3 = [0,R-2] are those of the FCW pattern, and Sec. 2
 re-derives that pattern at p = 7 (FCW itself is accepted only for kappa >= 3). The FCW additive pair
 {0,3,...,3kappa}, {1,4,...,3kappa+1} needs kappa-2 >= 1 separating runs at the wrap; at N = 8 its union
 {6,7,0,1} u {3,4} has m = 2 instead of 3. That union still lies in Cl, and (F3) joins it to Fp by deleting run 7. The
 parent's untrusted suggestion (the all-m = 2 triple {0,3}, {1,4}, {0,1,3,4}) would also work once f is known on those
 sets ({0,3}, {1,4} by (F4); {0,1,3,4} through {0,1,3,4,6} in Fp); it is not used.
(M2) kappa = 1. Win_1 = [2,R]: for a two-signed singleton every even signed value is realised (v = 0 by a zero-signed
 set Z0 of Lemma 7), so singletons get the same representative window as full sets. Putting m = 1 into the lift family G
 makes every theta_i equal to a representative U'({i}) <= -1-nu0, and summing over all eight runs leaves a slack of
 2+6nu0 against at most one exceptional unit. The parent's untrusted note (full m = 2 window; tight alternating-set
 sorting forcing unit labels; a possible theta = 0) describes the route that sorts the top two runs of each alternating
 set; that route gives at best B* <= R, i.e. a tight case needing separate analysis. Sec. 3 does not use it; a value
 theta = 0 matters only for empty runs, where Lemma 9(e) excludes it.
(M3) Margins at p = 7: pair-independence of theta needs 2(14-R) < 14 (12 for kappa = 1, 8 for kappa = 2); complements
 need 28-2B* < 14 (B* >= 8); additivity needs M0 >= 1, supplied by the light side (Lemma 6).
Failed or unused routes (kept; not premises).
(R1) kappa = 1, sorting the top two runs of each alternating set: B* <= R only (see (M2)).
(R2) kappa = 2, an FCW-form triple with all three sets in Fp: not available at N = 8 (see (M1)).
(R3) PL's Theorem K1 (p >= 11; it uses Theorem P and B0S-CJ''') and every other lemma accepted only for p >= 11: not
 available at p = 7 and not used.

## 5. Scope

Claimed: Theorem P7L-2 and Theorem P7L-1, i.e. at p = 7 the terminal cells k = 8 with kappa_hat = 2 and with
kappa_hat = 1 are excluded under the full existential-NF/word antecedent (some admissible NF, extra reflection pairs
anywhere in the odd blocks, genuine empty-run rule). Lemmas 1-9, 2.1-2.2, 3.1-3.2, (F1)-(F5) and (G1)-(G4) are proved
only at p = 7, k = 8, kappa in {1,2}, in the frame of Sec. 1.
NOT claimed: kappa_hat = 0 (the separate K0T verdict) and kappa_hat = 3 (the separate R7 verdict) are not re-proved;
every other kappa_hat at p = 7; nonterminal k at p = 7; the whole of p = 7; any p != 7 (in particular neither the
kappa = 1 singleton route nor the kappa = 2 route is claimed for any other prime); reflection rigidity; INV*; o_F
assembly; full ordered Olson; any multiset-only statement outside the antecedent; novelty, priority, "first", Lean or
human review. No FCW, SCW, USK, K1, K2, K3, R7 or TCW statement is extended or used as a premise.

## 6. Interface table

Aroot=/Users/jinleic/repos/aifours; R16=Aroot/institute/runs/six-lane-2026-10-16/review;
R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review;
ROT=Aroot/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation;
FBP=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/evidence;
CONT=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations.
| Input | Path; whole-file SHA256 | LF lines | Scope; use here |
|---|---|---|---|
| NF | ROT/proof-ROT-few-E-v4.md; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | 28-43 | Sec. 0 normal form: some admissible NF, all blocks odd, empty-run rule, H = (F-k)/2, kappa = p-1-H, R = 2p+2kappa-k (line 42); used at p = 7 as in the accepted R7 and K0T verdicts |
| GRX | ROT/notes-GRX-v1.md; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | 7-20 | if-direction; Lemma 1 |
| SC0 | R16/olson-index-one-primary-statement-parent-v1.md; e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6 | 1-11 | 1-element basis of a minimal zero-sum sequence of length >= floor(n/2)+2 over C_n, n >= 3; applied to Y'z with n = 14 (Lemma 3(c)) |
| ZSTRUCT, FB in (S') | R18/olson-FB-parent-verdict-v1.md 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a (1-16); FBP/proof-FB-v1.md 339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b (9-24); FBP/proof-FB-v1-erratum-1.md 33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202 (1-7, no statement change); (S') extension R18/olson-balfull-rotzb-parent-verdict-v1.md 56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0 (26-34) | as listed | Lemma 3(d), only t = 1 at (k',kappa') = (6,1): Z-shape, n- >= 1, balance, W+n+ <= 13. FB-E NOT used |
| (S1) definition | R16/olson-zx-s1c-parent-verdict-v1.md; 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af | 19 | the definition "(S1) bounds every zero-sum length by 2kappa" only; S1(a) NOT used (Lemma 3(b) is direct) |
| LOWER parent erratum | R18/olson-LOWER-parent-erratum-v1.md; 087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377 | 1-10 | m(P) = half the sign transitions (LF7); theta only through explicit pairs (LF6) |
| FCW parent erratum | R18/olson-FCW-parent-erratum-v1.md; e56bf0f337d7d670be99075829217431cf605437320dd3414cde75c3d1ae2413 | 1-14 | derivation patterns only: (SR) from NF + GRX (m4, LF8), redone in Lemma 1; the SC0 reading through Y'z (m3, LF7), redone in Lemma 3(c); no FCW lemma is a premise |
| R7 verdict | R18/olson-R7-parent-verdict-v1.md; b83058b2ed220d663da2e6906954572a5b3fbfe32d97f1c36317a2e87cf796f1 | 1-23 | context: LF5 records Sec. 0 NF and the GRX if-direction as accepted imports at the literal antecedent p = 7; no R7 lemma used |
| K0T verdict | R18/olson-K0T-parent-verdict-v1.md; 4a2a2ffd8d8624c33c0f7cc1265cf679c18ac3a9c63565bc093b2e8afc8bf8ba | 1-20 | context: LF5 applies NF at p = 5, 7 (kappa_hat = 0 cell); no lemma used |
| context only | R18/olson-FCW-parent-verdict-v1.md b28837c9c8a9549b99a6c2205e8bbe40d65ab1aad265595c511395d4c1738f71 (1-24); R18/olson-SCW-parent-verdict-v1.md d51b5d8e6c6a7c38047434b3740d477bccd2ab7e0e53ce68ea34aa83486bdfe0 (1-26); R18/olson-USK-parent-verdict-v1.md 6d3358ce3f1e9e95a366f2b32f10adbc73df607bc62723f561567dce1a53de18 (1-30); R18/olson-LOWER-K1-parent-verdict-v1.md 93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83 (1-22) | as listed | not premises |
| untrusted | CONT/lowerhalf-third-cut-window/proof-TCW-v1.md 62c747911239c32998d2ec2b3bd9ec538eee5e523f68b92233aa06e890f85713; CONT/lowerhalf-first-cut-window-boundary/proof-FCW-v1.md c23fd0378f68611070e3bf0fd74d66d1f7ad859bb01ccc1af4ce9a77cf4aaecf; CONT/lowerhalf-second-cut-window/proof-SCW-v1.md 6a1965aecf599e00b512ca1df36127d21e5bac21bea7ac0da5804092245f3650 | whole | methods only, re-derived at p = 7; never premises |
Not used: PL (proof-LOWER-v1.md 251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d, accepted only for
p >= 11) in its entirety, including its (SR), IF, LT, D, SS, U, A, C and THETA; Theorem P; B0S-CJ'''; S1(a); the Setting
fact; FB-E; every FCW, SCW, USK, K1, K2, K3, R7 and TCW lemma; P11R and every other unreviewed candidate.
Machine steps for this file: /bin/date, shasum -a 256, wc -c -l, reading files, and one exclusive creation (Python
open(path,'x')) of this text, drafted by hand in memory in six parts with one rewording replacement (Lemma 2.1(ii)) before creation; no
assertion of any kind and no check over mathematical objects.
