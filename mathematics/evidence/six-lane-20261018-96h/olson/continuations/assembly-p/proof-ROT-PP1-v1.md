# Proposition VAC, Lemmas P and U, Theorem ROT-PP1-TOP: the rotation half at terminal k = p+1 (written proofs), v1

Owner OlsonAssemblyP. Written after /bin/date 2026-10-19T12:09:29-0700. Status: CANDIDATE_UNVERIFIED written proofs (word
level). Scopes frozen BEFORE derivation: ROT-PP1-scope-v1.md, sha256
698521494bcfbd951f417e182698102e3ba1f49559adc15d6a23d709d93686e0 (11:57:04), and ROT-PP1-scope-v1-addendum-1.md, sha256
d29e2180eac74d78b0c1346819f586835824c8605df53742cabcc1fcf2741b7c (12:06:22; exact statements). Inputs: the accepted normal
form (NF), GRX, Lemma CT, and the classical Cauchy-Davenport theorem. NOT used: (S1), Lev, the index-one theorem, S(p), REFL,
SHgen/SHgen-E, ROT-LS, ROT-KP/ROT-KP+, ROT-FB, ROT-SING, ROT-SING+, ONE-SHORT-LS, ASSEMBLY-P. No computation, model call,
novelty, priority, Lean or human-review claim. Kept separate from the ASSEMBLY-P packet (parent instruction, 12:05).

## 0. Statements

Throughout, p >= 7 is prime, w is an avoider of length 4p-2 over D_(2p) (no 2p letters in increasing original index order
with identity product), and w^ is an admissible normal form of w with terminal k blocks, H^ = (F-k)/2, kappa^ = p-1-H^,
R = 4p-2-F.

**Proposition VAC.** If k >= p+1, then kappa^ >= 1.

**Lemma P (pairing).** Let k = p+1 and (p-1)/2 <= kappa^ <= p-2. For every NON-CONSTANT sign pattern z, the multiset of
signed rotation values of w^ under z (Sec. 1) has a value of multiplicity at least R-p+2 = 2kappa^+1.

**Lemma U (dominant pair).** In the setting of Lemma P there is a NONZERO a in Z_p such that for every non-constant z the
value of Lemma P lies in {a, -a}. In particular at most p-2 rotation letters of w have a value outside {a, -a}.

**Theorem ROT-PP1-TOP.** If SOME admissible normal form of w has terminal k = p+1 and kappa^ = p-2, then every rotation
letter of w lies in one set {rho_c, rho_-c} with c != 0. More precisely, for a suitable such c the rotation multiset of w is
rho_c^A rho_(-c)^(3p-5-A) with 2p-3 <= A <= 2p-1.

There is no hypothesis on o_F(w) and nothing is asserted about reflection runs, about 1 <= kappa^ <= p-3 beyond VAC/P/U
(see obstruction-ROT-PP1-v1.md), or about kappa^ = p-1. p = 5 is not claimed.

## 1. Conventions and accepted inputs

Group law (v,e)(v',e') = (v+ev', ee'); rho_x = (x,+1), sigma_y = (y,-1). Y(x) := (1,x) in C_2 x C_p = C_(2p); a
sub-multiset of the Y(x) is zero-sum iff it has even size and value sum 0 (mod p). Multisets are occurrence multisets.
(NF) proof-ROT-few-E-v4.md lines 28-43 (accepted chain: fewodd addendum line 12; ZX overlays 1-3; lowodd item 2, M1, M4):
     w^ is an avoider of length 4p-2 with the same F and the same rotation multiset as w, written cyclically
     R_1 S_1 R_2 S_2 ... R_k S_k (block S_i between runs R_i and R_(i+1); indices mod k), every block S_i = sigma_(y_i)^(l_i)
     of ODD length, runs possibly empty, and EVERY EMPTY RUN SEPARATES BLOCKS OF DIFFERENT VALUES (line 38).
(GRX) notes-GRX-v1.md lines 7-20 (lowodd verdict item 1): for every cyclic constant-block representation (empty runs allowed)
     and every z in {+1,-1}^k, with f_i := [z_i != z_(i+1)], Phi := sum f_i, delta := #{i : l_i != f_i (mod 2)},
     C_max := F - delta, theta_i := y_(i-1) - y_i and T(z) := sum of theta_i over z_i = +1: the word has an identity
     2p-subword iff for some z there are an even C with Phi <= C <= C_max, 0 <= 2p-C <= R, and 2p-C rotation letters whose
     SIGNED sum (a letter of run i counted z_i times its value) is T(z) (mod p). The all-plus pattern gives kappa^ >= 0
     (accepted: ZX overlay 3, K01 m4) and (ZP_kappa^): no zero-sum of the rotation sequence with length in
     [2kappa^+2, 2p].
(CT) proof-LSplus-e2-v1.md lines 13-19 (STAB-delta verdict item 6): p >= 5 prime, 0 <= kappa <= p-1, Y odd with (ZP_kappa),
     1 <= n <= |Y|, |Y|-n even in [2kappa+2, 2p]  =>  sum_x min(n, v_x(Y)) <= p+n-2.
(CD) Cauchy-Davenport (classical): |X1 + X2| >= min(p, |X1|+|X2|-1) for nonempty X1, X2 in Z_p. Iterating with X2 = {0, d}:
     for nonzero d_1, ..., d_t, the set {0,d_1} + ... + {0,d_t} has at least min(p, t+1) elements; equivalently the set of
     subset sums (empty sum 0 included) of t nonzero residues has at least min(p, t+1) elements.

Selection rule (all blocks odd). For z with Phi = 2m: l_i != f_i (mod 2) iff f_i = 0, so delta = k-2m and
C_max = F-k+2m = 2H^+2m. Writing n := 2p-C (the number of selected rotation letters), GRX says: w^ has an identity
2p-subword iff for some z some EVEN n with
  max(0, 2kappa^+2-2m) <= n <= min(2p-2m, R)                                                       (SR)
admits n rotation letters of signed sum T(z) (here 2H^ = 2p-2-2kappa^).
For a set P of runs, z_P := -1 on P and +1 elsewhere; P is non-constant iff P is neither empty nor all runs; m(P) is the number
of maximal cyclic intervals of P. Since sum_i theta_i = 0, T(z_P) = sum_(i in P) tau_i with tau_i := y_i - y_(i-1); by (NF),
tau_i != 0 whenever R_i is empty. The signed value of a letter u of value x_u in run r is s_z(u) := z_r x_u;
phi_s(z) := #{u : s_z(u) = s}. At k = p+1: R = 2p+2kappa^-k = p-1+2kappa^.

## 2. Interface table

Abbreviations: R16 = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/ ;
R18 = /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/ ;
ROT = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/rotation/ ;
SR2 = /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/stab-round2/ .
Inclusive line ranges; whole-file sha256 recomputed at this writing; each equals the pin of its accepting verdict where given.

| Row | Interface as used | Source (path:lines, sha256) | Accepting verdict (path:lines, sha256, item) | Original domain | How each hypothesis is met |
|---|---|---|---|---|---|
| NF | admissible normal form: avoider, same F and rotation multiset; all blocks odd; empty runs separate different values | ROT/proof-ROT-few-E-v4.md:28-43, ac560eb81b0e17af5cad69345d7498fd431bc8f3c7e94b56701509983cb9ea8f | R16/olson-fewodd-parent-verdict-v1-addendum-1.md:12, 279d89d2d74046745a0db7600e06956d9ab5c7c200a598aff78c2a37b33ba62a; R16/olson-zx-s1c-parent-verdict-v1.md:51-53 (overlays 1-3), 2f8d376b524bdbac7e0a3ff5fa588744bd26a49b2858c9d0f0bb1db6dbeee6af; R16/olson-rotation-lowodd-parent-verdict-v2.md:8,29,32, 0853f4ac231a63e76fd97e8c986686fe53c6758a771ee67c504435f8cf1cba29 | every avoider of length 4p-2, p>=5 prime | w, p>=7 |
| GRX | exact criterion; all-plus gives kappa^>=0 and (ZP_kappa^) | ROT/notes-GRX-v1.md:7-20, afc6c31a2f9c9502655e3666595e535f4a003ccd7670ddbe993ebe4b620b1a30 | R16/olson-rotation-lowodd-parent-verdict-v2.md:7 (item 1); R16/olson-zx-s1c-parent-verdict-v1.md:53 (overlay 3); R16/olson-k01-parent-verdict-v1.md:53 (m4), e11144f613c7a396b2a8e2284e240154367b09b9720f015b87132a5d30fe0df4 | every word over D_(2p), p odd prime; every cyclic constant-block representation, empty runs allowed; every sign pattern | w^ with odd blocks, patterns z_P and all-plus (Secs. 3-5) |
| CT | sum_x min(n, v_x) <= p+n-2 | SR2/proof-LSplus-e2-v1.md:13-19, 2effb09ea4e28553ab0321a64b3e660c422d767ef940fcf58615dec8edc208b1 | R18/olson-STAB-delta-parent-verdict-v1.md:23 (item 6), ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5 | p>=5 prime, 0<=kappa<=p-1, odd (ZP_kappa) Y, 1<=n<=|Y|, |Y|-n even in [2kappa+2,2p] | kappa=p-2, |Y|=R=3p-5, n=p-3, |Y|-n=2p-2 (Sec. 5, Step 3) |
| CD | Cauchy-Davenport and its iterate | classical | classical import (also inside the accepted CT/RS) | Z_p, p prime | swap sums (Lemma P), subset sums (Sec. 5, Step 9) |

Context only (NOT premises; Sec. 6): the LS+2 sharpness families E2(p-2), E3(p-2) (R18/olson-STAB-delta-parent-verdict-v1.md:21,
item 4; SR2/proof-LSplus-e2-v1.md:24-26).

## 3. Proof of Proposition VAC

Let k >= p+1 and suppose kappa^ = 0. The k block values y_i lie in Z_p, so y_j = y_(j') for some blocks j != j'. Let P be the
runs R_(j+1), ..., R_(j') (cyclically): a nonempty proper set of runs forming one cyclic interval, so z_P changes sign exactly
at S_j and S_(j') (m = 1), and T(z_P) = sum over R_i in P of tau_i = y_(j') - y_j = 0. By (SR) with kappa^ = 0 and m = 1,
n = 0 is admissible (0 <= 2p-2, 0 <= R), and the empty selection has signed sum 0 = T(z_P). GRX gives w^ an identity
2p-subword, contradicting (NF) (w^ avoids). So kappa^ >= 1 (kappa^ >= 0 is accepted). []

## 4. Lemma M (pairs), Lemma P, Lemma U

Lemma M. A finite multiset S of size N with maximal multiplicity mu contains q pairwise disjoint pairs of elements with
different values whenever 2q <= N and q <= N - mu.
Proof. Cap every multiplicity at q. The capped total is >= 2q: if mu <= q it is N >= 2q; if mu > q, the top value keeps q and
the other values keep min(q, their total) >= min(q, N-mu) = q. Choose a sub-multiset S' of exactly 2q elements within the
caps, list S' with equal values consecutive as x_1, ..., x_(2q), and pair x_i with x_(i+q) (1 <= i <= q). If x_i = x_(i+q),
that value fills the q+1 consecutive positions i, ..., i+q, against its cap q. []

Proof of Lemma P. Let k = p+1, kappa := kappa^ in [(p-1)/2, p-2], so R = p-1+2kappa >= 2p-2, and let z be non-constant with
Phi = 2m, 1 <= m <= (p+1)/2 (Phi <= k). Put n := max(p-1, 2kappa+2-2m), an even number. Then n <= 2kappa (as p-1 <= 2kappa and
m >= 1), n <= 2p-2m (as p-1 <= 2p-2m and kappa <= p-1), and n <= R; so n satisfies (SR).
Suppose the signed multiset S_z (size R) has no value of multiplicity >= R-p+2, i.e. R - mu >= p-1. As 2(p-1) <= R, Lemma M
gives p-1 disjoint pairs {u_i, u'_i} (1 <= i <= p-1) with s_z(u_i) != s_z(u'_i). Let F0 be the R-2(p-1) = 2kappa-p+1 letters
in no pair and F' a subset of F0 with |F'| = n-(p-1) (0 <= n-p+1 <= 2kappa-p+1). For I in {1, ..., p-1} put
Q_I := F' u {u'_i : i in I} u {u_i : i not in I}: actual distinct letters, |Q_I| = n, and its signed sum is
sigma(Q_empty) + sum_(i in I) d_i with d_i := s_z(u'_i) - s_z(u_i) != 0. By (CD) the sums sum_(i in I) d_i fill Z_p
(min(p, (p-1)+1) = p), so some Q_I has signed sum T(z), and GRX (with C = 2p-n) gives an identity 2p-subword: contradiction.
So some value has multiplicity >= R-(p-2) = 2kappa+1. []

Proof of Lemma U. Fix a non-constant z and a value s of multiplicity >= 2kappa+1 in S_z. Since 2(2kappa+1) > R (equivalently
2kappa > p-3), s is unique; call it s(z). A letter of signed value s(z) has value s(z) or -s(z), so the class {s(z), -s(z)}
contains >= 2kappa+1 rotation letters (by value). Two different classes {x, -x} are disjoint, and 2(2kappa+1) > R, so all
non-constant z give the same class {a, -a}. Non-constant patterns exist (k >= 2), so a is defined.
a != 0: otherwise at least 2kappa+1 letters have value 0. Take blocks j != j' with y_j = y_(j') (pigeonhole, k = p+1 > p) and P
as in Sec. 3: m = 1, T(z_P) = 0, and n = 2kappa satisfies (SR) (2kappa <= 2p-2, 2kappa <= R). Any 2kappa letters of value 0
have signed sum 0: an identity 2p-subword, contradiction.
Finally the letters of value outside {a, -a} number at most R-(2kappa+1) = p-2. []

## 5. Proof of Theorem ROT-PP1-TOP

Let w^ have k = p+1 and kappa^ = p-2. Then H^ = 1, F = p+3, R = 3p-5, and (SR) reads: n in {2p-2, 2p} for m = 0; n in
{2p-4, 2p-2} for m = 1; n in {2p-6, 2p-4} for m = 2. (ZP_(p-2)) forbids zero-sums of length 2p-2 or 2p. Lemmas P and U apply
((p-1)/2 <= p-2). Let a be as in Lemma U, replaced by -a if necessary so that A := #(value a) >= A' := #(value -a). Let B be
the rotation letters of value != a, b := |B| = R-A, and delta := #(letters of value not in {a, -a}) = b-A'.

Step 1 (counts). By Lemma U, A + A' >= 2kappa^+1 = 2p-3 and delta <= p-2.
Step 2 ((ZP) bounds). p-1 letters a and p-1 letters -a would form a zero-sum of length 2p-2; so min(A, A') <= p-2, i.e.
A' <= p-2. 2p letters a would form a zero-sum of length 2p; so A <= 2p-1.
Step 3 (CT). CT with kappa = p-2 and n = p-3 (|Y|-n = 2p-2 is even and in [2p-2, 2p]) gives sum_x min(p-3, v_x) <= 2p-5. As
A >= 2p-3-A' >= p-1, the value a contributes p-3, so sum over x != a of min(p-3, v_x) <= p-2. Every x != a has v_x <= p-2
(A' <= p-2; a deviant value has v_x <= delta <= p-2). If all v_x <= p-3 (x != a), then b <= p-2. Otherwise one x != a has
v_x = p-2 and contributes p-3, the remaining values != a total <= 1, and b <= p-1. Hence b <= p-1, A = R-b >= 2p-4, and with
Step 2, b in {p-4, p-3, p-2, p-1}.
Step 4 (window). For a set P of runs let alpha(P), beta(P) count the letters of value a, -a in runs of P and
e(P) := alpha(P) - beta(P). Under z_P, the letters of signed value a are the a-letters outside P and the (-a)-letters in P, so
phi_a(z_P) = A - e(P); similarly phi_(-a)(z_P) = A' + e(P). For P non-constant, Lemmas P and U give
max(phi_a, phi_(-a)) >= 2p-3, i.e.
  e(P) <= lambda := A-2p+3 = p-2-b   or   e(P) >= Lambda := 2p-3-A',                                    (W)
and Lambda - lambda = 4p-6-A-A' = p-1+delta (A+A' = R-delta). Note lambda in {-1, 0, 1, 2} and e(all runs) = A-A'.
Step 5 (a heavy run). Some run h has e({h}) >= Lambda. Otherwise every single run has e({i}) <= lambda by (W). Number the
runs R_1, ..., R_k cyclically, P_t := {R_1, ..., R_t} (1 <= t <= k-1; non-constant). e(P_1) <= lambda, and
e(P_(k-1)) = A-A'-e({k}) >= A-A'-lambda = Lambda. Let t be least with e(P_t) >= Lambda (t >= 2); by (W) e(P_(t-1)) <= lambda,
so e({t}) >= Lambda-lambda = p-1+delta >= p-1 > 2 >= lambda: contradiction. Since alpha({h}) >= e({h}) >= Lambda =
2p-3-A' >= p-1, the run h is nonempty.

From now on suppose delta >= 1; we derive a contradiction, which proves delta = 0.

Step 6 (the other runs are light). Every nonempty set P' of runs not containing h has e(P') <= lambda. Otherwise, by (W),
e(P') >= Lambda; then alpha(P') >= Lambda and alpha({h}) >= Lambda give A >= 2Lambda = 4p-6-2A'. With A = 3p-5-b and
A' = b-delta this reads b >= p-1+2delta >= p+1, against Step 3.
Step 7 (b = p-1 is impossible). Then lambda = -1, so every run i != h has e({i}) <= -1, hence contains a letter of value -a.
These are k-1 = p runs, so A' >= p, against Step 2.
Step 8 (two empty runs when b <= p-2). Now lambda = p-2-b >= 0. Let P+ := {i != h : e({i}) >= 1}. If P+ is nonempty, Step 6
gives |P+| <= e(P+) <= lambda. A nonempty run i != h without a B-letter consists of a-letters only, so e({i}) >= 1 and
i is in P+. Hence the nonempty runs other than h number at most b + lambda = p-2 (b runs can contain a B-letter), at most
p-1 runs are nonempty, and at least (p+1)-(p-1) = 2 runs are EMPTY.
Step 9 (empty runs are impossible). For u in B put omega(u) := x_u - a != 0, let Sigma(B) be the set of subset sums of the
omega(u) (empty sum 0 included), Sigma_(>=1)(B) the sums over nonempty subsets, and M := Z_p \ Sigma(B). By (CD),
|Sigma(B)| >= min(p, b+1), so |M| <= p-1-b; and 0 is not in M.
Selections. For a pattern z with no letter on its negative side, every letter has signed value equal to its value. A set of n
rotation letters made of J in B and n-|J| letters of value a (possible iff n-|J| <= A) has sum n a + sum_(u in J) omega(u).
Such patterns are: all-plus (m = 0, T = 0); z_{i} for an EMPTY run R_i (m = 1, T = tau_i != 0); z_{i,i'} for two EMPTY runs
R_i, R_(i') (m = 1 if adjacent, m = 2 otherwise; T = tau_i + tau_(i')). Avoidance therefore gives, for each admissible n in
(SR): T - n a is not of the form sum_J omega with |J| >= n-A. In particular, when n <= A (no restriction on J), T - n a is in M.
- Case b = p-2 (A = 2p-3, |M| <= 1). Let R_i be empty. n = 2p-4 <= A: tau_i + 4a is in M, so M = {tau_i + 4a}.
  n = 2p-2 needs |J| >= 1: tau_i + 2a is not in Sigma_(>=1)(B). As tau_i + 2a != tau_i + 4a, it lies in Sigma(B), hence
  tau_i + 2a = 0, i.e. tau_i = -2a, for EVERY empty run. For two empty runs (Step 8), T = -4a and n = 2p-4 is admissible both
  for m = 1 and m = 2; 2p-4 letters of value a (<= A) have sum (2p-4)a = -4a = T: an identity 2p-subword. Contradiction.
- Case b = p-3 (A = 2p-2, |M| <= 2). All-plus with n = 2p-2 <= A: -(2p-2)a = 2a is in M. An empty run R_i (Step 8) with
  n = 2p-4, 2p-2 <= A: tau_i + 4a and tau_i + 2a are in M. As tau_i != 0, tau_i + 2a != 2a. If tau_i = -2a then
  tau_i + 2a = 0 is in M, impossible; otherwise 2a, tau_i + 2a, tau_i + 4a are three distinct elements of M. Contradiction.
- Case b = p-4 (A = 2p-1, |M| <= 3). As in the previous case, 2a is in M and, for an empty run R_i, tau_i != -2a and
  M = {2a, tau_i + 2a, tau_i + 4a} (three distinct elements). For two empty runs R_i, R_(i'), comparing the two descriptions of
  M gives {tau_i + 2a, tau_i + 4a} = {tau_(i') + 2a, tau_(i') + 4a}; the crossed matching would give 2a = -2a, so
  tau_i = tau_(i') =: tau0. Put x := tau0 (2a)^(-1) (x != 0, x != -1) so that M (2a)^(-1) = {1, x+1, x+2}. The pattern
  z_{i,i'} has T = 2tau0 and n <= 2p-2 <= A:
    adjacent (m = 1, n in {2p-4, 2p-2}): 2tau0 + 4a and 2tau0 + 2a are in M, i.e. 2x+2 and 2x+1 are in {1, x+1, x+2}.
      2x+1 = 1 or x+1 gives x = 0; so 2x+1 = x+2, x = 1, and then 2x+2 = 4 is not in {1, 2, 3} (p >= 7). Contradiction.
    non-adjacent (m = 2, n in {2p-6, 2p-4}): 2x+3 and 2x+2 are in {1, x+1, x+2}. 2x+2 = x+1 or x+2 gives x = -1 or 0; so
      2x+2 = 1, x = -1/2, and then 2x+3 = 2 would equal 1, 1/2 or 3/2, i.e. 1 = 0, 4 = 1 or 4 = 3 in Z_p. Contradiction.
With Step 7, every b in {p-4, ..., p-1} contradicts delta >= 1.

Conclusion. delta = 0: every rotation letter of w^ (hence of w, same multiset) has value a or -a with a != 0; A + A' = 3p-5,
A' <= p-2 and A <= 2p-1 give 2p-3 <= A <= 2p-1, and c := a is as stated. []

## 6. Remarks and checks recorded for review

- Exhaustiveness. Step 5 needs only Lemma P/U and (W); Steps 6-9 assume delta >= 1; Step 3 lists all b. Step 8 uses that h is
  nonempty and that every non-h nonempty run either contains a B-letter or lies in P+.
- GRX use. Every selection is of actual distinct letters; the reflections are those prescribed by GRX for the chosen C = 2p-n
  (C even and Phi <= C <= C_max by (SR)). The patterns used: all-plus, z_P for arbitrary non-constant P (Lemmas P/U, (W)),
  z_{i} and z_{i,i'} for empty runs. Empty runs are never assumed absent; they are where the contradiction is found.
- Where the values of tau enter: only through tau_i != 0 for empty runs (NF) and the sums tau_i + tau_(i').
- Sequence context (not a premise). At length 3p-5 = p + 2(p-2) - 1 the accepted LS+2 sharpness families
  E2(p-2) = h^(2p-4) (3h)^(p-1) and E3(p-2) = h^(p-4) (3h)^(2p-1) satisfy (ZP_(p-2)) and contain long zero-sums, so no
  sequence-level (S1) statement is available in this cell. The theorem shows that neither rotation multiset occurs for an
  avoider with such a normal form: for E2 no class {x, -x} holds 2p-3 letters (Lemma U fails; Lemma P gives an identity
  2p-subword); for E3 the class of the 2p-1 letters 3h is {a, -a} and the p-4 letters h are outside it (Steps 6-9, b = p-4).
- p >= 7 is used in Step 9 (4 not in {1, 2, 3}) and to match the lane's range; the arguments need p >= 5 elsewhere. p = 5 is
  not claimed.
- Trust: written proof relative to the accepted NF, GRX and CT (which rests on Cauchy-Davenport through Lemma RS) and the
  classical Cauchy-Davenport theorem. No computation is a premise; no cited input rests on a computer-assisted step.
- Not claimed: rotation rigidity for 1 <= kappa^ <= p-3 at k = p+1 (obstruction-ROT-PP1-v1.md records the exact failure points
  of this argument there), kappa^ = p-1, reflection rigidity, INV*, any o_F assembly, ordered Olson, p = 5, novelty,
  priority, Lean, human review.
