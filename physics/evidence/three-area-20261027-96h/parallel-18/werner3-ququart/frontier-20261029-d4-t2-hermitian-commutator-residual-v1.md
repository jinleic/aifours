# The full original T2 residual as a marginal commutator inequality

**Status: WRITTEN, UNREVIEWED.** This is an exact all-variable reduction of the original traceless 4×4 T2 obligation; it is **not** its proof. It isolates the genuinely nonnormal coupling between Hermitian and anti-Hermitian local components, without a local-normal or magnitude hypothesis on the original factors. All needed normal-pair facts are reconstructed below. The optional one-negative-mode observation at the end additionally uses the separately UNREVIEWED tracezero rank-two dual theorem `frontier-20261029-d4-t2-traceless-dual-strict-chiral-consolidated-v2.md` (SHA-256 b96fcf9f42e0762132d7b843149f424fcde28bd978439b144f3196e09e34efb5). There is no numerical/physical-q sample, program, external source, false f198 estimate, held/ZERO input or novelty claim.

## 1. Exact real and imaginary parts of the full gap

Fix an arbitrary rank-two projector `P` on `C4⊗C4`, and denote its local marginals by `ρ=Tr_B P`, `τ=Tr_A P`. Each is positive semidefinite with trace two. Let `V` be the **real** 30-dimensional Hilbert space of pairs `H=(A_H,B_H)` of traceless Hermitian 4×4 matrices with inner product

`⟨H,K⟩=Tr(A_H A_K)+Tr(B_H B_K)`.

Write `X_H=A_H⊗I4+I4⊗B_H`. For `H,K∈V`, define

`K_P(H,K)=2⟨H,K⟩−(1/2)Tr[P{X_H,X_K}]`,

`J_P(H,K)=(1/2i)[Tr(ρ[A_H,A_K])+Tr(τ[B_H,B_K])]`.  (1.1)

`K_P` is real symmetric and `J_P` is real skew-symmetric. For **arbitrary complex** original factors `A=A_H+iA_K`, `B=B_H+iB_K`, their tensor sum is `X=X_H+iX_K`, and `[X_H,X_K]=[A_H,A_K]⊗I4+I4⊗[B_H,B_K]`. Therefore the exact original dual gap is

`2(||A||_F²+||B||_F²)−Tr(PX†X)`

`=K_P(H,H)+K_P(K,K)+2J_P(H,K)`.  (1.2)

There is no hidden cross-factor commutator: the two local tensor algebras commute. The entire imaginary/nonnormal coupling depends on `P` **only through the two marginals**; the real variance form still depends on the full projector.

## 2. Positivity of the real form and its singular-kernel condition

For every `H∈V`, `X_H` is Hermitian and diagonalizable in a product eigenbasis. Let `a,b∈R4` be the tracezero eigenvalue vectors of its local factors. For any two **distinct** tensor positions `(i,j),(k,l)`, the two evaluation functionals `(a,b)↦(a_i+b_j,a_k+b_l)` on the tracezero Hilbert space have Gram matrix

`[[3/2,κ],[κ,3/2]]`, `κ=δik+δjl−1/2∈{−1/2,+1/2}`.

Its top eigenvalue is `2`, so the sum of the two largest squared eigenvalue magnitudes of `X_H` is at most `2||H||²`. Any rank-two `P` gives no larger trace, proving **`K_P⪰0`**.

Moreover, if nonzero `H∈ker K_P`, equality holds throughout. The top Gram eigenvalue `2` is simple. If the two positions differ in both indices, equality forces, up to a real scalar `t`, `a=t(e_i−e_k)`, `b=t(e_j−e_l)`. If they share the A index, it forces `a=t(2e_i−1/2·1)`, `b=t(e_j+e_l−1/2·1)`; the shared-B case is symmetric. In every nonzero case the two largest absolute eigenvalues have modulus `2|t|` and **all** others have modulus at most `|t|`. Thus `σ2(X_H)>σ3(X_H)` and the maximizing `P` is the unique projector onto those two product eigenvectors.

In particular `ρ` commutes with `A_H` and `τ` commutes with `B_H`. Cyclicity of trace in (1.1) then gives `J_P(H,K)=0` for every `K∈V`. Hence

**`ker K_P⊆ker J_P`.**  (2.1)

This pays the singular range condition; it is not a proof that the full complex form is nonnegative.

## 3. The exact unpaid weighted commutator

Let `𝒦_P` and `𝒥_P` be the real Riesz operators of the two forms. The latter is explicitly

`𝒥_P(A_K,B_K)=([A_K,ρ]/(2i), [B_K,τ]/(2i))`.  (3.1)

It is real skew-adjoint and depends only on `ρ,τ`. On the support of `𝒦_P`, set

`T_P=𝒦_P^(+1/2) 𝒥_P 𝒦_P^(+1/2)`.

The Moore–Penrose square root is well defined even when `𝒦_P` is singular; (2.1) gives the required range compatibility. Completing the square, or taking the Schur complement of the real block matrix `[[𝒦_P,𝒥_P],[−𝒥_P,𝒦_P]]`, proves the exact equivalence

`K_P(H,H)+K_P(K,K)+2J_P(H,K)≥0 for all H,K`

`⇔  |J_P(H,K)|²≤K_P(H,H)K_P(K,K) for all H,K`

`⇔  ||T_P||_op≤1`.  (3.2)

The middle condition includes all zero-denominator cases by (2.1). Therefore the original T2 problem is **exactly** to prove (3.2) for **every** rank-two `P`. This weighted commutator inequality is entirely **UNPAID**; the fact that the real diagonal form is PSD does not prove it.

## 4. Marginal geometry and a warning

In a local eigenbasis of `ρ`, the real skew operator on the A factor rotates the two Hermitian directions belonging to an offdiagonal index pair with magnitude `|ρ_i−ρ_j|/2`; the B factor is analogous. Thus

`||𝒥_P||_op = (1/2) max{diam spec(ρ),diam spec(τ)} ≤1`.  (4.1)

The bound uses only `ρ,τ⪰0` and `Trρ=Trτ=2`. Equality in (4.1) occurs only if a marginal has an eigenvalue two, which forces the full projector to be `|v⟩⟨v|⊗Q` or its swap with `rank Q=2`; conversely such a product projector attains the unweighted norm one. Those product-projector physical inequalities were separately proved in `frontier-20261029-d4-t2-schur-coupling-singular-boundary-v1.md` (SHA-256 76d6ea5ef50e93619454f4190781595884d435df54746f067965b81655d2438c), not imported for (3.2).

The trace-functional direction `h_P=(ρ−I4/2,τ−I4/2)` lies in `ker 𝒥_P`, since each marginal commutes with itself. **Neither `||𝒥_P||≤1` nor `h_P∈ker𝒥_P` implies `||T_P||≤1`**: the real form `𝒦_P` may have arbitrarily small eigenvalues on its support, and both sides of the weighting matter.

If the separately UNREVIEWED tracezero rank≤2 dual theorem is admitted, the full complex source form has at most one negative eigenmode for each `P`. Since nonzero singular values of a real skew operator occur in pairs, this says at most one symplectic singular pair of `T_P` can exceed one. It does not show that pair is absent.

## 5. Scope

This is an all-original-pair residual, not a new normal-class physical result: Hermitian pairs are used only to form the two real halves of arbitrary complex factors. No value of (3.2) has been evaluated, bounded by one, or solved for the nonnormal interior. No unrestricted T2/T3/Z2/q3, f274 `η>2L`, physical counterexample, executable, formal/kernel, stronger-family/human review, source-correctness or novelty claim is made. The Gram equality classification, singular kernel, operator factors and commutator signs require disjoint written review.
