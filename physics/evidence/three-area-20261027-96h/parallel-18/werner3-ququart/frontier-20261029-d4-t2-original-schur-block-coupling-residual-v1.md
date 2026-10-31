# An exact 14+8 Schur-block coupling residual for the full original T2 quantifiers

**Status: WRITTEN, UNREVIEWED.** This is an exact finite-dimensional reduction of the original **unrestricted** traceless-pair T2 obligation, not its solution. The diagonal-block positivity below uses the UNREVIEWED separately 2+2 theorem `frontier-20261029-d4-t2-arbitrary-2plus2-blocks-v1.md` (SHA-256 bb09c6bf442b9d497241297c57f9da678b559b5d13ee56cc871de4a6fc7f1473); the offblock positivity uses the parent-adopted f215 square-normal T2 case. The subsequent restriction of the singular-kernel boundary uses the separately UNREVIEWED strictness addendum `frontier-20261029-d4-t2-2plus2-both-squares-nonnormal-strictness-v1.md` (SHA-256 bd4e86e6922b12277dd56438d1c12674810993b9996466e3907cf31cda7f19a1). No selected numerical instance, physical q, execution, false f198 lemma, external source, or held input is used.

## 1. Full original domain and an orthogonal 14+8 split

The original all-variable obligation is

`σ1(A⊗I4+I4⊗B)²+σ2(A⊗I4+I4⊗B)² ≤ 2(||A||_F²+||B||_F²)`

for every traceless `A,B∈M4(C)`. Independent unitary Schur transformations put any such pair into the following form without changing the singular values:

`A=Ad+E↑`, `B=Bd+F↑`,

`Ad=A1⊕A2`, `Bd=B1⊕B2`, `E↑=[[0,E],[0,0]]`, `F↑=[[0,F],[0,0]]`,

where all blocks are 2×2 and `Tr A1+Tr A2=Tr B1+Tr B2=0`. Conversely all these block-upper pairs are included in the original domain. The diagonal/offblock pieces are orthogonal in Frobenius norm.

Let `Dspace` be the complex Hilbert space of pairs `(Ad,Bd)` with these trace constraints, and `Nspace=M2(C)⊕M2(C)` be the space of pairs `(E,F)` with the Frobenius inner product. Their complex dimensions are **14 and 8**. Any matrix representation below uses **orthonormal Frobenius coordinates**; in particular the scalar block-trace parameter is not silently treated as unit norm.

For an arbitrary isometry `Ψ∈C^(16×2)` with `Ψ†Ψ=I2`, define the linear maps

`DΨ(Ad,Bd)=(Ad⊗I4+I4⊗Bd) Ψ`,

`NΨ(E,F)=(E↑⊗I4+I4⊗F↑) Ψ`.

The target space has its ordinary Frobenius inner product. Write

`D=2I_Dspace−DΨ†DΨ`, `N=2I_Nspace−NΨ†NΨ`, `J=DΨ†NΨ`.  (1.1)

For every `Ψ`, the separately 2+2 theorem gives `D⪰0`: a fixed rank-two isometry cannot exceed the sector's top-two squared singular sum. Independently, `(E↑)²=(F↑)²=0`, so the f215 square-normal case gives `N⪰0`. Both conclusions are universal over the coefficient vectors and `Ψ` at their stated written-assurance scopes.

## 2. Exact residual and singular case

By the Ky Fan variational formula, original T2 holds for all pairs iff, for **every** `Ψ`, the Hermitian `22×22` block operator

`MΨ = [[D,−J],[−J†,N]]`

is positive semidefinite on `Dspace⊕Nspace`. Indeed its quadratic form is exactly

`2(||Ad||_F²+||Bd||_F²+||E||_F²+||F||_F²) − ||DΨ(Ad,Bd)+NΨ(E,F)||_F²`.

No block-upper case is dropped: independent Schur conjugation transforms `Ψ` along with the tensor-sum matrix, and the condition quantifies over all isometries.

Since `D⪰0`, the following two conditions are **together necessary and sufficient** for `MΨ⪰0`:

1. `ker D ⊆ ker J†`, equivalently `range J⊆range D`;
2. `N−J†D⁺J ⪰ 0` on the **8-dimensional** offblock space, with `D⁺` the Moore–Penrose inverse.  (2.1)

For completeness, the range condition ensures `DD⁺J=J` and permits the exact completion of the square

`⟨x,Dx⟩−2 Re⟨x,Jy⟩+⟨y,Ny⟩`

`= ||D^(1/2)(x−D⁺Jy)||²+⟨y,(N−J†D⁺J)y⟩`.

If the range condition fails, choose `x∈ker D` and `y` with `Re⟨x,Jy⟩≠0` after a phase change; varying their relative real scale makes the quadratic form negative. In particular, neither `D⪰0` and `N⪰0` by themselves nor a formula omitting the kernel condition pays the residual. At nonsingular `D` the first condition is automatic, but no global invertibility is assumed.

**Exact remaining task:** establish both (2.1) conditions for all isometries, or produce an admissible original-domain failure. This packet proves neither condition globally. This is an 8-dimensional **operator inequality depending on the full 16×2 isometry**, not an asserted 8-variable optimization independent of `Ψ`.

## 3. The first unpaid condition as two concrete partial-trace identities

Let `x=(Ad,Bd)∈ker D`, set `Xd=Ad⊗I4+I4⊗Bd`, and let `P=ΨΨ†`. Since `D⪰0`,

`x∈ker D  ⇔  ||Xd Ψ||_F²=2(||Ad||_F²+||Bd||_F²)`.

The diagonal theorem and the rank-two variational bound then force `S2(Xd)=2(||Ad||²+||Bd||²)` and make `P` a maximizing rank-two right-singular projector. Conversely such a saturated pair/projector gives `x∈ker D`.

Let `Π1,Π2` denote the first and second local 2-dimensional block projections in the appropriate local factor. Direct Frobenius duality shows that `J†x=0` is exactly the pair

`Π1 Tr_B(Xd P) Π2=0`, `Π1 Tr_A(Xd P) Π2=0`.  (3.1)

For example, the coefficient of `E` in the cross form is `Tr[E↑† Tr_B(Xd P)]`; the coefficient of `F` is the analogous partial trace over `A`. Thus condition 1 in (2.1) amounts to proving (3.1) for **every saturated block-diagonal pair and every maximizing rank-two projector**. This is the precise first unpaid algebraic premise; it is not inferred merely because each diagonal quadratic form is nonnegative.

If a genuine violation of (3.1) were found, choosing offblocks aligned with the nonzero cross form and taking a suitable nonzero real scale would make the full quadratic form negative, because the diagonal part starts at zero and the offblock cost is quadratic. No such violation or original counterexample is claimed here.

## 4. Proven reductions of the kernel-boundary search

Two independent exact reductions apply, but do not solve (3.1).

**Sector-diagonal projector.** `Xd` preserves the four 2×2-by-2×2 sectors. If `P` commutes with all four sector projections, then `Xd P` is sector-block-diagonal, and both partial traces in (3.1) are local 2+2 block-diagonal. Thus both upper-right blocks vanish.

**No cutoff degeneracy.** If `σ2(Xd)>σ3(Xd)`, the maximizing rank-two projector is the unique spectral projector of `Xd†Xd` above the cutoff. The latter Gram matrix is sector-block-diagonal, so its unique top-two spectral projector commutes with all sector projections. Hence (3.1) is automatic. Any nonzero saturated kernel vector that still needs (3.1) can occur only at the cutoff-degenerate boundary `σ2=σ3`; degeneracy alone is not a counterexample.

**Square-normal boundary, conditional on the strictness addendum.** The 2+2 equality analysis proves `S2(Xd)=2(||Ad||²+||Bd||²) ⇒ Ad² or Bd² normal`. Consequently every saturated nonzero kernel vector lies on the f215 square-normal locus. This does not imply that the cross identities (3.1) hold there, and does not imply the residual 8×8 inequality.

## 5. Exact scope

The split and Schur-complement equivalence are elementary written linear algebra. The assertions `D⪰0`, `N⪰0` and the equality-boundary reduction use, respectively, the named unreviewed 2+2 candidate, adopted f215, and named unreviewed strictness addendum; they are not given broader assurance. The global kernel identities and `N−J†D⁺J⪰0` remain open. There is no source, target, Lean/kernel, executable, independent-family/human, novelty, unrestricted T2, T3, Z2, or q3 conclusion, and no f274 `η>2L` or physical counterexample claim.
