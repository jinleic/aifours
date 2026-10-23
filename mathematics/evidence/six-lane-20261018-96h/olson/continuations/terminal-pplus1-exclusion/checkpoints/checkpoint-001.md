# Checkpoint 001: PP1-EXCL (exclusion of terminal k = p+1, kappa^ = p-1, all-singleton blocks)

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T12:47:02-0700. Slice started 2026-10-19T12:29:48-0700 (first /bin/date); scope frozen 12:37:11.

- Scope (frozen 12:37:11, chmod a-w): PP1-EXCL-scope-v1.md, sha256 d386f94414f0bdcbd44694d9676b836da511daa5c923200ff9375db977e32fba,
  4841 bytes; it discloses the mental pre-freeze sketch (s1)-(s3) (nothing written before the freeze).
- Candidate (written 12:46:13, chmod a-w): proof-PP1-EXCL-v1.md, sha256 6fea2fd20ba4d13fb1cf972927da379556b1f33ea18a8ea661740705c80944d0,
  23669 bytes. CANDIDATE_UNVERIFIED.
- Actual result claimed (written, word level): for prime p >= 7 NO avoider of length 4p-2 over D_(2p) has an admissible normal form
  with terminal k = p+1 and kappa^ = p-1 (Theorem PP1-EXCL, via the word form PP1-EXCL'). No o_F hypothesis. Two routes:
  (a) Theorem EXCL-PM [NEW]: under the explicit pair hypothesis (rotations in one {rho_c, rho_-c}, c != 0; = conclusion of the
      PENDING ROT-SING+, stated as a hypothesis) the all-plus pattern forces (A,B) in {(2p-2,p-1),(2p-1,p-2)}, the p+1 single-run
      patterns with Lemma W (full window when both signed counts >= p-1) force at least p runs to hold a rho_(-c) letter
      (empty runs excluded via tau_i != 0 in the second case): contradiction. Input: GRX only.
  (b) Unconditional: Lemma CL (CT, n = p-3), Lemma OM/OM' (RS(b)), Lemma ER and the H1 elimination are RE-DERIVED from the
      ROT-SING+ route (not new progress); NEW Lemma SR (single-run count) eliminates H2a and H2c outright.
- Inputs re-hashed (shasum) before writing; all equal to the pinned values. No computation, enumeration, model call, Lean.
- Blocker: none for the written candidate. Next bounded action: review package + excerpt manifest (<= 100 KB), IRC Main with
  paths/SHAs, then park (parent owns model reviews/verdicts).
