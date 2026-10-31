# Balanced NL242 (3,112) — coset projection and exclusion of L ≤ 8, so L ≥ 10

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 07:18:54 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed and unadopted, with no machine check and no formal, kernel or novelty claim. No program, Eval, CAS, enumeration, solver, CLI, nested agent or GO was used; all arithmetic was done by hand in writing.

**Scope.** The residue type (polar rank 6, weight 112), i.e. r = 3 and d = 112. This raises the admitted Gate III floor at this one weight from L ≥ 8 to **L ≥ 10**. The weights 144 and 128 are NOT treated, and the d128/u8 branch is untouched. The (3,112) type, the (24,24,2) gap and the original problem remain OPEN.

## 0. Inputs

Admitted at their cuts:

- **S0017**: relation (3), B ≡ q − Hδ (mod 3); and (9)–(11). S0017 §5 gives, for r = 3, α + 2ν = 5d/8 − 40 − L − u/2, i.e. **α + 2ν = 30 − L − u/2** at d = 112.
- **Gate III**: L ≥ 8 at rank 6. It is not needed for the exclusion below, which covers every L ≤ 8 directly.

Own candidates used as premises (WRITTEN, unreviewed; any adoption must review them too):

- Theorem A of `u-class-L-parity-and-rank4-160-coset-projection-v1.md` (SHA `7cecd509…0c9b`): u ≡ 4 (mod 8) at d = 112, so u ≥ 4. One line from R(0) = 0 and S0017 (9).
- Lemma B and Corollary C of the same file: L is even at rank 6.
- Theorem O(b) of `lifted-odd-sum-support-and-affine-spanning-small-cosets-v1.md` (SHA `66981733…c7ce`): dim aff(P) ≥ 5.

Ordinary mathematics: bent quadratic forms on F_2^6, characters, and affine dependencies.

## 1. Setting

- D = D̄∘π, with |V| = 4 and D̄ bent of weight 28 on F_2^6.
- U = V^⊥ (64 points), and q = −σ on U, because ε = −1, A_r = 32 and Ŵ_D = 32σ on U.
- g(ā) := Σ_{b∈ā} δ(b) = c_ā(λ_ā − μ_ā), and h_0(ξ) := Σ_ā g(ā)(−1)^{ā·ξ}. Σ := supp g, and P is the set of cosets carrying small values.

By (3), u_0 := B|_U ≡ −σ − h_0. So:

- B = q = −σ exactly where h_0 ≡ 0 (these are the N_+ points);
- B = 0 exactly where h_0 ≡ −σ (α points);
- B = σ exactly where h_0 ≡ σ (ν points).

Hence **wt(h_0) = α + ν ≤ α + 2ν = 30 − L − u/2 ≤ 28 − L**. Write N_0 := #{ξ : h_0(ξ) ≡ 0} = 64 − wt(h_0) ≥ 36 + L.

Also:

- **L ≥ |Σ| + 2|P ∖ Σ|**, since a coset in P ∖ Σ has λ ≡ μ (mod 3) with (λ, μ) ≠ (0, 0);
- **|P| ≥ 6 and dim aff(P) ≥ 5** (Theorem O(b)).

## 2. Zero counts of F_3 character sums on F_2^6

Let Σ = {ā_1, …, ā_s} with g(ā_i) = ±1, and put z_i = g(ā_i)(−1)^{ā_i·ξ}. Then h_0 ≡ 0 iff Σz_i ≡ 0 (mod 3).

The symmetric-function indicator for {Σz ≡ 0} was solved by hand on every split (n_+, n_−). With e_k the elementary symmetric functions of the z_i, write A_k := Σ g(T) over the zero-sum k-subsets T ⊆ Σ; then Σ_ξ e_k = 64A_k for k ≥ 1 and Σ_ξ e_2 = 0. This gives:

| s | indicator of Σz ≡ 0 | N_0 |
|---|---|---|
| 4 | 3/8 − e_2/8 + 3e_4/8 | 24 + 24A_4 |
| 5 | (5 + e_2 − 3e_4)/16 | 20 − 12A_4 |
| 6 | (5 − e_2 + e_4 − 5e_6)/16 | 20 + 4A_4 − 20A_6 |
| 7 | (21 + e_2 − 3e_4 + 9e_6)/64 | 21 − 3A_4 + 9A_6 |
| 8 | (43 − e_2 + 3e_4 − 9e_6 + 27e_8)/128 | (43 + 3A_4 − 9A_6 + 27A_8)/2 |

Every row was re-checked by hand at all splits. Example for s = 8: at (8,0) the indicator gives 43 − 28 + 210 − 252 + 27 = 0, and at (7,1) it gives 43 − 14 + 126 − 27 = 128, i.e. value 1.

**Structural bounds.** The zero-sum even subsets of Σ form the affine-dependency space, of dimension s − 1 − dim aff(Σ). A zero-sum 6-subset of a zero-sum 6-set or of an 8-set with ΣΣ = 0 would leave a zero-sum pair, which is impossible.

## 3. Theorem R (L ≤ 8 is impossible at (3,112))

*Proof.* L is even (Corollary C). L ≤ 4 contradicts |P| ≥ 6. So let L ∈ {6, 8}. Then N_0 ≥ 36 + L ≥ 42, and in fact N_0 ≥ 44 when L = 8.

The constraints |P| ≥ 6 and |Σ| + 2|P∖Σ| ≤ L ≤ 8 allow only these (|Σ|, |P∖Σ|):

- (4, 2), (5, 1), (6, 0), (6, 1), (7, 0) or (8, 0), when L = 8;
- (6, 0), when L = 6.

**s = 4, type (4,2).** P = Σ plus two points, so dim aff(P) ≤ dim aff(Σ) + 2 ≤ 3 + 2. But N_0 ≥ 44 forces A_4 = 1, i.e. Σ is an affine 2-flat. Then dim aff(P) ≤ 4 < 5. Contradiction.

**s = 5.** Two distinct 2-flats inside a 5-set would share three points and hence coincide. So |A_4| ≤ 1 and N_0 ≤ 32 < 42.

**s = 6.**

- If ΣΣ = 0, then A_4 = 0 and N_0 = 20 − 20G ≤ 40.
- If ΣΣ ≠ 0, then A_6 = 0. The dependency space has dimension ≤ 6 − 1 − 3 = 2, so A_4 ≤ 3 and N_0 ≤ 32.

Both are below 42. (For L = 6 the zero-sum case would also need dim aff ≥ 5, which is impossible: Σ = P, and a zero-sum 6-set has dim aff ≤ 4.)

**s = 7.** Zero-sum 6-subsets have complement {ΣΣ}, so |A_6| ≤ 1.

- If A_6 = 1, put p = ΣΣ ∈ Σ. Then Σ ∖ {p} is a zero-sum 6-set with no zero-sum 4-subset, so every 2-flat in Σ contains p. The triples of Σ ∖ {p} summing to p come in complementary pairs, and two distinct triples have equal sums only if they are complementary. So |A_4| ≤ 2 and N_0 ≤ 21 + 6 + 9 = 36.
- If A_6 ≤ 0, the dependency space has at most 7 nonzero elements, so N_0 ≤ 21 + 21 = 42 with A_6 = 0. Equality would need A_4 = −7, i.e. all seven dependencies are 2-flats. Then Σ is an affine 3-flat minus one point, whose sum is that point, so A_6 = 0 is consistent. But L = 8 needs N_0 ≥ 44. Contradiction.

**s = 8, type (8,0).** Here P = Σ, so dim aff(Σ) ≥ 5 and the dependency space has dimension ≤ 2, i.e. at most 3 nonzero relations.

- If ΣΣ = 0, then A_6 = 0 and 3A_4 − 9A_6 + 27A_8 ≤ 27 + 6 = 33.
- Otherwise A_8 = 0 and the value is ≤ 27.

In both cases N_0 ≤ (43 + 33)/2 = 38 < 44. ∎

**Corollary.** At (3,112), **L ≥ 10**, and L is even. This improves the admitted Gate III value L ≥ 8 at this single weight. The exclusion of L ≤ 8 here is independent of Gate III's L4–L7 proofs. It does not replace them, and it inherits the WRITTEN status of Theorems A and O.

## 4. What remains

At L = 10, the configuration Σ = 2-flat with G = +1 (N_0 = 48), plus three balanced (1,1) cosets spanning dimension 5, passes every test above. The cases s = 9, 10 were not analysed.

The weight-144 case has a larger budget (wt(h_0) ≤ 40), and there s = 4 survives already at L = 8.

The (3,112) type, the (24,24,2) gap and the original problem remain OPEN. Novelty and priority are UNCLEARED. All earlier findings are retained, including the permanent v167 reviewer read-order PROCESS MAJOR and the own attribution MINOR. Same 18 owners, OWN root and HOLD. Science cutoff 2026-10-27T11:05:38-07:00; no early park.
