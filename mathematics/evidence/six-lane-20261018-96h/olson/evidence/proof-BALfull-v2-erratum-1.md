# Erratum 1 (pre-review) to evidence/proof-BALfull-v2.md (sha256 dffbfea8d97730e6c7a7a5f384cb471c64dda17091829fcd289a5c5a9775a3e1)

Owner ContinueOlson.  Written after /bin/date 2026-10-19T01:15:30-0700, before any review of BAL-full.  Applies to BAL-full v2 the
citation/notation points that the ROT-ZB v2 Claude review (run review/olson-rotzb-claude-v1.prompt.note.md
6c1b7108...72f2) raised for the parallel text (ROT-ZB v2 erratum 1, evidence/proof-ROT-ZB-v2-erratum-1.md
a181edbb...c0de).  The v2 text is not edited; no statement changes.

1. (ROT-ZB m5 analogue; source of k >= 1 and the case o_F = 0.)  Sec. 5(a)'s 'Every admissible normal form has
   1 <= k <= o' is cited to the accepted normal form (proof-ROT-few-E-v4.md Sec. 0; ROT-ZR verdict m4: F, R >= 1, odd
   terminal blocks, kappa^ >= 0): F = 0 is excluded by the rotations-only EGZ bound, and the terminal form is either
   1 <= k <= o odd blocks or one even block, the latter impossible by K1/Davenport.  Hence every avoider of length 4p - 2
   has o_F >= 1 and k >= 1, and Corollary (a) is vacuous at o_F = 0.
2. (ROT-ZB m6 analogue.)  Sec. 4 line 1 cites ZX overlay 1 (integer-domain condition) AND ZX overlay 2 (existential
   reading of the normal form).
3. (ROT-ZB m6 analogue.)  Sec. 4's SHgen-E caller is replaced by the ROT-ZR verdict's discharge: 'Empty runs use SHgen-E:
   expansions preserve k and odd blocks; base words have length 4p - 2, one nonzero pair, and o_F(u°) <= k <= p - 1, so
   restricted REFL and the accepted V3 caller apply.  The normal form preserves rotation letters.'
4. (ROT-ZB m2 analogue.)  Sec. 6 of BAL-full v2 uses no unrecorded planning functions; its residual description
   (3o_F >= 2p + 2 and F <= 2o_F - 2, for o_F <= p - 1) is relative to S1-sharp's corollary and Corollary ZB+ only.  In
   terminal terms, if BAL-full is accepted the rotation residual becomes: k = p with kappa^ >= 2; OR
   (2p + 2)/3 <= k <= p - 1 with 2kappa^ + k >= 2p (DAV kappa^ <= k - 1 forces k >= (2p + 2)/3 there).
5. Sec. 6 bullet 1's comparison with ROT-ZR is restated: ROT-ZR's cells have kappa^ <= (p - 1)/2 and k <= p - 1, hence
   2kappa^ + k <= 2p - 2, so every ROT-ZR cell with k >= 2 satisfies Theorem ROT-ZB+'s hypotheses.
