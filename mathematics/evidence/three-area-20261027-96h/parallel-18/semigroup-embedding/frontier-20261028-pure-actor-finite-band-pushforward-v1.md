# Pure onto completely-simple actor maps preserve local groups and need only a rectangular band enlargement

**NEW WRITTEN AUTHOR CANDIDATE; unreviewed and unadopted.** Native prewrite observation **Wed Oct 28 17:52:37 PDT 2026**. This independently reconstructs and sharpens the already recorded whole-host actor transport at the **surjective** pure-CS cut; it does not claim that the earlier U3 existence theorem is new. The extra conclusion is that no function-power extension of the band or enlargement of the structure group is needed: the target band can be `I_0×Λ_0×B` with the original B itself. No novelty or original all-source solution is claimed.

## 1. Theorem and useful consequence

Let `f:D0→D1` be ANY onto idempotent-pure homomorphism of nonempty completely simple semigroups, finite or infinite. Fix an actual Rees representation

`D0=M[G0;I0,Λ0;P0]`, `D1=M[G1;I1,Λ1;P1]`.

Let B be any nonempty band in V, the variety whose local corners are regular bands, with an action α:G0→Aut(B). Let `P(B,D0)` be the actual whole physical band-by-CS product.

**Claim.** There is a group isomorphism `h:G0→G1`, an action of G1 on the SAME B transported through h, and an explicit embedding

`Ψ:P(B,D0) ↪ P((I0×Λ0)×B,D1)` over f.                 (1)

The new band is a product of B with the rectangular band of source Rees row/column labels, so it remains in V. If B and the source row/column sets are finite, the constructed band remains finite; no function-space power is needed. No claim is made that Ψ is surjective or that the same physical band/action works without the rectangle and row gauges.

Consequently, if an actual original source S has a faithful physical host over ANY onto pure CS actor r:S→D0, then it has a faithful physical host over its actual syntactic pure CS actor q_τ. In particular, the unit-sandwich Rees sources of `frontier-20261028-unit-sandwich-rees-lift-v1.md`, SHA `8822d5ac2eeb8e50ee2e0d655b1a3619aa0f1ea43112caabb2083fb67b463747`, do **not** need the extra hypothesis `τ_D0=equality`: their actual canonical κ_q and both same-q R/L obligations are faithful for arbitrary such D0.

This is a conditional actor-transport theorem: it does not supply a faithful initial host for an arbitrary original source. It also does not assert unrestricted printed-target equivalence, a new nonembedding, novelty, or a proof for non-pure actor maps.

## 2. Pure surjective CS maps are local-group isomorphisms

Fix ANY idempotent e∈D0. The local semigroups eD0e and f(e)D1f(e) are groups, with identities e and f(e), by the Rees model. The restriction of f is a group homomorphism.

It is onto: for any z in the target local group, choose x∈D0 with f(x)=z (global onto-ness). Then exe∈eD0e and `f(exe)=f(e) z f(e)=z`.

It is one-to-one: if x,y lie in eD0e and f(x)=f(y), let y^{-1} be the inverse in that actual local group. Then f(xy^{-1})=f(e), an idempotent. Purity makes xy^{-1} idempotent in the source local group, whose only idempotent is e. Thus x=y.

This proof works for every actual source idempotent, with no assumption that f is injective on rows, columns or all of D0. It is the essential reason a **surjective** pure-CS actor map needs no coinduced B^(G1) power merely to extend the group action. For a non-surjective map this proof does not give surjectivity of local groups; that broader case is NOT covered by (1).

## 3. Rees homomorphism coordinates, derived and normalized

A homomorphism preserves R- and L-relations: if a=bx and b=ay in D0 then f(a)=f(b)f(x), f(b)=f(a)f(y), and similarly on the left. Rees R/L classes are rows/columns. Hence there are maps of row and column labels `a:I0→I1`, `b:Λ0→Λ1`.

Choose elementary normalized Rees coordinates for D0 with a base row i0 and column λ0 whose sandwich entries in that entire row and column are1. This is a standard elementary coordinate gauge: starting from P, set `A_i=p_(λ0,i)`, `B_λ=p_(λ,i0)p_(λ0,i0)^(-1)`, replace `(i,g,λ)` by `(i,A_i g B_λ,λ)`, and take `p'_(λ,i)=B_λ^(-1)p_(λ,i)A_i^(-1)`. The base row/column of P' are1, and `B_λ p'_(λ,i) A_i=p_(λ,i)` proves the product is preserved.

In these normalized coordinates put

`E_i=(i,1,λ0)`, `F_λ=(i0,1,λ)`, `T_g=(i0,g,λ0)`.

Every `(i,g,λ)` equals `E_i T_g F_λ`. Write the target group coordinates of f(E_i), f(F_λ), f(T_g) as `X_i,Y_λ,K_g`, and let `p*=P1_(b(λ0),a(i0))`. The base source H-class is a group, so `h(g)=K_g p*` is a group homomorphism. Factoring through E_i,T_g,F_λ gives

`f(i,g,λ)=(a(i), u_i h(g) v_λ, b(λ))`,
`u_i=X_i p*`, `v_λ=Y_λ`.                                  (RH)

Applying f to `F_λ E_j=T_(P0_(λ,j))` and cancelling only actual target group elements yields

`v_λ P1_(b(λ),a(j)) u_j = h(P0_(λ,j))`.                  (RH-P)

If original unnormalized coordinates are desired, undo the displayed gauge: replace `u_i` by `u_i h(A_i)` and `v_λ` by `h(B_λ)v_λ`; the same formulas (RH),(RH-P) follow. Thus these are reconstructed Rees homomorphism coordinates, not a blind use of an unverified row/column injection.

The map h is an isomorphism. More explicitly, the restriction of f from the base local group to its target local group is, in group coordinates, h followed by a fixed conjugation. Section 2 proves that restriction is bijective. Equivalently, in arbitrary coordinates with `p0=P0_(λ0,i0)`, `p1=P1_(b(λ0),a(i0))`, the source local element `(i0,x p0^(-1),λ0)` is sent to target local group parameter `u_(i0) h(x) u_(i0)^(-1)`. Therefore h itself is bijective. No independent assumption of full group image is made.

## 4. Explicit whole-host embedding with no power of B

Transport the action through h:

`γ_z=α_(h^(-1)(z))`,  z∈G1.

Let R0=I0×Λ0 be the rectangular band `(i,λ)(j,μ)=(i,μ)`. Let G1 act trivially on R0 and by γ on B. Define, for EVERY element of the whole source host,

`Ψ((b,(i,g,λ))) = (((i,λ), γ_(u_i)(b)), f(i,g,λ))`.        (2)

The band R0×B is in V: rectangles have regular local corners, direct products preserve the defining band identity, and B∈V. It requires no identity in B, no selected band element, no finite cardinality and no action-extension theorem.

For source actor factors `(i,g,λ),(j,k,μ)`, write `w0=g P0_(λ,j)`. By (RH-P), the target action weight is

`w1 = u_i h(g) v_λ P1_(b(λ),a(j)) = u_i h(w0) u_j^(-1)`.

Hence the target B-coordinate in Ψ(b,actor) Ψ(d,actor') is

`γ_(u_i)(b) · γ_(w1)γ_(u_j)(d)`
`=γ_(u_i)( b · α_(w0)(d) )`.

The rectangular coordinate becomes `(i,μ)`, and the actor coordinate is f of the source actor product. This is exactly Ψ of the original product, for EVERY b,d and actor pair. Thus Ψ is a whole-host homomorphism, not just a source-image formula.

If two Ψ images are equal, the rectangular coordinate recovers i and λ. Equality of the actor coordinates then gives `u_i h(g)v_λ=u_i h(g')v_λ`, so g=g' by injectivity of h. Equality of the B coordinates and invertibility of γ_(u_i) give b=b'. Hence Ψ is injective. No common-unit or rectangular collapse assertion is used.

## 5. Exact transport to the source syntactic actor

Let S be any regular semigroup with a faithful physical embedding `j:S→P(B,D0)` whose actor projection `r:S→D0` is onto and pure. For a nonempty band in this product, actor projection is automatically pure: if its CS coordinate is idempotent, the physical self-action weight is1 and the band coordinate squares to itself; faithfulness then reflects source idempotence.

For any onto pure r,

`s τ_S t  iff  r(s) τ_D0 r(t)`.                            (3)

The forward direction lifts each ACTUAL D0 context to S and uses purity; an absent actor context is handled by the corresponding absent source context. The reverse applies r to each source context and uses purity. Thus q_τS is `f∘r` up to the canonical isomorphism, where `f:D0→D0/τ_D0`.

D0 is regular and τ_D0 saturates idempotents by the absent-absent test. If q(x) is idempotent, choose an inverse t of x²; x t x is an idempotent in its class, so saturation proves q is pure. A homomorphic image of a completely simple semigroup is completely simple (ordinary named structural fact); equivalently, the full SQ-E proof already reconstructed in the cryptogroup note applies directly to D0, whose local corners are groups and whose natural order is equality. Therefore f has all hypotheses of §§2–4.

Compose Ψ with j. It is faithful over the SAME actual q_τS, after the displayed canonical actor isomorphism. The actual free-V-band universal property is direct: map every generator `X_(u,s)` to the transported action α'_u of the band coefficient of Ψj(s). Source multiplicativity proves every mixed relation, and the V identities/context relations hold in the constructed band. Hence κ_q is faithful. All same-q R- and L-idempotent separations follow; no global injectivity of β alone is claimed.

The preceding recorded whole-host U3 theorem also reached actor pushforward by the more general coinduced-power construction, including non-onto actor maps. The present argument independently pays the pure **onto** cut with the stronger same-B/rectangle and finite-band preservation; it does not retroactively replace or reverify the historical theorem's wider scope.

## 6. Application: remove the separated-actor restriction from the unit-Rees construction

Under the hypotheses of the pinned unit-sandwich Rees candidate, construct the source `S=M[A;I,Λ;P]`, the onto actor `r(i,a,λ)=(i,θ(a),λ)` and the faithful host `j(i,a,λ)=(b_a,r(i,a,λ))`. Its complete proof uses only unit sandwich elements and their actual `b_p=b_1` lift, not syntactic separation. The source is regular, weakly E-unitary and locally r-orthodox by the direct proofs there.

The present theorem now applies to **every** CS actor D0=M[G;I,Λ;θ(P)], even when its τ_D0 identifies rows/columns. Its q_τ quotient is actual and pure by (3); §§2–4 transport j to that quotient while retaining B up to a rectangle. Thus κ_q is faithful for ALL unit-sandwich sources satisfying the other displayed hypotheses. No arbitrary source is claimed to be such a Rees lift, and arbitrary nonunit sandwiches or missing unit-lift identities remain outside the result.

The earlier infinite example with nonorthogonal E, a noninverse local corner, and a non-completely-regular source remains an exact special case. The added finite example in §7 makes the removed actor-separation hypothesis genuinely observable.

## 7. Two executed exact finite checks

### Coarser actual actor

`frontier-20261028-unit-rees-coarse-actor-checker-v1.py`, SHA `88681e1c61f271e90ac8a61a5519fbf421823c428cc47db7d584651347522e79`, ran at **Wed Oct 28 17:48:06 PDT 2026**, timeout90s, exit0 (2.35s):

```text
source_size=90 idempotents=45 actor_r=18 actor_q=8
complete_contexts_per_source=8281 nonclosed_E=((0, (None, 0), 0), (2, (None, 1), 2), (0, (None, 1), 2))
same_q_idempotent_pairs=580 R_pairs=90 L_pairs=90
PASS source regularity, local_r, WEU, full actual tau, pushed host and R/L separation
CONTROL collapsing original source row rejected by pushed-host injectivity
```

This is a complete finite source/context check: r's18-element actor is strictly finer than the actual8-element τ actor. The pushed host retains original source row/column coordinates in its rectangular band; simply replacing r by q without them would lose faithfulness. The negative control demonstrates that failure on this source. It is one same-author finite witness, not an independent verifier or a proof for all P.

### Nontrivial row gauges

`frontier-20261028-surjective-actor-gauge-checker-v1.py`, SHA `3d6f70b65bc99767ea399eb95ef9119bf93157918765c8bf747ce63a5fd4787f`, ran at **Wed Oct 28 17:49:51 PDT 2026**, timeout20s, exit0:

```text
source_actor=18 quotient_actor=8 source_host=90
source_sandwich=((0, 1, 0), (1, 0, 1), (0, 1, 1)) row_gauges=(0, 1, 0) col_gauges=(0, 1, 0)
PASS full tau, pure surjective actor, every local-group isomorphism
PASS all 8100 source-host products and pushed-host injection with nontrivial row gauges
CONTROL omitted-row-gauge mismatches=2880
```

The second check validates a distinct finite actor/gauge configuration; both programs are same-owner and their exact output does not replace the all-variable proof or a disjoint review. No finite experiment proves that an arbitrary actor is pure/onto, and these examples do not establish novelty.

## 8. Exact remaining gap and verification level

The original challenge remains to obtain a faithful host, or an actual universal collapse, for **every** original weakly E-unitary locally r-orthodox source; not every source is shown to be a unit-sandwich Rees lift with a prior faithful A model. Condition (UL), the initial faithful embedding, and true unit sandwiches cannot be deleted without a new proof. The actor pushforward theorem only says that when an initial pure onto actor host exists, changing to τ does not create a new obstruction. It does not produce that initial host.

Used classical inputs: Rees representation of completely simple semigroups, their local-group structure and closure of the band variety under products; the displayed homomorphism coordinates/action transport, local-group isomorphism and whole-host injection are reconstructed here. The original theorem/proof ancestry and worldwide novelty remain unverified. No independent-model/human/kernel review or triple finite-witness certification occurred; current written candidate and finite scripts require disjoint review before adoption. Historical quarantined outcomes remain records, not premises or retrospectively validated results.
