# Total over-actor separating families: an exact product lemma, not an asserted family

MathSemigroup-2, original math-4. Actual `/bin/date` before this body: **Mon Oct 26 09:23:43 PDT 2026**. AUTHOR-WRITTEN / UNREVIEWED; no novelty claim. This body follows the parent's explicit future-only direction v56, SHA-256 `249d62954bf564ed8fc89674108d1942793a38d92a5e5d20045fff88e8165e45`, actually read completely before writing. The existing whole-state finding was sufficient under that direction; no new ACK loop or retrospective primary permission is claimed. The distinct cadence finding `5ad3763852cc691b4a485323576cb7544477de862cdc57adef396e41e6b88ef7` and every earlier finding remain permanent.

## 1. Exact statement for the physical P product

Fix a nonempty semigroup S, a completely simple semigroup C=M[G;I,Lambda;P], and a homomorphism q:S→C. Let A be a nonempty index set. For each a∈A suppose an ACTUAL band B_a and ACTUAL action alpha^a:G→Aut(B_a) are supplied, and an ACTUAL TOTAL homomorphism

`j_a:S→P(B_a,C),   j_a(s)=(b_a(s),q(s))`

is supplied. Every map has the SAME entire domain S and the SAME second-coordinate map q; charts on different subsemigroups are not such data. Suppose also each B_a has regular local corners. No injectivity of an individual j_a is required.

Set B=product_(a∈A) B_a, with coordinatewise product and diagonal action alpha_g((d_a)_a)=(alpha^a_g(d_a))_a. This product is nonempty without selecting arbitrary unrelated elements: fix s_*∈S and use (b_a(s_*))_a. Then

`J:S→P(B,C),   J(s)=((b_a(s))_a,q(s))`

is a total homomorphism, B has regular local corners, and

`ker J = intersection_(a∈A) ker j_a.`  (SP)

Consequently J is an embedding IF AND ONLY IF the SUPPLIED family jointly separates every distinct pair in S. This is an implication, not an existence theorem for such a family.

*Proof.* B is a band, every alpha_g is an automorphism with inverse alpha_(g^-1), and the action law holds in every coordinate. The corner at d=(d_a)_a is exactly product_a(d_a B_a d_a): one inclusion is immediate; the other follows directly by choosing for each corner element its already displayed middle-coordinate preimage, or from the ordinary choice principle for an arbitrary product. Equivalently, to avoid that last equality or choice entirely, the corner is a SUBBAND of product_a(d_a B_a d_a), which is sufficient. The regular-band identity xyxzx=xyzx holds coordinatewise in that product, hence in the corner. Thus B lies in the required band variety V.

For q(s)=(i,g,lambda) and q(t)=(j,h,mu), the a-coordinate of the first component of J(s)J(t) is

`b_a(s) alpha^a_(g p_(lambda,j))(b_a(t)) = b_a(st)`,

because j_a is multiplicative. The C-coordinate is q(st), so J is multiplicative for EVERY s,t, not only products inside a chart or component. Equality J(s)=J(t) is exactly q(s)=q(t) and b_a(s)=b_a(t) for every a. Since A is nonempty and every j_a has second coordinate q, this is exactly equality j_a(s)=j_a(t) for every a. This proves (SP) and the embedding equivalence. ∎

The same proof applies to W_L or W_R instead of V, because the relevant local-corner identity is again preserved by products and subbands. If A and all B_a and C are finite, the displayed target is finite; this conditional finiteness observation supplies no finite inputs or witnesses.

## 2. Congruence version and application criterion

Suppose actual congruences rho_a⊆ker q are supplied. Let pi_a:S→S/rho_a be the quotient maps and q_a:S/rho_a→C be induced by q. Suppose actual injective maps

`k_a:S/rho_a→P(B_a,C),  second-coordinate(k_a)=q_a`

are supplied with B_a∈V. Set j_a=k_a pi_a. Then ker j_a=rho_a, so Section 1 embeds S over q whenever intersection_a rho_a=Delta_S.

This identifies the exact NEW route obligation for the multilayer orthogroup frontier: construct such congruences whose quotients really fall within an established host theorem, VERIFY that those quotients and their induced maps meet every hypothesis, and prove that the congruences intersect trivially. No congruence-merging, two-layer quotient, retract, point-separating family or compatible host is assumed to exist. Existing one-sided quotient/spine composition is the two-factor special case, not a proof that arbitrary further decompositions exist.

For G a group, q=sigma and C=G, the formula specializes to ordinary semidirect products. The five prior unreviewed CT/MG/P/Q/T2 manuscripts may only be used as named candidate inputs with their hypotheses retained; this lemma does not adopt them or supply the missing congruences for them.

## 3. Restricted-action R reading

For the frozen R reading, replace the actions alpha^a by supplied endomorphism actions of the SAME C and define their coordinatewise product action. An element ((d_a)_a,x) satisfies the carrier condition alpha_(xx')((d_a)_a)=(d_a)_a exactly when each coordinate satisfies alpha^a_(xx')(d_a)=d_a, for the SAME x and inverse x'. Thus every J(s) is in the required carrier when every j_a(s) is. Multiplication and (SP) are coordinatewise exactly as above. Hence the same conditional separating-family implication holds for this reading too. No equivalence between the two readings is asserted here.

## 4. Imports, residual and assurance

Imports: only ordinary semigroup homomorphism/congruence facts and the frozen definitions of P and R in selection-v1.md Sections 1–2. All new product identities are proved above. Target-class preservation for the physical host is the existing source theorem, not newly certified by this product lemma; the directly proved band/action assertions are precisely what its hypotheses require. No scientific interpreter, calculator, numeric/state/control/magnitude/decimal probe, CAS, enumeration, table/checker, solver/replay, build/test, external CLI, nested agent or new GO. All-variable written proof only; no withdrawn-guidance reuse. No frozen/shared source edited.

Original full embedding/nonembedding acceptance remains UNMET. In particular, no actual separating family for the non-FULL multilayer orthogroup frontier is supplied here; nor any full mixed-relation/idempotent-fibre separation proof, all-host obstruction or arbitrary-infinite pure-CS existence theorem. Same original eighteen owners, scientific HOLD, science cutoff 2026-10-27T11:05:38-07:00, deadline 2026-10-27T12:35:38-07:00 and prospective thirty-minute substantive JSON cadence. This is not an early final park or round closeout.
