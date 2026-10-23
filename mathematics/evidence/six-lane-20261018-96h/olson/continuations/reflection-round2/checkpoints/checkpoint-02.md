# Reflection round 2 (Slice B), checkpoint 02

Written after host clock 2026-10-19T05:05:52-0700.  Written research only.

- proof-REFLHI-tools-v1.md (79741c7c6830161ad4bd93e8776886fc6761743ef250c948735001e3748a7d6e) is an UNSENT partial
  draft: Secs. 0-3 only, and its Lemma RW proof contains an uncorrected self-interruption.  It is kept unchanged; the
  candidate will be v2 (new file).
- New tool (proved in the draft, Sec. 3): Lemma TOG.  For an all-odd G-word, a base pattern P_0 plus pairwise separated
  regions of EMPTY runs (free or attached to an end of P_0) never change D_P; Cauchy-Davenport on the u-contributions of the
  regions against the common window [-G', G] kills as soon as 1 + sum(nu(Z) - 1) + G + G' + 1 >= p + 1, where nu(Z) is the
  number of distinct block values along the region.
- Planned v2 content: Theorem ETA (B = 0, R <= 2 kappa + 1): with m* = kappa + 1 - floor(R/2) every m*-interval pattern
  has a single mass-independent forbidden value v_P = -floor(R/2) (R odd: when run 1 is nonempty); hence, for every
  partition of the block cycle into 2m* consecutive arcs, sum |eta(arc)| <= p + 2m* - 2 with eta_j = y_j/2 + rho_j.
  Theorem ESB: around any interval Q with E+(Q), E+(Q^c) <= 2 kappa, the maximal empty stretches outside Q satisfy
  sum(nu - 1) <= p - 2 - (R - 2 kappa); at k = p + 1 no such Q exists.  These are structural restrictions on any residual
  avoider, not yet a full exclusion.
- Failed so far: plain toggle counting in IIIb (the m-range with large windows has length H = p - 1 - kappa, too short
  when R <= 2 kappa); balanced intervals can be absent when one run carries almost all of A (giant-run configurations).
