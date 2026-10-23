# TCW: third cut window p = 4kappa-5 (kappa >= 4): the lower-half terminal cell kappa_hat = kappa is excluded, v1

Owner OlsonThirdCutWindow. Drafted by hand after /bin/date 2026-10-20T05:13:14-0700. Status: CANDIDATE_UNVERIFIED written
proof of the FULL frozen target (TCW-scope-v1.md SHA256 f0dacbe3e1f2f8a4267f7bdfa5ea91097690168bbf0e50dced92e6cc49be02d1,
frozen 2026-10-20T03:27:24-0700 before any derivation; authority
RUN/control/written-olson-third-cut-window-transition-v1.json SHA256
201201cd69cc7148e22ccea814d5f61f6e46e540ddd64546fe5a5fd2436c25cf). Outcome: PROVED, no failing lemma. The cell
(kappa,p) = (4,11) is covered (Secs. 5 and 6); (6,19) is written out in Sec. 6. LABELLED PARTIAL of ordered Olson: one
family of terminal lower-half cells. All case work is by hand; no script, assertion, enumeration or computation over
scientific data. No novelty, priority, Lean or human-review claim; no other cell; no full ordered Olson.

## 0. Statement

THEOREM TCW. Let kappa >= 4 be an integer such that p = 4kappa-5 is prime (so p = 3 mod 4, p >= 11; (kappa,p) = (4,11),
(6,19), (7,23), (9,31), (12,43), ...). No word w of length 4p-2 over D_(2p) without an identity 2p-subword in increasing
original index order has an admissible normal form (NF) with terminal k = p+1 and kappa_hat = kappa. Full antecedent: SOME
admissible NF; the H = p-1-kappa extra reflection pairs lie anywhere in the odd blocks; every empty NF run separates
different reflection values; no o_F, nonempty-run, rotation-pair or reflection-rigidity hypothesis on w. In particular
the whole cell (kappa_hat,p) = (4,11) is excluded.
Route. Lemma 1 (windows; deficiency delta := 4kappa-p-1 = 4), Lemmas 2-4 (frame, label counts, density, the identity
q(P) = |letters(P) symdiff A|), Lemma 5 (lift margin), Lemmas 6-8 (minimal representations, exact exception lists for the
windows [2,R-4] and [0,R-6], duality for [4,R-2]), Lemma 9 (representative windows with explicit (lambda,mu) tables for
m in {kappa-1,kappa,kappa+1}), Lemmas 10-11 (additivity on an all-m=kappa triple, complements), Sec. 4 (lift framework at
N = 4kappa-4, including the m = kappa-1 sets J minus one run), Sec. 5 (final count with one unit of slack: generic,
"type Q" and "type P" sorted sets, swap inequalities, empty-run evenness, and a two-sided "no empty alternating set"
lemma).
Exposure. Read after the freeze: the FCW proof (accepted only at p = 4kappa-1) and the unaccepted SCW proof
(p = 4kappa-3), as sources of methods only. Every lemma below is proved here at p = 4kappa-5; no FCW or SCW lemma is a
premise. The parent observation recorded in the transition (windows [2,R-4], [0,R-6]; FCW-type count with slack 5; the
SCW additive-constant pair does not fit at (4,11)) was disclosed exposure only; Sec. 7 records how each item fares.

## 1. Setting, windows and frame [PL Secs. 2, 4-6, accepted via the K1 verdict, read with the LOWER parent erratum]

PL = proof-LOWER-v1.md (pinned in Sec. 8). Its standing range, p >= 11 prime and 1 <= kappa <= (p-3)/2, contains every
(kappa,p) here, since kappa = (p+5)/4 <= (p-3)/2 for p >= 11. Throughout, p = 4kappa-5 and kappa >= 4. There are
N = p+1 = 4kappa-4 runs (N even) and R = p-1+2kappa = 6kappa-6 rotation letters (R even, R >= 18); H = 3kappa-6 (scalar,
the number of extra reflection pairs), F = 3p-1-2kappa = 10kappa-16 reflections, 2p = 8kappa-10. Hence 2p-R = 2kappa-4,
R-2p = -(2kappa-4), 2R-2p = 4kappa-2, 2p-2kappa = R-4.
Word form [NF, GRX; PL Sec. 2]. The NF word u is an avoider of length 4p-2 with the rotation multiset of w. Read it
cyclically as R_0 S_0 R_1 S_1 ... R_p S_p: run R_i has r_i >= 0 letters, S_i = sigma_(y_i)^(l_i) with l_i odd and
sum (l_i-1)/2 = H, and an EMPTY run R_i has y_(i-1) != y_i (indices mod N). Put tau_i := y_i - y_(i-1) (sum 0). For a set
P of runs, m(P) is half the number of sign transitions of the pattern (-1 on P, +1 off P) (LOWER parent erratum): m(empty)
= m(all runs) = 0, a proper nonempty P has m(P) equal to its number of maximal cyclic intervals, and m(P^c) = m(P).
T(P) := sum_(i in P) tau_i; X^(P) is the list of letter values with every letter of a run of P negated; letters(P) is the
set of letters lying in runs of P. A set of runs is independent if its members are pairwise non-adjacent (cyclically); a
proper independent set of j >= 1 runs has m = j.
(SR) [PL Sec. 2, from the GRX if-direction; as derived in the FCW parent erratum m4] Odd blocks give Phi = 2m(P),
 delta_GRX = N-2m(P), C_max = F-delta_GRX = 2H+2m(P); with n := 2p-C: for every P and every even n with
 max(0,2kappa+2-2m(P)) <= n <= min(R,2p-2m(P)), T(P) is not a sum (in Z_p) of n letters (distinct occurrences) of X^(P).
 Write Win_m for this set of n when m(P) = m.

LEMMA 1 (windows; sets of even integers). (a) Win_0 = [2kappa+2,R] and Win_1 = [2kappa,R]. (b) Win_(kappa-1) = [4,R-2],
Win_kappa = [2,R-4], Win_(kappa+1) = [0,R-6].
Proof. (a) 2kappa+2 <= R, and 2p-2 = 8kappa-12 >= R. (b) 2kappa+2-2m equals 4, 2, 0 and 2p-2m equals R-2, R-4, R-6 for
m = kappa-1, kappa, kappa+1. []

LEMMA 2 (frame).
(a) [PL IF(a)] The N block values lie in Z_p, so y_c = y_c' for some c != c'. The arc P0 := runs c+1,...,c' is proper and
 nonempty with T(P0) = y_c' - y_c = 0, and its complementary arc C0 has T(C0) = 0.
(b) [DIRECT] Let Y be the sequence of the R elements (1,x) of Z_2 x Z_p = C_(2p), one for each letter x of X^(P0). A
 zero-sum of Y of length n is a set of n letters of X^(P0) with sum 0 = T(P0); n is even and n <= R. (SR) at P0
 (m(P0) = 1, Win_1 = [2kappa,R]) excludes every even n in [2kappa,R]. So every zero-sum of Y has length <= 2kappa-2.
(c) [SC0, through the minimal-zero-sum step] Let Z be a LONGEST zero-sum of Y, |Z| = 2t with 0 <= t <= kappa-1. Then
 Y' := Y - Z is zero-sum free (a nonempty zero-sum of Y' together with Z would be longer) of length
 L = R-2t >= 6kappa-6-2(kappa-1) = 4kappa-4 = p+1. Put z := -sigma(Y'); z != 0, and Y'z is a minimal zero-sum sequence
 (a nonempty proper zero-sum subsequence T of Y'z gives the nonempty zero-sum T inside Y' if z is not in T, and Y'z - T
 inside Y' if z is in T). Its length is L+1 >= p+2 = floor(2p/2)+2 and 2p >= 3, so by SC0 it has a 1-element basis {g}:
 every term is x*g with least positive coefficient x, and the coefficients sum to ord(g). There are L+1 >= p+2
 coefficients, each >= 1, so ord(g) >= p+2, i.e. ord(g) = 2p and g generates C_(2p). So Y' = (a_1 g)...(a_L g) with
 least positive coefficients a_i and W := sum a_i = 2p - x(z) <= 2p-1. Write g = (g_1,gamma). Every term of Y' is odd,
 so a_i g_1 = 1 (mod 2): g_1 = 1 and every a_i is odd; gamma != 0 because g generates.
(d) [ZSTRUCT, FB in (S')] If t = 0, put n+ = n- = 0. If t >= 1, then Y lies in setting (S') with (k',kappa') =
 (p-1,kappa-1): p >= 5 is prime; 1 <= k' <= p-1; kappa' is an integer with 1 <= kappa' < p; Y consists of
 2p+2kappa'-k' = p+2kappa-1 = R odd elements; every zero-sum of Y has length <= 2kappa' (this is (b), i.e. (S1) at
 kappa'); Z is longest with t <= kappa'; L = R-2t >= 2p-k' = p+1; and g is an index-<1 generator of Y-Z. ZSTRUCT
 (accepted in (S') through its proof) gives Z = g^(n+) (-s_1 g)...(-s_(n-) g) with odd s_j >= 1, n+ + n- = 2t and
 n- >= 1. Lemma FB gives the balance sum_j s_j = n+ and W + n+ <= 2p-1. Hence n- <= n+ (each s_j >= 1), so n- <= t <=
 kappa-1 and n+ >= t; and s_j <= n+ - (n- - 1) <= n+ <= 2t-1 <= 2kappa-3. In both cases W + n+ <= 2p-1.
(e) Labels. Each letter l gets an odd integer label b_l, and its value in X^(P0) is b_l*gamma. The multiset {b_l} is
 {a_1,...,a_L} u {1 (n+ times)} u {-s_1,...,-s_(n-)}. Put E := W-L = sum_i (a_i-1) >= 0, m1 := #{i : a_i = 1} and
 u1 := #{l : |b_l| = 1} >= m1 + n+.

LEMMA 3 (label counts). (i) E <= 2kappa-5+n- <= 2kappa-5+t <= 3kappa-6. (ii) Every a_i <= 1+E <= 3kappa-5 and every
s_j <= min(n+, 2kappa-3). (iii) m1 >= (10kappa-7-5t)/2 >= (5kappa-2)/2 >= 9. (iv) If some a_i equals b >= 3, then
m1 >= (5kappa-5+b)/2 and m1-b >= kappa. (v) u1 >= |b_l| + kappa >= |b_l| + 4 for every letter l.
Proof. (i) L = R-n+-n- and W <= 2p-1-n+, so E = W-L <= 2p-1-R+n- = 2kappa-5+n-; and n- <= t <= kappa-1. (ii) a_i-1 <= E;
Lemma 2(d). (iii) Each a_i > 1 is odd, so it adds at least 2 to E; hence L-m1 <= E/2 and m1 >= (6kappa-6-2t) -
(2kappa-5+t)/2 = (10kappa-7-5t)/2, which is >= (5kappa-2)/2 since t <= kappa-1; at kappa = 4 this is 9.
(iv) That a_i adds b-1 to E and every other a-label > 1 adds at least 2, so L-m1-1 <= (E-b+1)/2 and
m1 >= (6kappa-7-2t) - (2kappa-4+t-b)/2 = (10kappa-10-5t+b)/2 >= (5kappa-5+b)/2. As b <= 3kappa-5, m1-b >= (5kappa-5-b)/2
>= kappa. (v) If |b_l| = 1: u1 >= m1 >= (5kappa-2)/2 >= 1+kappa. If b_l = a_i = b >= 3: u1 >= m1 >= b+kappa by (iv). If
b_l = -s_j: u1 >= m1+n+ >= kappa+s_j, since s_j <= n+ and m1 >= kappa. []
Normalisation [PL Sec. 4]. (v,eps) -> (gamma^(-1)v,eps) is an automorphism of D_(2p); it preserves identity subwords, the
run/block structure (with the empty-run rule) and (SR), with tau_i and all values scaled by gamma^(-1). So take gamma = 1.
Put c_l := b_l for l in C0 and c_l := -b_l for l in P0. The original value of l is c_l (mod p), and its value in X^(P) is
eps_l c_l, where eps_l = -1 iff l lies in a run of P.
Light side [PL Lemma LT, re-derived]. Let o(Q) := #{letters of runs of Q with b = 1}. Letters of C0 with b = 1 have
original value 1, and letters of P0 with b = 1 have original value -1. If o(C0) >= kappa+1 and o(P0) >= kappa+1, then
kappa+1 of each have original values summing to 0 = T(empty), with n = 2kappa+2 in Win_0 = [2kappa+2,R]; (SR) at
P = empty forbids this. So min(o(P0),o(C0)) <= kappa. Exchanging P0 and C0 keeps Lemmas 2-3 with the same labels: C0 is a
proper arc with T(C0) = 0, X^(C0) = -X^(P0), its sequence is -Y because (1,-x) = -(1,x) in Z_2 x Z_p, the zero-sums of
-Y are those of Y, Z stays longest, and -g is an index-<1 generator of -Y' with the same coefficients (gamma -> -gamma).
Fix P0 with q1 := o(P0) <= kappa, and then apply the normalisation and the convention c = +-b to that frame.
Quantities. A := {l : c_l < 0} and A^c := {l : c_l > 0} (every c_l is odd, so nonzero). Pi0 and nu0 are the sums of
|c_l| over A^c and over A. B* := Pi0+nu0 = sum|b_l| = W+2n+ = R+E+n+-n-. B* is even: it is a sum of R odd terms, and R is
even. sigma(P) := sum of c_l over letters(P), and sigma_i := sigma({i}). X_i := sum of the original values of run i, so
X_i = sigma_i (mod p). hh_i := tau_i + X_i and Hh(P) := sum_(i in P) hh_i = T(P)+sigma(P) (mod p).
Frame quantifier. Lemmas 2-3 and the light-side choice hold for EVERY admissible choice of P0, Z, g and light side. The
proof fixes one such frame, and one always exists.

LEMMA 4 (density, signed sums, positive letters). (a) Every integer of [0,B*] is a sum of a sub-multiset of
{|c_l|}. (b) B* >= R, with equality iff every |c_l| = 1. (c) [the explicit PL Sec. 5 bijection, instantiated through
(a)] Fix P. Let Pos(P), Neg(P) be the letters with eps_l c_l > 0 and < 0, q := |Neg(P)|, q' := |Pos(P)| = R-q,
Pi(P) := sum over Pos(P) of |c| and nu(P) := sum over Neg(P) of |c|. The signed sums sum_(l in J) eps_l c_l over sets J
of letters are exactly the integers of [-nu(P),Pi(P)], and each has the parity of |J|. Moreover Pi(P) = Pi0-sigma(P) and
nu(P) = nu0+sigma(P). (d) Neg(P) = letters(P) symdiff A, so q(P) = |letters(P) symdiff A| and q'(P) =
|letters(P) symdiff A^c|. (e) |A^c| >= (5kappa-4)/2 >= 8.
Proof. (a) The multiset contains u1 ones, and every element is <= u1+1 by Lemma 3(v). Order the elements > 1 increasingly,
with prefix sums D_0 = 0 <= D_1 <= .... Every D_j + i (0 <= i <= u1) is a subset sum, and D_(j+1)-D_j <= u1+1, so these
intervals cover [0,B*]. (b) B*-R = E+(n+-n-) >= 0, with equality iff E = 0 and n+ = n-, i.e. iff every a_i = 1 and every
s_j = 1. (c) J -> (J n Pos(P)) u (Neg(P) \ J) is a bijection on sets of letters, with sum_(l in J) eps_l c_l =
sum_(l in image)|c_l| - nu(P); apply (a) and Pi(P)+nu(P) = B*. The terms are odd. Flipping the letters of P moves their
positive weight to the negative side and conversely. (d) A letter of P has value -c_l, negative iff l is in A^c; a letter
outside P has value c_l, negative iff l is in A. (e) The letters with b = 1 are the m1 a-labels equal to 1 and the n+
terms g of Z, i.e. m1+n+ >= (10kappa-7-5t)/2 + t >= (7kappa-4)/2 letters (n+ >= t, t <= kappa-1). At most o(P0) = q1 <=
kappa of them lie in P0; the others lie in C0 and have c = 1 > 0. So |A^c| >= (7kappa-4)/2 - kappa = (5kappa-4)/2. []

## 2. Lemma 5: the lift margin [re-derived at p = 4kappa-5]

A letter with c < 0 is (i) one of the q1 <= kappa letters of P0 with b = 1 (c = -1), or (ii) a letter of P0 whose label is
an a-label B >= 3 (c = -B), or (iii) a letter of C0 with label -s_j (c = -s_j).
LEMMA 5. nu0 <= q1 + 3E/2 + n+, and M0 := 2Pi0 + nu0 - 2p >= 2kappa-1+E/2 >= 7.
Proof. Each B >= 3 satisfies B <= (3/2)(B-1), and the numbers B-1 of type (ii) sum to at most E; the type (iii) labels sum
to at most sum_j s_j = n+. With Pi0 = B*-nu0, B* = R+E+n+-n- and 2R-2p = 4kappa-2:
M0 = 2B*-nu0-2p >= 4kappa-2+2E+2n+-2n- -q1-3E/2-n+ = 4kappa-2+E/2+n+-2n- -q1.
Use q1 <= kappa, then n+ >= n-, then n- <= kappa-1: this is >= 2kappa-1+E/2, and 2kappa-1 >= 7 because kappa >= 4. []

## 3. Realisation, exception lists and representative windows [NEW at delta = 4]

Let Cl := {P : m(P) in {kappa,kappa+1}}, Fp := {P : m(P) = kappa+1} and Cl' := {P : m(P) in {kappa-1,kappa,kappa+1}}.
Every P in Cl' is proper and nonempty, and P^c is in Cl' with m(P^c) = m(P). For a set P of runs and a set I of even
integers, an even integer v is REALISED (for I) if v = sum_(l in J) eps_l c_l for some set J of letters with |J| in I.
X^(P) is "two-signed" if q >= 1 and q' >= 1.

LEMMA 6 (minimal representations). Fix P and an even integer v in [-nu(P),Pi(P)], and let J be a set of letters with
signed sum v and |J| minimal (it exists by Lemma 4(c)). Then:
 (a) |J| is even, and no nonempty subset of J has signed sum 0.
 (b) If R-|J| <= 4, then J is contained in Pos(P) or in Neg(P).
 (c) If J is contained in Pos(P) and R-|J| <= 4, then q <= R-|J|, and Pos(P) \ J consists of k' := R-q-|J| letters with
     |c| = 1; so v = Pi(P)-k', with q+k' <= 4 and k' = q (mod 2). Symmetrically, if J is contained in Neg(P) and
     R-|J| <= 4, then v = -nu(P)+k' with k' := R-q'-|J|, q'+k' <= 4 and k' = q' (mod 2).
Proof. (a) The terms are odd and v is even. Removing a zero-signed nonempty subset would give a smaller J.
(b) Let M be the set of letters outside J, |M| <= 4. If J contains a letter of value +1 and one of value -1, they form a
zero-signed pair, contrary to (a). So the letters of J with |c| = 1 all have one value; J contains at least u1-4 >= 5 of
them (Lemma 3(v)). Say this value is +1 (the case -1 is the negative of this). If J contains a negative letter l, its
value is -b with b >= 3, and J contains at least u1-4 >= b letters of value +1 (Lemma 3(v): u1 >= b+4); l with b of them
is a zero-signed subset of J, contrary to (a). So J lies in Pos(P).
(c) Neg(P) is contained in M, so q <= |M| = R-|J|, and M' := Pos(P) \ J = M \ Neg(P) has k' letters. Suppose some l in M'
has |c_l| = x >= 3. Pos(P) contains at least u1-q letters with |c| = 1, and at most k'-1 of them lie in M', so J contains
at least u1-q-k'+1 >= u1-3 >= x of them (q+k' <= 4; Lemma 3(v)), all of value +1. Replacing x of them by l keeps the
signed sum and gives size |J|-x+1 < |J|, contrary to minimality. So M' consists of letters with |c| = 1 and
v = Pi(P)-k'. As R and |J| are even, k' = R-q-|J| = q (mod 2). The case J in Neg(P) is the negative. []

LEMMA 7 (exception lists). Fix P, q = |Neg(P)|, q' = R-q, and an even integer v in [-nu(P),Pi(P)].
 (a) [Win_kappa = [2,R-4]] v is realised for [2,R-4] except possibly in these cases: q = 0 and v in {0, B*-2, B*};
     q = 1 and v = Pi(P)-1; q = 2 and v = Pi(P); q' = 0 and v in {0, -B*+2, -B*}; q' = 1 and v = -nu(P)+1; q' = 2 and
     v = -nu(P).
 (b) [Win_(kappa+1) = [0,R-6]] v is realised for [0,R-6] except possibly in these cases: q <= 4 and v = Pi(P)-k' with
     0 <= k' <= 4-q and k' = q (mod 2); q' <= 4 and v = -nu(P)+k' with 0 <= k' <= 4-q' and k' = q' (mod 2).
 Since q+q' = R >= 18, at most one of q, q' is <= 4.
Proof. Take J as in Lemma 6. (a) Let v != 0. If |J| <= R-4, then |J| >= 2 and v is realised. Otherwise R-|J| <= 2, and
Lemma 6(b),(c) give v = Pi(P)-k' with q+k' <= 2, k' = q (mod 2), i.e. (q,k') in {(0,0),(0,2),(1,1),(2,0)} (for q = 0,
Pi(P) = B*), or the negative statement. Let v = 0. If X^(P) is two-signed, a zero-signed set Z0 with
2 <= |Z0| <= 3kappa-4 <= R-4 exists: if both values +1 and -1 occur among the letters with |c| = 1, a pair; otherwise say
all of them have value +1 (the other case is the negative), a negative letter has value -b with b >= 3, and it together
with b letters of value +1 (u1 >= b+4) is Z0, of size b+1 <= 3kappa-4 (Lemma 3(ii)). If q = 0 or q' = 0, v = 0 is listed.
(b) If |J| <= R-6, v is realised (this includes v = 0, J empty). Otherwise R-|J| <= 4, and Lemma 6(b),(c) give: J lies in
Pos(P), q <= 4 and v = Pi(P)-k' as listed, or J lies in Neg(P), q' <= 4 and v = -nu(P)+k' as listed. []

LEMMA 8 (duality for Win_(kappa-1) = [4,R-2]). Fix P and put Sigma(P) := Pi(P)-nu(P), the signed sum of all letters.
J -> (all letters) \ J maps signed sum v to Sigma(P)-v and size n to R-n, and maps [2,R-4] onto [4,R-2]. Hence v is
realised for [4,R-2] iff Sigma(P)-v is realised for [2,R-4]. Also Sigma(P)+2sigma(P) = Pi0-nu0. []

LEMMA 9 (representative windows). Let P be in Cl' and write I_P := Win_(m(P)).
 (a) Suppose the integers v+sigma(P), v realised for I_P, include every integer of the parity of sigma(P) in
     [-nu0+x, Pi0-y], where x, y >= 0 and both ends have that parity. Then B* <= 2p-4+x+y, and Hh(P) (mod p) has a unique
     representative U(P) with U(P) = sigma(P) (mod 2) in the interval [Pi0-y+2, 2p-2-nu0+x]. Put lambda(P) := y-1,
     mu(P) := x-1 and U'(P) := U(P)-2p, so that
       low(P) := Pi0+1-lambda(P)-2p <= U'(P) <= up(P) := -1-nu0+mu(P).
 (b) Valid (x,y), hence (lambda,mu), are given by the following tables, read with q = q(P), q' = q'(P):
     m(P) = kappa:   q = 0: (3,1); q = 1: (2,0); q = 2: (1,-1); q' = 0: (1,3); q' = 1: (0,2); q' = 2: (-1,1);
                     otherwise lambda = mu in {-1,0}.
     m(P) = kappa+1: q = s <= 4: (5-s, (s mod 2)-1); q' = s <= 4: ((s mod 2)-1, 5-s); otherwise lambda = mu in {-1,0}.
     m(P) = kappa-1: q = 0: (1,3); q = 1: (0,2); q = 2: (-1,1); q' = 0: (3,1); q' = 1: (2,0); q' = 2: (1,-1);
                     otherwise lambda = mu in {-1,0}   (the m = kappa table with lambda and mu exchanged).
 (c) Consequences. lambda, mu <= 3 when m(P) in {kappa-1,kappa}, and lambda, mu <= 5 when m(P) = kappa+1;
     lambda(P)+mu(P) <= 4 always; (lambda,mu)(P^c) = (mu,lambda)(P) for P in Cl. Compactly, for m(P) = kappa:
     lambda <= (3-q)^+ + [q' = 0] and mu <= (3-q')^+ + [q = 0]; for m(P) = kappa+1: lambda <= (5-q)^+ and
     mu <= (5-q')^+. If m(P) = kappa and q' >= 3, then mu(P) <= 1, with equality iff q = 0, i.e. letters(P) = A. If
     m(P) = kappa-1, then mu(P) >= 2 iff q <= 1.
 (d) U(P) is the unique integer of [Pi0+1-lambda(P), 2p-1-nu0+mu(P)] (length 2p-2-B*+lambda+mu <= 2kappa-2 < 2p) with
     U(P) = Hh(P) (mod p) and U(P) = sigma(P) (mod 2).
Proof. (a) By (SR), T(P) != v (mod p) for every realised v, since the values of X^(P) are eps_l c_l (mod p). As
Hh(P) = T(P)+sigma(P) (mod p), Hh(P) is congruent to no integer of the parity of sigma(P) in [a,b], a := -nu0+x,
b := Pi0-y. The p integers a, a+2, ..., a+2p-2 are pairwise incongruent mod p (p is an odd prime), so Hh(P) is congruent
to exactly one of them, a+2j, and a+2j > b. If b >= a+2p-2 this is impossible, so B*-x-y = b-a <= 2p-4, and a+2j lies in
[b+2, a+2p-2]; it has the parity of sigma(P).
(b) Recall -nu(P)+sigma(P) = -nu0 and Pi(P)+sigma(P) = Pi0 (Lemma 4(c)); nu(P) has the parity of q and Pi(P) that of q'.
 m = kappa, by Lemma 7(a). Generic (q, q' >= 3): every even v in [-nu(P),Pi(P)] is realised; with x = y := the parity of
 q (which equals that of q'), the ends -nu(P)+x and Pi(P)-y are the extreme even values. q = 0 (letters(P) = A,
 Pi(P) = B*, nu(P) = 0, sigma(P) = -nu0): realised [2,B*-4], shifted [-nu0+2, Pi0-4], (x,y) = (2,4). q = 1: realised
 [-nu(P)+1, Pi(P)-3], (x,y) = (1,3). q = 2: realised [-nu(P), Pi(P)-2], (0,2). q' = 0 (letters(P) = A^c, sigma(P) = Pi0):
 realised [-B*+4,-2], shifted [-nu0+4, Pi0-2], (4,2). q' = 1: [-nu(P)+3, Pi(P)-1], (3,1). q' = 2: [-nu(P)+2, Pi(P)], (2,0).
 m = kappa+1, by Lemma 7(b). For q = s <= 4 the largest excluded k' is 4-s (4-s = s mod 2), so the realised values are
 the even v in [-nu(P)+(s mod 2), Pi(P)-6+s]: (x,y) = (s mod 2, 6-s). The case q' = s <= 4 is the negative. Generic:
 x = y in {0,1} as before.
 m = kappa-1, by Lemma 8: the realised set for [4,R-2] is Sigma(P) minus the realised set for [2,R-4], and
 v+sigma(P) = (Pi0-nu0) - ((Sigma(P)-v)+sigma(P)). So the shifted realised set is the reflection of the m = kappa one in
 (Pi0-nu0)/2, which exchanges x and y (parities are kept because Pi0-nu0 = B* is even).
(c) Read off the tables; for complements, m(P^c) = m(P) and q(P^c) = q'(P) (Lemma 4(d)), and the tables are symmetric
under q <-> q' with lambda <-> mu.
(d) The interval of (a) is [Pi0+1-lambda, 2p-1-nu0+mu]; its length is 2p-2-B*+lambda+mu <= 2p-2-R+4 = 2kappa-2. Since p is
odd, the residues mod p and mod 2 fix the residue mod 2p, and an interval of length < 2p holds at most one integer of a
given residue mod 2p. []
Write D0 := 2p-2-B* <= 2p-2-R = 2kappa-6 (Lemma 4(b)); D0 may be negative.

LEMMA 10 (additivity on an all-kappa triple). If P1 and P2 are disjoint and m(P1) = m(P2) = m(P1 u P2) = kappa, then
U(P1) + U(P2) - U(P1 u P2) = 2p.
Proof. Delta := U(P1)+U(P2)-U(P1 u P2) is 0 (mod p), since Hh is additive, and 0 (mod 2), since sigma is additive; so
Delta = 0 (mod 2p). By Lemma 9 (lambda, mu <= 3 at m = kappa) and Lemma 5,
Delta >= 2(Pi0+1) - lambda(P1) - lambda(P2) - (2p-1-nu0+mu(P1 u P2)) = M0+3-(lambda1+lambda2+mu12) >= M0-6 >= 1, and
Delta <= 2(2p-1-nu0) + mu(P1) + mu(P2) - (Pi0+1-lambda(P1 u P2)) <= 4p-3-B*+9 < 4p (B* >= R >= 18). So Delta = 2p. []
LEMMA 11 (complements). If P is in Cl, then U'(P) + U'(P^c) = Pi0 - nu0 - 2p = B* - 2nu0 - 2p.
Proof. sum_(all i) hh_i = sum_i tau_i + sum_i X_i = 0 + sum_l c_l = Pi0 - nu0 (mod p), and sigma(P) + sigma(P^c) =
Pi0 - nu0. So U(P) + U(P^c) = Pi0 - nu0 (mod 2p). It lies in [2Pi0+2-lambda-lambda^c, 4p-2-2nu0+mu+mu^c] (lambda =
lambda(P), lambda^c = lambda(P^c) = mu(P), and so on), whose length is 4p-4-2B*+2(lambda+mu) <= 4p+4-2B* < 2p, because
B* >= R = 6kappa-6 > p+2. The integer Pi0-nu0 lies below it (B*+2 > lambda+mu), and Pi0-nu0+4p lies above it
(B*+2 > lambda+mu). So U(P)+U(P^c) = Pi0-nu0+2p. []

## 4. The lift framework at N = 4kappa-4 [NEW at p = 4kappa-5]

Runs are indexed mod N = 4kappa-4.
(F1) Theta. For a run i let Q_i := {i+1, i+3, ..., i+2kappa+1} (kappa+1 runs). Consecutive members differ by 2, and the
 2kappa-5 >= 3 runs i+2kappa+2, ..., i+N separate i+2kappa+1 from i+1+N; so Q_i is independent and m(Q_i) = kappa+1.
 The run i-1 = i+4kappa-5 is not in Q_i, so Q_i u {i} has the maximal intervals {i,i+1}, {i+3}, ..., {i+2kappa+1}, and
 the 2kappa-6 >= 2 runs i+2kappa+2, ..., i+N-1 separate i+2kappa+1 from i+N; so m(Q_i u {i}) = kappa+1. Define
 theta_i := U'(Q_i u {i}) - U'(Q_i) (theta only through this explicit pair, LOWER parent erratum).
 Range. For P and P u {i} in Cl' (i not in P), d := U'(P u {i}) - U'(P) satisfies d = hh_i (mod p), d = sigma_i (mod 2),
 and -(D0+X) <= d <= D0+Y with X := lambda(P u {i})+mu(P) and Y := mu(P u {i})+lambda(P), since
 d >= low(P u {i}) - up(P) and d <= up(P u {i}) - low(P) (Lemma 9(a)).
 (F1a) If P, P u {i} are in Cl, then X <= 6 and Y <= 10. Y <= 10 by Lemma 9(c). Put a := q(P u {i}) and b := q'(P). By
  Lemma 4(d), a >= |letters(P u {i}) n A^c| >= |letters(P) n A^c| and b >= |A^c \ letters(P)|, so a+b >= |A^c| >= 8
  (Lemma 4(e)). By the compact bounds of Lemma 9(c), lambda(P u {i}) <= (5-a)^+ unless m(P u {i}) = kappa and
  q'(P u {i}) = 0, in which case a = R and lambda(P u {i}) <= 1; likewise mu(P) <= (5-b)^+ unless m(P) = kappa and
  q(P) = 0, in which case b = R and mu(P) <= 1. With a+b >= 8, (5-a)^+ + (5-b)^+ <= 5 (if a, b <= 5 it is 10-(a+b) <= 2;
  otherwise one term is 0). So X <= 5, or X <= 1+5, or X <= 5+1, or X <= 2: always X <= 6.
 (F1b) If m(P) = kappa-1 and m(P u {i}) = kappa, then X, Y <= 6 (lambda, mu <= 3 at m in {kappa-1,kappa}).
 So every such d lies in [-(D0+6), D0+10]. Two such values for the same i are congruent mod 2p (p odd) and differ by at
 most 2D0+16 <= 4kappa+4 < 8kappa-10 = 2p (kappa >= 4). So they are equal, and d = theta_i for every pair of type (F1a)
 or (F1b). In particular theta_i = hh_i (mod p), theta_i = sigma_i (mod 2) and -(D0+6) <= theta_i <= D0+10, so
 |theta_i| < 2p.
 Empty runs. If run e is empty, then X_e = 0 and sigma_e = 0, so theta_e = tau_e = y_e - y_(e-1) (mod p), which is
 nonzero mod p by the empty-run rule; theta_e is even and |theta_e| < 2p, and the only even multiple of p in (-2p,2p) is
 0. So theta_e is a NONZERO EVEN integer. (E1)
(F2) Connectivity of Fp. Call P, P' in Fp neighbours if they differ in exactly one run.
 (a) If P in Fp has a maximal interval [x,y] with x != y, then P\{y} is in Fp. Repeating, every P in Fp is joined to an
     independent set of kappa+1 runs.
 (b) For an independent V = {v_1,...,v_(kappa+1)} in cyclic order, let g_j >= 1 be the number of runs strictly between v_j
     and v_(j+1) (v_(kappa+2) := v_1); sum_j g_j = N-kappa-1 = 3kappa-5. Suppose g_j >= 2. Then V u {v_(j+1)-1} is in Fp
     (it has the interval {v_(j+1)-1, v_(j+1)}, and v_(j+1)-1 is not adjacent to v_j), and so is the independent set
     (V\{v_(j+1)}) u {v_(j+1)-1}. Its gaps are those of V with g_j lowered by one and g_(j+1) raised by one.
 (c) While some g_j >= 2 with j <= kappa, move one unit from gap j to gap j+1, then on to j+2, ..., up to gap kappa+1. Every
     donor is >= 2: the first by assumption, the later ones because they have just received a unit. This ends with gaps
     (1,...,1,G), where G := 3kappa-5-kappa = 2kappa-5 >= 3; that is, V = {x,x+2,...,x+2kappa} for some x.
 (d) From V = {x,...,x+2kappa} with gaps (1,...,1,G), move v_(kappa+1), v_kappa, ..., v_1 forward by one, in this order;
     each time the gap ahead is G >= 2 or 2. The result is {x+1,...,x+2kappa+1}, again with gaps (1,...,1,G). So all
     members of Fp are joined.
(F3) For P in Cl' put Theta(P) := sum_(i in P) theta_i and f(P) := U'(P) - Theta(P). For every pair of type (F1a) or
 (F1b), f(P u {i}) = f(P). By (F2), f is a constant f0 on Fp.
(F4) f = f0 on all of Cl. (a) If m(P) = kappa and P has a maximal interval [x,y] with x != y, then m(P\{y}) = kappa;
 repeating joins P, through pairs in Cl, to an independent set J of kappa runs. (b) The complement of J has 3kappa-4 runs
 in kappa gaps. If some gap holds g >= 3 runs and follows j in J, then x := j+2 is adjacent neither to j nor to the member
 of J after the gap (distance g-1 >= 2), and J u {x} is an independent set of kappa+1 runs, in Fp. (c) Otherwise every
 gap holds at most 2 runs, so 3kappa-4 <= 2kappa: kappa = 4 and every gap holds exactly 2 runs. Pick v in J; its
 predecessor in J is v-3. Then J u {v-1} has the maximal intervals {v-1,v} and kappa-1 singletons (v-1 is not adjacent
 to v-3), so m = kappa; and J' := (J u {v-1})\{v} is an independent set of kappa runs with a gap of 3 runs (v, v+1, v+2).
 Apply (b) to J'. All steps are pairs of type (F1a), so f = f0 on every P with m(P) = kappa.
(F5) f0 = 0 [an all-kappa triple; valid for every kappa >= 4]. Let P1 := {0,3,6,...,3kappa-3} and
 P2 := {1,4,...,3kappa-2} (kappa runs each). P1 is independent: steps of 3, and the kappa-2 >= 2 runs 3kappa-2, ...,
 4kappa-5 separate 3kappa-3 from N. P2 is independent: steps of 3, and the kappa-2 runs 3kappa-1, ..., 4kappa-4 separate
 3kappa-2 from N+1. P1 and P2 are disjoint. P1 u P2 has the kappa maximal intervals {3j,3j+1} (0 <= j <= kappa-1),
 separated by the runs 3j+2 (0 <= j <= kappa-2) and by the kappa-3 >= 1 runs 3kappa-1, ..., 4kappa-5. So
 m(P1) = m(P2) = m(P1 u P2) = kappa, f = f0 on all three by (F4), and Lemma 10 with U = U'+2p = f+Theta+2p gives
   2p = U(P1)+U(P2)-U(P1 u P2) = f0 + (Theta(P1)+Theta(P2)-Theta(P1 u P2)) + 2p = f0 + 2p.
 So f0 = 0:
   U'(P) = Theta(P) for every P in Cl.                                                                       (F5)
(F6) Total. Q0 := {0,2,...,2kappa} is independent: the 2kappa-5 runs 2kappa+1, ..., N-1 separate 2kappa from N. Q0^c has
 the maximal intervals {1}, {3}, ..., {2kappa-1}, {2kappa+1,...,N-1}. So both are in Fp, and (F5) with Lemma 11 gives
   Theta(all runs) = U'(Q0) + U'(Q0^c) = B* - 2nu0 - 2p.                                                    (F6)
(F7) Sets of kappa-1 independent runs. If J is an independent set of kappa runs and a is in J, then J-a := J\{a} is a
 proper independent set of kappa-1 >= 3 runs, m(J-a) = kappa-1, and (J-a, J) is a pair of type (F1b). So
 U'(J) - U'(J-a) = theta_a, and by (F5)
   U'(J-a) = Theta(J) - theta_a = Theta(J-a).                                                                (F7)

## 5. Proof of Theorem TCW: the final count [NEW]

Assume an avoider w as in Sec. 0, and fix a frame for its NF word u (Sec. 1). S_ev := {0,2,...,4kappa-6} and
S_od := {1,3,...,4kappa-5} are complementary. Each has 2kappa-2 runs, and the runs in each are pairwise non-adjacent (N is
even). For S in {S_ev,S_od}, order its runs s_1, ..., s_(2kappa-2) with theta_(s_1) >= ... >= theta_(s_(2kappa-2)) (ties
broken arbitrarily) and put
  J_S := {s_1,...,s_kappa},  a_S := s_kappa,  t_a := theta_(a_S),  B_S := {s_(kappa+1),...,s_(2kappa-2)} (kappa-2 >= 2 runs).
Every subset Q of S with 1 <= |Q| <= 2kappa-3 is a proper independent set with m(Q) = |Q|. By (F5) and (F7),
Theta(Q) = U'(Q) for Q = J_S, for Q = J_S-a_S, and for Q = J_S-a_S+z := (J_S\{a_S}) u {z} (z in B_S); so
Theta(Q) <= up(Q) = -1-nu0+mu(Q) (Lemma 9(a)). Every run of B_S has theta <= t_a. Put
  eps_S := Theta(S) + nu0 + kappa - 1.
CLAIM. eps_(S_ev) + eps_(S_od) <= 1.
The CLAIM proves the theorem: by (F6), B* - 2nu0 - 2p = Theta(all runs) = Theta(S_ev) + Theta(S_od) <= -2nu0-2kappa+3,
so B* <= 2p-2kappa+3 = R-1, contradicting B* >= R (Lemma 4(b)). Every step used only NF, the frame inputs and (SR) for
the avoider u. So no such u exists, and hence no avoider w as in Sec. 0 exists. []
The rest of this section proves the CLAIM.
Swap inequalities. Theta(S) = Theta(J_S) + sum_(B_S) theta = Theta(J_S-a_S) + t_a + sum_(B_S) theta
= Theta(J_S-a_S+z) + t_a + sum_(B_S-z) theta, so for every z in B_S:
 (BI-1) Theta(S) <= up(J_S) + sum_(B_S) theta;
 (BI-2) Theta(S) <= up(J_S-a_S) + t_a + sum_(B_S) theta;
 (BI-3) Theta(S) <= up(J_S-a_S+z) + t_a + sum_(B_S\{z}) theta.
(E2) If t_a <= -1, every run of B_S has theta <= -1, and every EMPTY run of B_S has theta <= -2 (by (E1)). If t_a = 0,
 every run of B_S has theta <= 0, and every empty run of B_S has theta <= -2.
LEMMA 12 (empty top set). If every run of J_S is empty and up(J_S) <= 2kappa-1, then t_a <= -2 and
Theta(S) <= up(J_S) - 2(kappa-2).
Proof. If t_a >= 1, all kappa values on J_S are nonzero even (E1) and >= 1, hence >= 2, and Theta(J_S) >= 2kappa >
up(J_S). So t_a <= 0, hence t_a <= -2 (E1), and every run of B_S has theta <= -2. Use (BI-1). []
LEMMA 13 (no empty alternating set). Let lambda_X, mu_X be the (lambda,mu) values of Lemma 9(b), row m = kappa, at
q = |A|, q' = |A^c| (the values of every P with m(P) = kappa and letters(P) empty). If every run of S is empty, then
nu0 + lambda_X >= 5.
Proof. Every Q contained in S with |Q| = kappa has letters(Q) empty, so X^(Q) = X^(empty), (q(Q),q'(Q)) = (|A|,|A^c|),
and low_X := Pi0+1-lambda_X-2p <= Theta(Q) <= up_X := -1-nu0+mu_X by (F5) and Lemma 9(a). As |A^c| >= 8, mu_X <= 1 and up_X <= 0. The width is
up_X - low_X = D0+lambda_X+mu_X <= 2kappa-6+4 = 2kappa-2. Let u_1 >= ... >= u_(2kappa-2) be the theta values on S, all
nonzero even (E1). If u_kappa >= 2, the top kappa sum to >= 2kappa > up_X; so u_kappa <= -2. Let TOP := {1,...,kappa}
and BOT := {kappa-1,...,2kappa-2} (index sets, both of size kappa, meeting in {kappa-1,kappa}). If u_(kappa-1) >= 2, then
sum_TOP u - sum_BOT u = sum_(i<=kappa-2) u_i - sum_(i>=kappa+1) u_i >= 2(kappa-2)+2(kappa-2) = 4kappa-8 > 2kappa-2 >=
up_X - low_X, impossible. So u_(kappa-1) <= -2, and sum_BOT u <= -2kappa. Hence -2kappa >= low_X >= R-nu0+1-lambda_X-2p
= -2kappa+5-nu0-lambda_X (Pi0 = B*-nu0 >= R-nu0), i.e. nu0+lambda_X >= 5. []
Types of sorted sets. Call J_S "type P" if q'(J_S) <= 2, "type Q" if q(J_S) = 0 (letters(J_S) = A), and "generic"
otherwise; no set is of both types (q+q' = R >= 18). By Lemma 9(b),(c): if J_S is not type P, then mu(J_S) <= 1, with
equality iff J_S is type Q; if J_S is type P with k := q'(J_S), then mu(J_S) = 3-k and up(J_S) = 2-k-nu0.
LEMMA 14 (not type P). If J_S is not type P, then eps_S <= mu(J_S) <= 1, except that eps_S <= 3-kappa <= -1 when J_S is
type Q and A is empty.
Proof. If mu(J_S) <= 0, or J_S is type Q and nu0 >= 1, then up(J_S) <= -1, so Theta(J_S) <= -1 and t_a <= -1 (otherwise
all kappa values on J_S are >= 0). By (E2) and (BI-1), Theta(S) <= -1-nu0+mu(J_S)-(kappa-2), i.e. eps_S <= mu(J_S). If
J_S is type Q and nu0 = 0, then A is empty, letters(J_S) = A is empty, up(J_S) = 0, and Lemma 12 gives
Theta(S) <= -2(kappa-2), i.e. eps_S <= 3-kappa. []
LEMMA 15 (at most one exceptional set of each kind). (a) J_(S_ev) and J_(S_od) are not both type P. (b) If both are type
Q, then A is empty.
Proof. They are disjoint, so letters(J_(S_ev)) and letters(J_(S_od)) are disjoint. (a) Type P means
|letters(J_S) symdiff A^c| <= 2 (Lemma 4(d)); every letter of A^c lies outside at least one of the two sets, so
|A^c| <= 2+2, contrary to |A^c| >= 8. (b) letters(J_(S_ev)) = A = letters(J_(S_od)) forces A to be empty. []
LEMMA 16 (type P). If J_S is type P and J_(S') is not (S' the other alternating set), then eps_S + eps_(S') <= 1.
Proof. Write J := J_S, a := a_S, B := B_S, k := q'(J) <= 2, K1 := letters(J) n A and K2 := A^c \ letters(J); by
Lemma 4(d), |K1|+|K2| = k, and letters(J^c) = (A \ K1) u K2. Since Theta(J) >= kappa*t_a and Theta(J) <= up(J) =
2-k-nu0 <= 2 < kappa, we get t_a <= 0, and if t_a = 0 then nu0+k <= 2.
Case A: t_a <= -1. We show eps_S <= 0; with eps_(S') <= 1 (Lemma 14) this gives the CLAIM.
 (A.1) If mu(J-a) <= 1, (BI-2) and (E2) give Theta(S) <= -1-nu0+1 + t_a + (kappa-2)t_a <= -nu0-(kappa-1), i.e.
       eps_S <= 0.
 (A.2) Otherwise mu(J-a) >= 2, so q(J-a) <= 1 (Lemma 9(c), m = kappa-1). Then |letters(J-a) n A^c| <= q(J-a) <= 1
       (Lemma 4(d)), and A^c is covered by letters(J-a) n A^c, letters(a) and K2, so run a carries at least
       |A^c|-1-|K2| >= 8-3 = 5 letters of A^c. For z in B the set Q_z := J-a+z misses these letters, so q'(Q_z) >= 5
       and Q_z is not type P; hence mu(Q_z) <= 1, with equality iff letters(Q_z) = A.
       (i) If letters(Q_z) != A for some z in B, then mu(Q_z) <= 0, and (BI-3) with (E2) gives
           Theta(S) <= -1-nu0 + t_a + (kappa-3)t_a <= -1-nu0-(kappa-2): eps_S <= 0.
       (ii) Otherwise letters(J-a) u letters(z) = A for every z in B. Two distinct runs of B (kappa-2 >= 2) have disjoint
           letter sets, both equal to A \ letters(J-a); so every run of B is empty and letters(J-a) = A. Then
           mu(Q_z) = 1, and (BI-3) with (E2) (the kappa-3 runs of B\{z} are empty, theta <= -2) gives
           Theta(S) <= -nu0 + t_a - 2(kappa-3) <= -nu0-2kappa+5: eps_S <= 4-kappa <= 0.
Case B: t_a = 0. Then nu0+k <= 2. Every letter of A has |c| = 1 (odd values summing to nu0 <= 2), so |A| = nu0, and
letters(J^c) has l_c := |A|-|K1|+|K2| <= nu0+k <= 2 letters. Let n1 and n2 be the numbers of nonempty runs of B and of
S'; B and S' lie in J^c, so n1+n2 <= l_c <= 2. In the row m = kappa of Lemma 9(b) at q = |A| = nu0 in {0,1,2}:
(lambda_X,mu_X) = (3,1), (2,0), (1,-1), so nu0+lambda_X = 3 and mu_X <= 1.
 (B.1) All theta on J are >= t_a = 0, and Theta(J) <= 2-k-nu0. By (E2) and (BI-1),
       Theta(S) <= 2-k-nu0 - 2(kappa-2-n1), i.e. eps_S <= 5-k-kappa+2n1.
 (B.2) Let J' := J_(S'). If every run of J' is empty, then (lambda,mu)(J') = (lambda_X,mu_X), up(J') = -1-nu0+mu_X <= 0,
       and Lemma 12 gives eps_(S') <= mu_X+2-kappa. If J' has a nonempty run, then mu(J') <= 1, with equality only if
       letters(J') = A is nonempty (so nu0 >= 1); hence up(J') <= -1, the kappa-th value of S' is <= -1, and the kappa-2
       runs of S' \ J' contain at most n2-1 nonempty runs; (BI-1) and (E2) give eps_(S') <= mu(J') - (kappa-1-n2) <=
       2-kappa+n2. In both cases eps_(S') <= 2-kappa+max(mu_X,n2).
 (B.3) So eps_S + eps_(S') <= 7-k-2kappa+2n1+max(mu_X,n2). Over n1+n2 <= 2 and mu_X <= 1, 2n1+max(mu_X,n2) <= 5; hence
       the sum is <= 12-2kappa-k <= 0 when kappa >= 6.
 (B.4) kappa = 4 (the only kappa < 6 in the theorem). The bound reads eps_S + eps_(S') <= -1-k+2n1+max(mu_X,n2).
       n1 = 0: <= -1+2 = 1.
       n1 = 2: then n2 = 0 and every run of S' is empty; Lemma 13 would give nu0+lambda_X >= 5, but nu0+lambda_X = 3.
         Impossible.
       n1 = 1: then n2 <= 1 and the bound is <= 2-k, which is <= 1 unless k = 0. Let k = 0: K1 and K2 are empty,
         letters(J) = A^c and letters(J^c) = A. B has kappa-2 = 2 runs: z1 nonempty (its letters lie in A) and z2 empty.
         letters(J-a+z1) = (A^c \ letters(a)) u letters(z1), so q'(J-a+z1) = |letters(a)|+|letters(z1)| >= 1 and
         mu(J-a+z1) <= 2 (Lemma 9(b), m = kappa: mu = 3 only at q' = 0). (BI-3) with z = z1, t_a = 0 and
         theta_(z2) <= -2 gives Theta(S) <= -1-nu0+2-2, i.e. eps_S <= 2; and (B.2) with n2 <= 1 gives
         eps_(S') <= -2+1 = -1. So the sum is <= 1.
 This proves Lemma 16. []
Proof of the CLAIM. If neither J_(S_ev) nor J_(S_od) is type P, Lemma 14 gives eps_S <= 1 for both, and eps_S = 1 only if
J_S is type Q and A is nonempty; both cannot happen by Lemma 15(b). So the sum is <= 1. Otherwise exactly one is type P
(Lemma 15(a)), and Lemma 16 applies. []
Which inputs carry the weight. The empty-run rule enters only through (E1) (nonzero even theta of empty runs), used in
Lemmas 12-14 and in Lemma 16; the placement of the extra reflection pairs enters only through (SR) (C_max = 2m+2H).
Nonempty runs, o_F and rotation pairs are never assumed. Theorem P, CJ''', K3-11 and all USK, FCW and SCW lemmas are not
used; the all-rotations-equal sub-case (all c_l = 1, A empty, B* = R) needs no separate treatment: it is covered by the
same case analysis.

## 6. The cases (kappa,p) = (4,11) and (6,19), written out

(kappa,p) = (4,11): N = 12, R = 18, F = 24, H = 6, 2p = 22, 2p-R = 4, D0 = 20-B* <= 2.
- Lemma 1: Win_0 = [10,18], Win_1 = [8,18], Win_2 = [6,18], Win_3 = [4,16], Win_4 = [2,14], Win_5 = [0,12],
  Win_6 = [0,10]. Cl = {m in {4,5}}, Fp = {m = 5}, Cl' = {m in {3,4,5}}.
- Lemmas 2-4: every zero-sum of Y has length <= 6, so t <= 3 and L >= 12 = p+1; (S') at (k',kappa') = (10,3), with
  2p+2kappa'-k' = 18 = R; s_j <= 5; E <= 3+n- <= 6; every a_i <= 7; m1 >= (33-5t)/2 >= 9; an a-label b >= 3 gives
  m1 >= b+4; u1 >= |b_l|+4 for every letter; |A^c| >= 8.
- Lemma 5: M0 = 2Pi0+nu0-22 >= 7+E/2.
- Lemmas 6-9: a minimal representation missing at most 4 letters is single-signed. m = 4 (window [2,14]) loses values
  only when q <= 2 or q' <= 2; m = 5 (window [0,12]) only when q <= 4 or q' <= 4; m = 3 (window [4,16]) is the dual of
  m = 4. U(P) lies in [Pi0+1-lambda, 21-nu0+mu], of length 20-B*+lambda+mu <= 6 < 22.
- Lemma 10: Delta >= M0-6 >= 1 and Delta <= 44-3-B*+9 < 44. Lemma 11: the interval has length <= 48-2B* <= 12 < 22.
- (F1): Q_i = {i+1,i+3,i+5,i+7,i+9}, separated from i+13 = i+1 by i+10, i+11, i+12; Q_i u {i} has the intervals
  {i,i+1}, {i+3}, {i+5}, {i+7}, {i+9}, with the runs i+10, i+11 before i. theta_i lies in [-(D0+6), D0+10], contained in
  [-8,12]; two candidate values differ by at most 20 < 22.
- (F2): the gaps sum to 7; normal form (1,1,1,1,3). (F4): an independent 4-set leaves 8 runs in 4 gaps; if every gap
  holds 2 runs, J = {x,x+3,x+6,x+9}, then J u {x+2} (intervals {x},{x+2,x+3},{x+6},{x+9}; m = 4),
  J' = {x,x+2,x+6,x+9} (gaps 1,3,2,2) and J' u {x+4} (independent, m = 5) link J to Fp.
- (F5): P1 = {0,3,6,9}, P2 = {1,4,7,10}; P1 u P2 = {0,1},{3,4},{6,7},{9,10}, separated by 2, 5, 8, 11: all three have
  m = 4 (the SCW-type pair with a 5-run P2 would need 3kappa+2 = 14 > 12 runs). (F6): Q0 = {0,2,4,6,8},
  Q0^c = {1},{3},{5},{7},{9,10,11}.
- Sec. 5: S_ev = {0,2,...,10} and S_od = {1,3,...,11} have 6 runs each; J_S is the top 4 (m = 4), J_S-a_S has m = 3,
  B_S has 2 runs. Theta(all runs) = B*-2nu0-22 >= -4-2nu0, while the CLAIM gives Theta(all runs) <= -5-2nu0. In Case B
  with n1 = 2 the other alternating set would consist of 6 empty runs whose 4-subsets all have Theta in an interval of
  width <= 6; Lemma 13 excludes this (spread >= 8, or bottom sum <= -8 < -6 <= low_X). Conclusion: B* <= 17 < 18 = R.
So the whole cell (4,11) is excluded, including the configurations with all rotations equal (all c_l = 1, A empty,
B* = R), which need no separate treatment; CJ''' is not used.

(kappa,p) = (6,19): N = 20, R = 30, F = 44, H = 12, 2p = 38, 2p-R = 8, D0 <= 6.
- Lemma 1: Win_0 = [14,30], Win_1 = [12,30], Win_5 = [4,28], Win_6 = [2,26], Win_7 = [0,24].
- Lemmas 2-4: t <= 5, L >= 20 = p+1; (S') at (18,5), with 38+10-18 = 30 = R; s_j <= 9; E <= 7+n- <= 12; every
  a_i <= 13; m1 >= (53-5t)/2 >= 14; an a-label b >= 3 gives m1 >= b+6; u1 >= |b_l|+6; |A^c| >= 13.
- Lemma 5: margin >= 11+E/2. Lemma 9: windows of length <= 36-B*+4 <= 10 < 38. (F1): theta_i in [-12,16]; two candidate
  values differ by at most 28 < 38.
- (F1): Q_i = {i+1,i+3,...,i+13}, separated by the 7 runs i+14, ..., i+20; Q_i u {i} has the 6 runs i+14, ..., i+19
  before i. (F2): the gaps sum to 13; normal form (1,1,1,1,1,1,7). (F4): an independent 6-set leaves 14 runs in 6 gaps, so
  some gap holds >= 3 runs.
- (F5): P1 = {0,3,...,15}, P2 = {1,4,...,16}; P1 u P2 = {0,1},{3,4},...,{15,16}, separated by 2, 5, 8, 11, 14 and by
  17, 18, 19. (F6): Q0 = {0,2,...,12}, Q0^c = {1},{3},...,{11},{13,...,19}.
- Sec. 5: 10 runs per alternating set; J_S is the top 6, B_S has 4 runs. Case B is closed by (B.3) (sum <= 12-12-k <= 0).
  Conclusion: B* <= 29 < 30 = R.

## 7. Route remarks, the parent exposure, failed routes (no claims beyond Theorem TCW)

(M1) Where delta = 4 enters. With delta := 4kappa-p-1 = 4, Win_kappa = [2,R-4] and Win_(kappa+1) = [0,R-6] (Lemma 1). A
 minimal representation missing at most 4 letters is single-signed (Lemma 6(b), using u1 >= |c|+4), so values are lost
 only for patterns whose minority sign has at most 2 letters (m = kappa) or at most 4 letters (m = kappa+1), and the lost
 values are exactly listed (Lemma 7). The representative windows widen by lambda, mu <= 3 (m = kappa) and <= 5
 (m = kappa+1), with lambda+mu <= 4 (Lemma 9). These widenings are absorbed as follows: in (F1) through the coupling
 q(P u {i}) + q'(P) >= |A^c| >= 8, which bounds lambda(P u {i})+mu(P) by 6 (so |d-d'| <= 4kappa+4 < 2p even at
 kappa = 4); in the additive constant by using an all-m = kappa triple (Lemma 10 needs lambda1+lambda2+mu12 <= 9 <= M0+2);
 in complements by lambda+mu <= 4.
(M2) The parent exposure. The windows [2,R-4] and [0,R-6] are as observed. The FCW count B* <= 2p-2kappa-1 (slack
 4kappa-p = 5 against R) is FCW's count at N = 4kappa; at N = 4kappa-4 the alternating sets have 2kappa-2 runs and the
 generic count is B* <= 2p-2kappa+2 = R-2, so the slack against B* >= R is TWO units for a generic pair and the CLAIM
 needs eps_ev+eps_od <= 1. The minority-sign exceptions of the sorted sets (type P: up to 3 lost units; type Q: one unit)
 do not fit this slack directly; they are absorbed by the swap inequalities (BI-2), (BI-3), the m = kappa-1 sets J-a of
 (F7) (duality, Lemma 8), the empty-run evenness (E1) and Lemma 13 (Lemmas 14-16). At (4,11) the SCW additive-constant
 pair indeed does not fit (3kappa+2 = 14 > 12); (F5) uses an all-kappa triple instead, which fits for every kappa >= 4
 (3kappa <= 4kappa-4).
(M3) The two-sided use of windows. Upper bounds alone do not close Case B at (4,11): for nu0 = 0, k = 2, n1 = 2 and
 B* = R (all c_l = 1, one alternating set consisting of six empty runs) the one-sided estimates (B.1)-(B.2) give only
 Theta(all runs) <= -4 = B*-2p. Lemma 13 uses the LOWER end low_X of the window of all 4-subsets of that set; this is
 where the lower bounds of Lemma 9 are needed.
Failed or unused routes (kept; not premises).
(R1) A common window I* = [Pi0-4, 2p+4-nu0] for all of Cl, with Lemma 10 on mixed triples: the margin needed is 15
 against M0+3 >= 10 at kappa = 4; replaced by the tables and the all-kappa triple.
(R2) Sorting only the top kappa of each alternating set: a type-P sorted set loses up to 3 units against a slack of 1;
 replaced by Lemma 16.
(R3) Fullness-based frameworks (K3 Lemma FULL, P11R), USK's full-window family, CJ''' and Theorem P are not used.

## 8. Scope and interface table

Claimed: Theorem TCW, i.e. for every integer kappa >= 4 with p = 4kappa-5 prime, the terminal cell k = p+1,
kappa_hat = kappa is excluded under the full existential-NF/word antecedent; in particular the cells (4,11) and (6,19)
are excluded. Lemmas 1-16 and (F1)-(F7) are proved only at p = 4kappa-5, kappa >= 4, in this frame.
NOT claimed: any p not of the form 4kappa-5 (in particular the FCW case p = 4kappa-1, the SCW case p = 4kappa-3, and every
deficiency delta = 4kappa-p-1 other than 4); any statement for general delta; kappa_hat = 0 (the separate K0T verdict) or
any other kappa_hat; p = 7; other middle-range or upper-half cells; nonterminal k; reflection rigidity; INV*; o_F
assembly; full ordered Olson; any multiset-only statement outside the antecedent; novelty, priority, "first", Lean or
human review. No USK, K3, FCW or SCW statement is extended beyond its own scope, and no FCW or SCW lemma is a premise.
Aroot=/Users/jinleic/repos/aifours; R16=Aroot/institute/runs/six-lane-2026-10-16/review;
R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review;
ROT=Aroot/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation;
PL=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-terminal-cell/proof-LOWER-v1.md;
FBP=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/evidence;
CONT=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations.
| Input | Path; whole-file SHA256 | LF lines | Scope; use here |
|---|---|---|---|
| K1 verdict | R18/olson-LOWER-K1-parent-verdict-v1.md; 93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83 | 1-22 | PL Secs. 2-7 accepted relative to their inputs; only Secs. 2, 4-6 used |
| LOWER parent erratum | R18/olson-LOWER-parent-erratum-v1.md; 087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377 | 1-10 | m(P) = half the sign transitions; theta only through explicit pairs ((F1)) |
| PL | PL; 251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d | 40-129 (used: 40-50, 61-83, 93-104) | (SR); IF(a) and the gamma-normalisation; the SS bijection (through Lemma 4(a)); LT (re-derived). PL's S1(a)/FB-E/Setting-fact steps in IF(b) and its Lemmas D, U, A, C, THETA are NOT imported |
| NF | ROT/proof-ROT-few-E-v4.md; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | 28-43 | some admissible NF; odd blocks; empty-run rule |
| GRX | ROT/notes-GRX-v1.md; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | 7-20 | if-direction, through (SR) |
| (S1) definition | R16/olson-zx-s1c-parent-verdict-v1.md; 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af | 19 | the definition "(S1) bounds every zero-sum length by 2kappa" only; S1(a) NOT used (Lemma 2(b) is direct) |
| SC0 | R16/olson-index-one-primary-statement-parent-v1.md; e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6 | 1-11 | 1-element basis of a minimal zero-sum sequence of length >= floor(n/2)+2 over C_n, n >= 3; applied to Y'z (Lemma 2(c)) |
| ZSTRUCT, FB in (S') | R18/olson-FB-parent-verdict-v1.md 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a (1-16); FBP/proof-FB-v1.md 339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b (9-24); FBP/proof-FB-v1-erratum-1.md 33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202 (1-7, no statement change); (S') extension R18/olson-balfull-rotzb-parent-verdict-v1.md 56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0 (26-34) | as listed | Lemma 2(d), t >= 1 only, at (k',kappa') = (p-1,kappa-1): Z-shape, n- >= 1, balance, W+n+ <= 2p-1. FB-E NOT used |
| context only | R18/olson-FCW-parent-verdict-v1.md b28837c9c8a9549b99a6c2205e8bbe40d65ab1aad265595c511395d4c1738f71 (1-24) with R18/olson-FCW-parent-erratum-v1.md e56bf0f337d7d670be99075829217431cf605437320dd3414cde75c3d1ae2413 (1-14); CONT/lowerhalf-first-cut-window-boundary/proof-FCW-v1.md c23fd0378f68611070e3bf0fd74d66d1f7ad859bb01ccc1af4ce9a77cf4aaecf (accepted only at p = 4kappa-1; methods re-derived); R18/olson-USK-parent-verdict-v1.md 6d3358ce3f1e9e95a366f2b32f10adbc73df607bc62723f561567dce1a53de18 (1-30); R18/olson-K0T-parent-verdict-v1.md 4a2a2ffd8d8624c33c0f7cc1265cf679c18ac3a9c63565bc093b2e8afc8bf8ba (1-20) | as listed | not premises |
| untrusted context | CONT/lowerhalf-second-cut-window/proof-SCW-v1.md 6a1965aecf599e00b512ca1df36127d21e5bac21bea7ac0da5804092245f3650 | whole | methods re-derived at p = 4kappa-5; never a premise |
Not used: S1(a); the Setting fact; FB-E; Theorem P (PL Sec. 3); B0S-CJ'''; K3-11; PL Lemmas D, U, A, C, THETA and PL Secs.
7-9; every USK, K3, FCW and SCW lemma; P11R and every other unreviewed candidate.
Machine steps for this file: /bin/date, shasum -a 256, wc -c -l, reading files, and exclusive creation (Python
open(path,'x')) of this text, drafted by hand in memory (one in-memory sentence replacement before creation; no
assertion of any kind).
