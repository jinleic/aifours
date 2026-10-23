# Addendum to proof-ROT-ZX-v1.md: Lemma S1 (d) - (ZP) implies (S1) at kappa = (p+3)/2 for p >= 11; extended ranges, v1

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T12:41:50-07:00.  Status [W], UNREVIEWED.

This addendum changes no file.  It adds one sequence lemma, Lemma S1 (d), and its consequences through the
parent-accepted terminal criterion of R/olson-zx-s1c-parent-verdict-v1.md (2f8d376b...e6af), item 3.  It is read
through that verdict's overlay: integer kappa, existential normal form, k = 1 by K1, explicit SHgen-E discharge.
- The proof below is self-contained given its imports.
- It does not rely on the unreviewed notes-ZX-residual-v1.md, although Steps (1)-(5) re-prove the kappa = (p+3)/2 case
  of its (R1)-(R2).
No novelty claim.  Not ROT(p), INV*(p) or ordered Olson in general.

Imports:
- (D) D(Z_(2p)) = 2p: R/olson-rotation-lowodd-parent-verdict-v2.md (0853f4ac...ba29); classical D(C_n) = n.
- The Erdos-Ginzburg-Ziv theorem for Z_p (classical; already used by the accepted normal form, proof-ROT-few-E-v4.md
  (ac560eb8...ea8f) L32-33): among any 2p - 1 elements of Z_p, some p have sum 0.
- Davenport for Z_p, proved inline in proof-ROT-ZX-addendum-S1c-v1.md (7ce7102c...b0b6) Sec. 0: among any p elements
  of Z_p, some nonempty subsequence has sum 0.
- EXPLICIT CLASSICAL IMPORT (the Savchev-Chen / Yuan index theorem).  Every minimal zero-sum sequence S over the cyclic
  group C_n, n >= 3, of length >= floor(n/2) + 2 has index 1: there are an element a and positive integers x_1, ...,
  x_l with S = (x_1 a) ... (x_l a) and x_1 + ... + x_l = ord(a).
  - Sources:
    - V. Savchev and F. Chen, "Long zero-free sequences in finite cyclic groups", Discrete Math. 307 (2007)
      2671-2679, DOI 10.1016/j.disc.2007.01.012;
    - P. Yuan, "On the index of minimal zero-sum sequences over finite cyclic groups", J. Combin. Theory Ser. A 114
      (2007) 1545-1551;
    - stated in this form as Theorem 1, p. 4, of F. Chen's CANT 2016 slides
      (https://static.uni-graz.at/fileadmin/veranstaltungen/additive2016/Talks/chen_f_slides.pdf), which cite both.
    - Located and checked by the parent (IRC 12:2x-12:3x); the original 2007 body was not read.
  - Used once, in Step (6): n = p prime, a nonzero element of order p, and l = p - 1.  Here p - 1 >= floor(p/2) + 2
    holds for every p >= 5.
  - Not a self-contained proof; this is an import at the stated scope.

Notation.  For an odd element y = (1, x) of Z_2 x Z_p = Z_(2p), x(y) := x.  For a subsequence U (distinct occurrences),
x(U) is the sum of the x(y), and the group sum of U is (|U| mod 2, x(U)).  So a U with x(U) = 0 is:
- a zero-sum if |U| is even;
- a "half-sum", with group sum (1, 0), if |U| is odd.
Two disjoint half-sums together form a zero-sum.

## 1. Lemma S1 (d)

**Lemma S1 (d).**  Let p >= 11 be prime and kappa = (p + 3)/2, so that 2kappa = p + 3.  Let Y be a sequence of odd
elements of Z_(2p) with
  (ZP) no zero-sum subsequence of length in [2kappa + 2, 2p] = [p + 5, 2p].
Then (S1) holds: every zero-sum subsequence of Y has length <= p + 3.

Proof.  Suppose not.  Let T be a zero-sum subsequence of Y with |T| >= p + 5 and |T| least, and N := |T|.

(1) Lengths.
- N is even and not in [p + 5, 2p], so N >= 2p + 2.
- By (D), T minus one term (length >= 2p + 1) contains a nonempty zero-sum.  So T has a nonempty proper zero-sum
  subsequence.
- Let T' be any nonempty proper zero-sum subsequence.  T' and T - T' are nonempty zero-sums shorter than T, so by
  minimality neither has length >= p + 5.  Being even, both have length <= p + 3.
- Hence N <= 2p + 6, and every nonempty proper zero-sum subsequence of T has length in [N - p - 3, p + 3].

(2) Half-sums.  EGZ applied to any 2p - 1 terms of T gives a half-sum T_1 <= T with |T_1| = p.  Put M := T - T_1.
Then |M| = N - p >= p + 2, x(M) = 0, and |M| is odd.
- Claim A.  Let V <= M with 1 <= |V| <= p and x(V) = 0.  Then either |V| is even and |V| >= N - p - 3, or |V| is odd
  and |V| <= 3.
  - If |V| is even, V is a nonempty proper zero-sum (|V| <= p < N), and (1) applies.
  - If |V| is odd, T_1 V is a zero-sum of length p + |V| <= 2p < N, nonempty and proper.  So p + |V| <= p + 3.
- Claim B.  M contains no two disjoint subsequences V_1, V_2 of odd length <= 3 with x(V_i) = 0.
  - Otherwise V_1 V_2 is a nonempty proper zero-sum of length <= 6.
  - But by (1) its length would be >= N - p - 3 >= p - 1 >= 10.

(3) N = 2p + 2.
- Suppose N >= 2p + 4.  Then an even V as in Claim A would need |V| >= p + 1 > p, so every V there is odd with
  |V| <= 3.
- Davenport (on p terms of M; |M| >= p + 4) gives such a V_1.
- M - V_1 has >= p + 1 terms, so Davenport gives a second one, V_2, disjoint from V_1, contrary to Claim B.
- Hence N = 2p + 2 and |M| = p + 2.  Every nonempty proper zero-sum subsequence of T has length p - 1, p + 1 or p + 3.

(4) T has no term equal to (1, 0).  Suppose u = (1, 0) is a term.
- Take T_1 by EGZ among the 2p + 1 other terms.  Then u lies in M.  M - {u} has p + 1 terms, so Davenport gives
  V <= M - {u} with x(V) = 0 and 1 <= |V| <= p.
- If |V| is odd, then {u} and V are disjoint, both of odd length <= 3 with x-sum 0 (Claim A), contrary to Claim B.
- If |V| is even, then |V| = p - 1 (Claim A).  The two remaining terms of M - {u} - V have x-sum 0, so they form a
  zero-sum of length 2 < p - 1, contrary to (3).

(5) M = C V, where |C| = 3, x(C) = 0, and V is a zero-sum of length p - 1 with no nonempty proper subsequence of x-sum 0.
- Davenport gives V_0 <= M with x(V_0) = 0 and 1 <= |V_0| <= p.
  - If |V_0| is odd, then |V_0| <= 3 (Claim A), and |V_0| != 1 by (4), since a single term of x-sum 0 is (1, 0).  So
    |V_0| = 3; put C := V_0.
  - If |V_0| is even, then |V_0| = p - 1 (Claim A); put C := M - V_0.
- Put V := M - C.  Then |V| = p - 1 is even and x(V) = 0, so V is a zero-sum.
- Suppose V had a nonempty proper subsequence V'' with x(V'') = 0.
  - If |V''| is even, V'' is a zero-sum of length < p - 1, contrary to (3).
  - If |V''| is odd, V'' and V - V'' are disjoint subsequences of M of odd length <= p with x-sum 0.  By Claim A both
    have length <= 3, so |V| <= 6 < p - 1: a contradiction.
- So the x-values of V form a minimal zero-sum sequence over Z_p of length p - 1.

(6) Index 1.  By the Savchev-Chen / Yuan theorem (C_p, length p - 1 >= floor(p/2) + 2), there are h in Z_p \ {0} and
positive integers x_1, ..., x_(p-1) such that the x-values of V are x_1 h, ..., x_(p-1) h and x_1 + ... + x_(p-1) = p.
- p - 1 positive integers with sum p consist of one 2 and p - 2 ones.
- Put h^ := (1, h), and let y be the term of V with x-value 2h.  Then V = h^^(p-2) y.
- So t, the multiplicity of h^ in T, satisfies t >= p - 2.

(7) Every term of T is h^ or has x-value 2h.  Let z be a term of T other than h^, with x-value c h, c in [0, p - 1].
By (4), c != 0, and c != 1 since z != h^.
- c even.  Put beta := p - c.  It is odd with 1 <= beta <= p - 2 <= t.
  - The subsequence h^^beta z has x-sum (beta + c) h = 0 and even length beta + 1 <= p - 1 < N, so it is a nonempty
    proper zero-sum.
  - By (3), beta + 1 = p - 1, so c = 2.
- c odd, c >= 3.  Put j := p - 2 - c.  Then 0 <= j <= p - 5 <= t, and z != y (different x-values).
  - The subsequence h^^j y z has x-sum (j + 2 + c) h = 0.
  - Its length is j + 2 = p - c, which is even (p and c are odd) and <= p - 3.
  - So it is a nonempty proper zero-sum shorter than p - 1, contrary to (3).
- Hence T consists of t copies of h^ and u copies of y = (1, 2h), with t + u = 2p + 2.

(8) Contradiction.
- x(T) = (t + 2u) h = 0, so t + 2u = 0 (mod p).  With t = 2p + 2 - u this gives u + 2 = 0 (mod p), so u is p - 2 or
  2p - 2.
- u = 2p - 2 would give t = 4 < p - 2.  So u = p - 2 and t = p + 4.
- Then h^^(p-6) y^3 (p - 6 <= t, 3 <= u) has x-sum (p - 6 + 6) h = 0 and even length p - 3 < p - 1.  It is a nonempty
  proper zero-sum, contrary to (3).  []

Where p >= 11 is used:
- Claim B needs 6 < p - 1.
- Step (5) needs 6 < p - 1.
- Step (8) needs p - 6 >= 0.
At p = 7 and kappa = 5 the lemma is false: the parent's control g^13 (5g)^3 satisfies (ZP) and violates (S1).  There
Claim B fails, since 6 >= p - 1.

**Corollary S1++.**  For every prime p >= 11 and every integer kappa with 0 <= kappa <= (p + 3)/2, (ZP) implies (S1).
This combines S1+ (kappa <= (p + 1)/2, parent-accepted) with Lemma S1 (d).

## 2. Consequences, through the accepted terminal criterion

The accepted terminal criterion (verdict item 3): rotations lie in one nonzero pair if SOME normal form produced by the
accepted process has k = 1, or has 3k <= 2p + 1 and (S1) for its rotation sequence at kappa^.  GRX gives (ZP) at kappa^.
So Corollary S1++ yields the following.

**ROT-ZX++ (terminal form).**  Let p >= 11 be prime and w an avoider of length 4p - 2.  Suppose some normal form has
k = 1, or has 3k <= 2p + 1 and kappa^ <= (p + 3)/2.  Then all rotations of w lie in one {rho_c, rho_-c}, c != 0.  If
moreover o_F(w) <= p, then w satisfies INV*.

**ROT/INV*-ZX++ (uniform).**  Let p >= 11 be prime and w an avoider of length 4p - 2 with o := o_F(w) and F := F(w).
Suppose 3o <= 2p + 1, and o <= (p + 5)/2 or F >= o + p - 5.  Then w satisfies INV*.
Proof.
- Any normal form has k <= o, so 3k <= 2p + 1.
- For k >= 2 (k = 1 is K1):
  - if o <= (p + 5)/2, then kappa^ <= k - 1 <= o - 1 <= (p + 3)/2 (DAV);
  - otherwise kappa^ <= kappa(w) = p - 1 - (F - o)/2 <= (p + 3)/2.
- ROT-ZX++ applies, and o <= (2p + 1)/3 <= p gives INV* via Corollary REFL-few-odd, as in the accepted uniform
  corollary.  []

**OLSON-ZX++ (uniform).**  Let p >= 11 be prime and w a word of length 4p - 1 over D_(2p) with o := o_F(w) and
F := F(w).  Suppose 3o <= 2p + 1, and o <= (p + 5)/2 or F - o >= p - 5.  Then w has an identity 2p-subword in increasing
index order.
Proof.  As for the accepted OLSON-ZX+, with INV*-ZX++ in place of INV*-ZX+.  The accepted deletion ledger (verdict
overlay 8) gives:
- Case 1: o <= 2p - 3;
- Case 2: (o - 1, F - 1);
- Case 3: (o or o - 2, F).
Neither lowers F - o, and both keep o' <= (p + 5)/2 when o <= (p + 5)/2.  []

## 3. Ranges and what remains

|p|unconditional o_F bound (with 3 o_F <= 2p + 1)|with an F condition|
|---:|---|---|
|11|o_F <= 7 (unchanged)|-|
|13|o_F <= 9, i.e. every o_F with 3 o_F <= 2p + 1|-|
|17|o_F <= 11, every o_F with 3 o_F <= 2p + 1|-|
|19|o_F <= 12|o_F = 13 with F >= 27|
|23|o_F <= 14|o_F = 15 with F >= 33|

The F column is the condition F >= o_F + p - 5.

- For p = 5 and p = 7 nothing changes.  The accepted o_F <= max(4, (p + 3)/2) stands, and Lemma S1 (d) needs p >= 11.
- These are sufficient classes.  No claim is made that avoiders with these parameters exist.

Not covered by this route, inside 3k <= 2p + 1 (terminal): kappa^ >= (p + 5)/2, which needs p >= 19.
- Terminal pairs (k, kappa^): p = 19: (13, 12).  p = 23: (15, 14).  p = 29: (18, 17), (19, 17), (19, 18).
- Nothing is claimed to fail there.

Aid only, not a premise.  t-search-v1 run1 (out/run1.jsonl e79de631...2780) is ruled UNKNOWN by the parent after an
admission audit (t-search-v1/ADMISSION-AUDIT-RECEIPT-v1.md).  Its recorded outputs show no (R1)-structure T at
(13,8), (17,10), (19,11), (23,13), as this lemma requires, nor at (19,12), (23,14).  The positive control at p = 7 was
found.  No conclusion rests on that run.
