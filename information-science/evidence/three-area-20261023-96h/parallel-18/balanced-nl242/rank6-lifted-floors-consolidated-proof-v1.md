# Balanced NL242 — consolidated self-contained proof: (3,112) has L ≥ 14 and (3,144) has L ≥ 10

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 07:59:10 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is unreviewed and unadopted. It is not machine-checked, formal, kernel-checked, executed or novelty-cleared. No interpreter, Eval, CAS, enumeration, solver, CLI, nested agent or GO was used; all arithmetic was done by hand.

**Purpose.** This file consolidates, for review, the scattered proofs in the following own packets:

- u-class (7cecd509);
- odd-sum (66981733);
- the rank-6 packets 7b533fa5, 520f1484, 5da16610, 5c204162, 3f9e20f6 and 18613ab3.

It gives one self-contained derivation from the admitted inputs only. Where this file is cleaner than an earlier packet, this file governs; the earlier packets stay immutable.

**This file does NOT use Gate III.** The parity of L together with |P| ≥ 7 already gives L ≥ 8.

**Scope.** Only the lifted rank-6 residue types (r, d) = (3,112) and (3,144). Weight 128 (the d128/u8 branch) is untouched. No residue type is excluded. The (24,24,2) gap and the original problem remain OPEN.

## 0. Admitted inputs

All from **S0017** = `global-all-rank-ternary-lift-and-dual-occupancy-v1.md` (SHA `842bb4e6…86bf`), at the Gate I parent cut:

1. **(3)** B ≡ q − Hδ (mod 3), where B ∈ {0, ±1} is the S-sector inverse array, q = εHχ/A_r, and δ = φ(ζ) is supported on the small values: δ = +χ on {T = −12} and −χ on {T = 4}.
2. **(6)** S = 2HB, R = 2Ha, and R(0) = 0.
3. **(9)** w_R := wt(a) = 64 + 5d/16 − u/4, where u = z + 2c.
4. **(10) and (11)**, which at r = 3 give **α + 2ν = 5d/8 − 40 − L − u/2**. That is 30 − L − u/2 at d = 112, and 50 − L − u/2 at d = 144. Here α = #{x ∈ U : B = 0} and ν = #{x ∈ U : B = −q}.
5. **Congruences** S ≡ 4 + 8D (mod 16) and R ≡ 8D (mod 16). Put T := χS ∈ {−28, 20, −12, 4}.

Ordinary mathematics used: bent quadratic forms, Fourier analysis over Z and F_3, and binary linear codes.

## 1. Setting

- D is a lifted quadratic of polar rank 6. V is its radical, |V| = 4, and D = D̄∘π with D̄ bent on F_2^6.
- Coordinates: a = (ā, β) with β ∈ V ≅ F_2^2, and dual x = (ξ, η). U = V^⊥ = {η = 0}.
- On U, Hχ = 32σ with σ = ±1 the dual-bent sign, and Σ_ξ σ(ξ)(−1)^{b·ξ} = 8c_b, where c_b := (−1)^{D̄(b)}. Since ε = −1 and A_r = 32, q = −σ on U and q = 0 off U.
- **Slice functions** u_η(ξ) := B(ξ, η), and υ_η(ā) := Σ_ξ u_η(ξ)(−1)^{ā·ξ}. Because S = 2HB,

  ```
  υ_η(ā) = (1/8) Σ_β S(ā,β)(−1)^{β·η}.                                   (1.1)
  ```

- For each coset ā, put g_η(ā) := Σ_β δ(ā,β)(−1)^{β·η}, and write g := g_0.
- **P** is the set of cosets carrying a small value, and **Σ** := supp g = {ā : λ_ā ≢ μ_ā (mod 3)} ⊆ P. Here λ_ā = #{T = −12} and μ_ā = #{T = 4} in ā.
- A coset in P ∖ Σ has λ ≡ μ (mod 3) with (λ, μ) ≠ (0, 0), so it carries at least 2 small values. Hence **L ≥ |Σ| + 2|P ∖ Σ|**. Combined with |P| ≥ 7 (Theorem M), this forces s := |Σ| ≥ 14 − L, so s ≥ 6, 4, 2 at L = 8, 10, 12.
- h_0(ξ) := Σ_ā g(ā)(−1)^{ā·ξ}, read mod 3. Z := {ξ ∈ U : h_0 ≡ 0}, N_0 := |Z|, and wt(h_0) := 64 − N_0.
- **Pure** cosets are those not in P. On them T ∈ {−28, 20}; k_ā denotes the number of −28 entries.

By (3), u_0 ≡ −σ − h_0 (mod 3). Hence:

- u_0 = −σ = q on Z;
- u_0 = 0 exactly where h_0 ≡ −σ (α points);
- u_0 = σ exactly where h_0 ≡ σ (ν points).

So **wt(h_0) = α + ν**.

**Census of a coset.** From (1.1) at η = 0, s_ā := υ_0(ā) satisfies 8 c_ā s_ā = Σ_{b∈ā} T(b). For a pure coset this gives **c_ā s_ā = 10 − 6k_ā**.

## 2. Parity lemmas

**Lemma A.** u ≡ 4 (mod 8) at d = 112 and d = 144, so u ≥ 4.

*Proof.* R(0) = 0 gives Σ a = 0, so w_R is even. At d = 112, w_R = 99 − u/4; at d = 144, w_R = 109 − u/4. In both cases u/4 is odd. ∎

**Lemma B.** α is even.

*Proof.*

1. For any a_0: Σ_{v∈V} R(a_0 + v) = 8 Σ_{x∈U} a(x)(−1)^{a_0·x}. The same twisted identity holds for any coset c + U.
2. The left side is ≡ 8·#{D = 1 in a_0 + V} (mod 16). D is constant on V-cosets, so that count is 0 or 4, hence even. So |supp a ∩ U| is even.
3. On U, a ≠ 0 exactly where B = 0, so this size is α. ∎

**Corollary C.** L = 5d/8 − 40 − u/2 − α − 2ν. Here u/2 ≡ 2 (mod 4) and α is even, so **L is even**.

## 3. Structure lemmas

**Lemma Φ (expansions; ordinary algebra).** For z ∈ {±1}^s, let φ be the centred residue mod 3. Then

```
φ(Σz) = 2^{1−s} Σ_{|T| odd} (−1)^{s−|T|} (−3)^{(|T|−1)/2} z^T,
1[Σz ≡ 0 (mod 3)] = 1/3 + (2/3)(−1)^s 2^{−s} Σ_{|T| even} (−3)^{|T|/2} z^T.
```

*Proof.* Write φ(t) = (ω^t − ω^{−t})/(i√3) and 1[t ≡ 0] = (1 + ω^t + ω^{−t})/3. Use ω^{±1} = −1/2 ± i√3/2 and expand Π(−1/2 + (i√3/2)z_j). ∎

Put z_ā := g(ā)(−1)^{ā·ξ} for ā ∈ Σ, and A_k := Σ g(T) over the zero-sum k-subsets T ⊆ Σ. Summing over ξ ∈ U gives

```
N_0 = (64/3)·[1 + (−1)^s 2^{1−s} Σ_{k even} (−3)^{k/2} A_k],   with A_0 = 1, A_2 = 0, s = |Σ|.     (3.1)
```

For example s = 4 gives 24 + 24A_4, and s = 8 gives (43 + 3A_4 − 9A_6 + 27A_8)/2.

**Dependency code.** The zero-sum even subsets of Σ form a binary linear code R of dimension s − 1 − dim aff(Σ). Every coordinate that is not identically zero on R equals 1 in exactly half of the codewords. Hence Σ_{c∈R} wt(c) ≤ 2^{dim R − 1}·s.

**Lemma O (odd-sum support).** For η ≠ 0:

- u_η = −φ(Σ_{ā∈P} g_η(ā)(−1)^{ā·ξ}), by (3) with q = 0 off U.
- So u_η = −Σ_{T odd} b_{|T|} g_η(T)(−1)^{(ΣT)·ξ}, and its Walsh transform is supported in OddSums(P_η), where P_η := supp g_η ⊆ P.

Consequently, if ā ∉ OddSums(P), then (1.1) vanishes for every η ≠ 0. The S-row of ā is then constant, i.e. ā is **monochromatic**: k_ā ∈ {0, 4} and c_ā s_ā ∈ {10, −14}.

**Lemma SV (slice values on pure cosets).** For pure ā and η ≠ 0:

- writing T = −4 + 24ε_ā with ε_ā ∈ {±1}^4, (1.1) gives υ_η(ā) = 3c_ā ε̂_ā(η);
- on F_2^2, ε̂ ∈ {0, ±2, ±4} and Σ_η ε̂² = 16.

So **υ_η(ā) ∈ {0, ±6, ±12}**, and the triple (υ_η)_{η≠0} is one of:

- (0, 0, 0), when k ∈ {0, 4};
- one entry ±12 and two zeros, when k = 2;
- (±6, ±6, ±6), when k is odd.

**Theorem M (P spans).** At most 21 cosets lie outside OddSums(P). Hence aff(P) = F_2^6 and **|P| ≥ 7**.

*Proof.*

1. Write u_0 = −σ + e with e = (3σ·1_{U∖Z} + h_0)/2. Then s_ā = −8c_ā + ê(ā).
2. For ā ∈ O := F_2^6 ∖ OddSums(P), we have ĥ_0(ā) = 0, because h_0 = φ(Σ z) has odd-sum support inside OddSums(Σ) ⊆ OddSums(P). Also ā is monochromatic by Lemma O. Hence G(ā) := c_ā·Walsh(σ1_Z)(ā) ∈ {12, −4}.
3. Over all 64 cosets, Σ G = 8N_0 and Σ G² = 64N_0. So Σ_ā (G − N_0/8)² = 64N_0 − N_0².
4. Therefore |O|·min{(12 − N_0/8)², (4 + N_0/8)²} ≤ 64N_0 − N_0². Maximising over N_0 gives |O| ≤ 21.3.
5. So |OddSums(P)| ≥ 43 > 32. Since OddSums(P) ⊆ aff(P), dim aff(P) = 6. ∎

**Corollary.** Since L ≥ |P| ≥ 7 and L is even, **L ≥ 8 at both weights, independently of Gate III.**

**Lemma Ξ and (★).**

- Put Ξ := Σ_ξ h_0(ξ)σ(ξ) = ν − α. By Lemma Φ and Σ_ξ σ(−1)^{b·ξ} = 8c_b:

  ```
  Ξ = 2^{4−s} Σ_{|T| odd} (−1)^{s−|T|} (−3)^{(|T|−1)/2} g(T) c_{ΣT},     |Ξ| ≤ wt(h_0).
  ```

- From α + 2ν = (3wt + Ξ)/2 and S0017 (11):

  ```
  3·wt(h_0) + Ξ = 2(5d/8 − 40) − 2L − u   (= 60 − 2L − u at d = 112; 100 − 2L − u at d = 144).   (★)
  ```

- **Flat case.** If Σ is a 2-flat with G := Π g = +1, then h_0 = z_1·1_K for one W^0-coset K with |K| = 16. Summing characters over K gives Ξ = 2Σ_j g_j c_j ∈ [−8, 8].

## 4. Theorem 112: L ≥ 14 at (3,112)

At d = 112, wt(h_0) ≤ α + 2ν = 30 − L − u/2 ≤ 28 − L. So **N_0 ≥ 36 + L**. Put p′ := |P∖Σ|. The admissible pairs (s, p′) satisfy s + p′ ≥ 7 (Theorem M) and s + 2p′ ≤ L.

**L = 8 (N_0 ≥ 44).** Only (6,1), (7,0) and (8,0) are admissible.

- (6,1) and (7,0): |P| = 7 with dim aff 6 makes P affinely independent. So Σ has no relations and N_0 = 22 or 21.
- (8,0): dim aff(Σ) = 6 leaves exactly one relation. So N_0 ∈ {23, 20, 17, 26, 35, 8}.

All are < 44.

**L = 10 (N_0 ≥ 46).**

- (4,3) and (5,2): P is affinely independent, so N_0 = 24 or 20.
- s = 6: (3.1) gives N_0 = 22 + 6A_4 − 18A_6 ≤ 40. Indeed, ΣΣ = 0 forces A_4 = 0 and gives 22 − 18G; otherwise A_6 = 0 and A_4 ≤ 3.
- s = 7: N_0 = 21 − 3A_4 + 9A_6 ≤ 42. Here |A_6| ≤ 1; if A_6 = 1, every 2-flat contains ΣΣ, so |A_4| ≤ 2; and dim R ≤ 3 gives |A_4| ≤ 7.
- s = 8 (dim aff(Σ) ≥ 5, so at most 3 relations): N_0 ≤ (43 + 33)/2 = 38.
- s = 9 (dim R = 2): this needs −A_4 + 3A_6 − 9A_8 ≥ 33, but the value is ≤ 15.
- s = 10 (dim R = 3, Σwt ≤ 40): this needs A_4 − 3A_6 + 9A_8 − 27A_10 ≥ 66, but the value is ≤ 45.

**L = 12 (N_0 ≥ 48).**

- (2,5) and (3,4): N_0 = 32 and 16.
- s = 4 with p′ ∈ {3, 4}: N_0 ≥ 48 forces a flat with G = +1. Then (★) reads 48 + Ξ = 36 − u, so Ξ ≤ −16, but |Ξ| ≤ 8.
- s = 5, 6, 7: N_0 ≤ 32, 40, 42.
- s = 8:
  - dim aff(Σ) = 3 gives dim aff(P) ≤ 3 + p′ ≤ 5. Impossible.
  - dim aff = 4 gives the value ≤ 45, and dim aff ≥ 5 gives ≤ 33; 53 is needed.
- s = 9 (dim R ≤ 3): the value is ≤ 19 < 36.
- s = 10 (dim R ≤ 4): ≤ 55 < 71.
- s = 11 (dim R = 4, Σwt ≤ 88): ≤ 747 < 1281.
- s = 12 (dim R = 5, Σwt ≤ 192): X ≤ 2260, or 2080 when ΣΣ = 0. The bound X ≥ 2560 is needed.

Every case fails, so **L ∉ {8, 10, 12}. With L even and L ≥ 8, we get L ≥ 14.** ∎

The individual code-weight maximisations are written out in `rank6-112-L12-exclusion-L14-v1.md` (18613ab3) and `rank6-112-erratum-and-L10-exclusion-addendum-v1.md` (520f1484). They use n_{s−1} ≤ 1, n_{s−2} ≤ ⌊s/2⌋ and the per-pair complement structure when ΣΣ = 0.

## 5. Theorem 144: L ≥ 10 at (3,144)

At L = 8, wt(h_0) ≤ 42 − u/2 ≤ 40, so N_0 ≥ 24. As in §4, only (6,1), (7,0) and (8,0) are admissible.

- (6,1) and (7,0) give N_0 = 22 or 21. Impossible.
- (8,0) leaves only:
  - **(C1)** one zero-sum 6-subset Σ_6 with g(Σ_6) = −1 (N_0 = 26);
  - **(C2)** Σ zero-sum with G = +1 (N_0 = 35).

In both, every Σ-coset carries exactly one small value. So for every η ≠ 0, P_η = Σ, with g_η(x) = g(x)(−1)^{β_x·η}.

**(C2).**

1. Odd subsets of Σ, taken modulo complementation, biject onto F_2^6. The pure cosets are exactly the 56 sums ΣT = ΣT^c with |T| = 3.
2. Lemma Φ (s = 8) gives υ_η = −(1/2)(3 − 9G_η) g_η(T), where G_η := Π g_η = G(−1)^{B·η} and B = Σ β_x.
3. Lemma SV excludes the value ±3, so G_η = −1 for all three η ≠ 0, i.e. B·η = 1 for all three.
4. That is impossible for a linear functional on F_2^2.

**(C1).** Write Σ = Σ_6 ∪ {q_1, q_2} and G6_η := Π_{Σ_6} g_η.

- **Type (a):** the pure cosets x + y + q_i, with x, y ∈ Σ_6, have the 5-set partner (Σ_6∖{x,y}) ∪ {q_i}. So υ_η = −(1/2)(3 − 9G6_η) g_η(T), and Lemma SV forces G6_η = −1 for every η ≠ 0.
- **Type (c):** the pure cosets x + q_1 + q_2 have the 7-set partner. So υ_η = −(1/2)(3 + 27G6_η) g_η(T) = 12g_η(T) on all three slices. That needs Σ_{η≠0} ε̂² = 48 > 16, which is impossible.

Hence **L ≠ 8 at (3,144), so L ≥ 10.** ∎

## 6. Status and dependencies

The theorems use only S0017 at its admitted cut, together with ordinary mathematics. Gate III is not used. Every lemma above is proved here, apart from the routine code-weight maximisations, which are cross-referenced in §4.

This consolidated chain supersedes the case lists of 7b533fa5, 520f1484, 5da16610 and 5c204162. Those files, and their errata, remain immutable records.

**Remaining open** (own partial packets fc201185 and f576731b):

- (3,112) at L = 14: s ∈ {10, 12, 13, 14}, with the specified sub-structures.
- (3,144) at L = 10: (6,2)-b, (7,1), C1′ with the y's in {q_1, q_2}, (8,1), (9,0) and (10,0).

The weight-128 type, (2,160), rank 8, the (24,24,2) gap and the original problem all remain **OPEN**. Novelty and priority are UNCLEARED. All earlier findings are retained, including the permanent v167 reviewer read-order PROCESS MAJOR, the cadence MAJORs, the checkpoint-054 attribution MINOR and the checkpoint-059 s = 6 erratum MINOR. Same 18 owners, OWN root and HOLD. Science cutoff 2026-10-27T11:05:38-07:00.
