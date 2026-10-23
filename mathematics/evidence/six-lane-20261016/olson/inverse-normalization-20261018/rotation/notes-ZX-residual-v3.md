# The residual of the ZX route after Lemma S1 (d): reduction lemma and the exact point where the argument stops (notes, v3)

Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T12:47:58-07:00; v3 (erratum of v2, sha256
4cd9175889e3e1d85b77be80e33bad3f4d94ca0bfa49e749e3a9baa92754e19c, never sent) written after 12:48:42.  Status [W], UNREVIEWED notes.
v1 (notes-ZX-residual-v1.md, fdb5ad4a...ee98) is kept unchanged.  This v2 takes into account Lemma S1 (d)
(proof-ROT-ZX-addendum-S1d-v1.md, aefcfc58...c61b, unreviewed).  No new coverage is claimed here.  "Not covered" means
not covered by this route; nothing is claimed to fail.

## 1. What remains (if S1 (d) is accepted)

Inside 3k <= 2p + 1, the terminal criterion now covers kappa^ <= (p + 3)/2 for p >= 11 (and kappa^ <= (p + 1)/2 for
all p).
- Not covered: kappa^ >= (p + 5)/2.  Since kappa^ <= k - 1 <= (2p - 2)/3, this needs p >= 19.
- Terminal pairs (k, kappa^):
  - p = 19: (13, 12).
  - p = 23: (15, 14).
  - p = 29: (18, 17), (19, 17), (19, 18).
  - p = 31: (19, 18), (20, 18), (20, 19), (21, 18), (21, 19), (21, 20).
- Uniform shadow: words with 3o <= 2p + 1, o > (p + 5)/2 and F < o + p - 5.  Even these are covered if some admissible
  normal form meets the terminal criterion.

## 2. Lemma RED2 (the longest proper zero-sub-sum may be assumed to have length exactly 2kappa)

**Lemma RED2.**  Fix p and an integer kappa >= 1.  Assume that for every integer kappa' with 0 <= kappa' < kappa,
(ZP) at kappa' implies (S1) at kappa' for every sequence of odd elements of Z_(2p).  Let Y satisfy (ZP) at kappa and
violate (S1).  Let T be a shortest zero-sum of Y with |T| >= 2kappa + 2.  Then T has a nonempty proper zero-sum
subsequence of length exactly 2kappa.
Proof.
- By (ZP), |T| >= 2p + 2.  By (D), T has nonempty proper zero-sum subsequences.
- Let L be the largest of their lengths.  By the minimality of T, L <= 2kappa; and L is even.  Put kappa' := L/2.
- The zero-sums contained in T are T itself (length >= 2p + 2) and proper ones (length <= L).  So T satisfies (ZP) at
  kappa', and T violates (S1) at kappa', since |T| > 2kappa'.
- By hypothesis kappa' < kappa is impossible.  So L = 2kappa.  []
Consequence.  In an induction on kappa, a minimal failure has T = A B, where:
- A and B are minimal zero-sums;
- |A| = 2kappa = p + delta (delta := 2kappa - p);
- |B| = N - 2kappa, which is the smallest length of a nonempty proper zero-sub-sum of T.
For kappa >= (p + 5)/2, |A| >= p + 5 >= floor(2p/2) + 2.  So the Savchev-Chen/Yuan theorem gives A index 1 in
Z_(2p): A = (y_1 g) ... (y_(2kappa) g) with odd y_i >= 1 summing to 2p, and at least (p + 3delta)/2 of the y_i equal
to 1.

## 3. What the S1 (d) method gives for general delta, and where it stops

Let (p + 3)/2 <= kappa <= (2p - 2)/3 (so 3 <= delta <= (p - 4)/3).  Then the following hold.
- Steps (1)-(5) of S1 (d) generalise directly, with these changes:
  - every nonempty proper zero-sum of T has length in [N - 2kappa, 2kappa] and is minimal;
  - N <= 2p + delta - 1;
  - T has no (1, 0);
  - M = T - T_1 = C V, with C a half-sum of 3 to delta terms and V a minimal zero-sum over Z_p of length
    beta >= N - 2kappa >= p + 2 - delta.
- Step (6) (Savchev-Chen/Yuan in Z_p) gives V index 1 with respect to some h: at least 2beta - p >= p + 4 - 2delta
  copies of h^ = (1, h), and the other terms of V have h-coefficients in [2, delta - 1], at least one of them even.
- Step (7) of S1 (d) used two exchanges, h^^(p-c) z and h^^(p-2-c) y z.  They need up to p - 5 copies of h^.
- The available bound is t >= 2beta - p >= p + 4 - 2delta.  This is enough for delta = 3 but smaller than p - 5 once
  delta >= 5.  Coefficients c below about 2delta then escape the classification.
- Several "small" terms (coefficient <= about 2delta) and "near (1, 0)" terms can then coexist.  The case analysis
  needed to exclude them (pairs and triples of such terms, and the interaction between the index-1 generators g of A
  and h of V) was not completed.
Exact unresolved sub-obligation: whether (ZP) at kappa implies (S1) at kappa, for (p + 5)/2 <= kappa <= (2p - 2)/3.

## 4. Finite outputs (no conclusion rests on them)

t-search-v1 run1 (out/run1.jsonl e79de631...2780) was ruled UNKNOWN by the parent after an admission audit
(t-search-v1/ADMISSION-AUDIT-RECEIPT-v1.md).  Its recorded outputs list no (R1)-structure T at (19, 12) or (23, 14),
the two delta = 5 items, nor at the delta = 3 items.  The p = 7 positive control was present.

## Erratum fix map (v2 -> v3)

- The abbreviated hash of proof-ROT-ZX-addendum-S1d-v1.md was mistyped as aefcfc58...b61b; the file's sha256 is
  aefcfc58edfd878b8417d96f278406aedac99bd453c0553fb6979f838d3ac61b, so it is aefcfc58...c61b.  Found by the
  mechanical hash check right after v2 was hashed and logged (README 12:48:42); v2 was never sent.
- Header: version and erratum provenance.  No other change.

Unified body diff:

```
--- notes-ZX-residual-v2.md
+++ notes-ZX-residual-v3.md
@@ -1,8 +1,9 @@
-# The residual of the ZX route after Lemma S1 (d): reduction lemma and the exact point where the argument stops (notes, v2)
+# The residual of the ZX route after Lemma S1 (d): reduction lemma and the exact point where the argument stops (notes, v3)
 
-Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T12:47:58-07:00.  Status [W], UNREVIEWED notes.
+Owner OlsonRotationRigidity.  Written after host clock 2026-10-18T12:47:58-07:00; v3 (erratum of v2, sha256
+4cd9175889e3e1d85b77be80e33bad3f4d94ca0bfa49e749e3a9baa92754e19c, never sent) written after 12:48:42.  Status [W], UNREVIEWED notes.
 v1 (notes-ZX-residual-v1.md, fdb5ad4a...ee98) is kept unchanged.  This v2 takes into account Lemma S1 (d)
-(proof-ROT-ZX-addendum-S1d-v1.md, aefcfc58...b61b, unreviewed).  No new coverage is claimed here.  "Not covered" means
+(proof-ROT-ZX-addendum-S1d-v1.md, aefcfc58...c61b, unreviewed).  No new coverage is claimed here.  "Not covered" means
 not covered by this route; nothing is claimed to fail.
 
 ## 1. What remains (if S1 (d) is accepted)
```
