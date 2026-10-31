# Strict chiral norm for irreducible or rank-at-least-three local factors

**Status: WRITTEN, UNREVIEWED additive equality analysis.** This packet uses the rank-one swap identity and orthogonal-top-pair bound in `frontier-20261029-d4-chiral-operator-norm-strengthening-v1.md` (SHA-256 ef9941d92cecec526375913ae35789f9934a4286a01cc67a6680f9948aff7436), whose underlying source is the unreviewed traceless-dual/chiral packet. Earlier bytes and frozen review scopes remain unchanged. No false f198 estimate, held input, selected physical q/numerical instance, execution, external source or novelty assertion is used.

## 1. Universal strictness result

Let `A,B∈M4(C)` be traceless, `X=A⊗I4+I4⊗B`, `L=||A||_F²+||B||_F²`. Suppose a top singular pair `Xv=σ1 u`, `||u||=||v||=1`, satisfies `u⊥v`. Then

`σ1²=L  ⇒  each of A,B has rank at most two AND is unitarily reducible into 2+2 blocks`.  (1.1)

Consequently, if **either** local factor has rank at least three **or** is unitarily irreducible, then

`σ1²<L`, and hence `σ1²+σ2²≤2σ1²<2L`.  (1.2)

For `X=0` the rank/irreducibility hypotheses cannot hold, since local partial traces and `Tr A=Tr B=0` imply `A=B=0`.

Every chiral pair in the named source has such an orthogonal top singular pair. Thus (1.2) gives a **strict** global operator-norm and T2 conclusion for the whole chiral class whenever at least one factor has rank≥3 or is unitarily irreducible. This includes the source's fully symbolic, invertible, both-irreducible and both-squares-nonnormal family. There is no smallness or normal-factor condition. Whether any such pair lies outside f274's optimized `η≤2L` region remains unpaid.

## 2. Exact equality slack from the rank-one swap identity

Set `r=|u⟩⟨v|`, `C=Tr_B r`, `D=Tr_A r`, and

`p=||(P_-^A⊗P_-^B)(u⊗v)||²`.

Because `u⊥v`, both partial traces are traceless, and the swap identity gives `||C||_F²+||D||_F²=1−4p`. Also

`⟨(C,D),(A,B)⟩_F=Tr(r†X)=σ1`.

Expanding a squared norm yields the **exact** identity

`L−σ1² = ||(A,B)−σ1(C,D)||_F²+4σ1² p`.  (2.1)

Both terms are nonnegative. Equality in the operator bound for nonzero `X` therefore forces

`p=0`, `A=σ1 C`, `B=σ1 D`.  (2.2)

It remains only to show that `p=0` and `u⊥v` force both `C,D` to be supported on local subspaces of dimension at most two.

## 3. Mixed-minor classification

Schmidt-diagonalize `u` by local unitaries. Its coefficient matrix becomes

`U=diag(s1,…,sk,0,…,0)`, with `s_i>0`, `k≥1`.

Write `V` for the coefficient matrix of `v` in the same local bases. The condition `p=0` says that for all distinct row indices `i,k` and distinct column indices `j,l`,

`U_ij V_kl − U_il V_kj − U_kj V_il + U_kl V_ij = 0`.  (3.1)

These are precisely the coefficients of the two-copy local antisymmetrization; no numerical cases are sampled.

### 3.1. Schmidt rank at least three is impossible

If `U` has at least three nonzero diagonal entries, for any `k≠l` choose an active diagonal index `i` distinct from both. Substituting the row pair `(i,k)` and column pair `(i,l)` in (3.1) gives `s_i V_kl=0`, so every off-diagonal entry of `V` vanishes.

For diagonal entries, (3.1) with row and column pair `(i,k)` gives `s_i V_kk+s_k V_ii=0`. Three active indices force all their ratios `V_ii/s_i` to be zero; an inactive `k` then also has `V_kk=0`. Thus `V=0`, contradicting `||v||=1`. Hence `u` has Schmidt rank at most two.

### 3.2. Schmidt rank two

Let the active indices be `1,2`. If an off-diagonal pair `(k,l)` is not contained in `{1,2}`, at least one active index differs from both `k,l`; the same substitution forces `V_kl=0`. The diagonal equations force `V_kk=0` for `k>2`. Thus `V` is supported in the same upper-left 2×2 coefficient block as `U`.

It follows that both partial traces `C=Tr_B r` and `D=Tr_A r` are supported on the respective local spans of the first two Schmidt vectors. By (2.2), so are `A,B`: each is an operator on a 2-dimensional subspace direct-summed with zero on its orthogonal complement.

### 3.3. Schmidt rank one

Let `U=s1 E11`. In (3.1), choosing `i=j=1` shows `V_kl=0` whenever `k,l>1`. Orthogonality `u⊥v` gives `V11=0`. Thus `V` is supported on the first row and first column, with zero intersection entry.

The formula `C=U V†` makes `C` a rank-at-most-one operator with range in `span{e1}` and initial vector in `e1⊥`; similarly `D=Uᵀ conjugate(V)` has range in `span{f1}` and initial vector in `f1⊥`. Each is supported on the span of its output vector and at most one input vector, and is in fact nilpotent when nonzero. Consequently `A,B` are again supported on reducing local subspaces of dimension at most two.

These cases prove (1.1), and its contrapositive gives (1.2).

## 4. Scope

This is an all-variable strictness statement for the **orthogonal-top-pair/chiral** physical class, not a general classification of equality in unrestricted T2. It does not say that an arbitrary chiral pair with both local ranks≤2 saturates, does not prove any f274 `η>2L` or physical counterexample, and makes no T2-global/T3/Z2/q3, formal/kernel, independent-family/human review, source-correctness or novelty claim. The mixed-minor argument, indexing of the partial traces and equality identity require disjoint written review.
