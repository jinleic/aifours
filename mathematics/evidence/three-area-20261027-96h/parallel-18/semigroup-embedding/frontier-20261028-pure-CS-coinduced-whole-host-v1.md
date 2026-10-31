# Pure CS actor maps transport entire physical hosts, including nononto maps

**NEW AUTHOR WRITTEN CONSTRUCTION with exact finite check; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 19:25:27 PDT 2026**. This independently reconstructs, in the present frontier, the more general pure-actor transport that earlier notes named at narrower onto scope. It does not retroactively modify or adopt any historical gate, and it does not supply a host for an arbitrary original source.

## 1. Exact whole-host theorem

Let `f:D0→D1` be an idempotent-pure homomorphism between arbitrary completely simple semigroups, not necessarily onto or one-to-one. Give them Rees coordinates

`D0=M[G0;I0,Λ0;P0]`, `D1=M[G1;I1,Λ1;P1]`.

Let B be any nonempty locally regular band with a G0 action. Then the ENTIRE physical product P(B,D0), not just a selected source image, embeds into a physical product over D1. An explicit target band is

`B'=(I0×Λ0) × B^(G1)`,

where I0×Λ0 is rectangular and G1 acts trivially on it and by right shifts on the power. The construction allows infinite groups, nonnormal subgroup image, and collapsed source rows/columns. In particular, any faithful source model over D0 can be transported to actor `f∘r` without changing its source.

If f is onto, its local group map is an isomorphism; the power can be replaced by the SAME B, giving `(I0×Λ0)×B`. This recovers the finite-band preservation of `frontier-20261028-pure-actor-finite-band-pushforward-v1.md`, SHA `abdfecbfb03b7931ad8dac0e7912f6c359279fe7afd47662a4f376942b2d9057`, at its precise onto scope. The general nononto statement makes no finite-target claim when G1 is infinite.

## 2. Injective local group map and exact Rees gauges

For any source idempotent e, the restriction of f to its local group is injective. If f(x)=f(y), then `f(x y^(-1))=f(e)` is idempotent; purity makes x y^(-1) idempotent in the source local group, hence its identity, so x=y. No onto assumption is used.

The standard elementary Rees homomorphism factorization, reconstructed via normalized row/column generators in the named predecessor §3, gives row/column maps a,b, a group homomorphism φ:G0→G1, and actual gauge elements u_i,v_λ such that

`f(i,g,λ)=(a(i),u_i φ(g) v_λ,b(λ))`,
`v_λ P1_(b(λ),a(j)) u_j=φ(P0_(λ,j))`.                   (2)

The source base local group is mapped by φ up to a fixed group conjugation. The local-group injectivity above therefore makes φ injective. Row and column maps a,b need not be injective, and φ(G0) need not be normal or all of G1. Formula (2) and Rees representation are the exact named classical/previously reconstructed inputs.

## 3. Coinduce the action without an identity or fixed point

Identify G0 with its subgroup `H=φ(G0)≤G1` and transport its B action to H. Choose representatives R of the LEFT cosets rH, with 1∈R. Every x∈G1 is uniquely r h. Let

`C=B^(G1)`,       `(γ_g F)(x)=F(xg)`,
`J(b)(r h)=α_(φ^(-1)(h))(b)`.                            (3)

C is a locally regular band under pointwise multiplication. Right shifts form an action by automorphisms because `γ_g γ_k=γ_(gk)`. J is a band homomorphism and is injective by evaluation at1. For h0∈H,

`γ_(h0)J(b)(r h)=α_(φ^(-1)(h h0))(b)=J(α_(φ^(-1)(h0))b)(r h)`.

Thus J is G0-equivariant. This construction works for nonnormal H; it requires neither an action extension on the original B nor adjoining a band identity or choosing an α-fixed element.

## 4. The whole-product embedding

Make `R0=I0×Λ0` the rectangular band `(i,λ)(j,μ)=(i,μ)`, let G1 act trivially on R0 and by γ on C, and define

`Ψ(b,(i,g,λ)) = (((i,λ), γ_(u_i)J(b)), f(i,g,λ))`.       (4)

For source actor `(i,g,λ)(j,h,μ)`, its source action weight is `w0=g P0_(λ,j)`. The target weight is, by (2),

`u_i φ(g) v_λ P1_(b(λ),a(j)) = u_i φ(w0) u_j^(-1)`.

Hence the C-coordinate of the target product equals

`γ_(u_i)( J(b) · γ_(φ(w0))J(c) )`
`=γ_(u_i)J(b · α_(w0)c)`,

and the rectangle becomes `(i,μ)`. This is Ψ of the source physical product for EVERY band coefficient and actor pair, not just named source generators.

For injection, the rectangle recovers i,λ. Equality of target actors then gives `φ(g)=φ(g')`, hence g=g' by injectivity of φ. Equality of the C coordinates and injectivity of J give b=b'. Therefore Ψ is a whole-host embedding. R0×C is locally regular because it is a product of such bands.

If f is onto, its restriction to a local group is also onto: sandwich a preimage of any target local-group element by the source local idempotent. Therefore φ is an isomorphism. In (3) there is one H-coset, and the orbit subband `{J(b):b∈B}` is γ-invariant under all G1 and isomorphic to B; (4) may be restricted to R0×B. This establishes the onto specialization without a finite product power.

## 5. Actual syntactic actor consequence

For a regular source S with an onto pure CS actor `r:S→D0`, idempotence contexts lift/reflect, so `τ_S=r^(-1)(τ_D0)`. The syntactic quotient map `f:D0→D0/τ_D0` is pure: τ saturates idempotents, and a quotient idempotent has an idempotent representative by regularity. The image is CS. Applying the onto specialization of §4 to any faithful natural-D0 source host gives a faithful physical host over its ACTUAL q_τ, then the canonical free-V-band universal map proves κ_q injective. Thus the actual-q deductions in the new Rees-family packets follow from this written proof if reviewed and accepted; they are not retroactively declared reviewed here.

The same theorem also extends a faithful source model to a larger CS actor under a pure nononto map. It says nothing when f is not pure and does not construct the initial source model.

## 6. Exact nonnormal, nononto and row/column-collapse check

`frontier-20261028-pure-nononto-transport-checker-v1.py`, SHA `dc8caf28977376a30827e736d80429d4c99fb3e0942e9d77ede8a9ceedb28400`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 19:25:27 PDT 2026**, exit0. Its original band is the pinned5-element locally regular nonregular countermodel; G0=C2 acts nontrivially, and its subgroup image in G1=S3 is NONNORMAL. The pure CS map has source18 elements, image8 and target24; both its row and column maps collapse classes.

```text
pure map D0=18 image=8 target=24; group C2→S3 nonnormal; rows/cols collapse
PASS entire90-element physical host, all8100 products and injection with rectangle
CONTROL removing rectangle identifies two distinct source elements
```

The verifier checks every source D0 product, map purity, all90² WHOLE physical host products and injections, with nontrivial row/column gauges. Its rectangle-deletion control produces an actual collision. The different `frontier-20261028-local-global-coinduction-checker-v1.py`, SHA `3a0d6c2f4dc6001f9e73ece7cf632d10b068f5956b274a73c39ee1e3d3ed8cfc`, directly checks subgroup equivariance and observes4 failures for a deliberately wrong left-shift convention. Both are same-author finite checks, not independent witness certification or a proof of the general theorem.

No historical U3 review, external-model/human/formal proof, novelty or full-original-source closure is inferred from this note.
