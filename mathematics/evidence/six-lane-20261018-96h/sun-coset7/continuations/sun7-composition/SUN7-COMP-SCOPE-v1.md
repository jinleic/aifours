# SUN7-COMP-SCOPE-v1 — frozen target for the proof-level composition of full Sun(7) [no claim]

- **Written:** `/bin/date` read at 2026-10-19T16:25:21-0700, immediately before this exclusive write (directory created empty just before).
- **Owner:** SunM13MixedFibres, slot math-1. Written mathematics only; no computation, enumeration, solver, test, model
  call, nested agent or source import. Parent owns reviews and verdicts.
- **Authority:** `RUN/control/mathematics-slot-transition-sun-composition-20261019-1623-v1.json`, sha256
  769525e0091bb9d864cd08e9acad1f7ac5f58a163801a3461ca43bb4eee3c3b5 (first `/bin/date` of this slice 2026-10-19T16:23:34-0700);
  route correction `RUN/review/sun7-X1-stale-route-correction-v1.json`, sha256 d272679d2e9e68e002fe409ee1c11cc0b3948a0a81918a3a53f744a4adf95ff0.
  RUN := `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h`.

## 1. Frozen target (literal)
**Sun(7).** Let G be any group, U_1, ..., U_7 subgroups of finite index (possibly equal), and g_1U_1, ..., g_7U_7 pairwise
disjoint left cosets. Then gcd([G:U_i], [G:U_j]) >= 7 for some i < j. (Text of record: README line 11 of
`/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7/README.md`, sha256 2a6d6d6e…3fd1.) No
missing class, exponent cap assumption, minimal-counterexample frame or common-index-factor assumption may enter.
**Task:** a proof-level ASSEMBLY: CE definition and finite-core lift R0; the exact six-class partition from the accepted
written reduction; every class excluded by an authority applied at its literal scope with all mandatory errata; K7
exhausted by K7-NF + (a1) + (a2); K5.3 by the accepted written X1 (StageA not used); K6.2* by K62-FULL with all errata;
K6.3 by its accepted full exclusion; the latest authorities for K5.2*, KII, Sun(5), Sun(6) discovered from the records.

## 2. Deliverables
1. `SUN7-COMP-v1.md`: statement, CE, R0, partition, class table, Conditional Composition Theorem, exact dependency DAG
   (path, sha256, mandatory errata, verdict), computation boundary (every computer-assisted load-bearing node), full-result
   gate table, and every real mathematical gap stated as an exact obligation.
2. Review units, each independently complete with <= 100 KB raw excerpts and a JSON manifest {path, sha256, start, end}:
   one composition unit plus units containing the FULL bodies of the untrusted new nodes K7-NF and K7 A2 units 1-3 (with
   the literal accepted statements they import). Context-only declarations never replace a new node's proof. Whether the
   existing NF/A2 packages already satisfy this is decided after inspecting them; any reuse is stated with hashes.
3. Checkpoints <= 1800 s apart (target 1200 s) and a final IRC with paths and SHA256s.

## 3. Premise discipline
- Accepted nodes: only at the literal scope of their accepting verdict plus mandatory errata/overlays.
- Untrusted new nodes (CANDIDATE_UNVERIFIED): K7-NF (`continuations/k7-complement-f/K7-NF-v1.md`, 734613fd…3e97) and A2
  units 1-3 (`continuations/k7-a2-closure/`, 79d948bf…, 1bef6d8c…, a2b40a9e…). They enter ONLY as explicit hypotheses of a
  conditional composition; no review result or approval is used as a premise.
- Not premises anywhere: StageA output; M-S Lemma 4.6; Menon's theorems; FH/L5/L6; a minimal-counterexample frame; Sun(7);
  any pending candidate other than the four named new nodes.
- The result is CANDIDATE_UNVERIFIED and CONDITIONAL until all new-node two-family reviews, the parent composition check
  and every full-result gate pass. No acceptance, novelty, Lean, human-review or publication claim.

## 4. Outcomes
(A) a complete conditional composition with no missing class or interface; or (B) the exact missing interface or
obligation, with the failed route. No computation replaces a missing step.

## 5. Pre-freeze exposure and sketch (disclosed)
Read before this freeze in this slice: the transition and correction above; README lines 1-110 (R0, CE, P0, P1, R1(7),
section 5 class table); `six-lane-2026-10-16/review/sun-coset7-written-parent-verdict-v1.md` (whole);
`six-lane-2026-10-16/review/sun-coset7-stageB-classes-parent-verdict-v1.md` (whole); `RUN/review/sun7-K63RES-parent-verdict-v1.md`
(whole); `RUN/review/sun7-K63-frontier-status-correction-v1.json`; the review-directory listings. Earlier in this lane I
authored K7-NF (whose Corollary K7-REM states K7 \ (a2) is excluded by accepted results plus K7-NF) and the A2 units.
Expected shape (not yet checked): K5.2*, KII by the StageB verdict (computer-assisted, one independent checker); K5.3 by
the written X1 verdict plus the accepted bridge; K6.2* by K62-FULL; K6.3 by K63-D + K63-E + K63-RES; K7 by K7-NF + accepted
(a1) closure + candidate (a2) units; computation boundary at least Sun(5), Sun(6) and StageB. No derivation was written.
