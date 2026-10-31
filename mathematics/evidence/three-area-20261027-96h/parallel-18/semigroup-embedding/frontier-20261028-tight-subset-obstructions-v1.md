# Structural limits of the tight-sandwich condition

**NEW WRITTEN AUTHOR CANDIDATE; unreviewed and unadopted.** Native prewrite observation **Wed Oct 28 18:01:55 PDT 2026**. This is an additive algebraic analysis of the exact representation-dependent condition in `frontier-20261028-tight-sandwich-rees-criterion-v1.md`, SHA `03c4e9d83787a0b6b853ba85b2a3e5bf5c0ec21548e7359f9f333faf193ad7f2`. Its limited finite experiment is in §5. No original all-source solution or novelty is claimed.

## 1. Setup and results

Let A be ANY nonempty regular monoid, θ:A→G an onto group homomorphism, and `ι(a)=(b_a,θ(a))` a faithful homomorphism into a band-by-group semidirect product B⋊G. Let `e=b_1`, and write α for the actual G-action on B. A source element p is **tight relative to this fixed model** iff

`b_p=e α_(θ(p))(e)`.

The preceding note proves that this is equivalent to the full unmodified Rees-lift identity `b_(a p c)=b_a α_(θ(a)θ(p))(b_c)` for every source a,c; every unit is tight.

The following further statements are universal:

1. If p,q are tight, with g=θ(p), h=θ(q), their product is tight **iff**

   `e α_g(e) α_(gh)(e)=e α_(gh)(e)`.                       (P)

   Tight elements need not be closed under multiplication, even if p=q is a mutual-inverse element.
2. The identity 1_A is the **only tight idempotent**.
3. If α_(θ(p))(e)=e, then p is tight **iff p is a unit**. Consequently a genuinely nonunit tight sandwich must move the identity band coordinate under its group label.
4. Tightness is **not intrinsic to A and θ alone**: the same finite monoid and same group quotient can have two faithful V-band models for which a named nonunit is tight in one and nontight in the other.

These statements are restrictions on one proposed lift, not an all-host obstruction. Failure of tightness, failure of product closure or dependence on a representation does **not** establish nonembedding or collapse in B_q.

## 2. Exact product identity and singleton idempotent

The source identity `ι(1a)=ι(a1)=ι(a)` gives `e b_a=b_a` and `b_a α_(θ(a))(e)=b_a` for every a. If p,q are tight, direct multiplication gives

`b_(pq)=b_p α_g(b_q)`
`= (e α_g(e)) α_g(e α_h(e))`
`= e α_g(e) α_(gh)(e)`,

because α_g(e) is an idempotent. The tight coefficient for pq is `e α_(gh)(e)`, so (P) is both necessary and sufficient. No commutativity, extra unit in B, or rule that tight elements generate a subsemigroup was used.

If p∈E(A), θ(p)=1. Tightness gives `b_p=e α_1(e)=e²=e`. The two actual physical images `ι(p)=(e,1)` and `ι(1_A)=(e,1)` agree; faithfulness gives p=1_A. Conversely the source identity is tight. This proves statement2 without assuming any natural-order theorem.

## 3. Stabilizing the identity coordinate forces a tight element to be a unit

Let p be tight with g=θ(p) and suppose α_g(e)=e. Then b_p=e. Choose ANY actual mutual inverse p'∈V_A(p), available because A is regular. In the group G, θ(p')=g^(-1). As α_(g^(-1))(e)=e, the source identity gives `e b_(p')=b_(p')=b_(p') e`; hence b_(p') lies in the actual local band eBe. The action α_g preserves that corner.

From p p' p=p and the band component of ι,

`e = b_p α_g(b_(p')) α_(g g^(-1))(b_p)`
`  = e α_g(b_(p')) e = α_g(b_(p'))`.

Thus b_(p')=e. The physical images of pp' and p'p are both `(e,1)`, because α_g(e)=α_(g^(-1))(e)=e. Faithfulness makes pp'=p'p=1_A. So p is a unit. The reverse implication follows from the automatic unit formula already proved in the preceding note. This proves statement3 for every group label fixing e, including the trivial action and g=1; no arbitrary-element cancellation is used.

The contrapositive is a practical frontier constraint: any sought **nonunit** tight element must have α_(θ(p))(e)≠e. It does not say such an element exists for a given source or that an action moving e is sufficient.

## 4. Full finite counterexample to closure and representation independence

Use the explicit 15-element monoid A from the preceding note:

- `B=R^1×P({0,1})`, R^1 a 2×2 rectangular band with identity;
- G=C2 acts by flipping both R-coordinates and interchanging0,1 in the set factor;
- `e=(1_R,{0})`, `A=e(B⋊G)e`, and θ is the group coordinate;
- `p=(1_R,∅,1)`, `p²=(1_R,∅,0)`, `1_A=(1_R,{0},0)`.

Its inclusion ι into B⋊G is faithful. We have `b_p=e α_1(e)=(1_R,∅)`, so p is tight, while every product involving p has empty set-coordinate, so p is not a unit. It is self-inverse in its local group: p³=p. Its square is a source idempotent distinct from1_A, so by §2 it is **not tight**. Thus even p·p leaves the tight set, and the existence of inverse-stable-looking tight factors does not make sandwich closure automatic. This is a precise counterexample to the closure premise, not a nonregularity or embedding claim.

Now define `ρ:A→Q={∅,{0}}` by `ρ(v,U,h)=U`, with Q under intersection. It is a homomorphism: when h=0, its product set-coordinate is U∩V; when h=1, U is already empty, so both the true product set-coordinate and U∩V are empty.

Construct a second model with band `B'=B×Q` and action `α'_h=(α_h,id_Q)`:

`ι'(a)=((b_a,ρ(a)),θ(a))`.

It is a homomorphism by the preceding ρ identity and the original ι homomorphism, and is faithful because its B component is ι's band component and its group coordinate is unchanged. B' remains in V as a product with a semilattice. Let e'=(e,{0}). Then

`e' α'_1(e')=(e α_1(e),{0})`,
`b'_p=(e α_1(e),∅)`.

These are distinct, so the SAME p is nontight in ι'. Both representations use the SAME source A, the SAME θ and genuine allowed V-band actions. This demonstrates representation dependence directly, not by an unverified change of group coordinate or a numerical approximation.

## 5. Actually executed bounded exact check

`frontier-20261028-tight-set-stability-checker-v1.py`, SHA `63638854a8fdfa7c7646bfd395b05f6c72efdc7820f4fd0bd2a77d0199f5c689`, ran with `/opt/homebrew/bin/python3 -B` at **Wed Oct 28 18:01:24 PDT 2026**, timeout20s, exit0:

```text
source_size=15 original_tight_count=2
tight_elements=[(None, 1, 0), (None, 0, 1)] product_failure=((None, 0, 1), (None, 0, 1), (None, 0, 0))
two_faithful_models_same_group: p_tight=True p_tight_after_enlargement=False
PASS all225 mask-homomorphism and enlarged-model product/injectivity checks
```

The program imports the **same author's pinned** finite base multiplication from `frontier-20261028-tight-nonunit-rees-checker-v1.py` SHA `0398f9ed436b7fdbe2be250d4f6f07db134bded4ec77c6e58ff2945cf3c70bee`; it is not an independently authored finite verifier. It enumerates all15 actual source elements and all225 source products, rather than a truncated subset. The infinite/general statements are the written proofs in §§2–3, not extrapolations from this finite example.

## 6. Implication and unresolved target

A method that blindly closes the set of known tight P-entries under multiplication, or treats tightness as independent of the chosen faithful source representation, would be unsound. The exact product equation (P) and the stabilizer/unit lemma specify the missing hypotheses. In the Rees construction, each matrix entry need only be checked directly for tightness; the source-product calculation is still valid for arbitrary left/right factors even though the tight set is not a subsemigroup.

The full original embedding problem remains unresolved: these conditions classify only one concrete band-coordinate lift and do not exclude another source model or a nontrivial action. No independent-model/human/formal/kernel review, complete literature priority or novelty assessment has occurred. Earlier quarantines are historical records, not proofs or newly accepted premises.
