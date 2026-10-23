# Sun(7) lane: K7-D23-RICH and K7-D23P

Recorded at 2026-10-19T06:24:26-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL.** Both are written proofs, produced by a model and reviewed by models of both families. This is not a Lean or human check.

## Accepted statements (exact scope)
- **K7-D23-RICH, setting (a1).** Texts: [RICH-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-D23-RICH-v1.md) `ba32d2829d62a684d82748994e2fd519d22b041d4d41ed00ecb44235f43f2bb3`, with [erratum-1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-D23-RICH-erratum-v1.md) `8261831ba11777cf1a7c4a1c714ba324f77bc58a3c4fdb297029dce67790ba69` (whose R-1 replacement of the last NO5(a) branch is mandatory) and the [consolidated erratum](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-D23RICH-D23P-erratum-v1.md) `55cb66ca55008fa7219451d2e45458726282abce618cdcdba134a7d97a94d428`.
  - No K7 configuration in setting (a1) has T* ⊆ W3 or T ⊆ W3*.
  - The structural lemmas G0, FG7 (chain form), Cor 5/6 with its equality clause, NO5, R3 (survivors S1–S4 are local-test survivors only), TR, CC, TZ (i)–(iii) and LZ hold at their stated scopes.
  - The abstract pattern P is excluded only conditionally, as a navigation remark: **if** it has T* ⊆ W3 or T ⊆ W3*, it is not realised. No other local pattern is excluded.
- **K7-D23P, setting (a2).** Texts: [D23P-v1](/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/sun-coset7/continuations/k7-k62-residue/K7-D23P-v1.md) `89739dc2de4d174ab695146a4c6bd781e09044732cbdbb10269bfb497e337880` with the consolidated erratum.
  - No configuration in setting (a2) has a 4-type z-row in either orientation, so both z-rows are of type (b′).

## Reviews ([freeze](sun7-D23RICH-D23P-review-freeze-v1.json) `c1e127a4…`)
- [Codex](sun7-D23RICH-D23P-codex-v1.prompt.stdout.txt) `d158f82613d7236ac1cb329618ace098faacb4896f2b9a349c5ec59e406f93ea` (observed gpt-6.1-sol, max, read-only): ACCEPT for both, 0/0/0.
- [Claude](sun7-D23RICH-D23P-claude-v1.prompt.note.md) `1106bbb5e99ae270f7505d2c7986285370fabd7cf59e77d827d311448bf09359` (observed claude-opus-5-5, max, no tools): ACCEPT-WITH-FIXES for both, 0 FATAL / 0 MAJOR / 12 MINOR (RF1–RF9, PF1–PF3).
- The consolidated erratum applies all 12 MINORs as verbatim Old→New items. No theorem conclusion changes. FG7 is restated in the chain form the reviewer specified, with the old statement kept as a special case.
- The parent spot-checked the RF1 item and the disposition table.

## Import closure
- **Direct:** Sun(2), Sun(3) and Sun(4) only, plus R0, L0.1, L0.3, LFC (a)–(d), INV, L1/F7/VFC, D23-CENTER and the D23-MIX conclusion.
- **Transitive:** through ROW-1, ROW-2, ROW-U/E8 and LFC provenance, the closure reaches the locally accepted, **computer-assisted** Sun(5) and Sun(6).

## Still OPEN
- The (a1) residue: D_t ∩ D_u = ∅ for u ∈ T* without a W-three in its α-row, or a count tolerating such u.
- (a2) with both z-rows (b′).
- The full K7 residue, K6.2* with e_d ≥ 4, and Sun(7).
- Later candidates that build on RICH (K7-TC, K7-TC-A22, A1-STRUCT) are unreviewed. RICH being accepted only discharges their RICH premise.
- The reviewer's listed open item "shared 2/3 markers with a 5-marker elsewhere" is already excluded by the earlier accepted Z23-P5 verdict.
- No novelty claim.
