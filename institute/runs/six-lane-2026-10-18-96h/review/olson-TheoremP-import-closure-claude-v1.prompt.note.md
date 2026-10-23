# Theorem P review (written only, from the pasted text; frozen 2026-10-21T04:14:28-0700)

**Counts: FATAL 0 · MAJOR 0 · MINOR 3.** All three are expository and none affects correctness. I found no mathematical flaw.

References: **P-LF n** is a physical line of `proof-theoremP.md`; **S-LF n** is a line of the scope file. The pasted material contained no errata, so none were applied. I did not recompute any hashes.

## Theorem verdict

Theorem P as literally stated is **CORRECT and unconditional**. This means P-LF27–28 read under the conventions of P-LF10–23, which matches the statement in S-LF5. Every load-bearing step in P-LF32–93 re-derives.

The proof uses only three ingredients:
- the group law at P-LF11;
- Fermat's little theorem;
- the Boolean-box lemma, which is proved in the text at P-LF81–85.

The Chevalley–Warning theorem itself is never invoked. No computation, prime-power result or Remark is used.

## Claim-wise verdicts

| # | Claim | Source | Verdict |
|---|---|---|---|
| C0 | Group law, ordered product, independence from the cut, restoration to original order | P-LF10–23 | Correct (MINOR-1, MINOR-2) |
| C1 | Pairing, parameters, M = (F−1)+Σ⌊n_t/2⌋ ≥ 3p−2 | P-LF32–43 | Correct |
| C2 | Injectivity; S = ∅ ⇔ (u,m) = 0 | P-LF45–50 | Correct |
| C3 | Size formula; size is even and ≤ 4p−1 | P-LF52–54 | Correct |
| C4 | Signs c_t, total sign +1, telescoping, linear V and β_t | P-LF56–73 | Correct (MINOR-2, MINOR-3) |
| C5 | Z, deg Q ≤ 3(p−1) < M, Fermat indicator, box lemma, nonzero solution | P-LF75–88 | Correct |
| C6 | Size exactly 2p; product is the identity | P-LF90–93 | Correct (restoration: MINOR-1) |

## Independent re-derivation

**C0 — group law and cut restoration.**
- Associativity: both bracketings of three factors give (v + ev′ + ee′v″, ee′e″). The identity element is (0,+1).
- Ordered product, by induction from (A,E)(a,e) = (A+Ea, Ee):
  (a_1,e_1)⋯(a_k,e_k) = (Σ_j ε_j a_j, ∏_j e_j), where ε_j = ∏_{l<j} e_l.
- Restoration:
  - Write the original word as AB, cut just after some reflection. This needs F ≥ 1. The rotated word is BA and ends with that reflection.
  - Take any index set T, and let P_A and P_B be the ordered products of the selected letters in A and in B.
  - The rotated product is P_B P_A. The original product is P_A P_B = P_B⁻¹(P_B P_A)P_B.
  - So one product is the identity exactly when the other is, and |T| does not change.
- The cut leaves F and N unchanged and only shifts (n_1,…,n_F) cyclically (P-LF22–23). So the hypothesis does not depend on where the cut is made.
- A pair in X_1 may straddle the original end and start. This is harmless, because the transfer works for any T.

**C1 — parameter count.**
- M = (F + Σ⌊n_t/2⌋) − 1 ≥ 3p − 2.
- The pairs are disjoint and each lies inside a single gap.
- Any pairing within a gap would work, since every letter in a gap gets the same weight.

**C2 — injectivity.**
- For t = 1..F−1, u_{t+1} = u_t ⊕ [f_t ∈ S].
- Pairs are selected all-or-nothing, so m_π = [π ⊆ S] ⊕ u_{t(π)}.
- u_{F+1} := 0 is a definition, not a constraint, so all 2^M points are admissible.
- Hence the map is injective and S(0) = ∅, so x ≠ 0 implies S(x) ≠ ∅.

**C3 — evenness.**
- Over ℤ, Σ_{t=1}^F (u_{t+1} − u_t) = u_{F+1} − u_1 = 0, and every nonzero term is ±1.
- So the number of colour changes is even.
- |S| = (number of changes) + 2·(number of selected pairs) is therefore even.

**C4 — signs, telescoping, linear V.**
- The selected reflections before a letter of X_t, or before f_t itself, number Σ_{s<t}(u_s ⊕ u_{s+1}) ≡ u_1 + u_t ≡ u_t (mod 2). By C0, that letter's coordinate is weighted by c_t.
- The total sign is (−1)^{#changes} = +1.
- On Boolean values, [u_t ≠ u_{t+1}]·c_t = u_{t+1} − u_t. This is an identity in ℤ, so no division in ℤ_p is needed.
- Abel summation with u_1 = u_{F+1} = 0 gives Σ_{t=1}^F (u_{t+1}−u_t)y_t = Σ_{t=2}^F u_t(y_{t−1}−y_t). I checked this by reindexing for F ≥ 2; for F = 1 both sides are 0.
- For pairs, [m ⊕ u](−1)^u = m − u when u ∈ {0,1}.
- The u-terms from pairs in gap 1 vanish because u_1 = 0. Collecting terms gives exactly the formula at P-LF70–71:
  V = Σ_{t≥2} β_t u_t + Σ_π x_π m_π.
- V has no constant term, singletons never enter, and the product is the identity exactly when V(x) = 0.

**C5 — degree bound, box lemma, nonzero solution.**
- On Boolean values a + b − 2ab = a ⊕ b, so Z(x) = |S(x)| in ℤ.
- With u_1 = u_{F+1} = 0 substituted, deg V ≤ 1 and deg Z ≤ 2. So deg Q ≤ 3p − 3 < 3p − 2 ≤ M. The inequality is strict even when M = 3p − 2.
- By Fermat, 1 − a^{p−1} equals 1 if a = 0 and 0 otherwise, for a in F_p.
- Box lemma:
  - The signed sum is linear in Q, so it is enough to treat monomials.
  - By pigeonhole, a monomial of degree < M misses some variable x_j. Higher exponents are allowed, and no multilinearisation is needed.
  - Flipping coordinate j is a fixed-point-free involution. It reverses the sign (−1)^{|x|} and leaves the monomial's value unchanged, so the sum vanishes.
- Here |x| is the Hamming weight of the parameter vector, not |S(x)|.
- Let Sol be the set of x with V(x) = 0 and Z(x) ≡ 0 (mod p). Then Σ_{x∈Sol}(−1)^{|x|} = 0 in F_p.
- The point 0 is in Sol and contributes +1. If Sol were {0}, the sum would be 1 ≠ 0. So Sol contains some x ≠ 0.

**C6 — exact size.**
- 0 < |S(x)| ≤ N ≤ 4p−1, |S(x)| is even, and p divides |S(x)|.
- The positive multiples of p below 4p are p, 2p and 3p. Since p is odd, p and 3p are odd, so |S(x)| = 2p.
- The product is the identity by C4, and it transfers to the original order by C0.

## Boundary cases

- **F = 1.** Every step still holds: there are no u parameters, f_1 is never selected, V = Σx_π m_π and Z = 2Σm_π. However, the hypotheses then cannot all hold. In general they force F ≥ 2p−1:
  - Σ⌊n_t/2⌋ ≤ (N−F)/2 ≤ (4p−1−F)/2.
  - So 3p−1 ≤ F + (4p−1−F)/2, which gives F ≥ 2p−1 ≥ 5.
  - The cases F ≤ 2p−2 are therefore vacuous. The proof does not rely on this.
- **F = 0.** This is excluded by P-LF17, and P says nothing about it.
- **n_t ∈ {0,1}.** Such a gap has no pairs. A singleton is a rotation (sign +1) and is never selected.
- **N = 4p−1.** This bound is load-bearing because it rules out |S| = 4p.
- **Odd p.** Oddness is used only in Step 6; Fermat and the box lemma hold for every prime.
  - For p = 3: M ≥ 7 > 6, and the size must be 6.
  - For p = 2 Step 6 would fail, but p = 2 is excluded.
- **V identically zero.** This can happen, for example when every rotation letter is 0 and all y_t are equal. Then Q = 1 − Z^{p−1} and the degree bound still holds.

## Findings (all MINOR)

**MINOR-1 — restoration to original order is only implicit (P-LF14–23, P-LF27–28, P-LF90–93).**
- **Issue:** The symbol w is reused for the rotated word. Step 6 draws its conclusion about the rotated word without citing P-LF14–15. The fact that the hypothesis does not depend on the cut is only implicit in P-LF22–23.
- **Consequence:** None mathematically; C0 closes the gap. A reader who takes the theorem as "in original index order" (S-LF5) has to supply the conjugacy step.
- **Repair:**
  - Name the rotated word w′ = BA.
  - State that F, N and Σ⌊n_t/2⌋ do not depend on the cut.
  - Add to Step 6: "the same 2p letters, read in w's order, have product P_A P_B = P_B⁻¹(P_B P_A)P_B = (0,+1)."

**MINOR-2 — ordered-product formula not stated (P-LF59–61).**
- **Issue:** The phrases "multiplied by c_t" and "contributes c_t y_t" rely on the product formula from C0, which the text never states.
- **Consequence:** None; it is a one-line induction from P-LF11.
- **Repair:** State the formula together with the step (A,E)(a,e) = (A+Ea, Ee).

**MINOR-3 — degree and notation precision (P-LF72, P-LF78, P-LF82–88).**
- **Issue:**
  - "Degree 1" and "degree 2" should read "≤ 1" and "≤ 2", because V can be identically zero.
  - |x| (Hamming weight) and |S(x)| share notation.
  - P-LF88 chains an integer equality with a congruence.
- **Consequence:** None; P-LF79 uses only the upper bounds.
- **Repair:**
  - Write ≤ for both degrees.
  - Write wt(x) for the Hamming weight.
  - Write "|S(x)| = Z(x) ≡ 0 (mod p)".

## Separation of judgments

- **Correctness:** No error in P-LF8–93.
- **Completeness:** The proof is complete for the stated theorem once the two one-line additions (MINOR-1 and MINOR-2) are made. There is no missing premise, no circularity and no unresolved dependency, so nothing remains conditional.
- **Process:**
  - I recomputed no hashes, ran no computation and did not use the brute-force scripts mentioned in the header.
  - I did not treat the status label at P-LF3–6 or the earlier review history at S-LF3 as authority.
  - This is one independent written review. It is not Lean or human verification.
- **Priority and novelty:** Not assessed.
- **Computation and out-of-scope material:** Remarks P-LF95–109 receive no verdict. This includes the composite-sharpness claim, the D10 data, the mixed-modulus falsity claim and the conditional prime-power extension. The first sentence of Remark 1 is a direct instance of P (F = N = 3p−1, all n_t = 0), but it was not a review target.

**Not established by this verdict:**
- ordered Olson for D_{2p};
- words that fail P's hypothesis;
- composite or prime-power moduli;
- sharpness;
- any approval of the research target or runtime.
