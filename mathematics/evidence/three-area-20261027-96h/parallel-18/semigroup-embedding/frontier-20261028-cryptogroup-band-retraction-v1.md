# Direct same-quotient separation for locally r-orthodox cryptogroups

**NEW WRITTEN AUTHOR CANDIDATE; unreviewed and unadopted.** Native prewrite observation **Wed Oct 28 17:09:04 PDT 2026**. A bounded exact 36-element source check is reported in §7. This note does not use the external SZ87 embedding theorem or its unproved proof. No formal/kernel or novelty clearance is claimed.

## 1. Main result: an explicit global V-band invariant

Let S be ANY nonempty finite or infinite regular semigroup satisfying the printed weak E-unitarity and locally r-orthodox hypotheses. Suppose, additionally, that S is **completely regular** (every element lies in a subgroup) and its Green relation H is a semigroup congruence; this is the standard definition of a **cryptogroup**. Let q:S→C=S/τ be its ACTUAL syntactic idempotence quotient as in §2, and let B_q,β,κ_q be its canonical V-band/actor construction as in §3.

**Claim.** The band `B=S/H` belongs to the exact local-regular-band variety V. The natural quotient `π:S→B` separates ALL source idempotents. With the identity action of the group in the chosen Rees coordinates of C on B, the map

`X_(u,s) ↦ π(s)`

induces an equivariant band homomorphism `h:B_q→B`. Thus `β(e)=β(f)` implies e=f for every e,f∈E(S), whether or not q(e)=q(f). Moreover

`j:S→B×C`,  `j(s)=(π(s),q(s))`

is injective and multiplicative. Hence κ_q is injective and the original actual same-q R- and L-idempotent separation obligations both hold for **every** source in this named subclass. Because the action is trivial, j is an explicit direct-product/semidirect-product witness, not a proposed common-unit completion or a rectangular-only invariant.

The printed Question 1 follows for this subclass under the standard convention that a trivial-action band-by-completely-simple product is B×C; B is seminormal and C is completely simple. This is NOT the general printed question and not an assertion that the printed target and canonical formulation are equivalent in full generality. The subclass extends beyond globally orthodox sources: §7 supplies an exact actual nonorthodox and non-simple cryptogroup where the idempotents do not form a band and both R/L fibre obligations are nonvacuous.

## 2. Actual τ actor: reconstructed hypotheses and source

Use exactly

`s τ t` iff `x s y ∈ E(S) ↔ x t y ∈ E(S)` for every `x,y∈S¹`,

where S¹ allows absent contexts even when S has no identity. This relation is an equivalence and a congruence by moving a multiplied factor into the appropriate context. An absent-absent context shows τ saturates the source idempotents. For any onto homomorphism from a regular S and any a whose image is idempotent, choose t∈V(a²); then `b=ata` is idempotent because `(ata)²=a t a² t a=ata`, and b has the same quotient image as a. Thus the quotient q by any idempotent-saturating congruence, in particular τ, is idempotent pure.

The actual quotient C is completely simple under the original weak-E-unitary and local orthodoxy hypotheses. The existing complete SQ-E source is `math-4-source-packet-v1.md` S2:15–104, SHA `5a671de2533ed5c1dd241695bde1cb03f2833f0467a67f0c7440b0f7f5eddf4e`; its used argument is reconstructed in §2.1. The only named ordinary structural characterization at the end is: a nonempty simple semigroup with a primitive idempotent is completely simple. No arbitrary-source group quotient or global E(S) closure is assumed.

### 2.1 Written reconstruction of SQ-E at the exact source cut

If b³=b² then d=b² is idempotent with d=db=bd, so d≤b and weak E-unitarity gives b idempotent. Hence `ab∈E iff ba∈E`: `(ba)³=b(ab)²a=b(ab)a=(ba)²` when ab is idempotent. If f is idempotent and fv=v, this cyclic property gives `v∈E iff vf∈E`.

Every actual eSe is orthodox. In any orthodox subsemigroup T, if e∈E(T), a∈T and ea∈E(T), cyclic idempotence gives ae∈E(T). Their product aea lies in E(T), and `aea=(ae)a=a(ea)≤a`; weak E-unitarity implies a∈E. The right-sided version is symmetric.

If source idempotents e,f satisfy ef=fe=e, their contextual idempotence tests coincide. For the forward direction, from xey∈E obtain eyx∈E by cyclicity. As f(eyx)=eyx, its product eyxf is idempotent. Set u=fyxf∈fSf; then eu=eyxf is idempotent, so local unitary-E gives u∈E. For v=fyx, fv=v and vf=u; the support equivalence gives v∈E, and cyclicity gives xfy∈E. Conversely xfy∈E gives v=fyx∈E, hence u=fyxf∈E; e,u are idempotents in the same orthodox local monoid so eu=eyxf∈E. Set w=eyx; fw=w and wf=eu, so w∈E, hence xey∈E. Absent x/y are allowed. Therefore e τ f.

To see all quotient idempotents primitive, take ε≤φ in C and lift both to source idempotents e,f using the preceding lift. The element k=fef has q(k)=φ ε φ=ε, so purity makes k idempotent. Since k≤f, the just-proved comparable-idempotent property gives k τ f, so ε=φ. C is regular as a homomorphic image. For any idempotents ε,φ in C, take p=εφ and v∈V(p). The elements `p v ε≤ε` and `φ v p≤φ` are idempotents; primitiveness gives `p v ε=ε` and `φ v p=φ`, so p is R-related to ε and L-related to φ. All idempotents, hence all regular elements, lie in one D-class; C is simple with a primitive idempotent. By the named standard characterization it is completely simple. No unsupported identity-image case is hidden.

## 3. Canonical presentation and general trivial-action criterion

Use a Rees representation `C=M[G;I,Λ;P]`, write `q(s)=(i_s,g_s,λ_s)` and `w(s,t)=g_s p_(λ_s,i_t)`. The ordinary Rees representation is a named classical structural import; no proof of it is claimed here. Form the free V-band on all `X_(u,s)` (u∈G, s∈S), modulo the ENTIRE relations

`X_(u,s) X_(u w(s,t),t)=X_(u,st)` for all u,s,t.             (M)

The canonical G-action shifts the first coordinate, `β(s)=[X_(1,s)]`, and the actual physical host has

`κ_q(s)=(β(s),q(s))`,
`(b,(i,g,λ))(d,(j,h,μ))=(b α_(g p_(λ,j))(d),(i,g p_(λ,j)h,μ))`.

**General lemma.** For any such S and q, let ρ:S→D be any semigroup homomorphism into a V-band D. Give D the trivial G-action. The assignment `X_(u,s)↦ρ(s)` satisfies ALL M relations because `ρ(s)ρ(t)=ρ(st)`; all V identities, substitutions and outer contexts hold in D. Hence it induces an equivariant band homomorphism `h:B_q→D` with `hβ=ρ`.

Conversely, any equivariant h:B_q→D when D has trivial G-action produces a source homomorphism ρ=hβ: M at u=1 gives `β(st)=β(s) α_(w(s,t))β(t)`, and applying h gives `ρ(st)=ρ(s)ρ(t)`. Thus the existence of such an h whose `hβ` is **globally idempotent-separating** is EXACTLY equivalent to existence of an idempotent-separating source homomorphism into a V-band. This criterion does not claim that every canonical embedding must use trivial action, or that failure of this stronger global-idempotent criterion implies failure of the original host problem.

If ρ separates source idempotents and β(e)=β(f), apply h to obtain e=f. Thus both same-q R- and L-idempotent tests are paid simultaneously, as well as any distinct-idempotent test. This is a valid all-derivation invariant because h is a homomorphism on the quotient, not a coherent-word-only map.

## 4. Why S/H is a V-band and separates all idempotents

Because H is assumed a congruence, B=S/H is a semigroup. Every s belongs to a subgroup and is H-related to its group's unique idempotent e_s; thus `[s]^2=[s²]=[s]`, so B is a band. If two source idempotents are H-related, their common H-class is a group with a unique idempotent, so they are equal. Therefore π is idempotent-separating.

It remains to prove the **local** identity of B rather than silently assuming global regularity. Fix any b∈B. Pick the unique source idempotent e in any H-class mapping to b; then `bBb=π(eSe)`. For any x∈eSe, let x# be the inverse of x in its own subgroup and f=xx#=x#x. From ex=x=xe it follows that `ef=f=fe`; consequently `ex#=x#=x#e`, so x#∈eSe and f∈E(eSe). Since x H f, π(x)=π(f). Hence

`π(eSe)=π(E(eSe))`.

The original locally r-orthodox hypothesis says E(eSe) is a regular band. Its homomorphic image `bBb` is therefore a regular band, including for every b and every degenerate corner. This is exactly the V property, so the displayed map in §1 is well-defined. No closure of E(S) globally, no uniqueness of inverses outside the H subgroup and no external embedding theorem is used.

## 5. Injectivity in the SAME actual actor

Suppose π(s)=π(t) and q(s)=q(t). The first equality says s H t, so s,t lie in the SAME group H-class, with identity e and inverse s# of s. Since q is a homomorphism,

`q(s#t)=q(s#s)=q(e)`,

an idempotent. Actual q-purity makes s#t an idempotent in S. It belongs to the SAME group H-class, whose only idempotent is e; hence s#t=e and t=s. Thus j=(π,q) is injective for all source elements. Its multiplication is the direct product multiplication because π and q are both homomorphisms.

The all-generator homomorphism h in §3 has hβ=π. Therefore equality `κ_q(s)=κ_q(t)` forces π(s)=π(t) and q(s)=q(t), and the previous paragraph forces s=t. This independently pays the full κ injection directly, without a proof of any R/L-to-SEP equivalence, prior all-host theorem, common matrix, old globalization guide or unvalidated review. The source-side quotient π keeps the full H-class structure; it is NOT the actor quotient q.

The necessary trivial-action condition has a useful converse within completely regular S. If an idempotent-separating homomorphism ρ:S→D into ANY band exists, its restriction to each subgroup is constant: a group image in a band is trivial. Therefore ρ(s)=ρ(e_s). Equality ρ(s)=ρ(t) forces e_s=e_t by idempotent separation, which means s H t; the reverse holds because same-H elements lie in one group. Thus `ker ρ=H`, forcing H to be a congruence. Conversely H-congruence gives π as above. Under local r-orthodoxy, **for completely regular sources**, the all-idempotent-separating trivial-action V-band invariant exists iff H is a congruence. This is a condition on that restricted invariant only, not a no-go for noncryptogroup canonical hosts with nontrivial actions.

## 6. Novelty, imports and original target boundary

This is an explicit uniform relative-conservativity bridge for one substantive original-class subclass; it does not prove the original embedding question for sources outside the cryptogroup subclass. The cryptogroup terminology is standard: Wang–Feng–Chen, [*Some special congruences on completely regular semigroups*, §1](https://arxiv.org/html/1901.08776v1), defines completely regular and cryptic/H-congruence, calling the conjunction a cryptogroup. No theorem from that article is used in the proof.

Ordinary imports used and stated: the Rees representation of a completely simple semigroup; group structure of H-classes in a completely regular semigroup; and the characterization simple plus primitive idempotent ⇒ completely simple. Their standard proofs are not reproduced, so formal import/source validation remains a review obligation. The actual τ purity, source-to-V-band map, all M relations, original cryptogroup hypotheses, same-actor injectivity and physical trivial action are proved above.

There is no claim that this subclass result or the bridge is novel; it may be classical. No printed Question 2 generalization, arbitrary locally r-orthodox semigroup, noncryptogroup obstruction, all-host equivalence beyond the displayed host, or equivalence between the complete registered and printed targets is inferred. Syntactic quotient purity is used rather than presuming any group quotient. No earlier held review output is an accepted premise.

## 7. Exact genuine residual witness and bounded check

Let C be the Rees matrix semigroup on G=C2, I=Λ={0,1,2}, with sandwich entries (written additively modulo2)

`P=((0,0,0),(0,0,0),(0,0,1))`.

Let L be the two-element meet semilattice and S=C×L. This is an **explicit 36-element semigroup**, not an arbitrary abstract tuple. The exact checker below confirms its associativity, regularity, every local r condition, printed natural-order weak E-unitarity, complete regularity, H-congruence by principal left/right ideals, and the q syntactic congruence by all actual/absent two-sided contexts. It also checks S has a proper ideal, so this is not merely a completely simple source.

The actual idempotents `(0,0,0,0)` and `(2,1,2,0)` multiply to `(0,1,2,0)`, which is not idempotent. Consequently this original-class source is **outside the global-regular-E subclass** of `frontier-20261028-global-regular-band-separation-v1.md`, yet satisfies the hypotheses here. Its same-q fibre has nontrivial distinct R and L idempotents, so the tested separation is not vacuous. This demonstrates a real gap in trying to cover the entire original class by the preceding global-E theorem; it is NOT a nonembedding example.

Checker `frontier-20261028-cryptogroup-exact-checker-v1.py`, SHA256 `96e88d631ef3819651eefc538f42261300e169dcfc8151ca7618f27605dddb68`, was run with `/opt/homebrew/bin/python3` at **Wed Oct 28 17:08:16 PDT 2026**, timeout30s, and returned exit0:

```text
source_size=36 idempotents=18 H_classes=18 tau_quotient_size=8
proper_ideal_size=18 idempotent_nonclosure=((0, 0, 0, 0), (2, 1, 2, 0), (0, 1, 2, 0))
same_q_idempotent_pairs=82 R_pairs=12 L_pairs=12
PASS associativity, regularity, local_r, WEU, completely_regular, non-simple, E_nonclosed
PASS H_via_ideals, H_congruence, V_band_quotient, idempotent_separation, q_purity, host
CONTROL row-collapse remains homomorphic but fails host injectivity
```

An independently written checker/review has NOT yet certified this object or the proof. The run is a definition-based bounded experiment, not proof of the universal theorem. `frontier-20261028-rees-nonorthodox-checker-v1.py`, SHA `8b75b821f2817af5e4c0db437d632a6ff635fb97652a481c9a9201d2e856a80f`, independently checks an 18-element completely simple related source and a separate negative control; it returned exit0 at17:06:44, but these files share the same author and model construction and are not claimed as independent implementations of the 36-element witness.

## 8. Remaining gap and verification status

Remaining: arbitrary original weakly E-unitary locally r-orthodox regular sources that are NOT cryptogroups, and not otherwise covered by the separate globally regular-E / SZ87-dependent argument. No finite search failure or nontrivial action observation is a nonembedding proof. Original full target and Question 2 remain open at this record's scope.

Actual verification: symbolic written derivations above, the exact code execution and control in §7, and reading the separately identified source definition. No peer/external-model review, machine proof, full prior literature search, independent code verification or novelty clearance. Earlier quarantine/failure records remain historical and are not retrospectively accepted; the owner frontier direction permits the new source/check prospectively. Same-harness written work requires independent review before adoption.
