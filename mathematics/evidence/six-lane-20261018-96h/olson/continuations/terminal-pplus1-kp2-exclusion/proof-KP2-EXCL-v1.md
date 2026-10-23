# Theorem KP2-EXCL: no avoider has an admissible normal form with terminal k = p+1 and kappa^ = p-2, v1

Owner OlsonPP1Exclusion. Written after /bin/date 2026-10-19T13:03:04-0700 in one pass (no earlier draft). Status: CANDIDATE_UNVERIFIED
written proof (word level). Scope frozen BEFORE derivation: KP2-EXCL-scope-v1.md, sha256
20ea30954e76a18bbc6d4b02f826d35e2d285e1619f306997cf18f40447d9390 (2026-10-19T12:52:47-0700), with its pre-freeze disclosure
(generic plan only, nothing written or worked before the freeze).
Inputs, each at its accepted scope (table in Sec. 6): the normal form NF with its empty-run rule, GRX ("if" direction), Lemma
RS(b), and through RS(b) the classical Cauchy-Davenport theorem. Lemma CT is NOT needed (Sec. 4, Step 5 replaces the CT step of
ROT-PP1-TOP). NOT premises: the pending ROT-PP1 / ROT-PP1-TOP (context only), the pending PP1-EXCL, ROT-SING+, ROT-SING,
ONE-SHORT-LS, ASSEMBLY-P, (S1), Lev, S(p), LS+2, the index-one theorem, REFL at any o_F. No computation, enumeration, model call,
Lean, novelty, priority or human-review claim.
Labels: [NEW] = written here for this target. [RE-DERIVED] = same statement and argument as in the PENDING candidate
proof-ROT-PP1-v2.md (sha256 99143ea503a01a6376bed91a2a7ca8b91591617351f35ce4864117bf2949f1ca), Secs. 4-5, re-proved and re-checked
in full here so that it is not a premise; NOT new progress. [EXTENDED] marks the places where that argument is run WITHOUT its
assumption delta >= 1; this extension is what turns its rigidity statement into an exclusion.

## 0. Statements

THEOREM KP2-EXCL. Let p >= 7 be prime. No avoider w of length 4p-2 over D_(2p) (no 2p letters in increasing original index
order with identity product) has an admissible normal form w^ (SOME normal form produced by the accepted process; ZX overlay 2)
with terminal k = p+1 and kappa^ = p-2. No hypothesis on o_F(w), on the reflection runs of w, or on nonempty runs is made.

It is deduced (Sec. 2.1) from the word-level statement:

THEOREM KP2-EXCL'. Let p >= 7 be prime. No avoider u of length 4p-2 over D_(2p) has a cyclic constant-block representation
R_1 S_1 R_2 S_2 ... R_(p+1) S_(p+1) in which ONE block S_t = sigma_(y_t)^3 has length 3, the other p blocks are single
reflections S_i = sigma_(y_i), the rotation runs R_i may be empty, and every empty run R_i separates blocks of different values
(y_(i-1) != y_i).

THEOREM EXCL-PM2 [NEW]. Theorem KP2-EXCL' holds for every u all of whose rotation letters lie in one set {rho_c, rho_-c} with
c != 0. Its only input is GRX (the empty-run rule is part of the hypothesis on u).
Conditional reading: the pending ROT-PP1-TOP asserts exactly this pair hypothesis at this cell (for w, hence for w^, which has
the same rotation multiset), so ROT-PP1-TOP together with EXCL-PM2 would also give KP2-EXCL. The proof of KP2-EXCL' in Sec. 4
uses neither ROT-PP1-TOP nor EXCL-PM2; Sec. 3 is an independent route for the pair case.

Logical consequence (no further input): the hypothesis of the pending ROT-PP1-TOP is never satisfied, so it holds vacuously
and its rotation multisets rho_c^A rho_(-c)^(3p-5-A) describe no avoider. No step below uses p >= 7 beyond p >= 5; p = 5 is not
claimed.

## 1. Conventions and accepted inputs

Group law (v,e)(v',e') = (v+ev', ee'); rho_x = (x,+1), sigma_y = (y,-1); x, y in Z_p. Sequences and multisets are occurrence
sequences; v_x(.) is the multiplicity of the value x; Sigma_(<=K)(S) is the set of sums of at most K terms of S (empty sum 0
included); for K >= |S| it is the set of all subset sums of S.
(NF) proof-ROT-few-E-v4.md lines 28-43 (accepted: fewodd addendum 1 line 12; ZX overlays 1-3; lowodd verdict item 2 (PM*),
     M1, M4). The process ends with an avoider w^ of the same length and rotation multiset as w, written cyclically
     R_1 S_1 ... R_k S_k with blocks S_i = sigma_(y_i)^(l_i) of ODD length (S_i between R_i and R_(i+1), indices mod k), in which
     every EMPTY run separates two blocks of DIFFERENT values (line 38); H^ = (F-k)/2, kappa^ = p-1-H^, R = 2p+2kappa^-k.
(GRX) notes-GRX-v1.md lines 7-20 (lowodd verdict item 1: every word, every cyclic constant-block representation, empty runs
     allowed; group law as above, verdict M2). theta_i := y_(i-1) - y_i; for z in {+1,-1}^k: f_i := [z_i != z_(i+1)],
     Phi := sum f_i, delta := #{i : l_i != f_i (mod 2)}, C_max := F - delta, X^z := union over i of z_i X_i,
     T(z) := sum over z_i = +1 of theta_i. The word has an identity 2p-subword iff for some z there is an even C with
     Phi <= C <= C_max, 0 <= 2p-C <= R and T(z) in Sigma_(2p-C)(X^z). Only the "if" direction is used.
(RS(b)) proof-ROW-v1.md lines 16-19 (proof 20-27), read with erratum-2-prereq-consolidated.md R5 (lines 36-38) (CFXT verdict
     item 4): if every term of a sequence S over Z_p (p prime) is nonzero and K >= 0 is an integer, then
     |Sigma_(<=K)(S)| >= min(p, 1 + sum_x min(K, v_x(S))). Used only with K = |S|: the subset sums of t nonzero residues take at
     least min(p, t+1) values. (Its proof is iterated classical Cauchy-Davenport.)

## 2. The shape, the selection rule and the patterns

2.1 KP2-EXCL' implies KP2-EXCL. Let w be an avoider of length 4p-2 and w^ an admissible normal form of w with k = p+1 and
kappa^ = p-2. By (NF), w^ is an avoider of length 4p-2 written as above, and H^ = sum_i (l_i - 1)/2 = p-1-kappa^ = 1 with every
l_i odd: exactly one block S_t has l_t = 3 and the other p blocks have length 1. So F = p+3 and R = 4p-2-F = 3p-5
(= 2p+2kappa^-k). Thus u := w^ is a word excluded by KP2-EXCL'. []

2.2 The selection rule (recomputed for the length-3 block). From now on u is an avoider as in KP2-EXCL', X (|X| = 3p-5) its
rotation multiset and X_i that of R_i. For every z, all l_i are odd, so delta = #{i : f_i = 0} = p+1-Phi and
C_max = F - delta = Phi + 2; the even C allowed by GRX are C = Phi and C = Phi + 2. For C = Phi + 2 the long block S_t supplies
c_t = 3 letters (if f_t = 1) or c_t = 2 letters (if f_t = 0); every singleton supplies f_i letters. Also
0 <= 2p-Phi-2 and 2p-Phi <= 2p <= 3p-5 (Phi <= p+1, p >= 5). Writing n := 2p-C for the number of selected rotation letters:
(SEL2) if, for some z with Phi(z) = 2m, some n in {2p-2m, 2p-2m-2} rotation letters have signed sum T(z) (mod p), where a letter
      u of run r counts as z_r u, then u has an identity 2p-subword. T(z) does not depend on the choice of C.
Direct check of the extra reflections: two selected letters of the constant block S_t are consecutive in the selection and
multiply to sigma_(y_t) sigma_(y_t) = (0,+1); three multiply to sigma_(y_t). So C = Phi + 2 changes only the number of
selected rotation letters, not the signed-sum condition.
For a set P of runs let z_P := -1 on P and +1 elsewhere; P is non-constant if it is neither empty nor all runs; m(P) := the
number of maximal cyclic intervals of P, so Phi(z_P) = 2m(P); and T(z_P) = -sum_(i in P) theta_i = sum_(i in P) tau_i with
tau_i := y_i - y_(i-1). By the empty-run rule, tau_i != 0 for every empty run R_i. Patterns used:
(P0) z = all +1: Phi = 0, T = 0, n in {2p-2, 2p} (C = 2 uses two letters of S_t).
(P1) z_P for one cyclic interval P (m = 1): n in {2p-4, 2p-2}. For P = {i}: T = tau_i; for P = {i, i+1}: T = tau_i + tau_(i+1).
(P2) z_P for two non-adjacent runs P = {i, l} (m = 2): n in {2p-6, 2p-4}, T = tau_i + tau_l.
(Pm) z_P for any non-constant P: n in {2p-2m(P), 2p-2m(P)-2}, T = sum_(i in P) tau_i.

## 3. Theorem EXCL-PM2 [NEW]

Assume every rotation letter of u is rho_c or rho_-c, c != 0. For a pattern z let E_+(z) and E_-(z) be the numbers of rotation
letters whose signed value z_r u is c, resp. -c; E_+(z) + E_-(z) = 3p-5. Among n selected letters let q have signed value -c;
their signed sum is (n-2q)c, and exactly the integers q with max(0, n-E_+) <= q <= min(n, E_-) occur.

LEMMA W2 (signed window). Let P be non-constant, m := m(P), and n := 2p-2m-2 if m <= (p-1)/2, n := p-1 if m = (p+1)/2. Then n
is admissible in (SEL2), p-1 <= n <= 2p-4, and if E_+(z_P) >= p-1 and E_-(z_P) >= p-1, u has an identity 2p-subword.
Proof. Admissibility is clear (n = 2p-2m-2, resp. n = p-1 = 2p-2m). For m <= (p-1)/2, n = 2p-2m-2 >= p-1, and n <= 2p-4 as m >= 1;
also p-1 <= 2p-4. With L := max(0, n-E_+) and U := min(n, E_-): if L = 0 and U = n, U-L+1 = n+1 >= p; if L = 0 and U = E_-,
it is E_-+1 >= p; if L = n-E_+ and U = n, it is E_++1 >= p; if L = n-E_+ and U = E_-, it is E_+ + E_- - n + 1 = 3p-4-n >= p.
So q takes p consecutive values; as 2c is a unit mod p, the sums (n-2q)c are then all of Z_p, T(z_P) occurs and (SEL2)
applies. []

PROOF OF THEOREM EXCL-PM2. Let A := v_c(X), B := v_(-c)(X); A + B = 3p-5. The hypothesis is symmetric in c and -c, so assume
A >= B. For a set P of runs let a(P), b(P) be its numbers of letters rho_c, rho_(-c) (a_i, b_i for one run R_i); then
E_-(z_P) = B - b(P) + a(P) and E_+(z_P) = 3p-5-E_-(z_P). By Lemma W2, for every non-constant P:
  (*) E_-(z_P) <= p-2 or E_-(z_P) >= 2p-3.
Step 1 (P0). For n = 2p-2 the sum is -2(q+1)c, zero iff q = p-1, which is available iff A >= p-1 and B >= p-1; as A >= B,
avoidance gives B <= p-2. For n = 2p, q = 0 (2p letters rho_c, sum 2pc = 0) is available iff A >= 2p; so A <= 2p-1. Hence
(A, B) is (2p-3, p-2), (2p-2, p-3) or (2p-1, p-4).
Case (2p-3, p-2). By (*) for P = {i}: a_i - b_i <= 0 or a_i - b_i >= p-1; the latter needs a_i >= p-1, true for at most one
run (2p-2 > 2p-3). So at least p runs have a_i <= b_i; a nonempty one holds a letter rho_(-c), so at most B = p-2 of them are
nonempty and at least two runs are EMPTY. For an empty run R_i and z_{i}, every letter keeps its value (E_+ = 2p-3, E_- = p-2):
n = 2p-2 allows 1 <= q <= p-2 (sums -2(q+1)c), n = 2p-4 allows 0 <= q <= p-2 (sums -2(q+2)c); the attained sums are -2jc for
2 <= j <= p, i.e. every residue except -2c. As T = tau_i is not attained, tau_i = -2c for every empty run. For two empty runs
R_i, R_l the pattern z_{i,l} has T = -4c, and n = 2p-4 is admissible (m = 1 or 2); 2p-4 letters rho_c (A = 2p-3) have sum
(2p-4)c = -4c = T. Identity 2p-subword: contradiction.
Case (2p-2, p-3). For an empty run R_i and z_{i} (E_+ = 2p-2, E_- = p-3): n = 2p-2 allows 0 <= q <= p-3 (sums -2jc, j = q+1 in
[1, p-2]) and n = 2p-4 allows 0 <= q <= p-3 (j = q+2 in [2, p-1]); together every NONZERO residue, so tau_i != 0 is attained.
Hence no run is empty. By (*) for P = {i}: a_i - b_i <= 1 or a_i - b_i >= p; the latter needs a_i >= p, at most one run
(2p > 2p-2). At most B = p-3 runs hold a letter rho_(-c). So at least (p+1)-1-(p-3) = 3 runs have b_i = 0 and a_i <= 1 and are
nonempty, i.e. consist of one letter rho_c. For two of them, P = {i, i'}: E_-(z_P) = p-3+2 = p-1 and E_+(z_P) = 2p-4, so
Lemma W2 gives an identity 2p-subword: contradiction.
Case (2p-1, p-4). By (*) for P = {i}: a_i - b_i <= 2 or a_i - b_i >= p+1; the latter needs a_i >= p+1, at most one run
(2p+2 > 2p-1). At most B = p-4 runs hold a letter rho_(-c). So the set Q of runs with b_i = 0 and a_i <= 2 has at least
(p+1)-1-(p-4) = 4 elements, and Q is not all runs (B >= 1). For nonempty P in Q, E_-(z_P) = p-4+a(P), so (*) forbids
3 <= a(P) <= p. Adding the runs of Q one at a time, a(.) grows in steps <= 2; if a(Q) >= 3, the first partial union with
a >= 3 has a in {3, 4}, which lies in [3, p]. So a(Q) <= 2, and at least two runs of Q have a_i = 0, i.e. are EMPTY. For an empty
run R_i and z_{i} (E_+ = 2p-1, E_- = p-4): n = 2p-2 allows 0 <= q <= p-4 (j = q+1 in [1, p-3]) and n = 2p-4 allows
0 <= q <= p-4 (j = q+2 in [2, p-2]); the attained sums -2jc, 1 <= j <= p-2, miss exactly 2c and 0. So tau_i = 2c for every empty
run. For two empty runs R_i, R_l: T(z_{i,l}) = 4c and n = 2p-4 is admissible (m = 1 or 2); all p-4 letters rho_(-c) together
with p letters rho_c (p <= A) have sum (p - (p-4))c = 4c = T. Identity 2p-subword: contradiction. []

## 4. Theorem KP2-EXCL' without the pair hypothesis

For a pattern z, S_z denotes the multiset of the signed values z_r x_u of the R = 3p-5 rotation letters u (x_u the value of u),
and phi_s(z) := v_s(S_z).

### 4.1 Lemma M (pairs) [RE-DERIVED; ROT-PP1 Sec. 4]
A finite multiset S of size N with maximal multiplicity mu contains q pairwise disjoint pairs of elements with different values
whenever 2q <= N and q <= N - mu.
Proof. Cap every multiplicity at q. The capped total is >= 2q: if mu <= q it is N >= 2q; if mu > q, the top value keeps q and the
other values keep min(q, N - mu) = q or more (one of them alone keeps q if it has >= q copies; otherwise they keep their total
N - mu >= q). Choose 2q elements within the caps, list them with equal values consecutive as x_1, ..., x_(2q) and pair x_i with
x_(i+q) (1 <= i <= q). If x_i = x_(i+q), that value occupies the q+1 positions i, ..., i+q, against its cap. []

### 4.2 Lemma P (pairing) [RE-DERIVED; ROT-PP1 Sec. 4, at this cell]
For every non-constant z, S_z has a value of multiplicity >= 2p-3.
Proof. Let Phi(z) = 2m, 1 <= m <= (p+1)/2, and choose n as in Lemma W2: n admissible, p-1 <= n <= 2p-4. Suppose every
multiplicity of S_z is <= 2p-4 = R-(p-1). Lemma M (N = R = 3p-5, q = p-1, 2q <= N) gives p-1 disjoint pairs {u_i, u'_i} of
letters with s_i := z u_i != s'_i := z u'_i (signed values). The R-2(p-1) = p-3 letters in no pair contain a set F' of
n-(p-1) letters (0 <= n-(p-1) <= p-3). For I contained in {1, ..., p-1}, Q_I := F' u {u'_i : i in I} u {u_i : i not in I} is a
set of n actual letters with signed sum sigma(Q_empty) + sum_(i in I) d_i, d_i := s'_i - s_i != 0. By RS(b) (K = p-1 = number
of terms) the subset sums of the d_i take min(p, p) = p values, so some Q_I has signed sum T(z), and (SEL2) gives an identity
2p-subword. Contradiction. []

### 4.3 Lemma U (dominant pair) [RE-DERIVED; ROT-PP1 Sec. 4]
There is a NONZERO a in Z_p such that for every non-constant z the value of Lemma P lies in {a, -a}; at least 2p-3 rotation
letters have value in {a, -a}.
Proof. For non-constant z the value s(z) of Lemma P is unique, as 2(2p-3) > 3p-5. A letter of signed value s(z) has value s(z)
or -s(z), so the class {s(z), -s(z)} holds >= 2p-3 letters (by value). Different classes are disjoint and 2(2p-3) > 3p-5, so all
non-constant z give one class {a, -a}. If a = 0, at least 2p-3 letters have value 0; the p+1 block values lie in Z_p, so
y_j = y_(j') for some j != j', and for P := the runs R_(j+1), ..., R_(j') (one cyclic interval, between 1 and p runs) T(z_P) =
y_(j') - y_j = 0 and n = 2p-4 is admissible: 2p-4 letters of value 0 have signed sum 0 = T, an identity 2p-subword. []

### 4.4 The run analysis [RE-DERIVED from ROT-PP1 Sec. 5 Steps 2 and 4-9, EXTENDED to delta = 0, without CT]
Replace a by -a if necessary so that A := v_a(X) >= A' := v_(-a)(X). Put delta := 3p-5-A-A' (letters of value outside
{a, -a}) and b := 3p-5-A = A'+delta (letters of value != a); Lemma U gives A + A' >= 2p-3, i.e. delta <= p-2.
Step 1 (P0 bounds). p-1 letters a and p-1 letters -a have sum 0 (n = 2p-2): so A' <= p-2. 2p letters a have sum 0 (n = 2p): so
A <= 2p-1. Hence A >= 2p-3-A' >= p-1.
Step 2 (window). For a set P of runs let alpha(P), beta(P) be its numbers of letters of value a, -a, and e(P) := alpha(P) -
beta(P) (additive over disjoint unions; e(all runs) = A - A'); write alpha_i, beta_i, e_i for P = {i}. Under z_P the letters of
signed value a are the a-letters outside P and the (-a)-letters in P, so phi_a(z_P) = A - e(P) and phi_(-a)(z_P) = A' + e(P)
(a != -a). For P non-constant, Lemmas P and U give max(phi_a, phi_(-a)) >= 2p-3, i.e.
  (W) e(P) <= lambda := A-2p+3   or   e(P) >= Lambda := 2p-3-A',
with Lambda - lambda = 4p-6-A-A' = p-1+delta and lambda <= 2 (Step 1).
Step 3 (a heavy run). Some run h has e_h >= Lambda. Otherwise every single run has e_i <= lambda by (W). Number the runs
R_1, ..., R_(p+1) and put P_t := {R_1, ..., R_t} (1 <= t <= p, non-constant). e(P_1) <= lambda < Lambda and
e(P_p) = A - A' - e_(p+1) >= A - A' - lambda = Lambda. Let t >= 2 be least with e(P_t) >= Lambda; by (W), e(P_(t-1)) <= lambda,
so e_t >= Lambda - lambda = p-1+delta > 2 >= lambda, whence e_t >= Lambda by (W): contradiction. As alpha_h >= e_h >= Lambda =
2p-3-A' >= p-1, the run R_h is nonempty.
Step 4 (light sets) [EXTENDED]. Every nonempty set P' of runs not containing h has e(P') <= lambda. Otherwise e(P') >= Lambda by
(W) (P' is non-constant), so alpha(P') >= Lambda and alpha_h >= Lambda on disjoint runs, A >= 2Lambda = 4p-6-2A'; with
A = 3p-5-delta-A' this gives A' >= p-1+delta >= p-1, against Step 1. (This holds for every delta >= 0; ROT-PP1 used delta >= 1
here and derived b >= p-1+2delta, the same inequality.)
Step 5 (lambda >= 0) [NEW form; replaces the CT step and Step 7 of ROT-PP1]. If lambda <= -1, then by Step 4 every run i != h
has e_i <= -1, hence beta_i >= 1; these are p runs, so A' >= p, against Step 1. So lambda >= 0, i.e. A >= 2p-3, and with
A <= 2p-1: b = 3p-5-A is p-2, p-3 or p-4, and lambda = p-2-b is 0, 1 or 2.
Step 6 (two empty runs) [RE-DERIVED]. Let P+ := {i != h : e_i >= 1}. If P+ is nonempty, Step 4 gives |P+| <= e(P+) <= lambda.
A nonempty run i != h without a letter of value != a consists of a-letters only, so e_i >= 1 and i is in P+. Hence at most
b + lambda = p-2 runs other than h are nonempty (at most b runs hold a letter != a), at most p-1 runs are nonempty, and at least
(p+1) - (p-1) = 2 runs are EMPTY.
Step 7 (empty runs are impossible) [RE-DERIVED; valid for every delta >= 0]. Let B be the b letters of value != a; for u in B
put omega(u) := x_u - a != 0; Sigma(B) := the set of subset sums of the omega(u) (empty sum 0 included);
Sigma_(>=1)(B) := the sums over nonempty subsets; M := Z_p \ Sigma(B). By RS(b) (K = b, nonzero terms), |Sigma(B)| >=
min(p, b+1) = b+1, so |M| <= p-1-b, and 0 is not in M.
For the patterns all-plus, z_{i} with R_i empty, and z_{i,i'} with R_i, R_(i') empty, no letter lies on the negative side and every
signed value equals the value. A set of n rotation letters consisting of J contained in B and n-|J| letters of value a (possible
iff n-|J| <= A; here |J| <= b <= p-2 <= 2p-6 <= n always) has sum na + sum_(u in J) omega(u). So avoidance gives, for every
admissible n: T - na is not sum_J omega for any J with |J| >= n-A; in particular T - na is in M whenever n <= A.
- b = p-2 (A = 2p-3, |M| <= 1). Let R_i be empty (T = tau_i). n = 2p-4 <= A: tau_i + 4a is in M, so M = {tau_i + 4a}.
  n = 2p-2 = A+1 needs |J| >= 1: tau_i + 2a is not in Sigma_(>=1)(B). As tau_i + 2a != tau_i + 4a, it is in Sigma(B), hence it is
  the empty sum: tau_i + 2a = 0, i.e. tau_i = -2a, for EVERY empty run. For two empty runs (Step 6), T(z_{i,i'}) = -4a and
  n = 2p-4 is admissible for m = 1 and for m = 2; 2p-4 letters a (<= A) have sum (2p-4)a = -4a = T: identity. Contradiction.
- b = p-3 (A = 2p-2, |M| <= 2). All-plus with n = 2p-2 <= A: -(2p-2)a = 2a is in M. For an empty run R_i (Step 6) with
  n = 2p-4, 2p-2 <= A: tau_i + 4a and tau_i + 2a are in M. As tau_i != 0, tau_i + 2a != 2a. If tau_i = -2a, then 0 = tau_i + 2a is
  in M, impossible; otherwise 2a, tau_i + 2a, tau_i + 4a are three distinct elements of M. Contradiction.
- b = p-4 (A = 2p-1, |M| <= 3). As before 2a is in M, and for an empty run R_i, tau_i != -2a and M = {2a, tau_i+2a, tau_i+4a}
  (three distinct elements). For two empty runs R_i, R_(i') (Step 6): {tau_i+2a, tau_i+4a} = {tau_(i')+2a, tau_(i')+4a}; the
  crossed matching would give tau_i + 2a = tau_(i') + 4a and tau_i + 4a = tau_(i') + 2a, hence 4a = 0; so tau_i = tau_(i') =: tau0.
  Put x := tau0 (2a)^(-1); x != 0 and x != -1, and M (2a)^(-1) = {1, x+1, x+2}. Here every admissible n <= 2p-2 is <= A.
    If R_i, R_(i') are adjacent (m = 1, n in {2p-4, 2p-2}, T = 2tau0): 2tau0 + 4a and 2tau0 + 2a are in M, i.e. 2x+2 and 2x+1 are in
    {1, x+1, x+2}. 2x+1 = 1 or 2x+1 = x+1 gives x = 0; so 2x+1 = x+2, x = 1, and 2x+2 = 4 would be 1, 2 or 3 mod p (p >= 5).
    If they are not adjacent (m = 2, n in {2p-6, 2p-4}): 2x+3 and 2x+2 are in {1, x+1, x+2}. 2x+2 = x+1 or x+2 gives x = -1 or 0;
    so 2x+2 = 1, x = -1/2, and 2x+3 = 2 would equal 1, 1/2 or 3/2, i.e. 1 = 0, 4 = 1 or 4 = 3 mod p. Contradiction either way.
By Step 5, b is one of p-2, p-3, p-4, and every case is contradictory. This proves Theorem KP2-EXCL', and Theorem KP2-EXCL
follows by Sec. 2.1. []
(Specialised to delta = 0, Sec. 4 re-proves the pair case by a route different from Sec. 3.)

## 5. Remarks, preserved routes, scope

- New versus re-derived. NEW: Theorem EXCL-PM2 with Lemma W2 (Sec. 3); Step 5 (lambda >= 0 without CT); the observation that
  Steps 4, 6 and 7 hold for delta = 0, so that the ROT-PP1-TOP argument excludes the cell instead of proving delta = 0.
  RE-DERIVED (not new progress): Lemmas M, P, U, the window (W), the heavy run, the light sets, the empty-run count and the
  three-case empty-run analysis of proof-ROT-PP1-v2.md Secs. 4-5.
- Where the length-3 block enters: through C = Phi + 2, i.e. the second admissible length n = 2p-2m-2. It is used in Lemma P
  (n = 2p-2m-2 for m <= (p-1)/2), Lemma U (n = 2p-4), Step 1 and Sec. 3 Step 1 (all-plus n = 2p-2 uses two letters of S_t), and
  Step 7 and Sec. 3 (n = 2p-4 for one empty run, n = 2p-6 for two non-adjacent empty runs).
- Where k = p+1 enters: pigeonhole on p+1 block values (Lemma U, a != 0); the count "p runs other than h" (Step 5); the count
  (p+1)-(p-1) = 2 empty runs (Step 6); in Sec. 3 the counts (p+1)-1-B.
- Preserved routes (arithmetic kept; not used in the proof).
  (F1) Single-run omission counts in the style of PP1-EXCL (Lemma SR, K = p-1 omitted letters, n = 2p-4): with b letters != a,
       a run with A - alpha_i >= p-1 has b + alpha_i - beta_i nonzero weights, so OM' forces alpha_i <= beta_i + (p-2-b). For
       b = p-2 this gives alpha_i <= beta_i and two empty runs, but for b = p-3 (alpha_i <= beta_i + 1) and b = p-4
       (alpha_i <= beta_i + 2) single runs alone do not force empty runs; the set window (W) with Step 4 is what closes these.
  (F2) Pure +-c single-run windows in case (2p-2, p-3) allow runs consisting of one letter rho_c; pairs of such runs
       (Lemma W2 with m = 1 or 2) close the case.
  (F3) The CT step of ROT-PP1 (n = p-3, b <= p-1) is not needed: Step 5 gives b <= p-2 directly from Steps 1-4.
- Not claimed: reflection rigidity; INV*; any statement for other (k, kappa^) (in particular 1 <= kappa^ <= p-3 at k = p+1, where
  Lemma P needs kappa^ >= (p-1)/2 and Steps 5-7 use kappa^ = p-2) or for o_F; any assembly; ordered Olson for D_(2p) or for all
  groups; existence or non-existence of avoiders outside this exact cell; p = 5; Lev, S(p), REFL; novelty, priority, "first";
  Lean or human review. CANDIDATE_UNVERIFIED; the parent owns reviews and verdicts.

## 6. Interface / scope / import table (whole-file sha256; LF line numbers)

| Input | Text of record (lines; sha256) | Accepted at (verdict, item) | Instance used here | Used in |
|---|---|---|---|---|
| NF | proof-ROT-few-E-v4.md 28-43, empty-run rule line 38; ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | fewodd addendum 1 line 12; ZX overlays 1-3 (zx-s1c verdict lines 51-53); lowodd v2 item 2 (PM*), M1, M4 | k = p+1, kappa^ = p-2: H^ = 1, one length-3 block, w^ an avoider of the same length and rotation multiset, empty-run rule (tau_i != 0) | 2.1; 3; 4.3; 4.4 Steps 6-7 |
| GRX | notes-GRX-v1.md 7-20; afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | lowodd v2 item 1 (every word, every cyclic constant-block representation, empty runs) and M2 (group law) | "if" direction only; C = Phi or Phi + 2 with the long block supplying 2 or 3 letters | 2.2 and every pattern |
| RS(b) | proof-ROW-v1.md 16-27; a7b73415a83a6d898589c820d311e5ad084e864521adf937f1eee05d69fc4b2d; erratum-2-prereq-consolidated.md R5 lines 36-38; fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5 | CFXT item 4 (integer K >= 0, nonzero terms) | K = number of terms: p-1 differences d_i (Lemma P); b weights omega (Step 7) | 4.2, 4.4 |
| Cauchy-Davenport | classical; named in proof-ROW-v1.md lines 4-5 | CFXT verdict, "Limits" (classical import) | only inside RS(b) | - |

Verdict files (whole-file sha256): olson-rotation-lowodd-parent-verdict-v2.md
0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29; olson-zx-s1c-parent-verdict-v1.md
2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af; olson-fewodd-parent-verdict-v1-addendum-1.md
279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a (run six-lane-2026-10-16/review/);
olson-CFXT-ROW-LSII-parent-verdict-v1.md ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0 (run
six-lane-2026-10-18-96h/review/). Context only (not premises): proof-ROT-PP1-v2.md
99143ea503a01a6376bed91a2a7ca8b91591617351f35ce4864117bf2949f1ca with parent errata olson-ROT-PP1-parent-erratum-v1.md
7f192a89e50ab349a37999669d0e1d411034f626730fac6118c0a546b886e479 and -v2.md
49c3e4917ed59647d52eb204c73b6157a4aa08de7fb596345ca67c9f2c086646; Codex review olson-ROT-PP1-codex-v1.prompt.stdout.txt
7fda7f0bcc77c01a6adaabac658947ba4f1bd17db852ce25e1b17aebd9758525. No cited input rests on a computer-assisted step.
