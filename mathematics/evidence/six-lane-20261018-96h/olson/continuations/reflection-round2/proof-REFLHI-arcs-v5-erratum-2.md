# Erratum 2 to proof-REFLHI-arcs-v5.md (4e46374677e30bd7b306c6fcca9845a09b15daf93fa42a9f908d0beb8c8cff1c); overlay, file unchanged

Written after host clock 2026-10-19T06:11:12-0700 by OlsonReflectionSuccessor, applying the two Codex MINOR findings on v4 +
K2P+ relayed by the parent.  Erratum 1 (512e1d9e...3331) stays in force.

e5 (Codex MINOR 1; Sec. 3, the paragraph "Realisations of a parity change at M_j ...", v5 L107-108).  Replace it by:
"Let an arc choice consist only of single-block arcs ("singletons") and two-block arcs ("pairs").  A parity change at M_j is
realised by deleting a singleton of M_j if it has one; otherwise by adding a singleton on an unused block of M_j if it has
one; otherwise every block of M_j lies in a pair (M_j has >= 1 block), and one pair of M_j is split into two singletons.  The
result again consists of singletons and pairs; the arc count changes by +-1 and at most one pair is lost.  Nothing is claimed
for arc choices containing longer arcs."
Every use in v5 satisfies the restriction at the moment of each parity change: K2P+ (Sec. 5, steps (e)-(f)) and TOP (Sec. 6)
use only pairs and singletons; Theorem SEG and Corollary MID change parities only on the base, which consists of singletons and
pair-arcs, and add their segments afterwards (their explicit change rule - remove the base arc, or add a single block, a
pair-arc, or the first block of an L-run - is a special case).  Theorem FP and Corollary FP-1 (Sec. 4) never use this paragraph:
there the parities c_i are fixed directly and Lemma BAL is used only in its labelling form.
e6 (Codex MINOR 2; v4 Corollary K2P-num example "p = 31: kappa = 17..28, e.g. kappa = 20 with k = 71..65").  v5 contains no
such example; the v4 sentence is not carried into v5.  For the record, with K2P+ (k >= max(2p + 1, 3 kappa + 3) and, for
avoiders, k <= p + 2 kappa) the p = 31 cells are 16 <= kappa <= 28 with max(63, 3 kappa + 3) <= k <= 31 + 2 kappa; for
kappa = 20 these are k = 63, ..., 71, i.e. R = 2p - k + 2 kappa = 39, ..., 31 (R = p + 8 down to R = p).
No theorem statement or proof step changes.
