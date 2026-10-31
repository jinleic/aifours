# A derivation-preserving reduction of the original canonical R and L obligations

**NEW AUTHOR WRITTEN reduction and exact failed invariant case; UNREVIEWED / UNADOPTED.** This concerns the original source class, its actual syntactic actor and both finite and infinite sources. It neither proves either separation obligation nor identifies the canonical statement with embedding into a host with an arbitrary actor. It does not use Fact1, unreviewed park-v3 constructions, or a held source/method.

## 1. Scope, presentation and named imports

An original source is as in the parent disposition: a nonempty regular S, q its actual syntactic idempotence-context quotient onto a completely simple semigroup D, q idempotent-pure, and the local idempotent bands regular. Fix Rees coordinates D=M[G;I,Λ;P]. Write q(s)=(i_s,g_s,λ_s), and `w(s,t)=g_s p_(λ_s,i_t)`.

Let V be any of SN, RIGHTSN, LEFTSN, with SN the band variety whose local monoids are regular, RIGHTSN the band variety whose local monoids are right regular (`xyx=yx`), and LEFTSN the dual. Define the canonical V-band C_V(S,q) by generators X_(u,s), u∈G and s∈S, **all band identities of V in all substitutions and contexts**, and the relations

`X_(u,st) = X_(u,s) X_(u w(s,t),t)` for all u∈G and s,t∈S.    (H)

The generator permutation X_(u,s)↦X_(vu,s) descends to a G-action because all relations are included for every u. Let β_V(s)=[X_(1,s)]. We take a free semigroup on G×S and quotient by the least congruence containing these relations; this construction is meaningful for infinite alphabets. All claims below are fixed-q claims about this explicit presentation.

Named imported scope: `dispositions/math-4-one-sided-source-reductions-canonical-gap-parent-v1.md` (SHA 63546947083781f1b7743eb656026f0c8bf2e94c4e3bfdbd7b6849d6bcd764f8) supports (i) the source congruences λ_S⊆R and ρ_S⊆L, each in ker q, and their left-/right-regular-local original-source quotients; (ii) for every SN band B, the characteristic band congruences λ_B⊆R and ρ_B⊆L, giving its locally left-/right-regular reflections and a subdirect embedding. The identity bridge defining SN by regular local bands is parent-supported in `dispositions/math-4-local-regular-seminormal-band-equivalence-parent-v1.md`, conditional on its named classical free-band input. We do not import the matching note's unadopted arbitrary-actor/canonical equivalence.

## 2. The quotient retains the ACTUAL actor, including for infinite S

Let θ be any congruence on S contained in ker q. The quotient map p:S→S/θ is idempotent-pure: if (p(s))²=p(s), then q(s)²=q(s), so s²=s by purity of q. Conversely idempotents map to idempotents. q factors as q̄(p(s))=q(s).

Let τ_S be the actual syntactic congruence: s τ_S t iff, for all a,b∈S¹, asb is idempotent exactly when atb is. Every context in (S/θ)¹ has representatives in S¹; by purity of p its idempotence bit is exactly that of any representing source product. Hence

`p(s) τ_(S/θ) p(t)  ⇔  s τ_S t`.                           (1)

Since ker q=τ_S and θ⊆ker q, ker q̄=τ_(S/θ). Thus q̄ is the ACTUAL syntactic quotient, not merely an arbitrary pure actor. Its target D and the chosen Rees coordinates are literally unchanged. This is a direct context calculation, not transport from an unrelated host actor.

Apply this to θ=ρ_S and θ=λ_S. Write S_R=S/ρ_S and S_L=S/λ_S, with the same target D and actual quotient maps q_R,q_L. By the named source reduction, S_R is an original RRL source and S_L an original LRL source.

## 3. Canonical one-sided reflections for this same q

Let B=C_SN(S,q). Since ρ_B is characteristic, the G-action descends to B/ρ_B. The generators' images still satisfy (H), and this quotient is RIGHTSN. Conversely C_RIGHTSN(S,q) is an SN band (a right-regular local band is regular), carries the same action and satisfies the same source relations. By the defining universal properties there are maps both ways:

`C_RIGHTSN(S,q) → B/ρ_B → C_RIGHTSN(S,q)`.

The second exists because ρ_B is the *least* locally right-regular congruence. Both composites fix every generator, hence are identities. Therefore there is a G-equivariant isomorphism

`C_RIGHTSN(S,q) ≅ C_SN(S,q)/ρ_B`, preserving every X_(u,s).   (2)

Dually `C_LEFTSN(S,q) ≅ C_SN(S,q)/λ_B`. No fixed-q universality is extended to arbitrary actors here.

Let e,f be idempotents in one q-fibre. Since q(e)=q(f) is idempotent, both weights w(e,f), w(f,e) equal 1; consequently β_V(ef)=β_V(e)β_V(f) and likewise for fe. If e R f, their SN-band images are R-related. Since ρ_B⊆L, equality after quotient by ρ_B forces them also L-related, hence equal (in a band, ab=b, ba=a and ab=a, ba=b imply a=b). Therefore

`β_SN(e)=β_SN(f)  ⇔  β_RIGHTSN(e)=β_RIGHTSN(f)` for same-fibre R-pairs.  (3R)

Dually

`β_SN(e)=β_SN(f)  ⇔  β_LEFTSN(e)=β_LEFTSN(f)` for same-fibre L-pairs.   (3L)

These are exact equivalences of equality in the stated fixed-actor presentations, not a claim that the pairs separate.

## 4. All-derivation projection and the two universal reductions

For V∈{SN,RIGHTSN,LEFTSN} and θ∈{ρ_S,λ_S}, the map on letters

`X_(u,s) ↦ X_(u,p(s))`

extends to every word. It sends each V-band identity substitution and context to the same V-identity substitution and context, and sends (H) to the corresponding quotient-source relation because p(st)=p(s)p(t) and q̄(p(s))=q(s), so the weights are unchanged. The same is true of reverse steps and G-label shifts. Thus **every finite derivation**, including those passing through label-inconsistent words, projects step by step to a valid derivation in C_V(S/θ,q̄). This does not claim that a source evaluation exists for intermediate words.

Now define the two universal claims:

- R(SN): for every original S and every distinct same-q-fibre R-related idempotents e,f, β_SN(e)≠β_SN(f).
- L(SN): for every original S and every distinct same-q-fibre L-related idempotents e,f, β_SN(e)≠β_SN(f).

**R reduction.** R(SN) holds if and only if every original RRL source has β_RIGHTSN separating its distinct same-fibre R-idempotent pairs. Forward direction: restrict to RRL sources and apply (3R). Reverse direction: for arbitrary S project to S_R. If e,f are distinct and e R f, then p_R(e)≠p_R(f): otherwise ρ_S⊆L would give e L f, hence e=f. Their images remain R-related idempotents in the same actor fibre. Hypothetical RIGHTSN equality in S would project to equality of the images, contrary to the RRL hypothesis; use (3R) for SN. The quotient's q_R is actual by (1).

**L reduction.** L(SN) holds if and only if every original LRL source has β_LEFTSN separating its distinct same-fibre L-idempotent pairs. Use S_L and λ_S⊆R in the dual argument, together with (3L).

These are universal all-source/all-derivation reductions for the **registered R and L questions separately**. They preserve actual q and require no Fact1. They are not proofs of R(SN), L(SN), comparable-pair separation, full faithful embedding, or any arbitrary-actor equivalence.

## 5. Exact first failure of the partial coherent-word evaluator

For a word X_(u1,s1)…X_(un,sn), call it q-coherent when `u_(j+1)=u_j w(s_j,s_(j+1))` for every j. Its source product s1⋯sn is then a natural **partial** evaluation. Relations (H) preserve coherence and source product when expanded inside a coherent context. It is tempting to use this partial evaluation as an all-derivation invariant; the following elementary step shows exactly why that does not work.

Take any nonidempotent s∈S and any inverse s′∈V(s). Purity gives q(s) nonidempotent, and the Rees formula gives `w(s,s)≠1`. Put e=ss′ and v=w(s,s′). The canonical derivation

`X_(1,e)  =_(H)^(-1)  X_(1,s) X_(v,s′)  =_(x=x²)  X_(1,s) X_(1,s) X_(v,s′)`  (4R)

is legitimate in **every** band presentation V. The first two words are coherent; the last is not, because the first adjacent pair would require `1=w(s,s)`. The first failure is the reverse idempotence relation, with substitution x=X_(1,s), empty left context, and right context X_(v,s′). It occurs already in a derivation beginning at the source idempotent e; no numerical example or selected table is used.

For the dual orientation put f=s′s and v′=w(s′,s). The derivation

`X_(1,f)  =_(H)^(-1)  X_(1,s′) X_(v′,s)  =_(x=x²)  X_(1,s′) X_(v′,s) X_(v′,s)`  (4L)

has coherent first two words and an incoherent last word. The failed substitution is x=X_(v′,s), with left context X_(1,s′) and empty right context. Equations (4R)/(4L) are not counterexamples to R or L separation and do not show that e or f participates in any distinct target pair. They identify the precise first obstruction to this proposed **definedness-preserving** invariant; a successful invariant may handle inconsistent words by a different construction.

If G is trivial, D is a rectangular band. Purity forces S to be a band, and the original local-regular hypothesis makes S an SN band by the named f144 identity bridge. Every weight in (H) is 1, so source multiplication gives a homomorphism S→C_SN and evaluation X_(1,s)↦s gives its inverse. Thus C_SN(S,q)≅S, and both R and L obligations hold in this degenerate case. The nonidempotent-substitution obstruction above cannot occur there. This is a boundary of (4), not a substitute for the nontrivial-group all-source problem.

## 6. Remaining gap and evidence label

The quotient projection of §4 preserves **every derivation** but detects a pair only if its image is already known separate in the appropriate one-sided quotient. No general separating invariant in the RRL/RIGHTSN or LRL/LEFTSN target is proved. The coherent-word evaluator fails at the explicit first elementary relation (4R)/(4L), so one cannot silently restrict a full proof to coherent intermediate words.

Everything new in this packet is same-author WRITTEN reasoning with the named parent-supported inputs; no selected-instance table, arithmetic probe, new program, independent review, formal proof, actor-transport repair, Fact1 compatibility, novelty or Q1/Q2 closure is claimed. The STOP record and its consumers are not used as mathematical inputs.
