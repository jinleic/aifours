# LOWER: lower-half k=p+1 cells - integer form, lift framework, exclusion of kappa_hat=1, conditional rigidity, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T22:07:01-0700. Status: CANDIDATE_UNVERIFIED written proofs. LABELLED PARTIAL of the
frozen target (LOWER-scope-v1.md SHA256 2e9784c14a8c467d52eb43e2787d22a0d947a2bee255dd731ccc5a65b1007959, frozen 21:17:19 before
derivation; input addendum LOWER-scope-addendum-1.md 0a68bf4204623d9cff7950175bda235fffefe120a3a203e478fc333fadd60442). The
exact remaining regime is in residual-LOWER-v1.md. All case work by hand; no script, assertion, enumeration or computation over
scientific data. No novelty, priority, Lean or human-review claim. Unreviewed BOTTOM/RUH3/RUH2/KP3/KP4/R7 are not premises.

## 0. Statements

Throughout: p >= 11 prime, 1 <= kappa <= (p-3)/2, and the FULL antecedent: a length-(4p-2) avoider w over D_(2p) (no identity
2p-subword in increasing original index order) has SOME admissible NF u with terminal k=p+1 and kappa_hat=kappa; the H=p-1-kappa
extra reflection pairs lie anywhere in the odd blocks; every empty NF run separates different reflection values. No o_F,
nonempty-run, rotation-pair or reflection-rigidity hypothesis; no multiset-only statement outside this antecedent.
THEOREM R (range and coverage) [from pins]. At terminal k=p+1 the admissible values are 0<=kappa_hat<=p-1; the target 1..(p-3)/2
lies inside. No accepted result excludes a whole lower-half cell; accepted B0S-CJ''' excludes exactly the sub-case "all
rotation letters equal to one non-identity rotation" of every lower-half cell (cited, not re-proved).
THEOREM S (structure) [NEW]. For every such u: (S1) sum_i floor(r_i/2) <= 2kappa-1; (S2) integer form (Sec. 4);
(S3) signed sums fill intervals (Sec. 5); (S4) light side (Sec. 6); (S5) the lift framework of Sec. 7.
THEOREM K1 [NEW, cell, uniform in p]. For every prime p>=11 no avoider has an admissible NF with terminal k=p+1 and
kappa_hat=1 (the all-rotations-equal sub-case by cited B0S-CJ''').
LEMMA CR [NEW, CONDITIONAL]. If kappa<=(p-3)/4 and hypothesis (H-ALT) of Sec. 9 holds, all rotation letters lie in one pair
{rho_g, rho_-g}, and the lift data are tight (Sec. 9). (H-ALT) is NOT proved here.
NOT PROVED: exclusion of 2<=kappa<=(p-3)/2 (residual-LOWER-v1.md).

## 1. Range and coverage [from pins]

Accepted NF (ROT/proof-ROT-few-E-v4.md lines 37-43): every block odd, H=(F-k)/2, kappa_hat=p-1-H, R=2p+2kappa_hat-k, DAV
kappa_hat<=k-1; GRX all-plus gives kappa_hat>=0 (R18/olson-ASSEMBLY-LS-parent-verdict-v1.md line 38: if H>=p, C=2p reflections
with no rotation is admissible). At k=p+1: H>=0 gives kappa_hat<=p-1 (DAV gives only <=p); kappa_hat is an integer since F=k
(mod 2). So 0<=kappa_hat<=p-1. Accepted exclusions at k=p+1: PP1 (kappa_hat=p-1), KP2 (p-2), and per parent IRCs KP3 (p-3, verdict
bb9d8a27b0f95227c4e017b0749c0325906815b812c1e7694b7222d1fbc8ffe8) and KP4 (p-4, p>=11, verdict
5b56b3675a4c59fb849f5e1feedef06e50682f9bd227985631e58ecf1c62db74); these and the UH-constraint partials concern kappa_hat>=(p-1)/2. Accepted B0S-CJ''' (R16/olson-cj-cjx-parent-verdict-v1.md lines 8-15):
for a word of length 4p-2 whose R>=1 rotations all equal one non-identity rotation, F>=1, all maximal constant reflection
blocks odd, genuine empty runs, kappa=p-1-H>=1, Delta=k-p-kappa-1, with R>=4kappa-4 and 2kappa<=p-1 and Delta<=0, there is an
identity 2p-subword. The NF word u has these properties at k=p+1 in the lower half (each block S_i is a maximal constant block
because an empty run separates different values; Delta=-kappa; R=p-1+2kappa>=4kappa-4; 2kappa<=p-3), so CJ''' excludes the
sub-case of equal rotations; all equal to rho_0 is excluded by the pigeonhole arc of Sec. 4 with n=2kappa zero letters.

## 2. Word form and selection rule [from accepted NF and GRX]

u is an avoider of length 4p-2 with the rotation multiset of w (NF). Write it cyclically R_0 S_0 R_1 S_1 ... R_p S_p: N=p+1
runs R_i (possibly empty, r_i letters, sum X_i of their values), blocks S_i = sigma_(y_i)^(l_i), l_i odd, sum (l_i-1)/2 = H,
F = p+1+2H = 3p-1-2kappa, R = p-1+2kappa; an empty R_i has y_(i-1) != y_i (indices mod N). Put tau_i := y_i - y_(i-1) (sum 0).
For a set P of runs: m(P) := number of maximal cyclic intervals, T(P) := sum_(i in P) tau_i, and X^(P) := the letter values
with every letter of a run of P negated.
(SR) For every P and every even n with max(0,2kappa+2-2m(P)) <= n <= min(R,2p-2m(P)), T(P) is not a sum of n letters of X^(P).
Proof. GRX (ROT/notes-GRX-v1.md 7-20, if direction) applied to u (GRX block i = S_i, preceded by run R_i; its theta_i =
y_(i-1)-y_i = -tau_i): for the sign pattern z = -1 on P, Phi = 2m, delta_GRX = N - Phi (all l_i odd), C_max = Phi + 2H, every
even C in [2m, 2m+2H] with 0 <= 2p-C <= R is admissible, and its target is sum_(z=+1) theta = sum_(i in P) tau_i. Put n = 2p-C. []

## 3. Run structure [accepted Theorem P]

The gaps between consecutive reflections of u are the l_i-1 gaps inside each block (no rotation) and the N run gaps (r_i
rotations). Theorem P (length 4p-2 <= 4p-1, F>=1): if F + sum_i floor(r_i/2) >= 3p-1, u has an identity 2p-subword. Hence
  (S1) sum_i floor(r_i/2) <= 3p-2-F = 2kappa-1;
so at least R - 2(2kappa-1) = p+1-2kappa runs have odd length and at most 2kappa runs (empty ones included) have even length.
For kappa=1: sum_i (r_i - 1) = R - N = 0 and at most one run has length >= 2, of length 2 or 3; so u has one of the shapes
(a) all r_i = 1; (b) one r_i = 2, one r_i = 0, all others 1; (c) one r_i = 3, two r_i = 0, all others 1.

## 4. Integer form [accepted S1(a), SC0, ZSTRUCT, FB; NEW application]

LEMMA IF. (a) There is an arc P0 (a proper nonempty set of consecutive runs) with T(P0) = 0; its complementary arc C0 also has
T(C0) = 0. (b) There are gamma in Z_p\{0} and odd integers b_l for the letters l such that the value of l in X^(P0) is b_l*gamma,
and the multiset {b_l} consists of a_1,...,a_L >= 1 (L = R-2t), n+ further 1's and -s_1,...,-s_(n-) (s_j >= 1), where
n+ + n- = 2t <= 2kappa-2, sum s_j = n+ (so n- <= n+), W := sum a_i satisfies W + n+ <= 2p-1, every a_i, s_j <= p-2, and
m1 := #{i : a_i = 1} >= (3L-W)/2 >= (p+4)/2, m1 >= 2p+2-W when t >= 1. For kappa=1: t = n+ = n- = 0.
Proof. (a) The p+1 block values lie in Z_p, so y_c = y_c' for some c != c'; P0 := runs c+1,...,c' (mod N) is a proper nonempty
arc with T(P0) = y_c' - y_c = 0, and its complement C0 (runs c'+1,...,c) has T(C0) = 0.
(b) Let Y be the sequence of odd elements (1,x) of Z_2 x Z_p = C_(2p) over the letters x of X^(P0); a zero-sum of Y of length
n is n letters (n even) of X^(P0) with sum 0. (SR) at P0 (m=1, n in [2kappa,R] as R <= 2p-4) forbids target 0, so Y has no
zero-sum of length in [2kappa,2p] (|Y| = R < 2p): (ZP) at kappa-1. Accepted S1(a) (kappa-1 <= (p-1)/2): every zero-sum of Y has
length <= 2kappa-2. Let Z be a longest zero-sum, |Z| = 2t <= 2kappa-2, Y' = Y - Z: zero-sum free (a zero-sum of Y' would extend
Z), |Y'| = L >= p+1. SC0: Y' = (a_1 g)...(a_L g) for a generator g, positive integers a_i, W < 2p. As every a_i g is odd, g = (1,gamma)
with gamma != 0 and every a_i odd. If t = 0 (always when kappa = 1) put n+ = n- = 0. If t >= 1 then kappa >= 2 and Y lies in
setting (S') of the accepted FB verdict with (k',kappa') = (p-1,kappa-1): 1 <= k' <= p-1, 1 <= kappa' < p, |Y| = 2p+2kappa'-k'
= R, (S1) at kappa'. ZSTRUCT (accepted in (S')) gives Z = g^(n+) (-s_1 g)...(-s_(n-) g) with odd s_j >= 1; FB gives
sum s_j = n+ and W + n+ <= 2p-1; FB-E gives a_i, s_j <= p-2; the Setting fact gives m1 - (2p-1-W) >= 3. Finally
sum (a_i - 1) = W - L >= 2(L - m1) gives m1 >= (3L-W)/2 >= (3(p+1) - (2p-1))/2. []
Normalisation. (v,eps) -> (gamma^(-1) v, eps) is an automorphism of D_(2p); it preserves identity subwords, the run/block
structure and (SR) (with tau_i, values scaled). So take gamma = 1. Put c_l := b_l for letters of C0 and c_l := -b_l for letters
of P0: the ORIGINAL value of l is c_l (mod p). For a set P of runs and a letter l put eps_l = -1 if l lies in a run of P, else
+1; the value of l in X^(P) is eps_l c_l.

## 5. Density and signed sums [NEW]

LEMMA D. The multiset A = {|c_l|} has every integer of [0,B*] as a subset sum, where B* := sum |c_l| = W + 2n+ >= R.
Proof. A contains u >= m1 ones. No element exceeds m1+1: if r = L - m1 >= 1 of the a_i are >= 3, then
a_max - 1 <= (W-L) - 2(r-1) <= L - r = m1 because W <= 2p-1 < 2L + r - 2; and s_j <= 2p-1-W <= m1-3 (ZSTRUCT and the Setting
fact). Order the elements > 1 increasingly with prefix sums E_0 = 0 <= E_1 <= ...; each E_k + j (0 <= j <= u) is a subset sum,
and E_(k+1) - E_k <= m1+1 <= u+1, so these integer intervals cover [0,B*]. B* >= R since every |c| >= 1, with equality iff
every |c_l| = 1. []
LEMMA SS. For every set P of runs let Pos(P), Neg(P) be the letters with eps_l c_l > 0, < 0, Pi(P) := sum over Pos(P) of |c|,
nu(P) := sum over Neg(P) of |c|, and sigma(P) := sum of c_l over the letters of the runs of P. Then the sums sum_(l in J) eps_l c_l
(J any set of letters) are exactly the integers of [-nu(P), Pi(P)]; each such sum has the parity of |J|; and
Pi(P) = Pi0 - sigma(P), nu(P) = nu0 + sigma(P), with Pi0 := Pi(empty set), nu0 := nu(empty set), Pi0 + nu0 = B*.
Proof. J -> U := (J n Pos(P)) u (Neg(P) \ J) is a bijection and sum_J eps c = sum_U |c| - nu(P); apply Lemma D. Parity: odd
terms. Flipping the letters of P moves their positive weight to the negative side and conversely. []

## 6. Light side [NEW]

LEMMA LT. For a set Q of runs let o(Q) := #{letters l in runs of Q : b_l = 1}. Then min(o(P0), o(C0)) <= kappa.
Proof. In X (pattern empty set) these letters have value +1 in C0 and -1 in P0. (SR) with P empty (m=0) forbids zero-sums of
even length in [2kappa+2,R]; kappa+1 of each would be one. []
Since T(C0) = 0 and X^(C0) = -X^(P0), Lemma IF holds for C0 with the same b_l and generator -gamma; so the roles of P0 and C0 may
be exchanged, and below P0 denotes a side with o(P0) <= kappa ("light").

## 7. Full patterns and the lift framework [NEW]

Call a set P of runs FULL if every even v in [-nu(P), Pi(P)] equals sum_(l in J) eps_l c_l for some J with |J| in
[max(0,2kappa+2-2m(P)), min(R,2p-2m(P))]. Put h_i := tau_i + X_i, H(P) := sum_(i in P) h_i (so T(P) + sigma(P) = H(P) mod p).
LEMMA U. If P is full then B* <= 2p-2, and H(P) has a unique representative U(P) in [Pi0+1, 2p-1-nu0] with
U(P) = sigma(P) (mod 2). Put U'(P) := U(P) - 2p, so Pi0+1-2p <= U'(P) <= -1-nu0.
Proof. By (SR) and fullness, T(P) avoids every even v in [-nu(P),Pi(P)]; with u := v + sigma(P), H(P) avoids every integer
u in [-nu0, Pi0] with u = sigma(P) (mod 2) (Lemma SS). The integers of one parity in [-nu0, 2p-1-nu0] are p in number and
pairwise incongruent mod p (their differences are even and of absolute value < 2p); if B* >= 2p-1 those in [-nu0,Pi0] already
cover every residue, a contradiction; otherwise the representative of H(P) lies in [Pi0+1, 2p-1-nu0]. []
LEMMA A (additivity). If P1, P2 are disjoint, P1, P2, P1 u P2 are full and 2Pi0 + 3 + nu0 > 2p, then
U'(P1 u P2) = U'(P1) + U'(P2).
Proof. D := U(P1) + U(P2) - U(P1 u P2) is 0 mod p (H is additive) and 0 mod 2 (sigma is additive), hence a multiple of 2p, and
2Pi0 + 3 + nu0 - 2p <= D <= 4p - 3 - 2nu0 - Pi0 < 4p; so D = 2p. []
LEMMA C (complements). If P and its complement P^c are full, then U'(P) + U'(P^c) = Pi0 - nu0 - 2p.
Proof. H(P) + H(P^c) = sum of all letter values = Pi0 - nu0 (mod p), sigma(P) + sigma(P^c) = Pi0 - nu0, so
U(P) + U(P^c) = Pi0 - nu0 (mod 2p); it lies in [2Pi0+2, 4p-2-2nu0], which contains Pi0 - nu0 + 2p (as B* <= 2p-2) and no other
number of that class. []
LEMMA THETA. Let theta_i be the unique integer in (-p,p) with theta_i = h_i (mod p) and theta_i = sigma({i}) (mod 2). If P and
P u {i} (i not in P) are full, then U'(P u {i}) - U'(P) = theta_i.
Proof. The difference is h_i mod p, sigma({i}) mod 2, and at most 2p-2-B* < p in absolute value (B* >= R >= p+1); the two
integers of (-p,p) congruent to h_i mod p have different parities. []

## 8. Proof of Theorem K1 [NEW]

Let kappa = 1: R = N = p+1; windows: m=0: n in [4,p+1]; m=1: [2,p+1]; 2 <= m <= (p-1)/2: [0,p+1]. Lemma IF holds with t = 0:
all b_l = a_i are positive odd, W = sum a_i <= 2p-1, and W = p+1 (mod 2) as there are p+1 odd terms, so W <= 2p-2 and
m1 >= (3(p+1) - W)/2 >= (p+5)/2. Let P0 be light (o(P0) <= 1).
K1.1. Every letter of P0 has b_l = 1, and P0 contains at most one letter. Let l be a letter of P0 with b_l = a (value -a in X).
The other p letters have b-sum W - a <= 2p-2-a, so at least p - (p-2-a)/2 = (p+2+a)/2 of them equal 1; at most one of them lies
in P0, so C0 holds at least (p+a)/2 >= a ones, each of value +1 in X. With a of them, {l} gives a zero-sum of X of even length
a+1 <= p-1, forbidden by (SR) at P empty when a+1 >= 4; so a = 1, and o(P0) <= 1 leaves at most one letter in P0. []
So, in the original orientation, every c_l is a positive odd integer except at most one letter with c = -1 (lying in P0); let
delta in {0,1} count it. Then nu0 = delta, Pi0 = W - delta >= p, B* = W <= 2p-2, and 2Pi0 + 3 + nu0 > 2p.
K1.2 (fullness). (i) Every P with 2 <= m(P) <= (p-1)/2 is full (all |J| are allowed and Lemma SS). (ii) An arc P (m=1) is full
if Pos(P) and Neg(P) are both nonempty. Indeed n_hi = R; an even v != 0 is only realised by sets J with |J| = v (mod 2), |J| >= 2;
for v = 0 a nonempty zero-sum is needed: if both signs occur among the letters with |c| = 1, take {+1,-1}; otherwise all such
letters have one sign, say +, and Neg(P) contains -w with w >= 3; as in K1.1 at least (p+2+w)/2 >= w of the other letters
have |c| = 1, hence value +1 in X^(P), and {-w} with w of them is a nonempty zero-sum (symmetrically for -).
K1.3 (the sum). Let G be the set of runs containing a letter of positive value; every nonempty run except possibly the run z
holding the letter -1 lies in G. Fix r in G and put G' := G \ {r}. For i in G', {i} is an arc with Neg({i}) nonempty (its
positive letter flips) and Pos({i}) containing r's positive letter: full by K1.2(ii). Every arc A contained in G' is full for
the same reason. G' is the union of its maximal arcs A_1,...,A_k, pairwise separated by runs outside G' (empty runs, r, and
possibly z), so k <= E+2 <= 4 <= (p-1)/2 and every union of at least two of them is full by K1.2(i). Building each A_j run by run
and then uniting the A_j, Lemma A gives U'(G') = sum_(i in G') U'({i}). By Lemma U each U'({i}) <= -1-delta and
U'({i}) = sigma({i}) (mod 2), while U'(G') >= Pi0 + 1 - 2p = W - delta + 1 - 2p. Hence
  sum_(i in G') (-U'({i})) <= 2p - 1 - W + delta.                                                    (K1)
Case delta = 0. Every letter is positive and G is the set of nonempty runs, |G'| = p - E, each -U'({i}) >= 1; (K1) gives
p - E <= 2p - 1 - W, i.e. W <= p - 1 + E. If W = p+1 every letter equals 1, i.e. all rotations equal rho_1 (non-identity):
excluded by the cited B0S-CJ''' (Sec. 1). Otherwise W >= p+3 > p - 1 + E (E <= 2 by Sec. 3): contradiction.
Case delta = 1. Now -U'({i}) >= 2, and -U'({i}) >= 3 when sigma({i}) is odd, i.e. when run i has an odd number of letters; by
Sec. 3 at most one run has two letters. |G'| >= (p+1-E) - 2 >= p-3. So the left side of (K1) is at least 3(p-3) - 1, while the
right side is 2p - W <= p - 1: 3p - 10 <= p - 1 is false for p >= 5. Contradiction.
Both cases are impossible, which proves Theorem K1. []

## 9. Lemma CR: conditional rigidity [NEW, CONDITIONAL]

Let S_ev (runs 0,2,...,p-1) and S_od (runs 1,3,...,p) be the two alternating sets; they are complementary, each has (p+1)/2
pairwise non-adjacent runs, so every subset J of either has m(J) = |J|.
(H-ALT) For S in {S_ev, S_od}, every J contained in S with |J| >= kappa+1 (S itself included) is full.
Assume kappa <= (p-3)/4 (so |S| >= 2kappa+2), (H-ALT) and 2Pi0 + 3 + nu0 > 2p. Then every |c_l| = 1, i.e. all rotation letters
lie in {rho_1, rho_-1}; moreover in each of S_ev, S_od at most kappa runs have theta_i >= 0, all others have theta_i = -1, and the
kappa+1 largest theta_i sum to -1-nu0.
Proof. Fix S. For J in S with |J| >= kappa+1 put f(J) := U'(J) - sum_(i in J) theta_i. Lemma THETA gives f(J u {i}) = f(J), so f
is constant on these sets (any two are joined through their union); two disjoint such J with full union exist since
|S| >= 2kappa+2, and Lemma A gives f = 2f, so f = 0. Order theta on S decreasingly; the top kappa+1 form a full J*, so
sum_(J*) theta = U'(J*) <= -1-nu0; then the (kappa+1)-th largest theta is < 0, hence <= -1, and so are all smaller ones. Thus
sum_S theta <= -1 - nu0 - ((p+1)/2 - kappa - 1). Adding the two sets and using Lemma C (S_od = S_ev^c, both full):
Pi0 - nu0 - 2p = sum over all runs of theta <= -p - 1 - 2nu0 + 2kappa, i.e. B* = Pi0 + nu0 <= p - 1 + 2kappa = R. With B* >= R
(Lemma D) equality holds throughout, giving |c_l| = 1 for every l and the stated equalities. []
(H-ALT) holds automatically for |J| <= (p+1)/2 - kappa (then n_hi = R and n_lo = 0); for larger J, in particular J = S, it needs
every even v in [-nu(J),Pi(J)] to be realised with at most 2p-2|J| letters. This is NOT proved here (residual-LOWER-v1.md).

## 10. Scope and interface table

[NEW]: Theorem S (Secs. 3-7, the integer-form application at a T=0 arc, Lemmas D, SS, LT, U, A, C, THETA), Theorem K1, Lemma CR
(conditional). Cited: B0S-CJ''' (all-equal sub-case only). Not used: UH-A/L/E (upper half), RS, CD, LS-family, S1-sharp, SHgen,
REFL, assembly results; unreviewed BOTTOM, RUH3, RUH2, KP3/KP4 proof texts, R7.
Aroot=/Users/jinleic/repos/aifours; ROT=Aroot/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation;
R16=Aroot/institute/runs/six-lane-2026-10-16/review; R18=Aroot/institute/runs/six-lane-2026-10-18-96h/review.
| Input | Text, whole-file SHA256 | Scope; use |
|---|---|---|
| NF | ROT/proof-ROT-few-E-v4.md 28-43; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | some admissible NF; lowodd/ZX/fewodd overlays; Secs. 1-2 |
| GRX | ROT/notes-GRX-v1.md 7-20; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | if direction; (SR) |
| range | R18/olson-ASSEMBLY-LS-parent-verdict-v1.md 38; 249e07658762e7e3efe346063851b243369f14dadf6fbaedf121944a18db6a22 | kappa_hat>=0, DAV |
| Theorem P | Aroot/mathematics/evidence/six-lane-20261016/olson/proof-theoremP.md; 58a85ebeba8208e2f89b39a691235d2d1374656d8888ea905fe96aa75e1dafc2; accepted per R16/olson-reflection-K0star-RED-parent-verdict-v1.md 7 (879aeee781a080d1b1cb4a4489f62e45e2fa332f7c2d9242f725cfae1d00c02a) | Sec. 3 |
| S1(a) | R16/olson-zx-s1c-parent-verdict-v1.md 19; 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af | (ZP)=>(S1) at kappa-1 <= (p-1)/2 |
| SC0 | R16/olson-index-one-primary-statement-parent-v1.md; e461514461d23287beeecf04fa26334efd91d3de51caa33312f6c5b10b4d35c6 | index-<1 generator, length >= p+1 |
| ZSTRUCT, FB, FB-E | R18/olson-FB-parent-verdict-v1.md 8d6d4967af13fdf70a1a888ce904f4d3a8ea2a127bbc81cc01d6023197cbd63a; text proof-FB-v1.md 339dcadc...6cc6b lines 11-24 + erratum 33de46d2...e202; (S') extension R18/olson-balfull-rotzb-parent-verdict-v1.md 33 (56b988ee90805f850760c6969d9724f890fb637335248b9060189ef99b1e1bc0); Setting fact R16/olson-rotzr-parent-verdict-v1.md (6d8bb6c94f6263834c39130c6d39a2ab54e557740eb45f904732664e879dde73) | Lemma IF, kappa >= 2 |
| B0S-CJ''' | R16/olson-cj-cjx-parent-verdict-v1.md 8-15; 5cfd6a4fe15cab133e210cd6f6966e34fa633d1a8c432b79eb537c0016145f6d | equal-rotation sub-case only |
