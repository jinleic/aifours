# An all-variable Perron certificate on the d4 T2 complement

**PhysicsResearch96h-2 / physics-1. WRITTEN all-variable candidate; UNREVIEWED.** The certificate in §2 is an exact inequality valid for every complex traceless 4×4 pair, not a finite target search. Its strictly feasible region contains a full-dimensional open set in the genuine **both-squares-nonnormal** complement of f215's named rank-one, square-normal, weighted-permutation/cyclic-shift and two spectral sufficient pair classes. The separately scoped 4×2 lemma is not a class of 4×4 pairs. This packet does **not** prove T2 globally, T3, Z2, a global equality classification, novelty, or parent/reviewer/human/family/formal/Lean/physical-operational acceptance.

The complete parent disposition `dispositions/physics-1-werner-d4-t2-rank-one-B-closed-square-normal-and-weighted-shift-classes-parent-v1.md`, parent-reported SHA256 `2d479e9f48f707eba0ae98fe0689976fc32e6b1b04075176c261be35c819db30`, was read by this owner before the present original-target reasoning. It records f198 FATAL as written for arbitrary T, and f215 v4 support on precisely named classes at **same-harness written scope**. Main read both review returns completely and relied on their author-body coverage receipts, not a full-parent-source-read. This packet uses only the independently reproduced cyclic-shift algebra below; it never uses the false arbitrary-T bound. It does not alter the parent disposition or f196/f198/f215/f153/f62/f168 scopes.

## 1. Original all-variable dual and a new a priori gap bound

Let `A,B∈M_4(C)` be arbitrary traceless matrices and set

`X=A⊗I_4+I_4⊗B`, `L=||A||F²+||B||F²`.

The original two-copy dual obligation is

`σ_1(X)²+σ_2(X)² <= 2L`.                                             (T2)

For any independently chosen local unitaries U,V set

`X_(U,V)=(UAU†)⊗I_4+I_4⊗(VBV†)`,
`M_(U,V)=|X_(U,V)|` entrywise, `G_(U,V)=M_(U,V)^T M_(U,V)`.

G is a real symmetric PSD matrix with nonnegative entries. Define

`γ(A,B)=min_(U,V∈U(4)) ρ(G_(U,V))`,                                  (1)

where ρ is the spectral radius. The minimum exists: U(4)² is compact and all entries, absolute values and eigenvalues are continuous.

**Theorem 1 (universal dual-gap bound).** For every traceless A,B,

`2L−[σ_1(X)²+σ_2(X)²] >= 2[L−γ(A,B)]`.                             (2)

Thus `γ(A,B)<=L` is a source-independent T2 certificate, and `γ(A,B)<L` gives a strict positive dual gap. Formula (2) is valid even when its right-hand side is negative; it does not assert γ≤L for all A,B.

*Proof.* Local unitary conjugation preserves X's singular values and L. For any complex vector z, componentwise `|X_(U,V) z|<=M_(U,V)|z|`. Hence

`||Xz||²<=||M|z|||²<=ρ(M^T M)||z||²`.

It follows that `σ_1(X)²<=ρ(G_(U,V))`; the same upper bound applies to σ_2. Take the minimum over U,V. ∎

## 2. A positive-vector certificate, and exact strict feasibility

For any **fixed** local basis, let M,G be as above. Any real vector w with strictly positive entries and

`G w <= L w`                                                          (3)

certifies T2; if the inequality is strict in every component, it certifies a strict dual gap. Indeed, with `D=diag(w)`, the nonnegative matrix `D^(−1)GD` has every row sum `(Gw)_i/w_i<=L`; spectral radius is invariant under similarity and bounded by the induced maximum-row-sum norm. A certified nonnegative rational upper matrix `\widehat M>=M` entrywise and rational w>0 may be substituted in (3), provided `\widehat M^T\widehat M w<=Lw`; this is an optional finite exact certificate format, not an executed checker.

For L>0, **strict** feasibility of (3) is equivalent to `ρ(G)<L`: if ρ(G)<L, take

`w=(LI−G)^(−1) 1 = Σ_(k>=0) G^k 1 / L^(k+1) >0`,

which gives `Gw=Lw−1<Lw`; conversely (3) with strict componentwise inequality forces ρ(G)<L by the row-sum bound. A strict real witness can be perturbed to a rational positive witness because all inequalities are strict. This equivalence does not require G to be irreducible.

## 3. Nonempty open subset outside the previously supported classes

We give an exact **symbolic family**, not a selected q2/q3 value. Index the d4 basis by Z/4Z and for ε>0 let

`A_ε=B_ε=S(a)`, `a_0=1`, `a_1=ε`, `a_2=a_3=0`,
`S(a)=Σ_(i mod4) a_i |i−1><i|`.

Then `A_ε²=B_ε²=ε|3><1|`, a nonzero nilpotent and therefore nonnormal, for every ε>0. Both factors have rank2. Also

`L_ε=2(1+ε²)`, `||A_ε||op=||B_ε||op=1` for 0<ε<1,
`Tr[(A_ε†A_ε)²]=Tr[(B_ε†B_ε)²]=1+ε⁴`, `Tr A_ε²=Tr B_ε²=0`.

Thus the f215 tail test fails strictly for 0<ε<1, and its variance test fails strictly for all sufficiently small ε>0, since the variance-test left-minus-right side is `10−36ε²+10ε⁴`, positive at ε=0.

On the other hand the entries of `X_ε=A_ε⊗I+I⊗B_ε` are nonnegative, so `|X_ε|=X_ε`. Grade the basis |i,j> by i+j mod4. Every grade block has all four nonzero weights 1,ε,1,ε exactly once in distinct entries, hence Frobenius squared L_ε. Its cyclic-bidiagonal support graph has no four-cycle and row/column degrees at most2. Four nonzero entries cannot all occupy one row or one column; two with distinct rows and columns give a nonzero 2×2 minor because a complete four-edge rectangle is impossible. Every grade block therefore has rank≥2, and its operator norm squared is **strictly** smaller than L_ε. Distinct grade images are orthogonal, so

`ρ(|X_ε|^T|X_ε|)=||X_ε||op² < L_ε`.                                  (4)

The strict inequalities in (4), nonnormality of both squares, failure of the tail test, and failure of the variance test persist on some full-dimensional open neighborhood of `(A_ε,B_ε)` in `sl_4(C)×sl_4(C)`, by continuity. The base pair is a supported weighted partial-permutation pair, but generic points in this neighborhood need not be. To make this precise, let P be the set of traceless 4×4 matrices unitarily similar to a zero-diagonal weighted partial permutation. P is a finite union over permutations of images of `U(4)×C^4`, hence has real dimension at most 24, strictly below the 30 real dimensions of `sl_4(C)`; by the standard smooth-image/Sard measure-zero theorem it has empty interior. P is also closed: for a convergent sequence, permutation has a constant subsequence, U(4) is compact, and the weights are bounded by the Frobenius norm. The square-normal locus is a proper closed real-algebraic set, since a nonzero length-two weighted nilpotent path has a nonzero nonnormal square. It likewise has empty interior. Rank≤1 is a proper closed algebraic set.

Consequently every sufficiently small strict neighborhood above contains a nonempty **open** subset in which **both** A and B lie outside P, both have nonnormal squares and rank>1, and both f215 spectral sufficient tests fail. Theorem 1 nevertheless gives T2 with a strict positive dual gap there. This extends the scoped f215 weighted-permutation, rank-one, square-normal and spectral coverage on an open part of the genuine both-squares-nonnormal complement; it is not an extension of parent adoption or proof of the rest of that complement.

## 4. Exact unpaid bridge and provenance

The global target would follow from proving `γ(A,B)<=L` for every traceless A,B, but this packet does not assert that stronger statement or its necessity: Theorem 1 is a one-sided modulus majorant and can be conservative. In particular, failure of the Perron certificate is **not** a T2 counterexample and says nothing by itself about the original q2 sign. The remaining both-squares-nonnormal pairs outside strict or non-strict certificate feasibility remain unpaid by this method.

The proof uses only the original T2 dual, componentwise triangle inequality, finite-dimensional matrix norms, elementary cyclic grading, continuity and the named standard smooth-image/Sard fact. No source certificate, false arbitrary-T 4×2 estimate, f198/f215 review body, elected HELD/ZERO/NONINPUT episode/consumer/guidance, executable search, or selected physical target q-value is used. The earlier owner stale-authority checkpoint at 19:12 is explicitly corrected by `frontier-20261029-1913-post-disposition-stale-checkpoint-correction-v1.json` (SHA256 `34aa2cfbea94707c5bc8b0423947942a3d1d2801101650cecd4f2d8c0b171525`); no continuous work is inferred for that interval. Previous process/held controls and f196/f198/f215/f153/f62/f168 scopes remain unchanged.
