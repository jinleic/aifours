# Olson reflection half: Theorem K0* and Theorem RED — parent verdict v1

Parent at 2026-10-18T04:52:05-07:00: **CORRECTNESS-ACCEPTED as written partial results at the exact scopes below.** This is not a gate. REFL(p) and the reflection half of INV*(p) remain **open** (residual REFL-RES(p)); the rotation half and ordered Olson for D_2p are untouched.

## Accepted statements

- **Theorem K0\*** (`proof-K0star-r2.md`, sha256 `6681676e4f80018e792c7117ce9fc524a31aeb397c35880f57468ada9c0396e1`; r1 `99a8f2e0…9488` preserved). For every prime p ≥ 5, every avoider w of length 4p−2 over D_2p whose rotation letters all lie in one set {ρ_x, ρ_−x}, x ≠ 0, and with κ(w) := p−1−Σ⌊l_i/2⌋ = 0 has every maximal cyclic reflection run constant. The sum runs over the **maximal constant reflection blocks** of w. Imports: Theorem P (accepted), EGZ / Lemma AR, and the parent-accepted GRX/PM* as the accepted overlay of GR0. Davenport-alpha is listed but unused (Claude m4).
- **Theorem RED** (`proof-RED-r2.md`, sha256 `c4e7697f0f691980e19ef3332a1e2c6b0dbdc76ba268e87c32eb563f4d3fd3d7`; r1 `fa6c5054…bb3` preserved). Assume the accepted RGR imports (I1)–(I4) at their stated scopes, plus K0*. Then **REFL(p) ⇔ no avoider in RES_<(p) with κ ≥ 2.** REFL(p) is the frozen README definition (`reflection/README.md` L17–19): every such avoider has every maximal cyclic reflection run constant, with no κ and no inherited condition. The parent checked this against Claude findings m5/7, so the converse is the trivial direction. RES_<(p) is the class of G-words with at least one genuine empty run, all maximal constant blocks odd, every rotation run pure or empty, and B < κ.

## Reviews (two CLI families; advisory)

| Reviewer | Target | Disposition | Note sha256 |
|---|---|---|---|
| Codex gpt-6.1-sol | K0star-r1 + RED-r1 | ACCEPT-WITH-FIXES, 0 FATAL / 0 MAJOR / 5 MINOR | `311bdaccfe40425370d9cc4be2e9a8742d8f40705364a4e4af76aa98ab008a8b` |
| Claude claude-opus-5-5 | K0star-r2 | ACCEPT-WITH-FIXES, 0 / 0 / 6 MINOR | `79e6f65008161f0efc79477d606bfbaa6ac4ba089048a1e3538ce6449e8a9bf1` |
| Claude claude-opus-5-5 | RED-r2 (K0star-r2 lemmas given) | ACCEPT-WITH-FIXES, 0 / 0 / 7 MINOR | `56928f1c2d614d986a50073c8ef0ebe9a88f4dbf32e8edcc3317187856522e6d` |

Failed Claude attempts are preserved. v1 hit a provider session limit (receipt `2f117551…1216`). v2, the same 184 KB prompt, ended TIMEOUT_NO_VERDICT at 2400 s (receipt `c03c0081…3496`). The review was then split into smaller prompts over snapshot [v2 manifest](olson-reflection-review-v2/manifest.json) (`ec446354…d366`).

## Parent checks

1. **r1→r2 diff** (parent `diff`): only the marked local fixes for Codex MINOR 1–5. FUS's second inclusion was corrected to Spec(σ_u^(l'+l)) ⊆ Spec(σ_v^(l')σ_u^l). PM0 now requires k ≥ 2. The maximal-decomposition bookkeeping is restricted to R ≥ 1. SING's count is max(0, q−1). F3's domain was fixed. No formula, case or conclusion changed.
2. **Independent finite aids, not premises.** Parent code, no worker code (`olson-reflection-reduction-parent-v1/`):
   - [aid v1](olson-reflection-reduction-parent-v1/RESULT-aid-v1.json) (`2d91a2380c88bf8ce41b8b45c22a8813ce0c9341d87f4c1c94bbda2b0911ddc3`; script `7ac306d5…3ff2`), PASS.
     - Lemma H0 against raw subset DP: 67,544 words at p = 5 and 7, lengths 14–26, 257 avoiders (78 with empty runs), **0 mismatches**.
     - The printed r1 FUS second form fails in 744 instances; the corrected form, the first form and SL fail in none.
     - TR (44,913 checks) and SL on words (11,969): exact in both directions. PM0 (150) and FUS (37): one-way avoidance preserved.
   - [aid v2](olson-reflection-reduction-parent-v1/RESULT-aid-v2.json) (`bc1470e9753105099adf101d7d03211f8866441842b16352c002009920dc523f`; script `c6595675…2684`), PASS. Targeted κ = 0 search from shapes with genuine empty runs: 236 (p = 5) and 49 (p = 7) κ = 0 avoiders found, **none** with an empty run, as K0* predicts.
3. **Hand check of the K0* Step 5 sums** (k = o_F + e_F, R = 2p − o_F):
   - C1a: 1 + (R+k−1)/2 = p+1.
   - C1b: (R−(k−2))/2 + (k−1) = (R+k)/2 = p+1.
   - C2a and its mirror: 1 + (R+k−2)/2 = p+1.
   - C2b: (R−(k−3))/2 + (k−2) = (R+k−1)/2 = p+1.
4. **Reviewer agreement.** Both families independently re-derived GR0/H0 (sign, parity, endpoints), BC′ with the boost, CH, the P1–P4 process and its exits. Each found the termination order (κ, g, k) and terminal-class completeness correct.

## MINOR dispositions

- Codex 1–5: applied in r2 (verified above).
- Claude K0* m1–m6 and Claude RED 1–7 are citations, undischarged automatic hypotheses ((V), o_F ≥ 1, (P)), wording ("no use of FUS changed"), stale r1 citations, and the overstated P4 κ bookkeeping. Each reviewer states that none changes a formula, case or conclusion, and the parent concurs. Required: documentation-level r3 files (new versions with a fix map). This acceptance covers r2's mathematics read with those fixes.

## Scope and open items

- Open: **REFL-RES(p)**, no avoider in RES_<(p) with κ ≥ 2, for every p. Sub-results B0S (B = 0, k ≤ p) and MXG (B ≥ 1, k ≤ p) are under separate review, and their acceptance is not implied here.
- REFL(5) has a prior finite proof (README L47). It is not a premise here and was not rerun.
- No Lean formalization. Finite aids are not premises.
