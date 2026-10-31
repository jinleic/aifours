# A source-independent separable CP component for every global qubit input

**PhysicsResearch96h-2 / physics-1.** Native clock before writing: Wed Oct 28 21:00:27 PDT 2026. This is a WRITTEN all-variable, source-independent partial theorem about the **actual three-site map**. It provides a positive separable component for every admissible reference-qubit input, but it does **not** prove the remaining component is PPT or solve the original q3 target. No chosen physical state/control or numerical parameter is tested; no source novelty, operational distillability, parent/f62, human/family or formal/Lean acceptance is claimed.

## 1. Exact completely positive decomposition

On M4(C) define the linear maps

`D(X)=Tr(X)I4`, `K(X)=Tr(X)I4−X^T`,
`Psi(X)=Tr(X)I4−X^T/2 = (D+K)/2`.

D and K are completely positive. Their explicit finite Kraus representations are

`D(X)=Σ_(i,j) E_ij X E_ij†`,
`K(X)=Σ_(i<j)(E_ij−E_ji) X (E_ij−E_ji)†`.

Let D_i,K_i,Psi_i act on the corresponding factor of H=(C⁴)^tensor3. Exact expansion gives

`Psi_1⊗Psi_2⊗Psi_3
 = (1/12) Σ_i [Psi_i⊗D_j⊗D_k] + R`,                    (1)

where in each summand `{i,j,k}={1,2,3}` and

`R = (1/12) Σ_i [K_i⊗D_j⊗D_k]
   + (1/8) Σ_(i<j) [K_i⊗K_j⊗D_k]
   + (1/8) [K_1⊗K_2⊗K_3]`.                             (2)

The tensor-factor order is always the original site order. Every term in R is CP. To verify the coefficients, the first sum in (1) contributes `3/24=1/8` of `D_1D_2D_3` and `1/24` of each single-K term; (2) supplies their remaining `1/12` and all pair/triple terms at1/8. Thus (1)–(2) is an exact identity, not an inequality based on a sample.

## 2. The first component is separable for the whole qubit-reference cone

Let Q=C² and let ρ be **any** PSD operator on H⊗Q, not necessarily pure, normalized or Stiefel. For every i, applying D to the other two sites gives

`(Psi_i⊗D_j⊗D_k⊗id_Q)(rho)
 = I_j⊗I_k⊗(Psi_i⊗id_Q)(rho_(iQ))`,

with tensor factors placed in their original order and `rho_(iQ)=Tr_(jk)rho>=0`.

The source-independent written lemma `frontier-20261028-d4-local-qubit-corner-eb-analytic-v1.md`, SHA256 `3589a59a3dc019da87169a63844995c63e2016167dbcf1e863a048815a96eee8`, gives a direct measure–prepare formula for `Psi_i` restricted to **every** local two-dimensional input corner. To apply it to arbitrary PSD rho_(iQ), spectrally decompose rho_(iQ) into pure terms. Every pure vector in C⁴⊗C² has local Schmidt rank<=2 and hence lies in some isometric local qubit corner; the written lemma sends each term to a PSD operator separable across output site i | Q. Their finite positive sum is separable. Tensoring the two identity factors preserves separability across the **whole physical output H | Q** cut.

Define

`S(rho)=(1/12) Σ_i (Psi_i⊗D_j⊗D_k⊗id_Q)(rho)`,
`N(rho)=(R⊗id_Q)(rho)`.

Equations (1)–(2) prove for **every** PSD rho on H⊗C²

`(Psi^tensor3⊗id_Q)(rho)=S(rho)+N(rho)`,
`S(rho) is separable across H|Q`, `N(rho)>=0`.          (3)

This is an all-variable exact positive decomposition, not a claim that the residual N is separable or PPT. It does not require a local-rank<=2 support assumption for the original global encoding: the two D factors reduce the input to an actual site-i/qubit-reference operator before the local lemma is applied.

## 3. Exact original-target gap

For the original `Phi(X)=Tr(X)I4−X/2`, one has `Phi^tensor3=T_H∘Psi^tensor3`. Taking the transpose on H in (3) gives

`(Phi^tensor3⊗id_Q)(rho)=S(rho)^(T_H)+N(rho)^(T_H)`,

with `S(rho)^(T_H)>=0` because S is separable. The exact unpaid global requirement is

`S(rho)^(T_H)+N(rho)^(T_H) >= 0`                        (4)

for all original global-isometry pure inputs rho, or an analytic bound that implies it. Positivity of N before partial transpose alone does **not** imply positivity after it. We do not assume N is PPT, assume a tensor-stability theorem, or treat (3) as a complete q3 proof. The all-subset original-index equivalence between the full q3 target and this 2-positivity problem is `frontier-20261028-d4-positive-map-all-subsets-addendum-v1.md`, SHA256 `8cd42f794b79fec63fd8d607b41554891b3b6409d75efb7278ac29c962cbf500`.

This partial theorem is a potential route for a **separate** all-global-input analytic proof; it is not a narrower subclass presented as the solution. The published source already claims the full target, and the independently checked fixed-d4 certificate is a separate conditional route. The local lemma and present theorem are unreviewed; no prior held result is a premise. Main's actual read and prospective resumption after the 19:04 cadence self-stop do not erase the earlier timing deviation, confer f62/parent acceptance or change any human/family/Lean boundary.
