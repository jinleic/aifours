# Theorem ROT-KP: rotation rigidity for terminal k = p and kappa^ in {0, 1} (word-level exclusion of the k = p sequence obstructions), v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T14:28:29-07:00.  Status [W], UNREVIEWED.
No novelty claim.  Not ROT(p), INV*(p) or ordered Olson in general.  No computation was run for this file.

## 0. Dependencies (exact; all parent-accepted at their accepted scopes)

- GRX: notes-GRX-v1.md (afc6c31a...1a30), accepted (R/olson-rotation-lowodd-parent-verdict-v2.md, 0853f4ac...ba29).
  It holds for every cyclic constant-block representation, empty runs allowed.
- Normal form w^, kappa^ >= 0 and integral for k >= 2, (ZP), Lemma DAV, Proposition K1 (one block):
  proof-ROT-few-E-v4.md Sec. 0, L28-43 (ac560eb8...ea8f), as used by the accepted terminal criterion
  (R/olson-zx-s1c-parent-verdict-v1.md, 2f8d376b...e6af; overlay retained).
- Lemma SC0: proof-ROT-ZXSC-v1.md Sec. 0 (15958303...bb1a), accepted (R/olson-zxsc-parent-verdict-v1.md,
  cf039654...b134); it rests on the explicit Savchev-Chen / Yuan index-one import.
- S1+ (integer-domain, kappa^ = 1), accepted (R/olson-zx-s1c-parent-verdict-v1.md).
- KETA, PAIR1, ROT-K01, INV*-K01, OLSON-K01: proof-ROT-K01-v1.md (b3ecdb4e...b378), accepted with overlay
  (R/olson-k01-parent-verdict-v1.md, e11144f6...0df4; full sha256
  e11144f613c7a396b2a8e2284e240154367b09b9720f015b87132a5d30fe0df4).  Its sequence lemma is called PAIR1; the
  one-block Proposition K1 is distinct.
- Theorem SHgen (proof-SHgen-v3.md, fcbd5a97...eb5e) with exactly its accepted hypotheses (H) 2H >= E and
  (K) k <= 2p - eta - a_max - 1; Lemma SHgen-E (proof-ROT-few-E-v4.md Sec. 1) with the caller discharge of the K01
  verdict and R/olson-zs-v2-parent-verdict-v1.md (2ba1fedc...0734) overlay V3.
- Restricted REFL: Corollary REFL-few-odd (R/olson-refl-fewodd-parent-verdict-v1.md, 16436c07...f1ca), o_F <= p.
- RGR-LONG and the ordered deletion ledger, as in the K01 verdict.
Part A uses only GRX and the normal form (no SC0, no SHgen, no REFL).  Part B adds SC0, S1+, KETA, SHgen/SHgen-E.

Notation.  w^ = R_1 S_1 R_2 S_2 ... R_k S_k (cyclic), S_j = sigma_(y_j)^(l_j) with every l_j odd; block S_j lies
between runs R_j and R_(j+1); indices mod k.  H = (F - k)/2, kappa^ = p - 1 - H, R = 2p + 2kappa^ - k.
Rotation rho_x has value x in Z_p and Y(x) = (1, x) in C_2 x C_p.  For a pattern z, Phi = number of cyclic sign
changes; with all blocks odd, C_max = F - #{j : f_j = 0} = 2H + Phi.  GRX: w^ has an identity 2p-subword iff for some
z there are an even C with Phi <= C <= 2H + Phi, m := 2p - C with 0 <= m <= R, and a size-m sub-multiset of X^z whose
value sum is T(z).

**Arc patterns.**  For blocks j != j' let A = (j, j'] be the runs j+1, ..., j' (cyclically): nonempty and proper.
z_A := -1 on A and +1 elsewhere has Phi = 2 (sign changes at blocks j and j'), and T(z_A) = sum over runs outside A
of theta_i = -(y_j - y_(j')) = y_(j') - y_j.  X^(z_A) is X with the values in runs of A negated.  So:
(ARC) if some even m with max(0, 2kappa^) <= m <= min(R, 2p - 2) and some m rotation letters have signed value sum
y_(j') - y_j (sign + outside A, - inside A), then w^ has an identity 2p-subword (C = 2p - m lies in [2, 2H + 2]).

## Part A: kappa^ = 0, k = p

Here H = p - 1, F = 3p - 2, R = p, and (ZP) says no 2 <= m <= 2p even sub-multiset of rotations has value sum 0.

**Lemma DIST0.**  If kappa^ = 0, the k block values are pairwise distinct.
Proof.  If y_j = y_(j') with j != j', apply (ARC) with m = 0 (allowed as 2kappa^ = 0; C = 2p <= 2H + 2 = 2p).  []
So for k = p, y : {blocks} -> Z_p is a bijection.  For t in Z_p - {0} let pi_t := y^(-1) o (+t) o y, a permutation
of the p blocks conjugate to translation by t, hence a single p-cycle.

**Lemma WIND.**  Let t != 0 and A_j := (j, pi_t(j)] for each block j.  There is an integer w_t with 1 <= w_t <= p - 1
such that every run lies in exactly w_t of the p arcs A_j.
Proof.  Following the cycle j -> pi_t(j) -> ... -> j, the arcs A_j concatenate to a closed forward walk around the
p runs, so every run is covered the same number w_t of times, and the total length is w_t p.  Each arc has length in
[1, p - 1], so p <= w_t p <= p(p - 1).  []

**Lemma ONE0.**  If kappa^ = 0 and k = p and w^ avoids, then all rotation letters of w^ have one value c, and c != 0.
Proof.  Let x, x' be the values of two distinct rotation letters.
- Same run alpha.  t := x + x' != 0 by (ZP) (m = 2).  For each j, A_j has signed target y_(pi_t(j)) - y_j = t.  If alpha
  is outside A_j, both letters carry sign + and give the sum t with m = 2; (ARC) applies (2 <= R = p).  So alpha lies
  in all p arcs A_j, contradicting Lemma WIND (w_t <= p - 1).
- Different runs alpha != beta, x != x'.  t := x - x' != 0.  If for some j run beta is in A_j and run alpha is not,
  then x (sign +) and x' (sign -) give the sum x - x' = t with m = 2: (ARC).  So {j : beta in A_j} is contained in
  {j : alpha in A_j}; both have exactly w_t elements (Lemma WIND), so they are equal: no A_j contains exactly one of
  alpha, beta.  Put P := blocks alpha, ..., beta - 1 and Q := blocks beta, ..., alpha - 1 (both nonempty).  Walking
  forward from block j to block pi_t(j), crossing run alpha moves from Q to P and crossing run beta from P to Q, so
  A_j contains exactly one of alpha, beta iff j and pi_t(j) lie in different parts.  Hence pi_t(P) is contained in P,
  impossible for a p-cycle and a nonempty proper subset P.
So any two rotation letters have equal values.  R = p >= 2, and rho_0 rho_0 would violate (ZP), so c != 0.  []

## Part B: kappa^ = 1, k = p

Here H = p - 2, R = p + 2.  (ZP) and S1+ give (S1): every zero-sum of the sequence Y = (Y(x)) has length <= 2.

**Lemma ZP-D (Z_p, length p - 1).**  A sequence of p - 1 elements of Z_p with no nonempty zero-sum sub-multiset is
c^(p-1) for some c != 0.
Proof.  Elements are nonzero.  Suppose two terms a != b; list them first.  Let A_i be the set of sums of
sub-multisets of the first i terms (0 included).  A_2 = {0, a, b, a + b} has 4 elements (a + b != 0 and no term is 0).
For i >= 3, A_i = A_(i-1) u (A_(i-1) + s_i) is strictly larger than A_(i-1): otherwise A_(i-1) + s_i is contained in
A_(i-1), so A_(i-1) = Z_p and -s_i in A_(i-1) is a sum of earlier terms (nonempty, as s_i != 0), giving a zero-sum.
So |A_(p-1)| >= 4 + (p - 3) = p + 1 > p.  []

**Lemma PAIR1-P (PAIR1 at k = p).**  Let p >= 5 be prime and Y a sequence of p + 2 odd elements of C_(2p) all of whose
zero-sums have length <= 2.  Then either
- (i) there is a generator g = Y(c), c != 0, such that every coefficient b_g(y) is odd with -1 <= b_g(y) <= p - 2
  (at most one -1), Y(0) does not occur, and E := sum (|b| - 1) <= p - 3; or
- (ii) Y = Y(0)^3 Y(c)^(p-1) with c != 0 (the involution triple).
Proof.  The nonempty zero-sums are inverse pairs of occurrences, and any two pairs share an occurrence.
- No pair: Y is zero-sum-free of length p + 2 >= p + 1.  SC0 gives positive odd coefficients with total
  W <= 2p - 1, so sum (a_i - 1) <= p - 3 and every a_i <= p - 2.  Case (i), no -1.
- A pair {u, v} such that Y_0 := Y - {u} is zero-sum-free (after renaming u, v).  L := |Y_0| = p + 1.  SC0 gives
  W <= 2p - 1, so W - L <= p - 2; W - L is a sum of even numbers, so W - L <= p - 3.
  - u != Y(0): otherwise v = Y(0) lies in Y_0 with coefficient p and W >= p + (L - 1) = 2p.
  - Let v = a g.  If a >= 3, let h >= 1 be the number of terms of Y_0 with coefficient >= 3 and m_1 := L - h the number
    of copies of g.  Then W - L >= (a - 1) + 2(h - 1), so a <= p - 2h, and m_1 - a >= (p + 1 - h) - (p - 2h) =
    h + 1 >= 2.  So g^a u is a zero-sum of length a + 1 >= 4: contradiction.  Hence v = g and u = -g.
  - Coefficients of Y_0 are <= 1 + (p - 3) = p - 2; u has coefficient -1; E = W - L <= p - 3.  Case (i).
- A pair {u, v} for which neither Y - {u} nor Y - {v} is zero-sum-free.  As in the PAIR1 proof (K01 verdict,
  derivation of PAIR1), u = v = x as values, x being a third occurrence, and this value is the order-two element
  Y(0); a fourth occurrence would give two disjoint pairs.  Y'' := Y - {u, v} has no pair (every pair meets {u, v}),
  so it is zero-sum-free; |Y''| = p and Y'' contains x = Y(0) once.  The p - 1 values of Y'' - {x} have no nonempty
  zero-sum in Z_p: an even-size one is a zero-sum of Y''; an odd-size one together with x is.  Lemma ZP-D gives
  Y'' - {x} = Y(c)^(p-1), c != 0.  So Y = Y(0)^3 Y(c)^(p-1).  Case (ii).  []

**Lemma TRIPLE-ARC.**  Let kappa^ = 1 and k = p (forced: R = p + 2), and let the rotation multiset of w^ be
rho_0^3 rho_c^(p-1), c != 0.  Then w^ has an identity 2p-subword.
Proof.  Take any blocks j != j' and A = (j, j'], tau := y_(j') - y_j.  Let U- be the number of rho_c letters in runs of
A and U+ := p - 1 - U-.  The integers in [-U-, U+] are p consecutive integers, so one of them, D, has D c = tau (mod p).
Take D letters rho_c outside A if D >= 0, or -D letters rho_c inside A if D < 0: signed sum D c = tau.  Add t letters
rho_0 (value 0 under either sign): t = 2 if D = 0, t = 1 if |D| is odd, t = 0 otherwise.  Then m = |D| + t is even
with 2 <= m <= p - 1 (|D| <= p - 1, p odd), so max(0, 2kappa^) = 2 <= m <= min(R, 2p - 2).  (ARC) applies.  []

## Theorem ROT-KP

**Theorem ROT-KP.**  Let p >= 5 be prime and w an avoider of length 4p - 2 over D_(2p).  If some admissible normal form
w^ of w has terminal k = p and kappa^ in {0, 1}, then all rotation letters of w lie in one set {rho_c, rho_-c},
c != 0 (for kappa^ = 0 they are all equal).
Proof.  w^ avoids and has the rotation multiset of w.
- kappa^ = 0: Lemma ONE0.
- kappa^ = 1: Lemma PAIR1-P applies to Y.  Case (ii) is impossible by Lemma TRIPLE-ARC.  In case (i), g = Y(c),
  c != 0, and the coefficients are exactly the SHgen weights relative to c (|b| <= p - 2, no rho_0).  If E = 0 every
  rotation is rho_c or rho_-c.  Otherwise eta >= 1 and:
  - (H): 2H = 2p - 4 >= p - 3 >= E;
  - (K): KETA gives eta + a_max <= E + 2 <= p - 1, i.e. k = p <= 2p - eta - a_max - 1.
  Theorem SHgen (all runs nonempty) or Lemma SHgen-E (some run empty) gives an identity 2p-subword, a contradiction.
  SHgen-E caller: every expansion keeps k = p, the block values and the genuine empty runs; each base expansion has
  length 4p - 2, rotations in one nonzero pair and o_F = k = p <= p, inside restricted REFL.  []

**Corollary INV*-KP / OLSON-KP (uniform).**  Let p >= 5 be prime.
- (a) Every avoider of length 4p - 2 with o_F <= p and F - o_F >= 2p - 4 satisfies INV*.
- (b) Every word of length 4p - 1 over D_(2p) with o_F <= p and F - o_F >= 2p - 4 has an identity 2p-subword in
  increasing index order.
Proof.  (a) Every admissible normal form has k <= o_F <= p, k = o_F (mod 2), and kappa^ = kappa(w) - (o_F - k)/2 <= 1;
for k >= 2, kappa^ is an integer >= 0.  k = 1: Proposition K1.  2 <= k <= p - 1: Theorem ROT-K01 (accepted).
k = p: Theorem ROT-KP.  Restricted REFL applies to w since o_F <= p.  (b) The accepted deletion ledger, as in the K01
verdict: Case 1 uses o_F <= p <= 2p - 3 and framed equal pairs; Case 2 gives (o - 1, F - 1); Case 3 gives
(o or o - 2, F).  Both inequalities are preserved, so each shorter avoider meets (a); RGR-LONG completes.  []

## Scope

- New relative to the accepted results: terminal k = p with kappa^ in {0, 1}; uniformly, o_F = p with
  F >= 3p - 4 (the K01 range was o_F <= p - 1).
- The k = p sequence obstructions named in the K01 verdict - the involution triple Y(0)^3 Y(c)^(p-1) at kappa^ = 1 and
  Y(0) Y(c)^(p-1) at kappa^ = 0 - are excluded at word level here (Lemma TRIPLE-ARC; Lemma ONE0, which needs neither
  S(p) nor SC0).  They remain valid SEQUENCE examples; nothing here refutes or uses them otherwise.
- Not covered by this route: kappa^ >= 2 at k = p; kappa^ >= 2 beyond the accepted ranges (3k <= 2p + 1 with S1 (g),
  ZX-SC); o_F > p (REFL).  Sufficient conditions only; no existence of avoiders is asserted.
