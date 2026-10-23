# Theorem PP1-EXCL: no avoider has an admissible normal form with terminal k = p+1 and kappa^ = p-1, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T12:46:13-0700 in one pass (no earlier draft). Status: CANDIDATE_UNVERIFIED
written proof (word level). Scope frozen BEFORE derivation: PP1-EXCL-scope-v1.md, sha256
d386f94414f0bdcbd44694d9676b836da511daa5c923200ff9375db977e32fba (2026-10-19T12:37:11-0700), with its pre-freeze disclosure
(planned route (s1)-(s3), sketched mentally, nothing written before the freeze).
Inputs, each at its accepted scope (table in Sec. 6): the normal form NF with its empty-run rule, GRX, Lemma CT, Lemma RS(b);
RS(b) rests on the classical Cauchy-Davenport theorem. NOT premises: the pending ROT-SING+ (context only), ROT-SING (k = p),
ONE-SHORT-LS, ASSEMBLY-P, ROT-PP1 / ROT-PP1-TOP, (S1), Lev, S(p), the index-one theorem, REFL at any o_F. No computation,
enumeration, model call, Lean, novelty, priority or human-review claim.
Labels: [NEW] = written here for this target. [RE-DERIVED] = same statement and argument as in the PENDING candidate
proof-ROT-SINGPLUS-v1.md (sha256 68865d55311128167ead7e3e966e92545520eb5224e4b44458ab469af67a8d9d), re-proved and re-checked in
full here so that the pending candidate is not a premise; NOT new progress.

## 0. Statements

THEOREM PP1-EXCL. Let p >= 7 be prime. No avoider w of length 4p-2 over D_(2p) (no 2p letters in increasing original index
order with identity product) has an admissible normal form w^ (SOME normal form produced by the accepted process; ZX overlay 2)
with terminal k = p+1 and kappa^ = p-1. No hypothesis on o_F(w), on the reflection runs of w, or on nonempty runs is made.

It is deduced (Sec. 2.1) from the word-level statement:

THEOREM PP1-EXCL'. Let p >= 7 be prime. No avoider u of length 4p-2 over D_(2p) has a cyclic constant-block representation
R_1 S_1 R_2 S_2 ... R_(p+1) S_(p+1) in which every S_i is ONE reflection sigma_(y_i), the rotation runs R_i may be empty, and
every empty run R_i separates blocks of different values (y_(i-1) != y_i).

THEOREM EXCL-PM [NEW]. Theorem PP1-EXCL' holds for every u all of whose rotation letters lie in one set {rho_c, rho_-c} with
c != 0. Its only input is GRX (the empty-run rule is part of the hypothesis on u).
Conditional reading: the pending ROT-SING+ asserts exactly this pair hypothesis at this cell (for w, hence for w^, which has the
same rotation multiset), so ROT-SING+ together with EXCL-PM would also give PP1-EXCL. The proof of PP1-EXCL' in Sec. 4 uses
neither ROT-SING+ nor EXCL-PM; Sec. 3 is an independent shorter route under the pair hypothesis.

Logical consequence (no further input): the hypothesis of the pending ROT-SING+ is never satisfied, so ROT-SING+ holds
vacuously and its rotation multiset describes no avoider. No step below uses p >= 7 beyond p >= 5; p = 5 is not claimed.

## 1. Conventions and accepted inputs

Group law (v,e)(v',e') = (v+ev', ee'); rho_x = (x,+1), sigma_y = (y,-1); x, y in Z_p. Y(x) := (1,x) in C_2 x C_p = C_(2p) (an
odd element). Sequences and multisets are occurrence sequences; v_x(.) is the multiplicity of the value x, sigma(.) the sum,
Sigma_n(S) (resp. Sigma_(<=K)(S)) the set of sums of n-term (resp. at most K-term, empty sum 0 included) subsequences of S.
(NF) proof-ROT-few-E-v4.md lines 28-43 (accepted: fewodd addendum 1 line 12; ZX overlays 1-3; lowodd verdict item 2 (PM*),
     M1, M4). The process ends with an avoider w^ of the same length and rotation multiset as w, written cyclically
     R_1 S_1 ... R_k S_k with blocks S_i = sigma_(y_i)^(l_i) of ODD length l_i (S_i between R_i and R_(i+1), indices mod k), in
     which every EMPTY run separates two blocks of DIFFERENT values (line 38); H^ = (F-k)/2, kappa^ = p-1-H^,
     R = 2p+2kappa^-k (line 42).
(GRX) notes-GRX-v1.md lines 7-20 (lowodd verdict item 1: every word, every cyclic constant-block representation, empty runs
     allowed; group law as above, verdict M2). theta_i := y_(i-1) - y_i; for z in {+1,-1}^k: f_i := [z_i != z_(i+1)],
     Phi := sum f_i, delta := #{i : l_i != f_i (mod 2)}, C_max := F - delta, X^z := union over i of z_i X_i,
     T(z) := sum over z_i = +1 of theta_i. The word has an identity 2p-subword iff for some z there is an even C with
     Phi <= C <= C_max, 0 <= 2p-C <= R and T(z) in Sigma_(2p-C)(X^z). Only the "if" direction is used.
(CT) proof-LSplus-e2-v1.md lines 13-19 (STAB-delta verdict item 6): p >= 5 prime, 0 <= kappa <= p-1, Y an odd sequence over
     C_(2p) with (ZP_kappa) (no zero-sum subsequence of length in [2kappa+2, 2p]; STAB-delta verdict line 9), 1 <= n <= |Y|,
     |Y|-n even with 2kappa+2 <= |Y|-n <= 2p  =>  sum_x min(n, v_x(Y)) <= p+n-2.
(RS(b)) proof-ROW-v1.md lines 16-19 (proof 20-27), read with erratum-2-prereq-consolidated.md R5 (lines 36-38) (CFXT verdict
     item 4): if every term of a sequence S over Z_p (p prime) is nonzero and K >= 0 is an integer, then
     |Sigma_(<=K)(S)| >= min(p, 1 + sum_x min(K, v_x(S))). (Its proof is iterated classical Cauchy-Davenport.)

## 2. The shape, the selection rule and the patterns used

2.1 PP1-EXCL' implies PP1-EXCL. Let w be an avoider of length 4p-2 and w^ an admissible normal form of w with k = p+1 and
kappa^ = p-1. By (NF), w^ is an avoider of length 4p-2 written as above; kappa^ = p-1 gives H^ = sum_i (l_i - 1)/2 = 0, so every
l_i = 1, F = k = p+1 and R = 4p-2-(p+1) = 3p-3 (= 2p+2kappa^-k). Thus u := w^ is a word excluded by PP1-EXCL'. []

2.2 The selection rule. From now on u is an avoider as in PP1-EXCL', X (|X| = 3p-3) its rotation multiset and X_i that of R_i.
For every z, all l_i = 1 give delta = #{i : f_i = 0} = p+1-Phi, so C_max = F - delta = Phi and GRX allows only C = Phi (always
even); and 0 <= 2p-Phi <= 2p <= 3p-3 (Phi <= p+1 <= 2p, p >= 3). Hence, by the "if" direction of GRX:
(SEL) if, for some z with Phi(z) = 2m, some 2p-2m rotation letters have signed sum T(z) (mod p), where a letter u of run r counts
      as z_r u, then u has an identity 2p-subword. (Equivalently: K := 3p-3-(2p-2m) = p-3+2m rotation letters are omitted.)
Put tau_i := y_i - y_(i-1) = -theta_i. The patterns used (k = p+1 >= 8):
(P0) z = all +1: Phi = 0, T = sum_i theta_i = 0; a selection is 2p rotation letters with sum 0.
(P1) z = -1 exactly on a cyclic interval J = {i, i+1, ..., j} of runs with 1 <= |J| <= p: f = 1 exactly at S_(i-1) and S_j
     (distinct, as |J| <= p), Phi = 2, T = -sum_(l in J) theta_l = y_j - y_(i-1). For J = {i}: T = tau_i; for J = {i, i+1}:
     T = tau_i + tau_(i+1).
(P2) z = -1 exactly on two runs R_i, R_l that are not cyclically adjacent (l not in {i-1, i, i+1} mod p+1): f = 1 exactly at the
     four distinct blocks S_(i-1), S_i, S_(l-1), S_l, Phi = 4, T = -(theta_i + theta_l) = tau_i + tau_l.
Direct check of (P1) for J = {i}, independent of the sign bookkeeping of GRX: reading cyclically from R_(i+1), the selection is
(rotations outside R_i, sum A), sigma_(y_(i-1)), (rotations of R_i, sum B), sigma_(y_i); by the group law its product is
(A + y_(i-1) - B - y_i, +1), the identity iff A - B = tau_i, which is the signed-sum condition of (SEL). Changing the cyclic cut
conjugates the product, so the cyclic reading is exact.

## 3. Theorem EXCL-PM [NEW]

Assume every rotation letter of u is rho_c or rho_-c, c != 0. For a pattern z let E_+(z) and E_-(z) be the numbers of rotation
letters whose signed value z_r u equals c, resp. -c; E_+(z) + E_-(z) = 3p-3.

LEMMA W (signed window). If Phi(z) = 2, E_+(z) >= p-1 and E_-(z) >= p-1, then u has an identity 2p-subword.
Proof. Among n := 2p-2 selected letters let q have signed value -c; their signed sum is (n-2q)c, and exactly the integers q with
max(0, n-E_+) <= q <= min(n, E_-) occur. E_+ >= p-1 gives E_- = 3p-3-E_+ <= 2p-2 = n, and likewise E_+ <= n; so q runs over the
p consecutive integers E_- - p + 1, ..., E_- (note E_- - p + 1 = n - E_+ >= 0). As p is odd and c != 0, 2c is a unit mod p, so
these p signed sums are pairwise distinct mod p, i.e. they are all of Z_p. In particular T(z) occurs and (SEL) applies. []

PROOF OF THEOREM EXCL-PM. Let A := v_c(X), B := v_(-c)(X); A + B = 3p-3.
Step 1 (P0). Among 2p letters let q be rho_(-c); their sum is (2p-2q)c = -2qc (mod p), zero iff p | q, and the available q are the
integers with max(0, 2p-A) <= q <= min(2p, B). Here q = 0 is available iff A >= 2p, q = 2p iff B >= 2p, and q = p iff A >= p and
B >= p. As u avoids, A, B <= 2p-1 and min(A, B) <= p-1; with A + B = 3p-3 also min(A, B) >= p-2. The hypothesis is symmetric in
c and -c, so we may assume A >= B: (A, B) = (2p-2, p-1) or (2p-1, p-2).
Step 2 (P1, single runs). For a run R_i let a_i, b_i be its numbers of letters rho_c, rho_(-c). For z = -1 on R_i only,
E_-(z) = (B - b_i) + a_i and E_+(z) = 3p-3-E_-(z); by Lemma W an avoider has E_-(z) <= p-2 or E_+(z) <= p-2, i.e.
E_-(z) <= p-2 or E_-(z) >= 2p-1.
- (A, B) = (2p-2, p-1). Then E_-(z) = p-1 + (a_i - b_i), so a_i - b_i <= -1 or a_i - b_i >= p. The latter needs a_i >= p, which
  holds for at most one run (2p > 2p-2 = A). So at least p of the p+1 runs have b_i >= a_i + 1 >= 1, whence B >= p > p-1 = B.
  Contradiction. (An empty run has a_i - b_i = 0 and is excluded by the same inequality.)
- (A, B) = (2p-1, p-2). Then E_-(z) = p-2 + (a_i - b_i), so a_i <= b_i or a_i >= b_i + p + 1; the latter needs a_i >= p+1, which
  holds for at most one run (2p+2 > 2p-1 = A).
  Step 3 (empty runs). Let R_i be empty. By the empty-run rule y_(i-1) != y_i, so tau_i != 0. For z = -1 on R_i: E_+ = A = 2p-1
  and E_- = B = p-2, so the available q are 0, ..., p-2 (max(0, (2p-2)-(2p-1)) = 0 and min(2p-2, p-2) = p-2), with signed sums
  (2p-2-2q)c = -2(q+1)c (mod p). As q+1 runs over 1, ..., p-1 and -2c is a unit, these are exactly the nonzero residues, so
  T = tau_i occurs and (SEL) gives an identity 2p-subword. Hence u has no empty run.
  So every run except at most one is nonempty with a_i <= b_i, hence has b_i >= 1; there are at least p such runs, so
  B >= p > p-2 = B. Contradiction. []

Where k = p+1 enters: at least p runs must each hold a letter rho_(-c), while B <= p-1. (Remark, not a claim: with only p runs
and the multiset rho_c^(2p-1) rho_(-c)^(p-1) of the accepted k = p cell, the analogous single-run inequalities are satisfiable,
e.g. by one run holding all 2p-1 letters rho_c and every other run holding exactly one rho_(-c); the count is tight by one. This
concerns these inequalities only, not the existence of avoiders at k = p.)

## 4. Theorem PP1-EXCL' without the pair hypothesis

### 4.1 Lemma CL [RE-DERIVED; ROT-SING+ Sec. 3]
X is of exactly one of the types
  (H1)  v_a(X) = 2p-1 for some a; the other p-2 letters form B, and no letter of B equals a;
  (H2a) X = a^(2p-2) b^(p-1) with b != a;
  (H2c) X = a^(2p-3) b^(p-1) c with c = 2a-b and b != a (so a, b, c are distinct).
Proof. (Z) By (P0) no 2p letters of X sum to 0 mod p. For the sequence Y := (Y(x))_(x in X) of odd elements of C_(2p), a
subsequence of length 2p has C_2-coordinate 0 and C_p-coordinate the sum of its x's; so Y has no zero-sum subsequence of length
2p, which is (ZP_(p-1)) (the length range [2kappa+2, 2p] is {2p} for kappa = p-1). As x -> Y(x) is injective, v_x(Y) = v_x(X).
CT with kappa = p-1 and n = p-3: 1 <= n <= |Y| = 3p-3 (p >= 4), and |Y| - n = 2p is even and lies in [2kappa+2, 2p] = {2p}. So
  (CT') sum_x min(p-3, v_x) <= p+n-2 = 2p-5.
Call x heavy if v_x >= p-2. A heavy value contributes p-3 to the sum in (CT'), any other value contributes v_x. With no heavy
value the sum is 3p-3 > 2p-5; three heavy values already contribute 3(p-3) > 2p-5 (p > 4). So there are one or two heavy values.
- One heavy value a: (p-3) + (3p-3-v_a) <= 2p-5 gives v_a >= 2p-1, and (Z) gives v_a <= 2p-1 (2p letters a sum to 2pa = 0).
  Type H1.
- Two heavy values a != b: 2(p-3) + (3p-3-v_a-v_b) <= 2p-5, so eps := 3p-3-v_a-v_b is 0 or 1 (at most one further letter c,
  c not in {a, b}). For i + j = 2p the choice a^i b^j sums to j(b-a) (mod p), which is zero iff p | j, and it is available iff
  max(0, 2p-v_a) <= j <= min(2p, v_b). (Z) excludes j = 0 (v_a >= 2p), j = 2p (v_b >= 2p) and j = p (v_a >= p and v_b >= p).
  Labelling so that v_a >= v_b: v_b <= p-1, hence v_b in {p-2, p-1}, and v_a <= 2p-1.
  eps = 0: (v_a, v_b) = (2p-1, p-2) (type H1 with B = b^(p-2)) or (2p-2, p-1) (type H2a).
  eps = 1: (v_a, v_b) = (2p-2, p-2) or (2p-3, p-1). For i + j = 2p-1 the choice a^i b^j c sums to j(b-a) - (a-c) (mod p). Let
  j* in {0, ..., p-1} with j*(b-a) = a-c (mod p). Then j* = 0 iff c = a, and j* = p-1 iff c = b (as -(b-a) = a-c iff c = b);
  both are excluded, so 1 <= j* <= p-2. The choice with j = j* is available iff j* <= v_b and 2p-1-j* <= v_a. For (2p-2, p-2)
  it is always available, contradicting (Z): this type is impossible. For (2p-3, p-1) it is available iff j* >= 2; so j* = 1,
  i.e. b-a = a-c and c = 2a-b: type H2c. []

### 4.2 Lemma OM and Corollary OM' [RE-DERIVED; ROT-SING+ Sec. 4]
Let z be a pattern with Phi(z) = 2m, m >= 1; Pi_+ (Pi_-) the rotation letters in runs with z = +1 (z = -1); K := p-3+2m (the
number of omitted rotation letters in (SEL)); a in Z_p; alpha_+ := the number of letters of value a in Pi_+; assume
alpha_+ >= K. Call FREE every rotation letter except the a-letters of Pi_+; a free letter u of run r gets the weight
omega(u) := z_r u - a; N_z is the sequence of the weights of the free letters, and D := sum over all rotation letters of z_r u.
LEMMA OM. If D - aK - T(z) lies in Sigma_(<=K)(N_z), then u has an identity 2p-subword.
Proof. Take free letters C with |C| <= K and sum_(u in C) omega(u) = D - aK - T(z), and K - |C| a-letters of Pi_+ (possible as
alpha_+ >= K; they are not free, hence disjoint from C). Omit these K letters. The remaining 3p-3-K = 2p-2m rotation letters
have signed sum D - sum_(u in C) z_r u - a(K - |C|) = D - aK - sum_(u in C) omega(u) = T(z), and (SEL) applies. []
COROLLARY OM'. Under the same assumptions, if at least p-1 entries of N_z are nonzero, u has an identity 2p-subword.
Proof. Let N' be the subsequence of nonzero entries, |N'| >= p-1; and K = p-3+2m >= p-1. If some v_x(N') > K, then
sum_x min(K, v_x(N')) >= K >= p-1; otherwise this sum is |N'| >= p-1. RS(b) (integer K >= 0, nonzero terms) gives
|Sigma_(<=K)(N')| >= p, so Sigma_(<=K)(N_z) contains Sigma_(<=K)(N') = Z_p, and Lemma OM applies. []

### 4.3 Lemma SR (single-run count) [NEW in this form]
Let a in Z_p and N := the number of rotation letters of value != a; for a run R_i let alpha_i := v_a(X_i) and
beta_i := v_(-a)(X_i) (for a = 0, beta_i = alpha_i). If v_a(X) - alpha_i >= p-1 and N + alpha_i - beta_i >= p-1, then u has an
identity 2p-subword.
Proof. Take z = -1 on R_i only (P1): m = 1, K = p-1, alpha_+ = v_a(X) - alpha_i >= K. With N_i := the number of letters != a in
R_i, the free letters are the N - N_i letters != a outside R_i, of weight u - a != 0, and the alpha_i + N_i letters of R_i, of
weight -u - a, which is 0 exactly for the beta_i letters u = -a. So N_z has N + alpha_i - beta_i nonzero entries, and
Corollary OM' applies. []

### 4.4 Lemma ER (empty runs in type H1) [RE-DERIVED; ROT-SING+ Sec. 5]
If X is of type H1, then u has at most one empty run.
Proof. Put B~ := (u - a)_(u in B), a sequence of p-2 NONZERO residues, and Sigma(B~) := Sigma_(<=p-2)(B~), the set of all its
subsums (0 included). RS(b) with K = p-2 (every multiplicity is <= p-2) gives |Sigma(B~)| >= p-1. Passing to complements,
Sigma(B~) is invariant under s -> sigma(B~) - s, and sigma(B~) = sigma(B) - (p-2)a = sigma(B) + 2a. If every run on which z = -1
is EMPTY, all rotation letters lie in Pi_+; then alpha_+ = 2p-1, the free letters are exactly the letters of B with N_z = B~,
D = sigma(X) = (2p-1)a + sigma(B), and Sigma_(<=K)(N_z) = Sigma(B~) for every K >= p-2.
Suppose u has two distinct empty runs.
(i) For an empty run R_i and z = -1 on R_i (P1): m = 1, K = p-1 <= 2p-1, T = tau_i, and D - aK - T = pa + sigma(B) - tau_i =
    sigma(B) - tau_i. By Lemma OM an avoider has sigma(B) - tau_i not in Sigma(B~), i.e. (complement symmetry)
    tau_i + 2a not in Sigma(B~). So Sigma(B~) = Z_p \ {r0} for one r0, with r0 != 0 (0 is the empty subsum), and tau_i = r0 - 2a
    for EVERY empty run R_i.
(ii) If two empty runs R_i, R_(i+1) are adjacent, take z = -1 on both (P1, J = {i, i+1}): K = p-1, T = tau_i + tau_(i+1), and as
    in (i) tau_i + tau_(i+1) + 2a = r0 = tau_i + 2a, so tau_(i+1) = 0, i.e. y_(i+1) = y_i. But the empty run R_(i+1) separates
    S_i and S_(i+1), which have different values. Contradiction.
(iii) Otherwise two empty runs R_i, R_l are not adjacent; take z = -1 on both (P2): m = 2, K = p+1 <= 2p-1, T = tau_i + tau_l,
    and D - aK - T = (p-2)a + sigma(B) - T = sigma(B) - 2a - T. An avoider has sigma(B) - 2a - T not in Sigma(B~), i.e.
    sigma(B~) - (sigma(B) - 2a - T) = T + 4a not in Sigma(B~), so T + 4a = r0. By (i), T = 2(r0 - 2a); so 2r0 = r0 and r0 = 0.
    Contradiction. []

### 4.5 Proof of Theorem PP1-EXCL'
By Lemma CL, X is of type H1, H2a or H2c; a is the value named there, N := 3p-3-v_a(X), and alpha_i, beta_i are as in Lemma SR.
Type H2a [NEW]. v_a = 2p-2 and N = p-1. At most one run has alpha_i >= p (2p > 2p-2), so at least p runs have
v_a - alpha_i >= p-1, and for each of them Lemma SR forces N + alpha_i - beta_i <= p-2, i.e. beta_i >= alpha_i + 1. If a = 0,
then beta_i = alpha_i: impossible. If a != 0, the letters of value -a are letters != a, so each of these at least p runs holds a
letter != a, and N >= p > p-1. Contradiction.
Type H2c [NEW]. v_a = 2p-3 and N = p. At most one run has alpha_i >= p-1 (2p-2 > 2p-3), so at least p runs have
v_a - alpha_i >= p-1, and for each of them Lemma SR forces beta_i >= alpha_i + 2. If a = 0 this is impossible (beta_i = alpha_i);
if a != 0, each of these runs holds at least two letters != a, so N >= 2p > p. Contradiction.
Type H1, a = 0 [RE-DERIVED]. The p+1 block values lie in Z_p, so y_j = y_(j') for some j != j'. For z = -1 exactly on the runs
R_(j+1), ..., R_(j') (P1; between 1 and p runs), T = y_(j') - y_j = 0, and any 2p-2 of the 2p-1 letters of value 0 have signed
sum 0: an identity 2p-subword by (SEL). Contradiction.
Type H1, a != 0 [RE-DERIVED; ROT-SING+ Sec. 6, here through Lemma SR]. N = p-2. Every run with alpha_i <= p has
v_a - alpha_i >= p-1, so Lemma SR forces beta_i >= alpha_i. If every run had alpha_i <= p, then
2p-1 = sum_i alpha_i <= sum_i beta_i <= N = p-2. So some run R_h has alpha_h >= p+1; it is unique (2p+2 > 2p-1), and every other
run has alpha_i <= p-2, hence beta_i >= alpha_i. Therefore a nonempty run R_i, i != h, holds a letter != a (if alpha_i >= 1 then
beta_i >= 1 and -a != a; if alpha_i = 0 all its letters are != a). So at most N = p-2 of the p runs other than R_h are nonempty,
and at least two runs are empty, against Lemma ER. Contradiction.
Every type is impossible. This proves Theorem PP1-EXCL', and Theorem PP1-EXCL follows by Sec. 2.1. []

## 5. Remarks, preserved branches, scope

- New versus re-derived. NEW: Theorem EXCL-PM with Lemma W (Sec. 3); Lemma SR and the eliminations of H2a and H2c (Secs. 4.3,
  4.5). RE-DERIVED (not new progress): Lemma CL, Lemma OM/OM', Lemma ER and the elimination of H1, i.e. the route of the pending
  ROT-SING+ (its Secs. 3-6), re-proved here step by step so that ROT-SING+ is not a premise. Compared with ROT-SING+: H2a is
  eliminated outright (not only reduced to b = -a), H2c needs no sub-case split, and H1 with a != 0 uses Lemma SR in place of the
  per-run OM' count of ROT-SING+ Sec. 6 (the same inequality beta_i >= alpha_i, now stated also for alpha_i = 0).
- Two routes for the final step. If the pending ROT-SING+ is accepted, Theorem EXCL-PM (GRX only) already gives PP1-EXCL. Sec. 4
  gives PP1-EXCL from NF, GRX, CT and RS(b) alone.
- Where k = p+1 is used: the counts "at least p runs" in Sec. 3 Step 2 and in Sec. 4.5, Lemma ER (through the H1 run count), and
  p+1 > |Z_p| in type H1 with a = 0.
- Patterns used: all-plus; single runs; one two-run arc (ER (ii)); one four-change pattern (ER (iii)); one arc between two
  equal-valued blocks (H1, a = 0). Patterns with Phi >= 6 and other arcs are not needed.
- Preserved branches. The planned route of the scope's pre-freeze disclosure ((s1) Lemma W, (s2) EXCL-PM, (s3) the single-run
  count in H2a/H2c) was confirmed in writing; no branch failed, and no earlier draft exists. Not attempted because not needed:
  windows for general Phi = 2m, couplings of several arcs, and any use of block values beyond tau_i != 0 for empty runs, the
  pigeonhole in H1 (a = 0) and Lemma ER.
- Not claimed: reflection rigidity; INV*; any statement for other (k, kappa^) or for o_F; any assembly (ASSEMBLY-P and ROT-PP1
  stay candidates and are not used); ordered Olson for D_(2p) or for all groups; existence or non-existence of avoiders outside
  this exact cell; p = 5 (no step uses more than p >= 5, but p = 5 is outside the frozen scope); Lev, S(p), REFL; novelty,
  priority, "first"; Lean or human review. CANDIDATE_UNVERIFIED; the parent owns reviews and verdicts.

## 6. Interface / scope / import table (whole-file sha256; LF line numbers)

| Input | Text of record (lines; sha256) | Accepted at (verdict, item) | Instance used here | Used in |
|---|---|---|---|---|
| NF | proof-ROT-few-E-v4.md 28-43, empty-run rule line 38; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | fewodd addendum 1 line 12; ZX overlays 1-3 (zx-s1c verdict lines 51-53: integer kappa, EXISTENTIAL normal form, k = 1 / DAV); lowodd v2 item 2 (PM*), M1, M4 | k = p+1, kappa^ = p-1: H^ = 0, singleton blocks, w^ an avoider of the same length and rotation multiset, empty-run rule | 2.1; 3 (Step 3); 4.4 (ii) |
| GRX | notes-GRX-v1.md 7-20; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | lowodd v2 item 1 (every word, every cyclic constant-block representation, empty runs) and M2 (group law) | "if" direction only; Phi = 0, 2, 4 with C = Phi | 2.2 and every pattern |
| CT | proof-LSplus-e2-v1.md 13-19; 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1 | STAB-delta item 6 (p >= 5 prime, 0 <= kappa <= p-1); (ZP_kappa) as at STAB-delta line 9 | kappa = p-1, n = p-3, Y = (Y(x)), |Y| = 3p-3, |Y|-n = 2p | 4.1 |
| RS(b) | proof-ROW-v1.md 16-27; a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d; erratum-2-prereq-consolidated.md R5 lines 36-38; fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5 | CFXT item 4 (integer K >= 0, nonzero terms) | K = p-1 (single runs, ER (i)-(ii)), K = p+1 (ER (iii)), K = p-2 (ER bound); nonzero terms only | 4.2, 4.4 |
| Cauchy-Davenport | classical; named in proof-ROW-v1.md lines 4-5 | CFXT verdict, "Limits" (classical import) | only inside RS(b) | - |

Verdict files (whole-file sha256): olson-rotation-lowodd-parent-verdict-v2.md
0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29; olson-zx-s1c-parent-verdict-v1.md
2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af; olson-fewodd-parent-verdict-v1-addendum-1.md
279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a (run six-lane-2026-10-16/review/);
olson-STAB-delta-parent-verdict-v1.md ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5;
olson-CFXT-ROW-LSII-parent-verdict-v1.md ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0 (run
six-lane-2026-10-18-96h/review/). Context only (not premises): proof-ROT-SINGPLUS-v1.md
68865d55311128167ead7e3e966e92545520eb5224e4b44458ab469af67a8d9d with parent commentary erratum
olson-ROT-SINGPLUS-parent-erratum-v1.md 905d14fedabe0842706094235fa1703f6f65a663bc45bc6d2ef5407e354cc9f4. All hashes were
re-read with shasum before this file was written. No cited input rests on a computer-assisted step.
