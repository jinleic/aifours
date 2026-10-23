# Balanced ternary design BTD(14,18;7,1,9;7,4): parent verdict

## Result

**BTD(14,18;7,1,9;7,4) does not exist.** No 14 × 18 matrix over {0, 1, 2} has exactly seven entries 1 and exactly one entry 2 in every row, every column summing to 7, and inner product 4 between any two distinct rows. Repeated columns (repeated blocks) are allowed, so simple designs are excluded as well.

[Frozen contract](../screening/info-2-btd14-18-contract.json). Rosin (arXiv:2501.17725v1, Table 1) lists this instance first among the Handbook's smallest open BTDs; his May 2025 follow-up does not solve it, and the CPro1 definition file lists it first in `OPEN_INSTANCES`. This is an **explicitly listed open finite instance**.

## Proof

Final written proof [r2](btd14-18-parent-inputs-r2/nonexistence-proof-r2.md), SHA-256 `8769c218ca6ccd80beddbd2b13b2fb189095b513db9dc70dcc1a9a14c948a847`; reviewed [r1](btd14-18-parent-inputs-v1/nonexistence-proof-r1.md) `fd508ffb…87c0f` is unchanged. The parent read the full [r1→r2 diff](btd14-18-parent-inputs-r2/nonexistence-proof-r1-to-r2.diff): exactly the five editorial clarifications of the Claude review plus status/change-map lines; no equation or number changed.

1. With G = MᵀM and H := 63I − 9G + 28J, the design identities MMᵀ = 7I + 4J, M1 = 9·1, Mᵀ1 = 7·1 give H² = 63H and H1 = 0, so 63xᵀHx = |Hx|² ≥ 0 and Cauchy–Schwarz holds for H. A column with t twos has H_jj = 28 − 18t, so t ≤ 1: there are 14 type-1 columns (H_jj = 10) and 4 type-0 columns (H_jj = 28). Off-diagonal entries are ≡ 1 (mod 9).
2. Next to a type-1 column the entries lie in {−8, 1, 10}; the two row identities give exactly two entries 10 and five entries −8. An entry 10 between type-1 columns forces equal H-columns (E); two −8 entries from one type-1 column force 10 between the other two (F).
3. **Complementary-minor identity.** For any four columns S, Sylvester's determinant identity on the complementary 14 × 14 integer submatrix N gives 729·det(N)² = 7¹⁰·det H[S].
4. A type-1 column a has five −8 entries but only four type-0 columns exist, so some type-1 b has H_ab = −8. Then every type-1 column c has H_ca + H_cb = 2, and some type-1 u has H_ua = H_ub = 1. For a type-0 column c, Cauchy–Schwarz leaves H_ca + H_cb ∈ {−7, 2}. The value −7 forces det H[{a,b,u,c}] ∈ {3645, −2187}: −2187 is negative, and 3645 = 729·5 would give det(N)² = 5·7¹⁰ ≡ 2 (mod 3). So all 18 columns satisfy H_ca + H_cb = 2, contradicting Σ_c H_ca = Σ_c H_cb = 0 (0 = 36).

The method is Connor's (1952) determinant argument, here with B − V = 4. It is the same mechanism as the accepted [BTD(12,15) verdict](btd12-15-parent-verdict.md), so the two instances are one contribution.

## Verification

| Evidence | Observed result | Limit |
|---|---|---|
| Parent independent stdlib exact arithmetic | 27 checks pass: actual 14 × 14 inverse and determinant 9·7¹⁴, the D4 factor, H² coefficients, complete value set {−8, 1, 10}, row counts (2, 5), Lemma F, type-1 sums, type-0 sums {−7, 2}, all six mixed minors, the integer mod-3 exclusion ([script](btd14-18-parent-arithmetic-v1.py), [receipt](btd14-18-parent-arithmetic-v1.json)) | Arithmetic of the written steps |
| Parent replay of the worker's exact checker | byte-identical, all_ok ([receipt](btd14-18-parent-checker-replay-v1/parent-result.json)) | Replay |
| Codex CLI `gpt-6.1-sol`, hostile review of r1 | **ACCEPT**, no findings; independently re-derives every step, the coefficient and all six minors, and notes the 729 cancellation is done in ℤ before reducing mod 3 ([note](btd14-18-codex-hostile-review-v1.note.md)) | Model review, not peer review |
| Claude CLI `claude-opus-5-5`, complete review of r1 | **ACCEPT**, five editorial minors, no fatal/major; second derivation of the minors via adj B ([note](btd14-18-claude-complete-review-v1.note.md)) | No-tools model review |
| **Lean 4 kernel proof** of the explicit unrestricted statement | worker root `BTD14.Audit.root`; **parent replay**: source, toolchain and direct Mathlib pins match, parent forbidden-token scan clean, rebuild passes, a **parent-authored statement** over `Fin 14 → Fin 18 → ℤ` is accepted at exactly the root's type, a parent BTD(3,3) positive control holds, four parent statement mutations (Λ = 5, K = 8, two 2s per row, 15 rows) fail with type mismatch, `leanchecker --fresh` exit 0 (325.8 s), axioms `propext`, `Classical.choice`, `Quot.sound` only ([result](btd14-18-lean-parent-replay-v1/parent-result.json)) | One Lean 4.34.1 kernel implementation; read-only prebuilt Mathlib cache; not Comparator |

Review findings are [dispositioned](btd14-18-review-dispositions.json). The worker's CP-SAT and kissat witness searches are supporting attempts only; no solver result is used.

**Contract mapping.** The written mathematical contradiction plus the parent-replayed Lean kernel proof of the explicit unrestricted statement satisfies the nonexistence clause's "equivalent exact machine-checked proof" route, as stated in the contract itself.

## Priority, significance and trust limits

- [Priority audit](btd12-15-priority-audit.md) (covers both instances): no construction or nonexistence proof found; Rosin's 2025 papers, the CPro1 repository and the Kaski–Östergård data page (V ≤ 10 scope) leave it open. Access holes: Handbook VI.2 text, Greig's 2002/2003 chapter, Billington–Robinson 1983. A search miss is not novelty clearance.
- **Significance: modest specialist.** Together with BTD(12,15;6,2,10;8,6), two of the four Handbook BTD instances Rosin still lists as open are settled by one classical method. No general theorem is claimed.

## Status

**FRONTIER: CORRECTNESS-ACCEPTED — reviewed written proof plus parent-replayed Lean kernel proof of the explicit unrestricted statement; NOVELTY-UNCLEAR. The frozen info-2 BTD(14,18;7,1,9;7,4) target is met (2026-10-17 PT): an explicitly listed open instance is settled, with modest significance shared with BTD(12,15).**

No commit, push, publication or external contact was authorized.
