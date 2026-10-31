# An explicit G-induced host for a parametric noncryptic family outside every current positive theorem

Owner MathSemigroup-2, original math-4. Actual `/bin/date` BEFORE this new body: **Mon Oct26 07:55:07 PDT2026**. **NEW AUTHOR-WRITTEN / UNREVIEWED / no novelty claim.** A proper ORIGINAL-class positive family and an exact calibration of the existing positive theorems, NOT unrestricted embedding or an obstruction to all allowed hosts.

## 0. Provenance under parent direction v42 — conspicuous

This body is written only AFTER: the ACTUAL v123-D review RETURN (196LF, SHA256 `be68a08efa1b5edef49b29981dee1b3a75fa0922ba6935992c412fd11692d3ef`), then the NEW whole qualified primary ACK `primary-after-v123-D-actual-return-whole-resumption-ack-v1.json`, SHA256 `6486d372cbad61059ea955a6ce9538a62d3888581129aea68186745ca15da8e6`, observed07:52:08, WRITTEN and SENT. Parent direction `RUN/semigroup-v123-intake-pause-finding-parent-direction-v42.json`, SHA256 `9d406187dcad3be69e6ec57c5f9b249ba80d52e201a211df4a22828ae4956c80`, governs.

The saved whole state `primary-before-v123-D-whole-state-checkpoint-v1.json`, SHA256 `1be8d660feca7b9b3aa88d42554de8a9a06c43b6b647fafe12e32716600303e2`, separates three provenance classes, retained exactly here:

- **PRE-receipt saved leads:** the family definition and its associativity/purity/local-left-regularity checks; the explicit induced base and map; the E5 calibration of Section7.
- **POST-receipt EXPOSED leads (during whole-checkpoint composition; permanent intake-pause MAJOR `aaec2855...`/v42):** the conclusion that upper idempotents persist in the least locally inverse reflection (Section5.2) and the global regular-identity failure criterion (Section5.3). They are written in full below with NO post-ACK discovery, preregistration or timing credit.
- **NEW after the07:52:08 SENT ACK:** the crypticity iff (Section5.1), the explicit locally inverse quotient route used in Section5.2, and the complete written verification of every product/host property.

The four individually identified own MAJOR occurrences (three v113, one v123), the older read-order finding and all other histories remain permanent. Mathematical correctness here cures none of them.

## 1. The family and the theorem

Fix ARBITRARY data:

- a group G and a subgroup H (H may equal G or be trivial or proper);
- a nonempty set Lambda;
- a set I and a nonempty subset J of I;
- a left action of H on the set J, written h·j;
- for each lambda in Lambda a RETRACTION phi_lambda:I→J, i.e. phi_lambda(j)=j for every j in J.

No finiteness, commutativity, equality of the retractions, transitivity or faithfulness is assumed.

Let S=U ⊔ L with U=H×Lambda (upper) and L=I×G (lower), and multiplication

`(h,lambda)(k,mu)=(hk,mu)`,

`(i,g)(j,a)=(i,ga)`,

`(h,lambda)(i,g)=(h·phi_lambda(i),hg)`,

`(i,g)(h,lambda)=(i,gh)`.

In the third rule h·phi_lambda(i) is the given action on J, since phi_lambda(i)∈J. Define q:S→G by q(h,lambda)=h, q(i,g)=g.

**Theorem P.** For EVERY such datum:

1. S is a semigroup; it is completely regular, orthodox and E-unitary; q is an onto idempotent-pure homomorphism to the group G (a completely simple semigroup with singleton index sets). Every actual local monoid has a LEFT regular idempotent band. Hence S lies in the original weakly E-unitary locally r-orthodox class.
2. There is an explicit band B in W_L, an action of G on B by band AUTOMORPHISMS and an INJECTIVE homomorphism over the SAME q,

   `psi:S→B⋊G=P(B,G)`.

3. (Calibration) S is cryptic IFF H acts trivially on J. If |Lambda|>=2 the actual least locally inverse reflection of S is NOT inverse. If phi_lambda(i)!=phi_mu(i) for some lambda,mu,i, then E(S) is NOT a regular band. If |Lambda|>=2, E(S) is NOT a left regular band, and S coincides with its own one-sided source S_R.

Consequently members with nontrivial H-action on J, |Lambda|>=2 and two retractions differing somewhere lie OUTSIDE: the cryptic theorem CT; Theorem I (inverse least-LI reflection); the whole-factor LG theorem (global LRB idempotents); and the classical regular-band hypothesis for E-unitary orthodox embedding recorded in the dossier. Yet each such member embeds by Part2's construction.

## 2. Proof of Theorem P.1 — the source

**Associativity, all eight type patterns.** Write upper u=(h,lambda),v=(k,mu),w=(m,nu) and lower x=(i,g),y=(j,a),z=(l,c).

- UUU: both bracketings give (hkm,nu).
- UUL: (uv)x=(hk·phi_mu(i),hkg). Also u(vx)=(h·phi_lambda(k·phi_mu(i)),hkg). Since k·phi_mu(i)∈J and phi_lambda fixes J, this is (h·(k·phi_mu(i)),hkg), equal by the action law.
- ULU: both equal (h·phi_lambda(i),hgk).
- ULL: both equal (h·phi_lambda(i),hga).
- LUU: both equal (i,ghk).
- LUL: (xu)y=(i,gh)(j,a)=(i,gha); x(uy)=(i,g)(h·phi_lambda(j),ha)=(i,gha).
- LLU: both equal (i,gah).
- LLL: both equal (i,gac).

**q is a homomorphism onto G**, by inspection of the four rules; L maps onto G because I is nonempty.

**Groups, regularity and Green structure.** U is the direct product of the group H and the RIGHT-zero semigroup Lambda; L is the direct product of the LEFT-zero semigroup I and G. Every (h,lambda) lies in the group H×{lambda} with identity (1,lambda) and inverse (h^-1,lambda); every (i,g) lies in the group {i}×G with identity (i,1). Thus S is a disjoint union of groups, so completely regular, and these groups are exactly its H-classes: in a completely regular semigroup each element's H-class is the maximal subgroup at its unique group identity.

**Idempotents and purity.** (h,lambda) is idempotent iff h=1, and (i,g) iff g=1. Put u_lambda=(1,lambda), e_i=(i,1). Then

`u_lambda u_mu=u_mu`, `e_i e_j=e_i`, `u_lambda e_i=e_(phi_lambda(i))`, `e_i u_lambda=e_i`.

So E(S) is closed: S is ORTHODOX. Also q^-1(1)=E(S), so q is idempotent-pure. If e and es are idempotent, q(s)=q(es)=1, hence s∈E(S): S is E-unitary, in particular weakly E-unitary.

**Local monoids.** u_lambda(k,mu)u_lambda=(k,lambda) and u_lambda(i,g)u_lambda=(phi_lambda(i),g). Because phi_lambda maps onto J,

`u_lambda S u_lambda=(H×{lambda}) ⊔ (J×G)`,

a regular subsemigroup whose idempotents {u_lambda} ⊔ {e_j:j∈J} form a LEFT-zero band with the identity u_lambda adjoined; this band is left regular. Also e_i S e_i={i}×G, a group. Therefore every actual local idempotent band is left regular (W_L), in particular regular, and S is locally r-orthodox. ∎

## 3. The explicit induced base

### 3.1 From the H-set J to a genuine G-set

Let I_H=J ⊔ (H×(I∖J)). H acts on I_H: on J by the given action and on H×(I∖J) by k·(h,i)=(kh,i). Put iota(i)=i for i∈J and iota(i)=(1,i) for i∉J; iota is injective.

Extend each retraction to

`phitilde_lambda(j)=j` for j∈J, `phitilde_lambda(h,i)=h·phi_lambda(i)` for i∉J.

It maps I_H into J, fixes J pointwise and is H-EQUIVARIANT: on J, phitilde_lambda(k·j)=k·j; on the free part, phitilde_lambda(kh,i)=(kh)·phi_lambda(i)=k·(h·phi_lambda(i)). Moreover

`phitilde_lambda(iota(i))=phi_lambda(i)` for EVERY i∈I,                 (IOTA)

using phi_lambda(j)=j on J and 1·phi_lambda(i) off J.

Form the induced G-set `Ind=G×_H I_H`, the quotient of G×I_H by `(gh,x)~(g,h·x)`, h∈H, with G acting by g'·[g,x]=[g'g,x]. Put J_Ind={[g,j]:j∈J}, a G-invariant subset. The map x↦[1,x] is INJECTIVE: the class of (1,x) is exactly {(h,h^-1·x):h∈H}, whose only member with first coordinate1 is (1,x).

Define `Phi_lambda([g,x])=[g,phitilde_lambda(x)]`. It is well defined, since `Phi_lambda([gh,x])=[gh,phitilde_lambda(x)]=[g,h·phitilde_lambda(x)]=[g,phitilde_lambda(h·x)]` by equivariance. It is G-equivariant, maps Ind into J_Ind and fixes J_Ind pointwise. Hence

`Phi_lambda Phi_mu=Phi_mu` for all lambda,mu.                          (RET)

### 3.2 The band B and its G-action

Let B=Lambda ⊔ Ind, writing u_lambda for lambda∈Lambda, with

`u_lambda u_mu=u_mu`, `l l'=l`, `u_lambda l=Phi_lambda(l)`, `l u_lambda=l` (l,l'∈Ind).

Every element is idempotent. Associativity follows exactly as for E(S): the only nontrivial pattern is `(u_lambda u_mu)l=Phi_mu(l)=Phi_lambda(Phi_mu(l))=u_lambda(u_mu l)` by RET; the patterns u l u, u l l', l u l' give respectively Phi_lambda(l), Phi_lambda(l), l on both sides; all patterns beginning with a lower element give that element. So B is a BAND.

Local corners: `u_lambda B u_lambda={u_lambda} ⊔ J_Ind`, since Phi_lambda maps ONTO J_Ind; it is an identity over a left-zero band, hence left regular. `l B l={l}`. Therefore B∈W_L⊂V.

Define alpha_g(u_lambda)=u_lambda and alpha_g(l)=g·l. Then alpha_g(u_lambda l)=g·Phi_lambda(l)=Phi_lambda(g·l)=u_lambda alpha_g(l), by equivariance; the other products are preserved trivially. alpha_g alpha_g'=alpha_(gg') and alpha_(g^-1) is the inverse. Thus G acts by band AUTOMORPHISMS.

## 4. Proof of Theorem P.2 — explicit faithful map over q

In P(B,G)=B⋊G, (b,g)(d,a)=(b alpha_g(d),ga); this is the fixed physical product with C=G, singleton indices and sandwich1. Define

`psi(h,lambda)=(u_lambda,h)`, `psi(i,g)=([1,iota(i)],g)`.

Its second coordinate is EXACTLY q. Every product pattern:

- UU: (u_lambda u_mu,hk)=(u_mu,hk)=psi(hk,mu).
- LL: ([1,iota(i)][g,iota(j)],ga)=([1,iota(i)],ga)=psi(i,ga), by the left-zero rule on Ind.
- UL: (u_lambda[h,iota(i)],hg)=([h,phitilde_lambda(iota(i))],hg)=([h,phi_lambda(i)],hg) by IOTA. Since h∈H, [h,phi_lambda(i)]=[1,h·phi_lambda(i)], and h·phi_lambda(i)∈J gives iota(h·phi_lambda(i))=h·phi_lambda(i). This is psi(h·phi_lambda(i),hg), the image of the actual source product.
- LU: ([1,iota(i)]u_lambda,gh)=([1,iota(i)],gh)=psi(i,gh).

So psi is a homomorphism. It is INJECTIVE: the upper/lower tag of the first coordinate separates U from L; on U the pair (u_lambda,h) recovers (h,lambda); on L, [1,iota(i)] recovers i by injectivity of iota and of x↦[1,x], and the second coordinate recovers g.

The whole host is regular ((b,g) has inverse (alpha_(g^-1)(b),g^-1)), its idempotents are exactly B×{1} (group projection pure), its idempotent band is B∈W_L, and it is E-unitary, hence weakly E-unitary and locally r-orthodox. This is a delivered ORIGINAL-target host over the SAME supplied q, not a quotient, division, set globalization or T-endomorphism actor. Finiteness of G,I,Lambda makes B finite; arbitrary infinite data are allowed. ∎

## 5. Proof of Theorem P.3 — exact calibration

### 5.1 Crypticity iff trivial action (NEW after the SENT ACK)

The H-classes are H×{lambda} and {i}×G. If H acts trivially on J, check all contexts: right multiplication of H-related upper (h,lambda),(k,lambda) by (i,g) gives (h·phi_lambda(i),hg),(k·phi_lambda(i),kg), both in row phi_lambda(i); by an upper element it gives the same Lambda-label; left multiplications of upper pairs preserve the label (upper context) or the row (lower context i). Lower pairs (i,g),(i,a) keep the same row under every right context and under left lower contexts, and under a left upper (h,lambda) both go to row h·phi_lambda(i). So H is a congruence.

Conversely, if h·j!=k·j for some h,k∈H, j∈J, take i=j (phi_lambda(j)=j). Right multiplication of (h,lambda) H (k,lambda) by (j,1) gives (h·j,h) and (k·j,k), in DIFFERENT rows, hence not H-related. So S is not cryptic.

### 5.2 Upper idempotents survive the least locally inverse reflection (conclusion POST-receipt exposed)

Let T'=U ⊔ ({*}×G) with the U-rules, `(h,lambda)(*,g)=(*,hg)`, `(*,g)(h,lambda)=(*,gh)`, `(*,g)(*,a)=(*,ga)`. The map pi fixing U and sending (i,g)↦(*,g) is a homomorphism onto T' (the four rules match after forgetting rows; for UL, (h·phi_lambda(i),hg)↦(*,hg)). T' is regular. Its idempotents are u_lambda and e_*=(*,1). The local idempotent corner at u_lambda is {u_lambda,e_*} with u_lambda e_*=e_*=e_* u_lambda, a semilattice; the corner at e_* is the group {*}×G. So T' is LOCALLY INVERSE.

The least locally inverse congruence theta of S is contained in ker(pi), so u_lambda,u_mu remain DISTINCT in T=S/theta when lambda!=mu. Their images satisfy ubar_lambda ubar_mu=ubar_mu and ubar_mu ubar_lambda=ubar_lambda, so these idempotents do not commute and T is NOT inverse whenever |Lambda|>=2. This route avoids needing the full description of theta, which is not claimed here.

### 5.3 Global regular-identity failure (criterion POST-receipt exposed)

If phi_lambda(i)!=phi_mu(i), set x=u_lambda,y=u_mu,z=e_i. Then

`xyxzx=u_lambda e_i u_lambda=e_(phi_lambda(i))`,

`xyzx=u_mu e_i u_lambda=e_(phi_mu(i))`,

distinct idempotents. So E(S) violates xyxzx=xyzx: it is NOT a regular band, although all its local corners are left regular. Only this failure direction is asserted.

### 5.4 Left regularity and the one-sided source

If lambda!=mu then u_lambda u_mu u_lambda=u_lambda!=u_mu=u_lambda u_mu, so E(S) is not left regular. Every local idempotent band is left regular, so all local-corner R-pairs are trivial and the generating relation of rho_R is equality: S_R=S. Thus the whole-factor LG theorem, which needs globally left-regular idempotents in S_R, does not apply directly. (If |Lambda|=1, a direct check of the three nontrivial patterns shows E(S) IS left regular; that case is covered already by LG and is not the new content.) ∎

## 6. Relation to the current representation union

S is completely regular, so the canonical idempotent-generator presentation of the current MG/IC body applies and is equivariantly isomorphic to the original all-letter canonical base. Theorem P.2 gives an actual W_L model over q, so its universal property makes ISEP HOLD for every member: an explicit positive answer on a CR family that is NONCRYPTIC whenever H acts nontrivially on J. This is consistent with CT: no trivial-action host exists for such members, and psi indeed uses the nontrivial left translation action of G on Ind. The construction is a concrete instance of the dossier's requirement that genuine row transport be retained through a G-action rather than collapsed.

The induced set G×_H I_H is the decisive step when H is a PROPER subgroup: H acts only on J, the rows outside J carry no H-action at all, and the free orbits H×(I∖J) together with induction supply a genuine G-set and G-equivariant retractions without changing any source product. Without that step the given H-data define no G-action on a row set.

## 7. Existing calibration and exact scope (the E5 identification is a PRE-receipt lead)

With H=G a two-element group, J a two-element set swapped by the nontrivial element, I=J ⊔ {one extra row} and two retractions sending the extra row to the two different points of J, E(S) is the frozen positive E5 band of old Part3 §27 (upper right zero, lower left zero, the two upper elements sending the extra row to different lower rows and fixing the other two). This member is noncryptic, has |Lambda|=2 and differing retractions. It is a structural identification with an already-frozen source example, not a parameter trial; no conclusion is selected from an instance.

**Scope.** Theorem P is a proper ORIGINAL-class positive family theorem. It does NOT prove the unrestricted original embedding; does not cover non-completely-regular sources, sources whose idempotent band has other shapes, or arbitrary supplied CS actors with nontrivial Rees structure; and does not touch the arbitrary-infinite pure-CS existence prerequisite. It is not an obstruction of any kind. Noncrypticity, non-inverse T and non-regular E(S) are all shown NOT to obstruct embedding, which sharpens the calibration of every invariant previously recorded, without promoting any of them to a sufficient condition.

## 8. Imports, prior art and assurance

Only ordinary group actions, induced G-sets (G×_H X), left/right zero and rectangular semigroup structure, Green H-classes of completely regular semigroups and the definitions in the supported manuscripts are used; every model-specific identity is verified above. No LI2003, LG, CG/RU-LU, inverse-section existence, band globalization or amalgamation theorem is used. Induced actions and E-unitary orthodox semigroup theory are classical; no novelty, priority or publication claim is made. The family's relation to the published 1987 regular-band theorem and the 1998 nonembeddable example is recorded only at the bounded source boundaries already in the dossier; no unread proof is imported.

All mathematics is exact WRITTEN symbolic algebra over ARBITRARY data; no chosen numeric parameter instance or probe, scientific interpreter/calculator/eval/program/CAS, enumeration/table/checker, solver/replay, build/test, CLI, nested agent or new GO. No frozen/shared file edited. A fresh complete source/dependency/application gate is required before any parent promotion; it must carry the provenance classes of Section0 and the v42 finding. Same original18/HOLD/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38, actual <=30min substantive JSON cadence; no early final park. Original unrestricted acceptance remains **UNMET**.
