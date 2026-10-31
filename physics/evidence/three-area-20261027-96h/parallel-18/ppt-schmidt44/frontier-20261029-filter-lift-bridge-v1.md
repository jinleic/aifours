# Filter-lift bridge for the 4×4 PPT Schmidt-number-three problem

**Owner:** PhysicsPPT44-2  
**Actual clock before writing:** Thu Oct 29 08:32:03 PDT 2026  
**Status:** WRITTEN, with exact kernel checks for the explicit source state only. It has **not** been reviewed. **N4 = UNKNOWN.** N4 is the claim that some PPT operator on C⁴⊗C⁴ has Schmidt number ≥ 3. This packet neither proves nor refutes it.  
**Boundaries:** No held, STOPped or noninput material is used. That covers the f161 and f162 episodes, the old JL audit, the selected-parameter episode and all their consumers. This packet is **not** a variant of the consolidated packet `frontier-20261028-original-target-consolidated-v1.md`. It proves no witness-family no-go, and its numerical screens carry no weight as results.

## 0. Notation and the facts used

Notation:
- Bipartite operators act on C^p⊗C^q.
- Write [x] = |x⟩⟨x| and Ω_k = Σ_{i=1}^k |ii⟩.
- The Schmidt rank SR(y) of y ∈ C^p⊗C^q is the rank of its p×q coefficient matrix.
- A linear map Φ: M_4 → M_n is **k-positive** if id_k⊗Φ is positive.
- SN_k(p,q) is the closed convex cone of PSD operators of Schmidt number at most k.
- An operator W is **k-block-positive** if ⟨x|W|x⟩ ≥ 0 whenever SR(x) ≤ k.

Facts used:
- **(F1) Schmidt decomposition.** SR(y) ≤ k iff y = (F⊗G)Ω_k for some linear F: C^k→C^p and G: C^k→C^q.
- **(F2) Choi correspondence for k-positivity.** Any operator on C^4⊗C^4 can be written uniquely as W = Σ_{ij} Ψ(E_ij)⊗E_ij. W is k-block-positive iff Ψ is k-positive. A fresh public statement is Proposition 1(ii) of vom Ende–Khatri–Denisov, [arXiv:2508.21348](https://arxiv.org/html/2508.21348v1); the factor order does not matter. Also, Ψ is k-positive iff its adjoint Ψ* is.
- **(F3) Bipolar duality.** The dual cone of SN_2(4,4) is the cone of 2-block-positive operators.
- **(F4) Determinantal varieties.** n×m matrices of rank ≤ r form an irreducible affine cone of codimension (n−r)(m−r). The projective dimension theorem holds (Harris, *Algebraic Geometry*, Lectures 9 and 11). F4 is only needed in Theorem 3 when n or m exceeds 5.

**Lemma 0.** Let Φ: M_4 → M_p be k-positive and σ ∈ SN_k(4,q). Then (Φ⊗id_q)(σ) ⪰ 0.

*Proof.* Take a vector ψ with SR(ψ) ≤ k and write ψ = (V⊗U)Ω_k as in F1. Then

(Φ⊗id)([ψ]) = (I⊗U)[((Φ∘Ad_V)⊗id_k)([Ω_k])](I⊗U)*.

Here Φ∘Ad_V: M_k→M_p is k-positive and [Ω_k] ⪰ 0 on C^k⊗C^k, so the right-hand side is PSD. Sum over a Schmidt-rank-≤k decomposition of σ. ∎

## 1. Theorem 1 (filter lift, with an explicit state–separator pair)

Let ρ be PPT on C^4⊗C^m, let Φ: M_4→M_n be 2-positive and acting on the 4-dimensional factor, and set X := (Φ⊗id_m)(ρ). Suppose some y ∈ C^n⊗C^m has **SR(y) ≤ 4** and ⟨y|X|y⟩ < 0. Write y = (F⊗G)Ω_4 as in F1, and define:

- σ := (I_4⊗G*) ρ (I_4⊗G), an operator on C^4⊗C^4;
- Φ_F(Z) := F* Φ(Z) F, a map M_4→M_4;
- W := (Φ_F*⊗id_4)([Ω_4]) = Σ_{ij} Φ_F*(E_ij)⊗E_ij.

Then the following hold:
1. σ is PPT.
2. W is 2-block-positive.
3. Tr(Wσ) = ⟨y|X|y⟩ < 0.

Hence SN(σ) ≥ 3, and N4 holds.

*Proof.*
1. σ ⪰ 0 is immediate. Also σ^Γ = (I⊗G^T) ρ^Γ (I⊗Ḡ) ⪰ 0.
2. Φ_F is 2-positive, being Ad_{F*} composed with Φ. For SR(x) ≤ 2 we have ⟨x|W|x⟩ = Tr([Ω_4] (Φ_F⊗id)([x])), which is ≥ 0 by Lemma 0.
3. Congruence on Bob commutes with Φ⊗id, so

   (F*⊗G*) X (F⊗G) = (F*⊗I)(Φ⊗id)(σ)(F⊗I) = (Φ_F⊗id)(σ).

   Therefore ⟨y|X|y⟩ = ⟨Ω_4|(Φ_F⊗id)(σ)|Ω_4⟩ = Tr(σ W).

If SN(σ) ≤ 2, then Tr(Wσ) ≥ 0 by item 2, a contradiction. ∎

## 2. Theorem 2 (the bridge is exact)

N4 holds **iff** the following data exist:
- some m and n;
- a PPT ρ on C^4⊗C^m;
- a 2-positive Φ: M_4→M_n;
- a vector y with SR(y) ≤ 4 and ⟨y|(Φ⊗id)(ρ)|y⟩ < 0.

In particular, N4 holds iff, for some m, some 2-positive map **with 4-dimensional output** detects some PPT state on C^4⊗C^m: every vector of C^4⊗C^m has Schmidt rank ≤ 4.

*Proof.* The "if" direction is Theorem 1.

For "only if", let σ be PPT on C^4⊗C^4 with SN ≥ 3. By F3 there is a 2-block-positive W with Tr(Wσ) < 0. Write W = Σ Ψ(E_ij)⊗E_ij and set Φ := Ψ*, which is 2-positive by F2. Then

⟨Ω_4|(Φ⊗id)(σ)|Ω_4⟩ = Tr(σ (Ψ⊗id)([Ω_4])) = Tr(σW) < 0.

So m = n = 4, ρ = σ and y = Ω_4 work. ∎

## 3. Theorem 3 (negative-index criterion)

In the setting of Theorem 1, take n, m ≥ 4 and let ν be the number of negative eigenvalues of X. If

**ν ≥ (n−4)(m−4)+1,**

then there is a y with SR(y) ≤ 4 and ⟨y|X|y⟩ < 0, so N4 holds. For n ≤ 4 or m ≤ 4, ν ≥ 1 suffices. For **n = m = 5**, two negative eigenvalues suffice.

*Proof.* Let N be the span of the eigenvectors of X with negative eigenvalues, so X is negative definite on N. The vectors of Schmidt rank ≤ 4 form the determinantal cone D_4, of codimension (n−4)(m−4) (F4). Its projectivization meets P(N) as soon as (ν−1) + (nm−1−(n−4)(m−4)) ≥ nm−1. Any nonzero vector in the intersection has negative expectation.

The case n = m = 5 is elementary. Restricted to a 2-dimensional subspace of 5×5 matrices, det is a binary form of degree 5, and over C it has a nonzero root. ∎

## 4. Corollary 4 (what must hold if N4 fails)

Suppose N4 fails. Take any PPT ρ on C^4⊗C^m and any 2-positive Φ: M_4→M_n with n, m ≥ 4. Then the negative eigenspace of X = (Φ⊗id)(ρ) contains no nonzero vector of Schmidt rank ≤ 4; it is a "4-CES". Its dimension is therefore at most (n−4)(m−4).

For **n = m = 5** this means:
- (a) X has at most one negative eigenvalue.
- (b) If it has one, −λ < 0, with unit eigenvector y (a 5×5 matrix Y), then Y is invertible.
- (c) In that case, with s := σ_min(Y) and Λ := λ_max(X),

  **λ(1−s²) ≤ Λ s².**

*Proof of (c).* Let s u v* be the smallest singular term of Y and set Y′ := Y − s u v*, which has rank 4. Write Y′ = (1−s²) Y + z with z ⊥ Y and ‖z‖² = s²(1−s²). Since X preserves y^⊥,

⟨Y′|X|Y′⟩ = −λ(1−s²)² + ⟨z|X|z⟩ ≤ −λ(1−s²)² + Λ s²(1−s²).

This expectation must be ≥ 0 because N4 fails. ∎

**Reading.** Every pair (ρ, Φ) that violates (a), (b) or (c) proves N4, and Theorem 1 then produces the explicit 4×4 pair (σ, W). Conversely, if N4 is false, every 2-positive map M_4→M_5 that detects any 4×5 PPT state has this single-eigenvalue, invertible-eigenvector rigidity.

## 5. The actual-state instance: the explicit 4×5 source

### 5.1 The source state

Take the PPT state of Krebs–Gachechiladze, [arXiv:2509.07086v1](https://arxiv.org/pdf/2509.07086), Theorem 5 and Eq. (11), reconstructed here exactly. Alice index first (4), Bob index second (5):

ρ_KG = [e₀]+[e₁]+[e₂] + 3([02+34]+[20+33]+[04]+[23]+[30]+[32]),

with e₀ = |00⟩+|11⟩+|22⟩, e₁ = |01⟩+|12⟩ and e₂ = |10⟩−|21⟩.

The checker `frontier-20261029-kg45-source-check.py` (SHA-256 `8a9f5ba28a8c90e7ccc197e13b39754552c8c3ee38f76e2fab5bc31e69be40b2`) verifies the following in exact arithmetic:
- ρ_KG is PSD of rank 9.
- ρ_KG^Γ is PSD of rank 10.
- The range coordinate matrix Ψ (rows [ψ00,ψ01,ψ02,0,ψ04], [ψ10,ψ00,ψ01,0,0], [ψ20,−ψ10,ψ00,ψ23,0], [ψ30,0,ψ32,ψ20,ψ02]) matches the nine range vectors.
- The integer polynomial identity

  ψ00⁴ = ψ00·M[012|012] − ψ00·M[013|123] − ψ00·M[123|014] − ½ψ02·M[013|013] − ½ψ20·M[123|124]

  holds, where M[R|C] is the 3×3 minor on Alice rows R and Bob columns C. The identity was found by exact elimination over Q and verified by exact expansion.

So every vector of Schmidt rank ≤ 2 in the range has ψ00 = 0, while e₀ has ψ00 = 1. By the range criterion, SN(ρ_KG) ≥ 3. This is checked here and no longer depends on trusting the source's proof.

### 5.2 Consequences of Sections 1–4 for this source

1. **A detecting map exists.** By F3 and F2 (Bob dimension 5), there are 2-positive maps Φ: M_4→M_5 with (Φ⊗id)(ρ_KG) ⋡ 0. If N4 is false, every one of them obeys Corollary 4(a)–(c).
2. **The 4×4 candidates are Bob filters.** By Theorem 1, the 4×4 states this source can produce are σ = (I⊗G*)ρ_KG(I⊗G). If G* has rank 4, σ is local-GL-equivalent to σ_k := (I⊗P_{k⊥})ρ_KG(I⊗P_{k⊥}), where k spans ker G*. Lower-rank filters give PPT states on C^4⊗C^{≤3}. So this source's 4×4 candidates form the CP⁴ family σ_k together with degenerate limits.
3. **Range inheritance (exact).** Let τ be any PPT operator with range(τ) ⊆ range(ρ_KG) and range(τ) ⊄ {ψ00 = 0}. Its Schmidt-rank-≤2 range vectors lie in range(ρ_KG), so the identity above forces ψ00 = 0 on them. Hence SN(τ) ≥ 3. If such a τ also has Bob support of dimension ≤ 4, N4 holds.

## 6. Exploratory screens (floating point; not results)

None of the following is a proof or a no-go. Each is a proper-family or numerical sample only.

- **Range criterion on filters.** For 15 kernel directions k, the Schmidt-rank-≤2 vectors located in range(σ_k) span all of range(σ_k). Nine were structured: e0, …, e4, e3±e4, e0+e3 and e2+e4. Six were random. The range criterion therefore cannot certify those σ_k. The sampler finds a lower bound on the span, so a "full" verdict is reliable up to floating point. A "deficient" verdict is **not** reliable: on an unrelated grid-state test the sampler missed a 4-dimensional linear family, which exact hand algebra then exhibited.
- **Range inheritance, random k.** Six random k were run with Dykstra projections at ψ00 weight c = 0.05; residuals stayed near 0.015. One of them was re-run with penalty descent. There, PPT operators with range in range(ρ_KG) ∩ (C^4⊗k^⊥) were found only at c = 0, and requiring ψ00 weight c forced λ_min(τ^Γ) ≈ −0.2c for c = 0.01, 0.05, 0.1. The route looks infeasible for generic k; special k are not excluded.
- **SU(2) spin-3/2 invariant sector.** The exact recoupling map and eight exact PPT vertices were computed. Frank–Wolfe placed all eight inside the Schmidt-rank-two moment hull.

## 7. What remains open (exact)

The route is now concrete. It needs an **exactly certified** 2-positive Φ: M_4→M_5 that detects ρ_KG or another explicit 4×m PPT Schmidt-number-3 state. Any such certified Φ can be tested exactly against Corollary 4(a)–(c): one either obtains an explicit 4×4 pair (σ, W) with Tr(Wσ) < 0, or confirms the predicted rigidity for that pair.

No exactly certified detecting map is available yet; the range criterion does not produce a linear witness. Deciding N4 is unchanged. **N4 remains UNKNOWN**, novelty is unclear, and there has been no independent, formal or external review.
