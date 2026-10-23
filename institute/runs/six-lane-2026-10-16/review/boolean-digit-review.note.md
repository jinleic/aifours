## Verdict: ACCEPT-WITH-FIXES

I found no mathematical error in Claims 1–4 or Corollary 5. The corrected premise, 16 | W_Dq(z) for every z, is true, and it is all the proof uses. Beyond that wording, one real issue remains: the hypothesis s ≠ 0 is missing (fix 1). It limits what the result covers; it is not a logical flaw in the derivation.

## Required fixes

**1. State s ≠ 0 explicitly.** This applies to the second sentence of Claim 2, the "in particular" part of Claim 4, and all of Corollary 5.
- If s = 0, there are no coordinates with s = e9, s^⊥ is not a hyperplane, and D, q, σ, v are undefined.
- This case is not empty. s_i = wt(f·x_i) mod 2, which is the ANF coefficient of x^{[9]∖{i}} in f. (The x^{[9]} coefficient is 0 because wt f = 256.) So s ≠ 0 ⟺ deg f = 8.
- The branch deg f ≤ 7 is therefore not covered. In the target it forces d0 ≡ 0, T even, 8 | W and max|W| ≤ 24. Any later argument must handle or exclude it separately.

**2. Prove 16 | W_Dq instead of asserting it.**
- Polarizing on the coset a9 = 1 gives Dq(y+y') + Dq(y) + Dq(y') + Dq(0) = (y,0)ᵀB(y',0).
- So Dq has degree ≤ 2, and its polar form is B|_{s⊥}, the same as D's.
- For such a function g on F2^8 with polar rank 2h: W_g(z)² = 2^8·Σ_{u∈rad}(−1)^{g(u)+g(0)+z·u} ∈ {0, 2^{16−2h}}.
- Since h ≤ 4, W_g(z) ∈ {0, ±2^{8−h}} ⊂ 16ℤ.
- The old wording "|W_Dq| ≥ 16" is false whenever rank D < 8: Parseval then allows only 2^{2h} < 256 nonzero values. The proof never needs that wording.

**3. Conventions and wording.**
- (a) Write T ≡ N_a (mod 16), and define d_k as the bits of the least nonnegative residue. Both d3 = [W<0] and the carry e depend on this choice.
- (b) In Claim 2, "resulting rank B" must mean the rank of the normalized B, which is rank(B|_{s⊥}). The unnormalized rank can be 2 larger. State why it is translation-invariant: aᵀ(csᵀ+scᵀ)b = 0 for a, b ∈ s^⊥.
- (c) In Claim 1, "substitution preserves degree ≤ 8" says nothing on F2^8. The actual content is:
  - the weight parity equals the t1⋯t8 coefficient;
  - only the eight linear parts reach that coefficient;
  - det(LᵀβL) does not depend on L (since det P² = 1) or on c.
- (d) κ is not defined in the prompt. I verified W_Jq(z) ≡ 4κ (mod 8) **for every z ∈ F2^8**, taking κ := [rank D = 8] = det(β|_{s⊥}) = Pf(B|_{s⊥}). State it with that definition and that quantifier.

## Remark: the mod-8 congruence does not depend on the cap

This affects how Corollary 5 can be used. For any balanced f with s ≠ 0, q = 1 + 2Dq + 4Jq − 8σ + 16e(·,1), and the extra term 16·H8 e(·,1) is ≡ 0 (mod 16). The parity of wt σ comes straight from Claim 1, because σ is a digit. So W_Jq ≡ 4κ (mod 8) holds without the cap.

I confirmed this by an independent route:
- deg Jq ≤ 4 on F2^8, so W_Jq(z) ≡ −2·wt Jq (mod 8) for every z. (wt(g+ℓ) ≡ wt g mod 4, since deg(gℓ) ≤ 5.)
- From XOR(b) ≡ Σb − 2e2(b) (mod 4): wt g ≡ 2·Σ_{I⊔J=[8], |I|=|J|=4} g_I g_J (mod 4).
- By Claim 1, the quartic part of Jq is Σ_{I⊆[8]} Pf(B_I) y^I; monomials containing a9 drop to cubic on a9 = 1.
- Σ_{I⊔J=[8]} Pf(B_I)Pf(B_J) = 3·Pf(B_[8]), because each perfect matching of [8] splits in 3 ways.

So the only part of Corollary 5 that needs the target is the exact identity 4W_σ = 128v + W_Dq + 2W_Jq, together with σ = [W(·,1) < 0]. The congruence alone is not a constraint on target functions. Generic balanced controls should satisfy it.

## Statements I checked by hand

- **Setup:** W = 512δ0 − 512 + 4N_a and T ≡ N_a (mod 16). By Lucas, d_k = e_{2^k}((a·x)_{x∈X}) mod 2, with degree ≤ 2^k.
- **ANF coefficients:** for |I| = r, the monomial a^I arises only from bijections S→I. Its coefficient is Σ per V_{I,S} = Σ det V_{I,S} = Σ det² = det(V_I V_Iᵀ) = det β_I, by Cauchy–Binet.
- **d0 and d1:** d0 = a·s. I computed the polar form of d1 directly from e2(u+v) = e2(u) + e2(v) + Σ_{x≠y} u_x v_y. It equals β + ssᵀ = B, which is alternating.
- **Pfaffian identity:**
  - det(B_I + ssᵀ) = det B_I + sᵀadj(B_I)s holds over any commutative ring.
  - The adjugate of an even-order alternating matrix is symmetric. Its diagonal entries are determinants of odd-order alternating matrices, hence 0, so sᵀadj(B_I)s = 0.
  - With det = Pf² = Pf over F2, this gives det β_I = Pf B_I.
  - Hand check: for 4×4 matrices, J + 11ᵀ has det 1 = Pf J.
- **Affine hyperplane:** Möbius inversion gives weight parity = top coefficient. Cauchy–Binet with LᵀV then gives det(LᵀβL).
- **Translation:**
  - s and |W| are fixed, and W → (−1)^{a·c}W.
  - β → β + scᵀ + csᵀ, because 256·ccᵀ = 0.
  - Setting c_i = B_{i9} zeroes column 9 and leaves B_[8] unchanged.
  - Consistency check: Claim 1 for f and its translate requires #{a∈s^⊥, a·c=1 : N_a ≢ 0 mod 8} to be even. It is, because d1∨d2 has degree ≤ 6 on a 7-flat.
- **Claim 3:**
  - |T| ≤ 7, d3 = [T<0], and T = d0 + 2d1 + 4d2 − 8d3.
  - e is an integer, and e = 0 ⟺ T ∈ [−8, 7].
- **Inverse Walsh constants:**
  - HT = 128F and H(d) = 256δ0 − W_d/2.
  - The δ0 coefficient is 256(1+2+4−8) = −256, and W_{d0} = 512δ_s. This reproduces 32F + 64δ0 + 64δ_s + W_{d1}/4 + W_{d2}/2 and the −4He carry.
  - Spot check on f = 1+x0 (s = 0, β = 0, all d_k ≡ 0, e = −8δ_{e0}): both sides equal 512δ0.
- **Claim 4:** β|_{s⊥} = B|_{s⊥}, and the determinant of an 8×8 alternating Gram matrix equals [rank = 8]. The cap is genuinely needed: for f = 1+x0, h = e0, c = 1, the count is 1 but det = 0.
- **Corollary 5:**
  - H8 q = (HT(·,0) − HT(·,1))/2 = 128v, and the δ0 terms cancel (256 + 256 + 512 − 1024 = 0).
  - I re-derived the identity by splitting Claim 3's identity along a9; the δ0 and δ_s terms cancel because s = e9.
  - W_σ(z) ≡ 2·wt σ (mod 4) for all z, so reducing mod 16 gives W_Jq ≡ 4·wt σ (mod 8).

## Not checked

- I ran no computations and did not reproduce the controls.
- I did not see the source definition of κ or any later argument that uses these results.
- I make no claim about existence or novelty.

This is a model review, not human peer review.
