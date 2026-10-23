# Addendum to proof-ROT-ZX-v1.md: Lemma S1 (c) - (ZP) implies (S1) also at kappa = (p+1)/2; extended ranges, v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T11:57:01-07:00.  Status [W], UNREVIEWED.

This addendum changes no file.
- proof-ROT-ZX-v1.md (ad2460b2...815b) stays frozen and under review.
- This addendum adds one sequence lemma, Lemma S1 (c), and the corollaries that follow from it combined with Theorem
  ROT-ZX of that file.  Theorem ROT-ZX's hypothesis is (S1) itself, so nothing in its proof changes.
No novelty claim.  Not ROT(p), INV*(p) or ordered Olson in general.

Imports:
- (D) D(Z_(2p)) = 2p: R/olson-rotation-lowodd-parent-verdict-v2.md (0853f4ac...ba29).
- The Erdos-Ginzburg-Ziv theorem for Z_p: among any 2p - 1 elements of Z_p, some p have sum 0.  This is the classical
  theorem already used by the accepted normal form, proof-ROT-few-E-v4.md (ac560eb8...ea8f) L32-33, "EGZ (twice)".
- Davenport for Z_p: among any p elements of Z_p, some nonempty subsequence has sum 0.
  Proof: the p + 1 prefix sums S_0 = 0, S_1, ..., S_p take at most p values, so S_i = S_j for some i < j, and the
  terms i+1, ..., j sum to 0.
- From proof-ROT-ZX-v1.md: Lemma S1 (a), (b), Lemma ZX, Theorem ROT-ZX (terminal form) and its corollary proofs.

Notation: R = institute/runs/six-lane-2026-10-16/review/.  For an odd element y = (1, x) of Z_2 x Z_p = Z_(2p), x(y) is
its second coordinate.  A sequence T of odd elements has sum (|T| mod 2, sum of x).  So:
- a zero-sum of T has even length and x-sum 0;
- a subsequence of odd length with x-sum 0 has sum (1, 0).

## 1. Lemma S1 (c)

**Lemma S1 (c).**  Let p >= 5 be prime, kappa = (p + 1)/2, and let Y be a sequence of odd elements of Z_(2p) with
  (ZP) no zero-sum subsequence of length in [2kappa + 2, 2p] = [p + 3, 2p].
Then (S1) holds: every zero-sum subsequence of Y has length <= 2kappa = p + 1.

Proof.  Suppose not.  Let T be a zero-sum subsequence of Y with |T| >= p + 3, of least possible length, and N := |T|.
(i) N = 2p + 2, and every nonempty proper zero-sum subsequence T' of T has |T'| = p + 1.
- N is even and not in [p + 3, 2p] by (ZP), so N >= 2p + 2.
- T minus one term has length N - 1 >= 2p + 1, so by (D) it contains a nonempty zero-sum.  Hence T has a nonempty
  proper zero-sum subsequence.
- Let T' be any nonempty proper zero-sum subsequence.  Then T' and T - T' are nonempty zero-sums shorter than T.  By
  the minimality of N, each has length <= p + 1.  So N <= 2p + 2, hence N = 2p + 2, and |T'| = N - |T - T'| >= p + 1,
  hence |T'| = p + 1.
(ii) EGZ, applied to the x-values of any 2p - 1 terms of T, gives T_1 <= T with |T_1| = p and x-sum 0.  So
s(T_1) = (1, 0).  Put M := T - T_1.  Then |M| = p + 2 and s(M) = -(1, 0) = (1, 0).
(iii) Let V <= M be nonempty with x-sum 0 and |V| <= p.  Then V is a single term equal to (1, 0).
- If |V| is even, V is a nonempty zero-sum.  It is proper, since |V| <= p < N, so |V| = p + 1 by (i).  But
  |V| <= p, a contradiction.
- So |V| is odd and s(V) = (1, 0).  Then T_1 V is a zero-sum (sum (1, 0) + (1, 0) = 0) of length p + |V|.  It is
  nonempty, and proper because p + |V| <= 2p < N.  By (i), p + |V| = p + 1.  So V is one term with x = 0, i.e. (1, 0).
(iv) By Davenport for Z_p, any p terms of M contain such a V.  So M contains a term u_1 = (1, 0).  M - {u_1} still has
p + 1 >= p terms, so it contains a term u_2 = (1, 0).  Then u_1 u_2 is a nonempty proper zero-sum of length 2, and
2 != p + 1: contrary to (i).  []

**Corollary S1+.**  For every prime p >= 5 and every kappa with 0 <= kappa <= (p + 1)/2, (ZP) implies (S1).  This is
Lemma S1 (a) for kappa <= (p - 1)/2 (4kappa <= 2p - 2) and Lemma S1 (c) for kappa = (p + 1)/2.

## 2. Consequences, by Theorem ROT-ZX of proof-ROT-ZX-v1.md

ROT-ZX's hypothesis is that the rotation sequence of a normal form w^ (terminal k, kappa^) satisfies (S1).  GRX gives
(ZP) at kappa^ (proof-ROT-few-E-v4.md L42-43).  So Corollary S1+ supplies (S1) whenever kappa^ <= (p + 1)/2.

**ROT-ZX+ (terminal form).**  For every prime p >= 5 and every avoider w of length 4p - 2, suppose SOME normal form w^
of w has terminal k = 1, or 3k <= 2p + 1 and kappa^ <= (p + 1)/2.  Then there is c in Z_p \ {0} such that every
rotation letter of w is rho_c or rho_-c.
Proof.  Theorem ROT-ZX of proof-ROT-ZX-v1.md, with (S1) from Corollary S1+.  []

**ROT-ZX+ / INV*-ZX+ (uniform).**  For every prime p >= 5 and every avoider w of length 4p - 2 with o := o_F(w) and
F := F(w), suppose 3o <= 2p + 1, and o <= (p + 3)/2 or F >= o + p - 3.  Then there is c in Z_p \ {0} such that every
rotation letter of w is rho_c or rho_-c, and w is RGR (every maximal cyclic reflection run is constant).
Proof.
- Any normal form has terminal k <= o, so 3k <= 2p + 1.
- If o <= (p + 3)/2, then kappa^ <= k - 1 <= o - 1 <= (p + 1)/2 (Lemma DAV).
- Otherwise kappa^ = kappa(w) - (o - k)/2 <= kappa(w) = p - 1 - (F - o)/2 <= p - 1 - (p - 3)/2 = (p + 1)/2.
- ROT-ZX+ (terminal form) gives the pair.
- RGR: Corollary REFL-few-odd applies to w with (0) p >= 5 prime, (a) |w| = 4p - 2, (b) the pair, and
  (d) o <= (2p + 1)/3 <= p, as in Corollary INV*-ZX of proof-ROT-ZX-v1.md.  []

**OLSON-ZX+ (uniform).**  For every prime p >= 5 and every word w of length 4p - 1 over D_(2p) with o := o_F(w) and
F := F(w), suppose 3o <= 2p + 1, and o <= (p + 3)/2 or F - o >= p - 3.  Then w has an identity 2p-subword in increasing
index order.
Proof.  This is the proof of Corollary OLSON-ZX in proof-ROT-ZX-v1.md, Sec. 5, with INV*-ZX+ in place of INV*-ZX.  The
deletion calculations there give:
- Case 1: no INV* call;
- Case 2: o' = o - 1 and F' - o' = F - o;
- Case 3: o_i <= o and F_i - o_i >= F - o.
In each case either o' <= (p + 3)/2 (when o <= (p + 3)/2) or F' - o' >= p - 3, and 3o' <= 2p + 1.  []

## 3. Ranges and residual

Uniform condition for ROT, INV* and ordered Olson: 3 o_F <= 2p + 1, and either o_F <= (p + 3)/2 or F >= o_F + p - 3.

|p|unconditional o_F bound|with an F condition|
|---:|---|---|
|5|o_F <= 3 (3 o_F <= 2p + 1)|-|
|7|o_F <= 5, every avoider|-|
|11|o_F <= 7, every avoider|-|
|13|o_F <= 8|o_F = 9 with F >= 19|
|17|o_F <= 10|o_F = 11 with F >= 25|
|19|o_F <= 11|o_F in {12, 13} with F >= o_F + 16|

- Previously accepted bound: o_F <= max(4, (p + 1)/2); at p = 5 the accepted o_F <= 4 is larger than the 3 here.
- At p = 7 and p = 11, the terminal residual is empty.  There, ROT-ZX+ covers every avoider whose normal form has
  3k <= 2p + 1, in particular every avoider with 3 o_F <= 2p + 1.

Not covered by this route, inside 3k <= 2p + 1 (terminal): kappa^ >= (p + 3)/2.  This needs k >= (p + 5)/2, hence
p >= 13.
- Terminal pairs (k, kappa^): p = 13: (9, 8).  p = 17: (11, 10).  p = 19: (12, 11), (13, 11), (13, 12).
- There, (S1) can fail only through the pair P, P' of Lemma S1 (b).
- Lemma S1 (c)'s argument uses that all proper zero-sub-sums of the shortest long zero-sum have one length, p + 1.  For
  kappa >= (p + 3)/2 they may take several lengths in [N - 2kappa, 2kappa], and the argument above does not close.
- Nothing is claimed to fail there.

Outside 3k <= 2p + 1 (terminal): not covered by this route; see proof-ROT-ZX-v1.md Sec. 6.
