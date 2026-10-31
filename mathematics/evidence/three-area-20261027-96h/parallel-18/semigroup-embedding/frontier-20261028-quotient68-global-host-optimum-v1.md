# Exact whole-host optimum for the 68-source over all CS actors

**Status: NEW AUTHOR WRITTEN REDUCTION with pinned exact finite inputs; UNREVIEWED / UNADOPTED.** For the explicit 68-source S, the proposed minimum cardinality of a whole physical band-by-CS host, over **all** completely simple actors and all bands, is **80**. The upper bound is the ten-band/actual-eight-actor host. The proof below imports only the exact fixed-q nine-band exclusion and source tables, plus the standard Rees representation/gauge fact stated explicitly; it does not use the unreviewed onto actor-pushforward theorem. This is a finite-instance optimization, not general Q1.

## 1. Actor image, quotient and its size

Suppose S embeds in `P(B,D₀)` with any completely simple D₀. Let `r:S→D₀` be the actor map and `T=r(S)`. Since S is regular, T is a finite regular subsemigroup of D₀. It is completely simple: if `x≤R y` in D₀, write `x=ya` and choose `z∈T` with `y=yzy`; then `x=yzx`, so the R-preorder is inherited, and similarly the L-preorder. Thus `xy R_T x` and `xy L_T y` for all x,y∈T, making T simple; idempotents of T are primitive because those of D₀ are. The Rees–Suschkewitsch characterization gives CS.

The map r is pure: an idempotent actor makes the physical element idempotent, and the embedding reflects idempotence. If r(s)=r(t), every idempotence context has the same truth value on s,t, by purity. Thus the actual syntactic actor `q:S→D₈` factors through an onto homomorphism `f:T→D₈`. The source's pinned q is pure, so f is pure: if f(t) is idempotent, lift t to s; then q(s) is idempotent, s is idempotent and so is t.

For any Rees cell group of T, the restriction of f is injective: equal images of x,y make `f(xy⁻¹)` the target cell identity; purity makes `xy⁻¹` an idempotent in a group and hence its identity. Since every maximal subgroup of D₈ has order 2, every maximal subgroup of T has order at most 2. It cannot have order 1: then T would be a rectangular band, whose image under f consists entirely of idempotents, whereas D₈ contains nonidempotents. Thus the local group of T has order exactly 2. Surjectivity of f forces at least two occupied Rees rows and two occupied Rees columns. Therefore

`|T|=2|I_T||Λ_T|` is either 8 or at least 12.              (2)

Furthermore the regular-subsemigroup Green inheritance above shows that T's rows and columns are occupied ambient D₀ rows/columns. A maximal subgroup of T is a subgroup of an ambient D₀ maximal subgroup. If finite D₀ is larger than 8, its Rees group has even order at least 2 and it has at least two rows and columns; the only possible size below 12 is 8. Thus **|D₀| is 8 or at least 12**. Infinite D₀ gives an infinite host and needs no finite count.

## 2. Eight-actor case reduces to fixed q on the same band

If `|D₀|=8`, then `8≤|T|≤|D₀|` implies T=D₀ and |T|=8, while the onto f:T→D₈ is an isomorphism. The following standard Rees-isomorphism gauge is the exact named import: represent its inverse by

`f⁻¹(i,g,λ)=(I(i), a_i φ(g) b_λ, Λ(λ))`,
`b_λ P⁰_(Λ(λ),I(j)) a_j = φ(P_(λ,j))`,

where φ identifies the local groups and α is the original G₀ action on B. Replace each source coefficient c_s by `α_(a_(i_s)⁻¹)(c_s)` and let the q group act as `α_(φ(g))`. Direct substitution gives the same-band physical multiplication over q; source pairs with the same q have the same row gauge, so injectivity is preserved. The calculation is the occupied-row restriction in `frontier-20261028-all-cs-obstruction-actor-gauges-addendum-v1.md`, SHA `99a310d0b058de9a4fc754a0d05388f4fc1ed41a46f7fd439878a49fe9646bda`, §3, specialized to an isomorphism. The gauge and its use must be independently reviewed.

Consequently any eight-actor faithful host has `|B|≥10`, by the fixed-q exact minimum in `frontier-20261028-quotient68-exact-q-band-optimum-v1.md`, SHA `d9eed1b521d76da32a096b42d34f3cf66a05dc53b007613295976e73627a6174`. Hence its whole cardinality is at least 80.

## 3. Larger-actor case and witnesses

If `|D₀|≥12`, the eight distinct, commonly lower-bounded source idempotents force `|B|≥8` for every CS actor, as proved in `frontier-20261028-quotient68-global-band-optimum-v1.md`, SHA `513a404929f7c68b86256ac6db2c7cf86ddab3f0fd29a67c402f409d11ffc592`. Therefore the whole host has at least 96 elements. Combining this with §2 gives the universal lower bound 80.

The pinned ten-band/q host has 10×8=80 elements and is faithfully verified by `frontier-20261028-quotient68-minimum-band-replay-v1.py`, SHA `910dfe50d781d3c2791aa12790bdf57122318fcc47d3f31e7e9849c51fc659ce`, together with the source verifier. Thus the lower bound is attained. Equality in the size argument also forces |B|=10 and |D₀|=8. Separately, an eight-band actor-optimal host with D₁₂ has 96 elements; §3 proves this is the minimum whole-host size **among hosts with an eight-element band**.

No count relies on the existence or nonexistence of a host with an arbitrary infinite actor. The conclusion depends on independent verification of the source, the two fixed-q no-nine pruning traces, and the Rees gauge/restriction argument; all are same-author candidates at present. It does not establish any all-source Q1/Q2 statement, formal proof, or novelty.
