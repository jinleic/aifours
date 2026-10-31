# Repaired two-syndrome entropy theorem: actual local component decoders

**Status: WRITTEN with exact Shannon-certificate and finite-gadget checks; independent scientific review pending.** The earlier theorem candidate is subject to required pre-source erratum `frontier-20261028-two-syndrome-local-neighborhood-erratum-v1.md` SHA-256 `8ff79f6d07b935025e0b2f3de27928f030d251787724b64e05ccd9f1f012a37f`. The crucial correction is that the dual's local conditional FDs are **not** supplied by the original graph FDs; they follow instead from the actual triangle-factor component parities, as shown below. This successor does not modify or silently clear any earlier record.

## Theorem

For each of the ten ordered triangles of R-minus choose a nontrivial finite group `G_t`, not necessarily abelian. Give vertex `v` one group element from each of the three triangles containing it; let `X_v` be that triple. The ordered product of the three components in triangle `t` is its syndrome `sigma_t in G_t`.

For every finite joint law on these vertex triples satisfying all original-neighbour graph FDs, if the vector `(sigma_1,...,sigma_10)` takes at most two values, then

\[
H(X_V)\le\frac23\sum_{v=1}^{10}H(X_v).\tag{37}
\]

Hence any FD support in these two syndrome classes has at most `product_t |G_t|^2` words. The fixed-identity triangle-product support attains equality. When all groups have order `m`, the vertex alphabet is `q=m^3` and the support bound is `m^20=q^(20/3)`. This is a strict support-class theorem, not a general q-ary or unrestricted guessing-number bound.

## Common-selector lemma: all ten factors vary

Suppose all ten factor syndromes take one of two distinct per-factor group values, with the same binary selector `S`. Each factor syndrome determines `S`. The original-neighbour FDs imply `S` is determined by every neighbour tuple: choose a triangle containing `v`, recover `X_v` from `X_{N(v)}`, and evaluate that triangle's syndrome. A triangle's three vertex blocks directly determine `S`.

**Crucial local FD.** Let `L(v)` be the union of all other vertices in the ten triangles containing `v`. Given `S` and `X_{L(v)}`, each component of `X_v` is the unique group solution of its own triangle product equation. Thus

\[
H(X_v\mid X_{L(v)},S)=0\quad\text{for all }v.\tag{38}
\]

This holds at `v=3,4` although `L(v)` omits the original graph edge `3--4`. It relies on the actual group-factor representation, not on the original FD alone. The inverse formulas are stated and checked in `frontier-20261028-group-syndrome-gadget-check.py` SHA-256 `f9343b21eb991908211baae6b24a3f77d9cf12cb9951c3b08dbad94cc728551e`; receipt SHA-256 `ec1ac1a241e8647bdcb2d30e08a2dee06dc31cc9e75b9d76013ab696e60c1326` includes a nonabelian `S3` check.

Conditioning on `S`, any two components in each group triangle determine the third. Conditional triangle subadditivity and factor-by-factor tensorization yield `3H(X_V|S)<=2 sum_v H(X_v|S)`; since `S` is determined by `X_V`, this is the gate `G_S=3H(X_V)+17H(S)-2 sum_v H(X_v,S)<=0`.

The exact rational certificate `frontier-20261028-two-syndrome-all-factor-dual-v1.json` SHA-256 `a8f6822f2c3e3a8e0b0fd639a9b0095a8ea6f38c7833f0ef2fb6551fa9bba087` expresses `Delta` as negative elemental Shannon rows, original-FD equalities, syndrome-from-neighbour and syndrome-from-triangle equalities, local-factor equalities (38), and `(37/492)G_S`. The separate checker SHA-256 `64fa545134f913993ee9dd4857a7904010200b1bd546b66cccbfbc8842d0b65a`, receipt SHA-256 `8bd6527e81cd17c9a950d24a7e6f67e8ce29cb0d1f4af4ac7e34c570425f221d`, verifies all 2,047 coefficients, rational signs and all automorphisms. Every term is nonpositive or zero, proving (37) in the common-selector case.

## General difference set

For two arbitrary distinct syndrome vectors `s,t`, let `J={r:s_r!=t_r}`. Apply the bijection `X_i^r -> s_r^(-1)X_i^r` to the first component in each ordered triangle. Its syndromes become identity and `d_r=s_r^(-1)t_r`. For `r in J`, `d_r` is nonidentity and determines the same binary selector `S`; for `r notin J` the syndrome is fixed.

If `J` does not cover all ten vertices, condition on the fixed-syndrome factors first. At least one selected vertex block is constant, so the proper-subgraph entropy theorem `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49` gives nonpositive gap on the selected block, and conditional factor tensorization yields the original result. This import has its own exact independent checker but remains under scientific review.

If `J` covers all vertices, condition on the entire fixed-factor tuple. In each positive-probability fiber, selected blocks retain the original FDs and `S` is a function of every original-neighbour tuple. For each omitted factor `r`, choose any nonidentity `d_r in G_r` and append independent uniform `A,B in G_r` and `C=B^(-1)A^(-1)h_r(S)` with `h_r(0)=e_r`, `h_r(1)=d_r`. The new syndrome determines `S`; every new component is locally determined by `S` and the other two triangle components, so (38) holds in the augmented full-factor law. It also has the original FDs, since neighbour blocks already recover `S`. Each appended singleton component is uniform independent of the pre-existing law and other components at the same vertex; each factor increases joint entropy by `2log|G_r|` and singleton entropy sum by `3log|G_r|`, preserving `Delta`. The common-selector lemma therefore bounds every selected-block fiber; tensorize the fixed factors as above.

For one syndrome vector, all factors are fixed-syndrome and direct tensorization gives (37). Exact incidence/cover/lift-gadget checks are recorded in `frontier-20261028-two-syndrome-lifting-check-result.json` SHA-256 `d825e6c731219f3af2b965ed6941a9656eba9ab77b6ccadd1197df85c60c8f90`. These checks supplement rather than replace the written fiber, entropy and finite-group proofs. The main remaining science question is what happens with three or more syndrome vectors; formal proof, independent scientific adoption and novelty clearance are not asserted.
