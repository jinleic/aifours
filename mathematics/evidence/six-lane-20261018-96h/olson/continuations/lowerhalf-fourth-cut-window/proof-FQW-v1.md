# FQW: fourth cut window p = 4kappa-7 (kappa >= 5): the lower-half terminal cell kappa_hat = kappa is excluded, v1

Owner OlsonThirdCutWindow (same math2 slot). Drafted by hand after /bin/date 2026-10-20T06:55:19-0700. Status:
CANDIDATE_UNVERIFIED written proof of the FULL frozen target (FQW-scope-v1.md SHA256
97cbf46c970eca6e576b349f889cace799d33aec9bf37c268fbc1d17d604ba3d, frozen 2026-10-20T06:26:24-0700 before any derivation;
authority RUN/control/written-olson-fourth-cut-window-transition-v1.json SHA256
21fac2252ccfd0127c898b09aab83a63cd252d0283c0d391cafd3dae8f61327b). Outcome: PROVED, no failing lemma. The cell
(kappa,p) = (5,13) is covered (Secs. 5-6); (6,17) is written out in Sec. 6. LABELLED PARTIAL of ordered Olson: one family
of terminal lower-half cells. All case work is by hand; no script, assertion, enumeration or computation over scientific
data. No novelty, priority, Lean or human-review claim; no other cell; no full ordered Olson.

## 0. Statement

THEOREM FQW. Let kappa >= 5 be an integer such that p = 4kappa-7 is prime (deficiency delta := 4kappa-p-1 = 6; e.g.
(kappa,p) = (5,13), (6,17), (9,29), (11,37), (12,41)). No word w of length 4p-2 over D_(2p) without an identity 2p-subword in
increasing original index order has an admissible normal form (NF) with terminal k = p+1 and kappa_hat = kappa. Full
antecedent: SOME admissible NF; the H = p-1-kappa extra reflection pairs lie anywhere in the odd blocks; every empty NF run
separates different reflection values; no o_F, nonempty-run, rotation-pair or reflection-rigidity hypothesis on w. In
particular the whole cell (kappa_hat,p) = (5,13) is excluded.
Route. Sec. 1: (SR) from NF + GRX, windows, frame (SC0, ZSTRUCT/FB), label counts (u1 >= |b|+9), margin M0 >= 2kappa-1.
Sec. 2: minimal representations missing at most six letters are single-signed; exact candidate-exception lists for the
windows [2,R-6] (m = kappa), [0,R-8] (m = kappa+1) and the self-dual window [4,R-4] (m = kappa-1). Sec. 3: representative
windows with (lambda,mu) tables. Sec. 4: lift framework on all sets with m in {kappa-1,kappa,kappa+1}: pair-independent
theta through two couplings, connectivity, an all-(kappa-1) additive triple (valid at N = 14), complements. Sec. 5:
sorting the TOP kappa-1 runs of each alternating set of 2kappa-3 runs, with the exceptional types P and Q, the empty-run
evenness, and a two-sided "no empty alternating set" lemma.
Exposure. Before the freeze I had derived the unaccepted TCW (delta = 4) and P7L candidates and read FCW, SCW and their
inputs; the transition disclosed the parent's untrusted notes. No TCW, P7L, FCW, SCW or USK lemma is a premise; every step
is re-derived at p = 4kappa-7 from the literal NF, GRX, SC0 and ZSTRUCT/FB interfaces (Sec. 8).

## 1. Setting, windows and frame

Throughout p = 4kappa-7 is prime and kappa >= 5. There are N = p+1 = 4kappa-6 runs (N even) and R = p-1+2kappa = 6kappa-8
rotation letters (R even, R >= 22); H = 3kappa-8, F = 3p-1-2kappa = 10kappa-22, 2p = 8kappa-14. Hence 2p-R = 2kappa-6,
2p-1-R = 2kappa-7, 2R-2p = 4kappa-2, 2p-2kappa = R-6.
Word form [NF lines 28-43; GRX]. The NF word u is an avoider of length 4p-2 with the rotation multiset of w. Read it
cyclically as R_0 S_0 R_1 S_1 ... R_p S_p: run R_i has r_i >= 0 letters, S_i = sigma_(y_i)^(l_i) with l_i odd and
sum (l_i-1)/2 = H (NF line 42: H = (F-k)/2, kappa = p-1-H, R = 2p+2kappa-k), and an EMPTY run R_i has y_(i-1) != y_i
(indices mod N). Put tau_i := y_i - y_(i-1) in Z_p (sum 0). For a set P of runs, m(P) is half the number of sign
transitions of the pattern (-1 on P, +1 off P) (LOWER parent erratum): m(empty) = m(all runs) = 0, a proper nonempty P has
m(P) equal to its number of maximal cyclic intervals, and m(P^c) = m(P). T(P) := sum_(i in P) tau_i; X^(P) is the list of
letter values with every letter of a run of P negated; letters(P) =: L(P) is the set of letters lying in runs of P; L_i :=
L({i}), r_i = |L_i|. A set of runs is independent if its members are pairwise non-adjacent (mod N); a proper independent
set of j >= 1 runs has m = j.

LEMMA 1 ((SR)) [NF, GRX if-direction; the derivation of the FCW parent erratum m4]. For every set P of runs and every even
n with max(0,2kappa+2-2m(P)) <= n <= min(R,2p-2m(P)), T(P) is not a sum (in Z_p) of n letters (distinct occurrences) of
X^(P). Write Win_m for this set of n when m(P) = m.
Proof. GRX applies to the cyclic NF representation of u, with GRX's z_i the sign of run R_i and its theta_i = y_(i-1)-y_i =
-tau_i. Take z_i = -1 iff i is in P. Then X^z = X^(P) and T(z) = sum_(i not in P) theta_i = T(P) (sum_i tau_i = 0).
Phi = sum_i [z_i != z_(i+1)] = 2m(P). Every l_i is odd, so delta_GRX = #{i : f_i = 0} = N-2m(P) and C_max = F-delta_GRX =
2H+2m(P) (F = N+2H). GRX: an even C with 2m(P) <= C <= 2H+2m(P), 0 <= 2p-C <= R and T(P) in Sigma_(2p-C)(X^(P)) would give
an identity 2p-subword of u. With n := 2p-C these conditions read: n even, 2kappa+2-2m(P) <= n <= 2p-2m(P) (2p-2H =
2kappa+2), 0 <= n <= R. u is an avoider. []

LEMMA 2 (windows; sets of even integers). Win_0 = [2kappa+2,R], Win_1 = [2kappa,R], Win_(kappa-1) = [4,R-4],
Win_kappa = [2,R-6], Win_(kappa+1) = [0,R-8].
Proof. 2kappa+2 <= R and 2p-2 = 8kappa-16 >= R (kappa >= 4); 2kappa+2-2m = 4, 2, 0 and 2p-2m = R-4, R-6, R-8 for
m = kappa-1, kappa, kappa+1. []

LEMMA 3 (frame).
(a) [pigeonhole] The N block values lie in Z_p, so y_c = y_c' for some c != c'. The arc P0 := runs c+1,...,c' is proper and
 nonempty with T(P0) = 0; its complementary arc C0 has T(C0) = 0; m(P0) = m(C0) = 1.
(b) [direct] Let Y be the sequence of the R elements (1,x) of Z_2 x Z_p = C_(2p), one for each letter x of X^(P0). A
 zero-sum of Y of length n is a set of n letters with X^(P0)-sum 0 = T(P0); n is even and n <= R. Lemma 1 at P0 excludes
 every even n in Win_1 = [2kappa,R]. So every zero-sum of Y has length <= 2kappa-2.
(c) [SC0, through Y'z] Let Z be a LONGEST zero-sum of Y, |Z| = 2t with 0 <= t <= kappa-1. Y' := Y - Z is zero-sum free (a
 nonempty zero-sum of Y' with Z would be longer) of length L = R-2t >= 6kappa-8-2(kappa-1) = 4kappa-6 = p+1. z := -sigma(Y')
 is nonzero, and Y'z is a minimal zero-sum sequence (a nonempty proper zero-sum subsequence T of Y'z gives the nonempty
 zero-sum T, if z is not in T, or Y'z - T, if z is in T, inside Y'). Its length is L+1 >= p+2 = floor(2p/2)+2 and 2p >= 3,
 so by SC0 it has a 1-element basis {g}: every term is x*g with least positive coefficient x, and the coefficients sum to
 ord(g). There are L+1 >= p+2 coefficients, each >= 1, so ord(g) >= p+2, i.e. ord(g) = 2p. So Y' = (a_1 g)...(a_L g) with
 least positive coefficients a_i and W := sum a_i = 2p - x(z) <= 2p-1. Write g = (g_1,gamma). Every term of Y' is odd, so
 g_1 = 1 and every a_i is odd; gamma != 0 because g generates.
(d) [ZSTRUCT, FB in (S')] If t = 0, put n+ = n- = 0. If t >= 1, then Y lies in setting (S') with (k',kappa') =
 (p-1,kappa-1): p >= 5 is prime; 1 <= k' <= p-1; kappa' is an integer with 1 <= kappa' < p; Y consists of
 2p+2kappa'-k' = p+2kappa-1 = R odd elements; every zero-sum of Y has length <= 2kappa' ((b), i.e. (S1) at kappa'); Z is
 longest with t <= kappa'; L = R-2t >= 2p-k' = p+1; and g is an index-<1 generator of Y-Z. ZSTRUCT (accepted in (S')
 through its proof) gives Z = g^(n+) (-s_1 g)...(-s_(n-) g) with odd s_j >= 1, n+ + n- = 2t, n- >= 1 and
 s_j <= 2t-1; Lemma FB gives sum_j s_j = n+ and W + n+ <= 2p-1. Hence n- <= n+ (each s_j >= 1), n- <= t <= kappa-1,
 n+ >= t, and s_j <= n+ - (n- - 1) <= n+. In both cases W + n+ <= 2p-1.
(e) [labels] Each letter l gets an odd integer label b_l with X^(P0)-value b_l*gamma: the a-labels for Y', +1 for the n+
 terms g of Z and -s_j for the others. E := W-L = sum_i (a_i-1) >= 0 is even; m1 := #{i : a_i = 1};
 u1 := #{l : |b_l| = 1} >= m1 + n+.

LEMMA 4 (label counts). (i) E <= 2kappa-7+n- <= 3kappa-8. (ii) a_i <= 1+E <= 3kappa-7 and s_j <= min(n+, 2kappa-3).
(iii) m1 >= (10kappa-9-5t)/2 >= (5kappa-4)/2. (iv) If some a_i equals b >= 3, then m1 >= (10kappa-12-5t+b)/2.
(v) u1 >= |b_l| + 9 for every letter l; more precisely u1 >= b+2kappa-1 for an a-label b >= 3, u1 >= s_j + m1 for a label
-s_j, and u1 >= (7kappa-6)/2 in all cases.
Proof. (i) L = R-n+-n- and W <= 2p-1-n+, so E <= 2p-1-R+n- = 2kappa-7+n-, and n- <= kappa-1. (ii) a_i-1 <= E; s_j <= n+
and s_j <= 2t-1 <= 2kappa-3 (Lemma 3(d)). (iii) Each a_i > 1 adds at least 2 to E, so L-m1 <= E/2 and
m1 >= (6kappa-8-2t) - (2kappa-7+t)/2 = (10kappa-9-5t)/2 >= (5kappa-4)/2 (t <= kappa-1). (iv) That a_i adds b-1, every
other a-label > 1 at least 2: L-1-m1 <= (E-b+1)/2, so m1 >= (6kappa-9-2t) - (2kappa-6+t-b)/2 = (10kappa-12-5t+b)/2.
(v) u1 >= m1+n+ >= m1+t. For an a-label b >= 3: u1 >= (10kappa-12-3t+b)/2 >= (7kappa-9+b)/2, and b <= 3kappa-7 gives
u1-b >= (7kappa-9-b)/2 >= 2kappa-1 >= 9. For -s_j: u1 >= m1+n+ >= m1+s_j and m1 >= (5kappa-4)/2 > 10. For |b_l| = 1:
u1 >= (10kappa-9-3t)/2 >= (7kappa-6)/2 >= 14.5. []

Normalisation. (v,eps) -> (gamma^(-1)v,eps) is an automorphism of D_(2p) (multiplication by a unit of Z_p commutes with
v -> -v); applied letterwise it preserves identity subwords, the run/block structure with the empty-run rule and Lemma 1,
with tau_i and all values scaled by gamma^(-1), and carries the frame along with the same labels. So take gamma = 1. Put
c_l := b_l for l in C0 and c_l := -b_l for l in P0. The original value of l is c_l (mod p), and its value in X^(P) is
eps_l c_l, where eps_l = -1 iff l lies in a run of P.
Light side. Let o(Q) := #{l in L(Q) : b_l = 1}. Letters of C0 with b = 1 have c = 1, letters of P0 with b = 1 have c = -1.
If o(C0) >= kappa+1 and o(P0) >= kappa+1, then kappa+1 of each have original values summing to 0 = T(empty), with
2kappa+2 in Win_0; Lemma 1 at P = empty forbids this. Exchanging P0 and C0 keeps Lemmas 3-4 with the same labels (C0 is a
proper arc with T(C0) = 0, X^(C0) = -X^(P0), its sequence is -Y, the zero-sums of -Y are those of Y, Z stays longest, and
-g is an index-<1 generator of -Y' with the same coefficients). Fix P0 with q1 := o(P0) <= kappa and normalise.
Quantities. A := {l : c_l < 0}, A^c := {l : c_l > 0}. Pi0 := sum over A^c of |c_l|, nu0 := sum over A of |c_l|,
B* := Pi0+nu0 = sum_l |b_l| = W+2n+ = R+E+n+-n-; B* is even (R odd terms, R even), B* >= R, and e* := B*-R >= 0.
sigma(P) := sum of c_l over L(P); X_i := sum of the original values of run i, so X_i = sigma({i}) =: sigma_i (mod p);
hh_i := tau_i+X_i and Hh(P) := sum_(i in P) hh_i = T(P)+sigma(P) (mod p).
Frame quantifier. Lemmas 3-4 and the light side hold for EVERY admissible choice of P0, Z, g and light side; the proof fixes
one such frame, and one always exists.

LEMMA 5 (density, signed sums, negative letters).
(a) Every integer of [0,B*] is a sum of a sub-multiset of {|c_l|}.
(b) Fix P. Let Pos(P), Neg(P) be the letters with eps_l c_l > 0 and < 0, q(P) := |Neg(P)|, q'(P) := |Pos(P)| = R-q(P),
 Pi(P) := sum over Pos(P) of |c_l|, nu(P) := sum over Neg(P) of |c_l|. The signed sums sum_(l in J) eps_l c_l over sets J
 of letters are exactly the integers of [-nu(P),Pi(P)], each with the parity of |J|; Pi(P) = Pi0-sigma(P),
 nu(P) = nu0+sigma(P); nu(P) has the parity of q(P), and Pi(P) that of q'(P).
(c) Neg(P) = L(P) symdiff A; so q(P) = |L(P) symdiff A|, q'(P) = |L(P) symdiff A^c|, and q(P^c) = q'(P).
(d) |A^c| >= (5kappa-6)/2 >= 10 and |A| <= nu0.
Proof. (a) There are u1 ones and every element is <= u1+1 (Lemma 4(v)); order the elements > 1 increasingly with prefix
sums D_0 = 0 <= D_1 <= ...; every D_j+i (0 <= i <= u1) is a subset sum and D_(j+1)-D_j <= u1+1, so [0,B*] is covered.
(b) J -> (J n Pos(P)) u (Neg(P) \ J) is a bijection with sum_J eps_l c_l = sum_(image)|c_l| - nu(P); apply (a) and
Pi(P)+nu(P) = B*; the terms are odd; Pi(P)-nu(P) = (Pi0-nu0)-2sigma(P). (c) A letter of a run of P has value -c_l,
negative iff l is in A^c; any other letter has value c_l, negative iff l is in A; L(P^c) is the complement of L(P).
(d) The letters with b = 1 are at least m1+n+ >= m1+t >= (7kappa-6)/2 (Lemma 4); at most q1 <= kappa of them lie in P0 and
all others have c = 1. Every |c_l| >= 1. []

LEMMA 6 (lift margin). M0 := 2Pi0+nu0-2p >= 2kappa-1+E/2 >= 9.
Proof. A letter with c < 0 is one of the q1 <= kappa letters of P0 with b = 1, a letter of P0 with an a-label B >= 3
(B <= (3/2)(B-1), the numbers B-1 summing to at most E), or a letter of C0 with label -s_j (these sum to at most n+). So
nu0 <= q1 + 3E/2 + n+, and M0 = 2B*-nu0-2p >= (2R-2p) + E/2 + n+ - 2n- - q1 >= 4kappa-2 + E/2 - n- - kappa
>= 2kappa-1+E/2 (n+ >= n-, n- <= kappa-1). []

## 2. Minimal representations and exception lists [NEW at delta = 6]

An even v is REALISED at P if v = sum_(l in J) eps_l c_l for some set J of letters with |J| in Win_(m(P)). X^(P) is
"two-signed" if q(P) >= 1 and q'(P) >= 1. U+ and U- denote the unit letters (|c| = 1) of value +1 and -1 in X^(P).

LEMMA 7 (minimal representations). Fix P and an even v in [-nu(P),Pi(P)]; let J have signed sum v with |J| minimal.
(a) |J| is even, and no nonempty subset of J has signed sum 0.
(b) If R-|J| <= 6, then J lies in Pos(P) or in Neg(P).
(c) If J lies in Pos(P) and R-|J| <= 6, then Pos(P) \ J consists of k' := R-q(P)-|J| unit letters; so v = Pi(P)-k' with
 q(P)+k' = R-|J| and k' = q(P) (mod 2). Symmetrically, if J lies in Neg(P), then v = -nu(P)+k' with
 q'(P)+k' = R-|J|, k' = q'(P) (mod 2).
Proof. (a) The terms are odd; removing a zero-signed nonempty subset would give a smaller J. (b) Let M be the letters
outside J, |M| <= 6; J contains at least u1-6 unit letters. Two of opposite values would be a zero-signed pair; so they
all have one value, say +1 (the case -1 is the negative). A letter of J of negative value has value -b with b >= 3, and J
contains at least u1-6 >= b+3 letters of value +1 (Lemma 4(v)); with b of them it is a zero-signed subset of J. So J lies
in Pos(P). (c) Neg(P) lies in M, so M' := Pos(P) \ J has k' = |M|-q(P) letters. If l in M' has |c_l| = x >= 3: Pos(P)
has at least u1-q(P) unit letters, at most k'-1 of them in M', so J contains at least u1-5 >= x of them; replacing x of
them by l keeps the signed sum and lowers |J|. So M' consists of unit letters; R and |J| are even. []

LEMMA 8 (zero-signed sets; enlargement for [4,R-4]).
(a) If X^(P) is two-signed, some set Z0 with 2 <= |Z0| <= 3kappa-6 has signed sum 0.
(b) Let J0 have signed sum v and |J0| <= 2. If min(q(P),q'(P)) >= 3, some J with signed sum v has 4 <= |J| <= R-4. If
 q(P) <= 2, the same holds unless (q(P),v) is (0,0), (0,2), (1,-nu(P)+1) or (2,-nu(P)); if q'(P) <= 2, unless
 (q'(P),v) is (0,0), (0,-2), (1,Pi(P)-1) or (2,Pi(P)).
Proof. (a) A pair of unit letters of opposite values, or else (all unit letters of one value, say +1) a letter of value
-b, b >= 3, with b letters of U+ (u1 >= b); its size is b+1 <= 3kappa-6 (Lemma 4(ii)).
(b) Two moves keep the signed sum: ADD a zero-signed set disjoint from J0 (a pair {u+,u-}, or a letter of value -/+b,
b >= 3, with b letters of U+ resp. U-; sizes 2 and b+1 in [4,3kappa-6]); INFLATE a letter of J0 of value +/-x, x >= 3,
into x unit letters of the same sign outside J0. Every result below has size in [4, 2+3kappa-6], inside [4,R-4].
 min(q,q') >= 3, |J0| = 0 (v = 0): if |U+|, |U-| >= 2, add two disjoint pairs; if |U-| <= 1, at least two negative letters
 are non-units, and one of them, value -b, with b letters of U+ (|U+| >= u1-1 >= b) is added; if |U+| <= 1, symmetric.
 min(q,q') >= 3, |J0| = 2: if U+ \ J0 and U- \ J0 are nonempty, add a pair. If U- \ J0 is empty, then |U-| <= 2, some
 negative letter lies outside J0 (q >= 3) and is a non-unit, value -b; add it with b letters of U+ \ J0
 (|U+ \ J0| >= u1-4 >= b). If U+ \ J0 is empty, symmetric (q' >= 3).
 q = 0: all values are positive. v = 0 and v = 2 are listed (their only sets are empty, resp. two unit letters). If
 |J0| = 2 and v >= 4, J0 contains a letter of value x >= 3: inflate it (u1-2 >= x).
 q = 1, with the negative letter l* of value -b*: if |J0| = 0 and b* >= 3, add l* with b* letters of U+; if |J0| = 0 and
 b* = 1, v = 0 = -nu(P)+1 is listed. If |J0| = 2 and l* is not in J0, add l* with b* letters of U+ \ J0. If J0 = {l*,l'},
 l' of value x > 0: inflate l' if x >= 3; if x = 1, v = -nu(P)+1 is listed.
 q = 2, with negative letters l1, l2 of values -b1, -b2: if |J0| = 0, add a non-unit l_i with b_i letters of U+, or, if
 both are units, add {l1,l2} with two letters of U+. If |J0| = 2 and some l_i is not in J0, add l_i with b_i letters of
 U+ \ J0 (|U+ \ J0| >= u1-4 >= b_i). If J0 = {l1,l2}, v = -nu(P) is listed.
 q' <= 2: apply the above to P^c (X^(P^c) = -X^(P), q(P^c) = q'(P)). []

LEMMA 9 (candidate-exception lists). Let P be proper and nonempty, v even in [-nu(P),Pi(P)], q = q(P), q' = q'(P); at most
one of q, q' is <= 6 (q+q' = R >= 22).
(a) m(P) = kappa+1 (Win = [0,R-8]). v is realised except possibly when q <= 6 and v = Pi(P)-k' with 0 <= k' <= 6-q,
 k' = q (mod 2), or q' <= 6 and v = -nu(P)+k' with 0 <= k' <= 6-q', k' = q' (mod 2).
(b) m(P) = kappa (Win = [2,R-6]). v is realised except possibly when q <= 4 and v = Pi(P)-k' (0 <= k' <= 4-q, k' = q), or
 q' <= 4 and v = -nu(P)+k' (0 <= k' <= 4-q', k' = q'), or v = 0 and q = 0 or q' = 0.
(c) m(P) = kappa-1 (Win = [4,R-4]). If min(q,q') >= 3, every v is realised. Otherwise v is realised except possibly:
 q = 0: v in {0, 2, B*-2, B*}; q = 1: v in {-nu(P)+1, Pi(P)-1}; q = 2: v in {-nu(P), Pi(P)};
 q' = 0: v in {0, -2, -B*+2, -B*}; q' = 1: v in {-nu(P)+1, Pi(P)-1}; q' = 2: v in {-nu(P), Pi(P)}.
Proof. Let J be minimal (Lemma 7). (a) If |J| <= R-8, v is realised; otherwise R-|J| <= 6 and Lemma 7(b),(c) apply.
(b) If 2 <= |J| <= R-6, v is realised. If |J| >= R-4, Lemma 7 applies with R-|J| <= 4. If |J| = 0, then v = 0, realised by
Z0 (Lemma 8(a)) when X^(P) is two-signed. (c) If 4 <= |J| <= R-4, v is realised. If |J| >= R-2, Lemma 7 gives
v = Pi(P)-k' with q+k' <= 2 or v = -nu(P)+k' with q'+k' <= 2: none if min(q,q') >= 3, and otherwise one of the listed
values. If |J| <= 2, Lemma 8(b). []

## 3. Representative windows [NEW at delta = 6]

LEMMA 10 (representatives). Fix a proper nonempty P. Suppose that for integers x, y >= 0 with x+y <= B*, and with -nu0+x
and Pi0-y of the parity of sigma(P), every integer of that parity in [-nu0+x, Pi0-y] equals v+sigma(P) for some v realised
at P. Then B* <= 2p-4+x+y, and some integer U(P) with U(P) = Hh(P) (mod p) and U(P) = sigma(P) (mod 2) lies in
[Pi0+1-lambda(P), 2p-1-nu0+mu(P)], where lambda(P) := y-1 and mu(P) := x-1.
Proof. By Lemma 1, T(P) != v (mod p) for every realised v (the X^(P)-values are eps_l c_l mod p). As
Hh(P) = T(P)+sigma(P) (mod p), Hh(P) is congruent to no integer of the parity of sigma(P) in [a,b], a := -nu0+x,
b := Pi0-y (b >= a since x+y <= B*). The p integers a, a+2, ..., a+2p-2 are pairwise incongruent mod p, so Hh(P) is
congruent to exactly one of them, a+2j, and a+2j > b, i.e. a+2j >= b+2 (same parity). If b >= a+2p-2 this is impossible,
so B*-x-y <= 2p-4, and a+2j lies in [b+2, a+2p-2] = [Pi0+1-lambda(P), 2p-1-nu0+mu(P)]. []
Notation. U'(P) := U(P)-2p, low(P) := Pi0+1-lambda(P)-2p, up(P) := -1-nu0+mu(P), so low(P) <= U'(P) <= up(P);
D0 := 2p-2-B* <= 2p-2-R = 2kappa-6-2 = 2kappa-8; up(P)-low(P) = D0+lambda(P)+mu(P).

LEMMA 11 (tables). Every P with m(P) in {kappa-1,kappa,kappa+1} satisfies Lemma 10 with (lambda,mu) as follows
(q = q(P), q' = q'(P); "else" means min(q,q') above the listed range, and then lambda = mu = (q mod 2)-1 in {-1,0}):
 m = kappa+1: q = s <= 6: (7-s, (s mod 2)-1); q' = s <= 6: ((s mod 2)-1, 7-s); else lambda = mu in {-1,0}.
 m = kappa:   q = 0: (5,1); q = 1: (4,0); q = 2: (3,-1); q = 3: (2,0); q = 4: (1,-1);
              q' = 0: (1,5); q' = 1: (0,4); q' = 2: (-1,3); q' = 3: (0,2); q' = 4: (-1,1); else lambda = mu in {-1,0}.
 m = kappa-1: min(q,q') = 0: (3,3); = 1: (2,2); = 2: (1,1); else lambda = mu in {-1,0}.
Consequences: (i) lambda+mu <= 6 and lambda, mu <= 7; so up(P)-low(P) <= D0+6 <= 2kappa-2 < 2p and U(P) is the UNIQUE
integer of [Pi0+1-lambda(P), 2p-1-nu0+mu(P)] with the two congruences (residues mod p and mod 2 fix the residue mod 2p).
(ii) (lambda,mu)(P^c) = (mu,lambda)(P) (q(P^c) = q'(P), and every table is symmetric under q <-> q', lambda <-> mu).
(iii) Per-set bounds: m = kappa+1: lambda <= (7-q)^+ and mu <= (7-q')^+; m = kappa: lambda <= (5-q)^+ + [q = R] and
 mu <= (5-q')^+ + [q' = R]; m = kappa-1: lambda = mu <= (3-min(q,q'))^+. In particular mu(P) <= 0 if m(P) = kappa-1 and
 min(q,q') >= 3; mu(P) <= 0 if m(P) = kappa, q' >= 5 and q >= 1; mu(P) = 1 if m(P) = kappa and q = 0.
Proof. By Lemma 5(b), -nu(P)+sigma(P) = -nu0 and Pi(P)+sigma(P) = Pi0; nu(P) has the parity of q and Pi(P) that of q'
(= that of q, R even). If all even v in [-nu(P),Pi(P)] are realised, the extreme even values are -nu(P)+(q mod 2) and
Pi(P)-(q mod 2): x = y = q mod 2. Otherwise read Lemma 9 (values listed there are treated as missing):
 m = kappa+1, q = s <= 6: missing at most the even v in [Pi(P)-(6-s), Pi(P)]; realised [-nu(P)+(s mod 2), Pi(P)-8+s]:
  (x,y) = (s mod 2, 8-s). q' = s: the negative.
 m = kappa, q = 0 (Pi(P) = B*, nu(P) = 0): realised [2, B*-6], (x,y) = (2,6). q = s in {1,...,4}: v = 0 is realised (Z0);
  realised [-nu(P)+(s mod 2), Pi(P)-6+s], (x,y) = (s mod 2, 6-s). q' = s: the negative.
 m = kappa-1, q = 0: realised [4, B*-4], (x,y) = (4,4); q = 1: [-nu(P)+3, Pi(P)-3], (3,3); q = 2: [-nu(P)+2, Pi(P)-2],
  (2,2); q' = s <= 2: the same (x,y) by the symmetric lists.
In every case x+y <= 8 <= R <= B*. (i)-(iii) are read off the tables. []

## 4. The lift framework at N = 4kappa-6 [NEW at delta = 6]

Let Cl' := {P : m(P) in {kappa-1,kappa,kappa+1}} and Fp := {P : m(P) = kappa+1}; every P in Cl' is proper and nonempty,
and P^c is in Cl' with m(P^c) = m(P). An ALLOWED pair is (P, P u {i}) with i not in P, both in Cl', and
(m(P), m(P u {i})) in {(kappa-1,kappa), (kappa,kappa), (kappa,kappa+1), (kappa+1,kappa+1)}.

LEMMA 12 (lift principles).
(a) [additivity, all-(kappa-1) triples] If P1, P2 are disjoint and m(P1) = m(P2) = m(P1 u P2) = kappa-1, then
 U'(P1 u P2) = U'(P1)+U'(P2).
(b) [complements] If P is in Cl', then U'(P)+U'(P^c) = Pi0-nu0-2p = B*-2nu0-2p.
(c) [differences] For an allowed pair, d := U'(P u {i})-U'(P) satisfies d = hh_i (mod p), d = sigma_i (mod 2) and
 -(D0+X) <= d <= D0+Y, where X := lambda(P u {i})+mu(P) and Y := mu(P u {i})+lambda(P).
(d) [couplings] For every allowed pair, q(P u {i})+q'(P) >= c_X(i) := R-|L_i n A| and q'(P u {i})+q(P) >= c_Y(i) :=
 R-|L_i n A^c|; c_X(i)+c_Y(i) = 2R-r_i >= R.
(e) [pair-independence] For each run i, all allowed pairs (P, P u {i}) have the same difference d.
(f) [empty runs] If run e is empty and some allowed pair exists for e, the common difference theta_e is a NONZERO EVEN
 integer with |theta_e| < 2p.
Proof. (a) Delta := U(P1)+U(P2)-U(P1 u P2) is 0 mod p (Hh is additive) and 0 mod 2 (sigma is additive), hence 0 mod 2p.
By Lemmas 10-11 (lambda, mu <= 3 at m = kappa-1) and Lemma 6: Delta >= 2(Pi0+1) - lambda(P1)-lambda(P2) -
(2p-1-nu0+mu(P1 u P2)) >= M0+3-9 >= 3, and Delta <= 2(2p-1-nu0) + mu(P1)+mu(P2) - (Pi0+1-lambda(P1 u P2))
<= 4p-3-B*+9 < 4p. So Delta = 2p.
(b) sum_i hh_i = 0 + sum_l c_l = Pi0-nu0 (mod p) and sigma(P)+sigma(P^c) = Pi0-nu0, so U(P)+U(P^c) = Pi0-nu0 (mod 2p). By
Lemma 11(ii) it lies in [2Pi0+2-(lambda+mu), 4p-2-2nu0+(lambda+mu)], lambda+mu := lambda(P)+mu(P) <= 6. As
B*+2 > lambda+mu, Pi0-nu0 lies below this interval and Pi0-nu0+4p above it; so U(P)+U(P^c) = Pi0-nu0+2p.
(c) The congruences come from those of U; d >= low(P u {i})-up(P) = -(D0+X) and d <= up(P u {i})-low(P) = D0+Y.
(d) Write L := L(P), L_i and L u L_i = L(P u {i}) (disjoint). By Lemma 5(c), q(P u {i}) >= |A \ (L u L_i)| +
|(L u L_i) n A^c| and q'(P) >= |A^c \ L| + |L n A|. Now |A \ (L u L_i)| + |L n A| = |A|-|L_i n A| and
|(L u L_i) n A^c| + |A^c \ L| >= |A^c|; add. The second coupling is the same with A and A^c exchanged.
(e) Let Xmax, Ymax be the largest X, Y over the allowed pairs for i. With alpha := q(P u {i}), beta := q'(P) (alpha+beta >=
c_X) and the per-set bounds of Lemma 11(iii):
 type (kappa+1,kappa+1): X <= (7-alpha)^+ + (7-beta)^+ <= max(14-c_X, 7);
 type (kappa,kappa+1): X <= (7-alpha)^+ + (5-beta)^+ + [beta = R] <= max(12-c_X, 8);
 type (kappa,kappa): X <= (5-alpha)^+ + [alpha = R] + (5-beta)^+ + [beta = R] <= max(10-c_X, 6);
 type (kappa-1,kappa): X <= 5+3 = 8.
So Xmax <= max(14-c_X, 8), and likewise Ymax <= max(14-c_Y, 8). If c_X, c_Y >= 6, then Xmax+Ymax <= 16. If c_Y <= 5, then
c_X >= R-c_Y >= 17, Xmax <= 8 and Xmax+Ymax <= 22-c_Y, which is <= 21 unless c_Y = 0; the case c_X <= 5 is symmetric. If
c_Y = 0, then |L_i n A^c| = R: A is empty and L_i is the set of all letters, so for every allowed pair L(P) is empty and
L(P u {i}) is everything, q(P) = 0 and q'(P u {i}) = 0; the tables give X = -2, 0, 2, 4 for the four types in the order
listed, and Y <= 14; so Xmax+Ymax <= 18. The case c_X = 0 (A = all letters, L_i = all letters) is symmetric. Hence
Xmax+Ymax <= 21 in all cases. Two differences d1, d2 for i are congruent mod 2p (p odd) and, by (c),
|d1-d2| <= 2D0+Xmax+Ymax <= 4p-4-2B*+21 < 2p, because 2B* >= 2R = 12kappa-16 > 2p+17 = 8kappa+3 for kappa >= 5.
So d1 = d2.
(f) X_e = 0 and sigma_e = 0, so theta_e = hh_e = tau_e = y_e-y_(e-1) (mod p), nonzero by the empty-run rule; theta_e is
even; |theta_e| <= D0+14 <= 2kappa+6 < 2p, and the only even multiple of p in (-2p,2p) is 0. []

(F1) Theta. For a run i let Q_i := {i+1,i+3,...,i+2kappa+1} (kappa+1 runs). Consecutive members differ by 2 and the
 2kappa-7 >= 3 runs i+2kappa+2, ..., i+N separate i+2kappa+1 from i+1+N, so Q_i is independent and m(Q_i) = kappa+1. As
 2kappa+1 < N-1, the run i-1 is not in Q_i, and Q_i u {i} has the maximal intervals {i,i+1}, {i+3}, ..., {i+2kappa+1},
 with the 2kappa-8 >= 2 runs i+2kappa+2, ..., i+N-1 before i+N; so m(Q_i u {i}) = kappa+1. Define
 theta_i := U'(Q_i u {i}) - U'(Q_i) (an explicit pair, LOWER parent erratum). By Lemma 12(e) every allowed pair
 (P, P u {i}) has difference theta_i; theta_i = hh_i (mod p), theta_i = sigma_i (mod 2); by Lemma 12(f) theta_e is a
 nonzero even integer for every empty run e. For P in Cl' put Theta(P) := sum_(i in P) theta_i and f(P) := U'(P)-Theta(P);
 then f(P u {i}) = f(P) for every allowed pair.
(F2) Connectivity of Fp. (a) If P in Fp has a maximal interval [x,y] with x != y, then P\{y} is in Fp; so every P in Fp is
 joined to an independent set of kappa+1 runs. (b) For an independent V = {v_1,...,v_(kappa+1)} in cyclic order let
 g_j >= 1 be the number of runs strictly between v_j and v_(j+1); sum_j g_j = N-kappa-1 = 3kappa-7. If g_j >= 2, then
 V u {v_(j+1)-1} is in Fp and so is the independent set (V\{v_(j+1)}) u {v_(j+1)-1}, whose gaps are those of V with g_j
 lowered and g_(j+1) raised by one; symmetrically, through V u {v_j+1}, one unit moves from g_j to g_(j-1). (c) While some
 g_j >= 2 with j <= kappa, move one unit from gap j to gap j+1 and on up to gap kappa+1 (every donor is >= 2); this ends
 with gaps (1,...,1,G), G := 2kappa-7 >= 3, i.e. V = {x,x+2,...,x+2kappa}. (d) From there move v_(kappa+1), v_kappa, ...,
 v_1 forward by one, in this order (each time the gap ahead is G >= 2 or 2); the result is {x+1,...,x+2kappa+1}. So Fp is
 connected by allowed pairs of type (kappa+1,kappa+1), and f is a constant f0 on Fp.
(F3) m = kappa. (a) If m(P) = kappa and P has a maximal interval [x,y] with x != y, then m(P\{y}) = kappa; so P is joined to
 an independent kappa-set J by pairs of type (kappa,kappa). (b) The complement of J has 3kappa-6 runs in kappa gaps. If a
 gap holds g >= 3 runs and follows j in J, then x := j+2 is adjacent neither to j nor to the next member of J (distance
 g-1 >= 2), J u {x} is an independent (kappa+1)-set, and (J, J u {x}) is a pair of type (kappa,kappa+1). (c) Otherwise
 every gap holds at most 2 runs, so 3kappa-6 <= 2kappa, i.e. kappa in {5,6}, and the gaps are four 2's and one 1
 (kappa = 5) or six 2's (kappa = 6); in both cases some member v of J has gaps of 2 runs before and after it. Then
 J u {v-1} has the maximal intervals {v-1,v} and kappa-1 singletons (v-1 is two after the previous member), so m = kappa,
 and J' := (J u {v-1})\{v} is an independent kappa-set whose gap after v-1 holds 3 runs; apply (b) to J'. Hence f = f0 on
 every P with m(P) = kappa.
(F4) m = kappa-1. (a) An independent (kappa-1)-set Q has 3kappa-5 > 2(kappa-1) runs in kappa-1 gaps, so some gap following a
 member j holds g >= 3 runs, and Q u {j+2} is an independent kappa-set: a pair of type (kappa-1,kappa). So f = f0 on every
 independent (kappa-1)-set. (b) The sets P1 := {0,3,...,3kappa-6} and P2 := {1,4,...,3kappa-5} (kappa-1 runs each) are
 independent (steps of 3; each wrap gap holds kappa-1 >= 4 runs) and disjoint. P1 u P2 has the kappa-1 maximal intervals
 {3j,3j+1} (0 <= j <= kappa-2), separated by the runs 3j+2 (j <= kappa-3) and by the kappa-2 >= 3 runs 3kappa-4, ..., N-1;
 so m(P1 u P2) = kappa-1. The run x := 3kappa-3 has both neighbours 3kappa-4 and 3kappa-2 outside P1 u P2 and lies at
 distance kappa-3 >= 2 from N, so (P1 u P2) u {x} has m = kappa and (P1 u P2, (P1 u P2) u {x}) is a pair of type
 (kappa-1,kappa). So f = f0 on P1, P2 and P1 u P2.
(F5) f0 = 0. Lemma 12(a) gives U'(P1 u P2) = U'(P1)+U'(P2); Theta is additive, so f0 = 2f0 and f0 = 0:
   U'(P) = Theta(P) for every P with m(P) in {kappa,kappa+1}, every independent (kappa-1)-set, and P1 u P2.     (F5)
(F6) Total. Q0 := {0,2,...,2kappa} is independent (the 2kappa-7 runs 2kappa+1, ..., N-1 separate 2kappa from N), and Q0^c
 has the maximal intervals {1}, {3}, ..., {2kappa-1}, {2kappa+1,...,N-1}; both lie in Fp, so by (F5) and Lemma 12(b)
   Theta(all runs) = U'(Q0) + U'(Q0^c) = B* - 2nu0 - 2p = -(2kappa-6) + e* - 2nu0.                                   (F6)

## 5. Proof of Theorem FQW: the final count [NEW]

Assume an avoider w as in Sec. 0 and fix a frame for its NF word u (Sec. 1). S_ev := {0,2,...,N-2} and
S_od := {1,3,...,N-1} are complementary; each has 2kappa-3 runs, pairwise non-adjacent (N is even), so every subset Q of
an alternating set with 1 <= |Q| <= 2kappa-4 is a proper independent set with m(Q) = |Q|, and by (F5)
Theta(Q) = U'(Q) in [low(Q), up(Q)] whenever |Q| in {kappa-1,kappa}. For S in {S_ev,S_od} order its runs
s_1, ..., s_(2kappa-3) with decreasing theta (ties broken arbitrarily) and put
  J'_S := {s_1,...,s_(kappa-1)},  t_S := theta(s_(kappa-1)),  B_S := S \ J'_S (kappa-2 >= 3 runs, all with theta <= t_S),
  eps_S := Theta(S) + nu0 + kappa - 2.
By (F6), eps_ev + eps_od = Theta(all runs) + 2nu0 + 2kappa - 4 = 2 + e* >= 2.
CLAIM. eps_ev + eps_od <= 1.
The CLAIM contradicts the preceding line. Every step used only NF, the frame inputs and Lemma 1 for the avoider u; so no
such u exists, and hence no avoider w as in Sec. 0 exists. This proves Theorem FQW. The rest of Sec. 5 proves the CLAIM.
Types. J'_S has m = kappa-1; write q := q(J'_S), q' := q'(J'_S). J'_S is of type G if min(q,q') >= 3; of type P if
k := q' <= 2 (L(J'_S) is within k letters of A^c); of type Q if k := q <= 2 (L(J'_S) is within k letters of A). P and Q
exclude each other (q+q' = R). By Lemma 11, up(J'_S) <= -1-nu0 for type G, and up(J'_S) = 2-k-nu0 for types P and Q.
Basic inequality. Theta(S) = Theta(J'_S) + sum_(x in B_S) theta_x gives
  eps_S <= mu(J'_S) - 1 + sum_(x in B_S) (theta_x + 1).                                                             (BI)
Every theta-value on J'_S is >= t_S and every one on B_S is <= t_S; empty runs have nonzero even theta ((F1)).

LEMMA 13 (one alternating set). (a) If J'_S is of type G, then t_S <= -1 and eps_S <= -1.
(b) If J'_S is of type P or Q, then t_S <= 0; t_S <= -2 gives eps_S <= -1; t_S = -1 gives eps_S <= 2-k-e_B, where e_B is
 the number of empty runs in B_S.
(c) If J'_S is of type Q, then t_S <= -1.
(d) If J'_S is of type P and t_S = 0 ("case H"), then k+nu0 <= 2, every letter of A has |c| = 1, |A| = nu0, at most
 k+nu0 <= 2 letters lie outside L(J'_S), and eps_S <= 4-kappa-k+2n_B, where n_B is the number of nonempty runs of B_S.
Proof. (a) Theta(J'_S) <= -1-nu0 <= -1; if t_S >= 0 all kappa-1 values would be >= 0. So every term of (BI) is <= 0.
(b) (kappa-1)t_S <= Theta(J'_S) <= 2-k-nu0 <= 2 < kappa-1, so t_S <= 0. If t_S <= -2, every term of (BI) is <= -1 and
eps_S <= 2-k-(kappa-2) <= -1. If t_S = -1, a nonempty run of B_S has theta+1 <= 0, and an empty one has theta <= -2.
(c) Let t_S = 0. Then 0 <= Theta(J'_S) <= 2-k-nu0, so k+nu0 <= 2, and |L(J'_S)| <= |A| + |L(J'_S) n A^c| <= nu0+k <= 2
(|A| <= nu0). So at least kappa-3 >= 2 runs of J'_S are empty, their theta-values are >= 0, nonzero and even, hence >= 2,
and Theta(J'_S) >= 2(kappa-3) >= 4 > 2: impossible.
(d) k+nu0 <= 2 as in (c). A letter of A with |c| >= 3 would give nu0 >= 3; so all of A has |c| = 1 and |A| = nu0. A letter
outside L(J'_S) lies in A^c \ L(J'_S) (at most k letters, as k = |A^c \ L(J'_S)| + |L(J'_S) n A|) or in A (at most nu0).
In (BI) a nonempty run of B_S has theta+1 <= 1, an empty one theta <= -2; so eps_S <= (2-k) + n_B - (kappa-2-n_B). []

LEMMA 14 (no empty alternating set). If nu0 <= 2, no alternating set consists only of empty runs.
Proof. Let every run of S be empty, with theta-values w_1 >= ... >= w_(2kappa-3), all nonzero and even. Every Q in S has
L(Q) empty, so q(Q) = |A| = nu0 (as in Lemma 13(d), all of A has |c| = 1) and q'(Q) = R-nu0. Lemma 11: for |Q| = kappa,
(lambda,mu) = (5,1), (4,0), (3,-1) for nu0 = 0, 1, 2, so up(Q) = -2nu0 <= 0; for |Q| = kappa-1,
(lambda,mu) = (3-nu0, 3-nu0), so up(Q) = 2-2nu0 and low(Q) = (B*-nu0) + 1 - (3-nu0) - 2p = B*-2-2p = -2kappa+4+e*.
If w_kappa >= 2, the top kappa values sum to >= 2kappa > up; so w_kappa <= -2, and so are w_(kappa+1), ...,
w_(2kappa-3). The bottom kappa-1 values w_(kappa-1), ..., w_(2kappa-3) sum to >= -2kappa+4+e*, so
w_(kappa-1) >= -2kappa+4+2(kappa-2) = 0, i.e. w_(kappa-1) >= 2. Then the top kappa-1 values sum to >= 2(kappa-1) >= 8
> 2-2nu0: impossible. []

LEMMA 15 (two alternating sets). Let {S1,S2} = {S_ev,S_od} and write J'_i, t_i, k_i, B_i, eps_i for S_i.
(a) J'_1 and J'_2 are not both of type P.
(b) If J'_1 and J'_2 are both of type Q, then t_1 = t_2 = -1 is impossible.
(c) If J'_1 is of type P, J'_2 of type Q and t_1 = t_2 = -1, then eps_1+eps_2 <= 8-2kappa < 0.
(d) If J'_1 is in case H, then eps_1+eps_2 <= 1 (whatever J'_2 is).
Proof. L(J'_1) and L(J'_2) are disjoint, since J'_1 and J'_2 are.
(a) Every letter of A^c lies outside L(J'_1) or outside L(J'_2), so |A^c| <= k_1+k_2 <= 4, contrary to Lemma 5(d).
(b) Put alpha_i := |A \ L(J'_i)|, beta_i := |L(J'_i) n A^c|, so k_i = alpha_i+beta_i. Disjointness gives
 (|A|-alpha_1)+(|A|-alpha_2) <= |A|, i.e. |A| <= alpha_1+alpha_2, and |L(J'_i)| = |A|-alpha_i+beta_i <=
 alpha_(3-i)+beta_i. So J'_i has at least e_i >= kappa-1-alpha_(3-i)-beta_i empty runs. With t_i = -1 every value on J'_i
 is >= -1, and an empty run's value is >= 2 (nonzero even); so 3e_i-(kappa-1) <= Theta(J'_i) <= 2-k_i-nu0, which gives
 2kappa-4 <= 3alpha_(3-i)+2beta_i-alpha_i-nu0. Adding over i = 1, 2: 4kappa-8 <= 2(k_1+k_2)-2nu0 <= 8, i.e. kappa <= 4:
 impossible.
(c) A letter outside L(J'_1) u L(J'_2) lies in A^c \ L(J'_1) (at most k_1 letters) or in A \ L(J'_2) (at most k_2), and
 it lies in a run of B_1 u B_2 (S1 u S2 is all runs). So at most k_1+k_2 runs of B_1 u B_2 are nonempty, and
 e_(B_1)+e_(B_2) >= 2(kappa-2)-(k_1+k_2). Lemma 13(b): eps_1+eps_2 <= 4-(k_1+k_2)-(e_(B_1)+e_(B_2)) <= 8-2kappa.
(d) By Lemma 13(d), k_1+nu0 <= 2, at most two letters lie outside L(J'_1), and eps_1 <= 4-kappa-k_1+2n_(B_1). These
 letters lie in runs of B_1 u S2; so S2 has at most 2-n_(B_1) nonempty runs and |L(S2) n A^c| <= 2. Hence
 q'(J'_2) >= |A^c|-2 >= 8: J'_2 is of type G or Q. By Lemma 13: either eps_2 <= -1 (type G, or type Q with t_2 <= -2), or
 J'_2 is of type Q with t_2 = -1 and eps_2 <= 2-k_2-e_(B_2) with e_(B_2) >= kappa-2-(2-n_(B_1)) (type Q with t_2 = 0 is
 impossible by Lemma 13(c)). So eps_1+eps_2 <= 3-kappa-k_1+2n_(B_1) or eps_1+eps_2 <= 10-2kappa-k_1-k_2+n_(B_1). As
 n_(B_1) <= 2, both are <= 1 when kappa >= 6. For kappa = 5 they are <= -2+2n_(B_1) and <= n_(B_1), so <= 1 unless
 n_(B_1) = 2; then both letters outside L(J'_1) lie in B_1, every run of S2 is empty, and Lemma 14 (nu0 <= 2) excludes
 this. []
Proof of the CLAIM. If some S has eps_S <= -1 (Lemma 13(a), or 13(b) with t_S <= -2), let S' be the other set: it has
eps_(S') <= -1 (same cases), or eps_(S') <= 2 (types P/Q with t_(S') = -1, Lemma 13(b)), or it is in case H and Lemma 15(d)
applies; type Q with t = 0 does not occur (Lemma 13(c)). In all cases eps_ev+eps_od <= 1. Otherwise both J'_S are of type
P or Q with t_S in {-1,0}. If one is in case H, Lemma 15(d) applies. Otherwise t_ev = t_od = -1 (Lemma 13(c) for type Q),
and Lemma 15(a)-(c) leave only the pair (P,Q), with sum <= 8-2kappa < 1. []
Which inputs carry the weight. The empty-run rule enters only through Lemma 12(f) (used in Lemmas 13-15); the placement of
the extra reflection pairs only through Lemma 1 (C_max = 2H+2m); the light side through M0 (Lemma 12(a)) and |A^c| >= 10;
nonempty runs, o_F and rotation pairs are never assumed; the all-rotations-equal sub-case needs no separate treatment.

## 6. The cases (kappa,p) = (5,13) and (6,17), written out

(kappa,p) = (5,13): N = 14, R = 22, F = 28, H = 7, 2p = 26, 2p-R = 4, D0 = 24-B* <= 2.
- Lemma 2: Win_0 = [12,22], Win_1 = [10,22], Win_4 = [4,18], Win_5 = [2,16], Win_6 = [0,14].
- Lemmas 3-4: every zero-sum of Y has length <= 8, t <= 4, L >= 14 = p+1; (S') at (k',kappa') = (12,4) with
  26+8-12 = 22 = R; E <= 3+n- <= 7, so E <= 6; a_i <= 7, s_j <= 7; m1 >= (41-5t)/2 >= 11; u1 >= |b_l|+9 for every letter;
  |A^c| >= 10. Lemma 6: M0 >= 9+E/2.
- Lemma 7: a minimal representation missing at most 6 letters is single-signed (u1 >= 7+9 > 7+6).
- Lemma 11: the windows have length 24-B*+lambda+mu <= 8 < 26. Lemma 12: (a) Delta >= M0-6 >= 3 and Delta <= 58-B* < 52;
  (e) Xmax+Ymax <= 21 and 2D0+21 <= 25 < 26 (this is where B* >= R = 22 > p+8.5 = 21.5 is used at kappa = 5).
- (F1): Q_i = {i+1,i+3,...,i+11}, separated from i+15 = i+1 by i+12, i+13, i+14; Q_i u {i} has i+12, i+13 before i+14.
- (F2): gaps sum to 8, normal form (1,1,1,1,1,3). (F3)(c): an independent 5-set may have gaps (2,2,2,2,1); then two
  consecutive gaps of 2 exist, and J u {v-1}, J' = (J u {v-1}) \ {v} (gap of 3 after v-1), J' u {x} link J to Fp.
- (F4)-(F5): P1 = {0,3,6,9}, P2 = {1,4,7,10}, P1 u P2 = {0,1},{3,4},{6,7},{9,10} (separated by 2, 5, 8 and 11, 12, 13);
  x = 12 gives (P1 u P2) u {12} with m = 5. The TCW-type all-kappa triple {0,3,...,12}, {1,4,...,13} does not exist here
  (its union has m = 4), and no all-kappa triple exists at N = 14 (Sec. 7 (R2)).
- (F6): Q0 = {0,2,...,10}, Q0^c = {1},{3},...,{9},{11,12,13}; Theta(all runs) = B*-2nu0-26 = -4+e*-2nu0.
- Sec. 5: S_ev = {0,2,...,12}, S_od = {1,3,...,13} (7 runs each); J'_S is the top 4 (m = 4, window [4,18]), B_S has
  3 runs; eps_S = Theta(S)+nu0+3, eps_ev+eps_od = 2+e*. Lemma 15(d) at kappa = 5 uses Lemma 14 (an alternating set of
  seven empty runs with nu0 <= 2 is impossible: w_5 <= -2, then w_4 >= 2, then the top four sum to >= 8 > 2-2nu0).
  Conclusion: eps_ev+eps_od <= 1 < 2; the cell (5,13) is excluded, including the all-rotations-equal configurations.
(kappa,p) = (6,17): N = 18, R = 28, F = 38, H = 10, 2p = 34, 2p-R = 6, D0 <= 4.
- Win_5 = [4,24], Win_6 = [2,22], Win_7 = [0,20]; t <= 5, L >= 18; (S') at (16,5); E <= 5+n- <= 10; m1 >= (51-5t)/2 >= 13;
  u1 >= |b_l|+11; |A^c| >= 12; M0 >= 11.
- (F1): Q_i = {i+1,...,i+13}; (F2): gaps sum to 11, normal form (1,...,1,5); (F3)(c): an independent 6-set with all six
  gaps equal to 2 is linked by the two-step move; (F4): P1 = {0,3,...,12}, P2 = {1,4,...,13}, separated at the wrap by
  14, 15, 16, 17; x = 15. (F6): Q0 = {0,2,...,12}.
- Sec. 5: 9 runs per alternating set; J'_S is the top 5, B_S has 4 runs; Lemma 15(d) closes without Lemma 14.
  Conclusion: eps_ev+eps_od <= 1 < 2.

## 7. Route remarks, the parent exposure, failed routes (no claims beyond Theorem FQW)

(M1) Where delta = 6 enters. Win_(kappa-1) = [4,R-4], Win_kappa = [2,R-6], Win_(kappa+1) = [0,R-8] (as in the parent's
 untrusted note). Minimal representations missing up to 6 letters must be single-signed; this needs u1 >= |b|+6, and
 Lemma 4(v) gives u1 >= |b|+9 (using u1 >= m1+n+). The windows widen by up to 7 units (m = kappa+1) and 5 units
 (m = kappa); lambda+mu <= 6 in every table. The widening is absorbed by the two couplings of Lemma 12(d)
 (Xmax+Ymax <= 21 < 2p-2D0 for kappa >= 5, tight at kappa = 5), by an all-(kappa-1) triple (lambda, mu <= 3) for the
 additive constant, and by B*+2 > lambda+mu in complements.
(M2) The final count. Sorting the top kappa (m = kappa) runs, as in FCW/SCW/TCW, gives generic eps_S <= 0 but type-P sets
 (q' <= 4) may lose up to 5 units. The window [4,R-4] of m = kappa-1 is self-dual and closer to full: only sets with
 min(q,q') <= 2 lose (at most 3) units, and sorting the top kappa-1 runs gives generic eps_S <= -1, i.e. three units of
 slack in total. The exceptional types are handled by empty-run evenness (Lemmas 13-15), and the one tight sub-case at
 kappa = 5 (case H with both outside letters in B_1) by the two-sided Lemma 14.
(M3) Parent exposure. N = 4kappa-6 is even and the alternating sets have 2kappa-3 runs, as noted; the label margin exceeds
 6 at every kappa >= 5, including (5,13); the TCW swap machinery is not needed in this form.
Failed or unused routes (kept; not premises).
(R1) Top-kappa sorting (see (M2)).
(R2) Additive constants with all three sets of m = kappa at N = 14: impossible (two disjoint 5-interval sets inside five
 union intervals need at least 10 runs in intervals plus 5 separators > 14); the SCW/TCW/FCW pairs need N >= 3kappa+2,
 3kappa or 3kappa+3. The all-(kappa-1) triple of (F4) fits every kappa >= 5.
(R3) A single common window for all of Cl': its widening (up to 7 on each side) is too large for Lemma 12(a) at kappa = 5
 (it would need M0 >= 19).
(R4) PL Secs. 7-9, Theorem P, CJ''', K3-11 and all USK, FCW, SCW, TCW and P7L lemmas are not used.

## 8. Scope and interface table

Claimed: Theorem FQW, i.e. for every integer kappa >= 5 with p = 4kappa-7 prime, the terminal cell k = p+1,
kappa_hat = kappa is excluded under the full existential-NF/word antecedent; in particular the cells (5,13) and (6,17).
Lemmas 1-15 and (F1)-(F6) are proved only at p = 4kappa-7, kappa >= 5, in this frame.
NOT claimed: any p not of the form 4kappa-7 (in particular the FCW, SCW and TCW families and every deficiency other than
6); any statement for general deficiency; kappa_hat != kappa; kappa_hat = 0; p = 7; other middle-range or upper-half
cells; nonterminal k; reflection rigidity; INV*; o_F assembly; full ordered Olson; any multiset-only statement outside the
antecedent; novelty, priority, "first", Lean or human review. No FCW, SCW, USK, TCW or P7L statement is extended or used
as a premise.
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
| ZSTRUCT, FB in (S') | R18/olson-FB-parent-verdict-v1.md 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a (1-16); FBP/proof-FB-v1.md 339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b (9-24); FBP/proof-FB-v1-erratum-1.md 33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202 (1-7, no statement change); (S') extension R18/olson-balfull-rotzb-parent-verdict-v1.md 56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0 (26-34) | as listed | Lemma 3(d), t >= 1 only, at (k',kappa') = (p-1,kappa-1): Z-shape, n- >= 1, s_j <= 2t-1, balance, W+n+ <= 2p-1. FB-E NOT used |
| (S1) definition | R16/olson-zx-s1c-parent-verdict-v1.md; 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af | 19 | definition "(S1) bounds every zero-sum length by 2kappa" only; S1(a) NOT used (Lemma 3(b) is direct) |
| LOWER parent erratum | R18/olson-LOWER-parent-erratum-v1.md; 087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377 | 1-10 | m(P) = half the sign transitions (LF7); theta only through explicit pairs (LF6) |
| FCW parent erratum | R18/olson-FCW-parent-erratum-v1.md; e56bf0f337d7d670be99075829217431cf605437320dd3414cde75c3d1ae2413 | 1-14 | derivation patterns only: (SR) from NF+GRX (m4, LF8), redone in Lemma 1; SC0 through Y'z (m3, LF7), redone in Lemma 3(c); no FCW lemma is a premise |
| context only | R18/olson-FCW-parent-verdict-v1.md b28837c9c8a9549b99a6c2205e8bbe40d65ab1aad265595c511395d4c1738f71; R18/olson-SCW-parent-verdict-v1.md d51b5d8e6c6a7c38047434b3740d477bccd2ab7e0e53ce68ea34aa83486bdfe0; R18/olson-USK-parent-verdict-v1.md 6d3358ce3f1e9e95a366f2b32f10adbc73df607bc62723f561567dce1a53de18; R18/olson-K0T-parent-verdict-v1.md 4a2a2ffd8d8624c33c0f7cc1265cf679c18ac3a9c63565bc093b2e8afc8bf8ba; R18/olson-LOWER-K1-parent-verdict-v1.md 93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83; PL (CONT/lowerhalf-terminal-cell/proof-LOWER-v1.md 251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d; nothing imported: (SR), IF(a), normalisation, SS, LT are written out here) | whole | not premises |
| untrusted | CONT/lowerhalf-third-cut-window/proof-TCW-v1.md 62c747911239c32998d2ec2b3bd9ec538eee5e523f68b92233aa06e890f85713 with R18/olson-TCW-parent-erratum-v1.md eb673b3200d4d0f8f7e36f61fbf3225e5c3542e0b14de05a604ca50c640ee8c9 and -v2.md a8204c0e533828fc86816ea6de648a2d52ff3409898f0c557bd8fe5a79f8e88d; CONT/p7-lower-terminal/proof-P7L-v1.md 7e8bee08dacb10a9b4dd373dc9e57e526a21bd4bc77e91a41091b8e88cacb7e8; CONT/lowerhalf-first-cut-window-boundary/proof-FCW-v1.md c23fd0378f68611070e3bf0fd74d66d1f7ad859bb01ccc1af4ce9a77cf4aaecf; CONT/lowerhalf-second-cut-window/proof-SCW-v1.md 6a1965aecf599e00b512ca1df36127d21e5bac21bea7ac0da5804092245f3650 | whole | methods only, re-derived at p = 4kappa-7; never premises |
Not used: S1(a); the Setting fact; FB-E; Theorem P; B0S-CJ'''; K3-11; every PL, USK, K3, FCW, SCW, TCW and P7L lemma; P11R and
every other unreviewed candidate.
Machine steps for this file: /bin/date, shasum -a 256, wc -c -l, reading files, and one exclusive creation (Python
open(path,'x')) of this text, drafted by hand in memory in eight parts; plain in-memory rewording replacements before
creation are disclosed in checkpoints/cp-04.md and cp-05.md; no assertion of any kind and no check over mathematical
objects.
