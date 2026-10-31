# A stronger all-variable additive-compound Perron bridge for the d4 T2 complement

**PhysicsResearch96h-2 / physics-1. WRITTEN all-variable candidate; UNREVIEWED.** This is a self-contained successor to `frontier-20261029-d4-t2-entrywise-perron-open-complement-bridge-v1.md`, SHA256 `ee03876158c521fc74d365ec31b4cdd95237cbac6c5e59beb5cbfa4efac27728`, and its nonnecessity addendum SHA256 `548dcdd440f430b5548bcd6c746d5e1a6bcea62b6ec79694c5a2dac35dede509`; those bytes remain unchanged. It gives a **stronger all-variable** T2 gap bound, containing the earlier open both-squares-nonnormal complement and exactly resolving the normal-pair obstruction to the old certificate. It does not prove general T2/T3/Z2, a global equality classification, novelty, parent/reviewer/human/family/formal/Lean acceptance or a physical-operational consequence.

The complete parent f198/f215 disposition was read before this original-target reasoning. It supports the specified f215 classes only at qualified same-harness written scope and records the false arbitrary-T v2 estimate; neither the false estimate nor any f198/f215 review body is used below. No held episode, consumer or guidance, source certificate, selected physical q-value or finite Hessian/descent variant is used. f196/f198/f215/f153/f62/f168 and prior process boundaries are unchanged.

## 1. The original dual and a 120×120 additive compound

Let A,B∈M_4(C) be arbitrary traceless matrices. Define

`X=A⊗I_4+I_4⊗B`, `L=||A||F²+||B||F²`, `H=X†X >=0`.

The T2 dual is `σ_1(X)²+σ_2(X)²<=2L`. For any 16×16 Hermitian H let `K(H)` be its **second additive compound**: the restriction of `H⊗I+I⊗H` to `wedge² C^16`. On the orthonormal basis `e_i∧e_j=(e_i⊗e_j−e_j⊗e_i)/sqrt2`, i<j, K has entries

`K_(ij),(kl)=h_ik δ_jl+h_jl δ_ik−h_il δ_jk−h_jk δ_il`.             (1)

The dimension is `binom(16,2)=120`. Since an eigenbasis of H induces an exterior-product eigenbasis of K, its eigenvalues are all pair sums h_i+h_j. In particular, with h_1≥h_2 the top eigenvalues of X†X,

`λ_max K(H)=h_1+h_2=σ_1(X)²+σ_2(X)²`.                               (2)

K(H) is PSD because H is PSD.

## 2. The stronger all-variable bound and a finite certificate

For local unitaries U,V define

`X_(U,V)=(UAU†)⊗I+I⊗(VBV†)`, `H_(U,V)=X_(U,V)†X_(U,V)`,
`R_(U,V)=|K(H_(U,V))|` entrywise in the fixed i<j basis.

R is a real symmetric entrywise-nonnegative matrix. Set

`η(A,B)=min_(U,V∈U(4)) ρ(R_(U,V))`.                                  (3)

The minimum exists by compactness and continuity. The original operator's singular values are unchanged by these local conjugations.

**Theorem 2.1 (universal compound gap).** For every traceless A,B,

`2L−[σ_1(X)²+σ_2(X)²] >= 2L−η(A,B)`.                                (4)

Thus `η<=2L` is a sufficient T2 certificate; η<2L gives a strict gap. Formula (4) is valid even if its right side is negative. Failure of this sufficient certificate is not a T2 counterexample.

*Proof.* For any Hermitian K and unit vector z, `|z†Kz|<=|z|^T |K| |z|<=ρ(|K|)`. Apply this to K(H_(U,V)), use (2), and minimize. ∎

For any fixed U,V, a vector `w∈R^120` with all entries positive and

`R_(U,V) w <= 2L w`                                                   (5)

is a finite T2 certificate. Indeed diagonal similarity by diag(w) makes every row sum ≤2L, so ρ(R)≤2L. Strict componentwise inequality gives a strict gap. If ρ(R)<2L, strict w exists even for reducible R: take `(2LI−R)^(−1)1=Σ_(k>=0)R^k1/(2L)^(k+1)>0`. A rational nonnegative upper matrix for R and rational positive w can be used in (5) as an optional exact certificate format; no checker or target instance is executed here.

## 3. Exact domination of the earlier modulus certificate

Let `M_(U,V)=|X_(U,V)|` entrywise and `G_(U,V)=M_(U,V)^T M_(U,V)`. The earlier bridge used

`γ(A,B)=min_(U,V) ρ(G_(U,V))` and `σ_1²+σ_2²<=2γ(A,B)`.

The new compound bound is always at least as strong:

`σ_1²+σ_2² <= η(A,B) <= 2γ(A,B)`.                                   (6)

*Proof.* Fix U,V and abbreviate X,H,K,M,G,R. Let `J_+` send the coordinate indexed by i<j to the symmetric hard-core vector `(e_i⊗e_j+e_j⊗e_i)/sqrt2`. Formula (1), H's nonnegative diagonal, and the fact that two distinct pairs share at most one index give the exact entrywise identity

`R=J_+† (|H|⊗I+I⊗|H|) J_+`.                                         (7)

Here |H| is the real symmetric entrywise modulus. It is entrywise nonnegative, so its largest eigenvalue equals its spectral radius. Compression and (7) give `ρ(R)<=2ρ(|H|)`. Also

`|H_ij|=|Σ_k conjugate(X_ki)X_kj| <= Σ_k|X_ki||X_kj|=G_ij`.

Both |H| and G are real symmetric nonnegative, so their largest eigenvalues are monotone under entrywise domination; hence `ρ(R)<=2ρ(G)`. Minimize over U,V and combine with Theorem 2.1. ∎

This comparison is exact for arbitrary complex inputs; it does not claim either sufficient test always succeeds.

## 4. The old operator-norm obstruction is resolved for all normal pairs

If A and B are normal, choose local unitaries that diagonalize both. Then X, H and K(H) are diagonal in the product/pair bases; all diagonal entries of K(H) are nonnegative. Hence `ρ(|K(H)|)=λ_max K(H)=σ_1²+σ_2²`. Since every compound majorant is at least this value,

`η(A,B)=σ_1(X)²+σ_2(X)²` for all normal A,B.                       (8)

Thus the compound method is **exact** on the normal-pair class, not only on the subclass where `||X||op²<=L`. In particular it handles the entire symbolic family `A=B=t(4P−I_4)`, P any rank-one orthogonal projection and t any nonzero complex scalar. That family's X has singular values `6|t|` once and `2|t|` fifteen times, so η=`40|t|²<2L=48|t|²`, whereas the old γ is at least `||X||op²=36|t|²>L=24|t|²`. This is an all-P, all-t dual operator identity, not a selected original physical C/q value.

## 5. A full-dimensional open portion of the genuine f215 complement

The earlier modulus certificate supplied a strict open both-squares-nonnormal complement; (6) transfers it immediately to the stronger compound certificate. For completeness, let `S(a)=Σ_(i mod4)a_i|i−1><i|` and take the symbolic family `A_ε=B_ε=S(a)` with `a_0=1`, `a_1=ε>0`, `a_2=a_3=0`. Then both squares are nonzero nilpotent (hence nonnormal), and `L_ε=2(1+ε²)`.

All entries of X_ε are nonnegative, so M=X_ε. Its grade-k block under i+j mod4 contains all four nonzero weights in distinct cyclic-bidiagonal positions; each block has Frobenius squared L_ε and rank≥2 because its support graph has no four-cycle and degree at most2. Hence every block has operator norm squared <L_ε and `ρ(G)<L_ε`. By (6), `η<2L_ε`.

Both f215 spectral sufficient tests fail **strictly** for sufficiently small ε>0. The tail test fails since the leading singular values are1 and each tail is ε². For the variance test, `Tr(A_ε²)=0`, `p=q=1+ε⁴`, and left minus right equals `10−36ε²+10ε⁴>0` near ε=0. These are symbolic inequalities; no numerical q2/q3 value is evaluated.

Strict compound feasibility, nonnormality of both squares and strict failure of both spectral tests persist on an open neighborhood in `sl_4(C)×sl_4(C)`. Within that neighborhood choose A,B outside the zero-diagonal weighted-partial-permutation unitary-similarity locus P and outside rank≤1. P is a finite union of smooth images of `U(4)×C^4`, of real dimension at most24<30, so by the standard smooth-image/Sard theorem it has empty interior. It is closed because Frobenius norm bounds the weights, U(4) is compact, and there are finitely many permutations. The square-normal locus is a proper closed real-algebraic set, and rank≤1 is a proper closed algebraic set. Thus there is a nonempty **full-dimensional open** set outside the f215 rank-one, square-normal, weighted-permutation/cyclic-shift and two spectral pair classes/tests where η<2L. The restricted 4×2 lemma is not itself a class of 4×4 pairs.

## 6. Exact remaining gap and provenance

This packet does not establish `η(A,B)<=2L` for all A,B or assert that the compound certificate is necessary. Its failure, if any, is not a T2 counterexample. Generic both-squares-nonnormal pairs outside its certified region remain unpaid, as do T3 and global equality. The 120×120 certificate is a written finite-dimensional condition, not an executable verifier or formal proof.

The proof uses only original trace/Schmidt duality, elementary exterior powers, componentwise absolute values, positive-matrix spectral estimates, continuity, cyclic grading, and the named standard smooth-image/Sard fact. No false arbitrary-T estimate, source certificate, elected HELD/ZERO/NONINPUT episode/consumer/guidance, selected physical q-value, f198/f215 review body or additional Hessian/descent variant is a premise. The earlier stale owner checkpoint is explicitly corrected by `frontier-20261029-1913-post-disposition-stale-checkpoint-correction-v1.json`, SHA256 `34aa2cfbea94707c5bc8b0423947942a3d1d2801101650cecd4f2d8c0b171525`; no continuous work is inferred for that interval. No frozen review scope or parent disposition is changed.
