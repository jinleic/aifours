# Parent disposition - four-qubit depolarizing: exact parameter mirror, sharp t3 bound and one-uniform k3 gap (f5)

Observed native clock before writing: **2026-10-28T17:27:26-0700 PDT**. Same-harness written support; not formal/kernel, human, configured-family or novelty acceptance. Frontier-first direction: [contract addendum 2](../contract-addendum-2-frontier-first-owner-direction-v1.json).

## Complete reads by Main

| Input | SHA-256 | LF | Read |
|---|---|---|---|
| Candidate `frontier-20261028-01-spectral-mirror.md` (PhysicsDepol4-2) | `4fb86d219a99daf54cbe7ab6c37a6a7fbd11c40009879d63ae135c5195cb4b1c` | 63 | complete |
| Candidate `frontier-20261028-06-erasure-certificate.md` | `d33fa3cad8f26408e876163d975eb023821b6ab60bea8f220f82bfd1a73d5e2a` | 64 | complete |
| Candidate `frontier-20261028-08-one-uniform-proof.md` | `980d9f111f3fb685dfec9449b8bfcb325f3761a19ec91bea0615401d7d46cb38` | 62 | complete |
| Review `frontier-review-f5-depol-one-uniform-v1.md` (PhysicsMOQLS8-2) | `4cbd0cb18265b502faf4f3c1b3a9a632591290d7917031505fcccf451963d425` | 159 | raw 1-159 through ending |
| Assignment `review-waves/f5-depol-one-uniform/assignment-v1.json` | `ab8da34d00ac4051ab000cbc29b828cebb09724f368eb68a6f9453aecfaf9a66` | 32 | frozen before dispatch |

## Adopted statements (exact scope)

Let Φ_p(X) = (1-p)X + (p/2)Tr(X) I_2, Λ_p = Φ_p^{⊗4}, 0 <= p <= 4/3, Y = σ_y^{⊗4}, E_i(X) = (I_i/2) ⊗ Tr_i X, T_m = Σ_{|S|=m} E_S(ρ), t_m = Tr(P T_m), R_3(p) = a⁴ + 2a³b with a = (1+|1-p|)/2, b = (1-|1-p|)/2.

1. **Exact mirror.** For every four-qubit operator X and p in [1, 4/3], p' = 2-p: Λ_p(X) = Y Λ_{p'}(X)^T Y. Hence output spectra at p and p' coincide for every density, Tr[PΛ_p(ρ)] = Tr[(Y P^T Y) Λ_{p'}(ρ)] with P -> Y P^T Y a bijection of complex rank-3 projectors, R_3(p) = R_3(p'), and the original k=3 claim on [0, 4/3] is equivalent to the claim on [0,1] (likewise every Ky-Fan index).
2. **Sharp three-erasure bound.** For every density ρ and complex rank-3 projector P, t_3 <= (12 + r_1 + r_2 + 3r_3 + 3r_4)/16 <= 5/4, r_i the sorted Bloch lengths; equality forces all r_i = 1, i.e. a pure product input. The product reference ρ_* = |0000><0000|, P_* = span{|0000>,|1000>,|0100>} has layers (1, 3, 3, 5/4, 3/16) and attains R_3(p) for every p in [0,1]. Sufficient (unproved) global certificate: t_1 <= 3 and t_2 <= 3 for all actual pairs would give the full k=3 bound.
3. **One-uniform convex-hull gap.** For every ρ in the convex hull of pure four-qubit states whose four one-qubit marginals are exactly I/2, every complex rank-3 projector P and every p in [0, 4/3], with s = min(p, 2-p): Tr[PΛ_p(ρ)] <= R_3(p) - (1/2)s²(1-s). Proof: Λ_p = Σ_m (1-p)^{4-m} p^m T_m; for pure one-uniform inputs t_0 <= 1, t_1 <= 3 (each E_i(ρ) has four eigenvalues 1/4), t_3 = 3/4 (T_3 = I/4), t_4 = 3/16; the spin-flip operator identity Y ρ^T Y = T_0 - 2T_1 + 4T_2 - 8T_3 + 16T_4 with the SAME P gives 4t_2 <= 1 + 6 + 6 - 3, so t_2 <= 5/2; coefficientwise comparison with (1,3,3,5/4,3/16) gives gap >= (1/2)p²(1-p)² + (1/2)p³(1-p) = (1/2)p²(1-p) on [0,1]; affinity extends to mixtures, the mirror to [1, 4/3].

## Parent verification

Main hand-verified: σ_y X^T σ_y = Tr(X)I - X entrywise; S(Φ_{2-p}(X)) = Φ_p(X); R_3 formula at p = 0, 1; the sixteen eigenvalues (4 + Σ ε_i r_i)/16 of T_3 and the top-three sum (12 + r_1 + r_2 + 3r_3 + 3r_4)/16 (equivalently (6 + (3/2)(δ_(3)+δ_(4)) + (1/2)(δ_(1)+δ_(2)))/8); the Schmidt argument for t_1 <= 3; T_3 = I/4 under one-uniformity; the sign pattern of Π_i(2E_i - Id); the t_2 <= 5/2 derivation; and the coefficientwise gap sum (1/2)p²(1-p). Reviewer verdict NO_SUBSTANTIVE_DEFECT, 0F/0M/0m, with an independent exact Gaussian-rational verifier (512 matrix-unit mirror checks at two p values, exact spin-flip identity on two complex one-uniform states and a mixture, exact layer traces) treated as diagnostic.

## Not established

The original all-density k=3 majorization; t_1 <= 3 or t_2 <= 3 for general densities; any statement for mixed inputs with maximally mixed marginals outside the stated convex hull (the later Bloch-gap candidates are separately under review f23); novelty (NR). The historical L1 quarantine for this slot remains a historical record, not a premise.
