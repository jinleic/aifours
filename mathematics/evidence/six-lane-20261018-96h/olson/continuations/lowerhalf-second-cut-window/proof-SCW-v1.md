# SCW: second cut window p = 4kappa-3 (kappa >= 4): the lower-half terminal cell kappa_hat = kappa is excluded, v1

Owner OlsonSecondCutWindow. Written after /bin/date 2026-10-20T02:14:43-0700. Status: CANDIDATE_UNVERIFIED written proof of the FULL
frozen target (SCW-scope-v1.md SHA256 99707df43b6a577e479444d80459b123461b55d03c827389ccac445f54e7258d, frozen
2026-10-20T02:00:53-0700 before derivation; authority RUN/control/written-olson-second-cut-window-transition-v1.json SHA256
baf55df8a92cbe40e0f469ac8a21a0d541f529abe053c94450afe5b3e959ab40). Outcome: PROVED, no failing lemma. The cells
(kappa,p) = (4,13) and (5,17) are written out in Sec. 6. LABELLED PARTIAL of ordered Olson: one family of terminal
lower-half cells. All case work is by hand; no script, assertion, enumeration or computation over scientific data. No
novelty, priority, Lean or human-review claim; no other cell; no full ordered Olson.

## 0. Statement

THEOREM SCW. Let kappa >= 4 be an integer such that p = 4kappa-3 is prime (so p = 1 mod 4 and p >= 13; (kappa,p) = (4,13),
(5,17), (8,29), (10,37), (11,41), ...). No word w of length 4p-2 over D_(2p) without an identity 2p-subword in increasing
original index order has an admissible normal form (NF) with terminal k = p+1 and kappa_hat = kappa. Full antecedent: SOME
admissible NF; the H = p-1-kappa extra reflection pairs lie anywhere in the odd blocks; every empty NF run separates
different reflection values; no o_F, nonempty-run, rotation-pair or reflection-rigidity hypothesis on w.
Route [NEW at p = 4kappa-3]: Lemma 1 (windows W_kappa = [2,R-2], W_(kappa+1) = [0,R-4]), Lemma 2 (frame), Lemma 3 (label
counts), Lemma 4 (density, signed sums), Lemma 5 (lift margin), Lemma 6 (small zero-sums), Lemma 7 (realisation: for
m = kappa+1 the number of letters of the minority sign decides what is lost), Lemma 8 (one common window
I* = [Pi0-2, 2p+2-nu0] for every pattern with m in {kappa,kappa+1}, and the exact m = kappa sub-windows), Lemmas 9-10
(additivity, complements), Lemma 11 (lift framework at N = 4kappa-2, with an additive-constant pair valid at kappa = 4),
Sec. 5 (sorting the top kappa runs of each alternating set of 2kappa-1 runs, including two single-signed sorted sets).
Methods of the unaccepted FCW candidate (p = 4kappa-1) are re-derived here at p = 4kappa-3; no FCW lemma is a premise.

## 1. Setting, windows and frame [PL Secs. 2, 4-6, accepted via the K1 verdict, read with the LOWER parent erratum]

PL = proof-LOWER-v1.md (pinned in Sec. 8). Its standing range, p >= 11 prime and 1 <= kappa <= (p-3)/2, contains every
(kappa,p) here, since kappa = (p+3)/4 <= (p-3)/2 for p >= 9. Throughout, p = 4kappa-3 and kappa >= 4. There are N = p+1 =
4kappa-2 runs (N is even) and R = p-1+2kappa = 6kappa-4 rotation letters (R is even, R >= 20); H = 3kappa-4, F = 10kappa-10,
2p = 8kappa-6. Hence 2p-R = 2kappa-2, 2p-1-R = 2kappa-3, 2R-2p = 4kappa-2 and 2p-2kappa = R-2.
Word form [NF, GRX; PL Sec. 2]. The NF word u is an avoider of length 4p-2 with the rotation multiset of w. Read it
cyclically as R_0 S_0 R_1 S_1 ... R_p S_p: run R_i has r_i >= 0 letters, S_i = sigma_(y_i)^(l_i) with l_i odd and
sum (l_i-1)/2 = H, and an EMPTY run R_i has y_(i-1) != y_i (indices mod N). Put tau_i := y_i - y_(i-1) (sum 0). For a set
P of runs, m(P) is half the number of sign transitions of the pattern (-1 on P, +1 off P) (LOWER parent erratum): m(empty)
= m(all runs) = 0, a proper nonempty P has m(P) equal to its number of maximal cyclic intervals, and m(P^c) = m(P).
T(P) := sum_(i in P) tau_i; X^(P) is the list of letter values with every letter of a run of P negated; letters(P) is the
set of letters lying in runs of P. A set of runs is independent if its members are pairwise non-adjacent (cyclically); a
proper independent set of j >= 1 runs has m = j.
(SR) [PL Sec. 2, from the GRX if-direction] For every P and every even n with max(0,2kappa+2-2m(P)) <= n <= min(R,2p-2m(P)),
 T(P) is not a sum (in Z_p) of n letters (distinct occurrences) of X^(P). Write W_m for this set of n when m(P) = m.

LEMMA 1 (windows; sets of even integers). (a) W_0 = [2kappa+2,R] and W_1 = [2kappa,R]. (b) W_kappa = [2,R-2].
(c) W_(kappa+1) = [0,R-4].
Proof. (a) 2kappa+2 <= R and 2p-2 = 8kappa-8 >= R. (b) 2kappa+2-2kappa = 2 and 2p-2kappa = R-2. (c) 2kappa+2-2(kappa+1) = 0
and 2p-2kappa-2 = R-4. []

LEMMA 2 (frame).
(a) [PL IF(a)] The N block values lie in Z_p, so y_c = y_c' for some c != c'. The arc P0 := runs c+1,...,c' is proper and
 nonempty with T(P0) = y_c' - y_c = 0, and its complementary arc C0 has T(C0) = 0.
(b) [DIRECT] Let Y be the sequence of the R elements (1,x) of Z_2 x Z_p = C_(2p), one for each letter x of X^(P0). A
 zero-sum of Y of length n is a set of n letters of X^(P0) with sum 0 = T(P0); n is even and n <= R. (SR) at P0 (m(P0) = 1,
 W_1 = [2kappa,R]) excludes every even n in [2kappa,R]. So every zero-sum of Y has length <= 2kappa-2.
(c) [SC0] Let Z be a LONGEST zero-sum of Y, |Z| = 2t with 0 <= t <= kappa-1. Then Y' := Y - Z is zero-sum free (a nonempty
 zero-sum of Y' together with Z would be longer) of length L = R-2t >= 6kappa-4-2(kappa-1) = 4kappa-2 = p+1. SC0 is read
 through the standard step: z := -sigma(Y') is nonzero, and Y'z is a minimal zero-sum sequence (a nonempty proper zero-sum
 subsequence T of Y'z would give the nonempty zero-sum T, if z is not in T, or Y'z - T, if z is in T, inside Y'). Its
 length is L+1 >= p+2 = floor(2p/2)+2, and 2p >= 3, so by SC0 it has a 1-element basis {g}: every term is x*g with least
 positive coefficient x, and the coefficients sum to ord(g). There are L+1 >= p+2 coefficients, each >= 1, so
 ord(g) >= p+2, i.e. ord(g) = 2p and g generates C_(2p). So Y' = (a_1 g)...(a_L g) with least positive coefficients a_i and
 W := sum a_i = 2p - x(z) <= 2p-1: g is an index-<1 generator of Y'. Write g = (g_1,gamma). Every term of Y' is odd, so
 a_i g_1 = 1 (mod 2): g_1 = 1 and every a_i is odd; gamma != 0 because g generates.
(d) [ZSTRUCT, FB in (S')] If t = 0, put n+ = n- = 0. If t >= 1, then Y lies in setting (S') with (k',kappa') = (p-1,kappa-1):
 p >= 5 is prime; 1 <= k' <= p-1; kappa' is an integer with 1 <= kappa' < p (kappa' >= 3); Y consists of
 2p+2kappa'-k' = p+2kappa-1 = R odd elements; every zero-sum of Y has length <= 2kappa' (this is (b), i.e. (S1) at
 kappa'); Z is longest with t <= kappa'; L = R-2t >= 2p-k' = p+1; and g is an odd index-<1 generator of Y-Z. ZSTRUCT
 (accepted in (S') through its proof) gives Z = g^(n+) (-s_1 g)...(-s_(n-) g) with odd s_j >= 1, n+ + n- = 2t and
 n- >= 1. Lemma FB gives the balance sum_j s_j = n+ and W + n+ <= 2p-1. Hence n- <= n+ (each s_j >= 1), n- <= t <= kappa-1,
 and s_j <= n+ - (n- - 1) = 2t-2n-+1 <= 2kappa-3. In both cases W + n+ <= 2p-1.
(e) Labels. Each letter l gets an odd integer label b_l, and its value in X^(P0) is b_l*gamma. The multiset {b_l} is
 {a_1,...,a_L} u {1 (n+ times)} u {-s_1,...,-s_(n-)}. Put E := W-L = sum_i (a_i-1) >= 0, m1 := #{i : a_i = 1} and
 u1 := #{l : |b_l| = 1} >= m1 + n+.

LEMMA 3 (label counts). (i) E <= 2kappa-3+n- <= 2kappa-3+t <= 3kappa-4. (ii) Every a_i <= 1+E <= 3kappa-3, and every
s_j <= min(n+, 2kappa-3). (iii) m1 >= (10kappa-5-5t)/2 >= 5kappa/2 >= 10. (iv) If some a_i equals b >= 3, then
m1 >= (5kappa-3+b)/2 and m1-b >= kappa. (v) [K] u1 >= |b_l|+4 for every letter l.
Proof. (i) L = R-n+-n- and W <= 2p-1-n+, so E = W-L <= 2p-1-R+n- = 2kappa-3+n-; and n- <= t <= kappa-1. (ii) a_i-1 <= E;
s_j <= n+-(n- -1) <= n+, and s_j <= 2kappa-3 by Lemma 2(d). (iii) Each a_i > 1 is odd, so it adds at least 2 to E; hence
L-m1 <= E/2 and m1 >= (6kappa-4-2t)-(2kappa-3+t)/2 = (10kappa-5-5t)/2, which is >= 5kappa/2 since t <= kappa-1.
(iv) That a_i adds b-1 to E and every other a-label > 1 adds at least 2, so L-m1-1 <= (E-b+1)/2 and
m1 >= (6kappa-5-2t)-(2kappa-2+t-b)/2 = (10kappa-8-5t+b)/2 >= (5kappa-3+b)/2. As b <= 3kappa-3, m1-b >= (5kappa-3-b)/2 >= kappa.
(v) If |b_l| = 1: u1 >= m1 >= 10. If b_l = a_i = b >= 3: u1 >= m1 >= b+kappa >= b+4 (here kappa >= 4 is used). If
b_l = -s_j: u1 >= m1+n+ >= 10+s_j. []
Normalisation [PL Sec. 4]. (v,eps) -> (gamma^(-1)v,eps) is an automorphism of D_(2p); it preserves identity subwords, the
run/block structure (with the empty-run rule) and (SR), with tau_i and all values scaled by gamma^(-1). So take gamma = 1.
Put c_l := b_l for l in C0 and c_l := -b_l for l in P0. The original value of l is c_l (mod p), and its value in X^(P) is
eps_l c_l, where eps_l = -1 iff l lies in a run of P.
Light side [PL Lemma LT, re-derived]. Let o(Q) := #{letters of runs of Q with b = 1}. Letters of C0 with b = 1 have
original value gamma, and letters of P0 with b = 1 have original value -gamma. If o(C0) >= kappa+1 and o(P0) >= kappa+1,
then kappa+1 of each have original values summing to 0 = T(empty), with n = 2kappa+2 in W_0 = [2kappa+2,R]; (SR) at
P = empty forbids this. So min(o(P0),o(C0)) <= kappa. Exchanging P0 and C0 keeps Lemmas 2-3 with the same labels: C0 is a
proper arc with T(C0) = 0, X^(C0) = -X^(P0), and its sequence is -Y because (1,-x) = -(1,x) in Z_2 x Z_p; the zero-sums of
-Y are those of Y, Z stays longest, and -g is an index-<1 generator of -Y' with the same coefficients (gamma -> -gamma).
Fix P0 with o(P0) <= kappa, and then apply the normalisation and the convention c = +-b to that frame.
Quantities. Pi0 and nu0 are the sums of |c_l| over c_l > 0 and over c_l < 0; A- := {l : c_l < 0}. B* := Pi0+nu0 =
sum|b_l| = W+2n+ = R+E+n+-n-. B* is even: it is a sum of R odd terms, and R is even. sigma(P) := sum of c_l over
letters(P), and sigma_i := sigma({i}). X_i := sum of the original values of run i, so X_i = sigma_i (mod p).
h_i := tau_i + X_i and H(P) := sum_(i in P) h_i = T(P)+sigma(P) (mod p).
Frame quantifier. Lemmas 2-3 and the light-side choice hold for EVERY admissible choice of P0, Z, g and light side. The
proof fixes one such frame, and one always exists.

LEMMA 4 (density and signed sums). (a) Every integer of [0,B*] is a sum of a sub-multiset of A := {|c_l|}.
(b) B* >= R, with equality iff every |c_l| = 1.
(c) [the explicit PL Sec. 5 bijection, instantiated through (a)] Fix P. Let Pos(P), Neg(P) be the letters with
 eps_l c_l > 0 and < 0, Pi(P) := sum over Pos(P) of |c| and nu(P) := sum over Neg(P) of |c|. The signed sums
 sum_(l in J) eps_l c_l over sets J of letters are exactly the integers of [-nu(P),Pi(P)], and each has the parity of
 |J|. Moreover Pi(P) = Pi0-sigma(P) and nu(P) = nu0+sigma(P).
Proof. (a) A contains u1 ones, and every element of A is <= u1+1 by Lemma 3(v). Order the elements > 1 increasingly,
with prefix sums D_0 = 0 <= D_1 <= .... Every D_j + i (0 <= i <= u1) is a subset sum, and D_(j+1)-D_j <= u1+1, so these
intervals cover [0,B*]. (b) B*-R = E+(n+-n-) >= 0, with equality iff E = 0 and n+ = n-, i.e. iff every a_i = 1 and every
s_j = 1. (c) J -> (J n Pos(P)) u (Neg(P) \ J) is a bijection on sets of letters, with sum_(l in J) eps_l c_l =
sum_(l in image)|c_l| - nu(P); apply (a) and Pi(P)+nu(P) = B*. The terms are odd. Flipping the letters of P moves their
positive weight to the negative side and conversely. []

## 2. Lemma 5: the lift margin [NEW at p = 4kappa-3]

Let q1 := o(P0) <= kappa. A letter with c < 0 is (i) one of the q1 letters of P0 with b = 1 (c = -1), or (ii) a letter of
P0 whose label is an a-label B >= 3 (c = -B), or (iii) a letter of C0 with label -s_j (c = -s_j).
LEMMA 5. nu0 <= q1 + 3E/2 + n+, and 2Pi0 + nu0 - 2p >= 2kappa-1+E/2 >= 7.
Proof. Each B >= 3 satisfies B <= (3/2)(B-1), and the numbers B-1 of type (ii) sum to at most E; the type (iii) labels sum
to at most sum_j s_j = n+. With Pi0 = B*-nu0, B* = R+E+n+-n- and 2R-2p = 4kappa-2:
2Pi0+nu0-2p = 2B*-nu0-2p >= 4kappa-2+2E+2n+-2n- -q1-3E/2-n+ = 4kappa-2+E/2+n+-2n- -q1.
Use q1 <= kappa, then n+ >= n-, then n- <= kappa-1: this is >= 2kappa-1+E/2, and 2kappa-1 >= 7 because kappa >= 4. []

## 3. Realisation and the common window [NEW]

Let C := {P : m(P) in {kappa,kappa+1}} and F := {P : m(P) = kappa+1}. Every P in C is proper and nonempty, and P^c is in C.
For P in C put q := |Neg(P)| and q' := |Pos(P)|, so q+q' = R. X^(P) is "two-signed" if q >= 1 and q' >= 1, otherwise
"single-signed": X^(P) is all positive (q = 0) iff letters(P) = A-, and all negative (q' = 0) iff letters(P^c) = A-. An even
integer v is REALISED at P if v = sum_(l in J) eps_l c_l for some set J of letters with |J| in W_(m(P)).
LEMMA 6 (small zero-sums). If X^(P) is two-signed, some set Z0 of letters with 2 <= |Z0| <= 3kappa-2 has
sum_(l in Z0) eps_l c_l = 0.
Proof. Let O1 be the u1 letters with |c| = 1. If both values +1 and -1 occur on O1, a pair is Z0. Otherwise, say every
letter of O1 has value +1 (the case -1 is symmetric). The negative value then belongs to a letter l with |c_l| = b >= 3, and
l together with b letters of O1 (u1 >= b+4, Lemma 3(v)) is Z0; b+1 <= 3kappa-2 by Lemma 3(ii). []
LEMMA 7 (realisation). Let P be in C and let v be an even integer in [-nu(P),Pi(P)].
 (a) If m(P) = kappa and X^(P) is two-signed, v is realised.
 (b) If m(P) = kappa and q = 0, v is realised whenever 2 <= v <= B*-2. If m(P) = kappa and q' = 0, v is realised whenever
     -B*+2 <= v <= -2.
 (c) If m(P) = kappa+1, q >= 3 and q' >= 3, v is realised.
 (d) If m(P) = kappa+1 and q <= 2, v is realised unless: v in {B*-2, B*} (q = 0); v = Pi(P)-1 (q = 1); v = Pi(P) (q = 2).
 (e) If m(P) = kappa+1 and q' <= 2, v is realised unless: v in {-B*, -B*+2} (q' = 0); v = -nu(P)+1 (q' = 1); v = -nu(P)
     (q' = 2).
Proof. By Lemma 4(c) some J has signed sum v; fix such a J of minimum size. |J| is even, and J contains no nonempty set of
letters with signed sum 0 (removing it would give a smaller J).
 (a) If v != 0, then |J| >= 2, and J is not the set of all letters, which contains Z0 (Lemma 6); so |J| <= R-1, hence
     |J| <= R-2, and |J| lies in [2,R-2] = W_kappa. If v = 0, Z0 has signed sum 0 and |Z0| lies in [2,3kappa-2], inside
     [2,R-2].
 (b) For q = 0 every signed sum is a sum of positive terms. If 2 <= v <= B*-2, J is not empty (v != 0) and is not the set
     of all letters (whose sum is B*), so |J| lies in [2,R-2]. The case q' = 0 is the negative of this.
 (c) If |J| <= R-4, v is realised (W_(kappa+1) = [0,R-4]). Suppose |J| >= R-2. Then J misses at most two letters, and as
     q,q' >= 3, J contains letters of both signs. If J contains a letter of value +1 and a letter of value -1, they form a
     pair with signed sum 0; impossible. Otherwise, say J contains no letter of value -1 (the case "no letter of value +1"
     is symmetric). Then all letters of value -1 are among the at most two letters missing from J, so J contains at least
     u1-2 letters of value +1. J contains a letter l of negative value -b, and b >= 3; l together with b letters of value
     +1 from J (b <= u1-4) has signed sum 0; impossible.
 (d) Suppose v is not realised. Then |J| >= R-2 and J misses at most two letters. First, J lies in Pos(P): if l in J has
     value -b < 0, then J contains at least u1-4 letters of value +1 (at most q <= 2 letters of absolute value 1 are
     negative, and at most two letters are missing), and b <= u1-4 by Lemma 3(v), so l with b of them is a subset of J with
     signed sum 0; impossible. Now |Pos(P)| = R-q.
     q = 2: J = Pos(P), so v = Pi(P).
     q = 1: |J| is even and R-2 <= |J| <= R-1, so J = Pos(P) \ {l1} and v = Pi(P)-x with x := |c_l1|. If x >= 3, remove
       from Pos(P) x letters of value +1 (Pos(P) has at least u1-1 >= x of them, none equal to l1): the result has signed
       sum v and size R-1-x <= R-4 < |J|; impossible. So x = 1 and v = Pi(P)-1.
     q = 0: Pos(P) is the set of all letters and Pi(P) = B*. Either J is the set of all letters (v = B*), or J misses two
       letters l1, l2, with x_i := |c_li| and v = B*-x1-x2. If x1+x2 >= 4, say x2 >= 3, remove from the set of all letters
       either x2+1 letters of value 1 (if x1 = 1) or l1 and x2 letters of value 1 (if x1 >= 3); there are u1 >= x2+4
       letters of value 1. The result has signed sum v and size <= R-4 < |J|; impossible. So x1 = x2 = 1 and v = B*-2.
 (e) m(P^c) = m(P) and X^(P^c) = -X^(P), so v is realised at P iff -v is realised at P^c (same J); also Pos(P^c) = Neg(P),
     Pi(P^c) = nu(P) and nu(P^c) = Pi(P). Apply (d) to P^c. []

LEMMA 8 (common window). B* <= 2p. For every P in C there is a unique integer U(P) in I* := [Pi0-2, 2p+2-nu0] with
U(P) = H(P) (mod p) and U(P) = sigma(P) (mod 2). Put U'(P) := U(P)-2p. If m(P) = kappa, then U(P) lies in [Pi0, 2p-nu0],
and in [Pi0+1, 2p-1-nu0] when X^(P) is two-signed. In particular U'(P) <= -nu0 when m(P) = kappa, and U'(P) <= -1-nu0 when
moreover X^(P) is two-signed.
Proof. Step 1 (excluded values). By (SR), T(P) != v (mod p) for every realised v, since the values of X^(P) are eps_l c_l
(mod p). As H(P) = T(P)+sigma(P) (mod p), H(P) is congruent to no integer v+sigma(P) with v realised. These integers have
the parity of sigma(P). Since -nu(P)+sigma(P) = -nu0 and Pi(P)+sigma(P) = Pi0 (Lemma 4(c)), Lemma 7 shows that they include
every integer of that parity in an interval [a,b], with a and b of that parity, as follows (for q = 1 or q' = 1, Pi(P) and
nu(P) are odd; for q, q' in {0,2} they are even; v runs over even integers):
 (A) Lemma 7(a) or 7(c): a <= 1-nu0 and b >= Pi0-1.
 (B) m(P) = kappa and q = 0 (sigma(P) = -nu0, v in [2,B*-2]) or q' = 0 (sigma(P) = Pi0, v in [-B*+2,-2]):
     [a,b] = [2-nu0, Pi0-2].
 (C) m(P) = kappa+1 and q <= 2 or q' <= 2 (Lemma 7(d),(e)):
     q = 0 (sigma(P) = -nu0, v in [0,B*-4]): [-nu0, Pi0-4];   q' = 0 (sigma(P) = Pi0, v in [-B*+4,0]): [4-nu0, Pi0];
     q = 1 (v in [-nu(P)+1, Pi(P)-3]): [1-nu0, Pi0-3];        q' = 1 (v in [-nu(P)+3, Pi(P)-1]): [3-nu0, Pi0-1];
     q = 2 (v in [-nu(P), Pi(P)-2]): [-nu0, Pi0-2];            q' = 2 (v in [-nu(P)+2, Pi(P)]): [2-nu0, Pi0].
 In every case b-a >= B*-4.
Step 2 (representative). The p integers a, a+2, ..., a+2p-2 are pairwise incongruent mod p (p is an odd prime), so H(P) is
congruent to exactly one of them, a+2j, and a+2j > b. Hence b <= a+2p-4, so B*-4 <= b-a <= 2p-4 and B* <= 2p (C is
nonempty); and a+2j lies in [b+2, a+2p-2]. That interval is contained in [Pi0+1, 2p-1-nu0] in case (A) and in
[Pi0, 2p-nu0] in case (B). In case (C) it is [Pi0-2, 2p-2-nu0] (q = 0), [Pi0-1, 2p-1-nu0] (q = 1), [Pi0, 2p-2-nu0] (q = 2),
[Pi0+2, 2p+2-nu0] (q' = 0), [Pi0+1, 2p+1-nu0] (q' = 1) or [Pi0+2, 2p-nu0] (q' = 2). All of these lie in I*.
Step 3 (uniqueness). I* has length 2p+4-B* <= 2p+4-R = 2kappa+2 < 2p. Since p is odd, the residues mod p and mod 2 fix the
residue mod 2p, and an interval of length < 2p holds at most one integer of a given residue mod 2p. So U(P) := a+2j is the
unique such integer in I*, and it lies in the sub-interval of its case; for m(P) = kappa the cases are (A) (two-signed)
and (B) (single-signed). []
LEMMA 9 (additivity). If P1 and P2 are disjoint and P1, P2, P1 u P2 are in C, then U'(P1 u P2) = U'(P1) + U'(P2).
Proof. Delta := U(P1) + U(P2) - U(P1 u P2) is 0 (mod p), since H is additive, and 0 (mod 2), since sigma is additive; so
Delta = 0 (mod 2p). By Lemma 8, Delta >= 2(Pi0-2) - (2p+2-nu0) = (2Pi0+nu0-2p) - 6 >= 1 (Lemma 5), and
Delta <= 2(2p+2-nu0) - (Pi0-2) = 4p+6-Pi0-2nu0 <= 4p+6-B* < 4p (B* >= R >= 20). So Delta = 2p. []
LEMMA 10 (complements). If P is in C, then U'(P) + U'(P^c) = Pi0 - nu0 - 2p = B* - 2nu0 - 2p.
Proof. sum_(all i) h_i = sum_i tau_i + sum_i X_i = 0 + sum_l c_l = Pi0 - nu0 (mod p), and sigma(P) + sigma(P^c) = Pi0 - nu0.
So U(P) + U(P^c) = Pi0 - nu0 (mod 2p). By Lemma 8 it lies in [2Pi0-4, 4p+4-2nu0], an interval of length 4p+8-2B* < 2p
(as B* >= R = 6kappa-4 > 4kappa+1 = p+4), which contains Pi0-nu0+2p (each end condition reads B* <= 2p+4, true by
Lemma 8). So U(P) + U(P^c) = Pi0 - nu0 + 2p. []

## 4. Lemma 11: the lift framework on C at N = 4kappa-2 [NEW]

Runs are indexed mod N = 4kappa-2.
(F1) Theta. For a run i let Q_i := {i+1, i+3, ..., i+2kappa+1} (kappa+1 runs). Consecutive members differ by 2, and the
 2kappa-3 >= 1 runs i+2kappa+2, ..., i+N separate i+2kappa+1 from i+1+N; so Q_i is independent and m(Q_i) = kappa+1. The
 run i-1 = i+4kappa-3 is not in Q_i, so Q_i u {i} has the maximal intervals {i,i+1}, {i+3}, ..., {i+2kappa+1}, and the
 2kappa-4 >= 1 runs i+2kappa+2, ..., i+4kappa-3 separate i+2kappa+1 from i; so m(Q_i u {i}) = kappa+1. Define
 theta_i := U'(Q_i u {i}) - U'(Q_i).
 Now take ANY P and P u {i} in C (i not in P). Then d := U'(P u {i}) - U'(P) satisfies d = h_i (mod p) and d = sigma_i
 (mod 2), and |d| <= 2p+4-B* <= 2kappa+2 (both values lie in I* - 2p; Lemmas 8 and 4(b)). Two such values are congruent
 mod 2p and differ by at most 4kappa+4 < 8kappa-6 = 2p. So they are equal, and d = theta_i. In particular theta_i = h_i
 (mod p), theta_i = sigma_i (mod 2) and |theta_i| <= 2kappa+2 < p.
 Empty runs. If run e is empty, then X_e = 0 and sigma_e = 0, so theta_e = tau_e = y_e - y_(e-1) (mod p), which is nonzero
 by the empty-run rule; theta_e is even and |theta_e| < p. So theta_e is a nonzero even integer.
(F2) Connectivity of F. Call P, P' in F neighbours if they differ in exactly one run.
 (a) If P in F has a maximal interval [x,y] with x != y, then P\{y} is in F. Repeating, every P in F is joined to an
     independent set of kappa+1 runs.
 (b) For an independent V = {v_1,...,v_(kappa+1)} in cyclic order, let g_j >= 1 be the number of runs strictly between v_j
     and v_(j+1) (v_(kappa+2) := v_1); sum_j g_j = N-kappa-1 = 3kappa-3. Suppose g_j >= 2. Then V u {v_(j+1)-1} is in F (it
     has the interval {v_(j+1)-1, v_(j+1)}, and v_(j+1)-1 is not adjacent to v_j), and so is the independent set
     (V\{v_(j+1)}) u {v_(j+1)-1}. Its gaps are those of V with g_j lowered by one and g_(j+1) raised by one. Symmetrically,
     through V u {v_j+1}, one unit moves from g_j to g_(j-1).
 (c) While some g_j >= 2 with j <= kappa, move one unit from gap j to gap j+1, then on to j+2, ..., up to gap kappa+1. Every
     donor is >= 2: the first by assumption, the later ones because they have just received a unit. This ends with gaps
     (1,...,1,G), where G := 3kappa-3-kappa = 2kappa-3 >= 5; that is, V = {x,x+2,...,x+2kappa} for some x.
 (d) From V = {x,...,x+2kappa} with gaps (1,...,1,G), move v_(kappa+1), v_kappa, ..., v_1 forward by one, in this order;
     each time the gap ahead is G >= 2 or 2. The result is {x+1,...,x+2kappa+1}, again with gaps (1,...,1,G). So all members
     of F are joined.
(F3) Constant on F. For P in C put Theta(P) := sum_(i in P) theta_i and f(P) := U'(P) - Theta(P). For P and P u {i} both in
 C, (F1) gives f(P u {i}) = f(P). By (F2), f is a constant f0 on F.
(F4) Link to independent kappa-sets. Let J be a set of kappa independent runs (m(J) = kappa). Its complement has 3kappa-2
 runs in kappa gaps, so some gap holds g >= 3 runs. If that gap follows j in J, then x := j+2 is adjacent neither to j
 nor to the member of J after the gap, and J u {x} is independent with kappa+1 runs, so it is in F. Both J and J u {x} are in C, so (F1) and (F3)
 give f(J) = f(J u {x}) = f0.
(F5) f0 = 0 [a pair valid at kappa = 4]. Let P1 := {0,3,6,...,3kappa-3} (kappa runs) and P2 := {1,4,...,3kappa-2} u {3kappa}
 (kappa+1 runs); 3kappa <= N-1. P1 is independent: steps of 3, and the kappa runs 3kappa-2, ..., 4kappa-3 separate 3kappa-3
 from N. P2 is independent: steps of 3, then the step 3kappa-2 -> 3kappa of 2, and the kappa-2 runs 3kappa+1, ..., 4kappa-2
 separate 3kappa from 1+N. P1 and P2 are disjoint. P1 u P2 has the maximal intervals {0,1}, {3,4}, ..., {3kappa-3,3kappa-2},
 {3kappa}, separated by the runs 3j+2 (0 <= j <= kappa-2), the run 3kappa-1, and the kappa-3 >= 1 runs 3kappa+1, ...,
 4kappa-3 (here kappa >= 4 is used). So m(P1) = kappa and m(P2) = m(P1 u P2) = kappa+1, and all three are in C. By (F4),
 f(P1) = f0; by (F3), f(P2) = f(P1 u P2) = f0; Lemma 9 gives f(P1 u P2) = f(P1) + f(P2). So f0 = 2f0 and f0 = 0:
   U'(J) = Theta(J) for every set J of kappa independent runs, and U'(P) = Theta(P) for every P in F.            (F5)
(F6) Total. Q0 := {0,2,...,2kappa} is independent: the 2kappa-3 runs 2kappa+1, ..., N-1 separate 2kappa from N. Q0^c has the
 maximal intervals {1}, {3}, ..., {2kappa-1}, {2kappa+1,...,N-1}. So both are in F, and (F5) with Lemma 10 gives
   Theta(all runs) = U'(Q0) + U'(Q0^c) = B* - 2nu0 - 2p.                                                         (F6) []

## 5. Proof of Theorem SCW: sorting the top kappa runs [NEW]

Assume an avoider w as in Sec. 0, and fix a frame for its NF word u (Sec. 1). S_ev := {0,2,...,4kappa-4} and
S_od := {1,3,...,4kappa-3} are complementary. Each has 2kappa-1 runs, and the runs in each are pairwise non-adjacent (N is
even). For S in {S_ev, S_od}, order the theta-values on S decreasingly, theta_(1) >= ... >= theta_(2kappa-1). Let J_S be the
set of runs carrying the first kappa of them (ties broken arbitrarily). J_S is a set of kappa independent runs, so
m(J_S) = kappa and Theta(J_S) = U'(J_S) by (F5). Every one of the kappa-1 runs of S \ J_S has theta <= theta_(kappa).
Call S EXCEPTIONAL if nu0 >= 1 and X^(J_S) is single-signed.
CLAIM. (i) If S is not exceptional, then sum_(i in S) theta_i <= -nu0-kappa. (ii) If S is exceptional, then
sum_(i in S) theta_i <= -nu0-kappa+1, and sum_(i in S) theta_i <= -nu0-2kappa+2 if moreover every run of S \ J_S is empty.
Proof. Case X^(J_S) two-signed. Lemma 8 gives Theta(J_S) = U'(J_S) <= -1-nu0 <= -1. Then theta_(kappa) <= -1, since
 otherwise all first kappa values are >= 0. So sum_S theta <= (-1-nu0) + (kappa-1)*theta_(kappa) <= -nu0-kappa.
Case S exceptional. Lemma 8 gives Theta(J_S) <= -nu0 <= -1. As before theta_(kappa) <= -1, and sum_S theta <= -nu0-(kappa-1).
 If every run of S \ J_S is empty, each of their theta-values is a nonzero even integer (F1) that is <= theta_(kappa) <= -1,
 hence <= -2, and sum_S theta <= -nu0-2(kappa-1).
Case X^(J_S) single-signed and nu0 = 0. Then A- is empty and Theta(J_S) <= -nu0 = 0 (Lemma 8).
 If X^(J_S) is all positive, letters(J_S) = A- is empty: every run of J_S is empty, and its theta is a nonzero even integer.
 If theta_(kappa) > 0, the first kappa values are all >= 2 and Theta(J_S) >= 2kappa > 0, which is impossible. So
 theta_(kappa) <= -2, and sum_S theta <= 0 + (kappa-1)(-2) <= -kappa = -nu0-kappa.
 If X^(J_S) is all negative, letters(J_S^c) = A- is empty: every run outside J_S is empty. theta_(kappa) <= 0, since
 otherwise Theta(J_S) >= kappa > 0. Each run of S \ J_S has a nonzero even theta <= theta_(kappa) <= 0, i.e. <= -2, so
 sum_S theta <= 0 + (kappa-1)(-2) <= -nu0-kappa. []
By (F6), B* - 2nu0 - 2p = Theta(all runs) = sum_(i in S_ev) theta_i + sum_(i in S_od) theta_i.
 - Neither set is exceptional: B* - 2nu0 - 2p <= -2nu0-2kappa, so B* <= 2p-2kappa = R-2.
 - Exactly one set is exceptional: B* <= 2p-2kappa+1 = R-1.
 - Both sets are exceptional: nu0 >= 1, and X^(J_ev), X^(J_od) are single-signed (J_ev := J_(S_ev), J_od := J_(S_od)).
   J_ev and J_od are disjoint, so letters(J_ev) and letters(J_od) are disjoint.
   (alpha) Both all positive: letters(J_ev) = A- = letters(J_od) forces A- = empty, i.e. nu0 = 0; excluded.
   (beta) Both all negative: letters(J_ev^c) = A- = letters(J_od^c) forces letters(J_ev) = letters(J_od) = empty, so A- is
     the set of all letters, Pi0 = 0 and nu0 = B*. Lemma 5 then gives B* - 2p >= 7, contradicting B* <= 2p (Lemma 8).
   (gamma) One all positive and the other all negative: letters(J_S1) = A- = letters(J_S2^c) with {S1,S2} = {S_ev,S_od}.
     J_S1 is contained in J_S2^c, so the runs of J_S2^c \ J_S1 have no letters: every run outside J_ev u J_od is empty. In
     particular every run of S_ev \ J_ev and of S_od \ J_od is empty, and CLAIM (ii) gives
     B* - 2nu0 - 2p <= -2nu0-4kappa+4, so B* <= 2p-4kappa+4 = 4kappa-2 < R.
In every case B* <= R-1. This contradicts B* >= R (Lemma 4(b)). Every step used only NF, the frame inputs and (SR) for the
avoider u. So no such u exists, and hence no avoider w as in Sec. 0 exists. This proves Theorem SCW. []
Which inputs carry the weight. The empty-run rule enters only through the empty-run fact of (F1), used in the case nu0 = 0,
in CLAIM (ii) and in case (gamma); the placement of the extra reflection pairs enters only through (SR) (C_max = 2m+2H).
Nonempty runs, o_F and rotation pairs are never assumed. Theorem P, CJ''', K3-11 and all USK and FCW lemmas are not used;
the all-rotations-equal sub-case needs no separate treatment.

## 6. The cases (kappa,p) = (4,13) and (5,17), written out

(kappa,p) = (4,13): N = 14, R = 20, F = 30, H = 8, 2p = 26.
- Lemma 1: W_0 = [10,20], W_1 = [8,20], W_2 = [6,20], W_3 = [4,20], W_4 = [2,18], W_5 = [0,16], W_6 = [0,14], W_7 = [0,12].
  C = {m in {4,5}}, F = {m = 5}.
- Lemmas 2-3: every zero-sum of Y has length <= 6, so t <= 3 and L >= 14 = p+1; (S') at (k',kappa') = (12,3), with
  2p+2kappa'-k' = 20 = R; s_j <= 5; E <= 5+n- <= 8; every a_i <= 9; m1 >= (35-5t)/2 >= 10; an a-label b >= 3 gives
  m1 >= (17+b)/2 and m1-b >= 4; u1 >= |b_l|+4 for every letter.
- Lemma 5: 2Pi0+nu0-26 >= 7+E/2. Lemma 6: |Z0| <= 10.
- Lemma 7: m = 4 uses the window [2,18], m = 5 the window [0,16]; an m = 5 pattern with q >= 3 and q' >= 3 realises every even
  v in [-nu(P),Pi(P)]; with q <= 2 it may miss only B*-2, B* (q = 0), Pi(P)-1 (q = 1) or Pi(P) (q = 2).
- Lemma 8: B* <= 26; I* = [Pi0-2, 28-nu0] has length 30-B* <= 10; for m = 4, U(P) lies in [Pi0, 26-nu0], and in
  [Pi0+1, 25-nu0] when X^(P) is two-signed. Lemma 9: 1 <= Delta <= 58-B* < 52. Lemma 10: the interval [2Pi0-4, 56-2nu0]
  has length 60-2B* <= 20 < 26.
- (F1): Q_i = {i+1,i+3,i+5,i+7,i+9}, separated from i+15 = i+1 by the 5 runs i+10, ..., i+14; Q_i u {i} has the intervals
  {i,i+1}, {i+3}, {i+5}, {i+7}, {i+9}, with the 4 runs i+10, ..., i+13 before i. |theta_i| <= 10 < 13, and two candidate
  values differ by at most 20 < 26.
- (F2): the gaps sum to 9; normal form (1,1,1,1,5). (F4): an independent 4-set leaves 10 runs in 4 gaps, so some gap holds
  >= 3 runs. (F5): P1 = {0,3,6,9}, P2 = {1,4,7,10,12}; P1 u P2 = {0,1},{3,4},{6,7},{9,10},{12}, separated by 2, 5, 8, 11 and
  13. (F6): Q0 = {0,2,4,6,8}, Q0^c = {1},{3},{5},{7},{9,...,13}.
- Sec. 5: S_ev = {0,2,...,12} and S_od = {1,3,...,13} have 7 runs each; J_S is the top 4 (m = 4, window [2,18]). Conclusion:
  B* <= 26-8 = 18 (no exceptional set), B* <= 19 (one), B* <= 14 (case (gamma)); always B* < 20 = R.
(kappa,p) = (5,17): N = 18, R = 26, F = 40, H = 11, 2p = 34.
- Lemma 1: W_0 = [12,26], W_1 = [10,26], W_4 = [4,26], W_5 = [2,24], W_6 = [0,22].
- Lemmas 2-3: t <= 4, L >= 18 = p+1; (S') at (16,4), with 34+8-16 = 26 = R; s_j <= 7; E <= 7+n- <= 11; every a_i <= 12;
  m1 >= (45-5t)/2 >= 25/2, so m1 >= 13; m1-b >= 5 for an a-label b >= 3.
- Lemma 5: margin >= 9. Lemma 8: B* <= 34, I* has length <= 12; (F1): |theta_i| <= 12 < 17, two values differ by <= 24 < 34.
- (F1): Q_i = {i+1,i+3,...,i+11}, separated by the 7 runs i+12, ..., i+18; Q_i u {i} has the 6 runs i+12, ..., i+17
  before i. (F2): the gaps sum to 12; normal form (1,1,1,1,1,7).
- (F5): P1 = {0,3,6,9,12}, P2 = {1,4,7,10,13,15}; P1 u P2 = {0,1},{3,4},{6,7},{9,10},{12,13},{15}, separated by 2, 5, 8, 11,
  14 and by 16, 17. (F6): Q0 = {0,2,...,10}, Q0^c = {1},{3},...,{9},{11,...,17}.
- Sec. 5: 9 runs per alternating set; J_S is the top 5. Conclusion: B* <= 34-10 = 24, <= 25, or <= 18; always B* < 26 = R.

## 7. Route remarks, the deficiency delta, failed routes (no claims beyond Theorem SCW)

(M1) Where delta = 2 enters. Put delta := 4kappa-p-1 (an even number, as p is odd); here delta = 2. Then
 W_kappa = [2,R-2] and W_(kappa+1) = [0,R-4] (Lemma 1). A minimal representation contains no zero-signed subset, so for a
 two-signed list it misses at least one letter; this is exactly what W_kappa = [2,R-2] needs (Lemma 7(a)). For
 m = kappa+1 a minimal representation of size R-2 or R exists only when one sign has at most two letters (Lemma 7(c)-(e)),
 and then at most two values at one end are lost. This widens the common window by two units at each end
 (I* = [Pi0-2, 2p+2-nu0], Lemma 8). The widening is absorbed by the lift margin in Lemma 9 (2kappa-1 > 6 for kappa >= 4),
 by B* > p+4 in Lemma 10 and by 4kappa+4 < 2p in (F1). Sec. 5 uses only the m = kappa sub-windows [Pi0+1, 2p-1-nu0]
 (two-signed) and [Pi0, 2p-nu0] (single-signed).
(M2) The final count. Each alternating set has N/2 = 2kappa-1 runs. Sorting the top kappa runs gives B* <= 2p-2kappa = R-2,
 plus one unit for each exceptional set (Sec. 5); case (gamma), the only way both sets can be exceptional, recovers more
 through empty runs. The parent's untrusted exposure (the FCW bound 2p-1-2kappa with slack 4kappa-p) describes FCW's count
 at N = 4kappa; here the count is the one above. The window losses it anticipated do occur (Lemma 7(d),(e)), but they
 enter only through I* in Lemmas 8-10 and (F1), where the margins of (M1) absorb them.
(M3) Optional item, general deficiency delta: NOT CLAIMED. For delta = 2e >= 4 (p = 4kappa-1-2e) the windows are
 W_kappa = [2,R-2e] and W_(kappa+1) = [0,R-2e-2]. The argument of Lemma 7(a) stops at |J| <= R-2 and does not reach the top
 R-2e of W_kappa: an m = kappa pattern whose X^(P) has between 1 and 2e-2 letters of one sign is not shown to realise
 every even value, so neither the m = kappa sub-window of Lemma 8 nor the sorted-set bound of Sec. 5 is available for such
 J_S; the m = kappa+1 losses and the margins of Lemma 9 and (F1) also change with e. No statement for delta != 2 is made
 here (delta = 0 is the separate, unaccepted FCW candidate).
Failed or unused routes (kept; not premises).
(R1) The FCW additive-constant pair {0,3,...,3kappa}, {1,4,...,3kappa+1} needs kappa+1 two-run intervals and kappa+1
 separators, 3kappa+3 <= N = 4kappa-2, i.e. kappa >= 5; it fails at kappa = 4 (15 > 14). (F5) uses a kappa-run P1 (m = kappa,
 linked to F by (F4)) and a (kappa+1)-run P2 instead.
(R2) A common window [Pi0, 2p-nu0] for all of C (the FCW shape) does not follow from Lemma 7 here: a near-single-signed
 m = kappa+1 pattern may lose up to two values at one end. Lemma 8 uses I* instead.
(R3) Fullness-based frameworks (K3 Lemma FULL, P11R) and the USK full-window family are not used.
(R4) The m = kappa-1 window W_(kappa-1) = [4,R] (2p-2(kappa-1) = R) is not used.

## 8. Scope and interface table

Claimed: Theorem SCW, i.e. for every integer kappa >= 4 with p = 4kappa-3 prime, the terminal cell k = p+1, kappa_hat = kappa
is excluded under the full existential-NF/word antecedent; in particular the cells (4,13) and (5,17) are excluded. Lemmas
1-11 are proved only at p = 4kappa-3, kappa >= 4, in this frame.
NOT claimed: any p not of the form 4kappa-3 (in particular p = 4kappa-1, the FCW candidate, and every delta = 4kappa-p-1
other than 2); any statement for general delta; kappa_hat = 0; p = 7; other middle-range cells; reflection rigidity; INV*;
o_F assembly; full ordered Olson; any multiset-only statement outside the antecedent; novelty, priority, "first", Lean or
human review. No USK, K3 or FCW statement is extended beyond its own scope, and no FCW lemma is cited as a premise.
Aroot=/Users/jinleic/repos/aifours; R16=Aroot/institute/runs/six-lane-2026-10-16/review;
R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review;
ROT=Aroot/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation;
PL=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-terminal-cell/proof-LOWER-v1.md;
FBP=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/evidence;
FCWD=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-first-cut-window-boundary.
| Input | Path; whole-file SHA256 | LF lines | Scope; use here |
|---|---|---|---|
| K1 verdict | R18/olson-LOWER-K1-parent-verdict-v1.md; 93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83 | 1-22 | PL Secs. 2-7 accepted relative to their inputs; only Secs. 2, 4-6 used |
| LOWER parent erratum | R18/olson-LOWER-parent-erratum-v1.md; 087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377 | 1-10 | m(P) = half the sign transitions; theta only through explicit pairs ((F1)) |
| PL | PL; 251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d | 40-50, 61-106 | (SR); IF(a) and the gamma-normalisation; the SS bijection (through Lemma 4(a)); LT (re-derived). PL's S1(a)/FB-E/Setting-fact steps in IF(b) and its Lemmas D, U, A, C, THETA are NOT imported |
| NF | ROT/proof-ROT-few-E-v4.md; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | 28-43 | some admissible NF; odd blocks; empty-run rule |
| GRX | ROT/notes-GRX-v1.md; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | 7-20 | if-direction, through (SR) |
| (S1) definition | R16/olson-zx-s1c-parent-verdict-v1.md; 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af | 19 | the definition "(S1) bounds every zero-sum length by 2kappa" only; S1(a) NOT used (Lemma 2(b) is direct) |
| SC0 | R16/olson-index-one-primary-statement-parent-v1.md; e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6 | 1-11 | 1-element basis of a minimal zero-sum sequence of length >= floor(n/2)+2 over C_n, n >= 3; applied to Y'z (Lemma 2(c)) |
| ZSTRUCT, FB in (S') | R18/olson-FB-parent-verdict-v1.md 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a (1-9); FBP/proof-FB-v1.md 339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b (9-20); FBP/proof-FB-v1-erratum-1.md 33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202 (1-7, no statement change); (S') extension R18/olson-balfull-rotzb-parent-verdict-v1.md 56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0 (27-33) | as listed | Lemma 2(d), t >= 1 only, at (k',kappa') = (p-1,kappa-1): Z-shape, n- >= 1, balance, W+n+ <= 2p-1. FB-E NOT used |
| context only | R18/olson-USK-parent-verdict-v1.md 6d3358ce3f1e9e95a366f2b32f10adbc73df607bc62723f561567dce1a53de18 (1-30) with errata v1 85718782c14dcb913706d5b7245ebfda1ef50ef1e9e7661d671a9ecbfcf4519e and v2 4f3a2636594787337ebe8294dc086f8a3af9dccea89d5599e95e802e95590bfe; R18/olson-K3-parent-verdict-v1.md 9281cbc64bd2bc59edf7a8404481765d5d5d39c351ce5b2b28c35b6e6e03a9f6 (1-13) with erratum 8653cb3e183a6c8d21e95e971de95b598a5a29cb94e90bb69de6173623c332af | as listed | not premises |
| untrusted context | FCWD/proof-FCW-v1.md c23fd0378f68611070e3bf0fd74d66d1f7ad859bb01ccc1af4ce9a77cf4aaecf; FCWD/review-excerpts-FCW-v1.json a3225345e84476d296357d64e6055dbfd95ad79e71521b8431969e733a53e143 | whole | methods re-derived; manifest used only to locate accepted ranges; never a premise |
Not used: S1(a); the Setting fact; FB-E; Theorem P (PL Sec. 3); B0S-CJ'''; K3-11; PL Lemmas D, U, A, C, THETA and PL Secs.
7-9; every USK, K3 and FCW lemma; P11R and every other unreviewed candidate.
