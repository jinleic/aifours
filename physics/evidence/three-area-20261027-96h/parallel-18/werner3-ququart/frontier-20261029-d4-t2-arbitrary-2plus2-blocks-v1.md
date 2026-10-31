# A written T2 proof for arbitrary traceless 2+2 reducing pairs

**Status: WRITTEN, owner candidate, UNREVIEWED.** This is an all-complex, all-variable argument, not a numerical diagnostic, source-certificate replay, computer-checked proof, human review or novelty claim. It uses the original d=4 traceless-pair dual inequality and elementary singular-value, Schmidt-decomposition and Frobenius identities. Parent f215, f274 and f281 retain exactly their existing same-harness written scopes. In particular this packet does **not** reuse the false arbitrary-T assertion withdrawn after f198. Held/ZERO sources and guidance are not inputs.

## 1. The theorem and its exact boundary

Let `A,B ∈ M4(C)` be traceless. Assume that, **separately**, each is unitarily similar to a direct sum of two arbitrary 2×2 matrices. The two unitaries need not be the same; neither block need be normal or individually traceless. Set

`X = A⊗I4 + I4⊗B`, `L = ||A||_F² + ||B||_F²`, `S2(X) = σ1(X)² + σ2(X)²`.

Then **`S2(X) ≤ 2L`**. This is the entire claimed theorem. Local unitary conjugation of `A,B` conjugates `X` unitarily, so the proof may use their 2+2 reducing bases. The result includes pairs for which **both** `A²` and `B²` are nonnormal. It proves T2 on this algebraically defined family, not T2 for all traceless pairs, T3, Z2 or the original q3 target.

The theorem makes no claim that this family contains a pair with f274's `η>2L`; its comparison with the **entire** compound-certificate success region remains unresolved. Thus it is not established here that it enlarges that region as a set, and certificate failure is never inferred from a fixed-basis sign issue. Section 5 gives an exact all-variable family outside the f215 rank-one/square-normal/weighted-permutation classes and outside the normal-factor class; those exclusions do not settle its f274 membership. The first unpaid certificate-domain premise is to establish or refute `η(A,B)>2L` at some member, with minimization over **all** local product bases.

## 2. Two-qubit scalar-plus-traceless norm lemma

For arbitrary `t∈C` and arbitrary traceless `C,D∈M2(C)`,

`||t I4 + C⊗I2 + I2⊗D||_op² ≤ 4|t|² + ||C||_F² + 2||D||_F²`.  (2.1)

Swapping the two tensor factors also yields

`||t I4 + C⊗I2 + I2⊗D||_op² ≤ 4|t|² + 2||C||_F² + ||D||_F²`.  (2.2)

This lemma is about two 2×2 factors, with the scalar coefficient explicitly charged by `4|t|²`; it is **not** the false arbitrary-T 4×2 lemma from f198.

### 2.1. Proof by arbitrary unit vectors

Let `u,v∈C²⊗C²` be unit vectors, identified with coefficient matrices `U,V∈M2(C)`, and let `s=Tr(U†V)`. Put `M=VU†`, `N=Vᵀ conjugate(U)`; both have trace `s`. Write `M0=M−sI2/2`, `N0=N−sI2/2`. The coefficients of `C,D` in the scalar matrix element are the linear forms `Tr(CM)` and `Tr(DN)`; the possible harmless transpose depends only on vectorization convention and does not change the trace or Frobenius norm. Weighted Cauchy–Schwarz on the scalar/traceless-matrix direct sum gives

`|⟨u,(tI4+C⊗I2+I2⊗D)v⟩|²`

`≤ (4|t|²+||C||_F²+2||D||_F²) · (|s|²/4+||M0||_F²+||N0||_F²/2)`.  (2.3)

Set `x=||VU†||_F²` and `y=||U†V||_F²=||N||_F²`. Since `Tr M=Tr N=s`, the second factor in (2.3) is

`x + y/2 − |s|²/2`.  (2.4)

We show it is at most one. By independent local unitaries, Schmidt-diagonalize `u`: `U=diag(a,b)`, where `a,b≥0` and `a²+b²=1`. Write `V=[[p,q],[r,w]]`, so `|p|²+|q|²+|r|²+|w|²=1` and `s=ap+bw`. Direct expansion gives

`x = a²(|p|²+|r|²)+b²(|q|²+|w|²)`,

`y = a²(|p|²+|q|²)+b²(|r|²+|w|²)`,

`x+y = 1+|s|²−|bp+aw|²`.  (2.5)

Also `x≤1`: for instance the displayed expression is a convex combination of the squared column norms of `V`. Thus (2.4) equals `(1+x−|bp+aw|²)/2≤1`. This proves (2.1) after taking the supremum over all unit `u,v`; interchanging tensor legs proves (2.2). No selected matrix or physical parameter was used.

## 3. Four sectors for arbitrary block traces

Write the separately reduced matrices as

`A=(α I2+C1) ⊕ (−α I2+C2)`,

`B=(β I2+D1) ⊕ (−β I2+D2)`,

where `Tr Cr=Tr Ds=0` for `r,s∈{1,2}`. This follows from the **global**, not blockwise, trace-zero hypotheses. Thus

`L = 4(|α|²+|β|²)+Σr ||Cr||_F²+Σs ||Ds||_F²`.  (3.1)

The four orthogonal 4-dimensional reducing sectors of `X` are

`Xrs=(εr α+εs β) I4 + Cr⊗I2 + I2⊗Ds`,  `ε1=1`, `ε2=−1`.  (3.2)

Every singular value of `X` belongs to one of these four sectors. For `ar=||αr I2+Cr||_op`, `bs=||βs I2+Ds||_op`, with `αr=εrα`, `βs=εsβ`, the operator triangle inequality gives

`||Xrs||_op≤ar+bs`.  (3.3)

### 3.1. Both chosen singular values from one sector

Their squared sum is at most

`||Xrs||_F² = 4|εrα+εsβ|²+2||Cr||_F²+2||Ds||_F²`

`≤ 8(|α|²+|β|²)+2Σi||Ci||_F²+2Σj||Dj||_F² = 2L`,

using `|z+w|²≤2(|z|²+|w|²)`. All cross traces in the Frobenius expansion vanish because the blocks `Cr,Ds` are traceless.

### 3.2. One chosen singular value from each of two sectors in different rows AND columns

They are bounded by the two sector operator norms, hence by (3.3) and `2xy≤x²+y²`,

`(ar+bs)²+(ar′+bs′)² ≤ 2(ar²+ar′²+bs²+bs′²) ≤ 2L`,

where `r≠r′` and `s≠s′`. The final inequality uses `||block||_op²≤||block||_F²` and the two rows and columns exhaust the blocks.

### 3.3. One chosen singular value from each of two sectors in the SAME row

Apply (2.1) to each sector in the row, retaining coefficient `1` on the repeated `Cr` and `2` on the two `Ds`:

`||Xr1||_op²+||Xr2||_op²`

`≤ 4(|εrα+β|²+|εrα−β|²)+2||Cr||_F²+2Σs||Ds||_F²`

`= 8(|α|²+|β|²)+2||Cr||_F²+2Σs||Ds||_F² ≤ 2L`,

by the complex parallelogram identity and (3.1). For two sectors in the **same column**, apply (2.2), instead assigning coefficient `1` to the repeated `Ds`, to obtain the identical bound with the roles interchanged.

These three cases exhaust the sector locations, including degeneracies and ties, and establish `S2(X)≤2L` for every separately 2+2 reducing traceless pair. The argument does not require the sector operator-norm bounds to be simultaneously attained.

## 4. Explicit strictness information and residual

The same-row bound has slack at least `2||C_{3−r}||_F²` relative to `2L`; the same-column bound has slack at least `2||D_{3−s}||_F²`. The same-sector Frobenius bound has slack at least `2||C_{3−r}||_F²+2||D_{3−s}||_F²+4|εrα−εsβ|²`. For opposite sectors its triangle/Cauchy bound has slack

`2Σi(||Ai||_F²−||Ai||_op²)+2Σj(||Bj||_F²−||Bj||_op²)+(ar−bs)²+(ar′−bs′)²`,

where `Ai=εiα I2+Ci`, `Bj=εjβ I2+Dj`. These are bounds, not a global equality classification. For example, when each of `C1,C2,D1,D2` is nonzero and every 2×2 block `Ai,Bj` has rank two, **each** case above has strictly positive slack, hence `S2(X)<2L` uniformly throughout that stated class. This is an optional strict corollary of the same proof, not a separate neighborhood or certificate-necessity claim.

The original remaining T2 quantifier consists of all traceless 4×4 pairs outside this separately 2+2 reducing family, **except** whatever other scopes are independently covered by the existing adopted results. This packet does not prove that the new family extends outside f274's full `η≤2L` region. Nor does it close T3/Z2 or prove a physical source statement. The exact first unpaid comparison is an all-local-bases question for `η`, not a numerical fixed-basis check.

## 5. Both-squares-nonnormal family outside the named earlier structural classes

For arbitrary complex `α,c,β,d` satisfying `αcβd≠0`, let

`A=(α I2+c E12) ⊕ (−α I2)`,

`B=(β I2+d E12) ⊕ (−β I2)`.

Both are traceless and invertible, and

`A²=(α² I2+2αc E12) ⊕ α² I2`,

`B²=(β² I2+2βd E12) ⊕ β² I2`.

For nonzero `αc,βd` the displayed triangular Jordan blocks are nonnormal, so both squares are nonnormal. The two matrices are neither normal nor rank one, and each has a nontrivial Jordan block at a nonzero eigenvalue. An invertible weighted partial permutation matrix is a weighted permutation: each cycle has characteristic polynomial `z^k−w` with `w≠0` and hence is diagonalizable over `C`; a direct sum of cycles is diagonalizable. Therefore neither `A` nor `B` is unitarily similar to an invertible weighted partial permutation or cyclic weighted shift. The family is consequently outside the f215 named rank-one, square-normal and weighted-permutation/shift structural classes and outside f281's normal-factor class. It nevertheless is **not** established to lie outside the full f274 certificate region or outside other independently supported sufficient tests. No numerical parameter instance is selected.

## 6. Inputs, history, and non-claims

- Used: the parent f215/f274/f281 dispositions to identify earlier scope; basic unitary invariance, Schmidt decomposition, Frobenius duality, operator-norm variational formula, finite-dimensional block singular spectra and Cauchy/parallelogram identities. All new inequalities above are written derivations, not imports from the false v2 lemma.
- The f198 arbitrary-T 4×2 estimate remains FALSE and withdrawn. The present (2.1) has different dimensions and a different explicit scalar charge; no arbitrary-T transfer is asserted.
- The earlier same-owner compound phase-balance obstruction packet is independent; this proof does not require its unreviewed claims. Earlier process histories, stop/held/ZERO restrictions and the reported stale-checkpoint correction remain in force.
- No solver, code, finite search, selected physical q, source replay, Lean/kernel proof, cross-family/human review, adopted target theorem or novelty conclusion is claimed.
