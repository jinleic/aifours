# A finite-subsemigroup local-to-global criterion for pure CS actors

**NEW AUTHOR WRITTEN CANDIDATE with an exact nonnormal-subgroup gauge check; unreviewed/unadopted.** Native check-start observation **Wed Oct 28 19:19:29 PDT 2026**. This is an exact conditional reduction, not a proof that its finite obligations all hold, not a terminating algorithm for an arbitrary infinite source, and not a resolution of the original printed Q1/Q2. The compactness theorem, Green–Rees local finiteness of bands and Brown's semigroup extension theorem are named classical imports below. No original-source regularity is assumed for the finite subsemigroups.

## 1. Exact local-to-global statement

Let S be a **locally finite** semigroup, let `q:S→D` be an onto idempotent-pure homomorphism, and let D be completely simple. Use any fixed Rees presentation `D=M[G;I,Λ;P]`, with V the variety of locally regular bands. For every finite subsemigroup F⊂S, put `T_F=q(F)` and `r_F=q|_F:F→T_F`.

**Theorem.** The following are equivalent:

1. S embeds in a physical V-band-by-D host with actor EXACTLY q.
2. For every finite subsemigroup F⊂S, F embeds in a physical V-band-by-T_F host with actor EXACTLY r_F.
3. For every finite subsemigroup F⊂S, the canonical fixed-actor κ_(r_F) is injective.

T_F is finite and completely simple, and r_F is onto and pure. For each individual F, item3 is decidable by the finite-free-band construction in `frontier-20261028-finite-source-canonical-decision-v1.md`, SHA `b6f54918e468755366b215d64ac7fe247fcd3d73be6357105c8817ab47123f47`. That theorem works for a finite semigroup F with a given CS actor; it does NOT require F to be regular. The universal quantifier over all F may be infinite and gives NO terminating all-S decision procedure.

For an original regular S, a finite subsemigroup F can fail to be regular, even though q|_F remains pure. Therefore it is NOT legitimate to substitute “every finite original-class source” for item2 or item3 without an additional regular-subsemigroup containment theorem. Section6 exhibits the explicit nonregular F.

## 2. Finite actor images and the forward implication

A finite nonempty subsemigroup T of a CS semigroup D is CS. Each occupied T Rees cell is a finite nonempty subsemigroup of an ambient H-class group, hence is a subgroup containing that cell's identity. Products of occupied rows and columns occupy all cross-cells. If a∈T_(i,λ), b∈T_(j,μ), take cell identities x∈T_(i,μ), y∈T_(j,λ); xby lies in the cell group T_(i,λ), so its inverse z gives `x b y z a=a`. T is simple, and its idempotents are primitive because the ambient CS idempotent order is equality. The standard Rees characterization makes T CS. This does not assume F itself regular.

Given a global q-host, restrict its source to F and its actor image to T_F. The occupied-row/column Rees gauge calculation in `frontier-20261028-all-cs-obstruction-actor-gauges-addendum-v1.md`, SHA `99a310d0b058de9a4fc754a0d05388f4fc1ed41a46f7fd439878a49fe9646bda`, applies to ANY source homomorphism into that host: restrict the original G action along the subgroup map for `T_F↪D` and transform each band coefficient by its row gauge. It preserves the SAME V-band and gives a faithful host for F over T_F. Thus 1⇒2. The finite fixed-actor canonical universal property gives 2⇔3 without requiring F regular.

## 3. Extend a subgroup action without adjoining an identity

The reverse implication needs a real G action, not a partial action or an assumed fixed point. Let H≤G act on a nonempty V-band B by automorphisms δ_h. Choose representatives R for the left cosets `rH`, with 1∈R; write every x∈G uniquely as x=rh. Define the pointwise-product V-band

`C=B^G`,       `(γ_g F)(x)=F(xg)`,
`ι_B(b)(r h)=δ_h(b)`.                                     (4)

Each γ_g is an automorphism and `γ_g γ_k=γ_(gk)`. The map ι_B is an injective band homomorphism, with injectivity seen by evaluation at1. For h0∈H and x=rh,

`(γ_(h0)ι_B(b))(rh)=δ_(h h0)(b)=ι_B(δ_(h0)b)(rh)`.

Therefore γ restricted to H extends the given action equivariantly, including for NONNORMAL H. No identity, invariant basepoint or deletion/empty-support convention is introduced; V is preserved by direct products. This is an explicit coinduction construction, not a claim that δ extends on the original B.

Now let T=M[H;J,M;Q] embed into D, with Rees inclusion coordinates

`ι(j,h,μ)=(a(j),u_j φ(h) v_μ,b(μ))`,
`v_μ P_(b(μ),a(k)) u_k=φ(Q_(μ,k))`,

where φ:H→G is injective. Identify H with its subgroup image and use (4). Given a physical T-model of F with coefficient c_s, define, for a source actor row j,

`c'_s = γ_(u_j)(ι_B(c_s))`.

For source actor weights `w_T=h Q_(μ,k)`, the D weight is `u_j φ(w_T) u_k^(-1)`. Consequently

`c'_s γ_(u_j φ(w_T)u_k^(-1))(c'_t)`
`=γ_(u_j)(ι_B(c_s) γ_(φ(w_T))(ι_B(c_t)))`
`=γ_(u_j)(ι_B(c_s δ_(w_T)(c_t)))=c'_(st)`.

Thus F has a physical model over the GLOBAL actor D, still using q|_F. It is faithful: the inclusion T→D recovers the T actor; the common actor row fixes the gauge, and ι_B is injective. This proves the finite-to-global-actor extension with no assumption that H is normal, that the original B action extends, or that B has an identity.

## 4. Compactness supplies one simultaneous global host

Use a first-order language with a binary band product, one unary operation α_g for every g∈G, and one constant c_s for every s∈S. Include associativity, the band law, the local-regular identity on all corners, the group-action/automorphism equations, every source mixed equation

`c_(st)=c_s α_(g_s P_(λ_s,i_t))(c_t)`,

and `c_s≠c_t` for each distinct pair with q(s)=q(t).

Take any finite subset of these axioms. The finitely many mentioned source elements generate a finite subsemigroup F because S is locally finite. By item2, F has a faithful T_F host; §3 extends it to a full G-action host over D. Interpret the finitely many relevant source constants using this host, and any unused constants arbitrarily. All selected source equations, inequalities and action/variety axioms then hold. The case with no source constant has a one-element band model.

By the first-order compactness theorem, the entire axiom set has a model. Its band is in V, the α_g form a G action, and the mixed equations define a physical homomorphism over q. The inequalities make it injective inside every q-fibre; elements with different q values are already separated by the actor. Thus 2⇒1. This proof is existential and makes no finite target-size or effective construction claim for infinite S.

## 5. When local finiteness is automatic

For any onto pure q:S→D with D completely simple, S is locally finite **iff** a maximal subgroup G of D is locally finite.

If G is locally finite, D is locally finite: finitely many actor generators involve only finitely many rows/columns and finitely many sandwich/group entries, which generate a finite subgroup of G. Each idempotent fibre q^(-1)(e) is a band, since q is pure, and bands are locally finite by the named Green–Rees theorem. T. C. Brown's [On locally finite semigroups](https://www.sfu.ca/~vjungic/tbrown/tom-62.pdf), Ukraine Math. J. 20 (1968), main theorem, says an onto semigroup map to a locally finite semigroup with locally finite preimages of all idempotents has locally finite domain. Hence S is locally finite.

Conversely a homomorphic image of a locally finite semigroup is locally finite, so D and its subgroup G are locally finite. Brown's theorem is an explicit imported classical result, not independently proved here. Therefore the local-to-global theorem applies whenever the actual CS actor's maximal group is locally finite, including finite groups; it does not apply automatically to non-locally-finite groups.

## 6. Exact finite checks and the nonregular-subsource warning

`frontier-20261028-local-global-coinduction-checker-v1.py`, SHA `3a0d6c2f4dc6001f9e73ece7cf632d10b068f5956b274a73c39ee1e3d3ed8cfc`, ran `/opt/homebrew/opt/python@3.14/bin/python3.14 -B` at **Wed Oct 28 19:19:29 PDT 2026**, exit0. It uses G=S3 and a NONNORMAL C2 subgroup acting on the5-element locally regular nonregular band. It checks the embedding (4), all subgroup-equivariance/band equations and nontrivial Rees row/column gauges on every1600 products of a40-element physical source. Replacing right shifts by the wrong left shifts breaks4 equivariance cases.

The same script checks that the genuine original-class45-source with P=`((4,4,4),(4,1,3),(4,4,1))` contains the finite subsemigroup generated by `(1,4,1)`, namely

`{(1,4,1),(1,1,1),(1,2,1)}`.

The generator has NO mutual inverse inside that 3-element subsemigroup. Hence F need not be regular, despite the ambient original source being regular; a finite-original-source result alone cannot be used as item2. The actual source/actor proofs are in the previously pinned global-obstruction and locally regular-host notes.

The script does not prove compactness, Brown's theorem, the general coinduction formula or the local-to-global equivalence; these are explicitly written/named above. No cross-model/human/formal/kernel review, novelty or full-original-source resolution is claimed.
