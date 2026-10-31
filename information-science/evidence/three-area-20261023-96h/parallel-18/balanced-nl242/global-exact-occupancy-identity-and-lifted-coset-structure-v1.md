# Balanced NL242 — an exact all-rank occupancy identity, and the lifted-bent coset structure

Owner **InfoBalancedNL242-2**, slot info-6. Actual `/bin/date` observation BEFORE this write: **Tue Oct 27 06:31:15 PDT 2026**.

**NEW WRITTEN AUTHOR CANDIDATE.** It is not reviewed or adopted. It is not machine-checked, formal, kernel-checked, executed or novelty-cleared. No interpreter, Eval, calculator, CAS, enumeration, solver, replay, CLI, nested agent or GO was used. All arithmetic below was done by hand in writing.

This packet does **not** resolve the unrestricted balanced nine-variable NL242 problem. It does not close the (24,24,2) gap, and it excludes no residue type.

## 0. Authority, source separation and inputs

**Authority.** `NL-post-v167-whole-read-qualified-original-direction-v205.json` was read ENTIRE first. The work is prospective and source-separated.

**Inputs actually used**, all admitted at their stated cuts:

- **(I1) Canonical bridge, gate I.** Parent `nl242-all-rank-raw-and-rank4-rank6-entire-parent-v1.md`, using `hard-continuation-20261015/proof.md` §§1, 4. Every balanced peak-28 f gives odd halves with canonical spectra K1, K2 ≡ 2 (mod 8). Their inverse transforms are ±256, i.e. K1 = φ̂ and K2 = ψ̂ for ±1 functions φ, ψ on F_2^8. Write S = K1 + K2 and R = K1 − K2. These are actual Walsh coefficients of f on the two sectors, and R(0) = 0.
- **(I2) Residue type.** From `quadratic-distance/SHARPER.md` and PROOF §6, both reviewed:
  - D := R/8 mod 2 is a quadratic of polar rank 2r and weight d;
  - S ≡ 4 + 8D (mod 16) and R ≡ 8D (mod 16);
  - (r,d) is one of (1,192), (2,128), (2,160), (3,112), (3,128), (3,144), (4,120), (4,136).
- **(I3) Floors.** Gate II: L ≥ 10 for (2,160), with the mandatory alpha274 overlay. Gate III: L ≥ 8 for all rank-6 weights. Gate I: the sparse floor L ≥ 4.
- **(I4) Rank-2 identity.** The rank-2 occupancy identity α + 2ν = 8 − L/4 − u/8 (`wave-v19-nl242-completion-parent-v1.md`). It is used ONLY as a consistency check in §3.4, never as a premise.
- **Ordinary mathematics:** Plancherel; quadratic Walsh spectra; Arf classification of nondegenerate quadratic forms; the Walsh-divisibility / degree criterion.

**Not inputs** (all excluded):

- the unreviewed candidates v2–v12, including C3/C5–C8 floors;
- the HELD u8/L14 lead;
- the v147-F1 and v112 scouts and all their guidance.

No d128/u8 branch is touched.

**Notation.**

- ℓ_k = #{a : |S(a)| = k} for k ∈ {4,12,20,28}, and L = ℓ4 + ℓ12.
- n_k = #{a : |R(a)| = k} for k ∈ {0,8,16,24}, and z = n0. Then d = n8 + n24.
- T := (−1)^D·S. Since T ≡ 4 (mod 16), T ∈ {−28, −12, 4, 20}.
- Ŵ_D(x) = Σ_a (−1)^{D(a) + a·x}. Its support A_D is a coset of a 2r-dimensional space, with values ±2^{8−r}. Put σ := Ŵ_D/2^{8−r} on A_D.

## 1. Exact signed-partition form of the original problem

Put u := (φ+ψ)/2 and w := (φ−ψ)/2. Both take values in {0,±1}, |u| + |w| = 1 pointwise, and E := supp u, E^c = supp w.

- Then S = 2Û and R = 2Ŵ, where Û(a) = Σ_x u(x)(−1)^{a·x}.
- Equivalently Ŝ = 512u and R̂ = 512w.

**Converse.** Take any u, w ∈ {0,±1} with |u| + |w| = 1, |Û| ≤ 14, |Ŵ| ≤ 14 and Ŵ(0) = 0. Put φ = u + w and ψ = u − w; these are ±1. Then f(y,0) = g(y), f(y,1) = h(y), with (−1)^g = φ and (−1)^h = ψ, has Walsh values W_f(a,0) = 2Û(a) and W_f(a,1) = 2Ŵ(a). Hence f + t (adding the last coordinate) is balanced with peak ≤ 28.

**Conclusion.** A balanced nine-variable function with NL ≥ 242 exists if and only if F_2^8 admits such a complementary pair of signed sets. The forward direction is (I1); the converse is the display above.

## 2. Census identities and parity

**Size of E.**

- Σ_a S² = (1/256) Σ_x Ŝ(x)² = 1024|E|.
- From the R census: Σ_a R² = 64·n8 + 256·(256 − d − z) + 576·(d − n8) = 65536 + 320d − 256z − 512·n8.
- The 9-variable Parseval identity Σ S² + Σ R² = 262144 then gives

```
|E| = 192 - 5d/16 + z/4 + n8/2.                                  (E)
```

**Parity of z.**

- For d ∈ {192,128,160,112,144}, 5d/16 is an integer. For d ∈ {120,136} it is a half-integer.
- Integrality of |E| therefore makes z even. Since 0 ∈ Z, z ≥ 2.
- More precisely, **z ≡ 2·n8 (mod 4)** at polar ranks 2, 4, 6, and **z ≡ 2 + 2·n8 (mod 4)** at rank 8.

## 3. The exact C identity and the all-rank occupancy equation

**Proposition 3.1.** Put C := Σ_a (−1)^{D(a)} S(a) = Σ T. Then

```
C = 40d - 6656 - 64(L + n8) - 32z.                               (C)
```

*Proof.*

- On {−28, 20}, T² = 560 − 8T. On {−12, 4}, T² = 48 − 8T. Hence Σ S² = Σ T² = 143360 − 512L − 8C.
- Add the R census and use Parseval:

  143360 − 512L − 8C + 65536 + 320d − 256z − 512·n8 = 262144.

- Solving gives (C). ∎

**Proposition 3.2.** C = 2Σ_x u(x)·Ŵ_D(x) = 2^{9−r}·(N_+ − N_−). Here N_± = #{x ∈ A_D : u(x) = ±σ(x)} and m′ := #{x ∈ A_D : u(x) = 0}. So N_+ + N_− + m′ = 2^{2r}.

*Proof.* Plancherel gives Σ_a (−1)^D S = (1/256) Σ_x Ŵ_D(x)·Ŝ(x), and Ŝ = 512u. ∎

**Theorem 3.3 (exact all-rank occupancy equation).** For every balanced peak-28 target,

```
L + n8 + z/2 + 2^(4-r) N_+ + 2^(3-r) m' = B(r,d) := (40d - 6656)/64 + 2^(3+r).
```

| (r, d) | (1,192) | (2,128) | (2,160) | (3,112) | (3,128) | (3,144) | (4,120) | (4,136) |
|---|---|---|---|---|---|---|---|---|
| B | 32 | 8 | 28 | 30 | 40 | 50 | 99 | 109 |

*Proof.* Equate Proposition 3.1 with Proposition 3.2, substitute N_− = 2^{2r} − N_+ − m′, and divide by 64. ∎

At rank 8, A_D = F_2^8, so m′ = |E^c|. By (E), m′ = 64 + 5d/16 − z/4 − n8/2. Eliminating it gives

```
8L + 6 n8 + 3z + 8 N_+ = 386  (d=120)   or   446  (d=136).
```

Here N_+ = #{x ∈ E : u(x) = σ(x)}.

**3.4 Consistency with the admitted rank-two identity.**

- For (1,192) the theorem reads m′ + 2N_+ = 8 − L/4 − (z + 2n8)/8.
- This is exactly the parent-supported α + 2ν = 8 − L/4 − u/8, with u = #{p=0} + 2#{|p|=1} = z + 2n8, α = m′ and ν = N_+.
- So Theorem 3.3 is its exact generalization to every polar rank. The rank-2 identity is not a premise of this proof; the two were obtained independently and they agree.

**Corollary 3.5 (budgets).** All terms are nonnegative, so L + n8 + z/2 ≤ B − 2^{3−r}m′ − 2^{4−r}N_+. With z ≥ 2:

| Type | Bound |
|---|---|
| (2,128) | L + n8 ≤ 7. (This type was already excluded at its historical boundary; that exclusion is not re-proved here.) |
| (2,160) | L + n8 + 2m′ + 4N_+ ≤ 27. With admitted L ≥ 10: N_+ ≤ 4, m′ ≤ 8, n8 ≤ 17 (so n24 ≥ 143), z ≤ 36, L ≤ 27. |
| (3,112) | L + n8 + m′ + 2N_+ ≤ 29 |
| (3,128) | L + n8 + m′ + 2N_+ ≤ 39 |
| (3,144) | L + n8 + m′ + 2N_+ ≤ 49 |
| Rank 8 | 8L + 6n8 + 8N_+ ≤ 380 or 440 |

**Corollary 3.6 (large-value census).** Write C as Σ T and eliminate ℓ20:

```
l28 = (11776 - 40d)/48 + l4 + (2/3) l12 + (4/3) n8 + (2/3) z.
```

For d = 160 this is ℓ28 = 112 + ℓ4 + (2/3)ℓ12 + (4/3)n8 + (2/3)z. Integrality gives **ℓ12 ≡ n8 − z (mod 3)** at d = 160. The analogous residue holds for each d, through 3ℓ28 = 736 − 5d/2 + 3ℓ4 + 2ℓ12 + 4n8 + 2z.

## 4. Lifted-bent types: d ∈ {192, 160, 112, 144}

**Lemma 4.1.** Let V be the radical of D's polar form. If Ŵ_D(0) = 256 − 2d ≠ 0, then:

- D is constant on cosets of V;
- D = D̄∘π, where D̄ is a bent quadratic on F_2^8/V (dimension 2r) of weight d/2^{8−2r};
- A_D = V^⊥, and σ = σ̄ is the dual-bent sign.

*Proof.* D(a+v) = D(a) + D(v) for v ∈ V, and D|_V is linear. Hence Ŵ_D(0) = (Σ_{v∈V} (−1)^{D(v)})·(Σ_{cosets} (−1)^{D}), which is nonzero only if D|_V = 0. ∎

For d = 160 this gives D̄ bent of weight 10 on F_2^4 with D̄(0) = 0. By the Arf classification, every such D̄ is linearly equivalent to a1a2 + a1 + a2 + b1b2.

**Proposition 4.2 (coset census).** Write |V| = 2^v, with v = 8 − 2r even. For a coset ā, put s_ā := Σ_{x∈V^⊥} u(x)(−1)^{a·x}. Let k_ā, λ_ā, μ_ā count T = −28, −12, 4 in the coset. Then

```
Σ_{b in ā} S(b) = 2^(v+1) s_ā,      (−1)^{D̄(ā)} 2^(v+1) s_ā = 20·2^v − 48k − 32λ − 16μ.
```

The first equality is Fourier summation over the coset; the second is the census of T-values. For d = 160:

- (−1)^{D̄(ā)}·s_ā = 10 − (3k + 2λ + μ)/2;
- k_ā ≡ μ_ā (mod 2);
- summing over cosets reproduces (C).

**Proposition 4.3 (mod-3 determination of u on V^⊥).** Since 2^{v+1} ≡ 2 and 2^{2r} ≡ 1 (mod 3), every lifted-bent type satisfies

```
(−1)^{D̄(ā)} s_ā ≡ 1 − λ_ā + μ_ā  (mod 3),
u|_{V^⊥} ≡ (−1)^r σ̄ − Δ̂   (mod 3),
Δ̂(x) := Σ_ā (λ_ā − μ_ā)(−1)^{D̄(ā) + ā·x}.
```

Because u takes values in {0,±1} ≅ F_3, the restriction of u to V^⊥ is determined completely by how the small S-values (|S| = 12 against |S| = 4) are distributed among the V-cosets.

For d = 160 (r = 2):

- N_+ = #{Δ̂ ≡ 0};
- m′ = #{Δ̂ ≡ σ̄};
- N_− = #{Δ̂ ≡ −σ̄}.

**Corollary 4.4 (rank 4, weight 160).**

- **(a) Imbalance is forced.** Some V-coset has λ ≢ μ (mod 3). Otherwise Δ̂ ≡ 0, so N_+ = 16 and the left side of Theorem 3.3 is at least 64 > 28.
- **(b) One-coset concentration.** Suppose every small S-value lies in a single coset α*. Then Δ̂ = δ(−1)^{D̄(α*)}χ_{α*} with δ ≢ 0, so N_+ = 0. The dual-bent transform Σ_x σ̄(x)(−1)^{α·x} = 4(−1)^{D̄(α)} gives m′ = 8 + 2δ ∈ {6, 10}. With admitted L ≥ 10 this forces δ = −1, m′ = 6 and **L + n8 + z/2 = 16** exactly. Hence L ≤ 15.
- **(c) Extremal slack.** Equality L + n8 + z/2 = 28 holds iff N_+ = m′ = 0, i.e. u = −σ̄ on all of V^⊥. Then every coset has (−1)^{D̄}s = −4, i.e. 3k + 2λ + μ = 28. That has no solution with λ = μ = 0, so every coset carries a small value, and L ≥ 16.

**Proposition 4.5 (zero set when there is no |R| = 8 value).** Use the pointwise identity

  (R/8)² = 4 + 5D − 4·1_Z − 8·1_{|R|=8}.

Write p := R/8. Its transform is p̂ = R̂/8 = 64w, so the transform of p² is the convolution (p̂ ∗ p̂)/256 = 16·A_w, where A_w(x) = Σ_y w(y)w(x+y). With D̂(x) = −Ŵ_D(x)/2 for x ≠ 0, the transform of the right side gives, for x ≠ 0:

```
32 A_w(x) = −5 Ŵ_D(x) − 8 χ_Z(x) − 16 χ_{|R|=8}(x).
```

A_w(x) is even for x ≠ 0, because pairs y, x+y contribute ±2. Now suppose n8 = 0.

- **Ranks 2 and 4.** Here 5Ŵ_D/8 ≡ 0 (mod 8), so χ_Z(x) ≡ 0 (mod 8) for x ≠ 0, and z ≡ 0 (mod 8). Every Walsh coefficient of 1_Z is then divisible by 16. By the divisibility/degree criterion deg 1_Z ≤ 5, and since Z ≠ ∅, **z ≥ 8**. This reproves, in all-rank form, the rank-2 "z ≥ 8" under n8 = 0.
- **Rank 6.** z ≡ 0 (mod 4) and z ≥ 4.
- **Rank 8.** z ≡ 2 (mod 4).

## 5. What this does and does not give

**Proved here (WRITTEN):**

- the exact signed-partition equivalence;
- the exact identities (E) and (C), Theorem 3.3 and Corollary 3.6;
- the lifted-bent coset census and its mod-3 determination;
- Corollary 4.4 and Proposition 4.5.

Theorem 3.3 is the all-rank form of the parent-supported rank-2 occupancy identity. The budgets are sharp accounting identities with explicit slack terms (m′, N_+), not inequalities with hidden loss.

**Not proved:**

- No residue type is excluded. Combined with admitted floors, every open type keeps a nonempty window. For example (2,160) has 10 ≤ L ≤ 27, and the rank-6 types have L ≥ 8 with L + n8 + z/2 ≤ 30, 40 or 50.
- The (24,24,2) gap and the unrestricted balanced NL242 problem remain **OPEN**.
- No Boolean witness, numerical nonlinearity, truth table or global NL claim is made.

**First unproved step.** For (2,160), turn Proposition 4.3 (u on V^⊥ ≡ σ̄ − Δ̂) and the parallel R-coset data into a joint F_3 incompatibility. The supports of u|_{V^⊥} and w|_{V^⊥} must be complementary. Alternatively, establish a z + 2n8 lower bound strong enough to meet the floor.

## 6. Assurance

- Exact WRITTEN author candidate.
- Generic Plancherel, quadratic-spectrum, Arf and divisibility tools are prior mathematics. Theorem priority and novelty are UNCLEARED.
- No earlier verdict is transferred. Adoption requires a fresh, entire mathematical and dependency review.
- All earlier own, parent and reviewer findings are retained, including the permanent v167 reviewer read-order MAJOR.
- The same 18 owners, OWN root and HOLD apply. Science cutoff 2026-10-27T11:05:38-07:00; deadline 12:35:38. No early park.
