# The full T2 coupling residual on both singular boundaries

**Status: WRITTEN, UNREVIEWED.** Conditional on the named unreviewed equality/saturation classifications, this packet proves the **entire** 22×22 original-pair coupling matrix is positive on every rank-two test projector where either diagonal Schur form is singular. The only remaining 8×8 contraction cases have both forms positive definite and nonzero coupling. The interior contraction is not proved; unrestricted T2, T3, Z2, the original q3 target, source correctness and novelty remain open.

Named prerequisites and exact scope:

- original 14+8 reduction `frontier-20261029-d4-t2-original-schur-block-coupling-residual-v1.md`, SHA-256 ab1c95f60443316718494d00c9591d05964ded08ea240f1209dcc9010d5127ac, UNREVIEWED;
- block-diagonal equality/kernel classification `frontier-20261029-d4-t2-schur-coupling-universal-kernel-v1.md`, SHA-256 4a17f5a24b509528d6b4238f5adf4e7ca546e53154ff697ca0b86957f7b18ff8, UNREVIEWED and dependent on the named 2+2 theorem;
- strictly upper offblock saturation classification `frontier-20261029-d4-t2-schur-coupling-offblock-kernel-v1.md`, SHA-256 392982dd141a1e71fee30b5ac9acf39cbdfd81b919224d5eaafc3cc43455082c, UNREVIEWED.

The direct product-projector inequality in Section 2 is independently written below and does not use those classifications. No numerical instance, selected physical q, executable, held input or false f198 estimate is used.

## 1. Claim and notation

For `Ψ∈C^(16×2)` with `Ψ†Ψ=I2`, define `P=ΨΨ†` and the `14+8` coefficient-space forms

`D=2I−DΨ†DΨ`, `N=2I−NΨ†NΨ`, `J=DΨ†NΨ`, `MΨ=[[D,−J],[−J†,N]]`.

`D⪰0` follows from the separately 2+2 theorem, while `N⪰0` has the direct offblock SVD proof in the third prerequisite. We prove:

**If `D` is singular OR `N` is singular, then `MΨ⪰0`.**  (1.1)

As a result, conditional on those prerequisites, unrestricted original T2 is equivalent to checking

`||D^(−1/2) J N^(−1/2)||_op≤1`

only for `Ψ` with `D>0`, `N>0`, and `J≠0`. On the singular boundaries, the Moore–Penrose version remains valid, but no limiting or continuity inference is used to claim the interior bound.

## 2. A direct product-projector dual inequality

Let `A,B∈M4(C)` be **arbitrary traceless matrices**, `v` any unit vector in the first local factor, and `Q` any rank-two orthogonal projector in the second factor. For

`X=A⊗I4+I4⊗B`, `P=|v⟩⟨v|⊗Q`, `L=||A||_F²+||B||_F²`,

we claim

`Tr(P X†X)≤2L`.  (2.1)

Put `a=⟨v,Av⟩`, `b=Tr(QB)`. Direct expansion gives

`Tr(P X†X)=2||Av||²+||BQ||_F²+2 Re(conjugate(a)b)`.  (2.2)

Complete `v` to an orthonormal basis. The trace-zero relation makes the sum of the remaining three diagonal entries of `A` equal `−a`; Cauchy–Schwarz therefore gives

`||A||_F²−||Av||² ≥ |a|²/3`.  (2.3)

For `B`, the tracezero relation says `Tr[(I−Q)B]=−b`. Both `Q` and `I−Q` have rank two, so

`||BQ||_F²≥|b|²/2`, `||B(I−Q)||_F²≥|b|²/2`.  (2.4)

Using `||B||_F²=||BQ||_F²+||B(I−Q)||_F²`, the difference between the right and left sides of (2.1) is at least

`(2/3)|a|²+(3/2)|b|²−2|ab| ≥ 0`,

since the coefficients multiply to one. This proves (2.1), including `a=0` or `b=0`; exchanging the two factors proves it for `P=Q⊗|v⟩⟨v|` as well. Thus the **full** coefficient-space quadratic form is nonnegative for every product projector of either form, not just for the saturated boundary vector that revealed it.

## 3. The `D`-singular boundary

If `D` is singular, let `x≠0` be in its kernel. Its block-diagonal pair `(Ad,Bd)` saturates the separately 2+2 T2 inequality, and `P` is a maximizing rank-two right-singular projector. The named block-diagonal equality classification gives two alternatives.

- If `σ2>σ3`, the maximizing projector is unique and commutes with all four local 2+2 sector projections. In particular it commutes with `Γ=Z_A⊗Z_B`, with `Z_A=Z_B=I2⊕(−I2)`.
- Otherwise, up to exchanging factors, `Bd=0`, `Ad` is traceless rank one, and the entire top right-singular subspace is `span{v}⊗C4`. Every maximizing `P` has the product form `|v⟩⟨v|⊗Q` with `rank Q=2`.

In the first case the diagonal tensor sum commutes with `Γ`, while each strictly upper offblock tensor term anticommutes with `Γ`. Hence `Xd†Xn` is parity odd and `Tr(P Xd†Xn)=0` for all diagonal and offblock coefficients: **`J=0`**. Since `D,N⪰0`, the full `MΨ` is PSD. In the product case, Section 2 proves the full quadratic form nonnegative for every original pair and hence in particular for every block-upper coefficient vector. Thus (1.1) holds whenever `D` is singular.

## 4. The `N`-singular boundary

If `N` is singular, take `y=(E,F)≠0` in its kernel. The named exact offblock SVD classification gives `rank E≤1`, `rank F≤1`.

If only one offblock is nonzero, its maximizing rank-two projector is exactly a product projector `|v⟩⟨v|⊗Q` or its swap. Section 2 applies to the **full** coupling quadratic form.

If both are nonzero, write the two offblock factors as `a|u⟩⟨v|`, `b|p⟩⟨q|`, with `u,p` in the first local blocks and `v,q` in the second. The unique maximizing projector is the sum of the projectors onto

`|v q⟩`, `(b|u q⟩+a|v p⟩)/√(a²+b²)`.

The first vector is `Γ`-even and the second `Γ`-odd; hence `P` commutes with `Γ`. The same parity argument as in Section 3 gives `J=0`, so `MΨ⪰0`. This proves (1.1) on the `N`-singular boundary, including its intersection with the `D`-singular boundary.

## 5. Exact remaining obligation

The prior two kernel packets give the Moore–Penrose support identities. This packet goes further only at **singular** `D` or `N`. If both are positive definite, the full matrix is PSD exactly when

`I−(D^(−1/2) J N^(−1/2))†(D^(−1/2) J N^(−1/2)) ⪰0`.

The `J=0` subcase is automatic. The general `D>0,N>0,J≠0` contraction, uniformly over every rank-two `P`, is the **sole remaining algebraic inequality in this reduction** and is unproved. No assertion is made that the difficult region is empty, bounded away from the singular boundary, numerically validated, physically false or automatically handled by the boundary. All prior packet bytes, STOP/HOLD/ZERO restrictions and review scopes remain unchanged.
