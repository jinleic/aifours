# Erratum 4 to proof-REFLHI-arcs-v5.md (4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c); overlay, file unchanged

Written after host clock 2026-10-19T06:43:43-0700 by OlsonReflectionSuccessor, answering the parent review question
(RUN/review/olson-REFLHI-v5-split-review-freeze-v1.json): Theorem SEG's raw setting allows Pi_need = p - ceil(R/2) < 0.
Errata 1-3 stay in force.

## Finding (confirmed)

Pi_need < 0 can occur inside the hypotheses of Theorem SEG: an avoider has A <= 2p - 1 and, after the normalisation A >= B,
B <= kappa (K0star-r2 (Z0)), so R = A + B can exceed 2p when B >= 2 (e.g. parameters p = 11, kappa = 8, k = 12, R = 26 satisfy
R = 2p - k + 2 kappa, k >= p + 1, A <= 21 forces B >= 5 < kappa).  For such words the printed proof line
"sum t_j <= Pi_need" is false (the least admissible t_j are 0), and the printed (H1) m_hi - m_lo >= Pi_need + 1 can be <= 0,
whereas the proof needs the base value m_b in {m_lo, m_lo + 1} to satisfy m_b <= m_hi.  So the printed hypotheses do not
support the printed proof when Pi_need < 0.  The raw statement is therefore CORRECTED (narrowed, explicitly) as follows.

## Correction

Put Pi+ := max(0, Pi_need).  In Theorem SEG (v5 Sec. 5) read
   (H1') m_hi - m_lo >= Pi+ + 1   and   (H3') g_E >= Pi+ + 1
in place of (H1), (H3); in its proof read "sum t_j <= Pi+" and "m in [m_lo, m_lo + 1 + Pi+]".  With these hypotheses the proof
is unchanged: when Pi_need <= 0 all t_j = 0, every configuration is the base with m_b in {m_lo, m_lo + 1}, inside [m_lo, m_hi]
by (H1'), and Lemma 3.2 applies because the window sum floor(E+/2) + floor(E-/2) >= ceil(R/2) - 1 >= p - 1 - Pi_need >= p - 1
already (total gain >= 0 >= Pi_need).  (H3') is then automatic except for g_E = 0, where it is not needed either; it is kept
only to make the statement uniform.  For Pi_need >= 0, (H1') = (H1) and (H3') = (H3): nothing changes.

## Effect on the corollaries (no change)

Every application of Theorem SEG has Pi_need >= 1, so the correction does not touch them:
* SEG-p and MID: R = p, Pi_need = (p - 1)/2.
* SEG-num: R = p + delta with 5 delta <= p - 10, so R < 2p - 1 and Pi_need >= 1.
* SEG-k (separate addendum, not in this review set): if R >= 2p - 1 then k >= p + floor(R/2) + 1 >= 2p, hence
  R = 2p - k + 2 kappa <= 2 kappa <= 2p - 2, a contradiction; so R <= 2p - 2 and Pi_need >= 1 there.
K2P+, TOP and Lemmas ARC+, SEG, 3.2, BAL do not use the printed (H1)/(H3) of Theorem SEG.  K2P+ has R <= 2 kappa - 1 <= 2p - 3.
