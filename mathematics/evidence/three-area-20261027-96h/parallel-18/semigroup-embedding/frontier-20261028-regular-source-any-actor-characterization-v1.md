# Regular sources: arbitrary physical CS actors reduce to the actual syntactic actor

**NEW AUTHOR WRITTEN CHARACTERIZATION with exact finite and symbolic infinite controls; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 19:50:34 PDT 2026**. The theorem is about the precisely defined physical locally-regular-band-by-CS products. It does NOT assert that the printed book question is equivalent to that physical target, settle the canonical κ gap, adopt D1–D4, or claim novelty.

## 1. Exact characterization

Let S be ANY nonempty regular semigroup, finite or infinite. Form its idempotence-context syntactic congruence τ and quotient `q:S→D=S/τ`.

**Theorem.** S admits a faithful physical host `P(B,D0)` for SOME locally regular band B, SOME completely simple actor D0 and SOME permitted action **iff**

1. the actual syntactic quotient D is completely simple and q is idempotent pure; and
2. the actual canonical locally-regular-band physical map κ_q is injective.

The reverse direction is the canonical host itself. For the forward direction, every physical host can be transported to the ACTUAL q; a proof is in §§2–4. This is an all-actor reduction at physical-product scope, NOT a proof that condition2 holds for original sources. Under the named SQ-E original-source input, condition1 is already satisfied; the original same-q R/L/SEP gap therefore remains condition2 and is not silently closed.

## 2. A regular subsemigroup of a CS semigroup is CS

Let T be any nonempty regular subsemigroup of a completely simple semigroup D0; T may be infinite. Green R and L are inherited from D0. Indeed, if x,y∈T and `x≤_R y` in D0, write x=y a with a∈D0¹. Choose z∈T with y=y z y. Then `x=y z x`, and zx∈T, so `x≤_R y` in T. The reverse inclusion is automatic; dualize for L. This elementary proof is also stated as Theorem2/Lemma3 in [East et al., *Green’s relations and stability for subsemigroups*](https://arxiv.org/html/1906.02313) (2019).

In a Rees completely simple semigroup, xy is R-related to x and L-related to y. By inheritance, for all x,y∈T,

`x R_T xy L_T y`.

Thus T has a single D-class, hence a single J-class and is simple. T contains idempotents by regularity; any natural-order comparison of T idempotents is one in D0 and hence equality, so they are primitive. The standard Rees–Suschkewitsch characterization makes T completely simple. Finiteness is nowhere used.

A nonregular subsemigroup need not be CS: the positive integers under addition form a subsemigroup of the group Z but contain no idempotent and are not regular. This is a written counterexample to dropping the hypothesis, not a finite solver result.

## 3. An arbitrary physical actor image is pure CS

Suppose j:S→P(B,D0) is faithful, with B locally regular. Its actor projection `r0:S→D0` has image T. A homomorphic image of a regular semigroup is regular, so T is a REGULAR subsemigroup of D0 and is CS by §2, even when S,T are infinite.

The onto map r:S→T is pure. If r(s) is idempotent, the corresponding CS self-weight in the physical product is the group identity, so `j(s)²=j(s)` because B is a band. Faithfulness gives s²=s.

For any onto pure r, source idempotence-context congruence pulls back:

`τ_S = r^(-1)(τ_T)`.                                      (3)

Both actual and absent actor contexts lift to source contexts, and purity reflects idempotence. The quotient f:T→T/τ_T is pure: τ_T saturates idempotents by the absent context; if [t] is idempotent, take an inverse z of t² and `t z t` is an idempotent in the same quotient class. A homomorphic image of a CS semigroup is CS. Thus (3) identifies the actual q with `f∘r` and establishes condition1.

## 4. Restriction, pushforward and the converse

The inclusion `T↪D0` is a CS Rees homomorphism. Its local-group map into the ambient group is injective; with ordinary row/column gauges, the calculation in `frontier-20261028-all-cs-obstruction-actor-gauges-addendum-v1.md`, SHA `99a310d0b058de9a4fc754a0d05388f4fc1ed41a46f7fd439878a49fe9646bda`, §3 transforms the original source band coefficients by the inverse source-row gauge and restricts the action to that subgroup. This yields a faithful model of S over T using the SAME locally regular B. The gauge calculation needs only the Rees form of T and the inclusion, not finiteness; §2 pays that previously missing infinite-image prerequisite.

Now apply the pure onto-CS whole-host pushforward, constructed in `frontier-20261028-pure-CS-coinduced-whole-host-v1.md`, SHA `b129099ed4ae481a0d212ec68c5271b91b700757721d8c41d712b55e9755bad2`, §4. It sends the entire T-host injectively to one over T/τ_T, adding a rectangular band factor but retaining local regularity. Composing gives a faithful host over actual q. The canonical V-band universal map into that host shows κ_q must be injective, proving necessity of condition2.

Conversely, if the actual q is pure CS and κ_q is injective, its own canonical physical product is by definition a faithful locally regular-band-by-CS host. This proves the equivalence. The nononto coinduction formula is not needed in this last onto step, but the target row/column gauges and subgroup restriction in the first step are essential.

## 5. Infinite and finite checks

An explicit infinite example exercises the nonfinite actor-image scope: let

`D0={0,1,2}×Z×{0,1,2}`,     `T={0,1}×2Z×{0,1}`,

both with rectangular-group multiplication `(i,g,λ)(j,h,μ)=(i,g+h,μ)`. T is a proper infinite regular CS subsemigroup of D0. It embeds over the ambient actor with a singleton band. Its actual syntactic quotient is the group 2Z, and the map

`(i,2n,λ) ↦ ((i,λ),2n)`

is a faithful physical host over that actual quotient with a four-element rectangular band and trivial group action. This is a fully symbolic example; no finite run is claimed as verification of its infinitude.

`frontier-20261028-regular-cs-image-checker-v1.py`, SHA `f684630820514278d75119eca410358b470ffb93cf73637275a683a09c5aeb6e`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 19:50:34 PDT 2026**, exit0. It checks an ambient24-element CS Rees semigroup and its proper regular8-element actor image, all Green R/L inheritance comparisons, `xy R x`, `xy L y`, regularity and primitive idempotents. The named nononto-transport checker in §4 separately checks a pure CS map with C2 nonnormal in S3 and collapsed rows/columns. These same-author finite checks do not replace the symbolic infinite proof.

This characterization removes a finite-image limitation in earlier source notes, but preserves the printed-book/canonical-target qualification, every standing quarantine and the unresolved all-source κ_q question. No independent review, cross-vendor/human/formal proof or novelty clearance is claimed.
