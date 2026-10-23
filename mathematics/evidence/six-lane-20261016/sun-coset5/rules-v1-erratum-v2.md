# rules-v1 erratum v2

The host-clock freeze record is in `evidence/proof-v3.sha256`. `rules-v1.md` (cb86c168…390f) and `rules-v1-erratum-v1.md` (f1e51b37…bc56) stay frozen and unchanged.

**What this erratum does not change.** No formal lemma statement used by the engine changes, and no code changes.

**Sources.**
- The Claude written-math review `R/sun-coset5-written-proof-claude-v1.note.md`.
- The Codex engine/bridge audit `R/sun-core5-engine-codex-v1.note.md` (d87212a9…b3d1).

## E5. L1 remark on gcd(α, r_z) (Claude F-10)

**Old text.** "gcd(α, r_z) = α exactly when α = 2 and z = E2, or α = 3 and z = E3; otherwise it is 1."

**Correction.** "For α ∈ {2, 3}, gcd(α, r_z) = α exactly when (α = 2 and z = E2) or (α = 3 and z = E3), and otherwise gcd(α, r_z) = 1. For α = 1 the quotient α/gcd(α, r_z) is 1 in every case."

The formula for τ_min is unaffected.

## E6. L0.8 and R1: citations and the status of Prop 4.5 (Claude F-2, F-7, F-9)

**Zhu citation.** Zhu's results are now cited as **Theorem 1.1 (k = 3, 4)**. M-S Props 4.2 and 4.3 follow from it at once.

**M-S Lemma 4.4.** Its second bullet derives "3 | r_1" by applying M-S Lemma 3.10a outside that lemma's hypotheses, which require a common a. This is a load-bearing defect in the imported proof.

**Correction.** proof-v3 §2 gives a complete, self-contained proof of Prop 4.5 with the patch:
- T = 4r_1r_2r_3τ;
- 12r_2r_3 | T, so 3 | r_1τ;
- τ ≤ 2, because |U_2(U_1∩U_3)| = τ|G|/4 ≤ |G|/2;
- hence 3 | r_1.

That proof uses only "multiple of |G|/4" for the double-coset counts (F-8). It fixes "harmonic" to mean: there exist g_i such that the cosets g_iU_i are pairwise disjoint (F-9).

## E7. Control C4 and the engine-v1-run1 demos (Codex MAJOR wording; Codex MINOR)

**C4 is not independent verification.** C4 in engine-v1-run1 is a **shared-code witness recheck**:
- it reuses the engine's τ, link, p_bounds, N2 and fibre helpers;
- it does not reopen the certificate file;
- it ignores the recorded bounds and totals.

**The checker is lane evidence only.** `code/core5_check_v2.py` comes from the same lane, the same rules and the same author. It is not a replay independent of the parent.

**Controls do not gate.** All controls (C1–C4, controls-v2, controls-v3) only record observations. None of them gates the run.

**Mutation demos.** rules-v1's expectation that "mutating one label must break that certificate" is invalid as written; in run1, only 94,067 of 634,470 mutants break their certificate. It is replaced by **selected intended-reason demonstrations**, which are part (A) of controls-v2/v3. In controls-v3, all six selected mutations break their certificates as intended.

**Demo labels in engine-v1-run1.** Two of the named targeted demos fired a different rule from the one in their name:

| demo name | rule that actually fired |
|---|---|
| "K_star_1111_CorMS3.9" | T |
| "P_star_3333_N1" | K |

## E8. Record of an exploratory post-freeze attempt (not evidence)

**What was run.** At about 10:05–10:20 PDT, an exploratory, unfrozen eval-kernel cell tried a strengthened vertex form of Lemma R. The idea was an LP over right U_v-cosets, solved with a dual grid enumeration. The aim was to see whether that form alone refutes all patterns.

**Outcome.** The cell hit the 900 s eval timeout and produced no result. No file was written, and nothing in the proof depends on it.

**Timing caveat.** The start time above is an estimate. The governing host-clock records are the eval tool's own logs.
