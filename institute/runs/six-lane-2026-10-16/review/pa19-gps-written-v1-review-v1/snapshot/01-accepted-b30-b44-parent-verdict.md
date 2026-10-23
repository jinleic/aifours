# PA(19,8,6) ms09 skeleton cases b30 and b44 — parent structural-exclusion verdict v1

Parent at 2026-10-18T07:07:42-07:00. **CORRECTNESS-ACCEPTED: the frozen independent-B skeleton cases b30 (`ms09_s00018`) and b44 (`ms09_s00021`) admit no packing array**, by the written definition-level lemma in [the candidate](../../../../information-science/evidence/six-lane-20261016/packing-array19/cycle2/ms09-b30-b44-structural-candidate-v1.json) (`04cdca2316d5b3b9e38ad8189409929d0b25390ea2b44a1a528c9e570302fbba`). This is a partial structural result for two of the 71 ms09 skeleton cases. It is not a global PA(19,8,6) statement and not a gate.

## Accepted statement

Rows: 19. Columns: 8. Alphabet: 6. Any two distinct rows agree in at most one column. The column profiles are five P0 columns (4,3,3,3,3,3) and three P1 columns (4,4,3,3,3,2).

**Lemma.** Suppose a row h lies in four of the five distinguished size-4 P0 groups Q0..Q4, and j is the missing index. Then at least two distinct rows must have Q-membership exactly {j}.

**Proof outline.** Pair counting saturates C(19,2) = 171, so every pair agrees exactly once. That gives h a P0 contribution of 14 and a P1 contribution multiset of {1,1,2}. h's two size-2 partners are distinct and avoid h's four occupied quads. An empty-membership partner would need P1 contribution 8 > 1+3+3. In b30 exactly one row has membership {4}; in b44 none does. Both cases are contradictions, independent of all later symbol placements.

## Evidence

1. [Codex](pa19-b30-b44-structural-codex-v1.note.md), `5aa21603c55070a3a709b48bf8cf30ddf3651458103c4abfa0026057d602389c`: **ACCEPT**, 0 FATAL / 0 MAJOR / 0 MINOR. Re-derives every step and the private-row counts (b30: (3,2,2,2,1); b44: (2,2,2,2,0)).
2. [Claude](pa19-b30-b44-structural-claude-v1.note.md), `9c36c373815300fc2392c721d596654a3937911812d5ca82c2034961a882ed80`: **ACCEPT**, 0 FATAL / 0 MAJOR / 4 MINOR. Recounts the skeleton list and the b30/b44 block positions independently. All four MINORs are editorial (see below).
3. Parent check [RESULT](pa19-b30-b44-parent-v1/RESULT.json) (`531b06eb4d2e46803d1d06185336642b78744facaecf68f622ef2b3c411510c4`, script `check_v2.py` `43861d09018d9b3485e05d4057ac82fdc1d24556dad66474ffc634987e9eda41`, pinned before execution). It verifies:
   - pair saturation 171 and the forced triples {1,1,2};
   - the skeleton binding and eligible-partner counts 1 and 0;
   - exact list/contract binding: 2,858 and 547 placements, 29 and 6 original B100 intervals;
   - two boundary controls (no existence claim).
   The finite check is supporting evidence, not a premise.

## MINOR dispositions (editorial; no proof change)

- **Claude 1:** say why each P1 contribution lies in {1,2,3} (profile sizes; one size-2 group per column).
- **Claude 2:** in b30 the needed fact is "at most one {4} row", which holds even without the fill rule.
- **Claude 3:** define "all-P1, L=0", or drop it; the proof does not use it.
- **Claude 4:** concerns the parent checker only (a hard-coded status and a trivially passing control). The checker is not a premise.
- **Aside (Claude):** the same argument excludes a row in all five quads (residual 3 ⇒ {1,1,1}). This is **not** accepted here; it needs its own candidate and disposition.

## Production effect

The 35 original B100 intervals (3,405 placements) of b30 and b44 may be classified **STRUCTURALLY-EXCLUDED (parent verdict v1)** in a new versioned M9 contract or overlay. That requires exact interval IDs, this verdict's SHA, and no deletion or rewriting of earlier records. They must not be counted as solver/DRAT-certified. Final M9 coverage must report them separately, as parent-accepted written mathematics.
