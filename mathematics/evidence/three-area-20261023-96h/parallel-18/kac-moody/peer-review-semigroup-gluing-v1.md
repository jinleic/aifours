# Independent in-harness reconstruction of the semigroup gluing packet

Reviewer: **MathKacMoody**, actual job/slot math-3. Observed immediately before creation: **2026-10-23T14:18:49-07:00**. This is the ONE review assigned by peer-review-wave-eighteen-v1.json, not another scientific problem slot.

## Snapshot and exact verdict

Reviewed complete source: mathematics/evidence/three-area-20261023-96h/parallel-18/semigroup-embedding/proof-v1.md, lines1–262. Actual observed SHA-256:

    c79017231ebe5162ef3804f8dacc039da4232e613e911fd39ea058ef30737f5b

This matches the assignment. The source was NOT edited. Also read the complete selection-v1.md; the actual dossier's product definitions/book hypotheses in proof.md §§0–1; the literal book excerpt; and the imported xi-purity.md proof. The latter's actual observed SHA-256 is

    c7696fff180e29e7bfbc1fe9ed2e0070b2afe6a675a86171df45facd12f5e318,

matching Theorem X's declared source. I read X as the explicit written import rather than claiming a new independent formal acceptance or authenticating the old parent-audit process.

**Verdict: no FATAL or MAJOR mathematical defect found in claims A–D at their stated hypotheses and P/R readings. One MINOR wording issue below.** The paper supplies a valid written compactness/gluing barrier conditional on the named classical and historical imports. It does NOT prove the broad embedding question, finite embedding from purity, the faithful-functor condition, or the remaining algebraic N1–N3 step.

## Findings

### MINOR — “not regular” should specify the band identity

**Source lines220–222.** The text concludes that E is locally regular and then says “It is not regular because” before the failing regular-band identity. E is a band and hence is a regular SEMIGROUP. The intended conclusion is “not a regular band.” The displayed unequal products correctly establish that intended conclusion. This wording does not invalidate the construction or A–D, but the distinction matters in a paper whose source class consists of regular semigroups. A numbered clarification can repair it without changing frozen bytes.

No other substantive finding is asserted. In particular, I do not invent a failure because a compactness proof has not been executed; it is a written argument.

## Reconstruction by import boundary

### 1. Regular subsemigroups and the least completely-simple congruence

**Lines33–67 checked.** For e an idempotent of the regular subsemigroup T and x∈eTe, a chosen mutual inverse z∈T gives eze∈eTe, with x(eze)x=x and(eze)x(eze)=eze. In the ambient H-class group, x(eze)x=x forces eze=x^{-1}. Thus eTe really is a subgroup with identity e; no finiteness argument is used.

For e,f∈E(T), v=(efe)^{-1}∈eTe gives vfe=e and d=vf an idempotent in the ambient row of e and column of f. The square calculation d²=vfevf=evf=d is correct. For t∈T with a mutual inverse t', taking e=tt', f=t't makes d lie in the ambient H-class of t, so d is that group's identity and dt=t=td. Therefore t∈dTd and its H-class inverse lies in T.

For arbitrary u,v∈T, the crossed idempotents a,b make w=avb share u's ambient H-class. Then u=(u w^# a)v b∈TvT. This establishes simplicity, not just a union of groups. Ambient primitivity gives primitivity inside T. The image corollary follows because a homomorphic image of a regular semigroup is regular.

The set of congruences used in Lemma2.3 is a set (a subset of P(S×S)), not a proper class. The direct product of their Rees quotients is explicitly a completely-simple Rees semigroup, using choice for nonempty index products. The diagonal image is regular, hence completely simple by the proved image lemma. Thus the intersection is itself a completely-simple congruence, establishing the least one without assuming finite S.

### 2. Actual Pastijn P ultraproduct

**Lines69–105 checked against the dossier's formula.** The group element acting in the first coordinate is g p_(lambda,j), NOT g. The author's equation(3.2) identifies the ultraproduct of the four sorts B,I,G,Lambda with the actual Rees product built from their ultraproducts. Coordinate representative changes are controlled by a finite intersection of ultrafilter-large sets. The multiplication computation retains precisely the sandwich entry in both the group and band coordinates.

The action inverse is alpha_[g^{-1}], so this is an automorphism action, not only endomorphisms. Associativity/idempotence and the locally-regular band identity hold coordinatewise and are therefore preserved. No compactness shortcut silently changes the target product.

### 3. Actual restricted R carrier

**Lines107–135 checked.** In Rees coordinates x^#=(i,p_(lambda,i)^{-1} g^{-1} p_(lambda,i)^{-1},lambda) is the group inverse in H_x, and xx^#=epsilon_x. If e,f are idempotents in one row, ef=f and fe=e; hence their action endomorphisms satisfy phi_e phi_f=phi_f and phi_f phi_e=phi_e and have the SAME fixed set. For example, if phi_e(b)=b, then phi_f(b)=phi_f phi_e(b)=phi_e(b)=b. This verifies the change from any mutual inverse to the displayed H-class inverse without an extra assumption.

A quotient class satisfying the restricted-carrier equation has representatives satisfying it on a large set. Repairing other coordinates by an image point of the idempotent endomorphism produces valid pairs everywhere and changes no ultraproduct class. Thus the proof establishes surjectivity onto the restricted carrier, not merely an inclusion. The multiplication is the completely-simple specialization already fixed in the dossier, and the coordinate action identity makes the bijection multiplicative.

### 4. Finite-subset gluing and chosen-inverse localization

**Lines137–175 checked.** T_F contains the indexed finite set F but need not be finite. The ultrafilter tails have the finite-intersection property. On the tail containing s,t, the local subsemigroup contains s,t,st and the local map preserves their product. On that same tail the map separates distinct s,t. Dummy values away from the tail therefore affect neither the homomorphism law nor injectivity. No compatibility among local embeddings is needed.

For the localization, closure of a finite nonempty set under multiplication and a fixed global mutual-inverse choice gives a countable subsemigroup closed under that inverse operation, hence regular. The weak E-unitary witness equations use only elements already in that subsemigroup, so they inherit directly; no equality of intrinsic and ambient natural orders is assumed. The eTe inverse localization eze is valid, and the orthodox/regular-band identities pass to local idempotents. Contraposition of A gives a genuine countable finitely inverse-generated counterexample if any counterexample exists. It does NOT make that source finite or merely finitely generated as an underlying semigroup.

### 5. Covered infinite purity and necessary purity

**Lines177–205 checked, with X retained as import.** Each regular T_F inherits the hypotheses of X. Replacing local embeddings by pure maps q_F gives a global homomorphism. If s is not idempotent, every local T_F containing s also contains s² and its pure q_F sends s to a nonidempotent. Therefore the ultraproduct image of s is not idempotent. Restricting to the image gives a surjective map to a completely-simple semigroup by the image lemma.

The least completely-simple congruence xi lies inside ker q. Purity can be checked directly even in the quotient formulation: if s² xi s, then q(s)²=q(s), so purity of q forces s²=s. Thus no hidden idempotent-lifting assumption is needed for the least-quotient conclusion.

For D, in P an idempotent Rees coordinate has g p_(lambda,i)=1, so squaring its pair leaves b²=b. In R its carrier condition phi_x(b)=b supplies the same conclusion. Projection is therefore pure, and the image of regular S is completely simple. Nothing in this necessary direction constructs an embedding from a pure quotient.

### 6. Infinite nonvacuity example

**Lines207–243 checked algebraically, not by enumeration.** The theta maps on K fix3,4, with theta_u theta_v=theta_v, agreeing with the upper right-zero multiplication uv=v. The claimed mixed associativity follows. Each local uEu has identity u and a two-element left-zero ideal, and each kEk is a singleton. The displayed products4 versus3 really violate the GLOBAL regular-band identity.

For S=(E×(Z,min))×C, regularity, weak E-unitarity, local r-orthodoxy, failure of global orthodoxy and failure of local inverseness follow from the stated product coordinates. Any nonempty ideal J contains an element at some integer n and another at every lower m. The subset J_(<=m) is a nonempty proper two-sided ideal of J, since products take the minimum integer level and J still contains its original level-n element. Hence J is not simple. The finite truncations are regular and form an increasing cover; K×{-N}×C is their completely-simple ideal. This really witnesses the covered infinite case without a completely-simple ideal in S itself. The manuscript correctly disclaims a new embedding theorem for this already explicitly embedded example.

## Scope, trust and calibration

- **Checked:** a separate in-harness written reconstruction of the full pinned manuscript and its stated bridges, with one minor wording clarification.
- **Imported:** classical choice/ultrafilter/Rees theory, finite minimal-ideal fact, and the exact historical Theorem X at observed matching bytes. The original embedding problem's two product readings remain fixed and separate.
- **Not checked/performed:** scientific executable, enumeration, test suite, Lean/kernel replay, external-model CLI, human review, publication priority, or the inaccessible broad modern open-problem source.
- **Full target:** still unresolved, exactly as lines245–262 state. Compactness excludes incompatibility-only limits of already embeddable pieces; it does not create their embeddings. Finite purity does not imply finite embedding.

This review does not grant formal acceptance or novelty. Reviewer now returns to the ONE owned Kac–Moody problem under the same contract.
