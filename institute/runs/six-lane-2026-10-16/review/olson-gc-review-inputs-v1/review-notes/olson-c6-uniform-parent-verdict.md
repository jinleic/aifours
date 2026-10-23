# Olson cycle 6: reviewed seed, count and singleton results

Parent disposition recorded after 2026-10-17 23:40:15 PDT. **CORRECTNESS-ACCEPTED at the scopes below; PARTIAL, not a gate.** No full ordered-Olson, INV*, RUNS or NMH theorem is claimed.

## Accepted written statements

All notation and NMH hypotheses are those in the pinned cycle-3/6 source files, not arbitrary dihedral words. In particular, the all-single-letter conclusion below includes **R = k ≤ 2p−3**; it is not a statement about every singleton NMH word at larger R.

| Accepted component | Exact scope / dependency | Current source and SHA-256 |
|---|---|---|
| SEED-G r2 | Canonical lifts plus, for every run, a quality seed from actual configurations, or an actual-configuration empty intersection; the stated C0+ condition gives an identity 2p-subword | `proof-SEEDG-r2.md`, `353b0e95c4e58d874038a11b5864514f4049753853d355015e27ebf7330130b7` |
| LF / SCW-G* / QQ / SEED-G* | Relaxed seed bounds, the required two-run condition P2, and actual-configuration seed provenance; PIN is automatic. Empty QS/QS* windows alone do not exclude a word | `proof-SEEDGstar-r2.md`, `0a02042b089b1827099766fcf02b4094ea2d83dd55be2ba883ea5b49c4b6fcfe` |
| Written class-level implication | The precise allowed-profile and actual-empty/seed hypotheses imply the stated conditional exclusion. Numerical coverage claims remain computer-assisted aids | `proof-SEEDG-cls-r2.md`, `5a45bfe803eb717b2266a2ffec5d601b26f59bdc256f95c1dfe060d3493bfd41` |
| DF / C0W / C0B and conditional SEED-G** | The written count-side arguments under their stated NMH/lift hypotheses; SA**/PA** keep the original regions and actual-empty alternatives | `proof-C0WB-r2.md`, `7900f468c3f0cb10a1c586972b784e4184bc737ce6ad9caa6710f7a6b0d036f1` |
| RZ-wide | All-single-letter NMH, g=kB≥1, B≥g+1, κ=g+B≤p−3, primes p≥7; actual mixed-single configurations supply quality seeds or actual empty intervals | `proof-RZwide-r1.md`, `36fad72bfc12f7a9fced5c40d684e68fefa27c72332547800dc62be03886f41b` |
| S2-wide and its assembled corollary | Complementary g≥B≥2 singleton region, with the five exceptional families handled in writing. With RZ-wide and the reviewed B=1 results, **every all-single-letter NMH word with R=k≤2p−3, prime p≥5, has an identity 2p-subword** | `proof-S2wide-r1.md`, `ff96e3b52355b21be357dabfc88f95701112f4dfc3db4bae32d000552510ba02` |
| A0 and C0-all | Integer defect-prefix lemma A0; the lifted system (L) is infeasible for NMH with R≤2p−3. C0-all imports C0W, accepted above. This proves no universal seed-existence statement | `proof-A0-r1.md`, `fba51b126e05e865c0af50de1d2572f569e46e0a941d6b3f88d796332eb781a0` |

Source root for the table: `mathematics/evidence/six-lane-20261016/olson/inverse-run-count/mixdef-high/c6/`.

For the count-free seed corollary, the quantified alternatives are essential: some run has an empty intersection of bounds obtained from actual configurations; or every run has an actual quality seed; or every run has a nonempty actual seed satisfying QS* and the whole family satisfies P2. The accepted proof shows such seeds would contradict (L). It does **not** show every positive-excess word admits them.

## Review and verification chain

- SEED-G r1 received Codex and Claude ACCEPT-WITH-FIXES; the r1→r2 repairs passed the [delegated delta check](olson-c6g-r2-delta-v1/delta-check-v2.md). It checked the six Claim E′ classes' region memberships, the p=7 gap and 1,380,480 arithmetic region instances. The parent integrates that result here; its finite checks are aids.
- SEED-G*/class-level sources received [Codex](olson-c6g-r2-star-codex-review-v1.note.md) and [Claude](olson-c6g-r2-star-claude-review-v1.note.md) ACCEPT-WITH-FIXES. The Codex MAJOR was an overstatement of the remaining obstacle: **377** reported OPENE classes pass the seed test but fail C+'s class sufficient condition, while **one** fails the seed test. That was corrected, including the distinction from per-word C+ hypotheses.
- C0WB received [Codex](olson-c0wb-codex-review-v1.note.md) and [Claude](olson-c0wb-claude-review-v1.note.md) ACCEPT-WITH-FIXES with no FATAL/MAJOR. DF/C0W/C0B were judged sound; repairs clarify F3 bracketing, profile quantifiers, census ranges and one-way implications.
- The repaired r1 sources passed the [delegated repair delta check v2](olson-repair-delta-v1/delta-check-v2.md) and a [Codex delta review](olson-repair-delta-codex-v1.note.md). The desk independently checked exact LF forms, relaxation, QQ and PIN over the recorded ranges, including large-integer controls. Those checks do not certify the full class-census implementation.
- RZ-wide, S2-wide and A0 received [Codex](olson-uniform-codex-review-v1.note.md) and [Claude](olson-uniform-claude-review-v1.note.md) ACCEPT-WITH-FIXES, with no FATAL/MAJOR. Both checked the generic-arc arguments, packing cases and A0 inequalities. All arithmetic/mutation aids remain aids, not theorem premises.
- **Final parent delta:** the parent read all changed lines of all six final revisions. [Exact diffs and result](olson-c6-final-parent-delta-v1/result.json), SHA-256 `cc69badc233444fe02561afdbecc5e0e2f1f9ed9fc24c5056ff3eb0e83bd9f17`. Repairs address the d=0 gap formula, historical floating arithmetic, limit provenance, RA2 identification, imports, wraparound/properness, explicit R≤2p−3 scope and conditional C0W labels. No recipe, table entry or substantive inequality was changed by the final wording revisions. The optional S2 c=1 simplification is explicitly unused.

## Remaining limits and open obligations

- The scope is the specified NMH/lift system and singleton subcase. It does not close positive excess E≥4 outside the explicitly proved regions, or INV*.
- The 315-row E2 constant certificate, the small-prime supplement and `proof-E2all.md` remain producer-verified candidates. No independent certificate acceptance is implied here.
- Other excess-family files such as E-global have not been accepted by this verdict.
- PAR/MIX_low has its own [accepted partial verdict](olson-par-mixlow-parent-verdict.md). Full ordered Olson for D₂ₚ still requires RUNS(p) and INV*(p).
- No Lean formalization or human peer review. These are reviewed written partial lemmas. The [bounded priority screen](olson-par-priority-scout-v1.md) found no equivalent partial theorem but assessed no improvement to the published bound on z(D₂ₚ); no novelty or separate breakthrough gate is claimed.
- Historical status lines and project-relative source references are interpreted through the pinned snapshots and this dated disposition; originals are preserved.
