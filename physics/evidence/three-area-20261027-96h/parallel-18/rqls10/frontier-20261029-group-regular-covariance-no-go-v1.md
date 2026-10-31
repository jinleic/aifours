# No linear group-regular 1-RQLS(10), of any cardinality

**WRITTEN AUTHOR CANDIDATE plus EXACT COMPUTER CERTIFICATE. UNREVIEWED.** Native `/bin/date`: Thu Oct 29 07:42:46 PDT 2026.

Certificate pins:
- `frontier-20261029-group-regular-pattern-certificate-v1.py`: SHA-256 `19f67a104e814d69daaab8c793facfd9f92f1eafcfff3d76b3a664e5a262e49c` (141 LF).
- Its single-run output `…-v1.json`: SHA-256 `311ea85c6da2a6365ebe4f9c4a2aa1552e782f738f6cca54d707fdfe003023f7`. Status PASS, 331.6 s.

Novelty is unassessed. This is not a formal proof.

## Setting

A 1-RQLS(10) of **any** cardinality is *linearly group-regular* if all of the following hold:
- there is a group Γ of order 100 and a bijection cells ↔ Γ;
- there are subgroups H1, H2 and H3 whose left cosets are the rows, the columns and the label classes;
- there is a unitary **representation** π : Γ → U(10) and a unit vector v with ψ(γ) ∝ π(γ)v for every cell γ.

This is exactly the symmetric setting of the standard algebraic constructions. Examples are Zhang–Cao Construction 3.3 (Γ = G×G with characters) and the Huang–Li character constructions. Note that any group of type-preserving symmetries acting simply transitively on the cells has left-coset row, column and label blocks.

## Theorem G

No linearly group-regular 1-RQLS(10) exists.

**Step 1: structure of Γ (written).**
- The Latin axioms give |H_i| = 10, H_i ∩ H_j = 1 and Γ = H_iH_j for i ≠ j.
- Sylow-5 is normal: n_5 divides 4 and n_5 ≡ 1 (mod 5), so P ⊴ Γ with |P| = 25.
- Each P_i = H_i ∩ P has order 5, and the P_i are pairwise distinct. Hence P has at least three subgroups of order 5, so P ≅ Z5^2.
- The images of the H_i in Γ/P (order 4) are three distinct subgroups of order 2, so Γ/P ≅ Z2^2.
- By Schur–Zassenhaus, Γ = Z5^2 ⋊ V with V = Z2^2.
- The subgroups have the form H_i = P_i ⋊ ⟨(c_i, x_i)⟩. Here P_i is an M_{x_i}-invariant line, x_i is the i-th involution of V, and c_i + M_{x_i}c_i ∈ P_i (closure).

**Step 2: representation constraint (written).**
- A row is one H1-orbit {π(γ)π(h)v} forming an orthonormal basis. So f ↦ Σ f(h)π(h)v is an H1-equivariant unitary C[H1] → C^10 (up to scale), and π|H1 ≅ Reg(H1).
- The same holds for H2 and H3.
- Hence χ_π = 0 on X = (H1 ∪ H2 ∪ H3) \ {e} and χ_π(e) = 10. This must hold for **every** v.

**Step 3: abelian Γ (written).**
- π is a sum of 10 characters S. The constraint χ_π|X = 0 means that S restricts bijectively onto each Ĥ_i.
- With K_i = H_i^⊥ being three pairwise complementary order-10 subgroups of Γ̂ ≅ Z10^2, write S = {(a, σ(a))} and K3 = graph(θ). Then a ↦ σ(a) − θ(a) must be bijective.
- So θ^{-1}σ is an orthomorphism of Z10. None exists (Hall–Paige: the Sylow-2 subgroup is cyclic and nontrivial).

**Step 4: non-abelian Γ (exact certificate).**
- Up to GL(2,5)-conjugacy and permutation of the three symmetric types, the V-actions are:
  - negI: (−I, I, −I);
  - D: (D, I, D), and also (D, D, I) was run;
  - Klein: (D, −D, −I), with D = diag(1, −1).
- All subgroup triples were enumerated: 3000 + 40 + 40 + 520 = 3600, each verified closed with trivial pairwise intersections.
- For each triple:
  - every irreducible character was built exactly, by Clifford induction from Z5^2, with values in Z[ζ5] stored as integer vectors;
  - an exact meet-in-the-middle search looked for multiplicities r_ρ ∈ [0, d_ρ] with Σ r_ρ d_ρ = 10 and Σ r_ρ χ_ρ|X = 0.
- **Result: 0 patterns in all 3600 triples.**
- Positive control: Z7^2 with three lines returns exactly the 133 orthomorphisms of Z7.

∎

## Companion statements (written, UNREVIEWED)

- **D5 × D5 with right-coset diagonal labels** (vectors π(g,h)v, label g^{-1}h). Averaging φ over a reflection class leaves the one-dimensional characters with total ±0.2 ≠ 0, for every irrep matching. So this is impossible too.
- **Projective, abelian Γ = Z10^2.** Classify by cocycle order, with H^2 ≅ Z10:
  - **Order 5.** π is a sum of two irreps W5 ⊗ λ_j. The condition χ_π(0, x_i) = 5(λ1 + λ2)(x_i) = 0 would need λ1λ2^{-1} = −1 on all three involutions. That is impossible.
  - **Order 2 (Pauli).** π = ⊕_{k=1}^5 χ_{c_k} ⊗ σ.
    - The P-conditions force ‖v_k‖² = 1/5.
    - The conditions at (q, x_i), for all q ∈ P_i, force ⟨v_k, σ_a v_k⟩ = 0 for a = X, Y, Z, so v_k = 0. Contradiction.
  - **Order 10 (Weyl(Z10) = Weyl(Z2) ⊗ Weyl(Z5)).** This class passes the representation test, so only v can obstruct it.
    - The condition is a v ∈ C^2 ⊗ C^5 unbiased to three product bases. The reduced state on C^2 must be I/2.
    - It reduces to a 2-plane W ⊂ C^5 with ‖Π_W b‖² = 2/5 on three Weyl MUBs, plus Bloch-plane conditions. That is 24 conditions on 15 real parameters.
    - **Numerical only:** over all 120 line/axis assignments with 8 LM starts each, the best residual is 0.0523; the other class gives 0.202.
- **Not covered:** non-abelian projective cocycles; non-regular symmetry groups; symmetries that permute the three types.

## Significance

Every linear group-covariant construction with a regular symmetry group fails at order 10, for every cardinality. This includes all character-based constructions of the Zhang–Cao/Huang–Li type and their non-abelian twisted analogues. A maximal 1-RQLS(10), if it exists, must be either:
- projectively covariant, where the only abelian survivor is the Weyl(Z10) fiducial problem, numerically excluded; or
- covariant under a non-regular group or none.
