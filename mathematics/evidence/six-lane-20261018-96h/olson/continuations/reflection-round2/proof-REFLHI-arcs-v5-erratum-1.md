# Erratum 1 to proof-REFLHI-arcs-v5.md (4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c); overlay, file unchanged

Written after host clock 2026-10-19T06:08:24-0700 by OlsonReflectionSuccessor, from a self-check before sending.

e1 (Lemma SEG proof, Sec. 2).  Read "If b' = 2 <= 2t + ..., t >= 1" as "If b' = 2 and t >= 1".
e2 (Theorem K2P+ proof, Sec. 5, step (d)).  Add: for p = 5 the hypotheses cannot hold for an avoider (Fact 2.2 gives
k <= p + 2 kappa, and k >= 11, k >= 3 kappa + 3 then give kappa >= 3 and kappa <= 2), so the theorem is vacuous there; for
p >= 7, d <= p - 6 <= 2p - 12 as used.
e3 (Corollary MID, Sec. 6, rate argument; the printed sub-case reasoning "if every L-run is in O, then |AB| <= 2 forces
sum of e_j >= p - 3, so one of their segments has >= 3 blocks" is not valid as written).  Replace it by: if every L-run lies in
O, then lambda_0 = 0 (otherwise lambda_0 = N_O - n_CA = N_O - p + |L| and |L| <= |L n O| <= lambda_0 + 1 would give
N_O >= p - 1, while N_O = p + 3 - 2r <= p - 3 because r >= 3 for p >= 11), so |L| <= 1; with |AB| <= 2 the single L-run has
e_j >= g_E - 2 = p - 3 >= 8, and its segment (M_j minus its first block) has e_j >= 3 blocks, whose first pair gains 2.  If
L is empty, |AB| = g_E = p - 1 >= 3 and the first case (a base pair-arc survives BAL) applies.  The conclusion
sum t_j <= Pi_need - 1 is unchanged.
e4 (Corollary TOP, Sec. 6).  Replace "Pair capacity sum floor(b_i/2) >= kappa >= p - 2 >= Pi_need + 2 + 1" by: the pairs
available together with one singleton in M_l number at least kappa (sum floor(b_i/2) = kappa + (number of odd e_i)/2; if b_l
is odd, a singleton fits beside floor(b_l/2) pairs of M_l; if b_l is even, the number of odd e_i is >= 2 and one pair of M_l is
given up), and kappa >= p - 2 >= Pi_need + 2 = (p + 3)/2 for p >= 7.
No theorem statement changes.
