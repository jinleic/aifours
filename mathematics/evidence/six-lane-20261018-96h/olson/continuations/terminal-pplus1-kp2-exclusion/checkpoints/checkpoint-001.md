# Checkpoint 001: KP2-EXCL (exclusion of terminal k = p+1, kappa^ = p-2: one length-3 block, p singletons)

Owner OlsonPP1Exclusion. /bin/date 2026-10-19T13:03:45-0700. Slice started on Main's IRC (12:52:04; first /bin/date 12:52:21); scope frozen 12:52:47.

- Scope (chmod a-w): KP2-EXCL-scope-v1.md, sha256 20ea30954e76a18bbc6d4b02f826d35e2d285e1619f306997cf18f40447d9390, 4491 bytes;
  pre-freeze disclosure: generic plan only, nothing written or worked.
- Candidate (written 13:03:04, chmod a-w): proof-KP2-EXCL-v1.md, sha256 8be43069c0a7935db902ba2ae4dda533b661ae0c981517f62f0e2b64e518b002,
  24992 bytes. CANDIDATE_UNVERIFIED.
- Actual result claimed (written, word level): for prime p >= 7 NO avoider of length 4p-2 over D_(2p) has an admissible normal form
  with terminal k = p+1 and kappa^ = p-2 (Theorem KP2-EXCL via the word form KP2-EXCL'). No o_F or run hypothesis. (SEL) recomputed:
  delta = p+1-Phi, C_max = Phi+2, so n in {2p-2m, 2p-2m-2} (long block gives 2 or 3 letters).
  (a) Theorem EXCL-PM2 [NEW], pair hypothesis stated (pending ROT-PP1-TOP conclusion), GRX only: all-plus gives
      (A,B) in {(2p-3,p-2),(2p-2,p-3),(2p-1,p-4)}; general window Lemma W2; single runs, pairs/sets of runs, empty runs
      (tau_i forced to -2c resp. impossible resp. 2c) close all three cases.
  (b) Unconditional: Lemmas M, P, U, window (W), heavy run, empty-run count and three-case empty-run analysis RE-DERIVED from the
      pending proof-ROT-PP1-v2.md; NEW: those steps hold for delta = 0 (light sets via A' <= p-2), so the argument excludes the cell
      rather than proving delta = 0; NEW Step 5 (lambda >= 0) replaces the CT step, so CT is not used.
- Inputs re-hashed (shasum) before and after writing; all equal to the pinned values. No computation, enumeration, model call, Lean.
- Blocker: none for the written candidate. Next bounded action: review package + excerpt manifest (<= 100 KB), IRC Main, park.
