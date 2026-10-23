# AME(4,6) support lower bound s ≥ 48: parent verdict

## Result

**Every AME(4,6) state, with arbitrary complex amplitudes, has at least 48 non-zero coefficients in every product orthonormal basis.** This extends the accepted bound s ≥ 46 ([verdict](ame46-lower46-parent-verdict.md)). With Pandya's upper bound 60 (arXiv:2610.16673v1; not re-reviewed here), 48 ≤ s_min ≤ 60. **Partial progress; it does not decide the frozen phys-2 gate** (minimum support 59 versus 60).

Proof: [SUPPORT_LOWER48.r2.md](../../../../physics/evidence/six-lane-20261016/ame46-support/review/SUPPORT_LOWER48.r2.md) (SHA-256 `70daac01707158b2842159dbdc6713afa33e541c51f100a91034fdf4d432f60e`), a correction of r1 (`04575705…9f95`), with the guard [erratum](../../../../physics/evidence/six-lane-20261016/ame46-support/review/ENGINE_V2_GUARD.erratum-1.md). It imports LOWER42 r2 and LOWER46 r2. New written ingredients:

- **Lemma 17 (officer counting).** For every integer α, f(α) = κ₂ − ακ₁ + C(α+1,2)·t ≥ 0, with κ₁ = 6Σ|V_i| − 4h and κ₂ = Σ_{i<j}|V_i||V_j| − 6h. It excludes t = 29 entirely and seven further deficit profiles.
- **Lemma 18 (binary code).** Profile {4,4}{2⁴}³ at t = 28 is impossible.

Six cases are computer-assisted: (26,0), (27,2), (28,2), (28,3), (30,4), (30,5). Completeness now uses true supports, not CNF symmetry. The H-image of a genuine support is genuine, its lex-least image satisfies the generator lex constraints, and the certified final UNSAT forces it to be a recorded, excluded solution.

The first-position lex-prefix shorthand in r2 is made explicit in a parent [clarification](ame46-lower48-lex-prefix-clarification-v1.md): substitute q₀ = true and drop its tautological clause, not merely its literal. The checked code and all certificate hashes are unchanged.

## Evidence

| Obligation | Evidence (parent-held) |
|---|---|
| 37 load-bearing final UNSATs | Parent replay: each final CNF regenerated with matching SHA-256 and RUP-verified from the gzip LRAT **additions only** by the parent drat-trim (`-I -U`), including the one stream with satisfied hints; 6 gzip pipeline controls passed ([replay](ame46-lower48-parent-replay-v1/result.json)) |
| CNF = written schema | All 37 final CNFs regenerated from the written r2 schema (generators, lex chains, numbering, blocking, composition) without importing the lex engine: 37/37 SHA-256 match ([receipt](ame46-lower48-lex-from-text-v1.json)) |
| 137 load-bearing phase certificates | Checked independently: genuine closed 2 × 2 components, zero weighted form, odd weight sum (same replay) |
| Profile completeness and guards | Every deficit profile for each h enumerated independently and matched; all eight reports EXCLUDED with no guard trip (same replay) |
| Written lemmas, case table | Codex CLI `gpt-6.1-sol` ([note](ame46-lower48-codex-review-v1.note.md)) and Claude CLI `claude-opus-5-5` ([note](ame46-lower48-claude-review-v1.note.md)): both ACCEPT-WITH-FIXES. One MAJOR in both: the false syntactic-symmetry claim, which the realizable-support repair resolves. Codex ran exhaustive lex, counter, α and binary-code controls |
| r2 delta | All findings dispositioned; theorem and case table unchanged; all 37 proof and CNF hashes in r2 match the replay ([delta check](ame46-lower48-r2-parent-delta-check.json)) |

## Limits

- Computer-assisted. It trusts drat-trim, Python, the pinned base generator (bound and controlled for LOWER46) and the phase-certificate check. It is not Lean-checked.
- The 94 non-load-bearing proof streams (completion, moduli and component evidence) were not re-verified by the parent; Lemmas 17 and 18 make them unnecessary.
- No priority or novelty claim. Search misses are not novelty.

**FRONTIER: CORRECTNESS-ACCEPTED (partial result); not a gate.**
