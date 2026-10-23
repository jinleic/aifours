## Hostile review: E2/E3 F-family couple theorem (01-couple-sets-and-k4-exclusion-v1.md, with erratum v1)

**Verdict.** Theorems A and B are correct for the explicitly defined family F, within the scope set by the governing erratum. I found **no FATAL or MAJOR defect.**

- **Method.** I re-derived every step by hand, exactly, from the supplied text. I used no tools or scripts, and no decimal value is used as a proof step. I did not use the FCLOSE candidate or the disclosed floating evidence. I did not recompute the stated SHA-256 digests, byte count or line numbering; line references follow the supplied numbering.
- **Still open before acceptance.** F-3 and F-4 below need repair. Both concern side statements; neither affects Theorems A or B.

### First-family findings, adjudicated

- **PASS verdicts and stated identities: all confirmed.** This covers:
  - γ−δ = φκ and A−B = φ²κ.
  - c²s² = 1/1200, gd = −1/20, ‖X‖ = ‖Y‖ = 1, X†Y = e²+4gd = 0.
  - The closed forms for A1…E2 and their ordering.
  - The Dist₁ gap (5+3√5)κ/150.
  - Δ = −2κ/15, (g·aa)²−(d·bb)² = κ/300, det = −(16/5)IΔ.
  - A(VH)J = (det H)^(−1)(AVJ)H, and the uniform A_(b,0).
- **MINOR 1 (L206):** confirmed.
- **MINOR 3 (L173–179, L177):** confirmed. Its side remark that Σ_t n(t) = 0 follows from W†W = I₂ is also correct, and, as the erratum says, not needed.
- **MINOR 2:** confirmed for the flatness part. **Its MUB-pair sentence, copied into erratum item 2, proves a true statement about the wrong planes** (see F-3).
- **One reason is misattributed.** The first family says "APA = D conj(P) D† because every element of Anti_Z is an involution." The identity is a direct computation: KPDK = conj(P)·conj(D), and conj(D) = D† for a diagonal unitary. Involutivity is what makes APA equal to the conjugation APA^(−1). The conclusion is unaffected.

### Per-claim verdicts (line numbers refer to 01-…-v1.md)

| Claim | Lines | Verdict |
|---|---|---|
| Lemma 1: φ, G(1)=√5, G(2)=−√5, cos(2πk/15) products, AB=κ², κ>2, (2+β)A±(2+α)B | 27–46 | PASS |
| Prop 2: W8 necessity from (H): character inversion for rows/columns/classes, Gram I/2, Anti_b couple maps, converse | 48–74 | PASS |
| Lemmas 3–5: U on the three bases, U³=−I, M-transport, Anti transport, D_w-invariance, eigenvectors, multiplicities | 77–100 | PASS |
| Lemmas 6–7: coordinates, radical branches, norms, A>B>0, x/y expansions, rank 2, U P_τ U† = P_τ | 101–130 | PASS |
| Lemma 8: all ten entries, six moduli, arrangement, positivity, order relations | 133–154 | PASS |
| Cor 9: Dist₁ invariance, class separation, non-constant distance-1 sequence | 155–163 | PASS |
| Lemma 10: Bloch obstruction, including conjugation and orientation | 166–179 | PASS; wording fixed by erratum 3 |
| Lemma 11, Cor 12a: shift exclusion, τ′=−τ exclusion, scalar stabilizer, 100 distinct planes | 180–191 | PASS |
| Lemma 12, Thm 12 (Z): Q conj(P_τ) Q† = P_(−τ), operator order DQ†, both directions, circle | 194–204 | PASS |
| Thm 12 (T, X) | 205–209 | PASS; notation fixed by erratum 1 |
| Frames, λ-action, 5 partners per basis | 210–213 | PASS; flatness parenthetical needs erratum 2 |
| Label invariance under WH/U; Thm B triangle | 215–221 | PASS |
| Side claims of flatness (title, L211, L224 "not used anywhere") | 1, 211, 224 | MINOR, resolved by erratum 2 |
| "does not contain the 30 MUB-pair planes" / "F excludes MUB-pair planes" | 15; JSON 45 | MINOR, **not resolved** (F-3) |
| "E in the circle Z^c Q" | JSON 45 | MINOR (F-4) |
| Outside F, Cor 14, mixed configurations, 1-RQLS(10) | 225–229 | Correctly left open; no dependency |

### Independent checks (exact)

**Coordinates and radicals (L27–46, L101–130).**
- Write ε = e^(iπ/15). Then:
  - ω²ζ²+ω = ε²+ε¹⁰ = γζ
  - ω²ζ³+ω = ε⁸+ε¹⁰ = δζ⁴
  - ωζ²+ω² = ε²²+ε²⁰ = δζ
  - ωζ³+ω² = ε²⁸+ε²⁰ = γζ⁴
  - (ζ−ζ⁴)(ω²ζ²−ωζ³) = (ε⁸+ε²²)−(ε⁴+ε²⁶) = β−γ
  - (ζ−ζ⁴)(ωζ²−ω²ζ³) = (ε²⁸+ε²)−(ε¹⁴+ε¹⁶) = α−δ
  - (ζ²−ζ³)(ω²−ω) = κ
- With Π v_(μ,s) = v_(μ,−s), these reproduce L103–104 exactly. Parity also gives a ⊥ b and a′ ⊥ b′, which L129 asserts without justification.
- c(1+√5) = e, because c²(1+√5)² = (3−√5)(6+2√5)/40 = 1/5.
- κ/√B = √A and κ/√A = √B. With these, the expansions give exactly L121–122, including the −iσ′·bb term in Y₂.

**Moduli table (L133–154).**
- I re-expanded all ten entries. They match L134–137 and depend only on σσ′, so the arrangement at L140–141 is right.
- Global checksum, independent of the entry expansions:
  - For a rank-2 projector with diagonal 2/5, Σ_(t<t′) |P_tt′|² = (2 − 4/5)/2 = 3/5.
  - The table gives 2(A1+A2) + 2(C1+C2) + (E1+E2) = 6/25 + 2φ/25 + (8−√5)/25 = 3/5.
  - This uses E1+E2 = 2R0² + 8c²s²[(2+β)B + (2+α)A].
  - It also uses (2+β)B + (2+α)A = 15φ, which follows from β² = 2+δ, α² = 2+γ, βγ = γ−φ and αδ = δ−φ.
- The order C1 < A2 < C2 < E1 < A1 < E2 is confirmed. The last gap is E2−A1 = (5−√5)/50.

**Dist₁ and shift exclusion (L155–163, L182–185).**
- Dist₁(+) − Dist₁(−) = [(6+4√5)κ − 2(γ−δ)]/150 = (5+3√5)κ/150 > 0.
- The distance-1 sequences (A1,C1,E2,C1,A1) and (A2,C2,E1,C2,A2) are not constant. Any a ≠ 0 generates Z₅, so a = 0.

**Bloch obstruction (L166–179).**
- The Bloch vectors are:
  - n(0) = (0, 2/5, 0)
  - n(1), n(4) = (Δ, r, ±2I), with Δ = −2κ/15 < 0 and I ≠ 0 in both classes
  - det = −(16/5)IΔ ≠ 0
- Ψ = KE is an antiunitary involution commuting with `P~`.
  - Its fixed set W ⊂ `S~` is a real form (W ∩ iW = 0).
  - The rows of a real-orthonormal basis of W are e^(−iθ_t/2) times a real row.
  - Their Bloch vectors therefore lie in the linear plane n₃ = 0.
- The paper's route only needs one U(2) frame change acting on all Bloch vectors by a single invertible linear map. Orientation does not matter on this route.
- The first family's alternative, det(R_H·diag(1,1,−1)) = −1, is also valid.

**Stabilizer, antiunitaries, operator order (L180–204).**
- If EP = PE and every |P_tt′| > 0, all diagonal phases of E are equal.
- A P_τ A = DK P_τ DK = D conj(P_τ) D† = (DQ†) P_(−τ) (DQ†)†.
- Conjugating by X^a Z^(−c′) X^(−a) = ζ^(ac′) Z^(−c′) gives E′ = X^a Z^(−c′) X^(−a) D Q†.
- Lemma 11 then gives a = 0, τ′ = −τ and D = λZ^(c′)Q. The converse holds.
- The WH phase convention does not matter: (θD_w)A(θD_w)^(−1) = θ²·D_w A D_w^(−1), and the circle absorbs θ². Also (λA)² = I.

**Transport and labels (L205–209, L216).**
- M = [[0,1],[−1,−1]] has det 1 and M³ = I. It maps L_Z → L_T → L_X → L_Z.
- U fixes each P_τ individually (L125). So U^(−k) D_w P_τ D_w† U^k = D_(M^(−k)w) P_τ D_(M^(−k)w)†, with the same τ.
- Labels are intrinsic (Cor 12a) and preserved by every WH/U transform used. The T- and X-flips are therefore flips of exactly the labels Theorem B uses.

**Frames (L210–213).**
- A(VH)J = (det H)^(−1)(AVJ)H.
- V ↦ AVJ is a bijection between the frames of the two planes; its inverse is V′ ↦ AV′J^(−1).
- |v†(AVJ)| = |v†V| for every V. Flatness only supplies the common value 2/5, and that is the sense in which L211 uses it.

**Theorem B (L215–221).**
- Prop 2(iii) gives C_(b(r,s))(S_r, S_s) ≠ ∅; this relation is symmetric because A² = I.
- Theorem A then gives τ_s = −τ_r for each couple.
- The triangle 00–01 (M_Z), 01–10 (M_T), 10–00 (M_X) gives τ_00 = −τ_00, a contradiction.
- No frame, phase, distinctness or flatness input is used.

### Findings and minimal repairs

**F-1 MINOR, L206 (first family; confirmed).** Erratum item 1 is adequate. Optionally, also state the X case explicitly (U², M^(−2)) or adopt the first family's uniform A_(b,0).

**F-2 MINOR, L1, L211, L224 (first family; confirmed).** Erratum item 2's flatness paragraph is correct and sufficient:
- The diagonal of P_τ is e²+e² at t = 0 and g²+bb²+d²+aa² = 2/5 elsewhere (L146).
- U maps β_Z → β_T → β_X → β_Z up to phases.
- D_w permutes each basis up to phases.

**F-3 MINOR, L15 and JSON L45; affects the last sentence of erratum item 2 (new).**
- **What the erratum proves.** It excludes pair-spans of two vectors of β_Z, β_X or β_T. That is true. But by the erratum's own reason (the diagonal would contain 0 and 1), those planes are not flat.
- **What L15 needs.** L15 cites the 30 MUB-pair planes as flat planes outside F ("whether *other* flat planes exist"). L225–226 treat them as W8 candidates that need Corollary 14.
- **Why these must be different planes.** Pair-spans of a designated basis fail Prop 2(i) immediately, so they would not need Corollary 14. The planes L15 means are pair-spans in the three complementary MUBs, the eigenbases of XZ^k for k = 1, 2, 3 (3 × 10 = 30).
- **The gap.** The packet asserts that F excludes these planes but never proves it.
- **The fix.** It follows in one line from Lemma 11. Replace the last sentence of erratum item 2 with:

> No plane spanned by two vectors of an eigenbasis of W ∈ {Z} ∪ {XZ^k : k ∈ Z₅} lies in F. Such a plane is W-invariant, and D_w† W D_w is a unimodular multiple of W, so W P_τ W† = P_τ would follow. For W = Z this contradicts Lemma 11 (E = Z is not scalar). For W = XZ^k it reads Z^k P_τ Z^(−k) = X⁴ P_τ X^(−4), contradicting Lemma 11 (a = 4 ≠ 0).

- This covers all six MUBs, so it is correct under either reading of "MUB-pair."
- **If L15 should also assert that the 30 planes are flat** (needed for "F is not all flat planes"), add:
  - The eigenvectors of XZ^k are 5^(−1/2)(ζ^(3kt²+lt))_t.
  - For k = 1, 2, 3 the quadratic coefficients are 3, 1, 4. These differ from 0 (β_X) and 2 (β_T).
  - So Lemma 1(a), together with G(4) = G(1) and G(3) = G(2) via r ↦ 2r, makes these vectors unbiased to β_Z, β_X and β_T.
- Otherwise, delete the parenthetical.

**F-4 MINOR, JSON L45 (new).**
- "other than E in the circle Z^c Q" mixes two parametrizations.
- With E := DQ† (L200, L227), the partners inside F are exactly E ∈ {λZ^c}, i.e. D ∈ {λZ^cQ}.
- E = Z^cQ instead gives Z^cQ P_(−τ) Q† Z^(−c), which is not in F. Lemma 11 would force Q ∝ Z^m, but 2t² is not affine in t.
- **Repair:** "other than E ∈ {λZ^c : |λ| = 1} (equivalently D = EQ ∈ {λZ^cQ})". No effect on any proof.

**Nits (no mathematical effect).**
- **L57:** the condition "if |v†V|² = 2/5" only fixes the common value; the paired rows always have equal norms.
- **L190:** "rearranging the diagonal factor" is unnecessary. P_τ = X^aZ^c P_τ′ Z^(−c)X^(−a) gives the displayed equation directly.
- **Symbol reuse:**
  - F means both the Fourier matrix and the family.
  - A and B are scalars, antiunitaries, and (for B) a class label.
  - I is both the identity and the imaginary part at L170.
  - r is both a couple index and a Bloch coordinate (L169).
- **Numbering:** the labels Lemma 12, Theorem 12 (Z), Theorem 12 (T, X) and Corollary 12a collide, so "Theorem 12" at L11 names two results.
- **Erratum spacing:** as supplied, erratum lines 3–9 lack spaces between words (e.g. "D_(M^-1 w)*andD_(M^-1 wprime)*"). If the file itself reads this way, restore the spacing.

### Scope

- **Certified:** Theorems A and B for the explicit 100-plane family F, under (H) exactly as written at L49–51. Whether (H) matches the programme's W8 definition cannot be checked from the supplied text.
- **Not certified, still OPEN:**
  - any classification of flat planes;
  - W8 solutions with any plane outside F, including mixed configurations;
  - Corollary 14;
  - unrestricted 1-RQLS(10).
- **No proof weight:** the FCLOSE candidate and the floating evidence (scope freeze L35–37).
