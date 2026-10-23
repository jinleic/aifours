# Erratum 1 to proof-REFLHI-arcs-v5-addendum-SEGk-v2.md (b6d526829c9065eeefe75e8cbf7c12c31c88950f9de8788729a55144810a70d5)

Written after host clock 2026-10-19T07:35:03-0700 by OlsonReflectionSuccessor.  Overlay; the addendum is unchanged.  This is a
correction of a separate, unreviewed file, not a new candidate; it is not part of any current review set.  Found by analogy
with the Codex finding on v5 SEG-num (proof-REFLHI-arcs-v5-erratum-5.md I.13).

e1 (Proof, step (H1)).  The parenthetical "(v5 SEG-num proof; larger still if m_lo = 1 is the maximum)" is WRONG in direction:
m_lo = max(1, kappa + 1 - a) with a := ceil((R - d)/4), and the maximum with 1 can only shrink m_hi - m_lo.  Replace step (H1) by
the following two cases (b := floor((R + d)/4), c := ceil(R/2); m_hi = p - b, Pi_need + 1 = p - c + 1).
* a <= kappa (maximum inactive, m_lo = kappa + 1 - a): m_hi - m_lo = H - (b - a) >= H - floor(d/2), and (H1) follows from
  ceil(R/2) - floor(d/2) >= kappa + 2 exactly as printed ((q - 1)/2 >= (k - 2 kappa - 1)/2 >= kappa + 2).
* a >= kappa + 1 (m_lo = 1): (H1) reads p - b - 1 >= p - c + 1, i.e. c - b >= 2.  Since c >= R/2 and b <= (R + d)/4, the integer
  c - b is >= (R - d)/4, hence c - b >= a >= kappa + 1, which is >= 2 if kappa >= 1.  If kappa = 0, then R - d >= q - 1 >= k - 1
  >= p >= 5 (k >= p + floor(R/2) + 1), so c - b >= a >= 2.
The conclusion of Corollary SEG-k is unchanged.
e2 (Proof, step (H2), parenthetical on kappa).  Replace it by: "both follow from k >= 4 kappa + 5 whenever kappa >= -1; an avoider
has kappa >= 0 by (Pairs) of REFL/proof-K0star-r2.md (otherwise H >= p and p disjoint same-letter pairs give an identity
2p-subword)."
e3 (Theorem SEG as used).  Corollary SEG-k applies Theorem SEG with Pi_need >= 1 only (proof-REFLHI-arcs-v5-erratum-4.md shows
R <= 2p - 2 here), so it is read with erratum 5 Part I of v5 (clipped gains, I.12) and needs neither erratum 4's narrowing nor
Part II.
