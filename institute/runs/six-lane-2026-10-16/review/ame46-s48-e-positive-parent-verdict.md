# AME(4,6) s = 48 layer: four e > 0 cases — parent verdict

## Result and exact scope

**No AME(4,6) state has parameters (t,e) = (30,6), (28,4), (27,3) or (26,2)** in the support representation of LOWER42/46/48. Here t is the number of coefficients of modulus 1/6 (classical officers), support size is s, and e = s − (72 − t). Each listed pair has s = 48.

These are **partial exclusions, not a stronger support bound**. The remaining (24,0) proof run is UNKNOWN after its disk guard tripped. The accepted range remains **48 ≤ s_min ≤ 60** ([lower48 verdict](ame46-lower48-parent-verdict.md)); no s ≥ 49 or frozen-gate completion is claimed.

## Evidence

Parent-delegated replay: [result](ame46-s48-parent-replay-v2/result.json), SHA-256 `86eb215c…76b4`; script `ame46_s48_parent_replay_v1.py` (`b55a6b6b…0aac`). Run 2026-10-17 16:30:20–16:30:48 PDT. The first attempt (`ame46-s48-parent-replay-v1/`) failed with a path-formatting TypeError before checking anything; retained.

| (t,e) | Complete normal-form profiles | Lemma 17 exclusions | Regenerated final CNFs / RUP-verified proofs |
|---|---:|---:|---:|
| (30,6) | 2 | 1 | 1 / 1 |
| (28,4) | 7 | 2 | 5 / 5 |
| (27,3) | 6 | 3 | 3 / 3 |
| (26,2) | 25 | 1 | 24 / 24 |

- All 40 profiles independently enumerated and matched with no duplicate; Lemma 17 recomputed for every profile (α = 0..4; extending to −40..40 adds no exclusion).
- **All 33 final CNFs regenerated with matching SHA-256** from the corrected written [schema r2](../../../../physics/evidence/six-lane-20261016/ame46-support/review/V4_PROOF_SCHEMA.r2.md), SHA `ef692d9d…9309`. The officer clauses C1–C3, J linking, lex chains and composition were independently written by the parent replay worker; the base came from the previously bound pinned base generator. No lane J, W or lex builder was imported.
- All 33 gzip LRAT streams hash/byte-bound and converted to addition-only RUP (hints and deletions discarded), then verified by the parent-pinned drat-trim `-I -U`: exit 0, exactly `s VERIFIED` after carriage-return stripping, no feed error or guard trip. Two (26,2) streams (profiles 14 and 20) had 4 and 1 satisfied hints, respectively; both verify under additions-only RUP.
- Zero recorded Y and zero blocking clauses in all enumerated profiles: every first solve was UNSAT. No phase/moduli/completion exclusions are needed for these four cases.
- The uncorrected schema r1 matches **0/33** final CNF hashes; the differing pair order is an actual documentation-binding defect, corrected in r2 without changing any CNF or proof. The replay records the first differing clause.
- Controls: converter/checker smoke 6/6 as expected; a core-clause deletion and literal flip rejected by drat-trim; a J-core deletion rejected (an earlier redundant core deletion still verified and is recorded); wrong-e/profile hashes did not match. Peak sampled aggregate RSS 544,374,784 bytes, no guard trip.

## Mathematical imports and limits

The exclusion uses the previously reviewed base support lemmas, [Lemma 17](ame46-lower48-parent-verdict.md) (officer counting), Lemma 19 and J (officer-placement necessary conditions for arbitrary complex amplitudes), and realizable-support orbit-lex completeness. Both CLI families accepted the new mathematical lemmas with fixes ([Codex v4](ame46-v4-codex-review-v1.note.md), [Claude v4](ame46-v4-claude-review-v1.note.md)); the [v5 delta review](ame46-v5-codex-delta-review-v1.note.md) exposed the schema order and a late guard-reporting race. All four checked reports have `guard_tripped = null`; the replay independently recomputes their certification without trusting the worker's outcome boolean. W/Lemma 20 is e = 0 only and is not used here.

(24,0): the worker's proof-free exploration excluded all 158 profiles (not a certificate), but the proof run reached only 16 profiles before its 512 MiB run budget tripped. Its profile-0 proof alone was 471,421,610 compressed bytes; the full case was projected at about 1.2 GB. The lane has 519,184,384 bytes remaining under its frozen total-data reserve. The parent stopped this direction without a cap increase. Partial streams are retained, not an exclusion of the case.

Computer-assisted; not Lean-checked. No novelty claim. Trust includes the reviewed mathematical reduction, Python/base generator, drat-trim, compiler and hardware. No new bound follows from the four cases alone.

**FRONTIER: CORRECTNESS-ACCEPTED (four partial parameter exclusions); AME minimum-support gate remains open.**
