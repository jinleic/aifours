# The cyclic-15 spectral obstruction extends beyond rational populations

**WRITTEN AUTHOR CANDIDATE, UNREVIEWED.** Native `/bin/date`: Thu Oct 29 02:12:31 PDT 2026. This is an additive extension of `frontier-20261029-cyclic15-rational-spectral-no-go-v1.md`, SHA-256 `bb0d0cf314b2c7c94afddb99a3bfdfe44d7f16a28251f197e464215cf9b49ada`; all its cyclic-equivariance, distinct-ray and incidence hypotheses remain in force.

Let F be **any real field** such that `[F(zeta_15):F]=8`. Then the same no-go holds if all squared U-eigenbasis coordinates of v2 and v7 lie in F. Thus a putative 45-ray cyclic-equivariant realization must satisfy

`[Q(p_2j,p_7j for j=1..6)(zeta_15) : Q(p_2j,p_7j for j=1..6)] < 8`

for every U eigenbasis, where `p_dj=|<e_j,v_d>|²`. This is stronger than saying merely that some population is irrational.

**Reason.** The degree condition makes F and Q(zeta_15) linearly disjoint. Every cyclotomic automorphism used in the parent proof therefore extends while fixing F. The 3×5 CRT basis and its row-plus-column description of a vanishing coefficient grid remain valid over F. The coefficients are real and nonnegative, so the same elementary shift makes all row/column summands nonnegative; the support and two-coset arguments are unchanged. The subsequent complex 3×3 Hadamard and cross-row contradiction does not depend on the coefficient field.

In particular F may be `Q(sqrt(d))` for any positive squarefree integer `d != 5`; for example, simultaneous populations in `Q(sqrt(2))` or `Q(sqrt(3))` are impossible. Indeed the three quadratic subfields of Q(zeta_15) are `Q(sqrt(5))`, `Q(sqrt(-3))`, and `Q(sqrt(-15))`; the two quadratic Galois fields then have trivial intersection, so their compositum has degree 8 over F. These standard quadratic-subfield and cyclotomic-degree facts are explicit imports. The example `F=Q(sqrt(2),sqrt(3))` also has trivial intersection with Q(zeta_15): none of its quadratic subfields Q(sqrt(2)), Q(sqrt(3)), Q(sqrt(6)) occurs in the cyclotomic field, and both extensions are Galois.

This remains **conditional on cyclic unitary symmetry** and does not exclude spectral populations in fields that are not linearly disjoint, or symmetry-breaking solutions. Independent review of the parent proof and the field-disjointness caller is required; no formal or novelty claim is made.
