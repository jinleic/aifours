# RIGHTSN is not local, but RRL sources pass the witnessing path law; why item4 needs regularity

**Status: NEW AUTHOR WRITTEN lemmas with exact finite checks; UNREVIEWED / UNADOPTED.** This is a structural note on the item4 bridge in `frontier-20261029-Q1-reduction-state-v1.md` (SHA `231a862f484d1d304d7094319e98f715fa5f5442522d227a7a87ac0df9a66157`). It neither proves nor refutes item4 or Q1. Locality facts of this kind may well be known; no novelty is claimed.

**Terms.**
- RIGHTSN means locally right regular: every local monoid eBe satisfies xyx=yx.
- The *derived semigroupoid* 𝒟 of a source q:S→D=M[G;I,Λ;P] has objects `(m,λ)∈G×Λ` and arrows `(σ,s):σ→σ·s`, where `(m,λ)·s=(m p_(λ,i_s) g_s, λ_s)`.
- A twisted host `β(st)=β(s)·^(w(s,t))β(t)` is the same thing as a G-equivariant functor from 𝒟 to a one-object band.

## 1. Two characterizations of RIGHTSN

**Lemma A.** For a band B the following are equivalent:
1. B is RIGHTSN.
2. B satisfies `xyxzxy = xzxy`.
3. Every principal right ideal xB is a right regular band.

*Proof.*
- (1⇒2): put p=xyx and r=xzx in the local monoid xBx. Then prp=rp gives `xyxzxyx = xzxyx`. Right-multiply by y and use `xyxy=xy` on the suffixes: `xyxz(xyxy) = xyxzxy` and `xz(xyxy) = xzxy`.
- (2⇒3): for a=xu and b=xv in xB, `aba = xuxvxu = xvxu = ba` by (2), with y=u and z=v.
- (3⇒1): xBx⊆xB. □

## 2. RIGHTSN is not local in the semigroupoid sense

Let Γ be the graph with objects c and c′ and arrows `e:c→c′`, `x,y:c′→c`. The words exeyex and eyex are coterminal paths c→c. They are equal in every RIGHTSN band by Lemma A(2). Hence every semigroupoid that divides a RIGHTSN band satisfies this path equation: apply it to images in the band and use injectivity of the division on hom-sets.

**Proposition B.** Let B be any band that is not RIGHTSN. By Lemma A, B has elements ε,ξ,η with εξεηεξ ≠ εηεξ. Let M be the image semigroupoid of Γ under e↦ε, x↦ξ, y↦η; its arrows are the band values of paths. Then:
- the local semigroups `M(c,c)=⟨εξ,εη⟩` and `M(c′,c′)=⟨ξε,ηε⟩` are 2-generated bands, hence RIGHTSN (the free band on two letters is RIGHTSN);
- M violates the path equation, so M does not divide any RIGHTSN band.

Thus ℓRIGHTSN ≠ gRIGHTSN: local RIGHTSN-ness does not imply global representability. □

The checker finds the explicit witness ε=1 (adjoined identity), ξ=(r0,c0), η=(r1,c0) in the rectangular band RB₂ₓ₂ with identity adjoined. Both local semigroups are the left-zero pair {ξ,η}, and exeyex=ξ while eyex=η.

**Consequence for item4.** The derived semigroupoid of an RRL source has RIGHTSN local semigroups. Its loop semigroup at (m,λ) is the band of idempotents in actor column λ, and its local monoids are the local bands E(eSe). By Proposition B, item4 cannot follow from this local property alone. Any proof must use more of the source, for instance regularity.

## 3. Regularity does supply the witnessing law

**Proposition C.** Let S be regular with q pure onto CS D. Consider the condition

(C) for all e,x,y∈S such that a=ex and b=ey are idempotents with q(a)=q(b), we have aba=ba.

Then S is RRL if and only if S satisfies (C).

*Proof.*
- (C⇒RRL): for a,b∈E(gSg) take e=g, x=a, y=b. These idempotents share the fibre of g.
- (RRL⇒C): choose e′∈V(e) and put f=ee′, so fa=a and fb=b.
  - q(a) and q(f) are idempotents in the D-row of e, so `q(a)q(f)=q(f)`. By purity af is idempotent, and af∈fSf. Likewise bf∈E(fSf).
  - The local band E(fSf) is right regular, so (af)(bf)(af)=(bf)(af). With fb=b and fa=a this reads abaf = baf.
  - Right-multiply by a and use fa=a and a²=a: aba = ba. □

So in RRL sources, every arrow e of the derived semigroupoid has an idempotent loop f=ee′ at its source. The local right-regular law at f validates the path equation of Proposition B. This is exactly the non-local law that generic semigroupoids miss. The two ingredients actually used are the inverse arrow e′ and the RRB local band. A general proof of item4 is expected to need such regularity arguments throughout; this note supplies only this first one.

## 4. Exact checks

`frontier-20261029-rightSN-nonlocal-regularity-checker-v1.py` ran with python3.14 at Thu Oct 29 08:56:03–08:56:13 PDT 2026, exit 0. SHA: see the pin record. It verifies:
1. that RB₂ₓ₂¹ is a non-RIGHTSN band, with the witness above and RIGHTSN local semigroups;
2. the identity xyxzxy=xzxy on all 28 652 616 triples of the pinned 306-element S45 canonical band, and on a rebuilt 14-element group-top host band;
3. that S45, over its natural 3×3 actor, is RRL and satisfies (C);
4. over 6000 draws of 2–3-generated subsemigroups of `P(B5¹,D8)`: all 1325 distinct regular pure RRL sources satisfy (C), and all 178 regular pure non-RRL sources violate it.

These are same-author finite controls; the general statements are the written proofs above.
