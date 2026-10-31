# AME(4,6): supports 46 and 47 excluded at the recorded import boundary

**Disposition: parent composition, independently audited in the same harness, conditional on the pinned prior results.** No normalized complex AME(4,6) state has exactly 46 or exactly 47 nonzero coefficients in any local product basis. Together with the recorded lower bound 45 and the separately checked 60-term tensor, the minimum support `m` is constrained by

`m ∈ {45} ∪ {48,49,…,60}`.

This is an **outer set**, not a claim that any member other than the 60-term witness is attained. In particular, support 45 has not been excluded by these inputs, so this composition does **not** establish `m≥48`. The later `N=45` candidate is under the separate f226 review and is not a premise here.

## Exact union

Fix one normalized state and one product basis; all three 2|2 flattenings and all six pair projections refer to this same tensor. Write `N=t+|E|`, where `t` counts coefficients of modulus `1/6`. Removing the `t` singleton rows and columns of each scaled unitary leaves a `36−t` square residual with at least two nonzeros per line, giving `N≥72−t`.

- At `N=46`, this gives `t≥26`. The adopted f113 result gives `t≤29`, and the f141 disposition excludes `t=27,28,29` at `N=46`. Thus only `t=26` remains. The f127 no-Hamming-one lemma applies to the resulting 20-word residual of that same tensor. The f182 disposition excludes the nine non-`(4,4,4,4)` sorted residual-alphabet profiles, and f127's separate computer-assisted branch excludes `(4,4,4,4)`. These are the ten possible profiles, so no `N=46` state remains.
- At `N=47`, the separate f214 composition already excludes all states at its stated `t≤29` provenance. It does not follow by applying the `N=46`-specific f141 exclusions to `N=47`.
- The earlier lower-45 disposition and the recorded actual 60-term tensor provide the outer range and nonemptiness. The 60-term record reports exact row and column Gram `2I_36` in all three cuts before normalization by `sqrt(72)`; this audit inherits that checked witness statement rather than re-reading its coefficient table.

## Trust and process boundaries

The composition inherits the **unreplayed classical no-OLS(6) theorem**, f113's earlier `t≤30` provenance, and the f127 normal-form reduction and reviewer-enumerator coverage for the final 4444 branch. The f127 record reports that no separate historical f127 manifest file was present; the present audit does not create or retroactively repair one. The f182 reviewer independently implemented its control after reading author checker bodies, so that control is **not clean-room**. The f107 finite-only review did not independently establish its global lower-45 theorem; the written-proof review and parent disposition support that result at their recorded scope. The 60-term coefficients and checker were not replayed in f222.

Frozen composition manifest: `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f222-ame46-n46-n47-support-composition-audit/manifest-v1.json`, SHA-256 `d3413126ea184e26df025b414da35fd7c3003297963b5e41c39eae4f0737ba94`. Same-harness audit: adjacent `review-v1.md`, SHA-256 `c30eebc5850a4ecddc0449811918988889025e0246c104083e17454c494e056a`, 138 LF, **0F/0M/0m** on the conditional composition, with seven explicitly inconclusive stronger or unreplayed claims. It did not rerun an inherited enumerator. The parent displayed all 138 review lines in raw windows 1–15 through 136–138, read the seven pinned parent dispositions, and rechecked their complete hashes, bytes and LF against the manifest before this record.

Parent observed `/bin/date` `2026-10-29T13:53:48-0700 PDT` before writing. This is same-harness written/computer-assisted support, not human review, independent-model-family review, a formal/kernel certificate or a novelty/priority determination.
