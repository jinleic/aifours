# AME(4,6) minimum support: every AME(4,6) state has at least 42 nonzero coefficients (parent record)

## Result (partial)

**Every AME(4,6) state, complex or real, has at least 42 nonzero coefficients in every product orthonormal basis.** The published bound was 38 ≤ s_min ≤ 60 (Pandya, arXiv:2610.16673v1, 2026-10-12, LF504–520: "Whether the gap between 38 and 60 can be closed is open"). The new lower bound is 42.

This is **partial progress** on the [frozen phys-2 target](../screening/phys-2-ame46-support-contract.json): the gate needs an explicit state with at most 59 terms or a complete lower bound of 60. No gate is met.

By-product of the same arguments: no AME(4,6) state has 33, 34 or 35 classical coefficients (modulus 1/6), with Tarry's theorem at most 32, and if s = 72 − t exactly then t is even.

Proof: lane `review/SUPPORT_LOWER42.r1.md` `54880341…2bad` and its revision [r2](ame46-lower42-parent-inputs-r2/review/SUPPORT_LOWER42.r2.md) `1db90164…1418` (r2 = r1 plus the listed review fixes).

## Proof outline

1. AME ⇔ all three 36 × 36 reshapings are unitary; local unitaries reduce every product orthonormal basis to the computational one.
2. Classical coefficients (modulus 1/6) are alone in their lines and form a code of minimum distance 3, so s ≥ 72 − t. Unitary support components have equal row and column counts; every non-classical component has excess e_K ≥ 0, e_K = 0 exactly for 2 × 2 blocks, and e_K ≠ 1.
3. If s ≤ 41 then t ≥ 31: t = 36 gives two orthogonal Latin squares of order 6 (Tarry); t = 35, 34, 33 contradict slice deficits; t = 31 leaves an odd number of rows to pair; t = 32 forces the non-classical support onto a 2⁴ subcube whose 8 points form an OA(8,4,2,2), i.e. one of ten parity sets (written Fourier classification).
4. For each parity set, three 2 × 2 blocks (one per reshaping) give phase congruences ≡ π whose signed sum is the zero form with an odd right side, a contradiction. Two written representatives and a written symmetry lemma (Lemma 11) cover all ten sets; the finite checks are cross-checks only in r2.

## Verification

| Evidence | Result | Limit |
|---|---|---|
| Codex CLI `gpt-6.1-sol`, complete review of r1 (math + verifier) | **ACCEPT-WITH-FIXES**, no fatal/major; two minors (false one-class symmetry sentence; say "orthonormal") ([note](ame46-lower42-codex-review-v1.note.md)) | Model review |
| Claude CLI `claude-opus-5-5`, no-tools review of r1 | **ACCEPT-WITH-FIXES**, no fatal; one MAJOR (the same false symmetry sentence plus an unproved invariance claim; theorem survives) and minors ([note](ame46-lower42-claude-review-v1.note.md)) | Model review |
| Codex CLI `gpt-6.1-sol`, delta review of r2 | **ACCEPT-WITH-FIXES**, no fatal/major; Lemma 11, written instance 2, the two-class reduction and the corollary checked; two wording minors ([note](ame46-lower42-r2-codex-delta-review-v1.note.md)) | Model review |
| Parent replay of the pinned finite verifier | fresh tree, byte-identical JSON and stdout, exit 0 ([receipt](ame46-lower42-parent-replay-v1/result.json)) | Cross-check |
| Parent independent checker | all 12,870 subsets, exactly 10 uniform binary OAs, 10 exact signed phase contradictions; coefficient, RHS and support corruptions rejected for the intended reasons ([script](ame46-lower42-parent-check-v1.py), [receipt](ame46-lower42-parent-check-v1.json)) | Cross-check |
| Parent reading | all 259 r1 lines; the r1→r2 diff; written instance 2 recomputed by hand (closed components, forms, zero sum, RHS −π) | — |

Dispositions: [r1 dispositions](ame46-lower42-review-dispositions.json); the r2 delta minors (wording "Fourier frequency weight"; semidirect-product docstring) are editorial and do not affect the proof.

## Priority and significance

Bounded screen: [record](ame46-lower-bound-priority-screen-v1.json). The matched baseline is Pandya's 38 (same day as two related real-state papers by Bruzda and by Hontarenko–Życzkowski, whose abstracts state no lower bound). A search miss is not novelty. **Significance: modest specialist partial improvement (38 → 42) in a crowded, very recent area.**

## Status

**FRONTIER: CORRECTNESS-ACCEPTED (partial lower bound s_min ≥ 42), 2026-10-17 PT; NOVELTY-UNCLEAR; not the frozen gate.** Imports Tarry's theorem only (case t = 36). Not Lean-checked.
