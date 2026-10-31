# Strict T2 for every separately 2+2-reducing pair with both squares nonnormal

**Status: WRITTEN, UNREVIEWED additive successor.** This proof uses the same-owner 2+2 theorem packet `frontier-20261029-d4-t2-arbitrary-2plus2-blocks-v1.md` (SHA-256 bb09c6bf442b9d497241297c57f9da678b559b5d13ee56cc871de4a6fc7f1473), including its elementary two-qubit lemma and four-sector proof. It is conditional on that unreviewed written derivation and does not edit or alter any previously frozen scope. No numerical instance, chosen physical q, execution, held input, f198 false estimate, physical q3 or novelty claim is used.

## 1. The all-variable result

Let traceless `A,B∈M4(C)` each be unitarily reducible into two arbitrary 2×2 blocks. Put `X=A⊗I4+I4⊗B`, `L=||A||_F²+||B||_F²`, and `S2=σ1(X)²+σ2(X)²`. Then

**`S2=2L` implies `A²` is normal or `B²` is normal.**  (1.1)

Equivalently, in this entire separately 2+2-reducing class, **if both `A²` and `B²` are nonnormal then `S2<2L`**, with no small-parameter, norm-threshold, reality, normal-factor or genericity hypothesis. This proves a uniform strict T2 class on the actual both-squares-nonnormal side of the f215 structural boundary. It does not prove that any such point is outside the whole f274 `η≤2L` region: that all-bases comparison is still unpaid. It is not a proof of unrestricted T2, T3, Z2, q3 or source correctness.

Work in separate reducing bases and write

`A=(αI2+C1)⊕(−αI2+C2)`, `B=(βI2+D1)⊕(−βI2+D2)`,

where all `Cr,Ds` are traceless. The four sectors are

`Xrs=(εrα+εsβ)I4+Cr⊗I2+I2⊗Ds`, `ε1=1`, `ε2=−1`.

Every traceless 2×2 matrix `T` satisfies `T²=−det(T) I2`. Consequently, if `α=0`, then `A²` is a direct sum of scalar matrices and is normal; similarly `β=0` makes `B²` normal. We may assume `L>0`, since `A=B=0` is trivial.

## 2. Equality in the two-qubit lemma forces a normal second factor

We first isolate the precise equality property needed below. For traceless `C,D∈M2` and `t∈C`, the preceding packet proves

`||tI4+C⊗I2+I2⊗D||_op² ≤ 4|t|²+||C||_F²+2||D||_F²`.  (2.1)

**Claim.** If equality holds in (2.1), then `D` is normal. The all-zero input is trivial.

Choose maximizing unit vectors `u,v` for the matrix element of the left side. In Schmidt bases for `u`, let its coefficient matrix be `U=diag(a,b)`, with `a,b≥0`, `a²+b²=1`, and write `V=[[p,q],[r,w]]` for the coefficient matrix of `v`. Put `s=Tr(U†V)` and `h=||VU†||_F²`. The proof of (2.1) factors through weighted Frobenius Cauchy–Schwarz and the bound

`|s|²/4+||M0||_F²+||N0||_F²/2 = (1+h−|bp+aw|²)/2 ≤ 1`,

where `M=VU†`, `N=Vᵀ conjugate(U)` and subscript `0` denotes traceless part. Equality in (2.1) forces equality at every step, in particular `h=1`. But

`h=a²(|p|²+|r|²)+b²(|q|²+|w|²)`,

and the two column norms of `V` sum to one. Thus `h=1` is possible only if one of `a,b` is one, the other is zero, and `V` is supported entirely in the same column of `U`. Hence **both `u` and `v` are product vectors with the same second-factor unit vector**. In those local bases `N` is `s` times a rank-one orthogonal projector, up to a transpose, and `N0` is a complex multiple of a Hermitian traceless matrix.

Equality in the weighted Frobenius Cauchy–Schwarz step makes `D` a complex scalar multiple of `N0†`; when `N0=0`, equality forces `D=0`. In all cases `D` is normal. Reversing the two tensor factors gives the symmetric statement for the bound with coefficients `2||C||²+||D||²`.

## 3. Equality when the two selected singular values are in one sector

For the chosen sector, the previous proof bounds their sum by `||Xrs||_F²` and then by `2L`. Equality throughout forces

- `rank Xrs≤2`;
- `εr α=εs β` (equality in `|εrα+εsβ|²≤2(|α|²+|β|²)`);
- `C_{3−r}=0` and `D_{3−s}=0`.

If the matched scalar is zero, `α=β=0` and both `A²,B²` are normal, as observed above. Otherwise set `t=εrα+εsβ≠0`, `C=Cr`, `D=Ds`. We claim **if both `C,D` are nonnormal, then**

`rank(tI4+C⊗I2+I2⊗D)≥3`.  (3.1)

Let the eigenvalues of `C` be `±λ` and those of `D` be `±μ`, in `C`. If `λμ≠0`, both matrices are diagonalizable, and the four eigenvalues of the tensor sum are `t±λ±μ`. Since `t≠0` and both `λ,μ` are nonzero, no two distinct sign choices can both give zero: subtracting their equations would force `λ=0` or `μ=0`, or adding opposite-sign equations would force `t=0`. Thus the nullity is at most one.

If `λ=0`, nonnormality of `C` means that `C` is a nonzero nilpotent of rank one. When `μ≠0`, diagonalize `D` by a similarity; the tensor sum is similar to the direct sum of `(t+μ)I2+C` and `(t−μ)I2+C`. At most one scalar `t±μ` vanishes, and a vanishing block has rank one while the other is invertible; hence the total rank is at least three. The case `μ=0`, `λ≠0` is symmetric. If `λ=μ=0`, the two commuting tensor summands are nilpotent, their sum is nilpotent, and its nonzero scalar shift is invertible. This proves (3.1).

Since `rank Xrs≤2`, at least one of `C,D` is normal. If `C` is normal, then `A²` is the direct sum of the normal block `(α²−det C)I2+2εrα C` and a scalar block; hence `A²` is normal. The same reasoning with `D` gives normal `B²`.

## 4. Equality in two sectors sharing a row or column

If the selected sectors share row `r`, the previous proof applies (2.1) to `Xr1` and `Xr2` separately, adds the two bounds, and then adds the nonnegative unused term `2||C_{3−r}||²`. Equality in `S2=2L` forces equality in both applications of (2.1). By Section 2, **both `D1,D2` are normal** (including a zero sector). Therefore each block `±βI2+Ds` is normal, and `B`, hence `B²`, is normal.

For two sectors in the same column, use the swapped-coefficient version of the same lemma. Equality forces both `C1,C2` normal, so `A` and `A²` are normal.

## 5. Equality in two sectors in different rows and columns

Let `Ai=εiαI2+Ci`, `Bj=εjβI2+Dj`, `ai=||Ai||_op`, `bj=||Bj||_op`. For the two selected sectors the earlier proof uses

`||Xrs||_op≤ar+bs`, `||Xr′s′||_op≤ar′+bs′`,

`(ar+bs)²+(ar′+bs′)²≤2(ar²+ar′²+bs²+bs′²)≤2L`.

Equality forces each involved block to satisfy `||Ai||_op=||Ai||_F` and `||Bj||_op=||Bj||_F`; hence every one has rank at most one. It also forces `ar=bs` and `ar′=bs′`.

If a paired norm is zero, both blocks in that sector are zero and normal. Otherwise write the two rank-one blocks as `Ai=ar |u⟩⟨v|`, `Bj=bs |p⟩⟨q|`, with unit left/right vectors. Equality in the operator triangle inequality requires a unit vector to maximize **both** tensor summands and makes their outputs parallel. The common maximizing input is uniquely proportional to `v⊗q`; its two outputs are proportional to `u⊗q` and `v⊗p`. Their parallelity forces `u∥v` and `p∥q`. Thus both rank-one blocks are normal. The same holds for the other sector; the different-row/different-column condition means all four local blocks are covered. Therefore both `A,B` are normal.

Sections 3–5 exhaust all placements of the two singular values, including ties, and prove (1.1).

## 6. Consequence for the original Schur-block coupling residual

For unrestricted traceless `A,B`, independently put each in unitary 2+2 block-upper form, with a block-diagonal part `Ad,Bd` and strictly upper offblocks. The separate all-variable coupling reduction records a singular Schur-complement condition in which the block-diagonal positive-semidefinite term can have a kernel only when `(Ad,Bd)` **saturates** the 2+2 T2 inequality for an associated rank-two projector. By (1.1), any such saturated nonzero pair has `Ad²` or `Bd²` normal, i.e. it lies on the already-supported f215 square-normal boundary.

This is a reduction of the kernel-boundary search, not a proof that the kernel coupling vanishes and not a proof of the remaining 8×8 Schur-complement inequality. The new 2+2 theorem and this equality analysis remain unreviewed; parent adoption, all-basis f274 comparison, general T2, T3/Z2, original q3, physical or novelty claims do not follow.
