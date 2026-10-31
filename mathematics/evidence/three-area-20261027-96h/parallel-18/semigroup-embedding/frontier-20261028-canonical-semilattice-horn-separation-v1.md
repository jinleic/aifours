# Horn closure for comparable separation in the finite canonical band

**Status: NEW AUTHOR WRITTEN EXACT REDUCTION and exact finite kernel control; UNREVIEWED / UNADOPTED.** This provides a polynomial-sized test for separation in the canonical band's **semilattice quotient**; it is not a decision procedure for the entire SN-band quotient, and does not prove comparable separation for every original source. It does not settle the same-q R/L gap.

## 1. Exact finite Horn criterion

Let S be a finite semigroup, `r:S→D=M[G;I,Λ;P]` a specified homomorphism with finite G, and let the canonical band generators be `X_(u,s)` for u∈G, s∈S. The defining physical mixed-product relations, from `frontier-20261028-finite-source-canonical-decision-v1.md`, SHA `b6f54918e468755366b215d64ac7fe247fcd3d73be6357105c8817ab47123f47`, are

`X_(u,st) = X_(u,s) X_(u w(s,t),t)`,  where `w(s,t)=g_s P_(λ_s,i_t)`.

Pass to the quotient in the variety of semilattices, write its multiplication as join ∨, and assign a Boolean value `v_i` to each generator. Every relation requires `v_z=v_x∨v_y`, where `z=(u,st)`, `x=(u,s)`, and `y=(u w(s,t),t)`. Put `T_i=1−v_i`. Then the complete constraint is the Horn system

`T_z⇒T_x`, `T_z⇒T_y`, and `T_x∧T_y⇒T_z`.        (H)

Let C(q) be the least closure of `{q}` under every rule (H). Two generator classes `X_p,X_q` differ in the canonical semilattice quotient **iff** `p∉C(q)` or `q∉C(p)`. Proof: if `p∉C(q)`, the characteristic assignment `T_i=1 iff i∈C(q)` satisfies all of (H), so its complementary v makes `v_p=1,v_q=0`. Conversely, every model with that separation contains C(q), hence p∉C(q). Finally, distinct elements x,y of ANY join-semilattice admit a Boolean join-homomorphism separating them: if `x≰y`, use `χ_y(t)=1` iff `t≰y`; the other case is symmetric. Thus absence of both Boolean orientations is equivalent to equality in the presented semilattice, not just failure of a guessed model.

The system has `n=|G||S|` variables and `m=|G||S|²` relation triples. Worklist Horn closure of one generator uses O(n+m) stored clauses/adjacencies and O(n+m) rule activations up to the usual duplicate-edge bookkeeping; all singleton closures use O(n(n+m)) such work. This is independent of the enormous free-band cardinality and does not require SAT, floats, or bounded model enumeration. It still assumes the source table, actor and weights are already explicitly given.

Because semilattices are seminormal bands, every separation in this quotient is a valid separation in the actual canonical SN band. One may also realize the Boolean assignment as an equivariant semilattice host: set `b_s(u)=v_(u,s)` and let `(α_h b)(u)=b(uh)` on `2^G`. The defining source relation holds coordinatewise by (H). Failure of semilattice separation does NOT imply failure in the noncommutative canonical SN band.

## 2. Exact 45-source control

For the pinned 45-element Rees source and actual18-element actor appearing in the positive25-band host, `frontier-20261028-semilattice-support-horn-v1.py`, SHA `01f0c7846cefa890192081c7ab4889ae9673ec76ec20bc985caa9396abaea88d`, was run in the Python eval kernel before Wed Oct 28 21:38:58 PDT 2026. Its final version has 90 Boolean variables, 4,050 mixed triples and 24 source idempotents. It computes each singleton Horn closure and rechecks every mixed equation for the proposed separating assignments:

```text
same-actor ordered comparable distinct idempotent pairs = 12
semilattice-separated = 12; semilattice-collapsed = 0
same-actor ordered distinct R/L idempotent pairs = 18
all 18 collapse in both orientations of the semilattice quotient
```

For example `(0,0,0)≤(0,4,0)` in the same actor fibre, and a closure-derived Boolean assignment distinguishes them. The R/L collapse is the expected limitation of commutative bands, not a negative result for the SN host: the already pinned noncommutative25-band host separates all same-actor idempotents. A prior successful development run checked the 12 comparable pairs before the final program added the 18 R/L control; the displayed final execution reran the amended program, not an independent review.

## 3. Actual progress and boundary

The construction gives an explicit alternative representation for the comparable-coordinate problem and a cheaply checkable Boolean certificate whenever this particular semilattice quotient separates a pair. In the displayed source it pays all 12 comparable pairs, but that one source is already known to have a faithful SN host and does not close the universal comparable, R, L or SEP problems. It is NOT valid to infer from this sample that all original sources pass (H), nor to infer nonembedding from an R/L collapse in the semilattice quotient. General Q1/Q2, all-actor transport, source novelty and independent review retain their separate statuses.
