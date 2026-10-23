# rules-v1 erratum v1

Written 2026-10-18, finished at or before 09:57 PDT by the host clock; the freeze time is in `evidence/proof-v2.sha256`. `rules-v1.md` (cb86c168…390f) stays frozen and unchanged. This erratum corrects commentary and wording only. **No formal lemma statement used by the engine changes, and the engine code does not change.** The corrections come from the Codex written-math review `R/sun-coset5-written-proof-codex-v1` (84b3dadd…2002).

## E1. L3 commentary on M-S Cor 3.11 (Codex MINOR 2)

**Old text.** rules-v1, the paragraph that begins "M-S Cor 3.11". It said that, in this lane, Cor 3.11 is an instance of K1 + L3 because "τ ≤ τ_max forces a link at the vertex shared by the two equal edges".

**Correction.**
- Take α_UV = 1 and α_UW = α_VW = p with p ∈ {2, 3}. The products of the two α's at each vertex are p at U, p at V and p² at W.
- So τ_max = p. In Core(5), τ_min = p unless the opposite vertex is special for p.
- When τ = p, K1 gives links at **U and V**, the two endpoints of the α = 1 edge. It gives no link at W, the vertex shared by the two equal edges.
- Lemma K at U, with S = {V, W}, then gives 1 + p ≤ 3, which fails for p = 3. That is the (1,3,3) exclusion.
- The formal rules and the code (link test at the apex where (T2) is attained) were already correct; only the sentence was wrong.

## E2. Control C4 wording (Codex MINOR 3)

**Old text.** "(C4) Mutating one label (an α value or the E2/E3 status) in a certificate must break that certificate for the stated reason."

**Correction.**
- An arbitrary single-label mutation need not invalidate a witness. For example, changing an edge outside the witness triangle leaves a T-witness valid.
- The meaningful control mutates a **selected** label that is known to invalidate that exact witness, and checks that it does. This is `code/controls_v2.py`, part (A).
- The bulk count in engine-v1-run1 (634,470 mutants, 94,067 of which break the original witness) is descriptive only.
- Independent re-checking of every certificate (C4 re-verification, and the separate checker `core5_check_v2.py`) remains mandatory.

## E3. M-S Lemma 4.4 "misprint" (Codex additional note)

**Old text.** rules-v1 L3 ("M-S Lemma 4.4: the first bullet should read α(U_2,U_3) ≠ 2") and README §2, which called this a misprint.

**Correction.** The primary M-S text already states α ≠ 2. The apparent "= 2" was an artefact of extracting text from the PDF, which dropped the "≠" glyph. It was not a misprint in the paper, and no correction to M-S is needed.

## E4. Lemma R (R5) justification

**Change.** proof-v1 derived (R5) from (R4), Sun's statement on the whole set S_C. proof-v2 instead applies the k = 2 case directly to the two named pieces. See the fix map in `proof-v2.md`.
