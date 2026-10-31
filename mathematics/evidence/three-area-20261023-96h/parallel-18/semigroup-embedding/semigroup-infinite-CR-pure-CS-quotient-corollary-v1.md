# Arbitrary completely regular original-class sources have a pure completely simple quotient

MathSemigroup-2, original math-4. Actual `/bin/date` BEFORE this body: **Mon Oct 26 10:30:14 PDT 2026**. AUTHOR-WRITTEN / UNREVIEWED / no novelty claim. Exact all-variable conventional proof under the post-v131 actualRETURN/wholeACK/Main-v64 prospective authority. All previous process, admission, exactness, read-order, intake and cadence findings remain permanent.

## 1. Exact result and relation to old work

**Theorem CQ.** Let S be ANY nonempty COMPLETELY REGULAR semigroup, finite OR infinite. Suppose it is weakly E-unitary in the literal book sense, and each local monoid eSe is orthodox. Then S has an ACTUAL idempotent-pure onto homomorphism q to a completely simple semigroup. Its least completely simple congruence xi exists and is idempotent-pure.

Local regular-band identities are NOT needed for CQ, so it applies in particular to every completely regular source of the original locally r-orthodox class, without a supplied-q assumption. This does NOT prove an embedding or remove the NONFULL local-group-image gap.

This is an explicit specialization of the cofinal-CS-ideal purity mechanism already written in `proof-v1.md`, Theorem C, NOT an independent compactness method or a claim to have newly proved the old Theorem X. The new point is that EVERY completely regular S automatically has the EXACT cofinal regular/CS-ideal cover required by C, even with infinitely many components and NO least component or global completely simple ideal. The earlier scope had not made that general CR application explicit.

The named baseline input X is the COMPLETE written coordinate theorem in `mathematics/regular-semigroup-embedding/hmz-lean-20261014/xi-purity.md`, SHA256 `c7696fff180e29e7bfbc1fe9ed2e0070b2afe6a675a86171df45facd12f5e318`: a regular locally orthodox source WITH an actual nonempty CS ideal has a CS onto map, pure when the source is weakly E-unitary. That ENTIRE234LF argument, including its hypothesis boundary, was actually re-read before writing this body. It retains its old written parent-audit boundary, NOT formal/kernel or novelty status. Theorem X is an operative imported theorem, not established from a filename.

The current `proof-v1.md` whole SHA256 is `c79017231ebe5162ef3804f8dacc039da4232e613e911fd39ea058ef30737f5b`; its actual Sections1/2/7 were read at LF7–29,31–67,177–195 before this application. For clarity the cover and complete ultraproduct argument needed here are given below, so no omitted source window is claimed read.

Additional named classical inputs: Clifford's decomposition of a completely regular semigroup as a semilattice of completely simple components; Rees representation; the ultrafilter lemma and ordinary choices of witnesses/coordinates. No finite local-finiteness assumption, scientific enumeration or hidden inverse-closure termination is used.

## 2. EVERY finite subset has the required actual regular cover

Write S=(Y;S_alpha) as its classical semilattice of completely simple components. For ANY nonempty finite F⊆S, let alpha_F be the meet in Y of the component labels of the elements of F, and set

`T_F=union_(beta≥alpha_F) S_beta`.

This is an ACTUAL subsemigroup of S: the meet of two labels both above alpha_F remains above alpha_F. It is completely regular because it contains WHOLE components, so the inverse in the maximal subgroup of every member remains inside. It contains EVERY element of F, not only chosen generators or idempotents. Its component S_(alpha_F) is a nonempty completely simple IDEAL of T_F: multiplication with any higher component stays in S_(alpha_F).

Weak E-unitarity passes to T_F because any equation e=fa=ag with idempotents inside T_F is the SAME witness equation in S. Each local monoid e T_F e is a regular subsemigroup of the orthodox eSe; products of its idempotents remain inside e T_F e and idempotent in S, hence it is orthodox. If S has the stronger original local regular-band property, that identity also passes to these local bands. Thus Theorem X applies to EVERY actual T_F, regardless of its cardinality, giving an onto pure

`q_F:T_F→C_F`, with C_F completely simple.

There is NO claim that T_F is finite. This is why CQ is not the old finite corollary or an unjustified assertion that ordinary local finiteness makes inverse closure stop. Also no least element of Y or completely simple ideal of all S has been assumed.

## 3. Explicit completely simple ultraproduct target

Let A be the set of all nonempty finite subsets of S. The tails

`A_E={F∈A:E⊆F}`

for finite nonempty E have the finite-intersection property: their intersection contains the union of the finitely many E. Extend their filter to an ultrafilter U. For each F choose the actual q_F above and a Rees representation

`C_F=M[G_F;I_F,Lambda_F;P_F]`.

The group ultraproduct G_* is product_U G_F. Let I_*=product_U I_F and Lambda_*=product_U Lambda_F, ordinary set ultraproducts, nonempty by the named choice principle. Define

`p_*([lambda_F],[i_F])=[p^F_(lambda_F,i_F)]∈G_*`.

This is well defined: equal row/column representatives agree on U-large sets, whose intersection is U-large. Put

`C_*=M[G_*;I_*,Lambda_*;P_*]`.

The underlying ultraproduct of the sets C_F is explicitly identified with C_* by

`[(i_F,g_F,lambda_F)] ↦ ([i_F],[g_F],[lambda_F])`.

It is a bijection, because equality of the three coordinate classes is equivalent to equality of the triples on the intersection of three U-large sets, and any three representative sequences combine to a sequence of triples. Coordinatewise multiplication gives exactly the displayed Rees multiplication with P_*. Therefore the target is an ACTUAL completely simple semigroup by Rees representation, not an unspecified limit whose simplicity is guessed.

## 4. The actual pure homomorphism

Choose any c_F∈C_F. For s∈S define the F-coordinate

`z_F(s)=q_F(s)` if s∈T_F, and `z_F(s)=c_F` otherwise,

and define q_*(s)=[z_F(s)]∈C_*. For every F containing s, s∈T_F, and such F form a U-large tail. For s,t arbitrary, every F containing both has s,t,st in T_F by closure. Hence on a U-large set

`z_F(st)=q_F(st)=q_F(s)q_F(t)=z_F(s)z_F(t)`.

Thus q_* is a homomorphism for EVERY source pair; no compatibility of the chosen q_F is needed.

If s is NOT idempotent, q_F(s) is NOT idempotent whenever F contains s, by purity of q_F and because T_F has the original source multiplication. Therefore z_F(s)^2≠z_F(s) on a U-large tail, so q_*(s)^2≠q_*(s). Conversely a homomorphism sends source idempotents to idempotents. This proves q_* is idempotent-pure on the ENTIRE S. Dummy coordinates are outside a U-large domain set and do not affect any multiplication/purity claim.

## 5. Restricting to an ACTUAL completely simple image

Let Q=q_*(S). It is completely regular, being the image of a union of groups. To prove it is COMPLETELY SIMPLE, rather than merely infer simplicity from an ambient product, use its classical CR component semilattice.

Take idempotents e,f in Q. Set x=efe and p=x^0, its group identity in Q. Since ex=x=xe, multiplying by x^-1 on the appropriate sides gives ep=p=pe. Thus p≤e as idempotents. But Q⊆C_*, whose idempotents are primitive; a comparison of its idempotents forces p=e. If e,f have CR component labels alpha,beta, p has label alpha∧beta, so alpha∧beta=alpha. Interchanging e,f gives alpha∧beta=beta. Hence alpha=beta. Every component has an idempotent, so Q has ONLY ONE completely simple component and is completely simple.

Restrict q_*'s codomain to Q, writing q:S→Q. It is onto by definition and remains idempotent-pure. This proves CQ's first conclusion with an actual constructed homomorphism/target, not just existence of a nonempty family of congruences.

For the least congruence statement, the set of all CS congruences on S is nonempty (it includes the universal one). Choose Rees coordinates for each quotient; their direct product is a CS semigroup with product group, product row/column sets and coordinatewise sandwich matrix. The diagonal homomorphism has kernel xi equal to their intersection. Its image is CR and lies in that CS product, so the preceding primitive-idempotent argument proves the image CS. Thus xi itself is a CS congruence and is the least one. Since xi⊆ker q, s xi e with e idempotent implies q(s)=q(e) idempotent, and purity makes s idempotent. Hence xi is pure. This is an existence/purity conclusion, NOT a faithful embedding conclusion.

## 5.1. Explicit positive embedding for EVERY cryptic original-class source, without a supplied q

**Corollary CCT.** If S also satisfies the ORIGINAL locally r-orthodox condition and is CRYPTIC (its actual Green H is a congruence), then S embeds in an allowed physical P(B,C), for arbitrary cardinality and WITHOUT a supplied-q or FULL-CS hypothesis.

This is the earlier cryptic trivial-action construction with CQ now furnishing its otherwise required pure quotient. It is not a new independent method. Here is its complete application proof, so no unprovided old CT proof or currently live review verdict is an input.

Use the actual pure onto q:S→C from CQ and put B=S/H. It is an actual band: H is a congruence by the cryptic hypothesis, and s,s² are in the same maximal subgroup for every s. For b∈B choose an actual source idempotent e with [e]=b. The WHOLE local band bBb is the image of K_e=E(eSe): for any b[s]b, put x=ese and f=x^0. Since ex=x=xe, multiplication by the group inverse of x gives ef=f=fe, so f∈K_e and [f]=[x]=b[s]b. Hence K_e maps ONTO bBb. This map is a band homomorphism, and the original regular-band identity passes to bBb. Thus B∈V.

Give B the TRIVIAL G action and define

`J(s)=([s]_H,q(s))∈P(B,C)=B×C`.

Every product is correct because both coordinates are homomorphisms. If J(s)=J(t), then s,t lie in the SAME maximal subgroup H_e and have equal q-images. The group element st^-1 maps to the idempotent q(e); purity makes it the sole idempotent e of H_e, so s=t. This proves the displayed map injective on the ENTIRE S, not only on source idempotents or a selected component. The actual host is of the required type: B∈V, C is completely simple, and the action is trivial; its regularity, pure projection and local-orthodoxy/weak-E properties also follow directly from the ordinary direct product (local idempotents at (b,c) are (bBb)×{c}).

No FULL-CS is asserted for q; this corollary can cover nonfull cryptic sources. It does NOT cover noncryptic CR sources, and does not promote nonfullness into a nonembedding invariant. The new PR construction would additionally transfer this ACTUAL host to the frozen restricted-R reading, but that later two-body host-transfer theorem retains its own separate unreviewed gate.

This subsection is a pre-first-SHA-pin extension of this new CQ manuscript, not an edit to an already pinned/reviewed source. No invented first-version hash, earlier reader census or retrospective adoption is claimed.

## 6. Exact new scope and remaining original gaps

CQ removes supplied-pure-q existence as a prerequisite for ALL COMPLETELY REGULAR original-class sources, of arbitrary cardinality, using the named Theorem X and ultrafilter/Clifford/Rees imports. It does NOT derive FULL-CS for the resulting quotient: upper source groups can map to proper local C subgroups, precisely the remaining CR host-completion problem. It does NOT prove that an arbitrary non-CR source has this cover or a pure quotient.

The candidate FC lemma says FULL-CS under a supplied pure q forces CR. Together with CQ this clarifies the split: the NEW full-image host theorem is one proper region; every CR source now has the pure quotient, but the arbitrary NONFULL-image CR embedding is still open; for genuinely non-CR infinite sources pure-quotient existence can remain an additional gap. No nonembedding invariant follows from nonfullness or from failure of a proposed cover.

The new host-transfer PR/RP pair relates the TWO fixed product readings, not their unresolved source embedding. NONE of CQ, PR/RP or the canonical-full-ideal body is silently inserted into live v133's F/F2/FC freeze. Each later application/union needs its own complete mathematical and dependency/trust gate; no author consequence auto-adopts its named inputs.

Original unrestricted embedding/obstruction acceptance remains UNMET. No finite-witness execution, novelty/status, formal/kernel, human or configured-family certification is supplied. The CQ corollary is not counted as an independent discovery from its old compactness mechanism or old Theorem X.

## 7. Assurance

All new proof steps are conventional source-fixed all-variable exact WRITTEN algebra/set construction. No identity was machine-checked and no scientific interpreter/calculator/eval/program/CAS, chosen numerical/state/control/boundary/magnitude/decimal probe, enumeration/table/checker, solver/replay/build/test, external CLI, nested agent/GO or withdrawn-guidance reuse occurred. No frozen/shared edit or live reviewer-output reading. All own/author/parent process/exactness/read-order/intake/cadence/admission/mathwithdrawal findings and ZERO-credit history remain. Same18/exclusiveOWN/HOLD/sciencecutoff2026-10-27T11:05:38-07:00/deadline12:35:38/actual30minsubstantiveJSON/noearlypark or round closeout.
