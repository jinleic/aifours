# Additive corrections for the f159/f160 MINOR findings (no frozen bytes changed)

MathResearch96h-2, original math-1. Actual native clock observed before writing: **Thu Oct 29 08:19:05 PDT 2026**. This file answers the MINOR list in the parent disposition `dispositions/math-1-ph7-no-seven-states-at-eight-ninths-and-above-0p85-parent-v1.md`. It is an addendum: the pinned files below are unchanged and must be read together with it.

Affected pinned files: 8/9 candidate `frontier-20261029-ph7-eight-ninths-impossibility-v1.md` (SHA256 `599feaa589a6281316786cdd4d19050a88ba2945a12ce253d5f04678e862b2d4`); no-two-cycle core `frontier-20261029-ph7-critical-no-two-cycle-exclusion-v1.md` (`46659f60be21537f02d6ea76ceac3be2b89a7a55c3d2b1e8f249c7c315383745`); shift corollary `frontier-20261029-ph7-shift-monotonicity-corollary-v1.md` (`dde16615ea1cfcc0dcac77ca5f3329cc947e58287e4c126b13979468b7a390e1`); `frontier-20261029-ph7-impossibility-above-0p8765-v1.md` (`8084804cabea6159bf5bebe588c593d87abcf43090313a07483ef278a86cc7ff`); `frontier-20261029-ph7-impossibility-above-0p85-v1.md` (`a624b358c71e838963c8250bfb82af2e54b06f3bc886332abcc3891a3e24f133`); certificates and checkers named there.

## 1. "Positive", not "nonnegative", rates

Wherever these files say that Qpol>0 or Hpol>0 holds "on all six nonnegative rates" (8/9 candidate §2, item 2, and the same wording in the core), read **"at every point of the OPEN positive six-orthant"**. That is exactly what the compactified leaf rule proves (depth>=6, all Bernstein coefficients >=0, every coefficient at a box corner lying in the open unit cube >0), and it is all that is used: by Lemma 1 the seven numbers `ut_k` are strictly positive, so the six non-largest ones lie in the open orthant. No claim is made on boundary faces with a zero rate. The girth-four certificate's `scope` string names the graph class of the earlier theorem it was written for; it is not a hypothesis of the polynomial inequality.

## 2. Notation clash for "A"

In the symmetrization lemmas (8/9 candidate §3 and Lemma 5 of the 0.85 file) the matrix `A:=-S` is meant; in Lemma C/C2 (and all certificates) `A` is the scalar `f2-4f1+10-2z` (`f2-4f1+74/9` at 8/9). Read the matrix as **`𝒜:=-S`** throughout: `ut_1<=...<=ut_7` are the eigenvalues of 𝒜, `tr(𝒜_U)`, `e2(𝒜_U)` are traces/second elementary functions of principal submatrices of 𝒜, and the letter A without decoration always means the scalar.

## 3. Hypotheses of Lemma 1, stated in full

**Lemma 1.** Let G be an n×n **irreducible Metzler** matrix with spectral bound `s(G)=0` that has **at least one non-real eigenvalue**. Let S be its geometric symmetrization (`S_ii=G_ii`, `S_ij=sqrt(G_ij G_ji)`). Then every eigenvalue of S is real and strictly negative.

Used facts: for `c0>=max_i(-G_ii)`, `P=G+c0I` is nonnegative irreducible with Perron root `c0` (since `s(G)=0`) and positive right/left Perron vectors; `M=Dg P Dg^{-1}` with `Dg=diag(sqrt(l_i/r_i))` has the common positive Perron vector `sqrt(l∘r)`, so `M_s=(M+M^T)/2` is nonnegative, symmetric and irreducible with Perron root `c0`; `0<=S+c0I<=M_s` entrywise (AM-GM, `sqrt(M_ij M_ji)<=(M_ij+M_ji)/2`, and `S_ij=sqrt(P_ij P_ji)=sqrt(M_ij M_ji)`); strict monotonicity of the Perron root for irreducible nonnegative matrices gives `lambda_max(S)+c0<c0` unless `S+c0I=M_s`; equality forces M symmetric, so G is similar to a symmetric matrix and has real spectrum, contradicting the non-real eigenvalue. In the application `n=7` and the non-real eigenvalues are `-1±i sqrt(z)`, z>0.

## 4. Conditional title

The 8/9 file's title "the minimum PH order there is exactly 8" is to be read as: **conditional on the adopted irreducibility caller (for the lower bound) and on the retained prior-round eight-state construction (for the upper bound), the minimum PH order at z=8/9 is exactly 8**; unconditionally within this file only the seven-state exclusion given the caller is proved.

## 5. "Threshold" means a supremum

Lemma S proves that impossibility of the seven-state SPECTRAL problem at z0 propagates to all z>=z0; it does **not** show that the set of PH7-realizable ratios is downward closed (a PH representation also needs the numerator identity). In the 0.8765 and 0.85 files and in the shift corollary, every phrase "seven-state threshold", "existence region lies in z<...", or "bracketed in [0.8204, ...)" means: **the supremum of PH7-realizable ratios** is at most the stated value; the lower end is a realizable ratio only where an actual construction is adopted (currently 41/50 by the parent disposition of the v2 band; the v4 endpoint z_*≈0.8204204 is unreviewed-by-disposition). The sentence "spectral 7-state realizability is downward closed" in the shift corollary refers to the spectral problem only.

## 6. Certificate conventions (all six-cube and residual certificates of this owner)

- **Six-cube (girth-four `Q/H` at 8/9, `z1`, `z2`, `z3` outer and H covers).** Variables `u_0,...,u_5` in the order of the polynomial generators; compactification `u_j=x_j/(1-x_j)`, `x_j in [0,1]`, polynomial multiplied by `prod_j(1-x_j)^2`; the monomial coefficient `a_k` becomes the Bernstein coefficient `a_k/prod_j C(2,k_j)`, scaled to integers by the least common multiple. A leaf path is a binary string; character number t (0-based) splits **axis `t mod 6`** (axis j = variable `u_j`); **'0' = lower half `[lo,mid]`, '1' = upper half `[mid,hi]`**. Integer de Casteljau: the lower child's k-th coefficient is multiplied by `2^(d-k)`, the upper child's by `2^k` (positive factors, signs preserved). Leaf rule: depth>=6, all coefficients >=0, and the coefficient at every box corner lying in the open cube `(0,1)^6` is >0; excluded-cube leaves (z2, z3) are boxes contained in the stated closed cube.
- **Residual (no-two-cycle core, z1, z2, z3).** Variables in axis order **0 = y, 1 = tau, 2 = gamma** with `y=alpha1=s/(1-s)`, `gamma=beta1-y/2=g/(1-g)` (compactified as above with their own degrees) and `tau=alpha2/((3/8)y²) in [0,1]` (ordinary Bernstein basis); character t splits axis `t mod 3`, same bit convention; axes of degree 0 are not split. Leaf labels: `Abar<=0` and `Dbar<=0` mean all coefficients <=0; `f1-4<0` means all coefficients <0.
- **Sorted affine covers (z2 `N`, z3 `NB`, `MC`).** Labels `v1<=...<=v6`, map `v_i=lo+(hi-lo)s_i`, `s in [0,1]^6`, axis `t mod 6` = `v_{(t mod 6)+1}`, same bit convention; "unsorted" leaf: some i<j with `lo_i>hi_j` (no sorted point); every other leaf: all listed tensors >0 (>=0 where marked nonstrict).

## 7. Scope

Presentation corrections only; no mathematical step, certificate byte, digest or leaf changes. No review, formal, novelty or priority claim; historical holds unchanged.

END - f159/f160 MINORs addressed additively.
