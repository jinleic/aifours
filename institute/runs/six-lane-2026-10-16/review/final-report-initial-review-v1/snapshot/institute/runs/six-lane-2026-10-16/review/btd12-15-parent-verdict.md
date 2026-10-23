# Balanced ternary design BTD(12,15;6,2,10;8,6): parent verdict

## Result

**BTD(12,15;6,2,10;8,6) does not exist.** No 12 × 15 matrix over {0, 1, 2} has exactly six entries 1 and exactly two entries 2 in every row, every column summing to 8, and inner product 6 between any two distinct rows. Repeated columns (repeated blocks) are allowed, so simple designs are excluded as well.

[Frozen contract](../screening/info-2-btd12-15-contract.json). Rosin (arXiv:2501.17725v1, Table 1) lists this instance among the Handbook's smallest open BTDs; his May 2025 follow-up solves seven other BTDs, not this one; the CPro1 definition file still lists it as open. This is an **explicitly listed open finite instance**.

## Proof

The final written proof is [r2](btd12-15-parent-inputs-r2/nonexistence-proof-r2.md), SHA-256 `37795ae73be939e38bb628c0e05cba5ed95aba6e89c9dad4c706a420e3725dc0` ([pin](btd12-15-parent-inputs-r2/manifest.json), [r1→r2 diff](btd12-15-parent-inputs-r2/r1-to-r2.diff); r1 `837a26ea…` unchanged).

1. With G = MᵀM and H := 40I − 5G + 24J, the design identities MMᵀ = 8I + 6J, M1 = 10·1 and Mᵀ1 = 8·1 give H² = 40H and H1 = 0. Hence xᵀHx = |Hx|²/40 ≥ 0. Column j with c_j twos has H_jj = 24 − 10c_j, so c_j ≤ 2; off-diagonal entries are ≡ −1 (mod 5).
2. Counting twos gives n₂ = 9 + n₀ ≥ 9 columns with two 2s (diagonal 4).
3. Row relations Σ_k H_jk = 0 and Σ_k H_jk² = 40H_jj at a type-2 column force at most four other entries equal to 4. Between type-2 columns H_jk ∈ {−1, 4}, and H_jk = 4 makes the two H-columns equal, so "H_jk = 4" is an equivalence relation with classes of size ≤ 5.
4. **Connor-type lemma.** For any three columns S, the matrix determinant lemma applied to the complementary 12 × 12 integer submatrix N gives det(N)² = (2²⁸/25)·det H[S], so every 3 × 3 principal minor of H is a perfect square.
5. Three classes would give the minor det(5I − J₃) = 50, not a square; so there are exactly two classes and n₂ ∈ {9, 10}, leaving a column with one 2.
6. For a, b in different classes and such a column k, det H[{a,b,k}] = 210 − (4x² + 2xy + 4y²) with x, y ∈ {−6, −1, 4}, which takes only the values −150, 50, 150, 200. None is a non-negative square. Contradiction.

The method is classical: Connor (Ann. Math. Statist. 1952) proved the same perfect-square fact for block designs with b − v = 3, and McCarthy–Vanstone extended it to (r, λ)-designs. Its application to this BTD and the closing case analysis are the new parts found by this run.

## Verification

| Evidence | Observed result | Limit |
|---|---|---|
| Parent independent exact calculation of the r1 case analysis | consistent ([receipt](btd12-15-parent-check-v1.json)) | Arithmetic of the written steps |
| Parent mixed-minor table for the r2 closure | determinant values {−150, 50, 150, 200}, none a square ([receipt](btd12-15-parent-mixed-minor-v1.json)) | Same |
| Parent replay of the worker's r2 exact checker | byte-identical output, all_ok ([receipt](btd12-15-parent-r2-replay-v1/parent-result.json)) | Replay |
| Codex CLI `gpt-6.1-sol`, hostile review of r1 | ACCEPT-WITH-FIXES: one indexing minor in a step that r2 removes; no fatal/major ([note](btd12-15-codex-hostile-review-v1.note.md)) | Model review, not peer review |
| Claude CLI `claude-opus-5-5`, complete review of r1 | ACCEPT; editorial minors; recommended the short closure adopted in r2 ([note](btd12-15-claude-complete-review-v1.note.md)) | Model review, not peer review |
| Codex CLI `gpt-6.1-sol`, review of final r2 | **ACCEPT**, no findings; independently recomputes 2²⁸/25, the integer-square step, the class bound and the nine-case table ([note](btd12-15-r2-final-codex-review-v1.note.md)) | Model review |
| **Lean 4 kernel proof** of the explicit unrestricted statement | worker formalization of r2 (`BTD12.Audit.root`); **parent replay**: pins match, parent forbidden-token scan clean (no `sorry`, `native_decide`, `ofReduceBool`, axioms, options), rebuild passes, a **parent-authored statement** over `Fin 12 → Fin 15 → ℤ` is accepted at exactly the root's type, four parent mutations of the statement (Λ = 5, K = 7, three 2s, 13 rows) fail with type mismatch, `leanchecker --fresh` exit 0 (291 s), axioms `propext`, `Classical.choice`, `Quot.sound` only ([result](btd12-15-lean-parent-replay-v2/parent-result.json)) | One Lean 4.34.1 kernel implementation; Mathlib from the read-only prebuilt cache; not Comparator. [v1](btd12-15-lean-parent-replay-v1/parent-result.json) is retained: its driver's case-sensitive "type mismatch" match stopped it before the kernel step |

All review findings are [dispositioned](btd12-15-review-dispositions.json).

**Contract mapping.** The nonexistence clause asks for a complete unrestricted formulation with a correctness argument plus an independently checked DRAT/LRAT or equivalent exact proof, and a second route or a mathematical contradiction. The Lean development states the unrestricted matrix condition directly (bound to a parent-authored restatement by the kernel) and is replayed by the parent with a fresh kernel; the reviewed written proof is the mathematical contradiction. The plain-encoding SAT run is supplementary; no UNSAT result from it is used.

## Priority, significance and trust limits

- [Priority audit](btd12-15-priority-audit.md): no construction or nonexistence proof found; Rosin's 2025 papers and the CPro1 repository list the instance as open; the Kaski–Östergård enumeration covers V ≤ 10 only. Access holes include the Handbook VI.2 text and Greig's 2002/2003 chapter. A search miss is not novelty clearance.
- **Significance: modest specialist.** One explicitly listed finite existence case is settled by a classical method; no asymptotic theorem, general BTD classification or new method is claimed. The same mechanism may decide the companion open instance BTD(14,18;7,1,9;7,4), which would be part of the same contribution.

## Status

**FRONTIER: CORRECTNESS-ACCEPTED — reviewed written proof plus parent-replayed Lean kernel proof of the explicit unrestricted statement; NOVELTY-UNCLEAR. The frozen info-2 BTD(12,15;6,2,10;8,6) target is met (2026-10-17 PT): an explicitly listed open instance is settled, with modest significance and no broad breakthrough claim.**

No commit, push, publication or external contact was authorized.
