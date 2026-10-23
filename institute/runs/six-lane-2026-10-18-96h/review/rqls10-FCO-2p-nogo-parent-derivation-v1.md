# Proposition FCO-2p: no FCO mate of Cay(Z_n) exists when n = 2p, p an odd prime

Recorded at 2026-10-19T06:14:50-0700. Status: **CANDIDATE_UNVERIFIED**, pending review by both model families.

Origin: read-only scout QuantumGroupTableNoGo3 ([scout record](rqls10-quantum-grouptable-nogo-scout-v3.json), sha256 `0d7a5d1810c1c0b8bcf7db52d91176cf8b16cff19d4e7f8a1e5a0fb4cab9c629`, field `theorem_comparison.FCO_no_go_n_eq_2p_INFERENCE_unreviewed`). The scout produced the proof sketch. The parent rechecked every step below and filled in the omitted details. Nothing was computed.

## Setting
- Let n ≥ 2 and ζ = e^{2πi/n}. Let π, ρ be permutations of Z_n.
- The FCO family is q_ij(t) = ζ^{tj + π(t)ρ(i)} / √n for i, j, t ∈ Z_n.
- Its B-classes are C_s = {(i, i+s)}, so B = Cay(Z_n) in the j − i convention.
- Rows and columns are always orthonormal:
  - In row i, the inner product of cells (i, j) and (i, j') is (1/n) Σ_t ζ^{t(j'−j)} = δ_{jj'}.
  - In column j, the inner product of cells (i, j) and (i', j) is (1/n) Σ_t ζ^{π(t)(ρ(i')−ρ(i))} = (1/n) Σ_u ζ^{u(ρ(i')−ρ(i))}, which is δ_{ii'} because π is a bijection and ρ is injective.
- Cells (i, i+s) and (i', i'+s) of one class have inner product (1/n) Σ_t ζ^{a t + b π(t)}, with a = i' − i and b = ρ(i') − ρ(i).
- So the family is a QLS orthogonal to Cay(Z_n) iff
  (F)  Σ_t ζ^{a t + b π(t)} = 0  for all i ≠ i'.
- Equivalently, H with H_{i,t} = ζ^{it + ρ(i)π(t)} satisfies HH* = nI. H is square, so this also gives H*H = nI:
  (F*)  Σ_i ζ^{i(t'−t) + ρ(i)(π(t')−π(t))} = 0  for all t ≠ t'.

## Proposition FCO-2p
If n = 2p with p an odd prime, then no pair (π, ρ) satisfies (F).

## Proof (parent-checked)
1. **CRT.** Let ω = e^{2πi/p} and c = 2^{−1} mod p. Then ζ^x = (−1)^x ω^{cx} for every integer x.
   - Check: 1/(2p) ≡ 1/2 + c'/p (mod 1) with c' = (1−p)/2, and 2c' = 1 − p ≡ 1 (mod p). The parity of x is well defined mod 2p.
   - For a fixed pair (i, i'), put E_t = at + bπ(t) ∈ Z_{2p}. Then Σ_t ζ^{E_t} = Σ_{v∈F_p} (M⁺_v − M⁻_v) ω^{cv}, where M^±_v = #{t : E_t ≡ v (mod p), E_t even/odd}.
   - The minimal polynomial of ω over Q is 1 + x + … + x^{p−1}, and v ↦ cv permutes F_p. So the sum vanishes iff M⁺_v − M⁻_v = κ is independent of v.
   - Summing over v gives pκ = #even − #odd ∈ [−2p, 2p], so κ ∈ {−2, …, 2}.
2. **Parity of π.** Some pair i ≠ i' has both a and b odd.
   - Otherwise every even i and odd i' would give ρ(i) ≡ ρ(i') (mod 2), so all values of ρ would share one parity. That is impossible for a permutation of Z_{2p}.
   - For such a pair, E_t ≡ t + π(t) (mod 2). Let k = #{t even : π(t) even}. Exactly 2k values of t give t + π(t) even, so #even − #odd = 4k − 2p.
   - Since p is odd, 4k − 2p ≡ 2 (mod 4). This excludes κ = 0 and κ = ±1, since pκ is then 0 or odd. Hence κ = ±2, so k ∈ {0, p}: π preserves or swaps the parity classes.
3. **Parity of ρ.** Applying step 2 to (F*), with the roles of (i, ρ) and (t, π) exchanged, shows that ρ preserves or swaps parity.
4. **Constant parity.** By steps 2 and 3, b ≡ a (mod 2) for every pair, and E_t ≡ a(t + π(t)) (mod 2) is constant in t.
   - So #even − #odd = ±2p and κ = ±2. The values E_t mod p then take every residue of F_p exactly twice, for every pair i ≠ i'.
5. **Geometry.** Let P_i = (i mod p, ρ(i) mod p) and Q_t = (t mod p, π(t) mod p) in F_p². Then E_t ≡ (P_{i'} − P_i)·Q_t (mod p).
   - If P_{i'} = P_i for some i ≠ i', then E_t ≡ 0 for every t, contradicting step 4. So the 2p points P_i are distinct.
   - A direction of F_p² that no pair determines admits at most one point on each of its p parallel lines, hence at most p points. Since 2p > p, every one of the p + 1 directions is determined.
   - For each nonzero u ∈ F_p², pick i ≠ i' with P_{i'} − P_i = λu, λ ≠ 0. Step 4 then shows that u·Q_t takes every residue exactly twice.
6. **Fourier.** Let f(x) = #{t : Q_t = x} on F_p², with total mass 2p.
   - For u ≠ 0, f̂(u) = Σ_t ω^{u·Q_t} = 2 Σ_v ω^v = 0.
   - By Fourier inversion, f ≡ f̂(0)/p² = 2/p, which is not an integer for p ≥ 3. Contradiction. ∎

## Consistency and scope
- The proposition covers n = 6, 10, 14, 22, 26, …. It agrees with the parent's exhaustive FCO enumeration ([audit](rqls10-FCO-parent-run-v1/), which found 0 solutions at n = 10 and 0 at n = 6) and with the Ball–Simoens order-6 result.
- It does not cover n = 8, where the 0 count rests on enumeration only, or n = 2m with m odd composite.
- Scope: one restricted family (Fourier–permutation vectors with a row relabelling) and B = Cay(Z_n) only. It says nothing about unrestricted QLS mates of Cay(Z_10) or Cay(D_5), and nothing about 1-RQLS(10), which remains UNKNOWN.
- No novelty or priority claim. The scout calibrates the argument as a short specialist argument that may be folklore.
