# USK: the lower-half terminal cells 3 <= kappa_hat <= floor((p-1)/4) are excluded, uniformly in p, v1

Owner OlsonUniformSmallKappa. Written after /bin/date 2026-10-20T00:49:13-0700. Status: CANDIDATE_UNVERIFIED written proof of the FULL
frozen target (USK-scope-v1.md SHA256 fabc84fbe78dc978cb7164da1ecd34ed62925f3c2c178984b1669dac1eeec17e, frozen
2026-10-20T00:25:01-0700 before derivation; USK-scope-addendum-1.md SHA256
2dca26393f971953a4b6cb892430af185b0676f0960f0148b5d698dc0ba4d550; authority
RUN/control/written-olson-uniform-small-kappa-transition-v1.json SHA256
3ea785068797a0e0939d9c9130cee764a2774219717d8f7901cd7147919cb4ca). LABELLED PARTIAL of ordered Olson: one family of terminal
lower-half cells. All case work is by hand; no script, assertion, enumeration or computation over scientific data. No
novelty, priority, Lean or human-review claim; no other cell; no full ordered Olson.

## 0. Statement

THEOREM USK [NEW]. Let p be prime and kappa an integer with 3 <= kappa <= floor((p-1)/4) (so p >= 4kappa+1 >= 13). No word w
of length 4p-2 over D_(2p) without an identity 2p-subword in increasing original index order has an admissible normal form
(NF) with terminal k=p+1 and kappa_hat=kappa. Full antecedent: SOME admissible NF; the H=p-1-kappa extra reflection pairs lie
anywhere in the odd blocks; every empty NF run separates different reflection values; no o_F, nonempty-run, rotation-pair or
reflection-rigidity hypothesis on w.
Route [NEW at this range]: Lemma W (windows), Lemma IF* (integer frame, prerequisites explicit), Lemma D* (density), Lemma N
(negative letters; lift inequality), Lemma F (lift framework on the family m=kappa+1), Lemma RIG (rigidity with tight data),
Sec. 5 (one selection with m=kappa). Sec. 6 writes out the endpoint p=4kappa+1 and the case (kappa,p)=(3,13).
Exposure. Read after the freeze, as context only: proof-K2-v1.md (+ erratum 1), proof-K3-v1.md and, via Main's IRC, the K3
parent verdict and erratum. Methods re-used and re-derived here for general kappa: the full-pair shape in (F2), the gap
moves in (F3), the sets in (F4)/(F5), the sorting in RIG. Different from K2/K3: the label-count proof of the lift
inequality (Lemma N(a)), the general zero-sum count (Lemma N(b),(c)) and the single final selection of Sec. 5.
proof-P11R-v1.md was not read.

## 1. Frame [PL Secs. 2, 4-7, accepted via the K1 verdict, read with the LOWER parent erratum; prerequisites explicit]

PL = proof-LOWER-v1.md (pinned in Sec. 7). Its standing range, p>=11 prime and 1<=kappa<=(p-3)/2, contains ours, since
(p-1)/4 <= (p-3)/2 for p>=5. N=p+1 runs, R=p-1+2kappa rotation letters (R is even), F=3p-1-2kappa reflections, H=p-1-kappa.
As 4kappa <= p-1, we have R <= 2p-2 and 2kappa <= (p-1)/2.
Word form [NF, GRX; PL Sec. 2]. The NF word u is an avoider of length 4p-2 with the rotation multiset of w. Read it
cyclically as R_0 S_0 R_1 S_1 ... R_p S_p: run R_i has r_i >= 0 letters, S_i = sigma_(y_i)^(l_i) with l_i odd and
sum (l_i-1)/2 = H, and an EMPTY run R_i has y_(i-1) != y_i (indices mod N). Put tau_i := y_i - y_(i-1). For a set P of runs,
m(P) is half the number of sign transitions of the pattern (-1 on P, +1 off P). So m(empty) = m(all runs) = 0, and a proper
nonempty P has m(P) equal to its number of maximal cyclic intervals. T(P) := sum_(i in P) tau_i, and X^(P) is the list of
letter values with every letter of a run of P negated.
(SR) [PL Sec. 2, from the GRX if-direction] For every P and every even n with max(0,2kappa+2-2m(P)) <= n <= min(R,2p-2m(P)),
 T(P) is not a sum (in Z_p) of n letters of X^(P). Write W_m for this set of n when m(P)=m.

LEMMA W (windows; all intervals consist of even integers). (a) W_0 = [2kappa+2,R] and W_1 = [2kappa,R]. (b) W_kappa = [2,R].
(c) W_(kappa+1) = [0,min(R,2p-2kappa-2)], which equals [0,R] iff p >= 4kappa+1, i.e. iff kappa <= floor((p-1)/4).
(d) For m >= kappa+1, W_m = [0,R] iff m <= (p+1)/2-kappa. At the endpoint p=4kappa+1, only m=kappa+1 qualifies.
Proof. (a) R <= 2p-2. (b) R <= 2p-2kappa iff p >= 4kappa-1. (c) R <= 2p-2kappa-2 iff p-1+2kappa <= 2p-2kappa-2 iff
p >= 4kappa+1. (d) R <= 2p-2m iff 2m <= p+1-2kappa. []

LEMMA IF* (integer frame). (a) [PL IF(a)] The N block values lie in Z_p, so y_c = y_c' for some c != c'. The arc P0 := runs
c+1,...,c' is proper and nonempty with T(P0) = y_c' - y_c = 0, and its complementary arc C0 has T(C0) = 0.
(b) [DIRECT; replaces PL's S1(a) citation] Let Y be the sequence of the R elements (1,x) of Z_2 x Z_p = C_(2p), one for each
letter x of X^(P0). A zero-sum of Y is a set of n letters of X^(P0) with sum 0 = T(P0) and n even, and n <= |Y| = R. (SR) at
P0 (m=1, W_1 = [2kappa,R]) excludes every even n in [2kappa,R]. So every zero-sum of Y has length <= 2kappa-2.
(c) Let Z be a LONGEST zero-sum of Y, |Z| = 2t with 0 <= t <= kappa-1. Then Y' := Y - Z is zero-sum free (a nonempty
zero-sum of Y' would extend Z) and has length L = R-2t >= p+1. By SC0, Y' has an index-<1 generator g: Y' = (a_1 g)...(a_L g)
with least positive coefficients a_i and W := sum a_i <= 2p-1. Since g generates C_(2p) and every term is odd,
g = (1,gamma) with gamma != 0, and every a_i is odd.
(d) If t=0, put n+ = n- = 0. If t >= 1, Y lies in setting (S') with (k',kappa') = (p-1,kappa-1): p >= 5 is prime,
1 <= k' <= p-1, kappa' is an integer with 1 <= kappa' < p, Y consists of 2p+2kappa'-k' = R odd elements, every zero-sum of Y
has length <= 2kappa' (this is (b)), Z is longest with t <= kappa', L = R-2t >= 2p-k' = p+1, and g is an index-<1 generator
of Y-Z. ZSTRUCT (accepted in (S') through its proof, BAL-full overlay 5) gives Z = g^(n+) (-s_1 g)...(-s_(n-) g) with odd
s_j, 1 <= s_j <= 2t-1, n+ + n- = 2t and n- >= 1. Lemma FB gives the balance sum_j s_j = n+ and W + n+ <= 2p-1. Hence
n- <= n+, n- <= t <= kappa-1 and s_j <= 2kappa-3. In both cases W + n+ <= 2p-1.
(e) Labels. Each letter l gets an odd integer label b_l, and its value in X^(P0) is b_l*gamma. The multiset {b_l} is
{a_1,...,a_L} u {1 (n+ times)} u {-s_1,...,-s_(n-)}. Put E := W-L = sum_i (a_i-1) >= 0 and m1 := #{i : a_i = 1}.
(f) Direct counts. From L = R-n+-n- and W + n+ <= 2p-1 we get E <= 2p-1-R+n- = p-2kappa+n- <= p-kappa-1. So every
a_i <= 1+E <= p-kappa. Each a_i > 1 adds at least 2 to E, so m1 >= L-E/2 >= (p+1)-(p-kappa-1)/2 = (p+kappa+3)/2.
Normalisation [PL Sec. 4]. (v,eps) -> (gamma^(-1)v,eps) is an automorphism of D_(2p) that preserves identity subwords, the
run/block structure and (SR), so take gamma = 1. Put c_l := b_l for l in C0 and c_l := -b_l for l in P0. The original value
of l is c_l (mod p), and its value in X^(P) is eps_l c_l, where eps_l = -1 iff l lies in a run of P.
Light side [PL Lemma LT]. Let o(Q) := #{letters of runs of Q with b=1}. (SR) at the empty pattern (n = 2kappa+2 lies in W_0)
forbids having kappa+1 such letters in C0 (value +1) together with kappa+1 in P0 (value -1). So min(o(P0),o(C0)) <= kappa.
Exchanging P0 and C0 keeps the labels and replaces g by -g (the sequence of C0 is -Y), and (a)-(f) hold verbatim. Fix P0
with o(P0) <= kappa.
Quantities. Pi0 and nu0 are the sums of |c_l| over c_l > 0 and over c_l < 0. B* := Pi0+nu0 = sum|b_l| = W+2n+ = R+E+n+-n-.
sigma(P) := sum of c_l over the letters of runs of P. X_i := sum of the values of run i, so X_i = sigma({i}) (mod p).
h_i := tau_i + X_i, and H(P) := sum_(i in P) h_i = T(P)+sigma(P) (mod p).
Frame quantifier. (a)-(f) hold for EVERY admissible choice of P0, Z, g and light side. The proof below fixes one such frame;
one always exists.

LEMMA D* (density; PL Lemma D with the label bound re-derived). Every integer of [0,B*] is a sum of a sub-multiset of
A := {|c_l|}. Also B* >= R, with equality iff every |c_l| = 1.
Proof. A contains u1 >= m1 ones. Every element of A is <= m1+1. For an s_j: s_j <= 2kappa-3 <= (p+kappa+3)/2+1 <= m1+1, as
3kappa <= p+11. For the a-labels: if r := L-m1 >= 1 of them exceed 1, the largest satisfies a_max-1 <= E-2(r-1) <= L-r = m1,
because E <= p-kappa-1 <= L+r-2. Order the elements >1 increasingly, with prefix sums D_0 = 0 <= D_1 <= .... Every D_j + i
(0 <= i <= u1) is a subset sum, and D_(j+1)-D_j <= m1+1 <= u1+1, so these intervals cover [0,B*]. Finally
B* - R = E + (n+ - n-) >= 0. Equality holds iff E = 0 and n+ = n-, i.e. iff every a_i = 1 and every s_j = 1 (since
sum s_j = n+ = n-). []

Cited as stated [PL Secs. 5, 7]:
LEMMA SS. For every P, the sums sum_(l in J) eps_l c_l (J any set of letters) are exactly the integers of [-nu(P),Pi(P)].
 Each such sum has the parity of |J|, and Pi(P) = Pi0-sigma(P), nu(P) = nu0+sigma(P).
FULL. P is full if every even v in [-nu(P),Pi(P)] equals sum_(l in J) eps_l c_l for some J with |J| in W_(m(P)).
LEMMA U. If P is full, then B* <= 2p-2, and H(P) has a unique representative U(P) in [Pi0+1,2p-1-nu0] with
 U(P) = sigma(P) (mod 2). Then U'(P) := U(P)-2p lies in [Pi0+1-2p,-1-nu0].
LEMMA A. If P1 and P2 are disjoint, P1, P2 and P1 u P2 are full, and 2Pi0+3+nu0 > 2p, then U'(P1 u P2) = U'(P1)+U'(P2).
LEMMA C. If P and its complement P^c are full, then U'(P)+U'(P^c) = Pi0-nu0-2p.
PL Lemma THETA is replaced by (F2) below, as the parent erratum requires.

## 2. Lemma N: negative letters and the lift inequality [NEW at this range]

Let A- := {l : c_l < 0}, u+ := #{l : c_l = +1} and q1 := o(P0) <= kappa. The negative letters are of three types:
(i) the q1 letters of P0 with b = 1 (c = -1); (ii) letters of P0 whose label is an a-label B >= 3 (c = -B), say with labels
B_1,...,B_r'; (iii) letters of C0 with label -s_j (c = -s_j). Letters of C0 with b > 0 and letters of P0 with b < 0 are
positive.
LEMMA N. (a) nu0 <= q1 + 3E/2 + n+, and 2Pi0+3+nu0-2p >= 2kappa+2+E/2 > 0. This is the lift inequality of Lemma A.
(b) u+ >= (p-2+6kappa-3n- + sum_k (B_k-3))/2 - q1 >= (5kappa+2)/2.
(c) Every negative letter has |c| <= 2kappa-1, and |A-| + nu0 <= 2kappa. Hence nu0 <= 2kappa-1, which gives the lift
 inequality a second time, independently of (a): 2Pi0+3+nu0-2p = 2B*+3-nu0-2p >= 2R+3-(2kappa-1)-2p = 2kappa+2.
Proof. (a) nu0 = q1 + sum_k B_k + sum_(type iii) s_j. Each B_k-1 >= 2, so r' <= sum_k(B_k-1)/2 and
sum_k B_k <= (3/2)sum_k(B_k-1) <= 3E/2. Also sum_(type iii) s_j <= sum_j s_j = n+. Use B* = R+E+n+-n- and 2R+3-2p = 4kappa+1:
2Pi0+3+nu0-2p = 2B*+3-nu0-2p = 4kappa+1+2E+2n+-2n- -nu0 >= 3kappa+1+E/2+n+-2n- >= 3kappa+1+E/2-n- >= 2kappa+2+E/2. The
steps use q1 <= kappa, then n+ >= n-, then n- <= kappa-1.
(b) Letters of C0 with b=1 have c=+1, so u+ >= (m1+n+) - q1. The a-labels above 1 are the B_k and others, and each other one
adds >= 2 to E - sum_k(B_k-1). So m1 >= L - r' - (E - sum_k(B_k-1))/2. Insert E <= 2p-1-n+-L and L = R-n+-n-:
u+ >= (3L-2p+1+3n+ + sum_k(B_k-1) - 2r')/2 - q1 = (p-2+6kappa-3n- + sum_k(B_k-3))/2 - q1. For the last bound use p >= 4kappa+1,
n- <= kappa-1, B_k >= 3 and q1 <= kappa: (4kappa-1+6kappa-3kappa+3)/2 - kappa = (5kappa+2)/2.
(c) An INTEGER zero-sum is a set of letters whose c-values sum to 0 in Z. Its original values sum to 0 = T(empty) (mod p),
so (SR) at the empty pattern forbids it when its size is even and in W_0 = [2kappa+2,R]. For S contained in A- put
w(S) := sum_(l in S)|c_l| and x(S) := |S|+w(S); x(S) is even, since every |c_l| is odd.
 (*) If x(S) is in [2kappa+2,R] and w(S) <= u+, then S together with w(S) letters of value +1 is a forbidden integer zero-sum.
 (c1) A type (iii) letter has |c| = s_j <= 2kappa-3 (IF*(d)). Let l be of type (ii) with B >= 2kappa+1. Keeping only l's term,
 (b) gives u+ >= (p-2+6kappa-3(kappa-1)+B-3)/2 - kappa = (p-2+kappa+B)/2 >= B, as B <= p-kappa by IF*(f). Also
 x({l}) = B+1 lies in [2kappa+2,p-kappa+1], inside [2kappa+2,R]. So (*) gives a contradiction. Hence every negative letter has
 |c| <= 2kappa-1, i.e. x({l}) <= 2kappa.
 (c2) Let k1 := #{l in A- : |c_l| = 1}, so q1 <= k1. If k1 >= kappa+1, take S to be kappa+1 of them: x(S) = 2kappa+2 and
 w(S) = kappa+1 <= (5kappa+2)/2 <= u+, so (*) applies. Hence k1 <= kappa.
 (c3) Suppose x(A-) >= 2kappa+2. List A- with |c| non-decreasing, put X_j := x(first j letters), and let j* be the least j
 with X_j >= 2kappa+2. As X_(k1) = 2k1 <= 2kappa, j* >= k1+1, so B := |c| of the j*-th letter is >= 3. Since
 X_(j*-1) <= 2kappa, X_(j*) <= 2kappa+1+B <= 4kappa <= R. Let S := the first j* letters; then w(S) = X_(j*) - j* <= 2kappa+B-k1.
 If the j*-th letter has type (ii), (b) and q1 <= k1 give u+ >= (p-5+6kappa-3n-+B)/2 - k1 >= 2kappa+B-k1, because
 p-5+2kappa-3n- >= 3kappa-1 >= B. If it has type (iii), then B = s_j <= n+ - (n- - 1) = 2t-2n-+1 <= 2kappa-1-2n-, and (b)
 gives u+ >= (p-2+6kappa-3n-)/2 - k1 >= 2kappa+B-k1, because p-2+2kappa-3n- >= 6kappa-1-3n- >= 4kappa-2-4n- >= 2B. Either way
 (*) applies to S, a contradiction. Hence x(A-) = |A-|+nu0 <= 2kappa. So nu0 <= 2kappa-|A-| <= 2kappa-1 when A- is
 nonempty, and nu0 = 0 otherwise. []

## 3. Lemma F: the lift framework on F := {P : m(P) = kappa+1} [NEW at this range]

Runs are indexed mod N, and N = p+1 >= 4kappa+2. "Independent" means pairwise non-adjacent (cyclically); a proper set of j
independent runs has m = j. A proper nonempty set and its complement have the same number of maximal intervals, so F is
closed under complements.
(F1) Fullness. Every P in F is full: W_(kappa+1) consists of all even n in [0,R] (Lemma W(c)), and for every even v in
 [-nu(P),Pi(P)], Lemma SS gives J with sum v, |J| = v = 0 (mod 2) and 0 <= |J| <= R. Hence (Lemma U) B* <= 2p-2, and U' is
 defined on F with U'(P) in [Pi0+1-2p,-1-nu0], U'(P) = H(P) (mod p) and U'(P) = sigma(P) (mod 2). Lemma A applies to
 disjoint P1, P2 with P1, P2, P1 u P2 in F (its inequality is Lemma N(a)), and Lemma C applies to every P in F.
(F2) Explicit full pairs; theta. For a run i let Q_i := {i+1, i+3, ..., i+2kappa+1}. Consecutive members differ by 2, and the
 wrap gap (runs strictly between i+2kappa+1 and i+1+N) has N-2kappa-1 >= 2kappa+1 runs, so Q_i is independent and
 m(Q_i) = kappa+1. Q_i u {i} has the maximal intervals {i,i+1}, {i+3}, ..., {i+2kappa+1}, because the N-2kappa-2 >= 2kappa >= 1
 runs i+2kappa+2, ..., i-1 separate i+2kappa+1 from i. So m(Q_i u {i}) = kappa+1. Define theta_i := U'(Q_i u {i}) - U'(Q_i).
 Now take ANY full Q and Q u {i} (i not in Q). Then d := U'(Q u {i}) - U'(Q) satisfies d = h_i (mod p) and d = sigma({i})
 (mod 2), since H and sigma are additive. Also |d| <= (-1-nu0)-(Pi0+1-2p) = 2p-2-B* <= p-1-2kappa, as B* >= R. Two such
 values are congruent mod 2p and differ by at most 2p-2-4kappa < 2p, so they are equal; thus d = theta_i. In particular
 theta_i = h_i (mod p), theta_i = sigma({i}) (mod 2) and |theta_i| <= p-1-2kappa.
(F3) Connectivity. Call P, P' in F neighbours if they differ in exactly one run. Then F is connected:
 (a) If P in F has a maximal interval [x,y] with x != y, then P\{y} is in F: the interval becomes [x,y-1], and y+1 is not
     in P. Repeating, every P in F is joined to an independent set of kappa+1 runs.
 (b) For an independent V = {v_1,...,v_(kappa+1)} in cyclic order, let g_j >= 1 be the number of runs strictly between v_j
     and v_(j+1) (v_(kappa+2) := v_1); sum_j g_j = N-kappa-1. Suppose g_j >= 2. Then V u {v_(j+1)-1} is in F (its intervals
     are {v_(j+1)-1, v_(j+1)} and singletons, and v_(j+1)-1 is not adjacent to v_j). So is the independent set
     (V\{v_(j+1)}) u {v_(j+1)-1}, whose gaps are those of V with g_j lowered by one and g_(j+1) raised by one. Symmetrically,
     V u {v_j+1} and (V\{v_j}) u {v_j+1} move one unit from g_j to g_(j-1). So a unit can move from any gap >= 2 to either
     neighbouring gap.
 (c) While some g_j >= 2 with j <= kappa, move one unit from gap j to gap j+1, then on to j+2, ..., up to kappa+1. Every donor
     is >= 2: the first by assumption, the later ones because they have just received a unit. This ends with gaps
     (1,...,1,G), where G := N-2kappa-1 >= 2kappa+1; that is, V = {x,x+2,...,x+2kappa} for some x.
 (d) Start from V = {x,...,x+2kappa} with gaps (1,...,1,G). Move v_(kappa+1), v_kappa, ..., v_1 forward by one, in this order;
     each time the gap ahead is G >= 2 or 2. The result is {x+1,...,x+2kappa+1}, again with gaps (1,...,1,G). So all these
     sets are joined, and hence all members of F are joined.
(F4) Additive constant. For P in F put Theta(P) := sum_(i in P) theta_i and f(P) := U'(P) - Theta(P). For neighbours P and
 P u {i} in F, (F2) gives f(P u {i}) = f(P). By (F3), f is a constant f0 on F. Let P1 := {0,3,6,...,3kappa} and
 P2 := {1,4,...,3kappa+1} (3kappa+1 <= N-1-kappa). Both are independent: they move in steps of 3, and each wrap gap contains
 N-3kappa-1 >= kappa+1 runs. They are disjoint. P1 u P2 has the maximal intervals {3j,3j+1}, 0 <= j <= kappa; these are
 separated by the runs 3j+2 (j < kappa) and by the N-3kappa-2 >= kappa >= 1 runs 3kappa+2, ..., N-1. So P1, P2 and P1 u P2
 are in F. Lemma A (its inequality is Lemma N(a)) gives U'(P1 u P2) = U'(P1)+U'(P2), i.e.
 f0 + Theta(P1) + Theta(P2) = 2f0 + Theta(P1) + Theta(P2). So f0 = 0, and
   U'(P) = Theta(P) for every P in F.                                                                            (F4)
(F5) Complement total. Q0 := {0,2,...,2kappa} is independent: the N-2kappa-1 >= 2kappa+1 runs 2kappa+1, ..., N-1 separate
 2kappa from 0. Q0^c has the maximal intervals {1}, {3}, ..., {2kappa-1}, {2kappa+1,...,N-1}. Both are in F, so Lemma C and
 (F4) give
   Theta(all runs) = U'(Q0) + U'(Q0^c) = Pi0 - nu0 - 2p = B* - 2nu0 - 2p.                                      (F5) []

## 4. Lemma RIG: rigidity with tight data [NEW at this range]

S_ev := {0,2,...,p-1} and S_od := {1,3,...,p} are complementary. Each has M := (p+1)/2 >= 2kappa+1 runs, and the runs in each
are pairwise non-adjacent (p-1 and 0 are separated by p; p and 1 by 0). So every nonempty subset J of S_ev or S_od has
m(J) = |J|, and those with |J| = kappa+1 lie in F.
LEMMA RIG. B* = R. So every |c_l| = 1, i.e. every rotation letter of u is rho_1 or rho_-1 (after gamma -> 1), and
nu0 = |A-|. For S in {S_ev, S_od}, e_i := theta_i + 1 >= 0 for every i in S, and sum_(i in S) e_i = kappa - nu0; in
particular nu0 <= kappa.
Proof. Fix S and order its theta-values decreasingly, theta_(1) >= ... >= theta_(M). The runs carrying the top kappa+1 values
form a set J* in F, so theta_(1)+...+theta_(kappa+1) = U'(J*) <= -1-nu0 <= -1, by (F4) and Lemma U. Hence
theta_(kappa+1) <= -1 (otherwise all top kappa+1 values are >= 0). So theta_(j) <= -1 for all j >= kappa+1, and
   sum_(i in S) theta_i <= (-1-nu0) - (M-kappa-1).                                                              (R1)
Add (R1) for S_ev and S_od and use (F5): B* - 2nu0 - 2p <= -2-2nu0-(p+1)+2kappa+2, i.e. B* <= p-1+2kappa = R. Since B* >= R
(Lemma D*), B* = R. So every |c_l| = 1, and both instances of (R1) are equalities: the top kappa+1 values sum to -1-nu0, and
theta_(j) = -1 for j >= kappa+2. As M >= kappa+2, -1 = theta_(kappa+2) <= theta_(kappa+1) <= -1, so theta_(kappa+1) = -1,
theta_(1)+...+theta_(kappa) = -nu0, and every theta_(j) >= -1. Summing e = theta+1 over S gives (kappa-nu0)+0. []

## 5. Proof of Theorem USK: one selection with m = kappa [NEW]

Assume an avoider w as in Sec. 0, and fix a frame for its NF word u (Sec. 1). By Lemma RIG, every letter value is +1 or -1,
and exactly nu0 <= kappa letters have value -1. For a run i let s_i := sigma({i}), the number of +1 letters minus the
number of -1 letters of run i. Then X_i = s_i (mod p), theta_i = h_i = tau_i + s_i (mod p), and theta_i = s_i = r_i (mod 2)
by (F2). Hence for every set P of runs
   T(P) = Theta(P) - sigma(P) (mod p)   and   Theta(P) = sigma(P) (mod 2),                                         (T)
and X^(P) has exactly nu(P) = nu0 + sigma(P) letters of value -1, all others being +1 (Lemma SS with |c| = 1).
Run facts. (E1) If theta_i = -1, then r_i is odd, so run i is nonempty. (E2) If theta_i = 0, then run i is nonempty. Indeed,
an empty run has X_i = 0, so tau_i = theta_i = 0 (mod p), i.e. y_i = y_(i-1), contrary to the empty-run rule.
Selection. Fix S := S_ev (S_od works equally). Let Z_S := {i in S : e_i >= 1}, the excess support, so |Z_S| <= kappa-nu0.
Let O := S \ Z_S; these runs have theta = -1 and are nonempty by (E1). Put f := kappa - |Z_S|, so f >= nu0 >= 0, and
|O| = M - |Z_S| = f + (M-kappa) >= f+kappa+1. For O' contained in O with |O'| = f, let P(O') := Z_S u O'. Then P(O') lies in
S and has kappa runs, so m(P(O')) = kappa and its window is W_kappa = [2,R] (Lemma W(b)). Also
Theta(P(O')) = sum (e_i-1) = (kappa-nu0)-kappa = -nu0. By (T),
   T(P(O')) = -nu0 - sigma(P(O')) = -nu(P(O')) (mod p),   and   nu(P(O')) = nu0 + sigma(P(O')) = nu0 + Theta(P(O')) = 0 (mod 2).
KEY. Let P = P(O') and n := nu(P). If n >= 2, the n letters of X^(P) of value -1 have sum -n = T(P) (mod p), and n is even
with 2 <= n <= R, so n is in W_kappa. By (SR) this is an identity 2p-subword of u. Moreover, nu(P) = 0 holds iff no letter
of X^(P) has value -1, i.e. iff the set of letters of the runs of P is exactly A-.
Case (i): f >= 1. This includes every nu0 >= 1, since f >= nu0. Choose O'_1 contained in O with |O'_1| = f, a run o in O'_1,
and a run o' in O \ O'_1 (possible as |O| >= f+1). Put O'_2 := (O'_1 \ {o}) u {o'}. The run o is nonempty (E1), and its
letters lie in the runs of P(O'_1) but not in those of P(O'_2). So the two letter sets differ, at most one of them equals
A-, and the other P has nu(P) >= 2. KEY gives an identity 2p-subword.
Case (ii): f = 0. Then |Z_S| = kappa <= kappa-nu0, which forces nu0 = 0, so A- is empty. The sum of e over Z_S is kappa, with
kappa terms each >= 1, so e_i = 1 and theta_i = 0 on Z_S. These runs are nonempty by (E2). So P := Z_S has a nonempty letter
set, which is not A- = (empty set). Hence nu(P) >= 2, and KEY gives an identity 2p-subword.
By nu0. nu0 = 0 (all rotation letters equal rho_gamma; CJ''' is not needed): case (i) if f >= 1, case (ii) if f = 0, which
uses the empty-run rule through (E2). 1 <= nu0 <= kappa: case (i), which uses only (E1). nu0 >= kappa+1: impossible, by
Lemma RIG (and also by Lemma N(c)).
In every case the NF word u has an identity 2p-subword, contradicting that u is an avoider. Hence no avoider w as in Sec. 0
exists. This proves Theorem USK. []

## 6. The endpoint p = 4kappa+1 and the smallest case (kappa,p) = (3,13), written out

Endpoint p = 4kappa+1 (when prime): N = 4kappa+2, R = 6kappa, F = 10kappa+2, H = 3kappa, M = 2kappa+1.
- Windows: W_0 = [2kappa+2,6kappa]; W_1 = [2kappa,6kappa]; W_kappa = [2,6kappa] (2p-2kappa = 6kappa+2 > R); W_(kappa+1) =
  [0,6kappa], since 2p-2kappa-2 = 6kappa = R exactly; W_(kappa+2) = [0,6kappa-2]. So m = kappa+1 is the only family with
  the full window.
- Lemma IF*: L >= p+1 = 4kappa+2; E <= 2kappa+1+n- <= 3kappa; m1 >= (5kappa+4)/2; s_j <= 2kappa-3.
- Lemma N: u+ >= (5kappa+2)/2; the sets S in (c2)/(c3) have x(S) <= 4kappa <= 6kappa = R; lift margin >= 2kappa+2.
- (F2): the wrap gap of Q_i has 2kappa+1 runs, and 2kappa runs separate i+2kappa+1 from i.
- (F3): G = 2kappa+1 >= 2.
- (F4): 3kappa+1 = N-1-kappa. Each wrap gap of P1, P2 has kappa+1 runs, and the kappa >= 3 runs 3kappa+2, ..., 4kappa+1
  separate the last interval of P1 u P2 from the first.
- (F5): the last interval of Q0^c is {2kappa+1,...,4kappa+1} (2kappa+1 runs).
- RIG: M = 2kappa+1 >= kappa+2. Sec. 5: |O| >= f+kappa+1.
(kappa,p) = (3,13): N = 14, R = 18, F = 32, H = 9, M = 7.
- Windows: W_0 = [8,18], W_1 = [6,18], W_2 = [4,18], W_3 = [2,18], W_4 = [0,18], W_5 = [0,16], W_6 = [0,14], W_7 = [0,12].
  The family is F = {m = 4}.
- Lemma IF*: t <= 2, s_j <= 3, E <= 7+n- <= 9, every a_i <= 10, m1 >= 10.
- Lemma N: every negative |c| <= 5, |A-|+nu0 <= 6, u+ >= 9, lift margin >= 8.
- (F2): Q_i = {i+1,i+3,i+5,i+7}; Q_i u {i} has the intervals {i,i+1},{i+3},{i+5},{i+7}, and runs i+8,...,i+13 separate i+7
  from i.
- (F3): target gaps (1,1,1,7).
- (F4): P1 = {0,3,6,9}, P2 = {1,4,7,10}. P1 u P2 = {0,1},{3,4},{6,7},{9,10}, separated by runs 2, 5, 8 and by 11, 12, 13.
- (F5): Q0 = {0,2,4,6}; Q0^c = {1},{3},{5},{7,...,13}.
- RIG: S_ev = {0,2,...,12} and S_od = {1,3,...,13}; it sorts the top 4 of 7 values.
- Sec. 5: |Z_S| <= 3-nu0, and P(O') has 3 runs with window [2,18].
This agrees with the accepted K3 verdict at p >= 13 (context only, not used).

## 7. Failed routes, boundary remarks, scope and interface table

Failed or unused routes (kept; not premises).
(R1) K3-style unit-run selections. Take k pairwise non-adjacent singleton runs, each with one +1 letter and theta = -1. Then
 T(P) = -2k, and X^(P) has nu0+k letters of value -1. This needs kappa+1-nu0 <= k <= nu0, so nu0 >= (kappa+1)/2, and it
 needs k such runs. At p = 4kappa+1 the run counts available from the tight data guarantee only about (2/3)kappa+4 unit runs:
 the length excess 2kappa-2 and the theta excess 2(kappa-nu0) may occupy up to about (10/3)kappa runs. So this route is not
 uniform; Sec. 5 replaces it.
(R2) In Lemma N(c), a plain prefix bound fails for kappa >= 3 near p = 4kappa+1: w(S) <= 4kappa-2 against the crude
 u+ >= (p+kappa+1)/2. The refined count N(b) is needed: a large negative a-label raises u+, and the 1-letters are listed
 first. The lift inequality itself does not need (c) (Lemma N(a)).
(R3) PL Lemma CR's (H-ALT) is not used. It asks for fullness of whole alternating sets, whose window W_((p+1)/2) = [0,p-1]
 stops below R. Only (kappa+1)-subsets of S_ev and S_od are used, together with the complement total (F5).
Boundary remark (no claim). For p <= 4kappa-1 (kappa_hat > (p-1)/4, outside this target), Lemma W(c), and with it (F1),
fails: W_(kappa+1) stops at 2p-2kappa-2 < R. An m=kappa+1 pattern with single-signed X^(P), which needs all R letters for
v = +-B*, then need not be full; p=11, kappa=3 (window [0,14], R=16) is the separately recorded residual. The numerics of
Lemma N(b),(c) also use p >= 4kappa+1. This range is not analysed further here.
Scope. Claimed: Theorem USK, for every prime p and every integer kappa with 3 <= kappa <= floor((p-1)/4), under the full
existential-NF/word antecedent. Lemmas W, IF*, D*, N, F and RIG are proved only at this range, in this frame. NOT claimed:
kappa_hat <= 2 (accepted separately); kappa_hat > (p-1)/4, including p=11 with kappa_hat=3; kappa_hat = 0; p = 7; reflection
rigidity; INV*; o_F assembly; full ordered Olson; any multiset-only statement outside the antecedent.
Aroot=/Users/jinleic/repos/aifours; R16=Aroot/institute/runs/six-lane-2026-10-16/review;
R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review;
ROT=Aroot/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation;
PL=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-terminal-cell/proof-LOWER-v1.md;
FBP=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/evidence.
| Input | Text, whole-file SHA256 | Scope; use |
|---|---|---|
| K1 verdict | R18/olson-LOWER-K1-parent-verdict-v1.md; 93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83 | PL Theorem S accepted relative to its inputs |
| LOWER parent erratum | R18/olson-LOWER-parent-erratum-v1.md; 087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377 | m(P) convention; theta only via full pairs ((F2)); CR conditional (not used) |
| PL | PL Secs. 2, 4-7 (lines 40-129); 251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d | (SR); IF(a) and normalisation; the covering step of D; SS; LT; U, A, C (Sec. 1) |
| NF | ROT/proof-ROT-few-E-v4.md lines 28-43; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | some admissible NF; odd blocks; empty-run rule |
| GRX | ROT/notes-GRX-v1.md lines 7-20; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | if direction, through (SR) |
| (S1) definition | R16/olson-zx-s1c-parent-verdict-v1.md line 19; 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af | the definition "(S1) bounds every zero-sum length by 2kappa" only; S1(a) NOT used (IF*(b) is direct) |
| SC0 | R16/olson-index-one-primary-statement-parent-v1.md; e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6 | index-<1 generator of a zero-sum-free sequence of length >= p+1 in C_(2p); IF*(c) |
| ZSTRUCT, FB in (S') | R18/olson-FB-parent-verdict-v1.md 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a; FBP/proof-FB-v1.md lines 11-19, 339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b, erratum 1 33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202 (no statement change); (S') extension R18/olson-balfull-rotzb-parent-verdict-v1.md line 33, 56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0 | IF*(d), t >= 1 only: Z-shape, s_j <= 2t-1, n- >= 1, balance, W+n+ <= 2p-1 |
| context only | R18/olson-K2-parent-verdict-v1.md 5ca98c9a81b2e1607cf5f562bc276ad29ed81feb774857f1428e657293db04c7; R18/olson-K3-parent-verdict-v1.md 9281cbc64bd2bc59edf7a8404481765d5d5d39c351ce5b2b28c35b6e6e03a9f6 with R18/olson-K3-parent-erratum-v1.md 8653cb3e183a6c8d21e95e971de95b598a5a29cb94e90bb69de6173623c332af | not premises |
Not used: S1(a); the Setting fact; FB-E; Theorem P (PL Sec. 3); B0S-CJ''' (its all-equal sub-case is covered by Sec. 5);
PL Lemma THETA (replaced by (F2)); PL Secs. 8-9 (K1, CR); the K2/K3 lemmas; P11R and every other unreviewed candidate.
