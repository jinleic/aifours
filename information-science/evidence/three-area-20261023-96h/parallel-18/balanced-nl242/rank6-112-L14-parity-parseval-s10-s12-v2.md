# Balanced NL242 (3,112) at L = 14 — a parity–Parseval lemma excludes s = 10, reduces s = 12 to ΣΣ = 0 with G = +1, and excludes s = 14 with ΣΣ = 0 and G = +1

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 08:38:02 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed, with no machine check and no formal, kernel or novelty claim. No program was run; all arithmetic was done by hand.

**Scope.** This is the successor to `rank6-112-L14-partial-reduction-v1.md` (fc201185…2050), which stays unchanged. It covers the residue type (polar rank 6, weight 112) at L = 14 only. **L = 14 is still NOT excluded**; the floor stays L ≥ 14. The type, the (24,24,2) gap and the original problem remain OPEN.

## 0. Setting (as in fc201185)

- Σ ⊆ F_2^6 is the set of s distinct imbalanced small-value cosets, with signs g(x) = ±1.
- The zero-slice function is h_0 = φ(Σ_{x∈Σ} g(x) z_x), where φ(y) is the residue of y mod 3 taken in {−1, 0, 1}. The multilinear polynomial for φ in `rank6-112-erratum-and-L10-exclusion-addendum-v1.md` (520f1484) is the unique multilinear interpolation of this map on {±1}^s; it was checked by hand for s ≤ 3.
- Put Ψ(ξ) := Σ_{x∈Σ} g(x)(−1)^{x·ξ}. Then h_0(ξ) = 0 ⟺ 3 | Ψ(ξ), and N_0 = #{ξ ∈ F_2^6 : 3 | Ψ(ξ)}. The formula N_0 = (64/3)[1 + (−1)^s 2^{1−s} Σ_k (−3)^{k/2} A_k] of 520f1484 is the cube-root-of-unity filter applied to this count.
- At (3,112) with L = 14: wt(h_0) ≤ 14, so N_0 ≥ 50. Also |P∖Σ| ≤ (14 − s)/2, and dim aff(P) = 6 by Theorem M(a).

## 1. Lemma PP (parity–Parseval)

Let G := Π_{x∈Σ} g(x) and τ := Σ_{x∈Σ} x ∈ F_2^6.

**(a)** Ψ(ξ) = s − 2w(ξ), where w(ξ) := #{x ∈ Σ : g(x)(−1)^{x·ξ} = −1}, and (−1)^{w(ξ)} = G·(−1)^{τ·ξ}.

**(b)** Σ_ξ Ψ(ξ)² = 64s, by Parseval, since the points are distinct.

**(c)** Let τ′ ≠ 0, let H := τ′^⊥ be a hyperplane, and let c ∈ F_2^6. If Ψ ≡ 0 on c + H, then Σ is a union of pairs {y, y + τ′} with g(y + τ′) = −(−1)^{τ′·c} g(y), and so τ = (s/2)·τ′.

*Proofs.*

- (a) Take the product of the s signs.
- (c) Let g̃ := g·1_Σ. For every y,
  Σ_{ξ∈c+H} Ψ(ξ)(−1)^{y·ξ} = Σ_x g̃(x)(−1)^{(x+y)·c}·32·[x + y ∈ H^⊥ = {0, τ′}] = ±32[g̃(y) + (−1)^{τ′·c} g̃(y + τ′)].
  This vanishes for all y, which gives the pairing and the sign rule. ∎

**Consequence.** If τ ≠ 0, the map ξ ↦ τ·ξ is balanced, so exactly 32 ξ have w(ξ) even and 32 have w(ξ) odd. If τ = 0, the parity of w is the constant given by G.

## 2. Theorem P10: s = 10 is impossible at L = 14

When w is even, Ψ ≡ 2 (mod 4), so Ψ ∈ {±2, ±6, ±10} and 3 | Ψ iff |Ψ| = 6. When w is odd, Ψ ∈ {0, ±4, ±8} and 3 | Ψ iff Ψ = 0.

- **τ ≠ 0.** 32 of the ξ have w even. At most 14 ξ overall have 3 ∤ Ψ, so at least 18 of these 32 have |Ψ| = 6. Then ΣΨ² ≥ 18·36 = 648 > 640 = 64·10. ✗
- **τ = 0, G = +1.** Every w is even, so at least 50 ξ have |Ψ| = 6, and ΣΨ² ≥ 1800 > 640. ✗
- **τ = 0, G = −1.**
  1. Σ is itself an even zero-sum set (a relation). Since |P∖Σ| ≤ 2 and dim aff(P) = 6, we get dim aff(Σ) ≥ 4. So the relation code R (the even zero-sum subsets of Σ) has dim R = 9 − dim aff(Σ) ≤ 5.
  2. There are no 2-relations, because the points are distinct. Hence there are no 8-relations either, since the complement in Σ of an 8-relation would be a 2-relation. So R ∖ {0, Σ} splits into pairs {T, Σ + T} with |T| = 4, |Σ + T| = 6 and g(Σ + T) = G·g(T) = −g(T).
  3. With V′ := A_4 − 3A_6 + 9A_8 − 27A_10 = 27 + 4A_4, the formula of 520f1484 reads N_0 = (513 + 9V′)/24. So N_0 ≥ 50 needs V′ ≥ 77, i.e. A_4 ≥ 13.
  4. If dim R ≤ 4, there are at most 7 four-relations, so A_4 ≤ 7. ✗ Hence dim R = 5: there are 15 four-relations, and at most a ≤ 1 of them have g = −1.
  5. **Kernel code.** On R, g is the character r ↦ (−1)^{|r∩M|}, where M := {g = −1}. It is nontrivial because g(Σ) = −1. Its kernel K has dimension 4, and K∖{0} contains exactly one member of each pair {T, Σ + T}: the 15 − a positive 4-relations and the a six-relations Σ + T with T negative.
  6. For any binary linear code of dimension 4, Σ_{c∈K}|c| = 2^3·|supp K| ≡ 0 (mod 8). Here the sum is 4(15 − a) + 6a = 60 + 2a ∈ {60, 62}, which is not ≡ 0 (mod 8). ✗

**So s = 10 is impossible at L = 14.** ∎

## 3. Theorem P12: s = 12 at L = 14 forces τ = 0 and G = +1

When w is even, Ψ ∈ {0, ±4, ±8, ±12} and 3 | Ψ iff Ψ ∈ {0, ±12}. When w is odd, Ψ ∈ {±2, ±6, ±10} and 3 | Ψ iff |Ψ| = 6. Parseval gives ΣΨ² = 768.

- **τ = 0, G = −1.** Every w is odd, so at least 50 ξ have |Ψ| = 6, giving ≥ 1800 > 768. ✗
- **τ ≠ 0.**
  1. Let O := {w odd} (32 points) and E := {w even}. By Lemma PP(a), E = c + H with H = τ^⊥.
  2. Let k_O and k_E count the ξ in O and in E with 3 ∤ Ψ, so k_O + k_E ≤ 14. Let j be the number of ±10 values in O. Then Σ_O Ψ² = 36(32 − k_O) + 4k_O + 96j = 1152 − 32k_O + 96j. Also Σ_E Ψ² = 16i_4 + 64i_8 + 144i_12, where i_4 + i_8 = k_E. The total is 768. This forces k_O ≥ 12, and:
     - k_O = 12 gives j = 0 and Σ_E Ψ² = 0;
     - k_O = 13 needs Σ_E Ψ² + 96j = 32 with k_E ≤ 1, which is impossible;
     - k_O = 14 needs 96j + 144i_12 = 64 with k_E = 0, which is impossible.
  3. Hence Ψ ≡ 0 on E = c + H. By Lemma PP(c), Σ is a union of 6 pairs {y, y + τ}, so τ = 6τ = 0. ✗

**Hence s = 12 at L = 14 forces τ = ΣΣ = 0 and G = +1, together with dim aff(Σ) = 5 from fc201185.** ∎

**Remark (the h_0 condition alone cannot finish s = 12).** Hand-checked identity: identify a 5-flat with F_2^5, and take six distinct ζ_1, …, ζ_6 ∈ F_2^5 with Σζ_i = 0 and signs ε_i with Πε_i = −1. Then f(x) := Σ_i ε_i(−1)^{x·ζ_i} has an odd number of negative terms at every x, so f(x) ∈ {0, ±4}. By Parseval its support has 12 points. With g := f/4 there, Ψ is ±8 at exactly six classes and 0 elsewhere, which gives N_0 = 52 ≥ 50. This case therefore needs slice-level (Lemma SV) or (★) arguments. It is NOT a construction of a Boolean function.

## 4. s = 14 with τ = 0 and G = +1 is excluded

Here Ψ = 14 − 2w. When w is even, Ψ ≡ 2 (mod 4) and 3 | Ψ iff |Ψ| = 6. If τ = 0 and G = +1, every w is even, so ≥ 50 values have |Ψ| = 6, giving ≥ 1800 > 896. ✗

The other s = 14 cases are NOT excluded. For example, with τ ≠ 0 the tight Parseval case forces Ψ ≡ 0 on a half-space, so Σ is a union of 7 τ-pairs, and that is consistent.

## 5. Open list at (3,112), L = 14 (updated)

- s = 12 with dim aff(Σ) = 5, ΣΣ = 0 and G = +1.
- s = 13.
- s = 14 with τ ≠ 0, or with τ = 0 and G = −1.

Everything else at L = 14 is excluded: by fc201185 §1 and by §§2–4 here. **The floor stays L ≥ 14.**

The (24,24,2) gap and the original problem remain OPEN. Novelty is UNCLEARED. All findings are retained. Same 18 owners, OWN root and HOLD. Science cutoff 11:05:38 PDT.
