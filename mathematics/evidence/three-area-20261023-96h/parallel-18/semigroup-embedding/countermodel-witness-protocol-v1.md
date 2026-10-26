# Finite nonembedding witness protocol — written preparation only

MathSemigroup, math-4. Actual clock immediately before creation: **2026-10-24T03:00:37-0700**.

**Permission and status:** parent authorizes ONE bounded WRITTEN witness-protocol preparation and source-status note. This document is that preparation, not code, a search launch, an admission request that grants itself permission, or a new target. **No countermodel exists in this packet. No source program/checker is generated or executed.** Scientific execution, enumeration, compilation/tests, imports of scientific code, CLI, nested agents, old runtime/GO reuse and native retries remain unauthorized/HOLD. The original October27 deadline is unchanged; parked intervals are not continuous work.

## 1. Original target, exact products and finite/infinite scope

The book Question1 asks whether EVERY nonempty regular semigroup S that is weakly E-unitary and locally r-orthodox embeds into the specified product of a seminormal band by a completely simple semigroup. S is not restricted to finite objects. The book pp66–67 definitions are statement authority; it does not itself define that product. Preserve the dossier's two fixed readings:

**P — Pastijn product.** Let C=M[G;I,Lambda;P] with nonempty I,Lambda, group G, all sandwich entries p_(lambda,i) in G and multiplication

    (i,g,lambda)(j,h,mu)=(i,g p_(lambda,j) h,mu).

Let G act on a band B by actual automorphisms alpha_g, alpha_g alpha_h=alpha_(gh), alpha_1=id. Then B odot C has ALL pairs(b,(i,g,lambda)) and multiplication

    (b,(i,g,lambda))(d,(j,h,mu))
      =(b alpha_(g p_(lambda,j))(d),(i,g p_(lambda,j)h,mu)).

The sandwich entry acts on the band as well as in the Rees group coordinate. It must not be omitted or replaced by an ordinary semidirect product action.

**R — restricted product, completely-simple specialization.** Let C act on B by endomorphisms phi_x with phi_(xy)=phi_x phi_y. Its carrier is

    {(b,x): phi_(xx')(b)=b for some/every x' in V_C(x)}.

On that actual carrier multiplication is

    (b,x)(d,y)=(b phi_x(d),xy).

The restricted carrier is not all B×C in general. For completely simple C the condition may equivalently use its H-class group inverse x^#, but that does not delete the fixed-point requirement.

In either reading B must be **locally regular**: every bBb is a regular band, whose identity is xyxzx=xyzx. This is the book's seminormal-band condition, not global regular-band identity, normality, or an assumed band identity element.

An embedding is an INJECTIVE multiplicative map, not an idempotent-separating homomorphic image or a reformulation carrying an unproved faithful-functor premise. Problem2's image construction is not the target.

This protocol seeks one FINITE orthodox source countermodel. That is a stronger source-class restriction for a NEGATIVE witness, not a silent narrowing of the universal target. A qualifying finite example would refute the universal P/R assertion, including its finite subcase. Failure to obtain such an example says nothing about all finite sources or the remaining infinite sources.

## 2. Literal source requirements on any candidate

A prospective certificate supplies a declared N>=1, carrier S={0,...,N-1}, and the COMPLETE N×N multiplication table. No entry may be inferred from symmetry, relabelling, padding, a solver term or an omitted block. Products are exact table indices.

Define

    E={e: e e=e},
    V(a)={x: a x a=a and x a x=x},
    u<=v iff u=f v=v g for some f,g in E.

The source must satisfy, at the literal table level:

1. **Associativity:** (xy)z=x(yz) for EVERY x,y,z in S.
2. **Regularity:** V(a) is nonempty for EVERY a in S.
3. **Weak E-unitarity:** for EVERY e,f,g in E and a in S, if e=f a=a g, then a is idempotent. This is the exact book natural-order witness, not a one-sided inequality chosen for convenience.
4. **Local r-orthodoxy:** for EVERY e in E, the actual local carrier eSe={e x e:x in S} is regular; its idempotents form a subsemigroup; and those local idempotents obey u v u w u=u v w u. Local membership means actual e u=u=u e, not merely that u was produced by an auxiliary generator.
5. **Global orthodoxy, specific to this countermodel route:** E E is contained in E. This allows the orthodox reduction in §4; nonorthodox sources cannot be passed through that argument without their own necessary-condition proof.
6. **E-unitarity, matching the primary necessary theorem:** e,ea in E implies a in E, and likewise e,ae in E implies a in E. It follows from the book weak condition in an orthodox regular source by the existing written reduction, but future table checking should also verify this directly rather than trust that an encoding implemented the reduction correctly.

The redundant direct source checks are deliberate proof-boundary protections, not new hypotheses substituted for the book target. A finite certificate must display its full idempotent set, and optionally one mutual inverse for each element to aid written inspection; checking cannot trust those lists without recomputing the defining products.

No source identity element, complete regularity, specified D-class count, real/linear representation, or upper bound on a host group is assumed.

## 3. Primary necessary nonembedding criterion — N1/N2 with N3 violation

The actual accessible author thesis is Hartmann, *Ortodox félcsoportok és szemidirekt szorzatok* (University of Szeged,2007), **Theorem3.4[Bi], printed p18/PDFp20**. Its full displayed mathematical statement was read in the retained primary PDF, not only in a status ledger. Its definition of 'embeddable' is embedding in a semidirect product of an arbitrary band by a group, given in the same thesis preliminaries. The theorem is also corroborated by the exact retained2005 primary-tool excerpt, Theorem6. See the separate source-status note for pins/access limits.

In normalized notation the necessary theorem says: if S is an embeddable E-unitary regular semigroup and elements a,a',b,b',e,f,g satisfy

**N1:** a sigma b, a' in V(a), b' in V(b), and e,f,g in E(S), where sigma is the LEAST group congruence;

**N2:**

    e a a'=e,              e b b'=e,
    a' a f g=f g,
    b' b f a' e a f g=f a' e a f g;

then

**N3:**

    e a f g=e b f a' e a f g.

All products are associative source products, with their displayed order preserved. No commutativity of group labels is allowed. The theorem imposes NO pairwise distinctness among e,f,g and NO four-distinct-odd convention among a,b,a',b'. Those were historical search restrictions, not the mathematical criterion.

A prospective witness must therefore provide a tuple(a,a',b,b',e,f,g) for which ALL N1–N2 hold and the two N3 products are DISTINCT table elements. The inequality is the nonembedding obstruction; it is not an idempotent-purity failure, a failed completion recipe, or an incomplete canonical derivation.

### Independently checkable sigma evidence

'Equal under one chosen group map' does NOT prove a sigma b. Accept one of these exact sufficient certificates:

- **Idempotent bridge:** after verifying a' in V(a), check a'b is idempotent. Every homomorphism gamma into ANY group sends a'a and a'b to1, hence gamma(a')=gamma(a)^(-1) and gamma(a')gamma(b)=1; therefore gamma(a)=gamma(b). This proves a sigma b without assuming a supplied grading is the maximum group quotient.
- **Elementary group-kernel chain:** provide a finite chain from a to b where each jump replaces an idempotent p by another idempotent q inside literal left/right contexts: x=ell p r, y=ell q r, with ell/r either table elements or omitted factors. Every group homomorphism sends p,q to1 and hence equates x,y. Verify every jump from the table. A zero-length chain is allowed when a=b. This proves membership in every group congruence directly; no quotient classifier is trusted.

Other purported sigma evidence is not silently accepted. It would need a separate written soundness proof before being used in a witness. These are certificate mechanisms, not a claim that one fixed presentation exhausts possible witnesses.

An optional pure Z2 helper labelling can make a'b idempotent automatic when a,b,a',b' lie in the odd class and the even class is exactly E. If used, EVERY grading equation must be checked. The main admissibility requirements and the raw sigma proof still remain; equal helper grades alone are never accepted. The protocol does not require that helper or an idempotent-prefix convention.

## 4. Why this criterion rules out BOTH fixed P/R targets

The source theorem alone rules out any band-by-GROUP embedding. The needed bridge to the book targets is the orthodox reduction, whose complete coordinate proof was actually read in the dossier `proof.md` §3. Its scope must remain explicit; it is not being applied to a nonorthodox table.

Here is the mathematical chain, including the injectivity/action point.

Suppose the finite orthodox source S embedded in either product with band B and completely simple C. Its projection image T in C is regular. Every idempotent of finite T lifts to an idempotent of S: if pi(s)=t=t^2, take an idempotent power s^omega. Global orthodoxy of S then makes T orthodox. On the occupied rows I' and columns Lambda', every crossed H-class idempotent occurs, and closure of their products forces

    p_(lambda,i)=u_lambda v_i.

Thus the occupied rectangular hull D is a rectangular group after the coordinate change(i,g,lambda)→(i,v_i g u_lambda,lambda).

For **P**, let R=I'×Lambda' be the rectangular band. The explicit map

    (b,(i,g,lambda))
       |--> ((alpha_(v_i)(b),(i,lambda)), v_i g u_lambda)

embeds the relevant P hull in(B×R)⋊G. Multiplicativity uses u_lambda v_j=p_(lambda,j), and injectivity uses the automorphism alpha_(v_i) plus the retained row/column and group coordinates. This is not a projection asserted faithful without proof.

For **R**, transport the action to the rectangular-group coordinates. The restricted carrier over row i is B_i=Fix phi_(i,1,mu), independent of mu. Fix e0=(i0,1,lambda0). The restrictions phi_(i0,g,lambda0) give an actual automorphism action of G on B_i0. The map

    (b,(i,g,lambda))
       |--> ((phi_e0(b),(i,lambda)),g)

is multiplicative and injective: phi_(i,1,lambda0) phi_e0 recovers b on B_i. It lands in(B_i0×R)⋊G. The original restricted-carrier condition was used, not discarded.

If B is locally regular, so are its subbands and products with R; in fact the N3 source theorem rules out embeddings into band⋊G with ANY band, so this extra band preservation only strengthens the reduction. Both target embeddings would contradict a genuine N3 violation. Therefore a table meeting §§2–3 is a valid finite negative witness for BOTH adopted P/R readings.

This reduction and the classical N3 theorem are named written/import boundaries, not Lean/kernel acceptance. Original Billhardt1998's proof was not recovered in this preparation; the full necessary statement is nevertheless available in the actually read author thesis. A future acceptance must explicitly retain that source-theorem import rather than call it a new source-free proof.

**Finite purity is NOT the obstruction:** existing TheoremX already makes the least completely simple congruence pure for every finite book-class member. A qualifying N3 countermodel would still be subject to that baseline. The protocol has NO xi-nonpurity objective, premise or acceptance flag. Conversely purity, N3 equality, a solver timeout or lack of a found witness proves no embedding theorem.

## 5. Required finite witness record, with no code or search specified

A future proposed certificate must contain, in one frozen record:

- declared N and complete exact integer table with ordered row/column labels0,...,N-1;
- the actual idempotent list and the designated tuple;
- actual mutual inverse evidence, local-corner membership/identities and weak/E-unitarity witnesses or complete table checks;
- one sound sigma certificate from §3 and its literal products/contexts;
- the four N2 left/right values and the DISTINCT N3 left/right values;
- optional helper grading, labelled as a helper and checked on every ordered pair, never a substitute for sigma;
- exact bytes/hash, provenance, creation clock and claim scope. No 'SAT therefore valid' assertion replaces the table-level mathematics.

Missing rows/columns, duplicate labels, out-of-range integers, a changed declared size, malformed tuple or unsupported sigma assertion must stop validation. No implicit modular reduction or carrier padding is allowed.

The prospective direct-check order is parsing/ranges, associativity, actual E, regularity, global orthodoxy, weak E-unitarity, strong E-unitarity, literal local r-orthodoxy, tuple/inverse/sigma evidence, all N2 identities, and finally the STRICT N3 inequality. Future checks must use explicit invariant-specific failures, not assertions that disappear under optimization, broad exception swallowing or a printed success string detached from exit status. This paragraph specifies mathematical acceptance behavior; **no checker source is generated here**.

N is an arbitrary DECLARED finite carrier size for certificate validity. This document grants no carrier enumeration, size grid, solver timeout, run budget or execution permission. Any future search is a separately scoped parent decision with new source/input pins, controls, resources, settlement and exact GO.

## 6. Intended mathematical controls — defined here, NOT exercised

These controls distinguish source admissibility, the necessary criterion and the sigma interface. There is currently **no known full qualifying nonembedding table in this packet**, so none of the positive controls is falsely described as a counterexample.

### P1 — embedded group, all N premises but N3 equality

Use C2={1,h}, h^2=1, with its ordinary complete group table and tuple

    a=b=a'=b'=h, e=f=g=1.

Regularity, all source hypotheses, sigma(a)=sigma(b), N1 and every N2 hold. Both N3 products equal h. Expected result: source/tuple checks PASS, then **NO-N3-VIOLATION**. This is an intended full-premise rejection of a NONwitness, not a generic earlier failure. C2 embeds with one-element band and group C2.

### P2 — locally regular but NOT globally regular band

Use the actual E5 table:

| product |0|1|2|3|4|
|---|---:|---:|---:|---:|---:|
|0|0|1|4|3|4|
|1|0|1|3|3|4|
|2|2|2|2|2|2|
|3|3|3|3|3|3|
|4|4|4|4|4|4|

It is a band: upper{0,1} is right zero and lower{2,3,4} is a left-zero ideal; the two upper actions on the ideal fix3,4, send2 to4 or3, and satisfy theta_u theta_v=theta_v. This verifies associativity structurally. For k in the lower ideal, kE5k={k}; for u=0,1, uE5u={u,3,4}, identity u over a left-zero ideal, a regular band. Thus source admissibility must PASS. It is not a GLOBAL regular band because0·1·0·2·0=4 but0·1·2·0=3. An acceptance rule demanding global regularity would wrongly reject a valid book-class source. It already embeds as E5⋊{1}. The all-zero designated tuple is a legal coincident-variable premise control and has N3 equality, hence remains a NONwitness.

### N1 — same chosen helper image does not prove least-group congruence

In the SAME group C2 take

    a=a'=1, b=b'=h, e=f=g=1.

Every inverse and N2 condition holds, and the N3 products are1 and h, DISTINCT. Yet a sigma b is FALSE: the identity homomorphism to C2 separates them, a'b=h is not idempotent, and no valid idempotent-context chain can connect them. Even the trivial helper homomorphism equates a,b, demonstrating why that is not a sigma certificate. Expected rejection: **SIGMA-CERTIFICATE-INVALID**, not a false nonembedding result for an embedded group.

### N2 — omitted weak E-unitarity

Use C2 with an absorbing zero adjoined. It is inverse/regular, orthodox, and all local idempotent bands are semilattices. But0<=h using0 as both idempotent multipliers while h is not idempotent. Expected rejection: **WEAK-E-UNITARITY**, before considering any nonembedding tuple. It is not a book-class countermodel.

### N3 — omitted local regular-band hypothesis

Adjoin a new identity5 to the valid band E5. This remains an associative band, so regularity/orthodoxy/weak and strong E-unitarity hold. At e=5 the local monoid is the whole source; the products4 versus3 above violate the required regular-band identity. Expected rejection: **LOCAL-REGULAR-BAND**. No inference about the original target follows from this out-of-class source.

### N4 — associativity is an actual table condition

The table with rows[0,0,0],[1,1,1],[2,0,2] is idempotent on every diagonal and has valid range labels, but

    (2·2)·1=0, whereas2·(2·1)=2.

Expected rejection: **ASSOCIATIVITY**, with this concrete triple. It is not a semigroup, regardless of any later grading or theorem predicate.

### N5 — regularity cannot be inferred from an idempotent list

Use the associative two-element nilpotent semigroup{0,z}, with0 absorbing and z^2=0. No t satisfies ztz=z. Expected first mathematical rejection after associativity: **REGULARITY**. Other later hypotheses may fail too, but do not count an unrelated exception as this intended rejection.

### N6 — exact tuple, inverse and N2 guards

In C2, assigning a=h but a'=1 fails aa'a=a because h·1·h=1, not h; expected **DESIGNATED-INVERSE**. In valid E5, take a=b=a'=b'=e=0, f=2, g=0. Inverse and sigma-by-equality checks pass, eaa'=ebb'=e, but a'afg=4 differs from fg=2; expected **N2-a'afg**. These controls are intended to distinguish a premise failure from the final N3 inequality.

Future parser/range controls additionally remove a row, duplicate a label, change N, replace a product by N, and alter a sigma-chain context. Each needs its intended explicit rejection reason under a separately authorized checker run. NONE has been executed by this written preparation.

## 7. Verification/acceptance gates, with no implicit permission

If a genuine qualifying finite table is later supplied, freeze its bytes first. Parent and actual separate reconstructions must verify the full table from the literal definitions, not import a producer's helper or trust its solver status. The finite-witness discipline calls for three genuinely distinct checks and intended-reason mutations/reproduction as applicable; this does NOT authorize nested agents or external-model CLI under the current contract. Parent must arrange any permitted in-harness checks and separately admit every scientific executable. No such check is performed now.

No positive full-witness control can be fabricated before a qualifying table exists. 'Source admissibility passes' for C2/E5 is a narrower positive control, while their final N3-equality rejection is the correct full-certificate behavior. No solver UNSAT/UNKNOWN, finite range, old certificate portfolio or purity statement can substitute for an actual countermodel.

Correctness relative to the primary N3 theorem and the fully read P/R reduction, original-book scope, source trust, finite verification, formal assurance, novelty and significance must remain separate. A valid table would have a consequential negative theorem; preparation, an encoding or a failed recipe has none of that status. No publication, contact, Git mutation, credential/config change or old-runtime repair is authorized.

**Deliverable status:** WRITTEN_PROTOCOL_COMPLETE; EXACT_N3_INTERFACE_AVAILABLE; ACTUAL_ADMISSIBLE_COUNTERMODEL_NOT_FOUND; CODE_NOT_GENERATED; EXECUTION_NOT_PERFORMED. The same semigroup primary is retained, with the old all-contextual coherence result still unresolved. No second target, search grid or native launch is introduced.
