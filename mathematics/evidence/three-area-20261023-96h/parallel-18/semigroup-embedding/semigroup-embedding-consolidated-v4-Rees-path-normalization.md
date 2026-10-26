# Full-Rees all-(M) normal forms and the exact remaining square-excursion reflection

MathSemigroup-2, slot math-4. Actual `/bin/date` observed BEFORE this write: **Sun Oct 25 11:24:48 PDT 2026**. **AUTHOR-WRITTEN / PARTIAL / NOVELTY_UNCLEAR.** ONE consolidated primary successor under the actual102319 contract. This is NOT an embedding proof or a nonembedding obstruction. It gives a global convergent presentation for ALL mixed(M), extends the old group-graded path/isolated-excursion results to the actual nonorthodox Rees setting, and proves target-class preservation. Full band-reflection SEP remains open, including contextual boundary-crossing and multiple-gap excursions. No scientific interpreter/eval/program, symbolic computation, enumeration, solver, replay, table, compile, CLI or nested agent occurred.

## 1. Frozen scope, prior work and what is genuinely new here

Current contract `institute/runs/three-area-2026-10-23-96h/primary-continuation-20261025-102319-v1.json`, live SHA256 `b4dce3ac050ee6688295eff9cbf3e2f3f6326f93e8f973db8374e752770e594b`, retains the FULL original regular-semigroup problem. Assume an ACTUAL supplied idempotent-pure surjection

`q:S -> C=M[G;I,Lambda;P]`, `q(s)=(i_s,g_s,lambda_s)`.

S is regular and locally r-orthodox: every local monoid eSe is orthodox and E(eSe) is a regular band, satisfying xyxzx=xyzx. There is NO global orthodoxy assumption and no finiteness assumption. Pure-quotient existence for arbitrary infinite nonorthodox book-class inputs is still a separate unresolved prerequisite; it is not deduced from weak E-unitarity here.

Earlier explicit ancestry, retained without modification:

- v2,339LF, `6ac3ddf42a1a505529675d263f695de119f9a2507b35192b341ec255098c8ff8`: one-sided bands, all-choice comparisons and inner realization; the typed-v2 review boundary is SAME-DOMAIN SERIAL, not a cross-domain/family upgrade.
- v3,229LF, `966dfc63f1af06470afbafccfff61c07a8235c43f9fd6b1706c09869400b4dc7`: constant-fibre saturation is false on the explicit least-quotient twelve-element positive embedding control. Neither that control nor E5 is a nonembedding witness. No constant-fibre closure or common-unit completion is revived here.
- `path-separation-attack-v1.md`,132LF, `60d967621f44e20f36f25c4ce402446ff4d4bd6f5f7dbf4c6a0fe68a4451ff4d`, and `isolated-excursion-lemma-v1.md`,90LF, `325067cc92a383147e0c4294951225b1dd1fc81c7f6ec301155e725015771452`, already prove the path barrier and isolated one-gap result in the ORTHODOX PURE GROUP-GRADED diagnostic case. They are not claimed as new results. Their endings explicitly leave the full-Rees extension unproved. Both were now reread completely before this successor.
- Parent `semigroup-coherent-birth-parent-v1.md`,51LF, `54b9e20e58710749ff9fca9c47b761d543a49d0f56b3546727d32a6d8c415dfe`, and `semigroup-contextual-loads-parent-v1.md`,33LF, `19cbd84cd5aa0dd901779e83189aef67c8b5e0fab2896ef0652362cbdf8640d1`, were fully reread. Birth anchors do NOT solve later contextual loads; the actual forced-reuse falsifier starts/ends at the SAME path and cannot be promoted to nonembedding.

NEW exact scope: the ordinary-semigroup all-(M) rewriting theorem and regular-part classification; an exact global pre-band congruence conservative on ALL Rees-typed paths; full Rees bridge types for the context-isolated one-gap theorem; and the direct physical local-r-orthodoxy/weak-E-unitarity check for the fixed Pastijn target. These are written claims requiring actual reconstruction, not stronger acceptance. The old path mechanism itself is classical/previously recorded, not a novelty claim.

Mandatory v9/v10/v11 and all prior corrections remain binding. They have been completely read, most recently in order in the full v82 packet before my returned temporary review. V10/v11 are not retroactively inserted into older contracts. No frozen source was edited.

## 2. The actual Rees-typed alphabet and its two distinct ports

Let A contain X_(u,s) for every u in G,s in S. Work first in the ordinary FREE SEMIGROUP F=A^+, not in a band. Assign two ports:

`left(X_(u,s))=(u,i_s)`, `right(X_(u,s))=(u g_s,lambda_s)`.

A right port (r,lambda) can precede a left port (v,j) precisely if

`v=r p_(lambda,j)`.                                           (COMP)

A word is a PATH when all consecutive pairs satisfy this rule. This is the actual Rees condition, NOT equality of two unsorted group objects. A path's source value is the ordered product of its s-labels. Its left and right ports are those of its first and last letters.

All mixed relations are retained:

`X_(u,s) X_(v,t) -> X_(u,st)` iff `v=u g_s p_(lambda_s,i_t)`.     (Mdown)

The group factor p_(lambda_s,i_t) is never dropped or cancelled from a band equation. Since

`g_(st)=g_s p_(lambda_s,i_t)g_t`, `i_(st)=i_s`, `lambda_(st)=lambda_t`,

the merged letter has the original left port and the original final right port `(v g_t,lambda_t)`. Thus contraction preserves both neighboring boundary statuses, compatible OR incompatible. Its inverse expansion inserts only a compatible boundary and preserves the exterior ports. In particular(M) preserves path/nonpath status in ANY context in BOTH directions.

## 3. Global confluence of ALL(M), not only typed paths

**Theorem1.** The system(Mdown) terminates and is confluent on ALL words of F. Its normal form contracts each maximal compatible run to its actual indexed source product. Adjacent resulting letters are incompatible. Thus equality modulo ALL(M) has no hidden source collapse.

**Proof.** Each contraction decreases length by1. Disjoint contractions commute. The only overlap is a compatible triple X_(u,s) X_(v,t) X_(w,r), where

`v=u g_s p_(lambda_s,i_t)`,

`w=v g_t p_(lambda_t,i_r)`.

Contracting left first leaves the second compatibility because `w=u g_(st)p_(lambda_t,i_r)`; contracting right first leaves the first because i_(tr)=i_t. The final letters are X_(u,(st)r) and X_(u,s(tr)), equal by source associativity. A fixed compatible pair has only one output. Termination plus these local diamonds proves confluence by the usual well-founded diamond induction. No enumerated cases or program are involved.

Because ports adjacent to a contraction do not change, a gap between two maximal compatible runs can neither disappear nor become compatible under any(Mdown) sequence. Conversely each run contracts to a single letter, independently of bracketing. This is the asserted explicit normal form. QED.

Call this ordinary semigroup T_M=F/theta_M. If normal forms W,V have lengths m,n, their product has normal-form length m+n or m+n-1: at most the single newly concatenated boundary merges, since each old internal gap remains a gap.

**Corollary1.1.** The regular part of T_M is EXACTLY its one-letter normal forms, and its idempotents are exactly X_(u,e), e in E(S).

For a letter A=X_(u,s), choose s' in V_S(s) and set B=X_(u g_s p_(lambda_s,i_(s')),s'). The first boundary is compatible by definition. The second is compatible because q(ss') is idempotent:

`g_s p_(lambda_s,i_(s')) g_(s') p_(lambda_(s'),i_s)=1`.

Hence ABA=A and BAB=B by actual(M) and the source inverse identities. Every letter is regular. If W has normal-form length m>=2 and V any possible inverse candidate of length n>=1, then

`length NF(W V W)>=2m+n-2>=2m-1>m`.

So W cannot be regular. A one-letter square equals itself exactly when its source label is idempotent; then its self-boundary is compatible automatically. This proves the corollary. This regular-part classification is asserted ONLY for T_M, not for the later local-law quotient.

The source value of an arbitrary word also gives a homomorphism T_M->S, since(M) is actual source multiplication. It need NOT descend through the next local-law quotient on nonpath words; no such false global evaluation is assumed.

## 4. The full local-corner law is conservative on Rees paths

Use the primitive law on arbitrary nonempty word substitutions E,A,B,C:

`E A E B E A E C E A E = E A E B E C E A E`.                    (LOC)

Together with U^2=U it is exactly the variety V of locally regular bands. Indeed in a band it says that the three corner elements eae,ebe,ece satisfy xyxzx=xyzx; conversely every element of eBe is exe, so the law enforces the regular identity in every corner.

Both sides have the SAME set of formal boundary pairs

`EA, AE, EB, BE, EC, CE`.

Every variable internal word occurs on both sides, and both outer endpoints are those of E. Therefore an elementary(LOC) rewrite in ANY context preserves path/nonpath status in BOTH directions, not merely in a preselected proof branch.

**Theorem2.** If either side is path-typed, both have the same actual S-value, without assuming global orthodoxy.

Write e,a,b,c for the source products of E,A,B,C. Let E start at (u,i_e), and let A start with first group index v. The two actual compatibilities in E A E give

`v=u g_e p_(lambda_e,i_a)`,

`u=v g_a p_(lambda_a,i_e)`.

Thus `g_e p_(lambda_e,i_a) g_a p_(lambda_a,i_e)=1`, exactly the idempotency condition for q(ea). Purity gives ea in E(S). The same argument gives eb,ec in E(S). This is the new full-Rees replacement for the old inverse-group-grade calculation; their row and column indices are NOT assumed equal.

Choose e' in V_S(e), put d=ee'. Then d fixes ea,eb,ec on the left. The needed principal-band fact is reproduced here rather than assumed globally:

`B_d={x in E(S):dx=x}` is a REGULAR BAND. If x,y belong to it, xd,yd belong to E(dSd), whose product xyd is idempotent. Right-multiplying `(xyd)^2=xyd` by y and using dx=x,dy=y gives `(xy)^2=xy`; closure follows. The map x->xd is a homomorphism B_d->E(dSd). The latter satisfies xyxzx=xyzx. Equality of the two image words means w_left d=w_right d; right multiplication by their common last letter x removes d, since dx=x and both words end in x. Hence the regular identity holds in B_d itself.

Apply that identity to x=ea,y=eb,z=ec, then multiply on the right by e. It gives exactly

`e a e b e a e c e a e = e a e b e c e a e`.

This is the source-value equality of(LOC). No identity element was adjoined, no source idempotents were identified and no natural-order compatibility with multiplication was used. QED.

## 5. An exact GLOBAL pre-band congruence theorem

Let theta_0 be the congruence on F generated by ALL(M) and ALL instances of(LOC), but NOT by U^2=U. Put Q_0=F/theta_0.

**Theorem3.** The set of paths is a UNION of theta_0 classes, and its classes are EXACTLY the indexed source letters: a path beginning with group index u and having source value s is theta_0-equivalent to X_(u,s), and no two different such letters are theta_0-equivalent. Nonpath classes form a two-sided ideal.

**Proof.** Every elementary(M) or(LOC) step, in arbitrary contexts, preserves path/nonpath status. Thus a derivation from a path can never leave the path set, even though theta_0 is defined on the WHOLE free semigroup. On paths every such step preserves source value by Theorems1–2 and preserves outer ports. A path contracts by(M) to X_(u,s). Therefore different indexed source letters cannot be equated by theta_0: source value and the first group index remain fixed throughout. This proves both directions of the class description, not just a faithful typed image diagram.

Concatenation cannot remove an existing incompatible adjacency inside a nonpath word. Since class membership cannot change pathness, the nonpath classes are a two-sided ideal of Q_0. QED.

This theorem genuinely concerns ALL mixed(M) and an arbitrary global congruence derivation; it is not an assertion that the image of a noninjective beta diagram is faithful. Its limitation is precise: Q_0 is not yet a band.

## 6. The ORIGINAL canonical band is exactly the remaining band reflection

Let theta_B be generated by U^2=U for all nonempty words. Then the original canonical base, with the actual local-band variety and EVERY mixed relation, is

`B_q = F/(theta_M join theta_LOC join theta_B)`

`    = Q_0/(least congruence making every element idempotent)`.

This is equality of the original presentations: taking the joins in a different order changes no relation. The(LOC) law survives the final homomorphic image, so the final band is locally regular. No stronger semantics, Horn closure, completion with a common unit, or weakened subset of(M) has entered.

For a PATH U with source product s, UU is a path iff

`g_s p_(lambda_s,i_s)=1`,

i.e. q(s) is idempotent. Purity then gives s^2=s, so that square rewrite is source-valid. If q(s) is not idempotent, U->UU introduces exactly one incompatible adjacency and is the ONLY primitive way a derivation beginning on a path can first leave the path set. Conversely a square contraction inside a path is harmless; both sides are paths and its source factor is idempotent.

**Exact remaining obstruction to proof:** band reflection can travel through those nonpath words and return to a source path. Theorems1–3 do NOT eliminate such square excursions. A canonical collapse of two distinct same-q idempotents would necessarily use one, but necessity is not impossibility.

For clarity there is a genuine V-valued OUTER-PORT invariant. The rectangular band of pairs of a left port and a right port receives

`X_(u,s) -> ((u,i_s),(u g_s,lambda_s))`.

Multiplication keeps the first left and last right port, so all(M), (LOC) and square relations hold. This map descends to B_q and protects outer ports even along the final band reflection. It does NOT separate two source idempotents with the same q-type: their port pairs coincide. It cannot replace SEP.

## 7. The context-ISOLATED one-gap theorem now holds for full Rees types

This section extends the earlier90LF group-graded result; it does not silently extend it to contextual boundary-crossing.

For a unique gap whose left right-port is (r,lambda) and whose right left-port is (v,i), an eligible source bridge t has, for any j in I,mu in Lambda,

`q(t)=(j, p_(lambda,j)^(-1) r^(-1)v p_(mu,i)^(-1), mu)`.        (BR)

Its actual indexed letter starts at `r p_(lambda,j)`. Substitution into(COMP) verifies BOTH boundary compatibilities exactly. Surjectivity of q supplies bridges of each specified type. No endpoint-only simultaneous inverse is assumed.

For a one-gap word L|R define, for EVERY eligible t simultaneously,

`F_t(L|R)=value(L) t value(R)`.

An(M) move cannot straddle the incompatible pair and preserves its actual two ports and this whole family. For an(LOC) move with exactly one gap on both sides, the gap cannot lie inside E or A, or at EA/AE: each such location repeats at least twice on BOTH sides. It can only lie outside the rewritten substring, inside the single-occurrence B or C, or at the single-occurrence EB/BE/EC/CE boundary. In each case insert the bridge inside that one role, or absorb it at that role's end. The resulting full(LOC) instance is a PATH on both sides, so Theorem2 preserves F_t for every eligible t. Gap ports remain the same. Interior loop-square moves that retain exactly one gap are likewise harmless: they lie in a typed component and have idempotent source value. A square on an untyped subword would duplicate a gap; a nonloop typed square would create/remove the only gap and leave the one-gap interior, so neither is an unaccounted interior case.

Now consider the WHOLE CORE derivation

`U -> UU ~~ ... ~~ VV -> V`,

where U,V are paths, each interior word has exactly one gap and each interior step uses the displayed primitive relations while retaining that count. The outer-port invariant gives the same q-type c=(i,g,lambda) for the products s=value(U),v0=value(V). For UU's gap, (BR) becomes

`q(t)=(j,p_(lambda,j)^(-1)g^(-1)p_(mu,i)^(-1),mu)`.

These are exactly ALL mutual inverses of c in the Rees matrix semigroup. Hence both actual source inverses s' in V_S(s) and v0' in V_S(v0) are eligible bridge values. Invariance gives

`s t s = v0 t v0` for every eligible t.

Set t=s'. Then s=v0 s' v0, and q(v0 s'),q(s'v0) are idempotent because q(v0)=q(s). Purity makes these actual idempotents, so

`s=(v0 s')v0=v0(s'v0)`

witnesses s<=v0 in the actual natural order. Setting t=v0' gives v0<=s. Antisymmetry gives s=v0. Fixed left/right contexts can be multiplied AFTER this equality, provided the whole interior derivation stays inside this fixed core.

This proves the full-Rees isolated-excursion theorem with no global orthodoxy. It does NOT permit an interior rewrite to cross that fixed core boundary or change its contexts. For a general loaded excursion the invariant instead has the shape `ell s t s r`, and equality of cores has not been obtained. Natural order is NOT assumed compatible with multiplying arbitrary contexts. The previously accepted contextual-load falsifier and unresolved later-load equations therefore remain fully relevant. Multiple simultaneous gaps are also not normalized by this theorem.

## 8. Why simply killing the nonpath ideal is not a repair

The nonpath ideal of Q_0 is real, but quotienting it to zero before making a band can destroy the very source fibres. This is a METHOD warning, not nonembedding.

Take S=E cross C2 with E a two-element semilattice and trivial action, q projection to C2={1,g}. This is explicitly an allowed semilattice-by-group product and embeds; as a monoid its least completely simple quotient is this group quotient (every completely simple monoid image is a group, and all E idempotents must map to its identity). For each e in E the indexed letter A_(u,e)=X_(u,(e,g)) is non-self-compatible, so its square lies in the nonpath ideal. In the zero quotient followed by any band homomorphism, its image must equal the image of zero by idempotency. Its actual inverse-index letter composes with it to X_(u,(e,1)); hence that source idempotent also maps to zero. BOTH distinct idempotents of the same q-fibre are lost. The source nevertheless has its explicit positive embedding. Thus off-path states cannot simply all be collapsed to an absorbing state. This does not establish a collapse in B_q, which retains them separately as required by the original presentation.

## 9. Explicit canonical map and DIRECT preservation of the physical target class

The action on B_q is `alpha_v(X_(u,s))=X_(vu,s)`. It is an automorphism: left multiplication of every first index by v preserves the exact mixed compatibility, and the two band identities are substitution-invariant; alpha_(v^-1) is its inverse. In the fixed Pastijn product

`(b,(i,g,lambda))(d,(j,h,mu))`

` = (b alpha_(g p_(lambda,j))(d), (i,g p_(lambda,j)h,mu))`,

put `beta(s)=[X_(1,s)]` and

`kappa(s)=(beta(s),q(s))`.

Every(M) gives kappa(st)=kappa(s)kappa(t). This is an actual explicit multiplicative map, not a scaffold or assumed section. Injectivity is the remaining issue below.

The projection from this physical product to C is IDEMPOTENT PURE: if c=(i,p_(lambda,i)^(-1),lambda) is idempotent, its self-multiplication action shift is1, so `(b,c)^2=(b^2,c)=(b,c)` for every b in B_q. Conversely any idempotent pair has idempotent second component.

Let h=(b,c) be an idempotent. Every idempotent x of hPh has second component c, since cCc is a group with unique idempotent c. Write x=(d,c). The corner equations hx=x=xh, whose action shifts are1, say exactly bd=d=db. Conversely every such d=bdb gives h(d,c)h=(d,c). Therefore

`E(hPh) = { (d,c): d in b B_q b }`,

with ordinary band multiplication in the first coordinate. It is a regular band by the ACTUAL V hypothesis, not a global regular-band assumption.

For any regular subsemigroup T of this product, hTh is regular: if x in hTh and z is a mutual inverse in T, hzh is a mutual inverse in hTh. Its idempotents form a SUBBAND of the displayed regular band, since the product stays in T and in the same c-fibre. Thus hTh is orthodox with regular idempotent band: T is locally r-orthodox.

The book's exact weak-E-unitarity also follows directly. If idempotents e,f,g in T satisfy e=f a=a g, write q(a)=(i,k,lambda). From the equality of the two Rees products, the row of q(f) must be i and the column of q(g) must be lambda. Idempotency of q(f) then implies q(f)q(a)=q(a) (its row agrees), so q(e)=q(a) is idempotent. Projection purity makes a idempotent. This is precisely the condition `e=f a=a g => a in E(T)`; no missing infinite-source pure-quotient theorem is smuggled into it.

Finally kappa(S) is regular because homomorphisms preserve mutual-inverse equations. Therefore even its possibly noninjective image has both requested local-r-orthodoxy and weak-E-unitarity properties. This closes PRESERVATION of the candidate's image class, not faithfulness of the original source. No unproved equivalence with the separate restricted R carrier/action is used.

## 10. SEP remains exactly the original faithfulness obligation

For the actual supplied pure q, retain the original condition

`e,f in E(S), q(e)=q(f), beta(e)=beta(f) => e=f`.              (SEP)

If it holds, kappa is injective on all of S. Indeed assume kappa(s)=kappa(t), choose s' in V_S(s), and compare

`kappa(s's)=kappa(s't)`, `kappa(ss')=kappa(ts')`.

Their second components are equal idempotents; purity makes s't and ts' actual idempotents. SEP gives s's=s't and ss'=ts'. Then

`s=ss's=ts's=ts't=(ts')t=t(s't)`.

The two factors ts',s't are idempotents, so s<=t. The symmetric argument with an inverse t' gives t<=s, hence s=t by antisymmetry of the regular-semigroup natural order. Conversely injectivity of kappa implies SEP immediately. This supplies the complete implication from the remaining reflection claim to the original explicit P embedding, without pretending the claim has been proved.

Theorems1–3 and the isolated-Rees excursion theorem do not settle SEP. The first unproved step is to eliminate/transform EVERY loaded off-path square excursion in the actual final reflection while retaining the source endpoint value, including rewrites crossing core boundaries and arbitrary multiple-gap interactions; alternatively exhibit an actual collapse for the CANONICAL least-quotient presentation of an admissible source and prove it forbids every allowed embedding. No such collapse or normalization is provided here. A failed bridge assignment, constant-fibre model, common-unit completion or zero quotient is not that obstruction.

## 11. Evidence ceiling and continuation

Named correctness imports: Rees multiplication and inverse-coordinate equations; elementary terminating local-diamond confluence (or its well-founded induction proof given above); regular-semigroup mutual inverses, Green/local-corner facts and antisymmetry of the displayed natural order; free objects/quotients in a band variety. The principal-band, full-Rees path, bridge and target preservation formulas needed for this manuscript are explicitly proved here. No external classification/locality theorem, unverified finite table or executable witness is imported. Prior packets/parents are historical boundaries, not permission to discard arbitrary contexts, all(M), local versus global regularity or the separate pure-quotient gap.

The substantive checkpoints are `primary-102319-M-normalform-checkpoint-v1.json` and `primary-102319-typed-local-law-checkpoint-v1.json`. The temporary v78-A and v82-A reviews were actually returned before resuming this manuscript; their source-supported mathematical verdicts do not accept this new primary body. No blind/configured-family/human/formal/kernel/executable/triple-certificate/novelty/SOTA/publication gate has been performed for it. N3 remains the earlier WRITTEN preparation/necessary-condition work, with no table/checker execution admitted or performed.

**Original embedding/nonembedding acceptance remains UNMET.** This successor is a parkable full-Rees normalization reduction, not a phase ending or a narrowed replacement target. Next actionable primary work is the genuine loaded/multiple-gap square-reflection obligation above. Original October27 science cutoff11:05:38PDT/deadline12:35:38PDT and written-only HOLD are unchanged.
