# G-words: exact segment moves, a genuineness-boosted block chain, and Theorem K0* (REFL for kappa = 0)

Owner OlsonReflectionRigidity.  Revision r3, written after host clock 2026-10-18T06:31:21-0700; documentation errata only (Claude
review R/olson-k0star-r2-claude-v1.note.md, 79e6f650...9bf1, ACCEPT-WITH-FIXES 0/0/6), fix map at the end (r2 -> r3); no
mathematical change.  Parent verdict on r2: R/olson-reflection-K0star-RED-parent-verdict-v1.md (879aeee7...c02a).
r2 (6681676e...96e1) was written after host clock 2026-10-18T03:38:54-0700; it superseded proof-K0star-r1.md
(sha256 99a8f2e0403877bb571b66134be3889e9d606d4da16c9040b6bf0407edb69488, kept unchanged).  r2 applies the three MINOR findings of
the Codex hostile review R/olson-reflection-reduction-codex-v1.note.md (sha256 311bdacc...a8b) that concern this file; changed
places are marked [r2 fix n]; fix map at the end.  [r3, Claude m6] r2 changed no use of FUS, no case and no conclusion (its fix 1
replaced a false statement of the second FUS form by the correct one).  Status: written proofs
[W]; r1 reviewed by Codex (ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR); r2 itself not re-reviewed.
Target and scope: README.md of this directory (frozen, sha256 af55df78...d63b).  Everything here concerns words whose
rotation letters lie in {rho_1, rho_-1}; nothing here says anything about rotation values (rotation slice), about INV*(p) as a
whole, or about ordered Olson.  p >= 5 is prime throughout.  Paths are relative to olson/ unless stated.

## 0. Setting

D_(2p) = {(v,e)}, (v,e)(v',e') = (v + e v', e e'), rho_x = (x,+1), sigma_y = (y,-1).  A word is cyclic; an identity 2p-subword is
an increasing index set of size 2p with ordered product (0,+1); its existence is invariant under cyclic rotation
(proof-theoremP.md, Setting) and under the automorphisms rho_v -> rho_(cv), sigma_v -> sigma_(cv+d), c != 0.  An avoider has no
identity 2p-subword.

**G-words.**  A G-word is a word of length N with F >= 1 reflections, R >= 1 rotations, all rotations in {rho_1, rho_-1}
(normalised x = 1).  [r2 fix 3: R >= 1 for all maximal-decomposition statements below; a word with R = 0 is one cyclic
reflection run (for k = 1 its sole "run" is empty with theta_1 = 0), it is handled by Lemma AR, and Lemmas GR0, H0 remain valid for
every representation, R = 0 included.]  Cutting every maximal cyclic reflection run at every change of letter gives the maximal constant blocks
S_1, ..., S_k (S_i = sigma_(y_i)^(l_i), l_i >= 1) and the rotation runs R_1, ..., R_k, R_i between S_(i-1) and S_i (indices mod k,
y_0 := y_k); R_i has a_i letters rho_1 and b_i letters rho_-1, r_i = a_i + b_i >= 0, d_i = a_i - b_i, theta_i := y_(i-1) - y_i.
R_i is an EMPTY run if r_i = 0; then y_(i-1) != y_i by maximality, i.e. theta_i != 0 (a *genuine* empty run).  g := number of
empty runs.  w is RGR (in RGR_N(p) of proof-DR.md) iff g = 0.  More generally a *representation* is any cyclic alternation
R_1 S_1 ... R_k S_k of constant blocks and possibly empty runs reproducing w (adjacent blocks may then have equal values).
Parameters (of the maximal decomposition unless a representation is named): A = sum a_i, B = sum b_i, R = A + B, D = A - B,
F = sum l_i, H = sum floor(l_i/2), kappa := p - 1 - H, o_F = #{i : l_i odd}, e_F = k - o_F, o_R = #{i : r_i odd},
e_R = k - o_R (EMPTY RUNS COUNT AS EVEN ROTATION RUNS).  For N = 4p - 2:  F = 2H + o_F and R = 2p - o_F + 2 kappa.        (0.1)
Patterns: P subset of [k] (a set of rotation runs, empty runs included); m(P) = number of maximal cyclic intervals of P; the
boundary blocks of P are the S_j with exactly one of R_j, R_(j+1) in P (2m(P) of them); beta(P) = number of even boundary blocks;
D_P = sum_(i in P) d_i; R_P = sum_(i in P) r_i; u_P := 2^(-1) sum_(i in P) theta_i in Z_p (additive; u_([k]) = 0; for a cyclic
interval P = {i, ..., j}: u_P = (y_(i-1) - y_j)/2, so u_P != 0 iff its two boundary blocks have different values).
Normalisation N: rho_v -> rho_(-v), sigma_v -> sigma_(-v) maps G-words to G-words, keeps every block length and every empty run
(and its genuineness), swaps A and B; so WLOG A >= B.

## 1. Exact criteria (re-derived for representations with empty runs)

**Lemma GR0.**  For any representation (a_i, b_i, l_i, y_i) of any length, with f_i = [z_i != z_(i+1)], Phi = sum f_i,
delta = #{i : l_i != f_i mod 2}, C_max = F - delta, E+ = sum_(z_i = +1) a_i + sum_(z_i = -1) b_i, E- = R - E+, s0 = 2p - C_max,
s1 = 2p - Phi, Ach(z) = 2Z cap [max(-s1, s0 - 2E-, -E-), min(s1, 2E+ - s0, E+)] and tau(z) = -2^(-1) sum_i z_i (y_i - y_(i-1)):
w has an identity 2p-subword iff some z in {+1,-1}^k has Ach(z) cap (tau(z) + pZ) != empty.
Proof (the proof of Lemma GR, proof-GR.md Sec. 2, re-checked line by line; it never uses r_i >= 1).  Cut w at the start of R_1.
A selection with an even number of reflections has zone signs z_1 = +1, z_(i+1) = z_i (-1)^(c_i), c_i = number of letters chosen
from S_i (so c_i = f_i mod 2, z defined also at empty runs, and z_(k+1) = z_1).  Multiplying from the left, a chosen rotation
(x,+1) adds e x and a chosen reflection (y,-1) adds e y and flips e (e = current sign).  Inside S_i the chosen letters all equal
sigma_(y_i), so they add z_i y_i if c_i is odd and 0 if c_i is even; the product is rho_V with V = sum_i z_i n_i +
sum_(f_i = 1) z_i y_i (n_i = signed sum of chosen rotations of R_i, 0 for an empty run), and summation by parts gives
sum_(f_i=1) z_i y_i = sum_i z_i (y_i - y_(i-1))/2, so V = t - tau(z) with t = A+ - A- (numbers of chosen effectively positive /
negative rotations).  The realisable totals C = sum c_i are exactly the even numbers in [Phi, C_max] (each c_i independently runs
over f_i, f_i + 2, ..., l_i - [l_i != f_i mod 2] >= f_i), and for even t a pair (A+, A-) with A+ + A- = 2p - C, A+ <= E+,
A- <= E- exists for some admissible C iff t is in Ach(z) (the computation of proof-GR.md Sec. 2, unchanged).  Every admissible
data point is realised by a selection; global sign change z -> -z maps (Ach, tau) to (-Ach, -tau).  []
**Lemma H0 (half windows).**  For a representation (with H, kappa = p - 1 - H, o_F, m(P) and beta(P) all computed from the blocks
of THAT representation, including the kappa in I(empty) [r3, Claude m1]) and a proper pattern P put
  lambda(P) := min(p - m + 1, D_P + B - kappa + m - beta, floor((D_P + B)/2) + 1)   (m = m(P), beta = beta(P), kappa = p - 1 - H),
  I(P) := [1 - lambda(P^c), lambda(P) - 1]  (integers; possibly empty),
  I(empty) := [-min(p, A - kappa - 1, floor(A/2)), min(p, B - kappa - 1, floor(B/2))].
Then w avoids iff u_P notin I(P) (mod p) for every proper P and 0 notin I(empty) (mod p).
Proof.  Lemma GR0 with P = {z_i = +1}.  As sum theta_i = 0, tau(z_P) = 2^(-1) sum_i z_i theta_i = sum_(i in P) theta_i = 2 u_P,
and 2 is invertible, so the condition for z_P is u_P notin [ceil(lo/2), floor(hi/2)] (mod p).  For P proper with Phi = 2m and
beta even boundary blocks, delta = beta + (o_F - (2m - beta)), so c := C_max/2 = H + m - beta; E+ = A_P + B_(P^c) = D_P + B;
hence floor(hi/2) = min(p - m, E+ + c - p, floor(E+/2)) = lambda(P) - 1, and E+(P^c) = E-(P), same m, beta, gives
ceil(lo/2) = 1 - lambda(P^c).  P = empty (z = all -1): Phi = 0, c = H, E+ = B, E- = A gives I(empty); P = [k] gives -I(empty).
No step uses the length or r_i >= 1.  []
**Facts for G-avoiders of length 4p - 2** (F >= 1; if R = 0, Lemma AR of c2/invstar/proof-GR0-r1.md: 2p - 1 adjacent reflection
pairs and EGZ; so R >= 1; a G-word with g >= 1 has k >= 2, F >= 2):
 (Z0) A, B <= 2p - 1 (2p equal rotations); after N, B <= kappa (if A, B >= kappa + 1 then 0 is in I(empty)); hence by (0.1)
      o_F >= 2 kappa - B + 1 (R = A + B <= 2p - 1 + B).  (Pairs) kappa >= 0 (p disjoint pairs sigma_y sigma_y inside blocks, each
      pair adjacent in the selection, give 1).  (V) kappa <= o_F - 1 (Davenport-alpha, proof-dihedral-partial.md Sec. 4, with
      the H gaps "every second gap inside each block", pairwise non-adjacent; the gap at an empty run is not used; F >= 2,
      N = 4p - 2 < 4p).
 (P0) e_R <= e_F + 2 kappa.  Proof: Theorem P (proof-theoremP.md; its gaps are the F gaps between consecutive reflections,
      n_t = r_i at the gap of R_i and 0 elsewhere, empty runs included) gives F + sum_i floor(r_i/2) <= 3p - 2, i.e.
      R + o_R >= 2p; with (0.1) this is o_R >= o_F - 2 kappa.  []
 (Par) If kappa = 0 then B = 0 (after N) and e_R = e_F (mod 2): R = 2p - o_F = o_F (mod 2) and R = o_R (mod 2).

## 2. Moves

**Lemma SPEC (segment replacement).**  Spec(X) := {(|T|, ordered product of T) : T subset of the positions of the word X}.  If
w = U X V (after a cyclic rotation) and w' = U Y V with |Y| = |X| and Spec(Y) subset of Spec(X), then w avoids => w' avoids.
Proof.  An identity 2p-subword T' of w' splits as T_U, T_Y, T_V with ordered product prod(T_U) prod(T_Y) prod(T_V).  Choose
T_X in X with (|T_X|, prod T_X) = (|T_Y|, prod T_Y); T_U u T_X u T_V is an identity 2p-subword of w.  []
**Lemma FUS.**  For l >= 1, l' >= 2 even and any u, v: Spec(sigma_u^(l+l')) subset of Spec(sigma_u^l sigma_v^(l')), and
Spec(sigma_u^(l'+l)) subset of Spec(sigma_v^(l') sigma_u^l).  [r2 fix 1: r1 printed sigma_v^(l'+l) in the second inclusion, which is
false (l = 1, l' = 2, u != v: size 3 forces sigma_u, not sigma_v).]  In both forms the EVEN block sigma_v^(l') is recoloured with the
value u of its neighbour, on either side.
Proof (first form).  Spec(sigma_u^(l+l')) = {(c, sigma_u^c) : 0 <= c <= l + l'} (sigma_u^c = 1 for even c, sigma_u for odd c).
c <= l: c letters sigma_u.  c > l, c - l even: all l letters sigma_u and c - l letters sigma_v (even number): product sigma_u^l =
sigma_u^c.  c > l, c - l odd: then c - l <= l' - 1, take l - 1 letters sigma_u and c - l + 1 <= l' letters sigma_v.  Second form
[r2 fix 1]: the same counts, with the even number (c - l or c - l + 1) of letters sigma_v taken FIRST and then l or l - 1 letters
sigma_u; the product sigma_v^(even) sigma_u^(c') is sigma_u^(c') = sigma_u^c.  []
So, in a G-word (R >= 1; [r2 fix 3]), at a genuine empty run next to an EVEN block, recolouring the even block with the value of
the other block ("FUS step")
preserves avoidance, length, every rotation, B, A, R, F; it removes that empty run (and the empty run on the other side of the
even block if the new value equals the next block's value: a "double fusion").  H changes only in a double fusion of
sigma_u^a [] sigma_v^b [] sigma_u^c (b even) with a, c BOTH odd, where it rises by 1 (kappa falls by 1).
**Lemma SL (slide).**  For u != v and a, b >= 1, Spec(sigma_u^a sigma_v^b) depends only on floor(a/2) + floor(b/2), a mod 2, b mod 2.
Proof.  Its elements are (c1 + c2, sigma_u^(c1) sigma_v^(c2)), 0 <= c1 <= a, 0 <= c2 <= b; the product is 1, sigma_u, sigma_v,
rho_(u-v) for (c1, c2) = (even, even), (odd, even), (even, odd), (odd, odd) (four distinct elements), and for each parity type the
sizes form all numbers of that parity from the minimum to (max c1 of that parity) + (max c2 of that parity); with a = 2 alpha + eps,
b = 2 beta + eta these maxima are 2(alpha+beta), 2(alpha+beta) + 2 eps - 1, 2(alpha+beta) + 2 eta - 1, 2(alpha+beta) + 2 eps + 2 eta - 2.  []
Hence (a, b) -> (a - 2, b + 2) (a >= 3) is exact in both directions (Lemma SPEC twice) and keeps H, every parity, every value.
**Lemma TR (pair transfer).**  In a representation, moving one rho_1 and one rho_-1 from a run R_s (a_s, b_s >= 1) to another run
R_t (possibly empty) leaves E+(z), E-(z) unchanged for every z (the two letters are effectively of opposite signs in every zone),
and Phi, delta, F, tau are untouched; by Lemma GR0 the two words are avoiders or solvable together.  []
**Lemma PM0 (merge across an even block).**  Let k >= 2 [r2 fix 2; as in the accepted PM*] and S_j an even block of a
representation.  Merge R_j, R_(j+1) into one run
(a_j + a_(j+1), b_j + b_(j+1)) and append the l_j letters of S_j to S_(j+1) (value y_(j+1)).  If w avoids, so does the result w'.
Proof.  Patterns of w' are the patterns of w containing both or neither of j, j + 1; for them S_j is not a boundary block, m, D_P,
B and every boundary parity agree (l_(j+1) + l_j = l_(j+1) mod 2), H is unchanged (floor((l_(j+1) + l_j)/2) = floor(l_(j+1)/2) +
l_j/2), so lambda and I agree (Lemma H0); theta' of the merged run is theta_j + theta_(j+1), so u_P agrees; I(empty) agrees.  []
Used below only when R_j, R_(j+1) are both NONEMPTY: then w' has the same empty runs with the same neighbouring values, one even
block fewer, and all other block parities unchanged.

## 3. Lemma BC' (block chain with the genuineness boost)

For a proper pattern Q of an avoider put lambda'(Q) := lambda(Q) + [lambda(Q) = 0 and u_Q != 0 (mod p)].
**Lemma BC'.**  Let w be an avoider (any length; windows of Lemma H0).  Let (P_1, ..., P_s), s >= 2, be an ordered partition of
[k] into nonempty proper patterns, Q_t := P_1 u ... u P_t.  If
 (a) lambda'(P_1) + ... + lambda'(P_s) >= p + 1;
 (b) for 2 <= t <= s - 1, with X = Q_(t-1), Y = P_t, Z = Q_t^c:  lambda'(X u Y) + lambda'(Y u Z) + lambda'(Z u X) >= p + 1 and
     lambda'(X) + lambda'(Y) + lambda'(Z) >= 1;
 (c) lambda'(P_s) + lambda'(P_s^c) >= 1,
then w has an identity 2p-subword (contradiction).
Proof.  (*) For every proper Q, u_Q is congruent to no element of I'(Q) := [1 - lambda'(Q^c), lambda'(Q) - 1].  Indeed I'(Q) = I(Q)
if no boost occurs; if exactly one of lambda(Q), lambda(Q^c) is 0 and boosted, I'(Q) = I(Q) u {0} or is empty; if both are 0 and
boosted, I'(Q) = {0}; and u_Q avoids I(Q) (Lemma H0) and 0 (the boost condition; u_(Q^c) = -u_Q).  Hence |I'(Q)| <= p - 1,
i.e. lambda'(Q) + lambda'(Q^c) <= p.  From here the proof of Lemma BC (inverse-parity/proof-PAR-K0.md L67-87) is repeated
verbatim with lambda' in place of lambda; it uses only (*) and arithmetic:
Claim: if y = u_Q (mod p) and 1 - l' <= y <= p + l - 1 (l = lambda'(Q), l' = lambda'(Q^c)) then l <= y <= p - l' (the ranges
[1 - l', l - 1] and [p + 1 - l', p + l - 1] consist of integers congruent to elements of I'(Q); as l + l' <= p the three ranges
[1 - l', l - 1], [l, p - l'], [p + 1 - l', p + l - 1] tile [1 - l', p + l - 1]; if l + l' <= 1 the outer ones are empty and
[1 - l', p + l - 1] lies in [l, p - l']).  Choose v_t = u_(P_t) (mod p) in [lambda'(P_t), p - lambda'(P_t^c)] (by the claim if
l + l' >= 1, since [1 - l', p + l - 1] then has >= p integers; directly if l + l' <= 0).  V_t := v_1 + ... + v_t = u_(Q_t).
Induction: V_t in [lambda'(Q_t), p - lambda'(Q_t^c)] for t <= s - 1: V_t lies in [lambda'(X) + lambda'(Y),
2p - lambda'(Y u Z) - lambda'(Z u X)], which by (b) lies in [1 - lambda'(Z), p + lambda'(X u Y) - 1], and the claim for Q_t = X u Y
(complement Z) applies.  Finally V_s = 0 (mod p), V_s >= p + 1 by (a), V_s <= (p - lambda'(P_s)) + (p - lambda'(P_s^c)) <= 2p - 1
by (c).  []

**Lemma CH (conditions (b), (c) for a family of interval partitions, B = kappa = 0).**  Let w be an avoider of length 4p - 2 with
B = kappa = 0 and R >= p, and let P_1, ..., P_s (s >= 2) be consecutive cyclic intervals in cyclic order partitioning [k], such
that every part either has R_P >= 1 or is a single genuine empty run with beta <= 1, and at most one part has R_P = 0.  Then (b)
and (c) of Lemma BC' hold.
Proof.  For a cyclic interval Q (m = 1), B = kappa = 0 and R_Q <= R <= 2p - 1 (by (Z0): A <= 2p - 1 and B = 0; this makes the cap p
inactive [r3, Claude m2]) give lambda(Q) = min(p, R_Q + 1 - beta,
floor(R_Q/2) + 1) = floor(R_Q/2) + 1 - def(Q), def(Q) := max(0, beta(Q) - ceil(R_Q/2)).  Every union U of parts that contains
>= 2 parts has R_U >= 1, so def(U) <= 1, and lambda'(U) >= lambda(U) >= 0; a single part has lambda' >= 0 too (R_P >= 1, or
R_P = 0 with beta <= 1: lambda = 1 - beta, boosted to 1 when it is 0 since the part is a genuine empty run).  (b) lower: X, Y, Z
are unions of parts with R_X + R_Y + R_Z = R >= 5, the largest has R_Q >= 2 and lambda >= 1.  (b) upper: the three unions
contain >= 2 parts each; their R-values sum to 2R, at most two are odd, so the floors sum to >= R - 1; two unions with def = 1
would both have R_U <= 2 and would cover the cycle (X u Y and Y u Z do), so R <= 4: impossible.  Hence the sum is
>= R - 1 + 3 - 1 >= p + 1.  (c): one of P_s, P_s^c has R_Q >= 3 (R >= 5), so def = 0 and lambda >= 2; the other has lambda' >= 0.  []

## 4. Theorem K0*

**Theorem K0*.**  Let p >= 5 be prime and w a word of length 4p - 2 over D_(2p) whose rotation letters all lie in one set
{rho_x, rho_-x}, x != 0.  If w is an avoider with kappa(w) = 0 (i.e. H = p - 1 exactly for its maximal constant blocks; H <= p - 1 for every avoider by
(Pairs)), then every maximal cyclic reflection run of w is constant.  [r3, Claude m5] In the terms of README.md Sec. 1
("REFL(p): every avoider w of length 4p-2 over D_(2p) whose rotation letters all lie in one set {rho_x, rho_-x}, x != 0, has every
maximal CYCLIC reflection run constant"), this is REFL(p) for the avoiders whose MAXIMAL CONSTANT BLOCKS give
kappa = p - 1 - sum floor(l_i/2) = 0 (on non-RGR words this kappa differs from any count over maximal reflection runs).
(Uses only Theorem P, EGZ/Lemma AR and the elementary lemmas above; Davenport-alpha enters only fact (V), which is not used
for K0* [r3, Claude m4]; o_F >= 1 comes from (Z0); no RGR theorem is imported.)

Proof.  Normalise x = 1.  If F = 0 there is nothing to prove; if R = 0, Lemma AR.  So w is a G-word with F, R >= 1; suppose it has
g >= 1 genuine empty runs and avoids.  By (Z0) and kappa = 0: B = 0 (all rotations rho_1), R = 2p - o_F, 1 <= o_F.

Step 1 (FUS process).  While some genuine empty run is adjacent to an even block, apply a FUS step there.  Each step preserves
avoidance, the length, every rotation, and lowers g by >= 1.  It never performs an odd-odd double fusion: such a step would output a
length-(4p - 2) avoider with H = p, i.e. kappa = -1, contradicting (Pairs).  So kappa stays 0 and B stays 0.  Let w_end be the final word.
Step 2 (w_end has no empty run).  Otherwise every empty run of w_end lies between two odd blocks, and no even block of w_end is
adjacent to an empty run.  Apply PM0 across every even block (both neighbouring runs are nonempty): each step preserves avoidance
and kappa = 0, keeps every empty run and the odd parity of its neighbours, and creates no even block next to an empty run.  The
resulting avoider has e_F = 0 and e_R >= g >= 1 > e_F + 2 kappa, contradicting (P0).
Step 3 (the last step).  Hence the process ends with an RGR word and its last step w' -> w_end removed every empty run of the
avoider w' (kappa(w') = 0, B = 0, g(w') >= 1).  [r3, Claude m3(i)] At least one FUS step occurs, because g(w) >= 1 and g(w_end) = 0
by Step 2; so w' exists (possibly w' = w).  A FUS step at an empty run R_t recolours an even neighbour, which then fuses with
the block on its other side only through a second empty run; so either
 (C1) g(w') = 1: one empty run R_t, and at least one of S_(t-1), S_t is even; or
 (C2) g(w') = 2: S_(t-1) = sigma_u^a, R_t empty, S_t = sigma_v^b with b even, R_(t+1) empty, S_(t+1) = sigma_u^c, u != v, and
      a, c not both odd (kappa = 0).
Step 4 (normalisation).  Apply PM0 across every even block of w' whose two neighbouring runs are nonempty.  This keeps
avoidance, kappa = 0, B = 0, the empty runs, their neighbouring blocks' values and parities.  Call the result w'' (still k, o_F,
e_F, e_R, R, r_i for its own decomposition).  [r3, Claude m3(ii)] w'' is re-indexed so that its empty run(s) are R_t (and
R_(t+1)); the surviving adjacent blocks keep the names S_(t-1), S_t (and S_(t+1)) with unchanged values and parities; their
lengths grow only by even amounts.  Now every even block of w'' is adjacent to an empty run, so its even blocks lie in
{S_(t-1), S_t} (C1) or {S_(t-1), S_t, S_(t+1)} (C2).  By (P0) and (Par), e_R <= e_F and e_R = e_F (mod 2), and e_R >= g.  Also
o_F <= p: the k - g nonempty runs give k - g <= R = 2p - o_F, and k - g = o_F + e_F - g >= o_F as e_F >= e_R >= g; so R >= p >= 5.
Step 5 (cases and partitions).  For a cyclic interval Q, lambda(Q) = floor(R_Q/2) + 1 - def(Q) as in Lemma CH.  Single runs are
written {i}.
 C1a: exactly one of S_(t-1), S_t is even.  Then e_F = 1, e_R = 1: R_t is the only even run and every nonempty run is odd;
   k = o_F + 1.  Parts: all single runs in cyclic order.  {t}: beta = 1, R = 0, lambda = 0, u_t = theta_t/2 != 0, lambda' = 1.
   The other run next to the even block has beta = 1 and lambda = (r + 1)/2; every other run has beta = 0 and lambda = (r + 1)/2.
   Sum = 1 + (R + k - 1)/2 = 1 + (2p - o_F + o_F)/2 = p + 1.
 C1b: both S_(t-1), S_t even.  Then e_F = 2, e_R = 2: R_t and exactly one nonempty even run.  k = o_F + 2 >= 3, so S_(t-2) and
   S_(t+1) are odd.  Parts: {t, t+1} (boundaries S_(t-1) even, S_(t+1) odd; R = r_(t+1) >= 1) and all other single runs ({t-1} has
   beta = 1, R >= 1).  Every part has lambda = floor(R_P/2) + 1, and the sum is
   sum_(i != t) (floor(r_i/2) + 1) = (R + (k - 1) + 1)/2 = (2p - o_F + o_F + 2)/2 = p + 1.
 C2a: exactly one of a, c even, say a odd and c even (the case a even, c odd is the mirror image below).  Then e_F = 2 (S_t,
   S_(t+1)), e_R = 2 (the two empty runs), every nonempty run odd, k = o_F + 2 >= 3, S_(t+2) odd (it is S_(t-1) if k = 3).
   Parts: {t} (boundaries S_(t-1) odd, S_t even: beta = 1, lambda = 0, u_t = (u - v)/2 != 0, lambda' = 1), {t+1, t+2} (boundaries
   S_t even, S_(t+2) odd; R = r_(t+2) >= 1, lambda = (r_(t+2) + 1)/2), all other single runs (beta = 0).  Sum =
   1 + sum_(i notin {t, t+1}) (r_i + 1)/2 = 1 + (R + k - 2)/2 = p + 1.
   Mirror (a even, c odd): parts {t+1} (boundaries S_t even, S_(t+1) odd, u_(t+1) = (v - u)/2 != 0, lambda' = 1), {t-1, t}
   (boundaries S_(t-2) odd, S_t even; R = r_(t-1) >= 1), all other single runs; the same sum p + 1.
 C2b: a, c both even.  Then e_F = 3, e_R = 3 (the two empty runs and exactly one nonempty even run), k = o_F + 3 >= 4, so S_(t-2)
   and S_(t+2) are odd.  Parts: {t-1, t} (boundaries S_(t-2) odd, S_t even; R = r_(t-1) >= 1), {t+1, t+2} (boundaries S_t even,
   S_(t+2) odd; R = r_(t+2) >= 1), all other single runs (beta = 0).  Sum = sum over the nonempty runs of (floor(r_i/2) + 1) =
   (R + (k - 2) + 1)/2 = (2p - o_F + o_F + 2)/2 = p + 1.
In every case the parts are consecutive cyclic intervals in cyclic order, each has R_P >= 1 or is a single genuine empty run with
beta = 1, and at most one part has R_P = 0.  So (a) holds, Lemma CH gives (b), (c), and Lemma BC' shows that w'' has an identity
2p-subword, contradicting its avoidance.  []

Remarks.  (1) The boost is essential: without it the C1a and C2a sums are exactly p.  [r3, Claude m5] The side remark of r2 that
the corresponding fused words (theta_t = 0) "are RGR avoiders in general" is unverified and carries no load.  (2) No inherited condition and no bound on k is used; (D0) can fail.
(3) K0* is the kappa = 0 case of REFL(p) for EVERY prime p >= 5; the cases kappa >= 1 are treated (as a reduction) in a separate
file.  (4) Finite aids: code/e2_k0star_replay.py replays Step 5 (to be run after this file is written).

## Fix map r1 -> r2 (Codex review R/olson-reflection-reduction-codex-v1.note.md, MINOR items on this file)

1. Codex MINOR 1 (r1 L78-83): second FUS inclusion corrected to Spec(sigma_u^(l'+l)) subset of Spec(sigma_v^(l') sigma_u^l) for
   even l'; proof of the second form written out.  Every later use recolours the EVEN block with its neighbour's value, which is
   exactly the corrected statement; the finite check E1 (out/e1_moves.json) tested this orientation (its "FUS_even_before" case).
2. Codex MINOR 2 (r1 L97-103): PM0 now assumes k >= 2 (all uses have k >= 2).
3. Codex MINOR 3 (r1 L15-20, L84-87): the maximal-decomposition and fusion bookkeeping is restricted to R >= 1; R = 0 is Lemma AR
   (already the first line of the proof of Theorem K0*); GR0 and H0 stay valid for every representation.
No other text is changed.

## Fix map r2 -> r3 (Claude review R/olson-k0star-r2-claude-v1.note.md; documentation only)

m1 (r2 L55-59 with L28): Lemma H0 now states that H, kappa, o_F, m and beta (including the kappa of I(empty)) are those of the
   named representation.
m2 (r2 L145): Lemma CH cites (Z0) for R_Q <= R <= 2p - 1.
m3 (r2 L171-180): the two implicit bookkeeping facts are stated (at least one FUS step occurs; re-indexing of w''); Step 1's
   odd-odd double fusion sentence is phrased conditionally.
m4 (r2 L159 with L70-72): Davenport-alpha is marked as entering only fact (V), unused for K0*.
m5 (r2 L157-159, L207-208): the README REFL definition is quoted and the kappa of K0* (maximal constant blocks) is made
   explicit; the parenthetical now reads H = p - 1 exactly; Remark (1)'s side claim is labelled unverified.
m6 (r2 L6): the r2 status sentence is corrected (fix 1 replaced a false lemma statement).
No formula, case, step or conclusion changed.
