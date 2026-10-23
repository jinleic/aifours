# Reflection half for o_F > p: arc systems, Cauchy-Davenport kills, and the cell R = p for every B (candidate v3)

Owner OlsonReflectionSuccessor (Slice B of R18/olson-two-slice-successor-brief-v1.md).  Written after host clock
2026-10-19T05:33:33-0700.  Status: CANDIDATE_UNVERIFIED; written research only; no computation; no model review.
Supersedes proof-REFLHI-arcs-v2.md (unsent; kept unchanged) and the unsent draft proof-REFLHI-tools-v1.md (kept unchanged).
Fix map v2 -> v3 at the end.  Scope: words of length 4p - 2 over D_(2p) whose rotation letters lie in one pair
{rho_x, rho_-x}, x != 0.  No claim about rotation values, INV*(p) as a whole, ordered Olson, Lean, novelty or priority.

Paths: REFL/ = mathematics/evidence/six-lane-20261016/olson/inverse-normalization-20261018/reflection/;
R16/ = institute/runs/six-lane-2026-10-16/review/; R18/ = institute/runs/six-lane-2026-10-18-96h/review/.

## 0. Imports (parent-accepted, at their exact scopes; hashes re-checked 2026-10-19 03:5x PDT)

* (H0) Lemma H0, REFL/proof-K0star-r2.md, sha256 6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1, L55-65:
  for every cyclic constant-block representation of every length (accepted in R16/olson-reflection-K0star-RED-parent-
  verdict-v1.md, 879aeee781a080d1b1cb4a4489f62e45e2fa332f7c2d9242f725cfae1d00c02a, as algebra on the accepted GRX).
* (P0) and (Z0), same file, Sec. 1 "Facts for G-avoiders of length 4p - 2": e_R <= e_F + 2 kappa with empty runs counted
  as even rotation runs (from the accepted Theorem P); an avoider has A, B <= 2p - 1, and after the normalisation A >= B,
  B <= kappa.  Normalisation N (rho_v -> rho_-v, sigma_v -> sigma_-v; K0star-r2 L35-36) keeps blocks, lengths, empty runs.
* (RED) REFL/proof-RED-r2.md, c4e7697f0f691980e19ef3332a1e2c6b0dbdc76ba268e87c32eb563f4d3fd3d7: Theorem RED and its proof
  (with (I1)-(I4), K0*, K1*, SING, KB*, CAP, KBH*, TII, QQ at their accepted scopes), same verdict.
* (SMALLK) R16/olson-reflection-smallk-parent-verdict-v1.md (b71fcaf461a98bf9f034871208a298a471dcbb2006aa26c9153d523e140413b8):
  RES_<(p) has no avoider with k <= p.
* (FEW) REFL/proof-REFL-fewodd-r5.md (4615dcb957966ee4c18166c269e1c9c8a1bc4ee6f9bc48539155079b297a5363; parent verdict
  R16/olson-refl-fewodd-parent-verdict-v1.md accepts the errata-equivalent r4 1e447754...861d): REFL(p) for o_F <= p.
* (CD) Cauchy-Davenport (classical): nonempty A_1, ..., A_s in Z_p, p prime: |A_1 + ... + A_s| >= min(p, sum|A_i| - s + 1).
Not used: rotation rigidity, INV*, SLZ3, RED-r3, K0star-r3, MXG/B0S beyond (SMALLK), any finite computation.

## 1. Frozen target and the exact residual

**REFL-HI(p).**  For prime p >= 5, every avoider w0 of length 4p - 2 over D_(2p) whose rotation letters lie in one set
{rho_x, rho_-x}, x != 0, and with o_F(w0) >= p + 1 (o_F = number of ODD blocks of the maximal cyclic CONSTANT reflection
block decomposition, not of maximal reflection runs) has every maximal cyclic reflection run constant.
(FEW) and REFL-HI(p) together are REFL(p) of REFL/README.md L17-19.
**RES-HI(p).**  RES_<(p) (RED-r2 L132-133) has no avoider with kappa >= 2 and k >= p + 1.
**Lemma 1.1.**  RES-HI(p) implies REFL(p).
Proof.  A word violating REFL(p) is turned by the proof of Theorem RED into an avoider in RES_<(p) with kappa >= 2 (its
terminal state); by (SMALLK) it has k >= p + 1, contradicting RES-HI(p).  []
Status: RES-HI(p) and REFL-HI(p) remain OPEN.  Secs. 3-5 prove new exclusions and structure; Sec. 6 states what remains.

## 2. Setting and windows

Setting (S): p >= 5 prime; w a cyclic word R_1 S_1 ... R_k S_k (run R_t immediately precedes block S_t; indices mod k)
of length 4p - 2, F, R >= 1, rotation letters in {rho_1, rho_-1}, A >= B, every maximal constant block
S_t = sigma_(y_t)^(l_t) of ODD length; empty runs are genuine (y_(t-1) != y_t) by maximality.  Runs need not be pure.
kappa = p - 1 - H, g := kappa - B, D = A - B, d_t = a_t - b_t, u_t = (y_(t-1) - y_t)/2 in Z_p, R = 2p - k + 2 kappa.
**Lemma W.**  In setting (S), w has an identity 2p-subword as soon as some proper nonempty pattern P (set of runs) with
m = m(P) maximal cyclic intervals and D_P = sum_(t in P) d_t has u_P := sum_(t in P) u_t congruent (mod p) to an element of
   I(P) = [-G_m(D - D_P), G_m(D_P)],   G_m(x) := min(p - m, x + B - kappa + m - 1, floor((x + B)/2)).
Proof.  (H0) with beta(P) = 0 (all blocks odd): lambda(P) - 1 = min(p - m, E - kappa + m - 1, floor(E/2)) with
E = D_P + B, and the complement has E = D - D_P + B.  []
Notation.  E+(P) := D_P + B = A_P + B_(P^c) and E-(P) := R - E+(P).  Then G_m(D_P) = gamma_m(E+(P)) and
G_m(D - D_P) = gamma_m(E-(P)) with gamma_m(E) := min(p - m, E - kappa + m - 1, floor(E/2)).
**Fact 2.1.**  For integers E and m: gamma_m(E) = floor(E/2) iff  ceil(E/2) >= kappa + 1 - m  and  floor(E/2) <= p - m.
Proof.  E - kappa + m - 1 >= floor(E/2) iff E - floor(E/2) = ceil(E/2) >= kappa + 1 - m.  []

## 3. Arc systems (new)

An **arc** is a nonempty set X of cyclically consecutive blocks S_j, ..., S_(j+l), l >= 0, such that every run strictly
inside it (R_(j+1), ..., R_(j+l)) is EMPTY.  V(X) := {y_j, ..., y_(j+l)} and nu(X) := |V(X)|; an arc with an internal run
has nu >= 2 by genuineness.  An **arc system** is a family of 2m >= 2 pairwise disjoint arcs, listed in cyclic order
X_1, Y_1, ..., X_m, Y_m.  The **gap** after an arc is the set of runs and blocks strictly between its last block and the
first block of the next arc.  It contains the run immediately following the arc's last block, so every gap has a run.  Gaps
after X_i are IN-gaps, gaps after Y_i are OUT-gaps.  E_in := sum of d_t over the runs lying in IN-gaps.
**Lemma 3.1.**  For blocks a_i in X_i and b_i in Y_i, let J_i be the run interval R_(a_i + 1), ..., R_(b_i) and
P := J_1 u ... u J_m.  Then P is a proper nonempty pattern with exactly m maximal intervals, D_P = E_in, and
u_P = (1/2) sum_i (y_(a_i) - y_(b_i)).
Proof.  J_i consists of the internal runs of X_i after a_i, all runs of the IN-gap after X_i, and the internal runs of Y_i
up to b_i; it is a nonempty cyclic interval.  The runs of the OUT-gap after Y_i (at least one) lie in no J_j, so the J_i
are separated, m(P) = m and P != [k].  Internal runs of arcs are empty (d = 0), so D_P = E_in.  Telescoping,
sum over R_(a+1), ..., R_b of (y_(t-1) - y_t)/2 = (y_a - y_b)/2.  []
**Lemma ARC (Cauchy-Davenport arc kill).**  In setting (S) let an arc system with 2m arcs have E_in = E, and put
G := G_m(E), G' := G_m(D - E).  If  G + G' >= 0  and  sum over the 2m arcs of (nu - 1) + G + G' >= p - 1,  then w has an
identity 2p-subword.
Proof.  By Lemma 3.1 every choice (a_1, b_1, ..., a_m, b_m) in X_1 x Y_1 x ... x X_m x Y_m gives a pattern with the same m
and D_P = E, hence the same window I := [-G', G] (Lemma W), and u_P runs over the sumset
(1/2)V(X_1) + (-(1/2)V(Y_1)) + ... + (1/2)V(X_m) + (-(1/2)V(Y_m)) of 2m sets of sizes nu (2 is invertible).  By (CD) this
sumset has at least min(p, 1 + sum(nu - 1)) residues; I covers min(p, G + G' + 1) residues.  The hypothesis makes the two
counts add up to at least p + 1, so they meet, and Lemma W applies.  []
Remark.  Constant arcs (nu = 1) only change m and the gap labels.  The previous desk's lift/c-function machinery is not
used; Lemma ARC replaces a choice of one pattern by a Cauchy-Davenport count over a product family of patterns sharing one
window.

## 4. The cell R = p, every B

**Lemma 4.1 (structure).**  In setting (S) with R = p, if w avoids, then every nonempty run is a single letter (rho_1 or
rho_-1), exactly p runs are nonempty and 2 kappa are empty, k = p + 2 kappa, and w has exactly p maximal cyclic reflection
runs M_1, ..., M_p: if N_1, ..., N_p are the nonempty runs in cyclic order, M_i is the reflection run between N_i and
N_(i+1).  Each M_i is an arc; sum_i e_i = 2 kappa, where e_i is the number of (empty) runs inside M_i.
Proof.  k = 2p - R + 2 kappa = p + 2 kappa.  (P0) with e_F = 0 gives e_R <= 2 kappa, so o_R >= k - 2 kappa = p = R.  Each
odd run has at least one letter and the letters number R, so o_R = p, every odd run is a single letter and every even
run is empty.  So e_R = 2 kappa empty runs.  Between two consecutive nonempty runs the blocks are joined by empty runs, so
they form one maximal reflection run, which is an arc.  []
Put  m_0 := max(1, kappa + 1 - ceil((p - 1)/4)),  m_1 := p - floor((p + 1)/4).
**Fact 4.2.**  m_0 <= m_1, and for E in {(p - 1)/2, (p + 1)/2} and m_0 <= m <= m_1:  gamma_m(E) = floor(E/2), and
gamma_m((p - 1)/2) + gamma_m((p + 1)/2) = (p - 1)/2.
Proof.  ceil(((p - 1)/2)/2) = ceil((p - 1)/4) and floor(((p + 1)/2)/2) = floor((p + 1)/4); these are equal (q for
p = 4q + 1, q + 1 for p = 4q + 3), so m_0 <= m_1 reads kappa + 1 <= p, true, and 1 <= m_1.  For E in the two values,
ceil(E/2) >= ceil((p - 1)/4) >= kappa + 1 - m and floor(E/2) <= floor((p + 1)/4) <= p - m; Fact 2.1.  The sum:
q + q = 2q (p = 4q + 1) and q + (q + 1) = 2q + 1 (p = 4q + 3), i.e. (p - 1)/2.  []

**Theorem FP (R = p).**  Let w be in setting (S) with R = p, and suppose w avoids (so Lemma 4.1 applies; write sigma_j = +1
if N_j = rho_1 and -1 if N_j = rho_-1).  Choose pairwise disjoint arcs inside the reflection runs, c_i of them inside M_i,
with sum c_i = 2m and m_0 <= m <= m_1.  Define z in {+1, -1}^p by z_(i+1) = -z_i if c_i is odd and z_(i+1) = z_i if c_i is
even (consistent around the cycle because sum c_i is even; z is defined up to a global sign).  If
|sum_j sigma_j z_j| = 1, then the sum of (nu - 1) over the chosen arcs is at most (p - 3)/2.
Proof.  The chosen arcs, in cyclic order, form an arc system; the run N_j lies in a gap (it is not inside any arc, as arcs
contain only empty runs), and passing from N_i to N_(i+1) crosses exactly the c_i arcs in M_i, so the gap label (IN/OUT)
changes iff c_i is odd.  Hence the labels are z or -z (IN = +).  With the IN = + choice, E+(P) = A_P + B_(P^c) =
#{j : z_j = +1, sigma_j = +1} + #{j : z_j = -1, sigma_j = -1} = (p + sum_j sigma_j z_j)/2 (and the other choice gives
(p - sum_j sigma_j z_j)/2).  So {E+(P), E-(P)} = {(p - 1)/2, (p + 1)/2}, and by Fact 4.2 G + G' = (p - 1)/2 >= 0.
If the sum of (nu - 1) were >= (p - 1)/2, Lemma ARC would give an identity 2p-subword.  []
**Lemma 4.3 (a balanced one-defect labelling exists).**  For n in Z let z^(n) be the alternating labelling with its one
repeat across M_n: z^(n)_(n+1+t) = (-1)^t for t = 0, ..., p - 1 (indices of N mod p), and T(n) := sum_j sigma_j z^(n)_j.
Then |T(n)| = 1 for some n.  If B = 0, |T(n)| = 1 for every n.
Proof.  For s = 1, ..., p - 1: z^(n+1)_(n+1+s) = (-1)^(s-1) = -z^(n)_(n+1+s), and z^(n+1)_(n+1) = (-1)^(p-1) = +1 =
z^(n)_(n+1).  So T(n + 1) = -T(n) + 2 sigma_(n+1).  Put U(n) := (-1)^n T(n): U(n + 1) - U(n) = 2 (-1)^(n+1) sigma_(n+1) in
{2, -2}, and U(n + p) = -U(n) because T is p-periodic and p is odd.  T(n) is odd (a sum of p odd terms), so U moves by
steps of 2 through odd integers from U(n) to -U(n) and takes the value 1 or -1.  If B = 0, all sigma_j = +1 and
T(n) = (p + 1)/2 - (p - 1)/2 = 1.  []
The labelling z^(n) arises from Theorem FP exactly when c_i is odd for i != n and even for i = n.

**Corollary FP-1 (new exclusion; every B).**  Let p >= 5 be prime and w a word of length 4p - 2 over D_(2p) whose rotation
letters lie in one pair {rho_x, rho_-x}, x != 0, number exactly R = p, and all of whose maximal constant reflection blocks
have odd length.  Suppose
   kappa <= (p - 3)/2 + ceil((p - 1)/4)                                                                        (K)
and let nu_i be the number of distinct reflection values in the i-th maximal cyclic reflection run.  If
   sum_i (nu_i - 1) - max_i (nu_i - 1) >= (p - 1)/2,
or if the rotation letters are all equal and sum_i (nu_i - 1) - min_i (nu_i - 1) >= (p - 1)/2, then w has an identity
2p-subword (in increasing index order).
Proof.  Normalise x = 1 and A >= B (N keeps every nu_i).  If w avoided, Lemma 4.1 gives the p runs M_i and nu_i = nu(M_i).
Choose n by Lemma 4.3 (if all rotation letters are equal, B = 0 and n may be chosen with nu_n minimal).  Take c_i = 1 for
i != n (the whole run M_i as one arc) and c_n = 0.  Then 2m = p - 1, m = (p - 1)/2 >= m_0 by (K) (m_0 = kappa + 1 -
ceil((p - 1)/4) or 1), and m <= m_1 = p - floor((p + 1)/4).  The labelling is z^(n), |T(n)| = 1, and the arc sum is
sum_(i != n) (nu_i - 1) >= sum_i (nu_i - 1) - max_i (nu_i - 1) (resp. - min_i for B = 0 with the choice above), which is
>= (p - 1)/2, contradicting Theorem FP.  []
In particular (B = 0): if (K) holds and at least (p - 1)/2 maximal reflection runs are non-constant, w is solvable.
Scope.  Such a w has o_F = k = p + 2 kappa; for kappa >= 1, o_F >= p + 2, so FP-1 lies outside (FEW).  With B < kappa,
kappa >= 2 and pure runs (automatic here) FP-1 excludes part of RES-HI(p) at R = p for B = 0 and for 1 <= B < kappa;
the B >= 1, k >= p + 1 part of RES_<(p) was previously untouched (REFL/notes-B1-cfunc-r1.md, results-r4.md).  For B = 0 at
R = p the accepted CJ''''/REFL-B0 range is kappa <= (p + 10)/6 (R >= 4 kappa - 4 and 6 kappa <= p + 10); FP-1 reaches
kappa up to (p - 3)/2 + ceil((p - 1)/4), under its diversity hypothesis.  FP-1 is a statement about the word itself; it
needs no RED process, so it also applies to an initial avoider w0 of that shape: such a w0 has diversity below the bound.

## 5. Structure for B = 0 and R <= 2 kappa + 1

**Theorem ETA.**  In setting (S) with B = 0 and R <= 2 kappa + 1 put m* := kappa + 1 - floor(R/2) (>= 1).  Index blocks
1..k linearly starting after run R_1, chosen nonempty if R is odd, and put eta_j := y_j/2 + r_1 + ... + r_j in Z_p.  If w
avoids, then for every partition of the blocks 1..k into 2m* nonempty consecutive segments Z_1, ..., Z_(2m*) (in order;
segments may contain nonempty runs),  sum_i |eta(Z_i)| <= p + 2 m* - 2.
Proof.  For a_i in Z_(2i-1), b_i in Z_(2i) let P := union of the runs R_(a_i + 1), ..., R_(b_i).  The runs R_(b_i + 1),
..., R_(a_(i+1)) and R_(b_(m*) + 1), ..., R_k, R_1, ..., R_(a_1) are outside P and each such stretch contains a run, so P
has exactly m* intervals, R_1 notin P, and u_P - D_P = sum_i (eta_(a_i) - eta_(b_i)) (B = 0, D_P = R_P).  Since
ceil(x/2) <= floor(R/2) for 0 <= x <= R - 1 (and for x = R if R is even), Fact 2.1 and p - m* >= floor(R/2) >= x - floor(R/2)
give G_(m*)(x) = x - floor(R/2) there, and G_(m*)(R) = floor(R/2) if R is odd.  If R is even, I(P) = {D_P - R/2}.  If R is
odd, D_P <= R - r_1 <= R - 1 and D_P - (R - 1)/2 lies in I(P) (it is the upper end G(D_P); the lower end is
-G(R - D_P) <= D_P - (R - 1)/2 because R - D_P >= 1).  So avoidance forbids sum_i (eta_(a_i) - eta_(b_i)) = -floor(R/2).  The
set of these sums is the sumset of the eta(Z_(2i-1)) and -eta(Z_(2i)); by (CD) it has at least
min(p, sum_i |eta(Z_i)| - 2m* + 1) residues and misses one, so the bound follows.  []
Reading.  For R in {2 kappa, 2 kappa + 1} (m* = 1) every two-segment split has |eta(Z_1)| + |eta(Z_2)| <= p.  This is a
necessary condition for the IIIb residual (R <= 2 kappa, k >= 2p), not an exclusion.

## 6. Exact delta, what remains, failed directions

Delta of this file (all CANDIDATE, unreviewed): Lemma ARC (Sec. 3); Theorem FP, Lemma 4.3 and Corollary FP-1 (Sec. 4),
giving the first exclusions with B >= 1 and k >= p + 1; Theorem ETA (Sec. 5).
Remaining inside RES-HI(p) (and hence for REFL-HI(p)):
* R = p: avoiders would need sum(nu - 1) <= (p - 3)/2 for every arc choice allowed by Theorem FP (several arcs per run
  allowed).  The extremal surviving shape for FP is many reflection runs alternating two values with e_i = 3
  (sigma_a sigma_b sigma_a sigma_b), where an odd number of arcs captures only one unit per run; FP-1 also needs (K).
* R >= p + 1 (every B) and the B = 0 cells outside CJ''''/REFL-B0: Lemma ARC applies, but its window needs a balanced
  E+(P) and m in the range of Fact 2.1, which the R = p labelling argument supplies only because every nonempty run has
  one letter.  A giant run (most of A in one run) blocks balancing.  Not resolved.
* R <= 2 kappa (IIIb): the m-range with floor-type windows on both sides has length about H = p - 1 - kappa, and the
  E = 0 (single-reflection-run) arc systems need m in [kappa + 1, p - floor(R/2)], which is empty there; ETA gives only
  structure.
Failed or limited directions (written reasoning only): local SPEC moves cannot lower o_F; window-level fusion of two odd
blocks raises H and enlarges windows; Theorem P has M = 3p - 3 - kappa + e_R/2 <= deg Q = 3p - 3 parameters for these words
(boundary e_R = 2 kappa only); generalised Davenport items (H pairs, R rotations, brackets) need k - kappa disjoint
zero-mass brackets, only the (V) range.

## Fix map v2 -> v3 (v2 was never sent)

1. Lemma W stated for setting (S) with arbitrary (not only pure) runs; gamma_m and Fact 2.1 added.
2. v2's garbled m_0 <= m_1 sentence replaced by Fact 4.2 with proof.
3. Theorem FP generalised to every B (labelling z, condition |sum sigma_j z_j| = 1); new Lemma 4.3 (walk argument).
4. Corollary FP-1 strengthened from "(p - 1)/2 non-constant runs" to the nu-sum condition and extended to every B; its
   statement no longer presupposes "the p reflection runs" (Lemma 4.1 supplies them under avoidance).
5. v2's garbled remark at the end of Sec. 4 and its unproved "balancing closes for R <= 2 kappa" claim are removed.
6. ETA's odd-R window membership is proved explicitly.
