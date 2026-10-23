# MOLS(39) lane: exact-anchor mod-3 lift classification (Lemma U) and corrected R1

Recorded at 2026-10-19T06:10:52-0700.

**CORRECTNESS_ACCEPTED_SCOPED_PARTIAL — computer-assisted, exact anchor only.** The anchor is the Sage DM_39_6_1 matrix (raw SHA256 `3c8dbe62…a882a`), with rows in file order, normalised at row 0 and columns in file order.

- **Lemma U.** The rainbow mod-3 lifts of the anchor's mod-13 skeleton are exactly ε·α+e, with ε=±1 and e a row-constant vector: 2 classes and 486 lifts with A₀=0, counted before the quotient.
- **Corrected R1.** Read through [erratum 1](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/erratum-R1-S4-v1.md) and [erratum 2](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/erratum2-R1-S4-v1.md). Given Lemma U, a human proof shows that one-row extensions of the exact anchor exist if and only if β-route extensions of its skeleton exist. The explicit maps are f=μ⁻¹(D*₆−D*₀)+D₀ with μ∈{1,14}, and β₆=(f−D₀) mod 13.
- **Both extension questions remain UNKNOWN.** There is no construction or nonexistence result for CFR(6,39), six MOLS(39) or any other difference matrix. The non-anchor rows of S4 are not promoted.

## Evidence
- **Three enumerations, consistent with each other** (the two programs plus the parent control are independent implementations; recorded executions only):
  - Route 2 L4: an independently authored DFS with a GF(3) propagator, under a [parent endpoint audit](mols39-lift2-parent-endpoints-v1.json) (`c49207c3…`), with the DM21/Singer57 controls as expected.
  - The [parent's dense RREF control](mols39-lift-parent-control-v1/result.json) (`30341aaa…`). It is the parent's own code with a fresh gate and a supervisor run; it enumerates all 243 quotient vectors, has 190 gauged variables, rank 185 and dimension 5, and gives exactly the same two representative digests.
  - Route 1 S4a, which corroborates the counts only.
- **Reviews:**
  - [Codex](mols39-LemmaU-R1-codex-v1.prompt.stdout.txt) `3d7509c17bfd62ebb69c68daa07ac723e0acba2dbe72d1864baa1b306d6810cd` (observed gpt-6.1-sol, max, read-only): Lemma U ACCEPT; corrected R1 ACCEPT, conditional on U; MINOR provenance and contract qualifications.
  - [Claude](mols39-LemmaU-R1-claude-v1.prompt.note.md) `78f13c8806b67c284b202413d93447fb4c60684e329ef9bf503e8dabe8dd14ae` (observed claude-opus-5-5, max, no tools): Lemma U ACCEPT; R1 ACCEPT-WITH-FIXES. Its one MAJOR (M1) is confined to R1 Consequence 3; MINORs m1–m12.
- **Erratum 2** `88a4369970414303d6f90af127bb996827c76456cfef2c22cb70ce0c7db8cc84`: the parent read it in full.
  - Consequence 3 is restricted to the anchor and downgraded to "potentially wider; not established". The claims "genuinely wider", "6-row lift space" and "not wider" for DM21/33/51/P21 are withdrawn.
  - Every MINOR is disposed. Consequence 1 is restated as an existence equivalence; the T2/T6 statuses are imports and are unused; the G6/C3/C2 negatives are **not** transferred to the β route.
  - No statement is broadened.

## Deviations and limits
- Deviation M39-D6: per-child launch identities for L1–L4, the ext2 control wave and T4–R7 reached the parent only with the results. They were registered late, after an endpoint audit.
- There is no Lean or human-checkable certificate. A certificate specification ([spec](/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/mols39/evidence/lemmaU-certificate-spec-v1.md) `b151a61f…` plus erratum `beca7d33…`) is frozen but not executed, because of the runtime hold.
- No novelty or priority claim.
