# A finest pure completely simple actor for regular sources

**Status: NEW AUTHOR WRITTEN GENERAL THEOREM, exact finite controls in prior packets; UNREVIEWED / UNADOPTED.** This concerns the actual idempotence-context quotient and arbitrary pure CS quotients. It does not prove that an original source has a physical band host, pay canonical SEP/R/L, or equate printed and physical product conventions.

## 1. Statement

Let S be any nonempty regular semigroup, finite or infinite. Assume its actual idempotence-context quotient `q:S→D` is idempotent-pure and completely simple. Fix Rees coordinates `D=M[G;I,Λ;P]`. Then S has a **finest onto pure CS quotient** `q̂:S→D̂`: every onto pure homomorphism from S to any CS semigroup factors uniquely through q̂ by an onto pure CS homomorphism. The actual syntactic q is the coarsest pure CS quotient.

D̂ is explicit. Let R be the least equivalence relation on S containing `(s,st)` for every s,t; let C be the least equivalence relation containing `(t,st)` for every s,t. Write `R_s,C_s` for their classes. Every class R_s has a well-defined q-row `i(R_s)=i_s`, and every class C_s a well-defined q-column `λ(C_s)=λ_s`. Put

`D̂=M[G;S/R,S/C; P̂]`, with `P̂_(C,R)=P_(λ(C),i(R))`,
`q̂(s)=(R_s,g_s,C_s)` whenever `q(s)=(i_s,g_s,λ_s)`.

The homomorphism `π:D̂→D`, `(R,g,C)↦(i(R),g,λ(C))`, is onto and pure, with `q=πq̂`. The theorem includes the nontrivial assertions that q̂ itself is onto and pure and that it is finest.

## 2. Two CS preliminaries

**Regular subsemigroups.** A nonempty regular subsemigroup T of a CS semigroup is CS. Indeed, if `x≤R y` in the ambient CS semigroup, x=ya and y=yzy for z∈T; hence x=yzx and the R-preorder is inherited by T. The L argument is dual. Since `xy R x` and `xy L y` in the ambient Rees product, the same holds in T; T is simple. Its idempotents are primitive by inheritance, so the Rees–Suschkewitsch theorem yields CS. The argument is not restricted to finite T.

**Pure onto CS maps.** If `f:T→D` is onto, pure, and both semigroups are CS, then for every idempotent e∈T, the group homomorphism `eTe→f(e)Df(e)` is an isomorphism. It is injective: equal images of x,y in that group make `f(xy⁻¹)` the target group identity, so purity makes xy⁻¹ an idempotent group element and hence the identity. It is onto: for any d in `f(e)Df(e)`, choose x∈T with f(x)=d; then `exe∈eTe` and `f(exe)=f(e)d f(e)=d`. This does not assume finite groups.

## 3. Construction, purity and surjectivity

The definitions give `R_(st)=R_s` and `C_(st)=C_t`. The Rees product in D supplies `g_(st)=g_s P_(λ_s,i_t) g_t`, so q̂ is a homomorphism. The projection π is a homomorphism; it is onto because q is onto, and pure because `(R,g,C)` is idempotent exactly when `g=P̂_(C,R)⁻¹`, which is exactly the idempotence condition of its π-image. Since q=πq̂ is pure, q̂ is pure as well.

It remains to prove q̂ is onto the **whole** specified Rees product, not just an image. Its image U is regular as a homomorphic image of S, hence CS by §2. It occupies every R-row and every C-column by their definitions, so it occupies every cross-cell. The restricted map `π|U:U→D` is onto and pure, since π is pure and πq̂=q. By §2 it maps each local group of U ONTO the corresponding local group of D. In a fixed D̂ cell, π preserves the middle group coordinate g; the corresponding target H-cell contains every g∈G. Therefore every g occurs in that source cell of U, and U=D̂. This proves full onto-ness without finiteness.

## 4. Universal factorization

Let `r:S→T` be any onto pure CS homomorphism. If r(s)=r(t), every source idempotence context has the same truth value by purity; hence q(s)=q(t), and q factors as `f r` with `f:T→D` onto. If f(x) is idempotent, lift x via r; q-purity makes the lift idempotent, so x is idempotent. Thus f is pure. By §2 it is injective on each local group/cell of T.

Suppose `q̂(s)=q̂(t)`. Equal R and C classes force r(s),r(t) to have the same Rees row and column in T; equality of q̂ also gives `q(s)=q(t)`, so their f-images agree. Cellwise injectivity gives r(s)=r(t). Therefore

`h(q̂(s))=r(s)`

defines a unique onto homomorphism `h:D̂→T` with `r=h q̂`. It is pure: if h(d) is idempotent, choose s with q̂(s)=d; then r(s) is idempotent, so s is idempotent by r-purity, and d is idempotent. This proves the finest property and, since q itself factors through every pure r, the coarsest statement. □

## 5. Scope and finite control

For the 68-source, the exact partition checker `frontier-20261028-quotient68-actor-image-checker-v1.py`, SHA `593ab88a64cbc9d5bbda0296eda7efe259c4e62535e87281b77d70c3b06e04c4`, finds `|S/R|=2`, `|S/C|=3`, G=C₂ and the surjective refined 12-actor, while q has 8 elements. For the earlier 45-source, a same-author eval-kernel calculation found 3 row classes, 3 column classes and the full 18-element refined image, equal in size to q. These are finite checks of examples, not a proof of the general result.

This theorem does NOT by itself transfer a physical band host along h, preserve its band size, construct faithful q̂ coordinates, or show every original source meets the q-pure-CS hypothesis. Such claims require separate proved gauge equations. Original nonorthodox SEP/R/L and the general Q1/Q2 remain open. The quotient and source data, elementary Rees facts, and all algebra remain subject to independent review; no novelty or formal proof is claimed.
