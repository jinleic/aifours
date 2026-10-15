# Referee report: generic paired three-super-soliton obstruction (pinned snapshot)

**What I did.** I read every file in the snapshot. I re-derived §2 and §3 by hand and recomputed the following against `results/replay.json`: Φ₄ to Φ₇, R211 at n=4 and n=5, the n=4 tau coefficients, the wave-vector determinant, the P-value table and the n=30 tail gap (leading digits and the value mod 1000). I also read `code/replay.py` line by line.

**What I could not do.**
- I did not run `replay.py`. The only tools were Read, Glob and Grep, so the n=8..29 certificate values are checked only as far as noted below.
- I did not verify the SHA-256 values in `manifest.json`, for the same reason.
- I did not read anything outside the snapshot, including Hietarinta 1987, Li–Lou 2008 and Wang–Yang–Tang–Chen 2024.

`★ Insight ─────────────────────────────────────`
- The whole super-structure reduces to the body because the parameter ideal I=(ζ₁…ζ_r) is preserved by every operator in S_yP. Keeping θ is what keeps the D_yP equation alive. Setting θ=0 as well would delete it, which is what the f=xⁿy negative control shows.
- The restricted lift F=f(x,y+θζ,t) makes the converse hold too: a body solution exists exactly when a single-fermion super solution exists. For n≥4 the theorem is therefore a bosonic theorem. The super framing only adds the elementary projection.
`─────────────────────────────────────────────────`

## Findings

There are no fatal or major findings. The independent derivations (A)–(F) below are the basis for that.

1. **[minor] The interpretation is stated too strongly.** Locations: `RESULTS.md:268-269` ("standard generic all-pattern interpretation"), `RESULTS.md:305` ("Exact 2018 hypothesis/criterion addressed") and `README.md:18`.
   - The 2018 text (`source/wang-tang-liang-2018.txt:814-816`) names only "the criteria that the existence of three super-soliton solutions". It gives no ansatz, no quantifier and no seed pattern.
   - **Fix:** say "a Hietarinta-type generic interpretation fixed here". Add the argument that makes this choice principled rather than arbitrary: read literally, the existence criterion is satisfied for every n (G=1 linear superpositions, `RESULTS.md:90-91`, and the §5 lift). A genericity quantifier is therefore needed for the test to tell any n apart.

2. **[minor] Two restricted amplitude families for odd n are neither covered nor named.** Locations: `RESULTS.md:76-79` and `RESULTS.md:257-260`.
   - The first family is b_i=a_i, i.e. F=G. Here P_nτ·τ≡0, and the system collapses to the single-τ equation S_yP_nτ·τ=0. At n=3 this is the SUSY-BLMP equation (2018 eq. (26), `wang-tang-liang-2018.txt:506-517`).
   - The second family is b_i=−a_i, the mKdV-kink type.
   - Both are proper closed subsets of the two-amplitude family, so generic failure says nothing about them. They are plausibly what many readers mean by "the" three-soliton of an odd-n system.
   - **Fix:** list both explicitly among the exclusions. Note that the Wang–Yang–Tang–Chen 2024 paper cited at `STATUS.md:100` is exactly the F=G sub-case at n=5.

3. **[minor] Genericity: one logical step is missing and the result can be stated more strongly.** Locations: `RESULTS.md:81-84` and `RESULTS.md:242-248`.
   - (a) Lines 83–84 make nonvanishing denominators part of the *definition*. It should be a proof step: intersect the family's open set with the nondegenerate locus. That locus is nonempty and Zariski-open because the witness shows each factor is a nonzero polynomial.
   - (b) "for even n" at line 245 is an unnecessary restriction. By the same argument, the F–F–G sub-branch also fails generically for odd n.
   - (c) The proof gives more than it states. R211 = a₁²a₂b₃·l₃·Φ_n(k)/[l₁₂₃·P(−κ₁₂₃)·P(−κ₁₃)], and Φ_n depends only on (k₁,k₂,k₃).
     - So every nondegenerate square-free F–F–G solution has k on the hypersurface Φ_n(k)=0, whatever l and the amplitudes are.
     - This excludes families on any nonempty open set, Euclidean or Zariski, or on any positive-measure set. No regularity of the family in its parameters is needed.
     - It also shows that constraints on l or on the amplitudes alone cannot rescue the pattern, which sharpens `RESULTS.md:92-93`.

4. **[minor] The code evidence is described as stronger than it is.** Locations: `RESULTS.md:289-292` and `RESULTS.md:306`; `code/replay.py:145-155` and `code/replay.py:214-221`.
   - In the projected controls, every non-body term carries a ζ. The asserted identities therefore hold for *any* implementation that never deletes a ζ. They cannot detect sign errors in the odd derivatives or the θ-diagonal.
   - Only the n=2,3 unprojected lift checks (`replay.py:207-213`) and the three hand assertions (`replay.py:132-136`) are sign-sensitive.
   - "Arbitrary explicit nilpotent dressings" (`replay.py:215`) is in fact one fixed dressing.
   - **Fix:** add an unprojected off-shell control, e.g. F=1+e^{η+θζ₁}, G=1 with w≠−kⁿ. The exact result is (ζ₁+θl)P(κ)e^η, which must be matched including its ζ₁ coefficient. Alternatively, compare against the paper's (A1) expansion at n=2. Then reword the claim.

5. **[minor] The n=2,3 boundary controls can be upgraded to identities** (`RESULTS.md:277-280`). Φ≡0 holds on the *whole* F–F–G branch at n=2 and n=3 (derivation (E)). Adding this proves that the R211 obstruction vanishes identically there, rather than at one point. The full residuals would still be single-point checks.

6. **[minor] The claim that F–F–G "suffices" can be made sharp** (`RESULTS.md:88-89`).
   - Pure patterns are linear: all-F forces f_U=g_U=0 for |U|≥2 and G=1.
   - The map σ: (F,G)(x,y,t) ↦ (G,F)(−x,y,−t) sends solutions to solutions, since P F'·G' = (P F·G)∘σ and D_yP F'·G' = −(D_yP F·G)∘σ. It also exchanges F-type data (k,l,w) with G-type data (−k,l,−w).
   - So for even n, F–F–G is the only non-linearizable generic pattern, up to symmetry and relabeling.

7. **[minor] Novelty screen** (`STATUS.md:113-117`).
   - The 2018 paper says the bosonic n=3 pair was "rediscovered … by Hietarinta [16]" (`wang-tang-liang-2018.txt:127-128`). [16] is J. Math. Phys. 28, 2094, Hietarinta's search for mKdV-type equations passing the three-soliton test. His search space therefore demonstrably contains this paired family, so the small-n bosonic failure is a concrete prior-art risk, not a generic one.
   - Li–Lou 2008, which is the source of the D_y lift, is not recorded as read.
   - Zero OpenAlex citers (`STATUS.md:88-90`) is a low-confidence result for a 2018 CPB article and should be cross-checked.
   - **Fix:** quote the "rediscovered" sentence and flag the bosonic ingredient as possibly classical for small n.

8. **[minor] A simpler, code-independent tail proof is available** (`RESULTS.md:203-219`). Using |B|,|C| < 4ⁿ−3ⁿ and D,E > 5ⁿ−4ⁿ−2ⁿ, I get Φ_n<0 for all n≥7, with only n=4,5,6 needing exact evaluation (derivation (D)). This would replace the 26-value certificate with three hand-checkable integers.

9. **[nit] The overlap with Delisle–Jaouadi is stated incompletely** (`STATUS.md:68-81`).
   - The one literal intersection is this: odd n with F=G=τ, after swapping x↔y, is the Eq. (50)-type equation with P(Y,T)=Yⁿ+T. Delisle–Jaouadi treat only n=3 (`delisle-jaouadi-2609.14372v1.txt:656-672`).
   - The lift relation ζ_i=l_iζ (`RESULTS.md:286-288`) is the y-analogue of Carstea's relation (their Eq. (46)). It is therefore a "weak" solution in their terminology.
   - Their Eq. (51) appears typo-damaged, since (p_m−p_n) cancels. Do not use it as a numerical check.

10. **[nit] The §7 "Observed" block** (`RESULTS.md:317-324`) paraphrases the output. The actual print strings are at `replay.py:263-269`. Paste the real output verbatim or label the block as a summary.

11. **[nit] Typing and proof phrasing.**
    - `RESULTS.md:18` should read F_even∈C^∞⊗A_even and F_odd∈C^∞⊗A_odd.
    - In the proof at `RESULTS.md:106-110`, say three things explicitly:
      - π_ζ=ε⊗id is an even superalgebra homomorphism.
      - Δ:θ₁,θ₂↦θ is a well-defined homomorphism, since all the relations map to θ²=0.
      - With θ-monomials written leftmost, ∂θᵢ acts only on the θ factor.

      The result is then visibly independent of the left/right-derivative convention. It also extends to any supercommutative coefficient algebra with an even body map.

12. **[nit] Housekeeping.** `README.md:67` and `pins.json` refer to `review/` and to PDFs that are not in the snapshot. `replay.py:12` imports `itertools` but never uses it.

## Independent derivations

**(A) Projection.** All the operators ∂_{x,y,t}, ∂θᵢ, θᵢ· and Δ preserve I and act as themselves on the ζ-free subalgebra. Hence π_ζ∘L = L∘π_ζ. Since f and g have no θ, ∂θᵢ kills f(1)g(2). This gives:

```
π_ζ(S_yP F·G) = Δ[(θ₁∂y₁ − θ₂∂y₂) P f(1)g(2)] = θ · D_yP f·g
```

This holds with:
- shared ζ's,
- separate θ₁ and θ₂,
- even nilpotent dressings of any kind,
- localisation at even elements with invertible body.

No correction can cancel the coefficient of θ, because Λ(θ)⊗C^∞ is free on {1,θ}.

**(B) Recursion.**
- The 2×2 determinant is −2·l_U·P(κ_U)·P(−κ_U). ✓
- Taking l₁₃×(P eq) − (D_yP eq) gives g₁₃·P(−κ₁₃) = −l₃a₁b₃·P(κ₁−κ₃)/l₁₃. ✓
- At level 123, only (1,23) and (2,13) survive. This gives g₁₃₂₃-free elimination g₁₂₃·P(−κ₁₂₃) = −(l₂₃X+l₁₃Y)/l₁₂₃, which reproduces (3.3). ✓
- At (2,1,1), the terms (123,1), (12,13) and (13,12) vanish because g₁, f₁₂ and g₁₂ are zero. The D_yP coefficient is −l₂₃·R211; the replay's ratio 560640/(−56064) = −10 is consistent with this.
- **Odd n:** the determinants contain no amplitudes, so the specialization b₁=b₂=a₃=0 commutes with solving. The extra general-family terms all vanish at that point. ✓

**(C) The witness.** All six arguments in Φ have positive k (6, 3, 3, 5, 5, 2), so Φ_n contains no (−1)ⁿ terms. The checks:

| n | Value | Matches replay.json |
|---|---|---|
| 4 | Φ₄ = 28,508,160 − 29,180,928 = −672,768 | ✓ |
| 5 | Φ₅ = −241,920,000 | ✓ |
| 6 | Φ₆ = −51,881,195,520 | ✓ |
| 7 | Φ₇ = −8,735,982,796,800 | ✓ |
| 4 | R211 = −56064/5423 | ✓ |
| 5 | R211 = −313600/1573 | ✓ |
| 4 | g₁₂₃ = 1752/37961, f₁₃ = −23/168, g₁₃ = 161/87, g₂₃ = 16/5 | ✓ |
| 2 | f₁₂₃ = −7/60 | ✓ |

The determinant 4ⁿ+11·2ⁿ−26 is correct, and every entry in the P-table is correct.

**(D) Tail.**
- Every inequality in Lemma 3.1 checks out, including that both sides are monotone. The gap is ≈3.5331·10⁴¹ and is ≡177 (mod 1000), matching the stored integer.
- A tighter, hand-checkable version: Φ_n<0 whenever (5ⁿ−4ⁿ−2ⁿ)²·(4ⁿ−2ⁿ⁺¹) ≥ 6ⁿ·(4ⁿ−3ⁿ)².
  - n=7: 6.122e13 ≥ 5.642e13.
  - n=8: 6.861e15 ≥ 5.842e15.
  - n≥9: the left side divided by 96ⁿ increases with n and is ≥1 at n=9 (7.462e17 ≥ 96⁹ = 6.925e17), while the right side divided by 96ⁿ stays below 1.

**(E) Φ vanishes identically at n=2 and n=3.**
- n=2: Φ = −8k₁k₂k₃(k₁+k₃)(k₂+k₃)·[(k₂−k₁)+(k₁−k₂)] = 0.
- n=3: Φ = −27k₁k₂k₃²(k₁−k₃)(k₂−k₃)(k₁+k₃)(k₂+k₃)·[(k₁−k₂)+(k₂−k₁)] = 0.

**(F) Code.**
- The bitmask sign rules for products, the left derivative and the θ-diagonal are all correct.
- `super_pn` is correct for even F and G, which the code asserts.
- The Euler/binomial reconstruction imports nothing beyond SymPy.
- The lift identity D_θF = (ζ+θ)·f_y(·, y+θζ, ·) is correct.

`★ Insight ─────────────────────────────────────`
- At n=4 the two products in Φ cancel to within about 2.3%. That is why a crude tail bound cannot reach small n, and why n=4–6 need exact evaluation.
- Φ does not depend on l, so the obstruction is purely a statement about the x-wave numbers. y-data enters only through l₃ and the denominators.
`─────────────────────────────────────────────────`

## Verdicts

- **Projection theorem:** correct. It holds with arbitrary even nilpotent corrections, shared odd parameters and separate θ₁/θ₂, and no correction can cancel the body constraint.
- **All-degree obstruction:** correct. The determinant, the uniqueness argument, R211, all signs and the odd-n specialization check out. Lemma 3.1 is valid, and a hand-only proof exists (D).
- **Generic-family implication:** correct. It establishes failure on every nonempty open set, not just at the chosen witness. It actually proves the stronger hypersurface confinement in finding 3c.
- **Code evidence:** correct and adequate as supplementary evidence. I found no sign, projection or encoding errors. The lift proves only what is stated. The projected controls are weaker than claimed (finding 4).
- **Source and novelty scope:** the quotes and page references are accurate, and the symmetry hypothesis is correctly kept separate. No theorem in Delisle–Jaouadi covers or contradicts the F≠G paired result; their §VI lists two-function systems as open. The only overlap is the F=G, odd-n reduction, which they treat at n=3 only, consistent with the 2018 paper. Novelty is appropriately not claimed. The prior-art risk from Hietarinta's mKdV-type paper [16] should be made explicit (finding 7).

**Overall theorem verdict: correct.** Theorem 4.1 holds exactly as stated. The package as a whole is correct-with-fixes, but every fix (findings 1–12) is expository or about scope. No mathematical step remains.
