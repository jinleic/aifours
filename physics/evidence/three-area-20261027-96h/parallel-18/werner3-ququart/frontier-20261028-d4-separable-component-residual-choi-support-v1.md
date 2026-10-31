# Exact Choi support of the three-site separable-component residual

**PhysicsResearch96h-2 / physics-1.** Native clock before writing: Wed Oct 28 21:03:25 PDT 2026. This is a WRITTEN, source-independent structural theorem for the **actual residual CP map** from `frontier-20261028-d4-global-separable-cp-decomposition-v1.md`, SHA256 `07cba1eace84a037efa9784117e4ef91d952b8cdb0cce529a7581fa223a9664d`. It does not test a selected physical state/control, prove residual PPT or original q3, or imply source novelty/review/operational acceptance.

## 1. Actual residual and Choi operators

Use `D(X)=Tr(X)I4`, `K(X)=Tr(X)I4−X^T`, and the previously proved exact CP decomposition

`Psi^tensor3=(1/12)Σ_i Psi_i⊗D_j⊗D_k + R`,

`R=(1/12)Σ_i K_i⊗D_j⊗D_k
   +(1/8)Σ_(i<j) K_i⊗K_j⊗D_k
   +(1/8) K_1⊗K_2⊗K_3`.

Every tensor is in the original three-site order. For the unnormalized input⊗output Choi convention, a direct matrix-unit sum gives

`J(D)=I_4⊗I_4`, `J(K)=I_4⊗I_4−F = 2 P_-`,

where F swaps the local input/output factors and `P_-=(I−F)/2` projects onto their antisymmetric subspace. Put `P_+=(I+F)/2`, the symmetric projection. Both are orthogonal PSD projectors.

After the fixed tensor-factor regrouping from three local input/output pairs to total input⊗output, `J(R)` is the sum of the displayed R coefficients with each D replaced by I and each K replaced by `2P_-`. In particular, every term is PSD and the single-K terms contain a **positive coefficient** times each of `P_-,1⊗I⊗I`, `I⊗P_-,2⊗I`, `I⊗I⊗P_-,3`.

## 2. Entire kernel and rank, without selected states

For PSD operators, a vector lies in the kernel of their sum iff it lies in the kernel of each summand: `x†(Σ A_i)x=0` forces every nonnegative `x†A_i x=0`. Therefore the single-K terms force

`ker J(R) ⊂ ker P_-,1 ∩ ker P_-,2 ∩ ker P_-,3
          = Sym²(C⁴)⊗Sym²(C⁴)⊗Sym²(C⁴)`.

Conversely, every vector in this triple-symmetric subspace is annihilated by **every** term of J(R), because every term has at least one K/P_- factor. Hence equality holds exactly.

The local symmetric subspace has dimension `4·5/2=10`; the full Choi space has dimension `(4²)^3=4096`. Thus

`dim ker J(R)=10³=1000`, `rank J(R)=4096−1000=3096`.

The statement is on an **operator source space** and is valid for the entire exact residual map; no physical target C, input ρ, state value or spectral-boundary probe is selected.

## 3. What this does and does not buy for original q3

For any PSD rho on the original H⊗Q with Q=C², the earlier all-input theorem gives

`(Psi^tensor3⊗id_Q)(rho)=S(rho)+N(rho)`,

with S separable across H|Q and N=(R⊗id_Q)(rho)>=0. The present result identifies the full **Choi support** of the CP map producing N and shows every Kraus contribution can be taken inside the span of terms carrying at least one local antisymmetric input/output component.

It does **not** establish that `N(rho)^(T_H)` is PSD or bounded below by `−S(rho)^(T_H)`. Choi support is a different bipartition/condition from the output-H versus reference-Q PPT requirement. Thus it does not prove or disprove original q3, global tensor EB or any strict gap. The separately checked public-source d4 certificate is the existing conditional full-target route; no all-d, physical distillability, source novelty, parent/f62, human/family or formal/Lean acceptance is inferred.

All steps are symbolic and all-variable; no old held outcome is a premise. The earlier disclosed 20/30-minute cadence gaps remain in `frontier-20261028-1904-cadence-breach-self-stop-v1.json`, SHA256 `8b794de4b92c3a50b497333ac1164ddb3800b17c9a8aa541eae57b104c60d24e`; no retrospective continuous supervision or f62 scope extension follows.
