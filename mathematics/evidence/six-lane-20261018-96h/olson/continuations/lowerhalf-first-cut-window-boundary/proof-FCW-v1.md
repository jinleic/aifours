# FCW: first cut-window boundary p = 4kappa-1 (kappa >= 3): the lower-half terminal cell kappa_hat = kappa is excluded, v1

Owner OlsonUniformSmallKappa. Written after /bin/date 2026-10-20T01:37:11-0700. Status: CANDIDATE_UNVERIFIED written proof of the FULL
frozen target (FCW-scope-v1.md SHA256 dd0e5d1c7d85070f18f44815a013bb121706511e5bb2d63dd5f39b3ba92c425e, frozen
2026-10-20T01:19:12-0700 before derivation; authority
RUN/control/written-olson-first-cut-window-boundary-transition-v1.json SHA256
ba6e8038fda856125303c26a85bfac78741ab04186efa98c18f3ebe9071b02d6). The case (kappa,p) = (3,11) is covered (Sec. 6).
LABELLED PARTIAL of ordered Olson: one family of terminal lower-half cells. All case work is by hand; no script, assertion,
enumeration or computation over scientific data. No novelty, priority, Lean or human-review claim; no other cell; no full
ordered Olson.

## 0. Statement

THEOREM FCW [NEW]. Let kappa >= 3 be an integer such that p = 4kappa-1 is prime (so p >= 11; (kappa,p) = (3,11), (5,19),
(6,23), (8,31), ...). No word w of length 4p-2 over D_(2p) without an identity 2p-subword in increasing original index order
has an admissible normal form (NF) with terminal k=p+1 and kappa_hat=kappa. Full antecedent: SOME admissible NF; the
H=p-1-kappa extra reflection pairs lie anywhere in the odd blocks; every empty NF run separates different reflection
values; no o_F, nonempty-run, rotation-pair or reflection-rigidity hypothesis on w. In particular the whole cell
(kappa_hat,p) = (3,11) is excluded (Sec. 6).
Route [NEW at p=4kappa-1]: Lemma W (windows), Lemma IF* (frame), Lemma D* (density), Lemma N (lift inequality), Lemma Z
(two-signed lists have a zero-sum), Lemma U* (a common window for EVERY pattern with m in {kappa,kappa+1}, single-signed ones
included), Lemmas A* and C*, Lemma F (lift framework), Sec. 5 (sorting the top kappa runs of each alternating set).
At p = 4kappa-1 no pattern has the full window [0,R] (Lemma W(d)). Fullness is therefore replaced by Lemma U*.
Exposure. Read after the freeze, as untrusted context only: proof-P11R-v1.md. Methods re-used from my USK proof and re-derived
here at p=4kappa-1: the frame and density counts, the label count for the lift inequality, the explicit sets of (F1)-(F5),
and sorting over alternating sets. No USK lemma is a premise.

## 1. Frame [PL Secs. 2, 4-6, accepted via the K1 verdict, read with the LOWER parent erratum; bounds re-derived here]

PL = proof-LOWER-v1.md (pinned in Sec. 7). Its standing range, p>=11 prime and 1<=kappa<=(p-3)/2, contains every (kappa,p)
here, since (p+1)/4 <= (p-3)/2 for p>=7. Throughout, p = 4kappa-1 and kappa >= 3. There are N = p+1 = 4kappa runs and
R = p-1+2kappa = 6kappa-2 rotation letters (R is even). Also F = 10kappa-4 reflections, H = 3kappa-2, 2p = 8kappa-2 and
R <= 2p-2.
Word form [NF, GRX; PL Sec. 2]. The NF word u is an avoider of length 4p-2 with the rotation multiset of w. Read it
cyclically as R_0 S_0 R_1 S_1 ... R_p S_p: run R_i has r_i >= 0 letters, S_i = sigma_(y_i)^(l_i) with l_i odd and
sum (l_i-1)/2 = H, and an EMPTY run R_i has y_(i-1) != y_i (indices mod N). Put tau_i := y_i - y_(i-1). For a set P of runs,
m(P) is half the number of sign transitions of the pattern (-1 on P, +1 off P) (LOWER parent erratum). So m(empty) =
m(all runs) = 0, a proper nonempty P has m(P) equal to its number of maximal cyclic intervals, and m(P^c) = m(P).
T(P) := sum_(i in P) tau_i. X^(P) is the list of letter values with every letter of a run of P negated.
(SR) [PL Sec. 2, from the GRX if-direction] For every P and every even n with max(0,2kappa+2-2m(P)) <= n <= min(R,2p-2m(P)),
 T(P) is not a sum (in Z_p) of n letters (distinct occurrences) of X^(P). Write W_m for this set of n when m(P) = m.

LEMMA W (windows; intervals of even integers). (a) W_0 = [2kappa+2,R] and W_1 = [2kappa,R]. (b) W_kappa = [2,R].
(c) W_(kappa+1) = [0,R-2]. (d) No m has W_m = [0,R]: for m <= kappa the lower end is 2kappa+2-2m >= 2, and for
m >= kappa+1 the upper end is 2p-2m <= R-2.
Proof. (a) R <= 2p-2. (b) 2p-2kappa = 6kappa-2 = R. (c) 2p-2kappa-2 = R-2. (d) follows from (b), (c) and monotonicity. []

LEMMA IF* (integer frame).
(a) [PL IF(a)] The N block values lie in Z_p, so y_c = y_c' for some c != c'. The arc P0 := runs c+1,...,c' is proper and
 nonempty with T(P0) = y_c' - y_c = 0, and its complementary arc C0 has T(C0) = 0.
(b) [DIRECT] Let Y be the sequence of the R elements (1,x) of Z_2 x Z_p = C_(2p), one for each letter x of X^(P0). A
 zero-sum of Y is a set of n letters of X^(P0) with sum 0 = T(P0), where n is even and n <= |Y| = R. (SR) at P0 (m=1,
 W_1 = [2kappa,R]) excludes every even n in [2kappa,R]. So every zero-sum of Y has length <= 2kappa-2.
(c) [SC0] Let Z be a LONGEST zero-sum of Y, |Z| = 2t with 0 <= t <= kappa-1. Then Y' := Y - Z is zero-sum free and has
 length L = R-2t >= 4kappa = p+1. By SC0, Y' has an index-<1 generator g: Y' = (a_1 g)...(a_L g) with least positive
 coefficients a_i and W := sum a_i <= 2p-1. As every term is odd and g generates C_(2p), g = (1,gamma) with gamma != 0, and
 every a_i is odd.
(d) [ZSTRUCT, FB in (S')] If t = 0, put n+ = n- = 0. If t >= 1, then Y lies in setting (S') with
 (k',kappa') = (p-1,kappa-1): p >= 5 is prime; 1 <= k' <= p-1; kappa' is an integer with 1 <= kappa' < p; Y consists of
 2p+2kappa'-k' = R odd elements; every zero-sum of Y has length <= 2kappa' (this is (b)); Z is longest with t <= kappa';
 L = R-2t >= 2p-k' = p+1; and g is an index-<1 generator of Y-Z. ZSTRUCT (accepted in (S') through its proof) gives
 Z = g^(n+) (-s_1 g)...(-s_(n-) g) with odd s_j >= 1, n+ + n- = 2t and n- >= 1. Lemma FB gives the balance sum_j s_j = n+
 and W + n+ <= 2p-1. Hence n- <= n+, n- <= t <= kappa-1, and s_j <= n+ - (n- - 1) = 2t-2n-+1 <= 2kappa-3. In both cases
 W + n+ <= 2p-1.
(e) Labels. Each letter l gets an odd integer label b_l, and its value in X^(P0) is b_l*gamma. The multiset {b_l} is
 {a_1,...,a_L} u {1 (n+ times)} u {-s_1,...,-s_(n-)}. Put E := W-L = sum_i (a_i-1) >= 0 and m1 := #{i : a_i = 1}.
(f) Counts. From L = R-n+-n- and W + n+ <= 2p-1: E <= 2p-1-R+n- = 2kappa-1+n- <= 3kappa-2. So every a_i <= 1+E <= 3kappa-1.
 Each a_i > 1 adds at least 2 to E, so m1 >= L-E/2 >= (6kappa-2-2t) - (2kappa-1+t)/2 >= (5kappa+2)/2, using t <= kappa-1.
Normalisation [PL Sec. 4]. (v,eps) -> (gamma^(-1)v,eps) is an automorphism of D_(2p) that preserves identity subwords, the
run/block structure and (SR); so take gamma = 1. Put c_l := b_l for l in C0 and c_l := -b_l for l in P0. The original
value of l is c_l (mod p), and its value in X^(P) is eps_l c_l, where eps_l = -1 iff l lies in a run of P.
Light side [PL Lemma LT, re-derived]. Let o(Q) := #{letters of runs of Q with b=1}. If o(C0) >= kappa+1 and
o(P0) >= kappa+1, then kappa+1 letters of C0 with c=+1 and kappa+1 letters of P0 with c=-1 have original values summing to
0 = T(empty), with n = 2kappa+2 in W_0; (SR) forbids this. So min(o(P0),o(C0)) <= kappa. Exchanging P0 and C0 keeps the
labels and replaces g by -g (the sequence of C0 is -Y), so (a)-(f) hold verbatim. Fix P0 with o(P0) <= kappa, and then
apply the normalisation and the convention c = +-b to that frame.
Quantities. Pi0 and nu0 are the sums of |c_l| over c_l > 0 and over c_l < 0; A- := {l : c_l < 0}. B* := Pi0+nu0 = sum|b_l|
= W+2n+ = R+E+n+-n-. B* is even: it is a sum of R odd terms, and R is even. sigma(P) := sum of c_l over the letters of the
runs of P, and sigma_i := sigma({i}). X_i := sum of the values of run i, so X_i = sigma_i (mod p). h_i := tau_i + X_i and
H(P) := sum_(i in P) h_i = T(P)+sigma(P) (mod p). letters(P) := the set of letters lying in runs of P.
Frame quantifier. (a)-(f) hold for EVERY admissible choice of P0, Z, g and light side. The proof fixes one such frame, and
one always exists.

LEMMA D* (density). Every integer of [0,B*] is a sum of a sub-multiset of A := {|c_l|}. Also B* >= R, with equality iff every
|c_l| = 1.
Proof. A contains u1 >= m1 ones. Every element of A is <= m1+1. For an s_j: s_j <= 2kappa-3 <= (5kappa+2)/2+1 <= m1+1. For the
a-labels: if r := L-m1 >= 1 of them exceed 1, the largest satisfies a_max-1 <= E-2(r-1) <= L-r = m1, because
E <= 3kappa-2 <= L+r-2. Order the elements >1 increasingly, with prefix sums D_0 = 0 <= D_1 <= .... Every D_j + i
(0 <= i <= u1) is a subset sum, and D_(j+1)-D_j <= m1+1 <= u1+1. So these intervals cover [0,B*]. Finally
B* - R = E + (n+ - n-) >= 0, with equality iff E = 0 and n+ = n-, i.e. iff every a_i = 1 and every s_j = 1. []
LEMMA SS [the explicit PL Sec. 5 bijection, instantiated through D*]. Fix P. Let Pos(P), Neg(P) be the letters with
eps_l c_l > 0 and < 0, Pi(P) := sum over Pos(P) of |c| and nu(P) := sum over Neg(P) of |c|. The map
J -> (J n Pos(P)) u (Neg(P) \ J) is a bijection on sets of letters, with sum_(l in J) eps_l c_l = sum_(l in image)|c_l| - nu(P).
By D*, the sums sum_(l in J) eps_l c_l are exactly the integers of [-nu(P),Pi(P)]; each such sum has the parity of |J|.
Flipping the letters of P gives Pi(P) = Pi0-sigma(P) and nu(P) = nu0+sigma(P). []

## 2. Lemma N: the lift inequality [NEW at p=4kappa-1]

Let q1 := o(P0) <= kappa. A negative letter is of one of three types:
(i) one of the q1 letters of P0 with b = 1 (c = -1);
(ii) a letter of P0 whose label is an a-label B >= 3 (c = -B); call these labels B_1,...,B_r';
(iii) a letter of C0 with label -s_j (c = -s_j).
Letters of C0 with b > 0 and letters of P0 with b < 0 are positive.
LEMMA N. nu0 <= q1 + 3E/2 + n+, and 2Pi0 + nu0 - 2p >= 2kappa - 1 + E/2 > 0.
Proof. nu0 = q1 + sum_k B_k + sum_(type iii) s_j. Each B_k >= 3, so B_k <= (3/2)(B_k-1), and sum_k (B_k-1) <= E; also
sum_(type iii) s_j <= sum_j s_j = n+. With Pi0 = B* - nu0, B* = R+E+n+-n- and 2R-2p = 4kappa-2:
2Pi0 + nu0 - 2p = 2B* - nu0 - 2p >= 4kappa-2 + 2E + 2n+ - 2n- - q1 - 3E/2 - n+ = 4kappa-2 + E/2 + n+ - 2n- - q1.
Use q1 <= kappa, then n+ >= n-, then n- <= kappa-1: this is >= 3kappa-2 + E/2 - n- >= 2kappa-1 + E/2. []

## 3. A common window for every pattern with m in {kappa,kappa+1} [NEW]

Let C := {P : m(P) in {kappa,kappa+1}}. Every P in C is proper and nonempty, and P^c is in C.
"Two-signed" means that X^(P) has a positive and a negative value. X^(P) is all positive iff letters(P) = A- (every letter
of a run of P has c<0, and every other letter has c>0). It is all negative iff letters(P^c) = A-.
LEMMA Z. If X^(P) is two-signed, some nonempty set Z0 of letters has sum_(l in Z0) eps_l c_l = 0; |Z0| is even and >= 2.
Proof. Let O1 be the set of letters with |c_l| = 1. It contains the m1 letters with a-label 1. Their values in X^(P) are
+-1. If both values occur, a pair {+1,-1} is Z0. Otherwise, say all of O1 has value +1 (the case -1 is symmetric). Then
the negative value of X^(P) belongs to a letter l with |c_l| = b >= 3, and l together with b letters of O1 is Z0, provided
|O1| >= b. If b = s_j, then b <= 2kappa-3 <= (5kappa+2)/2 <= m1. If b is an a-label, each other a-label > 1 adds at least 2
to E-(b-1), so at most (E-b+1)/2 of them exist. Hence m1 >= L-1-(E-b+1)/2 >= (6kappa-3-2t) - (2kappa-1+t-b+1)/2 >=
(5kappa-1+b)/2 >= b, because n- <= t <= kappa-1 and b <= 3kappa-1. |Z0| is even, since a zero sum of odd terms has an
even number of terms. []

LEMMA U* (common window). Let P be in C. Then B* <= 2p-2, and there is a unique integer U(P) in [Pi0, 2p-nu0] with
U(P) = H(P) (mod p) and U(P) = sigma(P) (mod 2). Put U'(P) := U(P) - 2p, so U'(P) lies in [Pi0-2p, -nu0]. Moreover:
 (i) if X^(P) is two-signed, U'(P) lies in [Pi0+1-2p, -1-nu0];
 (ii) if letters(P) = A-: U'(P) lies in [Pi0+2-2p, -nu0] when m(P) = kappa, and in [Pi0-2p, -2-nu0] when m(P) = kappa+1;
 (iii) if letters(P^c) = A-: U'(P) lies in [Pi0-2p, -2-nu0] when m(P) = kappa, and in [Pi0+2-2p, -nu0] when m(P) = kappa+1.
In particular, if m(P) = kappa and letters(P) != A-, then U'(P) <= -1-nu0.
Proof. Step 1 (excluded values). Call an even v "realised at P" if v = sum_(l in J) eps_l c_l for some set J of letters
with |J| in W_(m(P)). By (SR), T(P) != v (mod p) for every realised v, since the values of X^(P) are eps_l c_l (mod p).
 (i) Every even v in [-nu(P),Pi(P)] is realised. By SS, choose J with sum v and |J| minimal. J contains no nonempty set of
     letters with signed sum 0, since removing one would give a smaller J. So J is not the set of all letters, which
     contains Z0 (Lemma Z). Hence |J| <= R-1, and |J| = v = 0 (mod 2) gives |J| <= R-2. If v != 0, then |J| >= 2, and
     [2,R-2] lies in W_kappa and in W_(kappa+1) (Lemma W). If v = 0, take Z0 (|Z0| in [2,R] = W_kappa) when m(P) = kappa,
     and J = empty (0 in W_(kappa+1)) when m(P) = kappa+1.
 (ii) letters(P) = A-: every value is |c_l| > 0, nu(P) = 0, Pi(P) = B* and sigma(P) = -nu0. For m(P) = kappa, every even
     v in [2,B*] is realised: by D*, some J has sum v, |J| = v = 0 (mod 2) and J is nonempty, so |J| is in [2,R]. For
     m(P) = kappa+1, every even v in [0,B*-2] is realised: v = 0 by J = empty, and otherwise a minimal J has |J| even and
     |J| != R (all R letters sum to B*), so |J| <= R-2.
 (iii) letters(P^c) = A-: negate (ii). Pi(P) = 0, nu(P) = B*, sigma(P) = Pi0. For m(P) = kappa every even v in [-B*,-2] is
     realised; for m(P) = kappa+1, every even v in [-B*+2,0] is realised.
Step 2 (translation). H(P) = T(P) + sigma(P) (mod p), so H(P) != v + sigma(P) (mod p) for every realised v. The numbers
v + sigma(P) are integers with the parity of sigma(P). By Step 1 they include every integer with the parity of sigma(P)
in [a,b], where:
 (i): a is the least such integer >= -nu0 and b the largest <= Pi0 (so a <= 1-nu0, b >= Pi0-1);
 (ii) with m=kappa and (iii) with m=kappa+1: (a,b) = (2-nu0, Pi0);
 (ii) with m=kappa+1 and (iii) with m=kappa: (a,b) = (-nu0, Pi0-2).
(Recall that B* is even, so Pi0 = nu0 (mod 2).) In each case a and b have the parity of sigma(P), and b - a >= B* - 2.
Step 3 (representative). The p integers a, a+2, ..., a+2p-2 are pairwise incongruent mod p, so H(P) is congruent to
exactly one of them, and not to any of them that is <= b. If b >= a+2p-2 this is impossible. Hence B*-2 < 2p-2, and since
B* is even, B* <= 2p-2. So H(P) = a+2j (mod p) for a unique a+2j in [b+2, a+2p-2], which has the parity of sigma(P). That
interval is contained in [Pi0+1, 2p-1-nu0] in case (i), in [Pi0+2, 2p-nu0] in the cases (a,b) = (2-nu0,Pi0), and in
[Pi0, 2p-2-nu0] in the cases (a,b) = (-nu0,Pi0-2). All lie in [Pi0, 2p-nu0], which has length 2p-B* < 2p. Since p is odd,
the residues mod p and mod 2 fix the residue mod 2p, and an interval of length < 2p holds at most one integer of a given
residue mod 2p. This gives uniqueness and (i)-(iii). For the last sentence: m(P) = kappa and letters(P) != A- leaves
case (i), with bound -1-nu0, or case (iii), with bound -2-nu0. []
LEMMA A* (additivity). If P1 and P2 are disjoint and P1, P2, P1 u P2 are in C, then U'(P1 u P2) = U'(P1) + U'(P2).
Proof. Delta := U(P1) + U(P2) - U(P1 u P2) = 0 (mod p), since H is additive, and = 0 (mod 2), since sigma is additive. So
Delta = 0 (mod 2p). By Lemma U*, Delta >= 2Pi0 - (2p-nu0) = 2Pi0 + nu0 - 2p > 0 (Lemma N), and
Delta <= 2(2p-nu0) - Pi0 < 4p. So Delta = 2p. []
LEMMA C* (complements). If P is in C, then U'(P) + U'(P^c) = Pi0 - nu0 - 2p = B* - 2nu0 - 2p.
Proof. sum_(all i) h_i = sum_i tau_i + sum_i X_i = 0 + sum_l c_l = Pi0 - nu0 (mod p), and sigma(P) + sigma(P^c) = Pi0 - nu0.
So U(P) + U(P^c) = Pi0 - nu0 (mod 2p), and it lies in [2Pi0, 4p-2nu0] by Lemma U*. This interval contains
Pi0 - nu0 + 2p (as B* <= 2p). It does not contain Pi0 - nu0 or Pi0 - nu0 + 4p (as B* > 0). []

## 4. Lemma F: the lift framework on C [NEW at p=4kappa-1]

Runs are indexed mod N = 4kappa. "Independent" means pairwise non-adjacent (cyclically), and a proper set of j independent
runs has m = j. Let F := {P : m(P) = kappa+1}, a subfamily of C.
(F1) Theta. For a run i let Q_i := {i+1, i+3, ..., i+2kappa+1}. Consecutive members differ by 2, and the 2kappa-1 >= 1 runs
 i+2kappa+2, ..., i+4kappa separate i+2kappa+1 from i+1+N. So Q_i is independent with m(Q_i) = kappa+1. Q_i u {i} has the
 maximal intervals {i,i+1}, {i+3}, ..., {i+2kappa+1}: the 2kappa-2 >= 1 runs i+2kappa+2, ..., i-1 separate i+2kappa+1 from i.
 So m(Q_i u {i}) = kappa+1. Define theta_i := U'(Q_i u {i}) - U'(Q_i).
 Now take ANY P and P u {i} in C (i not in P). Then d := U'(P u {i}) - U'(P) satisfies d = h_i (mod p) and d = sigma_i
 (mod 2), and |d| <= (-nu0) - (Pi0-2p) = 2p-B* <= 2p-R = 2kappa (Lemma U*, D*). Two such values are congruent mod 2p and
 differ by at most 4kappa < 2p = 8kappa-2. So they are equal, and d = theta_i. In particular theta_i = h_i (mod p),
 theta_i = sigma_i (mod 2) and |theta_i| <= 2kappa < p.
(F2) Connectivity of F. Call P, P' in F neighbours if they differ in exactly one run.
 (a) If P in F has a maximal interval [x,y] with x != y, then P\{y} is in F. Repeating, every P in F is joined to an
     independent set of kappa+1 runs.
 (b) For an independent V = {v_1,...,v_(kappa+1)} in cyclic order, let g_j >= 1 be the number of runs strictly between v_j
     and v_(j+1) (v_(kappa+2) := v_1); sum_j g_j = N-kappa-1 = 3kappa-1. Suppose g_j >= 2. Then V u {v_(j+1)-1} is in F (it
     has the interval {v_(j+1)-1, v_(j+1)}, and v_(j+1)-1 is not adjacent to v_j), and so is the independent set
     (V\{v_(j+1)}) u {v_(j+1)-1}. Its gaps are those of V with g_j lowered by one and g_(j+1) raised by one. Symmetrically,
     through V u {v_j+1}, one unit moves from g_j to g_(j-1).
 (c) While some g_j >= 2 with j <= kappa, move one unit from gap j to gap j+1, then on to j+2, ..., up to gap kappa+1. Every
     donor is >= 2: the first by assumption, the later ones because they have just received a unit. This ends with gaps
     (1,...,1,G), where G := 3kappa-1-kappa = 2kappa-1 >= 2; that is, V = {x,x+2,...,x+2kappa} for some x.
 (d) From V = {x,...,x+2kappa} with gaps (1,...,1,G), move v_(kappa+1), v_kappa, ..., v_1 forward by one, in this order;
     each time the gap ahead is G >= 2 or 2. The result is {x+1,...,x+2kappa+1}, again with gaps (1,...,1,G). So all members
     of F are joined.
(F3) Additive constant. For P in C put Theta(P) := sum_(i in P) theta_i and f(P) := U'(P) - Theta(P). For P and P u {i}
 both in C, (F1) gives f(P u {i}) = f(P). By (F2), f is a constant f0 on F. Let P1 := {0,3,6,...,3kappa} and
 P2 := {1,4,...,3kappa+1}; 3kappa+1 <= N-1. Both are independent: they move in steps of 3, and each wrap gap holds
 N-3kappa-1 = kappa-1 >= 1 runs. They are disjoint. P1 u P2 has the maximal intervals {3j,3j+1}, 0 <= j <= kappa,
 separated by the runs 3j+2 (j < kappa) and by the N-3kappa-2 = kappa-2 >= 1 runs 3kappa+2, ..., N-1 (here kappa >= 3 is
 used). So P1, P2 and P1 u P2 are in F. Lemma A* gives U'(P1 u P2) = U'(P1)+U'(P2), so f0 = 2f0 and f0 = 0.
(F4) Link to independent kappa-sets. Let J be a set of kappa independent runs. Its complement has 3kappa runs in kappa
 gaps, so some gap holds g >= 3 runs. If that gap follows j in J, then x := j+2 is adjacent to neither end of the gap, and
 J u {x} is independent with kappa+1 runs, so it is in F. Both J (m = kappa) and J u {x} are in C, so (F1) and (F3) give
 f(J) = f(J u {x}) = 0:
   U'(J) = Theta(J) for every set J of kappa independent runs.                                                   (F4)
(F5) Total. Q0 := {0,2,...,2kappa} is independent: the 2kappa-1 runs 2kappa+1, ..., N-1 separate 2kappa from 0. Q0^c has the
 maximal intervals {1}, {3}, ..., {2kappa-1}, {2kappa+1,...,N-1}. So both are in F, f = 0 on both, and Lemma C* gives
   Theta(all runs) = U'(Q0) + U'(Q0^c) = B* - 2nu0 - 2p.                                                         (F5) []

## 5. Proof of Theorem FCW: sorting the top kappa runs [NEW]

Assume an avoider w as in Sec. 0, and fix a frame for its NF word u (Sec. 1). S_ev := {0,2,...,4kappa-2} and
S_od := {1,3,...,4kappa-1} are complementary. Each has 2kappa runs, and the runs in each are pairwise non-adjacent (N is
even). For S in {S_ev, S_od}, order the theta-values on S decreasingly, theta_(1) >= ... >= theta_(2kappa). Let J_S be the
set of runs carrying the first kappa of them (ties broken arbitrarily). J_S is a set of kappa independent runs, so
m(J_S) = kappa and Theta(J_S) = U'(J_S) by (F4). Every run of S \ J_S has theta <= theta_(kappa).
CLAIM. sum_(i in S) theta_i <= -1-nu0-kappa, except when nu0 >= 1 and letters(J_S) = A-; in that case
sum_(i in S) theta_i <= -nu0-kappa.
Proof. Case letters(J_S) != A-. Lemma U* gives Theta(J_S) <= -1-nu0 <= -1. Then theta_(kappa) <= -1, since otherwise all
 first kappa values are >= 0. So sum_S theta <= (-1-nu0) + kappa*theta_(kappa) <= -1-nu0-kappa.
Case letters(J_S) = A- and nu0 >= 1. Lemma U* gives Theta(J_S) <= -nu0 <= -1. As before theta_(kappa) <= -1, and
 sum_S theta <= -nu0-kappa.
Case letters(J_S) = A- and nu0 = 0. Then A- is empty, so every run of J_S is empty. For an empty run e, X_e = 0, so
 theta_e = h_e = tau_e (mod p), and tau_e = y_e - y_(e-1) != 0 by the empty-run rule. Also theta_e = sigma_e = 0 (mod 2) and
 |theta_e| <= 2kappa < p, so theta_e is a nonzero even integer. Lemma U* gives Theta(J_S) <= -nu0 = 0. If theta_(kappa) > 0,
 all first kappa values are >= 2 and Theta(J_S) >= 2kappa > 0, which is impossible. So theta_(kappa) <= -2, and
 sum_S theta <= 0 + kappa*(-2) = -2kappa <= -1-kappa = -1-nu0-kappa. []
The exception cannot occur for both sets: letters(J_ev) = A- = letters(J_od) with disjoint run sets J_ev, J_od forces A- to
be empty, i.e. nu0 = 0. Adding the CLAIM over S_ev and S_od, and using (F5):
   B* - 2nu0 - 2p = Theta(all runs) <= (-1-nu0-kappa) + (-nu0-kappa) = -1-2nu0-2kappa,
so B* <= 2p-1-2kappa = 6kappa-3 = R-1. This contradicts B* >= R (Lemma D*). Every step used only NF, the frame inputs and
(SR) for the avoider u. So no such u exists, and hence no avoider w as in Sec. 0 exists. This proves Theorem FCW. []
Which inputs carry the weight. The empty-run rule is used only in the case nu0 = 0 with all runs of J_S empty; the
placement of the extra reflection pairs enters only through (SR) (C_max = 2m+2H). Nonempty runs, o_F and rotation pairs are
never assumed. CJ''', Theorem P and K3-11 are not used; the all-equal sub-case needs no separate treatment.

## 6. The cases (kappa,p) = (3,11) and (5,19), written out

(kappa,p) = (3,11): N = 12, R = 16, F = 26, H = 7, 2p = 22.
- Windows: W_0 = [8,16], W_1 = [6,16], W_2 = [4,16], W_3 = [2,16], W_4 = [0,14], W_5 = [0,12], W_6 = [0,10].
  No m has the window [0,16]. C = {m in {3,4}}, and F = {m = 4}.
- Lemma IF*: t <= 2, L >= 12, s_j <= 3, E <= 5+n- <= 7, every a_i <= 8, m1 >= 9 (m1 >= 17/2).
- Lemma N: 2Pi0+nu0-22 >= 5. Lemma Z: |O1| >= m1 >= (14+b)/2 >= b for every label b <= 8.
- Lemma U*: U(P) lies in [Pi0, 22-nu0], of length 22-B* <= 6; B* <= 20; |theta_i| <= 6; |d-d'| <= 12 < 22.
- (F1): Q_i = {i+1,i+3,i+5,i+7}; Q_i u {i} = {i,i+1},{i+3},{i+5},{i+7}, with runs i+8, ..., i+11 between i+7 and i.
- (F2): normal-form gaps (1,1,1,5). (F3): P1 = {0,3,6,9}, P2 = {1,4,7,10}; P1 u P2 = {0,1},{3,4},{6,7},{9,10}, separated by
  2, 5, 8 and 11. (F4): an independent triple leaves 9 runs in 3 gaps, so some gap holds >= 3 runs. (F5): Q0 = {0,2,4,6},
  Q0^c = {1},{3},{5},{7,...,11}.
- Sec. 5: S_ev = {0,2,...,10}, S_od = {1,3,...,11}. J_S is the top 3 of 6, with m = 3 and window [2,16]. Conclusion:
  B* <= 22-1-6 = 15 < 16 = R.
So the whole cell (3,11) is excluded. This includes the branch left open by the accepted conditional K3-11 (frames in
which (H11) fails); neither K3-11 nor P11R is used.
(kappa,p) = (5,19): N = 20, R = 28, 2p = 38. W_5 = [2,28], W_6 = [0,26], W_0 = [12,28]. t <= 4, E <= 9+n-, a_i <= 14,
m1 >= 14 (m1 >= 27/2). Lift margin >= 9. P1 = {0,3,...,15}, P2 = {1,4,...,16}, separated at the wrap by runs 17, 18, 19.
Q0 = {0,2,...,10}. Conclusion: B* <= 38-1-10 = 27 < 28 = R.

## 7. Route remarks, failed routes, scope and interface table

Route remarks (no claim beyond Theorem FCW).
(M1) At p = 4kappa-1 a single-signed pattern with m in {kappa,kappa+1} is not full. If X^(P) is all positive, v = 0 is
 not realised at m = kappa (window [2,R]), and v = B* is not realised at m = kappa+1 (window [0,R-2]); the all-negative
 case is symmetric. Lemma U* shows that each such pattern still has a unique U(P) in the common window [Pi0, 2p-nu0], at
 most one unit outside the two-signed window. The margin of Lemma N (2Pi0+nu0-2p >= 2kappa-1 > 0) absorbs this in Lemma A*.
 Hence the lift framework holds on all of C, and no fullness or connectivity statement for two-signed patterns is needed.
(M2) The lost unit matters only for the sorted set J_S, with m = kappa and letters(J_S) = A-. It can occur in at most one
 alternating set, and only when nu0 >= 1. Sorting the top kappa (not kappa+1) runs gains one unit per alternating set, so
 the bound B* <= R-1 survives.
Failed or unused routes (kept; not premises).
(R1) Fullness-based frameworks (K3 Lemma FULL/F3; P11R Lemma FULL11 with its missing connectivity claim) need a connected
 family of FULL patterns that contains the sorted sets. At p = 4kappa-1 the single-signed patterns of (M1) break this, and
 P11R records the connectivity of two-signed patterns as unproved. Lemma U* replaces that route.
(R2) Sorting the top kappa+1 runs (the USK route) gives only B* <= R at p = 4kappa-1, even when every sorted set is
 two-signed, and would then need a separate tight-case analysis. Sorting the top kappa runs avoids it.
(R3) USK Lemma N(b),(c) (the u+ count and |A-|+nu0 <= 2kappa), Theorem P, CJ''' and K3-11 are not needed here.
Boundary remark (no claim). The proof uses p = 4kappa-1 in Lemma W(b),(c) (W_kappa = [2,R], W_(kappa+1) = [0,R-2]) and in the
counts of IF*(f), Lemma Z and Lemma N. Other p are not addressed here.
Scope. Claimed: Theorem FCW, i.e. for every integer kappa >= 3 with p = 4kappa-1 prime, the terminal cell k = p+1,
kappa_hat = kappa is excluded under the full existential-NF/word antecedent; in particular the cell (3,11) is excluded.
Lemmas W, IF*, D*, N, Z, U*, A*, C* and F are proved only at p = 4kappa-1, kappa >= 3, in this frame. NOT claimed: other p
(p <= 4kappa-3, or any p not of the form 4kappa-1); kappa_hat = 0; p = 7; reflection rigidity; INV*; o_F assembly; full
ordered Olson; any multiset-only statement outside the antecedent. No USK statement is extended below its accepted range.
Aroot=/Users/jinleic/repos/aifours; R16=Aroot/institute/runs/six-lane-2026-10-16/review;
R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review;
ROT=Aroot/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation;
PL=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-terminal-cell/proof-LOWER-v1.md;
FBP=Aroot/mathematics/evidence/six-lane-20261018-96h/olson/evidence.
| Input | Text, whole-file SHA256 | Scope; use |
|---|---|---|
| K1 verdict | R18/olson-LOWER-K1-parent-verdict-v1.md; 93ea601c1255f52a8a186002e9e46986c99db1c81a1c4aba68eb6143ca926e83 | PL Secs. 2-7 accepted relative to their inputs |
| LOWER parent erratum | R18/olson-LOWER-parent-erratum-v1.md; 087ab3ae6e880633b26658ff68e8f787bdb59758a4a0662bc7744aeea5b96377 | m(P) = half the sign transitions; theta only through explicit pairs ((F1)) |
| PL | PL Secs. 2, 4-6 (lines 40-50, 61-106; lines 108-129 for comparison only); 251c8dca1c34be7b76432dc50d13368b11a7bf6da6bbb8bd31e4ee18e7cd476d | (SR); IF(a) and the gamma-normalisation; the SS bijection (instantiated through D*); LT (re-derived in Sec. 1). PL's U/A/C/THETA are NOT imported: Lemmas U*, A*, C* and (F1) are new proofs |
| NF | ROT/proof-ROT-few-E-v4.md lines 28-43; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | some admissible NF; odd blocks; empty-run rule |
| GRX | ROT/notes-GRX-v1.md lines 7-20; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | if direction, through (SR) |
| (S1) definition | R16/olson-zx-s1c-parent-verdict-v1.md line 19; 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af | the definition "(S1) bounds every zero-sum length by 2kappa" only; S1(a) NOT used (IF*(b) is direct) |
| SC0 | R16/olson-index-one-primary-statement-parent-v1.md; e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6 | index-<1 generator of a zero-sum-free sequence of length >= p+1 in C_(2p); IF*(c) |
| ZSTRUCT, FB in (S') | R18/olson-FB-parent-verdict-v1.md 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a; FBP/proof-FB-v1.md lines 11-19, 339dcadcd914a9f036ea71a5ec2b5d3f0678cc100e22aca9de2d75751373cc6b, erratum 1 33de46d245ec89a31cce1a06ac44a11f2c81c91a713b0830c59f31686245e202 (no statement change); (S') extension R18/olson-balfull-rotzb-parent-verdict-v1.md line 33, 56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0 | IF*(d), t >= 1 only, at (k',kappa') = (p-1,kappa-1): Z-shape, n- >= 1, balance, W+n+ <= 2p-1 |
| context only | R18/olson-USK-parent-verdict-v1.md 6d3358ce3f1e9e95a366f2b32f10adbc73df607bc62723f561567dce1a53de18 with errata v1 85718782c14dcb913706d5b7245ebfda1ef50ef1e9e7661d671a9ecbfcf4519e and v2 4f3a2636594787337ebe8294dc086f8a3af9dccea89d5599e95e802e95590bfe; R18/olson-K3-parent-verdict-v1.md 9281cbc64bd2bc59edf7a8404481765d5d5d39c351ce5b2b28c35b6e6e03a9f6 with erratum 8653cb3e183a6c8d21e95e971de95b598a5a29cb94e90bb69de6173623c332af; P11R proof-P11R-v1.md 6ee3df0985f02d01e6cde08c88944791b91dbc76e389e20f16e6b9accec87ac4 (unreviewed; read after the freeze) | not premises |
Not used: S1(a); the Setting fact; FB-E; Theorem P (PL Sec. 3); B0S-CJ'''; K3-11; PL Lemmas D, U, A, C, THETA (the proofs
here are new); PL Secs. 8-9; all USK and K3 lemmas; P11R and every other unreviewed candidate.
