# The offblock singular-kernel condition in the full T2 coupling reduction

**Status: WRITTEN, UNREVIEWED.** This proves the *second*, offblock-side range condition in the full 14+8 Schur coupling representation `frontier-20261029-d4-t2-original-schur-block-coupling-residual-v1.md` (SHA-256 ab1c95f60443316718494d00c9591d05964ded08ea240f1209dcc9010d5127ac). It also gives an independent exact proof that the offblock diagonal form is positive; it does not require the f215 bound for that fact. The other, block-diagonal-side kernel proof is in the separately UNREVIEWED `frontier-20261029-d4-t2-schur-coupling-universal-kernel-v1.md` (SHA-256 4a17f5a24b509528d6b4238f5adf4e7ca546e53154ff697ca0b86957f7b18ff8). Neither packet proves the full T2 residual.

## 1. The universal claim

For an arbitrary isometry `Ψ∈C^(16×2)`, let `DΨ,NΨ,D,N,J` be the maps and Hermitian forms defined in the coupling packet. In particular,

`NΨ(E,F)=(E↑⊗I4+I4⊗F↑)Ψ`, `N=2I−NΨ†NΨ`, `J=DΨ†NΨ`,

where `E↑=[[0,E],[0,0]]`, `F↑=[[0,F],[0,0]]` and `E,F∈M2(C)`. The new universal claim is

**`N⪰0` and `ker N ⊆ ker J` for every `Ψ`.**  (1.1)

The proof is exact all-variable written linear algebra. No numerical instance, selected physical q, execution, held input, false f198 lemma, physical counterexample or novelty claim is used.

## 2. Complete offblock singular spectrum at the top

Perform SVDs of `E,F` using independent unitaries on the first and second local 2×2 blocks. Such changes preserve the block-diagonal/offblock split. Reordering the local basis into singular pairs writes the two 4×4 offblock factors as orthogonal direct sums

`E↑ ≅ a1 E12 ⊕ a2 E12`, `F↑ ≅ b1 E12 ⊕ b2 E12`,

with `a1≥a2≥0`, `b1≥b2≥0`. The tensor sum `Xn=E↑⊗I4+I4⊗F↑` has four orthogonal 4×4 sectors

`Xij=ai E12⊗I2+I2⊗bj E12`.

Each sector has precisely two possibly nonzero squared singular values, both `ai²+bj²`: its two orthogonal rank-one pieces are the transition from `|22⟩` to `ai|12⟩+bj|21⟩` and the transition from `bj|12⟩+ai|21⟩` to `|11⟩`. Therefore

`S2(Xn)=2(a1²+b1²) ≤ 2(a1²+a2²+b1²+b2²) = 2(||E||_F²+||F||_F²)`.  (2.1)

For every `Ψ`, `||XnΨ||²≤S2(Xn)`, proving `N⪰0`. A nonzero `(E,F)` lies in `ker N` iff equality holds throughout (2.1) and `P=ΨΨ†` is a maximizing rank-two right-singular projector. Equality requires

`rank E≤1`, `rank F≤1`.  (2.2)

This classification includes either factor equal to zero.

## 3. Partial-trace orthogonality at saturation

Assume first that both offblock factors are nonzero. Write

`E↑=a |u⟩⟨v|`, `F↑=b |p⟩⟨q|`, `a,b>0`,

where `u,p` lie in their respective first local 2-blocks and `v,q` in their second blocks; in particular `u⊥v` and `p⊥q`. The active sector in Section 2 has its two top squared singular values equal to `a²+b²`, strictly exceeding all singular values in the other sectors. Hence its maximizing rank-two projector is unique and has orthonormal spanning vectors

`|v q⟩`, `w=(b|u q⟩+a|v p⟩)/√(a²+b²)`.

Let `P` be that projector. Since `Xn|v q⟩=a|u q⟩+b|v p⟩` and `Xn w=√(a²+b²)|u p⟩`, direct expansion yields

`Tr_B(Xn P)=2E↑`, `Tr_A(Xn P)=2F↑`.  (3.1)

Both matrices are strictly upper local 2×2 offblocks and therefore Frobenius-orthogonal to **every** tracezero block-diagonal local coefficient. Consequently `DΨ†NΨ(E,F)=J(E,F)=0`.

If `F=0` and `E↑=a|u⟩⟨v|` has rank one, its top right-singular subspace is `span{v}⊗C4`, and every maximizing rank-two projector is `P=|v⟩⟨v|⊗Q` with `rank Q=2`. Then `Tr_B(XnP)=2E↑` and `Tr_A(XnP)=Tr(E↑)Q=0`, again orthogonal to the block-diagonal space. The `E=0` case is symmetric; the zero coefficient vector is trivial. This proves `ker N⊆ker J` for all `Ψ`.

## 4. Exact residual with both support conditions

Combine (1.1) with the **separately UNREVIEWED** result `ker D⊆ker J†` from the named block-diagonal kernel packet. Both `D,N` are positive semidefinite, with `range J⊆range D` and `J` vanishing on `ker N`. The singular Schur complement therefore gives, for each `Ψ`,

`N−J†D⁺J⪰0  ⇔  ||D^(+1/2) J N^(+1/2)||_op≤1`,  (4.1)

where `D^(+1/2),N^(+1/2)` are the positive square roots of the Moore–Penrose inverses and the norm is on their finite-dimensional support spaces. To see this, use the two range conditions to factor the left side as

`N^(1/2) [I−(D^(+1/2) J N^(+1/2))†(D^(+1/2) J N^(+1/2))] N^(1/2)`.

The full original unrestricted T2 statement remains equivalent to (4.1) **for every** `Ψ∈C^(16×2)` with `Ψ†Ψ=I2`, conditional on the separately named 2+2 and kernel proofs. The 8×8 contraction inequality is entirely **UNPAID** here; the two kernel conditions and positive diagonal forms do not imply it. There is no unrestricted T2, T3, Z2, q3, η-failure, formal/kernel, external-review or novelty conclusion.
